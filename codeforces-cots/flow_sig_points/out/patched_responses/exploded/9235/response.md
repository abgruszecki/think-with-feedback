<think>
Okay, let's see. The problem is about finding the best time to start a contest so that the maximum number of people participate. The twist here is dealing with different time zones and figuring out when each time zone's local time falls into the [s, f) interval.

Hmm. Let's break it down. Each timezone is adjacent and differs by one hour. So the first timezone's time is the base. For example, if the contest starts at time t in the first timezone, then in the i-th timezone, the local start time is t + (i-1) mod n? Wait, wait. Wait, the problem says that adjacent timezones differ by one hour. So when it's 1 hour in the first, the i-th is i hours. So when the first timezone is at time x, the i-th is x + (i-1) mod n? Or maybe x is the first timezone's time. Wait, the problem says: "When local time in the 1st timezone is 1 hour, local time in the i-th timezone is i hours." Oh right. So when the first timezone is at time t, the i-th is (t + i -1 - 1) mod n +1. Wait, maybe not. Let's think again. Suppose the first timezone is at t. Then each adjacent timezone to the east (or next) is t+1. But since it's a cycle (since after n comes 1 again), the i-th timezone's time would be (t-1 + (i-1)) mod n + 1. Because the first timezone is i=1: (t-1 +0) mod n +1 = t. Then i=2 is (t-1+1) mod n +1 = t+1 mod n, but since when the first is 1, the second is 2, etc. So yes, that formula is correct.

So for a contest that starts at time h in the first timezone, the i-th timezone's local start time is (h-1 + i-1) mod n + 1. Which simplifies to (h + i -2) mod n + 1. Wait, let's calculate for h=3, i=2. Then (3-1 +1) mod n +1 = (3) mod n +1? Wait, maybe I'm miscalculating. Let's take the first example. In the first sample, the contest starts at 3 in the first timezone. Then, for i=2, the local start time is 3 + (2-1) -1 mod 3? Wait, maybe another approach. Since when the first timezone's time is h, the i-th timezone's time is h + (i-1) - k*n, adjusted to wrap around. But since the hours are cyclic mod n (since 1 follows n), the correct formula is (h + i -1 -1) mod n +1. Because when h is the first timezone's time, adding (i-1) steps (since each adjacent adds 1), but subtracting 1 because h is the first timezone's time (i=1 gives h). Then mod n and add 1 to get back into 1-based.

Wait, maybe the correct formula for the local start time in the i-th timezone when the first timezone starts at h is (h + i -1 -1) mod n +1? Which simplifies to (h + i -2) mod n +1. Let's test with the first sample. First sample input starts at h=3. For i=1, (3+1-2) mod 3 +1 = (2 mod3) +1 = 3. Which matches the first timezone. For i=2: (3 +2-2) mod3 +1 = 3 mod3 +1 = 0 +1=1. Which is correct (second timezone's start time is 1). For i=3: (3+3-2) mod3 +1=4 mod3 +1=1+1=2. Which is correct. So yes.

So the contest starts at h in the first timezone. For each participant in the i-th timezone, their local time is (h + i -2) mod n +1. They will participate if this time is >= s and <f. Because the contest starts no earlier than s and ends before f.

Wait, the problem says that the contest lasts exactly one hour. So it starts at the beginning of some hour (so, for example, at s:00), and ends at the next hour. So the interval is [s, f), meaning that if the start time is s, then it ends at s+1. But since the contest must start in the same hour across all timezones, we need to find h such that in each timezone i, the start time is >=s and <f. But the contest is exactly one hour long, so it's the start time that has to be in [s, f) for each participant.

So for each i, the participant will join if the start time in their timezone is in [s, f). So the condition is:

s <= start_time_i < f.

We need to find h such that the sum of a_i for all i where this condition holds is maximized.

So the problem reduces to, for each possible h (starting time in first timezone), compute the sum of a_i where (h +i -2) mod n +1 is in [s, f).

But h can be from 1 to n. The output is the h that gives the maximum sum. If multiple h's, pick the smallest.

Now, the constraints are n up to 1e5. So a naive approach of iterating each h and for each h, checking all n i's would be O(n^2), which is 1e10 operations—way too slow.

So we need an O(n) or O(n log n) solution.

Let's think about how to model the condition. The start time in timezone i is (h +i -2) mod n +1. Let's call this value S_i. We need S_i >=s and S_i <f.

Let's compute S_i:

S_i = ((h-1) + (i-1)) mod n +1. Because h-1 is the 0-based start time (since 1-based), adding (i-1) steps (since each timezone adds 1), mod n gives the 0-based time, then adding 1 to get back to 1-based.

So S_i = (h-1 + i-1) mod n + 1 = (h + i -2) mod n +1.

Wait, (h-1 + i-1) is h+i-2. Then mod n, then add 1. So S_i is (h+i-2 mod n) +1. So that's correct.

So the condition for a_i to be included is:

s ≤ (h + i -2 mod n) +1 <f.

