#!/usr/bin/env python3
"""
This script execs the final answers only for the "checkable" problems.

ATM it's specialized only to work on the entire (processed) dataset.
"""
from collections import namedtuple
import json
from pathlib import Path
import shutil

from loguru import logger
import typer

from dockerinator.run_in_containers import run_items_in_workdir_containers, ExecutionArgs
from py_shared import ser


item_t = namedtuple('item_t', ['snippet', 'examples'])

app = typer.Typer()


flow_outd = Path(__file__).parent/'out'
step_outd = flow_outd/'exec_checkable_answers'
step_outd.mkdir(parents=True, exist_ok=True)

dep_ds_f = flow_outd/'process_solutions_py+full/report.jsonl'
dep_checker_ds_f = flow_outd/'extract_checker_type+full/checker-types.jsonl'


def _ds_checker_type_by_idx_gen():
    for r in ser.jsonl_streamf(dep_checker_ds_f):
        yield r['idx'], r.get('type')
ds_checker_type_by_idx = dict(_ds_checker_type_by_idx_gen())


@app.command()
def main(max_workers: int | None = None):
    items = []
    for in_r in ser.jsonl_streamf(dep_ds_f):
        idx = in_r['idx']

        checker_type = ds_checker_type_by_idx.get(idx)
        if checker_type is None:
            logger.warning('no checker type for idx: {}', idx)
            continue

        if checker_type == 'diff':
            key = str(idx)
            item = item_t(
                snippet=in_r['final_answer'],
                examples=in_r['inputs']['examples'],
            )
            if item.snippet and item.examples:
                items.append((item, key))

    def prepare_workdir(
        item: item_t,
        local_workdir: Path
    ):
        assert local_workdir.exists(), f'expected to exist: {local_workdir}'
        shutil.copytree(flow_outd.parent/'checker-resources', local_workdir, dirs_exist_ok=True)
        ser.json_dumpf(item.examples, local_workdir/'examples.json')
        (local_workdir/'snippet.py').write_text(item.snippet)

    run_items_in_workdir_containers(
        executor_image_name='python',
        inputs=items,
        prepare_workdir=prepare_workdir,
        execution_args=ExecutionArgs(
            executor_args=['python', '/workdir/test_harness.py'],
            max_workers=max_workers,
            report_path=step_outd/'report.jsonl',
        ),
    )


if __name__ == '__main__':
    app()
