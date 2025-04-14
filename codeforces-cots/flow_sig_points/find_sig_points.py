#!/usr/bin/env python3
import json
from pathlib import Path
from typing import Any, Callable, Iterator

from loguru import logger
import numpy as np
from tqdm import tqdm
from pydantic import BaseModel
import regex as reg # regex is compatible with the re module

from py_shared import code_finder, ser


class SigPointData(BaseModel):
    offset: int
    type: str
    rel_offset: int = 0
    text_len: int = 0
    extra: dict[str, Any] = {}
    text: str = ''

flow_outd = Path(__file__).parent/'out'

def make_outf(tag: str = '') -> Path:
    tag_suffix = ''
    if tag:
        tag_suffix = '+'+tag
    step_outd = flow_outd/f'find_sig_points{tag_suffix}'
    step_outd.mkdir(parents=True, exist_ok=True)
    return step_outd / 'result.jsonl'

opt_dep_f = flow_outd/'extract_checkable_responses'/'clean-result.jsonl'


# Observations
# Simulations almost always start with "Let's test" or "Testing".
# (This is almost always followed on the same line by "samples"/"examples").
# "Let me check" sometimes starts a simulation but much more often it's insignificant.
# (Maybe it should be a start of simulation if it's followed by cases)
# The "cases" are most often many pars, rarely just a single par.
# Cases almost always start with "(Numeral) ('sample'|'example')",
# sometimes with "(Sample|Example) (numeral)",
# and there's always a colon.
#
# We only consider code blocks which look like answers, here's why.
# Lines like "id_ent is 0." and "id=1." are considered code.
# If the code block comprises only lines like that, it's probably not a code block.
# Also there's things like this:
# ```
# k2 >=1,
# k1 +k2 <=n,
# x1/k1 <= c[k1-1],
# x2/k2 <= c[k1 +k2-1].
# ```
# Also:
# ```
# A = [1, 2]
# P = [1]
# ```
# They could interrupt extracting data from simulation text.

simulation_start_rx = reg.compile(
    # r'^.*?(let\'s test|testing).*?(examples?|samples?)',
    r'^((?P<prefix>.*?)let\'s test|testing).*?.*$',
    flags=reg.IGNORECASE | reg.MULTILINE,
)

# TODO there's also "first test case" etc. look for them in the retrieved snippets?
_case_markers = [
    r'((first|second|third|fourth|fifth|sixth|seventh|eighth|ninth) (sample|example|case))',
    r'((1st|2nd|3rd|4th|5th|6th|7th|8th|9th) (sample|example|case))',
    r'((another|next) (sample|example|case))',
    r'((sample|example|case)\W.{,15}(1|2|3|4|5|6|7|8|9|10))',
    r'((sample|example|case) input)',
    r'(input (sample|example|case))',
]

simulation_case_rx = reg.compile(
    fr'^(?P<prefix>.*?)({"|".join(_case_markers)}).*?:.*$',
    flags=reg.IGNORECASE | reg.MULTILINE,
)

thinks_end_rx = reg.compile(
    r'^.*?<\/think>.*$',
    flags=reg.MULTILINE,
)

reflection_par_rx = reg.compile(
    r'\n.*?\W(?P<kw>(in)?correct|fails?|wrong)\W.*\n\n+(?=\w)',
    flags=reg.IGNORECASE,
)


