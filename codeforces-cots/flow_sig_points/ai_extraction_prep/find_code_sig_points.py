#! /usr/bin/env python3
from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from py_shared import ser
from py_shared.misc import cwd_rel, step_dirs
import flow_sig_points.find_sig_points as find_sig_points


app = typer.Typer()


@app.command()
def main():
    _, flow_outd, step_outd = step_dirs(__file__)

    dep_ds_f = flow_outd/'fetch_process_solutions_py/report.jsonl'
    dep_ds_checker_types_f = flow_outd/'fetch_extract_checker_type/checker-types.jsonl'

    out_f = step_outd/'result.jsonl'

    # NOTE this code is copied almost directly from find_sig_points.py...
    wanted_indices = set()
    for r in ser.jsonl_streamf(dep_ds_checker_types_f):
        if r.get('type') == 'diff':
            wanted_indices.add(r['idx'])

    data_f = dep_ds_f
    def _gen_data_rows():
        return (r for r in ser.jsonl_streamf(data_f) if r['idx'] in wanted_indices)
    data_len = sum(1 for _ in _gen_data_rows())
    data_gen = ((r['idx'], r) for r in _gen_data_rows())
    get_response = lambda r: r['inputs']['response']
    # END NOTE

    with out_f.open('w') as fh:
        for idx, in_r in tqdm(data_gen, total=data_len):
            r = {
                'idx': idx,
                'offset': None, # here for column ordering, will be filled in later
                'id': in_r['id'],
            }
            for p in find_sig_points.processed_response_gen(
                get_response(in_r),
                only_code=True,
            ):
                r.update(p.model_dump())
                print(ser.json.dumps(r), file=fh)
    logger.success('Wrote: {}', cwd_rel(out_f))

if __name__ == '__main__':
    app()
