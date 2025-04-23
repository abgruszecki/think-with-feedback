<think>
Okay, I need to solve this problem where Emma picks a street and Jack picks an avenue, but their choices are based on maximizing and minimizing the cost, respectively. Let's think through the problem step by step.

So the problem says: Emma chooses a street first. For each street, she knows that Jack will pick the avenue that gives the minimum cost in that street's row. So Emma's strategy is to pick the street where the minimum of that row is as large as possible. Because she wants to maximize the cost, but Jack will pick the smallest in her chosen row. So Emma will look for the row with the maximum possible minimum value.

Wait right. So for each row (street), we find the minimum value in that row. Then, among all those minima, Emma will choose the maximum one. Because she wants the highest possible minimum, knowing that Jack will choose the min in her selected row.

So the solution is to compute, for each street, the minimum cost in that street's row. Then the answer is the maximum of those minima.

Let me check the examples.

First example:

3 4
4 1 3 5 → min is 1
2 2 2 2 → min is 2
5 4 5 1 → min is 1
The maxima of these minima is max(1,2,1) = 2 → which matches the output.

Second example:

3 3
1 2 3 → min is 1
2 3 1 → min is 1
3 1 2 → min is 1
Max of minima is 1. Correct.

So the approach is clear. For each row, compute the minimum, then take the maximum of these minima.

Now, the constraints are n and m up to 100 each. So even the brute force approach is acceptable, but since it's allowed, there's no problem here.

The steps to implement:

1. Read n and m.
2. Read n rows, each with m integers.
3. For each row, find the minimum in that row.
4. Find the maximum among all these minima.
5. Output that maximum.

So coding this in Python should be straightforward.

Now, considering the input size, even with n=100, each row has up to 100 elements. Finding the min for each row is O(m) per row, so O(nm) total time which is 100*100 = 10^4 operations. Very manageable.

So the code structure would be:

Read n, m.

Then read n lines, each line split into integers. For each line, compute the min and collect all the minima. Then take the max of that list.

Yes.

Let me test the first example:

Sample Input 1:

3 4
4 1 3 5
2 2 2 2
5 4 5 1

The minima per row are 1, 2, 1. Max is 2.

Sample Input 2:

3 3
1 2 3 → min 1
2 3 1 → min 1
3 1 2 → min 1
Max is 1.

Another test case could be when all rows have their minima in varying positions.

Edge cases:

n=1 and m=1: then the min is the only element. So output is that element.

n=1, m=2: the row has two elements, min is the smaller. Emma has no choice but to choose that row, and Jack picks the min.

So code should handle all these.

Now, the code:

In Python, the code would read the inputs, then process each row.

Read n and m from the first line.

Then for n lines, read each line as a list of integers.

Compute the min of each list, collect into a list.

Then take the max of that list.

So the code is:

n, m = map(int, input().split())
minima = []
for _ in range(n):
    row = list(map(int, input().split()))
    minima.append(min(row))
print(max(minima))

Yes, that's the code. Let's test it against the examples.

First example input:

3 4
4 1 3 5 → min 1
2 2 2 2 → min 2
5 4 5 1 → min 1
minima list is [1,2,1]. max is 2 → correct.

Second example:

3 3
1 2 3 → min 1
2 3 1 → min 1
3 1 2 → min 1
max of [1,1,1] is 1 → correct.

Yes. So this code should work.

Another test case: n=1, m=1: input 1 1 followed by 5. Output is 5.

Another test case: n=2, m=3, rows: [3, 2, 5] and [1,4,6]. Minima are 2 and 1. Max is 2.

So code works.

So the code is correct.
</think>

```python
n, m = map(int, input().split())
print(max(min(map(int, input().split())) for _ in range(n)))
```