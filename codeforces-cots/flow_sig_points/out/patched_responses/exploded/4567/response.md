<think>
Okay, I need to solve this problem where I have to count the number of pairs of monitors that can form a suitable pair. A suitable pair is when two different monitors can be rotated such that their heights are the same. Let's think through this step by step.

First, let's understand the problem. For each monitor, we can choose to rotate it or not. The key is that after rotation (or not), the heights of the two monitors in the pair must be equal. So for each pair of monitors, there must be a way to choose orientations (each monitor can be either in original or rotated) so that their heights are the same.

So for each monitor i, I can represent the possible heights it can contribute. For example, for a monitor with dimensions w and h, its possible heights are the minimum of w and h. Wait, no. Wait, when we rotate a monitor, the height becomes either h or w, depending on how we rotate. Wait, no. The monitor can be placed in either orientation. So for each monitor, the possible height after rotation is the minimum of the two dimensions? Or is it that we can choose either orientation, so the height can be either h_i or w_i. Because rotating the monitor swaps width and height. So the monitor can be placed with height h_i (original) or height w_i (rotated). So for each monitor, there are two possible heights it can have. But the user can choose either of them for each monitor in the pair. So for two monitors, their heights (after possible rotation) must be the same.

So the problem reduces to: for each pair of monitors, check if there exists a height h such that h is either the original or rotated height of the first monitor, and also the original or rotated height of the second monitor.

Wait, no. Wait, for each monitor, when considering a pair, we can choose to rotate either of them. So the pair is suitable if there exists a way to rotate each of the two monitors such that their heights are equal. So the possible heights for monitor i are h_i and w_i. So the possible combinations are:

For monitor 1: h1 or w1 (after rotation)
For monitor 2: h2 or w2 (after rotation)
We need to check if there's any intersection between the two possible heights of each. Because if there's a common height between the two, then the pair is suitable.

Wait, no. Because if monitor 1 can have height A or B, and monitor 2 can have height C or D. The pair is suitable if at least one of A, B is equal to one of C or D. So the pair is suitable if the set {h1, w1} and {h2, w2} have a non-empty intersection. Because if there's a common value, then we can choose the rotations such that both monitors have that height.

Wait, that's correct. Because for monitor 1, you can choose to use either h1 or w1 as the height. Similarly for monitor 2. So if the two monitors' possible heights (the two options) have any common element, then the pair is suitable.

So the problem becomes: count the number of unordered pairs (i,j) where i < j, and the intersection of {h_i, w_i} and {h_j, w_j} is non-empty.

So how do I compute this efficiently?

The straightforward approach is to group the monitors by their possible heights. For each possible height value, count how many monitors have that value in their possible heights (either h_i or w_i). Then, for all pairs of monitors that share at least one common height, sum their combinations. But wait, this might overcount because a single pair could share multiple common heights. So we need to avoid counting the same pair multiple times.

Wait, no. Because the pair is counted once if there's at least one common height. So the problem is to count all pairs (i,j) where the two monitors have overlapping possible heights. To compute this, perhaps we can use inclusion-exclusion. But for n up to 1e5, the O(n^2) approach is impossible. So we need a smarter way.

Alternative approach: for each monitor, collect the set of possible heights (h_i, w_i), then for all pairs of monitors, check if their sets have a non-empty intersection. But checking all pairs is O(n^2), which is 1e10 operations—way too slow.

Therefore, we need a way to compute the total number of pairs where the two monitors share at least one common height. Let's model this as follows: each monitor contributes to the count for each of its two possible heights. Then, for each height h, the number of pairs that can form with h as the common height is (count[h] choose 2). But if two monitors share multiple heights, then they would be counted in multiple counts. So summing (count[h] choose 2) over all h will overcount the pairs. So the inclusion-exclusion principle comes into play here.

For example, if two monitors share two common heights (h1 and h2), then they would be counted once in h1's sum and once in h2's sum. So the total sum would be higher than the actual number of pairs.

Therefore, the correct approach is to find the total number of pairs that share at least one common height, but the sum over all h of (count[h] choose 2) counts each pair as many times as the number of common heights between them. So the sum is not the answer we need.

So we need to compute the union of all pairs that share at least one common height, but how?

An alternative idea: the total number of pairs is C(n,2) minus the number of pairs that have no common heights. So if we can compute the number of pairs that have no overlapping possible heights, then subtract that from the total pairs.

But how to compute the number of such pairs?

