#!/usr/bin/env python3
import json
from pathlib import Path
from typing import Annotated, Any, Callable, Iterator

from loguru import logger
import numpy as np
from tqdm import tqdm
from pydantic import BaseModel
import regex as reg # regex is compatible with the re module
import typer

from py_shared import code_finder, ser
import py_shared.flow as fl

app = typer.Typer()


class SigPointData(BaseModel):
    offset: int
    type: str
    rel_offset: int = 0
    text_len: int = 0
    extra: dict[str, Any] = {}
    text: str = ''


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

# TODO lengthen the distance at which a case is connected to a simulation?
_case_markers = [
    r'((?P<num>first|second|third|fourth|fifth|sixth|seventh|eighth|ninth) (test )?(sample|example|case).*?)',
    r"((?P<num>1st|2nd|3rd|4th|5th|6th|7th|8th|9th) (test )?(sample|example|case)(?!\w|').*?)",
    # NOTE the negative lookbehinds just reduce the number of false positives a bit,
    # but they're not strictly necessary.
    # TODO look into "case N" matches, they seem to mostly occur for sub-cases of examples
    r'((?<!for )(sample|example|case) ?(test )?(input ?)?(?P<num>1|2|3|4|5|6|7|8|9|10).*?)',
    r'((?<!for )(sample|example|case) ?(test )?input ?(?P<num>1|2|3|4|5|6|7|8|9|10)?.*?)',
    r'(input (sample|example|case) ?(?P<num>1|2|3|4|5|6|7|8|9|10)?.*?)',
    # TODO R1 *sometimes* writes "another sample: first input.", etc; see extra.extra_num
    r'(another ((test | edge )?case|example|sample))'
]

# TODO go through these prefixes, they may be more harmful than helpful
# NOTE prefixes with words like "wait" or "but" are suspicious
simulation_case_rx = reg.compile(
    fr'^(?P<prefix>.*?)(?P<marker>{"|".join(_case_markers)}):.*$',
    flags=reg.IGNORECASE | reg.MULTILINE,
)

_numerators = [
    r'(?P<num>first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth)',
    r'(?P<num>1st|2nd|3rd|4th|5th|6th|7th|8th|9th|10th)',
    # r'(?P<num>1|2|3|4|5|6|7|8|9|10)',
]

numerator_rx = reg.compile(fr'{"|".join(_numerators)}', flags=reg.IGNORECASE)

thinks_end_rx = reg.compile(
    r'^.*?<\/think>.*$',
    flags=reg.MULTILINE,
)

# TODO this may cut off too much.
# TODO look for a leading "is" or "are"?
# TODO add "correctly"?
# TODO why the lookahead?
reflection_par_rx = reg.compile(
    r'\n.*?\W(?P<kw>(in)?correct|fails?|wrong)\W.*\n\n+(?=\s*\w)',
    flags=reg.IGNORECASE,
)


