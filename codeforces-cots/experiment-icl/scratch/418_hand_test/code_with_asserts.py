def main(in_stream, out_stream):
    t = int(in_stream.readline())
    for _ in range(t):
        n = int(in_stream.readline())
        a = list(map(int, in_stream.readline().split()))
        total = sum(a)
        print(0 if total % n == 0 else 1, file=out_stream)

import io

TEST_CASES = [{
    "input": """\
3
3
10 10 10
4
3 2 1 2
5
1 2 3 1 5
""",
    "output": """\
0
0
1
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