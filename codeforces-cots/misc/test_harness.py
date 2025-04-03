import io
import subprocess
import sys


TEST_CASES = [

]


def test_program(input_stream, output_stream, command):
    input_data = input_stream.read()
    process = subprocess.run(
        command,
        input=input_data,
        text=True,
        capture_output=True
    )
    output_stream.write(process.stdout)


if __name__ == "__main__":
    # Get command from command line arguments
    command = sys.argv[1:]

    for i, test_case in enumerate(TEST_CASES):
        in_stream = io.StringIO(test_case["input"])
        expected_output = test_case["output"].rstrip()

        out_stream = io.StringIO()
        test_program(in_stream, out_stream, command)
        real_output = out_stream.getvalue().rstrip()

        assert real_output == expected_output, \
            f'Test case {i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}'

    print('Tests passed 😎')