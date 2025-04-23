<think>
Okay, let's tackle this problem. The goal is to maximize the profit from building houses with certain height restrictions. Each house's profit is the square of its height. The challenge is to set the heights such that all zoning restrictions are met and the sum of squares is maximized.

First, I need to understand the constraints. The problem states that each of the m restrictions specifies a range [l_i, r_i] where the tallest house in that range can't exceed x_i. So for every such interval, the maximum height in that interval must be <= x_i. Additionally, each house's height can't exceed h.

Hmm. The key here is that for each position, the maximum possible height is the minimum of h and all x_i that cover this position in their intervals. Wait, not exactly. Because a restriction applies to a range, and the maximum in that entire range must be <= x_i. So if a position is part of multiple overlapping intervals, each of those intervals' x_i must be considered. For example, if a house is in two intervals with x_i values 5 and 3, then the maximum in each of those intervals can't exceed their respective x_i. So the house might have to be lower than both 5 and 3 if it's the tallest in those ranges.

But how to model this? Let's think. For each position j, the maximum possible height allowed by all intervals that include j in their range, but not exactly. Wait, no. Because the restrictions are on the maximum in the interval. So for a given interval [l, r], the maximum in that interval can't exceed x. So for all houses in [l, r], their heights can't collectively have any of them exceeding x. So the tallest house in that interval must be <= x.

So the approach is to find for each interval [l, r], the maximum height in that interval is at most x. To model this, we can think that for each interval [l_i, r_i, x_i], the maximum height in that interval must be <= x_i. So each such restriction enforces that the maximum in that interval is as per x_i.

But how do we model this? Because a single interval could cover many positions. For example, if there's a restriction that the maximum in [1,3] is <=2, then the tallest house in positions 1,2,3 can't be higher than 2. So that could be achieved by all being <=2, but perhaps the max in any of them is 2, but others are lower. But for our problem, we want the maximum sum of squares, so each house's height should be as high as possible, provided that all the restrictions are met.

The problem is similar to interval constraints where each interval must have at least one element that is at most x_i (but no, because the maximum must be <= x_i). So for each interval [l_i, r_i], the maximum in that interval is <= x_i. Which implies that all elements in that interval are <= x_i. Wait, no. Because the maximum is <=x_i, so all elements in the interval must be <=x_i. Because the maximum is the highest, so if even one element is higher than x_i, the maximum would be higher. So, any restriction [l_i, r_i, x_i] implies that all positions in l_i..r_i must have their heights <=x_i. Because otherwise, the maximum would exceed x_i. Wait, no. Wait, if all elements in [l_i, r_i] are <= x_i, then the maximum is <=x_i. So the correct way to model this is that for each interval [l_i, r_i], all positions in that interval must be <= x_i. Because if any of them is higher than x_i, then the maximum of the interval would be higher than x_i, which violates the restriction.

Wait, but that's not correct. Wait, no. Suppose the restriction is that the maximum in [l_i, r_i] must be <= x_i. Then all elements in the interval must be <= x_i, because if any element is larger than x_i, then the maximum would be larger than x_i. Therefore, each such restriction [l_i, r_i, x_i] implies that the maximum allowed height for each position in that interval is the minimum of their own existing maximum (h) and x_i. But that's not correct. Because even if a position is in multiple intervals, each with x_i values, the maximum allowed for that position is the minimum of all x_i's from the intervals that include it, and the original h. Wait, no. Because if a position is part of two intervals with x_i=3 and x_i=5. Then the first interval's restriction is that the maximum in that interval is <=3, and the second's is <=5. So the first restriction requires that all positions in that interval (including this position) are <=3, but the second allows up to 5. But since the position is in the first interval, the maximum for that interval (including the position) must be <=3. So even if the position is in another interval that allows up to 5, but in the first interval's case, it's part of that interval, so all elements in that interval (including this position) must be <=3. So the position's maximum allowed height is 3. So the correct approach is that for each position j, the maximum allowed height is the minimum of h and the minimum x_i of all intervals that include j. Wait, no. Because even if j is part of an interval with x_i=3, but another interval that includes j has x_i=5, but j is allowed to be up to 3. But maybe that's not the case. Let me think again.

