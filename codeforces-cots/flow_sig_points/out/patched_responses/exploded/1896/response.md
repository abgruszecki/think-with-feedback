<think>
Okay, let's try to solve this problem. So the task is to find the earliest day d where a_d is smaller than all the x days before it and the y days after it. And all a_i are distinct. So the first thing I need to do is figure out for each day d, check if all the days in the window before (x days) and after (y days) are greater than a_d. If that's the case, then it's a valid day. We need to find the earliest such d.

Hmm. Let's think about the constraints. The maximum n is 100,000. For each day, we need to check up to x days before and y days after. But x and y can be up to 7 each, so for each day, checking up to 14 days (x + y) around it. So the total operations would be O(n * (x + y)). For n=1e5, that's 1e5 * 14 = 1.4e6 operations, which is acceptable for Python, right? Since the time limit is 1 second. So maybe a brute force approach is feasible here.

Wait, but maybe there's a smarter way. Let's see. For each day d, the x days before d (from d-x to d-1) and the y days after (d+1 to d+y). We need all of those to have a_j > a_d. So for each d, check the maximum x in the left window and the maximum in the right window, and see if a_d is less than both. Wait, no. Because a_d must be less than all of them, not just the maximum. But since all a_j are distinct, if the minimum in the left window is greater than a_d, then all elements are. Wait, no. Wait, if a_d is less than the minimum of the left window, then all elements in the left window are larger than a_d. Similarly for the right window.

Wait, but how do we compute the minimum of the left x elements and the right y elements for each d? Because for each d, the left window is the x elements before it (but not going beyond day 1), and the right window is the y elements after (but not beyond day n). Then, the condition is that a_d is less than the minimum of the left window and the minimum of the right window.

Wait, no. Wait, a_d must be less than all elements in the left window (each one) and all elements in the right window. So for the left window, the minimum of the left window must be greater than a_d. Because if the smallest element in the left window is larger than a_d, then all elements are. Similarly, for the right window, the minimum must be larger than a_d.

Wait, no. Let me think again. For example, if the left window has elements 5, 4, 3. The minimum is 3. So a_d must be less than 3. Then all elements in the window (5,4,3) are larger than a_d. So yes, checking that a_d is less than the minimum of the left window and the minimum of the right window would suffice.

So the problem reduces to, for each day d, check two things:

1. The minimum of the x days before d (but at least 1) is greater than a_d.

2. The minimum of the y days after d (but at most n) is greater than a_d.

If both are true, then d is a candidate. We need to find the earliest such d.

So how do we compute for each d the min in the left window and the right window?

But the left window for d is the x elements before d. So for example, if x is 2, then d-2, d-1. But if d is 3, then days 1 and 2. If d is 1, then the left window is empty (since x can be 0). Wait, x can be 0. So if x is zero, there's no left window. Similarly for y.

Wait, the problem statement says that x and y can be 0. So for example, if x is 0, then there's no days before d to consider. So the condition for the left window is automatically satisfied. Similarly, if y is 0, no days after to consider.

So for each d:

Left window: [d - x, d - 1]. But since days start at 1, we need to take max(1, d - x) to d -1. But wait, the left window is d -x <= j < d. Wait, according to the problem statement: "d - x ≤ j < d" and "d < j ≤ d + y". So the left window includes j starting from d-x (but not less than 1) up to d-1. So for example, if d is 3 and x is 5, then j can be from 3-5 = -2 up to 2. But since days start at 1, the left window is 1 to 2. So for each d, the left window is max(1, d -x) <= j < d. Similarly for the right window: j ranges from d+1 to min(n, d + y).

Wait, the problem says: "d - x ≤ j < d" and "d < j ≤ d + y". But j must be >=1 and <=n. So for the left window, the actual j's are the intersection of [d-x, d-1] and [1, n]. Similarly for the right window.

So for each d, the left window is from max(1, d -x) to d-1 (inclusive). But if d -x > d-1, then the window is empty. Which can happen if x is zero. For x=0, the left window is d -0 ≤ j < d → j <d. But since x=0, the left window is empty. So the condition for left window is automatically satisfied. Similarly for y=0, the right window is empty, so the condition is automatically satisfied.

So the problem is for each d, check two things:

- All elements in the left window (if any) are greater than a_d.

- All elements in the right window (if any) are greater than a_d.

But since all a_i are distinct, this can be checked by comparing a_d to the minimum of the left window (if x>0) and to the minimum of the right window (if y>0).

So, for each day d, we need to compute:

left_min = min(a[j] for j in left_window) if left_window is not empty.

Similarly for right_min.

