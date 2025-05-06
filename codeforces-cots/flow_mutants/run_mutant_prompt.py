#!/usr/bin/env python3
from pathlib import Path
import os
import openai

# Load file content
def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

# System message for the model
system_msg = """\
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

# Initialize the OpenRouter client
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

# List of problem IDs to process
PROBLEM_IDS = [17, 116, 319, 740, 873]
import time
for pid in PROBLEM_IDS:
    prompt_path = Path(f"mutant_fixing/cot-{pid}/prompt.md")
    if not prompt_path.exists():
        print(f"[{pid}] ❌ prompt.md not found at {prompt_path}")
        continue

    prompt = read_file(prompt_path)
    print(f"[{pid}] Prompt length (chars): {len(prompt)}")

    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user",   "content": prompt},
    ]
    response = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=messages
    )

    msg = response.choices[0].message

    out_path = Path(f"mutant_fixing/cot-{pid}/response.md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        if hasattr(msg, "reasoning") and msg.reasoning:
            f.write("<think>\n")
            f.write(msg.reasoning + "\n")
            f.write("</think>\n\n")
        f.write(msg.content)

    print(f"[{pid}] ✅ Wrote response.md")
