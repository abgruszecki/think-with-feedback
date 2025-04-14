#!/usr/bin/env python3
from pathlib import Path

import pandas as pd
import typer

from loguru import logger

flowd = Path(__file__).parent

app = typer.Typer()


@app.command()
def main(p: Path):
    df = pd.read_json(p, lines=True)
    logger.info('Read: {}', p.absolute().relative_to(flowd))

    start_len = len(df)
    df = df[
        (~df['text'].isna())
        & (df['text'].str.len() > 0)
        & (~df['code'].isna())
        & (df['code'].str.len() > 0)
    ]
    logger.info('Filtered row num: {} ({}%)', start_len - len(df), 100 * (start_len - len(df)) / start_len)

    logger.success('Text len mean: {}', df['text'].str.len().mean())
    logger.success('Text len stddev: {}', df['text'].str.len().std())


if __name__ == '__main__':
    app()
