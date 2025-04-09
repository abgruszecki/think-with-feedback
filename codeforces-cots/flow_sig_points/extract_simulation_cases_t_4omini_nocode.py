#!/usr/bin/env python3
from datetime import datetime
from os import environ
import json
from pathlib import Path
import asyncio

from loguru import logger
from tqdm import tqdm
from openai import AsyncOpenAI


def jsonl_streamf(pathlike):
    with open(pathlike, 'r') as fh:
        for line in fh:
            yield json.loads(line)


tag = '+4o-mini+nocode'
if _tagname := environ.get('STEP_TAG'):
    tag = '+'+_tagname
flowd = Path(__file__).parent
flow_outd = flowd/'out'
dep_f = flow_outd/'extract_simulation_snippets/result.jsonl'

run_outd = flow_outd/f'extract_simulation_cases{tag}'/datetime.now().strftime("%Y%m%dT%H%M%S")
run_outd.mkdir(parents=True, exist_ok=True)
out_prompts_f = run_outd/'prompts.jsonl'
out_res_f = run_outd/'result.jsonl'

PROMPT_TEMPLATE =\
'''\
The user is solving a competetive programming problem and and put their reasoning in text.

```text
{reasoning}

```

{instructions}\
{examples_header}\
{formatted_examples}\
'''

INSTRUCTIONS=\
'''\
The text is reasoning about a Python program which reads from the standard input and writes to the standard output. \
The text fragment should start by predicting what output the program produces on some inputs. \
Your task is to find those input and output predictions in the text, and put them into this JSON format:
```json
{
    "prediction-count": <int>,
    "predictions": [
        {
            "input": <str>,
            "output": <str>,
        },
        ...
    ]
}
```
'''

EXAMPLES_HEADER=\
'''\

Here are some examples of what inputs and outputs should look like for the problem the user is solving:
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
    model: AsyncOpenAI,
) -> list[str]:
    message = [{'role': 'user', 'content': prompt}]
    responses = await model.chat.completions.create(
        model='gpt-4o-mini',
        messages=message,
    )
    return [o.message.content for o in responses.choices]


async def process_prompt(in_r, semaphore, client):
    async with semaphore:
        try:
            response_strs = await make_request(
                prompt=in_r['prompt'],
                model=client,
            )
            for response_idx, response_str in enumerate(response_strs):
                r = {
                    'idx': in_r['idx'],
                    'offset': in_r['offset'],
                    'n': response_idx,
                    'response': response_str,
                }
                return r
        except Exception:
            logger.exception('Exn at prompt {}/{}', in_r['idx'], in_r['offset'])
            return None

async def main():
    client = AsyncOpenAI()

    prompts = []
    with open(out_prompts_f, 'w') as prompts_fh:
        for in_r in jsonl_streamf(dep_f):
            if not in_r['code']:
                continue
            r = { k: in_r[k] for k in ('idx', 'offset') }
            r_inputs = r['inputs'] = {}
            r_inputs['reasoning'] = in_r['text'][:3000]
            r_inputs['examples']  = in_r['examples']
            r['prompt']    = make_prompt(**r_inputs)
            prompts.append(r)
            print(json.dumps(r), file=prompts_fh)

    semaphore = asyncio.Semaphore(20)
    tasks = []
    with open(out_res_f, 'w') as res_fh:
        for i, in_r in enumerate(prompts):
            if i % 25 != 0:
                continue
            task = asyncio.create_task(process_prompt(in_r, semaphore, client))
            tasks.append(task)

        for f in tqdm(asyncio.as_completed(tasks), total=len(tasks)):
            r = await f
            if r is None:
                continue
            print(json.dumps(r), file=res_fh)


if __name__ == '__main__':
    asyncio.run(main())
