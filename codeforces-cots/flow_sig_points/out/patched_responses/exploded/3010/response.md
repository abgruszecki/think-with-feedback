<think>
Okay, I need to solve this problem where two beavers are playing a game with logs. The goal is to determine who wins given the initial conditions. Let's think through this step by step.

So, the problem statement says that each turn, a beaver takes a log and splits it into some number of equal parts. Each part must be an integer length and at least k meters. The key here is that the split has to result in parts of equal length. And the beaver who can't make a move loses. Timur goes first.

First, I need to model the game state. Each log can be considered a pile in a game of Nim, and the Grundy number (or mex) concept from combinatorial game theory might come into play here. The outcome of the entire game would be the XOR of the Grundy numbers of each individual log. If the XOR is non-zero, Timur wins; otherwise, Marsel does.

So, the problem reduces to calculating the Grundy number for a single log of length m, then combining all logs (n instances of this) to compute the overall XOR.

But how to compute the Grundy number for a log of length m?

Let's think recursively. For a log of length L, the possible moves are to split it into t parts, each of length s, where t >= 2, and s >= k. Also, since splitting into t parts requires that t*s = L. So s must be a divisor of L, and s >=k. But t must be at least 2, so s must be <= L/2. Wait, no. Wait, t can be any number >=2 as long as t*s = L. For example, if L is 15, and k is 4, you can split into 3 parts of 5 each (3*5=15). Here, s=5, which is >=k=4. So for a given L, the possible splits are determined by the divisors of L that are >=k and allow t >=2.

Wait, but for each possible split, we can split into t parts of s length. Each of those parts will then have their own Grundy numbers. The Grundy number of the current log is the mex (minimum excludant) of all possible outcomes from splitting the log.

The outcome when splitting into t parts of s is the XOR of t copies of the Grundy number of s. However, since all the t parts are the same, their XOR would be the Grundy number of s XORed t times. But since XORing a number with itself an even number of times cancels out (a XOR a = 0), and an odd number gives the number itself, the total for t copies would be 0 if t is even, and g(s) if t is odd. But wait, that's only when t is even or odd. So for example, if t is 3, then the XOR is g(s) XOR g(s) XOR g(s) = (g(s) XOR g(s)) XOR g(s) = 0 XOR g(s) = g(s). For t=2, it's g(s) XOR g(s) = 0. For t=4, 0. So the XOR of t copies of g(s) is 0 if t is even, and g(s) if t is odd.

But this complicates things. However, in the game theory context, when you split a log into t parts, the resulting position is a collection of t sub-logs, each of which has their own Grundy number. The Grundy number of the resulting position is the XOR of all t of their Grundy numbers. Then, the current log's Grundy number is the mex of all possible XORs obtained from all possible splits.

Hmm. So for a given log length L, to compute g(L), we need to look at all possible splits into t >=2 parts of s each (so s = L/t, and s >=k, and s must be an integer >=k). For each possible split, compute the XOR of t copies of g(s), then take the mex of all those XOR values.

But this seems computationally intensive for large L. However, the constraints here are up to 1e9 for n, m, k. So we need a way to compute this efficiently without recursion.

Alternatively, maybe there's a pattern or mathematical property that allows us to compute the Grundy number for each log in O(1) time, after some pre-processing.

Let's think about possible splits. For a log of length L, the possible splits are into t parts where t is a divisor of L, s = L/t >=k, and t >=2. So for each possible t (divisors of L) where t >=2 and L/t >=k, we can split the log into t parts of size s.

But for each such split, the resulting XOR is the XOR of t copies of g(s). As before, if t is even, the XOR is 0. If t is odd, it's g(s).

But wait, for example, if t is 3, then the XOR is g(s) XOR g(s) XOR g(s) = g(s). If t is 4, then XOR is 0.

So, the possible outcomes for splitting into t parts are 0 (if t is even) or g(s) (if t is odd).

So for each possible split (s, t), we have two possibilities:

- If t is even, contributes 0 to the mex calculation.
- If t is odd, contributes g(s) to the mex calculation.

But also, s must be >=k, and t must be >=2.

So, the mex for g(L) is the smallest non-negative integer not present in the set {0 (if even t), g(s) (if odd t)} for all possible splits.

But how to find this mex?

