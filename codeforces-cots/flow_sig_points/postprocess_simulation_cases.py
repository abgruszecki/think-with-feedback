#!/usr/bin/env python3
import json
from pathlib import Path
from os import environ

from loguru import logger
import typer

from py_shared import ser
from py_shared.json_finder import find_json


app = typer.Typer()

def _dirs(file_attr, tag: str = ''):
    p = Path(file_attr)
    flowd = p.parent
    flow_outd = flowd/'out'
    step_outd = flow_outd/(p.stem+tag)
    step_outd.mkdir(parents=True, exist_ok=True)
    return flowd, flow_outd, step_outd


tag = ''
if _tag_arg := environ.get('STEP_TAG'):
    tag = '+'+_tag_arg
flowd, flow_outd, step_outd = _dirs(__file__, tag)
dep_ds_f = flow_outd/'fetch_process_solutions_py/report.jsonl'
# dep_sims_f = flow_outd/'extract_simulation_snippets/result.jsonl'
dep_cases_stepd = flow_outd/f'extract_simulation_cases{tag}'

def _dep_ds_kvgen():
    for r in ser.jsonl_streamf(dep_ds_f):
        yield r['idx'], r
dep_ds_by_idx = dict(_dep_ds_kvgen())

# def _dep_sims_kvgen():
#     for r in ser.jsonl_streamf(dep_sims_f):
#         yield (r['idx'], r['offset']), r
# dep_sims_by_idx_offset = dict(_dep_sims_kvgen())


def _dep_cases_dirs_gen():
    for p in dep_cases_stepd.iterdir():
        if not p.is_dir():
            continue
        yield p
dep_cases_dirs = list(_dep_cases_dirs_gen())
dep_cases_dirs.sort(key=lambda x: x.stem, reverse=True)


def _def_prompts_kvgen(dir: Path):
    p = dir/'prompts.jsonl'
    for r in ser.jsonl_streamf(p):
        yield (r['idx'], r['offset']), r


@app.command()
def main(
    only_explode: bool = False,
    add_code: bool = False,
):
    for p in dep_cases_dirs:
        logger.info('Processing: {}', p.stem)
        prompts_by_idx_offset = dict(_def_prompts_kvgen(p))
        cur_outd = step_outd/p.stem
        cur_outd.mkdir(parents=True, exist_ok=True)
        main_f = cur_outd/'processed-simulation-cases.jsonl'
        exploded_f = cur_outd/'exploded-cases.jsonl'
        trustworthy_f = cur_outd/'trustworthy-cases.jsonl'
        with (
            open(main_f, 'w') as main_fh,
            open(exploded_f, 'w') as exploded_fh,
            open(trustworthy_f, 'w') as trustworthy_fh,
        ):
            for in_r in ser.jsonl_streamf(p/'result.jsonl'):
                r = {}
                idx      = r['idx']      = in_r['idx']
                offset   = r['offset']   = in_r['offset']
                n        = r['n']        = in_r['n']
                r['len_reasoning'] = -1 # here for key ordering, set below
                response = r['response'] = in_r['response']

                prompt_r = prompts_by_idx_offset[(idx, offset)]
                reasoning: str = prompt_r['inputs']['reasoning']
                r['len_reasoning'] = len(reasoning)

                ds_r = dep_ds_by_idx[idx]

                def emit(early: bool = False):
                    if early:
                        logger.warning('An issue with case {}/{}/{}', idx, offset, n)
                    print(json.dumps(r), file=main_fh)
                ans_str = find_json(in_r['response'], expect_thinks=False)
                if ans_str is None:
                    emit(early=True)
                    continue
                r['raw_ans'] = ans_str
                try:
                    ans = json.loads(ans_str)
                    assert isinstance(ans, list)
                    assert all(isinstance(c, dict) for c in ans)
                    cases = r['cases'] = ans
                except Exception:
                    emit(early=True)
                    continue

                def _gen_case_check_data():
                    def find_extracted_io(substr: str | None, offset: int) -> int:
                        if substr is None:
                            return -1
                        # the last trailing newline is definitely not significant
                        substr = substr.removesuffix('\n')
                        pos = reasoning.find(substr, offset)
                        if pos == -1 and '\n' in substr:
                            # 4o-mini sometimes collapses newlines (I guess it follows the IO samples)
                            substr = substr.replace('\n', '\n\n')
                            pos = reasoning.find(substr, offset)
                        return pos

                    for c in cases:
                        input_pos = find_extracted_io(c['input'], offset=0)
                        cur_pos = input_pos if input_pos != -1 else 0
                        output_pos = find_extracted_io(c['output'], offset=cur_pos)

                        yield {
                            'input_pos': input_pos,
                            'output_pos': output_pos,
                        }

                if not only_explode:
                    case_check_data = r['case_check_data'] = list(_gen_case_check_data())

                    def _one_case_ok(data: dict) -> bool:
                        input_pos  = data['input_pos']
                        output_pos = data['output_pos']
                        return input_pos != -1 and output_pos != -1

                    cases_ok = r['cases_ok'] = all(_one_case_ok(d) for d in case_check_data)
                else:
                    case_check_data = [None] * len(cases)

                emit()
                for case_idx, (c, check_data) in enumerate(zip(cases, case_check_data)):
                    expl_r = {}
                    for k in ('idx', 'offset', 'n'):
                        expl_r[k] = r[k]
                    expl_r.update({
                        'case_idx': case_idx,
                        'num': prompt_r.get('num'),
                        'examples': ds_r['inputs']['examples'],
                        'len_reasoning': len(reasoning),
                        'input': c.get('input', None),
                        'output': c.get('output', None),
                        'input_pos': check_data['input_pos'] if check_data else None,
                        'output_pos': check_data['output_pos'] if check_data else None,
                        'assessment': c.get('assessment', None),
                    })
                    if not only_explode:
                        expl_r['is_ok'] = _one_case_ok(check_data)
                    if add_code:
                        # TODO move this to another script
                        expl_r['code'] = prompt_r['inputs']['code']
                    print(json.dumps(expl_r), file=exploded_fh)

                    if not only_explode:
                        is_trustworthy = cases_ok
                        if is_trustworthy:
                            print(json.dumps(expl_r), file=trustworthy_fh)

        logger.success('Wrote: {}', main_f.relative_to(flowd, walk_up=True))
        logger.success('Wrote: {}', exploded_f.relative_to(flowd, walk_up=True))
        if not only_explode:
            logger.success('Wrote: {}', trustworthy_f.relative_to(flowd, walk_up=True))
        else:
            if len(trustworthy_f.read_text()) > 0:
                logger.error(
                    'Dev error - this file should be empty: {}',
                    trustworthy_f.relative_to(flowd, walk_up=True)
                )
            else:
                trustworthy_f.unlink()


if __name__ == '__main__':
    app()
