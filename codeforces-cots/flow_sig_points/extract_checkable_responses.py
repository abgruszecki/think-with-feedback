#!/usr/bin/env python3
import json
from pathlib import Path

from loguru import logger

from py_shared import ser


flow_outd = Path(__file__).parent/'out'
step_outd = flow_outd/'extract_checkable_responses'
step_outd.mkdir(parents=True, exist_ok=True)

dep_ds_f = flow_outd/'fetch_process_solutions_py'/'report.jsonl'
dep_checker_f = flow_outd/'fetch_checker_classification'/'data.jsonl'

full_outf = step_outd/'full-result.jsonl'
clean_outf = step_outd/'clean-result.jsonl'


dep_checker_data = []
dep_checker_data_by_idx = {}
for r in ser.jsonl_streamf(dep_checker_f):
    del r['responses']
    votes = r['votes']
    del r['votes']
    r['diff_votes'] = sum(1 for v in votes if v == 'diff')
    r['checker_votes'] = sum(1 for v in votes if v == 'checker')
    r['null_votes'] = sum(1 for v in votes if v == None)
    idx = r['idx']
    # dep_checker_data.append(r)
    dep_checker_data_by_idx[idx] = r
dep_checker_data.sort(key=lambda r: r['idx'])


clean_cols = [ 'idx', 'id', 'generation', ]
with open(full_outf, 'w') as full_fh, open(clean_outf, 'w') as clean_fh:
    diff_rows_count = 0
    for in_r in ser.jsonl_streamf(dep_ds_f):
        idx = in_r['idx']
        if idx not in dep_checker_data_by_idx:
            logger.warning('no checker data for idx: {}', idx)
            continue
        pre_out_r = {k: in_r[k] for k in ('idx', 'id')}
        pre_out_r['generation'] = in_r['inputs']['response']
        pre_out_r.update(dep_checker_data_by_idx[idx])
        out_r = { 'idx': pre_out_r['idx'], } # make idx the first key (for output column order)
        out_r.update(pre_out_r)
        print(json.dumps(out_r), file=full_fh)

        if out_r['diff_votes'] == 4:
            clean_out_r = { k: out_r[k] for k in clean_cols }
            print(json.dumps(clean_out_r), file=clean_fh)