Let's subtract 1 from all parts:

s-1 ≤ (h +i -2) mod n <f-1.

But (h +i -2) mod n is the same as (h-2 +i) mod n.

Wait, maybe we can rearrange this.

The condition can be rewritten as:

(h +i -2) mod n is in [s-1, f-1 -1] (since the upper bound is exclusive). Wait, no:

Original condition:

s <= S_i < f → s <= ( (h+i-2) mod n +1 ) < f.

Subtract 1 from all parts:

s-1 <= (h+i-2) mod n < f-1.

Yes. So (h+i-2) mod n must be >= s-1 and <f-1.

Let me denote A = s-1, B = f-1-1? Wait, no: the upper bound is f-1. Because (h+i-2) mod n must be less than (f-1). So the interval is [A, B) where A = s-1 and B = f-1.

So the condition is (h +i -2) mod n is in [A, B), i.e., the interval from A (inclusive) to B (exclusive) modulo n.

But since mod n wraps around, the interval [A, B) could be a single contiguous range or wrap around.

For example, if A=2 and B=0 (mod 3), then the interval is [2,0) mod 3 → which is the same as [2,3) → 2,0,1? Wait, no. Wait, mod 3, B=0 would be equivalent to 3. So [A, B) is [2,0), which is the same as [2,3), which is just 2. Wait, perhaps it's better to split into two cases: if A < B, then the interval is A ≤ x < B. If B <= A, then the interval is x >=A or x < B.

So, for each i, the condition is equivalent to (h + i -2) mod n is in the interval [A, B) when A < B, else (h+i-2) mod n >=A or <B.

But how can we model this for each h?

Wait, for a fixed i, the condition (h +i -2) mod n is in [A, B) is equivalent to h being in [ (A -i +2) mod n, (B -i +2) mod n ). Because:

Let's consider the equation (h +i -2) mod n = k. For a given k, h ≡ (k -i +2) mod n. So for (h +i -2) mod n to be >=A and <B, h must be in the range [A -i +2, B -i +2) mod n.

Wait, perhaps not. Let's think:

h +i -2 ≡ x mod n, where x is in [A, B).

So h ≡ (x -i +2) mod n.

But x can be in the interval [A, B). So for each x in that interval, h ≡ (x -i +2) mod n. So the possible h's for which i is included are the h's that are congruent to (x -i +2) mod n for some x in [A, B).

Alternatively, for a given i, the set of h's that would include a_i in the sum is the h's that satisfy (h +i -2) mod n is in [A, B). Let's rephrase this as:

h mod n ∈ [ (A -i +2) mod n, (B -i +2) mod n )

But how? Let's see.

We can rewrite h ≡ (x - i + 2) mod n for some x in [A, B). So the possible h's are the values (x -i +2) mod n as x ranges from A to B-1. But how can we model this as a range of h's?

Alternatively, perhaps for each i, the h's that would include a_i in the sum form a circular interval. For example, if the interval [A, B) is a contiguous block when viewed on a circle of 0..n-1, then h's that are in (A -i +2) mod n ... (B -i +1) mod n would be the ones that include a_i.

This seems complicated. But perhaps instead of thinking for each h, which i's are included, we can precompute for each i the range of h's that include i, and then sum over all a_i for those ranges.

Then the problem becomes finding the h that is covered by the maximum sum of ranges.

So for each i, the a_i contributes to a certain interval of h's. Then, the maximum h is the one with the highest sum of a_i's over all intervals that cover it.

This is similar to a line sweep problem, where we can accumulate the sum for each h by adding a_i when h is in the range for i and subtract when it's out.

So here's the plan:

1. For each i, compute the start and end of the interval [L_i, R_i) in h's where h in this interval would include i in the sum.

2. Convert all these intervals into events (like +a_i at L_i, -a_i at R_i).

3. Then, perform a sweep over h=1 to n (mod n), and track the current sum. The maximum sum and the earliest h where this occurs is the answer.

But since the intervals are circular (mod n), we have to handle the wrapping around.

But how to model this correctly.

Let's first compute for each i, the interval [L, R) of h's where including a_i.

So for i, the condition (h +i -2) mod n is in [A, B), where A = s-1, B = f-1.

We can rewrite this as:

(h + i -2) mod n >= A and < B.

Which is equivalent to:

A <= (h + i -2) mod n < B.

Let’s denote X = h mod n. So X can be 0..n-1 (since mod n). But h ranges from 1 to n. So when h is in 1..n, X is h-1.

Wait, h is the starting time in the first timezone, which is 1-based. So h can be 1, 2, ..., n.

So h-1 is 0-based. Let's let X = h-1. So X ranges from 0 to n-1. Then, the condition becomes:

A <= (X + i-1) mod n < B.

Because h + i -2 = (h-1) + (i-1) = X + i-1.

So (X + i-1) mod n must be >= A and < B.

So for each i, the X values that satisfy this are:

