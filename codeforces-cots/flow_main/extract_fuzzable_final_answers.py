#!/usr/bin/env python3
"""
This script extracts "fuzzable final answers" from the CoTs,
i.e., final answers to problems which we know how to check and which pass all the examples.
"""
import json
from pathlib import Path

from loguru import logger

from py_shared import ser


flow_outd = Path(__file__).parent/'out'
step_outd = flow_outd/'extract_fuzzable_final_answers'
step_outd.mkdir(parents=True, exist_ok=True)

dep_ds_outf = flow_outd/'process_solutions_py'/'report.jsonl'
dep_checker_outf = flow_outd/'fetch_checker_classification'/'data.jsonl'
dep_otherchecker_outf = flow_outd/'extract_checker_type'/'checker-types.jsonl'
dep_eval_outf = flow_outd/'exec_snippets_via_workdir'/'report.jsonl'


# dep_ds_data = []
dep_ds_data_by_idx = {}
for in_r in ser.jsonl_streamf(dep_ds_outf):
    idx = in_r['idx'] - 1 # make the index 0-based
    # r = { 'idx': idx, }
    r = {}
    examples = in_r['inputs']['examples']
    if examples is None:
        examples = []
    r['examples'] = examples
    r['final_answer'] = in_r['final_answer']
    # dep_ds_data.append(r)
    dep_ds_data_by_idx[idx] = r

# dep_checker_data = []
dep_checker_data_by_idx = {}
for r in ser.jsonl_streamf(dep_checker_outf):
    del r['responses']
    votes = r['votes']
    del r['votes']
    r['diff_votes'] = sum(1 for v in votes if v == 'diff')
    r['checker_votes'] = sum(1 for v in votes if v == 'checker')
    r['null_votes'] = sum(1 for v in votes if v == None)
    idx = r['idx'] # already 0-based
    # dep_checker_data.append(r)
    dep_checker_data_by_idx[idx] = r
# dep_checker_data.sort(key=lambda r: r['idx'])

dep_otherchecker_data_by_idx = {}
for r in ser.jsonl_streamf(dep_otherchecker_outf):
    idx = r['idx']
    dep_otherchecker_data_by_idx[idx] = r

dep_eval_data = []
# dep_eval_data_by_idx = {}
for in_r in ser.jsonl_streamf(dep_eval_outf):
    # if in_r['status'] == 'success' and in_r['item'].endswith('/final-answer'):
    if in_r['item'].endswith('/final-answer'):
        idx = int(in_r['item'].split('/', 1)[0]) - 1 # make the index 0-based
        in_r['idx'] = idx
        dep_eval_data.append(in_r)
        # dep_eval_data_by_idx[idx] = r
dep_eval_data.sort(key=lambda r: r['idx'])

full_outf = step_outd/'full-result.jsonl'
clean_outf = step_outd/'clean-result.jsonl'
clean_cols = [ 'idx', 'final_answer', 'examples', ]
with open(full_outf, 'w') as full_fh, open(clean_outf, 'w') as clean_fh:
    for in_r in dep_eval_data:
        idx = in_r['idx']
        if idx not in dep_checker_data_by_idx:
            logger.warning('idx not in dep_checker_data_by_idx: {}', idx)
            continue
        pre_out_r = in_r.copy()
        pre_out_r.update(dep_ds_data_by_idx[idx])
        pre_out_r.update(dep_checker_data_by_idx[idx])
        pre_out_r.update(dep_otherchecker_data_by_idx[idx])
        out_r = { 'idx': pre_out_r['idx'], } # make idx the first key (for output column order)
        out_r.update(pre_out_r)
        print(json.dumps(out_r), file=full_fh)

        if out_r['diff_votes'] == 4:
            clean_out_r = { k: out_r[k] for k in clean_cols }
            print(json.dumps(clean_out_r), file=clean_fh)

# ser.jsonl_dumpf(out_data, step_outd/'full-result.jsonl')
