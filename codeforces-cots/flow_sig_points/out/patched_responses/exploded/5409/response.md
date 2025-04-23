<think>
Okay, let's tackle this problem. So, the task is to determine for each procedure call how many template procedures are suitable based on the given variables and their types. Hmm, let's break it down.

First, the input has three main parts: the template procedures, the variables, and the procedure calls. For each call, we need to check against all the procedures with the same name and same number of parameters. Then, for each parameter in the template, check if the variable's type matches either the template's type (if it's T) or exactly the same as the template's specified type.

So, the steps I need to follow are:

1. Read all the template procedures and group them by their name. Also, for each procedure, store the list of parameter types (like a list, where each element is either a specific type like 'int', 'string', 'double', or 'T').

2. Read all variables into a dictionary mapping their names to their types.

3. For each procedure call:
   a. Extract the procedure name and the list of variable names used in the call.
   b. Look up all procedures with that name and the same number of parameters.
   c. For each such procedure, check if every parameter in the template matches the variable's type. For 'T' in the template, all variables in that position must have the same type as each other. Wait, no, wait. Wait, no. Wait, the problem says: the variable type matches the parameter if the parameter is T (regardless of the variable's type?), or the parameter's type is the same as the variable's type.

Wait, no. Wait, the problem statement says: the variable type matches the parameter if the parameter is T, or the variable's type equals the parameter's type. But each variable in the call has a fixed type (since variables are defined). So for example, if the template parameter is T, then any variable's type is acceptable for that position. But if the template parameter is, say, 'int', then the variable's type must be 'int'.

Wait, no. Wait, the condition is that the variable's type must match the parameter's type. So for each parameter in the procedure's template:

- If the parameter is T, then the variable's type can be anything (but all T parameters in the template that are part of the same procedure's parameters must correspond to the same actual type. Wait no, no. Wait, the problem statement says: the variable type matches the type of a parameter if the parameter has a generic type T OR the type of the variable and the parameter are the same.

Wait, no. Wait, the variable's type must match the parameter's type. The parameter can be a specific type (like int) or T. For a specific type, the variable must have exactly that type. For a T parameter, the variable can have any type, but for that particular procedure's template, all T parameters in the parameters list can be matched to variables of any type, but each T in the parameters can be different. Wait, no. Wait, the problem says that the variable's type must match the parameter's type. For a parameter that's T, any variable's type is acceptable. So each T in the parameter list is a wildcard that can match any variable type. But multiple Ts in the same procedure's parameters can match variables of different types. For example, a template like (T, T) would require that the variables in those two positions have the same type. Because, for each T in the parameters, the variable's type must match the parameter's type (which is T). Wait, but T is a generic type. So, the variable's type can be any type, but when the parameter is T, it's allowed. Wait, no. Let me recheck the problem statement.

The variable's type matches the parameter's type if the parameter is T OR the variable's type equals the parameter's type. So, for example:

If a template procedure has parameters (T, int), and the variables passed are (string, int), then the first parameter is T, so variable's type (string) matches. The second parameter is int, and the variable is int, so matches. So this procedure would be suitable.

Another example: template is (T, T). The variables passed are (int, string). Then the first T matches int, the second T matches string. But since both are T parameters, the variables can be any types, including different ones. So in this case, the procedure (T, T) would be suitable for a call with variables of (int, string), as each T is considered individually. Wait, but that's not correct. Wait, according to the problem statement, the variable's type must match the parameter's type. So T is a parameter type, so any variable type is allowed for that parameter. So (T, T) as parameters would require that both variables are of any types. For example, in the call f(a, a), where a is int, both Ts would accept. But in a call like f(a, s), where a is int and s is string, each T is matched by their respective variable's type. So the procedure (T, T) is considered suitable for such a call. Because each T is matched independently. So, the parameters (T, T) do not require the variables to have the same type. Each T is a separate check. So the answer in that case would be yes.

Wait, this is a crucial point. Let me recheck the problem statement.

The problem says:

"The variable type matches the type of a parameter if the parameter has a generic type T or the type of the variable and the parameter are the same."

So each parameter is checked against the variable. For T parameters, variable's type is irrelevant (matches any). For non-T parameters, the variable's type must be exactly the parameter's type.

So for a template (T, T), the variables can have any types, but each T is considered individually. So for example, if the call is (int, string), each T in the template parameters would match, so the procedure is considered suitable. So in the first sample input:

The first sample has two f procedures:

void f(int, T) and void f(T, T).

The first call is f(a, a), where a is int.

For the first procedure (int, T):

First parameter is int, which matches a's type (int). Second parameter is T, which matches a's type (int). So this is a match.

For the second procedure (T, T):

First parameter is T (matches any type), second is T (matches any type). So both a's are int, so the procedure is a match. So this call returns 2.

So, the answer is 2 here.

So, the key is that each T parameter in the template is checked against the variable's type in the corresponding position. So each T in the template is a wildcard that allows any variable type for that position, but there's no requirement that different Ts in the same template must correspond to the same type.

Wait, that's the case. So for example, a template (T, T) would match any two variables of any types, possibly different. Because each T is a separate check. So in the first sample input's first call, the variables are (int, int), which would match the second procedure (T, T) because both parameters are T. So yes.

Another example: the first sample's second call is f(s, a), where s is string and a is int.

Looking at the two f procedures.

First procedure: (int, T). The first parameter is int. The first variable is s (string), which does not match int. So this procedure is not suitable.

Second procedure: (T, T). The first parameter is T (matches string), second parameter is T (matches int). Both are T, so this procedure is suitable. So the count is 1. Wait, but according to the first sample's output for the second call, the answer is 1. Let me check the sample input.

Wait, the first sample's second call is f(s, a). s is string, a is int.

So the first procedure requires first parameter to be int. s is string, so no. The second procedure requires any parameters. So this call would match the second procedure. So the answer is 1. Which matches the sample's output. So in this case, the two parameters in the template are T and T, but the variables are string and int. So each T is considered independently, so the procedure is suitable.

Therefore, the conclusion is that for each parameter in the template, if it is T, the variable's type can be any. If it is a specific type, then the variable's type must match exactly. So, when checking a procedure against a call, each parameter is checked individually. There is no relation between Ts in the same procedure's parameters.

So, the plan is:

For each procedure call:

1. Get the procedure name and the list of variables (their names).

2. For each variable in the call, look up its type in the variables dictionary.

3. For each template procedure with the same name and parameter count:

   a. For each position i in the parameters:

      i. Check if the template's parameter type is T, in which case it's a match.

      ii. Else, check if the variable's type is equal to the template's parameter type.

   b. If all parameters match, count this procedure.

So, the steps are straightforward. Now, the challenge is to model the data structures efficiently.

Now, considering the constraints:

n, m, k can be up to 1000 each. So for each procedure call (k=1000), we have to check up to n procedures (n=1000) with up to 5 parameters each (5 steps per procedure). So total steps are 1000 * 1000 *5 = 5,000,000, which is acceptable for Python within 2 seconds.

So the solution is feasible.

Now, the data structures:

- Procedures: group them by name. So a dictionary where the key is the procedure name, and the value is a list of parameter lists. For example, for the first sample input, the 'f' key would have two entries: ['int', 'T'] and ['T', 'T'].

- Variables: a dictionary mapping variable names to their types (like 'a' → 'int', 's' → 'string', etc.)

For each call:

- Extract the procedure name and the list of variable names. Then, for each variable name in the list, get their type from the variables dict.

- Then, look up all procedures with that name and same parameter count. For each such procedure, check each parameter against the variable's type.

So, the steps are:

Read n procedures:

Each line is something like "void f(int,T)", but with possible spaces. Need to parse each line into the procedure name and the list of parameter types.

Parsing the procedure lines:

Split the line into parts. The line starts with 'void', then the procedure name, then parameters in parentheses. The parameters are separated by commas, with possible spaces.

For example, "void  f   (  T, double  )" → procedure name is 'f', parameters are ['T', 'double'].

Parsing steps for a procedure line:

- Split the line into tokens, ignoring whitespace. But perhaps using string manipulation to extract the parts.

Alternatively, split the line into parts by splitting on parentheses and commas.

For example:

Line: "void foo123   ( int,  double,  string,string  )"

We can split on the opening '(', then split the parameters part (before the closing ')') into individual types, stripping whitespace.

So, the steps for parsing a procedure line:

1. Strip leading and trailing whitespace.

2. Split the line into parts. The 'void' keyword is first. Then the procedure name, then the parameters in parentheses.

3. Split the line into parts after 'void' and before the '('.

For example:

