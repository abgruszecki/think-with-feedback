set venv_dir ".venv"
if test -d $venv_dir
    source "$venv_dir/bin/activate.fish"
else
    echo >&2 "Not activating venv; missing dir: $venv_dir"
    echo >&2 "(Sorry, this script must be sourced from the codeforces-cots directory.)"
    return 1
end

set -gx PYTHONPATH "$PYTHONPATH:$PWD"
