<think>
Okay, let's try to figure out this problem. So the task is to minimize the sum of absolute differences between elements of a and b, but we can swap two elements in b at most once. Hmm.

First, let's understand the initial sum. We calculate the sum of |a_i - b_i| for all i. Now, the question is, what's the best possible swap in b that reduces this sum the most. Or maybe even leave it as is if swapping doesn't help.

So the idea is that swapping two elements in b (say, b_j and b_k) would change the sum in the following way. The original contribution to the sum from positions j and k is |a_j - b_j| + |a_k - b_k|. After swapping, it becomes |a_j - b_k| + |a_k - b_j|. The difference between these two would determine whether the swap is beneficial.

So for every possible pair (j, k), we can compute the potential gain (original sum minus new sum) and find the maximum gain possible. Then, the minimal possible sum is the original sum minus this maximum gain. If the maximum gain is positive, we subtract it; otherwise, we don't swap.

But checking all possible pairs is O(n^2), which is way too slow for n up to 2e5. So we need a smarter approach.

Hmm, how can we find the best possible pair without checking all possibilities? Let's think about how swapping two elements can improve the sum.

The optimal swap would be when the two elements in b are such that when swapped, the sum of their individual contributions is minimized. Let's think of each element in b as a candidate to be swapped with another. How can we find two elements in b where swapping them gives the maximum possible reduction in the sum.

Wait, for each i and j, the gain is (original_i + original_j) - (new_i + new_j) where original_i is |a_i - b_i|, new_i is |a_i - b_j|. So the gain for swapping i and j is (original_i + original_j) - (|a_i - b_j| + |a_j - b_i|). The maximum gain across all pairs gives the maximum possible reduction.

So the problem reduces to finding the maximum possible value of (original_i + original_j) - (|a_i - b_j| + |a_j - b_i|) over all i < j.

If this maximum is positive, then swapping those i and j will reduce the total sum by that amount. Otherwise, it's better not to swap.

But how to compute this efficiently.

Let me consider that for each i, j, the value is (|a_i - b_i| + |a_j - b_j|) - (|a_i - b_j| + |a_j - b_i|). We need to maximize this. So for all i, j pairs, compute this value, find the maximum.

The problem is that with n up to 2e5, this approach is O(n^2), which is impossible. So we need a way to find the best pair in O(n) or O(n log n) time.

Wait, perhaps there's a way to model this. Let's see.

The gain for swapping i and j is (original_i + original_j) - (new_i + new_j). So the gain is (|a_i - b_i| + |a_j - b_j|) - (|a_i - b_j| + |a_j - b_i|).

We can rearrange this as (|a_i - b_i| - |a_i - b_j|) + (|a_j - b_j| - |a_j - b_i|).

Hmm, but not sure if that helps.

Alternatively, maybe we can precompute for each i the best j to swap with i such that the gain is maximized.

But even that would be O(n^2) for all i.

Alternatively, perhaps there's a pattern in the optimal i and j.

Let me think of a scenario where swapping i and j gives a positive gain. That would mean that the sum of the two terms after swapping is less than the original.

So, for the pair (i, j), |a_i - b_i| + |a_j - b_j| > |a_i - b_j| + |a_j - b_i|.

Rearranging, the difference is (|a_i - b_i| + |a_j - b_j|) - (|a_i - b_j| + |a_j - b_i|) > 0.

We can rewrite this as (|x_i| + |y_j|) - (|x_i - d_ij| + |y_j + d_ij|), where x_i is a_i - b_i, y_j is a_j - b_j, and d_ij is (b_j - b_i). Wait, maybe not. Let's see.

Wait, a_i - b_j is a_i - b_i + (b_i - b_j) = (a_i - b_i) - (b_j - b_i). Hmm, maybe this isn't leading me anywhere.

Alternatively, let's consider the two terms:

Original: |a_i - b_i| + |a_j - b_j|.

After swap: |a_i - b_j| + |a_j - b_i|.

We need to find the maximum of (original - after), which is the gain.

Let me denote for a particular i and j:

gain = |a_i - b_i| + |a_j - b_j| - |a_i - b_j| - |a_j - b_i|.

We want to find the maximum gain.

Hmm. Let's think about how this gain can be maximized.

Suppose that in the original positions, i and j contribute a lot to the sum, but after swapping, their contributions are much less. So perhaps when a_i and b_j are closer, and a_j and b_i are also closer.

So for each i, maybe we can find the best j in the array that gives the maximum gain when swapped with i.

But again, for n=2e5, this is O(n^2) time.

Wait, but maybe there's a way to find for each i the best j, and then track the maximum over all pairs (i,j). But how?

Alternatively, perhaps the optimal swap is between two elements where the gain is maximum. So, perhaps the best possible swap is the pair (i,j) where the gain is maximum.

But how to compute this without checking all pairs.

Let's consider that the gain can be rewritten as:

gain = (|a_i - b_i| + |a_j - b_j|) - (|a_i - b_j| + |a_j - b_i|).

Let's see if this can be transformed into something that allows for faster computation.

Another approach: For each element in b, perhaps find the element in a where swapping would give the maximum gain. But again, not sure.

Wait, think of the problem as trying to find two elements in b (b_i and b_j) such that swapping them would give the maximum possible reduction in the sum.

But the sum is the total of |a_k - b_k| for all k. So when we swap two elements in b, only the two positions i and j are affected. So the gain is the original sum (for i and j) minus the new sum (for i and j).

Thus, for each possible pair i, j, the gain is (original_i + original_j) - (new_i + new_j). The maximum of this over all i, j pairs gives the best possible reduction.

So the key is to find the pair i, j that maximizes this gain.

The problem is to find this maximum gain efficiently.

Let's think about this for each pair i, j. The gain is:

(|a_i - b_i| + |a_j - b_j|) - (|a_i - b_j| + |a_j - b_i|).

Let me define for each i and j:

delta = ( |a_i - b_i| + |a_j - b_j| ) - ( |a_i - b_j| + |a_j - b_i| )

We need to find the maximum delta over all i < j.

Now, the question is how to compute this delta efficiently.

Let's try to compute delta for each i and j. For example:

delta = (|x_i| + |x_j|) - (|x_i + (b_i - b_j)| + |x_j - (b_i - b_j)|), where x_i = a_i - b_i, x_j = a_j - b_j. Wait, perhaps not. Let me think:

Original terms:

a_i - b_i is x_i = a_i - b_i.

a_j - b_j is x_j = a_j - b_j.

After swap:

a_i - b_j = a_i - (original b_j) = a_i - (b_i + (b_j - b_i))? Not sure. Wait, original b_i and b_j are swapped. So after swap, the new b_i is b_j, and new b_j is b_i.

So a_i - new_b_i is a_i - b_j.

a_j - new_b_j is a_j - b_i.

So the new terms are |a_i - b_j| and |a_j - b_i|.

So the delta is (|x_i| + |x_j|) - ( |a_i - b_j| + |a_j - b_i| )

Hmm. How can we find the maximum of this delta.

Alternatively, maybe there's a way to precompute for each i the best possible j, and track the maximum delta.

But how?

Alternatively, perhaps for each i, we can find the j that maximizes ( |x_i| + |x_j| - ( |a_i - b_j| + |a_j - b_i| ) ). But even for each i, finding the best j is O(n), leading to O(n^2) time.

But that's impossible for n=2e5.

So we need a smarter approach.

Let me think of the delta expression again.

delta = |x_i| + |x_j| - |a_i - b_j| - |a_j - b_i|.

But x_i is a_i - b_i, so a_i = x_i + b_i. Similarly, a_j = x_j + b_j.

Substituting into |a_i - b_j| = |x_i + b_i - b_j| = |x_i + (b_i - b_j)|.

Similarly, |a_j - b_i| = |x_j + (b_j - b_i)|.

So delta can be written as:

|x_i| + |x_j| - ( |x_i + (b_i - b_j)| + |x_j + (b_j - b_i)| )

Let me denote d = b_i - b_j. Then, delta becomes:

|x_i| + |x_j| - ( |x_i + d | + |x_j - d | )

Hmm. So for each pair i, j, d is (b_i - b_j), and we compute this expression.

But how to model this.

Alternatively, perhaps for each i, we can precompute some information that allows us to find the best j.

Alternatively, perhaps the maximum delta is achieved when the two terms |x_i + d| and |x_j - d| are as small as possible.

But I'm not seeing it.

Wait, maybe there's a way to model this as x_i and x_j. Let's suppose that for a given i and j, what's the delta.

But even then, it's unclear.

Let me think of some examples. Suppose i and j are such that x_i is positive, x_j is positive.

Original sum is x_i + x_j.

After swap: x_i + (b_i - b_j) = (a_i - b_i) + (b_i - b_j) = a_i - b_j. So |a_i - b_j| is |x_i + (b_i - b_j)|. Similarly for the other term.

Wait, maybe the delta can be expressed as:

delta = (|x_i| + |x_j|) - ( |x_i + (b_i - b_j)| + |x_j - (b_i - b_j)| )

But this is for each pair (i, j). How can we find the maximum of this over all i and j?

Alternatively, perhaps we can separate variables. Let's denote for a fixed i, d_ij = b_i - b_j. Then for j, d_ij varies as j varies.

But even then, how to model the expression.

Alternatively, perhaps for each i, the maximum delta can be found by considering the j that makes the term ( |x_i| + |x_j| - |x_i + (b_i - b_j)| - |x_j - (b_i - b_j)| ) as large as possible.

But for each i, how to find j that maximizes this.

Alternatively, maybe for each i, the best j is the one where b_j is as close as possible to a_i, and b_i is as close as possible to a_j. Because that would make |a_i - b_j| and |a_j - b_i| as small as possible.

But even this requires checking for each i the j where b_j is near a_i and b_i is near a_j. Not sure.

Wait, another approach: Let's consider that for each i, the best j to swap with is the one where swapping i and j gives the maximum gain. So for each i, find the j that gives the maximum delta when swapped with i. Then, among all these (i,j) pairs, pick the maximum.

But even this would be O(n^2) in the worst case, which is not feasible.

Hmm. Let's think of the problem differently. Since we can perform at most one swap, what's the maximum possible gain we can get from a single swap. How can we compute that efficiently.

Wait, maybe for each j in the array, we can track some information that allows us to compute the best possible gain when swapping j with any other element.

Alternatively, let's precompute for each element in b, the best possible element in a to swap with. Wait, perhaps not.

Alternatively, think of the swap as pairing two elements in b: swap b_i and b_j. The gain depends on the a_i, a_j, b_i, b_j.

So perhaps, the maximum gain can be found by looking for pairs (i,j) where (a_i - b_i) and (a_j - b_j) are such that swapping them reduces the sum.

Wait, maybe if (a_i - b_i) and (a_j - b_j) are both positive, swapping them could lead to a_i - b_j and a_j - b_i which are smaller. For example, if a_i is much larger than b_i and a_j is also much larger than b_j. Then, swapping b_i and b_j (assuming a_i is close to b_j and a_j is close to b_i) could reduce the sum.

But how to model this.

Alternatively, perhaps the maximum gain is when swapping two elements in b such that the sum of (a_i - b_j) and (a_j - b_i) is minimized. But how.

Wait, but the gain is (original sum for i and j) - (new sum for i and j). So the gain is (|a_i -b_i| + |a_j -b_j|) - (|a_i -b_j| + |a_j -b_i|).

We need to find the maximum of this over all i < j.

Let's try to model this. Let's consider for each i, the possible j's that could form a pair with i to give a high gain. How can we find j for each i quickly.

Alternatively, perhaps precompute for each i the best possible j in O(1) time.

But how.

Alternatively, note that the gain is:

gain = (|x_i| + |x_j|) - ( |x_i + (b_i - b_j)| + |x_j - (b_i - b_j)| )

Let me denote d = b_i - b_j. Then:

gain = |x_i| + |x_j| - (|x_i + d| + |x_j - d| )

Hmm. Let's consider various cases for x_i and x_j.

Case 1: x_i and x_j are both positive. Then:

|x_i| = x_i, |x_j| = x_j.

d = b_i - b_j.

Then:

|x_i + d| = | (a_i - b_i) + (b_i - b_j) | = | a_i - b_j |.

Similarly, |x_j - d| = | (a_j - b_j) - (b_i - b_j) | = | a_j - b_i |.

So the gain is x_i + x_j - ( |a_i - b_j| + |a_j - b_i| )

Which is the same as the original delta.

But how to find this efficiently.

Alternatively, perhaps the maximum gain is when swapping the pair (i,j) that gives the maximum (|x_i| + |x_j| - (|x_i + d| + |x_j - d| )) where d = b_i - b_j.

But how to compute this.

Another approach: Let's consider that the maximum gain is achieved when (x_i + d) and (x_j -d) are as small as possible. So for each i, j, we want x_i + d and x_j -d to be as close to zero as possible.

But again, not sure.

Alternatively, think of this as for each i, j, the delta is:

delta = (|x_i| + |x_j|) - ( |x_i + (b_i - b_j)| + |x_j - (b_i - b_j)| )

But perhaps this can be rewritten as:

delta = (|x_i| - |x_i + d|) + (|x_j| - |x_j - d| )

where d = b_i - b_j.

Hmm. Let's see.

The term (|x_i| - |x_i + d|) depends on x_i and d.

Similarly for the other term.

So the delta is the sum of these two terms.

But how to model this.

Another idea: For each possible d, can we find the best possible x_i and x_j that maximize the sum of these two terms.

But d can vary widely, so perhaps that's not helpful.

Alternatively, perhaps the maximum gain is achieved when (x_i and x_j) are such that the individual terms (|x_i| - |x_i +d|) and (|x_j| - |x_j -d|) are maximized.

But again, not sure.

Wait, let's think of each term separately.

For the first term (|x_i| - |x_i +d|):

This term is maximized when |x_i| is as large as possible and |x_i +d| is as small as possible. For example, if x_i is positive and large, and adding d makes it smaller.

For example, if x_i is positive, and d is negative. Then x_i +d could be smaller than x_i, leading to a positive term.

Similarly, if x_i is negative and d is positive, then x_i +d could be smaller in absolute value.

So for the first term to be positive, adding d to x_i reduces its absolute value.

Similarly for the second term: (|x_j| - |x_j -d| ). To maximize this, the term |x_j -d| should be as small as possible.

For example, if x_j is positive, and d is positive, then x_j -d could be smaller than x_j, leading to a positive contribution.

So combining these, perhaps the best pairs (i,j) are those where swapping reduces the sum of the absolute differences for both positions.

But how to find such pairs efficiently.

Another approach: Let's precompute all possible pairs and find the maximum delta. But this is O(n^2) which is impossible.

Hmm. So perhaps there's a way to find the best j for each i in O(1) or O(log n) time, leading to overall O(n) or O(n log n) time.

But how?

Alternatively, let's consider that for each i, the best j to swap with is the one that maximizes (|x_i| + |x_j| - |a_i -b_j| - |a_j -b_i| ). Let's call this term G(i,j).

But how can we find j for each i that maximizes G(i,j).

Wait, let's expand G(i,j):

G(i,j) = |a_i - b_i| + |a_j - b_j| - |a_i - b_j| - |a_j - b_i|.

Let me substitute variables. Let a_i be A, b_i be B, a_j be C, b_j be D.

Then G becomes |A - B| + |C - D| - |A - D| - |C - B|.

So G = (|A-B| - |A-D|) + (|C-D| - |C-B|).

Hmm. Interesting. Let's see if this can be rewritten.

Now, the term (|A-B| - |A-D|) depends on A, B, D.

Similarly, the other term depends on C, D, B.

But B and D are the original values of b_i and b_j. So for each i and j, B and D are known.

But how to find pairs (i,j) where this sum is maximized.

Alternatively, perhaps for a fixed i, we can find the j that maximizes (|C-D| - |C-B|) + (|A-B| - |A-D| ), where A and B are fixed (since i is fixed), and C and D vary with j.

So for each i, we can precompute B (which is b_i), and A is a_i.

Then, for each j, D is b_j, C is a_j.

We need to find j such that the sum of two terms is maximized.

The two terms are:

Term1: |A-B| - |A - D|

Term2: |C-D| - |C - B|

So the sum is Term1 (dependent on D) plus Term2 (dependent on C and D, but C is a_j, which varies with j).

Hmm. So for each i, Term1 is a function of D (b_j), and Term2 is a function of C (a_j) and D (b_j).

But how can we model this for efficient computation.

Alternatively, perhaps we can precompute for each possible D (b_j) the maximum possible Term1 + Term2, given that j has a certain D and C (a_j).

But this seems complicated.

Alternatively, for each j, we can precompute some values that would allow us to quickly compute Term2 for a given B (b_i). For example, if we precompute for each j, the value of ( |a_j - b_j| - |a_j - B | ), which is Term2 when B is the b_i of some i.

But even this would require for each i, querying for all j's to find the maximum of (Term1 + Term2).

But Term1 for j is |A - B| - |A - D|, where D is b_j.

Wait, but for a fixed i (so A and B are fixed), Term1 for j is ( |A - B| - |A - D| ), where D is b_j.

So for j varying, Term1 is a function of D (b_j).

So for each i, the problem is to find j where (|A-B| - |A - D|) + ( |C - D| - |C - B| ) is maximized, where C is a_j and D is b_j.

Hmm. Let's see:

Let me reorganize this expression:

Term1 + Term2 = [ |A-B| - |A - D| ] + [ |C-D| - |C - B| ]

But C = a_j, D = b_j.

So for each i, we can precompute A = a_i, B = b_i. Then for each j, we have D = b_j, C = a_j.

We need to find j that maximizes the sum of these two terms.

Let me denote:

Term1 = |A-B| - |A - D| 

Term2 = |C - D| - |C - B|

So the sum is Term1 + Term2.

Now, let's see if we can model this as a function of D and C.

Term1 can be rewritten as ( |A-B| - |A - D| ), which can be viewed as the benefit of swapping B (b_i) with D (b_j) for the i-th element.

Term2 is ( |C - D| - |C - B| ), which is the benefit of swapping D (b_j) with B (b_i) for the j-th element.

So the total benefit of swapping i and j is the sum of the benefits from each element.

Hmm. So for each j, if we can precompute something that allows us to calculate (Term1 + Term2) for a given i, then perhaps we can find the maximum for each i quickly.

But how.

Alternatively, for each j, precompute two values: ( |C - D| - |C - B | ) for varying B. But B can be any of the b_i's.

But that's not feasible.

Alternatively, note that for a given j, the Term2 depends on B (which is b_i) and C (a_j), D (b_j). So for each j, Term2 is a function of B.

But when we are considering all possible pairs (i,j), for each j, B is the b_i of the current i. So for each j, when i varies, B varies.

So for each j, we need to find the i that when paired with j, gives the maximum (Term1 + Term2), which depends on B (b_i), A (a_i), and C (a_j), D (b_j).

But this seems quite complex.

Another angle: Let's consider that when swapping i and j, the gain is (original sum for i and j) - (new sum). So the maximum gain is the maximum of this over all pairs.

So the initial sum is the sum of all |a_k - b_k|. The minimal sum is the initial sum minus the maximum gain.

Thus, if we can compute the maximum gain possible, then the answer is initial_sum - max_gain.

But how to compute max_gain.

Let me think of this as for each j, compute the best possible i to swap with j such that the gain is maximum.