If x>0 and left_window is not empty (i.e., d -x <= d-1 >=1), then a_d must be less than left_min.

If y>0 and right_window is not empty (i.e., d+1 <=d + y <=n), then a_d must be less than right_min.

But how do we compute left_min and right_min efficiently?

For each d, the left window is up to x elements before it. For x up to 7, maybe for each d, we can just check the x elements before it. Since x is small (max 7), this is manageable. Similarly for y (up to 7). So for each d, check up to x elements before and y elements after.

So the approach could be:

Iterate d from 1 to n.

For each d:

- Check the left window: look back up to x days (but not before day 1). Check if all a[j] > a_d.

- Check the right window: look forward up to y days (but not after day n). Check if all a[j] > a_d.

If both conditions are met, return d as the earliest possible.

Since for each d, this is O(x + y) operations, and x and y are up to 7 each, this is O(14n) operations. For n=1e5, that's 1.4e6 operations, which is acceptable.

Yes, this approach should work.

So the steps are:

1. Iterate through each day d from 1 to n.

2. For each d, check the x days before (if x>0) and y days after (if y>0).

3. For the left check:

   - start from max(1, d - x) to d-1.

   - check if any a[j] <= a_d. If yes, then left check fails.

4. Similarly for the right check:

   - start from d+1 to min(n, d + y).

   - check if any a[j] <= a_d. If yes, right check fails.

5. If both checks pass, return d.

6. The first such d encountered is the answer.

So in code, for each d, loop through the left and right ranges.

But in Python, looping for x (up to 7) steps per d is manageable.

So let's see the sample input 1:

10 2 2

The array is 10,9,6,7,8,3,2,1,4,5.

For day 3 (index 3 in 1-based), the left days are 1 and 2 (values 10 and 9). Both are greater than 6. The right days are 4 and 5 (7 and 8). Both are greater than 6. So day 3 is valid.

For day 8, the left days are 6,7 (values 3,2,1?), wait no. Wait, d=8. x=2. So days 6,7. a[6] is 3, a[7] is 2. Both are greater than a[8] which is 1. The right days are 9 and 10 (4,5). So yes. So day 8 is valid.

In sample 1, the answer is 3, which is the earliest.

In sample 2, the y is 3, so for day 3, the right window is days 4,5,6. a[6] is 3. a_d is 6. 6 is not less than 3, so day 3 is invalid. So the next candidate is day 8. Let's see: for day 8, x=2. Left days are 6 and 7 (3, 2). Both are greater than a[8] =1. Right window is days 9,10 (4,5), and since y=3, but there's only 2 days after. So all are greater. So day 8 is valid. So answer is 8.

So the approach works.

Now, how to implement this in Python.

The code needs to read n, x, y. Then the array a (list of integers). Then for each d in 1..n, check left and right.

But in Python, the list is 0-based. So when processing day d (1-based), the index is d-1 in the list.

So code steps:

Read n, x, y.

a = list of integers (read from input).

for d in range(1, n+1):

    valid = True

    # check left window: days j where d -x <= j <d, and j >=1.

    start = max(1, d -x)

    end = d -1

    if x >0 and start <= end:

        for j in range(start, end+1):

            if a[j-1] <= a[d-1]:

                valid = False

                break

        if not valid:

            continue

    # check right window: days j where d <j <=d + y, j <=n.

    start_r = d +1

    end_r = min(n, d + y)

    if y >0 and start_r <= end_r:

        for j in range(start_r, end_r +1):

            if a[j-1] <= a[d-1]:

                valid = False

                break

        if not valid:

            continue

    if valid:

        print(d)

        exit()

So the first d that passes both checks is printed.

But in Python, for each d, the left window is up to x elements. For x=7, and y=7, each check is up to 7 elements. For 1e5 * 14 = 1.4e6 operations, this is acceptable.

But wait, in the code, the ranges for j could be up to x elements (if x is 7). So for each d, in the worst case, 14 checks (7 left, 7 right). For n=1e5, 1.4e6 iterations. Which is manageable.

So this should work.

Now, test the third sample:

Input:5 5 5

array: 100000 10000 1000 100 10.

