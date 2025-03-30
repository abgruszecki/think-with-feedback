#!/usr/bin/env python3
from pathlib import Path

import typer

from dockerinator.async_exec import async_exec


app = typer.Typer()


@app.command()
def main(inputs: list[Path]):
    async_exec(
        executor_image_name='python',
        inputs=inputs,
        executor_args=['python', '-']
    )


if __name__ == '__main__':
    app()
