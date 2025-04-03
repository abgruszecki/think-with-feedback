from dataclasses import dataclass
import json
from pathlib import Path


INSTRUCTIONS = \
'''\
# Request

You were given a description of a competetive programming problem: \
input/output formats, and also example inputs/outputs and notes if available.

Decide how to check the program output's correctness. \
You have three options: "diff", "checker", and "interaction".

"diff" means that just comparing each character is enough. \
"checker" means a more complex procedure is needed, for instance to compare floating point numbers or to make the comparison case-insensitive. \
Finally, "interaction" means that it's not enough to just send the entire input to a submitted program and read the entire output.

Remember, if the output is case-insensitive in any way, \
or if floating point numbers are involved, or if more than one output is allowed, \
your answer should be "checker".

Format your answer as JSON and put it in fences like this:
```json
{ "type": "checker" }
```
or like this:
```json
{ "type": "diff" }
```

Remember, your task is to describe how to check the program output's correctness. \
Don't try to solve the problem itself. \
If you start solving the problem, go back to your task instead.

Think carefully before giving your answer.
'''

EXAMPLE_TEMPLATE = \
'''\
## Example
```input
{example_input}
```
```output
{example_output}
```

'''

NOTE_TEMPLATE = \
'''\
## Note
{note}

'''

PROMPT_TEMPLATE = \
'''\
# Problem
## Input Format
{input_format}

## Output Format
{output_format}

{example}{note}{instructions}\
'''


root_outd = Path('./out')
root_outd.mkdir(parents=True, exist_ok=True)
outf = root_outd/'0--checker-decision-prompts.jsonl'


if __name__ == '__main__':
    import datasets
    ds = datasets.load_dataset('open-r1/codeforces-cots', 'solutions_py', split='train[:1000]')
    with outf.open('w') as fh:
        for idx, in_row in enumerate(ds):
            examples_data = in_row['examples']
            example_str = ''
            if examples_data:
                example_row = examples_data[0]
                example_str = EXAMPLE_TEMPLATE.format(
                    example_input=example_row['input'],
                    example_output=example_row['output'],
                )
            note_str = ''
            if in_row['note']:
                note_str = NOTE_TEMPLATE.format(
                    note=in_row['note'],
                )
            r = {
                'idx': idx,
                'id': in_row['id'],
                'prompt': PROMPT_TEMPLATE.format(
                    example=example_str,
                    note=note_str,
                    input_format=in_row['input_format'],
                    output_format=in_row['output_format'],
                    instructions=INSTRUCTIONS,
                ),
            }
            json.dump(r, fh)
            print(file=fh)
