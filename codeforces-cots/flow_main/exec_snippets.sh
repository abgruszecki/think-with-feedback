#!/usr/bin/env bash

# This script can be ran with sudo.
flowd=$(dirname "$(realpath "$0")")
rootd=$(dirname "$flowd")

source "$rootd/.venv/bin/activate"
exec env PYTHONPATH="$rootd:$PYTHONPATH" python "$flowd/exec_snippets.py" "$@"