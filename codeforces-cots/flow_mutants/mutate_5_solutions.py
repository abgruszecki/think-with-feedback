#!/usr/bin/env python3
import random
from collections import namedtuple
import importlib.util
import inspect
import json
from pathlib import Path
import os
import sys

from mutmut.__main__ import write_all_mutants_to_file
from tqdm import tqdm

import sys
from pathlib import Path

# Allow importing from ../py_shared
sys.path.append(str(Path(__file__).resolve().parent.parent / "py_shared"))

import ser
from test_code_maker import make_test_code

# --- Setup ---
random.seed(42)
NUM_MUTATIONS = 5

flow_d = Path(__file__).parent
data_path = flow_d / "dataset" / "fuzzable-final-answers.jsonl"
exploded_d = flow_d / "out" / "mutate_5" / "exploded"
answer_checks_d = flow_d / "out" / "mutate_5" / "answer-checks"
exploded_d.mkdir(parents=True, exist_ok=True)
answer_checks_d.mkdir(parents=True, exist_ok=True)

mutation_input = namedtuple("mutation_input", ["mutable", "suffix"])

def format_item_dirname(idx: int) -> str:
    return f"{idx:05d}"

def extract_mutable_lines(code: str) -> mutation_input:
    no_mut_suffix = " # pragma: no mutate"
    test_header = "import io\n\nTEST_CASES = ["
    assert test_header in code, f"Parsing error: {test_header} missing."

    def edit(text):
        for i, line in enumerate(text.splitlines()):
            if i < 4:
                line += no_mut_suffix
            yield line

    prefix, suffix = code.split(test_header, maxsplit=1)
    return mutation_input('\n'.join(edit(prefix)), test_header + suffix)

def _write_mutants(mutant_dir: Path, mutant_names: list[str], raw_mutant_file: Path, executable_code_suffix: str):
    mutant_dir.mkdir(exist_ok=True)
    for i, mut_name in enumerate(mutant_names):
        spec = importlib.util.spec_from_file_location(mut_name, raw_mutant_file.as_posix())
        mod = importlib.util.module_from_spec(spec).__loader__.load_module()
        source_code = inspect.getsource(getattr(mod, mut_name))
        full_code = source_code.replace(mut_name, "test_program") + "\n" + executable_code_suffix
        (mutant_dir / f"candidate_{i}.py").write_text(full_code)
        sys.modules.pop(spec.name)

def main():
    # Load dataset
    with open(data_path, "r", encoding="utf-8") as f:
        all_lines = [json.loads(line) for line in f if line.strip()]

    # Pick 5 random examples
    selected = random.sample(all_lines, NUM_MUTATIONS)

    print("✅ Selected problems for mutation:")
    for item in selected:
        idx = int(item["idx"])
        cf_problem = item.get("problem") or item.get("url") or "Unknown"
        print(f" - idx: {idx}, problem: {cf_problem}")

    for item in selected:
        idx = int(item["idx"])
        code = item["final_answer"]
        tests = item["examples"]

        item_dir = exploded_d / format_item_dirname(idx)
        item_dir.mkdir(exist_ok=True)

        # Write testable program
        test_code = make_test_code(code, tests)
        (item_dir / "executable_answer.py").write_text(test_code)

        # Mutate
        mutation_input_obj = extract_mutable_lines(test_code)
        mutant_names, _ = write_all_mutants_to_file(
            out=(item_dir / "raw_mutants.py").open("w"),
            source=mutation_input_obj.mutable,
            filename=item_dir.as_posix()
        )
        _write_mutants(
            answer_checks_d / format_item_dirname(idx),
            mutant_names,
            item_dir / "raw_mutants.py",
            mutation_input_obj.suffix,
        )

if __name__ == "__main__":
    main()