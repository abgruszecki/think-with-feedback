This dir has extracts from https://huggingface.co/datasets/open-r1/codeforces-cots , the `codeforces-cots` dataset.

The dataset features various competetive programming problems together with R1 responses to them.
(See the dataset card about `solutions` and `solutions_py` and other parts of the dataset.)

# Setup
I recommend using `uv` and `uv pip`, but `pip` alone also works.

1. Create a local venv in `.venv`
2. Install the dependencies in pyproject.toml (`uv sync` or `pip install -e .`)

# File organization
This directory has a whole bunch of Python scripts and modules. I tried to organize it just enough.

If you need to get things done, don't let the organization stop you.
Just copy things to your directory, make them work,
don't write to other directories (please),
include a README explaining how to work in the dir if you have the time.

There are "flows" and "experiment" dirs (their names start appropriately).

An "experiment" is a standalone thing which does whatever was interesting at the time.

A "flow" is supposed to be like a Jupyter notebook, but with Python scripts and not cells.
The README should explain the order of the scripts (if it's up-to-date).
Each script can be run with `scripts/step.sh`, which lets the script load its dependencies.
Like in a notebook, later steps may expect previous steps to be executed, not the other way around.
Each script should output to a subdir of `$flow/out` (subdir should be named after the script).
One flow may depend on the outputs of another;
I guess in that case it's a good idea to just have a step which copies them over.

Other dirs may contain Python code shared by the scripts.

# Directories
## Flows
- `flow_main` extracts answers (candidates and final) from CoTs and checks their correctness.
- `flow_checker_classification` classifies the problems by what checker they need.
- `flow_sig_points` extracts snippets with simulated executions out of the CoTs.
  - It works by finding "significant points" within the CoTs and chopping the CoTs appropriately.
## Experiments
Sorry, ATTW there's no readme for these, I'd have to read the source again.
- `experiment-icl`
- `experiment-regeneration`
- `experiment-repair`

# Future improvements
## Better dataset keys
I think it's a good idea for all datasets to have a structured "key" column.
That avoids issues with using the wrong key.
It can easily be exploded.
(The names are lost, but maybe that's ok...)
(Maybe put the field names as the first cell elt?)