#!/usr/bin/env bash
scriptd=$(dirname "$(realpath "$0")")
rootd=$(dirname "$scriptd")

cd "$rootd"

source ".venv/bin/activate"
export PYTHONPATH="$PYTHONPATH:$rootd"

# tests are files named `test_*.py` in the `test` directory
python -m unittest discover test