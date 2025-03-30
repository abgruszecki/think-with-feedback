import ast
from collections import namedtuple
import json
from pathlib import Path
import re
from os import environ as env
import sys
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Tree

py_language = Language(tspython.language())
py_parser = Parser(py_language)
outd = Path('out/go+solutions_py')
outd.mkdir(parents=True, exist_ok=True)

offset_re = re.compile(r'^<think>\n?')
# par_sep_re = re.compile(r'\n\n+|\n?</think>\n*|[^\n]\n```(.*?)\n+', re.MULTILINE)
par_sep_re = re.compile(r'\n\n+|(\n?</think>\n*)', re.MULTILINE)
fence_start_re = re.compile(r'^```(.*)\n+', re.MULTILINE)
fence_end_re = re.compile(r'^```($|\n+)', re.MULTILINE)

CUR_ITEM_IDX=-1


if 'DEBUG' in env:
    def dbg(s: str):
        print(f'dbg: {s}', file=sys.stderr)
else:
    def dbg(s: str):
        pass


def check_is_python(
    s: str,
    old_tree: Tree | None = None,
) -> tuple[bool, Tree]:
    # reusing trees is not faster :(
    # if old_tree:
    #     r = old_tree.root_node
    #     # minimal edit to the tree to make it reusable
    #     old_tree.edit(
    #         start_byte=r.start_byte,
    #         old_end_byte=r.end_byte,
    #         new_end_byte=r.end_byte,
    #         start_point=r.start_point,
    #         old_end_point=r.end_point,
    #         new_end_point=r.end_point,
    #     )
    #     tree = py_parser.parse(s.encode(), old_tree)

    tree = py_parser.parse(s.encode())
    return not tree.root_node.has_error, tree


def clean_backtick_fences(string: str) -> str:
    # TODO use a regex
    string = string.removeprefix('```')
    string = string.removeprefix('python')
    string = string.removeprefix('\n')
    string = string.removesuffix('```')
    string = string.removesuffix('\n')
    return string


def find_think_code_blocks(
    response: str,
    offset: int = 0,
) -> tuple[list[str], int]:
    results = []

    cur_idx = offset
    cur_par_start = cur_idx
    cur_match = par_sep_re.search(response, cur_idx)
    last_par_was_code = False
    loop = True
    # next_match = None
    while loop:
        # start of match is cur par's end
        # end of match is next par's start
        if cur_match and cur_match.group(1) is None:
            dbg(f'cur_match: {cur_match.start()} / {cur_match.group(0)!r}')
            cur_par_end = cur_match.start()

            cur_idx = cur_match.end()
            cur_match = par_sep_re.search(response, cur_idx)

            # if cur_match and cur_match.group(1) is not None:
            #     # next match is a mid-paragraph code block
            #     # just assume this means what we have so far is not code
            #     # TODO this jump logic should also set last_* variables
            #     cur_idx = cur_par_start = cur_match.end()
            #     fence_end_match = fence_end_re.search(response, cur_idx)
            #     continue

            par = response[cur_par_start:cur_par_end]
            # prepare for next par
            cur_par_start = cur_idx
        else:
            loop = False
            if cur_match:
                cur_par_end = cur_match.start()
                cur_idx = cur_match.end()
            else:
                print(f'Idx {CUR_ITEM_IDX}, thinks did not end!', file=sys.stderr)
                cur_idx = cur_par_end = len(response)
            par = response[cur_par_start:cur_par_end]


        dbg(f'Visiting par:\n{par}\n---')

        found_code = False
        if (
            # TODO regex, this is very Schlemiel-like
            any(par.startswith(p) for p in ('```', 'import ', 'from ')) or
            len(par) < 100 or
            '\n' in par
        ):
            par = clean_backtick_fences(par)
            if last_par_was_code:
                par = ''.join((results[-1], '\n\n', par))

            if check_is_python(par)[0]:
                if last_par_was_code:
                    results[-1] = par
                else:
                    results.append(par)
                found_code = True

        last_par_was_code = found_code

    return results, cur_idx


def find_final_answer_block(
    response: str,
    offset: int,
) -> str | None:
    # early exit on valid input
    if offset == len(response):
        return None

    # NOTE we just accumulate all the blocks b/c this is copypasta, clean up when needed
    results = []

    cur_idx = offset
    cur_par_start = cur_idx
    cur_match = fence_start_re.search(response, cur_idx)
    loop = True
    while loop:
        if cur_match:
            cur_par_start = cur_match.end()
            fence_end_match = fence_end_re.search(response, cur_match.end())
            if not fence_end_match:
                # we can't find any closing fences,
                # so we can't find any more answer blocks,
                # so we're done
                break

            cur_par_end = fence_end_match.start()

            par = response[cur_par_start:cur_par_end]

            # prepare for next par
            cur_idx = fence_end_match.end()
            cur_match = fence_start_re.search(response, cur_idx)
        else:
            loop = False
            if cur_match:
                cur_par_end = cur_match.start()
                cur_idx = cur_match.end()
            else:
                cur_idx = cur_par_end = len(response)
            par = response[cur_par_start:cur_par_end]

        if (
            # TODO regex, this is very Schlemiel-like
            any(par.startswith(p) for p in ('```', 'import ', 'from ')) or
            len(par) < 100 or
            '\n' in par
        ):
            par = clean_backtick_fences(par)
            if check_is_python(par)[0]:
                results.append(par)

    return results[-1] if results else None



