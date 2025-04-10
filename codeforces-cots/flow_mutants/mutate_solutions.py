#!/usr/bin/env python3
"""
Given a dataset of `fuzzable-final-answers.jsonl`, mutate each program,
then save the mutants to executable files in out/mutate_solutions/answer-checks
and out/mutate_solutions/exploded.
Then, run exec_snippets on this dir to receive a report of which mutants
break tests.

NOTE: mutmut has very basic mutants, but we can add more. See mutmut.node_mutation.py
"""
from collections import namedtuple
import importlib.util
import inspect
import json
from pathlib import Path
import os
import sys

from mutmut.__main__ import write_all_mutants_to_file
from tqdm import tqdm

from py_shared import ser
from py_shared.test_code_maker import make_test_code


flow_d = Path(__file__).parent
exploded_d = flow_d / "out" / "mutate_solutions" / "exploded"
answer_checks_d = flow_d / "out" / "mutate_solutions" / "answer-checks"
mutation_candidates = ser.jsonl_loadf(flow_d / "dataset" / "fuzzable-final-answers.jsonl")

mutation_input = namedtuple("mutation_input", ["mutable", "suffix"])


def format_item_dirname(idx: int) -> str:
    return f'{idx:05d}' # digits for sorting


def extract_mutable_lines(code: str) -> mutation_input:
    """
    Extract the mutable function to be mutated with mutmut.
    Add signal for mutmut not to mutate some code-running lines for
    testing.

    Must be added to:
        - first 4 lines
    """
    no_mut_suffix = " # pragma: no mutate"
    test_header = "import io\n\nTEST_CASES = ["
    assert code.count(test_header) == 1, f"Parsing error: {test_header} must appear exactly once in {code}."

    def edit(text):
        for i,line in enumerate(text.split("\n")):
            if i < 4:
                line = line + no_mut_suffix
            yield line

    prefix, suffix = code.split(test_header, maxsplit=1)
    return mutation_input('\n'.join(edit(prefix)), test_header+suffix)


def _write_mutants(
    mutant_dir: Path,
    mutant_names: list[str],
    raw_mutant_file: Path,
    executable_code_suffix: str,
):
    mutant_dir.mkdir(exist_ok=True)
    for i,mut_name in enumerate(mutant_names):
        spec = importlib.util.spec_from_file_location(mut_name, raw_mutant_file.as_posix())
        mod = importlib.util.module_from_spec(spec).__loader__.load_module()
        source_code = inspect.getsource(getattr(mod, mut_name))
        executable_source_code = source_code.replace(mut_name, "test_program") + "\n" + executable_code_suffix
        (mutant_dir / f"candidate_{i}.py").write_text(executable_source_code)

        # NOTE loading all of these modules uses a lot of memory (16Gb is not enough).
        # Unloading them via sys.modules.pop() seems to work.
        # Freeing the memory every loop iteration is important.
        # If this stops working, good luck! Creating a new process in each loop iteration
        # seems to significantly slow things down (at least when I used fork).
        sys.modules.pop(spec.name)


def create_mutants():
    """
    Using mutmut, create mutated versions of all executable_answer.py programs. This includes
    mutants that may or may not pass tests. Writes mutants to answer_checks/000<id>/candidate_x.py
    """
    for candidate in tqdm(list(exploded_d.glob("*/executable_answer.py")), desc="Mutating"):
        mutation_input = extract_mutable_lines(candidate.read_text())
        # (candidate.parent / "mutmut_input.py").write_text(mutation_input.mutable + mutation_input.suffix)
        mutant_names, hash_by_function_name = write_all_mutants_to_file(
            out=(candidate.parent / "raw_mutants.py").open(mode="w"),
            source=mutation_input.mutable,
            filename=candidate.as_posix(),
        )
        _write_mutants(
            answer_checks_d / candidate.parts[-2],
            mutant_names,
            candidate.parent / "raw_mutants.py",
            mutation_input.suffix,
        )


def extract_mutation_candidates():
    """
    Save original fuzzing candidates to out/exploded. Save
    a mutmut-compatible version of the candidate for mutations
    """
    for line in tqdm(mutation_candidates, desc="Extracting mutation candidates"):
        item_d = exploded_d / format_item_dirname(line["idx"])
        item_d.mkdir(exist_ok=True)
        code, tests = line["final_answer"], line["examples"]
        test_code = make_test_code(code, tests)

        (item_d / "final_answer.py").write_text(code)
        (item_d / "executable_answer.py").write_text(test_code)
        ser.json_dumpf(tests, item_d / "examples.json")


if __name__ == "__main__":
    exploded_d.mkdir(exist_ok=True, parents=True)
    answer_checks_d.mkdir(exist_ok=True)
    extract_mutation_candidates()
    create_mutants()
