#!/usr/bin/env python3
import io
from typing import Iterable, Iterator

import pydantic
from tqdm import tqdm
import typer

import py_shared.flow as fl

app = typer.Typer()

class DsOneExample(pydantic.BaseModel):
    input: str
    output: str

class DsInputs(pydantic.BaseModel):
    problem_statement: str
    input_format: str | None
    output_format: str | None
    examples: list[DsOneExample]
    problem_notes: str | None

class DsRow(pydantic.BaseModel):
    idx: int
    id: str
    inputs: DsInputs


PROMPT_PREFIX = '''\
Your task is to solve a competitive programming problem.

# Problem
'''

PROMPT_INPUT_FORMAT_HEADER = '''\

# Input Format
'''

PROMPT_OUTPUT_FORMAT_HEADER = '''\

# Output Format
'''

PROMPT_EXAMPLES_HEADER = '''\

# Examples
'''

PROMPT_ONE_EXAMPLE_TEMPLATE = '''\
# Example {i}
Input:
```
{input}
```

Output:
```
{output}
```
'''

PROMPT_NOTES_HEADER = '''\

# Notes
'''

PROMPT_SUFFIX = '''\

# Instructions
Analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed \
to process the largest possible test cases within the time and memory limits, \
then explain why your chosen implementation strategy is the most efficient solution. \
Please reason step by step about your solution approach, \
then provide a complete implementation in Lua 5.1 which targets LuaJIT and is thoroughly optimized for both speed and memory usage.

Put your final answer in a single code block:
```lua
<your code here>
```
'''

def build_prompt(
    inputs: DsInputs,
) -> str:
    b = io.StringIO()
    def put(*objects: str):
        print(*objects, sep='', end='', file=b)
    put(PROMPT_PREFIX, inputs.problem_statement, '\n')
    if inputs.input_format:
        put(PROMPT_INPUT_FORMAT_HEADER, inputs.input_format, '\n')
    if inputs.output_format:
        put(PROMPT_OUTPUT_FORMAT_HEADER, inputs.output_format, '\n')
    if inputs.examples:
        put(PROMPT_EXAMPLES_HEADER, '\n')
        for i, e in enumerate(inputs.examples, 1):
            if i > 1:
                put('\n')
            put(PROMPT_ONE_EXAMPLE_TEMPLATE.format(i=i, input=e.input, output=e.output))
    if inputs.problem_notes:
        put(PROMPT_NOTES_HEADER, inputs.problem_notes, '\n')
    put(PROMPT_SUFFIX)

    return b.getvalue()



@app.command()
def main(
    range_start: int = 0,
    range_size: int = -1,
):
    ctx = fl.dirs(__file__)

    dep_ds_checker_types_f = ctx.flow_outd/'fetch_extract_checker_type/checker-types.jsonl'
    dep_ds_f = ctx.flow_outd/'fetch_process_solutions_py/report.jsonl'

    outf = ctx.step_outd/'result.jsonl'

    wanted_indices = set(
        r['idx']
        for r in fl.ser.jsonl_streamf(dep_ds_checker_types_f)
        if r.get('type') == 'diff'
    )

    from itertools import islice
    def _gen_data_rows():
        return islice(
            (r for r in fl.ser.model_jsonl_streamf(DsRow, dep_ds_f) if r.idx in wanted_indices),
            range_start,
            (range_start + range_size) if range_size != -1 else None,
        )
    data_len = sum(1 for _ in _gen_data_rows())

    def gen_output_rows(
        wanted_ds_rows: Iterable[DsRow],
    ) -> Iterator[dict]:
        for r in wanted_ds_rows:
            r = {
                'idx': r.idx,
                'id': r.id,
                'prompt': build_prompt(r.inputs),
            }
            yield r

    fl.ser.jsonl_dumpf(
        gen_output_rows(_gen_data_rows()),
        outf,
    )


if __name__ == '__main__':
    app()