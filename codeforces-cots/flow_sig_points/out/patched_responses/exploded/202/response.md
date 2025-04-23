<think>
Okay, so I need to solve this problem where I have to insert at most one element into a sorted list of times, and find the maximum possible time the lamp is lit. Let's think through this step by step.

First, I need to understand how the lamp's state changes. The lamp starts on at time 0, and each time a in the list flips the state. Then at time M, it turns off. So the total lit time depends on the intervals between the flips where the lamp is on.

The original a array is sorted. So, when you insert a new element x, you have to put it in a position where the array remains strictly increasing. So x has to be between a[i-1] and a[i] for some i, or before the first element, or after the last (but less than M, since all elements are less than M).

The goal is to choose where to insert x (or not insert anything) to maximize the total time the lamp is on.

Hmm. Let's model the current intervals. Since the lamp starts on, the first interval is from 0 to a[0], then it's off from a[0] to a[1], on from a[1] to a[2], etc. Wait, no: each a[i] is a flip. So starting from on, each flip toggles the state. So the state after the first flip (a[0]) is off, after the second (a[1]) is on again, and so on.

Wait, let's see. The initial state is on at 0. Then, each a[i] toggles the state. So the intervals are:

0 to a[0]: on (since after a[0], it's off)
a[0] to a[1]: off (after a[0], state is off, then after a[1], toggles to on)
a[1] to a[2]: on
and so on.

Then, the last interval is from a[-1] to M. The state here depends on the number of flips. If there are even number of flips (original array length is even), then after a[-1] it's off. So the last interval (a[-1] to M) is off. If the original array is odd length, then after a[-1] it's on, so the last interval contributes (M - a[-1]) to the total.

So the original total is calculated by summing all the intervals where the lamp is on. So for each interval between flips, if the state is on during that interval, add the length. Then the final interval from a[-1] to M is considered.

Now, inserting an x into the array can change these intervals. The insertion would create a new flip at x, which will split an existing interval into two, and toggle the state in that region. The question is, where to insert x such that the sum of on intervals is maximized.

But since inserting x can be in any possible position, including the ends, we need to check all possible insertion points and see which one gives the maximum gain.

But considering that n can be up to 1e5, we need an O(n) or O(n) time solution.

Let me think: For each possible insertion position (i.e., between a[i-1] and a[i] for all possible i, or before a[0], or after a[n-1]), what is the maximum possible gain that inserting x there can bring.

But inserting x can be any value in the allowed range. Wait, but the optimal x would be the one that splits the interval in a way that the on time is maximized. However, the problem allows inserting any x that fits into the array as a good program. So the x can be chosen to optimize the gain for each possible interval.

Wait, but the inserted x must be between the previous and next element. So for example, inserting between a[i-1] and a[i], x can be any value in (a[i-1], a[i]). So to maximize the gain, the optimal x would be chosen such that it creates the maximum possible on time in the two split intervals.

But how do we model this? Let's take a particular interval where the current state is on or off, and see how inserting x can affect it.

Let me consider a general interval. Suppose between two existing flips at time s and e (s < e), and the lamp is in state 'current_state' during this interval. The current contribution to the total is (e - s) if current_state is on, else 0.

If we insert x into this interval (s < x < e), then the interval is split into s to x and x to e. The state during s to x is current_state, then after x it toggles. Then, during x to e, the state is the opposite of current_state. So the contribution for this split interval would be (x - s) * (current_state) + (e - x) * (1 - current_state). The original contribution was (e - s) * current_state. So the gain is [ (x - s) * current_state + (e - x) * (1 - current_state) ] - (e - s)*current_state = (e - x)*(1 - current_state - current_state) = (e - x)*(1 - 2*current_state). Wait, wait. Let me recalculate.

Original contribution: (e - s) * c, where c is 1 if on, 0 if off.

After insertion, the contribution becomes:

(x - s) * c + (e - x) * (1 - c)

The difference is:

[ (x - s)*c + (e - x)*(1 - c) ] - (e - s)*c 

= c(x - s) + (e - x)(1 - c) - c(e - s)

= c(x - s - e + s) + (e - x)(1 - c)

= c(x - e) + (e - x)(1 - c)

= (e - x)(1 - c - c)

= (e - x)(1 - 2c)

So the gain is (e - x)(1 - 2c). 

But in this scenario, inserting x into the interval [s, e] that's currently contributing (e-s)*c. The maximum possible gain here would be achieved by choosing x to maximize (e - x)(1 - 2c). 

But the value of (1 - 2c) depends on c. If c is 1 (current state is on), then (1-2c) is -1. So gain is (e - x)(-1) → the maximum gain would be when (e - x) is as small as possible, i.e., x as close to e as possible. But since we can choose x anywhere between s and e, but inserting x would split the interval. Wait, but inserting x here would create two intervals. But since the gain is (e -x)(-1), to maximize the gain, which is (e -x) multiplied by -1, the maximum would be when (e -x) is minimized, i.e., x approaches e. So the maximum possible gain in this case is (e - x)*-1. Wait, that's a negative number. So inserting in an interval where the current state is on would decrease the total. So that's bad. Wait, that can't be right. Let me re-examine.

Wait, original contribution is (e - s)*c. If the current state is on (c=1), then inserting x would split the interval into (x - s) * 1 (since state is on for that part) and (e - x) * 0 (since state is off after the flip). The original contribution was (e - s)*1. The new contribution is (x - s) *1. So the difference is (x - s) - (e -s) = x - e. Which is negative if x < e. So inserting x in an interval that was on would reduce the total. So inserting x in an on interval is not beneficial. So that's a loss. So inserting into an on interval is not a good idea.

On the other hand, if the current state is off (c=0), then inserting x would split the interval into (x - s)*0 (off) and (e - x)*1 (on after the flip). The original contribution was 0. The new contribution is (e - x)*1. So the gain here is (e - x) - 0 = e -x. To maximize this, we should choose x as small as possible (so x is just after s), making e -x as large as possible. So the maximum possible gain for inserting into an off interval is (e - s - 1) but x can be any value between s and e. Wait, but the maximum possible is when x is as small as possible, which is x = s + 1 (since x must be an integer between s and e). Wait, but the problem allows x to be any integer in (s, e) or in the case of inserting before a[0], x can be in (0, a[0}), etc. So to maximize e -x, x should be as small as possible. For example, inserting x = s + 1 gives the maximum possible gain of e - (s+1) = (e - s - 1). Wait, but how?

Wait, the interval between s and e is a current off interval. So inserting x anywhere in (s, e) splits it into two parts: s to x (off) and x to e (on). So the gain from inserting here is (e -x). The larger e -x is, the better. So to maximize e -x, x should be as small as possible (as close to s as possible). But x has to be an integer in (s, e). So the maximum possible gain is (e - (s+1)) = e - s -1. Wait, but x can be s+1, s+2, etc. So if we insert x = s+1, then the gain is e - (s+1) = (e - s) -1. But the maximum possible would be when x is s+1. So inserting x in an off interval gives a gain of e -x. So the maximum gain for that interval is (e - s -1), because x can be s+1.

Wait, but in the problem statement, the inserted x can be any integer such that 0 < x < M and it fits into the array as a good program, which is strictly increasing. So inserting into a current interval [s, e] (off) can give us a gain of (e - x). So to maximize this gain, x should be as small as possible, i.e., x = s + 1. But wait, s is the previous element, e is the next. So for example, between a[i-1] and a[i], the possible x is a[i-1] + 1, up to a[i] - 1. So the maximum gain for inserting into this interval is (a[i] - (a[i-1] +1)) = a[i] - a[i-1] -1. So the maximum possible gain here is (a[i] - a[i-1] -1). Because inserting x at s+1 (i.e., a[i-1]+1) gives the maximum possible (e -x) = (a[i] - (a[i-1]+1)) = a[i] - a[i-1] -1.

So for each interval between two existing points (including the start at 0 and end at M), we can compute the maximum possible gain by inserting into that interval, and choose the interval with the maximum gain.

But wait, we also need to consider inserting before the first element (if possible) and after the last element (if possible). Let's model all possible intervals:

The original intervals are:

- From 0 to a[0]: on (since after the first flip at a[0], the state is off)
- a[0] to a[1]: off
- a[1] to a[2]: on
- etc.
- The last interval is a[-1] to M. The state here depends on the parity of n. Since there are n flips, the state after a[-1] is (n % 2 == 0) ? off : on. So the last interval contributes (M - a[-1]) if the state is on.

So for the original intervals, each interval is either on or off. For each interval, we can compute the maximum possible gain if we insert into that interval.

But inserting into an on interval will decrease the total (as discussed earlier), so we should not do that. Only inserting into an off interval can potentially increase the total.

So the plan is:

1. Compute the original total on time.

2. For each interval where the state is off, compute the maximum possible gain by inserting a x into that interval.

3. The maximum of these gains (plus the original total) is the answer.

But how to model this?

First, we need to compute the original total.

Let's see. The original a array is sorted. So the intervals are:

- Between 0 and a[0], state is on.

- Between a[0] and a[1], state is off.

- Between a[1] and a[2], state is on.

- etc.

Then, between a[-1] and M: state is on if n is odd (since each flip toggles the state, starting with on. After n flips (even number), the state is off; after odd, on. Then, the last interval's state is on if n is odd.

So the original total is:

sum over all intervals where the state is on of (end - start).

So let's compute the original total.

Then, for each possible insertion interval (the intervals where inserting x can give a gain), compute the maximum possible gain for that interval.

Then, the maximum gain among all possible insertion intervals is added to the original total to get the maximum possible total.

So first step: compute the original total.

Second step: compute all possible insertion gains, and find the maximum.

But how to model the insertion gains.

Each insertion interval is between s and e. The state in that interval is on or off. For each such interval, if the state is off, then inserting x as s+1 (as small as possible in the interval) gives maximum gain of (e - x) = (e - (s+1)) = (e - s - 1). Because inserting x in that interval splits it into [s, x] (off) and [x, e] (on). The gain is (e -x) (since the original contribution is 0, and the new is (e -x)).

So for each interval where the state is off, the maximum possible gain is (e - s - 1).

But wait, what if the interval is at the beginning (0 to a[0])? Wait, no. The initial interval is 0 to a[0], which is on. So inserting there would be into an on interval, which is bad.

Wait, the possible insertion intervals are:

- Between 0 and a[0], but inserting x here is allowed only if x is less than a[0]. But in this interval, the state is on. So inserting x here would split into [0, x] (on) and [x, a[0]] (off). The original contribution was (a[0] - 0) * 1. The new contribution is (x -0)*1 + (a[0] -x)*0 = x. So the gain is x - a[0]. Since x < a[0], this is a loss. So inserting here is not good.

So the only intervals where inserting can improve the total are the ones where the state is off.

So for each interval between a[i] and a[i+1], where i is even (since the first interval is on, then a[0] to a[1] is off (i=0, which is even index?), wait, maybe we need to track the state.

Wait, the initial state is on. Each flip toggles the state. The first flip is at a[0], so after that, state is off. Then, the next flip (a[1]) toggles to on. So the intervals:

0 to a[0]: on

a[0] to a[1]: off

a[1] to a[2]: on

a[2] to a[3]: off

etc.

So the state of an interval between a[i] and a[i+1] is off if i is even (0, 2, 4, ...), but wait, let's see:

After 0 flips (initial state): on.

After 1 flip (a[0]): off.

After 2 flips (a[0], a[1]): on.

After 3 flips: off.

So the interval between a[k] and a[k+1] is on if k is odd (since after k+1 flips, the state is on if (k+1) is even), wait, perhaps it's better to model the state as follows.

Each interval between a[i-1] and a[i] (for i from 1 to n) has a state that is on if (i-1) is even (since after a[i-1], the state is (i) flips. Wait, the first interval is from 0 to a[0], which is after 0 flips (state on). Then, after a[0], state is off (1 flip). The next interval is a[0] to a[1], which is state off. After a[1], state is on (2 flips). The interval a[1] to a[2] is on. So the state of the interval between a[i] and a[i+1] is on if (i+1) is even. Wait, perhaps the parity of the number of flips up to that point.

Alternatively, the state of the interval between a[i] and a[i+1] is on if (i+1) is even. Wait, maybe another approach: for each interval between a[i] and a[i+1], the state is on if (i+1) % 2 == 0. Because the first interval (0 to a[0]) has state on (i=0, a[0] is first flip). So for interval a[i] to a[i+1], the number of flips before the interval is (i+1) (since after a[i], the state is (i+1) flips). So during this interval, the state is (i+1) % 2 == 1 ? off : on? Wait, no. Let's think:

At a[i], the state after flipping is (i+1) flips. Because the initial state is 0, then each a[i] adds a flip.

So the state after a[0] is 1 flip → off.

The state after a[1] is 2 flips → on.

So, during the interval a[i] to a[i+1], the state is determined by whether (i+1) is even or odd. Because:

For the interval between a[0] and a[1], the state is off (i=0, i+1=1, which is odd → off).

Between a[1] and a[2], i=1, i+1=2 even → on.

So the state for the interval a[i] to a[i+1] is on if (i+1) is even.

Thus, the intervals between a[i] and a[i+1] are off when (i+1) is odd, on when even.

Wait, but for the initial interval (0 to a[0]), the state is on, and it's before any flip. So that's a special case. So the intervals can be split as:

0 to a[0] → on.

Then, for each i from 0 to n-2, the interval a[i] to a[i+1] is off if (i+1) is odd, on if even.

Then, the interval a[-1] to M is on if n is even (since after a[-1], which is the nth flip, the state is on if n is even, because the number of flips is even → after even flips, the state is on again).

Wait, no. Let's think again.

Original state is on (after 0 flips).

Each flip toggles the state.

So after the first flip (a[0]), state is off.

After the second flip (a[1]), on.

After the third (a[2]), off.

So, after k flips, the state is on if k is even, off if k is odd.

So the state during the interval a[i] to a[i+1] is determined by the number of flips up to a[i], which is i+1. So after a[i], the state is (i+1) % 2. If even → on, odd → off. But wait, after a[i], the state is the result of (i+1) flips. So for the interval after a[i], which is from a[i] to a[i+1], the state is (i+1) % 2 == 0 → on, else off.

Wait, no. For example, after a[0], there's 1 flip. So state is off. So the interval a[0] to a[1] is off.

After a[1], 2 flips → on. So the interval a[1] to a[2] is on.

So the state for the interval a[i] to a[i+1] is (i+1) is even → on.

So, the interval a[i] to a[i+1] is on if (i+1) is even.

So, for each interval between a[i] and a[i+1], where i ranges from 0 to n-1, the state is on if (i+1) is even. Then, the last interval (a[-1] to M) is on if (n) is even (since after n flips, the state is on when n is even).

So the original total is:

sum of:

- a[0] - 0 (since first interval is on)

plus, for each i from 0 to n-2:

if (i+1) is even: (a[i+1] - a[i])

plus, if n is even: (M - a[-1])

Wait, no. Because:

The initial interval (0 to a[0]) is on → contributes a[0].

Then, for each interval a[i] to a[i+1], which is from i=0 to n-1 (but wait, the first interval is 0 to a[0], the next is a[0] to a[1], etc. So for a list of length n, there are n+1 intervals. Wait, no. Let's see:

The array a has n elements. The flips happen at a[0], a[1], ..., a[n-1]. So the intervals are:

0 to a[0]

a[0] to a[1]

a[1] to a[2]

...

a[n-2] to a[n-1]

a[n-1] to M.

So there are (n) + 1 intervals (n+1 intervals). Wait, no. For n elements, there are n+1 intervals (including 0 to a[0] and a[-1] to M). So for the initial example with a of size 3, there are 4 intervals.

So the initial interval (0 to a[0]) is on.

Then for each of the next intervals (a[i] to a[i+1], for i from 0 to n-2), their state is determined by (i+1) being even (since after a[i], the state is (i+1) flips → on if (i+1) is even).

Then the last interval (a[n-1] to M) is on if (n) is even.

So the original total is:

original_total = (a[0] - 0) + sum_{i=0 to n-2} (if (i+1) % 2 == 0 then (a[i+1] - a[i]) else 0) + (if n % 2 == 0 then 0 else (M - a[-1]))? Wait, wait:

Wait, the last interval is a[n-1] to M.

After the last flip (a[n-1]), the state is (n) flips. So if n is even, state is on → contributes (M - a[n-1]).

If n is odd, state is off → contributes 0.

So original_total = a[0] (from 0 to a[0]) 

plus sum_{i=0 to n-2} ( (a[i+1] - a[i]) if (i+1) % 2 == 0 else 0 )

plus (M - a[-1]) if n % 2 == 0 else 0.

So that's the original total.

Now, to compute the maximum possible gain by inserting a new x into any possible interval where inserting would give a gain.

As discussed earlier, inserting into an interval that is off can give a gain. For each such interval, the maximum possible gain is (e - s - 1), where s is the start and e is the end of the interval.

So the steps to compute the maximum gain:

1. For each interval (s, e) where the state is off, compute the possible gain (e - s - 1).

2. Find the maximum among these gains.

3. The answer is original_total + max_gain, where max_gain is the maximum possible gain (could be zero if no insertion is better than original).

So how do we find all intervals that are off?

Let's list all intervals and their state:

First interval: 0 to a[0] → on. No gain here.

Intervals between a[i] and a[i+1] (i from 0 to n-2): for each such interval, the state is on if (i+1) is even, else off.

The last interval: a[-1] to M → state is on if n is even, else off.

So the intervals that are off are:

- All intervals between a[i] and a[i+1] where (i+1) is odd.

- The last interval (a[-1] to M) if n is odd.

So for each such interval, compute (e - s - 1) where s is the start and e is the end. For example, for an interval between a[i] and a[i+1] that's off (i+1 is odd), s = a[i], e = a[i+1]. The gain is (e - s - 1). So the maximum gain possible in this interval is (a[i+1] - a[i] - 1).

For the last interval (if state is off), which is when n is odd, then s = a[-1], e = M. The gain is (M - a[-1] -1).

So the algorithm is:

Compute original_total.

Compute all possible gains from inserting into off intervals.

Take the maximum gain (if any, else zero).

The answer is original_total + max_gain.

But wait, inserting into the last interval (if it's off) can give a gain of (M - a[-1] -1). Because inserting x = a[-1] + 1 (since the interval is a[-1] to M, and x must be less than M and greater than a[-1]), so x can be a[-1] +1 up to M-1. The maximum gain is (M - x), which is maximized when x is as small as possible (x = a[-1] +1). So gain is (M - (a[-1]+1)) = M - a[-1] -1.

So now, the steps are:

1. Compute original_total.

2. For each interval between a[i] and a[i+1] where (i+1) is odd (so state is off), compute (a[i+1] - a[i] - 1) → these are possible gains.

3. If the last interval (a[-1] to M) is off (i.e., n is odd), compute (M - a[-1] -1) as another possible gain.

4. The maximum of all these possible gains is the best gain. If there are no gains (all intervals are on), then the best is zero.

Thus, the answer is original_total + max_gain.

But wait, what about inserting x before a[0]? For example, inserting x in the interval 0 to a[0], which is on. But inserting there would split the interval into 0 to x (on) and x to a[0] (off). The original contribution was a[0], and the new contribution is x + 0 → x. So the gain is x - a[0], which is negative unless x >= a[0], which is not allowed. So inserting here is not beneficial.

Similarly for inserting after a[-1], but in the last interval (if it's on). For example, if the last interval is on, inserting x there would split into a[-1] to x (on), and x to M (off). The original contribution was (M - a[-1]), the new is (x - a[-1]) → so the gain is (x - a[-1]) - (M -a[-1]) = x - M. Which is negative because x < M. So no gain.

So the only possible gains are from inserting into intervals that are off, and their maximum possible gain is (e - s -1), where e and s are the interval's endpoints.

Therefore, the approach is:

Compute the original_total as described.

Compute all possible gains for each off interval.

The maximum gain is the maximum of these gains (or zero if there are none).

The answer is original_total + max_gain.

Now, how to implement this efficiently?

First, compute the original_total.

Let's see:

original_total starts with a[0].

Then, for i from 0 to n-2:

interval is between a[i] and a[i+1]

the state is on if (i+1) is even.

So if (i+1) is even, add (a[i+1] - a[i]) to the total.

Then, if n is even, add (M - a[-1]).

So code for original_total:

original = a[0]

for i in range(n-1):

    if (i+1) % 2 == 0:

        original += a[i+1] - a[i]

if n % 2 == 0:

    original += M - a[-1]

Then, compute max_gain.

max_gain = 0

Check all intervals between a[i] and a[i+1] where (i+1) is odd. For each, compute (a[i+1] - a[i] -1) and track the maximum.

Also, check the last interval if n is odd: compute (M - a[-1] -1).

So:

for i in range(n-1):

    if (i+1) % 2 == 1:

        current_gain = a[i+1] - a[i] - 1

        if current_gain > max_gain:

            max_gain = current_gain

if n % 2 == 1:

    current_gain = M - a[-1] - 1

    if current_gain > max_gain:

        max_gain = current_gain

So the answer is original + max_gain.

But wait, what about inserting into the first interval (0 to a[0])? Oh, right, but that interval is on, so inserting x there would decrease the total.

So the code should be as described.

Now, testing the examples.

First example:

Input: 3 10

4 6 7

Original a: [4,6,7], M=10.

Original_total:

a[0] =4.

i ranges from 0 to 2-1=1 (i=0 and 1)

For i=0:

i+1=1 → odd → no addition.

For i=1:

i+1=2 → even → add (a[2] - a[1] )=7-6=1 → original becomes 4+1=5.

n is 3 → odd. So check if n is even? No. So last interval (7 to 10) is off. But original_total does not add anything for that. So original_total is 5.

Wait, no. Wait, original_total is:

original = a[0] =4.

Then, for i from 0 to n-2 = 1 (i=0 and 1):

i=0: (i+1) =1 → odd → no addition.

i=1: (i+1)=2 → even → add (7-6=1) → original becomes 5.

n is 3 (odd), so the last interval's contribution is (M - a[-1]) only if n is even. Since n is odd, no. So original_total is 5.

Now, compute the gains:

Check intervals between a[i] and a[i+1], where (i+1) is odd.

For i=0: i+1=1 → odd. Interval 4-6. gain is 6-4-1=1.

i=1: i+1=2 → even. Not considered.

i=2 is n-1? No, because for the intervals between a[i] and a[i+1], i ranges up to n-2. So in this case, n=3, n-2=1. So the loop for i in 0..1.

So for i=0: gain 1.

i=1: (i+1)=2 → even, not considered.

Also, check the last interval (a[-1] to M=10), since n is 3 (odd). So current_gain is 10-7-1=2. So max_gain starts at 0.

After checking i=0, max_gain is 1.

Then, check last interval: 10-7-1=2. So max_gain becomes 2.

So the answer is 5 + 2=7. But the sample output is 8. Wait, what's wrong?

Wait, the sample input says the correct answer is 8. But according to this code, original_total is 4 + (i=1 gives 1) → 5, and max_gain is 2. So 5+2=7. Which contradicts the sample.

Hmm, so there's a mistake here.

Wait, the sample's original program is [4,6,7]. Let's compute the original total:

Original intervals:

0-4: on → contributes 4.

4-6: off → 0.

6-7: on → 7-6=1.

7-10: off (since after 3 flips, state is off). So no contribution.

Total is 4 +1 =5. But the sample's explanation says that inserting x=3 into the program (so the new a is [3,4,6,7]) gives a total of 3-0 (on) + (4-3) off, 6-4 on (2), 7-6 off, 10-7 on (3). Sum:3 +2 +3=8.

But according to the code's calculation, original_total is 5, and the maximum gain is 2 (from inserting into the last interval, 7-10: gain is 10-7-1=2). So 5+2=7. But sample answer is 8. So something is wrong.

Wait, what's wrong here? Oh! The original_total in the first example is 4 (from 0-4) plus (6-4)*0 (off) → no addition. Then the next interval (6-7) is on (since i=1, i+1=2 even), so add 1. Then, since n=3 (odd), the last interval is off. So original_total is 4+1=5. Then the maximum gain comes from inserting into the interval 4-6 (gain 1) or inserting into the last interval (7-10) gives gain 2.

But according to the sample, inserting x=3 gives a gain of 3 (3 is inserted in the first interval, which is on, but according to our model that's not possible). So why is the sample's answer 8?

Wait, perhaps the code's logic is incorrect.

Ah, here's the mistake: the code's logic for gains is considering inserting into intervals that are off. But the sample's insertion is into the initial interval (0-4), which is on. But according to the model, inserting into an on interval would decrease the total. But in the sample, inserting x=3 into the initial on interval increases the total.

So clearly, there's a mistake in the model.

What's wrong here?

Wait, inserting x=3 into the first interval (0-4) which is on.

Original interval contributes 4-0=4.

After inserting x=3, the first interval splits into 0-3 (on) and 3-4 (off). The contribution is 3-0=3 (from on) + 0 (from off). So the total for this interval is 3, which is a loss of 1. But in the sample's explanation, inserting x=3 gives a new program that adds 3,4,6,7. Let's compute the intervals:

0-3 → on.

3-4 → off.

4-6 → on.

6-7 → off.

7-10 → on.

Original intervals:

0-4 on (4)

4-6 off (0)

6-7 on (1)

7-10 off (0). Original total is 5.

After inserting 3:

0-3 → on (3)

3-4 → off (0)

4-6 → on (2)

6-7 → off (0)

7-10 → on (3). So total is 3+2+3=8. Which is a gain of 8-5=3.

So the maximum gain is 3. So according to the model, why isn't this captured?

Because inserting into the initial on interval (0-4) would split into two intervals, but according to the model, inserting into an on interval would decrease the total. But in this case, inserting x=3 into the initial on interval actually leads to a gain.

This suggests that the model is incorrect. So where's the error?

Ah, the model assumes that inserting into on intervals gives a loss, but in this case, inserting into the initial interval (on) leads to a gain. So the model is wrong.

What's wrong here?

The original model for gains in on intervals assumed that inserting x into an on interval would split it into x-s and e-x. The original contribution is (e-s). The new is x-s (on) + (e-x) (off). So the gain is (x-s) + 0 - (e-s) = x - e. So for inserting into an on interval, the gain is (x - e). But x must be between s and e (0 and a[0] in the first example). So x can be up to a[0]-1. So the gain is x - a[0]. Which is negative. But in the sample, inserting x=3 into the initial interval (0-4) gives a gain of 3-4 = -1. So according to this, the gain is -1. But in the sample, the total after insertion is 8, which is an increase of 3 from the original total of 5. So how is this possible?

Wait, the original total is 5. After inserting x=3, the new total is 8, which is a gain of 3. But according to the model, inserting into an on interval gives a loss. So this suggests that the model is missing some cases.

Ah! Oh, right. Because inserting x can also affect other intervals. For example, inserting x into an interval changes the parity of the following intervals.

Wait, the model's approach was to compute the original total and then find the maximum gain by inserting into an off interval, assuming that inserting into other intervals does not affect the parity of subsequent intervals. But this is incorrect.

Because inserting x into the array changes the flip count. For example, inserting x into the initial on interval (0-4) adds a new flip. So after inserting x=3, the array becomes [3,4,6,7]. The flips are now 4 elements. So the state transitions are:

0 → on (0 flips)

3 → off (1)

4 → on (2)

6 → off (3)

7 → on (4)

Then M=10 → off (after 4 flips, even, so on, but power is off. So the last interval (7-10) is on. So contribution is 3 (from 0-3) + (4-3) is off (0) + (6-4) is on (2) + (7-6) is off (0) + (10-7) is on (3) → total 3+2+3=8.

But the original model for gains is only considering inserting into the existing intervals and their current state. However, inserting x into a certain interval not only splits that interval but also shifts all subsequent flips, which changes the state of all the following intervals.

Therefore, the previous approach is wrong. Oh no! So the initial approach is incorrect. Because inserting x into the array changes the parity of the following intervals.

This is a big problem.

So the previous approach of computing gains based on the current intervals is invalid, because inserting x changes the number of flips, which affects the parity of all subsequent intervals.

So the problem is more complex than initially thought.

This explains why the first sample's answer wasn't captured by the initial model.

So what's the correct approach here?

Hmm. So inserting x into the array can change the state transitions for all subsequent elements. Therefore, the gain isn't simply calculated based on the current interval's state but depends on how the insertion affects the entire array.

So this complicates things. The previous approach is incorrect, and a different strategy is needed.

Alternative approach:

The total time is determined by the sequence of flips. Each flip toggles the state.

We can model the lamp's state over time as a series of intervals, and inserting a new flip at x will split an interval into two, toggling the state in the process.

The problem is to find the x that can be inserted into the array (at most one) such that the total on time is maximized.

So for each possible insertion point (i.e., between a[i-1] and a[i], or before a[0], or after a[n-1]), and for each possible x in that interval, compute the new total on time. Then find the maximum.

But this is computationally infeasible for n=1e5, as the number of possibilities is O(n), and each requires O(1) or O(n) time.

Thus, the problem requires finding a way to model the best possible x insertion in O(n) time.

Alternative idea: for each possible insertion interval (the intervals where x can be inserted), compute the maximum possible gain that can be achieved by inserting x into that interval. The gain here must take into account the effect on all subsequent intervals.

But how to compute this efficiently.

Let's think of inserting x into position i (i.e., between a[i-1] and a[i], or before a[0], etc.). Inserting x into position i adds a new flip at x, which affects the parity of the flips after x. So the state transitions after x will be different.

So inserting x changes the flip count for all elements after x. For example, inserting x into the array at position i increases the number of flips by 1. So all flips after x will now have their parity shifted.

Thus, the effect of inserting x into the array is to split one interval into two and invert the parity of all intervals after x.

This is a major complication. So the gain from inserting x is not just the gain from splitting the current interval, but also the gain from the parity inversion of all subsequent intervals.

This makes the problem much more challenging.

So how to model this?

Let's think about the original array. Each interval between two consecutive flips (or between 0 and first flip, or last flip and M) has a certain state (on or off). Inserting x into interval j (which is between s and e) splits it into two intervals. The state of the first split interval is the same as the original, and the second split interval is the opposite. Then, all subsequent intervals (after x) have their state flipped.

Thus, inserting x into interval j will:

1. Split interval j into two parts, with a possible gain based on the split.

2. Flip the state of all intervals after j.

Therefore, the total gain from inserting x into interval j is:

gain_split (from splitting j into two parts) + gain_flip (from flipping the state of all intervals after j).

The gain_split is the same as before: for interval j, which originally contributes (e - s) * c, after inserting x, it becomes (x - s)*c + (e -x)*(1 -c) → gain_split = (x -s)*c + (e -x)*(1-c) - (e-s)*c = (e -x)(1 - 2c).

The gain_flip is the sum over all intervals after j of (new_contribution - old_contribution). Since the state is flipped for each of these intervals, their contribution changes from (e - s)*c to (e - s)*(1 -c). So the gain_flip for each such interval is (e - s)*(1 - 2c). Summing over all these intervals gives the total gain_flip.

So the total gain is gain_split + gain_flip.

Now, inserting x into interval j (the original j-th interval) can have different gains depending on where x is inserted and what the original state is.

But given that inserting x into interval j and the best possible x for that interval would be to maximize the gain_split + gain_flip.

But how to compute this for each j efficiently?

For each possible j (the original interval), compute the maximum possible gain_split + gain_flip.

The maximum gain_split is achieved by choosing x to maximize (e -x)(1 - 2c) + gain_flip. But x is constrained to be in the interval (s, e), and the choice of x affects gain_split.

But gain_flip is fixed once j is chosen. Because gain_flip depends on which intervals are flipped (all after j), not on x. So for a given j, gain_flip is fixed.

Therefore, for each j, the maximum possible gain_split is (max possible (e -x)(1-2c)) + gain_flip.

But since x can be any value in (s, e), the maximum of (e -x)(1-2c) depends on the sign of (1-2c).

If (1-2c) is positive (i.e., c=0), then (e -x) should be as large as possible. So x is as small as possible. So x = s +1 → gain_split = (e - (s+1)) *1.

If (1-2c) is negative (i.e., c=1), then (e -x) should be as small as possible. So x = e-1 → gain_split = (e -x)*-1. Which would be -1*(1) = -1. So inserting into a on interval (c=1) would give a negative gain_split, but perhaps the gain_flip could be positive and overall gain could be positive.

Thus, the maximum gain for inserting into interval j is:

if j's state is off (c=0):

gain_split_max = (e - s - 1) *1 → since x is s+1, (e - (s+1)) = e -s -1.

gain_flip is the sum of (e_i - s_i) * (1 - 2c_i) for all intervals after j. But since inserting x into j flips the state of all intervals after j, each interval after j contributes (e_i - s_i) * (1 - 2c_i) where c_i is their original state. Because flipping their state (from c_i to 1 - c_i) changes the contribution by (1 - 2c_i) * (e_i - s_i).

So for each j, we need to compute:

gain_split_max (for j's state) + sum over all intervals after j of (1 - 2*c_i) * (e_i - s_i).

So the algorithm would be:

Compute for each interval j:

- the state c of the interval j.

- compute gain_split_max (if c is off (0), then (e-s-1), else for on, (e-s-1)*-1 → but inserting into on is only possible if x is chosen to minimize (e-x), leading to negative gain_split).

But inserting into on interval may still be beneficial if the gain_flip is positive and larger than the loss from gain_split.

So the maximum possible gain is the maximum over all j (including intervals) of (gain_split_max_j + gain_flip_j).

But how to compute this for each j efficiently.

First, precompute the original intervals and their state.

Then, for each j in 0 to m (where m is the number of intervals), compute gain_split_max and gain_flip_j.

But with n up to 1e5, and m up to 1e5+1, this is O(n), which is manageable.

So the steps:

1. Split the timeline into intervals, note their start (s), end (e), state (c).

2. For each interval j, compute gain_split_max_j (depends on c_j).

3. For each interval j, compute gain_flip_j: sum of (1-2c_i) * (e_i - s_i) for all intervals i > j.

4. The maximum possible gain is the maximum of (gain_split_max_j + gain_flip_j) over all j.

The answer is original_total + max_gain.

But how to compute gain_flip_j efficiently.

We can precompute a suffix array where suffix[j] is the sum of (1-2c_i) * (e_i - s_i) for all i >= j.

Then, for each j, gain_flip_j is suffix[j+1], because inserting into j affects intervals after j (i > j).

So:

Compute a list of intervals.

Compute for each interval i, the value (1-2c_i) * (e_i - s_i). Let's call this delta_i.

Then, compute the suffix sum array: suffix[j] = sum_{i=j}^{m-1} delta_i.

So, for each j, gain_flip_j = suffix[j+1].

Then, for each interval j, gain_split_max_j is (e_j - s_j -1) if c_j is 0, else (s_j +1 - e_j) if c_j is 1 (but inserting into on intervals may lead to negative gain_split_max_j).

Wait, for c_j is 0 (off):

gain_split_max_j = (e_j - s_j -1) *1 → since (1-2c) is 1.

For c_j is 1 (on):

gain_split_max_j is (e_j - x) * (1-2c_j) → (e_j - x) * (-1). To maximize this, x should be as close to e_j as possible. But x has to be < e_j and > s_j. So x can be e_j -1. So the gain_split_max_j is (e_j - (e_j-1)) * (-1) = (1)*-1 = -1. Which is a loss. So inserting into an on interval gives a gain_split_max_j of -1.

But perhaps the gain_flip_j is positive enough to offset this.

So for each interval j, compute:

gain_split_max_j = (e_j - s_j -1) if c_j is 0,

gain_split_max_j = -1 if c_j is 1.

Then, total_gain_j = gain_split_max_j + gain_flip_j.

The maximum total_gain_j over all j is the answer.

So the algorithm is:

1. Compute the original intervals and their state.

2. Compute delta_i for each interval i.

3. Compute the suffix sums of delta_i.

4. For each interval j, compute gain_split_max_j and gain_flip_j = suffix[j+1].

5. Find the maximum total_gain_j.

6. The answer is original_total + max(total_gain_j, 0).

Because inserting is optional; if all total_gain_j are negative, the best is to do nothing.

Now, let's re-calculate the first sample with this approach.

Sample 1:

n=3, M=10, a=[4,6,7].

The intervals are:

0-4 (c=1, on).

4-6 (c=0, off).

6-7 (c=1, on).

7-10 (c=0, off).

Wait, no.

Wait, the original intervals are:

0 to a[0] (4): c is on.

Between a[0] and a[1] (4-6): i=0. i+1=1 → odd. So state is off (c=0).

Between a[1] and a[2] (6-7): i=1. i+1=2 → even. So state is on (c=1).

Then, the last interval (7-10): n=3 (odd). After 3 flips, state is off. So state is off (c=0).

So the intervals:

0-4: c=1.

4-6: c=0.

6-7: c=1.

7-10: c=0.

Now, compute delta_i for each interval:

delta_i = (1 - 2*c_i) * (e_i - s_i).

For interval 0: delta_0 = (1-2*1)*(4-0) = (-1)*4 = -4.

Interval 1: delta_1 = (1-0)*(6-4) = 2.

Interval 2: delta_2 = (1-2*1)*(7-6) = (-1)*1 = -1.

Interval 3: delta_3 = (1-0)*(10-7) = 3.

Suffix sum array is computed from the end.

suffix[3] = delta_3 =3.

suffix[2] = delta_2 + suffix[3] → -1 +3=2.

suffix[1] = delta_1 + suffix[2] → 2 +2=4.

suffix[0] = delta_0 + suffix[1] → -4 +4=0.

So the suffix array is:

suffix = [0,4,2,3].

Wait, indexes 0 to 3.

For j=0 (interval 0-4, c=1):

gain_split_max_j is -1 (since c=1).

gain_flip_j = suffix[j+1] = suffix[1] =4.

total_gain_j = -1 +4=3.

For j=1 (interval 4-6, c=0):

gain_split_max_j = (6-4-1) =1.

gain_flip_j = suffix[2] =2.

total_gain_j =1+2=3.

For j=2 (interval6-7, c=1):

gain_split_max_j is -1.

gain_flip_j = suffix[3] =3.

total_gain_j =-1 +3=2.

For j=3 (interval7-10, c=0):

gain_split_max_j= (10-7-1) =2.

gain_flip_j= suffix[4] → which is 0 (since j+1=4 is beyond the list).

So total_gain_j= 2 +0=2.

So the maximum total_gain_j is 3, achieved at j=0 and j=1.

So the answer is original_total +3.

Original_total is 4 (0-4) + (6-4)*0 (off) + (7-6)*1 (on) + (10-7)*0 (off) →4+0+1+0=5. So 5+3=8, which matches the sample.

Ah, this model now works for the first sample.

So the correct approach is to compute both the gain from splitting and the gain from flipping all subsequent intervals.

Now, the code needs to:

1. Generate all the intervals with their start, end, and state.

2. Compute delta_i for each interval.

3. Compute the suffix sums of delta_i.

4. For each interval j, compute gain_split_max_j and gain_flip_j.

5. Find the maximum total_gain_j.

Let's code this.

The steps:

First, generate the intervals.

The first interval is 0 to a[0], state is on (c=1).

Then, for each i from 0 to n-2:

interval is a[i] to a[i+1], state is (i+1) even → on (c=1) if (i+1) even, else off (c=0).

Then, the last interval is a[-1] to M. State is on if n even (c=1), else off (c=0).

Once the intervals are generated, compute delta_i for each.

Then, compute the suffix sums.

Then, for each interval j:

if c_j is 0 (off):

gain_split_max_j = (e_j - s_j -1) * 1.

else:

gain_split_max_j = -1.

gain_flip_j = suffix[j+1] (if j+1 < len(intervals), else 0).

total_gain_j = gain_split_max_j + gain_flip_j.

Compute the maximum of these.

Now, coding this.

Sample code:

Read n and M.

Read a list.

Generate the intervals.

intervals = []

# first interval is 0 to a[0], state is on.

intervals.append( (0, a[0], 1) )

# then intervals between a[i] and a[i+1]

for i in range(n-1):

    s = a[i]

    e = a[i+1]

    # state is on if (i+1) is even.

    c = 1 if (i+1) % 2 == 0 else 0

    intervals.append( (s, e, c) )

# last interval a[-1] to M

s = a[-1]

e = M

# state is on if n is even.

c = 1 if n % 2 == 0 else 0

intervals.append( (s, e, c) )

# compute delta for each interval.

delta = []

for s, e, c in intervals:

    delta_i = (1 - 2*c) * (e - s)

    delta.append(delta_i)

# compute suffix sums.

m = len(intervals)

suffix = [0]*(m+1) # suffix[i] = sum delta[i], delta[i+1], ..., delta[m-1]

for i in range(m-1, -1, -1):

    suffix[i] = delta[i] + suffix[i+1]

# compute max_gain.

max_gain = 0

for j in range(m):

    s_j, e_j, c_j = intervals[j]

    if c_j == 0:

        # off state.

        gain_split = e_j - s_j -1

    else:

        # on state.

        # inserting x in on state's interval gives gain_split of -1.

        gain_split = -1

    gain_flip = suffix[j+1]

    total = gain_split + gain_flip

    if total > max_gain:

        max_gain = total

answer = original_total + max_gain if max_gain > 0 else original_total

But wait, the original_total can be computed as the sum of (e -s)*c for each interval.

Yes. So original_total can be computed as the sum over all intervals of (e -s) * c.

So:

original_total = sum( (e - s) * c for s, e, c in intervals )

Which is simpler.

So for the first sample:

sum (4-0)*1 + (6-4)*0 + (7-6)*1 + (10-7)*0 = 4 +0 +1 +0 =5.

Yes.

Now, the code:

Read n and M.

Read a as list.

Generate intervals.

Compute original_total.

Compute delta.

Compute suffix.

Compute max_gain.

Add to original_total.

So this code should handle all cases.

Now, let's test the second sample.

Sample 2:

input:

2 12

1 10

Output:9.

Original a is [1,10], M=12.

The intervals are:

0-1: on.

1-10: state is i+1=1 (i=0) → odd → off.

10-12: state is on if n is even (n=2 even → yes).

So intervals:

0-1, c=1.

1-10, c=0.

10-12, c=1.

delta for each interval:

delta0: (1-2*1)*(1-0) =-1 *1 =-1.

delta1: (1-0)*(10-1) = 9.

delta2: (1-2*1)*(12-10) = -1*2 =-2.

suffix array:

suffix[3] =0.

suffix[2] =-2 +0 =-2.

suffix[1] =9 + (-2) =7.

suffix[0] =-1 +7 =6.

For each j:

j=0 (interval 0-1, c=1):

gain_split =-1.

gain_flip = suffix[1] =7.

total =-1+7=6.

j=1 (interval1-10, c=0):

gain_split=10-1-1=8.

gain_flip = suffix[2] =-2.

total=8-2=6.

j=2 (interval10-12, c=1):

gain_split=-1.

gain_flip=0.

total=-1.

max_gain is 6.

original_total is (1-0)*1 + (10-1)*0 + (12-10)*1 →1 +0 +2=3. So 3+6=9. Which matches the sample.

Sample 3:

input:

2 7

3 4

output:6.

Original a is [3,4], M=7.

intervals:

0-3: on.

3-4: i=0, i+1=1 → odd → off.

4-7: n=2 even → on.

delta0: (1-2*1)*3 =-3.

delta1: (1-0)*1 =1.

delta2: (1-2*1)*3 =-3.

suffix sums:

suffix[3] =0.

suffix[2] =-3.

suffix[1] =1 + (-3) =-2.

suffix[0] =-3 + (-2) =-5.

For each j:

j=0 (0-3, c=1):

gain_split =-1.

gain_flip = suffix[1] =-2.

total-3.

j=1 (3-4, c=0):

gain_split=4-3-1=0.

gain_flip= suffix[2]=-3.

total=0-3 =-3.

j=2 (4-7, c=1):

gain_split=-1.

gain_flip=0.

total=-1.

max_gain is -1. So answer is original_total +0 (since max_gain is negative). original_total is (3-0)*1 + (4-3)*0 + (7-4)*1 →3+0+3=6.

Which matches the sample.

Thus, the code should work.

Now, implement this in Python.

The code will:

Read n and M.

Read a as a list of integers.

Generate the intervals.

Compute original_total.

Compute delta and suffix sums.

Compute max_gain.

Output original_total + max_gain if max_gain >0, else original_total.

Now, coding this.

But in Python, for large n (up to 1e5), this code should be O(n) time and memory.

But for the intervals, when n is up to 1e5, the number of intervals is n+1 (n-1 intervals between the a's, plus 0 to a[0], plus a[-1] to M). So O(n) intervals.

Computing delta and suffix sum is O(n), which is acceptable.

Thus, the code should handle the constraints.

Now, code:

Read n, M.

a = list of integers.

Generate intervals.

intervals = []

# first interval

if n ==0:

    # but n >=1.

    pass.

intervals.append( (0, a[0], 1) )

for i in range(n-1):

    s = a[i]

    e = a[i+1]

    state = 1 if (i+1) %2 ==0 else 0

    intervals.append( (s, e, state) )

# last interval

s = a[-1]

e = M

state = 1 if n%2 ==0 else 0

intervals.append( (s, e, state) )

original_total = sum( (e -s)*c for s,e,c in intervals )

delta = [ (1-2*c)*(e-s) for s,e,c in intervals ]

m = len(intervals)

suffix = [0]*(m+1)

for i in range(m-1, -1, -1):

    suffix[i] = delta[i] + suffix[i+1]

max_gain = 0

for j in range(m):

    s_j, e_j, c_j = intervals[j]

    if c_j ==0:

        gain_split = e_j - s_j -1

    else:

        gain_split = -1

    gain_flip = suffix[j+1]

    total = gain_split + gain_flip

    if total > max_gain:

        max_gain = total

answer = original_total + max_gain if max_gain >0 else original_total

print(answer)

But wait, in Python, for lists, it's more efficient to precompute the intervals and delta as lists.

But the code should be correct.

Testing the first sample:

n=3, M=10, a=[4,6,7].

intervals are:

0-4: c=1.

4-6: c=0.

6-7: c=1.

7-10: c=0.

delta:

0-4: (1-2*1)*4= -4.

4-6: (1-0)*2=2.

6-7: (1-2*1)*1= -1.

7-10: (1-0)*3=3.

suffix sums:

suffix[3] =3.

suffix[2] =-1 +3=2.

suffix[1] =2 +2=4.

suffix[0] =-4 +4=0.

Then for j=0:

c=1 → gain_split -1.

gain_flip = suffix[1] =4 → total 3.

j=1:

c=0 → gain_split 2-4-1=6-4-1=1? Wait, no. s_j=4, e_j=6. e_j -s_j -1=6-4-1=1.

gain_flip = suffix[2]=2 → 1+2=3.

j=2: c=1 → gain_split -1 + suffix[3] = -1+3=2.

j=3: c=0 → 10-7-1=2. gain_flip suffix[4] =0. total 2+0=2.

Max_gain is 3.

original_total=4+0+1+0=5.

5+3=8.

Which is correct.

Thus, the code is correct.
</think>

```python
n, M = map(int, input().split())
a = list(map(int, input().split()))

intervals = []
# First interval: 0 to a[0], state on (c=1)
intervals.append((0, a[0], 1))

# Intervals between a[i] and a[i+1]
for i in range(n-1):
    s = a[i]
    e = a[i+1]
    # State is on if (i+1) is even
    state = 1 if (i+1) % 2 == 0 else 0
    intervals.append((s, e, state))

# Last interval: a[-1] to M
s = a[-1]
e = M
# State is on if n is even
state = 1 if n % 2 == 0 else 0
intervals.append((s, e, state))

original_total = sum((e - s) * c for s, e, c in intervals)

# Compute delta for each interval
delta = [(1 - 2 * c) * (e - s) for s, e, c in intervals]

m = len(intervals)
suffix = [0] * (m + 1)  # suffix sums

for i in range(m-1, -1, -1):
    suffix[i] = delta[i] + suffix[i+1]

max_gain = 0
for j in range(m):
    s_j, e_j, c_j = intervals[j]
    if c_j == 0:
        gain_split = e_j - s_j - 1
    else:
        gain_split = -1
    gain_flip = suffix[j+1]
    total = gain_split + gain_flip
    if total > max_gain:
        max_gain = total

answer = original_total + max_gain if max_gain > 0 else original_total
print(answer)
```