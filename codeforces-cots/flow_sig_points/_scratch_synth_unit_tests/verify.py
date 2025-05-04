#!/usr/bin/env python3
from dataclasses import dataclass
from pathlib import Path
import re
import shutil

from loguru import logger
import typer

from dockerinator.run_in_containers import run_items_in_workdir_containers, ExecutionArgs
from py_shared import ser
from py_shared.code_finder import find_final_answer_block
from py_shared.test_code_maker2 import make_test_code
from py_shared.misc import step_dirs


@dataclass
class Item:
    idx: int
    code: str


app = typer.Typer()


@app.command()
def main(
    extend_run: Path | None = None,
    force: bool = False,
    max_workers: int | None = None,
):
    _, _, substep_outd = step_dirs(__file__, has_runs=True, extend_run=extend_run or 'last', force=force)
    run_outd = substep_outd.parent

    dep_f = run_outd/'generate2/result.jsonl'

    out_workdir_root = substep_outd/'check-workdirs'
    out_workdir_root.mkdir(parents=True, exist_ok=True)
    out_f = substep_outd/'report.jsonl'

    items = []
    for in_r in ser.jsonl_streamf(dep_f):
        idx = in_r['idx']
        resp = in_r['response']
        code_str = find_final_answer_block(resp, offset=0)
        if code_str is None:
            logger.warning('No code extracted from: {}', idx)
            continue
        code_str = code_str.strip()
        if not code_str:
            continue
        item = Item(
            idx=idx,
            code=code_str,
        )
        items.append((item, idx))

    def prepare_workdir(
        item: Item,
        local_workdir: Path
    ) -> None:
        assert local_workdir.exists(), f'expected to exist: {local_workdir}'
        (local_workdir/'snippet.py').write_text(item.code)
        shutil.copytree(local_workdir, out_workdir_root/str(item.idx), dirs_exist_ok=True)

    logger.info('Running {} items...', len(items))
    run_items_in_workdir_containers(
        executor_image_name='python',
        inputs=items,
        prepare_workdir=prepare_workdir,
        execution_args=ExecutionArgs(
            executor_args=['python', '/workdir/snippet.py'],
            max_workers=max_workers,
            report_path=out_f,
        ),
    )


if __name__ == '__main__':
    app()
