<think>
Okay, let's tackle this problem. Hmm, the problem says we need to find the maximum possible score by transforming numbers according to certain rules. The key here is to figure out all possible valid transformations between pairs (a, b) where |a| and |b| are between 2 and n, inclusive. Each transformation contributes |x| points, where x is the factor that connects a and b either via a*x = b or b*x = a. Also, once we use a pair (a, b) or (b, a), we can't use them again.

First, I need to understand what counts as a valid transformation. Let's take the example given for n=4. The output is 8. The transformations there are 2 →4 (x=2), then 4 →-2 (x=-0.5, but wait, the problem says x must have |x|>1. Oh, wait, wait. Wait, the condition is that a * x = b or b * x = a, with |x|>1. So for example, if a=4 and b=-2, then x would be (-0.5), which has absolute value 0.5 <1. So that's invalid. Wait, but the note says in the first example, there's a transformation from 4 to -2. How does that work?

Wait, maybe I'm misunderstanding the direction. Let's re-examine the example. The note says the transformations are 2 →4 →-2 →-4 →2. Let's check each step:

2 →4: x is 2. So 2*2=4. That's valid. Then 4 →-2: here, the x would be -0.5, which is |x|=0.5, which is not allowed. But maybe the transformation is using the other direction. Like, maybe the condition is a * x =b OR b *x =a. So for 4 →-2, perhaps it's b *x =a. Here, a is 4, b is -2. So -2 * x =4. Solving for x gives x =-2. Then |x|=2>1. So yes, that's allowed. So in this case, the x is -2. So the contribution is |x|=2. So this step adds 2 points.

Ah, right. So when the transformation is from a to b, x can be either (b/a) if that's an integer with |x|>1, or (a/b) if that's an integer with |x|>1. Wait, no. Because the condition is a *x =b OR b *x =a. So for a and b, x can be such that either a multiplied by x gives b, or b multiplied by x gives a. So x can be either (b/a) or (a/b). But in either case, x must be an integer (since a and b are integers?), wait wait, the problem says a and b are integers. Wait, the problem says "For every pair of integers a and b (2 ≤ |a|, |b| ≤n), you can transform a into b if and only if there exists an integer x such that 1 < |x| and (a·x = b or b·x = a)".

Wait, x has to be an integer. So x must be an integer with |x|>1, and either a*x = b or b*x =a.

So for a pair (a, b), there's a possible transformation in either direction, but only if one of the two equations holds with x being an integer of absolute value >1. Also, once either transformation is used (a→b or b→a), you can't use the other.

So the problem is to find all possible ordered pairs (a, b) where such x exists, and then select a subset of these pairs such that no two pairs are inverses (like (a,b) and (b,a)), and each pair is used at most once, to maximize the sum of |x| for each used pair.

But how to model this? Because for each possible unordered pair {a, b}, there could be two possible ordered pairs (a→b and b→a), each with their own x values. But once you use one, you can't use the other. So for each unordered pair {a, b}, we need to choose which direction to take (if possible) to get the maximum possible |x|.

Wait, but in the problem statement, the maximum score is achieved by choosing the direction that gives the higher |x|. Because for a pair (a, b), if a*x =b, then x is b/a. But if b*x =a, then x is a/b. The sum contributed by each direction is |x|. So for the pair (a, b), the maximum possible contribution is the maximum of |b/a| and |a/b|, but only if one of the two conditions is possible (i.e., one of them is an integer with |x|>1).

Wait, but this is only possible if a divides b or b divides a. Because x has to be an integer. So for a and b to form a valid transformation pair, a must be a multiple of b (or vice versa) with a ratio of absolute value greater than 1. So for example, 4 and 2: 4/2=2, which is allowed. So the x here is 2 if you go from 2 to 4, or 0.5 if you go from 4 to 2. But 0.5 is not allowed because |x| must be >1. So the only possible transformation here is 2 →4 with x=2. So the contribution is 2.

But wait, in the example given in the note, the transformation from 4 to -2 is allowed. Let's see: 4 and -2. So possible x for a→b (4 to -2) is x = (-2)/4 = -0.5, which is not allowed. But if we consider the other direction: -2 * x =4. So x= -2. So the transformation is -2 →4, but that's the reverse of the previous step. Wait, maybe the note is using a chain that loops through multiple steps.

In any case, for each pair (a, b) where a and b are in the range and |a| and |b| ≥2, we can have at most one transformation between a and b. So for each such pair, we can contribute the maximum possible |x| from either possible direction, provided that direction's x is valid.

But how do we efficiently compute this for all possible pairs (a, b) where a and b are in [2, n] or their negatives?

