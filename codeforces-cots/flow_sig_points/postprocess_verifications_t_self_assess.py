#!/usr/bin/env python3
from collections import namedtuple
import json
from pathlib import Path
import shutil
from typing import Annotated, Iterator

from loguru import logger
import typer

from py_shared import ser
from py_shared.misc import step_dirs


item_t = namedtuple('item_t', ['code', 'examples'])

app = typer.Typer()


def gen_joined_rows(
    verification_report_rows: Iterator[dict],
    input_data_dict: dict,
    snippet_data_dict: dict | None,
) -> Iterator[dict]:
    for report_r in verification_report_rows:
        key_parts = report_r['item'].split('_')
        idx = int(key_parts[0])
        offset = int(key_parts[1])
        case_idx = int(key_parts[2])

        out_r = {
            'idx': idx,
            'offset': offset,
            'case_idx': case_idx,
        }
        out_r.update(input_data_dict[(idx, offset, case_idx)])
        if snippet_data_dict:
            snippet_data_r = snippet_data_dict.get((idx, offset))
            if snippet_data_r:
                for k in ('candidate_offset',):
                    out_r[k] = snippet_data_r[k]
            else:
                logger.warning('no snippet data for: {}', report_r['item'])
                continue
        out_r.update(report_r)
        yield out_r


@app.command()
def main(
    input_data: Annotated[Path, typer.Option()],
    verification_report: Annotated[Path, typer.Option()],
    add_sigpt_data: bool = False
):
    assert verification_report.is_file(), f'expected a file: {verification_report}'
    assert input_data.is_file(), f'expected a file: {input_data}'

    data_run_d = verification_report.parent
    data_step_outd = data_run_d.parent
    run_id = data_run_d.stem
    tag = data_step_outd.stem.split('+', 1)[-1]
    logger.info('run_id: {}, tag: {}', run_id, tag)
    assert run_id == input_data.parent.stem
    assert tag == input_data.parent.parent.stem.split('+', 1)[-1]
    assert tag == 'self-assess'

    flowd, flow_outd, step_outd = step_dirs(__file__, tag)
    opt_dep_snippet_data_f = flow_outd/'extract_simulation_snippets/result.jsonl'

    out_f = step_outd/f'{run_id}/report.jsonl'
    out_f.parent.mkdir(parents=True, exist_ok=True)

    def _input_data_kvgen():
        for r in ser.jsonl_streamf(input_data):
            yield (r['idx'], r['offset'], r['case_idx']), r
    input_data_dict = dict(_input_data_kvgen())

    snippet_data_dict = None
    if add_sigpt_data:
        def _sigpt_data_kvgen():
            for r in ser.jsonl_streamf(opt_dep_snippet_data_f):
                yield (r['idx'], r['offset']), r
        snippet_data_dict = dict(_sigpt_data_kvgen())

    ser.jsonl_dumpf(
        gen_joined_rows(
            ser.jsonl_streamf(verification_report),
            input_data_dict,
            snippet_data_dict,
        ),
        out_f,
    )
    logger.success('Wrote: {}', out_f.relative_to(flowd))


if __name__ == '__main__':
    app()
