You will be given a competitive programming problem.
Analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits, then explain why your chosen implementation strategy is the most efficient solution. Please reason step by step about your solution approach, then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage.

Your solution must read input from standard input (input()), write output to standard output (print()).
Do not include any debug prints or additional output.

Put your final solution within a single code block:
```python
<your code here>
```

# Problem

Vasily the Programmer loves romance, so this year he decided to illuminate his room with candles.

Vasily has a candles.When Vasily lights up a new candle, it first burns for an hour and then it goes out. Vasily is smart, so he can make b went out candles into a new candle. As a result, this new candle can be used like any other new candle.

Now Vasily wonders: for how many hours can his candles light up the room if he acts optimally well? Help him find this number.

## Constraints
Time limit per test: 1.0 seconds
Memory limit per test: 256.0 megabytes

## Input Format
The single line contains two integers, a and b (1 ≤ a ≤ 1000; 2 ≤ b ≤ 1000).

## Output Format
Print a single integer — the number of hours Vasily can light up the room for.

## Examples
```input
4 2
```
```output
7
```
-----
```input
6 3
```
```output
8
```

## Note
Consider the first sample. For the first four hours Vasily lights up new candles, then he uses four burned out candles to make two new ones and lights them up. When these candles go out (stop burning), Vasily can make another candle. Overall, Vasily can light up the room for 7 hours.
