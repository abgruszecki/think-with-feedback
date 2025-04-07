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
            'has_candidate_sim': False,
            # 'has_code_sim500': False,
            # 'has_code_sim1500': False,
            'has_answer_sim': False,
            'has_caseless_sim': False,
            # 'has_sim_in_code': False,
        }
        r = {}

        code_end_distance = 0
        for i in range(len(batch)):
            cur = batch[i]
            cur_tp = cur['type']
            if cur_tp in ('code-end', 'start', 'response-proper'):
                code_end_distance = 0
            elif cur_tp != 'sim':
                code_end_distance += cur['rel_offset']
            else:
                prev = batch[i - 1]
                cand_sim = False
                if code_end_distance < 2000:
                    cand_sim = True
                    r['has_candidate_sim'] = True
                sim_cases = 0
                thinks_end_distance = 0
                do_count_cases = True
                do_measure_thinks_end_distance = True
                # saw_code = False
                for j in range(i + 1, len(batch)):
                    nested = batch[j]
                    nested_tp = nested['type']
                    nested_rel_offset = nested['rel_offset']
                    if nested_tp == 'case':
                        if do_measure_thinks_end_distance:
                            thinks_end_distance += nested_rel_offset
                        if do_count_cases:
                            sim_cases += 1
                    elif nested_tp in ('code', 'code-end', 'sim', 'response-proper'):
                        # we go here for 'code' because in rare cases we're inside a code block already
                        do_count_cases = False
                        if nested_tp in ('code', 'sim'):
                            do_measure_thinks_end_distance = False
                        elif do_measure_thinks_end_distance:
                            thinks_end_distance += nested_rel_offset
                        if nested_tp == 'response-proper':
                            break
                    else:
                        # comment out if this is trouble
                        raise ValueError(f'Unexpected sig point type: {nested["type"]}')

                if sim_cases == 0:
                    r['has_caseless_sim'] = True
                if not cand_sim and do_measure_thinks_end_distance and thinks_end_distance < 2500:
                    r['has_answer_sim'] = True

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
