from io import StringIO
import re
import sys

from loguru import logger


TESTS_PREFIX = \
    '''\
import io

TEST_CASES = [\
'''

TEST_CASE_PREFIX = '''\
{
    "input": """\\
'''

TEST_CASE_INFIX = \
'''\

""",
    "output": """\\
'''

TEST_CASE_SUFFIX = \
'''\

""",
}, '''

TESTS_SUFFIX = \
'''\
]

for i, test_case in enumerate(TEST_CASES):
    in_stream = io.StringIO(test_case["input"])
    expected_output = test_case["output"].rstrip()

    out_stream = io.StringIO()
    test_program(in_stream, out_stream)
    real_output = out_stream.getvalue().rstrip()

    assert real_output == expected_output, \\
        f'Test case {i} failed.\\nExpected: {expected_output!r}\\nGot: {real_output!r}'

print('Tests passed 😎')
'''

# this only very rarely doesn't work, so it's fine
sys_stdin_rx = re.compile(r'(?<=\W)(sys\.)?stdin(?=\W)')
sys_stdout_rx = re.compile(r'(?<=\W)(sys\.)?stdout(?=\W)')
nonspace_char_rx = re.compile(r'\S')


def gen_instrumented_code_parts(code: str):
    yield 'def test_program(input_stream, output_stream):\n'
    yield '    import builtins\n'
    yield '    input = lambda: input_stream.readline()[:-1]\n'
    yield '    print = lambda *args, **kwargs: builtins.print(*args, **kwargs, file=output_stream)\n'
    is_first = True
    first_offset = 0
    for line in code.splitlines(keepends=True):
        offset = nonspace_char_rx.search(line)
        if offset is None:
            # drop insignificant empty lines
            yield '\n'
            continue
        offset = offset.start()
        if is_first:
            first_offset = offset
            is_first = False
        # if offset < first_offset:
        #     logger.warning('Bad offset ({}) < first_offset ({}); line: {!r}', offset, first_offset, line)
        # TODO this is a temporary hack in case lines with bad offsets show up.
        resolved_offset = min(first_offset, offset)
        # trim the leading whitespace
        line = line[resolved_offset:]
        offset -= resolved_offset
        yield ' '*4
        if line.startswith(('from ', 'import '), offset):
            yield line
        else:
            # Grug virtualize standard streams
            yield sys_stdout_rx.sub('output_stream', sys_stdin_rx.sub('input_stream', line))

def gen_test_code_parts(examples: list[dict]):
    yield TESTS_PREFIX
    for ex in examples:
        yield TEST_CASE_PREFIX
        yield ex['input']
        yield TEST_CASE_INFIX
        yield ex['output']
        yield TEST_CASE_SUFFIX
    yield TESTS_SUFFIX


def make_test_code(
    base_code: str,
    examples: list[dict],
) -> str:
    def _gen_parts():
        yield from gen_instrumented_code_parts(base_code)
        yield '\n\n'
        yield from gen_test_code_parts(examples)

    return ''.join(_gen_parts())