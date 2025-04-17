#!/usr/bin/env python3
from io import StringIO
import json
import os
from pathlib import Path
import re
from typing import Literal

from loguru import logger

from py_shared import ser


tag_suffix = ''
if tag := os.environ.get('STEP_TAG'):
    tag_suffix = f'+{tag}'
flowd = Path(__file__).parent
flow_outd = flowd/'out'
dep_ds_f = flow_outd/'fetch_process_solutions_py/report.jsonl'
dep_ext_sigpts_f = flow_outd/f'extend_sig_points_with_interests{tag_suffix}' / 'result.jsonl'

out_f = flow_outd/f'extract_simulation_snippets{tag_suffix}' / 'result.jsonl'
out_f.parent.mkdir(parents=True, exist_ok=True)


ds_by_idx = {in_r['idx']: in_r for in_r in ser.jsonl_streamf(dep_ds_f)}


_number_rx = re.compile(r'\d+')
_numerator_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
def numerator_to_int(s: str) -> int | None:
    if m := _number_rx.search(s):
        return int(m.group(0))
    s_low = s.lower()
    for i, n_str in enumerate(_numerator_list):
        if s_low == n_str:
            return i + 1
    return None


if __name__ == '__main__':
    def make_r(in_r: dict, code: str):
        numerator = in_r['extra'].get('num')
        if numerator is not None:
            numerator = numerator_to_int(numerator)
            if numerator is None:
                logger.warning('Bad numerator: {}/{}, num={}', in_r['idx'], in_r['offset'], numerator)

        r = {
            # k: in_r.get(k) for k in ('idx', 'offset', 'merge_count', 'text')
            'idx': in_r['idx'],
            'offset': in_r['offset'],
            'merge_count': in_r.get('merge_count'),
            'num': numerator,
            'code': code,
        }
        in_r_inputs = ds_by_idx[in_r['idx']]['inputs']
        # TODO this fits better in extract_simulation_cases.py I guess??
        for k in (
            'problem_statement',
            'input_format',
            'output_format',
            'examples',
            'problem_notes',
        ):
            r[k] = in_r_inputs[k]

        r['text'] = in_r['text']
        return r

    def process_batch(batch: list[dict], out_fh):
        last_code = None
        buffer_tp: Literal['candidate', 'answer'] | None = None
        buffered_case_num = 0
        buffered_rows: list[dict] = []
        def buffer(r, not_a_case: bool = False):
            nonlocal buffered_rows, buffered_case_num
            if not not_a_case:
                buffered_case_num += 1
            buffered_rows.append(r)
        def clear_buffer():
            nonlocal buffer_tp, buffered_rows, buffered_case_num
            buffer_tp = None
            buffered_case_num = 0
            buffered_rows.clear()
        def emit(in_r: dict):
            is_candidate_sim = in_r.get('is_candidate_sim', False)
            is_answer_sim = in_r.get('is_answer_sim', False)
            if is_candidate_sim:
                code = last_code
                if code is None:
                    logger.warning('Problem with row {}/{}: last_code is None', in_r['idx'], in_r['offset'])
                    return
            elif is_answer_sim:
                code = ds_by_idx[in_r['idx']]['final_answer']
                if code is None:
                    return
            else:
                logger.error('Bad row type passed to emit: {}/{}, type={}', in_r['idx'], in_r['offset'], in_r['type'])
                return
            print(json.dumps(make_r(in_r, code)), file=out_fh)
        def merge_buffered_rows() -> dict:
            assert buffered_rows
            str_buf = StringIO()
            for in_r in buffered_rows:
                print(in_r['text'], file=str_buf)
            buffered_r0 = buffered_rows[0].copy()
            buffered_r0['text'] = str_buf.getvalue()
            buffered_r0['merge_count'] = len(buffered_rows)
            return buffered_r0
        def emit_buffer():
            if buffered_rows:
                emit(merge_buffered_rows())
                clear_buffer()
                return True
            return False

        for in_r in batch:
            tp = in_r['type']
            if tp == 'code':
                emit_buffer()
                last_code = in_r['text']
                continue

            if tp not in ('sim', 'case'):
                continue

            is_candidate_sim = in_r.get('is_candidate_sim', False)
            is_answer_sim = in_r.get('is_answer_sim', False)

            if not any((is_candidate_sim, is_answer_sim)):
                continue

            # Merge short sims with the following case
            # TODO move this logic to find_sig_points.py
            # TODO don't merge sigpts with different enumerators
            if buffered_rows and tp == 'sim':
                emit_buffer()

            in_text_len = len(in_r['text'])
            in_is_bufferable = (
                tp == 'sim' and in_text_len < 100 and not in_r['extra'].get('is_also_case')
                or tp == 'case' and in_text_len < 80
            )

            if in_is_bufferable or buffered_rows:
                in_is_probably_only_text = \
                    tp == 'sim' and not in_r['extra'].get('is_also_case')
                if is_candidate_sim:
                    in_tp = 'candidate'
                elif is_answer_sim:
                    in_tp = 'answer'
                else:
                    raise ValueError('Missing case for row {}/{}', in_r['idx'], in_r['offset'])

                # emit the buffer if we cannot merge the current row
                if (
                    buffer_tp != in_tp
                    # too many cases in the buffer (don't want to make the model count too much)
                    or buffered_case_num > 2
                    # too much text in the buffer
                    or sum(len(r['text']) for r in buffered_rows) + in_text_len > 500
                ):
                    emit_buffer()

                # if current row should be buffered, do so
                if in_is_bufferable:
                    buffer_tp = in_tp
                    buffer(in_r, not_a_case=in_is_probably_only_text)
                    continue

                buffer(in_r, not_a_case=in_is_probably_only_text)
                in_r = merge_buffered_rows()
                clear_buffer()
            emit(in_r)
        emit_buffer()

    cur_idx = -1
    cur_batch = []

    with out_f.open('w') as out_fh:
        for in_r in ser.jsonl_streamf(dep_ext_sigpts_f):
            in_r_idx = in_r['idx']
            if cur_idx != in_r_idx:
                if cur_idx != -1:
                    process_batch(cur_batch, out_fh)
                cur_batch = []
                cur_idx = in_r_idx

            cur_batch.append(in_r)

        if cur_batch:
            process_batch(cur_batch, out_fh)