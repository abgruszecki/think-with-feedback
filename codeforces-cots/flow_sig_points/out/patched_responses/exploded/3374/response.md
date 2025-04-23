<think>
Okay, I need to solve this problem. Let's read it carefully.

The problem is about splitting n problems into two divisions such that:

1. Each division is non-empty.
2. All division 1 problems are harder than division 2. So there's a cutoff point where everything below (in difficulty) goes to div2 and above to div1.
3. Similar problems (given as m pairs) must be in different divisions.

The goal is to count the number of valid splits.

Hmm. So the first thing to note is that since the problems are sorted in ascending order of difficulty, the split must be a position k such that all problems up to k are in div2 and the rest in div1. Wait, no. Because the split can be any k where the div2 has all problems up to some k, and div1 has all problems after k. So for example, if k is 3, then problems 1,2,3 are div2 and 4,...n are div1. But since the cutoff must be such that every div1 problem is harder than div2, the split is a single point where all lower difficulties are div2 and higher are div1. So the possible splits are determined by choosing a k where the split is between problem k and k+1.

Wait, but the split is such that all in div2 are <=k, and div1 are >k. Or maybe the split is that all in div1 are >=k. Wait, no. Because the problems are in ascending order. So to have all div1 problems harder than div2, the split must be such that there's a k where div2 includes all problems with difficulty <=k, and div1 includes all >k. But wait, the problems are already sorted. So the split can be at any point between 1 and n-1. Because if we split after problem k, then div2 has 1..k and div1 has k+1..n. So for each possible k (from 1 to n-1), the split is determined. But the split must also satisfy the similar pairs condition.

Wait, but the split is determined by the cutoff k. So for each possible k (from 1 to n-1), we need to check if all similar pairs are in different divisions. If yes, then that k is a valid split, and contributes 1 to the count. But wait, the problem states that the split is considered different if any problem is in a different division. So the split is determined by the cutoff k. However, maybe there's more than one possible split for the same k if some problems can be moved around. Wait, no. Because once the cutoff is k, all problems 1..k must be in div2 and k+1..n in div1. So each k corresponds to exactly one way of splitting. So the total number of possible splits is the number of valid k's.

Wait, no. Wait, the split is determined by k: all problems in div1 must be harder than all in div2. So the split must be a cutoff where any problem in div2 is <=k and div1 is >k. So k is the maximum problem in div2. Therefore, the possible splits are determined by choosing any k between 1 and n-1, and then the split is 1..k in div2, k+1..n in div1. Then, for each such k, we need to check that for all similar pairs (u, v), one is in div2 and the other in div1.

So the problem reduces to counting the number of k in 1..n-1 such that for every similar pair (u, v), exactly one is in the first part (div2) and the other is in the second (div1).

So, how to model this?

For a given pair (u, v), if u and v are in the same division for a split k, then this split is invalid. So for a split k to be valid, for all similar pairs (u, v), they must cross the split. That is, one is in div2 and the other in div1.

So, for each similar pair (u, v), the split k must satisfy that either u <=k and v >k, or vice versa. So the pair (u, v) imposes a constraint on the possible k's.

The approach is to process all similar pairs and determine the allowed ranges of k that satisfy all pairs.

Let's think about how a single pair (u, v) affects the possible k. Let's assume u < v (since the problems are in ascending order). Wait, but wait: the problem says that the problems are arranged in ascending order by difficulty. So problem 1 is the easiest, problem 2 is next, etc. So if u and v are two different problems, then u < v in their numbers implies that u is easier than v. Wait, no: the problem states that the problems are arranged in ascending order by difficulty, so their indices reflect their difficulty. So problem 1 is the easiest, 2 is next, etc. So for any i < j, problem i is easier than problem j.

