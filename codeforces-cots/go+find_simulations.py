from collections import namedtuple
from pathlib import Path

import regex as reg # compatible with the re module, we need the reverse flag

from py_shared.schema.solutions_py import SolutionsRow
from py_shared import ser

root_outd = Path('out+v2')
solutions_py_file = root_outd / '1--solutions_py.jsonl'
boths_file = root_outd / '3--extract-boths.jsonl'
outf = root_outd / '4--simulations.jsonl'

boths_data = ser.jsonl_loadf(boths_file)
boths_by_problem = {int(r['problem']): r for r in boths_data}

response_t = namedtuple('response_t', ['idx', 'response'])

def gen_responses():
    with open(solutions_py_file, 'r') as fh:
        for line in fh:
            r = SolutionsRow.model_validate_json(line)
            if r.idx not in boths_by_problem:
                continue
            yield response_t(
                idx=r.idx,
                response=r.inputs.response,
            )

responses = list(gen_responses())

simulation_start_rx = reg.compile(
    # r'^.*?(let\'s test|testing).*?(examples?|samples?)',
    r'^.*?(let\'s test|testing)',
    flags=reg.IGNORECASE | reg.MULTILINE | reg.REVERSE,
)

dt = []
for in_row in responses:
    r = {
        'idx': in_row.idx,
        'inputs': in_row,
    }
    m = simulation_start_rx.search(in_row.response)
    simulation_idx = m.start() if m else -1
    percent_idx = int(simulation_idx / len(in_row.response) * 100) if m else -1
    r['simulation_idx'] = simulation_idx
    r['simulation_percent'] = percent_idx
    if m:
        r['simulation_text'] = in_row.response[simulation_idx:]
    dt.append(r)

ser.jsonl_dumpf(dt, outf)