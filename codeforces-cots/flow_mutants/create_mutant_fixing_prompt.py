#!/usr/bin/env python3
import sys
from pathlib import Path

# Problem IDs to process
PROBLEM_IDS = [17, 116, 319, 740, 873]

INTRO = """You will be given a competitive programming problem.
Your task is to analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits. Explain why your chosen implementation strategy is the most efficient solution and then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must:
- Read input using input()
- Write output using print()
- Avoid any debug prints or extra output

Wrap your final solution in a single code block using triple backticks, like this:
```python
<your code here>
```"""

CLOSING_HEADER = """Mutant Code

'''python"""
CLOSING_FOOTER = """'''

Now you must:
1. Identify the bug(s) in the mutant code.
2. Clearly explain your correct algorithmic approach.
3. Write a correct and optimized Python 3 solution, ensuring correctness for all test cases and respecting the constraints.
4. Output only your final code in a valid Python code block, using input() and print() directly.
"""

# Base paths assuming you are in flow_mutants/
PROMPT_IN_BASE = Path("chosen_problems")
PROMPT_OUT_BASE = Path("mutant_fixing")
MUTANT_BASE = Path("out") / "mutate_5" / "answer-checks"

def extract_mutant_snippet(pid: int) -> str | None:
    subdir = str(pid).zfill(5)
    mutant_file = MUTANT_BASE / subdir / "candidate_2.py"
    if not mutant_file.exists():
        print(f"Mutant file not found for ID {pid}: {mutant_file}", file=sys.stderr)
        return None

    snippet = []
    recording = False
    for line in mutant_file.read_text(encoding="utf-8").splitlines():
        if not recording and line.startswith("def test_program"):
            recording = True
            snippet.append(line)
        elif recording:
            if line.strip() == "import io":
                break
            snippet.append(line)

    if not snippet:
        print(f"No valid test_program found for ID {pid}", file=sys.stderr)
        return None

    return "\n".join(snippet)

def generate_prompt(pid: int, mutant_code: str):
    in_file = PROMPT_IN_BASE / f"cot-{pid}" / "prompt.md"
    out_dir = PROMPT_OUT_BASE / f"cot-{pid}"
    out_file = out_dir / "prompt.md"

    if not in_file.exists():
        print(f"Original prompt.md not found for ID {pid}: {in_file}", file=sys.stderr)
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    original_md = in_file.read_text(encoding="utf-8").rstrip()

    # Insert actual mutant code into the closing
    closing_filled = "\n".join([
        CLOSING_HEADER,
        mutant_code.rstrip(),
        CLOSING_FOOTER
    ])

    final_prompt = "\n\n".join([INTRO.rstrip(), original_md, closing_filled]) + "\n"
    out_file.write_text(final_prompt, encoding="utf-8")
    print(f"Generated: {out_file}")

def main():
    for pid in PROBLEM_IDS:
        mutant_code = extract_mutant_snippet(pid)
        if mutant_code:
            generate_prompt(pid, mutant_code)

if __name__ == "__main__":
    main()
