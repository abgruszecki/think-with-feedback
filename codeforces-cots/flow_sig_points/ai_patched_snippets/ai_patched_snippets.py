#!/usr/bin/env python3
"""
NOTE the idea is that this script can actually have various predecessors,
which adapt the output of previous steps for this script.

This script is intended to run on a single H100.
"""
from collections import namedtuple
from os import environ
from pathlib import Path
import re
from typing import Annotated, Any, Callable, Iterable, Iterator

from loguru import logger
import typer
from tqdm import tqdm

from py_shared import ser
from py_shared.code_finder import find_final_answer_block
from py_shared.misc import step_dirs, cwd_rel

type Jsonable = str|int|bool|list['Jsonable']|dict[str, 'Jsonable']
type JsonableDict = dict[str, Jsonable]


## PRELUDE: vLLM API ##
from vllm import LLM, RequestOutput, CompletionOutput, SamplingParams
type ModelHandle = LLM


def make_model_handle(
    model_path: str | Path,
    extra_kwargs: dict = {},
) -> ModelHandle:
    model = LLM(
        model=str(model_path),
        **extra_kwargs,
    )
    return model


# TODO figure out a better way to determine the max token length.
# For non-thinking mode (enable_thinking=False), we suggest using Temperature=0.7, TopP=0.8, TopK=20, and MinP=0.
sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.8,
    top_k=20,
    min_p=0,
    max_tokens=8*1024,
)


def make_request(
    prompt: str,
    api: ModelHandle,
    icl_shots: list[tuple[str, str]] = [],
    system_prompts: list[str] = [],
) -> CompletionOutput | None:
    messages = []
    for p in system_prompts:
        messages.append({'role': 'system', 'content': p})
    for shot_prompt, shot_response in icl_shots:
        messages.append({'role': 'user', 'content': shot_prompt})
        messages.append({'role': 'assistant', 'content': shot_response})
    messages.append({'role': 'user', 'content': prompt})

    responses: list[RequestOutput] = api.chat(
        messages=[messages],
        use_tqdm=False,
        sampling_params=sampling_params,
    )

    # defensive coding yay...
    num_responses = len(responses)
    if num_responses != 1:
        logger.error("Error in code: expected 1 RequestOutput, got {}. Using the 1st if any.", num_responses)
    if num_responses == 0:
        return None

    outputs = responses[0].outputs
    num_outputs = len(outputs)
    if num_outputs != 1:
        logger.error("Error in code: expected 1 CompletionOutput, got {}. Using the 1st if any.", num_outputs)
    if num_outputs == 0:
        return None

    return outputs[0]


def process_prompt_row(
    in_row: dict,
    api: ModelHandle,
    key_fn: Callable[[dict], str],
    prompt_fn: Callable[[dict], str],
    icl_shots: list[tuple[str, str]] = [],
    system_prompts: list[str] = [],
) -> tuple[dict, dict, str] | None:
    try:
        # defensive programming here we go...
        key = key_fn(in_row)
    except:
        logger.exception('Exn when getting key for row: {!r}', in_row)
        return None
    try:
        output = make_request(
            prompt=prompt_fn(in_row),
            api=api,
            icl_shots=icl_shots,
            system_prompts=system_prompts,
        )
        if not output:
            return None

        if output.finish_reason == 'length':
            logger.warning("Completion stopped due to length limit for key: {}", key)
            # You might want to handle this differently, e.g., return None or raise an error
            # depending on whether a truncated response is acceptable.

        extras = {
            'finish_reason': output.finish_reason,
            'stop_reason': output.stop_reason,
        }

        return in_row, extras, output.text
    except Exception:
        logger.exception('Exn at row: {}', key)
        return None
## END PRELUDE: OpenAI API ##


