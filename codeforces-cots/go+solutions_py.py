from pathlib import Path
import re
from typing import Iterable

from py_shared.schema.solutions_py import SolutionsInputs, SolutionsRow, make_rendered
from py_shared.test_code_maker import make_test_code
from py_shared.code_finder import find_code
from py_shared.ser import json_dumpf, str_dumpf


root_outd = Path('out+v2')
outf = root_outd / '1--solutions_py.jsonl'
exploded_root_outd = root_outd / '1--solutions_py+exploded'
exploded_root_outd.mkdir(parents=True, exist_ok=True)
answer_checks_root_outd = root_outd / '1--solutions_py+answer_checks'
answer_checks_root_outd.mkdir(parents=True, exist_ok=True)


def gen_rows(input_gen):
    backtick_or_end_think = re.compile(r'(```|</think>)')
    has_input_rx = re.compile(r'input\(\)|stdin')
    has_output_rx = re.compile(r'print\(|stdout')
    idx = 0

    def looks_like_answer(code: str) -> bool:
        return bool(
            has_input_rx.search(code) and
            has_output_rx.search(code)
        )

    for in_row in input_gen:
        idx += 1
        response: str = in_row['generation']

        has_extra_backticks_in_thinks = False
        has_extra_midparagraph_backticks_in_thinks = False
        if m := backtick_or_end_think.search(response):
            if m.group(0) == '```':
                m_start = m.start()
                m_start -= 2
                if m_start > 0 and response[m_start] != '\n':
                    has_extra_midparagraph_backticks_in_thinks = True

                has_extra_backticks_in_thinks = True

        think_code_blocks, final_answer = find_code(response)
        answer_candidates = list(filter(looks_like_answer, think_code_blocks))
        has_final_answer = final_answer is not None
        # cur_stat_dict = {
        #     'idx': idx,
        #     'response_len': len(response),
        #     'think_code_blocks': len(think_code_blocks),
        #     'answer_candidates': len(answer_candidates),
        #     'final_answer': has_final_answer,
        #     'has_input': has_final_answer and 'input()' in final_answer,
        #     'has_stdin': has_final_answer and 'stdin' in final_answer,
        #     'has_strange_stdin': has_final_answer and 'stdin' in final_answer and 'sys.stdin' not in final_answer,
        #     'has_print': has_final_answer and 'print(' in final_answer,
        # }
        from py_shared.schema.solutions_py import SolutionsRow
        r = SolutionsRow(
            idx=idx,
            inputs=SolutionsInputs(
                prompt=in_row['prompt'],
                response=response,
                title=in_row['title'],
                contest_name=in_row['contest_name'],
                contest_start_year=in_row['contest_start_year'],
                examples=in_row['examples'] or [],
            ),
            response_len=len(response),
            think_code_blocks=think_code_blocks,
            answer_candidates=answer_candidates,
            final_answer=final_answer,
            has_input=has_final_answer and 'input()' in final_answer,
            has_stdin=has_final_answer and 'stdin' in final_answer,
            has_strange_stdin=has_final_answer and 'stdin' in final_answer and 'sys.stdin' not in final_answer,
            has_print=has_final_answer and 'print(' in final_answer,
            has_extra_backticks_in_thinks=has_extra_backticks_in_thinks,
            has_extra_midparagraph_backticks_in_thinks=has_extra_midparagraph_backticks_in_thinks,
        )
        yield r


def write_rows(rows_gen: Iterable[SolutionsRow]):
    def format_item_dirname(idx: int) -> str:
        return f'{idx:05d}' # digits for sorting

    with outf.open('w') as outf_fh:
        for r in rows_gen:
            print(r.model_dump_json(), file=outf_fh)

            item_outd = exploded_root_outd / format_item_dirname(r.idx)
            item_outd.mkdir(parents=True, exist_ok=True)

            json_dumpf(r.inputs.examples, item_outd/'examples.json')
            # json_dumpf(cur_stat_dict, item_outd/'stats.jsonl')
            str_dumpf(r.inputs.prompt, item_outd/'prompt.md')
            str_dumpf(r.final_answer, item_outd/'final_answer.py')

            response = r.inputs.response
            thinks_end = response.rfind('</think>')
            if thinks_end != -1:
                thinks_str = response[:thinks_end].rstrip()
                str_dumpf(thinks_str, item_outd/'thinks.md')

            with (item_outd/'rendered.md').open('w') as fh:
                make_rendered(r, fh)

            if r.inputs.examples:
                code_outd = answer_checks_root_outd / format_item_dirname(r.idx)
                code_outd.mkdir(parents=True, exist_ok=True)
                for ans_idx, ans in enumerate(r.answer_candidates):
                    with (code_outd/f'candidate-{ans_idx}.py').open('w') as fh:
                        print(make_test_code(ans, r.inputs.examples), file=fh)

                if r.final_answer is not None:
                    with (code_outd/'final_answer.py').open('w') as fh:
                        print(make_test_code(r.final_answer, r.inputs.examples), file=fh)

            # with (item_outd/'examples.json').open('w') as fh:
            #     json.dump(in_row['examples'], fh)
            # # with (item_outd/'stats.jsonl').open('w') as fh:
            # #     json.dump(cur_stat_dict, fh)
            # with (item_outd/'prompt.md').open('w') as fh:
            #     print(in_row['prompt'], file=fh)
            # with (item_outd/'final_answer.py').open('w') as fh:
            #     print(final_answer, file=fh)
            # thinks_end = response.rfind('</think>')
            # if thinks_end != -1:
            #     thinks_str = response[:thinks_end].rstrip()
            #     with (item_outd/'thinks.md').open('w') as fh:
            #         print(thinks_str, file=fh)
            # with (item_outd/'rendered.md').open('w') as fh:
            #     print("# {title} ({contest_name}, {contest_start_year})".format(**in_row), file=fh)
            #     print("# Prompt", file=fh)
            #     print(in_row['prompt'], file=fh)
            #     print("# Response", file=fh)
            #     print(in_row['generation'], file=fh)
            #     print("\n# Think code blocks", file=fh)
            #     not_first = False
            #     for ans in think_code_blocks:
            #         if not_first:
            #             print('\n---\n', file=fh)
            #         print('```python', file=fh)
            #         print(ans, file=fh)
            #         print('```', file=fh)
            #         not_first = True
            #     del not_first

                # print('\n# Final answer', file=fh)
                # if final_answer is not None:
                #     print('```python', file=fh)
                #     print(final_answer, file=fh)
                #     print('```', file=fh)

            # if in_row['examples']:
            #     answer_check_dir = item_outd/'answer_checks'
            #     answer_check_dir.mkdir(parents=True, exist_ok=True)
            #     for ans_idx, ans in enumerate(answer_candidates):
            #         with (answer_check_dir/f'candidate-{ans_idx}.py').open('w') as fh:
            #             print(make_test_code(ans, in_row['examples']), file=fh)

            #     if final_answer is not None:
            #         with (answer_check_dir/'final_answer.py').open('w') as fh:
            #             print(make_test_code(final_answer, in_row['examples']), file=fh)


def main(ds):
    write_rows(gen_rows(ds))


from os import environ as env
if __name__ == '__main__' and 'NOGO' not in env:
    import datasets
    ds = datasets.load_dataset('open-r1/codeforces-cots', 'solutions_py', split='train[:1000]')
    main(ds)