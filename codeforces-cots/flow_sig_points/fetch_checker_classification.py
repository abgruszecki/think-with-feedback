#!/usr/bin/env python3
from pathlib import Path
import shutil

from loguru import logger

import py_shared.flow as fl


ctx = fl.dirs(__file__)
dep_outd = ctx.flowd.parent/'flow_checker_classification/out/process_checker_classifications'
outf = ctx.step_outd/'data.jsonl'

dep_out_files = []
for path in dep_outd.glob('*--processed-checker-classifications.jsonl'):
    ts = path.stem.split('-', 1)[0]
    dep_out_files.append((path, ts))
dep_out_files.sort(key=lambda x: x[1], reverse=True)

source_f = dep_out_files[0][0]
shutil.copy(source_f, outf)
logger.info('Copied {} to {}', fl.cwd_rel(source_f), fl.cwd_rel(outf))
