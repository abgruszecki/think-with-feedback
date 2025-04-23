#!/usr/bin/env python3
from io import StringIO
import json
import os
from pathlib import Path
import re
from typing import Iterator, Literal

from loguru import logger

from py_shared import ser


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


def gen_processed_extended_sigpts(
    dep_ds_f: Path,
    dep_ext_sigpts_f: Path,
) -> Iterator[dict]:
    ds_by_idx = {in_r['idx']: in_r for in_r in ser.jsonl_streamf(dep_ds_f)}

    def make_r(
        in_r: dict,
        code: str,
        candidate_offset: int | None,
    ):
        raw_numerators = in_r.get('nums', None)
        if raw_numerators is None:
            if basic_raw_numerator := in_r['extra'].get('num'):
                raw_numerators = [basic_raw_numerator]
        numerators = []
        for num_str in raw_numerators or []:
            if num := numerator_to_int(num_str):
                numerators.append(num)
            else:
                logger.warning('Bad numerator: {}/{}, num={}', in_r['idx'], in_r['offset'], num_str)

        # TODO update the downstream scripts to use `nums` and remove this
        old_num = numerators[0] if numerators else None
        if basic_raw_numerator := in_r['extra'].get('num'):
            old_num = numerator_to_int(basic_raw_numerator)

        r = {
            'idx': in_r['idx'],
            'offset': in_r['offset'],
            'merge_count': in_r.get('merge_count'),
            'new_nums': numerators,
            'num': old_num,
            'candidate_offset': candidate_offset,
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

    def gen_processed_batch(batch: list[dict]) -> Iterator[dict]:
        last_code = None
        last_code_offset = None
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

        def gen_emitted_r(in_r: dict):
            nonlocal last_code, last_code_offset
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
            yield make_r(in_r, code, candidate_offset=last_code_offset)

        def merged_buffered_rows() -> dict:
            assert buffered_rows
            str_buf = StringIO()
            num_buf = []
            for in_r in buffered_rows:
                print(in_r['text'], file=str_buf)
                if num := in_r['extra'].get('num'):
                    if not next((True for n in num_buf if n == num), False):
                        num_buf.append(num)
            buffered_r0 = buffered_rows[0].copy()
            buffered_r0['text'] = str_buf.getvalue()
            buffered_r0['merge_count'] = len(buffered_rows)
            buffered_r0['nums'] = num_buf
            return buffered_r0

        def gen_emitted_buffer():
            if buffered_rows:
                yield from gen_emitted_r(merged_buffered_rows())
                clear_buffer()

        for in_r in batch:
            tp = in_r['type']
            if tp == 'code':
                yield from gen_emitted_buffer()
                last_code = in_r['text']
                last_code_offset = in_r['offset']
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
                yield from gen_emitted_buffer()

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
                # TODO maybe row/buffer pairs with the same numerator should always be merged?
                if (
                    buffer_tp != in_tp
                    # too many cases in the buffer (don't want to make the model count too much)
                    or buffered_case_num > 2
                    # too much text in the buffer
                    or sum(len(r['text']) for r in buffered_rows) + in_text_len > (
                        # We allow much longer text if the number of cases stays low
                        500 if buffered_case_num > 1 else 2000
                    )
                ):
                    yield from gen_emitted_buffer()

                # if current row should be buffered, do so
                if in_is_bufferable:
                    buffer_tp = in_tp
                    buffer(in_r, not_a_case=in_is_probably_only_text)
                    continue

                buffer(in_r, not_a_case=in_is_probably_only_text)
                in_r = merged_buffered_rows()
                clear_buffer()
            yield from gen_emitted_r(in_r)
        yield from gen_emitted_buffer()

    cur_idx = -1
    cur_batch = []

    for in_r in ser.jsonl_streamf(dep_ext_sigpts_f):
        in_r_idx = in_r['idx']
        if cur_idx != in_r_idx:
            if cur_idx != -1:
                yield from gen_processed_batch(cur_batch)
            cur_batch = []
            cur_idx = in_r_idx

        cur_batch.append(in_r)

    if cur_batch:
        yield from gen_processed_batch(cur_batch)


def main():
    tag_suffix = ''
    if tag := os.environ.get('STEP_TAG'):
        tag_suffix = f'+{tag}'
    flowd = Path(__file__).parent
    flow_outd = flowd/'out'
    dep_ds_f = flow_outd/'fetch_process_solutions_py/report.jsonl'
    dep_ext_sigpts_f = flow_outd/f'extend_sig_points_with_interests{tag_suffix}' / 'result.jsonl'

    out_f = flow_outd/f'extract_simulation_snippets{tag_suffix}' / 'result.jsonl'
    out_f.parent.mkdir(parents=True, exist_ok=True)

    ser.jsonl_dumpf(gen_processed_extended_sigpts(dep_ds_f, dep_ext_sigpts_f), out_f)



if __name__ == '__main__':
    main()