def processed_response_gen(
    response: str,
    only_code: bool = False,
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

    code_block_search_res = code_finder.find_code_blocks(response)[0]
    # NOTE using numpy here help performance a bit,
    # but really it's more important not to watch YT while running the script
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

    if not only_code:
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
            num = m.group('num')
            extra_num = None
            if not num:
                extra_num = numerator_rx.search(m.group(0))
                if extra_num:
                    extra_num = extra_num.group('num')
            results.append(SigPointData(
                offset=pt,
                type='case',
                extra={
                    'prefix_len': len(prefix_g) if prefix_g else 0,
                    'line_len': len(m.group(0)),
                    'marker': m.group('marker'),
                    'num': num,
                    'extra_num': extra_num,
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
    cur_item: SigPointData = next(res_iter) # the start is always the first point
    # NOTE we only yield _some_ of the points
    while loop:
        try:
            next_item = next(res_iter)
            next_item.rel_offset = next_item.offset - cur_item.offset
            if not only_code and next_item.rel_offset == 0:
                # if the points have the same offset we de-duplicate them
                # note that the point types come in a specific order,
                # matching how they were inserted into the list,
                # since Python list sort preserves the order of equal elements
                if cur_item.type == 'sim':
                    if next_item.type == 'case':
                        new_extras = next_item.extra.copy()
                        new_extras.update(cur_item.extra)
                        cur_item.extra = new_extras
                        cur_item.extra['is_also_case'] = True

                        next_item = next(res_iter)
                        next_item.rel_offset = next_item.offset - cur_item.offset
                    if next_item.rel_offset == 0 and next_item.type == 'post-reflection':
                        # NOTE ATTW we don't care about merging extras of post-reflection
                        next_item = next(res_iter)
                        next_item.rel_offset = next_item.offset - cur_item.offset
                if cur_item.type == 'case':
                    if next_item.type == 'post-reflection':
                        # NOTE ATTW we don't care about merging extras of post-reflection
                        next_item = next(res_iter)
                        next_item.rel_offset = next_item.offset - cur_item.offset
        except StopIteration:
            loop = False
            # defensive programming: null out the next item since it shouldn't be used
            next_item = None

        part_start = cur_item.offset
        part_end = next_item.offset if next_item else len(response)
        cur_item.text = response[part_start:part_end]
        cur_item.text_len = part_end - part_start
        yield cur_item
        cur_item = next_item # type: ignore


@app.command()
def main(
    data_source: Annotated[str, typer.Option()] = 'checkables',
):
    valid_data_sources = ('checkables', 'unfiltered-ds', 'checkables-wrong', 'checkables-stream-full')
    if data_source not in valid_data_sources:
        raise typer.BadParameter(f'--data-source should be one of: {valid_data_sources!r}; was: {data_source!r}')

    ctx = fl.dirs(__file__)

    opt_dep_checkables_f = ctx.flow_outd/'extract_checkable_responses'/'clean-result.jsonl'
    opt_dep_checkables_wrong_f = ctx.flow_outd/'select_checkable_wrong_responses'/'report.jsonl'
    opt_dep_process_solutions_py_f = ctx.flow_outd/'fetch_process_solutions_py/report.jsonl'

    outf = ctx.step_outd/'result.jsonl'

    if data_source == 'checkables':
        data = ser.jsonl_loadf(opt_dep_checkables_f)
        data_len = len(data)
        data_gen = ((r['idx'], r) for r in data)
        get_response = lambda r: r['generation']
        tag = ''
    elif data_source == 'unfiltered-ds':
        import datasets
        ds: Any = datasets.load_dataset('open-r1/codeforces-cots', 'solutions_py', split='train[:1000]')
        data_len = len(ds)
        data_gen = ((idx, r) for idx, r in enumerate(ds))
        get_response = lambda r: r['generation']
        tag = '+unfiltered-ds'
    elif data_source == 'checkables-wrong':
        data = ser.jsonl_loadf(opt_dep_checkables_wrong_f)
        data_len = len(data)
        data_gen = ((r['idx'], r) for r in data)
        get_response = lambda r: r['inputs']['response']
        # NOTE right now we're not tagging the step output dir here, these tags propagate way too much.
        # I think I'd rather tag the output dir.
        tag = ''
    elif data_source == 'checkables-stream-full':
        # TODO this is yet another kludge on top of all the other kludges...
        dep_ds_checker_types_f = ctx.flow_outd/'fetch_extract_checker_type/checker-types.jsonl'
        wanted_indices = set()
        for r in ser.jsonl_streamf(dep_ds_checker_types_f):
            if r.get('type') == 'diff':
                wanted_indices.add(r['idx'])
        data_f = opt_dep_process_solutions_py_f
        def _gen_data_rows():
            return (r for r in ser.jsonl_streamf(data_f) if r['idx'] in wanted_indices)
        data_len = sum(1 for _ in _gen_data_rows())
        data_gen = ((r['idx'], r) for r in _gen_data_rows())
        get_response = lambda r: r['inputs']['response']
        tag = ''

    with outf.open('w') as fh:
        for idx, in_r in tqdm(data_gen, total=data_len):
            r = {
                'idx': idx,
                'id': in_r['id'],
            }
            for p in processed_response_gen(get_response(in_r)):
                r.update(p.model_dump(mode='json'))
                print(json.dumps(r), file=fh)


if __name__ == '__main__':
    app()