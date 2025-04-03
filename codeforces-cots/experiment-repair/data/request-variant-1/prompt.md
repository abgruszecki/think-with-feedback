You will be given a competitive programming problem.
Analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits, then explain why your chosen implementation strategy is the most efficient solution. Please reason step by step about your solution approach, then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must read input from standard input (input()), write output to standard output (print()).
Do not include any debug prints or additional output.

Put your final solution within a single code block:
```python
<your code here>
```

# Problem

You are given a positive integer $$$n$$$. You have to find $$$4$$$ positive integers $$$a, b, c, d$$$ such that

- $$$a + b + c + d = n$$$, and
- $$$\gcd(a, b) = \operatorname{lcm}(c, d)$$$.

If there are several possible answers you can output any of them. It is possible to show that the answer always exists.

In this problem $$$\gcd(a, b)$$$ denotes the greatest common divisor of $$$a$$$ and $$$b$$$, and $$$\operatorname{lcm}(c, d)$$$ denotes the least common multiple of $$$c$$$ and $$$d$$$.

## Constraints
Time limit per test: 1.0 seconds
Memory limit per test: 256.0 megabytes

## Input Format
The input consists of multiple test cases. The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases. Description of the test cases follows.

Each test case contains a single line with integer $$$n$$$ ($$$4 \le n \le 10^9$$$) — the sum of $$$a$$$, $$$b$$$, $$$c$$$, and $$$d$$$.

## Output Format
For each test case output $$$4$$$ positive integers $$$a$$$, $$$b$$$, $$$c$$$, $$$d$$$ such that $$$a + b + c + d = n$$$ and $$$\gcd(a, b) = \operatorname{lcm}(c, d)$$$.

## Examples
```input
5
4
7
8
9
10
```
```output
1 1 1 1
2 2 2 1
2 2 2 2
2 4 2 1
3 5 1 1
```

## Note
In the first test case $$$\gcd(1, 1) = \operatorname{lcm}(1, 1) = 1$$$, $$$1 + 1 + 1 + 1 = 4$$$.

In the second test case $$$\gcd(2, 2) = \operatorname{lcm}(2, 1) = 2$$$, $$$2 + 2 + 2 + 1 = 7$$$.

In the third test case $$$\gcd(2, 2) = \operatorname{lcm}(2, 2) = 2$$$, $$$2 + 2 + 2 + 2 = 8$$$.

In the fourth test case $$$\gcd(2, 4) = \operatorname{lcm}(2, 1) = 2$$$, $$$2 + 4 + 2 + 1 = 9$$$.

In the fifth test case $$$\gcd(3, 5) = \operatorname{lcm}(1, 1) = 1$$$, $$$3 + 5 + 1 + 1 = 10$$$.