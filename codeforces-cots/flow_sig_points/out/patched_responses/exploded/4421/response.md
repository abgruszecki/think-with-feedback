<think>
Okay, let's try to understand this problem. So Andrew has to compute, for each k from 1 to n-1, the number of elements in a k-ary heap that violate the min-heap property. The violation happens when a child is less than its parent. Hmm.

First, let's think about what a k-ary heap structure looks like. For each element v (starting from 1), its children are in positions k(v-1)+2 up to kv+1. So the parent of a node v (when v is not 1) is p(v) = ((v - 2) // k) + 1. Wait, maybe. Let's see: For a node v, how do you find its parent? Because for a node in a k-ary heap, each parent has exactly k children. So the parent of v is the floor of (v-2)/k +1. Let's verify this with k=1. For example, when k=1, the parent of node 2 is (2-2)/1 +1= 0 +1=1. Parent of 3 is (3-2)/1 +1=1+1=2. Which would make the heap a linked list. That's correct for a 1-ary heap (each node has 1 child, except maybe the last ones). So the formula for parent is correct.

So, for each k, we need to process all nodes from 2 to n (since node 1 has no parent), compute their parent using this formula, and check if a[v-1] (since arrays are 0-based in Python) is less than a[p-1]. If it is, that's a violation. The count for each k is the number of such violations.

The problem is, for each k from 1 to n-1, we need to compute this count. But if n is up to 2e5, then doing this naively (for each k, iterate all nodes from 2 to n and check their parent) would be O(n^2) time, which is way too slow for n=2e5. That's 4e10 operations. So we need a smarter approach.

So the challenge is to find an efficient way to compute, for all possible k values, the number of elements where a[v] < a[parent(v)].

Let me think: For each node v (v >=2), determine for which k's the parent of v in a k-ary heap would be some p, such that a[v] < a[p]. Then, for each such k, we need to increment the count. Then, after processing all nodes, the count for each k is the sum of all these increments.

But how can we model the ranges of k for which the parent of v is a particular p where a[v] < a[p]?

Wait, but first, let's consider each node v (v >=2). For each such v, the parent in a k-ary heap is p = ((v-2) // k) +1. So for each v, we can find all k's where this p is such that a[v] < a[p]. Then, for each such k, we add 1 to the result for that k. So the total result for a given k is the sum over all v >=2 of 1 if a[v] < a[parent(v)] for that k, else 0.

The key is to find, for each v, the set of k's where this condition is true. But since k can be up to n-1, which is 2e5, and v can be 2e5 as well, we need a way to represent these ranges efficiently.

Let's think for each node v, which values of k will cause p to be a certain node. For example, for a given v, when k is in some interval, the parent p of v is fixed. Because as k increases, the division (v-2) // k changes. For each possible p (which can be from 1 to v-1), we can find the range of k's where the parent is p. Then, if a[v] < a[p], we need to add 1 to all k's in that range.

So for each v, we need to find all possible p's (parents) and the ranges of k that would lead to that p. Then, for each such range where a[v] < a[p], we increment the count for all k in that range.

So this approach would allow us to precompute for each v the ranges of k where the parent is such that the condition holds, and then accumulate these ranges into the answer array.

Now, how to compute the ranges of k for a given v and possible p?

Let's consider the formula for p: p = ((v-2) // k) + 1. So solving for k:

k must satisfy (p-1) <= (v-2)/k < p.

Wait, wait. Let's rearrange the equation. Let's say for a given v and p, the k's that result in parent p are those k where (v-2)/(p-1) >= k > (v-2)/p. Because (v-2) divided by k gives (p-1), so (v-2) //k = p-1. So:

p-1 = floor( (v-2)/k )

Which implies that (p-1) * k <= v-2 < p *k

But k is a positive integer.

Alternatively, solving for k:

k > (v-2)/p 

and 

k <= (v-2)/(p-1), if p-1 >0.

But when p=1, then (p-1) is 0, but that's a division by zero. So when p=1, then the condition is k > (v-2)/1, which would imply that (v-2) < k * 1. But since p=1, the parent is ((v-2)//k) +1 = 0 +1=1. So for p=1, the condition is (v-2) //k =0, which implies that k > v-2. Because (v-2)/k < 1. So for k > v-2, then (v-2)//k is 0, so p=1.

So for each possible p (which must be <= v-1, since the parent can't be equal to or larger than v), we can find the possible k's.

So for a given v, the possible p's are from 1 to v-1 (since parent is at least 1, and the child is v >=2, so parent can't be v or larger). Wait, wait. Let's see: for example, when v=2, the parent is 1, regardless of k. Because (2-2)//k = 0, so p=0+1=1. So for v=2, p=1. So for any k, the parent of 2 is 1. So for all k, the condition a[2] < a[1] would contribute 1 to the count for that k if true.

But for larger v, like v=5, possible p's vary with k.

So, the approach is:

For each v from 2 to n:

- Check if a[v] < a[p] for any p that could be a parent of v for some k.

