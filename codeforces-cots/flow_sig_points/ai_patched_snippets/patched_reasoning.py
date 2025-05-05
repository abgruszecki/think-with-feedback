#!/usr/bin/env python3
from collections import defaultdict, namedtuple
from dataclasses import dataclass
import io
from os import environ
from pathlib import Path
import re
from typing import Annotated, Any, Callable, Iterable, Iterator, Literal

from loguru import logger
import typer
import pydantic
from tqdm import tqdm

import py_shared.flow as fl
# NOTE ideally we'd use this import, but it'd also import vLLM (slow), and the rx is unlikely to change
# from flow_sig_points.ai_patched_snippets.ai_patched_snippets import thinks_end_rx

app = typer.Typer()

keycols = fl.KeyCols(('idx', 'offset'))

class SigptRow(pydantic.BaseModel):
    idx: int
    offset: int
    text: str

class CotSliceRow(pydantic.BaseModel):
    idx: int
    offset: int
    candidate_offset: int | None
    text: str

class PatchInputs(pydantic.BaseModel):
    unit_test_code: str
    unit_test_exit_code: int
    unit_test_output: str

class PatchRow(pydantic.BaseModel):
    idx: int
    offset: int
    inputs: PatchInputs
    response: str

class OutRow(pydantic.BaseModel):
    idx: int
    patch_type: Literal['postcode_slices', 'tailpar']
    did_insert_test: bool
    src_reasoning: str
    patched_reasoning: str


md_heading_line_rx = re.compile(r'^#+ .*\n', re.MULTILINE)
marker_tag_rx = re.compile(r'\n*<test-with-result/>\n*')
# !!! should exactly match the regex in ai_patched_snippets.py !!!
thinks_end_rx = re.compile(r'\n*</think>\n*')


def process_patch_response(
    r: PatchRow,
) -> tuple[str, bool]:
    import io
    b = io.StringIO()

    response = r.response
    test_code = r.inputs.unit_test_code
    test_exit_code = r.inputs.unit_test_exit_code
    test_output = r.inputs.unit_test_output
    log_key = f'{r.idx}/{r.offset}'

    offset = 0
    if m_heading_ln := md_heading_line_rx.search(response):
        offset = m_heading_ln.end()
    else:
        logger.error('No heading line found in ai_patched_snippets row for: {}', log_key)

    m_tag = marker_tag_rx.search(response, offset)
    if m_tag is None:
        logger.error('No replacement tag found in ai_patched_snippets row for: {}', log_key)
        return response, False
    tag_start = m_tag.start()
    if tag_start < offset:
        logger.error('Replacement tag found before heading line in ai_patched_snippets row for: {}', log_key)
        offset = 0
    b.write(response[offset:tag_start])
    b.write('\n\n```python\n')
    b.write(test_code)
    if test_code[-1] != '\n':
        b.write('\n')
    b.write('```\n\n')
    b.write('<run-test/>\n\n')
    print('Exit code: ', test_exit_code, '. Output:', sep='', file=b)
    b.write('```\n')
    if test_output:
        b.write(test_output)
        if test_output[-1] != '\n':
            b.write('\n')
    b.write('```\n\n')
    b.write(response[m_tag.end():])
    return b.getvalue(), True