line = 'void f(T, double)'

After stripping, split into 'void', 'f(T, double)'?

Wait, maybe the correct approach is to split on the first occurrence of '('.

Wait, perhaps split the line as:

parts = line.strip().split('(')

So the first part is 'void procedureName ', then the parameters are in the second part (excluding the closing ')'). For example, 'void f ( int, T )' → split into ['void f ', ' int, T )'], then take the parameters part as the part after '(', before ')'.

So:

param_part = parts[1].split(')')[0].strip()

Then split param_part into individual types, splitting on commas, stripping each part.

So for the example, 'int, T' → split into ['int', 'T'].

So, in code:

def parse_procedure(line):
    line = line.strip()
    # Split into parts before and after '('
    name_part, param_part = line.split('(')
    # The name part is after 'void', e.g., 'void f ' → 'f'
    name_part = name_part.strip()
    # Split name_part into parts, first is 'void', rest is the procedure name
    _, proc_name = name_part.split(maxsplit=1)
    # Now, process the parameters
    param_part = param_part.split(')')[0].strip()
    if not param_part:  # no parameters?
        params = []
    else:
        params = [p.strip() for p in param_part.split(',')]
    return proc_name, params

But wait, the line may not have any parameters? The constraints say that the number of parameters t is between 1 and 5. So, no, each procedure has at least one parameter.

But in code, perhaps better to handle cases where param_part is empty (though according to problem statement, t >=1).

So, after parsing the procedure name and parameters, we can store them in a dictionary grouped by name. For example, procedures = defaultdict(list), where each key is the procedure name, and the value is a list of parameter lists.

Variables are parsed as:

Each line is like 'type variableName'. We split into type and name, stripping whitespace. Then, store in a dict, variables[variableName] = type.

Procedure calls are parsed as:

Each line is like 'procedureName (var_1, var_2, ..., var_t)'. Need to extract the procedure name and the list of variables.

Parsing steps:

line.strip().split('(') → first part is the procedure name (with possible leading/trailing spaces), then the variables part (before ')').

For example, 'f  (  s  ,x123 )' → split into ['f  ', '  s  ,x123 )']. Then, the variables part is 's  ,x123', which is split by commas, stripped.

So:

def parse_call(line):
    line = line.strip()
    name_part, vars_part = line.split('(')
    proc_name = name_part.strip()
    vars_part = vars_part.split(')')[0].strip()
    if not vars_part:
        variables = []
    else:
        variables = [v.strip() for v in vars_part.split(',')]
    return proc_name, variables

So, variables is a list of variable names in the call.

Once we have the variables' names, we can look up their types in the variables dict.

Putting it all together:

Read n procedures, group them by name. For each, store the list of parameters.

Read m variables into a dict.

Read k calls. For each call:

- Get proc name and variables.

- Get the list of variables' types.

- For each procedure in the procedures dict under that name, with same parameter count:

   Check each parameter in the procedure against the variable's type. For each position i:

      if proc_param[i] is 'T' → ok.

      else: check if variable_type[i] == proc_param[i].

   If all parameters match, count +=1.

So, for the code:

procedures = defaultdict(list)

for _ in range(n):
    line = input().strip()
    proc_name, params = parse_procedure(line)
    procedures[proc_name].append(params)

variables = {}

for _ in range(m):
    line = input().strip()
    type_, name = line.split(maxsplit=1)
    variables[name.strip()] = type_.strip()

for _ in range(k):
    line = input().strip()
    proc_name, var_names = parse_call(line)
    # Get variable types
    var_types = []
    for var in var_names:
        var_type = variables[var.strip()]
        var_types.append(var_type)
    # Check procedures with same name and parameter count
    count = 0
    if proc_name not in procedures:
        print(0)
        continue
    for param_list in procedures[proc_name]:
        if len(param_list) != len(var_types):
            continue
        # Check each parameter
        valid = True
        for p, vt in zip(param_list, var_types):
            if p == 'T':
                continue
            if p != vt:
                valid = False
                break
        if valid:
            count +=1
    print(count)

Wait, that seems correct.

But let's test with the first sample input.

Sample input 1:

4
void f(int,T)
void  f(T, T)
void foo123   ( int,  double,  string,string  )
void  p(T,double)
3
int a
string    s
double x123
5
f(a,  a)
f(s,a   )
foo   (a,s,s)
f  (  s  ,x123)
proc(a)

