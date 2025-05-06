from pathlib import Path
import os
import sys
import openai
import datetime
import json
import shutil

def read_file(filepath):
    with open(filepath, 'r') as f:
        return f.read()

system_msg = """\
During this conversation, you can execute Python snippets. \
When you are uncertain if your code is correct, \
write it together with some tests in a code block, and say RUN_SNIPPET.
You will see the output of the snippet in a Markdown code block, like this:

```python
print("Hello, world!")
```

RUN_SNIPPET
```text
Hello, world!
```\
"""

variants = ["variant-1", "variant-2", "variant-3"]

# Output directory setup
outd = Path("out_tejas_gpt4o_mini")
if outd.exists() and outd.is_dir():
    shutil.rmtree(outd)
outd.mkdir(parents=True, exist_ok=True)

# Setup OpenRouter client
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

# Loop over each variant
for variant in variants:
    messages = [{"role": "system", "content": system_msg}]

    # Add few-shot examples
    for shot_id in ['174', '180', '355', '377', '386']:
        shotd = Path(f"icl-shots-cot/cot-{shot_id}")
        messages.extend([
            {"role": "user", "content": read_file(shotd / "prompt.md")},
            {"role": "assistant", "content": read_file(shotd / "response.md")},
        ])

    # Add the test prompt and partial output
    prompt = read_file(f"data/request-{variant}/prompt.md")
    partial_output = read_file(f"data/request-{variant}/partial-output.md")
    messages.extend([
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": partial_output},
    ])

    # Query GPT-4o-mini via OpenRouter
    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=messages,
        temperature=0.2,
        max_tokens=1024,
    )

    msg = response.choices[0].message

    # Print to terminal and optionally to file
    def print_msg(msg, file=None):
        if hasattr(msg, 'reasoning') and msg.reasoning:
            print('<think>', file=file)
            print(msg.reasoning, file=file)
            print('</think>', file=file)
        print(msg.content, file=file)

    print_msg(msg)

    # Save to markdown and JSON
    timestamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    with open(outd / f"{timestamp}--gpt4o-mini--{variant}.md", "w") as f:
        print_msg(msg, f)
    with open(outd / f"{timestamp}--gpt4o-mini--{variant}.json", "w") as f:
        json.dump(response.model_dump(mode="json"), f)