@app.command()
def main(
    extend_run: Path | None = None,
    force: bool = False,
):
    ctx = fl.dirs(__file__, has_runs=True, extend_run=extend_run, force=force)

    dep_patches_f = ctx.run_outd/'ai_patched_snippets/result.jsonl'
    dep_slices_f = ctx.flow_outd/'ai_extraction_prep/sliced_reasoning/result.jsonl'
    dep_sigpts_f = ctx.flow_outd/'ai_extraction_prep/extend_sig_points_with_interests/result.jsonl'

    out_f = ctx.step_outd/'result.jsonl'

    sigpts_by_idx: dict[int, list[SigptRow]] = defaultdict(list)
    for r in fl.ser.model_jsonl_streamf(SigptRow, dep_sigpts_f):
        sigpts_by_idx[r.idx].append(r)
    for sigpts in sigpts_by_idx.values():
        sigpts.sort(key=lambda r: r.offset)

    def get_entire_reasoning(idx: int) -> str:
        b = io.StringIO()
        for r in sigpts_by_idx[idx]:
            b.write(r.text)
        return b.getvalue()

    tailpar_slices_by_idx: dict[int, CotSliceRow] = {}
    for r in fl.ser.model_jsonl_streamf(CotSliceRow, dep_slices_f):
        if r.candidate_offset is not None:
            if r.offset == 0:
                # an error in coding assumptions, more errors may follow
                logger.error('A sliced_reasoning row with candidate_offset but offset=0 at: {}/{}', r.idx, r.offset)
            continue
        if r.offset != 0:
            # an error in coding assumptions, more errors may follow
            logger.error('A sliced_reasoning row with offset != 0 at: {}/{}', r.idx, r.offset)
            continue
        tailpar_slices_by_idx[r.idx] = r

    patches_by_idx: dict[int, list[PatchRow]] = defaultdict(list)
    for r in fl.ser.model_jsonl_streamf(PatchRow, dep_patches_f):
        patches_by_idx[r.idx].append(r)

    def gen_out_rows(
        keyed_patchlists: Iterable[tuple[int, list[PatchRow]]],
    ) -> Iterator[OutRow]:
        # for idx, patchlist in patches_by_idx.items():
        for idx, patchlist in keyed_patchlists:
            patchlist.sort(key=lambda r: r.offset)
            out_buf = io.StringIO()
            r0 = patchlist[0]
            if r0.offset == 0:
                # assume: this means a single patch for tailing paragraphs
                tailpar_slice_r = tailpar_slices_by_idx[idx]
                tailpar_len = len(tailpar_slice_r.text)
                entire_reasoning = get_entire_reasoning(idx)
                out_buf.write(entire_reasoning[:-1*tailpar_len])
                processed_response, did_insert_test = process_patch_response(r0)
                out_buf.write(processed_response)
                m = thinks_end_rx.search(entire_reasoning)
                if m is not None:
                    out_buf.write(entire_reasoning[m.start():])
                else:
                    # TODO reconsider: actually this may not be an error
                    logger.error('No thinks end found in sigpt texts (despite tailpar patch) for: {}', idx)
                r = OutRow(
                    idx=idx,
                    patch_type='tailpar',
                    did_insert_test=did_insert_test,
                    src_reasoning=entire_reasoning,
                    patched_reasoning=out_buf.getvalue(),
                )
                yield r
                continue

            # assumption: there are only code-end patches
            patchlist_iter = iter(patchlist)
            patch_r: PatchRow | None = next(patchlist_iter) # assuming patchlist is not empty
            cur_sigpt_rows = sigpts_by_idx[idx]
            did_insert_test = False
            for i, sigpt_row in enumerate(cur_sigpt_rows):
                if patch_r and sigpt_row.offset == patch_r.offset:
                    processed_response, just_inserted_test = process_patch_response(patch_r)
                    did_insert_test = did_insert_test or just_inserted_test
                    out_buf.write(processed_response)
                    if i == len(cur_sigpt_rows) - 1:
                        if m := thinks_end_rx.search(sigpt_row.text):
                            out_buf.write(sigpt_row.text[m.start():])
                    patch_r = next(patchlist_iter, None)
                else:
                    out_buf.write(sigpt_row.text)
            if patch_r is not None:
                logger.error(
                    'A patch row was left at: {}/{} (sigpt offsets: {!r}; patch offsets: {!r})',
                    idx, patch_r.offset,
                    [r.offset for r in sigpts_by_idx[idx]],
                    [r.offset for r in patches_by_idx[idx]],
                )

            r = OutRow(
                idx=idx,
                patch_type='postcode_slices',
                did_insert_test=did_insert_test,
                src_reasoning=get_entire_reasoning(idx),
                patched_reasoning=out_buf.getvalue(),
            )
            yield r

    fl.ser.model_jsonl_dumpf(
        gen_out_rows(patches_by_idx.items()),
        out_f,
    )


@app.command()
def explode_out_rows(
    run_outd: Annotated[Path | None, fl.InputDirArg()] = None,
) -> None:
    # get step_outd
    sd = fl.dirs(__file__, has_runs=True, extend_run=run_outd or 'last', force=True)

    dep_f = sd.step_outd/'result.jsonl'

    out_root = sd.step_outd/'exploded'
    out_root.mkdir(parents=True, exist_ok=True)

    for r in fl.ser.model_jsonl_streamf(OutRow, dep_f):
        out_d = out_root/f'{r.idx}'
        out_d.mkdir(exist_ok=True)
        (out_d/'patched_reasoning.txt').write_text(r.patched_reasoning)
        (out_d/'src_reasoning.txt').write_text(r.src_reasoning)
        (out_d/'metadata.json').write_text(fl.ser.json.dumps({
            'patch_type': r.patch_type,
        }))
    logger.success('Exploded out rows in: {}', fl.cwd_rel(out_root))


if __name__ == '__main__':
    app()
