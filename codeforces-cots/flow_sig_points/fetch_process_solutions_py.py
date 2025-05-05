#!/usr/bin/env python3
import shutil
from pathlib import Path

from loguru import logger
import typer

import py_shared.flow as fl

app = typer.Typer()


@app.command()
def main(
    full: bool = False,
    link: bool = False,
):
    ctx = fl.dirs(__file__)
    tag_suffix = '' if not full else '+full'
    dep_outf = ctx.flowd.parent/f'flow_main/out/process_solutions_py{tag_suffix}/report.jsonl'
    outf = ctx.flow_outd/'fetch_process_solutions_py/report.jsonl'
    if not link:
        # Let's be careful not to overwrite the source...
        if outf.is_symlink():
            outf.unlink()
        shutil.copy(dep_outf, outf)
        logger.success('Copied {} to {}', fl.cwd_rel(dep_outf), fl.cwd_rel(outf))
    else:
        # NOTE this may blow up if the file exists, which may be what we want.
        outf.symlink_to(dep_outf)
        logger.success('Symlinked {} to {}', fl.cwd_rel(dep_outf), fl.cwd_rel(outf))


if __name__ == '__main__':
    app()
