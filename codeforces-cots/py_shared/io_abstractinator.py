from io import BytesIO, StringIO
import re
from typing import Literal

from loguru import logger
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Tree, Node, Query

py_language = Language(tspython.language())
py_parser = Parser(py_language)


newlines_rx = re.compile(r'(\n+(?!$)|^(?=\w))')

_sig_calls_query_str = """
[
  (
    (identifier) @call_ident
    (#any-of? @call_ident "input" "print" "exit")
  )
  (
    (identifier) @stream_ident
    (#any-of? @stream_ident "stdin" "stdout")
  )
]
"""
_sig_calls_q: Query = py_language.query(_sig_calls_query_str)

_main_boilerplate_query_str = """
(if_statement
  condition: (comparison_operator
    (identifier) @name
    "=="
    (string) @main
    (#match? @name "^__name__$")
    (#any-of? @main "'__main__'" "\\"__main__\\"")
  )
  consequence: (block
    (expression_statement
      (call
        function: (identifier) @main_fn
        arguments: (argument_list) @main_args
  )))
) @main_if
"""
_main_boilerplate_q = py_language.query(_main_boilerplate_query_str)


def _virtualize(
    root_nodes: list[Node],
    src_bytes: bytes,
) -> str:
    """
    "Virtualizes" code in the nodes:
    - replaces stdin/stdout with input_stream/output_stream
    - replaces exit() with return

    IMPORTANT: assumes root_nodes are consecutive.
    """
    global _ctx
    # We need to sort matches as tree-sitter doesn't guarantee order (according to Gemini).
    first_input_assignment = None
    processed_matches: list[tuple[
        int, # start_byte
        int, # end_byte
        Literal['call', 'ref'], # type of the matching pattern
        dict[str, Node], # processed captures
    ]] = []
    for _, captures in (
        m
        for node in root_nodes
        for m in _sig_calls_q.matches(node)
    ):
        # NOTE first arg may be the "pattern index" and it seems to always be 0
        # captures = {}
        # # Convert list of (name, node) tuples to a dictionary {name: [nodes]}
        # for name_str, node_obj in captures_list:
        #     capture_name = py_language.capture_name_for_id(name_str)
        #     if capture_name not in captures:
        #         captures[capture_name] = []
        #     captures[capture_name].append(node_obj)

        # Determine the primary node (call or attribute) for position sorting
        pattern_tp = None
        node = None
        processed_captures = None
        if 'call_ident' in captures:
            ident_n = captures['call_ident'][0]
            parent = ident_n.parent
            parent_tp = parent.type

            if parent_tp == 'call':
                pattern_tp = 'call'
                node = parent
                processed_captures = {
                    'call': node,
                    'func': ident_n,
                    'args': parent.child_by_field_name('arguments'),
                }
            elif parent_tp == 'assignment' and parent.child(0) == ident_n:
                if ident_n.text in (b'print', b'exit'):
                    logger.error('Code assigns to `{}`!!! (ctx={})', ident_n.text.decode(), _ctx)
                    continue

                if not first_input_assignment:
                    logger.debug('Found assignment to `input` (ctx={})', _ctx)
                    first_input_assignment = parent
                    continue
            else:
                continue
        elif 'stream_ident' in captures:
            pattern_tp = 'ref'
            ident = captures['stream_ident'][0]
            parent = ident.parent
            parent_tp = parent.type
            if parent_tp in ('dotted_name', 'import_from_statement'):
                continue

            if (
                parent_tp == 'assignment' and
                parent.child(0) == ident
            ):
                logger.warning(
                    'Symbol to be replaced is being assigned to: sym=`{}`, ctx={}',
                    ident.text.decode(),
                    _ctx,
                )
                continue

            node_for_replacement = ident
            if (
                parent_tp == 'attribute' and
                parent.child(0).text == b'sys' and
                parent.child(2) == ident
            ):
                node_for_replacement = parent

            node = node_for_replacement
            processed_captures = {
                'node_for_replacement': node,
                'ident': ident,
            }
        else:
            raise ValueError(f'Unexpected match: {captures!r}')

        assert node is not None, f'{captures=!r}'
        assert processed_captures is not None, f'{captures=!r}'
        processed_matches.append((node.start_byte, node.end_byte, pattern_tp, processed_captures))

    # Sort matches by their start byte
    processed_matches.sort(key=lambda x: x[0])

    out_buf = StringIO()
    current_pos = root_nodes[0].start_byte
    limit = root_nodes[-1].end_byte
    input_overridde_offset = limit
    if first_input_assignment:
        input_overridde_offset = first_input_assignment.end_byte

    for start_byte, end_byte, pattern_tp, processed_captures in processed_matches:
        out_buf.write(src_bytes[current_pos:start_byte].decode())

        if pattern_tp == 'call':
            func = processed_captures['func']
            args = processed_captures['args']
            func_text = func.text
            if func_text == b'input':
                if start_byte < input_overridde_offset:
                    out_buf.write('input_stream.readline().rstrip("\\n")')
                else:
                    out_buf.write(src_bytes[start_byte:end_byte].decode())
            elif func_text == b'print':
                # Reconstruct print call adding file=output_stream
                # Write the call up to the end of arguments, excluding the closing ')'
                out_buf.write(src_bytes[start_byte : end_byte - 1].decode())
                # args node includes '(' and ')' in its children
                if len(args.children) > 2:
                    out_buf.write(', ')
                out_buf.write('file=output_stream)')
            elif func_text == b'exit':
                # this doesn't work when exit is in a function
                # perhaps raising an exception would be better
                # TODO at least warn if exit is found in a function
                out_buf.write('return')
            else:
                raise ValueError(f'Unexpected func: {func_text.decode()}')

        elif pattern_tp == 'ref':
            node_for_replacement = processed_captures['node_for_replacement']
            ident = processed_captures['ident']
            ident_text = ident.text
            if ident_text == b'stdin':
                out_buf.write('input_stream')
            elif ident_text == b'stdout':
                out_buf.write('output_stream')
            else:
                raise ValueError(f'Unexpected ident: {ident_text.decode()}')

        current_pos = end_byte

    out_buf.write(src_bytes[current_pos:limit].decode())
    return out_buf.getvalue()


