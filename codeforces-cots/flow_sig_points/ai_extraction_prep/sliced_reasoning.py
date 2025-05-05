#!/usr/bin/env python3
from io import StringIO
import json
import os
from pathlib import Path
import regex as reg
from typing import Any, Iterable, Iterator, Literal

from loguru import logger
import typer

from py_shared import ser
from py_shared.misc import step_dirs

app = typer.Typer()


py_indent_re = reg.compile(r'^ *')
double_nl_rev_rx = reg.compile(r'\n\n', reg.REVERSE)
xml_tag_rx = reg.compile(r'<(/)?(\w+)( [^>\n]*)?>')
nonws_rx = reg.compile(r'\S')
nonws_rev_rx = reg.compile(r'\S', reg.REVERSE)


def find_preceding_par_start(
    haystack: str,
    pos: int,
) -> int:
    m = double_nl_rev_rx.search(haystack, endpos=pos)
    return m.end() if m else -1


def gen_tag_contents(
    haystack: str,
    tag_name: str
) -> Iterator[str]:
    last_opening_idx = -1
    for m in xml_tag_rx.finditer(haystack):
        group1 = m.group(1)
        if group1 and last_opening_idx != -1:
            startpos = last_opening_idx
            endpos = m.start()
            if m1 := nonws_rx.search(haystack, startpos, endpos):
                startpos = m1.start()
            if m1 := nonws_rev_rx.search(haystack, startpos, endpos):
                endpos = m1.end()
            yield haystack[startpos:endpos]
            last_opening_idx = -1
        elif not group1:
            last_opening_idx = m.end() if m.group(2) == tag_name else -1


def remove_indent(code: str) -> str:
    out_buf = StringIO()
    first_indent: str | None = None
    for line in code.splitlines():
        if first_indent is None:
            m = py_indent_re.match(line)
            assert m # TODO I should find a way encapsulate this
            first_indent = m.group(0)
        print(line.removeprefix(first_indent), file=out_buf)
    return out_buf.getvalue()


def finalize_row(
    in_r: dict,
    code: str,
    candidate_offset: int | None,
    ds_by_idx: dict[int, dict] | None,
):
    idx = in_r['idx']
    offset = in_r['offset']
    cleaned_code = remove_indent(code)

    r = {
        'idx': idx,
        'offset': offset,
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


def gen_processed_batch(
    batch: list[dict],
    ds_by_idx: dict[int, dict],
) -> Iterator[dict]:
    if len(batch) == 1:
        # in this case the only row contains the entire CoT and we return the tail paragraphs,
        # since they may contain simulated execution of the answer code
        b0 = batch[0]
        idx = b0['idx']
        offset = b0['offset']
        final_answer = ds_by_idx[idx]['final_answer']
        if final_answer is None:
            # Too many items don't have a final answer.
            # TODO we should just accumulate these keys in a separate file
            logger.warning('No final answer for: {}/{}', idx, offset)
            return

        text = b0['text']
        startpos = len(text) - 5000
        if startpos > 0:
            startpos = find_preceding_par_start(text, startpos)
            if startpos != -1:
                b0 = b0.copy()
                b0['text'] = text[startpos:]
        yield finalize_row(b0, final_answer, candidate_offset=None, ds_by_idx=ds_by_idx)

    last_code: str | None = None
    last_code_offset: int | None = None

    for in_r in batch:
        tp = in_r['type']
        if tp == 'code':
            last_code = in_r['text']
            last_code_offset = in_r['offset']
            continue
        elif tp == 'code-end':
            assert last_code is not None
            yield finalize_row(in_r, last_code, last_code_offset, ds_by_idx=ds_by_idx)
        elif tp != 'start':
            raise ValueError('Unexpected row type: {}/{}', in_r['idx'], in_r['offset'])


def gen_reasoning_rows(
    dep_ds_rows: Iterable[dict],
    dep_ext_sigpt_rows: Iterable[dict],
) -> Iterator[dict]:
    ds_by_idx = {in_r['idx']: in_r for in_r in dep_ds_rows}

    cur_idx = -1
    cur_batch = []

    for in_r in dep_ext_sigpt_rows:
        in_r_idx = in_r['idx']
        if cur_idx != in_r_idx:
            if cur_idx != -1:
                yield from gen_processed_batch(cur_batch, ds_by_idx=ds_by_idx)
            cur_batch = []
            cur_idx = in_r_idx

        cur_batch.append(in_r)

    if cur_batch:
        yield from gen_processed_batch(cur_batch, ds_by_idx=ds_by_idx)


@app.command()
def main():
    _, flow_outd, substep_outd = step_dirs(__file__)
    subflow_outd = substep_outd.parent

    dep_ds_f = flow_outd/'fetch_process_solutions_py/report.jsonl'
    dep_ext_sigpts_f = subflow_outd/'extend_sig_points_with_interests/result.jsonl'

    out_f = substep_outd/'result.jsonl'

    ser.jsonl_dumpf(
        gen_reasoning_rows(
            ser.jsonl_streamf(dep_ds_f),
            ser.jsonl_streamf(dep_ext_sigpts_f),
        ),
        out_f,
    )



if __name__ == '__main__':
    app()
