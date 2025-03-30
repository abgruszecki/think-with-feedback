import asyncio
from pathlib import Path
from typing import Any, Awaitable, Callable
import json

from loguru import logger
from tqdm.asyncio import tqdm as tqdm_async


type StepResult = None | str | tuple[str, dict]


async def run_proc(
    *cmd: str,
    input: str,
    timeout: float,
    **kwargs: Any,
) -> tuple[asyncio.subprocess.Process, str, str]:
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        **kwargs,
    )
    try:
        stdout, stderr = await asyncio.wait_for(
            proc.communicate(input.encode()),
            timeout=timeout
        )
        return proc, stdout.decode(), stderr.decode()
    except asyncio.TimeoutError as e:
        proc.kill()
        # Wait for the process to die.
        # Bad idea? In unusual conditions the process may actually not die:
        # this happened for me when the command was `docker run`.
        # May be the parent wasn't running as root, so it couldn't kill the child.
        # TODO: add another timeout here too?
        await proc.wait()
        raise e


async def __process(
    limiter: asyncio.Semaphore,
    p: Path,
    process_fn: Callable[[Path], Awaitable[StepResult]],
) -> tuple[dict, Exception|None]:
    problem_name: str = p.name
    async with limiter:
        try:
            res0 = await process_fn(p)
            if not res0:
                res = {
                    'problem': problem_name,
                    'status': 'success',
                }
            elif isinstance(res0, str):
                res = {
                    'problem': problem_name,
                    'status': res0,
                }
            else:
                res = {
                    'problem': problem_name,
                    'status': res0[0],
                }
                res.update(res0[1])

            return res, None
        except Exception as e:
            res = {
                'problem': problem_name,
                'status': 'fail:exception',
                'details': str(e),
            }
            return res, e


# TODO(alex): change the argument order and refactor the callsites...
async def __go(
    process_fn: Callable[[Path], Awaitable[StepResult]],
    problems: list[Path],
    work_dir: Path | None, # for logging
    phase_name: str, # as above
    log_file: Path | None = None,
    completion_callback: Callable[[dict], Awaitable[None]] | None = None,
    concurrency_limit: int = 10,
):
    if log_file is None:
        assert work_dir is not None
        log_file = work_dir/f'report_{phase_name}.jsonl'
    logger.info('Starting {}...', phase_name)
    limiter = asyncio.Semaphore(concurrency_limit)
    with open(log_file, 'w+') as f:
        with tqdm_async(total=len(problems)) as pbar:
            for res in asyncio.as_completed(__process(limiter, p, process_fn) for p in problems):
                res, e = await res
                if e:
                    try:
                        # Use Loguru, it formats traces well. Also: we log here not when e is caught,
                        # that way redrawing the progress bar doesn't interfere with the trace.
                        logger.opt(exception=e) \
                            .error('Exception in {} for problem {}', phase_name, res['problem'])
                    except Exception:
                        logger.exception('Failed to log exception')
                if completion_callback:
                    await completion_callback(res)
                pbar.update(1)
                f.write(json.dumps(res))
                f.write('\n')