X ≡ (A - (i-1)) mod n ... (B-1 - (i-1)) mod n.

Wait, no. Let's solve for X.

We need (X + i-1) mod n >= A and < B.

Let’s let Y = X + i-1.

Then Y mod n >= A and Y mod n < B.

So Y can be written as Y = k*n + y, where y is in [A, B).

So Y can be any integer such that when divided by n, the remainder is in [A, B).

Thus, Y is in the interval [A, B) + m*n, for any integer m.

But since X is between 0 and n-1 (since X = h-1), and Y = X + i-1, then Y can range from (i-1) to (i-1) + (n-1) = i +n-2.

So possible values of Y are in [i-1, i +n -2].

But for Y to have a remainder in [A, B) when divided by n, the possible Y's are in [A, A+1, ..., B-1] + k*n, where k is such that Y is in [i-1, i+n-2].

But this might be a bit complex. Alternatively, perhaps we can model the possible X's for each i as follows:

X + i-1 >= A → X >= A - (i-1) + m*n (for some m).

But since X is in 0..n-1, perhaps the possible X's form a range.

Alternatively, the possible X's are those for which (X + i-1) mod n is in [A, B). Let's rewrite this as:

A <= (X + i-1) mod n < B.

Which can be split into two cases:

Case 1: A < B.

In this case, the condition is equivalent to X + i-1 ≡ y mod n, where y is in [A, B). So X ≡ (y - (i-1)) mod n for some y in [A, B-1].

Which can also be written as X ∈ [(A - (i-1)) mod n, (B - (i-1) -1) mod n] ?

Wait, perhaps not. Let's think:

If A < B, then the valid Y mod n values are [A, B-1]. So Y can be from A to B-1. Then Y = X + i-1. So X = Y - (i-1).

But X must be in 0..n-1. So Y can be from A to B-1, and X = Y - (i-1) mod n.

But perhaps the valid X's form a continuous interval. Let's compute:

The minimal X is (A - (i-1)) mod n.

The maximal X is (B-1 - (i-1)) mod n.

But when you subtract (i-1), you might go into negative numbers, hence the mod n.

Wait, perhaps the valid X's are those in the interval [ (A - (i-1) + n) % n, (B - 1 - (i-1) + n) % n +1 ), but considering wrap-around.

Alternatively, the valid X's are those for which X is in [ (A - (i-1)) mod n, (B - (i-1) -1) mod n ].

But this might not capture the entire interval. Let me see with an example.

Let’s take n=5, A=1, B=4 (so A < B).

So Y mod 5 should be in [1, 3]. So Y can be 1,2,3, or 6,7,8 (but X is in 0..4). Let's take i=2. Then Y = X +1 (since i-1=1). So Y must be in [1,3], 6 mod5 is 1, 7 is 2, 8 is 3. So for X in 0..4, Y ranges from 1 to 5 (since X can be 0, Y=1; X=4, Y=5). So Y can be 1,2,3, or 5 (mod5, but Y=5 mod5 is 0, which is not in [1,3]. So the valid X's for i=2 and A=1, B=4 would be X=0,1,2 (since Y=1,2,3). So X ranges from 0 to 2, which is [0,2]. So the interval is length 3 (B-A=3). So for this case, X is in [A - (i-1), B-1 - (i-1)] mod n.

In this example, A=1, i-1=1. So A - (i-1) = 0. B-1=3. B-1 - (i-1) = 3-1=2. So X ranges from 0 to 2. Which matches.

So when A < B, the X's are from (A - (i-1)) mod n to (B-1 - (i-1)) mod n, but since X must be in 0..n-1, perhaps the interval is a contiguous range.

So when (A - (i-1)) <= (B-1 - (i-1)), then the X's form a contiguous interval. But if (A - (i-1)) is larger than (B-1 - (i-1)), then the interval wraps around.

Wait, no. If A < B, then (A - (i-1)) mod n is (A - (i-1) + n) mod n if A - (i-1) is negative. But if A >= (i-1), then it's straightforward.

Alternatively, maybe the interval for X is [L, R), where L = (A - (i-1)) mod n and R = (B - (i-1)) mod n. Because for the X values where L <= X < R (mod n), then (X + i-1) mod n is between A and B-1.

Wait, perhaps. Let's see.

If L and R are computed as (A - (i-1)) mod n and (B - (i-1)) mod n, then the interval is from L to R, but considering wrap-around.

But since A and B are between 0 and n-1 (since A = s-1, s >=1 and <=n, so A can be 0 to n-1, and B is f-1, which can be up to n-1 when f=n+1, but f<=n so B can be up to n-1).

Wait, but s and f are given as 1<=s < f <=n. So A = s-1 ranges from 0 to n-1 -1 = n-2. B = f-1 ranges from 1 to n-1. So A < B is always true, because s < f implies s-1 < f-1. Because A is s-1, B is f-1. So since s < f, then A < B. So the interval [A, B) is a contiguous range, and A < B.

