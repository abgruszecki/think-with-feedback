<think>
Okay, I need to solve this problem where I have to find an array a given arrays b and c. The constraints are that for each i, the sum of a_i AND each a_j (including a_i itself) equals b_i, and the sum of a_i OR each a_j equals c_i. Hmm, let's think about how to approach this.

First, I remember that for each element in a, the sum of ANDs and ORs depends on the bits present in the elements. Maybe I can model this bit by bit. Like, for each bit position, determine how many elements have that bit set. Then, using that information, compute possible a_i values that satisfy the given b and c arrays.

Wait, the key here is to decompose the problem into individual bits. Because for each bit position k (like 0 to 30), the contribution to b_i and c_i can be calculated independently. Let's break it down.

For each bit k, suppose there are x elements in a that have the k-th bit set. Then, for a particular a_i:

The sum of (a_i AND a_j) for bit k is equal to the number of times both a_i and a_j have the k-th bit set. So, if a_i has the k-th bit set, the contribution is x * 2^k (because each of the x elements contributes 2^k when ANDed). If a_i doesn't have the bit set, the contribution is 0.

Similarly, for the OR sum: for each a_j, if either a_i or a_j has the bit set, then the contribution is 2^k. So the total for OR is (if a_i has the bit set: n * 2^k. Otherwise, x * 2^k. Because if a_i doesn't have the bit, then only the x elements that do have it contribute.)

So for each bit k, and for each a_i, the contribution to b_i and c_i from bit k is as follows:

If a_i has bit k set:
- b contributes x * 2^k
- c contributes n * 2^k
If a_i does not have bit k set:
- b contributes 0
- c contributes x * 2^k

Wait, but the sum for OR is for each j: a_i OR a_j. So for a particular bit k, if a_i has the bit set, then OR with any a_j will have the bit set. So the sum for that bit is n * 2^k. If a_i does not have the bit set, then the OR will have the bit set only if a_j has it, so the sum is x * 2^k.

So for each bit k, the contributions to the b and c arrays can be determined by whether the bit is set in a_i and the total count x of bits set in that position across all a elements.

Now, the problem can be broken down per bit. For each bit k, we can model the possible x (number of elements with the bit set) and determine for each a_i whether they have that bit set, such that the sum of contributions to b_i and c_i matches.

But how do we compute this for all bits and all elements?

Let me think. For each bit k:

Let x be the number of elements in a with bit k set.

For each a_i, if the bit is set, then for that bit's contribution to b_i is x * 2^k. For c_i, it's n * 2^k.

If the bit is not set, then the contribution to b_i is 0, and to c_i is x * 2^k.

But the actual b_i and c_i are the sum over all bits of these contributions. So for each bit, the sum of contributions must equal the total for that bit.

But how can we separate the contributions from different bits? Since each bit's contribution is a multiple of 2^k, and each bit is independent (since binary digits don't interfere with each other), we can decompose each b_i and c_i into their binary components and check for each bit whether the contributions from that bit fit.

Wait, perhaps for each bit, the contributions to all b_i and c_i from that bit can be checked independently. Let me see.

Let's denote that for each bit k, the contribution to b_i is B_ik, and to c_i is C_ik. Then, the total b_i is sum over k of B_ik, and similarly for c_i. But since 2^k is a power of two, each bit's contribution to B_ik and C_ik is unique. Therefore, we can process each bit independently, and for each bit, determine the possible x (number of elements with that bit set) and which a_i's have that bit set.

But how?

Let's process each bit k separately.

For each a_i, whether it has bit k set (let's denote this as s_i) is a binary variable (0 or 1). Then, the total x is sum(s_i for all i).

For each i, the contribution to B_ik is s_i * x * 2^k. The contribution to C_ik is (s_i ? n : x) * 2^k.

But the actual B_ik is the part of b_i that is in the 2^k's place. Wait, no. Because when you add up all the bits, the total b_i is sum over k of B_ik, where B_ik is the sum of (a_i AND a_j) for all j, but considering only the k-th bit. Similarly for C_ik.

But how do we extract B_ik and C_ik from the given b and c values?

Wait, perhaps for each bit k, the sum of the contributions (from all bits) to b_i must equal the given b_i. Similarly for c_i. But since each bit's contribution is a multiple of 2^k, the total contribution from bit k is (B_ik) which is s_i * x * 2^k. So for each bit k, the sum over all bits of (s_i * x_k) * 2^k must equal b_i, where x_k is the number of elements with bit k set.

Wait, perhaps the approach is to consider each bit k in isolation, and for that bit, determine x_k and the s_i (whether each a_i has the bit set) such that:

For each i:

B_ik = s_i * x_k * 2^k

C_ik = (s_i * n + (1 - s_i) * x_k) * 2^k

And these B_ik and C_ik must sum to the given b_i and c_i.

But how do we find x_k and s_i for each bit?

Alternatively, since all bits are independent, perhaps we can process each bit k individually. For each bit k, we can compute the required x_k and which a_i have the bit set, such that the contributions from this bit to the b and c arrays are compatible with the given values.

But how to extract the possible x_k and s_i?

Let's consider that for each bit k, the contribution to each b_i and c_i from this bit must be such that when summed over all bits, they equal the given b and c.

But the problem is that the given b and c arrays are given as their total sum, not per bit. So we need to find for each bit k, a way to split the bits such that the sum over all bits' contributions gives the correct b and c. However, since each bit's contribution is a multiple of 2^k, and different bits don't interfere (since 2^k is unique), perhaps for each bit, we can compute the required x_k and s_i for that bit, and then combine all bits' contributions.

Wait, maybe the approach is to process each bit in isolation, considering that for each a_i, the presence of the bit (s_i) affects the contribution of that bit to both b_i and c_i. So for each bit k, we can compute the possible x_k (number of set bits in this position) and the s_i's, such that for each i, the sum of the contributions from this bit to b_i and c_i are compatible with the given b and c.

But how?

Let's think for each bit k:

Let’s denote for each i:

s_i is 1 if a_i has the bit set, else 0.

x = sum(s_i) = number of elements with bit k set.

For the bit k, the contribution to b_i is s_i * x * 2^k. So the total b_i must be the sum over all bits of s_i (for that bit) multiplied by x_k (for that bit) * 2^k.

Similarly, the contribution to c_i is (s_i * n + (1 - s_i)*x) * 2^k.

But how can we process this bit by bit?

The key idea is that for each bit k, the sum of the contributions from this bit to b_i and c_i must equal the part of the given b_i and c_i that is in the 2^k's place. Wait, but that's not necessarily the case. Because for example, when you have higher bits, their contributions could affect the lower bits through the sum. No, actually, each bit's contribution is in the 2^k term, and since other bits' contributions are multiples of different powers, the sum for each bit can be considered independently.

Wait, no. Because for example, if you have two bits, say k=1 and k=0. Then the sum of their contributions is (s_i * x_1) * 2^1 + (s_i * x_0) * 2^0. But in the actual b_i, the value is the sum of all (a_i AND a_j) terms. Since each a_i AND a_j is the sum over all bits where both a_i and a_j have the bit set. So the sum for each bit is s_i * x_k * 2^k. So the sum across all bits is indeed the sum of each bit's contribution. Therefore, the total b_i is equal to the sum over all bits of s_i (for that bit) multiplied by x_k (for that bit) times 2^k.

Similarly for c_i.

So, for each bit k, the sum (s_i * x_k) * 2^k is the contribution to b_i, and (s_i * n + (1 - s_i)*x_k) * 2^k is the contribution to c_i.

Therefore, the given b_i and c_i must be compatible with these per-bit contributions. But since the per-bit contributions are additive, perhaps we can decompose each b_i and c_i into their individual bits' contributions and process each bit independently.

But how?

Let’s think for a particular bit k. Let's compute the required contribution from this bit to each b_i and c_i.

For example, for each i, the contribution from bit k to b_i is (s_i * x) * 2^k, and to c_i is (s_i * n + (1 - s_i) * x) * 2^k.

But the actual given b_i and c_i are the sum of all such contributions. Therefore, the sum over all bits k of [s_i (k) * x_k * 2^k] = b_i, and sum over all bits k of [ (s_i(k) * n + (1 - s_i(k)) * x_k) * 2^k ] = c_i.

But to process this, perhaps for each bit k, we can find x_k (number of elements with the bit set) and the s_i(k) (whether a_i has the bit set) such that the per-bit contributions for that bit to each b_i and c_i are compatible.

But how to do that?

An alternative approach is to model for each bit k, the possible x_k and the s_i(k) values, ensuring that for each i, the sum of contributions across all bits equals the given b_i and c_i. But since each bit is independent, perhaps we can process each bit individually and accumulate the results.

Wait, but the problem is that the s_i(k) for each bit k contributes to multiple bits in the a_i (since each a_i is the sum over all bits of s_i(k) * 2^k). So when processing a bit, the s_i(k) for that bit is determined, and then the a_i's bits are built up.

But how can we process each bit in isolation?

Let's think of it this way: For each bit k, the possible s_i(k) (0 or 1) for each i, and x_k (sum of s_i(k)), must satisfy the following for each i:

- For bit k, the contribution to b_i is (s_i(k) * x_k) * 2^k. Similarly for c_i.

But the sum of these across all bits must equal the given b_i and c_i.

But how do we know which part of b_i and c_i comes from each bit?

Ah, this is the crux of the problem. Because the given b_i and c_i are the sum of contributions from all bits, but we need to decompose them into per-bit contributions. However, since each bit's contribution is a multiple of 2^k, and for higher bits (larger k), their contributions are larger than the sum of all lower bits. So perhaps, we can process bits in order from highest to lowest, and for each bit, determine the contribution that must be present in the given b_i and c_i.

Wait, let's see. For example, the highest possible bit is 30 (since 2^30 is around 1e9, which is the maximum for b_i and c_i). Let's process each bit starting from 30 down to 0.

For each bit k, after processing higher bits, we can subtract their contributions from the current b_i and c_i, and then the remaining parts for each i must be compatible with the current bit's contribution.

But how?

Let me outline the steps:

1. For all bits from highest (30) to 0:

   a. For each a_i, determine if the current bit k is set (s_i(k) = 1 or 0).

   b. Compute x_k, the number of elements where bit k is set.

   c. For each i, compute the contribution of this bit to b_i and c_i, subtract these from the current remaining b_i and c_i. Then, proceed to the next lower bit.

But how do we compute s_i(k) and x_k for each bit, given the remaining b_i and c_i?

Alternatively, for each bit k, the contribution to the current remaining b_i and c_i must be exactly (s_i(k) * x_k) * 2^k and (s_i(k) * n + (1 - s_i(k)) * x_k) * 2^k, respectively.

But how to find x_k and s_i(k) such that this holds for all i.

Let’s consider that for each bit k, the possible contributions are:

For each i, let's denote the remaining b_i and c_i (after subtracting higher bits' contributions) as current_b_i and current_c_i.

