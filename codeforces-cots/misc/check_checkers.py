#!/usr/bin/env python3
from dataclasses import dataclass
import json
from pathlib import Path
import shutil
from typing import Iterable, Iterator

import datasets
from loguru import logger
from tqdm import tqdm
import typer

from dockerinator.run_in_containers import run_items_in_workdir_containers, ExecutionArgs
from py_shared import ser
from py_shared.json_finder import find_json
from py_shared.misc import step_dirs, cwd_rel


app = typer.Typer()


def gen_checker_rows():
    logger.info('Processing solutions_py')
    ds_by_id: dict[str, tuple[int, dict]] = {}
    ds_solutions_py = datasets.load_dataset('open-r1/codeforces-cots', 'solutions_py', split='train')
    for idx, in_r in enumerate(tqdm(ds_solutions_py)):
        id = in_r['id']
        examples = in_r.get('examples', None)
        if examples:
            ds_by_id[id] = (idx, examples)

    logger.info('Processing checker_interactor')
    ds_checkers = datasets.load_dataset('open-r1/codeforces-cots', 'checker_interactor', split='train')
    for in_r in tqdm(ds_checkers):
        id = in_r['id']
        ds_entry = ds_by_id.get(id, None)
        if not ds_entry:
            continue
        idx, examples = ds_entry

        checker_response = in_r['generation']
        json_str = find_json(checker_response)
        if json_str is None:
            logger.warning('No JSON found in checker response: {}', idx)
            continue

        try:
            json_obj = json.loads(json_str)
        except:
            logger.warning('Error parsing JSON in checker response: {}', idx)
            continue

        type_ = json_obj.get('type')
        if type_ != 'checker':
            continue
        code = json_obj.get('code')
        if code is None:
            logger.warning('No code found in checker response: {}', idx)
            continue

        r = {
            'idx': idx,
            'id': id,
            'type': type_,
            'examples': examples,
            'checker_code': code,
        }
        yield r


def check_checkers(
    checker_rows: list[dict],
    out_workdir_root: Path,
    out_report_f: Path,
    max_workers: int | None,
):
    items = []
    for r in checker_rows:
        idx = r['idx']
        items.append((r, idx))

    out_report_f.parent.mkdir(parents=True, exist_ok=True)

    def prepare_workdir(
        item: dict,
        local_workdir: Path
    ):
        assert local_workdir.exists(), f'expected to exist: {local_workdir}'
        (local_workdir/'checker.py').write_text(item['checker_code'])
        examples_root = local_workdir/'examples'
        examples_root.mkdir(parents=True, exist_ok=True)
        for example_idx, example in enumerate(item['examples']):
            example_d = examples_root/str(example_idx)
            example_d.mkdir(parents=True, exist_ok=True)
            (example_d/'input.txt').write_text(example['input'])
            (example_d/'output.txt').write_text(example['output'])
        (local_workdir/'run.sh').write_text(
'''\
#!/usr/bin/env bash
cd "$(dirname "$0")"
for f in examples/*; do
    echo "Checking $f"
    result=$(python checker.py "$f/input.txt" "$f/output.txt" "$f/output.txt")
    if [ "$result" = "0" ]
    then
        echo "Fail at: $f" >&2
        exit 1
    elif ! [ "$result" = "1" ]
    then
        echo "Unknown result: $result"
        exit 1
    fi
done
''')

        stored_workdir = out_workdir_root/str(item['idx'])
        # not deleting the workdir right now to avoid changing the permissions
        # shutil.rmtree(stored_workdir, ignore_errors=True)
        shutil.copytree(local_workdir, stored_workdir, dirs_exist_ok=True)

    logger.info('Checking the checkers...')
    run_items_in_workdir_containers(
        executor_image_name='python',
        inputs=items,
        prepare_workdir=prepare_workdir,
        execution_args=ExecutionArgs(
            executor_args=['bash', '/workdir/run.sh'],
            max_workers=max_workers,
            report_path=out_report_f,
        ),
    )


@app.command('write-checker-rows')
def cmd_write_checker_rows():
    _, flow_outd, step_outd = step_dirs(__file__)
    out_checkers_f = step_outd / 'checkers.jsonl'
    ser.jsonl_dumpf(gen_checker_rows(), out_checkers_f)
    logger.success('Wrote: {}', cwd_rel(out_checkers_f))


@app.command('check-checkers')
def cmd_check_checkers(
    max_workers: int | None = None,
):
    _, flow_outd, step_outd = step_dirs(__file__)
    out_checkers_f = step_outd / 'checkers.jsonl'
    checker_rows = ser.jsonl_loadf(out_checkers_f)
    out_workdir_root = step_outd / 'check-workdirs'
    out_report_f = step_outd / 'checkers-report.jsonl'
    check_checkers(
        checker_rows[:100],
        out_workdir_root,
        out_report_f,
        max_workers=max_workers,
    )


# @app.command()
# def main(
#     max_workers: int | None = None,
# ):
#     pass


if __name__ == '__main__':
    app()
