You will be given a competitive programming problem.
Analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits, then explain why your chosen implementation strategy is the most efficient solution. Please reason step by step about your solution approach, then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must read input from standard input (input()), write output to standard output (print()).
Do not include any debug prints or additional output.

Put your final solution within a single code block:
```python
<your code here>
```

# Problem

Chaneka, Pak Chanek's child, is an ambitious kid, so Pak Chanek gives her the following problem to test her ambition.

Given an array of integers $$$[A_1, A_2, A_3, \ldots, A_N]$$$. In one operation, Chaneka can choose one element, then increase or decrease the element's value by $$$1$$$. Chaneka can do that operation multiple times, even for different elements.

What is the minimum number of operations that must be done to make it such that $$$A_1 \times A_2 \times A_3 \times \ldots \times A_N = 0$$$?

## Constraints
Time limit per test: 1.0 seconds
Memory limit per test: 256.0 megabytes

## Input Format
The first line contains a single integer $$$N$$$ ($$$1 \leq N \leq 10^5$$$).

The second line contains $$$N$$$ integers $$$A_1, A_2, A_3, \ldots, A_N$$$ ($$$-10^5 \leq A_i \leq 10^5$$$).

## Output Format
An integer representing the minimum number of operations that must be done to make it such that $$$A_1 \times A_2 \times A_3 \times \ldots \times A_N = 0$$$.

## Examples
```input
3
2 -6 5
```
```output
2
```
-----
```input
1
-3
```
```output
3
```
-----
```input
5
0 -1 0 1 0
```
```output
0
```

## Note
In the first example, initially, $$$A_1\times A_2\times A_3=2\times(-6)\times5=-60$$$. Chaneka can do the following sequence of operations:

1. Decrease the value of $$$A_1$$$ by $$$1$$$. Then, $$$A_1\times A_2\times A_3=1\times(-6)\times5=-30$$$
2. Decrease the value of $$$A_1$$$ by $$$1$$$. Then, $$$A_1\times A_2\times A_3=0\times(-6)\times5=0$$$

In the third example, Chaneka does not have to do any operations, because from the start, it already holds that $$$A_1\times A_2\times A_3\times A_4\times A_5=0\times(-1)\times0\times1\times0=0$$$

