#!/usr/bin/env python3
from pathlib import Path

import pandas as pd
import typer

from loguru import logger

flowd = Path(__file__).parent

app = typer.Typer()


def analyze_one(d: Path):
    logger.info('Analyzing: {}', d.absolute().relative_to(flowd.absolute()))
    expl_df = pd.read_json(d/'exploded-cases.jsonl', lines=True)
    main_df = pd.read_json(d/'processed-simulation-cases.jsonl', lines=True)

    # expl_df['cases_len'] = expl_df['cases'].apply(len)
    main_df['cases_len'] = main_df['cases'].apply(len)

    def log(description: str, df: pd.DataFrame, sr):
        logger.success('{} cases, ok: {}/{} ({:.2%})',
            description,
            sum(sr),
            len(df),
            sum(sr) / len(df),
        )

    log('Exploded', expl_df, expl_df['is_ok'])
    log('Main', main_df, main_df['cases_ok'] & (main_df['cases_len'] != 0))


@app.command()
def analyze(paths: list[Path]):
    for p in paths:
        analyze_one(p)


def foo(paths: list[Path]):
    def get_ok_row_indices(idx: int, p: Path):
        df = pd.read_json(p/'processed-simulation-cases.jsonl', lines=True)
        df['cases_len'] = df['cases'].apply(len)
        sr =  df['cases_ok'] & (df['cases_len'] != 0)
        df = df[sr][['idx', 'offset']]
        df.set_index(['idx', 'offset'], inplace=True)
        df[f'_{idx}'] = True
        return df

    dframes = [get_ok_row_indices(i, p) for i, p in enumerate(paths)]
    df = dframes[0].join(dframes[1:], how='outer')
    df.fillna(False, inplace=True)
    df['total'] = df.sum(axis=1)
    df.reset_index(inplace=True)
    return df

bar_result = None
@app.command()
def bar(paths: list[Path]):
    global bar_result
    bar_result = foo(paths)
    flowd = Path(__file__).parent
    scratchd = flowd/'out/scratch'
    scratchd.mkdir(parents=True, exist_ok=True)
    bar_result.to_json(scratchd/'scratch.jsonl', orient='records', lines=True)

if __name__ == '__main__':
    app()
