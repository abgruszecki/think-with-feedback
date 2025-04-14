from collections import namedtuple
from pathlib import Path
step_data_t = namedtuple('step_data_t', ['flowd', 'flow_outd', 'step_outd'])
def step_dirs(file_attr, tag: str|None = None) -> step_data_t:
    p = Path(file_attr)
    flowd = p.parent
    flow_outd = flowd/'out'
    tag_suffix = ''
    if tag:
        tag_suffix = tag if tag.startswith('+') else ('+'+tag)
    step_outd = flow_outd/(p.stem+tag_suffix)
    step_outd.mkdir(parents=True, exist_ok=True)
    return step_data_t(flowd, flow_outd, step_outd)