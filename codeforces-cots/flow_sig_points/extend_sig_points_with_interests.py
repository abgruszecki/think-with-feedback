#!/usr/bin/env python3
from collections import namedtuple
import json
from pathlib import Path

from py_shared import ser


flow_outd = Path(__file__).parent/'out'
step_outd = flow_outd/'extend_sig_points_with_interests'
step_outd.mkdir(parents=True, exist_ok=True)
dep_interest_f = flow_outd/'find_interest_items' / 'result.jsonl'
dep_sig_points_f = flow_outd/'find_sig_points' / 'result.jsonl'
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
            extras = interest_items_by_sigpt_idx.get(sigpt_idx, {})
            in_row.update(extras)
            print(json.dumps(in_row), file=out_fh)