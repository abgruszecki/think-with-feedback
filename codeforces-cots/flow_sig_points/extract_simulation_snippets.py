#!/usr/bin/env python3
from io import StringIO
from pathlib import Path
import re
from typing import Iterator, Literal

from loguru import logger

from py_shared import ser
import py_shared.flow as fl


py_indent_re = re.compile(r'^ *')


def remove_indent(code: str) -> str:
    out_buf = StringIO()
    first_indent: str | None = None
    for line in code.splitlines():
        if first_indent is None:
            first_indent = py_indent_re.match(line).group(0)
        print(line.removeprefix(first_indent), file=out_buf)
    return out_buf.getvalue()


_number_rx = re.compile(r'\d+')
_numeral_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
def numeral_to_int(s: str) -> int | None:
    if m := _number_rx.search(s):
        return int(m.group(0))
    s_low = s.lower()
    for i, n_str in enumerate(_numeral_list):
        if s_low == n_str:
            return i + 1
    return None


def finalize_row(
    in_r: dict,
    code: str,
    candidate_offset: int | None,
    ds_by_idx: dict[int, dict] | None,
):
    raw_numerals = in_r.get('nums', None)
    if raw_numerals is None:
        if basic_raw_numeral := in_r['extra'].get('num'):
            raw_numerals = [basic_raw_numeral]
    numerals = []
    for num_str in raw_numerals or []:
        if num := numeral_to_int(num_str):
            if num in numerals:
                continue
            numerals.append(num)
        else:
            logger.warning('Bad numeral: {}/{}, num={}', in_r['idx'], in_r['offset'], num_str)

    idx = in_r['idx']
    offset = in_r['offset']
    cleaned_code = remove_indent(code)

    r = {
        'idx': idx,
        'offset': offset,
        'merge_count': in_r.get('merge_count'),
        'nums': numerals,
        'candidate_offset': candidate_offset,
        'code': cleaned_code,
    }
    if ds_by_idx:
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

def gen_snippet_rows(
    dep_ds_f: Path,
    dep_ext_sigpts_f: Path,
) -> Iterator[dict]:
    ds_by_idx = {in_r['idx']: in_r for in_r in ser.jsonl_streamf(dep_ds_f)}

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
            yield finalize_row(in_r, code, candidate_offset=last_code_offset, ds_by_idx=ds_by_idx)

        def merged_buffered_rows() -> dict:
            assert buffered_rows
            str_buf = StringIO()
            nums = []
            for in_r in buffered_rows:
                if num := in_r['extra'].get('num'):
                    nums.append(num)
                # NOTE It's important not to add any new characters here,
                # some scripts need the snippet's length to exactly match the original text.
                print(in_r['text'], end='', file=str_buf)

            buffered_r0 = buffered_rows[0].copy()
            buffered_r0['text'] = str_buf.getvalue()
            buffered_r0['merge_count'] = len(buffered_rows)
            buffered_r0['nums'] = nums
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
            if buffered_rows and tp == 'sim':
                yield from gen_emitted_buffer()

            in_text_len = len(in_r['text'])
            in_is_bufferable = (
                tp == 'sim' and in_text_len < 100 or tp == 'case' and in_text_len < 80
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
                # TODO maybe row/buffer pairs with the same numeral should always be merged?
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
    sd = fl.dirs(__file__)

    dep_ds_f = sd.flow_outd/'fetch_process_solutions_py/report.jsonl'
    dep_ext_sigpts_f = sd.flow_outd/'extend_sig_points_with_interests'/'result.jsonl'

    out_f = sd.flow_outd/'extract_simulation_snippets'/'result.jsonl'

    ser.jsonl_dumpf(gen_snippet_rows(dep_ds_f, dep_ext_sigpts_f), out_f)



if __name__ == '__main__':
    main()
