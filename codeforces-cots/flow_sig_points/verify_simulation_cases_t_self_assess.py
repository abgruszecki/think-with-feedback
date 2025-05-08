#!/usr/bin/env python3
from dataclasses import dataclass
from pathlib import Path
import re
import shutil

from loguru import logger
import typer

from dockerinator.run_in_containers import run_items_in_workdir_containers, ExecutionArgs
from py_shared import ser
from py_shared.test_code_maker2 import make_test_code
from py_shared.misc import step_dirs

app = typer.Typer()


@dataclass
class Item:
    key: str
    idx: int
    offset: int
    case_idx: int
    code: str
    examples: list[dict]


py_indent_rx = re.compile(r'^ *')


@app.command()
def main(
    data: Path,
    use_test_harness: bool = True,
    max_workers: int | None = None,
):
    assert data.is_file(), f'expected a file: {data}'
    data_run_d = data.parent
    data_step_outd = data_run_d.parent
    run_id = data_run_d.stem
    tag = data_step_outd.stem.split('+', 1)[-1]
    logger.info('run_id: {}, tag: {}', run_id, tag)
    assert tag == 'self-assess'

    flowd, flow_outd, step_outd = step_dirs(__file__, tag)
    run_outd = step_outd/run_id
    out_workdir_root = run_outd/'check-workdirs'
    out_f = run_outd/'report.jsonl'
    out_f.parent.mkdir(parents=True, exist_ok=True)
    out_workdir_root.mkdir(parents=True, exist_ok=True)

    items: list[tuple[Item, str]] = []
    sus_ds_indices = set()
    filtered_items_num = 0
    for r in ser.jsonl_streamf(data):
        num = r.get('num')
        if num is None:
            continue

        idx = r['idx']
        offset = r['offset']
        case_idx = r['case_idx']
        key = f'{idx}_{offset}_{case_idx}'
        if idx in sus_ds_indices:
            filtered_items_num += 1
            continue

        in_examples = r['examples']
        if num > len(in_examples):
            # if the numerator written by the model is higher than the number of examples,
            # we treat this as an indication that the problem has many cases per example
            # and the model decided to number them individually.
            sus_ds_indices.add(idx)
            filtered_items_num += 1
            continue
        example = in_examples[num-1]

        code = r['code']
        examples = [{
            # fail if the keys aren't there...
            'input': example['input'],
            'output': example['output'],
        }]
        item = Item(
            key=key,
            idx=idx,
            offset=offset,
            case_idx=case_idx,
            code=code,
            examples=examples,
        )
        items.append((item, key))

    # filter out items with marked keys
    if sus_ds_indices:
        _items_gen = iter(items)
        items = []
        for item, key in _items_gen:
            if item.idx not in sus_ds_indices:
                items.append((item, key))
            else:
                filtered_items_num += 1
        logger.info('Filtered {} items', filtered_items_num)

    def prepare_workdir(
        item: Item,
        local_workdir: Path
    ) -> None:
        assert local_workdir.exists(), f'expected to exist: {local_workdir}'
        if use_test_harness:
            shutil.copytree(flowd/'checker-resources', local_workdir, dirs_exist_ok=True)
            ser.json_dumpf(item.examples, local_workdir/'examples.json')
            with open(local_workdir/'snippet.py', 'w') as fh:
                first_indent = None
                for line in str(item.code).splitlines():
                    if first_indent is None:
                        first_indent = py_indent_rx.match(line).group(0)
                    print(line.removeprefix(first_indent), file=fh)
        else:
            test_code = make_test_code(item.code, item.examples)
            (local_workdir/'snippet.py').write_text(test_code)

        stored_workdir = out_workdir_root/item.key
        shutil.rmtree(stored_workdir, ignore_errors=True)
        shutil.copytree(local_workdir, stored_workdir, dirs_exist_ok=True)

    script_name = '/workdir/' + ('test_harness.py' if use_test_harness else 'snippet.py')
    run_items_in_workdir_containers(
        executor_image_name='python',
        inputs=items,
        prepare_workdir=prepare_workdir,
        execution_args=ExecutionArgs(
            executor_args=['python', script_name],
            max_workers=max_workers,
            report_path=out_f,
        ),
    )


if __name__ == '__main__':
    app()