<think>
Okay, let's see. So the problem is to compute the expected total difficulty of Leha's journey multiplied by 2^(n-1), modulo 998244353. Hmm. Right, because there are 2^(n-1) possible rest site configurations, each contributing some sum, and the expected value is the average. So multiplying by 2^(n-1) gives the total sum over all possible configurations, which is what we need to compute.

The key here is to model the contribution of each a_i in all possible scenarios. Let's think for each kilometer (each a_k), how many times it contributes across all possible configurations. Then the answer is the sum of a_k multiplied by their respective counts, all mod 998244353.

Wait, exactly. So for each position in the journey (each km from 1 to n), we need to determine how many configurations result in that km's difficulty being a_j, for some j. But maybe it's easier to think in terms of each a_i. Wait, no. Let's break it down.

Each kilometer (like the m-th km of the journey) is part of a segment that starts after a rest stop (or the start) and ends at the next rest stop (or the end). The difficulty of this m-th km depends on how many kilometers since the last rest stop. So for the m-th km of the journey (which is between coordinate m-1 and m), the difficulty is a_t, where t is the number of consecutive km's since the last rest stop before m.

The question is: for each possible t, how many times does a_t get added to the total sum across all possible configurations?

But perhaps a better approach is to model for each kilometer m (the m-th km in the journey), and each possible value of t (the difficulty a_t is used here), how many configurations have the m-th km being the t-th since the last rest stop. Then sum over all m and t, a_t multiplied by the number of configurations where that's true.

But since the a's are non-decreasing, perhaps there's a pattern here. However, the a's are given, so we can't exploit their order for the computation. We need to find for each a_i, how many times it's added across all configurations.

Wait, but maybe for each a_k (the a_1, a_2, ..., a_n), we can find the number of times a_k is used in the total sum across all configurations. Then the answer is sum (a_k * count_k) mod 998244353.

So for each k in 1..n, compute count_k, which is the total number of times a_k is added across all possible configurations.

So how do we compute count_k for each k?

Let's think. For a particular a_k, it is the difficulty used for the (t)th kilometer in a segment. For example, if a rest stop is placed at position x, then the next km after x (x+1) is a_1, then a_2, etc., until the next rest stop.

So for a given km m (from 1 to n), the difficulty a_k is used when the number of consecutive km's since the last rest stop (including m) is exactly k. So for km m to be in a segment of length at least k, and the k-th in that segment. Also, the rest stop must be placed at m -k (if m -k >=0), but not placed between m -k +1 to m-1.

Wait, maybe the way to model it is: for each km m, and for each possible k (1 <= k <= m), what is the number of configurations where the km m is the k-th in its segment (i.e., since the last rest stop). Then sum over all m and k the a_k multiplied by the number of configurations where that's true.

So for each m, and for each possible k (1 <= k <= m), we need to find how many configurations have km m as the k-th in its segment.

So for a given m and k, the conditions are:

- The position m -k is a rest stop (or m -k == -1, which is Moscow, which is the starting point, so considered as a rest stop implicitly). Also, for the km m to be the k-th in the segment, there must be no rest stops between m -k +1 and m-1.

So the number of configurations where km m is the k-th in its segment is equal to the number of ways to choose rest stops such that:

1. There is a rest stop at position m -k (or m -k is 0, which is allowed as a starting point).

Wait, no. Wait, the starting point (Moscow) is considered as a rest stop. So for the km m to be the k-th in its segment, the last rest stop before m is at position m -k. Then, the positions m -k +1 to m-1 must not have any rest stops. Also, the position m is not part of the segment (since the km is from m-1 to m, so the rest stops are at integer points). Hmm.

Wait, the rest stops are at integer coordinates. So the km m is from position (m-1) to m. So the last rest stop before m is at some position x, where x is <= m-1. Then, the number of km's since the last rest stop is (m-1 -x). Wait, maybe I'm getting confused here.

Let me rephrase. Let's say that the journey is divided into segments by rest stops. Each segment starts at a rest stop (or the start) and ends just before the next rest stop (or the end). Each km in the segment contributes a_1, a_2, etc., depending on their position in the segment.