Each a[i] is decreasing. So for day 5 (d=5), the left window is 0 (since x=5: d -x =0, so start is 1. end is 4. All elements 100000, 10000, 1000, 100. a[5] is 10. So all are greater. The right window is empty (since d+ y=5+5=10, but n is 5). So condition holds. So answer is 5.

So code would check d=1,2,3,4,5.

For d=5, the left window is 1-4 (x=5, but d is 5, so 5-5=0 → start is 1. end is 4). All elements are larger than 10. So yes. So code returns 5.

Yes.

So the code works.

Now, code optimization.

In Python, for loops are not the fastest, but with x and y up to 7, it's manageable.

But perhaps, we can precompute for each day the left and right minimums, but given that x and y are small, the current approach is better.

Another optimization: for the left window, check if any element in [d-x, d-1] (adjusted for boundaries) is less than or equal to a_d. But since the elements are all distinct, if any is less than a_d, then the condition fails. Wait, no: the condition is a_d must be less than all. So if any a[j] <= a_d, the condition fails. So in the left window, we can break early once we find any a[j] <= a_d.

Which the code is doing. So for each j in the left window, as soon as one element is <= a_d, the check fails, and the code skips to the next d.

Similarly for the right window.

So the code is optimized in that way.

Another thing: for d=1, x could be up to 7, but since d- x could be 0, the start is 1, end is 0 → no elements. So left check is skipped (since start > end). So code correctly skips.

Similarly for days near the end.

So the code is correct.

Now, let's code it in Python.

Read n, x, y from input.

Read a as a list of integers.

Loop d from 1 to n:

   check left.

   check right.

   if both pass, output d and exit.

Now, the code.

Wait, but in Python, when you read from input, the a is read as a list. So for 1-based d, a[d-1] is correct.

Yes.

So code:

n, x, y = map(int, input().split())
a = list(map(int, input().split()))

for d in range(1, n+1):
    # Check left
    valid = True
    # Left window: j from max(1, d -x) to d-1 inclusive
    left_start = max(1, d - x)
    left_end = d - 1
    if x > 0 and left_start <= left_end:
        for j in range(left_start, left_end + 1):
            if a[j-1] <= a[d-1]:
                valid = False
                break
        if not valid:
            continue
    # Check right
    right_start = d + 1
    right_end = min(n, d + y)
    if y > 0 and right_start <= right_end:
        for j in range(right_start, right_end +1):
            if a[j-1] <= a[d-1]:
                valid = False
                break
        if not valid:
            continue
    print(d)
    exit()

Yes.

This should handle all cases.

Testing the sample inputs.

Sample 1:

Input:
10 2 2
10 9 6 7 8 3 2 1 4 5

Processing days:

d=1: left window is max(1, 1-2)=0 → 1. left_end is 0. So no left check. Right window is 2 to 3. Check if any of a[1], a[2] (9,6) <=10. Yes, 9 and 6 are <=10. So a_d=10, right check will check days 2 and 3. For j=2, a[j-1] is 9 <=10 → yes. So right check fails. So d=1 is invalid.

d=2: left window is max(1, 2-2=0 → 1. left_end=1. Check a[0] (10) >9? 10>9: yes. So left check passes. Right window is 3-4. Check a[2] (6) and a[3] (7) <=9. 6 is less than 9 → right check fails. So d=2 invalid.

d=3: left window is max(1,3-2=1) to 2. Check a[0] (10) and a[1] (9) → both >6. Left check passes. Right window 4-5. a[3]=7, a[4]=8. Both >6. So passes. So output 3.

Which matches the sample.

Sample 2:

Input:

10 2 3

a is same as sample 1.

d=3: check left (days 1-2: 10,9>6). Right window is days 4-6 (7,8,3). a[5] (3) is less than 6? 3 <6. So right check fails. So d=3 invalid.

Eventually, d=8. Check left days 6 and 7 (a[5], a[6] →3,2). Both >1. Right window is 9-10 (4,5). Both >1. So passes. So output 8.

Sample 3:

n=5, x=5, y=5.

array is 100000, 10000, 1000, 100, 10.

d=5: left window is max(1,5-5=0 →1) to 4. So check days 1-4 (values 1e5,1e4,1e3,100). All are >10. So left passes. Right is days 6-... but n=5. So no right check. So output 5.

So code works.

Thus, this approach should be correct and efficient enough for the constraints.
</think>

```python
n, x, y = map(int, input().split())
a = list(map(int, input().split()))

for d in range(1, n + 1):
    valid = True
    left_start = max(1, d - x)
    left_end = d - 1
    if x > 0 and left_start <= left_end:
        for j in range(left_start, left_end + 1):
            if a[j - 1] <= a[d - 1]:
                valid = False
                break
        if not valid:
            continue
    
    right_start = d + 1
    right_end = min(n, d + y)
    if y > 0 and right_start <= right_end:
        for j in range(right_start, right_end + 1):
            if a[j - 1] <= a[d - 1]:
                valid = False
                break
        if not valid:
            continue
    
    print(d)
    exit()
```