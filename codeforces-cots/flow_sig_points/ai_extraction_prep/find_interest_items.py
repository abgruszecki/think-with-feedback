#! /usr/bin/env python3
from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from py_shared import ser
from py_shared.misc import cwd_rel, step_dirs
import flow_sig_points.find_interest_items as find_interest_items


app = typer.Typer()


@app.command()
def main():
    _, flow_outd, substep_outd = step_dirs(__file__)
    subflow_outd = substep_outd.parent

    dep_f = subflow_outd/'find_code_sig_points/result.jsonl'
    outf = substep_outd/'result.jsonl'

    with outf.open('w') as out_fh:
        for r in find_interest_items.gen_interest_item_rows(ser.jsonl_streamf(dep_f)):
            print(ser.json.dumps(r), file=out_fh)
    logger.success('Wrote: {}', cwd_rel(outf))


if __name__ == '__main__':
    app()
