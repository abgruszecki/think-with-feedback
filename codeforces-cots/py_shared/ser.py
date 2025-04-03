import json
from pathlib import Path


def json_dumpf(obj, pathlike):
    with pathlike.open('w') as fh:
        json.dump(obj, fh)


def jsonl_streamf(pathlike):
    with open(pathlike, 'r') as fh:
        for line in fh:
            yield json.loads(line)


def jsonl_loadf(pathlike):
    return list(jsonl_streamf(pathlike))


def jsonl_dumpf(data, pathlike):
    with open(pathlike, 'w') as fh:
        for row in data:
            print(json.dumps(row), file=fh)


def str_dumpf(obj, pathlike):
    Path(pathlike).write_text(str(obj))