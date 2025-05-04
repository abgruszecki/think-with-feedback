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
    def mk_args(r):
        return RequestArgs(
            prompt=prompt_fn(r),
            icl_shots=icl_shots,
        )

    def safe_key_fn(r) -> str:
        """ Defensive programming yay! """
        try:
            return key_fn(r)
        except:
            logger.exception('Exn when getting key for row: {!r}', r)
            return ''

    indices = [ safe_key_fn(r) for r in in_rows ]
    try:
        # NOTE I'm not sure if run_batch is lazy or not...
        batch_res = list(make_request.run_batch([{'args': mk_args(r)} for r in in_rows]))
    except Exception:
        logger.exception('Exn at rows: {!r}', indices)
        return
    s: SglState
    for r, s in zip(in_rows, batch_res):
        try:
            response = s['response']
            yield r, response
        except:
            # yes, an exception can happen here (sometimes 'response' is missing, IDK why)
            logger.exception('Exn when yielding at row: {}', safe_key_fn(r))


app = typer.Typer()


PROMPT_TEMPLATE =\
'''\
The user wrote some notes while making a solution to a competetive programming problem. \
They were simulating how their code behaves on some inputs; the text where they were doing so was extracted into XML tags.

# {first_heading}
{problem_statement}
{input_format_section}\
{output_format_section}\
{problem_examples_section}\
{problem_notes_section}

# User's code
```python
{code}
```

# Code simulation snippets from the user's notes
{code_simulation_snippets}

{instruction_section}\
'''

FIRST_HEADING_NORMAL = 'The competetive programming problem'
FIRST_HEADING_SHORT = 'The I/O format descriptions and examples for the competetive programming problem'

