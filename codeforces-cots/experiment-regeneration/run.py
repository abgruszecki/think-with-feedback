import datetime
import io
import json
import os
import sys
from pathlib import Path
from typing import Annotated, Literal

import httpx
import openai
import typer


type ApiEndpointKind = Literal['openrouter', 'fireworks',]


app = typer.Typer()

timestamp = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
root_outd = Path('out')


def prepare_outf(variant: str, api: ApiEndpointKind):
    tag = ''
    tag += f'+{api}'
    outd = root_outd / f'{timestamp}--r1-{variant}{tag}'
    outd.mkdir(parents=True, exist_ok=True)
    outf = outd / 'results.jsonl'
    return outf


def make_client(api: ApiEndpointKind):
    if api == 'openrouter':
        base_url = 'https://openrouter.ai/api/v1'
        key_env_var = 'OPENROUTER_API_KEY'
    elif api == 'fireworks':
        base_url = 'https://api.fireworks.ai/inference/v1'
        key_env_var = 'FIREWORKS_API_KEY'
    else:
        raise ValueError(f'Unknown API endpoint: {api}')
    return openai.OpenAI(
        base_url=base_url,
        api_key=os.environ[key_env_var],
    )


def make_messages(variant: str):
    messages = []

    # messages.extend([
    #     {'role': 'system', 'content': system_msg},
    # ])

    prompt = (Path(f'data/request-{variant}/prompt.md')).read_text()
    messages.extend([
        {'role': 'user', 'content': prompt},
    ])

    return messages

def gen_response(messages, api: ApiEndpointKind, client: openai.OpenAI):
    if api == 'openrouter':
        model='deepseek/deepseek-r1:free'
    elif api == 'fireworks':
        model='accounts/fireworks/models/deepseek-r1'
    else:
        raise ValueError(f'Unknown API endpoint: {api}')
    api_response = client.chat.completions.create(
        model=model,
        messages=messages,
        timeout=httpx.Timeout(5*60), # NOTE raw floats don't work
    )
    # TODO some validation. Sometimes reasoning is empty. Why?
    return api_response.choices[0].message


# Print or save the response
def print_msg(msg, file=None):
    # TODO this field is not there in responses from Fireworks
    if hasattr(msg, 'reasoning') and msg.reasoning:
        print('<think>', file=file)
        print(msg.reasoning, file=file)
        print('</think>', file=file)
    else:
        # TODO handle this in gen_response?
        print('Missing field in the API response: message.reasoning', file=sys.stderr)
    print(msg.content, file=file)


@app.command()
def main(
    variant: str,
    count: Annotated[int, typer.Option(help='Number of requests to make')],
    api: Annotated[str, typer.Option(help='API endpoint to use')],
    loud: bool = False,
):
    if api not in ('openrouter', 'fireworks'):
        raise typer.BadParameter(f'--api can be one of {", ".join(("openrouter", "fireworks"))}; got: `{api}`')
    client = make_client(api)
    outf = prepare_outf(variant, api)
    messages = make_messages(variant)
    with open(outf, 'w') as outf_fh:
        for i in range(count):
            msg = gen_response(messages, api=api, client=client)
            if loud:
                print(f'== STEP {i} ==')
                print_msg(msg, sys.stdout)
            str_out = io.StringIO()
            print_msg(msg, str_out)
            msg = str_out.getvalue()
            r = {
                'idx': i,
                'message': msg,
            }
            json.dump(r, outf_fh); outf_fh.write('\n')
            outf_fh.flush()

            # variant-0 is for debugging
            if variant == 'variant-0':
                debugf = outf.parent / f'step-{i}.json'
                with open(debugf, 'w') as debugf_fh:
                    json.dump(msg, debugf_fh)


if __name__ == '__main__':
    app()
