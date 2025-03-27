You will be given a competitive programming problem.
Analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits, then explain why your chosen implementation strategy is the most efficient solution. Please reason step by step about your solution approach, then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must read input from standard input (input()), write output to standard output (print()).
Do not include any debug prints or additional output.

Put your final solution within a single code block:
```python
<your code here>
```

# Problem

Polycarp has $$$n$$$ coins, the value of the $$$i$$$-th coin is $$$a_i$$$. Polycarp wants to distribute all the coins between his pockets, but he cannot put two coins with the same value into the same pocket.

For example, if Polycarp has got six coins represented as an array $$$a = [1, 2, 4, 3, 3, 2]$$$, he can distribute the coins into two pockets as follows: $$$[1, 2, 3], [2, 3, 4]$$$.

Polycarp wants to distribute all the coins with the minimum number of used pockets. Help him to do that.

## Constraints
Time limit per test: 1.0 seconds
Memory limit per test: 256.0 megabytes

## Input Format
The first line of the input contains one integer $$$n$$$ ($$$1 \le n \le 100$$$) — the number of coins.

The second line of the input contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le 100$$$) — values of coins.

## Output Format
Print only one integer — the minimum number of pockets Polycarp needs to distribute all the coins so no two coins with the same value are put into the same pocket.

## Examples
```input
6
1 2 4 3 3 2
```
```output
2
```
-----
```input
1
100
```
```output
1
```
