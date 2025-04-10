Steps to get mutants from the "fuzzable final answers" dataset (generated in flow_main):

1. run mutate_solutions.py to generate mutants (mutants may pass or fail tests)
   - (note: this step takes a lot of memory)
2. run exec_mutants.py to get a report of which mutants fail tests