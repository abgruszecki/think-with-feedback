#!/usr/bin/env python3
from dataclasses import dataclass
from pathlib import Path
import shutil
from typing import Annotated, Generator, Iterable, Iterator

from loguru import logger
import typer

from dockerinator.run_in_containers import run_items_in_workdir_containers, ExecutionArgs
import py_shared.flow as fl
from py_shared.code_finder import thinks_end_rx, find_final_answer_block
from py_shared.schema import solutions_py

app = typer.Typer()


@dataclass
class VerifierItem():
    key: str
    io_examples: list[solutions_py.IOExample]
    code: str


class StepCtx(fl.StepDirs):
    def __init__(self, extend_run: Path | None, force: bool):
        src_ctx = fl.dirs(__file__, has_runs=True, extend_run=extend_run, force=force)
        # TODO how else to do this? add a method to StepDirs which turns it into kwargs?
        super().__init__(
            flowd=src_ctx.flowd,
            flow_outd=src_ctx.flow_outd,
            step_outd=src_ctx.step_outd,
            run_outd=src_ctx.run_outd,
        )

        self.rsrc_d = Path(__file__).parent/'resources'/Path(__file__).stem
        self.dep_ds_f = self.flow_outd/'fetch_process_solutions_py/report.jsonl'
        self.dep_responses_f = self.run_outd/'ai_generate_responses/result.jsonl'

        self.out_answers_f = self.step_outd/'answers.jsonl'
        self.out_report_f = self.step_outd/'report.jsonl'


def gen_answer_rows(
    dep_responses_rows: Iterable[dict],
    expect_thinks: bool,
) -> Iterator[dict]:
    for in_r in dep_responses_rows:
        idx = in_r['idx']
        response = in_r['response']

        r = { 'idx': idx }

        issues: list[str] = []
        r['issues'] = ''

        def gen_res():
            r['issues'] = ','.join(issues)
            yield r

        proper_response_offset = 0
        if expect_thinks:
            m = thinks_end_rx.search(response)
            if not m:
                issues.append('no-thinks-end')
                yield from gen_res()
                continue
            proper_response_offset = m.end()

        code = find_final_answer_block(response, proper_response_offset, answer_must_be_valid_python=False)
        if not code:
            issues.append('no-answer')
            yield from gen_res()
            continue

        r['code'] = code
        yield from gen_res()


def run_answer_verifier(
    answer_rows: Iterable[dict],
    ds_by_idx: dict[int, solutions_py.SolutionsRow],
    verifier_template_dir: Path,
    out_report_f: Path,
    max_workers: int | None = None,
) -> None:

    items: list[(VerifierItem, str)] = []
    for in_r in answer_rows:
        if 'code' not in in_r:
            continue

        idx = in_r['idx']
        key = str(idx)
        ds_r = ds_by_idx[idx]
        items.append((VerifierItem(
            key=key,
            io_examples=ds_r.inputs.examples,
            code=in_r['code'],
        ), key))

    def prepare_workdir(
        item: VerifierItem,
        local_workdir: Path,
    ) -> None:
        assert local_workdir.exists(), f'expected to exist: {local_workdir}'
        # need to pass dirs_exist_ok since the *root dir* always exists.
        shutil.copytree(verifier_template_dir, local_workdir, dirs_exist_ok=True)
        jsonable_io_examples = [{
            'input': example.input,
            'output': example.output,
        } for example in item.io_examples]
        fl.ser.json_dumpf(jsonable_io_examples, local_workdir/'examples.json')
        fl.ser.str_dumpf(item.code, local_workdir/'snippet.lua')

    run_items_in_workdir_containers(
        executor_image_name='think-with-feedback-lua-executor',
        inputs=items,
        prepare_workdir=prepare_workdir,
        execution_args=ExecutionArgs(
            executor_args=['python3', '/workdir/test_harness.py'],
            max_workers=max_workers,
            report_path=out_report_f,
        ),
    )


@app.command()
def extract_answers(
    expect_thinks: Annotated[bool, typer.Option()],
    extend_run: Path | None = None,
    force: bool = False,
):
    ctx = StepCtx(extend_run, force=force)

    fl.ser.jsonl_dumpf(
        gen_answer_rows(
            fl.ser.jsonl_streamf(ctx.dep_responses_f),
            expect_thinks=expect_thinks,
        ),
        ctx.out_answers_f,
    )
    logger.success('Wrote: {}', fl.cwd_rel(ctx.out_answers_f))


@app.command()
def verify_answers(
    extend_run: Path | None = None,
    force: bool = False,
    max_workers: int | None = None,
):
    ctx = StepCtx(extend_run, force=True)
    if not force and ctx.out_report_f.exists():
        logger.error('Command was already ran, pass --force to overwrite the existing result: {}', ctx.out_report_f)
        return

    ds_by_idx = {
        r.idx: r
        for r in fl.ser.model_jsonl_streamf(solutions_py.SolutionsRow, ctx.dep_ds_f)
    }

    run_answer_verifier(
        answer_rows=fl.ser.jsonl_streamf(ctx.out_answers_f),
        ds_by_idx=ds_by_idx,
        verifier_template_dir=ctx.rsrc_d/'verifier-template',
        out_report_f=ctx.out_report_f,
        max_workers=max_workers,
    )
    logger.success('Wrote: {}', fl.cwd_rel(ctx.out_report_f))


@app.command()
def main(
    expect_thinks: Annotated[bool, typer.Option()],
    extend_run: Path | None = None,
    force: bool = False,
    max_workers: int | None = None,
):
    extract_answers(expect_thinks, extend_run, force)
    verify_answers(extend_run, force, max_workers)


if __name__ == '__main__':
    app()
