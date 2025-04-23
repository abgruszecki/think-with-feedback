<think>
Okay, so I need to solve this problem where three friends decide to solve a problem only if at least two of them are sure. The input gives me n problems, each with three 0 or 1 values indicating their confidence. For each problem, I have to check if the sum of the three is at least 2. Then, count how many such problems there are.

Let me think about the steps. First, read the input. The first line is n, then n lines each with three integers. For each of those lines, sum the three numbers. If the sum is >=2, increment the count. Then output the count.

Wait, but each of the three can be 0 or 1. So adding them gives how many are sure. So yes, if the sum is 2 or 3, that's when they'll proceed. So the approach is straightforward.

Now, considering the constraints. The maximum n is 1000, which is very small. So even a O(n) solution with a loop is more than sufficient. Time isn't an issue here. So no need for any optimizations beyond the obvious.

The data structures needed: probably just read each line as a list of integers, sum them, check if >=2. Count how many times this happens.

So the plan is:

1. Read n from input.
2. Initialize a counter to 0.
3. For each of the next n lines:
   a. Split the line into three integers.
   b. Sum them.
   c. If sum >=2, increment counter.
4. Print the counter.

In Python, this should be straightforward. But need to handle input correctly.

Wait, how to read each line? For each line after the first, split the input into parts and convert to integers.

But in Python, reading via input() can be done. For each line after the first n lines, we can process them.

Wait, first line is n. Then next n lines are the three numbers each.

So code outline:

n = int(input())
count = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        count +=1
print(count)

Yes, that's the code. Simple and efficient.

Testing with the examples:

First example:

3

1 1 0 --> sum 2 --> count 1

1 1 1 --> sum 3 --> count 2

1 0 0 --> sum 1 --> no. Total 2. Which matches the sample output.

Second example:

2

1 0 0 --> sum 1 --> no

0 1 1 --> sum 2 --> yes. So count is 1. Which matches.

So the code works for the samples.

What about edge cases?

Like n=1. For example, all three 1: sum 3 --> count 1.

Or n=0? But according to the constraints, n is >=1. So no need to handle that.

Another edge case: all three 0. Sum 0: not counted.

So the code should be correct.

This approach is O(n) time and O(1) space, which is optimal for the constraints given. Since n is up to 1000, even in Python with loops, it's fast enough. The code is as efficient as possible, since each problem is processed in O(1) time, and there's no need for any data structures beyond the variables to hold the current line's values.

So I think this is the optimal solution.
</think>

```python
n = int(input())
count = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        count += 1
print(count)
```