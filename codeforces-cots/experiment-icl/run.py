from pathlib import Path
import os
import sys
import openai


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

variant = "variant-6"

messages = []

messages.extend([
    {"role": "system", "content": system_msg},
])

# for shotd in Path("data/icl-shots").glob("*"):
for shot_id in ['418', '304', '486', '268', '641']:
    shotd = Path(f"data/icl-shots/{shot_id}")
    messages.extend([
        {"role": "user", "content": read_file(shotd / "prompt.md")},
        {"role": "assistant", "content": read_file(shotd / "response.md")},
    ])

prompt = read_file(f"data/request-{variant}/prompt.md")
partial_output = read_file(f"data/request-{variant}/partial-output.md")
messages.extend([
    {"role": "user", "content": prompt},
    {"role": "assistant", "content": partial_output},
])

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)

response = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages=messages,
)

# Print or save the response
def print_msg(msg, file=None):
    if hasattr(msg, 'reasoning') and msg.reasoning:
        print('<think>', file=file)
        print(msg.reasoning, file=file)
        print('</think>', file=file)
    else:
        print('Got no reasoning in the message', file=sys.stderr)
    print(msg.content, file=file)

msg = response.choices[0].message
print_msg(msg)

import datetime
timestamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")

# Optionally save to file
outd = Path('out')
outd.mkdir(parents=True, exist_ok=True)
with open(outd / f"{timestamp}--r1--{variant}.md", "w") as f:
    print_msg(msg, f)

# import json
# with open(outd / f"{timestamp}--r1--{variant}.json", "w") as f:
#     json.dump(response.model_dump(mode='json'), f)