Ah! That's a key insight. Since s < f, then A = s-1, B = f-1. So A < B. Because s < f → s-1 < f-1. So the interval [A, B) is a contiguous range in the 0-based mod n system.

Therefore, the condition (X + i-1) mod n is in [A, B) → which is equivalent to X +i-1 >= A and X +i-1 < B, mod n. But since A and B are in 0..n-1 and A < B, this is equivalent to X +i-1 >=A and X +i-1 < B, regardless of mod n. Because if X +i-1 >=A and <B, then mod n is the same as X +i-1, which is in [A, B). If X +i-1 >=n, then mod n would be less than B (since B is at most n-1), but X is in 0..n-1, so X +i-1 can be up to (n-1) + (n-1) = 2n-2. But since X ranges from 0 to n-1 and i ranges from 1 to n, X +i-1 can be up to (n-1) + (n-1) = 2n-2. But mod n, that's 2n-2 mod n = n-2. Which is less than B (since B is <=n-1). So in that case, the mod n would not affect the condition. Wait, but this is only true if X +i-1 is in [A, B) or [A +n, B +n), etc. But since A < B, the only way for X +i-1 to be in [A, B) is if X +i-1 is exactly in [A, B). Because if X +i-1 >=n, then mod n would be X +i-1 -n. But in that case, the condition (X +i-1) mod n >=A and <B would require that X +i-1 -n is in [A, B). Which implies that X +i-1 >= A +n and X +i-1 < B +n. But since X is at most n-1, and i can be up to n, X +i-1 can be up to (n-1) + (n-1) = 2n-2. So possible ranges where X +i-1 is in [A, B) or [A +n, B +n) (but B +n could be larger than 2n-2). For example, if A=1, B=3, n=5. Then X +i-1 could be 1,2 (mod 5). Or 6,7 (but X +i-1 can be up to 2*5-2=8, so 6,7 would correspond to 6 mod5=1, 7 mod5=2. So in that case, even though X +i-1 is 6, which is >=A (1) but < B (3), mod5 gives 1 which is in the desired interval. So in this case, even if X +i-1 is greater than n, the mod n would still allow it to be in the interval.

So the initial approach of thinking that the condition is (X +i-1) mod n is in [A, B) is equivalent to X +i-1 being in [A, B) + k*n for some integer k. So the possible X's are such that X +i-1 is in the union of intervals [A +k*n, B +k*n), for all integers k.

But X ranges from 0 to n-1, and i ranges from 1 to n, so X +i-1 can be as small as 0 (X=0, i=1) to (n-1) + (n-1) = 2n-2. So the possible k's are 0 and 1.

So the possible X's are those for which X +i-1 is in [A, B) or [A+n, B+n).

But A and B are between 0 and n-1. So [A, B) is within 0 to n-1. [A +n, B +n) is within n to 2n-1. Since X +i-1 can be up to 2n-2, the possible X's are in either [A, B) - (i-1) mod n or [A+n, B+n) - (i-1) mod n. But since X must be in 0..n-1, the second interval [A+n - (i-1), B+n - (i-1)) could wrap around.

Wait, perhaps this is getting too complicated.

An alternative approach: For each i, the X's (h-1) that satisfy (X +i-1) mod n is in [A, B) can be found as X >= (A - (i-1) + n) mod n and X < (B - (i-1) + n) mod n. But I'm not sure.

Alternatively, since A and B are fixed and A < B, the condition (X +i-1) mod n >=A and <B can be rephrased as:

X >= (A - (i-1) + n) mod n and X < (B - (i-1) + n) mod n.

Wait, perhaps not. Let's think of X as being in 0..n-1.

Then X +i-1 can be written as (X + i-1) = q *n + r, where r is in [A, B).

So X +i-1 can be in [A, B) → X in [A - (i-1), B - (i-1)).

But X can't be negative. So if A - (i-1) is negative, then X could be in two intervals: from 0 to B - (i-1) -1, and from (A - (i-1) +n) to n-1.

Wait, that's possible.

So the valid X ranges for i can be:

If (A - (i-1)) <= (B - (i-1)):

   If the entire interval [A - (i-1), B - (i-1) -1] is within 0..n-1, then X is in that interval.

   Else, split into two intervals.

Else, it wraps around.

Wait, this seems complicated. Let's take an example.

Suppose n=5, A=1, B=3 (so [1, 2] mod5).

i=2. So i-1=1.

So X +1 must be in [1, 3).

So X+1 >=1 → X >=0.

X+1 <3 → X <2.

So X is in [0, 2) → 0 <=X <2 → X=0,1.

Which are valid as 0 and 1 are within 0..4.

Another example: i=3, A=1, B=3. i-1=2.

X+2 >=1 → X >=-1 (but X >=0).

X+2 <3 → X <1.

So X is in [0, 1) → X=0.

Another example: i=1, A=3, B=5 (since A=3, B=5, which is equivalent to [3,4] mod5).

i-1=0. X +0 >=3 → X >=3.

