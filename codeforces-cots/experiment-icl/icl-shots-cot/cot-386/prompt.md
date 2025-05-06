# Strange Table (Codeforces Round 710 (Div. 3), 2021)

You will be given a competitive programming problem.
Analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits, then explain why your chosen implementation strategy is the most efficient solution. Please reason step by step about your solution approach, then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must read input from standard input (input()), write output to standard output (print()).
Do not include any debug prints or additional output.

Put your final solution within a single code block:
```python
<your code here>
```

# Problem

Polycarp found a rectangular table consisting of $$$n$$$ rows and $$$m$$$ columns. He noticed that each cell of the table has its number, obtained by the following algorithm "by columns":

- cells are numbered starting from one;
- cells are numbered from left to right by columns, and inside each column from top to bottom;
- number of each cell is an integer one greater than in the previous cell.

For example, if $$$n = 3$$$ and $$$m = 5$$$, the table will be numbered as follows:

$$$$$$ \begin{matrix} 1 & 4 & 7 & 10 & 13 \\ 2 & 5 & 8 & 11 & 14 \\ 3 & 6 & 9 & 12 & 15 \\ \end{matrix} $$$$$$

However, Polycarp considers such numbering inconvenient. He likes the numbering "by rows":

- cells are numbered starting from one;
- cells are numbered from top to bottom by rows, and inside each row from left to right;
- number of each cell is an integer one greater than the number of the previous cell.

For example, if $$$n = 3$$$ and $$$m = 5$$$, then Polycarp likes the following table numbering: $$$$$$ \begin{matrix} 1 & 2 & 3 & 4 & 5 \\ 6 & 7 & 8 & 9 & 10 \\ 11 & 12 & 13 & 14 & 15 \\ \end{matrix} $$$$$$

Polycarp doesn't have much time, so he asks you to find out what would be the cell number in the numbering "by rows", if in the numbering "by columns" the cell has the number $$$x$$$?

## Constraints
Time limit per test: 2.0 seconds
Memory limit per test: 256.0 megabytes

## Input Format
The first line contains a single integer $$$t$$$ ($$$1 \le t \le 10^4$$$). Then $$$t$$$ test cases follow.

Each test case consists of a single line containing three integers $$$n$$$, $$$m$$$, $$$x$$$ ($$$1 \le n, m \le 10^6$$$, $$$1 \le x \le n \cdot m$$$), where $$$n$$$ and $$$m$$$ are the number of rows and columns in the table, and $$$x$$$ is the cell number.

Note that the numbers in some test cases do not fit into the $$$32$$$-bit integer type, so you must use at least the $$$64$$$-bit integer type of your programming language.

## Output Format
For each test case, output the cell number in the numbering "by rows".

## Examples
```input
5
1 1 1
2 2 3
3 5 11
100 100 7312
1000000 1000000 1000000000000
```
```output
1
2
9
1174
1000000000000
```
