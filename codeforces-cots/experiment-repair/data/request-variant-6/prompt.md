You will be given a competitive programming problem.
Analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits, then explain why your chosen implementation strategy is the most efficient solution. Please reason step by step about your solution approach, then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must read input from standard input (input()), write output to standard output (print()).
Do not include any debug prints or additional output.

Put your final solution within a single code block:
```python
<your code here>
```

# Problem

You are given an integer array $$$a_0, a_1, \dots, a_{n - 1}$$$, and an integer $$$k$$$. You perform the following code with it:

Your task is to calculate the expected value of the variable ans after performing this code.

Note that the input is generated according to special rules (see the input format section).

## Constraints
Time limit per test: 3.0 seconds
Memory limit per test: 512.0 megabytes

## Input Format
The only line contains six integers $$$n$$$, $$$a_0$$$, $$$x$$$, $$$y$$$, $$$k$$$ and $$$M$$$ ($$$1 \le n \le 10^7$$$; $$$1 \le a_0, x, y < M \le 998244353$$$; $$$1 \le k \le 17$$$).

The array $$$a$$$ in the input is constructed as follows:

- $$$a_0$$$ is given in the input;
- for every $$$i$$$ from $$$1$$$ to $$$n - 1$$$, the value of $$$a_i$$$ can be calculated as $$$a_i = (a_{i - 1} \cdot x + y) \bmod M$$$.

## Output Format
Let the expected value of the variable ans after performing the code be $$$E$$$. It can be shown that $$$E \cdot n^k$$$ is an integer. You have to output this integer modulo $$$998244353$$$.

## Examples
```input
3 10 3 5 13 88
```
```output
382842030
```
-----
```input
2 15363 270880 34698 17 2357023
```
```output
319392398
```

## Note
The array in the first example test is $$$[10, 35, 22]$$$. In the second example, it is $$$[15363, 1418543]$$$.