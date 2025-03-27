from collections import Counter

def main(in_stream, out_stream):
    n = int(in_stream.readline())
    a = list(map(int, in_stream.readline().split()))
    count = Counter(a)
    print(max(count.values()), file=out_stream)


import io

TEST_CASES = [{
    "input": """\
6
1 2 4 3 3 2
""",
    "output": """\
2
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