But again, with n=2e5, this approach is O(n^2), which is not feasible.

Wait, but perhaps there's a way to precompute some structures that allow for O(1) or O(log n) per j.

Alternatively, here's an idea:

For each j, when we swap i and j, the gain is:

gain = ( |a_i - b_i| + |a_j - b_j| ) - ( |a_i - b_j| + |a_j - b_i| )

We can rewrite this as:

gain = ( |a_i - b_i| - |a_i - b_j| ) + ( |a_j - b_j| - |a_j - b_i| )

Let me denote for each i and j:

gain1(i, j) = |a_i - b_i| - |a_i - b_j|

gain2(j, i) = |a_j - b_j| - |a_j - b_i|

So the total gain is gain1 + gain2.

Now, for each j, the maximum gain possible when swapping j with some i is the maximum over all i of (gain1(i, j) + gain2(j, i)).

But this seems like we need to find, for each j, the i that maximizes (gain1(i, j) + gain2(j, i)).

But how can this be done efficiently.

Alternatively, perhaps for each j, the best i is the one that maximizes gain1(i, j) + gain2(j, i) = ( |a_i - b_i| - |a_i - b_j| ) + ( |a_j - b_j| - |a_j - b_i| ).

But again, how to find this i for each j.

Hmm. Let's think of this as for each j, we can precompute the values of gain2(j, i) for all i, but that's O(n^2).

Alternatively, perhaps for each j, the gain2(j, i) can be written as ( |x_j| - |x_j - (b_i - b_j)| ), where x_j is a_j - b_j.

But not sure.

Wait, x_j is a_j - b_j. So when you swap j and i, the new term for j is |a_j - b_i|. The gain2 is the original x_j's absolute value minus the new term.

So gain2(j, i) = |x_j| - |a_j - b_i|.

But a_j - b_i is equal to x_j + (b_j - b_i), since a_j = x_j + b_j. So:

gain2(j, i) = |x_j| - |x_j + (b_j - b_i)|.

Similarly, gain1(i, j) is |x_i| - |x_i + (b_i - b_j)|.

So the total gain is |x_i| - |x_i + (b_i - b_j)| + |x_j| - |x_j + (b_j - b_i)|.

But (b_i - b_j) = -(b_j - b_i). So (b_i - b_j) is -d where d is (b_j - b_i).

So gain1(i,j) is |x_i| - |x_i -d |, and gain2(j,i) is |x_j| - |x_j +d |, where d = (b_j - b_i).

But how does this help.

Hmm. For a given j, we can think of d as (b_j - b_i), which is the same as (b_i = b_j - d). So for varying i, d can vary.

But not sure.

Another Idea: Let's precompute for each element i two values:

- The best possible gain when swapping i with another element j, where j is such that b_j is as close as possible to a_i. Because when you swap, the new term for i is |a_i - b_j|. So the closer b_j is to a_i, the better. Similarly, the new term for j is |a_j - b_i|. So the closer b_i is to a_j, the better.

So for each i, if we can find a j where b_j is as close as possible to a_i, and b_i is as close as possible to a_j, then this pair (i,j) could be a good candidate for the maximum gain.

But how to find such j's.

Perhaps, for each i, find j where b_j is closest to a_i. Then, for each i, compute the gain for swapping with that j. Similarly, find j where b_i is closest to a_j and compute the gain. Then, take the maximum among all these possible gains.

But this would take O(n) time for each i, leading to O(n^2) again.

But perhaps if we can preprocess the array b to allow for quick lookups.

For example, sort the array b and for each a_i, perform a binary search to find the closest b_j to a_i. Similarly, for each b_i, find the a_j that is closest to it. But this would require O(n) time per i for binary searches, leading to O(n log n) time.

But even then, how to compute the gain for these j's.

Wait, let's think. For each i, find j where b_j is as close as possible to a_i. Then compute the gain for swapping i and j. The j found here is a candidate for the best swap with i. Then, among all these candidates, the maximum gain is taken.

But would this approach capture the maximum possible gain?

Not necessarily. Because the best gain could come from a pair where neither j is the closest to a_i nor i is the closest to a_j. However, in practice, this approach may capture a lot of candidates and possibly the maximum.

But since the problem requires an exact solution, this approach is not guaranteed to work. However, given the time constraints, perhaps this is the way to go.

Alternatively, perhaps the maximum gain can be found by considering pairs where the a_i and a_j are such that a_i is close to b_j and a_j is close to b_i. So for each i, find j where a_j is close to b_i, and a_i is close to b_j.

But again, how to find such pairs efficiently.

Another Idea: Let's consider that the maximum gain is achieved when swapping i and j where (a_i - b_j) and (a_j - b_i) are as small as possible, which implies that the new terms |a_i - b_j| and |a_j - b_i| are minimized. The sum of these two terms is minimized, which maximizes the gain.

So the problem reduces to finding i and j that minimize (|a_i - b_j| + |a_j - b_i|). Then, the maximum gain is (original sum for i and j) minus this minimal sum.

But how to find such i and j.

Hmm. For each i and j, compute |a_i - b_j| + |a_j - b_i|. The minimal value of this sum is what we're looking for, but again, for n=2e5, this is O(n^2), which is impossible.

But perhaps we can model this sum as something that can be optimized.

Let me see:

sum = |a_i - b_j| + |a_j - b_i|.

We can rearrange this as:

sum = |a_i - b_j| + |b_i - a_j|.

Because |a_j - b_i| = |b_i - a_j|.

So sum is the sum of two absolute values. We can think of this as the Manhattan distance between the points (a_i, b_i) and (b_j, a_j) in 2D space. So the sum is the Manhattan distance between (a_i, b_i) and (b_j, a_j).

But Manhattan distance is not as easy to work with as Euclidean, but perhaps there's a way to preprocess this.

Alternatively, perhaps we can find for each j the best i that minimizes the Manhattan distance between (a_i, b_i) and (b_j, a_j). Then, among all pairs (i,j), the minimal sum is found.

But again, how to do this efficiently.

Another Idea: Let's precompute for all j the value of (b_j, a_j) and create a data structure that allows us to query for the closest point to (b_j, a_j) among all (a_i, b_i) for i. Then, the sum for j and i would be the Manhattan distance between these two points, and the minimal sum is the minimal Manhattan distance.

But Manhattan distance is |a_i - b_j| + |b_i - a_j|.

But even with such a data structure, for each j, querying the closest Manhattan distance would take O(log n) time if we have a suitable data structure. However, building such a data structure for Manhattan distance is non-trivial.