def _extract_main_name_from_boilerplate(node) -> bytes | None:
    matches = _main_boilerplate_q.matches(node)
    # pairs = list(zip(captures['main_fn'], captures['main_args']))
    if not matches:
        return None
    if len(matches) > 1:
        # log unexpected code
        pass

    match_captures = matches[0][1]
    main_fn = match_captures['main_fn'][0]
    main_args = match_captures['main_args'][0]

    arg_child_num = main_args.child_count
    if arg_child_num < 2:
        # log unexpected node structure
        return None
    elif arg_child_num > 2:
        # log unexpected code
        pass

    return main_fn.text


type StatementKind = Literal['definition', 'instruction']
_SplitToplevelsNT = tuple[
    list[Node], # initial imports
    list[tuple[StatementKind, Node]], # other statements
]
def _split_toplevels(node) -> _SplitToplevelsNT:
    global _ctx
    if node.type != 'module':
        logger.warning('Unexpected node type `{}` (ctx={})', node.type, _ctx)

    import_node_types = [
        'import_statement',
        'import_from_statement',
        'future_import_statement',
    ]
    defn_node_types = [
        'function_definition',
        'decorated_definition',
        'class_definition',
        'type_alias_statement',
    ]

    initial_imports = []
    statements = []

    for child in node.children:
        tp = child.type
        if not statements and tp in import_node_types:
            # we only extract the initial imports to avoid reordering the nodes
            initial_imports.append(child)
        elif tp in defn_node_types:
            statements.append(('definition', child))
        else:
            statements.append(('instruction', child))

    return initial_imports, statements



def _is_def_main(node) -> bool:
    if node.type == 'decorated_definition':
        node = node.children[1]

    if node.type != 'function_definition':
        return False

    return node.child_by_field_name('name').text == b'main'


def _preprocess_program(
    tops: _SplitToplevelsNT,
) -> None | tuple[_SplitToplevelsNT, Literal['exprs']] | tuple[_SplitToplevelsNT, Literal['defs'], bytes]:
    global _ctx
    imports, stmts_with_kinds = tops
    main_name = None
    for kind, n in stmts_with_kinds:
        if kind != 'definition':
            continue
        if _is_def_main(n):
            main_name = b'main'
            break

    found_main_boilerplate = False
    instruction_count = 0
    new_stmts_with_kinds = []
    for kind, n in stmts_with_kinds:
        if kind != 'instruction':
            new_stmts_with_kinds.append((kind, n))
            continue

        instruction_count += 1
        extraction = _extract_main_name_from_boilerplate(n)
        if extraction is None:
            new_stmts_with_kinds.append((kind, n))
            continue

        if extraction:
            if found_main_boilerplate:
                logger.warning('Multiple main boilerplates found (ctx={})', _ctx)
                return None
            # do not add the boilerplate to the processed list
            found_main_boilerplate = True
            main_name = extraction

    # This is below debug level at this point.
    # if main_name and instruction_count > 1:
    #     logger.debug('Found a main with top-level instructions (ctx={})', ctx)

    if main_name:
        return ((imports, new_stmts_with_kinds), 'defs', main_name)
    else:
        return ((imports, new_stmts_with_kinds), 'exprs')


