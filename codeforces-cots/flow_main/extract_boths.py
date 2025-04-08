"""
Extracts responses where both the candidate and the final answer produce wrong outputs on a sample input.
"""
from pathlib import Path

from py_shared import ser


root_outd = Path(__file__).parent/'out'
exec_report_file = root_outd / 'exec-report.jsonl'
outf = root_outd / 'extract-boths.jsonl'

data = ser.jsonl_loadf(exec_report_file)
data_by_problem = {}
failing_test_snippets = []
for r in data:
    data_by_problem[r['problem']] = r
    if 'AssertionError' in r.get('stderr', ''):
        failing_test_snippets.append(r)

fins = []
cans = []
cans_full_ids = {}
fins_full_ids = {}
for r in failing_test_snippets:
    problem_id = r['problem']
    short_id = problem_id.split('/')[0]
    if 'candidate' in problem_id:
        cans.append(short_id)
        cans_full_ids[short_id] = problem_id
    if 'final' in problem_id:
        fins.append(short_id)
        fins_full_ids[short_id] = problem_id

boths_list = list(set(fins).intersection(set(cans)))
boths_list.sort()

def gen_out_rows():
    for line in boths_list:
        can_id=cans_full_ids[line]
        fin_id=fins_full_ids[line]
        # these should never fail
        can_stderr = data_by_problem[can_id]['stderr']
        fin_stderr = data_by_problem[fin_id]['stderr']
        can_err_msg = next(l for l in can_stderr.splitlines() if 'AssertionError' in l)
        fin_err_msg = next(l for l in fin_stderr.splitlines() if 'AssertionError' in l)
        # if can_err_msg.strip() == fin_err_msg.strip():
        #     if '0' not in can_err_msg:
        #         print('Nonzero', file=sys.stderr)
        yield {
            'problem': line,
            'can_err_msg': can_err_msg,
            'fin_err_msg': fin_err_msg,
            'candidate': can_id,
            'final': fin_id,
            'can_stderr': can_stderr,
            'fin_stderr': fin_stderr,
        }
out_rows = list(gen_out_rows())

ser.jsonl_dumpf(out_rows, outf)
