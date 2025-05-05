Basic chain:

1. fetch_checker_classification_py
1. fetch_process_solutions_py.py
1. extract_checkable_responses.py
1. find_sig_points.py && find_interest_items.py && extend_sig_points_with_interests.py
1. extract_simulation_snippets.py
1. extract_simulation_cases.py && postprocess_simulation_cases.py
   - (the first script uses a model)
1. join_trustworthy_cases_with_code.py && verify_simulation_cases.py
   - These are named badly.
   - The former script makes prepares a dataset for the latter to execute.

Generating patched responses:

1. fetch_process_solutions_py.py
1. fetch_extract_checker_type.py
1. find_sig_points.py checkables-stream-full && find_interest_items.py && extend_sig_points_with_interests.py
1. extract_simulation_snippets.py
1. sudo ../scripts/step.sh simulation_replacements.py all
1. patched_responses.py

# "WIP"
Why "WIP"? Because these steps are partially manual and it frustrates me but I need to work on other things.

Steps to extract simulation data from wrong responses to checkable problems.

1. Copy the current `out` since these steps will overwrite it with incompatible data
   - (They should probably be writing to a different output dir instead...)
1. fetch_process_solutions_py.py --link --full
   - (Or copy, the full dataset is ~0.5GB)
1. fetch_exec_checkable_answers.py
1. select_checkable_wrong_responses.py
1. find_sig_points.py checkables-wrong && find_interest_items.py && extend_sig_points_with_interests.py
1. extract_simulation_snippets.py
1. extract_simulation_cases_t_self_assess.py
1. STEP_TAG=self-assess postprocess_simulation_cases.py --only-explode --add-code
   - (adding code really shouldn't be in this script...)
1. verify_simulation_cases_t_self_assess.py $postprocess_simulation_cases_output
1. This:
   ```
   postprocess_verifications_t_self_asses.py \
       --input-data $postprocess_simulation_cases_output \
       --verification-report $docker_exec_report
   ```


# Notes
## 2024.04.24
There's a lot of kludges in these scripts.
They're starting to have variants where they expect different steps to be executed before.
They're also starting to serve in different script chains, and do slightly different things in each of them.

Maybe the most sure sign that something is off is that I'm starting to get lost in what scripts to run.