Suppose a position j is in two intervals: interval A [1,5] x=3, and interval B [3,4] x=5. Then for interval A, all positions 1-5 must be <=3, because the maximum in that interval must be <=3. So even if j is in another interval that allows higher, the first interval's restriction is more strict. So j's maximum allowed height is 3. So the maximum allowed for each position j is the minimum between h and the minimum x_i of all intervals that contain j. Because each such interval requires that in their range, the maximum is <=x_i. Therefore, any position in such an interval can't have a height exceeding x_i, otherwise, the interval's maximum would be higher than x_i, violating the restriction.

Wait, no. Suppose j is part of an interval [1,5] x=5 and [3,7] x=3. Then j is in both intervals. The first interval allows up to 5, but the second interval (which includes j) requires that the maximum in [3,7] is <=3. So for j, which is in [3,7], the maximum allowed is 3, because the second interval's restriction is stricter. Therefore, the maximum allowed height for j is the minimum of x_i for all intervals that include j, but also considering h.

So the correct approach is: for each position j, the maximum allowed height is the minimum between h and the minimum x_i among all intervals that include j. If a position is not covered by any intervals, then its maximum is h.

Wait, but this approach would ignore overlapping intervals. For example, if j is part of two intervals with x_i=4 and x_i=5, then the minimum x_i is 4. So j's maximum allowed is 4, which is correct because any interval that includes j and has x_i=4 requires that the maximum in that interval is <=4, which implies that j's height can't exceed 4. So yes, this approach is correct.

So the steps would be:

1. For each position j (1 to n), compute the maximum allowed height as the minimum between h and the minimum x_i of all intervals that include j. If there are no intervals covering j, then the maximum allowed is h.

2. Then, assign each position j the maximum possible allowed height (the value from step 1) to maximize the sum of squares.

But wait, that might not be correct. Because the same position can be part of multiple intervals, and the minimal x_i among those intervals would be the strictest. However, in the case where a position is part of an interval where x_i is larger than the minimal x_i from another interval, but the minimal x_i comes from another interval that doesn't include that position. Wait, no. Because each x_i for intervals that include j contributes to the minimal x_i for j.

Wait, the problem is that the initial approach of taking the minimal x_i for each j is the correct way to compute the maximum possible height for j. Because for any interval that includes j, the maximum in that interval must be <=x_i. But if j's height is higher than x_i for any of those intervals, then that interval's maximum would be higher than x_i, violating the restriction. So, the minimal x_i among all intervals that include j gives the upper bound for j's height.

So the correct approach is:

For each position j, the maximum allowed height is min(h, the minimal x_i among all intervals that include j). If there are no intervals covering j, then it's h.

Once we compute this for all positions, then the optimal strategy is to set each j's height to its maximum allowed value. Because the sum of squares is maximized when each individual term is as large as possible.

Wait, but is that correct? Let's see. Because if you have two positions, j and k, both in the same interval. Suppose j's maximum allowed is 3, and k's is 3. If we set j to 3 and k to 3, then the maximum in their interval is 3, which is allowed. But maybe if j is set to 3 and k to 2, but that's worse. So yes, setting each to their maximum allowed is optimal.

But wait, what if there are multiple overlapping intervals. For example, j is in interval A (x=3) and interval B (x=5). Then j's max allowed is 3. So setting it to 3 is allowed. Then, in interval B, which includes j and other positions, the maximum in that interval would be 3, which is <=5, which is allowed. So yes, that's correct.

So the conclusion is: the optimal solution is to compute for each position the minimum x_i among all intervals that include it (and compare with h), then set that position's height to that value. Then the sum is the sum of squares of those values.

But wait, let's check the first example.

First example input:

3 3 3

Restrictions:

1-1: x=1

2-2: x=3

3-3: x=2

So for position 1, the only interval is [1,1], x=1. So max allowed is 1.

