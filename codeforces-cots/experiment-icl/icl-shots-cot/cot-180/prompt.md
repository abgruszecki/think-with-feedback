# Turtle Puzzle: Rearrange and Negate (Codeforces Round 929 (Div. 3), 2024)

You will be given a competitive programming problem.
Analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits, then explain why your chosen implementation strategy is the most efficient solution. Please reason step by step about your solution approach, then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must read input from standard input (input()), write output to standard output (print()).
Do not include any debug prints or additional output.

Put your final solution within a single code block:
```python
<your code here>
```

# Problem

You are given an array $$$a$$$ of $$$n$$$ integers. You must perform the following two operations on the array (the first, then the second):

1. Arbitrarily rearrange the elements of the array or leave the order of its elements unchanged.
2. Choose at most one contiguous segment of elements and replace the signs of all elements in this segment with their opposites. Formally, you can choose a pair of indices $$$l, r$$$ such that $$$1 \le l \le r \le n$$$ and assign $$$a_i = -a_i$$$ for all $$$l \le i \le r$$$ (negate elements). Note that you may choose not to select a pair of indices and leave all the signs of the elements unchanged.

What is the maximum sum of the array elements after performing these two operations (the first, then the second)?

## Constraints
Time limit per test: 2.0 seconds
Memory limit per test: 256.0 megabytes

## Input Format
The first line of the input contains a single integer $$$t$$$ ($$$1 \le t \le 1000$$$) — the number of test cases. The descriptions of the test cases follow.

The first line of each test case contains a single integer $$$n$$$ ($$$1 \le n \le 50$$$) — the number of elements in array $$$a$$$.

The second line of each test case contains $$$n$$$ integers $$$a_1, a_2, \ldots, a_n$$$ ($$$-100 \le a_i \le 100$$$) — elements of the array.

## Output Format
For each test case, output the maximum sum of the array elements after sequentially performing the two given operations.

## Examples
```input
8
3
-2 3 -3
1
0
2
0 1
1
-99
4
10 -2 -3 7
5
-1 -2 -3 -4 -5
6
-41 22 -69 73 -15 -50
12
1 2 3 4 5 6 7 8 9 10 11 12
```
```output
8
0
1
99
22
15
270
78
```

## Note
In the first test case, you can first rearrange the array to get $$$[3,-2,-3]$$$ (operation 1), then choose $$$l = 2, r = 3$$$ and get the sum $$$3 + -((-2) + (-3)) = 8$$$ (operation 2).

In the second test case, you can do nothing in both operations and get the sum $$$0$$$.

In the third test case, you can do nothing in both operations and get the sum $$$0 + 1 = 1$$$.

In the fourth test case, you can first leave the order unchanged (operation 1), then choose $$$l = 1, r = 1$$$ and get the sum $$$-(-99) = 99$$$ (operation 2).

In the fifth test case, you can first leave the order unchanged (operation 1), then choose $$$l = 2, r = 3$$$ and get the sum $$$10 + -((-2) + (-3)) + 7 = 22$$$ (operation 2).

In the sixth test case, you can first leave the order unchanged (operation 1), then choose $$$l = 1, r = 5$$$ and get the sum $$$-((-1)+(-2)+(-3)+(-4)+(-5))=15$$$ (operation 2).