Then, for the current bit k:

current_b_i must be equal to s_i(k) * x_k * 2^k + ... (lower bits contributions).

But perhaps, for each bit k, the current remaining b_i and c_i must have their k-th bit (in the binary representation) matching the contributions from this bit's s_i(k) and x_k.

Wait, maybe not. Because the contributions from this bit are multiples of 2^k. So for example, the contribution from this bit to b_i is s_i(k) * x_k * 2^k. So the sum of all bits' contributions must equal the original b_i.

But when processing bits from high to low, perhaps for each bit k, the remaining part of b_i and c_i (after higher bits) must allow the contribution for this bit to be an integer multiple of 2^k.

Wait, here's an idea: For each bit k, the contribution from this bit to b_i is a multiple of 2^k. So, when we process the bits in order, for each k, the remaining current_b_i must be congruent modulo 2^{k} to the sum of contributions from lower bits.

But perhaps this is getting too complicated. Let's try to model this for a single bit.

Suppose we are processing bit k. Let's first check the possible x (number of elements with bit k set) and for each i, whether s_i is 0 or 1.

For each i, the contribution to current_b_i is s_i * x * 2^k. The contribution to current_c_i is (s_i * n + (1 - s_i)*x) * 2^k.

These contributions must be subtracted from the current remaining current_b_i and current_c_i, and the remaining after processing all bits should be zero for all i.

But how can we compute x and s_i for each bit?

Let’s think for each bit k:

We need to find x (number of elements with bit k set) and s_i (for each i, 0 or 1) such that:

For each i:

s_i * x * 2^k ≤ current_b_i (because this is part of the contribution)

Similarly, (s_i * n + (1 - s_i)*x) * 2^k ≤ current_c_i.

But also, after subtracting these contributions, the remaining current_b_i and current_c_i should be valid for lower bits.

But how?

Alternatively, perhaps for each bit k, we can determine x and s_i's such that:

sum over i of s_i * x * 2^k equals the sum over i of (current_b_i's bits that are in 2^k's place) ?

No, maybe that's not the case. Because the sum of contributions from this bit to the b array is x^2 * 2^k (since sum(s_i * x * 2^k) over i is x * sum(s_i) * 2^k = x^2 * 2^k). Similarly, the sum for c array is sum( (s_i * n + (1-s_i)*x ) * 2^k ) = (sum(s_i * n) + sum( (1-s_i)*x )) * 2^k = (n x + (n - x) x) ) * 2^k = (n x + x(n -x )) 2^k = x (n + n -x ) * 2^k ? Wait, perhaps not.

But this is getting too abstract. Let's think of possible cases.

Suppose for a certain bit k, and a certain x (number of elements with bit k set), what are the conditions?

For each element i, the contribution to b_i is s_i * x * 2^k. Similarly, to c_i is (s_i * n + (1 - s_i) * x) * 2^k.

But the sum of these contributions must be compatible with the current remaining b_i and c_i.

But how?

Another approach: for each bit k, the possible contribution to b_i is s_i * x * 2^k. The sum over all i of this is x * sum(s_i) * 2^k = x^2 * 2^k. Similarly, sum over c_i contributions is sum( [s_i n + (1 - s_i) x] ) * 2^k. The sum inside is sum(s_i n) + sum( (1-s_i)x ). Since sum(s_i) is x, sum(s_i n) is n x. sum( (1-s_i) x ) is x (n - x). So total sum is (n x + x (n -x )) * 2^k = x (2n -x) * 2^k.

But these sums must be equal to the sum of the current_b_i and current_c_i. However, since the current_b_i and current_c_i are the sum of all bits' contributions, including this one, perhaps this isn't directly helpful.

Alternatively, perhaps for each bit k, the sum of all bits' contributions to the b array is sum(b_i) = sum_{k} x_k^2 * 2^k. Similarly, sum(c_i) = sum_{k} x_k (2n - x_k) * 2^k.

So we can precompute sum(b_i) and sum(c_i) and check if this holds. If not, it's impossible. But even if the sum holds, individual elements might not.

But this could be a way to check for some conditions. For example:

sum(b_i) must be equal to sum_{k} x_k^2 * 2^k.

sum(c_i) must be equal to sum_{k} x_k (2n -x_k) * 2^k.

If these conditions are not met, the solution is impossible.

But even if they are met, it doesn't guarantee that individual elements are correct.

But perhaps this can help in early pruning.

But how to model x_k for each bit?

Alternatively, let's think for each bit k:

If x_k is the number of elements with bit k set, then for each i:

The contribution to b_i from this bit is s_i * x_k * 2^k. And the contribution to c_i is (s_i * n + (1 - s_i) * x_k) * 2^k.

But for the sum of these contributions over all bits to equal the given b_i and c_i, perhaps for each bit k, the sum of the contributions for this bit must be such that when added to the contributions from other bits, it equals the given values.

But again, how to model this.

Alternatively, since each bit's contribution to b_i and c_i is a multiple of 2^k, perhaps for each bit k, the contributions for that bit can be determined by dividing the current remaining b_i and c_i by 2^k, and then checking modulo 2.

Wait, perhaps this is the key. Let's see.

For example, when processing bit k, all higher bits (k+1 to 30) have already been processed. So the remaining b_i and c_i for each i are the contributions from bits 0 to k.

Wait, no. If we process bits from high to low, then for each i, after processing bits higher than k, the remaining current_b_i and current_c_i are the contributions from bits 0 to k.

But when processing bit k, the contributions from higher bits have already been subtracted. So for each i, the remaining current_b_i must be equal to the sum of contributions from bits 0 to k.

Wait, but when processing bit k, we are subtracting the contributions from this bit, and then proceed to lower bits. So for each bit k, the steps are:

current_b_i = original_b_i minus contributions from all bits higher than k.

current_c_i = original_c_i minus contributions from all bits higher than k.

Then, for this bit k, we need to compute the contribution from this bit (s_i * x * 2^k and (s_i * n + (1-s_i)*x) * 2^k) and subtract them from current_b_i and current_c_i, leaving the remainder for lower bits.

So for bit k:

For each i:

contribution_b = s_i * x * 2^k

contribution_c = (s_i * n + (1 - s_i) * x) * 2^k

current_b_i_after = current_b_i_before - contribution_b

current_c_i_after = current_c_i_before - contribution_c

These current_b_i_after and current_c_i_after must be non-negative, and when all bits are processed, they must be zero for all i.

So how can we model this for each bit k.

But how to find x and s_i's for this bit.

Let's consider the remaining current_b_i and current_c_i before processing bit k. For each i:

contribution_b must be a multiple of 2^k, and when divided by 2^k, gives s_i * x.

Similarly, contribution_c must be a multiple of 2^k, and when divided by 2^k, gives s_i * n + (1 - s_i) * x.

But contribution_b and contribution_c must be exactly equal to s_i * x * 2^k and (s_i * n + (1 - s_i) * x) * 2^k.

So, for each i:

current_b_i_before must have the contribution from bit k equal to s_i * x * 2^k.

So current_b_i_before must be congruent to s_i * x * 2^k modulo 2^{k+1}.

Similarly for current_c_i_before.

But this might not be directly helpful.

Alternatively, when processing bit k, we can divide the current_b_i and current_c_i by 2^k to get the contribution in terms of this bit.

Let me see:

For current_b_i_before, the contribution from bit k is s_i * x * 2^k. So, current_b_i_before must be >= s_i * x * 2^k. Also, after subtracting this contribution, the remaining current_b_i_after must be divisible by 2^k.

Wait, no. Because the remaining current_b_i_after = current_b_i_before - contribution_b. The contribution_b is divisible by 2^k, so current_b_i_after is current_b_i_before - multiple of 2^k. So current_b_i_after is congruent to current_b_i_before mod 2^k.

