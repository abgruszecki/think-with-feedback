import json
from pathlib import Path

from loguru import logger
import typer

from py_shared import ser
from py_shared.json_finder import find_json


app = typer.Typer()


subproject_d = Path('flow_checker_classification')
assert subproject_d.exists(), 'this looks like the wrong dir'
root_ds_d = subproject_d/'datasets'
root_out_d = subproject_d/'out'
raw_checker_ds = root_ds_d / 'raw-checker-classifications.jsonl'
root_out_d.mkdir(parents=True, exist_ok=True)
outf = root_out_d / '1--processed-checker-classifications.jsonl'


@app.command()
def main(
    input: Path = raw_checker_ds,
):
    def process_batch(
        batch: list[dict],
        out_fh,
    ):
        b0 = batch[0]
        votes = []
        responses = []
        r = {
            'id': b0['id'],
            'idx': b0['idx'],
            'prompt': b0['prompt'],
            'votes': votes,
            'responses': responses,
        }
        for in_r in batch:
            r_resp = in_r['response']
            responses.append(r_resp)

            r_answer_str = find_json(r_resp, skip_thinks=False)
            if r_answer_str is None:
                logger.warning('No answer found for {}/{} (id={})', in_r['idx'], in_r['gen_idx'], in_r['id'])
                votes.append(None)
                continue

            try:
                r_answer_obj = json.loads(r_answer_str)['type']
                assert r_answer_obj in {'diff', 'checker', 'interaction'}
                votes.append(r_answer_obj)
            except Exception as e:
                logger.exception('Error parsing answer for {}/{} (id={})', in_r['idx'], in_r['gen_idx'], in_r['id'])
                votes.append(None)
        json.dump(r, out_fh)
        print(file=out_fh)

    cur_idx = -1
    cur_batch = []

    with outf.open('w') as out_fh:
        for in_r in ser.jsonl_streamf(input):
            in_r_idx = in_r['idx']
            if cur_idx != in_r_idx:
                if cur_idx != -1:
                    process_batch(cur_batch, out_fh)
                cur_batch = []
                cur_idx = in_r_idx

            cur_batch.append(in_r)

        if cur_batch:
            process_batch(cur_batch, out_fh)


from os import environ as env
if __name__ == '__main__' and 'NOGO' not in env:
    app()
