This dir has extracts from https://huggingface.co/datasets/open-r1/codeforces-cots , the `codeforces-cots` dataset.

The dataset features various competetive programming problems together with R1 responses to them.
(See the dataset card about `solutions` and `solutions_py` and other parts of the dataset.)

# Turboquick overview

I recommend using `uv`. Create a local venv, install `requirements.txt`.

Run `render+solutions_py.py` to create a dir `out+solutions_py` with dataset items rendered in Markdown.

Run `go+solutions_py.py` to find code blocks and probable "answer candidates" in CoTs from the dataset
and output them to `out/go+solutions_py`.
The stdout will have a CSV file with stats about the processed items.

`experiment-icl` has the ICL experiment.

