# import asyncio
# from dataclasses import dataclass, field
# from multiprocessing import cpu_count
# import os
# from pathlib import Path
# import shutil
# import tempfile
# from typing import Callable

# from loguru import logger

# from .asyncer import StepResult, __go, run_proc
# from .async_docker_utils import _docker_kill_container, _running_container_count, _wait_for_running_containers


# DEFAULT_TIMEOUT_S = 60
# DEFAULT_DOCKER_COMMAND = [
#     "docker", "run",
#     "--rm", "-i",
#     "--memory", "500M",
#     "--oom-score-adj", "1000",
# ]


# @dataclass
# class ExecutionArgs:
#     docker_command: list[str] = field(default_factory=lambda: DEFAULT_DOCKER_COMMAND)
#     executor_args: list[str] = field(default_factory=lambda: [])
#     max_workers: int | None = None
#     timeout_s: int = DEFAULT_TIMEOUT_S
#     report_path: Path = Path('exec-report.jsonl')


# def run_scripts_in_containers(
#     executor_image_name: str,
#     inputs: list[Path],
#     execution_args: ExecutionArgs,
#     input_filename_glob: str = '*',
# ):
#     """
#     Executes given files, each in a (Docker) container, in parallel
#     """

#     # A file's id is normally its path except the extension,
#     # but for convenience if the only input source is a directory
#     # we skip the directory name in the IDs.
#     # (Maybe this should be an option?)
#     use_short_ids = len(inputs) == 1 and inputs[0].is_dir()
#     def long_id(path: Path) -> str:
#         parent = path.parent
#         if parent == Path('.'):
#             return path.stem
#         return str(parent / path.stem)
#     def file_id(path: Path) -> str:
#         # if use_short_ids:
#         #     return path.stem
#         if use_short_ids:
#             return long_id(path.relative_to(inputs[0]))
#         else:
#             return long_id(path)

#     files_as_items = []
#     def visit_dir(path: Path):
#         for file in (p for p in path.glob(input_filename_glob) if p.is_file()):
#             files_as_items.append((file, file_id(file)))
#         for subdir in (p for p in path.iterdir() if p.is_dir()):
#             visit_dir(subdir)

#     for path in inputs:
#         if path.is_dir():
#             visit_dir(path)
#         else:
#             files_as_items.append((path, file_id(path)))

#     def prep_input(item: Path, tmpdir: Path | None) -> ItemExecutionSpec:
#         return ItemExecutionSpec(
#             stdin_source=item,
#         )

#     return _run_in_containers(
#         executor_image_name,
#         files_as_items,
#         prep_input,
#         make_tmpdir=False,
#         args=execution_args,
#     )

# def run_items_in_workdir_containers[X](
#     executor_image_name: str,
#     inputs: list[tuple[X, str]],
#     prepare_workdir: Callable[[X, Path], None],
#     execution_args: ExecutionArgs,
# ):
#     """
#     A minimal API:
#     prepares a tmp workdir for each input item,
#     mounts it into the container at `/workdir`,
#     and passes no input to the container.
#     """
#     def prep_input(
#         item: X,
#         tmpdir: Path | None,
#     ) -> ItemExecutionSpec:
#         assert tmpdir
#         prepare_workdir(item, tmpdir)
#         return ItemExecutionSpec(
#             stdin_source=None,
#             volumes=[VolumeSpec(
#                 mount_path='/workdir',
#                 local_volume_path=tmpdir,
#             )],
#         )

#     return _run_in_containers(
#         executor_image_name,
#         inputs,
#         prep_input,
#         make_tmpdir=True,
#         args=execution_args,
#     )


# @dataclass
# class ItemExecutionSpec:
#     stdin_source: Path | None
#     volumes: list['VolumeSpec'] = field(default_factory=lambda: [])

# @dataclass
# class VolumeSpec:
#     local_volume_path: Path
#     mount_path: str


# def _run_in_containers[X](
#     executor_image_name: str,
#     items: list[tuple[X, str]],
#     prepare_item: Callable[[X, Path | None], ItemExecutionSpec],
#     make_tmpdir: bool,
#     args: ExecutionArgs,
# ):
#     """
#     Run given items in parallel, each in a (Docker) container.

#     An "item" is anything which `prepare_item` can turn into `ItemExecutionSpec`,
#     a description of how to run the item with the given executor image.
#     (Right now the image can get data on the standard input and/or it can have volumes mounted.)
#     (`prepare_item` can create a directory hierarchy to be mounted,
#      and it can get a temporary directory as an argument if `make_tmpdir` is true.)

#     Each item is paired with an ID, used for logging and reporting.

#     ## Implementation notes ##
#     `items` is a list because its len is used for the progress bar.
#     items could come from a generator if we also get the len or don't care about the bar.