So for example, a segment of length 3 (from position x to x+3, with rest stops at x and x+3) has km x+1 (a_1), km x+2 (a_2), km x+3 (a_3). Wait, no. The km from x to x+1 is the first in the segment, so a_1. Then km x+1 to x+2 is a_2, etc.

Wait, the rest stops are at integer points. So when Leha starts at position x (a rest stop), the next km is x to x+1 (km x+1 in the journey?), which is the first since the rest, so a_1. Then, x+1 to x+2 is a_2, and so on. So for the km between position x and x+1 (the (x+1)th km?), the difficulty is a_1. Then, for the next km (x+1 to x+2), if there's a rest stop at x+1, then that's a new segment starting with a_1 again. Otherwise, it's a_2.

So for km m (the m-th km, from position m-1 to m), the difficulty is a_t where t is the number of consecutive km's since the last rest stop before m. So the last rest stop before m is at position s, where s <= m-1. The number of km's since s is (m-1 - s). Then, t is (m - s). Because s is the last rest stop, so the km m is (m - s)th in the segment.

So for example, if s is m-1, then t is 1. If s is m-2, then t is 2, etc.

So for km m, the t can be up to m, when s is 0 (the starting point) and there are no rest stops between 0 and m-1. So the maximum possible t is m.

So for each km m (1<=m<=n), we need to consider all possible t (1<=t<=m), and for each t, compute the number of configurations where the last rest stop before m is at m-t. Then, the number of such configurations is the number of ways to choose the rest stops such that:

- The rest stop is at m-t (which must be >=0, so m-t >=0 => t <=m)
- Between m-t and m-1, there are no rest stops.

Additionally, the rest of the rest stops (those outside the interval [m-t +1, m-1]) can be chosen freely.

So the total number of such configurations is (number of ways to choose rest stops in [0, m-t-1] and [m, n-1]) multiplied by the condition that in [m-t+1, m-1] there are no rest stops, and at m-t there is a rest stop (unless m-t is 0, which is always considered to have a rest stop? Wait, no. The starting point (Moscow) is considered to be a rest stop, but it's not part of the possible rest sites. Because the rest sites are between 1 and n-1. So the initial position (0) is considered a rest stop, but is not counted as a rest site. So for m-t=0, which is the starting point, we don't have to place a rest site there, but it's considered as a rest stop.

Wait, the problem says: "Every integer point from 1 to n−1 may contain a rest site." So the rest sites are at positions 1, 2, ..., n-1. The starting point (position 0) is not a rest site but acts as an implicit rest stop. So when considering the last rest stop before m, it could be position 0 (if there are no rest sites before m) or any other rest site in positions 1 to m-1.

So for a km m, the last rest stop before m is either 0 (no rest sites in 1..m-1) or some x in 1..m-1 where x is a rest site, and there are no rest sites between x+1 and m-1.

So for each possible t (1 <= t <= m), the last rest stop is at position m - t. But wait, the last rest stop is at position s, and s is such that s <= m-1. The number of km since s is (m-1 - s) + 1 = m - s. So t = m - s. So s = m - t.

So for t, the last rest stop is at s = m - t. So s must be >=0, so m - t >=0 → t <=m. So for t in 1..m, s can be m-t, which must be >=0.

But s can be 0 (if m-t =0 → t =m). In that case, the last rest stop is the starting point (0), and there are no rest sites between 1 and m-1.

So for each km m, and for each possible t (1<=t<=m), the number of configurations where the last rest stop is at s = m - t is equal to:

If s =0 (t =m), then the number of configurations is the number of ways where none of the positions 1..m-1 are rest sites. The rest can be any combination for the positions m..n-1.

So for s=0:

The positions 1 to m-1 must have no rest sites. The rest (positions m to n-1) can be chosen freely.

The number of such configurations is 2^{(number of positions in m to n-1)}. Since each position can be chosen or not. The number of positions here is (n-1) - m +1 = n-1 -m +1 = n -m.

So if s=0, the count is 2^{(n -m)}.

If s >=1 (i.e., t <=m -1), then s is m -t. We need s >=1 → m -t >=1 → t <=m-1. So for t from 1 to m-1, s =m -t must be >=1. So for these cases, s is a position where there is a rest site. And between s+1 and m-1, there must be no rest sites. Additionally, the rest of the positions (other than s, s+1 to m-1, and m to n-1) can be chosen freely.

So the conditions are:

- There is a rest site at s = m -t (which is in 1..m-1)
- The positions s+1, s+2, ..., m-1 must not have any rest sites.
- The positions from 1 to s-1 can be any combination (but s is a rest site)
- The positions from m to n-1 can be any combination.

So the number of configurations for this case is:

1 (for the rest site at s) multiplied by 2^{number of positions in 1..s-1} × 2^{number of positions in m..n-1} }.

