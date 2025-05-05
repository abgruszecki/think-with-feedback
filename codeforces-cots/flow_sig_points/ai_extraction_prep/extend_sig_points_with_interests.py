#! /usr/bin/env python3
from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from py_shared import ser
from py_shared.misc import cwd_rel, step_dirs
import flow_sig_points.extend_sig_points_with_interests as extend_sig_points_with_interests

app = typer.Typer()


@app.command()
def main():
    _, _, substep_outd = step_dirs(__file__)
    subflow_outd = substep_outd.parent

    dep_interest_f = subflow_outd/'find_interest_items/result.jsonl'
    dep_sig_points_f = subflow_outd/'find_code_sig_points/result.jsonl'

    out_f = substep_outd/'result.jsonl'

    with out_f.open('w') as out_fh:
        for r in extend_sig_points_with_interests.gen_extended_sig_point_rows(
            ser.jsonl_streamf(dep_interest_f),
            ser.jsonl_streamf(dep_sig_points_f),
        ):
            print(ser.json.dumps(r), file=out_fh)
    logger.success('Wrote: {}', cwd_rel(out_f))


if __name__ == '__main__':
    app()