#     With some tweaks different items could be ran with different images.
#     Right now, we use `executor_image_name` to check how many containers are running,
#     but that can be removed if you like to live dangerously.
#     """
#     real_max_workers = args.max_workers
#     if args.max_workers in (None, 0):
#         real_max_workers = max(1, cpu_count() - 1)
#         if args.max_workers is None:
#             real_max_workers = min(real_max_workers, 16)
#         logger.info('Defaulting worker count to: {}', real_max_workers)
#     assert real_max_workers is not None

#     async def do_exec(item: X, item_id: str) -> StepResult:
#         # Sanity check: make sure the container count is as expected.
#         # If this is a problem for you, comment out this block.
#         await _wait_for_running_containers(image_name=executor_image_name, max_containers=real_max_workers, sleep_secs=10)

#         tmpdir = None
#         if make_tmpdir:
#             tmpdir = tempfile.mkdtemp()
#         try:
#             spec = prepare_item(item, Path(tmpdir) if tmpdir else None)
#         except Exception as e:
#             logger.exception('Exception when preparing item: {}', item_id)
#             return 'fail:preparation-exception', {
#                 'item': item_id,
#                 'error': str(e),
#             }

#         # Docker expects cidfile not to exist. This may lead to a turbo-rare race condition
#         # where another program creates a temporary file with the same name.
#         # To be ultra-safe, we could create cidfiles within a temporary directory.
#         cidfile = tempfile.mktemp()
#         try:
#             command = args.docker_command.copy()
#             command.append('--cidfile')
#             command.append(cidfile)
#             for v in spec.volumes:
#                 command.append('--volume')
#                 command.append(f'{v.local_volume_path}:{v.mount_path}')
#             command.append(executor_image_name)
#             command.extend(args.executor_args)
#             in_src = spec.stdin_source
#             proc, stdout, stderr = await run_proc(
#                 *command,
#                 input=in_src.read_text() if in_src else None,
#                 timeout=args.timeout_s,
#             )
#         except asyncio.TimeoutError:
#             await _docker_kill_container(cidfile)
#             return 'fail:timeout', {
#                 'item': item_id,
#                 'time-secs': args.timeout_s,
#             }
#         finally:
#             # cidfile may not exist if Docker didn't even try to run the container.
#             if os.path.exists(cidfile):
#                 os.unlink(cidfile)
#             if tmpdir:
#                 shutil.rmtree(tmpdir)

#         if proc.returncode != 0:
#             return 'fail:nonzero-exit', {
#                 'item': item_id,
#                 'stdout': stdout,
#                 'stderr': stderr,
#             }
#         return 'success', {
#             'item': item_id,
#             'stdout': stdout,
#             'stderr': stderr,
#         }

#     async def __really_go():
#         running_containers = await _running_container_count(executor_image_name)
#         if running_containers > 0:
#             # in this case we will run less jobs than requested. Probably
#             print(f'Expected 0 running {executor_image_name} containers, but got {running_containers}')
#             # ask the user to confirm
#             confirm = input('This may cause issues. Continue? (Y/n) ')
#             if confirm and confirm.lower() != 'y':
#                 return

#         # TODO maybe just count the bad results, show the count with the tqdm bar?
#         # async def log_bad_results(res: dict):
#         #     if res['status'] != 'success':
#         #         problem_name = res['problem']
#         #         stdout = res.get('stdout', None)
#         #         stderr = res.get('stderr', None)
#         #         if stdout is not None:
#         #             assert stderr is not None
#         #             logger.warning('Got bad result ({}) for problem `{}`\n#STDOUT#\n{}#STDERR#\n{}', res['status'], problem_name, stdout, stderr)
#         #         else:
#         #             logger.warning('Got bad result ({}) for problem `{}`', res['status'], problem_name)

#         await __go(
#             do_exec, items, None, 'evaluation',
#             log_file=args.report_path,
#             concurrency_limit=real_max_workers,
#             # completion_callback=log_bad_results,
#         )

#     asyncio.run(__really_go())

import asyncio
from dataclasses import dataclass, field
from multiprocessing import cpu_count
import os
from pathlib import Path
import shutil
import tempfile
from typing import Callable, TypeVar

from loguru import logger

from .asyncer import StepResult, __go, run_proc
from .async_docker_utils import _docker_kill_container, _running_container_count, _wait_for_running_containers

DEFAULT_TIMEOUT_S = 60
DEFAULT_DOCKER_COMMAND = [
    "docker", "run",
    "--rm", "-i",
    "--memory", "500M",
    "--oom-score-adj", "1000",
]

X = TypeVar("X")

@dataclass
class ExecutionArgs:
    docker_command: list[str] = field(default_factory=lambda: DEFAULT_DOCKER_COMMAND)
    executor_args: list[str] = field(default_factory=lambda: [])
    max_workers: int | None = None
    timeout_s: int = DEFAULT_TIMEOUT_S
    report_path: Path = Path('exec-report.jsonl')


