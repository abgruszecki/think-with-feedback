# from pathlib import Path
# import datasets
# import json
# import random

# # Load 500 DeepSeek R1 completions
# ds_py = datasets.load_dataset('open-r1/codeforces-cots', 'solutions_py', split='train[:500]')

# # fixed seed to ensure same output
# random.seed(1)

# # Output directory for few-shot examples
# out_base = Path("icl-shots-cot")
# out_base.mkdir(parents=True, exist_ok=True)

# # Output mapping file
# mapping = {}

# # Heuristic to detect good Chain-of-Thought completions
# def is_good_cot(generation: str) -> bool:
#     gen_lower = generation.lower()
#     code_start = generation.find("```")
#     pre_code = generation[:code_start].strip() if code_start != -1 else generation.strip()

#     return (
#         len(pre_code.split()) >= 15 and
#         any(phrase in pre_code for phrase in [
#             "let's", "we can", "to solve", "first", "notice", "observe", "consider", "the idea"
#         ])
#     )

# # Generate 5 good CoT few-shot examples + mapping
# count = 0
# used_indices = set()

# # Get random order of indices from the dataset
# indices = list(range(len(ds_py)))
# random.shuffle(indices)

# for i in indices:
#     if count >= 5:
#         break
#     if i in used_indices:
#         continue
#     row = ds_py[i]
#     if is_good_cot(row['generation']):
#         shot_id = f"cot-{i+1}"
#         shot_dir = out_base / shot_id
#         shot_dir.mkdir(parents=True, exist_ok=True)

#         # Write prompt
#         with open(shot_dir / "prompt.md", "w") as f:
#             f.write(f"# {row['title']} ({row['contest_name']}, {row['contest_start_year']})\n\n")
#             f.write(row['prompt'])

#         # Write DeepSeek R1's generation
#         with open(shot_dir / "response.md", "w") as f:
#             f.write(row['generation'])

#         # Add to mapping
#         mapping[shot_id] = {
#             "title": row['title'],
#             "contest_name": row['contest_name'],
#             "contest_start_year": row['contest_start_year'],
#             "dataset_index": i
#         }

#         print(f"Saved: {shot_id} → {row['title']} ({row['contest_name']})")
#         used_indices.add(i)
#         count += 1

# # Save mapping.json
# with open(out_base / "mapping.json", "w") as f:
#     json.dump(mapping, f, indent=2)

# print(f"\n mapping.json created with {len(mapping)} entries.")

#!/usr/bin/env python3
from pathlib import Path
import datasets
import json

# Load the first 1000 DeepSeek R1 completions
ds_py = datasets.load_dataset('open-r1/codeforces-cots', 'solutions_py', split='train[:1000]')

# Where to write the chosen problems
out_base = Path("flow_mutants") / "chosen_problems"
out_base.mkdir(parents=True, exist_ok=True)

# Which dataset indices to pick
DESIRED_INDICES = [17, 116, 319, 740, 873]

mapping = {}

for i in DESIRED_INDICES:
    row = ds_py[i]
    shot_id = f"cot-{i}"
    shot_dir = out_base / shot_id
    shot_dir.mkdir(exist_ok=True)

    # Write prompt.md
    with open(shot_dir / "prompt.md", "w", encoding="utf-8") as f:
        f.write(f"# {row['title']} ({row['contest_name']}, {row['contest_start_year']})\n\n")
        f.write(row['prompt'])

    # Write response.md
    with open(shot_dir / "response.md", "w", encoding="utf-8") as f:
        f.write(row['generation'])

    # Record metadata
    mapping[shot_id] = {
        "dataset_index": i,
        "title": row['title'],
        "contest_name": row['contest_name'],
        "contest_start_year": row['contest_start_year'],
    }

    print(f"Saved {shot_id}: {row['title']}")

# Save the mapping file
with open(out_base / "mapping.json", "w", encoding="utf-8") as f:
    json.dump(mapping, f, indent=2)

print(f"\nCreated mapping.json with {len(mapping)} entries in {out_base}/")
