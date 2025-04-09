#!/usr/bin/env python3
import json
from pathlib import Path
from typing import Any

from tqdm import tqdm
from pydantic import BaseModel
import regex as reg # regex is compatible with the re module

from py_shared import code_finder


class SigPointData(BaseModel):
    offset: int
    type: str
    rel_offset: int = 0
    text_len: int = 0
    extra: dict[str, Any] = {}
    text: str = ''


step_outd = Path(__file__).parent/'out/find_sig_points'
step_outd.mkdir(parents=True, exist_ok=True)
outf = step_outd / 'result.jsonl'


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

_case_markers = [
    r'((first|second|third|fourth|fifth|sixth|seventh|eighth|ninth) (sample|example|case))',
    r'((1st|2nd|3rd|4th|5th|6th|7th|8th|9th) (sample|example|case))',
    r'((another|next) (sample|example|case))',
    r'((sample|example|case).{,15}(1|2|3|4|5|6|7|8|9|10))',
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


def process_response(
    response: str
) -> list[SigPointData]:
    results: list[SigPointData] = [
        SigPointData(
            offset=0,
            type='start',
        )
    ]
    for m in simulation_start_rx.finditer(response):
        prefix_g = m.group('prefix')
        results.append(SigPointData(
            offset=m.start(),
            type='sim',
            extra={
                'prefix_len': len(prefix_g) if prefix_g else 0,
                'line_len': len(m.group(0)),
            },
        ))
    # Cases are temporarily commented out, they make later steps harder. @case
    # for m in simulation_case_rx.finditer(response):
    #     prefix_g = m.group('prefix')
    #     results.append(SigPointData(
    #         offset=m.start(),
    #         type='case',
    #         extra={
    #             'prefix_len': len(prefix_g) if prefix_g else 0,
    #             'line_len': len(m.group(0)),
    #         },
    #     ))
    for code_block, offset in code_finder.find_code_blocks(response)[0]:
        if not code_finder.looks_like_answer(code_block):
            continue
        results.extend([
            SigPointData(offset=offset, type='code'),
            SigPointData(offset=offset + len(code_block), type='code-end'),
        ])
    for m in thinks_end_rx.finditer(response):
        results.append(SigPointData(
            offset=m.start(),
            type='response-proper',
        ))

    results.sort(key=lambda x: x.offset)

    # there's *one* case where we find a sim in code.
    # so we get rid of all points inside code blocks
    def _cleaned_results_gen(results: list[SigPointData]):
        inside_code = False
        for item in results:
            if item.type == 'code':
                inside_code = True
                yield item
            elif item.type == 'code-end':
                inside_code = False
            if not inside_code:
                yield item
    results = list(_cleaned_results_gen(results))

    # cut the response at each sig point
    res_iter = iter(results)
    loop = True
    cur_item: SigPointData = next(res_iter) # 1st point is the start
    while loop:
        try:
            next_item = next(res_iter)
            next_item.rel_offset = next_item.offset - cur_item.offset
        except StopIteration:
            loop = False
            next_item = None

        part_start = cur_item.offset
        part_end = next_item.offset if next_item else len(response)
        cur_item.text = response[part_start:part_end]
        cur_item.text_len = len(cur_item.text)
        cur_item = next_item # type: ignore
    return results


if __name__ == '__main__':
    import datasets
    ds: Any = datasets.load_dataset('open-r1/codeforces-cots', 'solutions_py', split='train[:1000]')
    with outf.open('w') as fh:
        for idx, in_r in enumerate(tqdm(ds)):
            points = process_response(in_r['generation'])
            for p in points:
                r = {
                    'idx': idx,
                    'id': in_r['id'],
                }
                r.update(p.model_dump())
                json.dump(r, fh)
                fh.write('\n')