def run_scripts_in_containers(
    executor_image_name: str,
    inputs: list[Path],
    execution_args: ExecutionArgs,
    input_filename_glob: str = '*',
):
    """
    Executes given files, each in a (Docker) container, in parallel
    """

    use_short_ids = len(inputs) == 1 and inputs[0].is_dir()

    def long_id(path: Path) -> str:
        parent = path.parent
        if parent == Path('.'):
            return path.stem
        return str(parent / path.stem)

    def file_id(path: Path) -> str:
        if use_short_ids:
            return long_id(path.relative_to(inputs[0]))
        else:
            return long_id(path)

    files_as_items = []
    def visit_dir(path: Path):
        for file in (p for p in path.glob(input_filename_glob) if p.is_file()):
            files_as_items.append((file, file_id(file)))
        for subdir in (p for p in path.iterdir() if p.is_dir()):
            visit_dir(subdir)

    for path in inputs:
        if path.is_dir():
            visit_dir(path)
        else:
            files_as_items.append((path, file_id(path)))

    def prep_input(item: Path, tmpdir: Path | None) -> 'ItemExecutionSpec':
        return ItemExecutionSpec(
            stdin_source=item,
        )

    return _run_in_containers(
        executor_image_name,
        files_as_items,
        prep_input,
        make_tmpdir=False,
        args=execution_args,
    )


def run_items_in_workdir_containers(
    executor_image_name: str,
    inputs: list[tuple[X, str]],
    prepare_workdir: Callable[[X, Path], None],
    execution_args: ExecutionArgs,
):
    """
    A minimal API:
    prepares a tmp workdir for each input item,
    mounts it into the container at /workdir,
    and passes no input to the container.
    """
    def prep_input(
        item: X,
        tmpdir: Path | None,
    ) -> 'ItemExecutionSpec':
        assert tmpdir
        prepare_workdir(item, tmpdir)
        return ItemExecutionSpec(
            stdin_source=None,
            volumes=[VolumeSpec(
                mount_path='/workdir',
                local_volume_path=tmpdir,
            )],
        )

    return _run_in_containers(
        executor_image_name,
        inputs,
        prep_input,
        make_tmpdir=True,
        args=execution_args,
    )


@dataclass
class ItemExecutionSpec:
    stdin_source: Path | None
    volumes: list['VolumeSpec'] = field(default_factory=lambda: [])

@dataclass
class VolumeSpec:
    local_volume_path: Path
    mount_path: str


def _run_in_containers(
    executor_image_name: str,
    items: list[tuple[X, str]],
    prepare_item: Callable[[X, Path | None], ItemExecutionSpec],
    make_tmpdir: bool,
    args: ExecutionArgs,
):
    """
    Run given items in parallel, each in a (Docker) container.

    Each item is paired with an ID, used for logging and reporting.
    """

    real_max_workers = args.max_workers
    if args.max_workers in (None, 0):
        real_max_workers = max(1, cpu_count() - 1)
        if args.max_workers is None:
            real_max_workers = min(real_max_workers, 16)
        logger.info('Defaulting worker count to: {}', real_max_workers)
    assert real_max_workers is not None

    async def do_exec(item: X, item_id: str) -> StepResult:
        await _wait_for_running_containers(
            image_name=executor_image_name,
            max_containers=real_max_workers,
            sleep_secs=10
        )

        tmpdir = None
        if make_tmpdir:
            tmpdir = tempfile.mkdtemp()
        try:
            spec = prepare_item(item, Path(tmpdir) if tmpdir else None)
        except Exception as e:
            logger.exception('Exception when preparing item: {}', item_id)
            return 'fail:preparation-exception', {
                'item': item_id,
                'error': str(e),
            }

        cidfile = tempfile.mktemp()
        try:
            command = args.docker_command.copy()
            command.append('--cidfile')
            command.append(cidfile)
            for v in spec.volumes:
                command.append('--volume')
                command.append(f'{v.local_volume_path}:{v.mount_path}')
            command.append(executor_image_name)
            command.extend(args.executor_args)
            in_src = spec.stdin_source
            proc, stdout, stderr = await run_proc(
                *command,
                input=in_src.read_text() if in_src else None,
                timeout=args.timeout_s,
            )
        except asyncio.TimeoutError:
            await _docker_kill_container(cidfile)
            return 'fail:timeout', {
                'item': item_id,
                'time-secs': args.timeout_s,
            }
        finally:
            if os.path.exists(cidfile):
                os.unlink(cidfile)
            if tmpdir:
                shutil.rmtree(tmpdir)

        if proc.returncode != 0:
            return 'fail:nonzero-exit', {
                'item': item_id,
                'stdout': stdout,
                'stderr': stderr,
            }
        return 'success', {
            'item': item_id,
            'stdout': stdout,
            'stderr': stderr,
        }

    async def __really_go():
        running_containers = await _running_container_count(executor_image_name)
        if running_containers > 0:
            print(f'Expected 0 running {executor_image_name} containers, but got {running_containers}')
            confirm = input('This may cause issues. Continue? (Y/n) ')
            if confirm and confirm.lower() != 'y':
                return

        await __go(
            do_exec, items, None, 'evaluation',
            log_file=args.report_path,
            concurrency_limit=real_max_workers,
        )

    asyncio.run(__really_go())