But wait, the positions 1..s-1 can have any rest sites, because the only constraints are on s and the positions s+1 to m-1. So the number of configurations here is:

1 (s is a rest site) × [sum of possible choices for 1..s-1] × [product of choices for positions s+1 to m-1 (all must be 0)] × [sum of possible choices for m..n-1].

Wait, the positions s+1 to m-1 must not have any rest sites, so each of these positions must be 0 (no rest site). So for these positions (if any), there's only one choice. The positions 1..s-1 can be any combination (so 2^{s-1} possibilities). The positions m..n-1 can be any combination (2^{n-1 - (m-1)} } = 2^{n -m} possibilities. And the s-th position must be chosen (so 1 possibility for that).

So the total for this case (t from 1 to m-1, s = m-t >=1) is:

2^{(s-1) + (n - m)} }.

So putting it all together, for each km m, the total count for a_k (where k is the t in this scenario) is:

sum over t=1 to m:

if t == m:

count = 2^{n -m} (since s=0, and positions 1..m-1 must be 0, m..n-1 can be anything)

else (t < m):

s = m -t must be >=1. So s ranges from m-1 (t=1) down to 1 (t = m-1). For each t in 1..m-1, the count is 2^{ (s-1) + (n -m) } }, where s = m-t. So substituting s:

s-1 = (m-t -1), so (s-1) + (n -m) = (m-t -1) + (n -m) = n -t -1 -1? Wait:

Wait, (m-t -1) + (n -m) = (m - t -1 + n -m) = n - t -1.

So for each t in 1..m-1, the count is 2^{n - t -1} }.

So for each km m, the total count for a_k (for each k) is:

For t=1 to m:

If t = m: count += 2^{n - m}

For t=1 to m-1: count += 2^{n - t -1}

Wait, but how does this sum over s? Because for each t, we have a term. Wait, for each t in 1..m, the count is:

if t = m: 2^{n -m}

else: 2^{n - t -1}

So for a given km m, the total contribution to the count of a_t is:

sum_{t=1 to m} (number of configurations where the t-th a is used for km m) = sum_{t=1}^m (count_t)

where count_t is 2^{n-t-1} for t < m, and 2^{n-m} for t = m.

Wait, but for t < m, the count is 2^{n - t -1} ?

Wait, let's see. For t=1, s = m-1. So s must be a rest site, positions m-1+1 (m) up to m-1-1 (m-2) are not possible. Wait, no. The positions between s and m-1 are s+1 to m-1. So if s = m-1 (t=1), then there are no positions between s and m-1 (since m-1 is s). So the positions from s+1 to m-1 is empty. So the condition is that s is a rest site, and the rest of the positions (1..s-1) can be anything, and the positions m..n-1 can be anything. So the count for t=1 is 2^{(s-1) + (n -m)} } = 2^{(m-1-1) + (n -m)} } = 2^{ (m-2) + (n -m) } } = 2^{n -2} }.

Similarly, for t=2, s = m-2. So s must be a rest site. The positions s+1 (m-2 +1 = m-1) to m-1 must not be rest sites. So for t=2, the count is 2^{ (m-2-1) + (n -m) } } = 2^{ (m-3) + (n -m) } } = 2^{n-3}.

So for t in 1..m-1, the count is 2^{n - t -1}.

So for each t from 1 to m-1, the count is 2^{n - t -1}, and for t=m, the count is 2^{n-m}.

So the total for km m is:

sum_{t=1}^{m-1} 2^{n - t -1} + 2^{n -m}

But 2^{n -m} is the same as 2^{n - m} = 2^{n - (m) -1 +1} ? Not sure. Let's compute the sum.

