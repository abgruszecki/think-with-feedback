#!/usr/bin/env python3
from dataclasses import dataclass
from pathlib import Path
import shutil
from typing import Generator, Iterable, Iterator

from loguru import logger
import typer

from dockerinator.run_in_containers import run_items_in_workdir_containers, ExecutionArgs
from py_shared import ser
from py_shared.code_finder import find_final_answer_block
from py_shared.misc import step_dirs

app = typer.Typer()


@dataclass
class Item:
    key: str
    code: str


keycols = ('idx', 'offset')


def run_checks_on_response_code(
    dep_rows: Iterable[dict],
    out_workdir_root: Path,
    out_report_f: Path,
    max_workers: int | None,
) -> None:
    items = []
    for in_r in dep_rows:
        key = '/'.join(str(in_r[k]) for k in keycols)
        resp = in_r['response']
        code_str = find_final_answer_block(resp, offset=0)
        if code_str is None:
            logger.warning('No code block found at: {}', key)
            continue
        code_str = code_str.strip()
        if not code_str:
            continue
        item = Item(
            key=key,
            code=code_str,
        )
        items.append((item, key))

    def prepare_workdir(
        item: Item,
        local_workdir: Path
    ) -> None:
        assert local_workdir.exists(), f'expected to exist: {local_workdir}'
        (local_workdir/'snippet.py').write_text(item.code)
        shutil.copytree(local_workdir, out_workdir_root/item.key.replace('/', '_'), dirs_exist_ok=True)

    logger.info('Running {} items...', len(items))
    run_items_in_workdir_containers(
        executor_image_name='python',
        inputs=items,
        prepare_workdir=prepare_workdir,
        execution_args=ExecutionArgs(
            executor_args=['python', '/workdir/snippet.py'],
            max_workers=max_workers,
            report_path=out_report_f,
        ),
    )


def postprocess_checks_report(
    dep_rows: Iterable[dict],
    report_f: Path,
) -> Iterator[dict]:
    dep_r_by_keytup = { tuple(r[k] for k in keycols): r for r in dep_rows }

    for in_r in ser.jsonl_streamf(report_f):
        keytup = tuple(map(int, in_r['item'].split('/')))
        r = dep_r_by_keytup[keytup].copy()
        for k, v in in_r.items():
            if k == 'item':
                continue
            r[k] = v
        yield r


@app.command()
def main(
    extend_run: Path | None = None,
    force: bool = False,
    max_workers: int | None = None,
):
    _, _, step_outd = step_dirs(__file__, has_runs=True, extend_run=extend_run or 'last', force=force)
    run_outd = step_outd.parent

    dep_f = run_outd/'synth_unit_tests/result.jsonl'

    out_workdir_root = step_outd/'check-workdirs'
    out_workdir_root.mkdir(parents=True, exist_ok=True)
    out_report_f = step_outd/'raw-report.jsonl'
    out_postprocessed_f = step_outd/'result.jsonl'

    run_checks_on_response_code(
        dep_rows=ser.jsonl_streamf(dep_f),
        out_workdir_root=out_workdir_root,
        out_report_f=out_report_f,
        max_workers=max_workers,
    )

    ser.jsonl_dumpf(
        postprocess_checks_report(
            dep_rows=ser.jsonl_streamf(dep_f),
            report_f=out_report_f,
        ),
        out_postprocessed_f,
    )

    for fp, _, _ in step_outd.walk():
        fp.chmod(0o777)


if __name__ == '__main__':
    app()
