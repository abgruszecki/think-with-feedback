You will be given a competitive programming problem.
Analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits, then explain why your chosen implementation strategy is the most efficient solution. Please reason step by step about your solution approach, then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must read input from standard input (input()), write output to standard output (print()).
Do not include any debug prints or additional output.

Put your final solution within a single code block:
```python
<your code here>
```

# Problem

Sorting arrays is traditionally associated with high-level languages. How hard can it be in Befunge? Sort the given array in non-descending order.

## Constraints
Time limit per test: 2.0 seconds
Memory limit per test: 64.0 megabytes

## Input Format
The first line of input contains an integer n (1 ≤ n ≤ 100) — the size of the array. The following n lines contain the elements of the array, one per line. Each element of the array is an integer between 1 and 60, inclusive. The array might contain duplicate elements.

## Output Format
Output space-separated elements of the sorted array.

## Examples
```input
5
7
1
9
7
3
```
```output
1 3 7 7 9
```
-----
```input
10
60
1
60
1
60
1
60
1
60
1
```
```output
1 1 1 1 1 60 60 60 60 60
```