Position 2: allowed is 3 (h is 3, and the x_i for the interval [2-2] is 3. So min(3,3)=3.

Position 3: allowed is 2.

So heights are [1,3,2], sum is 1+9+4=14, which matches the example.

Second example:

4 10 2

Restrictions:

2-3: x=8

3-4: x=7

For each position:

Position 1: no intervals. So allowed is 10.

Position 2: covered by interval 2-3 (x=8). So allowed is min(10, 8) =8.

Position 3: covered by both intervals. The first interval's x=8, second's x=7. So min is 7. Allowed is 7.

Position4: covered by second interval (3-4, x=7). So allowed is 7.

So heights are [10,8,7,7], sum 100+64+49+49 = 262. Which matches the example.

So this approach works for the sample inputs.

Therefore, the algorithm is:

1. For each position from 1 to n:

   a. Find all intervals that include this position.

   b. Take the minimum x_i among these intervals (or h if no intervals).

   c. The maximum possible height for this position is the minimum of h and the minimal x_i (if any).

2. Sum the squares of these heights.

So now, the problem reduces to, for each position j, compute the minimal x_i among all intervals that contain j. If no intervals contain j, then use h.

Then, the sum is the sum of squares of those values.

So how to compute this for each position?

We can model it as follows:

Initialize an array max_allowed of size n, with each element set to h.

For each restriction (l_i, r_i, x_i):

   For each j in [l_i, r_i], check if x_i is less than the current max_allowed[j-1]. If so, update max_allowed[j-1] to x_i.

Because each interval's x_i affects all positions in l_i to r_i. So for each such position, if x_i is smaller than the current max_allowed, we update it.

Yes, this makes sense. Because for each interval, all positions in it must have their allowed maximum height at least as small as x_i. So the minimal x_i among all intervals that include the position is the minimum of all x_i's of those intervals.

So the approach is:

Initialize max_allowed = [h] * n

for each of the m restrictions:

   l, r, x = input

   for j in l-1 to r-1 (assuming 0-based index):

       if max_allowed[j] > x:

           max_allowed[j] = x

Then, the profit is sum(a^2 for a in max_allowed)

Wait, but wait. What if a position is covered by multiple intervals with different x_i's. For example, position j is covered by two intervals, x1=5 and x2=3. Then, the minimal x_i is 3, so the allowed height is 3. So the code above would process each interval and for each j in that interval, set their max_allowed to min(current max_allowed, x_i). So yes, processing each interval and for each j in l_i..r_i, if x_i is smaller than the current max_allowed[j], then update it. So after processing all intervals, each j's max_allowed is the minimal x_i among all intervals that include j. And if there are no intervals, it remains h.

This seems correct.

So the code is straightforward.

Now, considering the constraints:

n, h, m up to 50.

So for m=50, each interval can be up to 50 positions. So the total operations are m * (r_i - l_i + 1) = 50 * 50 = 2500 operations. Which is very manageable.

So this approach is feasible.

Therefore, the code steps are:

Read n, h, m.

Initialize max_allowed as [h] * n.

Then read each of the m restrictions. For each, loop from l to r (converted to 0-based) and update max_allowed[j] to be the minimum between current and x.

Finally, compute the sum of squares.

Yes, this is correct.

Now, let's test this approach against the sample inputs.

First sample:

n=3, h=3, m=3.

max_allowed starts as [3,3,3].

Processing restrictions:

1. l=1, r=1, x=1. So j=0 (since 1-based to 0-based). For j=0: max_allowed[0] becomes min(3,1)=1. So max_allowed is [1,3,3].

2. l=2, r=2, x=3. j=1. max_allowed[1] is min(3,3) remains 3.

3. l=3, r=3, x=2. j=2. max_allowed[2] is min(3,2)=2.

Sum is 1^2 + 3^2 + 2^2 = 1+9+4=14. Correct.

Second sample:

n=4, h=10, m=2.

max_allowed is [10,10,10,10]

First restriction: l=2, r=3, x=8. So positions 1 and 2 (0-based). For each, update max_allowed to min(current, 8). So positions 1 and 2 become 8. max_allowed is [10,8,8,10].

Second restriction: l=3, r=4, x=7. Positions 2 and 3 (0-based). For position 2: current is 8, x=7. So update to 7. Position3: current is 10, updated to 7. Now max_allowed is [10,8,7,7].

Sum squares: 100 +64 +49 +49= 262. Correct.

So the code works for these cases.

Therefore, the code is as follows.
</think>

```python
n, h, m = map(int, input().split())
max_allowed = [h] * n
for _ in range(m):
    l, r, x = map(int, input().split())
    for j in range(l-1, r):
        if max_allowed[j] > x:
            max_allowed[j] = x
print(sum(a*a for a in max_allowed))
```