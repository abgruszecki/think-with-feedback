#!/usr/bin/env python3
import os
from pathlib import Path
import json

from loguru import logger

from py_shared import ser

tag_suffix = ''
if tag := os.environ.get('STEP_TAG'):
    tag_suffix = f'+{tag}'
flow_outd = Path(__file__).parent/'out'
step_outd = flow_outd/f'find_interest_items{tag_suffix}'
step_outd.mkdir(parents=True, exist_ok=True)

dep_outd = flow_outd/f'find_sig_points{tag_suffix}'
dep_f = dep_outd / 'result.jsonl'

out_f = step_outd / 'result.jsonl'


if __name__ == '__main__':
    def process_batch(batch: list[dict], out_fh):
        b0 = batch[0]

        default_sim_attrs = {
            'is_candidate_sim': False,
            'is_answer_sim': False,
            # 'is_caseless_sim': False,
        }
        last_sim_attrs = None

        r_tmpl = {
            'idx': b0['idx'],
            'offset': -1, # a placeholder for key ordering
            'sigpt_idx': -1, # a placeholder for key ordering
            'id': b0['id'],
        }
        r_tmpl.update(default_sim_attrs)

        rows = []
        code_end_distance = -1
        cur_tp = None
        # TODO fix: this is wrong in general, one point can have many attributes
        # it's ok for now because is_candidate_sim and is_answer_sim are exclusive
        # TODO (more important): this script should just output all the sigpt cols
        # (and extend_sig_points_with_interests should just be deleted)
        def add_row(in_r: dict, updates: dict):
            nonlocal last_sim_attrs
            if in_r['type'] == 'sim':
                last_sim_attrs = default_sim_attrs.copy()
                last_sim_attrs.update(updates)
            if not in_r['text'] or in_r['text'].isspace():
                return
            r = r_tmpl.copy()
            for k in ('offset', 'sigpt_idx'):
                r[k] = in_r[k]
            r.update(updates)
            rows.append(r)

        for i in range(len(batch)):
            cur = batch[i]
            cur_tp = cur['type']
            if cur_tp in ('code-end', 'start', 'response-proper'):
                code_end_distance = 0 if cur_tp == 'code-end' else -1
                last_sim_attrs = None
            elif cur_tp != 'sim':
                if code_end_distance > -1:
                    code_end_distance += cur['rel_offset']
                if last_sim_attrs and (
                    cur_tp == 'case'
                    or cur_tp == 'post-reflection' and last_sim_affects_reflection
                ):
                    if ((
                            last_sim_attrs['is_candidate_sim']
                            and -1 < code_end_distance <= (2000 + 3000)
                        ) or (
                            last_sim_attrs['is_answer_sim'] # defensive coding, ATTW always true
                        )
                    ):
                        match cur_tp:
                            case 'case':
                                last_sim_affects_reflection = True
                            case 'post-reflection':
                                last_sim_affects_reflection = False
                            case _:
                                # defensive coding...
                                raise ValueError(f'Unexpected sig point type: {cur_tp}')
                        add_row(cur, last_sim_attrs)
            else:
                last_sim_attrs = None
                last_sim_affects_reflection = True

                is_candidate_sim = False
                if code_end_distance > -1:
                    code_end_distance += cur['rel_offset']
                    if code_end_distance < 2000:
                        is_candidate_sim = True
                        add_row(cur, {'is_candidate_sim': True})

                sim_cases = 0
                thinks_end_distance = 0
                do_count_cases = True
                do_measure_thinks_end_distance = True
                for j in range(i + 1, len(batch)):
                    nested = batch[j]
                    nested_tp = nested['type']
                    nested_rel_offset = nested['rel_offset']
                    if nested_tp == 'case':
                        if do_count_cases:
                            sim_cases += 1
                        if do_measure_thinks_end_distance:
                            thinks_end_distance += nested_rel_offset
                    elif nested_tp in ('code', 'code-end', 'sim', 'post-reflection', 'response-proper'):
                        # we go here for 'code' because in rare cases we're inside a code block already
                        do_count_cases = False
                        if nested_tp in ('code', 'sim'):
                            do_measure_thinks_end_distance = False
                        elif do_measure_thinks_end_distance:
                            thinks_end_distance += nested_rel_offset
                        if nested_tp == 'response-proper':
                            # NOTE we don't break at post-reflection because a case may follow
                            break
                    else:
                        # comment out if this is trouble
                        raise ValueError(f'Unexpected sig point type: {nested["type"]}')

                if not is_candidate_sim and do_measure_thinks_end_distance and thinks_end_distance < 2500:
                    add_row(cur, {'is_answer_sim': True})

        for r in rows:
            print(json.dumps(r), file=out_fh)

    cur_idx = -1
    cur_batch = []

    with out_f.open('w') as out_fh:
        for sigpt_idx, in_r in enumerate(ser.jsonl_streamf(dep_f)):
            in_r_idx = in_r['idx'] # this is the dataset idx
            in_r['sigpt_idx'] = sigpt_idx
            if cur_idx != in_r_idx:
                if cur_idx != -1:
                    process_batch(cur_batch, out_fh)
                cur_batch = []
                cur_idx = in_r_idx

            cur_batch.append(in_r)

        if cur_batch:
            process_batch(cur_batch, out_fh)
