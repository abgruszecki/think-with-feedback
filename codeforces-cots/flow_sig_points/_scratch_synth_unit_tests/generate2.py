#!/usr/bin/env python3
import asyncio
from collections import namedtuple
from dataclasses import dataclass, field
from datetime import datetime
import json
from os import environ
from pathlib import Path
from typing import Annotated, Callable, Iterable, Iterator

from loguru import logger
from openai import AsyncOpenAI
from openai.types.completion_usage import CompletionUsage
import sglang as sgl
from sglang.lang.interpreter import ProgramState as SglState
import typer
from tqdm import tqdm

from py_shared import ser
from py_shared.misc import step_dirs, cwd_rel


@dataclass
class RequestArgs:
    """
    Arguments to `make_request`.
    Keeping them in a dataclass makes working with SGLang APIs easier:
    no matter if we call `make_request` directly or via `run_batch`,
    the args are always typechecked and the defaults are uniform.
    """
    prompt: str
    icl_shots: list[tuple[str, str]] = field(default_factory=list)


@sgl.function
def make_request(
    s: SglState,
    args: RequestArgs,
):
    for shot_prompt, shot_response in args.icl_shots:
        s += s.user(shot_prompt)
        s += s.assistant(shot_response)
    s += s.user(args.prompt)
    s += s.assistant(sgl.gen('response', max_tokens=4*1024))



def gen_processed_prompt_rows(
    in_rows: list[dict],
    key_fn: Callable[[dict], str],
    prompt_fn: Callable[[dict], str],
    icl_shots: list[tuple[str, str]] = [],
) -> Iterator[tuple[dict, str]]:
    indices = []
    for r in in_rows:
        try:
            indices.append(key_fn(r))
        except:
            logger.exception('Exn when getting key for row: {!r}', r)
            # return  # early quitting in batch jobs is a bad idea...
    try:
        s: SglState
        for r, s in zip(in_rows, make_request.run_batch([{'args': RequestArgs(
            prompt=prompt_fn(in_row),
            icl_shots=icl_shots,
        )} for in_row in in_rows])):
            response = s['response']
            yield r, response
    except Exception:
        logger.exception('Exn at rows: {!r}', indices)


app = typer.Typer()


flowd, flow_outd, run_outd = step_dirs(__file__, has_runs=True)

dep_f = flow_outd/f'extract_simulation_snippets/result.jsonl'

out_prompts_f = run_outd/'prompts.jsonl'
out_res_f = run_outd/'result.jsonl'

# NOTE I'm not sure about including the entire problem statement in the prompt,
# but at least the examples and I/O format may be useful.
PROMPT_TEMPLATE =\
'''\
The user is solving a competetive programming problem and put their reasoning in text.

# User's problem
{problem_statement}
{input_format_section}\
{output_format_section}\
{problem_examples_section}\
{problem_notes_section}\

# User's code
```python
{code}
```

# User's reasoning about the code
```text
{reasoning}
```
{instructions}\
'''

INSTRUCTIONS=\
'''\

# Instructions
The user is reasoning about a Python program which reads from stdin and writes to stdout. \
The reasoning fragment may predict what the program does on some inputs. \
If it does, then write a Python script which tests the program on those inputs and put it in a Markdown code block. \
If it doesn't, then just output an empty code block.

Your script must include the user's code as a function. \
To test it, you may need to slightly rewrite the user's code to take input/output streams as arguments. \
The user may refer to input/output samples from the problem statement in their reasoning. \
If any of the tests fail, the script should print the expected and the actual output and exit with a non-zero exit code. \
Otherwise, it exits normally with exit code 0.
'''

INPUT_FORMAT_TEMPLATE=\
'''\

## Input format
{input_format}
'''

OUTPUT_FORMAT_TEMPLATE=\
'''\

## Output format
{output_format}
'''

EXAMPLES_HEADER=\
'''\

## Input/output examples
'''

ONE_EXAMPLE_TEMPLATE=\
'''\
```json
{formatted_json}
```
'''