Each pair that does not have any common possible heights contributes to the total. So the problem reduces to calculating how many pairs (i,j) where {h_i, w_i} ∩ {h_j, w_j} = empty.

So the total answer is total_pairs - non_overlapping_pairs.

This might be easier. Because calculating non_overlapping_pairs requires checking for each pair whether their possible heights are disjoint.

But again, how to compute this efficiently.

Alternatively, think of each monitor as having a set S_i = {a, b}, where a and b are h_i and w_i. We need to count the number of pairs (i,j) where S_i ∩ S_j is not empty.

Let me think of all possible pairs. Let's represent each monitor's set as a sorted pair. For example, for a monitor with h=3 and w=2, the set is {2,3}. For a square, it's {5,5} → {5}.

But in the problem, when a monitor's h and w are the same, the set {h, w} is just a singleton. So for such a monitor, the possible heights can only be that value, so when paired with another monitor, if the other monitor's possible heights include that value, the pair is counted.

So the key is to model each monitor's possible heights as the set {min(h_i, w_i), max(h_i, w_i)}, but perhaps sorted. Wait, no. Because h_i and w_i can be in any order when rotated. But when considering the possible heights, the actual order doesn't matter. For example, a monitor with (h=5, w=3) can be rotated to have height 3 or 5. So the set is {3,5}. The same as if h=3 and w=5.

So perhaps, for each monitor, we can represent the possible heights as a sorted tuple (a, b) where a <= b. Then, the possible heights are a and b. But even if a == b, it's the same as a singleton.

So for each monitor, the possible heights are {a, b}, where a = min(w_i, h_i), b = max(w_i, h_i). So the set is {a, b}, which may have 1 or 2 elements.

Now, the problem is to count the number of pairs (i,j) where the sets {a_i, b_i} and {a_j, b_j} have at least one common element.

So how can we compute this?

Let's think in terms of the frequency of each possible value. For example, if we have a frequency map that counts how many monitors have x in their possible heights (either as a_i or b_i), then for each x, the number of monitors that can form a pair with x as the common height is C(cnt[x], 2), but again, this counts pairs multiple times if they share multiple heights.

But this approach would overcount. For example, if two monitors share both x and y as possible heights, they would be counted once in x's count and once in y's count, leading to an overcount.

So the sum of C(cnt[x], 2) for all x is greater than or equal to the actual answer, but the actual answer is the number of pairs that share at least one common height.

Therefore, we need to find a way to compute this without overcounting.

Alternative approach: Let’s group the monitors based on their possible height sets.

Each monitor has a sorted pair (a, b) where a <= b.

We can represent each monitor as a pair (a, b), and then for each such pair, compute the number of pairs that have overlapping sets.

But this seems challenging.

Alternatively, the inclusion-exclusion approach can be used.

The total number of pairs is C(n, 2). The number of pairs that do not share any common heights is equal to the total pairs minus the answer. So if we can compute the number of pairs that have no common heights, then the answer is total_pairs - non_overlapping_pairs.

So how to compute non_overlapping_pairs.

For two monitors i and j, their possible height sets are S_i and S_j. They have no common elements if S_i ∩ S_j is empty.

So S_i could be a singleton or a pair, and similarly for S_j.

So for each monitor i, how many monitors j (j > i) have S_j ∩ S_i = empty.

If we can compute this for all i, then summing over all i and dividing by 2 (since each pair is considered once) would give the non_overlapping_pairs count.

But again, for n up to 1e5, this approach is O(n^2) which is not feasible.

So we need a smarter way to compute the number of pairs that have no overlapping elements.

Let’s think of each monitor's possible heights as a set S_i. So for two monitors i and j, their S_i and S_j must be disjoint.

We need to count all pairs (i,j) where S_i and S_j are disjoint.

Hmm. How to compute this.

Alternative idea: For each monitor, collect the elements in S_i. Then, the number of monitors that have no elements in common with S_i is equal to the total number of monitors minus the number of monitors that have at least one element in S_i.

But again, for each i, this is O(1) with some pre-processing, but how.

Another approach: build a frequency map for each possible value. Then, for each monitor i, compute the sum over x in S_i of the frequency of x. Then, subtract the overlaps (like if two elements in S_i are in the same S_j, etc.), but this seems complicated.

Wait, maybe for a monitor i with S_i = {x, y}, the number of monitors j where S_j and S_i share at least one element is (cnt[x] + cnt[y] - cnt_xy), where cnt_xy is the number of monitors that have both x and y in their S_j. But this might not be correct.