Alternatively, let's consider that for each possible split, the possible mex candidates are either 0 or some g(s). So the mex is either 0, 1, etc., depending on the presence of these values.

But perhaps the key is to find for each L, whether the number of possible splits' XOR values (which contribute to the mex) can be determined, and then find the mex.

But even this seems difficult. Let's look for patterns.

Let's try small examples.

Example 1:

Sample Input 1: 1 15 4.

The log is 15, k=4. The possible splits are into t parts where s = 15/t >=4, and t >=2.

Possible t's:

t must divide 15. Possible t >=2: 3,5,15. But s must be >=4.

t=3 → s=5, which is >=4. So split into 3 parts. t is odd, so the outcome is g(5).

t=5 → s=3, which is less than 4. So invalid.

t=15 → s=1, invalid.

So the only possible split is t=3 (odd). So the mex is the mex of the set {g(5)}.

So to compute g(15), we need to compute the mex of all possible splits. In this case, the possible outcomes are {g(5)}. The mex is the smallest non-negative integer not in this set.

So what is g(5)?

For L=5, k=4. Possible splits: t >=2, s >=4. So t can be 2, 5 (but 5 is 5/t=1, which is <4). t=2: s=5/2=2.5 → but s must be integer. So no possible splits. Thus, g(5) is 0.

So for L=5, the mex is 0 (no possible splits), so g(5) = 0.

So for L=15, the possible outcome is {0}. The mex is 1, so g(15) = 1.

But then the XOR for the initial log (n=1) is 1, which is non-zero. Timur wins.

Which matches the sample.

Another example: sample input 2 is 4 9 5.

Each log is 9, k=5. Let's compute g(9).

Possible splits: t >=2, s=9/t >=5. So s must be integer.

Possible t's: t=2 → 9/2 is 4.5, not integer. t=3 → 3. So s=3, which is <5. So no possible splits. So g(9) is 0. Then XOR of 4 zeros is 0. So Marsel wins.

So the key is to compute for each log (length m) its Grundy number, then XOR all n copies. If the result is non-zero, Timur wins, else Marsel.

The problem now reduces to calculating the Grundy number for m. Then, if n is even, the XOR is 0 (if the grundy is 0) or grundy XOR ... (even times). Wait, no. Because when you have n copies of the same grundy number, the XOR is grundy if n is odd, 0 if even. So for example, if each log's grundy is x, then the total XOR is x if n is odd, 0 if even. Because x XOR x ... (n times) is x when n is odd, 0 when even.

So the overall XOR is (g(m) if n is odd) XOR (0 if n is even) → but since XORing with 0 doesn't change it, the result is (g(m) * (n mod 2)).

Wait, yes. Because XORing n copies of x is x if n is odd, 0 if even.

So, the total game's outcome depends on whether the XOR of all n grundy numbers is non-zero. Since all are the same (each log is m), this is equivalent to (g(m) !=0) and (n is odd), OR (g(m) !=0) and (n is even) → but no, the XOR is g(m) XOR g(m) ... n times. Which is 0 if n is even, g(m) if odd. So the total XOR is non-zero if and only if (g(m) !=0 and n is odd) OR (g(m) !=0 and n is even but XOR is 0? No. Wait, XOR of even number of same non-zero numbers is zero. So the total XOR is zero when either:

- All grundy numbers are zero, regardless of n.

OR

- The grundy numbers are non-zero, but their count is even.

Otherwise, if the grundy is non-zero and n is odd, then XOR is non-zero.

So to compute the total XOR, it's (g(m) if n is odd else 0) XOR (0 for the rest, since others are even and cancel out).

Wait no. For n copies of x:

if x is 0, XOR is 0.

Else, for n even, XOR is 0.

For n odd, XOR is x.

So the total XOR is x * (n mod 2).

So the total game's grundy number is (g(m) * (n % 2)).

If this is non-zero, Timur wins. Else Marsel.

So the key is to compute whether the grundy number of m is non-zero and multiplied by n's parity (n mod 2) is non-zero. Which simplifies to:

if n is even: total is zero → Marsel wins if g(m) is zero or not?

Wait, no. Because even if g(m) is non-zero, but n is even, then XOR is zero. So Marsel wins.

So the total XOR is non-zero (Timur wins) if and only if g(m) is non-zero AND n is odd.

So the steps are:

