#!/usr/bin/env python3
from dataclasses import dataclass
from pathlib import Path
import shutil
from typing import Iterable, Iterator

from loguru import logger
import typer

from dockerinator.run_in_containers import run_items_in_workdir_containers, ExecutionArgs
from py_shared import ser
from py_shared.misc import step_dirs, cwd_rel
from py_shared import io_abstractinator, test_code_maker2


app = typer.Typer()


@dataclass
class ExecItem:
    key: str
    snippet: str


def row_key(idx, offset):
    return f'{idx}_{offset}'


def make_replacement_snippet(
    code: str,
    examples: list[dict],
    row_key: str,
) -> str:
    instrumented_code = io_abstractinator.go2(code, row_key)
    test_code = test_code_maker2.make_test_code(instrumented_code, examples)
    return test_code


def gen_replacement_snippets(
    snippet_rows: Iterable[dict]
) -> Iterator[dict]:
    total_rows = 0
    index_errors = 0
    for in_r in snippet_rows:
        total_rows += 1
        idx = in_r['idx']
        offset = in_r['offset']
        key = row_key(idx, offset)

        code = in_r['code']
        examples = in_r['examples']
        nums = in_r['nums']
        if not examples:
            logger.warning('No examples for row: {}', idx)
            continue
        if not nums:
            continue

        has_index_error = False
        try:
            used_examples = [examples[i-1] for i in nums]
        except IndexError:
            has_index_error = True
            index_errors += 1
            used_examples = [examples[0]]
            nums = [1]
            logger.warning('Index error for row: {}', idx)
            # continue

        snippet = make_replacement_snippet(code, used_examples, key)

        r = {
            'idx': idx,
            'offset': offset,
            'candidate_offset': in_r['candidate_offset'],
            'reasoning_len': len(in_r['text']),
            'nums': nums,
            'has_index_error': has_index_error,
            'code': snippet,
        }
        yield r
    logger.warning('Num of rows with index errors: {} / {}', index_errors, total_rows)


def exec_replacement_snippets(
    snippet_rows: Iterable[dict],
    out_workdir_root: Path,
    out_report_f: Path,
    max_workers: int | None,
):
    items = []
    for r in snippet_rows:
        idx = r['idx']
        offset = r['offset']
        key = row_key(idx, offset)
        item = ExecItem(
            key=key,
            snippet=r['code'],
        )
        items.append((item, key))

    out_workdir_root.mkdir(parents=True, exist_ok=True)

    def prepare_workdir(
        item: ExecItem,
        local_workdir: Path
    ):
        assert local_workdir.exists(), f'expected to exist: {local_workdir}'
        (local_workdir/'snippet.py').write_text(item.snippet)

        stored_workdir = out_workdir_root/item.key
        # not deleting the workdir right now to avoid changing the permissions
        # shutil.rmtree(stored_workdir, ignore_errors=True)
        shutil.copytree(local_workdir, stored_workdir, dirs_exist_ok=True)

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


def gen_processed_report(
    report_rows: Iterable[dict],
    replacement_snippet_rows_by_key: dict[str, dict],
) -> Iterator[dict]:
    for in_r in report_rows:
        key = in_r['item']
        replacement_snippet_r = replacement_snippet_rows_by_key[key]
        r = replacement_snippet_r.copy()
        r.update(in_r)
        del r['item']
        yield r


class StepCtx():
    def __init__(self):
        _, flow_outd, step_outd = step_dirs(__file__)
        self.flow_outd = flow_outd
        self.step_outd = step_outd

        self.dep_snippets_f = flow_outd/'extract_simulation_snippets/result.jsonl'

        self.out_replacement_snippets_f = step_outd/'replacement-snippets.jsonl'

        self.out_workdir_root = step_outd/'check-workdirs'
        self.out_report_f = step_outd/'report.jsonl'

        self.out_processed_report_f = step_outd/'processed-report.jsonl'


@app.command('make-replacement-snippets')
def cmd_make_replacement_snippets():
    ctx = StepCtx()
    ser.jsonl_dumpf(
        gen_replacement_snippets(ser.jsonl_streamf(ctx.dep_snippets_f)),
        ctx.out_replacement_snippets_f
    )
    logger.success('Wrote: {}', cwd_rel(ctx.out_replacement_snippets_f))


@app.command('exec-replacement-snippets')
def cmd_exec_replacement_snippets(
    max_workers: int | None = None,
):
    ctx = StepCtx()
    exec_replacement_snippets(
        ser.jsonl_streamf(ctx.out_replacement_snippets_f),
        ctx.out_workdir_root,
        ctx.out_report_f,
        max_workers,
    )
    logger.success('Wrote: {}', cwd_rel(ctx.out_report_f))


@app.command('postprocess-report')
def cmd_postprocess_report():
    ctx = StepCtx()
    replacement_snippet_rows_by_key = {}
    for r in ser.jsonl_streamf(ctx.out_replacement_snippets_f):
        key = row_key(r['idx'], r['offset'])
        replacement_snippet_rows_by_key[key] = r
    processed_report_rows_gen = gen_processed_report(
        ser.jsonl_streamf(ctx.out_report_f),
        replacement_snippet_rows_by_key,
    )
    ser.jsonl_dumpf(processed_report_rows_gen, ctx.out_processed_report_f)
    logger.success('Wrote: {}', cwd_rel(ctx.out_processed_report_f))


@app.command('all')
def cmd_all(
    max_workers: int | None = None,
):
    cmd_make_replacement_snippets()
    cmd_exec_replacement_snippets(max_workers)
    cmd_postprocess_report()


if __name__ == '__main__':
    app()
