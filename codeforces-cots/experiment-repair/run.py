import asyncio
from dataclasses import dataclass
import datetime
import io
import json
import os
import sys
from pathlib import Path
from typing import Annotated, Literal

import openai
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletionMessage, ChatCompletionMessageParam
import typer
from loguru import logger


type ApiEndpointKind = Literal['openrouter', 'fireworks',]
API_ENDPOINTS: list[ApiEndpointKind] = ['openrouter', 'fireworks']


@dataclass
class ResponseData:
    message: ChatCompletionMessage
    idx: int
    num_requests: int


app = typer.Typer()

timestamp = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
root_outd = Path('out')

system_msg = """\
During this conversation, you can execute Python snippets. \
When you are uncertain if your code is correct, \
write it together with some tests in a code block, and say RUN_SNIPPET.
You will see the output of the snippet in a Markdown code block, like this:

```python
print("Hello, world!")
```

RUN_SNIPPET
```text
Hello, world!
```\
"""


def prepare_outf(variant: str, no_icl: bool, api: ApiEndpointKind):
    tag = ''
    tag += f'+{api}'
    if no_icl:
        tag = '+no-icl'
    outd = root_outd / f'{timestamp}--r1-{variant}{tag}'
    outd.mkdir(parents=True, exist_ok=True)
    outf = outd / 'results.jsonl'
    return outf


def make_client(api: ApiEndpointKind) -> AsyncOpenAI:
    if api == 'openrouter':
        base_url = 'https://openrouter.ai/api/v1'
        key_env_var = 'OPENROUTER_API_KEY'
    elif api == 'fireworks':
        base_url = 'https://api.fireworks.ai/inference/v1'
        key_env_var = 'FIREWORKS_API_KEY'
    else:
        raise ValueError(f'Unknown API endpoint: {api}')
    return AsyncOpenAI(
        base_url=base_url,
        api_key=os.environ[key_env_var],
    )


def make_messages(variant: str, no_icl: bool) -> list[ChatCompletionMessageParam]:
    messages: list[ChatCompletionMessageParam] = []

    messages.extend([
        {'role': 'system', 'content': system_msg},
    ])

    if not no_icl:
        for shot_id in ['418', '304', '486', '268', '641']:
            shotd = Path(f'data/icl-shots/{shot_id}')
            messages.extend([
                {'role': 'user', 'content': (shotd / 'prompt.md').read_text()},
                {'role': 'assistant', 'content': (shotd / 'response.md').read_text()},
            ])

    prompt = (Path(f'data/request-{variant}/prompt.md')).read_text()
    messages.extend([
        {'role': 'user', 'content': prompt},
    ])

    partial_output_path = Path(f'data/request-{variant}/partial-output.md')
    if partial_output_path.exists():
        partial_output = partial_output_path.read_text()
        messages.extend([
            {'role': 'assistant', 'content': partial_output},
        ])

    return messages