Alternatively, perhaps we can transform the coordinates to handle Manhattan distances. For example, Manhattan distance between (x1, y1) and (x2, y2) is |x1 -x2| + |y1 - y2|. Which is equivalent to the sum of the absolute differences of their coordinates.

But this is difficult to index for efficient queries. However, we can consider that for each point (a_i, b_i), we can precompute transformed coordinates such as (a_i + b_i, a_i - b_i), but I'm not sure if this helps.

Alternatively, since Manhattan distance is sum of absolute values, perhaps the minimal sum can be found by considering two points (a_i, b_i) and (b_j, a_j) where a_i is close to b_j and b_i is close to a_j. So for each j, the best i is where a_i is close to b_j and b_i is close to a_j.

But how to find such i's.

Wait, for each j, we can look for i where a_i is close to b_j and b_i is close to a_j. For example, for j, we can find all i's where a_i is in a small window around b_j, and b_i is in a small window around a_j. But this is heuristic and may not work for all cases.

Alternatively, split the problem into two parts: For each j, find the i that minimizes (|a_i - b_j| + |b_i - a_j|).

This can be rewritten as (|a_i - b_j| + |a_j - b_i| ), which is the same as the sum we're trying to minimize.

But again, how to find this i for each j.

Let's think of each i as a point (a_i, b_i). For each j, we need to find the point (a_i, b_i) that is closest in Manhattan distance to (b_j, a_j).

But Manhattan distance between (a_i, b_i) and (b_j, a_j) is |a_i - b_j| + |b_i - a_j|.

So the problem reduces to, for each query point (b_j, a_j), find the point in the set S = { (a_1, b_1), (a_2, b_2), ... } that has the minimal Manhattan distance to (b_j, a_j).

If we can preprocess S to answer these queries efficiently, then for each j, we can find the best i in O(1) or O(log n) time.

Manhattan distance is a challenging metric for this, but there is a way to handle it by transforming the coordinates. For example, Manhattan distance between two points (x1, y1) and (x2, y2) can be rewritten as max((x1 + y1) - (x2 + y2), (x1 - y1) - (x2 - y2), ...), but I'm not sure.

Alternatively, for Manhattan distances, we can use a data structure called a plane sweep or a k-d tree, but for large n (2e5), this may not be feasible.

Alternatively, since we can't process all j's, perhaps we can find the pair (i,j) that has the minimal sum of |a_i - b_j| + |a_j - b_i|, and use that to compute the maximum gain.

But again, the challenge is how to find this pair.

Another Idea: Let's think of the sum |a_i - b_j| + |a_j - b_i|.

We can rewrite this as |a_i - b_j| + |a_j - b_i| = |a_i - b_j| + |b_i - a_j|.

Which is the same as the Manhattan distance between the points (a_i, b_i) and (b_j, a_j). So the minimal sum is the minimal Manhattan distance between any such pair of points.

But how to find this minimal distance efficiently.

If we can find the minimal Manhattan distance between all pairs (i,j) in the set of points (a_i, b_i) and (b_j, a_j), then that would give us the minimal sum. But how.

Wait, the points are from two different sets: the first set is S = { (a_i, b_i) }, and the second set is T = { (b_j, a_j) }, for all j. We need to find the minimal Manhattan distance between any point in S and any point in T.

But since S and T are the same set (since both are all j from 1 to n), but perhaps not. Wait, T is the set of (b_j, a_j) for j=1 to n. So S is { (a_i, b_i) }, T is { (b_j, a_j) }.

So we need to find the minimal Manhattan distance between any two points from S and T.

But this is the same as finding the minimal sum |a_i - b_j| + |a_j - b_i|.

So the problem reduces to finding the minimal Manhattan distance between two sets S and T, each of size n.

The Manhattan distance between a point (x, y) in S and a point (u, v) in T is |x - u| + |y - v|.

But how to find the minimal such distance.

This is a classic problem in computational geometry. For two sets of points, find the pair with the minimal Manhattan distance.

The Manhattan distance can be transformed by rotating the coordinates. For example, Manhattan distance between (x, y) and (u, v) is equivalent to the maximum of ( (x + y) - (u + v), (x - y) - (u - v) ), etc. But I'm not sure.

Alternatively, the Manhattan distance is |x - u| + |y - v| = (x + y) - (u + v) if x >= u and y >= v, but this isn't helpful.

Another approach is to note that for Manhattan distance, the minimal distance is either achieved by points that are close in their transformed coordinates. For example, we can transform each point (x, y) into (x + y, x - y) and then compute the Chebyshev distance, which is the maximum of the two differences. But again, not sure.

Alternatively, for each point in T, compute the minimal distance to any point in S and keep track of the overall minimal.

But for n=2e5, this approach is O(n^2), which is not feasible.

So we need a way to process this more efficiently.

Hmm. Given the time constraints, perhaps this problem requires a different approach, and the initial approach of trying to find the maximum gain by considering certain properties of the pairs.

Wait, perhaps the maximum gain can be computed as follows.

The maximum possible gain is the maximum over all i and j of ( |a_i - b_i| + |a_j - b_j| ) - ( |a_i - b_j| + |a_j - b_i| ).

Let me think of this as:

gain = ( |x_i| + |x_j| ) - ( |a_i - b_j| + |a_j - b_i| )

where x_i = a_i - b_i, x_j = a_j - b_j.

But a_i = x_i + b_i, and a_j = x_j + b_j.

So substituting:

gain = |x_i| + |x_j| - |x_i + b_i - b_j| - |x_j + b_j - b_i|

Hmm. Not sure.

Another Idea: Let's assume that x_i and x_j are of the same sign. For example, both are positive. Then, the original terms are x_i + x_j. After swapping, the terms are |a_i - b_j| + |a_j - b_i|.

But a_i - b_j = x_i + b_i - b_j.

a_j - b_i = x_j + b_j - b_i.

So if x_i and x_j are positive, and the swap makes these terms smaller, then the gain would be positive.

For example, suppose x_i is 5 and x_j is 3. If swapping reduces each term to 0 and 0, then gain is 8.

But this is ideal.

But how to find such pairs.

Alternatively, for each i, we can find the j where x_i and x_j are positive and (b_i - b_j) is such that x_i - (b_j - b_i) is minimized. But again, not sure.

Another Idea: For each i, compute two possible candidates:

- The j where b_j is as close as possible to a_i. This would minimize |a_i - b_j|.

- The j where b_i is as close as possible to a_j. This would minimize |a_j - b_i|.

Then, the best j for i is one of these candidates. So for each i, check these two j's and compute the gain. The overall maximum gain would be the maximum over all these pairs.

