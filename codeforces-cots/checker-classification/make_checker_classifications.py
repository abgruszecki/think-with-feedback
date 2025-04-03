from datetime import datetime
from pathlib import Path
import json

from vllm import LLM, SamplingParams


def jsonl_streamf(pathlike):
    with open(pathlike, 'r') as fh:
        for line in fh:
            yield json.loads(line)


def jsonl_loadf(pathlike):
    return list(jsonl_streamf(pathlike))


root_outd = Path('./out')
root_outd.mkdir(parents=True, exist_ok=True)
outf = root_outd / '{timestamp}--raw-checker-classifications.jsonl'.format(
    timestamp=datetime.now().strftime('%Y%m%dT%H%M%S'),
)

input_data = jsonl_loadf('datasets/inputs.jsonl')

llm = LLM(
    str((Path.home()/'models/Qwen--QwQ-32B').absolute()),
    max_model_len=10240,
    gpu_memory_utilization=0.95,
)

sp = SamplingParams(
    n=4,
    temperature=0.9,
    top_p=0.95,
    max_tokens=1024,
)

def make_messages(r):
    return [{
        'role': 'user',
        'content': r['prompt'],
    }]

# 12 is already too much on 1 H100 at gpu_mem=0.95
batch_size = 10

with outf.open('w') as outf_fh:
    for i in range(0, len(input_data), batch_size):
        batch = input_data[i:i+batch_size]
        batch_responses = llm.chat([make_messages(r) for r in batch], sp)
        # batch_outputs = [g for r in batch_responses for g in r.outputs]

        # print(f'batch sz = {len(batch)}')
        # print(f'batch outputs sz = {len(batch_outputs)}')

        for in_row, resp in zip(batch, batch_responses):
            for gen_idx, gen in enumerate(resp.outputs):
                r = {
                    'idx': in_row['idx'],
                    'id': in_row['id'],
                    'gen_idx': gen_idx,
                    'prompt': in_row['prompt'],
                    'response': gen.text,
                }
                json.dump(r, outf_fh)
                print(file=outf_fh, flush=True)
