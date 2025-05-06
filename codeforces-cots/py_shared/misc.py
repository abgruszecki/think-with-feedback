from collections import namedtuple
from pathlib import Path

step_data_t = namedtuple('step_data_t', ['flowd', 'flow_outd', 'step_outd'])
def step_dirs(file_attr, tag: str|None = None) -> step_data_t:
    p = Path(file_attr)
    if '_t_' in p.stem:
        untagged_prefix = p.stem.split('_t_', 1)[0]
        p = p.parent/untagged_prefix

    flowd = p.parent
    flow_outd = flowd/'out'
    tag_suffix = ''
    if tag:
        tag_suffix = tag if tag.startswith('+') else ('+'+tag)
    step_outd = flow_outd/(p.stem+tag_suffix)
    step_outd.mkdir(parents=True, exist_ok=True)
    return step_data_t(flowd, flow_outd, step_outd)


# def cwd_rel(p: Path) -> Path:
#     return p.relative_to(Path.cwd(), walk_up=True)

from pathlib import Path

def cwd_rel(p: Path) -> Path:
    try:
        # make p relative to cwd if it’s a subpath
        return p.relative_to(Path.cwd())
    except ValueError:
        # otherwise fall back to absolute
        return p.resolve()