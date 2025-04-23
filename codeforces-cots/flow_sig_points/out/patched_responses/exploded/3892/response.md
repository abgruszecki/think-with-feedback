<think>
Okay, let's see. The problem is about three friends on a line who want to meet at a point so that the total distance they travel is minimized. Hmm, right. So the task is to find the point where their combined travel distance is the smallest possible.

Wait, the optimal point for minimizing the sum of absolute differences is the median of the three points. Oh right, because when you have three points, the median is the point where the sum of distances is minimized. Let me think. For example, if the points are sorted as a, b, c, then choosing b (the median) would give total distance (b-a) + (c - b) + 0? Wait no, wait. Wait, the total distance would be (b - a) for the first friend, (c - b) for the third friend, and the second friend is already at b. So total is (b-a) + (c - b) = c - a. But if the meeting point is somewhere else, like between a and b, then the sum would be longer. For instance, if the meeting point is a, then the sum is 0 + (b - a) + (c -a). Which is (b -a) + (c -a) = (b + c) - 2a. Which is larger than c -a if a < b < c. So the median is indeed the best choice here.

So the approach would be: sort the three points, take the middle one as the meeting point, then compute the sum of absolute differences between each point and the median.

So the steps are:

1. Read the three integers x1, x2, x3.
2. Sort them in non-decreasing order.
3. The meeting point is the middle value (the median).
4. Calculate the total distance: sum of (each point - median) absolute values.

Wait, but wait. Let's test the examples given.

First example input: 7 1 4. Sorted, they are 1,4,7. Median is 4. The sum is (4-1) + (4-4) + (7-4) = 3 +0 +3 =6. Which matches the first sample's output.

Second example: 30 20 10. Sorted as 10,20,30. Median is 20. Sum is (20-10) + 0 + (30-20) =10 +10=20. Which matches the second sample.

So that's the correct approach.

So the steps are straightforward. Now, the code in Python.

So code steps:

Read the three numbers as a list.

Sort the list.

Find the median (which is the second element in the sorted list of three elements).

Compute the sum of absolute differences between each element and the median.

Output that sum.

So in Python:

x = list(map(int, input().split()))
x_sorted = sorted(x)
median = x_sorted[1]
total = 0
for num in x:
    total += abs(num - median)
print(total)

That's the code. It's O(1) time and space, since the input is fixed size, so no issues with constraints.

Testing the first sample:

Input 7 1 4. Sorted is [1,4,7]. Median 4.

Sum: |7-4| (3) + |1-4| (3) + |4-4| (0) → 6. Correct.

Second sample: 30 20 10 sorted to 10,20,30. Median 20. Sum 10 (20-10) + 0 (20-20) + 10 (30-20) → 20. Correct.

So this should work.

No edge cases, since the problem statement says all inputs are distinct. So sorting them gives three distinct elements, the median is the middle one. So code works.
</think>

```python
x = sorted(map(int, input().split()))
print(x[2] - x[0])
```

Wait, wait! Wait a minute. Oh, right. Because the sum of the absolute differences between the three points and their median is equal to the difference between the maximum and the minimum. Because for sorted [a, b, c], the sum is (b - a) + (c - b) → c - a. Because the median is b. So the sum of the three distances is (b - a) + 0 + (c - b) = c - a. So in code, after sorting, the answer is simply x[2] - x[0]. Which is even simpler.

So the code can be written as:

Read the three numbers, sort them, subtract the first from the third. That gives the total distance.

Which is much more efficient. Let me check the examples again.

First example: 7 1 4 sorted as 1,4,7 → 7-1=6. Correct.

Second example: 10,20,30 → 30-10=20. Correct.

Yes! So this is a better approach. So the code can be written in two lines. That's even better.