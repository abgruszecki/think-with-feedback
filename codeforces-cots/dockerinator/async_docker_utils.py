import asyncio
from pathlib import Path
import re

from loguru import logger

from .asyncer import run_proc


async def _docker_kill_container(cidfile: str):
    # at this point `docker run` is killed but the container keeps running
    cid = '???' # make sure cid is bound in the `except`
    try:
        cid = Path(cidfile).read_text()
        proc, stdout, stderr = await run_proc(
            'docker', 'kill',
            # docker stops containers by first sending SIGTERM and then SIGKILL after 10s
            # we don't care so we just send SIGKILL immediately
            '--signal', 'SIGKILL',
            cid,
            input='', timeout=10,
        )
        if proc.returncode != 0:
            logger.error(
                'Failed to kill container cid={}, docker kill returned {}\n#STDOUT#\n{}\n#STDERR#\n{}',
                cid, proc.returncode, stdout, stderr,
            )
        else:
            # it takes a moment for the container to die
            await asyncio.sleep(1)
    except Exception:
        logger.exception('Failed to kill container cid={}', cid)


async def _running_container_count(image_name: str) -> int:
    proc, stdout, stderr = await run_proc(
        'docker', 'ps',
        '-q', # print ids only
        '--filter', f'ancestor={image_name}',
        input='', timeout=10)
    assert proc.returncode == 0, \
        f'docker ps failed with {proc.returncode}: \n#STDOUT#\n{stdout}\n#STDERR#\n{stderr}'
    return len(re.findall(r'\w\b', stdout)) # count word ends


async def _wait_for_running_containers(*, image_name: str,max_containers: int, sleep_secs: int):
    while True:
        try:
            running_containers = await _running_container_count(image_name)
            if running_containers < max_containers:
                break
            else:
                logger.error(
                    'Expected <{} running {} containers, but got {}; will re-count in {}s.',
                    max_containers,
                    image_name,
                    running_containers,
                    sleep_secs,
                )
        except Exception:
            logger.exception('Failed to get running container count, will retry in {} seconds', sleep_secs)
        await asyncio.sleep(sleep_secs)