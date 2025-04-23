#!/usr/bin/env python3
import shutil
from pathlib import Path

from loguru import logger
import typer


app = typer.Typer()


def path2rel(p: Path) -> str:
    return str(p.relative_to(Path.cwd(), walk_up=True))


flowd = Path(__file__).parent
dep_outf = flowd.parent/'flow_main/out/process_solutions_py/report.jsonl'
outf = flowd/'out/fetch_process_solutions_py/report.jsonl'
outf.parent.mkdir(parents=True, exist_ok=True)


@app.command()
def main(
    link: bool = False,
):
    if not link:
        # Let's be careful not to overwrite the source...
        if outf.is_symlink():
            outf.unlink()
        shutil.copy(dep_outf, outf)
        logger.success('Copied {} to {}', path2rel(dep_outf), path2rel(outf))
    else:
        # NOTE this may blow up if the file exists, which may be what we want.
        outf.symlink_to(dep_outf)
        logger.success('Symlinked {} to {}', path2rel(dep_outf), path2rel(outf))


if __name__ == '__main__':
    app()
