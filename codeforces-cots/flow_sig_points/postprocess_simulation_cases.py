#!/usr/bin/env python3
import json
from pathlib import Path
from os import environ

from loguru import logger

from py_shared import ser
from py_shared.json_finder import find_json


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
_, flow_outd, step_outd = _dirs(__file__, tag)
# dep_ds_f = flow_outd/'fetch_process_solutions_py/report.jsonl'
# dep_sims_f = flow_outd/'extract_simulation_snippets/result.jsonl'
dep_cases_stepd = flow_outd/f'extract_simulation_cases{tag}'

# def _dep_ds_kvgen():
#     for r in ser.jsonl_streamf(dep_ds_f):
#         yield r['idx']-1, r
# dep_ds_by_idx = dict(_dep_ds_kvgen())

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

for p in dep_cases_dirs:
    logger.info('Processing: {}', p.stem)
    prompts_by_idx_offset = dict(_def_prompts_kvgen(p))
    cur_outd = step_outd/p.stem
    cur_outd.mkdir(parents=True, exist_ok=True)
    with (
        open(cur_outd/'processed-simulation-cases.jsonl', 'w') as main_fh,
        open(cur_outd/'exploded-cases.jsonl', 'w') as exploded_fh,
    ):
        for in_r in ser.jsonl_streamf(p/'result.jsonl'):
            r = {}
            idx      = r['idx']      = in_r['idx']
            offset   = r['offset']   = in_r['offset']
            n        = r['n']        = in_r['n']
            r['len_reasoning'] = -1 # here for key ordering, set below
            response = r['response'] = in_r['response']

            reasoning: str = prompts_by_idx_offset[(idx, offset)]['inputs']['reasoning']
            r['len_reasoning'] = len(reasoning)

            def emit(early: bool = False):
                if early:
                    logger.warning('An issue with case {}/{}/{}', idx, offset, n)
                print(json.dumps(r), file=main_fh)
            ans_str = find_json(in_r['response'])
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
            case_check_data = r['case_check_data'] = list(_gen_case_check_data())

            def _one_case_ok(data: dict) -> bool:
                input_pos  = data['input_pos']
                output_pos = data['output_pos']
                return input_pos != -1 and output_pos != -1

            cases_ok = r['cases_ok'] = all(_one_case_ok(d) for d in case_check_data)

            emit()
            for case_idx, (c, check_data) in enumerate(zip(cases, case_check_data)):
                expl_r = {}
                for k in ('idx', 'offset', 'n'):
                    expl_r[k] = r[k]
                expl_r.update({
                    'case_idx': case_idx,
                    'len_reasoning': len(reasoning),
                    'source_sample_id': c.get('source_sample_id', None),
                    'input': c.get('input', None),
                    'output': c.get('output', None),
                    'is_correct': c.get('is_correct', None),
                    'input_pos': check_data['input_pos'],
                    'output_pos': check_data['output_pos'],
                    'is_ok': _one_case_ok(check_data),
                })
                print(json.dumps(expl_r), file=exploded_fh)

    logger.success('Processed: {}', p.stem)