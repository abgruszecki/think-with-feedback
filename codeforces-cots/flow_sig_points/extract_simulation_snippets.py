#!/usr/bin/env python3
import json
import os
from pathlib import Path

from loguru import logger

from py_shared import ser


tag_suffix = ''
if tag := os.environ.get('STEP_TAG'):
    tag_suffix = f'+{tag}'
flowd = Path(__file__).parent
flow_outd = flowd/'out'
dep_ds_f = flow_outd/'fetch_process_solutions_py/report.jsonl'
dep_ext_sigpts_f = flow_outd/f'extend_sig_points_with_interests{tag_suffix}' / 'result.jsonl'
out_f = flow_outd/f'extract_simulation_snippets{tag_suffix}' / 'result.jsonl'
out_f.parent.mkdir(parents=True, exist_ok=True)


ds_by_idx = {in_r['idx']: in_r for in_r in ser.jsonl_streamf(dep_ds_f)}

if __name__ == '__main__':
    def make_r(in_r: dict, code: str):
        r = {
            k: in_r[k] for k in ('idx', 'offset', 'text')
        }
        r['code'] = code
        examples = ds_by_idx[in_r['idx']]['inputs']['examples']
        r['examples'] = examples if examples is not None else []
        return r

    def process_batch(batch: list[dict], out_fh):
        last_code = None
        for in_r in batch:
            tp = in_r['type']
            if tp == 'code':
                last_code = in_r['text']
                continue

            if tp not in ('sim', 'case'):
                continue

            if in_r.get('is_candidate_sim', False):
                code = last_code
                if code is None:
                    logger.warning('Problem with row {}/{}: last_code is None', in_r['idx'], in_r['offset'])
                    continue
            elif in_r.get('is_answer_sim', False):
                code = ds_by_idx[in_r['idx']]['final_answer']
                if code is None:
                    continue
            else:
                continue

            r = make_r(in_r, code)
            print(json.dumps(r), file=out_fh)

    cur_idx = -1
    cur_batch = []

    with out_f.open('w') as out_fh:
        for in_r in ser.jsonl_streamf(dep_ext_sigpts_f):
            in_r_idx = in_r['idx']
            if cur_idx != in_r_idx:
                if cur_idx != -1:
                    process_batch(cur_batch, out_fh)
                cur_batch = []
                cur_idx = in_r_idx

            cur_batch.append(in_r)

        if cur_batch:
            process_batch(cur_batch, out_fh)