Wait, the problem allows a and b to be any integers with absolute values between 2 and n. So negative numbers are allowed as well. So for example, a could be 2, b could be -4. Then 2 * (-2) =-4, so x is -2, which is allowed. So the contribution here would be 2.

This complicates things, but perhaps there's a pattern here. Maybe we can model this by considering the absolute values of a and b. Let's think: if a and b are connected via x, then their absolute values must be multiples of each other. For example, |a| * |x| = |b|, or |b| * |x| = |a|. So the absolute values are in a multiplicative relationship. So for each pair of integers (m, k) where m and k are in [2, n], we can see if m divides k (so m * x =k, x integer >1) or k divides m (k *x =m, x>1). But even that's not enough, because the signs could differ. Hmm.

But perhaps considering the absolute values simplifies the problem. Let's think in terms of pairs of positive integers. Let's say a and b are positive. Then for a to transform into b, either a *x =b (x>1 integer) or b*x =a (x>1 integer). So for each pair (a, b), if a divides b (and the quotient is >1) or vice versa, then we can have a contribution of the maximum between those two possible x's, but only if they are valid.

Alternatively, since a and b can be any integers (positive or negative), but their absolute values are between 2 and n, maybe the maximum contribution for a pair (m, k) (where m and k are the absolute values) is the same as considering their positive counterparts, since the sign can be adjusted by multiplying by -1. For example, the pair (m, k) can be transformed in either direction, and the maximum x would be same as if they were positive. The sign can be adjusted by using x as a negative number. For example, m and -k: m *x =-k → x= -k/m. But x has to be an integer with |x|>1. So for m and k, the possible x's in either direction (a→b or b→a) would have the same absolute values as their positive counterparts. So the maximum contribution for a pair (a, b) is determined by their absolute values.

Therefore, perhaps we can model the problem by considering the absolute values of a and b. That is, for all pairs (m, k) where m and k are in [2, n], and m ≠k, we can compute the maximum possible x between them (if any) and sum that across all valid pairs, but making sure that each unordered pair is considered once.

Wait, but the problem allows a and b to be any integers in the range, including negatives. However, the maximum contribution for a pair (a, b) and (-a, b) etc., would be the same as the contribution for their absolute values. Because, for example, if a is 2 and b is 4, the x is 2. If a is 2 and b is -4, then x is -2, but |x| is 2. So the contribution is the same. Similarly, if a is -2 and b is -4, then x is 2 again. So for any pair (a, b), the absolute value of x is determined by their absolute values. Therefore, the maximum contribution for all possible (a, b) pairs (including negative ones) can be computed by considering only their absolute values, and then multiplying by the number of possible sign combinations that would produce such a contribution.

Wait, but perhaps for each pair of absolute values m and k (where m and k are in 2..n), the maximum possible contribution per (m, k) pair (considering all possible combinations of signs) would be the same as the contribution for their absolute values, multiplied by the number of times such a pair can be formed. Hmm, not sure. Let's think.

For each pair (m, k), where m and k are positive integers in 2..n, we can generate four possible pairs of (a, b) by considering the signs: (m, k), (m, -k), (-m, k), (-m, -k). Each of these pairs may have a possible x, but the maximum |x| would be determined by m and k. So the total contribution for all possible (a, b) pairs derived from (m, k) would be the sum of the maximum |x| for each possible (a, b) pair. However, this seems complicated. Alternatively, perhaps the maximum possible contribution for the entire problem can be determined by considering the pairs (m, k) (as their absolute values) and then multiplying by the number of sign variations that allow that x.

Wait, perhaps each pair (m, k) (m, k positive) can have multiple (a, b) pairs (with different signs) that allow the same maximum x. For example, if m=2, k=4, then x can be 2 (when a=2 and b=4), or x= -2 (a=2, b=-4), etc. Each of these would contribute 2 to the total score, but they are considered separate transformations. Wait, but the problem statement says that once you use a transformation from a to b, you can't use a to b or b to a again. Wait, but in the problem statement, for each pair (a, b), once you use either a→b or b→a, you can't use either again. So the problem is that each unordered pair {a, b} can be used once, in one direction, with the maximum possible x for that direction.

Wait, no. The problem says: you can't transform a into b nor b into a anymore. So for the pair (a, b), if you use a→b, then you can't use a→b again, and you can't use b→a again. Because the transformation of a into b is considered a single step, and once done, neither direction is allowed again.

So, each unordered pair {a, b} can be used exactly once, contributing the maximum x possible between the two directions, provided that such x exists. So for each pair (a, b), we can compute the maximum x between the two possible directions (a→b and b→a), and add that to the total, but only if either of those directions is valid.

