#!/usr/bin/env python3
from dataclasses import dataclass
import json
from pathlib import Path

from tqdm import tqdm


root_outd = Path('./out')
outf = root_outd/'x--troublesome-example-outputs.jsonl'


@dataclass
class Result:
    needs_checker: bool
    is_troublesome: bool

    def merge(self, other: 'Result') -> 'Result':
        return Result(
            needs_checker=self.needs_checker or other.needs_checker,
            is_troublesome=self.is_troublesome or other.is_troublesome,
        )

    def matters(self) -> bool:
        return self.needs_checker or self.is_troublesome

def analyze(
    ex_out: str
) -> Result:
    needs_checker = False
    is_troublesome = False
    def res(): return Result(
        needs_checker=needs_checker,
        is_troublesome=is_troublesome,
    )

    one_line_had_proper_float = False
    all_lines_are_all_floats = True
    one_line_had_bool = False
    one_line_had_nonbool_alpha = False
    for ln in ex_out.splitlines():
        words = ln.split()

        any_is_proper_float = False
        all_are_floats = True
        any_is_bool = False
        had_nonbool_alpha = False
        for w in words:
            try:
                float(w)
                try:
                    int(w)
                except ValueError:
                    any_is_proper_float = True
            except ValueError:
                all_are_floats = False

            if w.lower() in ('yes', 'no', 'true', 'false'):
                any_is_bool = True
            elif any(c.isalpha() for c in w):
                had_nonbool_alpha = True

        if any_is_proper_float:
            one_line_had_proper_float = True
        if not all_are_floats:
            all_lines_are_all_floats = False
        if any_is_bool:
            one_line_had_bool = True
        if had_nonbool_alpha:
            one_line_had_nonbool_alpha = True

        if any_is_proper_float or any_is_bool:
            needs_checker = True
            if len(words) > 1 and (any_is_bool or (any_is_proper_float and not all_are_floats)):
                is_troublesome = True

    if one_line_had_proper_float and not all_lines_are_all_floats:
        is_troublesome = True
    if one_line_had_bool and one_line_had_nonbool_alpha:
        is_troublesome = True

    return res()


if __name__ == '__main__':
    import datasets
    ds = datasets.load_dataset('open-r1/codeforces-cots', 'solutions_py', split='train')
    outf.parent.mkdir(parents=True, exist_ok=True)
    with outf.open('w') as fh:
        for idx, r in enumerate(tqdm(ds)):
            res = Result(
                needs_checker=False,
                is_troublesome=False,
            )

            for ex in r['examples'] or []:
                res = res.merge(analyze(ex['output']))

            if res.matters():
                r = {
                    'idx': idx,
                    'id': r['id'],
                    'needs_checker': res.needs_checker,
                    'is_troublesome': res.is_troublesome,
                    # 'prompt': r['prompt'],
                    # 'examples': r['examples'],
                }
                print(json.dumps(r), file=fh)
