import asyncio
import json
from multiprocessing import cpu_count
import os
from pathlib import Path
import tempfile

from loguru import logger
import typer

from .asyncer import StepResult, __go, run_proc
from .async_docker_utils import _docker_kill_container, _running_container_count, _wait_for_running_containers


DEFAULT_TIMEOUT_S = 60
DEFAULT_DOCKER_COMMAND = [
    "docker", "run",
    "--rm", "-i",
    "--memory", "500M",
    "--oom-score-adj", "1000",
]


def async_exec(
    executor_image_name: str,
    inputs: list[Path],
    input_filename_glob: str = '*',
    docker_command: list[str] = DEFAULT_DOCKER_COMMAND,
    executor_args: list[str] = [],
    max_workers: int | None = None,
    timeout_s: int = DEFAULT_TIMEOUT_S,
    report_path: Path = Path('exec-report.jsonl'),
):
    if max_workers is None:
        max_workers = max(1, cpu_count() - 1)
        logger.info('Defaulting worker count to: {}', max_workers)

    report_path_suffix = report_path.suffix
    if report_path_suffix not in ('.jsonl', '.yaml'):
        raise typer.BadParameter(f'Report path should end in .jsonl or .yaml. Got: {report_path}')

    # A file's id is normally its path except the extension,
    # but for convenience if the only input source is a directory
    # we skip the directory name in the IDs.
    # (Maybe this should be a CLI option?)
    use_short_ids = len(inputs) == 1 and inputs[0].is_dir()
    def long_id(path: Path) -> str:
        parent = path.parent
        if parent == Path('.'):
            return path.stem
        return str(parent / path.stem)
    def file_id(path: Path) -> str:
        # if use_short_ids:
        #     return path.stem
        if use_short_ids:
            return long_id(path.relative_to(inputs[0]))
        else:
            return long_id(path)

    files_to_exec = []
    def visit_dir(path: Path):
        for file in (p for p in path.glob(input_filename_glob) if p.is_file()):
            files_to_exec.append(file)
        for subdir in (p for p in path.iterdir() if p.is_dir()):
            visit_dir(subdir)

    for path in inputs:
        if path.is_dir():
            visit_dir(path)
        else:
            files_to_exec.append(path)

    ### START OF THE ACTUAL "BUSINESS" CODE ###
    # TODO: deduplicate – most of this code is also in `discourse_problem_generator`.
    async def do_exec(file: Path) -> StepResult:
        # Sanity check: make sure the container count is as expected.
        # If this is a problem for you, comment out this block.
        await _wait_for_running_containers(image_name=executor_image_name, max_containers=max_workers, sleep_secs=10)

        problem_id = file_id(file)

        cidfile = tempfile.mktemp(dir=tempfile.gettempdir())
        try:
            command = docker_command.copy()
            command.append('--cidfile')
            command.append(cidfile)
            command.append(executor_image_name)
            command.extend(executor_args)
            # TODO: running containers can be factored out
            proc, stdout, stderr = await run_proc(
                *command,
                input=file.read_text(),
                timeout=timeout_s,
            )
        except asyncio.TimeoutError:
            await _docker_kill_container(cidfile)
            return 'fail:timeout', {
                'problem': problem_id,
                'time-secs': timeout_s,
            }
        finally:
            os.unlink(cidfile)

        if proc.returncode != 0:
            return 'fail:nonzero-exit', {
                'problem': problem_id,
                'stdout': stdout,
                'stderr': stderr,
            }
        return 'success', {
            'problem': problem_id,
            'stdout': stdout,
            'stderr': stderr,
        }

    async def __really_go():
        running_containers = await _running_container_count(executor_image_name)
        if running_containers > 0:
            # in this case we will run less jobs than requested. Probably
            print(f'Expected 0 running {executor_image_name} containers, but got {running_containers}')
            # ask the user to confirm
            confirm = input('This may cause issues. Continue? (Y/n) ')
            if confirm and confirm.lower() != 'y':
                return

        async def log_bad_results(res: dict):
            if res['status'] != 'success':
                problem_name = res['problem']
                stdout = res.get('stdout', None)
                stderr = res.get('stderr', None)
                if stdout is not None:
                    assert stderr is not None
                    logger.warning('Got bad result ({}) for problem `{}`\n#STDOUT#\n{}#STDERR#\n{}', res['status'], problem_name, stdout, stderr)
                else:
                    logger.warning('Got bad result ({}) for problem `{}`', res['status'], problem_name)

        await __go(
            do_exec, files_to_exec, None, 'evaluation',
            log_file=report_path,
            concurrency_limit=max_workers,
            completion_callback=log_bad_results,
        )

    asyncio.run(__really_go())