Wait, the sum for t from 1 to m-1 of 2^{n -t -1} is sum_{k=1}^{m-1} 2^{n -k -1} }.

Let me make a substitution. Let j = t +1. Then when t=1, j=2; t=m-1 → j=m. So sum from j=2 to j=m of 2^{n - j}.

Wait, because 2^{n - t -1} = 2^{n - (t+1)} } → j = t+1 → t ranges from 1 to m-1 → j ranges from 2 to m.

So sum_{j=2 to m} 2^{n-j} } = sum_{j=2}^m 2^{n-j} = sum_{k= n -m}^{n-2} 2^k } (if we let k = n-j → j = n -k, j ranges from 2 to m → k ranges from n-2 down to n -m. Wait, perhaps it's easier to think of the sum as 2^{n-2} + 2^{n-3} + ... + 2^{n -m} }.

This is a geometric series. The sum from i = a to b of 2^i is 2^{b+1} - 2^a, assuming a <= b.

Wait, in this case, the sum is 2^{n-2} + 2^{n-3} + ... + 2^{n -m}.

Let me write the exponents in order: n-2, n-3, ..., n -m. The number of terms here is (n-2) - (n -m) +1 = m-1 terms. But perhaps it's easier to reverse the order.

The sum is equal to sum_{k= n -m}^{n-2} 2^k }.

So this is (2^{n-1} - 2^{n -m -1}) ) / (2 -1) ? Wait, the sum from a to b (inclusive) of 2^k is 2^{b+1} - 2^a.

Yes. So sum_{k=a}^b 2^k = 2^{b+1} - 2^a.

In our case, a = n - m, and b = n-2. So sum is 2^{(n-2)+1} - 2^{n -m} = 2^{n-1} - 2^{n -m}.

So the sum from t=1 to m-1 of 2^{n -t -1} is 2^{n-1} - 2^{n -m}.

Adding the term for t=m (which is 2^{n -m}), the total for km m is:

(2^{n-1} - 2^{n -m}) ) + 2^{n -m} ) = 2^{n-1}.

Wait, that's interesting. So for each km m, the sum of counts over t is 2^{n-1}.

But that can't be right. Because each configuration contributes exactly m's difficulty, but the sum over all configurations for all km m would be 2^{n-1} * sum of all a's. But that's not possible given the sample input.

Wait, the first sample input is n=2, a=[1,2]. The answer is 5. Let's see: the sum for each km.

For km 1: sum is 2^{2-1} = 2^1 = 2. So contributes 1 * 2.

For km 2: sum is 2^1 = 2. Contributes 2 * 2.

Total is 2*1 + 2*2 = 6. But the sample output is 5. So this can't be right.

Ah, so I must have made a mistake here.

Wait, the sample input's first case is n=2. The possible configurations are 2^1 = 2. The two possibilities are:

1. No rest site at 1. Then the journey is two km. The first is a_1, the second is a_2. Sum is a1 + a2 = 1 + 2 = 3.

2. Rest site at 1. The first km is a_1, then rest, then second km is a_1 again. Sum is a1 + a1 = 2.

Total sum is 3 + 2 =5, which is the answer.

But according to the previous approach, each km m contributes 2^{n-1} = 2^1 =2, so total sum would be 2*(1+2) =6. Which is different. So the approach is wrong.

So where is the error?

Ah, right. The mistake is that when t varies, the sum for a particular km m is not 2^{n-1} for each m. But according to the previous calculation, it was. But the sample input shows that this is not the case.

So the earlier reasoning must be flawed.

Let's re-examine the previous analysis.

The error is in the conclusion that the sum for each m is 2^{n-1}. Let's re-calculate.

In the first sample input, m=1 and m=2.

For m=1: possible t can be 1. Because m=1, so t can't be larger than m.

So for t=1, s = 1-1 =0. So the count is 2^{n-m} =2^{2-1} =2^1=2. So for km 1, the count is 2, so contribution is 1*2=2.

For m=2: possible t ranges from 1 to 2.

For t=2: s =2-2=0. So count is 2^{2-2} =1. Because n-m is 2-2=0 → 2^0=1.

