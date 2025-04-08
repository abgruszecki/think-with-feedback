#!/usr/bin/env python3
from collections import namedtuple
from pathlib import Path
import shutil

import typer

from dockerinator.run_in_containers import run_items_in_workdir_containers, ExecutionArgs
from py_shared import ser


item_t = namedtuple('item_t', ['snippet', 'examples'])

app = typer.Typer()


@app.command()
def main(max_workers: int | None = None):
    flowd = Path(__file__).parent
    prev_outd = flowd/'out'/'process_solutions_py'
    input_f = prev_outd/'report.jsonl'
    step_outd = flowd/'out'/'exec_snippets_via_workdir'
    step_outd.mkdir(parents=True, exist_ok=True)

    items = []
    for r in ser.jsonl_loadf(input_f):
        r_idx = r['idx']
        examples = r['inputs']['examples']
        if examples is None:
            examples = []
        for candidate_idx, candidate_snippet in enumerate(r['answer_candidates']):
            items.append((item_t(candidate_snippet, examples), f'{r_idx}/candidate-{candidate_idx}'))
        if final_answer := r['final_answer']:
            items.append((item_t(final_answer, examples), f'{r_idx}/final-answer'))

    def prepare_workdir(
        item: item_t,
        local_workdir: Path
    ):
        assert local_workdir.exists(), f'expected to exist: {local_workdir}'
        shutil.copytree(flowd/'checker-resources', local_workdir, dirs_exist_ok=True)
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