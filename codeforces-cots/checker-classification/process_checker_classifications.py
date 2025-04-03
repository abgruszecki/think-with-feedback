import json
from pathlib import Path


from loguru import logger


from py_shared.json_finder import find_json


def jsonl_streamf(pathlike):
    with open(pathlike, 'r') as fh:
        for line in fh:
            yield json.loads(line)


def jsonl_loadf(pathlike):
    return list(jsonl_streamf(pathlike))


root_ds_d = Path('./datasets')
root_out_d = Path('./out')
raw_checker_ds = root_ds_d / 'raw-checker-classifications.jsonl'
root_out_d.mkdir(parents=True, exist_ok=True)
outf = root_out_d / '1--processed-checker-classifications.jsonl'


from os import environ as env
if __name__ == '__main__' and 'NOGO' not in env:
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
        for in_r in jsonl_streamf(raw_checker_ds):
            in_r_idx = in_r['idx']
            if cur_idx != in_r_idx:
                if cur_idx != -1:
                    process_batch(cur_batch, out_fh)
                cur_batch = []
                cur_idx = in_r_idx

            cur_batch.append(in_r)

        if cur_batch:
            process_batch(cur_batch, out_fh)