But given that a and b can be positive or negative, but their absolute values are in 2..n, we need to find all possible unordered pairs {a, b} (where a and b are integers with |a|, |b| ≥2, |a|, |b| ≤n) such that either a divides b or b divides a with |x|>1, and then sum the maximum |x| for each such pair.

But considering the problem constraints (n up to 1e5), we need a way to compute this efficiently.

First, let's model the problem in terms of the absolute values. For any pair (m, k), where m and k are positive integers between 2 and n, inclusive, and m <=k, there are multiple possible (a, b) pairs (with various signs) that can be transformed. However, the maximum x for each such (m, k) pair (if any) would be the same for all (a, b) pairs derived from m and k. For example, if m=2 and k=4, then the maximum x is 2 (when a→b with a=2, b=4, or a=2, b=-4, etc.). So the total contribution for all possible (a, b) pairs derived from (m, k) is the maximum x multiplied by the number of such (a, b) pairs.

Wait, but the unordered pairs {a, b} are considered once. So if a and b are different (even with different signs), they form a different pair. Wait, no. For example, (2,4) and (2,-4) are two different unordered pairs. Because {2,4} and {2,-4} are different sets. So each of these pairs can be considered separately, as long as they have a valid transformation.

But this complicates things, as the number of possible pairs could be very large. For n=1e5, the total possible pairs would be O(n^2), which is 1e10, which is impossible to process directly.

Therefore, there must be a mathematical approach to model this.

Alternative approach:

The problem can be transformed into considering all possible pairs (m, k) of absolute values (m and k in 2..n), and for each such pair, compute the maximum possible x (if any) between them (either m divides k or k divides m, with x>1 in absolute value). Then, multiply that maximum x by the number of ordered pairs (a, b) with |a|=m and |b|=k, and a and b can form such a transformation. But this seems difficult.

Alternatively, for each possible (m, k) where m and k are positive and 2<=m, k<=n, compute whether there's a valid x (either m divides k and k/m >1, or k divides m and m/k >1). For each such (m, k), if such x exists, then compute the maximum possible x between the two directions (k/m or m/k), then multiply by the number of (a, b) pairs with |a|=m and |b|=k that can form a valid transformation.

Wait, but for a given (m, k), the valid transformations between a and b (where |a|=m, |b|=k) can be:

Case 1: a*x = b. So |a| * |x| = |b|. So |x| = |b| / |a|. So if |x|>1, then |b| > |a|, and |b| must be divisible by |a|. Then, x is either (b/a) which is positive (if a and b have same sign) or negative (if signs differ). But |x| must be |b| / |a|.

Case 2: b*x =a. So |b| * |x| = |a|. So |x| = |a| / |b|. Similarly, this requires |a| > |b| and |a| divisible by |b|. |x|>1 implies |a| > |b|.

So for each (m, k), m and k are the absolute values of a and b. Let's consider m and k.

If m < k:

Then, the possible x for a→b is x = k/m, but only if m divides k. Then, the contribution is k/m. For this to be valid, x must be integer (since a and b are integers). So m must divide k. And x must be >1. So k/m must be an integer greater than 1.

Alternatively, for the other direction (b→a), the x would be m/k, which is a fraction. So that's invalid because |x| must be >1.

So for m <k, the only possible direction is a→b, contributing x=k/m (if k is a multiple of m, and k/m>1).

Similarly, if m >k, the only possible direction is b→a, contributing x=m/k (if m is a multiple of k, and m/k>1).

If m =k, then x would be 1 (if a→b via x=1) which is invalid. Or x could be -1, but |x|=1 is not allowed. So for m=k, no valid transformation.

So the maximum x for a pair (m, k) is max(k/m if m divides k and k/m>1, m/k if k divides m and m/k>1). But for m <k, only the first is possible. For m>k, only the second is possible.

So for each pair (m, k) where m and k are positive integers between 2 and n, and m divides k (if m<k) or k divides m (if m>k), with the quotient x>1, then the contribution is x multiplied by the number of ordered pairs (a, b) that can form this x. But how to count the number of such ordered pairs (a, b) where |a|=m, |b|=k, and the transformation is possible.

Wait, the unordered pair {a, b} is considered once. Each such pair can contribute the maximum x possible for that pair.

But wait, no. The problem statement allows all possible (a, b) pairs (with |a| and |b| in [2, n], and a and b can be positive or negative), and for each pair (a, b), if there exists x such that a*x =b or b*x =a with |x|>1, then the maximum x possible for that pair is added to the total once.

So for each (a, b) pair, if they can form a transformation, then their contribution is the maximum x possible (from either direction), but each unordered pair {a, b} is considered once. However, if (a, b) and (b, a) are considered the same pair, then we need to choose the maximum possible x between the two directions.

