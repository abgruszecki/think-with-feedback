#!/usr/bin/env python3
from pathlib import Path

import pandas as pd
import typer

from loguru import logger

flowd = Path(__file__).parent

# app = typer.Typer()


old_f = flowd/'archived/out-second/extract_simulation_snippets/result.jsonl'
new_f = flowd/'out/extract_simulation_snippets/result.jsonl'

old_df = pd.read_json(old_f, lines=True)
new_df = pd.read_json(new_f, lines=True)

def step1(df, prefix: str):
    df = df[['idx', 'offset', 'text']].copy()
    df.set_index(['idx', 'offset'], inplace=True)
    df['text_len'] = df['text'].str.len()
    # add prefix to cols
    df.columns = [prefix + '_' + col for col in df.columns]
    return df

old_df = step1(old_df, 'old')
new_df = step1(new_df, 'new')

df = old_df.join(new_df, how='inner')
df['len_diff'] = df['old_text_len'] - df['new_text_len']
df['len_diff_pct'] = df['len_diff'] / df['old_text_len']

len_sr = df.loc[df['len_diff'] > 0, 'len_diff']
pct_sr = df.loc[df['len_diff'] > 0, 'len_diff_pct']
logger.success('% of rows changed: {:.2%}', len(len_sr) / len(df))
logger.success('Len diff description:\n{}', len_sr.describe())
logger.success('Pct diff description:\n{}', pct_sr.describe())

df.reset_index(inplace=True)
df.to_json(flowd/'out/scratch/compare_snippets.jsonl', orient='records', lines=True)