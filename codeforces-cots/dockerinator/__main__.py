#!/usr/bin/env python3
from pathlib import Path

import typer

from dockerinator.run_in_containers import run_scripts_in_containers, ExecutionArgs


app = typer.Typer()


@app.command()
def main(inputs: list[Path], max_workers: int | None = None):
    """
    Executes given Python files in a Docker container.
    """
    run_scripts_in_containers(
        executor_image_name='python',
        inputs=inputs,
        execution_args=ExecutionArgs(
            executor_args=['python', '-'],
            max_workers=max_workers,
        ),
    )


if __name__ == '__main__':
    app()
