#!/usr/bin/env python3
from collections import namedtuple
import json
import os
from pathlib import Path

from py_shared import ser

tag_suffix = ''
if tag := os.environ.get('STEP_TAG'):
    tag_suffix = f'+{tag}'
flow_outd = Path(__file__).parent/'out'
step_outd = flow_outd/f'extend_sig_points_with_interests{tag_suffix}'
step_outd.mkdir(parents=True, exist_ok=True)
dep_interest_f = flow_outd/f'find_interest_items{tag_suffix}' / 'result.jsonl'
dep_sig_points_f = flow_outd/f'find_sig_points{tag_suffix}' / 'result.jsonl'
out_f = step_outd / 'result.jsonl'


if __name__ == '__main__':
    interest_items_by_sigpt_idx = {}
    for in_row in ser.jsonl_streamf(dep_interest_f):
        sigpt_idx = in_row['sigpt_idx']
        for k in ('idx', 'id', 'offset', 'sigpt_idx'):
            del in_row[k]
        interest_items_by_sigpt_idx[sigpt_idx] = in_row

    with out_f.open('w') as out_fh:
        for sigpt_idx, in_row in enumerate(ser.jsonl_streamf(dep_sig_points_f)):
            extras = interest_items_by_sigpt_idx.get(sigpt_idx, None)
            if extras:
                in_row['interest'] = True
                in_row.update(extras)
            else:
                in_row['interest'] = False
            print(json.dumps(in_row), file=out_fh)