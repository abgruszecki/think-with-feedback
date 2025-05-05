#!/usr/bin/env python3
from typing import Iterable, Iterator

from loguru import logger
import typer

from py_shared import ser
import py_shared.flow as fl

app = typer.Typer()


def gen_interest_item_rows(
    data_rows: Iterable[dict],
) -> Iterator[dict]:
    def process_batch(batch: list[dict]):
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

        last_sim_affects_reflection = False
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
                elif cur_tp == 'case':
                    if -1 < code_end_distance < 2000:
                        # NOTE These points *maybe* could be candidate simulations,
                        # but I didn't really investigate that. So for the time being,
                        # they're only marked as "simless cases" to be investigated later.
                        add_row(cur, {
                            # 'is_candidate_sim': True,
                            'is_simless_case': True,
                        })
            else:
                last_sim_attrs = None
                last_sim_affects_reflection = True

                is_candidate_sim = False
                if code_end_distance > -1:
                    code_end_distance += cur['rel_offset']
                    if code_end_distance < 2000:
                        is_candidate_sim = True
                        add_row(cur, {'is_candidate_sim': True})
                        continue

                # NOTE this loop also can calculate the # of cases for a sim,
                # but that's commented out since it doesn't seem interesting right now.
                # To re-enable it, remember to also remove the 'continue' above.
                # sim_cases = 0
                thinks_end_distance = 0
                # keep_counting_cases = True
                keep_measuring_thinks_end_dist = True
                for j in range(i + 1, len(batch)):
                    nested = batch[j]
                    nested_tp = nested['type']
                    nested_rel_offset = nested['rel_offset']
                    if nested_tp == 'case':
                        # if keep_counting_cases:
                        #     sim_cases += 1
                        if keep_measuring_thinks_end_dist:
                            thinks_end_distance += nested_rel_offset
                    elif nested_tp in ('code', 'code-end', 'sim', 'post-reflection', 'response-proper'):
                        # we go here for 'code' because in rare cases we're inside a code block already
                        # keep_counting_cases = False
                        if nested_tp in ('code', 'sim'):
                            keep_measuring_thinks_end_dist = False
                        elif keep_measuring_thinks_end_dist:
                            thinks_end_distance += nested_rel_offset
                        if nested_tp == 'response-proper':
                            # NOTE we don't break at post-reflection because a case may follow
                            break
                    else:
                        # comment out if this is trouble
                        raise ValueError(f'Unexpected sig point type: {nested["type"]}')

                if not is_candidate_sim and keep_measuring_thinks_end_dist and thinks_end_distance < 2500:
                    add_row(cur, {'is_answer_sim': True})

        for r in rows:
            yield r

    cur_idx = -1
    cur_batch = []

    for sigpt_idx, in_r in enumerate(data_rows):
        in_r_idx = in_r['idx'] # this is the dataset idx
        in_r['sigpt_idx'] = sigpt_idx
        if cur_idx != in_r_idx:
            if cur_idx != -1:
                yield from process_batch(cur_batch)
            cur_batch = []
            cur_idx = in_r_idx

        cur_batch.append(in_r)

    if cur_batch:
        yield from process_batch(cur_batch)


@app.command()
def main():
    ctx = fl.dirs(__file__)
    dep_f = ctx.flow_outd/'find_sig_points/result.jsonl'
    out_f = ctx.step_outd/'result.jsonl'

    with out_f.open('w') as out_fh:
        for r in gen_interest_item_rows(ser.jsonl_streamf(dep_f)):
            print(ser.json.dumps(r), file=out_fh)
    logger.success('Wrote: {}', fl.cwd_rel(out_f))


if __name__ == '__main__':
    app()
