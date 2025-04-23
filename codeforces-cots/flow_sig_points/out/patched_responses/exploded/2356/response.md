<think>
Okay, let's tackle this problem. So the task is to find the minimal distance between any two cities and count how many pairs have this minimal distance. Hmm. The first thing that comes to mind is that we need to process all pairs of cities, but with n up to 2e5, that's O(n^2) which is way too slow. So we need a smarter approach.

Wait, right. The brute force approach of checking every possible pair is definitely not feasible here. So what's the optimal way? Oh right, if we sort the array of coordinates first. Then the minimal distance between adjacent elements in the sorted array must be the minimal possible overall. Because once the array is sorted, the closest elements are next to each other, so checking consecutive elements will give the minimal distance. Then, the count is the number of pairs of consecutive elements that have this minimal distance.

So the steps are: sort the array, compute the differences between consecutive elements, find the minimum difference, then count how many times this minimum occurs.

Let me think about the steps in code. First, read n and the array. Then sort the array. Then compute the differences between each adjacent pair. Find the minimum difference. Then go through the differences again and count how many times the minimum occurs.

Yes, that's the plan. Now, let's consider the edge cases. For example, if all consecutive pairs have the same difference, like in the second example where the array after sorting is -2, 0, 2. The differences are 2 and 2. So minimal is 2, and there are 2 pairs. But wait, the answer in that case is 2 pairs, which corresponds to ( -2 and 0 ) and (0 and 2), each contributing a difference of 2. But the actual pairs of cities are (-2,0), (0,2), (-2,2) is larger. Wait, no. Wait, after sorting, the array is -2,0,2. The consecutive pairs are (-2,0) and (0,2), each with difference 2. So the minimal is 2, and there are two pairs. So that's correct. So the count is correct.

So the approach of looking only at consecutive pairs in the sorted array works because the minimal distance must be between some pair of consecutive elements. Because if there were three elements a < b < c, then the minimal could be between a and b or b and c. But if there's a pair that's not consecutive in the sorted array, like a and c, their distance is larger than the minimal consecutive pairs, so the minimal can't be there.

So the algorithm is correct.

Now, let's think about the implementation. The time complexity comes from sorting, which is O(n log n), which is acceptable for n up to 2e5. Then the rest is O(n) steps. So that's manageable.

Now, code steps:

1. Read n from input.
2. Read the list of integers a.
3. Sort the list.
4. Compute the differences between consecutive elements.
5. Find the minimum difference.
6. Count the number of times this minimum occurs in the differences.
7. Output the minimum and the count.

For example, in the first sample input:

4
6 -3 0 4

After sorting: -3, 0,4,6. The consecutive differences are 3,4,2. The minimal is 2, which occurs once. So output is 2 1.

Yes.

Now, code in Python.

But wait, handling large input. Since n can be up to 2e5, in Python, reading the input efficiently is important. So using input().split() directly might be okay, but we need to read the second line as a list of integers.

So the code:

Read n as int(input()), then the list as list(map(int, input().split())).

Sort the list.

Compute the differences. Initialize min_diff as a large number, then iterate from 1 to n-1, compute a[i] - a[i-1], but since we take absolute value (but wait, after sorting, the array is in ascending order, so a[i] >= a[i-1], so the difference is positive. So no need for absolute value here. Because the list is sorted in non-decreasing order. So the consecutive differences are non-negative. So the minimal difference is the minimal of these consecutive differences.

Once the list is sorted, yes.

So code steps:

sorted_a = sorted(a)

diffs = [sorted_a[i] - sorted_a[i-1] for i in range(1, len(sorted_a))]

min_diff = min(diffs)

count = diffs.count(min_diff)

Then output min_diff and count.

Yes. That's straightforward.

Now, possible optimizations. For n=2e5, creating a list of diffs with 2e5-1 elements is acceptable, but in Python, perhaps using a generator would save memory, but for 2e5 elements, it's manageable. Let's see, each difference is an integer (could be up to 2e9?), but storing them as a list is okay. But when n is 2e5, the list has 199,999 elements, which is about 200k, which is acceptable.

So the code can be written as:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    a.sort()

    min_diff = float('inf')
    count = 0

    for i in range(1, n):
        diff = a[i] - a[i-1]
        if diff < min_diff:
            min_diff = diff
            count = 1
        elif diff == min_diff:
            count +=1

    print(min_diff, count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
-2 0 2
""",
            "output": \
"""\
2 2
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

Second sample:

3

-2 0 2.

Sorted: -2,0,2.

Differences are 2 and 2.

First difference: 2. min_diff is 2, count 1. Next difference: 2. equal to min_diff, count becomes 2. So output is 2 2.

Yes.

Edge case when all differences are same. Like n=2e5, all sorted and consecutive differences are 1. Then min_diff is 1, count is 2e5 -1.

But that's okay.

Another edge case when n=2. Then the difference is one, count is 1.

So code handles that.

Thus, this approach is correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
a.sort()

min_diff = float('inf')
count = 0

for i in range(1, n):
    diff = a[i] - a[i-1]
    if diff < min_diff:
        min_diff = diff
        count = 1
    elif diff == min_diff:
        count += 1

print(min_diff, count)
```
