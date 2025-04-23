<think>
Okay, let's try to solve this problem. Hmm. The problem is about calculating f(p_i(n)) for each i from 1 to n. Each p_i is a permutation where the first element is i, followed by 1, 2, ..., i-1, then i+1, ..., n. So for each permutation, we need to compute the sum of absolute differences between consecutive elements in the array x, based on their positions in the permutation.

The key challenge here is handling the large constraints—n and m up to 2e5. So any O(nm) solution is definitely out of the question. We need an O(m + n) approach or something similar.

First, let's understand how the positions of elements in the permutation p_i work. Let's think about the position of a value v in p_i(n).

For a permutation p_i, the position of i is 1. For other elements, if v < i, then in p_i, the position of v is v+1 (since the first element is i, followed by 1, 2, ..., i-1. Wait, wait. Wait, the permutation is [i, 1, 2, ..., i-1, i+1, ..., n]. So the positions are:

- The first position is i.
- Then positions 2 to i are 1, 2, ..., i-1.
- Positions i+1 to n are i+1, i+2, ..., n.

Wait, no. Let's see for p_i(n). For example, p_3(4) is [3,1,2,4]. So for elements:

- 3 is in position 1.
- 1 is in position 2.
- 2 is in position 3.
- 4 is in position 4.

Wait, but in the example given for p_3(4), the positions for elements 1,2,3,4 are:

pos(p_3(4),3) is 1.

pos(p_3(4),1) is 2.

pos(p_3(4),2) is 3.

pos(p_3(4),4) is 4.

So, generalizing, for p_i(n):

- The position of i is 1.

For any other element v:

- if v < i: its position is v + 1. Because after i comes 1, then 2, ..., up to i-1. So 1 is in position 2, 2 is in position 3, etc. Wait, no. Wait, in p_i(n), the elements after i are [1, 2, ..., i-1, i+1, ..., n]. So the first position is i.

The second element is 1, third is 2, ..., i-th element is i-1. Then, the (i+1)-th element is i+1, up to n. So for v not equal to i:

if v < i: the position of v is v + 1? Let's see:

In p_3(4), 1 is position 2, 2 is position 3. So for v=1 <3: 1+1=2, yes. For v=2 <3: 2+1=3. Correct.

For v=4 (which is >3), the position is 4. Because after the first element (3), the next elements are 1, 2 (positions 2 and 3), then comes 4 as the fourth element.

Wait, but for p_3(4), the elements are [3,1,2,4]. So 4 is in position 4, which is i+1 (3+1=4). But for i=3 and v=4 which is greater than i, the position is v (since after the first i elements, the rest are i+1, i+2, ..., n. So for v>i, their position is v, because they are placed starting from position i+1. Wait, no.

Wait, let's take i=4 and n=4. p_4(4) is [4,1,2,3]. So for v=1, position is 2; v=2 is 3; v=3 is 4. For v=4, position is 1.

So, the general formula for pos(p_i, v) is:

if v == i: 1.

else if v < i: v + 1.

else (v > i): v.

Wait, let's check that.

Take i=2, n=4. p_2(4) is [2,1,3,4]. So:

pos(2) is 1.

pos(1) is 2 (which is 1+1=2).

pos(3) is 3 (which is 3, which is v>i (2), so 3 remains 3. Correct.

pos(4) is 4 (v>i, so 4. Correct.

Yes. So the position of v in p_i is:

pos(v) = 1, if v ==i.

Else, if v <i: pos(v) = v+1.

Else (v>i): pos(v) = v.

So, for each i, when we process the x array, we need to compute the sum over consecutive elements of the absolute difference between their positions in p_i.

Now, the problem is that for each i from 1 to n, compute this sum. But with n up to 2e5, and m up to 2e5, we need an O(n + m) solution.

So the straightforward approach of iterating each i and then each pair in x is O(nm), which is 4e10 operations. That's way too slow.

We need a smarter way.

Let's think about the contribution of each consecutive pair (x_j, x_{j+1}) to the sum for each i. For each such pair, we can compute how their absolute difference in positions varies with i, and then for each i, sum all these contributions.

So, for each pair (a, b) in x (there are m-1 such pairs), compute for each i the value of |pos(a in p_i) - pos(b in p_i)|, and then sum all these for each i.

The question is: how can we efficiently compute, for each i, the sum of |pos(a) - pos(b)| for all consecutive pairs (a, b) in x.

Let's break down the problem into considering each pair (a, b) and determining how much it contributes to each i's total sum.

For a single pair (a, b), we can model how their positions' difference varies with i, and then compute the contribution to each i.

So, for each (a, b), compute for all i in 1..n, the |pos_a(i) - pos_b(i)|, then sum over all pairs.

So, for each (a, b), we need to calculate a function that gives |pos_a(i) - pos_b(i)| for all i, and then accumulate that into the sum for each i.

The key is to find, for each (a, b), how the absolute difference depends on i, and then compute the contribution to each i efficiently.

Let's consider all possible cases for a and b.

Case 1: a == b.

In this case, pos_a and pos_b are the same, so the difference is 0. So the contribution to all i is 0. So these pairs can be ignored.

Case 2: a != b.

We need to compute |pos_a(i) - pos_b(i)| for each i.

Let's model pos_a(i) and pos_b(i) as functions of i.

Remember:

pos_a(i) = 1 if a == i, else (a < i) ? (a + 1) : a.

Similarly for pos_b(i).

So, for a given i, the positions of a and b depend on whether a and/or b are equal to i, and their relation to i (less than or greater than).

But handling this for all possible i, a, b seems complex. Let's try to find a way to model the difference for each pair (a, b) across all i.

Let's think for a specific pair (a, b). Let's assume a and b are fixed, and we need to compute the contribution for each i in 1..n.

We can break this into different scenarios based on the value of i relative to a and b.

First, note that the position of a in p_i is:

pos_a(i) = 1 if i == a.

Else if a < i: pos_a(i) = a + 1.

Else (a > i): pos_a(i) = a.

Similarly for pos_b(i).

So the difference between pos_a(i) and pos_b(i) depends on whether i is a, b, or neither, and the relative sizes of a and b with i.

This seems complicated, but perhaps we can model it by considering different ranges of i.

Let's consider all possible values of i and see how the positions of a and b are determined.

Let's consider the different intervals of i:

1. i < min(a, b)
2. i = a
3. i = b
4. a < i < b (if a < b)
5. b < i < a (if b < a)
6. i > max(a, b)

Wait, but a and b could be in any order. Let's suppose that a and b are fixed. Let's consider all possible i in [1, n], and for each i, compute the difference between pos_a(i) and pos_b(i).

Alternatively, perhaps we can split the analysis into several cases based on the relation between i and a, b.

Another approach: for a given i, the positions of a and b can be in one of several possible states. Let's model the possible combinations.

But this might get too complicated. Let's think of the possible scenarios for a pair (a, b):

Case A: i = a

In this case, pos_a(i) = 1.

pos_b(i) is:

if b == a → 1 (but a != b, so this is not possible).

if b < a → pos_b(i) = b + 1 (since i = a, and b < a).

if b > a → pos_b(i) = b (since i = a < b, so pos_b(i) = b).

So difference is |1 - (b +1)| if b < a, else |1 - b|.

Case B: i = b

pos_b(i) = 1.

pos_a(i):

if a < b → pos_a(i) = a + 1.

if a > b → pos_a(i) = a.

So difference is |(a +1) - 1| = a if a < b, else |a - 1|.

Case C: i is neither a nor b.

In this case, i can be in different ranges relative to a and b.

Let me see.

For i not equal to a or b, then:

pos_a(i) = if a < i → a + 1, else a.

pos_b(i) = if b < i → b + 1, else b.

So the difference between these two depends on how a and b compare to i.

But this is getting complex. Maybe there's a way to model the difference for all i except a and b.

Alternatively, perhaps for each pair (a, b), we can compute the contribution for i = a and i = b separately, and then handle the general case where i is not a or b.

Let's proceed step by step.

For a pair (a, b), the contribution to i is:

if i == a: compute |1 - pos_b(i)|.

if i == b: compute |pos_a(i) - 1|.

Else, for i not a or b:

compute |pos_a(i) - pos_b(i)|, which depends on a, b, and i.

But for the general case where i is not a or b, let's model pos_a and pos_b.

pos_a(i) is:

if a < i → a + 1.

else → a.

Similarly for pos_b(i).

So for i < min(a, b):

pos_a(i) = a (since a > i? No, wait, if i is less than a, then a > i, so pos_a(i) = a.

Wait, no. Wait, the condition is:

pos_a(i) is 1 if i == a.

Else, if a < i → pos_a(i) = a + 1.

Else (a > i) → pos_a(i) = a.

Wait, this is incorrect. Let's correct this.

Wait, when i is not a:

if a < i → pos_a(i) = a + 1.

if a > i → pos_a(i) = a.

Because in permutation p_i, the elements less than i are arranged as 1, 2, ..., i-1 in positions 2 to i. So for example, in p_i, if a is less than i, then a is in position a + 1. If a is greater than i, then a is in position a (since the elements after i are arranged as i+1, i+2, ..., n in their own positions.

So, for i != a:

pos_a(i) = a + 1 if a < i.

pos_a(i) = a if a > i.

Similarly for pos_b(i).

So, for i not a and not b, the positions are:

pos_a(i) = a if i < a, a+1 if i > a.

pos_b(i) = b if i < b, b+1 if i > b.

So the difference between pos_a and pos_b depends on the relation between i and a and b.

But how?

Let's consider different scenarios.

Scenario 1: i < min(a, b).

In this case, pos_a(i) = a, pos_b(i) = b. So the difference is |a - b|.

Scenario 2: i is between a and b.

Assume a < b. Then i can be in (a, b), or (b, a) if b < a.

Wait, perhaps splitting into a < b and a > b.

Let's first assume a < b.

Case a < b:

Then, for i < a: both a and b are greater than i. So pos_a = a, pos_b = b. Difference |a - b|.

For a < i < b:

pos_a is a+1 (since i > a), pos_b is b (since i < b). So difference is |(a+1) - b|.

For i > b:

pos_a is a+1, pos_b is b+1. Difference is |(a+1) - (b+1)| = |a - b|.

For i = a: contribution as discussed earlier.

For i = b: contribution as discussed.

If a > b:

For i < b: pos_a = a, pos_b = b. Difference |a - b|.

For b < i < a: pos_a = a (since i < a), pos_b = b+1 (since i > b). Difference |a - (b+1)|.

For i > a: pos_a = a+1, pos_b = b+1. Difference |(a+1) - (b+1)| = |a - b|.

So in general, the difference can be split into several intervals.

So for a pair (a, b), the contribution to i is:

If i is not a or b:

For i < min(a, b): |a - b|.

For i between min(a, b) and max(a, b): depends on which is a or b.

For i > max(a, b): |a - b|.

But this is not considering when a and b are equal, but we already handled that case (contribution 0).

So, the key idea is that for a pair (a, b) where a != b, the contribution for i not equal to a or b can be broken into three intervals:

1. i < min(a, b): contribution is |a - b|.

2. i in (min(a, b), max(a, b)): contribution is |(a+1) - b| if a < b, but wait, no. Let's re-examine.

Wait, for a < b:

When i is between a and b (a < i < b):

pos_a(i) is a+1 (since i > a).

pos_b(i) is b (since i < b).

So difference is | (a+1) - b |.

For a > b:

When i is between b and a (b < i < a):

pos_a(i) is a (since i < a).

pos_b(i) is b+1 (since i > b).

So difference is |a - (b+1)|.

Which is the same as | (a - b) - 1 |.

In either case, when i is between min(a,b) and max(a,b), the contribution is | (a - b) - (if a < b then (a < i < b) would contribute (a+1 - b) ) |.

Hmm. Let's see:

If a < b:

For i between a and b:

contribution is |a+1 - b| = | (a - b) + 1 | = (b - a) - 1, since a < b.

Wait, a+1 - b is (a - b) + 1. So if a < b, then a+1 could be <= b or not. Wait, if a < b and i is in (a, b), then i can be up to b-1. So a+1 could be as small as a+1 (when i is a+1) and up to b-1. For example, a=2, b=5, i can be 3,4, which are between a and b. Then pos_a(i) is 2+1=3, pos_b is 5. So difference is 5-3=2. Which is (5-2) -1 = 2. So in this case, the contribution is (b - a) - 1.

Similarly, if a > b, then for i between b and a:

contribution is a - (b+1) = (a - b) -1. Which is the same as |(a - (b+1))| = (a - b -1) since a > b.

So in both cases, when i is between the two, the contribution is |a - b| -1. But wait, no. Wait, if a < b and the contribution is (b - (a+1)) = (b - a -1), which is |a - b| -1. Similarly, if a > b, the contribution is (a - (b+1)) = (a -b -1) which is |a -b| -1.

So for the interval between min(a,b) and max(a,b), the contribution is |a -b| -1.

But wait, let's confirm with examples.

Take a=2, b=5 (a < b). For i=3 (between 2 and 5):

pos_a(3) = 2+1 =3, pos_b(3) =5. Difference is 5-3=2. |a -b| is 3. So |a -b| -1 = 3-1=2. Correct.

Another example: a=5, b=2 (a > b). For i=3 (between 2 and5):

pos_a(3) =5 (since 3 <5), pos_b(3) =2+1=3. Difference is 5-3=2. |a -b|=3. So 3-1=2. Correct.

So in the interval between min and max, the contribution is |a-b| -1.

Then, for i > max(a,b), the contribution is |a -b| again.

So for the pair (a, b), where a != b, the contribution to i (when i is not a or b) can be broken into:

- i < min(a, b): contribution is D = |a -b|.

- i in (min(a, b), max(a, b)): contribution is D -1.

- i > max(a, b): contribution is D.

But also, when i is a or b, the contribution is different.

So, the total contribution for a pair (a, b) is:

For each i in 1..n:

if i is a → compute the contribution for i=a.

if i is b → compute the contribution for i=b.

Else, compute based on the intervals.

So, for a given pair (a, b), the contribution can be modeled as:

sum over all i of the contribution, which includes:

- contribution from i =a.

- contribution from i =b.

- contributions from the intervals where i is not a or b.

So, for each pair (a, b), we can calculate how much they contribute to each i in O(1) time, by considering these intervals and adding the appropriate values.

But how to accumulate this for all pairs and all i?

We need to find, for each i, the sum over all pairs of the contribution of that pair to i.

The approach is:

1. For each pair (a, b) in x (i.e., consecutive elements in x), compute:

   a. If a == b: no contribution.

   b. Else:

      i. Compute the contribution when i is a.

      ii. Compute the contribution when i is b.

      iii. Compute the contributions for the three intervals (i < min, min < i < max, i > max).

Then, for each i, sum all these contributions across all pairs.

But how to efficiently compute this for all i?

Let's think of each pair as contributing to certain ranges of i.

For the intervals:

For the case where i is not a or b:

The pair contributes D (|a -b|) to all i < min(a,b).

Then contributes (D-1) to all i in (min, max).

Then contributes D to all i > max.

So for each pair (a, b), we can model these ranges and their contributions.

But adding these contributions directly for each pair would be O(1) per pair (for the ranges), using a prefix sum array.

Yes! The idea is to represent the contribution for each pair as ranges and update a difference array, then compute the prefix sums once after processing all pairs.

So, the steps would be:

- Initialize an array ans of size n+2 (to handle 1-based indexing) with 0.

- For each pair (a, b) in x where a != b:

   Compute D = abs(a - b).

   Compute min_ab = min(a, b), max_ab = max(a, b).

   The contribution for i < min_ab: D per i.

   The contribution for min_ab < i < max_ab: (D-1) per i.

   The contribution for i > max_ab: D per i.

   Also, compute the contributions when i is a and i is b.

So, for each pair, we need to add the following to ans:

- For i < min_ab: add D to each i in 1 to min_ab -1.

   But this is O(1) using a range update with a difference array.

- For min_ab < i < max_ab: add (D-1) to each i in (min_ab +1) to (max_ab -1).

- For i > max_ab: add D to each i in (max_ab +1) to n.

Also, handle the contributions for i =a and i =b.

Then, after processing all pairs, compute the prefix sums for ans and add the individual contributions for i =a and i =b.

But how to model the range updates efficiently.

Ah, yes! We can use a difference array approach. For example, to add D to all i in [L, R], we can do:

diff[L] += D

diff[R+1] -= D

Then, after processing all pairs, compute the prefix sum of diff to get the total contribution for each i from the ranges. Then, we add the contributions from i=a and i=b.

So, the plan is:

Initialize a difference array, delta, of size n+2, initialized to 0.

For each pair (a, b) where a != b:

   D = abs(a - b).

   min_ab = min(a, b)

   max_ab = max(a, b)

   # Contribution for i < min_ab: D

   if min_ab > 1:

       L = 1

       R = min_ab -1

       delta[L] += D

       delta[R+1] -= D

   # Contribution for min_ab < i < max_ab: D-1

   if max_ab - min_ab > 1:

       L = min_ab +1

       R = max_ab -1

       delta[L] += (D-1)

       delta[R+1] -= (D-1)

   # Contribution for i > max_ab: D

   if max_ab < n:

       L = max_ab +1

       R = n

       delta[L] += D

       delta[R+1] -= D

   # Now, handle the contributions for i =a and i =b.

   # Contribution for i=a:

   # compute when i=a, which is in the pair (a, b):

   # pos_a(a) is 1. pos_b(a) is:

   # if b < a: pos_b(a) = b+1. So difference is |1 - (b+1)| = b.

   # if b > a: pos_b(a) = b. So difference is |1 - b| = b-1.

   # So, if b <a: |1 - (b+1)| = a -b.

   # Wait, let's compute.

   if a == b: continue (handled earlier)

   # For i =a:

   if b < a:

       # pos_b(a) = b + 1. So difference is |1 - (b+1)| = | -b | = b.

       # Wait, 1 - (b+1) = -b. Absolute value is b.

       contribution_a = b

   else: # b > a

       # pos_b(a) = b. So difference is |1 - b| = b-1.

       contribution_a = b -1

   # Add this to ans[a]

   ans[a] += contribution_a

   # For i =b:

   # pos_b(b) is 1. pos_a(b) is:

   # if a < b: pos_a(b) = a+1. So difference is | (a+1) -1 | = a.

   # if a > b: pos_a(b) = a. So difference is |a -1 | = a-1.

   if a < b:

       contribution_b = a

   else:

       contribution_b = a -1

   ans[b] += contribution_b

Once all pairs are processed, compute the prefix sum of the delta array, which gives the contribution from all the ranges. Then, add this to the ans array (which already contains the contributions for i=a and i=b for all pairs).

Finally, sum the prefix sum array with the ans array, and output the result.

Wait, but the ans array is separate. Let me clarify:

The delta array represents the contributions from all ranges (the intervals where i is not a or b). The ans array holds the contributions from when i is a or b. So, the total for each i is the value from the prefix sum of delta[i] plus ans[i].

So, the steps are:

1. Initialize ans array as [0]*(n+1) (since i ranges from 1 to n).

2. Initialize delta array as [0]*(n+2).

3. For each pair (a, b) in x:

   if a == b: skip.

   else:

      process the three ranges (adding D, D-1, D) to delta.

      compute the contribution for i=a and i=b and add to ans[a] and ans[b].

4. Compute the prefix sum of delta to get the base contribution for each i.

5. For each i from 1 to n, the total contribution is delta_prefix[i] + ans[i].

6. Output this sum for each i.

This approach is O(m + n), since for each of the (m-1) pairs, we process in O(1) time (the range updates via delta array), and then the prefix sum takes O(n) time, plus the ans array which is O(n).

Yes! This should handle the constraints.

Now, let's test this with the first example.

Sample Input 1:

4 4

1 2 3 4

So pairs are (1,2), (2,3), (3,4).

Processing pair (1,2):

a=1, b=2. D=1.

min_ab=1, max_ab=2.

Ranges:

i <1: no (min_ab is 1, so no contribution here.

i between 1 and 2: but max_ab - min_ab is 1, so no interval here.

i>2: 3 to4.

Add D=1 to i>2.

So:

delta[3] +=1, delta[5] -=1.

Then, contribution for i=1 (a):

since b=2 >a=1, contribution_a = b-1=1.

Add to ans[1] +=1.

contribution for i=2 (b):

a=1 <b=2, so contribution_b = a =1. Add to ans[2] +=1.

Next pair (2,3):

a=2, b=3. D=1.

min_ab=2, max_ab=3.

Ranges:

i <2: add 1 to i=1.

i between 2 and3: no (since max_ab - min_ab=1).

i>3: add 1 to 4.

So delta[1] +=1, delta[2] -=1 (for i<2).

delta[4] +=1, delta[5] -=1.

contribution for i=2: b=3>2, contribution_a=3-1=2. ans[2] +=2.

contribution for i=3: a=2 <3: contribution_b=2. ans[3] +=2.

Third pair (3,4):

a=3, b=4. D=1.

min_ab=3, max_ab=4.

Ranges:

i <3: add 1.

i between 3 and4: no.

i>4: add 1 (but n=4, so no).

So delta[1] +=1, delta[3] -=1 (for i<3).

i>4: no.

contribution for i=3: b=4>3, contribution_a=4-1=3. ans[3] +=3.

contribution for i=4: a=3 <4: contribution_b=3. ans[4] +=3.

So after processing all pairs:

ans = [0, 1, 3, 5, 3]

delta after all updates:

For (1,2):

delta[3] +=1, delta[5] -=1.

For (2,3):

delta[1] +=1, delta[2] -=1.

delta[4] +=1, delta[5] -=1.

For (3,4):

delta[1] +=1, delta[3] -=1.

So delta array:

index: 1 2 3 4 5

values after all additions:

delta[1] = 1+1 = 2.

delta[2] = -1.

delta[3] = 1 -1 =0.

delta[4] =1.

delta[5] = -1 (from each pair).

Now, compute the prefix sum of delta:

prefix array:

prefix[0] =0.

prefix[1] =0 + delta[1] = 2.

prefix[2] =2 + delta[2] =1.

prefix[3] =1 + delta[3] =1.

prefix[4] =1 + delta[4] =2.

prefix[5] =2 + delta[5] =1.

But i ranges from 1 to4.

So for each i:

i=1: prefix[1] =2.

i=2: prefix[2] =1.

i=3: prefix[3] =1.

i=4: prefix[4] =2.

Then, ans is:

ans[1] =1.

ans[2] =3.

ans[3] =5.

ans[4] =3.

Total for each i:

i=1: 2 +1 =3.

i=2:1 +3=4.

i=3:1 +5=6.

i=4:2 +3=5.

Which matches the sample output.

So this approach works.

Now, let's code this.

The code steps are:

Read n and m.

Read x array.

Compute the list of pairs (x[j], x[j+1]) for j from 0 to m-2.

Initialize ans and delta arrays.

For each pair in pairs:

   a, b = pair.

   if a == b: continue.

   D = abs(a -b).

   min_ab = min(a, b)

   max_ab = max(a, b)

   # Process ranges:

   # i < min_ab: add D.

   if min_ab > 1:

       L =1

       R= min_ab -1

       delta[L] += D

       delta[R+1] -= D

   # i between min_ab and max_ab: add D-1.

   if max_ab - min_ab >1:

       L = min_ab +1

       R = max_ab -1

       delta[L] += (D-1)

       delta[R+1] -= (D-1)

   # i > max_ab: add D.

   if max_ab <n:

       L = max_ab +1

       R =n

       delta[L] += D

       delta[R+1] -= D

   # handle i =a and i =b:

   # contribution for i=a.

   if b < a:

       contribution_a = (b +1) -1 # since pos_b(a) is b+1. 1 - (b+1) → absolute value is (b+1 -1) =b.

       # wait, the contribution is |1 - (b+1)| = | -b | =b.

       contribution_a = b

   else:

       # b >a. pos_b(a) is b. |1 -b| =b-1.

       contribution_a = b -1

   ans[a] += contribution_a

   # contribution for i =b.

   if a <b:

       # pos_a(b) is a+1. | (a+1) -1 | =a.

       contribution_b =a

   else:

       # a >b. pos_a(b) is a. |a -1|.

       contribution_b =a -1

   ans[b] += contribution_b

After processing all pairs, compute the prefix sum of delta.

Then, for each i from 1 to n:

sum_delta = prefix_sum[i]

total = sum_delta + ans[i]

print all totals.

Implementing this in Python.

But in Python, for the delta array, which can be size n+2 (up to 2e5+2), and m up to 2e5, the code should handle this efficiently.

Now, code:

Read n, m.

x = list of integers.

pairs = list of (x[i], x[i+1]) for i in range(m-1).

Initialize ans as [0]*(n+2) (since indices go up to n).

delta = [0]*(n+2)

for a, b in pairs:

   if a == b:

       continue

   D = abs(a -b)

   min_ab = min(a, b)

   max_ab = max(a, b)

   # i < min_ab: add D to 1..min_ab-1

   if min_ab >1:

       delta[1] += D

       delta[min_ab] -= D

   # i in min_ab+1 to max_ab-1: add D-1

   if max_ab - min_ab >1:

       L = min_ab +1

       R = max_ab -1

       delta[L] += (D-1)

       delta[R+1] -= (D-1)

   # i > max_ab: add D to max_ab+1..n

   if max_ab <n:

       L = max_ab +1

       R =n

       delta[L] += D

       delta[R+1] -= D

   # handle i =a and i =b

   # contribution for i =a.

   if b <a:

       contribution_a = b

   else:

       contribution_a = b-1

   ans[a] += contribution_a

   # contribution for i =b.

   if a <b:

       contribution_b =a

   else:

       contribution_b = a-1

   ans[b] += contribution_b

# compute prefix sum for delta.

current =0

prefix = [0]*(n+2)

for i in range(1, n+1):

   current += delta[i]

   prefix[i] = current

# compute total for each i.

result = [0]*n

for i in range(1, n+1):

   result[i-1] = prefix[i] + ans[i]

print(' '.join(map(str, result)))

Testing this code with sample input.

Sample Input 1:

4 4

1 2 3 4

pairs are (1,2), (2,3), (3,4).

Processing (1,2):

a=1, b=2.

D=1.

min_ab=1, max_ab=2.

i <1: no.

i between 1+1=2 and 2-1=1: no.

i>2: add D=1 to 3..4.

delta[3] +=1, delta[5] -=1.

contributions for i=1: a=1, b=2.

since b> a: contribution_a =2-1=1. ans[1] +=1.

contribution_b: a <b → contribution_b =1. ans[2] +=1.

Processing (2,3):

a=2, b=3.

D=1.

min_ab=2, max_ab=3.

i <2: add D=1 to 1.

delta[1] +=1, delta[2] -=1.

i between 3-1: but 3-2=1, so no.

i>3: add D=1 to 4.

delta[4] +=1, delta[5] -=1.

contributions:

i=2: b=3>2 → contribution_a=3-1=2. ans[2] +=2.

i=3: a=2 <3 → contribution_b=2. ans[3] +=2.

Processing (3,4):

a=3, b=4.

D=1.

min_ab=3, max_ab=4.

i <3: add D=1 to 1-2.

delta[1] +=1, delta[3] -=1.

i between 4-1=3: no.

i>4: no (n=4).

contributions:

i=3: b=4>3 → contribution_a=4-1=3. ans[3] +=3.

i=4: a=3 <4 → contribution_b=3. ans[4] +=3.

So after processing:

ans[1] =1, ans[2]=1+2=3, ans[3]=2+3=5, ans[4]=3.

delta:

delta[1] =1+1=2 (from pair 2 and 3).

delta[2] =-1 (from pair 2).

delta[3] =1 (from pair 1) -1 (from pair3) → 0.

delta[4] =1 (from pair2).

delta[5] =-1 (from pair1, pair2).

prefix sum:

current starts at 0.

i=1: current +=2 → 2.

i=2: current +=-1 →1.

i=3: current +=0 →1.

i=4: current +=1 →2.

prefix is [0, 2, 1, 1, 2].

So for each i:

i=1: 2 +1=3.

i=2:1+3=4.

i=3:1+5=6.

i=4:2+3=5. Which matches the sample.

Another sample input:

Sample Input 2:

5 5

2 1 5 3 5

Output: 9 8 12 6 8.

We can test this, but perhaps time is tight. But the code seems correct.

Thus, the code should handle all cases.
</think>

```python
n, m = map(int, input().split())
x = list(map(int, input().split()))
pairs = []
for i in range(m-1):
    a, b = x[i], x[i+1]
    pairs.append((a, b))

ans = [0] * (n + 2)
delta = [0] * (n + 2)

for a, b in pairs:
    if a == b:
        continue
    D = abs(a - b)
    min_ab = min(a, b)
    max_ab = max(a, b)
    
    # Range i < min_ab: add D
    if min_ab > 1:
        delta[1] += D
        delta[min_ab] -= D
    
    # Range min_ab < i < max_ab: add D-1
    if max_ab - min_ab > 1:
        L = min_ab + 1
        R = max_ab - 1
        delta[L] += (D - 1)
        delta[R + 1] -= (D - 1)
    
    # Range i > max_ab: add D
    if max_ab < n:
        L = max_ab + 1
        R = n
        delta[L] += D
        delta[R + 1] -= D
    
    # Contribution for i = a
    if b < a:
        contribution_a = b
    else:
        contribution_a = b - 1
    ans[a] += contribution_a
    
    # Contribution for i = b
    if a < b:
        contribution_b = a
    else:
        contribution_b = a - 1
    ans[b] += contribution_b

# Compute prefix sums for delta
current = 0
prefix = [0] * (n + 1)
for i in range(1, n+1):
    current += delta[i]
    prefix[i] = current

# Calculate the result
result = []
for i in range(1, n+1):
    total = prefix[i] + ans[i]
    result.append(str(total))

print(' '.join(result))
```