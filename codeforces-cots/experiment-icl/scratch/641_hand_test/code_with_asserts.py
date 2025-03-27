def main(in_stream, out_stream):
    n = int(in_stream.readline())
    arr = [int(in_stream.readline()) for _ in range(n)]
    arr.sort()
    print(' '.join(map(str, arr)), file=out_stream)

import io

TEST_CASES = [{
    "input": """\
5
7
1
9
7
3
""",
    "output": """\
1 3 7 7 9
""",
}, {
    "input": """\
10
60
1
60
1
60
1
60
1
60
1
""",
    "output": """\
1 1 1 1 1 60 60 60 60 60
""",
}]

for i, test_case in enumerate(TEST_CASES):
    in_stream = io.StringIO(test_case["input"])
    expected_output = test_case["output"].rstrip()

    out_stream = io.StringIO()
    main(in_stream, out_stream)
    real_output = out_stream.getvalue().rstrip()

    assert real_output == expected_output, f'Test case {i} failed'

print('Tests passed 😎')