Wait, but how? For each v, we need to find all possible p's that can be its parent for some k. Then for each p, compute the range of k's where p is the parent of v, and if a[v] < a[p], add 1 to all k's in that range.

So for each v, the possible p's are in 1 <= p <= v-1.

For each p, we can find the possible k's that would make the parent of v equal to p. Then, for those k's, if a[v] < a[p], we add 1.

So for each v, iterate over all possible p's and find the k's where p is the parent. Then, if a[v] < a[p], add 1 to the answer for those k's.

But how to find the ranges of k where p is the parent of v.

Let's consider the case where p >=1.

The parent of v is p if and only if:

p-1 = floor( (v-2)/k )

Which is equivalent to:

p-1 <= (v-2)/k < p

Multiply all parts by k (assuming k>0, which it is):

k*(p-1) <= v-2 < k*p

Which can be rearranged as:

(v-2)/p < k <= (v-2)/(p-1)

But this is valid only when p >1.

Wait, because when p=1, then the condition becomes 0 <= (v-2)/k <1, which implies that k > v-2. So for p=1, k must be > v-2. But k can be up to n-1, which for v >=2 is possible only if v-2 <k <=n-1. But when v-2 is >=k, then p would not be 1.

So for p=1, the condition is k > v-2.

Now, for each p in 1 to v-1, let's find the possible k ranges.

Case 1: p=1.

Then, the parent is p=1 when (v-2)/k <1 and >=0. So k > v-2.

But since k must be >=1, this is possible only when v-2 <k.

But k can be from 1 to n-1. So for p=1, the k's are in (v-2, ∞), but since k is at most n-1, the valid k's are max(v-1, 1) to n-1. But wait, since v >=2, v-2 can be 0 (when v=2). For example, when v=2 and p=1, then k must be >0 (since (2-2)/k=0 <1). So for v=2, all k >=1 (since k can be up to n-1). So the range is k >=1. So for p=1 and v=2, the k's are all possible k (1 to n-1). So if a[2] < a[1], then all k would have this count increased by 1.

But how to handle that.

Case 2: p >1.

Then, for p>1, the condition is:

k must satisfy:

(v-2)/p < k <= (v-2)/(p-1)

But since k is an integer >=1.

So for each p in 2 to v-1, the valid k's are in the interval [ floor( (v-2)/p ) +1 , floor( (v-2)/(p-1) ) ]

Wait, let's compute the lower and upper bounds.

The lower bound is (v-2)/p <k → k> (v-2)/p → since k is integer, k >= floor( (v-2)/p ) +1.

The upper bound is k <= (v-2)/(p-1). So floor( (v-2)/(p-1) )

So the valid k's for p>1 are from l to r, where:

l = floor( (v-2)/p ) +1

r = floor( (v-2)/(p-1) )

But p must be such that this interval is valid (l <= r).

If l > r, then there are no such k's for this p.

So for each p in 2 to v-1, compute l and r. If l <=r and r >=1, then k can be from l to r. Also, k must be >=1 and <=n-1.

But how to handle these ranges for each v and p.

Now, the problem is that for each v and p, we need to compute the possible k's that fall into these ranges, and then if a[v] < a[p], add 1 to each k in those ranges.

But since n can be up to 2e5 and v can be up to 2e5, iterating for each v and p would be O(n^2), which is not feasible.

Thus, we need a smarter approach.

Alternative idea: For each v, find all possible p's that can be a parent for some k, and then for those p's where a[v] < a[p], add 1 to all k's in the range of k's that correspond to that p.

But even that seems challenging. Let's think of it another way: for each possible k, we need to process all nodes and count how many have a[v] < a[parent(v)]. So the answer for a particular k is the sum over v >=2 of 1 if a[v] < a[p], else 0.

