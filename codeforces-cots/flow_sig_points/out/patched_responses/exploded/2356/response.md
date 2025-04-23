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
        count +=1

print(min_diff, count)

Wait, but this approach only requires O(1) extra space (except for the sorted list), which is better. Because we can compute the differences on the fly, track the current minimal, and count how many times it occurs. This is more efficient in terms of memory, which could be important for large n.

Yes, because in the previous approach of creating a list of diffs, we use O(n) space for that list. But with n up to 2e5, 200k integers is about 1.6MB (since each int in Python is 28 bytes or something, but maybe more). Hmm, but 2e5 * 28 bytes is around 5.6 million bytes, which is about 5.6MB. Still manageable under 256MB. But the second approach is better for memory, even though both are O(n). But in Python, the code that computes the difference on the fly and tracks min and count is better, as it avoids creating a separate list. So that's the way to go.

So code:

After sorting, loop through the array once, compute each difference. For each difference:

- if it's smaller than current min_diff, reset min_diff to this value, reset count to 1.

- else if equal to current min_diff, increment count.

- else do nothing.

So this way, we process all consecutive pairs and track the minimal difference and count in O(n) time, O(1) space (excluding the sorted list).

Yes. So the code should be efficient.

Testing the sample inputs.

First sample:

Input:

4

6 -3 0 4

After sorting: -3,0,4,6.

Differences:

0 - (-3) = 3

4-0=4

6-4=2.

So min_diff starts as inf. The first diff is 3. min_diff becomes 3, count 1. Next diff 4: larger, no change. Next diff 2: less than 3. So min_diff becomes 2, count reset to 1. So the output is 2 1.

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