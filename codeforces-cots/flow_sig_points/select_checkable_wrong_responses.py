#!/usr/bin/env python3
"""
Take the pre-processed dataset, and select rows with wrong responses to checkable problems
"""
import json
from pathlib import Path

from loguru import logger

from py_shared import ser
import py_shared.flow as fl


ctx = fl.dirs(__file__)
dep_ds_f = ctx.flow_outd/'fetch_process_solutions_py/report.jsonl'
dep_check_report_f = ctx.flow_outd/'fetch_exec_checkable_answers/report.jsonl'
outf = ctx.step_outd/'report.jsonl'


def _failures_by_idx_gen():
    for r in ser.jsonl_streamf(dep_check_report_f):
        if r['status'] == 'fail:nonzero-exit':
            yield int(r['item']), r
failures_by_idx = dict(_failures_by_idx_gen())

with open(outf, 'w') as fh:
    for in_r in ser.jsonl_streamf(dep_ds_f):
        idx = in_r['idx']
        fail_r = failures_by_idx.get(idx)
        if fail_r is None:
            continue

        if fail_r['stdout']:
            logger.warning('Non-empty stdout for idx: {}', idx)
        in_r['fail_stderr'] = fail_r['stderr']
        print(json.dumps(in_r), file=fh)