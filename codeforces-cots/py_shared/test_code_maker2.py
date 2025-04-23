from io import StringIO
import re
import sys


TESTS_PREFIX = '''\
def test():
    import io

    TEST_CASES = [\
'''

TEST_CASE_PREFIX = '''\
        {
            "input": \\
"""\\
'''
TEST_CASE_INFIX = '''\

""",
            "output": \\
"""\\
'''
TEST_CASE_SUFFIX = '''\

""",
        }, \
'''

TESTS_SUFFIX = '''\
    ]

    for i, test_case in enumerate(TEST_CASES):
        in_stream = io.StringIO(test_case["input"])
        expected_output = test_case["output"].rstrip()

        out_stream = io.StringIO()
        main(in_stream, out_stream)
        real_output = out_stream.getvalue().rstrip()

        assert real_output == expected_output, \\
            f'Test case {i} failed.\\nExpected: {expected_output!r}\\nGot: {real_output!r}'

    print('Tests passed 😎')


if __name__ == '__main__':
    test()
'''


def make_test_code(
    instrumented_code: str,
    examples: list[dict],
) -> str:
    buf = StringIO()
    print(
        instrumented_code,
        '\n\n',
        sep='',
        file=buf,
    )

    print(TESTS_PREFIX, file=buf)
    for ex in examples:
        print(
            TEST_CASE_PREFIX,
            ex['input'],
            TEST_CASE_INFIX,
            ex['output'],
            TEST_CASE_SUFFIX,
            sep='',
            file=buf,
        )
    print(TESTS_SUFFIX, file=buf)

    return buf.getvalue()