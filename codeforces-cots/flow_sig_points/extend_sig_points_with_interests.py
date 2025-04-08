from pathlib import Path

from py_shared import ser


root_outd = Path('./out+v2')
sig_points_f = root_outd / 'x--sig-points.jsonl'
interest_items_f = root_outd / 'x--interest-sig-points-by-idx.jsonl'
outf = root_outd / 'x--sig-points-with-interests.jsonl'


if __name__ == '__main__':
    interest_items_by_idx = {}
    for in_row in ser.jsonl_loadf(interest_items_f):
        idx = in_row['idx']
        del in_row['idx']
        del in_row['id']
        interest_items_by_idx[idx] = in_row

    with outf.open('w') as outf_fh:
        for in_row in ser.jsonl_loadf(sig_points_f):
            extras = interest_items_by_idx.get(in_row['idx'], {})
            in_row.update(extras)
            ser.json.dump(in_row, outf_fh)
            print(file=outf_fh)