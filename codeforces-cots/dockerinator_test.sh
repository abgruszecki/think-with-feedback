#!/usr/bin/env bash
rootd=$(dirname "$(realpath "$0")")

source "$rootd/.venv/bin/activate"
"$rootd/dockerinator_test.py" "$@"
