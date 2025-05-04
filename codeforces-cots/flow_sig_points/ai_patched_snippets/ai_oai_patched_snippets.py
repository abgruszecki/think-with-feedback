#!/usr/bin/env python3
"""
NOTE the idea is that this script can actually have various predecessors,
which adapt the output of previous steps for this script.
"""
from collections import namedtuple
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from os import environ
import asyncio
from pathlib import Path
import re
from typing import Annotated, Any, Callable, Iterable, Iterator, TypedDict, cast

from loguru import logger
import typer
from tqdm import tqdm
from openai import AsyncOpenAI
from openai.types.completion_usage import CompletionUsage

from py_shared import ser
from py_shared.code_finder import find_final_answer_block
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
        # defensive programming here we go...
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
## END PRELUDE: OpenAI API ##


## PRELUDE: Prompt ##
TEMPLATE = \
'''\
# User's original notes
{cot_snippet}

# Execution simulation snippets in the notes
{simulation_snippets}

# Unit test with result
```python
{unit_test_code}
```

Exit code:
```
{unit_test_exit_code}
```

Output:
```
{unit_test_output}
```

# Instructions
The user wrote notes when solving about a competetive programming problem. \
In these notes, the user was simulating how a program would run. \
Snippets with such simulations were extracted from the notes into XML tags. \
Later, the user wrote a test script mirroring some of the extracted simulations. \

We're writing a new version of the notes, which starts with the test script and its result. \
Your task is to make minimal adjustments to the notes, to replace the simulation snippets \
with conclusions from the test script and its result. \
Put `<test-with-result/>` in your adjusted notes to mark where the test script and its result should go. \
Make sure to carefully preserve as much of the original text as possible. \
Only replace the simulation parts which we've extracted into the XML tags. \
Start your adjusted notes with this header: `# Adjusted notes`.
'''


def make_prompt(
    cot_snippet: str,
    simulation_snippets: str,
    unit_test_code: str,
    unit_test_exit_code: int,
    unit_test_output: str,
) -> str:
    return TEMPLATE.format(
        cot_snippet=cot_snippet,
        simulation_snippets=simulation_snippets,
        unit_test_code=unit_test_code,
        unit_test_exit_code=unit_test_exit_code,
        unit_test_output=unit_test_output,
    )
## END PRELUDE: Prompt ##


app = typer.Typer()


acceptable_failure_rx = re.compile(r'test\b.*\bfail', re.IGNORECASE)
thinks_end_rx = re.compile(r'\n*</think>')
keycols = ('idx', 'offset')
# openai_model = 'gpt-4o-mini'
openai_model = 'gpt-4.1-mini'


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


def find_code(
    response: str,
    log_key: Any,
) -> str | None:
    code_str = find_final_answer_block(response, offset=0)
    if code_str is None:
        logger.error('Unexpected: no code block found in the response (at {!r})', log_key)
        return None
    code_str = code_str.strip()
    if not code_str:
        raise ValueError('No code found in the response')
    return code_str


def gen_prompt_rows(
    data_rows: Iterable[dict],
    cot_rows: Iterable[dict],
) -> Iterator[dict]:
    def _gen_cot_kvs():
        for in_r in cot_rows:
            key_tup = tuple(in_r[k] for k in keycols)
            yield key_tup, in_r
    cot_rows_by_key = dict(_gen_cot_kvs())

    for data_r in data_rows:
        key_tup = tuple(data_r[k] for k in keycols)
        key = '/'.join(map(str, key_tup))
        status: str = data_r['status']
        if status == 'fail:timeout':
            continue
        stdout: str = data_r['stdout']
        exit_code = 0
        if status.startswith('fail:'):
            exit_code = 1
            if not acceptable_failure_rx.search(stdout):
                continue

        code_synth_response: str = data_r['response']
        code = find_code(code_synth_response, key)
        if code is None:
            continue

        cot_snippet = cot_rows_by_key[key_tup]['text']
        if m := thinks_end_rx.search(cot_snippet):
            cot_snippet = cot_snippet[:m.start()]

        sim_snippets = data_r['inputs']['simulations']

        r = { k: data_r[k] for k in keycols }
        r['inputs'] = inputs = {
            'cot_snippet': cot_snippet,
            'simulation_snippets': sim_snippets,
            'unit_test_code': code,
            'unit_test_exit_code': exit_code,
            'unit_test_output': stdout,
        }
        r['prompt'] = make_prompt(**inputs)
        yield r