def _process_toplevels1(
    tops: _SplitToplevelsNT,
    src_bytes: bytes,
) -> str:
    imports, stmts_with_kinds = tops

    out_buf = StringIO()
    for n in imports:
        print(n.text.decode(), file=out_buf)

    if imports:
        print('\n', file=out_buf)
    print('def main(input_stream, output_stream):', file=out_buf)
    s = _virtualize([stmt for _, stmt in stmts_with_kinds], src_bytes)
    print(newlines_rx.sub(r'\g<0>    ', s), file=out_buf)

    return out_buf.getvalue()


def _process_toplevels2(
    tops: _SplitToplevelsNT,
    src_bytes: bytes,
    main_name: bytes,
) -> str:
    imports, stmts_with_kinds = tops

    out_buf = StringIO()
    for n in imports:
        print(n.text.decode(), file=out_buf)

    if imports:
        print('\n', file=out_buf)
    for kind, n in stmts_with_kinds:
        if kind != 'definition':
            print(n.text.decode(), file=out_buf)
            print('', file=out_buf)
            continue

        if n.type == 'decorated_definition':
            logger.warning('Untested code - decorated definition:\n{}', n.text.decode())
            children = n.children
            print(children[0].text.decode(), file=out_buf)
            n = children[1]

        if n.type != 'function_definition':
            print(n.text.decode(), file=out_buf)
            print('', file=out_buf)
            continue

        name_node = n.child_by_field_name('name')
        if name_node.text != main_name:
            print(n.text.decode(), file=out_buf)
            print('', file=out_buf)
            continue

        print('def ', main_name.decode(), '(input_stream, output_stream):', sep='', file=out_buf)
        print('    ', end='', file=out_buf)
        body_node = n.child_by_field_name('body')
        print(_virtualize([body_node], src_bytes), file=out_buf)

    return out_buf.getvalue()


# =================
# temporary
# =================
from pathlib import Path
import re


_py_indent_re = re.compile(rb'^ *')


# Used for logging; if needed can be done via contextvars or loguru binds
_ctx = None


def _remove_indent(code: bytes) -> bytes:
    # NOTE This should now be done when extracting code snippets.
    # TODO should we instead just warn on leading indents?
    out_buf = BytesIO()
    first_indent: bytes | None = None
    for line in code.splitlines():
        if first_indent is None:
            first_indent = _py_indent_re.match(line).group(0)
        out_buf.write(line.removeprefix(first_indent))
        out_buf.write(b'\n')
    return out_buf.getvalue()


def _process_toplevels(
    tops: _SplitToplevelsNT,
    src_bytes: bytes,
) -> str:
    # debug code
    # print('## imports')
    # for n in tops[0]:
    #     print(n.text.decode())
    # print('## defns')
    # for kind, n in tops[1]:
    #     print(f'# {kind=}')
    #     print(n.text.decode())

    prepro_res = _preprocess_program(tops)
    if prepro_res is None:
        logger.error('Unrecognized toplevel type (ctx={})', _ctx)
        return None
    prepro_tops = prepro_res[0]
    prepro_type = prepro_res[1]

    if prepro_type == 'exprs':
        res = _process_toplevels1(prepro_tops, src_bytes)
    elif prepro_type == 'defs':
        main_name = prepro_res[2]
        if main_name != b'main':
            # NOTE we could rename the def to `main`, but recursion is a problem, so we bail instead.
            logger.error('Unexpected main name (ctx={})', _ctx)
            return None
        res = _process_toplevels2(prepro_tops, src_bytes, main_name)
    else:
        raise ValueError(f'Unexpected: {prepro_type=!r}')

    return res


def process_file(file: str | Path):
    global _ctx
    _ctx = 'file'

    contents = _remove_indent(Path(file).read_bytes())
    tree = py_parser.parse(contents)
    if tree.root_node.has_error:
        # TODO only bail if the top node is ERROR?
        logger.error('Syntax error in file: {}', file)
        return None
    tops = _split_toplevels(tree.root_node)

    return _process_toplevels(tops, contents)


def process_string(in_: str, ctx_ = None):
    global _ctx
    _ctx = ctx_ or 'row'

    contents = _remove_indent(in_.encode())
    tree = py_parser.parse(contents)
    if tree.root_node.has_error:
        # TODO only bail if the top node is ERROR?
        logger.error('Syntax error in row: {}', _ctx)
        return None
    tops = _split_toplevels(tree.root_node)

    return _process_toplevels(tops, contents)


def go(file: str | Path):
    import warnings
    warnings.warn("The 'go' function is deprecated. Use 'process_file' instead.", DeprecationWarning, stacklevel=2)
    return process_file(file)


def go2(in_: str, ctx_ = None):
    import warnings
    warnings.warn("The 'go2' function is deprecated. Use 'process_string' instead.", DeprecationWarning, stacklevel=2)
    return process_string(in_, ctx_)


import os
if __name__ == '__main__' and 'NOGO' not in os.environ:
    import sys
    arg = sys.argv[1]
    print(go(arg))