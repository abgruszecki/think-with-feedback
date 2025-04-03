You will be given a competitive programming problem.
Analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits, then explain why your chosen implementation strategy is the most efficient solution. Please reason step by step about your solution approach, then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must read input from standard input (input()), write output to standard output (print()).
Do not include any debug prints or additional output.

Put your final solution within a single code block:
```python
<your code here>
```

# Problem

The only difference between problems C1 and C2 is that all values in input of problem C1 are distinct (this condition may be false for problem C2).

You are given a sequence $$$a$$$ consisting of $$$n$$$ integers. All these integers are distinct, each value from $$$1$$$ to $$$n$$$ appears in the sequence exactly once.

You are making a sequence of moves. During each move you must take either the leftmost element of the sequence or the rightmost element of the sequence, write it down and remove it from the sequence. Your task is to write down a strictly increasing sequence, and among all such sequences you should take the longest (the length of the sequence is the number of elements in it).

For example, for the sequence $$$[2, 1, 5, 4, 3]$$$ the answer is $$$4$$$ (you take $$$2$$$ and the sequence becomes $$$[1, 5, 4, 3]$$$, then you take the rightmost element $$$3$$$ and the sequence becomes $$$[1, 5, 4]$$$, then you take $$$4$$$ and the sequence becomes $$$[1, 5]$$$ and then you take $$$5$$$ and the sequence becomes $$$[1]$$$, the obtained increasing sequence is $$$[2, 3, 4, 5]$$$).

## Constraints
Time limit per test: 2.0 seconds
Memory limit per test: 256.0 megabytes

## Input Format
The first line of the input contains one integer $$$n$$$ ($$$1 \le n \le 2 \cdot 10^5$$$) — the number of elements in $$$a$$$.

The second line of the input contains $$$n$$$ integers $$$a_1, a_2, \dots, a_n$$$ ($$$1 \le a_i \le n$$$), where $$$a_i$$$ is the $$$i$$$-th element of $$$a$$$. All these integers are pairwise distinct.

## Output Format
In the first line of the output print $$$k$$$ — the maximum number of elements in a strictly increasing sequence you can obtain.

In the second line print a string $$$s$$$ of length $$$k$$$, where the $$$j$$$-th character of this string $$$s_j$$$ should be 'L' if you take the leftmost element during the $$$j$$$-th move and 'R' otherwise. If there are multiple answers, you can print any.

## Examples
```input
5
2 1 5 4 3
```
```output
4
LRRR
```
-----
```input
7
1 3 5 6 7 4 2
```
```output
7
LRLRLLL
```
-----
```input
3
1 2 3
```
```output
3
LLL
```
-----
```input
4
1 2 4 3
```
```output
4
LLRL
```

## Note
The first example is described in the problem statement.