For t=1: s=2-1=1. But since n=2, the positions m (2) to n-1 (1) is invalid. Wait, m=2, so positions m to n-1 is positions 2 to 1, which is empty. So for t=1 in m=2, the count is 2^{(s-1) + (n -m)} }, where s=1. So s-1=0, n-m=0. So 2^0 * 2^0 =1.

So sum for m=2 is 1 (t=2) +1 (t=1) = 2. So contribution is 2*2=4.

Total sum is 2+4=6. But sample output is 5. So something is wrong here.

But the actual sum for all configurations is 5. So the approach must be incorrect.

Hmm. So where is the error?

Looking back:

For m=2, t=1:

s =2-1=1. But s must be a rest site. But in the first sample input, when there is a rest site at 1, the second km is a_1. So how many configurations have a rest site at 1?

The count for t=1 in m=2 is the number of configurations where s=1 is a rest site, and between s+1 (2) and m-1 (1) (since m is 2, m-1 is 1) there are no rest sites. But s=1 is the rest site, and between 2 and 1 is invalid. So the positions between s+1 and m-1 are 2 to 1, which is empty. So the count for this case is 2^{(s-1) + (n -m)} }, where s=1, s-1=0, n-m=0. So 2^0 * 2^0 =1. But the number of configurations where s=1 is chosen (so rest site is present at 1) and the rest (positions m=2 to n-1=1, which is empty) can be anything. But in this case, positions after m (which is 2) is up to n-1=1, which is empty. So the only condition is that position 1 is a rest site, and the other positions (positions 0 and 2 are not considered). So the count is 1 (position 1 must be chosen) multiplied by 2^(number of other positions not in [s+1, m-1] and not s). The other positions are none (since in this case, m=2, n=2, the only rest site is position 1). So the count is 1.

But in the sample input, when there is a rest site at 1, the contribution to a_1 for m=2 is 1. So in that configuration, the second km is a_1. So the count for a_1 (t=1) in m=2 is 1 configuration. But according to the previous approach, the count is 1. But in the actual configurations, the sum for a_1 in m=2 is 1 (when rest site is present), and 0 otherwise (when it's not present). So total count for a_1 in m=2 is 1. But according to the previous approach, it's 1. So why does the sum of 1 (t=1) and 1 (t=2) for m=2 give a contribution of 2*2=4, but in reality it's a_1 is 1 (count 1) and a_2 is 1 (count 1) → sum 1*1 +2*1=3. But according to the previous approach, it's 2* (1+2) =6. But the actual sum is 3 (from the two configurations: 3+2=5, which is the sample's output. Wait, no: the two configurations are:

Case 1: no rest sites. So km 1 is a_1, km 2 is a_2. Sum 3.

Case 2: rest site at 1. So km 1 is a_1, rest, then km 2 is a_1. Sum 2.

So sum across all configurations is 3 + 2 =5. So the total is 5.

So for each km:

For km 1:

- All configurations have t=1. Because in case 1, no rest sites, so km 1 is first in the segment. In case 2, km 1 is first (since rest at 0), then rest at 1. So km 1 is t=1. So count for a_1 in km 1 is 2.

So contribution is 1 *2=2.

For km 2:

In case 1: t=2 (since no rest after 0). So a_2 is added once.

In case 2: t=1 (rest at 1). So a_1 is added once.

So for km 2, a_1 is added in 1 case, a_2 in 1 case. So count for a_1 is 1, a_2 is 1. So contribution is 1*1 + 2*1 =3.

So total is 2+3=5, which matches the sample.

But according to the previous approach, for km 2, the sum is 2^{n-1} =2^1=2. So contribution is 2 * (a_1 +a_2) ?

No, but that's not the case. So the previous approach's conclusion that each km m contributes sum a_t * count_t where sum count_t =2^{n-1} is wrong.

So where is the mistake?

The mistake is in the calculation of the sum of count_t for a given m.

Let's re-calculate for m=2:

t can be 1 or 2.

For t=2:

s =2-2=0. So the count is 2^{n-m} =2^0=1. Which is correct (case where no rest site is present at 1).

For t=1:

s=2-1=1. So the count is 2^{(s-1) + (n -m)} } → s-1=0, n-m=0. 2^0 * 2^0=1. So count is 1. Which corresponds to the case where rest site is present at 1. So for m=2, the total count for t=1 and t=2 is 2, which sums to 1+1=2. So km 2's contribution is a_1*1 +a_2*1. So in the first case, the sum is 1*1 (a_1) +1*2 (a_2) =3. Which matches the sample.

So why in this case, the sum for m=2 is 2^{n-1} =2^1=2? Because 2^1=2, which is the sum of counts for t=1 and t=2. So sum count_t is indeed 2, which is 2^{n-1} (n=2). But in the sample, the sum for a's is a_1 *1 + a_2 *1. So for the sum to be 3, which is 1*1 + 2*1 =3. But according to the previous approach, the sum for m=2 is 2^{n-1} =2, which would imply that each a_t is multiplied by 2. But no. The sum of count_t for m=2 is 2, but the a_1 is multiplied by 1 and a_2 by 1. So the sum of count_t is 2, but each a_t is multiplied by their respective count.

So the previous conclusion that the sum for each m is 2^{n-1} is correct, but how does that help? Because each m contributes to different a_t's.

Ah, right. So the sum over all t for a given m is 2^{n-1}, but each t is multiplied by a different a_t. So the total sum over all configurations is sum_{m=1 to n} sum_{t=1}^m (count_{m,t} * a_t) }, where count_{m,t} is the number of times a_t is used for km m across all configurations.

