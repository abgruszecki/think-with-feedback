import json
from pathlib import Path

from py_shared.ser import jsonl_streamf

root_outd = Path('./out+v2')

unwanted_indices = set(
    int(r['idx']) for r in jsonl_streamf(root_outd / '4--simulations.jsonl')
)

with (root_outd/'x--all_solutions_but_bad_simulations.jsonl').open('w') as fh:
    for ln in (root_outd/'1--solutions_py.jsonl').open():
        r = json.loads(ln)
        if int(r['idx']) in unwanted_indices:
            continue
        print(ln, file=fh)