Procedures:

For 'f' → two entries:

['int', 'T'] and ['T', 'T']

For the first call f(a,a):

variables a is int, a is int.

var_types = ['int', 'int']

Check each procedure:

For ['int', 'T'] → first parameter is 'int' → matches, second is T → matches. So valid.

For ['T', 'T'] → both parameters are T → valid. So count is 2. Correct.

Second call f(s,a):

var_types: s is 'string', a is 'int'.

Check 'int', 'T' → first parameter is int, but s is string → invalid. So not counted.

Check 'T', 'T' → both parameters are T → valid. So count 1.

Third call: foo(a, s, s) → parameters are 3? But the foo123 procedure has 4 parameters. So the procedure 'foo123' expects 4 parameters. The call has 3. So no match. Count is 0.

Fourth call: f(s, x123). Variables: s is string, x123 is double.

Check for 'int', 'T' → first is 'int' (s is string → invalid). So not counted.

Check 'T', 'T' → both parameters are T → valid. So count 1.

Fifth call: proc(a) → no procedures named 'proc' → count 0.

So the outputs are as in the sample.

Sample 2:

6 procedures, 4 variables, 5 calls.

But the code should handle it.

So, the code seems correct.

Now, need to implement the parsing correctly.

But in the code above, for parsing procedures, the code splits the line into name_part and param_part via split('('), which may not be correct if the line contains other parentheses. But according to the problem statement, the input lines are properly formatted. So the code should handle it.

But perhaps the split on '(' could split into multiple parts. For example, if the procedure name has a '(' in it. But the problem states that the procedure names are non-empty strings of lowercase letters and numbers, no other characters. So the split on '(' is safe.

Similarly, the variable names and procedure names are valid.

So the code should handle the parsing correctly.

Now, code optimization:

In Python, for speed, using dictionaries and pre-processing procedures by name and parameter count.

But in the code, for each procedure call, we check all procedures with the same name and same parameter count. So during preprocessing, perhaps group the procedures by name and parameter count. For example, a nested dictionary:

procedures = defaultdict(lambda: defaultdict(list))

So, procedures[proc_name][param_count] = list of param_lists.

But in the current code, for each call, after getting the proc name and the variable list's length, you can directly access the procedures for that name and length.

This can save some time, but in practice, the current code already skips procedures with different parameter counts. So grouping by parameter count might save some loops.

But with n up to 1000 and k up to 1000, even if each call checks all procedures of the same name, and for each, check the length, it's acceptable.

But for code efficiency, perhaps pre-grouping by name and parameter count.

So:

from collections import defaultdict

procedures = defaultdict(lambda: defaultdict(list))

for _ in range(n):
    # parse line
    # then:
    procedures[proc_name][len(params)].append(params)

Then, for a call with parameters of length t, look up procedures[proc_name][t], and check each param_list in that list.

This would reduce the number of checks, as it directly accesses the list of procedures with the required parameter count.

In the code as written, for each procedure in procedures[proc_name], we check len(param_list) == len(var_types). But if we pre-group by parameter count, we can directly iterate over the list of procedures with the correct parameter count.

So this optimization can save some steps. For example, if a procedure has 1000 procedures named 'f', but only 10 have the correct parameter count for a particular call, then the code would check 10 instead of 1000.

But given that the maximum parameter count is 5, and n is 1000, the impact may be minimal. But it's better to pre-group.

So modifying the code accordingly.

In code:

procedures = defaultdict(lambda: defaultdict(list))

for each procedure:

    proc_name, params = parse_procedure(line)
    param_len = len(params)
    procedures[proc_name][param_len].append(params)

Then, for a call:

proc_name = ...
var_count = len(var_types)

if proc_name not in procedures or var_count not in procedures[proc_name]:
    print(0)
else:
    for param_list in procedures[proc_name][var_count]:
        check each parameter.

This way, we only check the procedures with the correct parameter count.

This is a small optimization but can help in worst-case scenarios.

Thus, the code becomes more efficient.

So, the code steps are:

Read n procedures:

Grouped by name and parameter count.

Read m variables.

Read k calls:

For each call:

   get proc name and variables, then their types.

   get the param count (len(var_types)).

   check in the procedures dict if there are any procedures with that name and param count.

   for each such procedure's param list:

      check each param against the variable's type.

