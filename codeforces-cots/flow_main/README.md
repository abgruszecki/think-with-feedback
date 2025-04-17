Remember, this is a "flow" - see [this README](../README.md).

These scripts process and evaluate the `solutions_py` part of the `codeforces-cot` dataset.


Steps:

0. extract_checker_type.py
1. process_solutions_py.py
2. exec_snippets.py
3. exec_snippets_via_workdir.py
4. extract_boths.py
5. simulations.py
6. fetch_checker_classification.py
7. extract_fuzzable_final_answers.py

Steps to extract "fuzzable final answers":

0. Run flow_checker_classification
1. process_solutions_py.py
2. exec_snippets_via_workdir.py
3. fetch_checker_classification.py
4. extract_fuzzable_final_answers.py

# Notes
These steps are partially manual and they should be done in a different way.

Steps to exec checkable answers from the entire dataset:

1. Edit `extract_checker_type.py` to run on the entire dataset,
   copy the output to dir used by`exec_checkable_answers.py`
   (please add a CLI flag the next time this is done...)
   - We're not using our dataset because it actually mostly agrees with open-r1.
2. Run `process_solutions_py.py --only-report --range full`
3. Run `exec_checkable_answers.py`