So the sum over all m and t is sum_{t=1}^n a_t * (sum_{m=t}^n count_{m,t}).

Wait, because for a given t, a_t can be used in any km m where m >=t. Because t can't exceed m.

So for each a_k, the total contribution is a_k multiplied by the sum over all m >=k of count_{m, k}.

So the question is, for each k, compute sum_{m=k}^n count_{m,k}, which is the total number of times a_k is used across all km and all configurations.

Then the answer is sum a_k * (sum_{m=k}^n count_{m,k}).

So how to compute sum_{m=k}^n count_{m,k} ?

count_{m,k} is the number of configurations where in km m, the difficulty is a_k.

From the previous analysis, for km m and t=k:

If k ==m:

count_{m,k} = 2^{n -m}.

Else (k <m):

count_{m,k} = 2^{n -k -1}.

So for each a_k, the sum over m from k to n of count_{m,k} is:

sum_{m=k}^n count_{m,k} = [sum_{m=k}^n (if m >=k, then count_{m,k}) ]

But for m >=k:

if m ==k → count is 2^{n -k}.

if m >k → count is 2^{n -k -1} for each m from k+1 to n.

So sum is:

2^{n -k} + sum_{m=k+1}^n 2^{n -k -1}

The sum from m=k+1 to n is (n -k) terms each equal to 2^{n -k -1}?

Wait, no. Because for each m from k+1 to n, count_{m,k} = 2^{n -k -1}.

Wait, when m >k, then for t=k, m must be >=k+1.

Wait, for m >=k+1 and t=k:

count_{m,k} = 2^{n -k -1}.

So the number of terms where m ranges from k+1 to n is (n - (k+1) +1) )= n -k terms.

So sum_{m=k+1}^n count_{m,k} = (n -k) * 2^{n -k -1}.

So the total sum for a_k is:

2^{n -k} + (n -k) * 2^{n -k -1}.

Factor out 2^{n -k -1}:

= 2^{n -k -1} [ 2 + (n -k) ]

= (n -k + 2) * 2^{n -k -1}.

But wait, let's compute:

2^{n -k} is equal to 2 * 2^{n -k -1}.

So:

sum = 2^{n -k -1} * (2 + (n -k)) )

So, sum_{m=k}^n count_{m,k} = (n -k + 2) * 2^{n -k -1} }

But wait, let's test this with the first sample.

For k=1:

sum is (n -1 +2) * 2^{n-1-1 -1} ?

Wait, no. Wait:

For k=1, the sum is 2^{n-1} + (n-1)*2^{n-2} → ?

Wait, n=2.

sum is (2-1 +2) * 2^{2-1-1 -1} → (3) * 2^(-1) → no, that can't be right. So the previous approach must have an error.

Wait, let's compute for the first sample where k=1:

sum_{m=1}^2 count_{m,1}.

For m=1: count is 2^{2-1} =2.

