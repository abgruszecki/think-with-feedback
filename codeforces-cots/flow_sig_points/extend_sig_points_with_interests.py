#!/usr/bin/env python3
from collections import namedtuple
import json
from pathlib import Path

from py_shared import ser


key_t = namedtuple('key_t', ['idx', 'offset'])


flow_outd = Path(__file__).parent/'out'
step_outd = flow_outd/'extend_sig_points_with_interests'
step_outd.mkdir(parents=True, exist_ok=True)
dep_interest_f = flow_outd/'find_interest_items' / 'result.jsonl'
dep_sig_points_f = flow_outd/'find_sig_points' / 'result.jsonl'
out_f = step_outd / 'result.jsonl'


if __name__ == '__main__':
    interest_items_by_idx_offset = {}
    for in_row in ser.jsonl_streamf(dep_interest_f):
        idx = in_row['idx']
        offset = in_row['offset']
        del in_row['idx']
        del in_row['id']
        del in_row['offset']
        interest_items_by_idx_offset[key_t(idx=idx, offset=offset)] = in_row

    with out_f.open('w') as out_fh:
        for in_row in ser.jsonl_streamf(dep_sig_points_f):
            key = key_t(**{k: in_row[k] for k in ('idx', 'offset')})
            extras = interest_items_by_idx_offset.get(key, {})
            in_row.update(extras)
            print(json.dumps(in_row), file=out_fh)