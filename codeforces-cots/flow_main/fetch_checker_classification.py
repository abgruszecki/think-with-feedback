#!/usr/bin/env python3
from pathlib import Path
import shutil

from loguru import logger


flowd = Path(__file__).parent
dep_outd = flowd.parent/'flow_checker_classification/out/process_checker_classifications'
step_outd = flowd/'out/fetch_checker_classification'
step_outd.mkdir(parents=True, exist_ok=True)

dep_out_files = []
for path in dep_outd.glob('*--processed-checker-classifications.jsonl'):
    ts = path.stem.split('-', 1)[0]
    dep_out_files.append((path, ts))
dep_out_files.sort(key=lambda x: x[1], reverse=True)

source_f = dep_out_files[0][0]
outf = step_outd/'data.jsonl'
shutil.copy(source_f, outf)
logger.info('Copied {} to {}', source_f.relative_to(Path.cwd(), walk_up=True), outf.relative_to(Path.cwd()))