But current_b_i_after must be the sum of contributions from lower bits, which are multiples of 2^{k-1}, etc. So, current_b_i_after must be congruent to 0 modulo 2^k? Or not necessarily. Because lower bits can sum to any value. So maybe this line of thinking is not helpful.

Let's think differently. For a given bit k, the contributions to b_i and c_i from this bit must be determined.

The contribution to b_i is s_i * x * 2^k. The contribution to c_i is (s_i * n + (1 - s_i) * x) * 2^k.

These contributions must be subtracted from current_b_i and current_c_i, which are the remaining values after processing higher bits.

So, for each i, after processing higher bits, we have current_b_i and current_c_i. For bit k, the contributions must be such that:

s_i * x * 2^k <= current_b_i

and

(s_i * n + (1 - s_i) * x) * 2^k <= current_c_i.

But this is necessary but not sufficient.

Moreover, after subtracting these contributions, the remaining current_b_i and current_c_i must be compatible with the contributions from lower bits.

But how to model this.

Let’s think of the following steps for processing each bit k:

1. For each i, current_b_i and current_c_i are known.

2. For the current bit k, we need to determine s_i (0 or 1) and x (number of s_i=1) such that:

   a. For each i, s_i * x * 2^k <= current_b_i

   b. For each i, (s_i * n + (1 - s_i) * x) * 2^k <= current_c_i

   c. After subtracting these contributions, the remaining current_b_i_after and current_c_i_after must be non-negative.

But how can we find x and s_i's that satisfy these conditions for all i.

Moreover, once x is determined, the s_i's must be such that exactly x of them are 1.

This seems like a problem that could have multiple possibilities for x and s_i. But how to find it.

Alternative approach:

For a given x (number of elements with bit k set), we can determine for each i whether s_i is 0 or 1.

But how?

For each i, the possible s_i is determined by:

If s_i is 1:

   contribution_b = x * 2^k

   contribution_c = n * 2^k

   So, current_b_i must be >= x * 2^k

   current_c_i must be >= n * 2^k

If s_i is 0:

   contribution_b = 0

   contribution_c = x * 2^k

   So, current_c_i must be >= x * 2^k

But also, the choice of s_i must be such that exactly x elements have s_i = 1.

But how to find x and the s_i's that satisfy these constraints.

This seems challenging. Let's think for a specific x.

Suppose we fix x for the current bit k. Then, for each i:

If s_i is 1, then:

   current_b_i >= x * 2^k

   current_c_i >= n * 2^k

If s_i is 0:

   current_c_i >= x * 2^k

But how can we select x and s_i's such that exactly x elements are 1, and the constraints are satisfied.

But even if the constraints are satisfied for each i, the sum of s_i's must equal x. So, x must be the number of elements where s_i is 1.

This seems like a chicken and egg problem. How to choose x and the s_i's.

Alternatively, for each possible x (from 0 to n), check if there exists a subset of x elements where:

- For each element in the subset (s_i=1), current_b_i >= x * 2^k and current_c_i >= n * 2^k.

- For elements not in the subset (s_i=0), current_c_i >= x * 2^k.

But trying all x from 0 to n is impossible for n up to 2e5.

Thus, we need a smarter way to find x.

Wait, perhaps for each bit k, we can compute possible x values based on the current_b_i and current_c_i.

Let's think about the possible x values for a bit k.

The maximum possible x is the number of elements where current_c_i >= n * 2^k. Because for s_i=1, current_c_i must be >= n * 2^k. So, the maximum x possible is the count of elements where current_c_i >= n * 2^k.

Similarly, the minimum x possible is 0. But how.

Alternatively, for x to be a valid value for bit k, the following must hold:

- All elements where s_i=1 must have current_b_i >= x * 2^k and current_c_i >= n * 2^k.

- All other elements must have current_c_i >= x * 2^k.

Moreover, the number of elements with s_i=1 is exactly x.

So, for a given x, the set of possible s_i=1 is the elements i where current_b_i >= x * 2^k and current_c_i >= n * 2^k. The remaining elements (not in this set) must have current_c_i >= x * 2^k.

Additionally, the number of elements in the set must be >= x (to select x elements from them). Wait, no. Because for x to be the count of s_i=1, the set of elements where s_i can be 1 must have at least x elements. Wait, no. For example, if x is 3, we need exactly 3 elements in the subset. So the subset must have at least x elements where they can be 1 (current_b_i >= x * 2^k and current_c_i >= n * 2^k), but we need to choose exactly x of them.

But how?

Alternatively, for a fixed x, the steps would be:

1. Find all elements i where current_b_i >= x * 2^k and current_c_i >= n * 2^k. Let the count of such elements be m.

2. We need to select exactly x elements from these m elements to set s_i=1. So m must be >=x.

3. Additionally, for the remaining elements (those not selected), their current_c_i must >= x * 2^k.

Wait, but if an element is not selected (s_i=0), then current_c_i must be >= x * 2^k. So all elements not in the initial set (those i where either current_b_i < x*2^k or current_c_i <n*2^k) must have current_c_i >=x*2^k.

So, the procedure is:

For a given x, check:

a. The number of elements i where current_b_i >=x*2^k and current_c_i >=n*2^k is >=x.

b. For all elements not in this set, current_c_i >=x*2^k.

If these conditions are met, then x is a possible candidate.

Then, among all possible x candidates, we need to choose one that allows the rest of the bits to be processed.

But how to find x?

Since x can range from 0 to n, trying all possible x for each bit is O(n) per bit, which is not feasible for n up to 2e5 and 31 bits. So this approach is O(31 * n^2), which is way too slow.

Thus, we need a smarter way to compute x for each bit.

Alternative idea: For a bit k, the possible x can be determined by the constraints imposed by the elements.

Let’s consider that for each element i:

If s_i=1:

   current_b_i must >= x*2^k --> x <= current_b_i / (2^k)

   current_c_i must >=n*2^k --> n*2^k <= current_c_i

If s_i=0:

   current_c_i must >=x*2^k --> x <= current_c_i / (2^k)

But since x is the number of elements with s_i=1, and s_i can be 0 or 1, this is a bit of a circular problem.

But perhaps, for the elements where current_c_i < n*2^k, they cannot have s_i=1. Because for s_i=1, current_c_i must be >=n*2^k.

So, these elements must have s_i=0. Hence, for these elements, their current_c_i must be >=x*2^k.

Similarly, elements where current_b_i <x*2^k cannot have s_i=1, because if s_i=1, x*2^k must be <= current_b_i.

But x is the count of s_i=1 elements, so this is a bit of a problem.

Alternatively, let's proceed step by step.

For a given bit k, let's first determine which elements can possibly be s_i=1.

An element i can have s_i=1 only if:

current_b_i >= x * 2^k

current_c_i >= n * 2^k

But x is the number of such elements. So, this is a chicken and egg problem.

But perhaps, the elements that can be s_i=1 are those i where current_c_i >=n*2^k.

Because if current_c_i <n*2^k, then s_i cannot be 1.

So, let's first compute the set S of elements i where current_c_i >=n*2^k. These are the candidates for s_i=1.

The number of elements in S is m.

For x to be valid, x must be <= m (since we can choose x elements from S), and also, x must satisfy that for each element in S, current_b_i >=x*2^k.

Additionally, for the elements not in S (i not in S), current_c_i >=x*2^k.

So, the steps are:

1. Compute m = number of elements i where current_c_i >=n*2^k.

2. For x to be valid, x must be <= m.

3. For all elements i in S, current_b_i must >=x*2^k.

4. For all elements not in S, current_c_i must >=x*2^k.

Moreover, x can be any value between 0 and m that satisfies these conditions.

But how to find x.

Let's see:

Condition 3: For all elements in S, current_b_i >=x*2^k --> x <= min (current_b_i / (2^k)) for i in S.

Condition 4: For all elements not in S, current_c_i >=x*2^k --> x <= (current_c_i) / (2^k) for all i not in S.

So x must be <= the minimum of:

- m,

- min (current_b_i / (2^k) for i in S),

- min (current_c_i / (2^k) for i not in S).

But x must also be >=0.

So the maximum possible x for this bit k is the minimum of these values.

If this maximum possible x is >=0, then we can choose x as this maximum possible value. Otherwise, no solution.

But why choose the maximum x possible?

Because selecting the largest possible x maximizes the contributions from this bit, which might allow lower bits to be processed more easily. However, there's no guarantee that this choice will lead to a valid solution for all bits. So this approach could be greedy and might not work.

Alternatively, we need to find any x that satisfies the conditions. For example, x could be 0, but this may not allow the remaining bits to be processed.

But how to find x.

Let’s formalize:

possible_x_max = min( m, min(current_b_i / (2^k) for i in S), min(current_c_i / (2^k) for i not in S) )

But all of these must be considered. For example, if any of the current_b_i in S is less than x*2^k, then x is invalid. So possible_x_max is the maximum x that is <= all these constraints.

But how to compute possible_x_max.

Let's proceed step by step:

For the current bit k:

1. Compute 2^k as bit_mask.

2. Compute required_c = n * bit_mask.

   S is the set of elements i where current_c_i >= required_c.

   m = len(S)

