#!/usr/bin/env python3
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


base_tag_suffix = '+checkables'
tag_suffix = base_tag_suffix+'+4o-mini+nocode'
# TODO consider: assert environ.get('STEP_TAG') in (None, 'checkables')
# if _tagname := environ.get('STEP_TAG'):
#     tag_suffix = '+'+_tagname
flowd = Path(__file__).parent
flow_outd = flowd/'out'
dep_f = flow_outd/f'extract_simulation_snippets{base_tag_suffix}/result.jsonl'

run_outd = flow_outd/f'extract_simulation_cases{tag_suffix}'/datetime.now().strftime('%Y%m%dT%H%M%S')
run_outd.mkdir(parents=True, exist_ok=True)
out_prompts_f = run_outd/'prompts.jsonl'
out_res_f = run_outd/'result.jsonl'

openai_model = 'gpt-4o-mini'

PROMPT_TEMPLATE =\
'''\
The user is solving a competetive programming problem and and put their reasoning in text.

```text
{reasoning}
```
{examples_header}\
{formatted_examples}\
{instructions}\
'''

INSTRUCTIONS=\
'''\

# Instructions
The text is reasoning about a Python program which reads from the standard input and writes to the standard output. \
The text fragment may predict what output the program produces on some inputs. \
Your task is to find those input and output predictions in the text, \
and extract information from them into this JSON format:
```json
[
    {
            "source_sample_id": <int or null>,
            "input": <str or null>,
            "output": <str or null>,
            "is_correct": <bool or null>,
    },
    ...
]
```

You can output many predictions, or none.

The user may say the prediction is for an input/output pair sample from the problem statement, \
for instance by starting the prediction with "For example, sample/example 3:". \
In that case, set the `source_sample_id` to the sample id, \
otherwise set it to null.

If the prediction doesn't directly specify the input or the output, \
then use null for the `input` and `output` fields. \
For instance, do this if the prediction just says "the output is correct", \
or only starts with "Let's consider n=3" without saying what the standard input is.

If the text directly says the output is correct or incorrect, \
then set the `is_correct` field appropriately, \
otherwise leave it null.
'''

EXAMPLES_HEADER=\
'''\

Here are some samples of what inputs and outputs should look like for the problem the user is solving:
'''

ONE_EXAMPLE_TEMPLATE=\
'''\
```json
{formatted_json}
```
'''


def make_prompt(
    reasoning: str,
    examples: list[dict],
) -> str:
    examples_header = ''
    formatted_examples = ''
    if examples:
        examples_header = EXAMPLES_HEADER
        formatted_examples = ''.join(
            ONE_EXAMPLE_TEMPLATE.format(
                formatted_json=json.dumps(e, indent=4)
            )
            for e in examples
        )
    return PROMPT_TEMPLATE.format(
        reasoning=reasoning,
        instructions=INSTRUCTIONS,
        examples_header=examples_header,
        formatted_examples=formatted_examples,
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


def test_openai():
    from openai import OpenAI
    client = OpenAI()
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'user', 'content': 'Hello, world!'},
        ],
    )
    print(response.choices[0].message.content)

async def async_main(
    partial_run: bool = True,
    use_fireworks: bool = False,
):
    if use_fireworks:
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
    used_total_toks = 0 # we can use this to make sure things add up

    prompts = []
    with open(out_prompts_f, 'w') as prompts_fh:
        for in_r in jsonl_streamf(dep_f):
            r = { k: in_r[k] for k in ('idx', 'offset') }
            r_inputs = r['inputs'] = {}
            r_inputs['reasoning'] = in_r['text'][:3000]
            r_inputs['examples']  = in_r['examples']
            r['prompt'] = make_prompt(**r_inputs)
            prompts.append(r)
            print(json.dumps(r), file=prompts_fh)
    logger.success('Wrote: {}', out_prompts_f.relative_to(flowd))

    semaphore = asyncio.Semaphore(20)
    tasks = []
    with open(out_res_f, 'w') as res_fh:
        for i, in_r in enumerate(prompts):
            if partial_run and i % 8 != 0:
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

    if openai_model != 'gpt-4o-mini':
        logger.warning('Used a different model than expected, costs may be off.')
    input_tok_price = 0.15/1e6
    output_tok_price = 0.6/1e6
    usage_cost = (used_prompt_toks*input_tok_price) + (used_compl_toks*output_tok_price)
    logger.success('Usage cost: ${:.2f}', usage_cost)


@app.command()
def main(
    # Keep in sync with async_main ( typer doesn't allow async commands :( )
    partial_run: bool = True,
    use_fireworks: bool = False,
):
    # TODO ask Sonnet to check with reflection that main, async_main are in sync?
    asyncio.run(async_main(
        partial_run=partial_run,
        use_fireworks=use_fireworks,
    ))


if __name__ == '__main__':
    app()
