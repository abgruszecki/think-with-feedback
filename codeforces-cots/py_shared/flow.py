from collections import namedtuple
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import typer

from . import ser as ser # re-export (ser should probably become a submodule)


type Jsonable = str|int|bool|list['Jsonable']|dict[str, 'Jsonable']
type JsonableDict = dict[str, Jsonable]


@dataclass
class KeyCols():
    names: tuple[str, ...]

    def values(self, r: dict[str, Any]) -> tuple[Any, ...]:
        return tuple(r[n] for n in self.names)

    def kvs(self, r: dict[str, Any]) -> dict[str, Any]:
        return { n: r[n] for n in self.names }

    def key(self, r: dict[str, Any], *, sep: str) -> str:
        return sep.join(str(r[n]) for n in self.names)


StepDataNT = namedtuple('step_data_t', ['flowd', 'flow_outd', 'resolved_outd'])


class StepDirs():
    flowd: Path
    flow_outd: Path

    step_outd: Path

    @property
    def run_outd(self) -> Path:
        if not self._run_outd:
            raise ValueError('run_outd not set, was has_runs=True?')
        return self._run_outd

    def __init__(
        self,
        flowd: Path,
        flow_outd: Path,
        step_outd: Path,
        run_outd: Path | None,
    ):
        self.flowd = flowd
        self.flow_outd = flow_outd
        self.step_outd = step_outd
        self._run_outd = run_outd


def step_dirs(
    file_attr, # should be the __file__ of the step script
    *,
    tag: str | None = None,
    no_subflow: bool = False,
    has_runs: bool = False,
    extend_run: str | Path | None = None,
    force: bool = False,
) -> StepDataNT:
    sd = dirs(
        file_attr=file_attr,
        tag=tag,
        no_subflow=no_subflow,
        has_runs=has_runs,
        extend_run=extend_run,
        force=force,
    )
    return StepDataNT(sd.flowd, sd.flow_outd, sd.step_outd)


def dirs(
    file_attr, # should be the __file__ of the step script
    *,
    tag: str | None = None,
    no_subflow: bool = False,
    has_runs: bool = False,
    # TODO it doesn't make sense to pass 'last' here. Pass a bool instead.
    extend_run: str | Path | None = None,
    force: bool = False,
) -> StepDirs:
    # TODO allow extend_run to point to this step's output dir?
    assert not (tag and has_runs), 'tag and has_runs not (yet?) supported together'
    if extend_run is not None:
        assert has_runs, 'extend_run requires has_runs'
        extend_run = Path(extend_run)

    maybe_in_subflow = False
    script_relpath = None
    flowd = None
    for p in Path(file_attr).absolute().parents:
        if not p.name.startswith('flow_'):
            maybe_in_subflow = True
            continue
        flowd = p
        script_relpath = Path(file_attr).absolute().relative_to(p)
        break
    if flowd is None: # fun fact: a for..else also works here but Cursor doesn't like it :)
        raise ValueError(f'Could not find the flow parent dir for: {file_attr}')
    flow_outd = flowd/'out'
    assert script_relpath is not None

    script_relpath_parts = script_relpath.parts
    if len(script_relpath_parts) not in (1, 2):
        raise ValueError(f'Highly nested subflows not supported: {script_relpath}')
    step_relpath = Path(script_relpath_parts[0])
    step_name = step_relpath.stem
    if '_t_' in step_name:
        untagged_prefix = step_name.split('_t_', 1)[0]
        step_name = untagged_prefix

    tag_suffix = ''
    if tag:
        tag_suffix = tag if tag.startswith('+') else ('+'+tag)

    in_subflow = maybe_in_subflow and not no_subflow
    if not in_subflow:
        assert not extend_run, 'extend_run requires a subflow'
        step_outd = flow_outd/(step_name+tag_suffix)
        substep_name = None
    else:
        step_outd = flow_outd/step_name
        substep_name = Path(script_relpath_parts[1]).stem
        step_outd_symlink = flowd/step_relpath/'out'
        step_outd_symlink.unlink(missing_ok=True)
        step_outd_symlink.symlink_to(step_outd, target_is_directory=True)

    last_run_outd_symlink: Path | None = None
    def _resolve_outd() -> Path:
        nonlocal last_run_outd_symlink
        resolved_outd = step_outd
        if has_runs:
            last_run_outd_symlink = step_outd/'last'
            if extend_run:
                if extend_run.name == 'last':
                    # resolved_outd = last_run_outd_symlink.readlink()
                    raise NotImplementedError('There is a bug in this code path. I think.')
                else:
                    extend_run_relpath = extend_run.resolve().relative_to(step_outd.resolve())
                    assert len(extend_run_relpath.parts) == 1, f'Not a run dir: {extend_run}'
                    resolved_outd = step_outd/extend_run_relpath
            else:
                resolved_outd = step_outd/datetime.now().strftime('%Y%m%dT%H%M%S')
        if in_subflow:
            assert substep_name is not None
            resolved_outd = resolved_outd/substep_name
            if extend_run and not force:
                assert not resolved_outd.exists(), f'substep outd already exists: {resolved_outd}'
        return resolved_outd

    resolved_outd = _resolve_outd()
    resolved_outd.mkdir(parents=True, exist_ok=True)
    if has_runs:
        assert last_run_outd_symlink
        last_run_outd_symlink.unlink(missing_ok=True)
        last_run_outd_symlink.symlink_to(resolved_outd, target_is_directory=True)
    last_outd_symlink = flow_outd/'last'
    last_outd_symlink.unlink(missing_ok=True)
    last_outd_symlink.symlink_to(resolved_outd, target_is_directory=True)

    return StepDirs(
        flowd=flowd,
        flow_outd=flow_outd,
        step_outd=resolved_outd,
        run_outd=resolved_outd.parent if has_runs else None,
    )


def cwd_rel(p: Path) -> Path:
    return p.relative_to(Path.cwd(), walk_up=True)


def InputDirArg(decl: str | None = None):
    typer_decls = [decl] if decl else []
    return typer.Argument(..., *typer_decls, exists=True, file_okay=False, dir_okay=True, readable=True)


def InputDirOption(decl: str | None = None):
    typer_decls = [decl] if decl else []
    return typer.Option(..., *typer_decls, exists=True, file_okay=False, dir_okay=True, readable=True)


def InputFileOption(decl: str | None = None):
    typer_decls = [decl] if decl else []
    return typer.Option(..., *typer_decls, exists=True, file_okay=True, dir_okay=False, readable=True)

