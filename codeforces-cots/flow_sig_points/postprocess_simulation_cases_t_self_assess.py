#!/usr/bin/env python3
import typer

from py_shared import ser
from py_shared.misc import step_dirs
from flow_sig_points.postprocess_simulation_cases import postprocess_simulation_cases, _dep_cases_dirs_gen

app = typer.Typer()


@app.command()
def main():
    tag = 'self-assess'
    flowd, flow_outd, step_outd = step_dirs(__file__, tag)
    dep_ds_f = flow_outd/'fetch_process_solutions_py/report.jsonl'
    dep_cases_stepd = flow_outd/f'extract_simulation_cases+{tag}'

    def _dep_ds_kvgen():
        for r in ser.jsonl_streamf(dep_ds_f):
            yield r['idx'], r
    dep_ds_by_idx = dict(_dep_ds_kvgen())

    dep_cases_dirs = list(_dep_cases_dirs_gen(dep_cases_stepd))
    dep_cases_dirs.sort(key=lambda x: x.stem, reverse=True)

    postprocess_simulation_cases(
        dep_cases_dirs=dep_cases_dirs,
        dep_ds_by_idx=dep_ds_by_idx,
        step_outd=step_outd,
        only_explode=True,
        add_code=True,
    )


if __name__ == '__main__':
    app()