3. For elements in S, compute min_b = min( current_b_i // bit_mask for i in S )

   If S is empty, min_b is infinity (but x has to be 0).

4. For elements not in S, compute min_c_not_S = min( (current_c_i) // bit_mask for i not in S )

   If all elements are in S, then this is infinity.

5. possible_x_max = min(m, min_b, min_c_not_S )

6. If possible_x_max >=0 and possible_x_max <=m, then x can be possible_x_max.

   Otherwise, no solution.

But wait, possible_x_max may be negative. For example, if m is zero, then x has to be zero, but if possible_x_max is min(m=0, ... ), which is zero.

But if possible_x_max is negative, then no solution for this bit.

Once x is determined as possible_x_max, then:

The x elements in S with the largest current_b_i are selected as the ones to set s_i=1.

Wait, why? Because for the elements in S, we need current_b_i >=x*bit_mask. So when x is determined as possible_x_max, which is the minimum between m, min_b, and min_c_not_S, then x is the maximum possible value for x.

But then, when x is possible_x_max, then for all elements in S, current_b_i >=x*bit_mask, since x <= min_b (because min_b is the minimum of current_b_i//bit_mask for S). So x*bit_mask <= current_b_i for all i in S.

Similarly, x <= min_c_not_S implies x*bit_mask <= current_c_i for i not in S.

But then, after selecting x, how to choose which x elements in S to set s_i=1.

We need to choose any x elements from S, but perhaps the ones with the highest current_b_i. But why?

Because for lower bits, the remaining current_b_i and current_c_i need to be sufficient. But how to choose which elements to set. Since the choice may affect lower bits, this could be a problem. But given that we are processing bits from highest to lowest, perhaps this greedy approach is valid.

But I'm not sure. However, given time constraints, this approach might be the only feasible one.

So the algorithm for each bit k is:

1. Compute bit_mask = 2^k.

2. Compute required_c_for_1 = n * bit_mask.

   S is the set of i where current_c_i >= required_c_for_1.

   m = len(S)

3. For elements in S, compute the minimal current_b_i // bit_mask. If S is empty, min_b = 0.

   So min_b = min( (current_b_i // bit_mask) for i in S ) if S is not empty else 0.

4. For elements not in S, compute the minimal current_c_i // bit_mask. If there are no elements not in S, min_c_not_S = infinity.

   min_c_not_S = min( (current_c_i // bit_mask) for i not in S ) if any else infinity.

5. possible_x = min(m, min_b, min_c_not_S )

   If possible_x <0, then impossible.

6. If possible_x is valid, then x = possible_x.

   Now, select x elements from S to be s_i=1.

   Which elements? We can choose any x elements from S. But perhaps we need to choose those with the highest current_b_i, or any. For the current bit, it doesn't matter, as long as they are in S and x is correct.

   But for lower bits, the remaining current_b_i and current_c_i after subtracting the contributions are important. So perhaps the choice of which elements to set can affect the lower bits. But how?

   For example, if two elements in S have current_b_i of 100 and 200, but after setting s_i=1 for the one with 100, the remaining current_b_i becomes 100 - x * 2^k. If x is 50, then the remaining is 100 - 50*2^k. But how this affects lower bits depends on the value of 2^k and x.

   However, the problem is that if we choose the elements with the smallest current_b_i first, then subtracting the contribution may leave more remaining for lower bits. But this is not guaranteed.

   So, perhaps for the current bit, any selection of x elements from S is acceptable, but we need to choose them in a way that allows lower bits to have enough contributions.

   Since this is not trivial, perhaps the best approach is to select the first x elements in S (sorted or not) as long as their current_b_i is >= x * bit_mask.

   But since x is determined as the possible_x_max, all elements in S satisfy current_b_i >= x * bit_mask. So any subset of x elements from S will work.

   Therefore, we can choose any x elements from S. For simplicity, perhaps select the first x elements in S.

But how to manage this.

Once x is determined, the contribution for each i is:

For s_i=1:

   contribution_b = x * bit_mask

   contribution_c = n * bit_mask

For s_i=0:

   contribution_b = 0

   contribution_c = x * bit_mask

So, for the elements selected as s_i=1, subtract x * bit_mask from their current_b_i, and n * bit_mask from their current_c_i.

For the other elements (s_i=0), subtract 0 from current_b_i and x * bit_mask from current_c_i.

Thus, for each i:

if s_i=1:

   current_b_i -= x * bit_mask

   current_c_i -= n * bit_mask

else:

   current_c_i -= x * bit_mask

But wait, no: contribution_c is (s_i * n + (1-s_i)*x ) * bit_mask. So for s_i=1, it's n * bit_mask. For s_i=0, it's x * bit_mask. So yes.

So, for each i:

if s_i=1:

   current_c_i -= n * bit_mask

else:

   current_c_i -= x * bit_mask

So, after processing the bit, the current_b and current_c arrays are updated.

Now, the steps for the algorithm:

Initialize current_b and current_c as the input arrays.

For each bit k from 30 down to 0:

   bit_mask = 1 << k

   required_c_for_1 = n * bit_mask

   S = list of indices i where current_c[i] >= required_c_for_1

   m = len(S)

   if S:

      min_b = min( current_b[i] // bit_mask for i in S )

   else:

      min_b = 0

   # compute min_c_not_S

   not_S = [i for i not in S]

   if not_S:

      min_c_not_S = min( current_c[i] // bit_mask for i in not_S )

   else:

      min_c_not_S = float('inf')

   possible_x = min( m, min_b, min_c_not_S )

   if possible_x < 0 or (possible_x > m) or (possible_x > min_b) or (possible_x > min_c_not_S):

      # invalid, no solution

      return -1

   x = possible_x

   # select x elements from S to set s_i=1

   # but how to select them. For the current purpose, any x elements in S would work.

   # but need to track which elements are selected for setting the bits.

   # for the current bit k, store the bits in a array.

   # but how to manage that.

   # create a list of bits for each a_i. Initially 0, then set to 1 if selected.

   # for each bit, after selecting x elements, their a_i's bit is set.

   # So, for this bit k:

   # select x elements from S (sorted in some order). For example, take the first x elements.

   # for those elements, set their a_i's bit k to 1.

   # So, for each element in the first x elements of S:

   # a_i |= (1 <<k)

   # Then, subtract the contributions from current_b and current_c.

   # So the steps are:

   # select x elements from S. Let's select the first x elements.

   selected = S[:x]

   # but S is a list of indices where current_c[i] >= required_c_for_1. How to order them?

   # since we are processing in a way that doesn't depend on the order, perhaps any order is fine.

   # for each selected i:

   for i in selected:

       a[i] += bit_mask  # set the k-th bit.

   # now, subtract the contributions from current_b and current_c.

   for i in selected:

       current_b[i] -= x * bit_mask

       current_c[i] -= n * bit_mask

   # for elements not in selected (whether in S or not):

   for i in range(n):

       if i not in selected:

           current_c[i] -= x * bit_mask

           # but need to ensure that this subtraction does not make current_c[i] negative.

           # but since possible_x is chosen as the minimum of min_c_not_S and x is <= min_c_not_S, then x*bit_mask <= current_c[i] for i not in S.

           # and for i in S not selected: current_c[i] >= required_c_for_1 =n*bit_mask. x is <= m (number of elements in S). So x*bit_mask <= m * bit_mask. But current_c[i] is >=n * bit_mask. But n is >=m (since S is a subset of all elements). So if i is in S, but not selected, then x <= m, and current_c[i] >=n*bit_mask. So x*bit_mask <= m*bit_mask <=n*bit_mask <= current_c[i]. So the subtraction is safe.

   # after subtraction, check if any current_b or current_c is negative.

   # but possible_x is chosen such that x*bit_mask <= current_b[i] for selected i, and x*bit_mask <= current_c[i] for non-selected i.

   # so the subtraction should not make current_b[i] or current_c[i] negative.

But wait, for i in S but not selected (since x is less than m), their current_c[i] is >= required_c_for_1 =n*bit_mask, and x*bit_mask is <= m*bit_mask. But since m <=n (because S is a subset of all elements), x*bit_mask is <=n*bit_mask. So current_c[i] -x*bit_mask >=n*bit_mask -x*bit_mask >=n*bit_mask -n*bit_mask=0.

So for i not in selected but in S: current_c[i] >=0.

For i not in S: current_c[i] >= x*bit_mask (since x is <= min_c_not_S), so current_c[i] -x*bit_mask >=0.

Thus, the current_c[i] is non-negative.

For selected elements, current_b[i] was >=x*bit_mask, so current_b[i] -x*bit_mask >=0.

Thus, all current_b and current_c are non-negative after processing.

Once all bits are processed, we need to check that current_b and current_c are zero for all elements. Otherwise, it's invalid.

But why?

Because after processing all bits, the remaining current_b and current_c should be zero.

So after processing all bits, if any current_b[i] or current_c[i] is not zero, then the solution is invalid.

So the algorithm steps are:

1. Initialize current_b and current_c as input arrays.

2. For each bit k from 30 downto 0:

   a. Compute required_c_for_1 = n * (1 <<k)

   b. Find elements i where current_c[i] >= required_c_for_1 (this is set S)

   c. Compute possible_x as the minimum of len(S), min(current_b[i]//(1<<k) for i in S), min(current_c[i]//(1<<k) for i not in S if any)

   d. If possible_x is invalid (e.g., negative), return -1.

   e. Select x = possible_x elements from S. Any x elements.

   f. For each selected element, subtract x*(1<<k) from current_b[i], and n*(1<<k) from current_c[i].

   g. For each unselected element, subtract x*(1<<k) from current_c[i].

   h. Set the k-th bit of a[selected elements] to 1.

3. After processing all bits, check if all current_b[i] and current_c[i] are zero. If not, return -1.

4. Otherwise, output the a array.

Now, let's test this approach with the example.

Example 1:

Input:

4

6 8 4 4

16 22 10 10

Output: 3 5 1 1

Let's see.

current_b starts as [6,8,4,4]

current_c as [16,22,10,10]

Processing bits from 30 down to 0. Let's find the highest bit where some contribution is made. Let's see.

The maximum possible bit is 3 (since 8 is 2^3).

Let's process bit 3 (k=3):

bit_mask = 8.

required_c_for_1 = 4*8 =32.

Looking for elements i where current_c[i] >=32. The current_c array is [16,22,10,10], which all are less than 32. So S is empty.

So m=0.

possible_x is min(0, 0 (since S is empty), min(current_c[i]//8 for all elements not in S, which is all elements).

current_c[i] for all elements are 16,22,10,10.

current_c[i]//8: 16//8=2, 22//8=2, 10//8=1, 10//8=1. So min is 1.

possible_x = min(0, 0, 1) =0.

So x=0.

No elements are selected. So all elements remain with s_i=0 for this bit.

Subtract x * bit_mask =0 *8=0 from current_c for all elements.

current_c remains the same.

current_b remains the same.

Proceed to next bit.

k=2: bit_mask=4.

required_c_for_1=4*4=16.

current_c is [16,22,10,10]. So elements where current_c[i]>=16 are i=0 (16) and i=1 (22). So S = [0,1]. m=2.

For elements in S (0 and 1), current_b[i] are 6 and 8. current_b[i]//4 is 6//4=1, 8//4=2. min_b is 1.

For elements not in S (2 and3), current_c[i]//4 is 10//4=2 and 10//4=2. min_c_not_S=2.

possible_x = min(2, 1, 2) → 1.

So x=1.

We need to select 1 element from S (0 and 1).

Let's choose element 0.

Set a[0]'s bit 2: 1 <<2 =4, so a[0] becomes4.

For selected element 0:

current_b[0] -= 1*4 →6-4=2.

current_c[0] -=4*4=16 →16-16=0.

For unselected elements (1,2,3):

current_c[i] -=1*4:

current_c[1] =22-4=18.

current_c[2]=10-4=6.

current_c[3]=10-4=6.

Now current_b is [2,8,4,4], current_c is [0,18,6,6].

Next bit k=1 (bit_mask=2).

required_c_for_1 =4*2=8.

current_c is [0,18,6,6]. Elements where current_c[i] >=8 are i=1 (18 >=8) and 2,3 (6 <8).

So S = [1]. m=1.

For elements in S (1), current_b[i] =8. current_b[i]//2=4.

For elements not in S (0,2,3):

current_c[i]//2: 0//2=0, 6//2=3, 6//2=3. min_c_not_S=0.

possible_x = min(1,4,0) →0.

So x=0.

No elements selected. Subtract 0*2=0 from all current_c[i] not selected. No change.

current_b and current_c remain as before.

Next bit k=0 (bit_mask=1).

required_c_for_1=4*1=4.

current_c[i] are [0,18,6,6]. Elements with current_c[i] >=4 are i=1 (18), 2 (6),3 (6). So S = [1,2,3]. m=3.

For elements in S:

current_b[i] are 8,4,4. current_b[i]//1=8,4,4. min_b=4.

For elements not in S (0), current_c[i]//1=0. So min_c_not_S=0.

possible_x = min(3,4,0) →0.

x=0.

No elements selected.

Now, after processing all bits, check current_b and current_c.

current_b is [2,8,4,4]. Not zero. So the solution is invalid. But according to the example, the output is valid. So there's a mistake in the approach.

Wait, this indicates a problem. Because according to the algorithm, the solution is invalid, but the example has a valid solution.

So the algorithm is not working correctly. What's wrong here?

Let me re-examine the example.

The example input is:

n=4

b = [6,8,4,4]

c= [16,22,10,10]

The output is a = [3,5,1,1].

Let's compute the contributions for each bit.

a = [3 (0b11),5(0b101),1(0b01),1(0b01)]

For each element a_i, let's compute the sum of ANDs and ORs.

Sum of ANDs for each a_i:

a_1=3 (0b11):

sum (3&3 +3&5 +3&1 +3&1) =3 +1 +1 +1 =6 → matches b_1=6.

a_2=5 (0b101):

sum (5&3 +5&5 +5&1 +5&1) =1 +5 +1 +1=8 → matches b_2=8.

a_3=1:

sum (1&3 +1&5 +1&1 +1&1) =1 +1 +1 +1=4 → matches b_3=4.

Similarly for a_4=1.

OR sums:

a_1=3:

sum (3|3 +3|5 +3|1 +3|1) =3 |3=3, 3|5=7, 3|1=3, 3|1=3. Sum 3+7+3+3=16 → matches c_1=16.

a_2=5:

5|3=7, 5|5=5,5|1=5,5|1=5. Sum 7+5+5+5=22 → matches c_2=22.

a_3=1:

sum (1|3=3,1|5=5,1|1=1,1|1=1. Sum 3+5+1+1=10 → matches c_3=10.

So the solution is valid.

But according to the algorithm, after processing all bits, current_b and current_c should be zero. But during processing, let's see where the algorithm went wrong.

Let's re-run the algorithm step by step.

Original current_b = [6,8,4,4], current_c = [16,22,10,10].

Processing bit 3 (mask 8):

required_c_for_1=4*8=32.

current_c values are [16,22,10,10] → all <32. S is empty. possible_x=0.

No changes.

current_b remains [6,8,4,4], current_c remains [16,22,10,10].

Next bit 2 (mask 4):

required_c_for_1=4*4=16.

current_c[i] >=16 → i=0 (16), i=1 (22). S = [0,1]. m=2.

For S elements, current_b[i]//4 →6//4=1, 8//4=2 → min_b=1.

For non-S elements (2,3), current_c[i]//4 →10//4=2, 10//4=2 → min_c_not_S=2.

possible_x=min(2,1,2) →1.

x=1. Select 1 element from S. Let's say we select element 0.

Set a[0] to 4 (bit 2 is set).

Subtract x*4=4 from current_b[0] →6-4=2.

Subtract n*4=16 from current_c[0] →16-16=0.

Subtract x*4=4 from current_c of elements not selected (1,2,3).

current_c[1] becomes 22-4=18.

current_c[2] →10-4=6.

current_c[3] →10-4=6.

Now current_b is [2,8,4,4], current_c is [0,18,6,6].

Bit 1 (mask 2):

required_c_for_1=4*2=8.

current_c[i] >=8: i=1 (18), i=2 (6 <8?), i=3 (6 <8). So S is [1]. m=1.

For S element 1, current_b[i] is 8 → 8//2=4. min_b=4.

Non-S elements (0,2,3). current_c[i]//2:

0//2=0, 6//2=3, 6//2=3. min_c_not_S=0.

possible_x=min(1,4,0) →0.

x=0. No elements selected.

current_b remains [2,8,4,4], current_c remains [0,18,6,6].

Bit 0 (mask 1):

required_c_for_1=4*1=4.

current_c[i] >=4: i=1 (18), i=2 (6), i=3 (6). So S=[1,2,3]. m=3.

For elements in S:

current_b[i] are 8,4,4. current_b[i]//1=8,4,4. min_b=4.

Non-S elements: i=0. current_c[i] =0//1=0. min_c_not_S=0.

possible_x=min(3,4,0) →0.

x=0.

No elements selected.

After processing all bits, current_b is [2,8,4,4], current_c is [0,18,6,6]. These are not zero. So the algorithm outputs -1, but the correct solution exists. So the algorithm is incorrect.

So what's wrong here?

The problem is that the algorithm doesn't choose the correct x for some bit.

Looking back, during processing bit 2, x is chosen as 1. But according to the correct solution, the a array has two elements (a_0=3 and a_1=5) which have bit 2 set. So during bit 2 processing, x should be 2, not 1.

But according to the algorithm, possible_x was computed as 1. Why?

Let me re-calculate the steps for bit 2 (mask 4).

current_c is [16,22,10,10]. required_c_for_1=16.

S is [0,1], because current_c[0]=16 >=16, current_c[1]=22 >=16.

For these elements in S, current_b[i] is 6 and 8.

current_b[i]//4 is 6//4=1, 8//4=2. min_b=1.

For non-S elements (2,3), current_c[i] is 10 and 10. current_c[i]//4=2.

So possible_x is min(2,1,2) →1.

But why can't x be 2?

Because:

If x=2, then:

elements in S must have current_b[i] >=2*4=8.

current_b[0] is 6 <8 → violates the condition.

So x=2 is invalid.

But in the correct solution, a_0 and a_1 have bit 2 set. So during processing bit 2, x should be 2. But according to the algorithm's calculation, possible_x is 1.

This suggests that the algorithm is incorrect.

But why does the correct solution have x=2 for bit 2, but according to the algorithm, it's not possible.

Wait, because in the correct solution, the contribution to b_i for bit 2 is:

For a_0=3 (bit 2 is set) and a_1=5 (bit 2 is set), x=2.

Contribution to b_0 is 2 * 4 =8. But the original b_0 is 6. How does this fit?

Wait, this seems conflicting. But in the correct solution, the sum for a_0's b_i is 6, which includes contributions from multiple bits.

Ah, I see. The algorithm's approach of processing bits from high to low is incorrect, as the lower bits can contribute to the higher bits' sum.

Wait, no. Because each bit's contribution is considered in isolation. The problem arises because the algorithm's way of choosing x for each bit is incorrect. For example, in the correct solution, the contribution for bit 2 is x=2 (two elements have the bit set). But according to the algorithm's step, x=2 is invalid because for element 0 in S, current_b[i] (6) is less than x*4=8. So why does the correct solution allow this?

Ah, because the sum of contributions from all bits must equal the original b_i. But the algorithm assumes that for each bit, the contribution is subtracted from current_b_i and current_c_i, which is the sum of contributions from higher bits. But perhaps the algorithm is processing the bits in the wrong order.

Wait, no. The algorithm processes bits from highest to lowest. So when processing bit 2, the current_b_i and current_c_i have already had higher bits' contributions subtracted. But in the example, the higher bits (bit 3) were not processed, so current_b and current_c are original.

So in the example, when processing bit 2 (mask 4), the current_b is [6,8,4,4]. For x=2, the contribution for bit 2 would be 2*4=8 for elements in S (0 and 1).

But for element 0, current_b[i] =6 is less than 8. So the algorithm is correct in choosing x=1 for this step, but the correct solution requires x=2. So there's a contradiction.

But according to the correct solution, a_0 has bit 2 set. So during processing bit 2, the contribution for a_0 is 2*4=8. But the current_b[i] for a_0 is 6. How can this be allowed?

This suggests that the algorithm's approach is incorrect. Because the correct solution's contribution for a higher bit may rely on contributions from lower bits. So the algorithm's method of processing bits from highest to lowest is invalid.

Ah, this is the crux of the problem. The algorithm assumes that each bit can be processed independently, but the contributions from lower bits can affect the higher bits' processing. However, this is not the case. Because each bit's contribution is to the sum of (a_i AND a_j) and (a_i OR a_j) for all j. These are computed based on the actual a_i and a_j values, not the remaining current_b and current_c.

So the algorithm's approach of processing bits from highest to lowest and subtracting their contributions from current_b and current_c is flawed. Because the actual contributions for higher bits depend on the lower bits. For example, the higher bits may have contributions that are influenced by the lower bits' settings.

Thus, the algorithm's approach of processing bits in order and subtracting contributions is incorrect. This is why the example fails.

So what's the correct approach?

We need a way to determine the bits of a_i based on the given b and c arrays. The earlier idea of considering each bit's contribution based on the number of elements with that bit set seems correct, but the way of processing bits in order and subtracting their contributions is not working.

Alternative approach:

For each bit k, the number of elements with the bit set is x_k. For each element i, the contribution to b_i from this bit is s_ik * x_k * 2^k. The contribution to c_i is (s_ik * n + (1 - s_ik) * x_k) * 2^k.

The sum of these for all bits must equal the given b and c.

The variables are x_k and s_ik for each bit k and element i.

The problem is to find s_ik and x_k for each k such that:

For each k:

x_k = sum(s_ik for all i)

For each i:

sum over k of s_ik * x_k * 2^k = b_i

sum over k of (s_ik * n + (1 - s_ik)*x_k) * 2^k = c_i

This is a system of equations, but it's challenging to solve directly.

Another observation is that for each bit k, the value (c_i - b_i) must be equal to x_k * 2^k for all i. Because:

c_i - b_i = sum_{j} (a_i OR a_j) - (a_i AND a_j) = sum_{j} a_i XOR a_j.

But a_i XOR a_j is equal to (a_i OR a_j) - (a_i AND a_j).

But sum_{j} a_i XOR a_j can be rewritten as sum_{j} (a_i - (a_i AND a_j) + a_j - (a_i AND a_j)) = sum_{j} (a_i + a_j - 2*(a_i AND a_j)) ) = n a_i + sum a_j - 2*b_i.

But this is for sum(a_i XOR a_j) over j.

Alternatively, sum (a_i XOR a_j) = sum (a_i OR a_j - a_i AND a_j) = c_i - b_i.

But sum (a_i XOR a_j) can also be computed as sum (a_i XOR a_j) for j=1 to n.

For each bit k, the sum over j of (a_i XOR a_j) is equal to (number of j where a_i and a_j differ in bit k) multiplied by 2^k.

Thus, for each i and k:

The sum over j of (a_i XOR a_j) for bit k is equal to (x_k (1 - s_ik) + (n - x_k) s_ik) * 2^k.

So, sum (a_i XOR a_j) for j is sum over k of [ (x_k (1 - s_ik) + (n - x_k) s_ik) ] * 2^k.

But sum (a_i XOR a_j) for j is c_i - b_i.

Thus, for each i:

c_i - b_i = sum_{k} [ x_k (1 - s_ik) + (n - x_k) s_ik ] * 2^k.

But this must hold for all i.

But x_k is the number of elements with bit k set, i.e., x_k = sum_j s_jk.

So for each bit k, the term inside the sum is:

For each i:

If s_ik = 1: (x_k (0) + (n -x_k) * 1 ) = (n -x_k) → number of elements where bit k is not set (n -x_k).

If s_ik = 0: (x_k * 1 + (n -x_k) *0) =x_k.

Thus, for each i, the contribution from bit k to (c_i -b_i) is:

s_ik ? (n -x_k) * 2^k : x_k * 2^k.

But (c_i -b_i) is known. So for each bit k, the sum of these contributions across all bits must equal (c_i -b_i).

But how to use this.

The key observation is that for each bit k, the contribution to (c_i -b_i) is either x_k*2^k or (n-x_k)*2^k, depending on whether s_ik is 0 or 1.

Furthermore, the sum of these contributions for all bits must equal (c_i -b_i).

But how to find x_k and s_ik.

But since x_k is the number of s_ik=1, and for each bit k, the contribution depends on x_k and s_ik.

This seems difficult, but perhaps for each bit k, the contribution to (c_i -b_i) must be a multiple of 2^k, and the sum of these multiples must equal (c_i -b_i).

Let’s denote d_i = c_i - b_i. For each i, d_i must be equal to the sum over k of t_ik * 2^k, where t_ik is either x_k or (n -x_k), depending on s_ik.

So for each bit k, the contribution to d_i is t_ik * 2^k, and t_ik is either x_k or (n -x_k).

Thus, for each bit k, we can model t_ik as x_k or (n -x_k) for each i.

But how.

Another observation: for a particular bit k, if x_k is the number of elements with the bit set, then:

For each i:

if s_ik is 1: t_ik = (n -x_k)

if s_ik is 0: t_ik = x_k

So t_ik = x_k (1 - s_ik) + (n -x_k) s_ik.

But x_k is the number of s_ik=1 elements, so x_k = sum_j s_jk.

But this seems complicated.

Alternatively, for each bit k, the possible values of t_ik can be either x_k or (n -x_k).

But for each i, t_ik must be one of these two options.

Moreover, the sum over all bits of t_ik * 2^k must equal d_i.

But since x_k is the same for all i in the same bit, but t_ik can vary per i.

This seems challenging, but perhaps for each bit k, we can determine x_k and whether each i's t_ik is x_k or (n-x_k), such that the sum of t_ik *2^k for all bits equals d_i.

But how.

Let's consider that for each bit k, the contribution to d_i is t_ik * 2^k, and this can be written as 2^k multiplied by either x_k or (n-x_k).

Thus, for each bit k, the possible contribution to d_i is either x_k * 2^k or (n-x_k) * 2^k.

So for each i, the sum of these for all bits must equal d_i.

Thus, the problem reduces to choosing for each bit k a value x_k (number of set bits), and for each i a choice between x_k and (n-x_k) as the multiplier for 2^k, such that the sum equals d_i.

This is a different way to model the problem. Now, for each bit k, we need to find x_k such that:

sum_{k} (x_k * 2^k) * s_ik' + (n-x_k)*2^k * (1-s_ik') ) = d_i for all i.

Where s_ik' is 1 if t_ik = x_k, and 0 if t_ik = (n-x_k).

But this is the same as:

sum_{k} [ (n-x_k) * 2^k + s_ik' ( x_k - (n-x_k) ) * 2^k ] = d_i.

Which simplifies to:

sum_{k} [ (n-x_k) * 2^k + s_ik' ( 2x_k -n ) * 2^k ] = d_i.

But this is getting complicated.

Alternatively, for each bit k, the possible contribution is either x_k *2^k or (n-x_k)*2^k. So the difference between these two options is (x_k - (n -x_k)) *2^k = (2x_k -n) *2^k.

Thus, for each bit, the choice for each i is to add either (n-x_k)*2^k or x_k*2^k to the sum.

But how to find x_k and the choices for each i.

But perhaps, for each bit k, we can compute x_k and then for each i, choose whether to take x_k or (n-x_k) as the multiplier, based on the bit's presence in d_i.

But how.

This line of reasoning is getting stuck, so perhaps I should look for a different approach.

Alternative Idea:

We can compute for each bit k, x_k = the number of elements with that bit set. Then, for each i, the contribution to d_i (c_i -b_i) from this bit is:

If a_i has the bit set: (n -x_k) * 2^k.

If a_i does not have the bit set: x_k * 2^k.

Thus, the sum of these contributions for all bits must equal d_i.

But how to find x_k and the bits for a_i.

But since the contributions for each bit are additive and each bit is processed independently, perhaps we can determine x_k for each bit k based on the d_i.

For example, for a particular bit k, the sum of the contributions for this bit across all i must equal the sum of (n -x_k) * 2^k for the elements where a_i has the bit set, plus x_k * 2^k for the elements where a_i does not have the bit set.

Sum over i: contribution for bit k = x_k * (n -x_k) * 2^k + (n -x_k) * x_k * 2^k ?

Wait, no.

Wait, for each i, if a_i has the bit set, the contribution is (n -x_k) * 2^k. There are x_k such elements. So their total contribution is x_k * (n -x_k) * 2^k.

For the remaining (n -x_k) elements, the contribution is x_k * 2^k. So their total contribution is (n -x_k) * x_k * 2^k.

So the total contribution for bit k is x_k (n -x_k) * 2^k * 2 = 2 x_k (n -x_k) * 2^k.

But this sum over i is equal to sum_{i} d_i's contribution from bit k.

But sum_{i} d_i is equal to sum_{i} (c_i - b_i).

Let's denote D = sum_{i} (c_i - b_i).

Thus, sum_{k} 2 x_k (n -x_k) * 2^k = D.

This is a necessary condition for the existence of a solution.

But how to use this.

But even if this condition is met, individual elements must also satisfy their own d_i.

But this is a necessary condition. For example, in the first example:

sum d_i = (16-6)+(22-8)+(10-4)+(10-4) = (10 +14 +6 +6) = 36.

sum_{k} 2 x_k (n -x_k) * 2^k must equal 36.

In the correct solution:

x_0 (bit 0):

a = 3 (bit 0 and 1),5 (bit 0 and 2),1 (bit 0),1 (bit 0).

x_0 for bit 0 is 4 (all have bit 0 set).

x_0 =4. 2*4*(4-4)*2^0 =0.

bit 1:

a_0 has bit 1 set (3 in binary 11), a_1 has bit 1 not set (5 is 101, bit 1 is 0?), wait 5 is 101 in binary. So bits are 0, 2.

Wait, in the correct solution, the a array is [3,5,1,1].

Let's break down each bit:

bit 0:

3 (binary 11) has bit 0 set.

5 (binary 101) has bit 0 not set.

Wait, no. 5 in binary is 101. So bit 0 is 1, bit 1 is 0, bit 2 is 1.

So for a_0=3 (0b11), bits 0 and 1 are set.

a_1=5 (0b101), bits 0 and 2 are set.

a_2 and a_3 have bit 0 set.

So for bit 0: x_k is 3 (a_0, a_2, a_3 have it set. a_1 does not).

So x_0=3.

contribution for bit 0: 2 *3*(4-3)*1 =6.

bit 1:

a_0 has bit 1 set. a_1 does not. a_2 and a_3 do not. x_1=1.

contribution: 2 *1*(4-1)*2= 2*1*3*2=12.

bit 2:

a_1 and a_0 have bit 2 set? a_0=3 (binary 11) has bits 0 and 1. bit 2 is not set. a_1=5 (101) has bit 2 set. a_2 and a_3 do not. So x_2=1.

contribution: 2*1*(4-1)*4= 2*1*3*4=24.

bit 3: no elements have it set. contribution is zero.

sum is 6+12+24=42. Which is not equal to D=36. So this suggests that the initial approach is incorrect.

But according to the example, the sum of d_i is 36. So the earlier reasoning is wrong.

This indicates that the previous approach is not working.

At this point, I realize that this problem is more complex than I initially thought, and that my current approach isn't working. Perhaps I should look for a different way to model the problem.

Another Idea:

We have:

For each i:

b_i = sum_j (a_i & a_j)

c_i = sum_j (a_i | a_j)

But a_i & a_j = a_i + a_j - (a_i | a_j)

So sum_j (a_i & a_j) = a_i * n + sum a_j - sum_j (a_i | a_j)

But sum_j (a_i | a_j) = c_i.

So:

b_i = a_i * n + sum a_j - c_i.

Rearranging:

sum a_j = b_i + c_i - a_i * n.

But sum a_j is a constant (same for all i). So for all i and j:

b_i + c_i - a_i * n = b_j + c_j - a_j * n.

This implies that:

b_i + c_i - a_i * n = K for all i, where K is the sum of a_j.

But K = sum a_j.

Thus, K = b_i + c_i - a_i * n for all i.

But K is also sum a_j.

So, for all i:

sum a_j = b_i + c_i - a_i * n.

This can be rewritten as:

sum a_j + a_i * n = b_i + c_i.

Summing over all i:

sum (sum a_j + a_i *n ) = sum (b_i + c_i )

sum (sum a_j ) + n sum a_i = sum (b_i + c_i )

sum a_j * n + n sum a_i = sum (b_i + c_i )

But sum a_j = K, so:

n K + n K = sum (b_i + c_i )

2n K = sum (b_i + c_i )

Thus:

K = sum (b_i + c_i ) / (2n)

If sum (b_i + c_i ) is not divisible by 2n, then there's no solution.

So, this is a necessary condition.

Once K is known, for each i:

a_i = (b_i + c_i - K) /n

But K is sum a_j, and we have:

a_i = (b_i + c_i - K)/n.

But since K is sum a_j, this gives a system of equations.

Let's see:

For each i:

a_i = (b_i + c_i - K)/n.

Summing over all i:

K = sum (b_i + c_i - K)/n.

Multiply both sides by n:

n K = sum (b_i + c_i) - K * sum 1.

n K = sum (b_i + c_i) - K * n.

n K + K *n = sum (b_i + c_i)

2n K = sum (b_i + c_i ), which matches the earlier equation.

Thus, this is a valid equation.

So, the necessary condition is that sum (b_i + c_i) must be divisible by 2n. If not, output -1.

Assuming this condition is met, K is determined as sum (b_i + c_i ) / (2n).

Then, for each i, a_i = (b_i + c_i - K)/n.

This is a crucial insight!

So, the steps are:

1. Compute sum_b_c = sum (b_i + c_i for all i).

2. If sum_b_c is not divisible by 2n, output -1.

3. Else, K = sum_b_c / (2n).

4. For each i, compute a_i = (b_i + c_i - K) //n. If (b_i + c_i - K) is not divisible by n, output -1.

5. Check if the computed a_i's satisfy the original b and c arrays.

If all conditions are met, output the a_i's. Else, -1.

This is a much simpler approach. Let's test this with the first example.

Example 1:

n=4

b = [6,8,4,4]

c = [16,22,10,10]

sum_b_c = (6+16)+(8+22)+(4+10)+(4+10) = 22 +30 +14 +14 = 80.

sum_b_c / (2n) = 80/(8) =10 → K=10.

For each i:

a_i = (b_i +c_i -10)/4.

i=0: (6+16-10)/4 = (12)/4=3 → a_0=3.

i=1: (8+22-10)/4=20/4=5 →a_1=5.

i=2: (4+10-10)/4=4/4=1 →a_2=1.

i=3: (4+10-10)/4=4/4=1 →a_3=1.

Which matches the sample output.

Check if these a_i's satisfy the original conditions.

For a_0=3:

sum (3 & a_j for j=0-3) is 3&3 +3&5 +3&1 +3&1 =3 +1 +1 +1 =6 → matches b_0=6.

sum (3 | a_j) is3|3 +3|5 +3|1 +3|1 =3+7+3+3=16 → matches c_0=16.

Similarly for other elements.

This works.

Example 2:

Input:

5

8 25 14 7 16

19 6 9 4 25

sum_b_c = (8+19)+(25+6)+(14+9)+(7+4)+(16+25) = 27 +31 +23 +11 +41 = 133.

2n=10 → 133/10=13.3 → not integer. So output is -1. Which matches the sample.

Thus, this approach seems correct.

But why? Because we derived that the sum of a_i is K = sum (b_i + c_i)/(2n), and each a_i is (b_i +c_i -K)/n.

Once a_i's are computed, we can verify if they indeed produce the original b and c arrays.

Thus, the algorithm is:

1. Compute sum_b_c = sum(b_i) + sum(c_i).

2. If sum_b_c is not divisible by 2n → output -1.

3. K = sum_b_c // (2n).

4. For each i, compute a_i = (b_i + c_i - K) // n. If (b_i + c_i -K) is not divisible by n → output -1.

5. Check if the computed a_i's indeed produce the original b and c arrays. If yes, output them. Else, output -1.

But how to check step 5 efficiently.

Computing b and c arrays for the computed a_i's for n up to 2e5 may be time-consuming. But there's a way to check using the original equations.

But for large n, computing sum (a_i & a_j) and sum (a_i | a_j) for each i is O(n^2), which is not feasible.

But in practice, the problem requires us to output a valid a array if it exists. So steps 1-4 are necessary, but step 5 is required to check for validity.

But how to check step 5 efficiently.

An alternative approach is to compute the sum of a_i's (which is K), and also compute the sum of a_i^2.

Because:

sum_{i,j} (a_i & a_j) = sum_{i} b_i = sum_b.

sum_{i,j} (a_i | a_j) = sum_{i} c_i = sum_c.

But sum_{i,j} (a_i & a_j) is equal to sum_{i} sum_{j} (a_i & a_j) = sum_{i} b_i = sum_b.

Similarly, sum_{i,j} (a_i | a_j) = sum_c.

Now, sum_{i,j} (a_i & a_j) can be computed as sum_{k} x_k^2 * 2^k, where x_k is the number of elements with bit k set.

Similarly, sum_{i,j} (a_i | a_j) can be computed as sum_{k} x_k (2n -x_k) * 2^k.

But computing this for all bits and checking if sum_b and sum_c match is possible in O(30n) time.

Thus, the algorithm is:

1. Check sum_b_c is even and divisible by 2n.

2. Compute K and check each a_i is computed correctly.

3. Compute the sum of all a_i and verify it equals K.

4. Compute the sum of all a_i^2, and compute sum_{i,j} (a_i & a_j) = sum_{i} b_i. Compare with sum_b.

But sum_{i,j} (a_i & a_j) = sum_{i} b_i = sum_b.

Also, sum_{i,j} (a_i | a_j) = sum_c.

But sum_{i,j} (a_i & a_j) + sum_{i,j} (a_i | a_j) = sum (a_i & a_j + a_i | a_j) for all i,j.

But a_i & a_j + a_i | a_j = a_i + a_j.

So sum_{i,j} (a_i & a_j) + sum_{i,j} (a_i | a_j) = sum_{i,j} (a_i + a_j) = 2nK.

But sum_b + sum_c should be 2nK.

Which is already guaranteed by the way K is computed. So this is not a new check.

Thus, the only checks needed after computing a_i's are:

- Each a_i is non-negative.

- sum a_i == K.

- For each bit k, the sum of squares of x_k (number of elements with bit k set) multiplied by 2^k equals sum_b.

But for large n, this can be done by processing each bit.

So the steps are:

After steps 1-4, compute a array.

Check:

- All a_i are non-negative.

- sum a_i equals K.

- Compute sum_ands and sum_ors.

sum_ands = sum_{k} x_k^2 * 2^k.

sum_ors = sum_{k} x_k (2n -x_k) * 2^k.

If sum_ands == sum_b and sum_ors == sum_c → output a array.

Else, output -1.

This can be done in O(n) time by counting the number of bits set in each position.

Thus, the algorithm is:

1. Compute sum_b and sum_c.

2. Compute sum_b_c = sum_b + sum_c.

3. Check sum_b_c is divisible by 2n. If not, output -1.

4. Compute K = sum_b_c // (2n).

5. For each i, compute a_i = (b_i + c_i - K) /n. Check divisibility and non-negativity.

6. Compute sum_a = sum a_i. If sum_a != K → output -1.

7. For each bit k, compute x_k (number of elements with bit k set).

8. Compute sum_ands and sum_ors using x_k's.

9. If sum_ands == sum_b and sum_ors == sum_c → output a array. Else, -1.

But how to compute x_k's.

For each bit k, iterate through all a_i and count how many have the bit set. For n up to 2e5 and 31 bits, this is O(n*31) = 6e6 operations, which is acceptable.

Thus, this approach is feasible.

Let's test it on the first example.

sum_b = 6+8+4+4=22.

sum_c=16+22+10+10=58.

sum_b_c=80. 80/(2*4)=10=K.

a = [3,5,1,1]. sum_a=3+5+1+1=10=K.

sum_ands: For each bit:

bit 0: x_k=3 (3,5,1,1 → 3 has bit 0, 5 has bit 0, 1 has bit 0, 1 has bit 0. Wait wait:

Wait, a[0] =3 → binary 11 → bits 0 and 1 set.

a[1]=5 → binary 101 → bits 0 and 2 set.

a[2]=1 → bit 0.

a[3]=1 → bit 0.

So:

bit 0: x_k=4 (all a_i have bit 0 set? 3 has it, 5 has it (binary 101 has bit 0 set), 1 and 1 have it. Yes. So x_k=4. contribution to sum_ands is 4^2 *1=16.

bit 1: a_0 has it, a_1 does not, a_2 and 3 do not. x_k=1 → contribution 1^2 *2=2.

bit 2: a_1 has it. x_k=1 → contribution 1*1*4=4.

Higher bits: x_k=0.

sum_ands=16+2+4=22= sum_b.

sum_ors: for each bit:

bit 0: x_k=4 → contribution 4*(2*4 -4)*1 =4*(4)*1=16.

bit 1: x_k=1 →1*(8-1)*2=7*2=14.

bit 2: x_k=1 →1*(8-1)*4=7*4=28.

sum_ors=16+14+28=58=sum_c.

Thus, this approach works.

Thus, the correct approach is to compute a_i using the formula a_i = (b_i +c_i -K)/n, where K=sum(b_i +c_i)/(2n), and then verify that the computed a_i's indeed produce the correct sum_ands and sum_ors.

Thus, the steps are:

Implement this approach.

Now, let's code this.

First, read n, read b and c arrays.

Compute sum_b = sum(b).

sum_c = sum(c).

sum_b_c = sum_b + sum_c.

If sum_b_c is not divisible by 2n → output -1.

Else, K = sum_b_c // (2n).

Then, for each i:

a_i = (b[i] + c[i] - K) // n.

But must check that (b[i] + c[i] - K) is divisible by n, and a_i >=0.

Then, compute sum_a = sum of a_i. If sum_a != K → invalid.

Then, compute for each bit k, the number of elements with the bit set (x_k).

Compute sum_ands = sum x_k^2 * 2^k for all k.

sum_ors = sum x_k * (2n -x_k) * 2^k for all k.

If sum_ands == sum_b and sum_ors == sum_c → output a array. Else, -1.

Thus, this is the correct approach.

Now, code this.

The code will be:

Read n.

Read list b.

Read list c.

sum_b = sum(b)

sum_c = sum(c)

sum_bc = sum_b + sum_c

if sum_bc % (2*n) !=0:

    print(-1)

else:

    K = sum_bc // (2*n)

    a = []

    valid = True

    for i in range(n):

        numerator = b[i] + c[i] - K

        if numerator % n !=0:

            valid = False

        ai = numerator //n

        if ai <0:

            valid = False

        a.append(ai)

    if not valid:

        print(-1)

    else:

        sum_a = sum(a)

        if sum_a != K:

            print(-1)

        else:

            # compute x_k for each bit.

            bits = [0]*31

            for num in a:

                for k in range(31):

                    if num & (1 <<k):

                        bits[k] +=1

            # compute sum_ands and sum_ors

            sum_ands =0

            sum_ors =0

            for k in range(31):

                x = bits[k]

                sum_ands += x *x * (1 <<k)

                sum_ors += x * (2*n -x) * (1 <<k)

            if sum_ands == sum_b and sum_ors == sum_c:

                print(' '.join(map(str,a)))

            else:

                print(-1)

This code should handle all cases.

Now, let's test the first example:

sum_b=22, sum_c=58. sum_bc=80. 2n=8. 80/8=10=K.

Each a_i is computed correctly.

sum_a=10=K.

bits:

bit 0:4, bit 1:1, bit 2:1.

sum_ands = 4^2*1 +1^2*2 +1^2*4= 16 +2+4=22.

sum_ors=4*(8-4)*1 +1*(8-1)*2 +1*(8-1)*4= 4*4*1 +7*2 +7*4 →16+14+28=58.

Thus, output is correct.

Another test case:

Second example:

sum_b =8+25+14+7+16 = 70.

sum_c=19+6+9+4+25=63.

sum_bc=133. 2n=10. 133%10=3 → not divisible → output -1.

Thus, correct.

Thus, this approach should work.

Now, code this in Python.

But for large n (up to 2e5), the loop for bits may be optimized.

But in Python, even 2e5 * 31 is 6.2e6 operations, which is acceptable.

Thus, the code is:

Read n.

Read b and c.

Check sum_bc.

Compute K.

Compute a_i.

Check all a_i are non-negative, and sum_a = K.

Compute bits.

Compute sum_ands and sum_ors.

Check and output.

Thus, the code should be as follows.
</think>

```python
import sys

def main():
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))
    
    sum_b = sum(b)
    sum_c = sum(c)
    sum_bc = sum_b + sum_c
    
    if sum_bc % (2 * n) != 0:
        print(-1)
        return
    
    K = sum_bc // (2 * n)
    a = []
    valid = True
    
    for i in range(n):
        numerator = b[i] + c[i] - K
        if numerator % n != 0:
            valid = False
        ai = numerator // n
        if ai < 0:
            valid = False
        a.append(ai)
    
    if not valid:
        print(-1)
        return
    
    sum_a = sum(a)
    if sum_a != K:
        print(-1)
        return
    
    bits = [0] * 31
    for num in a:
        for k in range(31):
            if num & (1 << k):
                bits[k] += 1
    
    sum_ands = 0
    sum_ors = 0
    for k in range(31):
        x = bits[k]
        sum_ands += x * x * (1 << k)
        sum_ors += x * (2 * n - x) * (1 << k)
    
    if sum_ands == sum_b and sum_ors == sum_c:
        print(' '.join(map(str, a)))
    else:
        print(-1)

if __name__ == "__main__":
    main()
```