1. Compute the grundy number for m. Let's call it g.

2. If g is zero: the total XOR is zero → Marsel wins.

3. Else, check if n is odd. If yes → Timur wins. Else → Marsel.

Therefore, the problem reduces to calculating whether the grundy number of m is non-zero and n is odd.

So the main task is to compute g(m). How?

Now, how to compute g(m). Let's think recursively, but find a way to compute it efficiently.

Let's model the grundy number for a log of length L. The grundy number is 0 if there are no possible moves. Otherwise, it's the mex of the XOR values of all possible splits.

But for a log L, the possible splits are determined by the possible t (>=2) such that s = L/t is >=k and integer. So s must divide L, and s >=k. Then t = L/s.

So for each divisor s of L (s >=k), t must be >=2. So s can be any divisor of L where s >=k and t = L/s >=2. So s <= L/2.

Wait, t must be >=2. So L/s >=2 → s <= L/2. So for example, for L=15, possible s is 5 (since 15/5=3 >=2). But s can't be 15, because t=1 <2.

Wait, but s can be a divisor of L and s >=k, but t must be >=2. So s must satisfy s >=k and s <= L/2.

So for L, possible s's are the divisors of L that are in [k, L/2], and s must divide L.

So the steps to find the possible s's for L are:

- Find all divisors of L (both in the range [k, L/2]).

But for very large L (up to 1e9), enumerating all divisors is not feasible. So we need a smarter approach.

Alternatively, we can find the minimal s for which a split is possible.

Wait, but perhaps the grundy number can only be 0 or 1. Let's check some small examples.

For L where no splits are possible (like when m=9, k=5 in sample 2), g(m)=0.

