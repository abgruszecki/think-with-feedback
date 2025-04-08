#!/usr/bin/env python3
import json
from pathlib import Path
import sys

from py_shared import ser
from py_shared.json_finder import find_json


flow_outd = Path(__file__).parent/'out'
step_outd = flow_outd/'extract_checker_type'
step_outd.mkdir(parents=True, exist_ok=True)
outf = step_outd / 'checker-types.jsonl'


from os import environ as env
if __name__ == '__main__' and 'NOGO' not in env:
    import datasets
    ds = datasets.load_dataset('open-r1/codeforces-cots', 'solutions_py', split='train[:1000]')
    wanted_ids_list = []
    wanted_ids_set = set()
    for r in ds:
        wanted_ids_list.append(r['id'])
        wanted_ids_set.add(r['id'])

    checker_ds = datasets.load_dataset('open-r1/codeforces-cots', 'checker_interactor', split='train')
    checker_dict = {}
    for r in checker_ds:
        if r['id'] in wanted_ids_set:
            checker_dict[r['id']] = r['generation']

    output = []
    for row_idx, row_id in enumerate(wanted_ids_list):
        r = {'idx': row_idx, 'id': row_id}
        output.append(r)

        json_str = find_json(checker_dict[row_id])
        if json_str is None:
            print(f'No JSON found for {row_id}', file=sys.stderr)
            continue

        try:
            json_obj = json.loads(json_str)
        except Exception as e:
            print(f'Error parsing JSON for {row_id}: {e}', file=sys.stderr)
            continue

        r.update(json_obj)

    ser.jsonl_dumpf(output, outf)