async def process_prompt_row_(
    in_r,
    semaphore,
    api: ModelHandle,
    icl_shots: list[tuple[str, str]] = [],
) -> tuple[dict, CompletionUsage | None] | None:
    prompt_fn = lambda r: r['prompt']
    res = await process_prompt_row(
        in_row=in_r,
        semaphore=semaphore,
        api=api,
        key_fn=lambda r: '/'.join(str(r[k]) for k in keycols),
        prompt_fn=prompt_fn,
        icl_shots=icl_shots,
    )
    if res is None:
        return None

    in_r, response, usage = res
    r = { k: in_r[k] for k in keycols }
    r['inputs'] = in_r['inputs']
    r['prompt'] = in_r['prompt']
    r['response'] = response
    return r, usage


marker_tag_rx = re.compile(r'\n?\n?<test-with-result/>\n?\n?')
def replace_marker_tag(
    response: str,
    test_code: str,
    test_exit_code: int,
    test_output: str,
) -> str:
    import io
    b = io.StringIO()

    m = marker_tag_rx.search(response)
    if m is None:
        # TODO warn?
        return response
    b.write(response[:m.start()])
    b.write('\n\n```python\n')
    b.write(test_code)
    if test_code[-1] != '\n':
        b.write('\n')
    b.write('```\n\n')
    b.write('<run-test/>\n\n')
    print('Exit code: ', test_exit_code, '. Output:', sep='', file=b)
    b.write('```\n')
    b.write(test_output)
    if test_output[-1] != '\n':
        b.write('\n')
    b.write('```\n\n')
    b.write(response[m.end():])
    return b.getvalue()


async def async_main(
    input_checks_run_dir: Path,
    range_start: int,
    range_size: int,
    use_icl: bool,
    use_openrouter: bool,
):
    input_checks_report_file = input_checks_run_dir/'verify/result.jsonl'

    api = make_model_handle(openai_model, use_openrouter)
    usage_counter = UsageCounter()

    _, flow_outd, step_outd = step_dirs(__file__, has_runs=True)
    subflowd = Path(__file__).parent
    rsrc_d = subflowd/'resources'/Path(__file__).stem
    logger.add(step_outd/'logs.txt')

    rsrc_icl_f = rsrc_d/'icl.json'
    dep_cots_f = flow_outd/'ai_extraction_prep/sliced_reasoning/result.jsonl'

    out_config_f = step_outd/'config.json'
    out_icl_f = step_outd/'icl.jsonl'
    out_prompts_f = step_outd/'prompts.jsonl'
    out_f = step_outd/'result.jsonl'

    config = {
        'openai_model': openai_model,
        'use_openrouter': use_openrouter,
        'input_checks_run_dir': str(input_checks_run_dir),
        'range_start': range_start,
        'range_size': range_size,
        'use_icl': use_icl,
    }
    ser.json_dumpf(config, out_config_f)
    logger.info('Wrote step config: {}', cwd_rel(out_config_f))

    if use_icl:
        icl_data = ser.json_loadf(rsrc_icl_f)
        icl_shots = [( make_prompt(**r['inputs']), r['response'] ) for r in icl_data[:3]]
        ser.jsonl_dumpf(
            [{ 'prompt': p, 'response': r } for p, r in icl_shots ],
            out_icl_f,
        )
    else:
        icl_shots = []

    prompts = list(gen_prompt_rows(
        data_rows=ser.jsonl_streamf(input_checks_report_file),
        cot_rows=ser.jsonl_streamf(dep_cots_f),
    ))
    ser.jsonl_dumpf(prompts, out_prompts_f)
    logger.success('Wrote: {}', cwd_rel(out_prompts_f))

    semaphore = asyncio.Semaphore(20)
    with open(out_f, 'w') as out_fh:
        tasks = [
            asyncio.create_task(process_prompt_row_(in_r, semaphore, api, icl_shots=icl_shots))
            for in_r in islice(prompts, range_start, range_start+range_size if range_size >= 0 else None)
        ]

        for t in tqdm(asyncio.as_completed(tasks), total=len(tasks)):
            out = await t
            if out is None:
                continue
            r, usage = out
            _count_usage(usage_counter, usage)
            print(ser.json.dumps(r), file=out_fh)
    logger.success('Wrote: {}', cwd_rel(out_f))
    _log_usage(usage_counter)


InputDirOption = typer.Option(exists=True, file_okay=False, dir_okay=True, readable=True)
@app.command()
def main(
    input_run: Annotated[Path, InputDirOption],
    range_start: int = 0,
    range_size: int = -1,
    use_icl: bool = True,
    use_openrouter: bool = False,
):
    asyncio.run(async_main(
        input_checks_run_dir=input_run,
        range_start=range_start,
        range_size=range_size,
        use_icl=use_icl,
        use_openrouter=use_openrouter,
    ))


if __name__ == '__main__':
    app()
