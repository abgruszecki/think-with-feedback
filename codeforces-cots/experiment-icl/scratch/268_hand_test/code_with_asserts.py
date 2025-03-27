def main(in_stream, out_stream):
    n = int(in_stream.readline())
    a = list(map(int, in_stream.readline().split()))
    if 0 in a:
        print(0, file=out_stream)
    else:
        print(min(abs(x) for x in a), file=out_stream)

if __name__ == "__main__":
    import sys
    main(sys.stdin, sys.stdout)


import io

TEST_CASES = [{
    "input": """\
3
2 -6 5
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