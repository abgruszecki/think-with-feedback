#!/usr/bin/env python3
from pathlib import Path
import json

from loguru import logger

from py_shared import ser


flow_outd = Path(__file__).parent/'out'
dep_outd = flow_outd/'find_sig_points'
step_outd = flow_outd/'find_interest_items'
step_outd.mkdir(parents=True, exist_ok=True)
dep_f = dep_outd / 'result.jsonl'
out_f = step_outd / 'result.jsonl'


if __name__ == '__main__':
    def process_batch(batch: list[dict], out_fh):
        b0 = batch[0]
        r_tmpl = {
            'idx': b0['idx'],
            'id': b0['id'],
            'offset': -1, # here just for key ordering
            'is_candidate_sim': False,
            'is_answer_sim': False,
            # 'is_caseless_sim': False,
        }
        rows = []
        # TODO fix: this is wrong in general, one point can have many props
        # it's ok for now because is_candidate_sim and is_answer_sim are exclusive
        def add_row(in_r: dict, updates: dict):
            r = r_tmpl.copy()
            r['offset'] = in_r['offset']
            r.update(updates)
            rows.append(r)

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
                code_end_distance += cur['rel_offset']
                if code_end_distance < 2000:
                    cand_sim = True
                    add_row(cur, {'is_candidate_sim': True})
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

                # See comment in find_sig_points.py, grep @case
                # if sim_cases == 0:
                #     r['has_caseless_sim'] = True
                if not cand_sim and do_measure_thinks_end_distance and thinks_end_distance < 2500:
                    # logger.warning('here! {}', thinks_end_distance)
                    add_row(cur, {'is_answer_sim': True})

        for r in rows:
            print(json.dumps(r), file=out_fh)

    cur_idx = -1
    cur_batch = []

    with out_f.open('w') as out_fh:
        for in_r in ser.jsonl_streamf(dep_f):
            in_r_idx = in_r['idx']
            if cur_idx != in_r_idx:
                if cur_idx != -1:
                    process_batch(cur_batch, out_fh)
                cur_batch = []
                cur_idx = in_r_idx

            cur_batch.append(in_r)

        if cur_batch:
            process_batch(cur_batch, out_fh)