X +0 <5 → X <5. Since X is in 0..4, this is X >=3 → X=3,4.

So the valid X's are 3 and4.

So for each i, the valid X's are those in the interval [A - (i-1), B - (i-1)) but adjusted for the modulo n.

But since X is in 0..n-1, the interval can be written as:

start = (A - (i-1)) % n

end = (B - (i-1)) % n

But then, if start < end, the valid X's are in [start, end).

If start >= end, then it's [start, n) and [0, end).

But since A < B, and i ranges from 1 to n, we can compute start and end as follows:

start = (A - (i-1)) % n

end = (B - (i-1)) % n

But since A < B, (B - (i-1)) - (A - (i-1)) ) = B -A.

So B -A is the length of the interval.

But how to compute the interval for X.

Alternatively, the X's for i are:

X >= (A - (i-1) + n) %n and X < (B - (i-1) +n) %n.

But this may not be correct.

Alternatively, perhaps the valid X's for i are the X's that lie in the interval [ (A - (i-1)) mod n, (B - (i-1)) mod n ), treating the modulo as a circular interval.

But since A < B, and X is in 0..n-1, perhaps the interval is:

If (A - (i-1)) <= (B - (i-1)), then the valid X's are [ (A - (i-1)), (B - (i-1)) -1 ]

But if (A - (i-1)) is negative, then this would wrap around.

Alternatively, perhaps we can compute the interval as follows:

The valid X's for i are those X where X is in the interval [L, R), where L = (A - (i-1) + n) %n and R = (B - (i-1) +n) %n.

But how?

Alternatively, perhaps the interval for X is [ (A - (i-1)) mod n, (B - (i-1)) mod n ), but considering that when (B - (i-1)) mod n is less than (A - (i-1)) mod n, then it wraps around.

But since A < B, (B - (i-1)) mod n can be less than (A - (i-1)) mod n when (i-1) is such that (A - (i-1)) mod n is greater than (B - (i-1)) mod n.

But this is getting too complicated. Maybe there's a smarter way.

Alternative approach: For each i, the a_i is added to all X's (h-1) where (X +i-1) mod n is in [A, B). Since A < B, this is the same as (X +i-1) >=A and (X +i-1) < B.

So solving for X:

X >= A - (i-1)

X < B - (i-1)

But X must be in 0..n-1.

So the valid X's are in the intersection of [A - (i-1), B - (i-1)) and [0, n-1].

This intersection may be one interval or two intervals if the first interval wraps around.

Let's compute the possible X's for each i.

The interval for X is [max(A - (i-1), 0), min(B - (i-1)-1, n-1)].

But this only works if A - (i-1) <= B - (i-1) -1. But since B - (i-1) - A + (i-1) = B -A >0 (since A < B), this interval is valid.

Wait, but this approach would miss the cases where the interval wraps around. For example, if A - (i-1) is negative, then the X's could start from 0 up to (B - (i-1) -1) and also from (A - (i-1) +n) to n-1. But this is not captured in this method.

Hmm. Let's take an example:

n=5, A=3, B=5 (so [3,4] in 0-based mod5). i=2, i-1=1.

A - (i-1) = 3-1=2. B - (i-1) =5-1=4. So X must be >=2 and <4 → X=2,3. So the valid X's are 2 and3.

Another example: A=1, B=3, i=4 (i-1=3). A -3 = -2. B-3 =0. So X >=-2 and <0 → X can be -2, -1. But since X is in 0..4, this is empty. So no X's would be valid. But that's incorrect. Because:

X +i-1 = X +3. For X in 0..4, X+3 ranges from 3 to7. Mod5, that's 3,4,0,1,2. So the condition (X+3) mod5 >=1 and <3 → mod5 is in [1,3). So the possible mod5 values are 1,2. So X+3 mod5 =1 → X+3 =1 +5k → X= -2 +5k. But X must be in 0..4. So k=1 → X=3 (since 1+5*1=6 → X=3 → 3+3=6 mod5=1). Similarly, X=4 →4+3=7 mod5=2. So valid X's are 3,4. Also, X=0 →0+3=3 mod5=3 which is >=3 → but B is 3, so the condition is (X+3 mod5) <3 → no. So X=3 and4 are valid.

But according to the previous approach:

X >= A - (i-1) → 1-3= -2 → X >=-2 and <0. But X is in 0..4. So no valid X's. Which is not correct.

So this approach is missing cases where the interval wraps around.

So the correct way to compute the valid X's is:

For X in 0..n-1:

X +i-1 >= A and X +i-1 < B → X >= A - (i-1) and X < B - (i-1).

But since X is in 0..n-1, we have to find all X that satisfy this, considering possible wrap-around.

So the valid X's can be in two parts:

1. When X >= A - (i-1) and X < B - (i-1), and X is >=0 and <n.

But A - (i-1) could be negative, and B - (i-1) could be greater than n.

So let's split into cases:

