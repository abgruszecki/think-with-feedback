<think>
Okay, I need to solve this problem where I have to count the number of local extrema in an array. Let's see. The problem says a local extremum is either a local minimum or maximum. And for each element (except the first and last), I have to check if it's either a min or max compared to its immediate neighbors.

Hmm, first, I need to iterate through the elements starting from index 1 up to index n-2 (since the first and last elements are excluded). Wait, wait. Wait, the array is 0-based or 1-based here? Oh, the problem statement uses a1 and an, so probably the first element is a1 (1-based), but in code, arrays are 0-based. So when the input is read as a list in Python, the elements are 0-based. So for elements from index 1 to n-2 (if n is at least 3?), because if n is 2, there's no elements to check.

So the steps are:

1. Read n.
2. Read the array as a list of integers.
3. Initialize a counter to 0.
4. For each i from 1 to n-2 (inclusive), check if a[i] is a local min or max.
5. For each i, check if (a[i] > a[i-1] and a[i] > a[i+1]) → local max. Or (a[i] < a[i-1] and a[i] < a[i+1]) → local min. If either is true, increment the counter.
6. Return the counter.

Wait, but the elements can't be the first or last. So for example, in the first sample input where n=3, the elements are 1,2,3. The middle element is 2. Compare to 1 and 3. Since 2 is less than 3? So 2 is not a local max (since 3 is bigger) nor a min (since 1 is smaller). So output is 0. Which matches the example.

Another example: 4 elements 1 5 2 5. The second element (5) is compared to 1 and 2. 5 is greater than both → local max. Third element (2) is compared to 5 and 5. 2 is less than both → local min. So total 2. Which matches the output.

So the approach is straightforward. For each of the middle elements (indices 1 to len(arr)-2 in 0-based), check if it's a peak or valley.

Now, considering the constraints. The maximum n is 1000, which is very small. So even a O(n) solution (which this is) will be fast enough. So no issues with time.

The code steps in Python:

Read n from input. Then read the array as a list of integers. Then loop from i=1 to i=n-2 (but wait, in Python, the range is up to but not including the end. So for i in range(1, len(arr)-1). Because len(arr) is n. So for example, if n=4, len(arr) is 4. Then indices 0,1,2,3. The elements to check are 1 and 2. So range(1, 3) → 1 and 2. So that's correct.

So the code would be something like:

n = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(1, n-1):
    if (a[i] > a[i-1] and a[i] > a[i+1]) or (a[i] < a[i-1] and a[i] < a[i+1]):
        count +=1
print(count)

Wait, but for n < 2, like n=1 or n=2, there are no elements to check. For example, if n=1, then no elements. If n=2, then elements 0 and 1, but the loop runs from 1 to n-2. Since n=2, n-1 is 1, but the range is 1 to n-1 (since n-2 is 0), so range(1, 0) is empty. So the loop doesn't run. So that's correct.

So this code should handle all cases. Let's test the examples.

First example: input 3, 1 2 3. The loop runs for i=1 (0-based). Check a[1] (2) compared to 1 and 3. 2 is not greater than both (3 is bigger), and not less than both (1 is smaller). So no increment. Output 0. Correct.

Second example: input 4, 1 5 2 5. Loop runs for i=1 and i=2.

i=1: a[1] is 5. a[0] is 1, a[2] is 2. 5>1 and 5>2 → local max → count +=1.

i=2: a[2] is 2. a[1] is5, a[3] is5. 2 <5 and 2<5 → local min → count +=1. Total 2. Correct.

So this code should work.

Now, in terms of optimization. Since n is small (1000), even if we process all elements, it's O(n) time, which is acceptable. No data structures needed beyond the array. So this is optimal.

So the code is straightforward and correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(1, n-1):
    prev, curr, next_ = a[i-1], a[i], a[i+1]
    if (curr > prev and curr > next_) or (curr < prev and curr < next_):
        count += 1
print(count)
```