NOTES_TEMPLATE=\
'''\

## Notes
{notes}
'''


def make_prompt(
    reasoning: str,
    code: str,
    problem_statement: str,
    input_format: str|None,
    output_format: str|None,
    examples: list[dict],
    problem_notes: str|None,
) -> str:
    input_format_section = ''
    output_format_section = ''
    if input_format:
        input_format_section = INPUT_FORMAT_TEMPLATE.format(input_format=input_format)
    if output_format:
        output_format_section = OUTPUT_FORMAT_TEMPLATE.format(output_format=output_format)

    examples_section = ''
    if examples:
        examples_section = EXAMPLES_HEADER + ''.join(
            ONE_EXAMPLE_TEMPLATE.format(
                formatted_json=json.dumps(e, indent=4)
            )
            for e in examples
        )
    notes_section = ''
    if problem_notes:
        notes_section = NOTES_TEMPLATE.format(notes=problem_notes)

    return PROMPT_TEMPLATE.format(
        reasoning=reasoning,
        code=code,
        problem_statement=problem_statement,
        input_format_section=input_format_section,
        output_format_section=output_format_section,
        problem_examples_section=examples_section,
        problem_notes_section=notes_section,
        instructions=INSTRUCTIONS,
    )


def _gen_processed_prompt_rows(
    in_rows: list[dict],
    icl_shots: list[tuple[str, str]] = [],
) -> Iterator[dict]:
    for in_r, response in gen_processed_prompt_rows(
        in_rows=in_rows,
        key_fn=lambda r: r['idx'],
        prompt_fn=lambda r: r['prompt'],
        icl_shots=icl_shots,
    ):
        r = {
            'idx': in_r['idx'],
            'offset': in_r['offset'],
        }
        r.update(in_r['inputs'])
        r['response'] = response
        yield r


@app.command()
def main(
    port: Annotated[int, typer.Option()],
):
    sgl.set_default_backend(
        sgl.RuntimeEndpoint(f'http://localhost:{port}'),
    )

    res_icl_f = flowd/'resources/synth_unit_tests/icl.json'
    out_icl_f = run_outd/'icl.jsonl'
    icl_data = ser.json_loadf(res_icl_f)
    icl_shots = [
        (make_prompt(**r['inputs']), r['response'])
        for r in icl_data[:3]
    ]
    ser.jsonl_dumpf(
        [{ 'prompt': p, 'response': r } for p, r in icl_shots ],
        out_icl_f,
    )

    def _gen_prompts(
        dep_rows: Iterable[dict],
    ) -> Iterator[dict]:
        for in_r in dep_rows:
            r = { k: in_r[k] for k in ('idx', 'offset') }
            r_inputs = r['inputs'] = {}
            r_inputs['reasoning'] = in_r['text'][:3000]
            for k in (
                'code',
                'problem_statement',
                'input_format',
                'output_format',
                'examples',
                'problem_notes',
            ):
                r_inputs[k] = in_r[k]
            r['num'] = in_r.get('num')
            r['prompt'] = make_prompt(**r_inputs)
            yield r

    from itertools import islice
    start = 200
    limit = 100
    prompts = []
    with open(out_prompts_f, 'w') as prompts_fh:
        # NOTE technically the slice leaves the dep_f file handle open :(
        for r in islice(
            _gen_prompts(ser.jsonl_streamf(dep_f)),
            start,
            start+limit,
        ):
            prompts.append(r)
            print(json.dumps(r), file=prompts_fh)
    logger.success('Wrote: {}', cwd_rel(out_prompts_f))

    batch_sz = 24
    def _r_gen():
        for i in tqdm(range(0, len(prompts), batch_sz)):
            in_rows_batch = prompts[i:i+batch_sz]
            yield from _gen_processed_prompt_rows(
                in_rows=in_rows_batch,
                icl_shots=icl_shots,
            )

    ser.jsonl_dumpf(_r_gen(), out_res_f)
    logger.success('Wrote: {}', cwd_rel(out_res_f))

    # _log_usage(usage_counter)


if __name__ == '__main__':
    app()