Case 1: A - (i-1) >=0 and B - (i-1) <=n:

   X ranges from A - (i-1) to B - (i-1)-1, inclusive.

Case 2: A - (i-1) <0 and B - (i-1) <=n:

   X ranges from 0 to B - (i-1)-1, and also from (A - (i-1) +n) to n-1.

Case 3: B - (i-1) >n:

   X ranges from A - (i-1) to n-1, and from 0 to (B - (i-1) -n) -1.

But wait, this seems complicated. But perhaps the correct way to handle all cases is to compute the lower and upper bounds and then check where they fall within 0..n-1.

Alternatively, since X is in 0..n-1, we can compute the minimal and maximal values that X can take, considering the condition X >= (A - (i-1)) and X < (B - (i-1)).

So for each i:

low = max(A - (i-1), 0)

high = min(B - (i-1) -1, n-1)

If low <= high, then the valid X's are [low, high].

But if low > high, then there are two intervals:

[0, high] and [low, n-1].

But this only captures cases where the entire interval is within the 0..n-1 range.

Wait, for example, when A - (i-1) is negative and B - (i-1) is positive:

Then the X's are >= A - (i-1) (which is negative) → so all X >=0 and < B - (i-1). So valid X's are 0 to (B - (i-1) -1).

But if B - (i-1) is >n, then X can be up to n-1.

Wait, perhaps this is getting too complicated, and there's a better way.

Another approach is to note that the problem can be transformed into a circular array where each a_i contributes to a range of X's (h-1) of length (B - A) mod n. Since A < B, the length is B - A.

So for each i, the a_i contributes to a segment of X's of length (B - A). So for each i, the X's that include a_i are in the interval [ (A - (i-1)), (B - (i-1)) ) modulo n.

So, we can model this as a circular array, where for each i, we add a_i to the interval [L, R), where L = (A - (i-1)) mod n, R = (B - (i-1)) mod n.

But handling this for each i as a circular interval is computationally expensive unless we find a way to represent this efficiently.

The standard way to handle such ranges is to use a difference array. For each interval [L, R), we add a_i to the difference array at L, and subtract at R. Then, after processing all intervals, we compute the prefix sum to get the sum for each X.

But since the array is circular, we have to handle wrap-around intervals.

So for each i:

L = (A - (i-1)) mod n

R = (B - (i-1)) mod n

We need to add a_i to all positions X in [L, R).

If L < R:

   add a_i to diff[L], subtract from diff[R]

Else:

   add a_i to diff[L], subtract from diff[0], add a_i to diff[0], subtract from diff[R]

Wait, that's the standard way. For example, if the interval wraps around (L >= R), then the interval is [L, n) and [0, R). So for the difference array:

diff[L] += a_i

diff[0] += a_i (if R is not zero?)

Wait, no. For a circular array, if the interval is from L to R (with L >= R), then it's equivalent to two intervals: [L, n) and [0, R). So for the difference array:

For [L, n): add a_i at L, subtract at n (which is beyond the array, so ignored).

For [0, R): add a_i at 0, subtract at R.

So combined:

diff[L] += a_i

diff[0] += a_i

diff[R] -= a_i

But since the array is 0-based and of size n, the end of the array is at n-1. So when R is zero, it's equivalent to adding to [L, n-1] and [0, 0) which is nothing. So perhaps for L >= R:

diff[L] += a_i

diff[0] += a_i

diff[R] -= a_i

But if R is zero, then the second interval is [0,0), which is nothing. So when R=0, the second interval is empty, so we only add to [L, n-1].

Wait, maybe I should handle it as:

if L <= R:

   diff[L] += a_i

   diff[R] -= a_i

else:

   diff[L] += a_i

   diff[0] += a_i

   diff[R] -= a_i

But wait, in the case where L >= R, the interval is [L, n) and [0, R). So the first part is [L, n), which is handled by adding to diff[L] and subtracting at diff[n], which is beyond the array. Then the second part is [0, R), which is handled by adding to diff[0] and subtracting at diff[R].

So the difference array would have:

diff[L] += a_i

diff[0] += a_i

diff[R] -= a_i

But for the first part, since the array is of size n, the subtraction at R would account for the [0, R) part, but the [L, n) part would need to be accounted for by diff[L] += a_i and then a subtract at n (which is not in the array). But in reality, the subtraction at n would not affect the array. So when L >= R, the code would have to add a_i to diff[L], add a_i to diff[0], and subtract a_i from diff[R].

Yes. For example, if L=3, R=2, n=5:

The interval is [3,4] (since n=5) and [0, 2). So the total X's are 3,4,0,1.

The difference array would be:

diff[3] +=a_i

diff[0] +=a_i

diff[2] -=a_i.

Then when computing the prefix sum:

At 0: sum +=a_i (from diff[0]).

At 1: sum +=0.

At 2: sum -=a_i.

At 3: sum +=a_i.

So the sum for X=0: a_i (from diff[0]).

X=1: a_i.

X=2: a_i -a_i =0.

X=3: a_i.