For m=2: count is 2^{2 -1 -1} =2^0=1.

So sum is 2+1=3.

The formula (n -k +2) * 2^{n -k -1} }.

n=2, k=1 → (2-1 +2) * 2^{2-1-1} → (3)* 2^0=3*1=3. Which matches.

Similarly, for k=2:

sum_{m=2}^2 count_{m,2} =2^{2-2} =1.

The formula gives (2-2 +2) * 2^{2-2-1} → 2 * 2^{-1} → which is 2*(1/2) =1. Which also matches.

So the formula seems to work.

So for each a_k, the total contribution is a_k multiplied by (n -k +2) * 2^{n -k -1} mod 998244353.

So the answer is sum_{k=1 to n} a_k * ( (n -k + 2) * 2^{n -k -1} ) mod 998244353.

So the problem reduces to calculating this sum efficiently.

Now, the question is how to compute this for large n (up to 1e6) quickly.

First, note that 2^x can be precomputed modulo 998244353 up to x=1e6.

But n can be up to 1e6, so for each k from 1 to n, the exponent is (n -k -1). Let's make a substitution: let d = n -k. Then for each k, d ranges from 0 (k=n) to n-1 (k=1). So for each d from 0 to n-1, the term becomes (d + 2) * 2^{d-1}.

Wait, for d =n -k:

(n -k +2) → (d +2).

And 2^{n -k -1} → 2^{d-1}.

So the term for each k is a_k * (d+2)*2^{d-1}, where d = n -k.

So the sum is sum_{d=0}^{n-1} a_{n-d} * (d+2) * 2^{d-1}.

But when d=0 (k =n), the term is (0+2)*2^{-1} = 2 * (1/2) =1. So a_n * 1.

When d=1 (k=n-1): (1+2)*2^{0} =3*1=3. So a_{n-1} *3.

When d=2: 4 * 2^1 = 4*2=8 → a_{n-2} *8, etc.

So the sum can be computed by iterating over d from 0 to n-1, and for each d, compute a_{n-d} multiplied by (d+2) * 2^{d-1}.

The problem is to compute this sum efficiently.

So steps:

1. Precompute all the powers of 2 modulo 998244353 up to exponent (n-1 -1) =n-2. Because the maximum exponent in 2^{d-1} is when d =n-1: 2^{n-2}.

But wait, 2^{d-1} for d from 0 to n-1: maximum exponent is (n-1)-1= n-2. So we need to precompute pow2 up to n-2.

But for d=0, the exponent is -1. How to handle that? 2^{-1} mod 998244353 is the modular inverse of 2. Since 998244353 is a prime, the inverse is 499122177.

So for d=0: 2^{-1} mod MOD is inv_2 = 499122177.

For d >=1, 2^{d-1} can be precomputed.

So plan:

- Precompute pow2 for exponents from 0 to n-2. pow2[i] = 2^i mod MOD.

- Compute inv_2 = pow(2, MOD-2, MOD).

Then, for each d from 0 to n-1:

term = a_{n-d} * (d+2) * (pow2[d-1] if d >=1 else inv_2)

Sum all terms.

So the steps are:

Read n.

Read a_1, a_2, ..., a_n.

Compute inv_2 = pow(2, MOD-2, MOD).

Precompute pow2 up to max exponent needed: n-2.

pow2[0] =1, pow2[1] =2, ..., pow2[n-2] = 2^{n-2}.

Then, for each d in 0..n-1:

k = n -d. So a_k is a[k-1] (since the list is 0-based in Python).

term = a[k-1] * (d+2) * (pow2[d-1] if d >=1 else inv_2) % MOD.

Sum all terms mod MOD.

But for d >=1, pow2[d-1] is available as pow2[d-1], since d-1 can be up to n-2.

For d=0, use inv_2.

But wait, when d=0, the term is (0+2) * 2^{-1} → 2 * inv_2 → which is 1.

Yes. So that's correct.

Now, for n=1e6, the precomputation of pow2 up to n-2 is manageable. Precompute a list pow2 where pow2[i] is 2^i mod MOD.

But in Python, even for n=1e6, precomputing a list of size 1e6 is trivial.

So the code steps:

Read n.

Read the list a as a list of integers.