def processed_response_gen(
    response: str
) -> Iterator[SigPointData]:
    # We search for multiple regexes in a pretty long string, so this may get slow.
    # When it does, we can try combining all the regexes into just one like this:
    # r'((?P<_1>)a)|((?P<_2>)b)|((?P<_3>)c)'
    # The empty groups can be used to check which regex matched:
    # one will be empty, others will be null.
    # We need to be careful about overlapping regexes etc, but this is doable.
    results: list[SigPointData] = [
        SigPointData(
            offset=0,
            type='start',
        )
    ]

    # valid_code_blocks = [
    #     (block, offset)
    #     for block, offset in code_finder.find_code_blocks(response)[0]
    #     if code_finder.looks_like_answer(block)
    # ]

    code_block_search_res = code_finder.find_code_blocks(response)[0]
    valid_code_ranges = np.empty((0, 2), dtype=int)
    if code_block_search_res:
        valid_code_ranges = np.array([
            [offset, offset + len(block)]
            for block, offset in code_block_search_res
            if code_finder.looks_like_answer(block)
        ])

    for start, end in valid_code_ranges:
        results.extend([
            SigPointData(offset=int(start), type='code'),
            SigPointData(offset=int(end), type='code-end'),
        ])

    def is_inside_code_blocks(offset: int) -> bool:
        # Check if offset is between any start and end points
        if len(valid_code_ranges) == 0:
            return False
        return np.any(
            (valid_code_ranges[:, 0] <= offset)
            & (offset < valid_code_ranges[:, 1])
        )

    # def is_inside_code_blocks(offset: int) -> bool:
    #     """Check if an offset is inside any code block."""
    #     for code_block, code_start in valid_code_blocks:
    #         code_end = code_start + len(code_block)
    #         if code_start <= offset < code_end:
    #             return True
    #     return False

    def finditer_notin_code_blocks(
        rx: reg.Pattern,
        haystack: str,
        point_fn: Callable[[reg.Match], int] = lambda m: m.start(),
    ) -> Iterator[tuple[int, reg.Match]]:
        for m in rx.finditer(haystack):
            pt = point_fn(m)
            if is_inside_code_blocks(pt):
                continue
            yield pt, m

    # Find simulation start points, but only if they're not inside code blocks
    for pt, m in finditer_notin_code_blocks(simulation_start_rx, response):
        prefix_g = m.group('prefix')
        results.append(SigPointData(
            offset=pt,
            type='sim',
            extra={
                'prefix_len': len(prefix_g) if prefix_g else 0,
                'line_len': len(m.group(0)),
            },
        ))

    # Find simulation case points, but only if they're not inside code blocks
    for pt, m in finditer_notin_code_blocks(simulation_case_rx, response):
        prefix_g = m.group('prefix')
        results.append(SigPointData(
            offset=pt,
            type='case',
            extra={
                'prefix_len': len(prefix_g) if prefix_g else 0,
                'line_len': len(m.group(0)),
            },
        ))

    # Find thinks_end, but only if they're not inside code blocks
    for pt, m in finditer_notin_code_blocks(thinks_end_rx, response):
        results.append(SigPointData(
            offset=pt,
            type='response-proper',
        ))

    # Find paragraphs containing "correct" or "fail" and the start of the next paragraph
    for pt, m in finditer_notin_code_blocks(reflection_par_rx, response, lambda m: m.end()):
        results.append(SigPointData(
            offset=pt,
            type='post-reflection',
            extra={
                'keyword': m.group('kw'),
            },
        ))

    results.sort(key=lambda x: x.offset)

    # cut the response at each sig point
    res_iter = iter(results)
    loop = True
    cur_item: SigPointData = next(res_iter) # 1st point is the start
    # NOTE we only yield _some_ of the points
    while loop:
        try:
            next_item = next(res_iter)
            next_item.rel_offset = next_item.offset - cur_item.offset
            if next_item.rel_offset == 0:
                # if the points have the same offset we de-duplicate them
                # note that the point types come in a specific order,
                # matching how they were inserted into the list,
                # since Python list sort preserves the order of equal elements
                if cur_item.type == 'sim':
                    if next_item.type == 'case':
                        next_item = next(res_iter)
                        next_item.rel_offset = next_item.offset - cur_item.offset
                    if next_item.rel_offset == 0 and next_item.type == 'post-reflection':
                        next_item = next(res_iter)
                        next_item.rel_offset = next_item.offset - cur_item.offset
                if cur_item.type == 'case':
                    if next_item.type == 'post-reflection':
                        next_item = next(res_iter)
                        next_item.rel_offset = next_item.offset - cur_item.offset
        except StopIteration:
            loop = False
            # defensive programming: null out the next item since it shouldn't be used
            next_item = None

        part_start = cur_item.offset
        part_end = next_item.offset if next_item else len(response)
        cur_item.text = response[part_start:part_end]
        cur_item.text_len = len(cur_item.text)
        yield cur_item
        cur_item = next_item # type: ignore

if __name__ == '__main__':
    from sys import argv
    data_src = 'ds'
    if len(argv) > 1:
        arg = argv[1]
        assert arg in ('ds', 'checkables')
        data_src = arg

    if data_src == 'ds':
        import datasets
        ds: Any = datasets.load_dataset('open-r1/codeforces-cots', 'solutions_py', split='train[:1000]')
        data_len = len(ds)
        data_gen = ((idx, r) for idx, r in enumerate(ds))
        tag = ''
    else:
        data = ser.jsonl_loadf(opt_dep_f)
        data_len = len(data)
        data_gen = ((r['idx'], r) for r in data)
        tag = 'checkables'

    outf = make_outf(tag)
    with outf.open('w') as fh:
        for idx, in_r in tqdm(data_gen, total=data_len):
            r = {
                'idx': idx,
                'id': in_r['id'],
            }
            for p in processed_response_gen(in_r['generation']):
                r.update(p.model_dump())
                print(json.dumps(r), file=fh)