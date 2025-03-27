import datasets

ds_py = datasets.load_dataset('open-r1/codeforces-cots', 'solutions_py', split='train[:500]')
ds_py.to_json('./codeforces-cots__solutions_py.jsonl')