Thus, the code's time complexity is O(k * avg_procedures_per_call * param_count), which is acceptable.

So, the code should work.

Now, coding this in Python.

Handling all the parsing correctly is crucial.

Implementing the parse_procedure and parse_call functions.

Wait, but in code, for parsing the procedure line:

The code can be written as follows.

For example:

def parse_procedure(line):

    line = line.strip()
    # Remove 'void' part.
    parts = line.split(maxsplit=2)  # split into 'void', proc_name_part, rest (parameters)
    # After 'void', the rest is the procedure name and parameters.

    # Split the remaining into proc name and parameters part.
    # For example, parts[2] would be 'procedureName ( ... )'
    # So, split on '(' to separate name and parameters.

    name_part, param_part = parts[2].split('(', 1)
    proc_name = name_part.strip()

    param_part = param_part.rsplit(')', 1)[0].strip()
    params = [p.strip() for p in param_part.split(',')] if param_part else []

    return proc_name, params

Wait, perhaps this is a better way.

But the initial code may have issues with lines where the procedure name has spaces. But according to the problem statement, the procedure names are non-empty strings of lowercase letters and numbers, so they cannot contain spaces. So the code can safely split the line after 'void' into the procedure name and parameters.

But the line may have multiple spaces between 'void' and the procedure name.

Alternative approach:

Split the line into parts after 'void' and before the '('.

For example, line is 'void   f   (T, int)'.

We can split into parts after 'void' → 'f   (T, int)'.

Then split that into the procedure name part and parameters part.

So:

After stripping 'void', split the rest into the procedure name and parameters.

So:

proc_part = line[len('void'):].lstrip()

Now, split proc_part into name and parameters.

Split on the first occurrence of '('.

So:

name_part, param_part = proc_part.split('(', 1)

proc_name = name_part.strip()

param_part = param_part.rsplit(')', 1)[0].strip()

params = [p.strip() for p in param_part.split(',')] if param_part else []

Thus, this approach handles all possible spaces.

So code for parse_procedure:

def parse_procedure(line):

    line = line.strip()

    # Check that line starts with 'void'

    if not line.startswith('void'):
        # but according to problem statement, the input is correct.
        # so we can proceed.

    # remove 'void' and any whitespace after it
    content = line[len('void'):].lstrip()

    # split into procedure name and parameters
    name_part, param_part = content.split('(', 1)

    proc_name = name_part.strip()

    param_part = param_part.rsplit(')', 1)[0].strip()

    if param_part:
        params = [p.strip() for p in param_part.split(',')]
    else:
        params = []

    return proc_name, params

This code should handle cases where the procedure line has any amount of whitespace.

Testing this with the first sample input's first procedure line:

"void f(int,T)" → after stripping, line is 'void f(int,T)'

content is 'f(int,T)'.

split into name_part 'f' and param_part 'int,T)'.

Then, split param_part into part before ')', which is 'int,T'.

split into ['int', 'T'].

Yes.

Another example:

"void  f(T, T)" → content after 'void' is 'f(T, T)'

split into name_part 'f' and param_part 'T, T)'.

split param_part into 'T, T'.

split into ['T', 'T'].

Another example: "void foo123   ( int,  double,  string,string  )" → content after 'void' is 'foo123   ( int,  double,  string,string  )'

split into name_part 'foo123' and param_part ' int,  double,  string,string  )'.

split param_part into 'int,  double,  string,string  ' → split by commas → ['int', 'double', 'string', 'string'].

Yes.

Thus, the parsing is correct.

Similarly, for parsing the procedure calls.

parse_call function:

def parse_call(line):

    line = line.strip()

    # split into procedure name and variables part
    name_part, param_part = line.split('(', 1)

    proc_name = name_part.strip()

    param_part = param_part.rsplit(')', 1)[0].strip()

    if param_part:
        var_names = [v.strip() for v in param_part.split(',')]
    else:
        var_names = []

    return proc_name, var_names

Test with line 'f  (  s  ,x123 )' → splits into name_part 'f', param_part 's  ,x123 ' → split into ['s', 'x123'].

Yes.

Thus, the parsing code should work.

Putting it all together:

Now, the code:

Read n procedures, group by name and parameter count.

Read m variables.

Read k calls.

For each call:

   parse into proc name and variables.

   get variable types.

   get the list of procedures with the same name and parameter count.

   for each such procedure's parameters, check if each param matches.

   count the valid ones.