async def gen_response(
    messages: list[ChatCompletionMessageParam],
    api: ApiEndpointKind,
    sem: asyncio.Semaphore,
    client: AsyncOpenAI,
    request_idx: int,
) -> ResponseData:
    if api == 'openrouter':
        model='deepseek/deepseek-r1:free'
    elif api == 'fireworks':
        # basic is the same except slower/cheaper
        model='accounts/fireworks/models/deepseek-r1-basic'
    else:
        raise ValueError(f'Unknown API endpoint: {api}')

    if api == 'openrouter':
        async with sem: # critical section
            api_response = await client.chat.completions.create(
                model=model,
                messages=messages,
                timeout=5*60,
            )
        # TODO some validation. Sometimes reasoning is empty. Why?
        return ResponseData(
            message=api_response.choices[0].message,
            idx=request_idx,
            num_requests=1,
        )
    elif api == 'fireworks':
        messages_acc: list[ChatCompletionMessageParam] = messages.copy()
        response_messages = []
        want_thinks = True
        want_code = True
        import re
        # NOTE these work, the responses can stop in the middle of a code block,
        # it seems they're continued char-by-char.
        # TODO ...what happens if the code block itself gets interrupted?
        # TODO should I instead work with an incrementally accumulated response?
        thinks_end_rx = re.compile(r'</think>')
        # TODO look for opening and closing fences
        code_end_rx = re.compile(r'```\n')
        num_requests = 0
        for i in range(20): # TODO make this a constant
            async with sem: # critical section
                api_response = await client.chat.completions.create(
                    model=model,
                    messages=messages_acc,
                    timeout=5*60,
                )
            num_requests += 1
            response_message = api_response.choices[0].message
            response_messages.append(response_message)
            messages_acc.append(response_message)

            content_str = str(response_message.content)
            offset = 0
            if want_thinks:
                # NOTE normal Fireworks responses do contain </think> tags
                if m := thinks_end_rx.search(content_str, offset):
                    offset = m.end()
                    want_thinks = False
            if not want_thinks and want_code:
                if m := code_end_rx.search(content_str, offset):
                    offset = m.end()
                    want_code = False

            if not want_thinks and not want_code:
                break
            else:
                logger.warning(f'Req {request_idx}: No answer yet ({i+1}/5), continuing...')

        return ResponseData(
            message=ChatCompletionMessage(
                content='\n\n<CONTINUE/>\n\n'.join([str(m.content) for m in response_messages]),
                role='assistant',
            ),
            idx=request_idx,
            num_requests=num_requests,
        )


# Log or save the response
def print_msg(msg, file=None):
    if hasattr(msg, 'reasoning') and msg.reasoning:
        print('<think>', file=file)
        print(msg.reasoning, file=file)
        print('</think>', file=file)
    else:
        # TODO handle this in gen_response?
        logger.warning('Missing field in the API response: message.reasoning')
    print(msg.content, file=file)


async def async_main(
    variant: str,
    count: int,
    api: ApiEndpointKind,
    no_icl: bool,
    loud: bool,
):
    client = make_client(api)
    outf = prepare_outf(variant, no_icl, api)
    messages = make_messages(variant, no_icl)

    sem = asyncio.Semaphore(10) # TODO make the concurrency degree a constant
    async def wrap(request_idx, future):
        try:
            return await future
        except Exception:
            logger.exception('== ERROR {} ==', request_idx)
            return None
    def do_gen_response(request_idx):
        return gen_response(messages, api=api, sem=sem, client=client, request_idx=request_idx)

    tasks = [wrap(idx, do_gen_response(idx)) for idx in range(count)]

    with open(outf, 'w') as outf_fh:
        for future in asyncio.as_completed(tasks):
            resp_data = await future
            if resp_data is None:
                continue
            idx = resp_data.idx

            str_out = io.StringIO()
            print_msg(resp_data.message, str_out)
            msg_str = str_out.getvalue()

            if loud:
                logger.info('== RESULT {} ==\n{}', idx, msg_str)
            else:
                logger.info('== RESULT {} ==', idx)

            r = {
                'idx': resp_data.idx,
                'num_requests': resp_data.num_requests,
                'message': msg_str,
            }
            json.dump(r, outf_fh); outf_fh.write('\n')
            outf_fh.flush()


@app.command()
def main(
    variant: str,
    count: Annotated[int, typer.Option(help='Number of requests to make')],
    api: Annotated[str, typer.Option(help='API endpoint to use')],
    no_icl: bool = False,
    loud: bool = False,
):
    if api not in API_ENDPOINTS:
        raise typer.BadParameter(f'--api must be one of: {", ".join(API_ENDPOINTS)}; was: {api}')
    # Typer doesn't directly support casting Literal from CLI args in async func
    # See https://github.com/tiangolo/typer/issues/411
    # Workaround: define an async inner function and call it via asyncio.run
    asyncio.run(async_main(variant, count, api, no_icl, loud))


if __name__ == '__main__':
    app()
