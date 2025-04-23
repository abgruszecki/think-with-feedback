<think>
Okay, I need to solve this problem where I have to find a segment that covers all others. Let's see. The problem says that there's a segment in the list which contains all other segments. So, for each segment, I need to check if its left is less than or equal to all other segments' lefts and its right is greater than or equal to all others' rights. If such a segment exists, return its index (1-based), else -1.

First, let's think about the steps. How can I efficiently find such a segment?

The brute force approach would be for each segment, check all others to see if their l and r are within this segment's l and r. But with n up to 1e5, that's O(n^2) which is way too slow. So that's not feasible.

So, I need a smarter way. Let's think: the segment that can cover all others must have the minimum l and maximum r among all segments. Because if there's a segment that covers all others, its l must be the smallest possible and r the largest possible. Otherwise, there's a segment that starts before it or ends after it, which can't be covered by it.

Wait, but maybe there are multiple segments with the same min l and max r. But according to the problem statement, all segments are distinct. So maybe only one segment has the min l and max r.

Wait, but how? For example, if two segments have the same l and r, but the problem states that no two segments coincide. So each segment is unique. So the min l and max r can only be present in one segment.

Wait, maybe not. Let's see. Suppose there's a segment [1,5], another [1,6]. Then the min l is 1, max r is 6. So the segment [1,6] would have the min l (1) and max r (6). So in that case, the segment with min l and max r is unique. Because any other segment with min l would have a higher l, or same l but different r. Since the segments are all unique, even if two have the same l, their r's must differ.

Wait, the problem says "no two segments coincide". So for two different segments, either their l's differ, or their r's differ. So, for example, if one segment is [1,5], another is [1,6], they are different.

So, the candidate for covering all others must be the segment that has the minimum l and maximum r. Because only such a segment can possibly cover all others. Because any other segment would have either a higher l (so the candidate's l is smaller, hence can cover that) or a lower r (so the candidate's r is larger). So if there's a segment with l equal to the global min l, and r equal to the global max r, then that's the only possible candidate. Then, we need to check if this candidate indeed covers all other segments.

Because, even if a segment has the min l and max r, maybe some other segment has a l between this segment's l and r, but their r is also between. For example, if the candidate is [1,10], but another segment is [2,9], which is covered. But if another segment is [0,5], but the candidate's l is 0. Wait, no. Because the candidate's l is the global min. So all other segments have l >= candidate's l. And the candidate's r is the global max, so all other segments have r <= candidate's r. Therefore, if there exists a segment that has l equal to the global min and r equal to the global max, then all other segments' l >= candidate's l, and r <= candidate's r. Therefore, that candidate must cover all others.

