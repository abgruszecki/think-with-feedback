#!/usr/bin/env python3
import os
import sys
import json
import shutil
import datetime
from pathlib import Path

import openai

def read_file(filepath: Path) -> str:
    return filepath.read_text(encoding="utf-8")

# ─── Locate script and project directories ─────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

# ─── Constants ─────────────────────────────────────────────────────────────────
SYSTEM_MSG = """\
During this conversation, you can execute Python snippets. \
When you are uncertain if your code is correct, \
write it together with some tests in a code block, and say RUN_SNIPPET.
You will see the output of the snippet in a Markdown code block, like this:

```python
print("Hello, world!")
RUN_SNIPPET
Hello, world!
```\
"""

# The indices we want to test
SELECTED = ["17"]  # or ["17", "116", "319", "740", "873"]

# Where prompts live (absolute path)
PROMPTS_DIR = PROJECT_ROOT / "flow_mutants" / "chosen_problems"

# Output directory
OUT_DIR = SCRIPT_DIR / "out" / "deepseek_selected"
if OUT_DIR.exists():
    shutil.rmtree(OUT_DIR)
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Initialize OpenAI client
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

# ─── Main loop: send each prompt to Deepseek-R1 ────────────────────────────────
for idx in SELECTED:
    shot_dir   = PROMPTS_DIR / f"cot-{idx}"
    prompt_path = shot_dir / "prompt.md"

    # Debug print: absolute path and existence
    print(f"Checking prompt at: {prompt_path}  → exists? {prompt_path.exists()}", file=sys.stderr)
    if not prompt_path.exists():
        print(f"Missing prompt.md for index {idx}", file=sys.stderr)
        continue

    # Build messages
    messages = [
        {"role": "system", "content": SYSTEM_MSG},
        {"role": "user",   "content": read_file(prompt_path)},
    ]

    # Call the API
    response = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=messages,
    )
    msg = response.choices[0].message

    # Helper to print reasoning + content
    def print_msg(m, file=None):
        if getattr(m, "reasoning", None):
            print("<think>", file=file)
            print(m.reasoning, file=file)
            print("</think>", file=file)
        print(m.content, file=file)

    # Print to stdout
    print(f"\n=== Deepseek response for idx {idx} ===")
    print_msg(msg)

    # Save to Markdown and JSON
    timestamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    md_file   = OUT_DIR / f"{timestamp}--idx{idx}.md"
    json_file = OUT_DIR / f"{timestamp}--idx{idx}.json"

    with md_file.open("w", encoding="utf-8") as f_md:
        print_msg(msg, file=f_md)

    with json_file.open("w", encoding="utf-8") as f_json:
        json.dump(response.model_dump(mode="json"), f_json, indent=2)

print(f"\nAll selected prompts sent. Results in: {OUT_DIR}")