But according to the problem statement, once you use a transformation from a to b, you can't use any transformation between a and b again. So for each unordered pair {a, b}, you can choose to use either a→b (if possible) or b→a (if possible), whichever gives a higher x. But if both are possible, you have to choose the higher x.

So the problem reduces to:

For each unordered pair {a, b} (where a and b are integers with |a|, |b| ≥2, ≤n), compute the maximum x possible (either from a→b or from b→a, if any). Sum all such x's.

But the problem is that for n=1e5, the number of possible pairs is O(n^2), which is 1e10 and impossible to handle directly. So we need a smarter approach.

But perhaps we can model the problem by considering the absolute values of a and b, and then for each possible (m, k) (m and k are their absolute values), calculate how many (a, b) pairs (with signs) would have this (m, k) and contribute x. Then sum over all (m, k) pairs.

But even this requires O(n^2) operations, which is impossible.

Alternative approach: group the pairs (a, b) by their absolute values m and k, and for each m and k, compute the number of such pairs and their maximum x.

For example:

For a pair (m, k) where m divides k (m <k), the x is k/m. Each such pair (a, b) where |a|=m, |b|=k, and a divides b (i.e., a divides b, and b/a is integer, but in the problem statement, the x must be integer. So for a to multiply by x to get b, x must be integer.

Wait, but a can be negative. For example, a = -m, b =k. Then a *x =b → -m *x =k → x= -k/m. But m divides k, so k/m is integer. So x is -(k/m). But |x|=k/m>1, which is allowed. So for a given m and k (with m <k and m divides k), all possible (a, b) pairs with |a|=m, |b|=k, and a and b have signs such that a*x =b (with x being k/m or -k/m) are valid. How many such pairs are there?

Let's see: a can be m or -m. For each a, to have a*x =b (where |b|=k, and x is an integer with |x|>1):

Case 1: m divides k. Then k/m is x. So possible x's are ±(k/m), but since |x|>1, k/m must be >=2.

So for a given m and k (m divides k, x =k/m >=2), the possible pairs (a, b) would be:

a can be m or -m.

For each a, x can be either positive or negative, as long as a*x =b (where |b|=k).

Wait, but x must be an integer. So for a =m:

b = a *x → x must be such that m *x has absolute value k. So |x| =k/m. Since k/m is x0 (an integer >=2), x can be x0 or -x0.

So for a =m:

x can be x0 or -x0.

Then, b = m *x0 → which is k, or m * (-x0) → which is -k.

So for a =m, possible b's are k and -k. Each of these gives a valid transformation (a, b).

Similarly, for a =-m:

a *x = (-m) *x. We want this to be equal to b, which has absolute value k. So |(-m)*x| = m * |x| =k. So |x|=k/m, which is x0. So x can be x0 or -x0.

So for a =-m:

b can be (-m)*x0 = -m *x0 = -k (since x0 =k/m) → b =-k. Or (-m)*(-x0) = m*x0 =k → b=k.

So for a =-m, possible b's are -k and k.

So for each (a, b) pair with |a|=m and |b|=k (where m divides k, and k/m >=2), there are 4 possible pairs:

(m, k), (m, -k), (-m, k), (-m, -k).

But each of these is a separate unordered pair? Wait, no. Because {a, b} is unordered. So for example, {m, k} and {k, m} are the same if m=k. But m and k are different here. Wait, but if m divides k, then m <k. So the pairs (m, k) and (k, m) are considered different when m !=k. But for m <k, the pairs (a, b) where a is m and b is k is considered as a pair with a <b? No, because a and b can be negative. So the unordered pairs {a, b} are the same as {b, a} regardless of their values.

But in our case, for a pair (m, k) where m <k, each possible (a, b) pair (with |a|=m, |b|=k) will have a unique {a, b} pair. For example, (m, k), (m, -k), (-m, k), (-m, -k) are all distinct unordered pairs. Because, for example, {m, k} is the same as {k, m}, but since m and k are distinct, and m <k, the unordered pairs {a, b} will have |a|=m and |b|=k. Wait, no. For example, if a=3 and b=6, {3,6} is the same as {6,3} but in our case, since m=3 and k=6, which is m <k, but when considering unordered pairs, {a, b} is the same as {b, a}, but in this scenario, since m <k, all (a, b) pairs derived from m and k will have |a|=m and |b|=k, but the unordered pairs {a, b} can vary based on signs. For example, (3,6) and (6,3) are different only if 3 is not equal to 6. But in this case, m=3, k=6, so a=3, b=6: the unordered pair is {3,6}, which is the same as {6,3}. But since m and k are in the order m <k, perhaps each unordered pair {a, b} with |a|=m and |b|=k (m <k) is considered once. But I'm getting confused here.

Alternatively, let's think of all possible unordered pairs {a, b} where a and b are integers with |a|, |b| >=2 and <=n. Each such pair can be considered once. For each pair, compute the maximum x possible (if any) and add it to the sum.

But how do we compute this efficiently?

Alternative idea: For each possible x (>=2), compute how many pairs (a, b) can be connected via x, such that a *x =b. For each such pair, we can count how many such (a, b) exist, and multiply by x (since each contributes x to the sum). But we need to avoid double-counting pairs that can be connected via multiple x's.

But this approach may not work directly, but perhaps there's a way to model the problem in terms of multiples.

Another approach: For each possible a in the range [2, n], both positive and negative, for each possible x (integer, |x| >=2), compute b =a *x. If |b| is within [2, n], then this transformation is allowed. Each such pair (a, b) contributes |x| to the sum. However, each unordered pair {a, b} can only be counted once, even if multiple x's are possible. But since we want the maximum sum, we need to choose the x with the largest |x| for each pair.

Wait, but this isn't correct. Because for a pair (a, b), there may be multiple x's that satisfy the condition (either a*x =b or b*x =a). For example, a=2, x=2 gives b=4. Then, for a=4, x=0.5 gives b=2 (but x must have |x|>1, which is not allowed here). So the maximum x for {2,4} is 2. So the sum adds 2 for this pair.

But for a pair like a=8, b=4: a*x =b → x=0.5 (invalid). b*x =a → x=2 (valid). So the maximum x is 2.

So for each pair (a, b), the maximum x is max of possible x's from a→b and b→a. So the maximum x is the maximum between (b/a if it's integer and |b/a|>1) and (a/b if it's integer and |a/b|>1). If both are valid, take the maximum.

But again, this would require checking each pair (a, b), which is O(n^2) and impossible for n=1e5.

So we need a way to compute this sum efficiently by grouping terms.

Let's think of the problem in terms of the absolute values of a and b. Let's say m =|a|, k=|b|.

Then, for each pair (m, k), we can compute whether there's a valid x (either m divides k or vice versa) with x >=2. The maximum x for this pair is max(k/m, m/k) if one is valid, or whichever is valid.

But for each (m, k), the maximum x is the maximum of (k/m if k is divisible by m and k/m >=2) and (m/k if m is divisible by k and m/k >=2). Only one of these can be possible, except when m=k, which is not possible as x would be 1.

So for each (m, k), where m and k are in [2, n], m !=k, and either m divides k or k divides m, with the quotient >=2, the maximum x is the quotient (either k/m or m/k). And for each such pair, we need to count the number of unordered pairs {a, b} (with |a|=m, |b|=k) that can contribute this x.

But how many such {a, b} pairs are there for a given (m, k) pair?

Let's take an example. For m=2, k=4. The valid x is 2 (since 4/2=2). For each possible a and b:

a can be 2 or -2.

b can be 4 or -4.

The possible pairs (a, b) that can be transformed with x=2 are those where a*2 =b. So:

2 *2 =4 → (2,4).

2 *2 =4 → (2,4). Similarly, other possibilities:

-2 * (-2) =4 → (-2,4). So x= -2. |x|=2.

-2 *2 =-4 → (-2, -4). x=2. |x|=2.

2 * (-2) =-4 → (2, -4). x=-2. |x|=2.

Similarly, when a is 2 and b is 4 or -4, there are two possible x's (2 or -2) that can make a*x =b. But the maximum x between the two directions (a→b and b→a) is 2. So each of these (a, b) pairs contributes 2 to the sum.

But how many such pairs are there?

For m=2 and k=4:

Each a can be 2 or -2.

For each a, there are two possible b's (4 or -4) such that a*x =b with x=2 or x=-2.

So for a=2: x=2 gives b=4, x=-2 gives b=-4.

For a=-2: x=-2 gives b=4 (since -2 * (-2) =4), x=2 gives b=-4.

So there are 4 possible ordered pairs (a, b) where a→b is possible with x=2 or x=-2, but each of these contributes |x|=2.

But since the pairs {a, b} are unordered, how many distinct unordered pairs are there?

For each (a, b) pair, like (2,4), (2,-4), (-2,4), (-2,-4), these are four distinct unordered pairs. Because {2,4} is different from {2,-4}, etc.

So each of these four pairs contributes 2 to the sum.

But wait, wait. For {2,4}, the transformation can be done via x=2. For {2,-4}, the transformation is a=2, x=-2 gives b=-4. So x's absolute value is 2. So each of these pairs contributes 2.

So for the pair (m=2, k=4), the total contribution is 4 * 2 =8? But in the first example, n=4, the output is 8. Which matches. Because in that example, the maximum sum is 8. Which is exactly the contribution from m=2, k=4 (4 pairs, each contributing 2).

But what about other pairs?

Wait, in the first example, n=4. Are there other pairs that contribute?

For example, m=2, k=6: but n=4, so k can't be 6.

Other pairs: m=2, k=6 is out.

Another pair: m=3, k=6: but again, n=4.

So in the first example, perhaps only m=2, k=4 contributes. Which gives 4 pairs, each contributing 2: 4*2=8.

But what about m=2 and k=8? No, but n=4, so k is 4.

So in the first example, that's the only possible pair. Which gives 8, which matches the sample.

Another example: n=6, output is 28.

Let's see. For m=2, k=4: 4 pairs contributing 2 each (sum 8). For m=2, k=6: x=3. Each pair contributes 3. How many such pairs? For m=2, k=6: a can be 2 or -2, and for each a, x can be 3 or -3. So for a=2: x=3 → b=6, x=-3 → b=-6. So two pairs. Similarly for a=-2: x=-3 gives b=6, x=3 gives b=-6. So four pairs. Each contributes 3. So 4*3=12. So sum is 8+12=20. But the sample output is 28, so there are other contributions.

Other pairs: m=3, k=6. x=2. Contribution is 2 per pair. Number of pairs: 4. So 4*2=8. Sum now 28. Which matches the sample.

So for n=6, the pairs are (2,4) (sum 8), (2,6) (sum 12), (3,6) (sum 8), and maybe others? Wait, what about (2, 8)? No, n=6. Or (4, 6): 4 divides 6? No, 6/4=1.5. So no. So the sum is 8+12+8=28. Which matches the sample.

So the approach is:

For each possible pair (m, k) where m divides k and k/m >=2, or k divides m and m/k >=2 (but since m and k are ordered, perhaps we can process m <k and m divides k, and then m >k and m is a multiple of k. But how to avoid double counting? Because m and k can be in any order. So perhaps it's better to process all pairs where m <k and m divides k, and then multiply by the number of sign combinations (4) for each such pair, and sum m x (k/m) * 4. Similarly for m>k, but that would be redundant.

Wait, no. Because if we process all pairs where m <k and m divides k (so k/m >=2), then for each such pair, the contribution is (k/m) multiplied by 4 (number of sign combinations) because each a can be ±m and each b can be ±k, leading to 4 possible pairs {a, b} where the transformation is possible. Each of these 4 pairs contributes (k/m) to the total.

Similarly, for pairs where k <m and k divides m (so m/k >=2), the contribution is (m/k) multiplied by 4. But in this case, since m >k, these pairs are different from the previous ones (m <k), so we can handle them separately.

Wait, no. Because for m=3 and k=6, the pairs are (3,6) → m=3, k=6. But m <k, but 3 does not divide 6? Wait, 3 divides 6 (6/3=2). So m=3, k=6: m divides k, x=2. So contribution is 2*4=8.

But for m=6, k=3: m is 6, which is divisible by k=3. So m/k=2. So for this pair, the contribution is 2*4=8. But this is the same as the pair (3,6), which is m=3, k=6. So processing m <k and m divides k would include all such pairs, but when we process m >k and k divides m, we would be counting the same pairs again. So this would lead to double-counting.

Therefore, to avoid double-counting, we need to process each pair (m, k) where m <k and m divides k, and then each pair (m, k) where m >k and k divides m, but that would result in processing each pair (m, k) exactly once, but in reality, each pair {m, k} (unordered) is considered once. So perhaps we can process all pairs where m <k and m divides k, and each of those pairs contributes 4 * (k/m). And also process all pairs where m >k and k divides m, which is the same as m being a multiple of k and m/k >=2. But this would be the same as processing pairs where k <m and k divides m. So for each such pair, the contribution is (m/k) *4. But these are separate pairs, so the sum is for all (m, k) where m divides k or k divides m, with quotient >=2, multiplied by the corresponding x and 4.

But this approach would result in processing each possible valid pair (m, k) exactly once (either m <k or m >k), and summing their contributions.

But how to compute this efficiently?

The key is to iterate over all possible m and x such that m*x <=n, and then compute k=m*x. For each m >=2 and x >=2, and m*x <=n, add 4 *x to the total sum. Because each such (m, k) pair (where k =m*x) contributes 4*x (since there are four sign combinations, each contributing x).

But also, for each m >=2, x >=2, and k=m*x <=n, this covers all pairs (m, k) where m divides k and x= k/m. Then, for each such (m, k), we add 4*x.

But what about the case where k divides m (i.e., m is a multiple of k), but k <m. For example, m=6, k=3 (x=2). But in this case, m=6, k=3, x=2 (since 3*2=6). So in this case, when m=6 and x=2, we need to process k=3. But in our previous iteration over m and x, m=3, x=2 gives k=6, which would be processed as part of the m=3 case.

So in other words, the pairs where m >k and k divides m are already covered when m is k*x, which is when k is a divisor of m. So when processing k and x, k*x =m. But this would be handled when m is k*x. So this suggests that by iterating m from 2 to n, and for each m, iterate x from 2 to m*x <=n, then we can cover all pairs where m divides k (k= m*x), and then the contribution is 4*x. But what about pairs where m is a multiple of k (k divides m)?

Ah, no. Because when m is a multiple of k, then k = m /x where x >=2. For example, m=6, k=3, x=2. So in this case, when we process k=3, x=2, then k*x=6, so the pair (3,6) is added with contribution 4*2=8. But when m=6 and k=3, the pair (6,3) would be processed when k=3 and x=2, leading to m=6. So the contribution is already counted.

Therefore, to avoid double-counting, we only need to process all pairs where m <k and m divides k (k =m*x). For each such pair, we add 4*x. This will cover all possible pairs (m, k) where m divides k and x >=2. And when k is m*x, then for the pair (k, m), we would need to check if m divides k. Which it does, but since m <k, we have already processed it when m was the smaller number.

Thus, the approach is to iterate over all possible m >=2, and for each m, iterate x >=2, such that m*x <=n. For each such (m, x), compute k=m*x, and add 4*x to the total. This covers all pairs where m <k and m divides k, and x= k/m. This way, each valid pair (m, k) with m <k and k divisible by m is processed once, contributing 4*x where x =k/m.

Additionally, pairs where k <m and k divides m would be processed when m is a multiple of k. For example, if m=6 and k=3, then this is processed when k=3 and x=2, leading to m=6. So the contribution is 4*2=8 for the pair (3,6).

Wait, no. When k=3 and x=2, then m=k*x=6. So the pair (3,6) is processed, and the contribution is 4*2=8. So for the pair (6,3), which is the same as (3,6) in terms of unordered pairs, it is already counted once.

But according to our approach, for each m (starting from 2 to n), and x >=2, we compute k =m*x. So for m=3, x=2, k=6. This contributes 4*2=8 for the pair (3,6). For the pair (6,3), since m=6, x=0.5 (but x must be >=2), it is not processed. So the approach of iterating m from 2 to n and x from 2 upwards, and k=m*x, ensures that all pairs where m <k and m divides k are processed once, and their contributions are added. The pairs where k <m and k divides m are not processed in this loop, but those pairs are processed when k is the m and m is the k*x.

For example, the pair (6,3) is processed when m=3, x=2, leading to k=6, which is the same as the pair (3,6). So the contribution for (6,3) is already accounted for in the (3,6) processing.

Thus, the correct approach is to loop through all m from 2 to n, and for each m, loop x from 2 to as long as m*x <=n. For each such (m, x), add 4 *x to the total sum.

But what about pairs where m=2, k=8, and x=4 (if n >=8). For example, m=2, x=4, k=8. Contribution is 4*4=16. But are there other pairs like (2,8) that can be processed via different x's? For example, x=2 would give k=4. Then x=2 again for m=4 gives k=8, contributing 4*2=8. So for the pair (2,8), it's processed once when x=4 (2*4=8) and once when m=4 and x=2 (4*2=8). But wait, no. Because when m=4 and x=2, k=8, so the pair (4,8) is processed. But (2,8) is a different pair, which is processed when m=2 and x=4 (if 2*4 <=n).

So each pair (m, k) is processed only once: when m is the smallest possible divisor of k, multiplied by x. For example, (2,8) is processed when m=2, x=4. (4,8) is processed when m=4, x=2.

But each pair (m, k) is processed once, and their contributions are summed.

So the approach is correct.

Therefore, the solution is to compute the sum over all m >=2, x >=2, m*x <=n, of 4*x.

But wait, no. Because for each m and x, k=m*x. So the contribution is 4*x for each (m, k) pair where k is a multiple of m, and x =k/m >=2.

So for example, m=2, x=2: k=4. Contribution 4*2=8.

m=2, x=3: k=6. Contribution 4*3=12.

m=2, x=4: k=8. Contribution 4*4=16, etc.

But what about when m=3, x=2: k=6. Contribution 8.

Thus, for the sample input n=4, the sum would be:

m=2, x=2 → k=4. contribution 8.

No other pairs. So total sum is 8. Which matches the first sample.

For n=6:

m=2, x=2 →4: contribution 8.

m=2, x=3 →6: contribution 12.

m=3, x=2 →6: contribution 8.

m=4, x=2 →8: which is larger than 6, so not processed.

So sum is 8+12+8=28, which matches the second sample.

For n=2:

m=2, x=2 →4 >2: not processed. So no contributions. Output is 0.

Thus, the correct approach is to sum for all m >=2 and x >=2 where m*x <=n, 4*x.

But wait, why 4*x? Because each (a, b) pair with |a|=m and |b|=k can be formed in four ways (a can be ±m, b can be ±k). For each of these four pairs, the contribution is x. So each (m, x) contributes 4*x.

Yes. So the sum is indeed the sum over all m >=2, x >=2, m*x <=n of 4*x.

So the algorithm is:

Initialize the total sum to 0.

For each m from 2 to n:

   For x from 2 to ...:

      if m *x exceeds n, break.

      add 4*x to the total sum.

But wait, what about multiple x's for the same m and k?

For example, m=2, x=2 →k=4. Then m=2, x=3 →k=6. Also, m=2, x=4 →k=8 (if allowed). Each of these is processed once, adding 4*x for each.

So the code can be written as:

sum = 0

for m in 2 to n:

   x = 2

   while True:

       k = m *x

       if k >n:

           break

       sum += 4 *x

       x +=1

So this loops through all m >=2, and x starts at 2. For each x, compute k =m *x. If k <=n, add 4*x. Then x increases by 1.

This should compute the correct sum.

But let's test this with the sample inputs.

Sample 1: n=4.

m starts at 2.

x=2: k=4 <=4. sum +=4*2=8.

x=3: k=6>4 → break.

So sum is 8. Correct.

Sample 2: n=6.

m=2:

x=2: k=4 → add 8.

x=3: k=6 → add 12.

x=4: k=8>6 → break.

sum is 20.

m=3:

x=2: k=6 → add 8. sum is 28.

x=3: k=9>6 → break.

m=4:

x=2: k=8>6 → break.

m=5: x=2 →10>6.

m=6: x=2 →12>6.

So sum is 28. Correct.

Sample 3: n=2.

m=2: x=2 →k=4>2 → no addition. sum remains 0. Correct.

So this approach works.

Thus, the code can be written as follows.

Now, considering the constraints. For n=1e5, this algorithm's time complexity is O(n * sqrt(n))? No. Wait, for each m, the x runs from 2 to floor(n/m). So the total number of iterations is sum_{m=2 to n} floor(n/m) -1 (since x starts at 2, but floor(n/m) >=x implies x can be up to floor(n/m). So the total number of iterations is sum_{m=2}^n floor(n/m -1), because x starts at 2 and goes up to floor(n/m), so x can be 2, 3, ..., floor(n/m). The number of x's is floor(n/m) -1. Because x starts at 2. For example, if floor(n/m) is 5, then x can be 2,3,4,5 → 4 terms, which is 5-1=4.

But sum_{m=2}^n floor(n/m -1) is approximately O(n log n), which is acceptable for n=1e5. Because sum_{m=1}^n floor(n/m) is O(n log n). For m=2 to n, it's sum_{m=2}^n (floor(n/m) -1) = sum_{m=2}^n floor(n/m) - (n-1) → which is roughly O(n log n) - O(n) → O(n log n), which is acceptable for n=1e5.

Thus, the code should work within the time limits.

So the Python code will be:

Read n from input.

Initialize total=0.

Loop m from 2 to n:

   x = 2

   while True:

       k = m *x

       if k >n:

           break

       total +=4 *x

       x +=1

Print(total)

Wait, but for m=2 and x=2: k=4. This is correct.

But wait, for m=6 and x=2: k=12, but if n is 6, it's not processed. So the code is correct.

Yes.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    total = 0
    for m in range(2, n + 1):
        x = 2
        while True:
            k = m * x
            if k > n:
                break
            total += 4 * x
            x += 1
    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
""",
            "output": \
"""\
28
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    total = 0
    for m in range(2, n + 1):
        x = 2
        while True:
            k = m * x
            if k > n:
                break
            total += 4 * x
            x += 1
    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
""",
            "output": \
"""\
0
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

Sample 3: n=2. All m=2:

x=2 →k=4>2. Break. Sum 0.

Thus, the code works for the samples.

But wait, in the problem statement, the third example n=2, output is 0. Correct.

Thus, the code should be correct.
</think>

```python
n = int(input())
total = 0
for m in range(2, n + 1):
    x = 2
    while True:
        k = m * x
        if k > n:
            break
        total += 4 * x
        x += 1
print(total)
```
