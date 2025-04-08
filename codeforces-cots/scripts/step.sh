#!/usr/bin/env bash
scriptd=$(dirname "$(realpath "$0")")
rootd=$(dirname "$scriptd")

source "$rootd/.venv/bin/activate"

cmd=$1
shift
# Fix paths to local files.
# Local files are preferred over global commands, too bad.
[[ "$cmd" != ./* && "$cmd" != ../* && -f ./"$cmd" ]] && {
    cmd=./"$cmd"
}

exec env PYTHONPATH="$PYTHONPATH:$rootd" "$cmd" "$@"