## PRELUDE: Prompt ##
TEMPLATE = \
'''\
We will write a new version of notes that the user wrote when \
working on a solution to a competitive programming problem. \
First, the context information.

# Script testing the user's code
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

# User's original notes
{cot_snippet}

# Execution simulation snippets in the notes
{simulation_snippets}

# Instructions
The user wrote notes when solving about a competetive programming problem. \
In these notes, the user was simulating how a program would run. \
These "simulation snippets" were extracted from the notes into XML tags, \
and a test script based on some of the extracted simulations was written. \

We're writing a new version of the notes, which starts with the test script and its result. \
Your task is to replace the simulation snippets with conclusions from the test script and its result, \
while carefully preserving as much of the original text as possible. \
Put `<test-with-result/>` in your adjusted notes to mark where the test script and its result should go. \
Only replace the simulation snippets which were extracted into the XML tags. \
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
thinks_end_rx = re.compile(r'\n*</think>\n*')
keycols = ('idx', 'offset')

model_ref = Path.home()/'models/Qwen3-32B'
model_extra_kwargs: JsonableDict = { 'max_model_len': 10240 }
# model_ref = Path.home()/'models/Qwen3-14B'
# model_extra_kwargs: JsonableDict = {}

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


def process_prompt_row_(
    in_r,
    api: ModelHandle,
    icl_shots: list[tuple[str, str]] = [],
    system_prompts: list[str] = [],
) -> dict | None:
    prompt_fn = lambda r: r['prompt']
    res = process_prompt_row(
        in_row=in_r,
        api=api,
        key_fn=lambda r: '/'.join(str(r[k]) for k in keycols),
        prompt_fn=prompt_fn,
        icl_shots=icl_shots,
        system_prompts=system_prompts,
    )
    if res is None:
        return None

    in_r, meta, response = res
    r = { k: in_r[k] for k in keycols }
    r['inputs'] = in_r['inputs']
    r['prompt'] = in_r['prompt']
    r['response_meta'] = meta
    r['response'] = response
    return r


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


def InputDirOption(decl):
    return typer.Option(..., decl, exists=True, file_okay=False, dir_okay=True, readable=True)
@app.command()
def main(
    input_checks_run_dir: Annotated[Path, InputDirOption('--input-run')],
    range_start: int = 0,
    range_size: int = -1,
    use_icl: int = 3,
):
    input_checks_report_file = input_checks_run_dir/'verify/result.jsonl'
    if not use_icl > -1:
        raise typer.BadParameter(f'--use-icl must be >= 0, was: {use_icl}')

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

    config: Jsonable = {
        'model_ref': str(model_ref),
        'model_extra_kwargs': model_extra_kwargs,
        'input_checks_run_dir': str(input_checks_run_dir),
        'range_start': range_start,
        'range_size': range_size,
        'use_icl': use_icl,
    }
    ser.json_dumpf(config, out_config_f)
    logger.info('Wrote step config: {}', cwd_rel(out_config_f))

    api = make_model_handle(model_ref, model_extra_kwargs)

    if use_icl:
        icl_data = ser.json_loadf(rsrc_icl_f)
        icl_shots = [( make_prompt(**r['inputs']), r['response'] ) for r in icl_data[:use_icl]]
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

    sys_prompts = ['/nothink'] # this disables Qwen3 thinking
    with open(out_f, 'w') as out_fh:
        start = range_start
        end = range_start+range_size if range_size >= 0 else None
        for in_r in tqdm(prompts[start:end]):
            r = process_prompt_row_(in_r, api, icl_shots=icl_shots, system_prompts=sys_prompts)
            if r is None:
                continue
            response = r['response']
            if m := thinks_end_rx.search(response):
                r['response'] = response[m.end():]
            print(ser.json.dumps(r), file=out_fh)
    logger.success('Wrote: {}', cwd_rel(out_f))


def _intr_explode_result(
    run_dir: Path,
):
    result_f = run_dir/'result.jsonl'
    assert result_f.exists()

    out_root = run_dir/'exploded'
    out_root.mkdir(parents=True, exist_ok=True)

    for r in ser.jsonl_streamf(result_f):
        key_filename = '_'.join(str(r[k]) for k in keycols)
        out_d = out_root/key_filename
        out_d.mkdir(exist_ok=True)
        (out_d/'prompt.md').write_text(r['prompt'])
        response = r['response']
        if m := thinks_end_rx.search(response):
            response = response[m.end():]
        (out_d/'response.md').write_text(response)


if __name__ == '__main__' and 'NOGO' not in environ:
    app()