For L=15, k=4: splits into s=5. Then for s=5, there are no splits possible (since t=2 would split into 2 parts of 2.5, which is invalid. So g(5) is 0. So when splitting into 3 parts (t=3, odd), the XOR is g(5) =0. So the mex for L=15 is the mex of {0}, which is 1. So g(15)=1.

Another example: suppose L=8, k=2.

Possible splits: t can be 2,4,8. Let's see:

t=2 → s=4. s=4 >=2. So split into 2 parts. t is even → XOR is 0.

t=4 → s=2. Split into 4 parts. Even t → XOR 0.

t=8 → s=1 <2, so invalid.

So possible splits for L=8 are s=4 and s=2 (but wait, s=4 gives t=2 (even), s=2 gives t=4 (even). So for each split, the XOR is 0. So mex of {0} is 1. So g(8) is 1.

Wait, but what's the mex of {0}? The mex is the smallest non-negative integer not in the set. So {0} → mex is 1.

So the grundy number here is 1.

Another example: L=6, k=3.

Possible splits:

t=2 → s=3. s=3 >=3. t even → XOR 0.

t=3 → s=2 <3 → invalid.

t=6 → s=1 <3.

So only split is t=2, which contributes 0. So mex is 1. So g(6)=1.

Another example: L=4, k=2. Possible splits: t=2 → s=2. s=2 >=k. Split into two parts. XOR is 0. So mex is 1. So g(4)=1.

Wait, but what's the grundy number here? If g(4) is 1, then the mex is 1.

Another example: L=6, k=2. Let's see:

Possible splits:

s=2 → t=3 (odd). XOR is g(2).

s=3 → t=2 (even). XOR is 0.

s=1 → invalid.

So s can be 2 or 3.

So for s=2: t=3 (odd). So XOR is g(2).

For s=3: t=2 (even). XOR is 0.

So the mex is the mex of {g(2), 0}.

What is g(2)? For L=2, possible splits are t >=2. But s must be 2/t >=k. But if k=2, then s must be >=2. So t can be 1, which is invalid. So no splits. So g(2)=0.

So the mex for L=6 is the mex of {0,0} → which is 1. So g(6) is 1.

Wait, but for s=2, t=3. So the split is into 3 parts of 2 each. The XOR is g(2) (since t is 3, odd). But g(2) is 0, so that contributes 0. The split into s=3, t=2 (even) contributes 0. So the mex is 1.

So the grundy number here is 1.

So far, the grundy numbers seem to be 0 when there are no splits, and 1 otherwise. But wait, in the first example where L=15, the grundy number was 1. But that's when there was a split possible. So perhaps the grundy number is 1 if there's at least one split possible, and mex of the possible XORs is 1. But that's not the case.

Wait, in the case where there's a split possible, but all possible splits result in XOR 0, then the mex is 1.

If there's a split that results in XOR 1, then mex would be 0 or something else.

Wait, maybe I'm missing something here. Let's see.

Let's take another example. Suppose L=5, k=2.

Possible splits:

t=5 → s=1 <2.

t=5 is possible? No, because s=1 is less than k=2. So no splits. So g(5)=0.

Another example: L=10, k=2.

Possible splits:

s can be divisors of 10 >=2 and <=5 (since t >=2, s <=10/2=5).

So possible s are 2,5.

For s=2: t=5 (odd). The XOR is g(2). Since g(2)=0, this contributes 0.

For s=5: t=2 (even). XOR is 0.

So mex of {0,0} → 1. So g(10)=1.

Another case: L=9, k=3.

Possible splits: s=3 (t=3, odd → XOR g(3)), s=3 is >=3. So for s=3, t=3. What's g(3)?

For L=3, k=3: possible splits? s must be >=3, but t >=2. So s=3/t. For t=2, s=1.5 which is not integer. So no splits. So g(3)=0. So the XOR here is 0 (t=3 is odd, so XOR is g(3)=0). So the mex is mex of {0} → 1. So g(9)=1.

But wait, what if there are splits that contribute different XOR values? Let's imagine a scenario where a split leads to XOR 1, and another to XOR 0. Then the mex would be 2.

For example, suppose for some L, possible splits contribute XOR values 0 and 1. Then mex is 2.

But I haven't found such a scenario yet. Let's create one.

Let's say L=12, k=2. Let's compute g(12).

Possible splits:

s can be divisors of 12 >=2 and <=6 (since 12/2=6).

Divisors >=2 and <=6: 2,3,4,6.

So possible s values: 2,3,4,6.

For each s:

s=2 → t=6 (even). XOR is 0.

s=3 → t=4 (even). XOR is 0.

s=4 → t=3 (odd). XOR is g(4). What's g(4)?

For L=4, k=2. Possible splits: s=2 (t=2, even → XOR 0. So mex of {0} is 1. So g(4)=1. So XOR for s=4 is 1 (since t is 3, odd → XOR is g(4)=1). 

s=6 → t=2 (even). XOR 0.

So the possible XOR values are 0 (from s=2, 3, 6) and 1 (from s=4). So mex is 2. So g(12) is 2.

So in this case, the grundy number is 2. Which would imply that the grundy numbers can be higher than 1. But this complicates things, as now how do we compute grundy numbers for large L?

But this seems possible. So the grundy numbers can be 0, 1, 2, etc., depending on the splits.

But how to model this efficiently for large L (up to 1e9)?

We need a way to compute the grundy number for a given L and k.

Alternative approach: find whether the number of splits that produce an even t is zero, or other conditions. But I'm not sure.

Alternatively, perhaps the grundy number for a log is determined by the maximum number of splits possible (like in the game of Nimbers), but I'm not sure.

Alternatively, think of this as a variant of the take-away game, but the possible moves depend on the divisors.

But given the time constraints, perhaps there's a pattern here. Let's try to find a pattern for the grundy numbers.

Looking at previous examples:

- If a log can't be split (no possible moves), grundy is 0.

- If there's at least one split, then grundy number is the mex of the XOR values from all possible splits.

But perhaps the mex is 1 if any split results in an odd t, leading to a grundy number of 0. But this may not hold.

Wait, in the first example where L=15, the split is into t=3 (odd). The XOR is g(5)=0. So mex is {0}, so grundy 1.

Another example where L=12, the split into s=4 (t=3, odd) gives XOR 1. So mex is {0,1} → 2.

So the mex can vary.

But for large L, we can't compute this recursively. So perhaps the key is to find whether the grundy number is zero or non-zero.

Because, for the problem's solution, we need to know whether the grundy number is non-zero. Because if it's non-zero and n is odd, Timur wins. Otherwise, Marsel.

So perhaps the problem reduces to determining if the grundy number of m is non-zero.

But how?

The grundy number is zero only if there are no possible moves. But that's not true. Because even if there are possible moves, but all of them lead to XOR values that include 0 and 1, the mex could be 2. So the grundy number would be 2, which is non-zero.

Wait, but the grundy number is zero only if the mex is zero. The mex is zero only if the set of possible XOR values includes all non-negative integers except zero. Wait, no. The mex is the smallest non-negative integer not present in the set of possible XOR values.

So mex is zero only if zero is not in the set of possible XOR values. But that's impossible because mex is zero when zero is not present. For example, if all possible splits' XOR values are 1, then mex is 0.

So in such a case, the grundy number is zero, even though there are splits possible.

So this complicates things. So the grundy number can be zero even when splits are possible.

Thus, the key is to compute the grundy number of m. But how?

Alternative approach: instead of calculating the actual grundy number, perhaps we can find whether the grundy number is zero or non-zero. Because that's all we need for the problem.

If we can determine for a given m and k whether the grundy number is non-zero, then we can proceed.

So how to determine if the grundy number of m is non-zero.

Let's think: the grundy number is zero if and only if all possible splits (t and s) lead to a position where the XOR of the splits is non-zero. Wait, no. That's not correct. The mex is zero only if none of the possible splits' XORs is zero.

Wait, mex is the minimal excluded value. So for mex to be zero, zero must not be present in the set of possible XORs. So if all possible splits' XOR values are >=1, then mex is zero.

So grundy number is zero if none of the possible splits leads to an XOR of zero.

But how to determine that.

Alternatively, the grundy number is non-zero if there exists at least one split whose XOR is zero. Because mex would be the smallest non-negative integer not in the set. If there's a split with XOR zero, then mex would be at least one.

Wait, no. Because mex is the smallest non-negative integer not present. If zero is present in the set, then mex is the smallest integer not present. For example, if the set is {0}, mex is 1. If the set is {0, 1}, mex is 2. If the set is {0,2}, mex is 1.

So the grundy number is non-zero if the mex is non-zero. But that depends on the mex, not directly on the presence of zero in the possible splits.

But perhaps there's a pattern here. Let's think:

For a log L, the grundy number g(L) is zero if there are no possible splits (so no moves → losing position). Otherwise, it's non-zero.

But that's not the case. For example, in the case where all splits' XORs are 0, the mex is 1. So the grundy number is 1, which is non-zero. So if there are splits possible, the grundy number is non-zero.

Wait, no. Suppose there's a split possible, but all possible splits result in XOR values that are all 1. Then the mex is 0, so grundy number is 0. But how would that happen.

For example, if the splits lead to XOR values 1, 2, 3. Then mex is 0. So grundy number is zero even though there are splits.

But how can that happen?

Alternatively, perhaps the grundy number is zero only if there are no splits possible.

Because whenever there is a split possible, the grundy number is non-zero. But that's not necessarily the case.

But maybe the problem's rules ensure that any split possible leads to a grundy number of non-zero. For example, if any split is possible, then the mex is at least 1.

But that's not true. Suppose all splits have XOR values that include 0. Then the mex is 1.

So grundy is 1. So if there is at least one split, the grundy number is non-zero.

But wait, if there is a split that produces XOR 0, then mex is at least 1. If all splits produce XOR 0, then mex is 1. So grundy is 1. So any split possible implies grundy is non-zero.

But what if there are splits that produce XOR 0 and others that produce XOR 1? Then mex is the smallest non-present, which could be 2.

But regardless, the grundy number would be non-zero.

Ah, so the only time the grundy number is zero is when there are no possible splits.

Because if there are splits possible, then the grundy number is at least 1.

So this changes everything. Because then, the grundy number is zero if and only if there are no possible splits.

Because if there's at least one split, the mex is the minimum excluded value from the possible XORs. But since all possible XORs are computed from splits, which are possible when s and t are valid. So if there's at least one split, the mex is at least 1. So grundy number is non-zero.

But this is only true if there exists at least one split.

So the grundy number for a log is zero if and only if there are no possible splits. Otherwise, it's non-zero.

If this is true, then the problem simplifies to:

Compute whether there exists at least one possible split for the log of length m. If yes, then the grundy number is non-zero, and the outcome depends on whether n is odd (Timur wins) or even (Marsel wins). If no splits are possible, the grundy is zero, so Marsel wins.

So how to determine whether there exists a possible split for m and k.

A split is possible if there exists t >=2 such that t divides m, and s = m/t >=k. Also, since t = m/s, s must be a divisor of m. So s must be a divisor of m, and s >=k, and m/s >=2 (since t >=2 → s <= m/2).

So the problem reduces to checking if there exists a divisor s of m such that s >=k and s <= m/2.

So the question is: does m have a divisor s in [k, m/2]?

If yes → grundy number is non-zero → outcome is Timur if n is odd, Marsel else.

If no → grundy number is zero → Marsel wins.

So now, the problem reduces to checking if m has a divisor s in the range [k, m/2].

But how to compute this efficiently for large m (up to 1e9)?

Approach:

Check if there exists a divisor s of m such that s >=k and s <= m/2.

But generating all divisors of m is not feasible for m up to 1e9. So we need an efficient way.

Alternatively, we can find the minimal possible divisor of m that is >=k. If this minimal divisor is <= m/2, then yes. Else no.

Alternatively, we can check for any possible divisor s in the range [k, m/2]. But how?

Another approach:

The minimal divisor of m >=k is the minimal between the divisors >=k. But perhaps the minimal s that satisfies s >=k is a divisor of m. Once we find the minimal such s, we check if s <= m/2.

Alternatively, if m >= 2k, then s=k is possible? Because m/k is at least 2 (since m >=2k → m/k >=2 → t >=2). So s=k.

But wait, s must divide m. So if k divides m and m/k >=2 (i.e., m >=2k), then s=k is a valid divisor. So the split is possible.

But if k doesn't divide m, then perhaps there is a larger s that divides m and is >=k.

So the problem is:

If there exists a divisor s of m where s >=k and s <= m/2 → answer is yes.

Else → no.

So to check this, we can:

- Check if m >= 2k. Because if m >=2k, then there exists s=k if k divides m, but even if it doesn't, perhaps there's a divisor s >=k and <= m/2.

But this is not sufficient. For example, m=15, k=4. m=15 >= 2*4=8. 15/2=7.5, so m/2=7.5. s must be >=4 and <=7.5. And s must divide 15.

The divisors of 15 are 1,3,5,15. So possible s is 5. Which is >=4 and <=7.5. So yes.

But if m=16, k=5. 16/2=8. s must be >=5 and <=8. Divisors of 16 are 1,2,4,8,16. So s=8 is in the range. So yes.

Another example: m=9, k=5. m/2=4.5. s needs to be >=5 and <=4.5. Impossible. So no.

So the key is to find any divisor s of m that is >=k and <=m/2.

So how to find if such a divisor exists.

Let's think of the following steps:

1. If m < 2k, then m/2 <k. So any s >=k would be >m/2. So no possible s. So no splits. So answer is no.

Wait, m <2k → m/2 <k. So s >=k implies s> m/2. So no possible s, because s must be <= m/2. So in this case, no splits. So answer is no.

So if m < 2k, then return no.

Else, m >=2k. Now, check if there's a divisor s of m in [k, m/2].

But even if m >=2k, there might be no such s.

For example, m=7, k=3. m >=2*3=6. 7/2 is 3.5. So s needs to be >=3 and <=3.5. Possible s can be 3.5, but s must be integer. The divisors of 7 are 1 and7. So no s in [3,3.5]. So answer is no.

So even when m >=2k, there might be no valid s.

So how to check for this.

In the case where m >=2k, we need to check if m has a divisor in [k, m/2].

But how to find this efficiently.

An efficient approach is to find the minimal divisor of m that is >=k. If that divisor is <= m/2, then yes. Otherwise, no.

Alternatively, find the largest divisor of m that is <= m/2 and >=k.

But how to find this.

Another approach: the minimal possible s is the minimal divisor >=k and <=m/2.

If such a divisor exists, then the answer is yes.

To find this, we can check if k <= m/2. If not, then no. But if k <= m/2, then we need to check if there's a divisor of m in [k, m/2].

But for large m, we can't check all numbers up to sqrt(m) to find the divisors. So we need a smarter way.

An alternative idea: any divisor of m that is >=k and <= m/2 must be in the range [k, m/2]. Also, for each divisor d of m in this range, there's a corresponding divisor m/d. But m/d would be >=2 (since d <=m/2 → m/d >=2).

But this doesn't directly help.

Another idea: the minimal divisor of m that is >=k is the smallest possible s. If this s is <=m/2, then yes. Else, no.

So let's find the smallest s >=k that divides m. Then check if s <= m/2.

But how to find the smallest s >=k that divides m.

The minimal s is the smallest divisor of m that is >=k and <= sqrt(m), or the corresponding m/s if it's larger.

Wait, but to find the minimal s >=k that divides m, we can loop through possible divisors from 1 to sqrt(m). For each divisor d of m, if d >=k, then s=d is a candidate. Also, the corresponding m/d may be a candidate.

But for m up to 1e9, this is feasible, as the number of divisors is O(1e5) for numbers with many divisors, but in practice, numbers up to 1e9 have a manageable number of divisors.

But for numbers with large prime factors, this might take O(1e4) operations.

But given that the time limit is 1 second, and per test case, this is manageable.

But how to generate all divisors of m efficiently.

Alternatively, find the minimal divisor of m >=k.

Here's an approach:

Loop from i=1 to sqrt(m). For each i that divides m, check if i >=k. If yes, then i is a candidate. Also, check m/i >=k. The minimal candidate is the minimal between i and m/i, if applicable.

But this is a bit involved.

Alternatively, the minimal s >=k is the minimal between the minimal divisor >=k and the minimal (m/d) >=k where d divides m and d <=sqrt(m).

But perhaps there's a better way.

Another approach: the minimal s is the smallest integer >=k that divides m. So if m is divisible by k, then s=k. Else, check k+1, up to m/2. But this is not feasible for large m.

Alternative idea:

The minimal divisor of m >=k is the smallest d such that d divides m and d >=k.

To find this, we can check if m has any divisors in [k, m]. The smallest such divisor is either k (if k divides m), or the next possible divisor.

But again, checking all possible divisors up to m is not feasible for large m.

Alternative plan:

We can find the greatest common divisor (gcd) of m and any number in the range [k, m/2]. But this approach is unclear.

Alternatively, we can check if there exists a divisor of m in [k, m/2].

But how?

Let's think of the following:

If m >= 2k, then there must be a divisor s in [k, m/2], provided that k <= m/2.

But if m >=2k and there exists a divisor s of m where s >=k and s <= m/2.

But how to check for that.

Wait, for example, m= 2k. Then s=k is a divisor, but s= m/2= k. So yes. So if m is even and m=2k, then s=k is a divisor.

But if m is not divisible by k, then perhaps there's a larger s that divides m.

But how to check.

Alternatively, the problem can be restated as follows:

Check if m >= 2k and there exists a divisor s of m where s >=k and s <= m/2.

But how to check this efficiently.

Here's an approach:

We can check if any of the divisors of m (except m itself) is >=k. Because if there's a divisor s that is >=k and s <=m/2, then s is a proper divisor (since s <=m/2 implies s <m).

So the problem reduces to checking if m has a proper divisor (divisor other than 1 and m) that is >=k and <=m/2.

But how to check this.

Let's think of the steps:

1. If m < 2k: answer is no.

2. Else:

   a. Find if m has any divisor d where d >=k and d <= m/2.

   b. If yes: answer is yes.

   c. Else: no.

So, how to implement this.

An efficient way would be to iterate through all possible divisors up to sqrt(m) and check for the condition.

Here's a plan for the code:

- Check if m < 2k → answer is no.

- Else, iterate through all possible divisors of m up to sqrt(m):

   For each divisor d:

      if d divides m:

         if d >=k and d <= m/2 → yes.

         Also, check the complementary divisor m/d. If m/d >=k and m/d <= m/2 → yes.

         If any of these conditions are met, return yes.

- If after checking all divisors, none meet the condition → return no.

But for m up to 1e9, the number of divisors is manageable. For example, even if m is a prime, there are only two divisors: 1 and m. But since m >=2k, and k >=1, then m is >=2. But in this case, the only divisors are 1 and m. So s = m would need to be >=k and <= m/2. But s =m is > m/2, so no.

So, the code would need to generate all divisors of m and check each.

But how to generate all divisors.

Here's the code outline:

def has_valid_divisor(m, k):

    if m < 2*k:

        return False

    # Check for any divisor d of m where d >=k and d <= m/2

    # Iterate up to sqrt(m)

    sqrt_m = int(math.isqrt(m))

    for d in range(1, sqrt_m +1):

        if m % d == 0:

            if d >=k and d <= m//2:

                return True

            comp = m //d

            if comp >=k and comp <= m//2:

                return True

    return False

But wait, for example, when m=15, k=4:

m >=2*4=8 → yes.

Check divisors:

d=1 → 15%1=0. d=1 <4 → no. comp=15 → 15 >=4 → 15 <=7 (15//2=7)? 15 is 15, which is 15>7 → no.

d=3 → 15%3=0. 3 >=4? No. comp=5. 5 >=4 → 5 <=7 → yes. So return True.

So the code would return True.

Another example: m=7, k=3.

m=7 >=6 → yes.

Check divisors:

d=1 → comp=7. 7 >=3 → 7 <=3.5 (7//2=3) → 7>3 → no.

d=7's sqrt is 2.645, so the loop runs up to 2.

d=1: checked.

d=2: 7%2=1 → no.

So no divisors found. returns False.

Thus, the code works.

Another example: m=9, k=5.

m=9 >=10? 9 <10 → code returns False.

Yes, which matches sample 2.

Another example: m=16, k=5.

m=16 >=10 → yes.

Check divisors:

d=1: comp=16 → 16 >=5 → 16 <=8 → no.

d=2: comp=8 → 8 >=5 → 8 <=8 → yes. So return True.

Thus, the code correctly returns yes.

So this function would correctly determine whether there's a valid split.

So putting it all together:

The code reads n, m, k.

If m < 2*k → no split possible. So the grundy number is zero. Marsel wins.

Else, check if there's a divisor of m in [k, m/2]. If yes → grundy is non-zero. If n is odd → Timur wins. Else → Marsel.

Else, no split possible → Marsel wins.

Thus, the code is:

Read n, m, k.

if m < 2*k:

    print("Marsel")

else:

    if there exists a divisor of m >=k and <= m//2:

        if n % 2 ==1:

            print("Timur")

        else:

            print("Marsel")

    else:

        print("Marsel")

Thus, the code depends on the function has_valid_divisor(m, k).

Implementing this in Python.

But for m up to 1e9, the function has_valid_divisor must be efficient.

Implementing the code as follows:

import math

n, m, k = map(int, input().split())

if m < 2 * k:

    print("Marsel")

else:

    # Check for any divisor of m >=k and <= m//2

    found = False

    sqrt_m = int(math.isqrt(m))

    for d in range(1, sqrt_m + 1):

        if m % d == 0:

            if d >= k and d <= m//2:

                found = True

                break

            comp = m // d

            if comp >=k and comp <= m//2:

                found = True

                break

    if found:

        if n % 2 ==1:

            print("Timur")

        else:

            print("Marsel")

    else:

        print("Marsel")

But wait, what if m is a square. For example, m=16, d=4. comp=4. So both d and comp are 4, so we check if 4 >=k and <=8. So it's checked once, not twice.

So the code is correct.

Testing sample input 1:

1 15 4 → m=15, k=4. 15 >=8 → yes.

Loop d from 1 to 3.

d=1 → 15%1=0. d=1 <4 → no. comp=15 → check 15 >=4 → yes, but 15 <=7 (15//2=7) → 15>7 → no.

d=3 → 15%3=0. 3 <4 → no. comp=5. 5 >=4 → 5 <=7 → yes. So found is True. So n is 1 (odd) → Timur.

Sample input 2: 4 9 5 → 9 < 10 → Marsel.

Another test case: m=6, k=2. m=6 >=4 → yes.

Check divisors:

d from 1 to 2.

d=1: 6%1=0. 1<2 → no. comp=6. 6 >=2 → 6 <=3 → 6>3 → no.

d=2: 6%2=0. 2 >=2 → yes. 2 <=3 → yes. Found True. So if n is 1 → Timur.

Thus, the code works.

This code should handle all cases efficiently.
</think>

```python
import math

n, m, k = map(int, input().split())

if m < 2 * k:
    print("Marsel")
else:
    found = False
    sqrt_m = int(math.isqrt(m))
    for d in range(1, sqrt_m + 1):
        if m % d == 0:
            if d >= k and d <= m // 2:
                found = True
                break
            comp = m // d
            if comp >= k and comp <= m // 2:
                found = True
                break
    if found:
        print("Timur" if n % 2 == 1 else "Marsel")
    else:
        print("Marsel")
```