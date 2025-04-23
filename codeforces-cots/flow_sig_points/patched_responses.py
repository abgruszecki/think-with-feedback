#!/usr/bin/env python3
from io import StringIO
import json
from typing import Iterable, Iterator
from collections import defaultdict

from loguru import logger
import typer

from py_shared import ser
from py_shared.misc import step_dirs, cwd_rel


app = typer.Typer()


REPLACEMENT_PREFIX_TEMPLATE = \
'''\
Testing against sample input{plural_suffix} {example_ids}.

```python
'''
REPLACEMENT_INFIX = \
'''
```

<RUN_SNIPPET>
```output
'''
REPLACEMENT_SUFFIX = \
'''
```

'''


def gen_patched_responses(
    dep_replacements_rows: Iterable[dict],
    dep_ds_rows: Iterable[dict],
) -> Iterator[dict]:
    replacements_by_idx = defaultdict(list)
    for r in dep_replacements_rows:
        idx = r['idx']
        offset = r['offset']
        start = r['candidate_offset']
        r['replacement_start'] = start or offset
        r['replacement_end'] = offset + r['reasoning_len']
        r['candidate_sim'] = bool(start)
        replacements_by_idx[idx].append(r)

    for in_r in dep_ds_rows:
        idx = in_r['idx']
        if idx not in replacements_by_idx:
            continue

        replacements = replacements_by_idx[idx]
        replacements.sort(key=lambda x: x['replacement_start'])

        response = in_r['inputs']['response']
        # identifiers of code snippets involved in the patches:
        # the offset for candidate snippets and 'final' for the final answer
        seen_snippets = []
        seen_nums = []
        did_patch = False
        out_buf = StringIO()
        cur_pos = 0
        for replace_r in replacements:
            start = replace_r['replacement_start']
            end = replace_r['replacement_end']
            offset = replace_r['offset']
            nums = replace_r['nums']
            candidate_sim = replace_r['candidate_sim']
            status = replace_r['status']

            out_buf.write(response[cur_pos:start])

            snippet_id = 'final' if candidate_sim else start
            if status == 'success':
                output = replace_r['stdout']
            else:
                output = replace_r.get('stderr', '') # timeouts have no stderr
                if (
                    not status.startswith('fail:')
                    or 'AssertionError: Test case' not in output
                    or "Got: ''" in output
                ):
                    logger.debug('Bad output: {}/{}', idx, offset)
                    if snippet_id not in seen_snippets:
                        seen_snippets.append(snippet_id)
                        out_buf.write(response[start:end])
                    cur_pos = end
                    continue

            if snippet_id in seen_snippets and all(num in seen_nums for num in nums):
                continue
            did_patch = True
            seen_snippets.append(snippet_id)
            seen_nums.extend(nums)
            print(
                REPLACEMENT_PREFIX_TEMPLATE.format(
                    example_ids=', '.join(map(str, nums)),
                    plural_suffix='s' if len(nums) > 1 else '',
                ),
                replace_r['code'],
                REPLACEMENT_INFIX,
                output,
                REPLACEMENT_SUFFIX,
                sep='',
                end='',
                file=out_buf,
            )
            cur_pos = end
        if not did_patch:
            logger.debug('No patches, skipping: {}/{}', idx, offset)
            continue
        print(response[cur_pos:], file=out_buf)
        patched_response = out_buf.getvalue()

        r = {
            'idx': idx,
            'original_response': response,
            'patched_response': patched_response,
        }
        yield r


@app.command()
def main():
    _, flow_outd, step_outd = step_dirs(__file__)

    dep_replacements_f = flow_outd/'simulation_replacements/processed-report.jsonl'
    dep_ds_f = flow_outd/'fetch_process_solutions_py/report.jsonl'

    out_f = step_outd/'result.jsonl'
    out_exploded_root = step_outd/'exploded'
    out_exploded_root.mkdir(parents=True, exist_ok=True)

    with out_f.open('w') as out_fh:
        for r in gen_patched_responses(
            dep_replacements_rows=ser.jsonl_streamf(dep_replacements_f),
            dep_ds_rows=ser.jsonl_streamf(dep_ds_f),
        ):
            print(json.dumps(r), file=out_fh)
            out_exploded_dir = out_exploded_root/str(r['idx'])
            out_exploded_dir.mkdir(parents=True, exist_ok=True)
            (out_exploded_dir/'original-response.md').write_text(r['original_response'])
            (out_exploded_dir/'patched-response.md').write_text(r['patched_response'])

    logger.success('Wrote: {}', cwd_rel(out_f))


if __name__ == '__main__':
    app()
