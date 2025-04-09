#!/usr/bin/env python3
import shutil
from pathlib import Path

from loguru import logger


def path2rel(p: Path) -> str:
    return str(p.relative_to(Path.cwd(), walk_up=True))


flowd = Path(__file__).parent
dep_outf = flowd.parent/'flow_main/out/process_solutions_py/report.jsonl'
outf = flowd/'out/fetch_process_solutions_py/report.jsonl'
outf.parent.mkdir(parents=True, exist_ok=True)

shutil.copy(dep_outf, outf)
logger.success('Copied {} to {}', path2rel(dep_outf), path2rel(outf))