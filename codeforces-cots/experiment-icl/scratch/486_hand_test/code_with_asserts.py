def main(in_stream, out_stream):
    t = int(in_stream.readline())
    for _ in range(t):
        n = int(in_stream.readline())
        a = list(map(int, in_stream.readline().split()))
        print(-sum(a), file=out_stream)

import io

TEST_CASES = [{
    "input": """\
2
4
3 -4 5
11
-30 12 -57 7 0 -81 -68 41 -89 0
""",
    "output": """\
-4
265
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