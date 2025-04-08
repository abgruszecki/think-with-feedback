#!/usr/bin/env python3
import json
from pathlib import Path

from loguru import logger
import typer

from py_shared import ser
from py_shared.json_finder import find_json


app = typer.Typer()


flowd = Path(__file__).parent
flow_outd = flowd/'out'
dep_outd = flow_outd/'make_checker_classifications'
# dep_outd contains files named like this:
# '{timestamp}--raw-checker-classifications.jsonl'.format(
#     timestamp=datetime.now().strftime('%Y%m%dT%H%M%S'),
# )
# list them all, pair them with the timestamp, and sort by timestamp
dep_out_files = [
    (path, path.stem.split('-', 1)[0])
    for path in dep_outd.glob('*--raw-checker-classifications.jsonl')
]
dep_out_files.sort(key=lambda x: x[1], reverse=True) # earlier first


step_outd = flow_outd/'process_checker_classifications'
step_outd.mkdir(parents=True, exist_ok=True)
outf_template = '{timestamp}--processed-checker-classifications.jsonl'


@app.command()
def main(
    # input: Path = raw_checker_ds,
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
            except Exception:
                logger.exception('Error parsing answer for {}/{} (id={})', in_r['idx'], in_r['gen_idx'], in_r['id'])
                votes.append(None)
        json.dump(r, out_fh)
        print(file=out_fh)

    # TODO consider limiting how many dep files we process
    # We could:
    # - read a CLI arg for the range of files to process (they're sorted by timestamp)
    # - only re-generate outputs which are out-of-date (based on file modification times)
    for dep_out_f, timestamp in dep_out_files:
        outf = step_outd / outf_template.format(timestamp=timestamp)
        cur_idx = -1
        cur_batch = []
        # TODO sort by idx?
        with outf.open('w') as out_fh:
            for in_r in ser.jsonl_streamf(dep_out_f):
                in_r_idx = in_r['idx']
                if cur_idx != in_r_idx:
                    if cur_idx != -1:
                        process_batch(cur_batch, out_fh)
                    cur_batch = []
                    cur_idx = in_r_idx

                cur_batch.append(in_r)

            if cur_batch:
                process_batch(cur_batch, out_fh)
        logger.success('Processed: {}', dep_out_f.relative_to(Path.cwd()))


from os import environ as env
if __name__ == '__main__' and 'NOGO' not in env:
    app()
