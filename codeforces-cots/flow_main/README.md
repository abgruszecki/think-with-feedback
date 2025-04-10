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