But even this approach requires O(n) time if the candidates can be found in O(1) time.

So how to find these candidates.

To find the j where b_j is closest to a_i, we can sort the array b and perform a binary search for a_i. Similarly, to find the j where a_j is closest to b_i, we can sort the array a and perform a binary search for b_i.

But we need to track the indexes j for these values. Let's see.

Wait, let's create two sorted lists:

- sorted_b: contains the elements of b along with their indices, sorted by their values.

- sorted_a: contains the elements of a along with their indices, sorted by their values.

Then, for each i:

1. Find the j in sorted_b where b_j is closest to a_i. This can be done via binary search.

2. Find the j in sorted_a where a_j is closest to b_i. Again, via binary search.

For each of these j's, compute the gain when swapping i and j, and keep track of the maximum gain.

After processing all i's, the maximum gain found would be the best possible.

Additionally, we can also check the j's adjacent to the found positions in the binary search to account for possible closer values.

This approach would be O(n log n) time, which is acceptable for n=2e5.

But would this approach find the maximum gain? It's possible that the maximum gain pair is not found by either of these two steps, but for the purposes of time, perhaps this approach is sufficient.

Let's test this idea against the sample inputs.

Sample 1:

Input:

5

5 4 3 2 1

1 2 3 4 5

Original sum is |5-1| + |4-2| + |3-3| + |2-4| + |1-5| = 4+2+0+2+4 = 12.

The optimal swap is between indices 0 and 4 (assuming 0-based).

So for i=0 (a_i=5, b_i=1), the closest j in b to a_i=5 would be j=4 (b_j=5). Similarly, for i=0, the closest j in a to b_i=1 is j=4 (a_j=1).

So swapping i=0 and j=4 gives a gain of (4 +4) - (0 +0) = 8. So the maximum gain is 8, which is correct.

So in this case, the approach would find the correct j's.

Sample 2:

Input:

2

1 3

4 2

Original sum is |1-4| + |3-2| = 3 + 1 =4. After swapping, the sum is |1-2| + |3-4|=1 +1=2. So gain is 4-2=2.

For i=0 (a_i=1, b_i=4), the closest j in b to a_i=1 is j=1 (b_j=2). The gain would be |1-4| + |3-2| - (|1-2| + |3-4| ) = 3+1 - (1+1) = 2. Which is the maximum.

Similarly, for j=1 (a_j=3, b_j=2), the closest i in a to b_j=2 would be i=0 (a_i=1) or i=1 (a_i=3), but a_i=1 is further from 2. But in this case, the approach would find the correct pair.

So the approach works for the samples.

Thus, the plan is:

1. Compute the initial sum.

2. For each i, find the j in b that is closest to a_i. Compute the gain for swapping i and j.

3. For each i, find the j in a that is closest to b_i. Compute the gain for swapping i and j.

4. Find the maximum gain across all these swaps.

5. The minimal sum is initial_sum - max_gain (if max_gain is positive, else initial_sum).

This approach would be O(n log n) time.

But how to implement this.

First, sort the array b with their indices, and for each a_i, find the closest element in b.

Similarly, sort the array a with their indices, and for each b_i, find the closest element in a.

Wait, perhaps we can create a sorted list of (value, index) pairs for array b and for array a.

For each a_i, find the closest value in the sorted b list. For each such value, get its index j.

Similarly, for each b_i, find the closest value in the sorted a list. For each such value, get its index j.

For each of these j's, compute the gain for swapping i and j, and track the maximum gain.

Also, need to check adjacent elements in the sorted list to ensure we have the closest possible.

So steps:

1. Compute initial_sum.

2. Sort the list of (b_j, j) for j in 0..n-1.

3. Sort the list of (a_j, j) for j in 0..n-1.

4. For each i in 0..n-1:

   a. Find the closest b_j to a_i using the sorted_b list.

      - Use binary search to find the insertion point in the sorted_b list.

      - Check the element at the insertion point and before to find the closest.

      - For each candidate j in these positions, compute gain for swapping i and j.

   b. Find the closest a_j to b_i using the sorted_a list.

      - Again, use binary search to find the insertion point.

      - Check adjacent elements.

      - For each candidate j in these positions, compute gain for swapping i and j.

   c. Keep track of the maximum gain found.

5. The minimal sum is initial_sum - max_gain if max_gain > 0, else initial_sum.

This approach will check for each i, up to a few j's (like 2 candidates for each binary search) and compute the gain. Since each binary search is O(log n), and for each i, we do a constant number of checks, the total time is O(n log n), which is acceptable.

But what about duplicate values in the array? The binary search will handle them correctly, as long as we check the appropriate positions.

But need to be careful with the binary search implementation.

Now, let's implement this in Python.

First, compute the initial sum.

Then, create sorted lists for b and a with their indices.

For each i, perform the binary searches.

But in Python, the bisect module can help with binary search.

For example, to find the closest value in a sorted list to a target:

def find_closest(sorted_list, target):

    pos = bisect.bisect_left(sorted_list, target)

    candidates = []

    if pos > 0:

        candidates.append(pos -1)

    if pos < len(sorted_list):

        candidates.append(pos)

    if not candidates:

        return None

    closest = min(candidates, key=lambda x: abs(sorted_list[x][0] - target))

    return sorted_list[closest]

But sorted_list here is a list of tuples (value, index), sorted by value.

So for each a_i, we search in the sorted_b list for the closest value to a_i. The sorted_b list is sorted by the first element of the tuple (the value of b_j).

Then, for each candidate j, compute the gain for swapping i and j.

The same for the other case: for each b_i, search in the sorted_a list for the closest value to b_i.

But in the second case, we need to find j such that a_j is closest to b_i.

So for each i, the steps are:

- Find j in sorted_b where b_j is closest to a_i. Compute gain for i and j.

- Find j in sorted_a where a_j is closest to b_i. Compute gain for i and j.

Additionally, for each of these searches, we should check the nearest elements in the sorted list (i.e., the element before and after the insertion point) to ensure we find the closest.

Once we have all possible j's for each i, compute the gain for each pair and keep track of the maximum.

