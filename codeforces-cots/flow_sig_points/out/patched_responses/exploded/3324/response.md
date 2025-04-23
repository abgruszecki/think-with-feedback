<think>
Okay, let's tackle this problem. The goal is to find the minimum number of points to add so that all neighboring points have equal distances. So the points after adding must form an arithmetic sequence. Hmm.

First, I need to sort the given points. Because when they're sorted, the differences between consecutive points can be examined. But the key is to find the maximum possible common difference (gcd of all the differences between consecutive points after sorting) because the minimum number of points is achieved when the common difference is as large as possible.

Wait, right. The idea is that the existing points must form a subset of an arithmetic progression. The minimal number of points to add is determined by the largest possible step (d) that divides all the differences between consecutive sorted points. Then, for each interval, the number of points to add is (difference / d) - 1. Summing all these gives the answer.

So the steps are:

1. Sort the input coordinates.
2. Compute the differences between consecutive points.
3. Find the greatest common divisor (gcd) of all these differences. That's the step size d.
4. For each original difference, compute (diff // d) - 1 and sum them all. That sum is m.

Wait, but how do we compute the gcd of multiple numbers? Let's see. For example, if the sorted points have differences 4, 6, 8, then the gcd of 4 and 6 is 2, then gcd of 2 and 8 is 2. So the overall d is 2. Then each interval of 4 would require (4/2)-1 = 1 point added, 6/2-1=2, 8/2-1=3. Sum is 1+2+3=6. But how does that fit into the arithmetic sequence?

Yes. So the approach is correct.

So first, sort the array. Then compute the differences between consecutive elements. Then compute the gcd of all those differences. Then for each difference, the number of points needed is (diff // d) - 1. Sum all those values.

Now, the problem is how to compute the gcd efficiently when there are up to 1e5 elements. Because n can be up to 1e5, the number of differences is (n-1), which is 1e5-1.

But computing the gcd of a list of numbers can be done by iteratively computing the gcd of the current result with the next element. For example, start with the first difference, then compute the gcd between that and the next difference, and so on. That's O(n) time, which is acceptable.

But wait, what if all the differences are zero? But the problem states that all coordinates are distinct. So after sorting, the differences are all positive. So no problem.

So, the plan is:

- Sort the array.
- Compute the differences between consecutive elements.
- Compute the gcd of all differences.
- For each difference, add (diff // d) - 1 to the total.

Now, the edge cases:

If all the differences are the same, then d is that difference. So each (diff//d -1) is zero. Sum is zero. Correct.

If the differences are not all the same, then the gcd will divide all of them, so the sum is correct.

Testing the first example:

Sample input 3:

-5, 5, 10 after sorting. Wait, original input was -5, 10,5. So sorted would be -5,5,10. The differences are 10 (5 - (-5) =10?), wait no: 5 - (-5) is 10? Then 10 -5 is 5. So differences are 10 and 5. The gcd of 10 and 5 is 5. Then the required step is 5. The total points needed:

10//5 -1 = 2-1=1 for the first difference, 5//5-1=0. Sum is 1. Correct.

Another example:

Sample input 4:

10 9 0 -1. After sorting: -1,0,9,10. Differences are 1,9,1. The differences are 1,9,1. The gcd is 1. So each difference is divided by 1. For 1, (1//1)-1=0. 9//1-1=8. 1//1-1=0. Sum is 8. Which matches the sample output.

So the approach works.

Now, the code steps:

Read n, then list of x's. Sort them. Compute the differences. Compute the gcd of those differences. Then sum (diff//d -1) for each difference.

So how to compute the gcd in Python?

The math.gcd function in Python returns the gcd of two numbers. But for a list, you can iteratively compute the gcd. However, math.gcd only takes two arguments, and for more than two, you can compute pairwise.

But there's a problem: what if the list of differences is empty? Well, n is at least 3, so the sorted list has at least two differences. So for the list of differences, len is at least 2. So compute the gcd of the first two, then compute the gcd of that result with the next difference, and so on.

But wait, math.gcd returns a positive integer. Since all differences are positive (as the list is sorted and all x's are distinct), this is okay.

But in Python, math.gcd returns the absolute value? Or does it work for positive numbers? Because the differences are positive. So no problem.

So code steps:

Sort the x list.

Compute the differences: for i in range(1, n):

   diffs.append(x[i] - x[i-1])

Then compute the gcd of all elements in diffs.

If there's only one difference, then d is that difference. But n is at least 3, so the number of differences is at least 2. So proceed.

Then compute sum of (d//g -1) for each d in diffs.

Now, code:

Read n.

Read list, sort.

Compute diffs.

Compute the gcd of all diffs.

Sum (diff//gcd -1) for each diff in diffs.

Return the sum.

So the code in Python:

But wait, how to compute the gcd for the list?

Initialize current_gcd as diffs[0], then loop through each diff in diffs[1:], compute current_gcd = gcd(current_gcd, diff). Repeat.

Yes.

But in Python, the math.gcd function returns the greatest common divisor of the two numbers. However, if the numbers are zero, but in our case, the diffs are all positive. So no problem.

So code:

import math

n = int(input())

x = list(map(int, input().split()))
x.sort()

if n == 1:
    # but n is >=3 according to constraints, so no need.
    pass

diffs = [x[i] - x[i-1] for i in range(1, n)]

current_gcd = diffs[0]
for d in diffs[1:]:
    current_gcd = math.gcd(current_gcd, d)

sum_m = 0
for d in diffs:
    sum_m += (d // current_gcd) -1

print(sum_m)

That's the code.

Testing sample input 1:

3

-5 10 5 → sorted [-5,5,10]

diffs are 10,5.

current_gcd starts as 10. Then next d is 5. gcd(10,5)=5.

sum is (10//5 -1) + (5//5 -1) → (2-1) + (1-1) =1 +0=1. Correct.

Sample input 2:

6

100 200 400 300 600 500 → sorted [100,200,300,400,500,600]

diffs are 100, 100, 100, 100, 100. current_gcd is 100.

sum each (100//100 -1)=0 for each. Sum is 0.

Sample input3:

4

10 9 0 -1 → sorted [-1,0,9,10]

diffs are 1,9,1.

current_gcd is 1. sum is (1//1-1) =0, (9//1-1)=8, (1//1-1)=0. Total 8.

So code works.

What about when the diffs are 4,6,8?

gcd(4,6) is 2. gcd(2,8) is 2. sum for each is (4/2-1)=1, 6/2-1=2, 8/2-1=3 → sum 6.

Yes.

So the code seems correct.

Now, considering the constraints. For n up to 1e5, the code runs in O(n) time, which is acceptable. Sorting 1e5 elements is O(n log n) which is acceptable for Python.

So this should be the correct approach.
</think>

```python
import math

n = int(input())
x = list(map(int, input().split()))
x.sort()

diffs = [x[i] - x[i-1] for i in range(1, n)]

current_gcd = diffs[0]
for d in diffs[1:]:
    current_gcd = math.gcd(current_gcd, d)

total = sum((d // current_gcd) - 1 for d in diffs)
print(total)
```