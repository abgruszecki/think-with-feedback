#!/usr/bin/env python3
from collections import namedtuple
from dataclasses import dataclass
from datetime import datetime
from os import environ
import asyncio
from pathlib import Path
from typing import TypedDict, cast

import datasets
from loguru import logger
import typer
from tqdm import tqdm
from openai import AsyncOpenAI
from openai.types.completion_usage import CompletionUsage

from py_shared import ser
from py_shared.misc import step_dirs, cwd_rel


## PRELUDE: OpenAI API ##
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
## END PRELUDE: OpenAI API ##


## PRELUDE: Prompt ##
PROMPT_TEMPLATE = \
'''\
# Text
{response}

# Request
You were given a response snippet where an LLM was solving a competetive programming problem. \
This response may contain text where the LLM was simulating execution of code or pseudocode. \
Such text usually either mentions what's the input and output to the program, \
or mentions that the LLM is considering an example input/output pair which was part of the problem statement. \
Be careful: a simulation isn't just code or description of code or reasoning about code, \
the text must actually describe how some program would execute.

Your task is to find such simulations.

You can only output the start of the simulation text. \
Format each simulation you found with XML like this:

<simulation type="code|pseudocode">
SIMULATION_TEXT_START
</simulation>

Now, find the simulations in the text and format them with as above.
'''


def make_prompt(response: str) -> str:
    return PROMPT_TEMPLATE.format(response=response)
## END PRELUDE: Prompt ##


## PRELUDE: Types ##
class InRow(TypedDict):
    idx: int
    offset: int
    code: str
    candidate_offset: int | None
    examples: list[dict]
    text: str

InRowKeysNT = namedtuple('InRowKeysNT', ['key', 'idx', 'offset'])
in_row_key_cols = InRowKeysNT._fields[1:]
def mk_key(in_r: InRow) -> InRowKeysNT:
    idx = in_r['idx']
    offset = in_r['offset']
    return InRowKeysNT(
        key=f'{idx}/{offset}',
        idx=idx,
        offset=offset,
    )
## END PRELUDE: Types ##


app = typer.Typer()


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


async def make_request(
    prompt: str,
    icl_shots: list[tuple[str, str]],
    api: tuple[str, AsyncOpenAI],
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
    gen_msg_contents = filter(None, (o.message.content for o in response.choices))
    return list(gen_msg_contents), response.usage


async def process_item(
    in_row: InRow,
    icl_shots: list[tuple[str, str]],
    semaphore: asyncio.Semaphore,
    api: ModelHandle,
):
    key_data = mk_key(in_row)
    try:
        async with semaphore:
            response_strs, usage = await make_request(
                prompt=make_prompt(in_row['text']),
                icl_shots=icl_shots,
                api=api,
            )
        response_num = len(response_strs)
        if response_num > 1:
            logger.warning(
                'Expected only 1 response, got {} at: {}',
                response_num,
                key_data.key,
            )
        r = {
            # r[k]: key_data[i] for i, k in enumerate(InRowKeysNT._fields[1:], 1)
            'idx': key_data.idx,
            'offset': key_data.offset,
            'response': response_strs[0],
        }

        return r, usage
    except Exception:
        logger.exception('Exn at prompt {}', key_data.key)
        return None


# openai_model = 'gpt-4.1-mini'
openai_model = 'gpt-4o-mini'
async def async_main(
    icl: bool,
    use_openrouter: bool,
    overwrite_last_run: bool,
    range_start: int,
    range_size: int,
):
    api = make_model_handle(openai_model, use_openrouter)
    usage_counter = UsageCounter()

    if not overwrite_last_run:
        _, flow_outd, run_outd = step_dirs(__file__, has_runs=True)
    else:
        _, flow_outd, run_outd = step_dirs(__file__, has_runs=True, extend_run='last', force=True)
    substepd = Path(__file__).parent
    rsrc_d = substepd/'resources'/Path(__file__).stem

    rsrc_icl_shots_d = rsrc_d/'icl'

    dep_f = flow_outd/'ai_extraction_prep/sliced_reasoning/result.jsonl'

    out_config_f = run_outd/'config.json'
    out_f = run_outd/'result.jsonl'

    icl_shots = []
    if icl:
        _icl_dirs = []
        for d in rsrc_icl_shots_d.iterdir():
            if not d.is_dir():
                continue
            _icl_dirs.append(d)
        _icl_dirs.sort(key=lambda d: d.name)
        for d in _icl_dirs:
            shot_prompt = make_prompt((d/'input_snippet.txt').read_text())
            shot_response = (d/'sample_output.txt').read_text()
            icl_shots.append((shot_prompt, shot_response))

    out_config_f.write_text(ser.json.dumps({
        'openai_model': openai_model,
        'range_start': range_start,
        'range_size': range_size,
        'use_icl': icl,
    }))

    def gen_ds_wanted_rows():
        for in_r in ser.jsonl_streamf(
            dep_f,
            start=range_start,
            end=range_start+range_size if range_size >= 0 else -1,
        ):
            in_r = cast(InRow, in_r)
            if (not in_r['examples']):
                continue
            yield in_r

    semaphore = asyncio.Semaphore(20)
    tasks = []
    with out_f.open('w') as out_fh:
        for in_r in gen_ds_wanted_rows():
            t = asyncio.create_task(process_item(in_r, icl_shots, semaphore, api))
            tasks.append(t)

        for t in tqdm(asyncio.as_completed(tasks), total=len(tasks)):
            req_res = await t
            if not req_res:
                continue
            resp, usage = req_res
            print(ser.json.dumps(resp), file=out_fh)
            _count_usage(usage_counter, usage)
    logger.success('Wrote: {}', cwd_rel(out_f))

    _log_usage(usage_counter)


@app.command()
def main(
    icl: bool = True,
    use_openrouter: bool = False,
    overwrite_last_run: bool = False,
    range_start: int = 0,
    range_size: int = -1,
):
    asyncio.run(async_main(
        icl=icl,
        use_openrouter=use_openrouter,
        overwrite_last_run=overwrite_last_run,
        range_start=range_start,
        range_size=range_size,
    ))


if __name__ == '__main__':
    app()
