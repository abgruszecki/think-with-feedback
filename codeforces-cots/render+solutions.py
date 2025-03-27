import json
from pathlib import Path

tag = 'solutions'

outd = Path(f'out+{tag}')
outd.mkdir()

i = 1
with open(f'./codeforces-cots+{tag}.jsonl', 'r') as f:
    for line in f:
        data = json.loads(line)
        with (outd/f'{i}.md').open('w') as fh2:
            fh2.write("# {title} ({contest_name}, {contest_start_year})\n".format(**data))
            fh2.write("# Prompt\n")
            fh2.write(data['prompt'] + '\n')
            fh2.write("# Response\n")
            fh2.write(data['generation'] + '\n')
        i += 1
