#!/usr/bin/env python3
import json
from pathlib import Path

# --- Configuration ---
# Path to your fuzzable JSONL file
FUZZABLE_JSONL = Path("dataset/fuzzable-final-answers.jsonl")

# The indices you want to extract
DESIRED_IDX = {17, 116, 319, 740, 873}

# Where to write the extracted solutions
OUT_DIR = Path("extracted_solutions")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def main():
    with FUZZABLE_JSONL.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            entry = json.loads(line)
            idx = int(entry.get("idx", -1))
            if idx in DESIRED_IDX:
                code = entry["final_answer"]
                out_path = OUT_DIR / f"{idx}.py"
                with out_path.open("w", encoding="utf-8") as wf:
                    wf.write(code)
                print(f"Extracted idx={idx} → {out_path}")

    missing = DESIRED_IDX - {int(p.stem) for p in OUT_DIR.glob("*.py")}
    if missing:
        print(f"Warning: could not find entries for indices: {sorted(missing)}")

if __name__ == "__main__":
    main()
