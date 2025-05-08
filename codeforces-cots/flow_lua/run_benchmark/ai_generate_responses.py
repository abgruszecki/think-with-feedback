#!/usr/bin/env python3
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Collection, Iterable, Iterator, cast

from loguru import logger
import typer
from tqdm import tqdm

from py_shared.code_finder import find_final_answer_block
import py_shared.flow as fl

app = typer.Typer()


## PRELUDE: vLLM API ##
# I think this'd be nicer if it was in a separate, late-imported module.
# That way, we'd only import vLLM (slow) just before we need it.
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


# (Qwen3) for non-thinking mode (enable_thinking=False), we suggest using Temperature=0.7, TopP=0.8, TopK=20, and MinP=0.
# TODO figure out a better way to determine the max token length.
# TODO this should be part of the model handle (as the default sampling params)
sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.8,
    top_k=20,
    min_p=0,
    max_tokens=24*1024,
)


@dataclass
class RequestData():
    prompt: str
    log_key: str

def make_request(
    data: list[RequestData],
    api: ModelHandle,
    icl_shots: list[tuple[str, str]] = [],
    system_prompts: list[str] = [],
) -> list[CompletionOutput]:
    base_messages = []
    for p in system_prompts:
        base_messages.append({'role': 'system', 'content': p})
    for shot_prompt, shot_response in icl_shots:
        base_messages.append({'role': 'user', 'content': shot_prompt})
        base_messages.append({'role': 'assistant', 'content': shot_response})
    message_lists = []
    for rd in data:
        messages = base_messages.copy()
        messages.append({'role': 'user', 'content': rd.prompt})
        message_lists.append(messages)

    responses: list[RequestOutput] = api.chat(
        messages=message_lists,
        use_tqdm=False,
        sampling_params=sampling_params,
    )

    # defensive coding yay...
    num_responses = len(responses)
    expected_num_responses = len(data)
    if num_responses != expected_num_responses:
        keys = [rd.log_key for rd in data]
        logger.error(
            "Error in code at keys: {!r}: expected {} RequestOutput, got {}. "
            "Responses will be mismatched with prompts.",
            keys,
            expected_num_responses,
            num_responses,
        )

    results: list[CompletionOutput] = []
    for (rd, response) in zip(data, responses):
        outputs = response.outputs
        num_outputs = len(outputs)
        if num_outputs != 1:
            logger.error("Error in code at key {!r}: expected 1 CompletionOutput, got {}. Using the 1st if any.", rd.log_key, num_outputs)
        if num_outputs == 0:
            continue
        results.append(outputs[0])

    return results


@dataclass
class ProcessPromptResult():
    output: str
    extras: dict

def process_prompts(
    data: list[RequestData],
    api: ModelHandle,
    icl_shots: list[tuple[str, str]] = [],
    system_prompts: list[str] = [],
) -> list[ProcessPromptResult]:
    # The reason we have both this function and make_request is that
    # in principle only make_request needs to change for different model backends (e.g. APIs).
    try:
        outputs = make_request(
            data=data,
            api=api,
            icl_shots=icl_shots,
            system_prompts=system_prompts,
        )

        results: list[ProcessPromptResult] = []
        for rd, o in zip(data, outputs):
            if o.finish_reason == 'length':
                logger.warning('Completion stopped due to length limit at key: {!r}', rd.log_key)
                # You might want to handle this differently, e.g., return None or raise an error
                # depending on whether a truncated response is acceptable.

            extras = {
                'finish_reason': o.finish_reason,
                'stop_reason': o.stop_reason,
            }
            results.append(ProcessPromptResult(
                output=o.text,
                extras=extras,
            ))

        return results
    except Exception:
        # TODO try unbatched processing at this point?
        # The exception could be because we exceeded the max token limit for one generation request.
        # In that case, processing the prompts individually would work.
        logger.exception('Exn at keys: {!r}', [rd.log_key for rd in data])
        return []
## END PRELUDE: vLLM API ##


def gen_batch_output_rows(
    in_rows_batch: Collection[dict], # I think Collection means it can be repeatedly iterated
    api: ModelHandle,
    icl_shots: list[tuple[str, str]] = [],
    system_prompts: list[str] = [],
) -> Iterator[dict]:
    """
    This function processes a batch of input rows into a batch of output rows.
    """
    # Technically dict access could throw. The proper way to prevent that is to use Pydantic.
    requests = [RequestData(
        prompt=r['prompt'],
        log_key=keycols.key(r, sep='/'),
    ) for r in in_rows_batch]
    res = process_prompts(
        data=requests,
        api=api,
        icl_shots=icl_shots,
        system_prompts=system_prompts,
    )

    for in_r, o in zip(in_rows_batch, res):
        r = keycols.kvs(in_r)
        r['prompt'] = in_r['prompt']
        r['response_meta'] = o.extras
        r['response'] = o.output
        yield r


keycols = fl.KeyCols(('idx',))

# model_ref = Path.home()/'models/Qwen3-32B'
# model_extra_kwargs: fl.JsonableDict = { 'max_model_len': 10240 }
# model_ref = Path.home()/'models/Qwen3-14B'
# model_extra_kwargs: fl.JsonableDict = {}
# model_ref = Path.home()/'models/Qwen3-8B'
# model_ref = 'Qwen/Qwen3-4B'
# model_extra_kwargs: fl.JsonableDict = {}
model_ref = 'Qwen/Qwen3-1.7B'
model_extra_kwargs: fl.JsonableDict = {}
# model_ref = Path.home()/'models/Qwen2p5-Coder-14B-Instruct'
# model_extra_kwargs: fl.JsonableDict = {}

@app.command()
def main(
    range_start: int = 0,
    range_size: int = -1,
    batch_size: int = 1,
):
    ctx = fl.dirs(__file__, has_runs=True)

    dep_f = ctx.flow_outd/'lua_prompts/result.jsonl'

    out_config_f = ctx.step_outd/'config.json'
    out_f = ctx.step_outd/'result.jsonl'

    config: fl.Jsonable = {
        'model_ref': str(model_ref),
        'model_extra_kwargs': model_extra_kwargs,
        'range_start': range_start,
        'range_size': range_size,
        'batch_size': batch_size,
    }
    fl.ser.json_dumpf(config, out_config_f)
    logger.info('Wrote step config: {}', fl.cwd_rel(out_config_f))

    api = make_model_handle(model_ref, model_extra_kwargs)

    start = range_start
    end = range_start+range_size if range_size >= 0 else -1
    data_size = range_size
    if range_size < 0:
        data_size = sum(1 for _ in fl.ser.jsonl_streamf(dep_f)) - start

    from itertools import batched
    out_rows_gen = (
        r
        for in_rows_batch in batched(
            tqdm(fl.ser.jsonl_streamf(dep_f, start=start, end=end), total=data_size),
            batch_size,
        )
        for r in gen_batch_output_rows(in_rows_batch, api)
    )
    fl.ser.jsonl_dumpf(out_rows_gen, out_f)
    logger.success('Wrote: {}', fl.cwd_rel(out_f))


if __name__ == '__main__':
    app()
