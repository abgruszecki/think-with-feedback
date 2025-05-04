#!/usr/bin/env python3
from collections import namedtuple
from datetime import datetime
from os import environ
import json
from pathlib import Path
import asyncio

from loguru import logger
import typer
from tqdm import tqdm
from openai import AsyncOpenAI
from openai.types.chat.chat_completion import CompletionUsage


def jsonl_streamf(pathlike):
    with open(pathlike, 'r') as fh:
        for line in fh:
            yield json.loads(line)


app = typer.Typer()


flowd = Path(__file__).parent
flow_outd = flowd/'out'
dep_f = flow_outd/f'extract_simulation_snippets/result.jsonl'

run_outd = flow_outd/f'extract_simulation_cases'/datetime.now().strftime('%Y%m%dT%H%M%S')
out_prompts_f = run_outd/'prompts.jsonl'
out_res_f = run_outd/'result.jsonl'

openai_model = 'gpt-4o-mini'

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
The user is reasoning about a Python program which reads from the standard input and writes to the standard output. \
The reasoning text fragment may predict what output the program produces on some inputs. \
Your task is to find those input and output predictions in the text, \
and extract information from them into this JSON format:
```json
[
    {
            "input": <str or null>,
            "output": <str or null>,
    },
    ...
]
```

You can output many predictions, or none.

If the prediction doesn't directly specify the input or the output, \
then use null for the `input` and `output` fields. \
For instance, do this if the prediction just says "the output is correct", \
or only starts with "Let's consider n=3" without saying what the standard input is.
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


async def make_request(
    prompt: str,
    api: tuple[str, AsyncOpenAI],
) -> tuple[list[str], CompletionUsage|None]:
    message = [{'role': 'user', 'content': prompt}]
    model, client = api
    response = await client.chat.completions.create(
        model=model,
        messages=message,
    )
    return [o.message.content for o in response.choices], response.usage


async def process_prompt(in_r, semaphore, api: tuple[str, AsyncOpenAI]):
    async with semaphore:
        try:
            response_strs, usage = await make_request(
                prompt=in_r['prompt'],
                api=api,
            )
            for response_idx, response_str in enumerate(response_strs):
                r = {
                    'idx': in_r['idx'],
                    'offset': in_r['offset'],
                    'n': response_idx,
                    'response': response_str,
                }
                return r, usage
        except Exception:
            logger.exception('Exn at prompt {}/{}', in_r['idx'], in_r['offset'])
            return None


_pricing_nt = namedtuple('pricing_nt', ['input_tok', 'output_tok'])
pricings = {
    'gpt-4o-mini': _pricing_nt(input_tok=0.15/1e6, output_tok=0.6/1e6),
    'gpt-4.1-mini': _pricing_nt(input_tok=0.4/1e6, output_tok=1.6/1e6),
}
def total_cost(
    model: str,
    used_prompt_toks: int,
    used_compl_toks: int,
) -> float | None:
    pricing = pricings.get(model)
    if not pricing:
        return None
    return sum((
        used_prompt_toks*pricing.input_tok,
        used_compl_toks*pricing.output_tok,
    ))


async def async_main(
    partial_run: bool,
    use_openrouter: bool,
):
    if use_openrouter:
        model = 'openai/'+openai_model
        base_url='https://openrouter.ai/api/v1'
        api_key=environ['OPENROUTER_API_KEY']
    else:
        model = openai_model
        base_url = None
        api_key = None

    client = AsyncOpenAI(
        base_url=base_url,
        api_key=api_key,
    )
    api = (model, client)
    used_prompt_toks = 0
    used_compl_toks = 0
    used_total_toks = 0 # used to make sure the costs add up

    run_outd.mkdir(parents=True, exist_ok=True)

    prompts = []
    with open(out_prompts_f, 'w') as prompts_fh:
        for in_r in jsonl_streamf(dep_f):
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
            r['prompt'] = make_prompt(**r_inputs)
            prompts.append(r)
            print(json.dumps(r), file=prompts_fh)
    logger.success('Wrote: {}', out_prompts_f.relative_to(flowd))

    semaphore = asyncio.Semaphore(20)
    tasks = []
    with open(out_res_f, 'w') as res_fh:
        for i, in_r in enumerate(prompts):
            if partial_run and i % 8 != 0:
                # TODO: should a partial run be "just" c. 100 rows?
                continue
            task = asyncio.create_task(process_prompt(in_r, semaphore, api))
            tasks.append(task)

        for f in tqdm(asyncio.as_completed(tasks), total=len(tasks)):
            out = await f
            if out is None:
                continue
            r, usage = out
            if usage:
                used_prompt_toks += usage.prompt_tokens
                used_compl_toks += usage.completion_tokens
                used_total_toks += usage.total_tokens
            else:
                logger.warning('Got usage=None, costs will be off')
            print(json.dumps(r), file=res_fh)

    used_total_toks_check = sum([used_prompt_toks, used_compl_toks])
    if used_total_toks != used_total_toks_check:
        logger.warning('Token usage does not add up (cache or reasoning?): {} != {}', used_total_toks, used_total_toks_check)

    usage_cost = total_cost(
        openai_model,
        used_prompt_toks,
        used_compl_toks,
    )
    if usage_cost:
        logger.success('Usage cost: ${:.2f}', usage_cost)
    else:
        usage_dict = {
            'prompt': used_prompt_toks,
            'compl': used_compl_toks,
            'total': used_total_toks,
        }
        logger.warning(
            'Unknown costs, since model is unknown: model={}, usage={!r}',
            openai_model,
            usage_dict,
        )


@app.command()
def main(
    # Keep in sync with async_main ( typer doesn't allow async commands :( )
    partial_run: bool = True,
    use_openrouter: bool = False,
):
    # TODO ask Sonnet to check with reflection that main, async_main are in sync?
    asyncio.run(async_main(
        partial_run=partial_run,
        use_openrouter=use_openrouter,
    ))


if __name__ == '__main__':
    app()