Wait, that's correct. Because the candidate has the minimum l and maximum r. So any other segment's l can't be less than the candidate's l (since it's the minimum), and the other's r can't be more than the candidate's r (since it's the maximum). So the candidate's l <= other's l, and candidate's r >= other's r. Therefore, the candidate's segment [l, r] will cover [other's l, other's r] because other's l >= candidate's l and other's r <= candidate's r. So if such a candidate exists, then it's the answer. Otherwise, there is no such segment.

So the plan is:

1. Find the global min l and global max r among all segments.

2. Check if there exists a segment in the list whose l is equal to the global min l and r is equal to the global max r.

3. If such a segment exists, return its index (1-based). Otherwise, return -1.

Because that's the only possible candidate. Because any other segment would have a larger l or smaller r, meaning it can't cover all segments.

So the steps are:

- Iterate through all segments to find the min l and max r.

- Then, iterate through the segments again to find the first one (since they are unique) that has l == min_l and r == max_r.

If found, output its position. Else, output -1.

Yes. Because if there's a segment with min l and max r, then all other segments have l >= min_l and r <= max_r, so that segment covers them all.

But wait, the problem statement says "the i-th segment starts at the position li and ends at the position ri. We will denote such a segment as [li, ri]." So the candidate must have l equal to the global minimum of all l's, and r equal to the global maximum of all r's. Because if there's another segment with l equal to the global min but r less than the global max, then there's a segment with higher r which is not covered by the candidate.

So the candidate must have both l and r as the global extremes.

So the approach is correct.

Now, how to implement this efficiently?

In Python, reading n up to 1e5. So need to read the input efficiently.

First, read all the segments, storing their l, r, and their original indexes. Then, compute the min of all l's and the max of all r's.

Then, check each segment to see if any of them has l == min_l and r == max_r. Since the segments are unique, there can be at most one such segment.

Once found, return the index. Otherwise, -1.

So, code steps:

Read n.

Read n lines, each with li and ri. Store them as a list of tuples, along with their 1-based index.

Compute min_l as the minimum of all li's.

Compute max_r as the maximum of all ri's.

Loop through the list of segments, checking if any of them has li == min_l and ri == max_r.

If found, output the index (original position). Else, -1.

This is O(n) time, which is acceptable for 1e5.

So for example, in the second test case:

Segments are:

1 5

2 3

1 10

7 10

7 7

10 10

The min_l is 1 (from the first and third segments). The max_r is 10 (third and fourth segments). The third segment is (1,10), which has l=min_l and r=max_r. So that's the answer. So output 3.

In the first test case:

Segments are 1-1, 2-2, 3-3. min_l is 1, max_r is 3. None of the segments has l=1 and r=3. So output -1.

So code seems correct.

Now, code in Python.

But need to read the input efficiently. For 1e5 lines, using input() in a loop can be slow in Python. So perhaps read via sys.stdin.

But according to the problem statement, the solution must read input via input() and write via print(). But for handling large input, using sys.stdin is better.

Wait, but in Python, using input() in a loop for 1e5 lines can be slow, but maybe with some optimizations.

Alternatively, read all the data at once.

But let's code it as follows:

Read n.

Then read n lines, each as a pair of integers.

So code:

segments = []
min_l = float('inf')
max_r = -float('inf')

for i in range(n):
    l, r = map(int, input().split())
    segments.append( (l, r, i+1) )
    if l < min_l:
        min_l = l
    if r > max_r:
        max_r = r

Then, loop through the segments to find one with l == min_l and r == max_r.

If found, return its index (third element in the tuple).

Else, -1.

Yes.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    min_l = float('inf')
    max_r = -float('inf')
    segments = []
    for idx in range(n):
        l, r = map(int, input_stream.readline().rstrip("\n").split())
        segments.append( (l, r) )
        if l < min_l:
            min_l = l
        if r > max_r:
            max_r = r

    found = -1
    for i in range(n):
        l, r = segments[i]
        if l == min_l and r == max_r:
            found = i + 1  # 1-based index
            break

    print(found, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
1 5
2 3
1 10
7 10
7 7
10 10
""",
            "output": \
"""\
3
""",
        }, 
    ]

    for i, test_case in enumerate(TEST_CASES):
        in_stream = io.StringIO(test_case["input"])
        expected_output = test_case["output"].rstrip()

        out_stream = io.StringIO()
        main(in_stream, out_stream)
        real_output = out_stream.getvalue().rstrip()

        assert real_output == expected_output, \
            f'Test case {i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}'

    print('Tests passed 😎')


if __name__ == '__main__':
    test()


```

<RUN_SNIPPET>
```output
Tests passed 😎

```

Second example:

Segments are:

1 5 → min_l 1, max_r 5 → then next segment 2 3 → min remains 1, max remains 5. Then third segment 1 10 → min_l 1, max_r 10. So after processing all segments, min_l is 1 and max_r is 10. Then check each segment. The third one has l=1, r=10. So found is 3.

Yes.

Another test case: suppose n=1. Then the only segment must cover itself. So min_l and max_r are same as the l and r of that segment. So found is 1.

Yes.

Another test case: two segments, [1,3], [2,4]. min_l is 1, max_r is 4. Check if any segment has l=1 and r=4. No. So output -1.

Yes.

Thus, the code works.
</think>

```python
n = int(input())
min_l = float('inf')
max_r = -float('inf')
segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))
    if l < min_l:
        min_l = l
    if r > max_r:
        max_r = r

found = -1
for i in range(n):
    l, r = segments[i]
    if l == min_l and r == max_r:
        found = i + 1
        break

print(found)
```