So for a similar pair (u, v), with u < v. For the split k to separate them, one must be in div2 (<=k) and the other in div1 (>k). So for this pair to be in different divisions, the split k must be >=u and <v. Because if k >=u and <v, then u is in div2 and v is in div1. So for this pair (u, v), the valid k's are those where u <=k <v. Because if k <u, then both are in div1 (since u <v, both >k). If k >=v, both are in div2. So the allowed k's for this pair are [u, v-1].

So for each similar pair (u, v), where u < v, the allowed k's are those in [u, v-1]. For each pair where u > v (but that can't happen since the pairs are stored in any order?), we need to swap them first.

Wait, the input gives pairs (ui, vi) where ui and vi can be any two distinct numbers. So first, for each pair, we need to sort them so that u is the smaller and v is the larger.

So for each pair (u, v), after sorting, u <v. Then the allowed k's are those between u and v-1, inclusive.

Thus, the valid k's must be in the intersection of all these intervals for all pairs. Additionally, the split must be between 1 and n-1, so k must be in [1, n-1].

So the problem reduces to finding the set of k in [1, n-1] that is covered by all the intervals [u, v-1] for each pair (u, v) sorted as u <v.

If there are no similar pairs (m=0), then any split is allowed. So the answer is n-1, but we must subtract the splits that are possible but require non-empty divisions. Wait, no. For m=0, the split can be any k between 1 and n-1. So the answer would be n-1.

But with the constraints from the pairs. So the answer is the number of k in [1, n-1] that lie in all the intervals defined by the pairs.

Wait, but for each pair, the allowed k's are [u, v-1]. So the overall allowed k's are the intersection of all these intervals. So the valid k's must be in the intersection of all these intervals and also in [1, n-1].

So first, compute the intersection of all [u, v-1] intervals. Then, take the intersection with [1, n-1], and count the number of integers in that range.

So how do we compute the intersection of multiple intervals?

The overall allowed k's must satisfy the maximum of all u's and the minimum of all (v-1) for each pair. So the left boundary is the maximum of all u's of the pairs, and the right boundary is the minimum of all (v-1) of the pairs.

