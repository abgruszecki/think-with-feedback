#!/usr/bin/env python3
import json
from pathlib import Path
import sys

from loguru import logger
import typer

from py_shared import ser
import py_shared.flow as fl
from py_shared.json_finder import find_json

app = typer.Typer()


flow_outd = Path(__file__).parent/'out'
step_outd = flow_outd/'extract_checker_type'
step_outd.mkdir(parents=True, exist_ok=True)
outf = step_outd / 'checker-types.jsonl'


@app.command()
def main(
    range: str = 'normal',
):
    valid_ranges = ('normal', 'full')
    if range not in valid_ranges:
        raise typer.BadParameter(f'--range was {range!r}, but should be one of: {valid_ranges!r}')

    selector = '' if range == 'normal' else '[:1000]'
    split = f'train{selector}'

    import datasets
    ds = datasets.load_dataset('open-r1/codeforces-cots', 'solutions_py', split=split)
    wanted_ids_list = []
    wanted_ids_set = set()
    for r in ds:
        wanted_ids_list.append(r['id'])
        wanted_ids_set.add(r['id'])

    checker_ds = datasets.load_dataset('open-r1/codeforces-cots', 'checker_interactor', split='train')
    checker_dict = {
        r['id']: r['generation'] for r in checker_ds if r['id'] in wanted_ids_set
    }

    def gen_output_rows():
        for row_idx, row_id in enumerate(wanted_ids_list):
            r = {'idx': row_idx, 'id': row_id }

            json_str = find_json(checker_dict[row_id])
            if json_str is None:
                logger.warning('No JSON found at {}', row_idx)
                continue

            try:
                json_obj = json.loads(json_str)
            except Exception as e:
                logger.warning('Error parsing JSON at {}: {}', row_idx, e)
                continue

            r.update(json_obj)
            yield r

    ser.jsonl_dumpf(gen_output_rows(), outf)
    logger.success('Wrote: {}', fl.cwd_rel(outf))


from os import environ as env
if __name__ == '__main__' and 'NOGO' not in env:
    app()
