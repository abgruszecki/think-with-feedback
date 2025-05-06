You will be given a competitive programming problem.
Your task is to analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits. Explain why your chosen implementation strategy is the most efficient solution and then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must:
- Read input using input()
- Write output using print()
- Avoid any debug prints or extra output

Wrap your final solution in a single code block using triple backticks, like this:
```python
<your code here>
```

# Anton and Letters (Codeforces Round 253 (Div. 2), 2014)

You will be given a competitive programming problem.
Analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits, then explain why your chosen implementation strategy is the most efficient solution. Please reason step by step about your solution approach, then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must read input from standard input (input()), write output to standard output (print()).
Do not include any debug prints or additional output.

Put your final solution within a single code block:
```python
<your code here>
```

# Problem

Recently, Anton has found a set. The set consists of small English letters. Anton carefully wrote out all the letters from the set in one line, separated by a comma. He also added an opening curved bracket at the beginning of the line and a closing curved bracket at the end of the line.

Unfortunately, from time to time Anton would forget writing some letter and write it again. He asks you to count the total number of distinct letters in his set.

## Constraints
Time limit per test: 2.0 seconds
Memory limit per test: 256.0 megabytes

## Input Format
The first and the single line contains the set of letters. The length of the line doesn't exceed 1000. It is guaranteed that the line starts from an opening curved bracket and ends with a closing curved bracket. Between them, small English letters are listed, separated by a comma. Each comma is followed by a space.

## Output Format
Print a single number — the number of distinct letters in Anton's set.

## Examples
```input
{a, b, c}
```
```output
3
```
-----
```input
{b, a, b, a}
```
```output
2
```
-----
```input
{}
```
```output
0
```

Mutant Code

'''python
def test_program(input_stream, output_stream): # pragma: no mutate
    import builtins # pragma: no mutate
    input = lambda: input_stream.readline()[:-1] # pragma: no mutate
    print = lambda *args, **kwargs: builtins.print(*args, **kwargs, file=output_stream) # pragma: no mutate
    s = input().strip()
    if len(s) == 3:
        print(0)
    else:
        print(len(set(s[1:-1].split(', '))))
'''

Now you must:
1. Identify the bug(s) in the mutant code.
2. Clearly explain your correct algorithmic approach.
3. Write a correct and optimized Python 3 solution, ensuring correctness for all test cases and respecting the constraints.
4. Output only your final code in a valid Python code block, using input() and print() directly.