def find_code(response: str) -> tuple[list[str], str | None]:
    # TODO we should also look for actual backticked code blocks
    # (confirmed that backticked code can be in thinks)
    # TODO all answer candidates should have a print
    offset = 0
    if m := offset_re.search(response):
        offset = m.end()

    think_code_blocks, offset = find_think_code_blocks(response, offset)

    final_answer = find_final_answer_block(response, offset)

    return think_code_blocks, final_answer

# s = """
# Thus, the code should handle all cases correctly.
# </think>

# ```
# t = int(input())
# for _ in range(t):
#     keyboard = input().strip()
#     s = input().strip()
#     pos = {c: i for i, c in enumerate(keyboard)}
#     total = 0
#     prev = pos[s[0]]
#     for c in s[1:]:
#         curr = pos[c]
#         total += abs(curr - prev)
#         prev = curr
#     print(total)
# ```

# Bye.
# """.strip()
# find_answer_candidates(s)

def main(input_gen):
    from test_code_maker import make_test_code

    global CUR_ITEM_IDX
    backtick_or_end_think = re.compile(r'(```|</think>)')
    # the file handle is closed on program exit :)
    idx = 0

    cols = ['idx', 'response_len', 'think_code_blocks', 'answer_candidates', 'final_answer', 'has_input', 'has_stdin', 'has_strange_stdin', 'has_print']
    stat_row = namedtuple('stat_row', cols)
    def print_row(row: list):
        not_first = False
        for cell in row:
            if not_first:
                print(', ', end='')
            print(cell, end='')
            not_first = True
        print()

    def looks_like_answer(code: str) -> bool:
        return (
            'input()' in code and
            ('stdin' in code or 'print(' in code)
        )

    print_row(cols)
    # for line in open('codeforces-cots+solutions_py.jsonl', 'r'):
        # row = json.loads(line)
    for row in input_gen:
        idx += 1
        CUR_ITEM_IDX = idx
        response: str = row['generation']

        # TODO looks like mid-paragraph code blocks are never in thinks
        # so we can just scan the proper response differently
        if m := backtick_or_end_think.search(response):
            if m.group(0) == '```':
                extra = ''
                m_start = m.start()
                m_start -= 2
                if m_start > 0 and response[m_start] != '\n':
                    extra = '(mid-paragraph) '

                print(f'Idx {idx}, found {extra}backticks in thinks!', file=sys.stderr)

        think_code_blocks, final_answer = find_code(response)
        answer_candidates = list(filter(looks_like_answer, think_code_blocks))
        has_final_answer = final_answer is not None
        cur_stat_dict = {
            'idx': idx,
            'response_len': len(response),
            'think_code_blocks': len(think_code_blocks),
            'answer_candidates': len(answer_candidates),
            'final_answer': has_final_answer,
            'has_input': has_final_answer and 'input()' in final_answer,
            'has_stdin': has_final_answer and 'stdin' in final_answer,
            'has_strange_stdin': has_final_answer and 'stdin' in final_answer and 'sys.stdin' not in final_answer,
            'has_print': has_final_answer and 'print(' in final_answer,
        }
        print_row(stat_row(**cur_stat_dict))

        item_outd = outd / f'{idx}'
        item_outd.mkdir(parents=True, exist_ok=True)
        with (item_outd/'examples.json').open('w') as fh:
            json.dump(row['examples'], fh)
        with (item_outd/'stats.jsonl').open('w') as fh:
            json.dump(cur_stat_dict, fh)
        with (item_outd/'prompt.md').open('w') as fh:
            print(row['prompt'], file=fh)
        with (item_outd/'final_answer.py').open('w') as fh:
            print(final_answer, file=fh)
        thinks_end = response.rfind('</think>')
        if thinks_end != -1:
            thinks_str = response[:thinks_end].rstrip()
            with (item_outd/'thinks.md').open('w') as fh:
                print(thinks_str, file=fh)
        with (item_outd/'rendered.md').open('w') as fh:
            print("# {title} ({contest_name}, {contest_start_year})".format(**row), file=fh)
            print("# Prompt", file=fh)
            print(row['prompt'], file=fh)
            print("# Response", file=fh)
            print(row['generation'], file=fh)
            print("\n# Think code blocks", file=fh)
            not_first = False
            for ans in think_code_blocks:
                if not_first:
                    print('\n---\n', file=fh)
                print('```python', file=fh)
                print(ans, file=fh)
                print('```', file=fh)
                not_first = True
            del not_first


            print('\n# Final answer', file=fh)
            if final_answer is not None:
                print('```python', file=fh)
                print(final_answer, file=fh)
                print('```', file=fh)

        if row['examples']:
            answer_check_dir = item_outd/'answer_checks'
            answer_check_dir.mkdir(parents=True, exist_ok=True)
            for ans_idx, ans in enumerate(answer_candidates):
                with (answer_check_dir/f'candidate-{ans_idx}.py').open('w') as fh:
                    print(make_test_code(ans, row['examples']), file=fh)

            if final_answer is not None:
                with (answer_check_dir/'final_answer.py').open('w') as fh:
                    print(make_test_code(final_answer, row['examples']), file=fh)

if __name__ == '__main__' and 'NOGO' not in env:
    import datasets
    ds = datasets.load_dataset('open-r1/codeforces-cots', 'solutions_py', split='train[:1000]')
    main(ds)