Alternatively, the inclusion-exclusion principle: the number of monitors j that have x or y in their S_j is (cnt[x] + cnt[y] - cnt_both), where cnt_both is the number of monitors that have both x and y in their S_j. But how to compute cnt_both.

Wait, cnt_both is the number of monitors j where x is in S_j and y is in S_j. So for example, monitors that have S_j containing both x and y. For example, if a monitor's S_j is {x, y} (i.e., a <= x <= y <= b?), no, wait S_j is {a_j, b_j}, sorted. So a monitor j has x and y in S_j only if x is a_j and y is b_j, or x and y are both present.

Wait, for S_j to contain x and y, x and y must be the elements of S_j. So S_j can be a singleton {x} (if x = y) or a pair {x, y} (if x < y), but if x and y are the same, then S_j is a singleton. So for S_j to contain both x and y, x and y must be in S_j. So for example, if x and y are the same, then S_j must be {x}. If x and y are different, then S_j must be {x, y}.

Wait, no. Because S_j is the set {a_j, b_j}, where a_j is the min and b_j is the max. So if a_j and b_j are x and y (in any order), but S_j is sorted. So for example, if S_j is {x, y}, then x <= y, and the monitor's original dimensions could be x and y (so possible to rotate to either x or y as height). So if S_j is {x, y}, then the possible heights are x and y.

So for a monitor j to have both x and y in S_j, S_j must be exactly {x, y} (if x != y) or {x} (if x == y).

So, for a given x and y (sorted), the number of monitors j where S_j contains both x and y is equal to the number of monitors where a_j = x and b_j = y (if x < y) or a_j = x (if x == y).

So to compute cnt_both(x, y), which is the number of monitors j with S_j containing both x and y, we can have a dictionary that maps each (a, b) pair to the count of monitors with that (a, b) pair.

For example, when x and y are the same (x == y), then cnt_both(x, y) is the count of monitors where a_j = x and b_j = x (i.e., S_j is {x}).

When x < y, then cnt_both(x, y) is the count of monitors where a_j = x and b_j = y (i.e., S_j is {x, y}).

So, if for each monitor i, which has S_i = {x, y}, then the number of monitors j that have S_j overlapping with S_i is the sum of cnt[x] + cnt[y] - cnt_both(x, y). Because cnt[x] includes all monitors that have x in their S_j (either as a singleton or part of a pair), and similarly for cnt[y]. But monitors that have both x and y in S_j (i.e., their S_j is {x, y}) are counted in both cnt[x] and cnt[y], so we subtract them once to avoid double-counting.

Wait, let's think: For a monitor j that has S_j = {x, y}, where x < y. Then, in cnt[x], it is included, and in cnt[y], it is included. So when we compute cnt[x] + cnt[y], this monitor is counted twice. So to get the correct number of unique monitors that have either x or y in their S_j, we need to subtract the number of monitors that have both x and y in S_j, which is cnt_both(x, y).

So, the number of monitors j that share at least one element with S_i is (cnt[x] + cnt[y] - cnt_both(x, y)). Then, subtract 1 if the monitor i itself has x or y in S_j (since j must be different from i). Wait, because we are looking for j != i.

So, for each monitor i, the number of monitors j (j != i) that share at least one element with S_i is (cnt[x] + cnt[y] - cnt_both(x, y)) - 1 (if S_i has x and y, which could be the same or different). Wait, because in the sum (cnt[x] + cnt[y] - cnt_both(x, y)) includes the current monitor i if x is in S_i or y is in S_i. So we need to subtract 1 to exclude the current monitor i from the count.

So for each monitor i, the number of j's that can form a pair with i (sharing at least one element) is (sum_of_relevant_counts) - 1. Then, the total number of such pairs is the sum over all monitors i of this count, divided by 2 (since each pair is counted twice). But this approach would have O(n) time, but requires maintaining the counts and the (a_j, b_j) pairs.

Alternatively, the total number of pairs that share at least one element is equal to the sum for all x in all possible heights of C(cnt[x], 2) minus the sum for all (x, y) where x < y of C(cnt_both(x,y), 2), plus the sum for all x of C(cnt_singleton[x], 2). Wait, I'm not sure.

Alternatively, another way to approach this:

Total pairs that share at least one element = sum over x (C(cnt[x], 2)) - sum over x < y (C(cnt_both(x,y), 2)).