But for each k, the parent of v is ((v-2)//k) +1. So for each v, the parent is determined by k.

But calculating this for each k is O(n), which would be 2e5 * 2e5 = 4e10 operations. That's way too slow.

So we need to find a way to precompute for all possible k's the sum of 1's where a[v] < a[p(v,k)].

Alternative approach: For each v, find all k's where a[v] < a[p(v,k)] and accumulate these into the answer array. But again, doing this for each v and k is O(n^2).

But perhaps we can model the problem as for each v, find the set of k's where p(v,k) = p and a[v] < a[p], then for each such p, add 1 to all k's in the k range corresponding to p.

This way, for each v, we can iterate over possible p's (those where a[v] < a[p]) and compute the ranges of k that would make p the parent of v, and add 1 to those k's.

The question is, how many p's per v do we need to check? For example, for a given v, how many p's are there where a[v] < a[p], and for which there exists a k where p is the parent of v.

But even this might not be feasible for large v. However, perhaps the number of such p's is small.

Alternatively, for each v, the p's that can be parents are in 1 to v-1. For each p in 1 to v-1, if a[v] < a[p], then we need to find the ranges of k where p is the parent of v and add 1 to those k's.

But for v=2e5, this would take O(2e5) operations per v, leading to O( (2e5)^2 ) operations, which is 4e10 again. Not feasible.

So this approach is not going to work. We need a smarter way.

Alternative Idea: For each node v, the parent in a k-ary heap is p = (v-2) //k +1. Let's think about the possible k's that would make p such that a[v] < a[p]. So for each v, we can find the minimal and maximal k that make p a certain value where a[v] < a[p].

Wait, but perhaps the key is that for each v, the set of k's where a[v] < a[p(v,k)] can be represented as a union of intervals. Then, we can precompute all these intervals and use a prefix sum array to count the total for each k.

So let's think: for each v, the answer for k is 1 if a[v] < a[p], else 0. The total answer for k is the sum over all v of these 1s.

So for each v, we need to find all k's in 1..n-1 where a[v] < a[p(v,k)].

We can model this as for each v, find the set of k's where p(v,k) is such that a[v] < a[p], and then collect all these k's. Then, the answer for each k is the total number of v's that include k in their set.

Now, the problem reduces to, for each v, find all k's where p(v,k) exists and a[v] < a[p(v,k)], then add these k's to the count. The challenge is to compute this efficiently.

So let's focus on a single v. For each possible k, p(v,k) can be determined. But how can we find all k's for which a[v] < a[p(v,k)].

But since p(v,k) = (v-2) //k +1, which depends on k, perhaps we can find the ranges of k where p(v,k) equals a certain p, and then check if a[v] < a[p]. If yes, then all k's in that range contribute 1 to the answer.

So for each v, we can iterate over possible p's (those that are possible for some k), compute the range of k's that make p the parent of v, and if a[v] < a[p], add 1 for all k in that range.

This way, each v contributes multiple ranges of k's (each for a different p) where a[v] < a[p].

But how many ranges do we need to process per v?

The number of possible p's for a given v is O(sqrt(v)), because p can be up to v-1. But for a given k, the parent p is (v-2)//k +1. So as k increases from 1 to n-1, p decreases. For example, when k is 1, p is (v-2) +1 = v-1. As k increases, (v-2)//k decreases, so p decreases. For k up to (v-2), the parent could be 1. So the number of different p's for a given v is O( sqrt(v) ), since for k <= sqrt(v), (v-2)//k can be up to O(sqrt(v)), and for k > sqrt(v), (v-2)//k is O(sqrt(v)).

Thus, for each v, the number of possible p's is O(sqrt(v)), which for n=2e5 would be O( ~450 per v ), leading to a total of 2e5 * 450 = 9e7 operations, which is manageable.

So the plan is:

1. For each v from 2 to n:

   a. Compute all possible p's (parents) that can exist for some k, along with their k ranges.

   b. For each such p, check if a[v-1] (0-based) is less than a[p-1].

   c. If yes, then for the corresponding k range of p, add 1 to the answer for all k in that range.

2. After processing all v's, compute the prefix sums for each k and output the counts for k=1 to n-1.

But how to compute the ranges for p?

Let's proceed step by step.

For a given v, the possible p's are all possible values of ((v-2)//k) +1 as k varies from 1 to n-1.

But how to find all possible p's and their corresponding k ranges.

Alternative approach: for each v, we can find all possible p's by considering that for each possible p, the k ranges can be determined as follows.

For p=1:

   k must be > v-2. So the range is k in (v-2, ∞) ∩ [1, n-1]. So if v-2 < n-1, then the range is k from max(v-1, 1) to n-1. For example, if v=2, v-2=0, so k must be >0. But since k starts from 1, the range is 1 to n-1. So for p=1, the k's are from (v-1) to n-1. But wait, (v-2) <k → k >=v-1 (since k is integer). So for p=1, the k's are from k_min = v-1 (but since k must be at least 1) to k_max = n-1.

For p>1:

   The k ranges are determined by (v-2)/p <k <= (v-2)/(p-1). So for each p, the k's are in [ floor( (v-2)/p ) +1, floor( (v-2)/(p-1) ) ].

But p can range from 2 to v-1.

But how to find all possible p's for a given v. We can iterate p from 1 upwards until (p-1) > (v-2)/k_min, but I'm not sure.

Alternatively, we can note that for a given v, the possible p's can be found by iterating over all possible divisors or something similar.

Another approach is to iterate through the possible values of k and find the p for each, but that's O(n) again. So perhaps we can model this as a division of the possible k's into ranges where p is a certain value.

But how?

Alternatively, for each v, we can find the maximum possible p (which is v-1, when k=1). Then, for each p from 1 down to 1, find the k ranges where p is the parent of v.

But this approach may not be efficient.

Alternatively, perhaps we can use the fact that for p=1, the k's are >=v-1. For p=2, the k's are in a certain range, and so on.

Wait, let's take an example. Let's say v=5. Then v-2=3.

For p=3: we need (3-1) = 2. So (3-2)/k = 2 → 3/k = 2 → k=1.5. So k must be >3/3=1 → k>1. So k can be 2 or 3. Because:

For p=3:

k must satisfy (3-2)/3 <k <= (3-2)/(3-1) → 1/3 <k <= 1/2 → but k must be integer >=1, so there's no solution. So p=3 is not possible for any k.

Wait, but this seems conflicting. Let me re-calculate.

Wait, the parent p is ((v-2)//k) +1.

For v=5, v-2=3. For k=1, (3//1) +1=4. So p=4, but p must be <=5-1=4. So p=4.

So for v=5, when k=1, the parent is 4. For k=2, (3//2) =1 → p=2. For k=3, (3//3)=1 → p=2. For k=4, (3//4)=0 → p=1. For k=5, same as k=4. So possible p's are 4, 2, 1.

So the possible p's are 4, 2, 1.

So for each v, the possible p's are the different values of ( (v-2) //k ) +1 for k from 1 to n-1. The number of distinct p's is O(sqrt(v)).

Thus, for each v, we can generate all possible p's by iterating over possible divisors of (v-2) or something similar, but I'm not sure.

Alternative Idea: For a given v, the possible values of (v-2)//k can be found by considering that for k in 1 to sqrt(v-2), the quotient is (v-2)//k. For larger k, the quotient can be found as the floor of (v-2)/k, which may correspond to smaller values. So the number of possible quotients is O(2*sqrt(v-2)), which is O(sqrt(v)).

This is similar to the method used in some divisor problems where you iterate up to sqrt(n) and handle the rest as complements.

So for each v, we can generate all possible quotients q = (v-2)//k for k from 1 to n-1. Each q corresponds to p = q+1.

The quotients q can be found by considering that for k from 1 to sqrt(v-2), q can be up to sqrt(v-2). For k larger than sqrt(v-2), q can be up to sqrt(v-2) as well.

So the approach is:

For each v:

   Initialize a set of possible q's (quotients) and their k ranges.

   For k from 1 to sqrt(v-2):

       compute q = (v-2) //k

       add q to the set.

       also add (v-2) // (q) to the set (for the higher k's that yield the same q).

   Then, for each q in the set, compute the corresponding p = q+1, and find the k ranges where (v-2)//k = q.

But perhaps a better way is to iterate over all possible q's that can be obtained from (v-2)//k.

Alternatively, for each v, we can iterate over all possible q's (the possible values of (v-2)//k) and compute the k ranges for each q.

Let's see: For each possible q, the k's that satisfy q = (v-2) //k.

Which is equivalent to k > (v-2)/(q+1) and k <= (v-2)/q.

But when q is 0, then (v-2) <k, so k > v-2. So q=0 corresponds to k> v-2.

But for q=0, p =1.

So for each possible q (starting from 0 up to (v-2)), compute the k's that result in that q, then compute p = q+1. Then, check if a[v] < a[p], and if so, add the corresponding k's to the answer.

But how to find all possible q's for a given v.

Alternatively, for each v, the possible q's can be found by iterating k from 1 to n-1 and tracking q's. But this is O(n), which is not feasible.

But using the fact that for q in 0 to sqrt(v-2), each q can be obtained from some k >=1, and for q >= sqrt(v-2), the k's are small.

Wait, perhaps the following approach can be used:

For each v, the possible values of q are 0, 1, 2, ..., floor( (v-2) ), but that's not efficient. However, the number of distinct q's for a given v is O(2*sqrt(v-2))).

To find all possible q's and their corresponding k ranges, we can:

1. Iterate k from 1 to sqrt(v-2), and record q = (v-2) //k.

2. For each such q, also consider q1 = (v-2) //k, and then add q1 to the set, but this seems redundant.

Alternatively, we can find all possible q's by considering k up to sqrt(v-2), and for each q obtained from k, we can also compute the other possible q's that come from the division.

Wait, perhaps this is similar to the way we find all divisors. Let's think:

For example, if v-2 is 3, then k can be 1, 2, 3, 4, 5, etc. For k=1, q=3. For k=2, q=1. For k=3, q=1. For k=4, q=0. For k>3, q=0.

So q can be 0,1,3.

Thus, the possible q's are 0,1,3.

The way to find them is:

Iterate k from 1 to sqrt(v-2) (sqrt(3) is ~1.7, so k=1).

q = (v-2) //k =3//1=3.

Then, for this q, the range of k's is [ (v-2)/(q+1)+1, (v-2)/q ] → for q=3, (3)/(3+1) =0.75, so k >=1 (0.75+1 is 1.75, but k must be integer >=1. So k=1.

Then, q=1: when k is in [ (3)/(1+1)+1= 1.5+1=2.5 → k >=3. Or wait, for q=1, the k's are in (3/(1+1), 3/1] → (1.5, 3], so k=2,3.

For q=0: k>3 → k>=4.

So the approach is, for each q in possible q's, compute the k's and add them to the range.

But how to find all possible q's for a given v.

The steps to generate all possible q's for a given v are:

1. Initialize a set S.

2. Add q=0 to S (since when k>v-2, q=0).

3. For k in 1 to sqrt(v-2):

   a. q = (v-2) //k.

   b. add q to S.

   c. q1 = (v-2) // ( (v-2) // (k) )

   d. add q1 to S.

But this seems unclear.

Alternatively, for each v, we can iterate k from 1 to sqrt(v-2) and collect the q's, and also collect q's for the complementary ranges.

But perhaps the following method works:

For each v:

   Initialize a set of q's.

   q_max = v-2

   for k in 1 to int( sqrt(v-2) ) +1:

       q = (v-2) //k

       add q to the set.

       if q !=0:

           q_comp = (v-2) // q

           add q_comp to the set.

   add 0 to the set.

   then, for each q in the set, compute the possible k ranges and see if a[v] < a[p], then add to the answer ranges.

But this might miss some q's. Alternatively, perhaps the following code can generate all possible q's:

But this is getting complicated.

Alternative Idea: For each v, the possible q's (quotients) are all the possible values of (v-2) //k for k >=1, plus q=0. To find all q's:

   q can range from 0 up to v-2.

   for q in 0 to floor( sqrt(v-2) ), add q to the set.

   for each q in 0 to floor( sqrt(v-2) ), compute k = (v-2) // (q+1), which gives the maximum k that would have quotient q.

But I'm not sure.

Alternatively, perhaps for each v, the possible q's are:

q=0, and all possible q's such that q <= sqrt(v-2) or (v-2)/q <= sqrt(v-2).

But I'm getting stuck here.

Let's take a concrete example: v=5 (v-2=3).

Possible k's and q's:

k=1: q=3 → p=4.

k=2: q=1 → p=2.

k=3: q=1 → p=2.

k=4: q=0 → p=1.

k=5: q=0 → p=1.

k=6: q=0 → p=1 (but n is 5, so k can be up to 4 in the first sample input).

So the possible q's are 3,1,0.

The set S would include 0, 3,1.

But how to generate them.

Alternatively, for k from 1 to sqrt(3) ~1.7, so k=1.

q=3//1=3. Add 3 to the set.

Then, for q=3, compute k_max and k_min.

k_min is (3)/(3+1) +1= 0.75 +1=1.75 → k>=2. But for q=3, k must be in (3/(3+1), 3/3] → (0.75, 1], which only includes k=1. So q=3 can be generated by k=1.

Then for q=1:

k=2,3.

Then for q=0: k=4,5,6, etc.

So the possible q's are 3,1,0.

But how to find them.

Another Idea: For each v, generate all possible q's by iterating k from 1 to sqrt(v-2) and also adding the q's from the higher ranges.

The code for this would be:

Initialize a set of q's.

for k in 1 to int( sqrt(v-2) ):

   q = (v-2) //k

   add q to the set.

   q_comp = (v-2) // ( (v-2) //k )

   add q_comp to the set.

Then add 0 to the set.

But this might not capture all possible q's.

Alternatively, perhaps the correct way is to iterate k from 1 to sqrt(v-2), and for each q obtained, add it to the set, then add q_comp = (v-2) // (q +1), but I'm not sure.

Alternatively, perhaps the approach is to iterate over all possible q's where q <= sqrt(v-2), and then the corresponding k ranges.

But I'm stuck.

Let's think differently. For each v, we can find all possible p's (parents) by considering that p can be written as q+1, where q is the quotient (v-2) divided by k.

The possible values of q are the floor divisions of (v-2) by k for k>=1. So q can be any integer from 0 up to v-2.

But for each q, the possible k's that would result in that q are in the interval [ (v-2)/(q+1) +1, (v-2)/q ].

Wait, no. Because q = (v-2) //k → q <= (v-2)/k < q+1 → k >= (v-2)/(q+1) +1 → no, that's not correct.

Wait, for a given q, the k's that satisfy q = (v-2) //k are the k's such that:

q <= (v-2)/k < q+1 → k > (v-2)/(q+1) and k <= (v-2)/q.

But since k is an integer, k can be in the interval ( (v-2)/(q+1), (v-2)/q ].

So the possible k's for a given q are:

k_min = floor( (v-2)/(q+1) ) + 1

k_max = floor( (v-2)/q )

But q can't be 0. For q=0, the condition is k> (v-2)/1 → k> v-2.

So for q=0, k_min = v-1, k_max = n-1.

So for each q, the range of k's is [k_min, k_max], but only if k_min <= k_max.

So for each possible q (including 0), compute k_min and k_max. If k_min >k_max, then this q is not possible.

So the approach is:

For each v:

   For each possible q in 0 to (v-2):

       compute k_min and k_max as:

       if q ==0:

           k_min = v-1

           k_max = n-1

       else:

           k_min = (v-2) // (q+1) +1

           k_max = (v-2) // q

       if k_min >k_max:

           continue

       then, check if k_min <=n-1 and k_max >=1. Adjust the k_min and k_max to be within 1..n-1.

       then, the p is q+1.

       if p is in 1..v-1 and a[v] < a[p]:

           add the interval [k_min, k_max] to the answer.

But how to iterate q.

But iterating q from 0 to v-2 is O(v), which for v up to 2e5 would be 2e5 * 2e5 =4e10 operations. Not feasible.

So this approach is not viable.

Thus, we need a way to iterate over q's that are possible without checking every single q from 0 to v-2.

This brings us back to the initial idea that the number of possible q's for each v is O(sqrt(v)), and thus the per v processing is O(sqrt(v)) time.

To find these q's, we can iterate q from 1 to sqrt(v-2) and also generate the q's from the corresponding k's.

So here's the plan for each v:

1. Generate all possible q's where q can be obtained from k <= sqrt(v-2).

   For each k in 1 to sqrt(v-2):

       q = (v-2) //k

       add q to the set.

   Also, add q_comp where q_comp is (v-2) // ( (v-2) //k )

   This way, we capture the q's from the higher k's.

2. Also add q=0 to handle the case where k>v-2.

3. For each q in the set, compute the k_min and k_max as before, then check if p=q+1 is a valid parent (i.e., p is between 1 and v-1).

   If yes, and if a[v] < a[p], then add 1 to all k's in [k_min, k_max] (adjusted to 1..n-1).

This way, the number of q's per v is O(sqrt(v)), leading to O(n*sqrt(n)) time overall, which is feasible for n=2e5.

Now, the next step is to implement this.

Let's outline the steps:

For each v in 2..n:

   parent is p(v,k) = q +1, where q = (v-2) //k.

   So for each possible q, compute k's range and check if a[v] < a[p].

   Generate all possible q's for this v.

   For each q in the generated set:

       if q+1 > v-1 → p is invalid (since p must be <=v-1). Skip.

       if q+1 <1 → p is invalid. Skip.

       compute k_min and k_max:

           if q ==0:

               k_min = v-1

               k_max = n-1

           else:

               k_min = (v-2) // (q+1) +1

               k_max = (v-2) // q

           if k_min >k_max → skip.

           k_min = max(k_min, 1)

           k_max = min(k_max, n-1)

           if k_min >k_max → skip.

           Now, check if a[v] < a[p], where p = q+1.

           if yes:

               add the interval [k_min, k_max] to the answer.

So, for each v and q, if the conditions are met, increment the answer for all k in [k_min, k_max].

But how to efficiently accumulate these ranges.

The standard approach for such range increments is to use a prefix sum array (difference array). For example:

Initialize an array ans of size n (k can be up to n-1), initialized to 0.

For each interval [l, r], we do ans[l] +=1 and ans[r+1] -=1.

After processing all intervals, compute the prefix sum and the answer for each k is ans[1], ans[2], ... ans[n-1].

This way, we can handle all intervals in O(1) per interval, and then compute the prefix sum in O(n) time.

So the steps are:

Initialize a difference array diff of size n, initialized to 0.

For each v in 2..n:

   Generate all possible q's for this v.

   For each q in the set:

       compute p = q+1.

       if p <1 or p >=v → skip.

       if a[v] >= a[p] → skip.

       compute k_min and k_max as per the above.

       adjust k_min and k_max to be within 1..n-1.

       if k_min >k_max → skip.

       then, diff[k_min] +=1

       if k_max+1 <=n-1:

           diff[k_max+1] -=1

Once all intervals are processed, compute the prefix sum of diff to get the answer array.

Then, output ans[1..n-1].

Now, the key is to generate all possible q's for each v.

So, how to generate the q's.

For a given v:

   s = v-2

   if s <0 → s=0 (but since v>=2, s is >=0).

   Generate all q's for which there exists a k such that q = s//k.

   To generate these q's, iterate k from 1 to sqrt(s), and collect q = s//k and q_comp = s // (s//k).

   Also, add q=0.

But wait, for example, when s=3:

k=1 → q=3 → q_comp =3//3=1 → add 3 and 1.

k=2 → q=1 → q_comp =3//1=3 → add 1 and3.

But then, the set becomes {0,3,1}.

But in the case of s=3, the possible q's are 3,1,0.

So the code would be:

s = v-2

if s ==0:

   then q can only be 0 (since k >=1, s=0 → q=0 for all k). So for v=2, s=0.

   So for v=2:

       q=0, p=1.

       check if a[2] < a[1].

       then, k_min =v-1=1, k_max =n-1.

       So add interval [1, n-1].

But for s=0, the code would generate q=0, which is correct.

So for s=0:

   q=0 → compute k_min =v-1 =1 (since v=2), k_max =n-1.

   p=1.

   if a[2] <a[1], add interval [1, n-1].

So the code can handle this.

Thus, the steps to generate q's for a given v are:

s = v-2

q_set = set()

q_set.add(0)

if s >0:

   sqrt_s = int(s**0.5)

   for k in range(1, sqrt_s +1):

       q = s //k

       q_set.add(q)

       q_comp = s // q if q !=0 else 0

       if q_comp !=0:

           q_set.add(q_comp)

   # Also add the q's from the higher k's.

Thus, this code captures all possible q's.

But for example, when s=3, sqrt_s is 1. So k=1:

   q=3//1=3. Add to set.

   q_comp =3//3=1. Add to set.

So the q_set is {0,3,1}.

Which is correct.

Another example: s=4.

sqrt_s =2.

k=1: q=4//1=4. q_comp=4//4=1. Add 4 and 1.

k=2: q=4//2=2. q_comp=4//2=2. Add 2.

So q_set is {0,4,1,2}.

Which covers all possible q's (0,1,2,4).

Thus, this code seems to capture all possible q's.

Thus, the steps are:

For each v:

   s = v-2

   q_set = {0}

   if s >0:

       sqrt_s = int(s**0.5)

       for k in range(1, sqrt_s +1):

           q = s //k

           q_set.add(q)

           if q !=0:

               q_comp = s //q

               q_set.add(q_comp)

   for q in q_set:

       p = q +1

       if p <1 or p >=v:

           continue

       if a[v-1] >= a[p-1]:

           continue

       # compute k_min and k_max for this q

       if q ==0:

           k_min = v-1

           k_max = n-1

       else:

           k_min = (s) // (q +1) +1

           k_max = (s) // q

       # adjust k_min and k_max

       if k_min >k_max:

           continue

       # now, clamp to [1, n-1]

       k_min = max(k_min, 1)

       k_max = min(k_max, n-1)

       if k_min >k_max:

           continue

       # add to difference array

       diff[k_min] +=1

       if k_max+1 <=n-1:

           diff[k_max+1] -=1

Once all v's are processed, compute the prefix sum of diff, and output the values from 1 to n-1.

Now, let's test this approach against the first sample input.

Sample Input 1:

5

1 5 4 3 2

Sample Output:3 2 1 0

Let's process v=2 (0-based index 1):

s =2-2=0.

q can only be 0.

p=0+1=1.

a[v] is 5, a[p] is 1. 5 >=1 → no contribution.

So no interval added.

v=3 (0-based index 2, a[v]=4):

s=3-2=1.

sqrt(1)=1.

k=1:

q=1//1=1.

add q_comp =1//1=1.

q_set is {0,1}.

For q=0:

p=0+1=1. a[v]=4 <a[0] (1) → false. So no contribution.

For q=1:

p=2.

a[3-1] =4 < a[1] (5) → yes.

Compute k_min and k_max:

q=1.

k_min =1//(1+1) +1 =0+1=1.

k_max =1//1=1.

So interval [1,1].

Add diff[1] +=1.

diff[2] -=1.

For v=3, this adds 1 to k=1.

v=4 (0-based index 3, a[v]=3):

s=4-2=2.

sqrt(2) is 1.

k=1:

q=2//1=2.

q_comp=2//2=1.

q_set is {0,2,1}.

For q=0:

p=1. a[3] =3 <a[0] (1) → no.

q=2:

p=3.

v=4, p must be <4. So p=3 is valid.

a[3] < a[2] (4)? Yes.

Compute k_min and k_max:

q=2.

k_min =2//(2+1) +1=0 +1=1.

k_max=2//2=1.

So interval [1,1]. Add 1 to k=1.

q=1:

p=2.

a[3] =3 <a[1] (5) → yes.

compute k_min and k_max:

q=1.

k_min =2//2 +1=1 +1=2.

k_max=2//1=2.

so interval [2,2].

Add 1 to k=2.

So for v=4, two intervals: [1,1] and [2,2].

v=5 (0-based index 4, a[v]=2):

s=5-2=3.

sqrt(3)=1. So k=1.

q=3//1=3. q_comp=3//3=1.

q_set is {0,3,1}.

Processing each q:

q=0 → p=1. a[v]=2 <a[0]=1 → no.

q=3 → p=4. v=5, p=4 <5. a[v] =2 < a[3] (3) → yes.

k_min =3//(3+1) +1=0 +1=1.

k_max=3//3=1.

Interval [1,1]. Add 1 to k=1.

q=1 → p=2.

a[v]=2 <a[1]=5 → yes.

k_min =3//(1+1) +1=1 +1=2.

k_max=3//1=3.

so k ranges from 2 to3. But n=5, so k_max is 4-1=4. Wait, n=5, so k can be up to4. So k_max=3.

So interval [2,3]. Add 1 to k=2 and 3.

So for v=5, intervals [1,1], [2,3].

So after processing all v's:

diff array:

For k=1:

v=3 adds +1, v=4 adds +1, v=5 adds +1 → total 3.

For k=2:

v=4 adds +1, v=5 adds +1 (from 2-2 and 2-3) → total 2.

For k=3:

v=5 adds +1 (from 3-3) → total 1.

k=4: no intervals.

So the prefix sum would be:

After applying all intervals:

diff[1] = 3 → for k=1.

diff[2] = 2 → k=2.

diff[3] =1 → k=3.

diff[4] =0 → k=4.

Which matches the first sample's output: 3 2 1 0.

Thus, this approach works.

Now, the code can be written as follows.

The code will:

Read n and a array.

Initialize the difference array of size n (since k can be up to n-1).

For each v from 2 to n:

   s = v-2

   generate q_set.

   process each q in q_set.

   compute p, check conditions.

   compute k_min and k_max.

   update the difference array.

Finally, compute the prefix sum and output the results.

Now, let's code this.

Edge cases to consider:

- When s=0 (v=2). Then q=0.

- When p is out of bounds (like when q+1 >=v).

- When k_min exceeds n-1.

Implementing the code:

But in Python, for large n (up to 2e5), we need to use a list of size n, initialized to zero.

But for n=2e5, the difference array would be of size 2e5, which is manageable.

So code:

Read n.

Read the array a.

Initialize diff = [0] * (n)

For v in 2..n:

   s = v-2

   q_set = set()

   q_set.add(0)

   if s >0:

       sqrt_s = int(s ** 0.5)

       for k in range(1, sqrt_s +1):

           q = s //k

           q_set.add(q)

           if q !=0:

               q_comp = s // q

               q_set.add(q_comp)

   for q in q_set:

       p = q +1

       if p <1 or p >=v:

           continue

       if a[v-1] >= a[p-1]:

           continue

       if q ==0:

           k_min = v-1

           k_max = n-1

       else:

           k_min = (s) // (q+1) + 1

           k_max = (s) // q

       if k_min >k_max:

           continue

       k_min = max(k_min, 1)

       k_max = min(k_max, n-1)

       if k_min >k_max:

           continue

       # update the diff array

       diff[k_min] +=1

       if k_max+1 < len(diff):

           diff[k_max+1] -=1

# Compute the prefix sum

ans = []

current =0

for k in range(1, n):

   current += diff[k]

   ans.append(str(current))

print(' '.join(ans))

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    diff = [0] * (n + 2)  # To handle up to k_max+1

    for v in range(2, n + 1):
        s = v - 2
        q_set = {0}
        if s > 0:
            sqrt_s = int(s**0.5)
            for k in range(1, sqrt_s + 1):
                q = s // k
                q_set.add(q)
                if q != 0:
                    q_comp = s // q
                    q_set.add(q_comp)
        for q in q_set:
            p = q + 1
            if p < 1 or p >= v:
                continue
            if a[v-1] >= a[p-1]:
                continue
            if q == 0:
                k_min = v - 1
                k_max = n - 1
            else:
                k_min = (s // (q + 1)) + 1
                k_max = s // q
            if k_min > k_max:
                continue
            k_min = max(k_min, 1)
            k_max = min(k_max, n - 1)
            if k_min > k_max:
                continue
            diff[k_min] += 1
            if k_max + 1 <= n - 1:
                diff[k_max + 1] -= 1

    current = 0
    result = []
    for k in range(1, n):
        current += diff[k]
        result.append(str(current))

    print(' '.join(result), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
2 2 2 2 2 2
""",
            "output": \
"""\
0 0 0 0 0
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

Another test case:

Sample Input 2:

6

2 2 2 2 2 2

The output is 0 0 0 0 0.

Because for all v and p, a[v] == a[p], so no increments.

Thus, the code should handle this.

Now, for performance.

For n=2e5, each v would generate O(sqrt(v)) q's. For v=2e5, sqrt(v) is about 447. So per v, 447 iterations. For 2e5 v's, that's 2e5 * 447 = 8.94e7 operations. Which is acceptable for Python.

The prefix sum computation is O(n), which is acceptable.

Memory: The diff array is O(n), which is 2e5 elements, manageable.

Thus, this code should work.
</think>

```python
n = int(input())
a = list(map(int, input().split()))

diff = [0] * (n + 2)  # To handle up to k_max+1

for v in range(2, n + 1):
    s = v - 2
    q_set = {0}
    if s > 0:
        sqrt_s = int(s**0.5)
        for k in range(1, sqrt_s + 1):
            q = s // k
            q_set.add(q)
            if q != 0:
                q_comp = s // q
                q_set.add(q_comp)
    for q in q_set:
        p = q + 1
        if p < 1 or p >= v:
            continue
        if a[v-1] >= a[p-1]:
            continue
        if q == 0:
            k_min = v - 1
            k_max = n - 1
        else:
            k_min = (s // (q + 1)) + 1
            k_max = s // q
        if k_min > k_max:
            continue
        k_min = max(k_min, 1)
        k_max = min(k_max, n - 1)
        if k_min > k_max:
            continue
        diff[k_min] += 1
        if k_max + 1 <= n - 1:
            diff[k_max + 1] -= 1

current = 0
result = []
for k in range(1, n):
    current += diff[k]
    result.append(str(current))

print(' '.join(result))
```
