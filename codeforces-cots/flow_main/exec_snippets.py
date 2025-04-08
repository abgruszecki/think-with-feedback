from pathlib import Path

from dockerinator.run_in_containers import run_scripts_in_containers, ExecutionArgs

flowd = Path(__file__).parent
root_outd = flowd/'out'
step_outd = root_outd/'exec_snippets'
step_outd.mkdir(parents=True, exist_ok=True)

run_scripts_in_containers(
    executor_image_name='python',
    # inputs=[Path('flow_main/out/processed-solutions-py/answer-checks/')],
    inputs=[root_outd/'process_solutions_py'/'answer-checks'],
    execution_args=ExecutionArgs(
        executor_args=['python', '-'],
        report_path=step_outd/'exec-report.jsonl',
    ),
)
