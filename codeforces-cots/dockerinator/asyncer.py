# import asyncio
# from pathlib import Path
# from typing import Any, Awaitable, Callable
# import json

# from loguru import logger
# from tqdm.asyncio import tqdm as tqdm_async

# from typing import TypeAlias

# StepResult: TypeAlias = None | str | tuple[str, dict]
# # type StepResult = None | str | tuple[str, dict]


# async def run_proc(
#     *cmd: str,
#     input: str | None,
#     timeout: float,
#     **kwargs: Any,
# ) -> tuple[asyncio.subprocess.Process, str, str]:
#     proc = await asyncio.create_subprocess_exec(
#         *cmd,
#         stdin=asyncio.subprocess.PIPE if input is not None else None,
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE,
#         **kwargs,
#     )
#     try:
#         stdout, stderr = await asyncio.wait_for(
#             proc.communicate(input.encode() if input is not None else None),
#             timeout=timeout
#         )
#         return proc, stdout.decode(), stderr.decode()
#     except asyncio.TimeoutError as e:
#         proc.kill()
#         # Wait for the process to die.
#         # Bad idea? In unusual conditions the process may actually not die:
#         # this happened for me when the command was `docker run`.
#         # May be the parent wasn't running as root, so it couldn't kill the child.
#         # TODO: add another timeout here too?
#         await proc.wait()
#         raise e


# async def __process[X](
#     limiter: asyncio.Semaphore,
#     it: X,
#     item_id: str,
#     process_fn: Callable[[X, str], Awaitable[StepResult]],
# ) -> tuple[dict, Exception|None]:
#     async with limiter:
#         try:
#             res0 = await process_fn(it, item_id)
#             if not res0:
#                 res = {
#                     'item': item_id,
#                     'status': 'success',
#                 }
#             elif isinstance(res0, str):
#                 res = {
#                     'item': item_id,
#                     'status': res0,
#                 }
#             else:
#                 res = {
#                     'item': item_id,
#                     'status': res0[0],
#                 }
#                 res.update(res0[1])

#             return res, None
#         except Exception as e:
#             res = {
#                 'item': item_id,
#                 'status': 'fail:exception',
#                 'details': str(e),
#             }
#             return res, e


# # TODO(alex): change the argument order and refactor the callsites...
# async def __go[X](
#     process_fn: Callable[[X, str], Awaitable[StepResult]],
#     items: list[tuple[X, str]],
#     work_dir: Path | None, # for logging
#     phase_name: str, # as above
#     log_file: Path | None = None,
#     completion_callback: Callable[[dict], Awaitable[None]] | None = None,
#     concurrency_limit: int = 10,
# ):
#     if log_file is None:
#         assert work_dir is not None
#         log_file = work_dir/f'report_{phase_name}.jsonl'
#     logger.info('Starting {}...', phase_name)
#     limiter = asyncio.Semaphore(concurrency_limit)
#     with open(log_file, 'w+') as f:
#         with tqdm_async(total=len(items)) as pbar:
#             for res in asyncio.as_completed(__process(limiter, item, item_id, process_fn) for item, item_id in items):
#                 res, e = await res
#                 if e:
#                     try:
#                         # Use Loguru, it formats traces well. Also: we log here not when e is caught,
#                         # that way redrawing the progress bar doesn't interfere with the trace.
#                         logger.opt(exception=e) \
#                             .error('Exception in {} for item {}', phase_name, res['item'])
#                     except Exception:
#                         logger.exception('Failed to log exception')
#                 if completion_callback:
#                     await completion_callback(res)
#                 pbar.update(1)
#                 f.write(json.dumps(res))
#                 f.write('\n')

import asyncio
from pathlib import Path
from typing import Any, Awaitable, Callable, TypeAlias, TypeVar
import json

from loguru import logger
from tqdm.asyncio import tqdm as tqdm_async

# A union alias for the possible return types of your steps
StepResult: TypeAlias = None | str | tuple[str, dict]

# Declare a type variable for generic item types
X = TypeVar("X")


async def run_proc(
    *cmd: str,
    input: str | None,
    timeout: float,
    **kwargs: Any,
) -> tuple[asyncio.subprocess.Process, str, str]:
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdin=asyncio.subprocess.PIPE if input is not None else None,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        **kwargs,
    )
    try:
        stdout, stderr = await asyncio.wait_for(
            proc.communicate(input.encode() if input is not None else None),
            timeout=timeout
        )
        return proc, stdout.decode(), stderr.decode()
    except asyncio.TimeoutError as e:
        proc.kill()
        await proc.wait()
        raise e


async def __process(
    limiter: asyncio.Semaphore,
    it: X,
    item_id: str,
    process_fn: Callable[[X, str], Awaitable[StepResult]],
) -> tuple[dict, Exception | None]:
    async with limiter:
        try:
            res0 = await process_fn(it, item_id)
            if not res0:
                res = {"item": item_id, "status": "success"}
            elif isinstance(res0, str):
                res = {"item": item_id, "status": res0}
            else:
                status, details = res0
                res = {"item": item_id, "status": status}
                res.update(details)

            return res, None
        except Exception as e:
            return (
                {"item": item_id, "status": "fail:exception", "details": str(e)},
                e,
            )


async def __go(
    process_fn: Callable[[X, str], Awaitable[StepResult]],
    items: list[tuple[X, str]],
    work_dir: Path | None,                     # for logging fallback
    phase_name: str,                           # descriptive phase name
    log_file: Path | None = None,
    completion_callback: Callable[[dict], Awaitable[None]] | None = None,
    concurrency_limit: int = 10,
):
    if log_file is None:
        assert work_dir is not None
        log_file = work_dir / f'report_{phase_name}.jsonl'

    logger.info('Starting {}...', phase_name)
    limiter = asyncio.Semaphore(concurrency_limit)

    with open(log_file, 'w+') as f:
        with tqdm_async(total=len(items)) as pbar:
            # Schedule all tasks, then await them as they complete
            tasks = [
                __process(limiter, item, item_id, process_fn)
                for item, item_id in items
            ]
            for coro in asyncio.as_completed(tasks):
                res, err = await coro

                if err:
                    try:
                        logger.opt(exception=err).error(
                            'Exception in {} for item {}', phase_name, res['item']
                        )
                    except Exception:
                        logger.exception('Failed to log exception')

                if completion_callback:
                    await completion_callback(res)

                pbar.update(1)
                f.write(json.dumps(res) + '\n')
