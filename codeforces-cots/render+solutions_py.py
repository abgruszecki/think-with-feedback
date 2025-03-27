import json
from pathlib import Path

tag = 'solutions_py'

outd = Path(f'out+{tag}')
outd.mkdir(exist_ok=True)

import datasets
ds = datasets.load_dataset('open-r1/codeforces-cots', 'solutions_py', split='train[:500]')

i = 1
for row in ds:
    with (outd/f'{i}.md').open('w') as fh2:
        fh2.write("# {title} ({contest_name}, {contest_start_year})\n".format(**row))
        fh2.write("# Prompt\n")
        fh2.write(row['prompt'] + '\n')
        fh2.write("# Response\n")
        fh2.write(row['generation'] + '\n')
    i += 1