INSTRUCTIONS=\
'''\

# Instructions
The user wrote some notes while working on a competetive programming problem. \
The XML tags contain snippets extracted from the notes where the user was probably \
"thinking aloud" about how the code they were writing would behave on some inputs.

If the user was really simulating the code, \
then write a Python script which tests the program on those inputs \
and put it in a code block. \
Otherwise, just output an empty code block.

Your script must include the user's code as a function. \
To test the code, you may need to slightly rewrite it, e.g. to take input/output streams as arguments. \
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
    simulations: str,
    code: str,
    problem_statement: str,
    input_format: str|None,
    output_format: str|None,
    examples: list[dict],
    problem_notes: str|None,
    short_problem_description: bool,
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
    if not short_problem_description and problem_notes:
        notes_section = NOTES_TEMPLATE.format(notes=problem_notes)

    if not short_problem_description:
        first_heading = FIRST_HEADING_NORMAL
    else:
        first_heading = FIRST_HEADING_SHORT
        problem_statement = ''

    return PROMPT_TEMPLATE.format(
        first_heading=first_heading,
        code_simulation_snippets=simulations,
        code=code,
        problem_statement=problem_statement,
        input_format_section=input_format_section,
        output_format_section=output_format_section,
        problem_examples_section=examples_section,
        problem_notes_section=notes_section,
        instruction_section=INSTRUCTIONS,
    )


def has_extracted_simulations(sims: str) -> bool:
    return '<simulation' in sims # good enough at the moment


def _gen_processed_prompt_rows(
    in_rows: list[dict],
    icl_shots: list[tuple[str, str]] = [],
) -> Iterator[dict]:
    prompt_fn = lambda r: r['prompt']
    for in_r, response in gen_processed_prompt_rows(
        in_rows=in_rows,
        key_fn=lambda r: '/'.join(str(r[k]) for k in ('idx', 'offset')),
        prompt_fn=prompt_fn,
        icl_shots=icl_shots,
    ):
        r = { 'idx': in_r['idx'], 'offset': in_r['offset'], }
        r['inputs'] = in_r['inputs']
        r['prompt'] = in_r['prompt']
        r['response'] = response
        yield r


@app.command()
def main(
    port: Annotated[int, typer.Option()],
    use_icl: bool = True,
    prompt_type: str = 'normal',
    extend_run: Path | None = None,
    force: bool = False,
):
    allowed_prompt_types = ('normal', 'short-problem-description')
    if prompt_type not in allowed_prompt_types:
        raise typer.BadParameter(f'--prompt-type was {prompt_type!r}, must be one of: {", ".join(allowed_prompt_types)}')

    use_short_descr = prompt_type == 'short-problem-description'

    sgl.set_default_backend(
        sgl.RuntimeEndpoint(f'http://localhost:{port}'),
    )

    flowd, flow_outd, step_outd = step_dirs(__file__, has_runs=True, extend_run=extend_run or 'last', force=force)
    subflowd = Path(__file__).parent
    rsrc_d = subflowd/'resources'/Path(__file__).stem
    run_outd = step_outd.parent
    logger.add(step_outd/'logs.txt')

    rsrc_icl_f = rsrc_d/'icl.json'

    dep_code_f = flow_outd/'ai_extraction_prep/sliced_reasoning/result.jsonl'
    dep_sims_f = run_outd/'ai_extract_simulations/result.jsonl'

    out_cfg_f = step_outd/'config.json'
    out_icl_f = step_outd/'icl.jsonl'
    out_prompts_f = step_outd/'prompts.jsonl'
    out_res_f = step_outd/'result.jsonl'

    ser.json_dumpf({
        'use_icl': use_icl,
        'prompt_type': prompt_type,
    }, out_cfg_f)

    if use_icl:
        icl_data = ser.json_loadf(rsrc_icl_f)
        icl_shots = [(
            make_prompt(**r['inputs'], short_problem_description=use_short_descr),
            r['response'],
        ) for r in icl_data[:3]]
        ser.jsonl_dumpf(
            [{ 'prompt': p, 'response': r } for p, r in icl_shots ],
            out_icl_f,
        )
    else:
        icl_shots = []

    keycols = ('idx', 'offset')

    def _gen_code_kv(
        dep_code_rows: Iterable[dict],
    ):
        for r in dep_code_rows:
            key_tup = tuple(r[k] for k in keycols)
            yield key_tup, r

    def _gen_ext_sim_rows(
        dep_sim_rows: Iterable[dict],
        code_by_key: dict,
    ):
        for in_r in dep_sim_rows:
            key_tup = tuple(in_r[k] for k in keycols)
            r = code_by_key[key_tup].copy()
            r.update(in_r)
            yield r

    def _gen_prompts(
        ext_sim_rows: Iterable[dict],
    ) -> Iterator[dict]:
        for in_r in ext_sim_rows:
            r = { k: in_r[k] for k in keycols }
            r_inputs = r['inputs'] = {}
            r_inputs['simulations'] = sims = in_r['response']
            if not has_extracted_simulations(sims):
                continue
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
            r['prompt'] = make_prompt(**r_inputs, short_problem_description=use_short_descr)
            yield r

    code_by_key = dict(_gen_code_kv(ser.jsonl_streamf(dep_code_f)))

    prompts = []
    with open(out_prompts_f, 'w') as prompts_fh:
        for r in _gen_prompts(_gen_ext_sim_rows(
            dep_sim_rows=ser.jsonl_streamf(dep_sims_f),
            code_by_key=code_by_key,
        )):
            prompts.append(r)
            print(json.dumps(r), file=prompts_fh)
    logger.success('Wrote: {}', cwd_rel(out_prompts_f))

    # NOTE SGL does "smart" batching (at least at the moment), i.e., it dynamically adjusts
    # the real batch size based on OOM errors. In principle, this means we can send it a large
    # number of prompts and it will make it work. 24 is a good number because it divides well.
    # However, at the moment it seems that figuring out the batch size like this is very slow,
    # so we're sending a much smaller batch to avoid OOM errors. There's also the part where
    # if one member of the batch triggers an error, e.g. by exceeding max token length,
    # the entire batch is rejected.
    # batch_sz = 24
    batch_sz = 4
    def _out_row_gen():
        with tqdm(desc='Processing prompts', total=len(prompts)) as pbar:
            for i in range(0, len(prompts), batch_sz):
                in_rows_batch = prompts[i:i+batch_sz]
                yield from _gen_processed_prompt_rows(
                    in_rows=in_rows_batch,
                    icl_shots=icl_shots,
                )
                pbar.update(batch_sz)

    ser.jsonl_dumpf(_out_row_gen(), out_res_f)
    logger.success('Wrote: {}', cwd_rel(out_res_f))

    # _log_usage(usage_counter)


if __name__ == '__main__':
    app()