But if there are no pairs, then the left boundary is 0 (since all intervals are [u, v-1], but when m=0, the intersection is all possible k's. Wait, no. Wait, when m=0, there are no constraints. So the allowed k's are all in [1, n-1], since all splits are allowed as long as the divisions are non-empty. So the answer is n-1.

So the algorithm is:

If there are no similar pairs, the answer is n-1.

Else:

For all pairs, after sorting u and v (so u <v), compute the interval [u, v-1].

The intersection of all these intervals is [max_u, min (v-1)].

If max_u > min (v-1), then there's no valid k. So the answer is 0.

Otherwise, the number of valid k's is (min_v - max_u + 1).

But also, this interval must be within [1, n-1]. So the final interval is the intersection of [max_u, min_v] and [1, n-1].

Wait, the initial interval is [max_u, min_v], where min_v is the minimum of (v-1) across all pairs.

Wait, for each pair, after sorting, the interval is [u, v-1]. So the left boundary is the maximum of all u's, and the right boundary is the minimum of all (v-1).

So the overall allowed k's are the intersection of all these intervals. So the left is the maximum of all u's and the right is the minimum of (v-1) of all pairs.

So if max_u <= min_v, then the allowed k's are from max_u to min_v, inclusive. Otherwise, no solution.

But also, even if max_u <= min_v, the allowed k's must lie in [1, n-1]. So the actual allowed interval is the overlap between [max_u, min_v] and [1, n-1]. So:

start = max(max_u, 1)

end = min(min_v, n-1)

if start > end: 0

else: end - start +1

So the answer is (end - start +1) if start <= end else 0.

But this is only when m >=1.

Wait, but when m=0, the answer is n-1. So the code would be:

if m ==0:

   return max(0, n-1) (but since n >=2, it's n-1)

else:

   compute max_u and min_v_1 (v-1 for each pair, then min of those)

   start = max(max_u, 1)

   end = min(min_v_1, n-1)

   if start > end:

       answer 0

   else:

       answer end - start +1

But wait, let's test this with the examples.

First example:

Input:

5 2

1 4

5 2

First, for each pair:

Pair (1,4): sorted is u=1, v=4. The interval is [1,3].

Pair (5,2): sorted is u=2, v=5. The interval is [2,4].

So max_u is max(1,2) = 2.

min_v_1 is min(3,4) =3.

So the allowed k's are [2,3].

But n-1 is 4. So end is 3.

So the allowed k's are 2 and 3. So two options.

Which matches the first sample's output of 2.

Yes.

Second example:

3 3

1 2

2 3

1 3

Each pair sorted:

(1,2) → [1,1]

(2,3) → [2,2]

(1,3) → [1,2]

max_u is max(1,2,1) =2.

min_v_1 is min(1,2,2) =1.

So allowed k's are [2,1], which is invalid. So answer is 0.

Which matches sample two.

Third example:

3 2

3 1 → sorted as (1,3) → interval [1,2]

3 2 → sorted as (2,3) → interval [2,2]

So max_u is max(1,2) =2.

min_v_1 is min(2,2) =2.

So allowed k's is [2,2]. n-1 is 2. So start=2, end=2. So 1 way.

Which matches sample three.

So this logic works.

So the steps are:

1. If there are no similar pairs (m=0), then the answer is n-1, but since the split must have non-empty divisions. Wait, when m=0, the split is allowed as any k between 1 and n-1. So the answer is n-1.

But wait, the problem says that the split must have each division non-empty. So the split must have at least one problem in each division. So k can be from 1 to n-1. So yes, the answer is n-1 when m=0.

But when m=0, the answer is n-1, unless n=1, but n >=2 as per constraints.

So code for m=0 is to output n-1.

If m>0:

For each pair, sort u and v, compute u and v-1.

Collect all the u's and compute max_u.

Collect all the (v-1) and compute min_v_1.

Then compute start = max(max_u, 1)

end = min(min_v_1, n-1)

If start > end → answer 0.

Else, answer is end - start +1.

But wait, when there are no pairs (m=0), the allowed k's are all from 1 to n-1. So the answer is n-1.

But in code, m could be 0. So the code needs to handle that.

So now, let's code this.

But first, how to process the m pairs.

We can loop through each pair, sort the two numbers to get u and v, then compute for each pair the interval [u, v-1]. For all such intervals, the allowed k's must be in the intersection of all these.

But instead of storing all intervals, we can track the maximum u and the minimum (v-1) across all pairs.

So for each pair:

read u and v.

if u >v: swap them.

so now u <v.

then, for this pair, the allowed k's are between u and v-1.

So we can track the maximum of all u's, and the minimum of (v-1) for all pairs.

Thus, for all pairs:

max_u = max(max_u, u)

current_v_min = min(current_v_min, v-1)

Once all pairs are processed, compute:

start = max(max_u, 1)

end = min(current_v_min, n-1)

if start > end → 0

else → end - start +1

But what if m is zero? Then, there are no pairs. So answer is n-1.

So code:

n, m = map(int, input().split())

if m ==0:

   print(n-1)

else:

   max_u = 0

   min_v = float('inf')

   for _ in range(m):

       u, v = map(int, input().split())

       if u >v:

           u, v = v, u

       # Now u <v. The allowed interval is [u, v-1]

       max_u = max(max_u, u)

       current_v_min = v-1

       if current_v_min < min_v:

           min_v = current_v_min

   start = max(max_u, 1)

   end = min(min_v, n-1)

   if start > end:

       print(0)

   else:

       print(end - start +1)

But wait, in the case where m is 1, like in the third sample. Let's see.

Yes.

Now, let's test the third sample:

n=3, m=2.

pairs:

3 1 → sorted to 1 and3 → interval [1,2]

3 2 → sorted to 2 and3 → interval [2,2]

max_u is max(1,2) =2.

min_v is min(2, 2) =2.

start = max(2,1) =2.

end = min(2, 3-1=2) →2.

so end - start +1 =1. Correct.

Another test case:

Sample 2:

n=3, m=3.

Pairs:

1 2 → [1,1]

2 3 → [2,2]

1 3 → [1,2]

max_u is max(1,2,1) →2.

min_v is min(1,2,2) →1.

start is max(2,1) →2.

end is min(1,2) →1.

start >end →0. Correct.

So the code seems to handle these cases.

Now, what about when the computed start is 0? For example, if all pairs have u=0 (but u can't be 0 because the problem numbers are 1-based). Wait, u comes from the input pairs which are between 1 and n.

So u is at least 1.

Thus, when m>=1, max_u is at least 1. So start is max(max_u, 1) which is max_u >=1. So start can't be 0.

So for example, if all pairs have u=1, then start is 1.

But what if the min_v is less than 1?

But since in the code, end is the minimum between min_v and n-1. For example, if min_v is 0, then end would be 0. But since start is at least 1, start > end. So answer is zero.

But can min_v be zero?

Only if a pair is (1,1), but the problem says that u and v are different. So each pair (u, v) has u <v, so v-1 >=u >=1. So for each pair, the interval is [u, v-1], where u >=1, v-1 >=u. So for each pair, the interval starts at u >=1 and ends at v-1 >=u >=1. So min_v (the minimum of all (v-1)) is >=1.

Wait, no. For example, consider a pair (1,2). u=1, v=2. v-1=1. So interval is [1,1]. So min_v could be 1.

Another pair (1,3) → v-1=2. So for multiple pairs, the min of (v-1) can be 1 or higher.

So in code, min_v is >=1.

So when m >=1, the min_v is >=1, and start is >=1. So end is min(min_v, n-1) which is >=1 (since min_v >=1 and n-1 >=1 because n>=2).

Wait, but n can be 2. Then n-1=1. So for example, if n=2 and m=1, and the pair is (1,2). Then u=1, v=2. The interval is [1,1]. So max_u is 1, min_v=1. start = max(1,1) →1. end = min(1,1) →1. So answer is 1. Which is correct. Because the split can be k=1, which is allowed.

But according to the code, for n=2, m=1, output is 1. Which is correct.

So code works.

Another edge case: n=2, m=1, pair (1,2). The split k=1: 1 in div2, 2 in div1. Similar pair (1,2) must be in different divisions. So valid. So answer 1.

Another case: n=4, m=2.

Pairs (1,2) and (3,4).

The intervals are [1,1] and [3,3]. So max_u is max(1,3) =3. min_v is min(1,3) =1. So start is max(3,1) →3. end is min(1,3) →1. So 3>1 →0. So answer 0. Because no split k satisfies both pairs.

Which makes sense. For example, split k=3: div2 is 1-3, div1 4. The pair (3,4) would be split (3 in div2, 4 in div1). But the pair (1,2) would be in div2 (k=3 >=1, 2 <=3). So both in div2. So invalid.

So code's answer is 0. Correct.

So code seems to handle all cases.

Thus, the code is as written.

But let me check the code again.

In the code, for each pair, after sorting, u and v are in order. Then, current_v_min is v-1. We check if this is smaller than the current min_v.

Wait, no. Because min_v is the minimum of all (v-1) for all pairs.

For example, for two pairs, one has (v-1) as 5, another 3. So min_v is 3.

So in code, for each pair:

current_v_min = v-1

if current_v_min < min_v:

   min_v = current_v_min

Yes.

So the code is correct.

Thus, the code should work.
</think>

```python
n, m = map(int, input().split())

if m == 0:
    print(n - 1)
else:
    max_u = 0
    min_v = float('inf')
    for _ in range(m):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        max_u = max(max_u, u)
        current_min = v - 1
        if current_min < min_v:
            min_v = current_min
    start = max(max_u, 1)
    end = min(min_v, n - 1)
    print(end - start + 1 if start <= end else 0)
```