import json
import subprocess
import sys
from pathlib import Path

cwd = Path(__file__).parent


def test_snippet(input_str: str) -> str:
    process = subprocess.run(
        ['luajit', str(cwd/'snippet.lua')],
        input=input_str,
        text=True,
        capture_output=True
    )
    if process.stderr:
        print(process.stderr, file=sys.stderr)
    return process.stdout


if __name__ == '__main__':
    with open(cwd/'examples.json') as fh:
        test_cases = json.load(fh)

    for i, test_case in enumerate(test_cases):
        in_str = test_case['input']
        expected_output = test_case['output'].rstrip()
        real_output = test_snippet(in_str).rstrip()

        assert real_output == expected_output, \
            f'Test case idx={i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}'

    print('Tests passed 😎')
