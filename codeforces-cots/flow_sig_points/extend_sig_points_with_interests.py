#!/usr/bin/env python3
from pathlib import Path

from py_shared import ser


flow_outd = Path(__file__).parent/'out'
step_outd = flow_outd/'extend_sig_points_with_interests'
step_outd.mkdir(parents=True, exist_ok=True)
dep_interest_f = flow_outd/'find_interest_items' / 'result.jsonl'
dep_sig_points_f = flow_outd/'find_sig_points' / 'result.jsonl'
out_f = step_outd / 'result.jsonl'


if __name__ == '__main__':
    interest_items_by_idx = {}
    for in_row in ser.jsonl_streamf(dep_interest_f):
        idx = in_row['idx']
        del in_row['idx']
        del in_row['id']
        interest_items_by_idx[idx] = in_row

    with out_f.open('w') as out_fh:
        for in_row in ser.jsonl_streamf(dep_sig_points_f):
            extras = interest_items_by_idx.get(in_row['idx'], {})
            in_row.update(extras)
            ser.json.dump(in_row, out_fh)
            print(file=out_fh)