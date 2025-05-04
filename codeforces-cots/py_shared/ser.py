import json as json # re-export
from os import PathLike
from pathlib import Path
from typing import Any, Iterable


type Pathlike = str | bytes | PathLike[str] | PathLike[bytes]



def json_dumpf(obj, pathlike: Pathlike):
    with open(pathlike, 'w') as fh:
        json.dump(obj, fh)


def json_loadf(pathlike: Pathlike):
    with open(pathlike, 'r') as fh:
        return json.load(fh)


def jsonl_streamf(pathlike: Pathlike, start: int = 0, end: int = -1):
    with open(pathlike, 'r') as fh:
        for i, line in enumerate(fh):
            if i < start:
                continue
            if end != -1 and i >= end:
                break
            yield json.loads(line)


def jsonl_loadf(pathlike: Pathlike):
    return list(jsonl_streamf(pathlike))


def jsonl_dumpf(data: Iterable[Any], pathlike: Pathlike):
    with open(pathlike, 'w') as fh:
        for row in data:
            print(json.dumps(row), file=fh)


def str_dumpf(obj: Any, pathlike: Pathlike):
    Path(pathlike).write_text(str(obj))