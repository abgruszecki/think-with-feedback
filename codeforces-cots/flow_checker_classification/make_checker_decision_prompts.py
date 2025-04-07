import io
import json
from pathlib import Path

# TODO add the problem statement, it seems to often be necessary
# TODO explain: we mean a line-by-line diff
# TODO add another type for a "smart" comparer (booleans or floats)
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
## Example{heading_extension}
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
{description}

## Input Format
{input_format}

## Output Format
{output_format}

{examples}{note}{instructions}\
'''


root_outd = Path(__file__).parent/'out'
root_outd.mkdir(parents=True, exist_ok=True)
outf = root_outd/'0--checker-decision-prompts.jsonl'


if __name__ == '__main__':
    import datasets
    ds = datasets.load_dataset('open-r1/codeforces-cots', 'solutions_py', split='train[:1000]')
    with outf.open('w') as fh:
        for idx, in_row in enumerate(ds):
            examples_data = in_row['examples']
            if examples_data is None:
                examples_data = []
            examples_buf = io.StringIO()
            examples_count = len(examples_data)
            for ex_idx, ex_row in enumerate(examples_data):
                heading_extension = f' {ex_idx+1}' if examples_count > 1 else ''
                examples_buf.write(
                    EXAMPLE_TEMPLATE.format(
                        heading_extension=heading_extension,
                        example_input=ex_row['input'],
                        example_output=ex_row['output'],
                    )
                )
            examples_str = examples_buf.getvalue()

            note_str = ''
            if in_row['note']:
                note_str = NOTE_TEMPLATE.format(
                    note=in_row['note'],
                )
            r = {
                'idx': idx,
                'id': in_row['id'],
                'prompt': PROMPT_TEMPLATE.format(
                    **{k: in_row[k] for k in ['description', 'input_format', 'output_format']},
                    examples=examples_str,
                    note=note_str,
                    instructions=INSTRUCTIONS,
                ),
            }
            json.dump(r, fh)
            print(file=fh)
    print(f'Wrote {idx+1} prompts to: {outf}')