Because when you sum C(cnt[x], 2) for each x, you count all pairs that share x. But if two monitors j and k have S_j = {x, y} and S_k = {x, y}, then they are counted in C(cnt[x], 2) and C(cnt[y], 2), so they are counted twice. So we need to subtract the pairs that were counted more than once.

But how to model this.

Alternatively, the total number of pairs is sum_x C(cnt[x], 2) - sum_{x < y} C(cnt_both(x,y), 2).

Because for a pair that shares both x and y (i.e., their S_j and S_k have x and y in common), they are counted in both x and y, so they are subtracted once in the sum over x < y.

But I'm not sure. Let's take an example.

Suppose two monitors j and k, both with S_j = S_k = {x, y}. Then, their pair is counted once in x's C(cnt[x], 2) and once in y's C(cnt[y], 2). So the sum_x C(...) counts them twice. So we need to subtract 1 (since the actual count should be 1). But how?

So, the formula would be:

Total_pairs = sum_x C(cnt[x], 2) - sum_{x < y} C(cnt_both(x, y), 2).

Because for each pair (j,k) that share both x and y, they are counted in two terms (x and y) and thus contribute 2 to the first sum. But they should only be counted once. So the correction term subtracts C(cnt_both(x,y), 2) for each pair x < y. Because for those pairs (j,k) that share both x and y, they are counted twice in the first sum and subtracted once in the second sum, resulting in a net count of 1.

But is this correct?

Let's take another example. Suppose all monitors have S_i = {x, y}, and there are m such monitors. Then:

sum_x C(cnt[x], 2) would be C(m, 2) (for x) + C(m, 2) (for y) → total 2*C(m,2).

sum_{x < y} C(cnt_both(x,y), 2) is C(m,2).

Thus, Total_pairs = 2*C(m,2) - C(m,2) = C(m,2), which is correct.

Yes, because each pair is counted once. So that formula works.

Another example: a pair of monitors that share x but not y. Then they are counted once in the x's term. The formula works.

So the correct total is sum_x C(cnt[x], 2) minus the sum of C(cnt_both(x, y), 2) for all x < y.

So how to compute this?

We need to:

1. For each monitor, compute a = min(w_i, h_i), b = max(w_i, h_i). So S_i is {a, b}.

2. For all a and b, we track:

   a. cnt[x] → the number of monitors that have x in their S_i (either as a or b).

   b. For pairs (a, b), track how many monitors have exactly (a, b) as their S_i. Let's call this a dictionary pair_counts, where the key is (a, b) and the value is the count.

Then, sum_x C(cnt[x], 2) is straightforward.

Then, sum over all pairs (a, b) where a < b, of C(pair_counts[(a, b)], 2). Because these pairs contribute to both a and b, so we need to subtract these.

Wait, the sum_{x < y} C(cnt_both(x,y), 2) is equal to sum over all (x, y) pairs where x < y of C(k, 2), where k is the number of monitors with S_i = {x, y}.

Because for each such monitor pair (x, y), their pair is counted in both cnt[x] and cnt[y], and thus the sum_x C(cnt[x], 2) counts these pairs twice. So by subtracting C(k, 2) for each such (x, y) pair where x < y, we correct for that double-counting.

So the formula is:

answer = sum_x C(cnt[x], 2) - sum_{(a,b) where a < b} C(pair_counts[(a,b)], 2)

Yes! Because for each (a, b) pair (a < b) that appears in some monitors, the number of pairs between those monitors is C(k, 2), which was counted twice in the first sum (once for a, once for b). So subtracting C(k, 2) for each such (a,b) pair removes the duplicate counts.

So the algorithm is:

- For each monitor, compute a = min(w_i, h_i), b = max(w_i, h_i).

- Update cnt[x] for x = a and x = b (increment by 1 each).

- Update pair_counts[(a, b)] by 1.

Then, compute:

sum_x (cnt[x] * (cnt[x] - 1) // 2) 

minus 

sum_{(a, b) in pair_counts where a < b} (pair_counts[(a,b)] * (pair_counts[(a,b)] - 1) // 2)

That gives the answer.

Yes! That makes sense.

Let's test this approach against the examples.

First example:

Input:
5
3 2 → a=2, b=3. So cnt[2] +=1, cnt[3] +=1. pair_counts[(2,3)] +=1
2 2 → a=2, b=2. cnt[2] +=2? Wait, because for a=2 and b=2, S_i is {2}. So for x =2, cnt[2] increases by 1. Because the possible heights are {2, 2} → {2}. So a = min(2,2) =2, b =2.

So for this monitor, a=2, b=2. So in pair_counts, (2, 2) is a key. So in pair_counts[(2,2)] +=1.

Then, the next monitors:

5 5 → a=5, b=5. So pair_counts[(5,5)] +=1. cnt[5] +=1 (since S_i is {5}).

3 5 → a=3, b=5. So cnt[3] +=1, cnt[5] +=1. pair_counts[(3,5)] +=1.

4 3 → a=3, b=4. cnt[3] +=1, cnt[4] +=1. pair_counts[(3,4)] +=1.

So after processing all monitors:

pair_counts:
(2,3): 1 → a=2 < b=3 → in the sum for a < b.

(2,2):1 → a =b, not included in the sum.

(5,5):1 → not included.

(3,5):1 → included.

(3,4):1 → included.

cnt:

2: 2 (from first monitor (2,3) and the second (2,2) → cnt[2] is incremented twice? Wait, no. Let's see:

For first monitor (2,3):

a=2, b=3. So cnt[2] +=1, cnt[3] +=1.

Second monitor (2,2): a=2, b=2. So cnt[2] +=1 (since a and b are 2, so the possible heights are {2}, so for this monitor, in the cnt[x], we add 1 for x=2.

So cnt[2] after second monitor is 1+1=2.

Third monitor (5,5): a=5, b=5. cnt[5] +=1.

Fourth monitor (3,5): a=3, b=5. cnt[3] +=1, cnt[5] +=1.

Fifth monitor (4,3): a=3, b=4. So cnt[3] +=1, cnt[4] +=1.

So the cnt map is:

2:2 (from first and second monitor)

3: 1 (first) +1 (fourth) +1 (fifth) → total 3.

5:1 (third) +1 (fourth) → 2.

4:1 (fifth) → 1.

So sum_x C(cnt[x], 2) is:

C(2,2) → 1 (x=2)

C(3,2) → 3 (x=3)

C(5,2) → 1 (x=5)

C(4,2) → 0 (x=4)

Others (like 3, 4, etc.) have cnt[x] <2.

Sum is 1 +3 +1 =5.

Now, subtract the sum over pairs (a, b) where a < b:

The pairs are (2,3), (3,5), (3,4).

Each has pair_counts of 1.

So each contributes C(1,2) =0.

So the total is 5 -0 =5, which matches the first example's output.

Yes! So the approach works.

Another example: the second input.

7 monitors:

All pairs (10,10), (10,20), (20,10), (10,20), (10,20), (10,10), (20,10).

Let's process each:

First monitor: (10,10) → a=10, b=10 → cnt[10] +=1. pair_counts[(10,10)] +=1.

Second monitor: (10,20) → a=10, b=20 → cnt[10] +=1, cnt[20] +=1. pair_counts[(10,20)] +=1.

Third: (20,10) → same as (10,20). So a=10, b=20. So same as second monitor. So cnt[10] +=1 (now 3), cnt[20] +=1 (now 2). pair_counts[(10,20)] increases by 1 (now 2).

Wait, no. Third monitor's a and b are 10 and 20. So pair_counts[(10,20)] increments by 1 → becomes 2.

Fourth: (10,20) → same as before → pair_counts[(10,20)] becomes 3.

Fifth: (10,20) → pair_counts[(10,20)] becomes 4.

Sixth: (10,10) → pair_counts[(10,10)] becomes 2.

Seventh: (20,10) → same as (10,20). So pair_counts[(10,20)] becomes 5.

So after processing all:

pair_counts:

(10,10):2

(10,20):5 (since third, fourth, fifth, seventh monitors contribute here).

Other pairs?

No others.

So sum_x C(cnt[x], 2):

Let's compute cnt for each x.

For x=10:

Each monitor contributes to cnt[10] as follows:

- (10,10) → adds 1 per monitor. There are 2 such monitors → 2.

- (10,20) → each adds 1 to 10. There are 5 monitors → 5.

So cnt[10] =2+5=7.

For x=20:

Each (10,20) monitor adds 1. 5 monitors → cnt[20] =5.

Also, any other monitors?

No. Other monitors are (10,10) → their S_i is {10}, so x=10.

So cnt[20] is 5.

So sum_x C(cnt[x], 2) is C(7,2) + C(5, 2) =21 +10=31.

Now subtract sum over (a,b) a < b of C(pair_counts[(a,b)], 2).

Only (10,20) is a pair with a < b. pair_counts[(10,20)] is5. So C(5,2) =10.

So total is 31 -10=21, which matches the example.

Yes! So this approach works.

Therefore, the algorithm is:

- For each monitor, compute a = min(w, h), b = max(w, h).

- Update cnt[a] and cnt[b] (increment each by 1).

- Update the pair_counts dictionary for (a, b) (increment by 1).

- After processing all monitors, compute the sum over x of C(cnt[x], 2).

- Subtract the sum over all (a, b) with a < b of C(pair_counts[(a, b)], 2).

So the code can be written as follows.

Now, considering the constraints: n up to 1e5. So we need an O(n) solution.

In Python, using a defaultdict for cnt and a normal dict for pair_counts.

But for 1e5 elements, the code needs to be efficient.

But in Python, using a Counter or defaultdict is manageable.

Now, code steps:

Read n.

Initialize cnt as a defaultdict(int).

Initialize pair_counts as a defaultdict(int).

For each of the n lines:

   read w and h.

   a = min(w, h)

   b = max(w, h)

   cnt[a] +=1

   if a != b:

       cnt[b] +=1

   pair_key = (a, b)

   pair_counts[pair_key] +=1

Wait, but for a pair (a, b) where a == b, we need to count it in pair_counts, but when a == b, the pair_counts key is (a, a), but in the subtraction step, we only subtract pairs where a < b.

So when a == b, the pair is not considered in the subtraction sum.

Thus, in code:

sum1 = sum( c * (c-1) // 2 for c in cnt.values() )

sum2 = 0

for (a, b), count in pair_counts.items():

   if a < b:

       sum2 += count * (count -1) // 2

answer = sum1 - sum2

So the code is:

Read n.

Process each monitor into a and b.

Update cnt and pair_counts.

Compute sum1 and sum2.

Return sum1 - sum2.

Yes.

Now, testing edge cases.

Case where a monitor is (5,5). Then a =5, b=5. So pair_counts[(5,5)] +=1. cnt[5] +=1.

In sum1, this will contribute to C(1, 2) which is 0.

If there are two such monitors, then cnt[5] is 2. sum1 will have C(2,2) =1. sum2 is 0. So answer is 1, which is correct. Because two monitors with same (5,5) can form a pair (since their possible heights are 5, so they share the same height).

Another case: two monitors (2,3) and (3,2). Both are processed as (2,3). So pair_counts[(2,3)] is 2. sum1 will have cnt[2] =2, cnt[3] =2. So sum1 is C(2,2) + C(2,2) =1+1=2. sum2 is C(2,2) =1. So answer is 2-1=1. Which is correct.

Thus, the code works.

Now, implement this.

In Python:

We can use collections.defaultdict for cnt and pair_counts.

But since the numbers can be up to 1e9, but the number of entries in cnt is manageable (since each monitor contributes up to two entries, but for n=1e5, cnt can have up to 2e5 entries).

The code would look like:

Read n.

Testing against sample input 1.

```python
from collections import defaultdict


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    cnt = defaultdict(int)
    pair_counts = defaultdict(int)

    for _ in range(n):
        w, h = map(int, input_stream.readline().rstrip("\n").split())
        a = min(w, h)
        b = max(w, h)
        cnt[a] += 1
        if a != b:
            cnt[b] += 1
        pair_counts[(a, b)] += 1

    sum1 = 0
    for c in cnt.values():
        sum1 += c * (c-1) // 2

    sum2 = 0
    for (a, b), count in pair_counts.items():
        if a < b:
            sum2 += count * (count -1) // 2

    print(sum1 - sum2, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7
10 10
10 20
20 10
10 20
10 20
10 10
20 10
""",
            "output": \
"""\
21
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

Sample input 2:

7

The code correctly computes sum1 as 21+10=31, sum2=10, so 21.

So the code is correct.
</think>

```python
from collections import defaultdict

n = int(input())
cnt = defaultdict(int)
pair_counts = defaultdict(int)

for _ in range(n):
    w, h = map(int, input().split())
    a = min(w, h)
    b = max(w, h)
    cnt[a] += 1
    if a != b:
        cnt[b] += 1
    pair_counts[(a, b)] += 1

sum1 = 0
for c in cnt.values():
    sum1 += c * (c - 1) // 2

sum2 = 0
for (a, b), count in pair_counts.items():
    if a < b:
        sum2 += count * (count - 1) // 2

print(sum1 - sum2)
```
