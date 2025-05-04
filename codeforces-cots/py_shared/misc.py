from collections import namedtuple
from datetime import datetime
from pathlib import Path

step_data_t = namedtuple('step_data_t', ['flowd', 'flow_outd', 'resolved_outd'])
def step_dirs(
    file_attr, # should be the __file__ of the step script
    *,
    tag: str | None = None,
    no_subflow: bool = False,
    has_runs: bool = False,
    extend_run: str | Path | None = None,
    force: bool = False,
) -> step_data_t:
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
                extend_run_relpath = extend_run.resolve().relative_to(step_outd.resolve())
                assert len(extend_run_relpath.parts) == 1, f'Not a run dir: {extend_run}'
                if extend_run_relpath.name == 'last':
                    resolved_outd = last_run_outd_symlink.readlink()
                else:
                    resolved_outd = step_outd/extend_run_relpath
            else:
                resolved_outd = step_outd/datetime.now().strftime('%Y%m%dT%H%M%S')
        if in_subflow:
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

    return step_data_t(flowd, flow_outd, resolved_outd)


def cwd_rel(p: Path) -> Path:
    return p.relative_to(Path.cwd(), walk_up=True)