Now, code:

Testing against sample input 1.

```python
import sys
from collections import defaultdict


def main(input_stream, output_stream):
    n = int(input_stream.readline())
    procedures = defaultdict(lambda: defaultdict(list))  # name: {param_count: [param_list]}
    for _ in range(n):
        line = input_stream.readline().strip()
        # Parse procedure
        if not line.startswith('void'):
            # According to problem statement, input is correct
            pass
        content = line[len('void'):].lstrip()
        name_part, param_part = content.split('(', 1)
        proc_name = name_part.strip()
        param_part = param_part.rsplit(')', 1)[0].strip()
        if param_part:
            params = [p.strip() for p in param_part.split(',')]
        else:
            params = []
        param_count = len(params)
        procedures[proc_name][param_count].append(params)
    
    m = int(input_stream.readline())
    variables = {}
    for _ in range(m):
        line = input_stream.readline().strip()
        type_name, var_name = line.split(maxsplit=1)
        variables[var_name.strip()] = type_name.strip()
    
    k = int(input_stream.readline())
    for _ in range(k):
        line = input_stream.readline().strip()
        # Parse call
        name_part, param_part = line.split('(', 1)
        proc_name = name_part.strip()
        param_part = param_part.rsplit(')', 1)[0].strip()
        var_names = [v.strip() for v in param_part.split(',')] if param_part else []
        # Get variable types
        var_types = []
        for var in var_names:
            var_types.append(variables[var])
        param_count = len(var_types)
        # Check procedures
        count = 0
        # Check if there are any procedures with this name and param count
        if proc_name in procedures and param_count in procedures[proc_name]:
            for param_list in procedures[proc_name][param_count]:
                valid = True
                for p, vt in zip(param_list, var_types):
                    if p != 'T' and p != vt:
                        valid = False
                        break
                if valid:
                    count += 1
        print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
void f(string,double,int)
void f(int)
void f  ( T  )
void procedure(int,double)
void f  (T, double,int)
void f(string, T,T)
4
int a
int x
string  t
double  val
5
f(t, a, a)
f(t,val,a)
f(val,a, val)
solve300(val, val)
f  (x)
""",
            "output": \
"""\
1
3
0
0
2
""",
        }, 
    ]

    for i, test_case in enumerate(TEST_CASES):
        in_stream = io.StringIO(test_case["input"])
        expected_output = test_case["output"].rstrip()

        out_stream = io.StringIO()
        main(in_stream, out_stream)
        real_output = out_stream.getvalue().rstrip()

        assert real_output == expected_output, \
            f'Test case {i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}'

    print('Tests passed 😎')


if __name__ == '__main__':
    test()


```

<RUN_SNIPPET>
```output
Tests passed 😎

```

Sample 2:

The code should handle it similarly.

Thus, the code should be correct.
</think>

```python
import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline())
    procedures = defaultdict(lambda: defaultdict(list))
    for _ in range(n):
        line = sys.stdin.readline().strip()
        content = line[len('void'):].lstrip()
        name_part, param_part = content.split('(', 1)
        proc_name = name_part.strip()
        param_part = param_part.rsplit(')', 1)[0].strip()
        params = [p.strip() for p in param_part.split(',')] if param_part else []
        param_count = len(params)
        procedures[proc_name][param_count].append(params)
    
    m = int(sys.stdin.readline())
    variables = {}
    for _ in range(m):
        line = sys.stdin.readline().strip()
        type_name, var_name = line.split(maxsplit=1)
        variables[var_name.strip()] = type_name.strip()
    
    k = int(sys.stdin.readline())
    for _ in range(k):
        line = sys.stdin.readline().strip()
        name_part, param_part = line.split('(', 1)
        proc_name = name_part.strip()
        param_part = param_part.rsplit(')', 1)[0].strip()
        var_names = [v.strip() for v in param_part.split(',')] if param_part else []
        var_types = [variables[var] for var in var_names]
        param_count = len(var_types)
        count = 0
        if proc_name in procedures and param_count in procedures[proc_name]:
            for param_list in procedures[proc_name][param_count]:
                valid = True
                for p, vt in zip(param_list, var_types):
                    if p != 'T' and p != vt:
                        valid = False
                        break
                if valid:
                    count += 1
        print(count)

if __name__ == "__main__":
    main()
```