X=4: a_i.

So the sum for X=0,1,3,4 is a_i.

Which is correct.

So the correct way to handle the difference array is:

for each i:

compute L = (A - (i-1)) mod n

R = (B - (i-1)) mod n

if L < R:

   diff[L] += a_i

   diff[R] -= a_i

else:

   diff[L] += a_i

   diff[0] += a_i

   diff[R] -= a_i

Then, after processing all i's, compute the prefix sum of the diff array. The maximum sum and the corresponding X (which is h-1) can be found.

Once we have the maximum sum for X, the corresponding h is X+1. We need to find the smallest h with the maximum sum.

This approach is O(n) time and space, which is acceptable for n=1e5.

So the steps are:

1. Compute A = s-1, B = f-1.

2. Initialize a difference array diff of size n with zeros.

3. For each i in 1..n:

   Compute L = (A - (i-1)) % n

   R = (B - (i-1)) % n

   If L < R:

       diff[L] += a[i-1]

       diff[R] -= a[i-1]

   else:

       diff[L] += a[i-1]

       diff[0] += a[i-1]

       diff[R] -= a[i-1]

   (Note that in Python, indices are 0-based, so a is a list where a[i-1] is the i-th timezone's people.)

Wait, input is a_1 to a_n. So in Python, the list is a = list(map(int, input().split())), where a[0] is a_1, a[1] is a_2, etc. Wait no. The second line of input is n space-separated integers a_1, a_2, ..., a_n. So for i in 1..n, the a_i is stored as a[i-1] in the list. So for example, the first sample input:

3

1 2 3 → a = [1,2,3]. So a[0] is a_1=1, a[1]=a_2=2, a[2]=a_3=3.

So yes.

4. After processing all i, compute the prefix sum of the diff array.

5. Find the X (0-based) with the maximum sum. If multiple X's have the same sum, choose the smallest X. Then, h = X +1.

But wait, X is 0-based (0..n-1), so h is X+1.

But according to the problem statement, the contest starts at h in the first timezone. So the correct h is X+1.

But when we compute the maximum sum in the diff array (after prefix sum), the X corresponds to h-1. So the correct h is X+1.

Now, implement this.

Let's test the first sample:

Sample Input 1:

3

1 2 3

1 3 → s=1, f=3 → A=0, B=2.

For each i from 1 to 3:

i=1:

L = (0 - 0) mod3 =0

R = (2 -0) mod3=2.

0 <2 → diff[0] +=1, diff[2] -=1.

i=2:

L = (0-1) mod3= 2.

R = (2-1) mod3=1.

2 >=1 → so split into [2,3) and [0,1).

diff[2] +=2, diff[0] +=2, diff[1] -=2.

i=3:

L = (0 -2) mod3=1.

R = (2-2) mod3=0.

1 >=0 → split into [1,3) and [0,0) (which is nothing).

So diff[1] +=3, diff[0] +=3, diff[0] -=3 → net: diff[1] +=3, diff[0] remains 0.

Wait, no. Wait for i=3:

L = (A - (i-1)) mod3 = (0-2) mod3 = (-2 mod3) =1.

R = (2-2) mod3=0.

So L >= R.

So we add to diff[L] (diff[1] +=3), add to diff[0] (3), subtract from diff[R] (diff[0] -=3).

So diff[0] +=3 -3 =0.

So for i=3:

diff[1] +=3

diff[0] +=3

diff[0] -=3.

So net:

diff[1] +=3, diff[0] is 0.

Now, the diff array is:

After processing all i's:

i=1:

diff[0] +=1 → 1.

diff[2] -=1 → -1.

i=2:

diff[2] +=2 → 1 (from -1 to 1).

diff[0] +=2 → 3 (from 1+2=3).

diff[1] -=2 → -2.

i=3:

diff[1] +=3 → 1 (from -2 +3=1).

diff[0] +=3 → 3+3=6.

diff[0] -=3 → 6-3=3.

So final diff array:

index 0: 3 (from i=1: +1, i=2: +2, i=3: +3-3=0 → 1+2=3)

Wait, perhaps I'm getting confused. Let me recompute the steps.

Initial diff array is [0, 0, 0].

Processing i=1:

L=0, R=2.

diff[0] +=1 → diff becomes [1, 0, -1].

Processing i=2:

L=2, R=1.

So L >= R.

diff[2] +=2 → [1, 0, -1+2=1].

diff[0] +=2 → [1+2=3, 0, 1].

diff[1] -=2 → [3, 0-2=-2, 1].

Processing i=3:

L=1, R=0.

So L >= R.

diff[1] +=3 → [3, -2+3=1, 1].

diff[0] +=3 → [3+3=6, 1, 1].

diff[0] -=3 → [6-3=3, 1, 1].

So final diff array is [3, 1, 1].

Now, compute the prefix sum:

current_sum = 0.

prefix sums:

X=0: current_sum +=3 → 3.

X=1: current_sum +=1 →4.

X=2: current_sum +=1 →5.

But wait, the diff array is [3,1,1]. So the prefix sum is:

After X=0: sum=3.

X=1: sum=3+1=4.

X=2: sum=4+1=5.

The maximum sum is 5 at X=2. So h is 2+1=3. Which matches the first sample.

So this approach works.

Another example: sample 2.

Input:

5

1 2 3 4 1

1 3 → s=1, f=3 → A=0, B=2.

n=5.

For each i from 1 to5:

A=0, B=2.

i=1:

L=(0 -0) mod5=0.

R=2-0=2 mod5=2.

diff[0] +=1, diff[2] -=1.

i=2:

L=0-1 mod5=4.

R=2-1=1 mod5=1.

4 >=1.

diff[4] +=2.

diff[0] +=2.

diff[1] -=2.

i=3:

L=0-2= -2 mod5=3.

R=2-2=0 mod5=0.

3 >=0.

diff[3] +=3.

diff[0] +=3.

diff[0] -=3 → net diff[3] +=3, diff[0] 0.

i=4:

L=0-3= -3 mod5=2.

R=2-3= -1 mod5=4.

So L=2, R=4.

2 <4.

diff[2] +=4.

diff[4] -=4.

i=5:

L=0-4= -4 mod5=1.

R=2-4= -2 mod5=3.

So L=1, R=3. 1 <3.

diff[1] +=1.

diff[3] -=1.

So the diff array after processing all:

i=1:

diff[0] =1, diff[2] =-1.

i=2:

diff[4] +=2 →2.

diff[0] +=2 →1+2=3.

diff[1] -=2 →-2.

i=3:

diff[3] +=3 →3.

diff[0] +=3 →3+3=6.

diff[0] -=3 →3.

i=4:

diff[2] +=4 →-1 +4=3.

diff[4] -=4 →2-4=-2.

i=5:

diff[1] +=1 →-2 +1 =-1.

diff[3] -=1 →3-1=2.

So the diff array is:

index 0:3, 1:-1, 2:3, 3:2,4:-2.

Now, compute the prefix sums:

X=0: sum=3.

X=1: sum=3-1=2.

X=2: sum=2+3=5.

X=3: sum=5+2=7.

X=4: sum=7-2=5.

So the maximum sum is7 at X=3. So h is4.

Which matches the second sample.

So this approach works.

Now, the code.

In Python, for n up to 1e5, creating a diff array of size n is feasible.

Now, code steps:

Read n.

Read a list as integers.

Read s and f.

Compute A = s-1, B = f-1.

Initialize a diff array of size n, filled with 0.

For each i in 1..n:

   current i (1-based).

   L = (A - (i-1)) % n

   R = (B - (i-1)) % n

   if L < R:

       diff[L] += a[i-1]

       diff[R] -= a[i-1]

   else:

       diff[L] += a[i-1]

       diff[0] += a[i-1]

       diff[R] -= a[i-1]

Then compute the prefix sum.

Find the X (0-based) with the maximum sum, and smallest X if tie.

h is X+1.

Now, implementing this in Python.

But for n=1e5, this should be manageable.

But in Python, for efficiency, we need to handle the list efficiently.

Sample code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    s, f = map(int, input_stream.readline().rstrip("\n").split())

    A = s-1

    B = f-1

    diff = [0]*n

    for i in range(1, n+1):

        L = (A - (i-1)) % n

        R = (B - (i-1)) % n

        ai = a[i-1]

        if L < R:

            diff[L] += ai

            if R < n:

                diff[R] -= ai

        else:

            diff[L] += ai

            diff[0] += ai

            if R < n:

                diff[R] -= ai

    # Compute prefix sum

    max_sum = -1

    current_sum =0

    best_x =0

    for x in range(n):

        current_sum += diff[x]

        if current_sum > max_sum or (current_sum == max_sum and x < best_x):

            max_sum = current_sum

            best_x = x

    h = best_x +1

    print(h, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
1 2 3 4 1
1 3
""",
            "output": \
"""\
4
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

Testing sample 2:

Yes.

Now, edge cases.

Test case where B -A =n (but since B =f-1 and f <=n, B can be up to n-1. So B -A can't be >=n).

So no problem.

Another edge case: s=2, f=2. But the problem states that s <f. So no.

So code should handle all cases.

Thus, this code should be correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
s, f = map(int, input().split())
A = s - 1
B = f - 1

diff = [0] * n

for i in range(1, n + 1):
    L = (A - (i - 1)) % n
    R = (B - (i - 1)) % n
    ai = a[i - 1]
    if L < R:
        diff[L] += ai
        diff[R] -= ai
    else:
        diff[L] += ai
        diff[0] += ai
        diff[R] -= ai

current_sum = 0
max_sum = 0
best_x = 0

for x in range(n):
    current_sum += diff[x]
    if current_sum > max_sum or (current_sum == max_sum and x < best_x):
        max_sum = current_sum
        best_x = x

print(best_x + 1)
```
