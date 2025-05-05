#!/usr/bin/env python3
"""
This effectively prepares a dataset of Python code snippets to be executed.
"""

import json
from pathlib import Path
from collections import namedtuple
from loguru import logger

from py_shared import ser

StepDataNT = namedtuple('StepDataNT', ['flowd', 'flow_outd', 'step_outd'])
def _dirs(file_attr, tag: str|None = None) -> StepDataNT:
    p = Path(file_attr)
    flowd = p.parent
    flow_outd = flowd/'out'
    tag_suffix = ''
    if tag:
        tag_suffix = tag if tag.startswith('+') else ('+'+tag)
    step_outd = flow_outd/(p.stem+tag_suffix)
    step_outd.mkdir(parents=True, exist_ok=True)
    return StepDataNT(flowd, flow_outd, step_outd)

# TODO outdated code, +checkables are the default now
base_tag_suffix = '+checkables'
tag_suffix = base_tag_suffix+'+4o-mini+nocode'
flowd, flow_outd, step_outd = _dirs(__file__, tag_suffix)

dep_extraction_d = flow_outd/f'postprocess_simulation_cases{tag_suffix}'
dep_snippets_f = flow_outd/f'extract_simulation_snippets{base_tag_suffix}/result.jsonl'


def _dep_snippets_kv_gen():
    for r in ser.jsonl_streamf(dep_snippets_f):
        yield (r['idx'], r['offset']), r
dep_snippets_by_idx_offset = dict(_dep_snippets_kv_gen())


dep_snippets_cols = ['idx', 'offset', 'code']
dep_extraction_cols = ['input', 'output', 'source_sample_id', 'is_correct',]
def process_extraction_row(in_r: dict) -> dict | None:
    idx, offset = in_r['idx'], in_r['offset']
    if (idx, offset) not in dep_snippets_by_idx_offset:
        logger.warning('(idx, offset) not in dep_snippets_by_idx_offset: {}', (idx, offset))
        return None
    out_r = {}
    dep_snippets_r = dep_snippets_by_idx_offset[(idx, offset)]
    for k in dep_snippets_cols:
        out_r[k] = dep_snippets_r[k]
    for k in dep_extraction_cols:
        out_r[k] = in_r[k]
    return out_r

if __name__ == '__main__':
    for dep_extraction_run_d in dep_extraction_d.iterdir():
        if not dep_extraction_run_d.is_dir():
            continue
        dep_extraction_f = dep_extraction_run_d/'trustworthy-cases.jsonl'
        out_f = step_outd/dep_extraction_run_d.stem/'result.jsonl'
        out_f.parent.mkdir(parents=True, exist_ok=True)
        out_r_gen = filter(None, (
            process_extraction_row(in_r)
            for in_r in ser.jsonl_streamf(dep_extraction_f)
        ))
        ser.jsonl_dumpf(out_r_gen, out_f)
