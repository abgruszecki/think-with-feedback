#!/usr/bin/env python3
from io import StringIO
import json
from pathlib import Path

import typer
from loguru import logger

from py_shared import ser, io_abstractinator
from py_shared.misc import step_dirs, cwd_rel

app = typer.Typer()

# _, flow_outd, step_outd = step_dirs(__file__, tag='self-assess')


# code_list = [r['code'] for r in ser.jsonl_streamf(dep_f)]

# out_list = []
# errs = []
# for idx, code in enumerate(code_list):
#     try:
#         out = io_abstractinator.go2(code, idx)
#         out_list.append(out)
#     except Exception as e:
#         logger.exception('Failed to process code; ctx={}', idx)
#         errs.append((idx, code, e))


# def show_err(e):
#     logger.opt(exception=e).error('Failed to process code')

MAIN_BOILERPLATE = '''

if __name__ == '__main__':
    from sys import stdin, stdout
    main(input_stream=stdin, output_stream=stdout)
'''

@app.command()
def main(
    data: Path,
    skip_main_call: bool = False
):
    data_run_d = data.parent
    data_step_outd = data_run_d.parent
    run_id = data_run_d.stem
    tag = data_step_outd.stem.split('+', 1)[-1]
    logger.info('run_id: {}, tag: {}', run_id, tag)
    assert tag == 'self-assess'

    flowd, flow_outd, step_outd = step_dirs(__file__, tag)
    run_outd = step_outd/(run_id+'+abstracted-io')
    outf = run_outd/'result.jsonl'
    outf.parent.mkdir(parents=True, exist_ok=True)

    with outf.open('w') as out_fh:
        for r in ser.jsonl_streamf(data):
            idx = r['idx']
            offset = r['offset']
            case_idx = r['case_idx']
            key = f'{idx}_{offset}_{case_idx}'

            code = r['code']
            abstracted_code = io_abstractinator.go2(code, idx)
            if abstracted_code is None:
                logger.warning('Failed to process code; ctx={}', key)
                continue

            final_code_buf = StringIO()
            print(abstracted_code, file=final_code_buf)
            if not skip_main_call:
                print(MAIN_BOILERPLATE, file=final_code_buf)

            r['code'] = final_code_buf.getvalue()
            print(json.dumps(r), file=out_fh)
    logger.success('Wrote: {}', cwd_rel(outf))

if __name__ == '__main__':
    app()