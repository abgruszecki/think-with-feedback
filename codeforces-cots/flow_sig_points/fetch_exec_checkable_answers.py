#!/usr/bin/env python3
import shutil
from pathlib import Path

from loguru import logger

import py_shared.flow as fl


ctx = fl.dirs(__file__)
dep_outf = ctx.flowd.parent/'flow_main/out/exec_checkable_answers/report.jsonl'
outf = ctx.flow_outd/'fetch_exec_checkable_answers/report.jsonl'

shutil.copy(dep_outf, outf)
logger.success('Copied {} to {}', fl.cwd_rel(dep_outf), fl.cwd_rel(outf))