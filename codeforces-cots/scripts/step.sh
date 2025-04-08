#!/usr/bin/env bash
scriptd=$(dirname "$(realpath "$0")")
rootd=$(dirname "$scriptd")

source "$rootd/.venv/bin/activate"
exec env PYTHONPATH="$PYTHONPATH:$PWD" "$@"
