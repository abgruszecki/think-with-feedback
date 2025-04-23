<think>
Okay, let's see. The problem is, for each element in array b, we need to find how many elements in array a are less than or equal to that element. Hmm. So the straightforward approach would be for each bj in b, iterate through all elements in a and count those <= bj. But wait, the constraints say n and m can be up to 2e5. So if I do that, the time complexity would be O(m*n), which is 4e10 operations. That's way too slow. Definitely won't work within 2 seconds. So I need a more efficient method.

What's the optimal way here? Oh right, sorting and binary search. Because if array a is sorted, then for each query bj, I can perform a binary search to find the largest element in a that's <= bj. The index of that element (plus one) would be the count. So that's O(n log n) for sorting a, and O(m log n) for processing all elements in b. Which totals to O((n + m) log n) time. Since n and m are up to 2e5 each, log n is about 20, so 2e5 * 20 is 4e6 operations, which is manageable.

So the steps would be:

1. Sort array a in non-decreasing order.
2. For each element bj in array b:
   a. Use binary search to find the rightmost position in a where the element is <= bj.
   b. The count is (position + 1) if found, else 0 (if all elements are larger than bj).

But wait, how to handle the binary search correctly? Because there might be duplicates. For example, if a is [1,3,3,5], and bj is 3, the answer is 3. So the upper bound might not work here. Wait, no. The upper bound gives the first element greater than the target, but since we need elements <= target, the number of elements is the upper_bound's index. Wait, maybe using bisect_right here. Let me think.

In Python, the bisect module has bisect_right and bisect_left. For a sorted array a, bisect_right returns the insertion point which gives the number of elements <= to the target. Wait, no. Let me think again. For example, if a is [1,3,5], and target is 3. bisect_right returns 2, which is the index after the last 3. So the number of elements <=3 is 2. That's correct. So yes, using bisect.bisect_right(a_sorted, bj) would give the correct count.

Wait, but if the array has elements larger than the target, bisect_right returns the insertion point where all elements before are <=. So the number is the insertion index. So for each bj, we can sort a, then for each bj, perform a bisect_right and the result is the count. That's exactly what we need.

So the plan is:

- Sort a.
- For each bj in b, compute bisect.bisect_right(a, bj), then output that.

Yes. So the steps are straightforward. Now, considering the data size, we need to handle this efficiently.

In Python, the bisect module's bisect_right function is O(log n) per query, which is acceptable.

So the main steps are:

Read n and m.

Read array a.

Read array b.

Sort a.

For each element in b, compute bisect.bisect_right(a, bj) and collect all results.

Output them space-separated.

But wait, the input might have a lot of elements. So using input().split() for reading the arrays could be efficient, but in Python, for large inputs, it's better to read via sys.stdin. For example, using sys.stdin.readline for faster input.

Because with 2e5 elements, the input lines can be very long, and using input() might be slower. So in code:

We can read the arrays as:

import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

Sort a.

Then for each element in b, perform bisect.bisect_right(a, elem).

But wait, in Python, the bisect module's bisect_right function is available. So yes.

So the code would be:

import bisect

a.sort()
result = [bisect.bisect_right(a, x) for x in b]
print(' '.join(map(str, result)))

That's the core code.

But what about the time? Sorting a takes O(n log n) time. For m elements, each bisect is O(log n), so total O(m log n). Since n and m are up to 2e5, the total time would be acceptable.

But in Python, list comprehensions are efficient. So this approach should work.

Testing the first example:

Input:

5 4

1 3 5 7 9

6 4 2 8

After sorting a becomes [1,3,5,7,9].

For 6: bisect_right finds the position where 6 would be inserted. The elements are 1,3,5,7,9. 6 is between 5 and 7. So bisect_right returns 3 (since 5 is the last element <=6). So count is 3.

For 4: elements <=4 are 1,3. So bisect_right returns 2.

For 2: elements <=2 are 1. So 1.

For 8: elements <=8 are 1,3,5,7. So 4. Which matches the sample output.

The code seems correct.

Another sample input:

5 5

1 2 1 2 5 → sorted a is [1,1,2,2,5]

For each bj in [3,1,4,1,5]:

3 → elements <=3 are all except the last 5. So 4 elements (1,1,2,2). bisect_right(a,3) would find the index where 3 would be inserted. Since all elements are <=3 except the last 5? No, a is [1,1,2,2,5]. So bisect_right(3) would return 4. So count 4. Which matches the first output 4.

For 1: bisect_right(a,1) returns 2 (since the two 1s are in positions 0 and 1. Inserting after them gives 2). So output 2.

Yes, which matches the sample.

So the code works.

Now, considering memory. The arrays are stored in lists. For 2e5 elements, each integer is stored. Python lists can handle this, as 2e5 elements are manageable within 256MB.

In Python, using the bisect module's functions is optimized, but since we have to process 2e5 elements in b, each requiring a binary search on a list of 2e5 elements, the code should be efficient enough.

So the code is correct and efficient.
</think>

```python
import bisect
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    a.sort()
    result = [bisect.bisect_right(a, x) for x in b]
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
```