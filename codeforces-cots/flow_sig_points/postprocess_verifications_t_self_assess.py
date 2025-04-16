#!/usr/bin/env python3
from collections import namedtuple
import json
from pathlib import Path
import shutil
from typing import Annotated

from loguru import logger
import typer

from py_shared import ser
from py_shared.misc import step_dirs


item_t = namedtuple('item_t', ['code', 'examples'])

app = typer.Typer()


@app.command()
def main(
    input_data: Annotated[Path, typer.Option()],
    verification_report: Annotated[Path, typer.Option()],
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
    out_f = step_outd/f'{run_id}/report.jsonl'
    out_f.parent.mkdir(parents=True, exist_ok=True)

    def _input_data_kvgen():
        for r in ser.jsonl_streamf(input_data):
            yield (r['idx'], r['offset'], r['case_idx']), r
    input_data_dict = dict(_input_data_kvgen())

    with open(out_f, 'w') as out_fh:
        for report_r in ser.jsonl_streamf(verification_report):
            key_parts = report_r['item'].split('_')
            idx = int(key_parts[0])
            offset = int(key_parts[1])
            case_idx = int(key_parts[2])

            original_input_r = input_data_dict[(idx, offset, case_idx)]
            out_r = {
                'idx': idx,
                'offset': offset,
                'case_idx': case_idx,
            }
            out_r.update(original_input_r)
            out_r.update(report_r)
            print(json.dumps(out_r), file=out_fh)
    logger.success('Wrote: {}', out_f.relative_to(flowd))


if __name__ == '__main__':
    app()
