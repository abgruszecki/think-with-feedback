#!/usr/bin/env python3
import asyncio
from collections import namedtuple
from dataclasses import dataclass
from datetime import datetime
import json
from os import environ
from pathlib import Path
from typing import Callable, Iterable, Iterator

from loguru import logger
from openai import AsyncOpenAI
from openai.types.completion_usage import CompletionUsage
import typer
from tqdm import tqdm

from py_shared import ser
from py_shared.misc import step_dirs, cwd_rel


type ModelHandle = tuple[str, AsyncOpenAI]


def make_model_handle(
    model: str,
    use_openrouter: bool,
) -> ModelHandle:
    if use_openrouter:
        resolved_model = 'openai/'+model
        base_url='https://openrouter.ai/api/v1'
        api_key=environ['OPENROUTER_API_KEY']
    else:
        resolved_model = model
        base_url = None
        api_key = None

    client = AsyncOpenAI(
        base_url=base_url,
        api_key=api_key,
    )

    return (resolved_model, client)


@dataclass
class UsageCounter:
    prompt_toks: int = 0
    compl_toks: int = 0
    total_toks: int = 0 # we can use this to make sure things add up

    def add(self, usage: CompletionUsage):
        self.prompt_toks += usage.prompt_tokens
        self.compl_toks += usage.completion_tokens
        self.total_toks += usage.total_tokens

    def expected_total_toks(self) -> int:
        return self.prompt_toks + self.compl_toks

    def adds_up(self) -> bool:
        return self.total_toks == self.expected_total_toks()


_PricingNT = namedtuple('_PricingNT', ['input_tok', 'output_tok'])
pricings = {
    'gpt-4o-mini': _PricingNT(input_tok=0.15/1e6, output_tok=0.6/1e6),
    'gpt-4.1-mini': _PricingNT(input_tok=0.4/1e6, output_tok=1.6/1e6),
}
def total_cost(
    model: str,
    counter: UsageCounter,
) -> float | None:
    pricing = pricings.get(model)
    if not pricing:
        return None
    return sum((
        counter.prompt_toks*pricing.input_tok,
        counter.compl_toks*pricing.output_tok,
    ))


async def make_request(
    prompt: str,
    api: tuple[str, AsyncOpenAI],
    icl_shots: list[tuple[str, str]] = [],
) -> tuple[list[str], CompletionUsage|None]:
    messages = []
    for shot_prompt, shot_response in icl_shots:
        messages.append({'role': 'user', 'content': shot_prompt})
        messages.append({'role': 'assistant', 'content': shot_response})
    messages.append({'role': 'user', 'content': prompt})
    model, client = api
    response = await client.chat.completions.create(
        model=model,
        messages=messages,
    )
    msg_contents = list(filter(None, (o.message.content for o in response.choices)))
    return msg_contents, response.usage



async def process_prompt_row(
    in_row: dict,
    semaphore: asyncio.Semaphore,
    api: tuple[str, AsyncOpenAI],
    key_fn: Callable[[dict], str],
    prompt_fn: Callable[[dict], str],
    icl_shots: list[tuple[str, str]] = [],
) -> tuple[dict, str, CompletionUsage | None] | None:
    try:
        idx = key_fn(in_row)
    except:
        logger.exception('Exn when getting key for row: {!r}', in_row)
        return None
    try:
        async with semaphore:
            response_strs, usage = await make_request(
                prompt=prompt_fn(in_row),
                api=api,
                icl_shots=icl_shots,
            )
        if len(response_strs) != 1:
            logger.warning('Expected exactly 1 response, got {} at: {}', len(response_strs), idx)
            if len(response_strs) == 0:
                return None
        response = response_strs[0]
        return in_row, response, usage
    except Exception:
        logger.exception('Exn at row: {}', idx)
        return None


app = typer.Typer()


flowd, flow_outd, run_outd = step_dirs(__file__, has_runs=True)

dep_f = flow_outd/f'extract_simulation_snippets/result.jsonl'

out_prompts_f = run_outd/'prompts.jsonl'
out_res_f = run_outd/'result.jsonl'

openai_model = 'gpt-4o-mini'
# openai_model = 'gpt-4.1-mini'

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


def _count_usage(counter: UsageCounter, usage: CompletionUsage | None):
    if usage:
        counter.add(usage)
    else:
        logger.warning('Got usage=None, costs will be off')


def _log_usage(counter: UsageCounter):
    if not counter.adds_up():
        logger.warning('Token usage does not add up (cache or reasoning?): {!r}', counter)

    usage_cost = total_cost(openai_model, counter)
    if usage_cost:
        logger.success('Usage cost: ${:.2f}', usage_cost)
    else:
        logger.warning(
            'Unknown costs, since model is unknown: model={!r}, usage={!r}',
            openai_model,
            counter,
        )


async def _process_prompt_row(
    in_r,
    semaphore,
    api: ModelHandle,
    icl_shots: list[tuple[str, str]] = [],
) -> tuple[dict, CompletionUsage | None] | None:
    res = await process_prompt_row(
        in_row=in_r,
        semaphore=semaphore,
        api=api,
        key_fn=lambda r: r['idx'],
        prompt_fn=lambda r: r['prompt'],
        icl_shots=icl_shots,
    )
    if res is None:
        return None

    in_r, response, usage = res
    r = {
        'idx': in_r['idx'],
        'offset': in_r['offset'],
    }
    r.update(in_r['inputs'])
    r['response'] = response
    return r, usage


async def async_main(
    use_openrouter: bool = False,
):
    api: ModelHandle = make_model_handle(openai_model, use_openrouter)
    usage_counter = UsageCounter()

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

    semaphore = asyncio.Semaphore(20)
    with open(out_res_f, 'w') as res_fh:
        # NOTE Right now we load all the prompts into memory.
        # NOTE Async queues could be better since for large datasets we want "backpressure".
        tasks = [
            asyncio.create_task(_process_prompt_row(in_r, semaphore, api, icl_shots=icl_shots))
            for in_r in prompts
        ]

        for t in tqdm(asyncio.as_completed(tasks), total=len(tasks)):
            out = await t
            if out is None:
                continue
            r, usage = out
            _count_usage(usage_counter, usage)
            print(json.dumps(r), file=res_fh)
    logger.success('Wrote: {}', cwd_rel(out_res_f))

    _log_usage(usage_counter)


@app.command()
def main(
    # Keep in sync with async_main ( typer doesn't allow async commands :( )
    use_openrouter: bool = False,
):
    # TODO ask Sonnet to check with reflection that main, async_main are in sync?
    asyncio.run(async_main(
        use_openrouter=use_openrouter,
    ))


if __name__ == '__main__':
    app()
