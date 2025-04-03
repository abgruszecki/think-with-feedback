from pathlib import Path
import json

from py_shared import ser


root_outd = Path('out+v2')
input_f = root_outd / 'x--sig-points.jsonl'
outf = root_outd / 'x--interest-sig-points-by-idx.jsonl'


if __name__ == '__main__':
    def process_batch(batch: list[dict], out_fh):
        b0 = batch[0]
        r_base = {
            'idx': b0['idx'],
            'id': b0['id'],
            'has_code_sim': False,
            'has_code_sim200': False,
            'has_code_sim500': False,
            'has_caseless_sim': False,
        }
        r = {}

        for i in range(len(batch)):
            cur = batch[i]
            if cur['type'] == 'sim':
                prev = batch[i - 1]
                if prev['type'] == 'code':
                    if cur['rel_offset'] < 100:
                        r['has_code_sim'] = True
                    elif cur['rel_offset'] < 200:
                        r['has_code_sim200'] = True
                    elif cur['rel_offset'] < 500:
                        r['has_code_sim500'] = True
                found_cases = 0
                for j in range(i + 1, len(batch)):
                    nested = batch[j]
                    if nested['type'] == 'case':
                        found_cases += 1
                    elif nested['type'] == 'sim':
                        break
                if found_cases < 0:
                    r['has_caseless_sim'] = True
        if len(r) > 0:
            r_base.update(r)
            json.dump(r_base, out_fh)
            print(file=out_fh)

    cur_idx = -1
    cur_batch = []

    with outf.open('w') as out_fh:
        for in_r in ser.jsonl_streamf(input_f):
            in_r_idx = in_r['idx']
            if cur_idx != in_r_idx:
                if cur_idx != -1:
                    process_batch(cur_batch, out_fh)
                cur_batch = []
                cur_idx = in_r_idx

            cur_batch.append(in_r)

        if cur_batch:
            process_batch(cur_batch, out_fh)