precompute pow2 up to max (n-2, 0). Because when n=1, max exponent is -1, but in that case, for d=0, which is the only term, it's handled by inv_2.

But for n=1, the code should compute d=0:

term = a_1 * (0+2) * inv_2 → 2 * inv_2 → 1. So sum is a_1 * 1 → correct.

So the code:

MOD = 998244353

n = int(input())

a = list(map(int, input().split()))

Compute inv_2 = pow(2, MOD-2, MOD)

max_pow = max(n-2, 0)

pow2 = [1]*(max_pow +1)

for i in range(1, max_pow+1):

    pow2[i] = (pow2[i-1] *2 ) % MOD

sum_ans =0

for d in range(n):

    # d ranges from 0 to n-1

    k = n -d

    # a[k-1] is a_{k}

    factor = (d+2) % MOD

    if d ==0:

        power = inv_2

    else:

        if d-1 > max_pow:

            # but max_pow is n-2. since d ranges up to n-1, for d >=1, d-1 can be up to n-2.

            # So this case is not possible.

            pass

        power = pow2[d-1]

    term = a[k-1] * factor % MOD

    term = term * power % MOD

    sum_ans = (sum_ans + term) % MOD

print(sum_ans)

But wait, when d ranges from 0 to n-1 (inclusive), and for each d, k =n-d. So k ranges from n (when d=0) down to 1 (when d =n-1).

Wait, when d=0: k =n-0 =n. But a is given as a_1, a_2, ..., a_n. So a[k-1] is a_n.

Yes.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    MOD = 998244353

    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    if n == 0:
        print(0, file=output_stream)
        return

    inv_2 = pow(2, MOD - 2, MOD)
    max_pow = max(n - 2, 0)
    pow2 = [1] * (max_pow + 1)
    for i in range(1, max_pow + 1):
        pow2[i] = (pow2[i-1] * 2) % MOD

    sum_ans = 0
    for d in range(n):
        k = n - d
        ak = a[k-1]
        factor = (d + 2) % MOD
        if d == 0:
            term = ak * factor % MOD
            term = term * inv_2 % MOD
        else:
            power = pow2[d-1] if d-1 <= max_pow else 0
            term = ak * factor % MOD
            term = term * power % MOD
        sum_ans = (sum_ans + term) % MOD

    print(sum_ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
1 3 3 7
""",
            "output": \
"""\
60
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

Yes.

So the code works for the first sample.

Second sample input:

4

1 3 3 7

Output is 60.

Let's compute:

d ranges 0 to 3.

d=0: k=4, a[3]=7. factor=2 → term =7 *2 * inv_2 → 7 * (2 * inv_2) →7*1=7.

d=1: k=3, a[2]=3. factor=3. power=pow2[0] =1. term=3*3*1=9.

d=2: k=2, a[1]=3. factor=4. power=pow2[1] =2. term=3*4*2=24.

d=3: k=1, a[0]=1. factor=5. power=pow2[2] =4. term=1*5*4=20.

Sum: 7+9+24+20=60 → correct.

So the code works.

Now, the code needs to handle up to n=1e6. Precomputing pow2 up to 1e6-2 is feasible.

But for n=1, the pow2 array will have max_pow=0, and pow2[0] is 1. But d ranges from 0 to 0 (d=0).

So code works.

Now, the code must read a list of n integers, which is manageable.

Thus, the final code is as described.
</think>

```python
MOD = 998244353

n = int(input())
a = list(map(int, input().split()))

if n == 0:
    print(0)
    exit()

inv_2 = pow(2, MOD - 2, MOD)
max_pow = max(n - 2, 0)
pow2 = [1] * (max_pow + 1)
for i in range(1, max_pow + 1):
    pow2[i] = (pow2[i-1] * 2) % MOD

sum_ans = 0
for d in range(n):
    k = n - d
    ak = a[k-1]
    factor = (d + 2) % MOD
    if d == 0:
        term = ak * factor % MOD
        term = term * inv_2 % MOD
    else:
        power = pow2[d-1] if d-1 <= max_pow else 0
        term = ak * factor % MOD
        term = term * power % MOD
    sum_ans = (sum_ans + term) % MOD

print(sum_ans)
```
