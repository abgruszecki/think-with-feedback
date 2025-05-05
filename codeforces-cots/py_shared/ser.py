import json as json # re-export
from os import PathLike
from pathlib import Path
from typing import Any, Iterable, Iterator, Literal, Protocol


type Pathlike = str | bytes | PathLike[str] | PathLike[bytes]


class ModelClassProto[A](Protocol):
    def model_validate(self, obj: Any) -> A: ...


class ModelInstanceProto(Protocol):
    def model_dump(self, *, mode: str | Literal['json', 'python'] = 'json') -> dict: ...


# TODO support Pydantic model classes here
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


def model_jsonl_streamf[A](
    model: ModelClassProto[A],
    pathlike: Pathlike,
    start: int = 0,
    end: int = -1,
) -> Iterator[A]:
    for r in jsonl_streamf(pathlike, start, end):
        yield model.model_validate(r)


def model_jsonl_loadf[A](
    model: ModelClassProto[A],
    pathlike: Pathlike,
) -> list[A]:
    return list(model_jsonl_streamf(model, pathlike))


def model_jsonl_dumpf(
    data: Iterable[ModelInstanceProto],
    pathlike: Pathlike,
):
    jsonl_dumpf(
        (r.model_dump(mode='json') for r in data),
        pathlike,
    )

def str_dumpf(obj: Any, pathlike: Pathlike):
    Path(pathlike).write_text(str(obj))