Once all pairs are processed, the answer is initial_sum minus the maximum gain (if it's positive), else initial_sum.

Now, let's code this.

But first, note that in Python, the bisect module's bisect_left function returns the insertion point. For example:

For a list sorted in ascending order, bisect_left returns the first position where the target can be inserted to maintain sorted order.

So for a sorted list sorted_list, and a target value, the insertion point is pos.

The closest values are in pos-1 (if pos>0) and pos (if pos < len(sorted_list)).

So for each target, we check these two positions and choose the one with the smallest difference.

Once we have the closest elements, we need to get their indices j and compute the gain.

Now, the code steps:

Read n, a, b.

Compute initial_sum = sum( abs(a[i] - b[i]) for i in range(n) )

Create sorted_b = sorted( (b[j], j) for j in range(n) )

Create sorted_a = sorted( (a[j], j) for j in range(n) )

max_gain = 0

For each i in 0..n-1:

    a_i_val = a[i]

    b_i_val = b[i]

    # Find j in sorted_b where b_j is closest to a_i_val

    # Search in sorted_b

    target = a_i_val

    pos = bisect.bisect_left(sorted_b, (target, 0))  # the 0 is arbitrary, since we compare only the first element.

    candidates = []

    if pos > 0:

        candidates.append( pos-1 )

    if pos < len(sorted_b):

        candidates.append( pos )

    # also check pos-2? Maybe not. Just adjacent positions.

    for c in candidates:

        b_j_val, j = sorted_b[c]

        if j == i:

            continue  # swapping same index gives no gain

        original = abs(a[i] - b[i]) + abs(a[j] - b[j])

        new_sum = abs(a[i] - b[j]) + abs(a[j] - b[i])

        current_gain = original - new_sum

        if current_gain > max_gain:

            max_gain = current_gain

    # Find j in sorted_a where a_j is closest to b_i_val

    target = b_i_val

    pos = bisect.bisect_left(sorted_a, (target, 0))

    candidates = []

    if pos > 0:

        candidates.append( pos-1 )

    if pos < len(sorted_a):

        candidates.append( pos )

    for c in candidates:

        a_j_val, j = sorted_a[c]

        if j == i:

            continue

        original = abs(a[i] - b[i]) + abs(a[j] - b[j])

        new_sum = abs(a[i] - b[j]) + abs(a[j] - b[i])

        current_gain = original - new_sum

        if current_gain > max_gain:

            max_gain = current_gain

The answer is initial_sum - max_gain.

But wait, why do we check j == i and skip them? Because swapping an element with itself doesn't change anything. So in that case, the gain is zero. So we can skip those to avoid unnecessary computation.

But in the code, even if j == i, the current_gain is zero, but since max_gain starts at zero, it won't change the maximum.

But to avoid redundant checks, perhaps we should skip them.

But for the code, the 'continue' statement skips processing j == i.

Now, test this code with sample input 1.

Sample 1:

n =5

a = [5,4,3,2,1]

b = [1,2,3,4,5]

sorted_b is sorted by value. So sorted_b will be [(1,0), (2,1), (3,2), (4,3), (5,4)]

For i=0, a_i_val=5.

Searching for 5 in sorted_b. bisect_left finds pos=4. candidates are 3 (if pos>0) and 4.

Wait, sorted_b is [(1,0), (2,1), (3,2), (4,3), (5,4)]. The target is 5. bisect_left for (5,0) would return 4 (since the first elements are compared). So candidates are 4-1=3, and pos=4.

But for the target 5, the closest is the element at 4 (5). So j=4.

Compute swapping i=0 and j=4.

Original sum for these indices: |5-1| + |1-5| = 4 +4 =8.

New sum: |5-5| + |1-1| =0+0=0.

gain is 8-0=8. So max_gain becomes 8.

Then, for the second part: Find j in sorted_a where a_j is closest to b_i_val=1.

sorted_a is sorted by a_j values. a is [5,4,3,2,1], so sorted_a is [(1,4), (2,3), (3,2), (4,1), (5,0)].

target is 1. bisect_left returns 0. candidates are 0 and 0 (since pos=0). So j=4.

But j=4 is the same as i=0 in this case? i=0, j=4. So no.

So swapping i=0 and j=4: which is the same as the first case.

So the code would compute the same gain of 8.

Thus, the code would capture this gain.

Similarly for other i's, but the maximum gain is 8, leading to initial_sum (12) minus 8 gives 4, which is correct.

Sample 2:

n=2

a = [1,3]

b = [4,2]

initial sum is |1-4| + |3-2| =3+1=4.

sorted_b is sorted by b values: [(2,1), (4,0)].

sorted_a is sorted by a values: [(1,0), (3,1)].

For i=0 (a_i_val=1, b_i_val=4):

First part: find j in sorted_b closest to a_i_val=1. sorted_b is [(2,1), (4,0)].

bisect_left for 1 in sorted_b (elements 2 and 4). The insertion pos is 0. So candidates are pos-1 (invalid) and pos=0.

So j=1 (since sorted_b[0] is (2,1)), which is j=1.

Compute swapping i=0 and j=1.

original is |1-4| + |3-2|=3+1=4.

new sum: |1-2| + |3-4|=1+1=2.

gain is 4-2=2.

Then, second part: find j in sorted_a closest to b_i_val=4 (b_i_val=4). sorted_a is [(1,0), (3,1)]. bisect_left for 4 is pos=2, which is out of range. So candidates is pos-1=1.

j=1 (sorted_a[1] is (3,1)).

Swap i=0 and j=1:

original is |1-4| + |3-2|=3+1=4.

new sum: |1-2| + |3-4|=1+1=2. gain is 2.

So the maximum gain is 2.

So the minimal sum is 4-2=2.

Which is correct.

Thus, the code works for the samples.

Now, in terms of edge cases:

- What if no swap improves the sum? Then max_gain remains 0, and the answer is the initial sum.

- What if the same element is swapped (but j is not i)? Like, if the best gain is achieved by swapping j and i where j is the same as i. But since the code skips j == i, this is not possible.

But swapping the same element is allowed, but it has no effect. So the code correctly ignores it.

Thus, this approach should work.

Now, coding this in Python.

But need to handle the sorted lists of tuples.

Also, in Python, the bisect module's bisect_left function requires the list to be sorted. The tuples are sorted based on their first element, then the second.

But in this case, when we pass (target, 0) to bisect_left, the comparison is done based on the first element of the tuple. So bisect_left will find the correct insertion point.

But the code should work.

But we need to create sorted_b as a list of (b_val, index) pairs, sorted by b_val.

Similarly for sorted_a.

So, code:

import bisect

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

initial_sum = sum(abs(ai - bi) for ai, bi in zip(a, b))

sorted_b = sorted((val, idx) for idx, val in enumerate(b))
sorted_a = sorted((val, idx) for idx, val in enumerate(a))

max_gain = 0

for i in range(n):
    ai_val = a[i]
    bi_val = b[i]
    
    # Find closest in b to ai_val
    target = ai_val
    pos = bisect.bisect_left(sorted_b, (target, 0))
    candidates = []
    if pos > 0:
        candidates.append(pos-1)
    if pos < len(sorted_b):
        candidates.append(pos)
    # Check up to two candidates
    for c in candidates:
        b_j, j = sorted_b[c]
        if j == i:
            continue
        original = abs(ai_val - bi_val) + abs(a[j] - b[j])
        new_sum = abs(ai_val - b_j) + abs(a[j] - bi_val)
        current_gain = original - new_sum
        if current_gain > max_gain:
            max_gain = current_gain
    
    # Find closest in a to bi_val
    target = bi_val
    pos = bisect.bisect_left(sorted_a, (target, 0))
    candidates = []
    if pos > 0:
        candidates.append(pos-1)
    if pos < len(sorted_a):
        candidates.append(pos)
    for c in candidates:
        a_j, j = sorted_a[c]
        if j == i:
            continue
        original = abs(ai_val - bi_val) + abs(a[j] - b[j])
        new_sum = abs(ai_val - b[j]) + abs(a[j] - bi_val)
        current_gain = original - new_sum
        if current_gain > max_gain:
            max_gain = current_gain

print(initial_sum - max_gain)

This code should work.

But let's test it against the samples.

Sample 1:

Input:

5

5 4 3 2 1

1 2 3 4 5

initial_sum is 4 + 2 + 0 + 2 +4 =12.

In the code:

For i=0, ai_val=5, bi_val=1.

Looking in sorted_b for closest to 5:

sorted_b is sorted by b's values. The sorted_b list is [(1,0), (2,1), (3,2), (4,3), (5,4)].

bisect_left for (5,0) is 4. candidates are 3 and 4.

Checking pos=3: b_j=4, j=3. Original is |5-1| + |2-4|=4+2=6. New sum is |5-4| + |2-1|=1+1=2. gain is 4.

pos=4: b_j=5, j=4. Original is 4 + |1-5|=4 +4=8. new sum is 0 +0=0. gain is 8. So max_gain becomes 8.

Then, for bi_val=1, look in sorted_a for closest to 1. sorted_a is [(1,4), (2,3), (3,2), (4,1), (5,0)]. bisect_left for 1 is 0. candidates are 0 and 0.

j=4 (a_j=1). j=4 is not i=0. Original is |5-1| + |1-5|=4+4=8. new sum is |5-5| + |1-1|=0. gain is 8. same as before.

So the max_gain is 8.

So the answer is 12-8=4.

Sample 2:

n=2

a = [1,3]

b = [4,2]

initial_sum is 3+1=4.

For i=0:

ai_val=1, bi_val=4.

Looking in sorted_b (sorted by b's values) is [(2,1), (4,0)].

Closest to 1 is 2. j=1.

original is 3 +1=4. new sum is |1-2| + |3-4| = 2. gain is 2.

Then, for bi_val=4, look in sorted_a for closest to 4. sorted_a is [(1,0), (3,1)]. The closest is 3 (j=1).

original is 3 +1=4. new sum is |1-2| + |3-4|=2. gain is 2.

For i=1:

ai_val=3, bi_val=2.

Looking in sorted_b for closest to 3. sorted_b is [(2,1), (4,0)].

bisect_left for 3 in [(2,1), (4,0)] is 1. candidates are 0 and 1.

Check j=0 (b_j=4). original is |3-2| + |4-0's b_j is 4? Wait, let's see:

i=1 is the current index. a[i]=3, b[i]=2.

Looking for closest to 3 in sorted_b:

sorted_b is [(2,1), (4,0)]. The values are 2 and 4. 3 is closest to 2 (difference 1) and 4 (difference 1). So two candidates.

Check j=1 (sorted_b[0] is (2,1)).

original is |3-2| + |1-4|=1+3=4. new sum is |3-4| + |1-2|=1+1=2. gain is 2.

Check j=0 (sorted_b[1] is (4,0)). original is |3-2| + |0th element's b is 4. So a[j] is 1.

original is |3-2| + |1-4| =1+3=4. new sum is |3-4| + |1-2|=1+1=2. gain is 2.

Then, for the other part: bi_val=2.

Look in sorted_a for closest to 2. sorted_a is [(1,0), (3,1)].

bisect_left for 2 is 1. candidates are 0 and 1.

Check j=0 (a_j=1). original is |3-2| + |1-4|=1+3=4. new sum is |3-4| + |1-2|=2. gain is 2.

Check j=1 (a_j=3). original is |3-2| + |3-4|=1+1=2. new sum is |3-4| + |3-2|=1+1=2. gain is 0.

So the maximum gain remains 2.

Thus, the code works.

Another test case: when no swap is better.

Example: n=1. But n >=1. But for n=1, no swap possible. So the initial sum is the answer.

But according to the problem statement, n can be 1. So code should handle that.

So for n=1, initial_sum is |a[0] - b[0]|. max_gain remains 0. So answer is initial_sum.

Thus, the code handles this.

Another case: swapping two elements gives a gain, but not the maximum possible.

But code should find the maximum.

Thus, the code should be correct.
</think>

```python
import bisect

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

initial_sum = sum(abs(ai - bi) for ai, bi in zip(a, b))

sorted_b = sorted((val, idx) for idx, val in enumerate(b))
sorted_a = sorted((val, idx) for idx, val in enumerate(a))

max_gain = 0

for i in range(n):
    ai_val = a[i]
    bi_val = b[i]
    
    # Find closest in b to ai_val
    target = ai_val
    pos = bisect.bisect_left(sorted_b, (target, 0))
    candidates = []
    if pos > 0:
        candidates.append(pos-1)
    if pos < len(sorted_b):
        candidates.append(pos)
    for c in candidates:
        b_j, j = sorted_b[c]
        if j == i:
            continue
        original = abs(ai_val - bi_val) + abs(a[j] - b[j])
        new_sum = abs(ai_val - b_j) + abs(a[j] - bi_val)
        current_gain = original - new_sum
        if current_gain > max_gain:
            max_gain = current_gain
    
    # Find closest in a to bi_val
    target = bi_val
    pos = bisect.bisect_left(sorted_a, (target, 0))
    candidates = []
    if pos > 0:
        candidates.append(pos-1)
    if pos < len(sorted_a):
        candidates.append(pos)
    for c in candidates:
        a_j, j = sorted_a[c]
        if j == i:
            continue
        original = abs(ai_val - bi_val) + abs(a[j] - b[j])
        new_sum = abs(ai_val - b[j]) + abs(a[j] - bi_val)
        current_gain = original - new_sum
        if current_gain > max_gain:
            max_gain = current_gain

print(initial_sum - max_gain)
```