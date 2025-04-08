#!/usr/bin/env python3
import io
import json
from pathlib import Path

# The idea is that if the checker needs to do _anything_ more complicated than a line-wise diff,
# the problem is marked with "checker".
# We can later filter out the "checker" problems where it looks like a standard checker is enough.
# ("Standard" checker tries to compare floats or booleans.)
# ((1) it seems rare for floats/booleans to occur in problems which allow multiple valid outputs,
#  (2) we don't really know if floats/booleans are the only )
INSTRUCTIONS = \
'''\
# Request
You were given a description of a competetive programming problem, \
together with input/output formats, input/output examples and notes, if available.

Decide how to check the program output's correctness. \
Pick one of three "types": "diff", "checker", and "interaction". \
Also, you can "tag" a problem as "many-valid-outputs" if there are many valid outputs for one input.

"diff" means that comparing each line character-by-character is enough. \
"checker" means we need to do a more complicated comparison, \
for instance to compare floating point numbers or to make the comparison case-insensitive. \
Finally, "interaction" means that it's not enough to \
send the entire input to a submitted program and read the entire output.

Remember, if the output is case-insensitive in any way, \
or if floating point numbers are involved, \
the "type" should be "checker". \
If there are many valid outputs for one input, also add the "many-valid-outputs" tag.

Format your answer as JSON with two fields, "type" and "tags", and put it in fences like this:
```json
{ "type": "checker", "tags": ["many-valid-outputs"] }
```
or like this:
```json
{ "type": "diff", "tags": []}
```

Remember, your task is to describe how to check if the output is correct. \
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
step_outd = root_outd/'make_checker_decision_prompts'
step_outd.mkdir(parents=True, exist_ok=True)
outf = step_outd/'checker-decision-prompts.jsonl'


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
    print(f'Wrote {idx+1} prompts to: {outf.relative_to(Path.cwd())}')