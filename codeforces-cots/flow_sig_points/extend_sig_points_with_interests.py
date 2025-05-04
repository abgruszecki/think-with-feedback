#!/usr/bin/env python3
import os
from pathlib import Path
from typing import Iterable, Iterator

import typer

from py_shared import ser


app = typer.Typer()


tag_suffix = ''
if tag := os.environ.get('STEP_TAG'):
    tag_suffix = f'+{tag}'
flow_outd = Path(__file__).parent/'out'
step_outd = flow_outd/f'extend_sig_points_with_interests{tag_suffix}'
step_outd.mkdir(parents=True, exist_ok=True)

dep_interest_f = flow_outd/f'find_interest_items{tag_suffix}' / 'result.jsonl'
dep_sig_points_f = flow_outd/f'find_sig_points{tag_suffix}' / 'result.jsonl'

out_simless_indices_f = step_outd / 'ds-simless-row-indices.json'
out_result_f = step_outd / 'result.jsonl'


def gen_extended_sig_point_rows(
    dep_interest_rows: Iterable[dict],
    dep_sig_point_rows: Iterable[dict],
) -> Iterator[dict]:
    interest_items_by_sigpt_idx = {}
    for in_row in dep_interest_rows:
        sigpt_idx = in_row['sigpt_idx']
        for k in ('idx', 'id', 'offset', 'sigpt_idx'):
            del in_row[k]
        interest_items_by_sigpt_idx[sigpt_idx] = in_row

    for sigpt_idx, in_row in enumerate(dep_sig_point_rows):
        extras = interest_items_by_sigpt_idx.get(sigpt_idx, None)
        in_row = in_row.copy()
        if extras:
            in_row['interest'] = (
                extras.get('is_candidate_sim', False)
                or extras.get('is_answer_sim', False)
            )
            in_row.update(extras)
        else:
            in_row['interest'] = False
        yield in_row


@app.command()
def main():
    all_indices = set()
    interest_indices = set()
    with out_result_f.open('w') as out_fh:
        for r in gen_extended_sig_point_rows(
            ser.jsonl_streamf(dep_interest_f),
            ser.jsonl_streamf(dep_sig_points_f),
        ):
            idx = r['idx']
            if r['interest']:
                interest_indices.add(idx)
            all_indices.add(idx)
            print(ser.json.dumps(r), file=out_fh)

    with out_simless_indices_f.open('w') as out_fh:
        ser.json.dump(
            list(i for i in all_indices if i not in interest_indices),
            out_fh,
        )


if __name__ == '__main__':
    app()
