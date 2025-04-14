#!/usr/bin/env python3
from collections import namedtuple
from pathlib import Path
import shutil

from loguru import logger
import typer

from dockerinator.run_in_containers import run_items_in_workdir_containers, ExecutionArgs
from py_shared import ser
from py_shared.misc import step_dirs


item_t = namedtuple('item_t', ['code', 'examples'])

app = typer.Typer()


@app.command()
def main(
    data: Path,
    max_workers: int | None = None,
):
    assert data.is_file(), f'expected a file: {data}'
    data_run_d = data.parent
    data_step_outd = data_run_d.parent
    run_id = data_run_d.stem
    tag = data_step_outd.stem.split('+', 1)[-1]
    logger.info('run_id: {}, tag: {}', run_id, tag)

    flowd, flow_outd, step_outd = step_dirs(__file__, tag)
    out_f = step_outd/f'{run_id}/report.jsonl'
    out_f.parent.mkdir(parents=True, exist_ok=True)

    items = []
    for r in ser.jsonl_streamf(data):
        key = f'{r["idx"]}_{r["offset"]}'
        code = r['code']
        examples = [{
            'input': r['input'],
            'output': r['output'],
        }]
        items.append((item_t(code, examples), key))

    def prepare_workdir(
        item: item_t,
        local_workdir: Path
    ):
        assert local_workdir.exists(), f'expected to exist: {local_workdir}'
        shutil.copytree(flowd/'checker-resources', local_workdir, dirs_exist_ok=True)
        ser.json_dumpf(item.examples, local_workdir/'examples.json')
        (local_workdir/'snippet.py').write_text(item.code)

    run_items_in_workdir_containers(
        executor_image_name='python',
        inputs=items,
        prepare_workdir=prepare_workdir,
        execution_args=ExecutionArgs(
            executor_args=['python', '/workdir/test_harness.py'],
            max_workers=max_workers,
            report_path=out_f,
        ),
    )


if __name__ == '__main__':
    app()