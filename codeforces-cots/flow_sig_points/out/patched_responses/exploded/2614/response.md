<think>
Okay, let's tackle this problem. So, the task is to compute the expected number of inversions in a permutation where some elements are replaced by -1, and we have to fill those -1s with the remaining numbers to form a valid permutation. The answer needs to be modulo 998244353 in the form P * Q^{-1} mod MOD.

Hmm. Let's start by breaking down the problem. The expected value is the average of the number of inversions over all possible valid permutations. But calculating this directly is impossible for large n since the number of permutations could be huge. So, we need a smarter approach.

Inversion counting can be decomposed into contributions from each pair of elements. The expectation is linear, so the expected total number of inversions is the sum of the expected contributions from each possible pair (i, j) where i < j. Wait, wait. Wait, inversion is i > j and a_i < a_j. So, for each pair (i, j) where i > j, we need to compute the probability that a_i < a_j in the permutation. Then sum all those probabilities.

So the key is to compute for each pair (i, j) where i > j, the probability that in the permutation, the element at position i is less than the element at position j. Then sum all those probabilities.

So the problem reduces to calculating, for each such pair, the probability that a_i < a_j.

Now, the pairs can be of different types depending on whether the elements are fixed (non -1) or unknown (-1). So for each pair (i, j), there are several cases:

Case 1: Both p_i and p_j are known (not -1). Then, we can directly check if p_i < p_j. If i > j, then this contributes 1 to the sum if p_i < p_j, else 0. Otherwise, since i < j, it's not an inversion. Wait no, because in the pair (i, j) where i > j, we check if a_i < a_j. So in this case, both positions are known. So if i > j and p_i (the known value) is less than p_j (also known), then this pair contributes 1 to the inversion count. Otherwise, 0. So for such pairs, their contribution is fixed and can be added directly.

Case 2: One of p_i or p_j is known, the other is unknown. For example, p_i is known (x), and p_j is unknown. So we need to find the probability that when the unknown is filled in, the value at j (call it y) is such that if i > j, then x < y (since in that case, (i,j) is an inversion if x < y). Wait, no. Wait, in the pair (i, j), i is larger than j. So if i > j, then in the permutation, if a_i < a_j, that's an inversion. So for the pair (i, j) where i > j, the probability that a_i < a_j is what we need.

So suppose i > j, and in positions i and j:

Subcase 1: Both known. As before.

Subcase 2: i is known (x) and j is unknown (y). So y is a missing value. The unknown values are the ones not present in the known elements. Let's say there are k unknowns in total. Then, the possible values for y are the ones not in the known set. But when j is filled, y is chosen uniformly from the remaining possible numbers. So, given that x is fixed, the probability that y is greater than x (because for inversion, a_i < a_j, which is x < y since a_i is x and a_j is y) would depend on how many numbers are missing and greater than x.

But wait, this depends on the available numbers. Suppose the known elements are a set S. The missing elements (unknowns) are M, which are the numbers from 1 to n not in S. Let m be the size of M. Then, when choosing y (for position j, which is unknown), y must be one of the m elements. Since all permutations of the unknowns are equally likely, the probability that y is greater than x is the number of elements in M that are greater than x divided by m.

But wait, but in this case, the position j is part of the unknowns. So the unknowns are filled in the positions that were -1. For each unknown position, the value is a permutation of the missing elements.

So when considering a pair where j is unknown (and i is known, and i > j), the value of j is a variable from the missing elements. So, the probability that y (the value at j) is greater than x (the value at i) is equal to the number of elements in M greater than x divided by m.

But wait, m is the number of missing elements. Let's say, the missing elements are M. Then for each such pair (i, j), where i is known as x, j is unknown, and i > j. Then the probability that a_i < a_j is (number of elements in M that are > x) / m.

Similarly, if i is unknown and j is known (x), then for the pair (i, j) where i > j, the probability that a_i < x is (number of elements in M that are < x) / m, because a_i is part of M. So in this case, the contribution is (count) / m.

Subcase 3: Both positions are unknown. So both a_i and a_j are part of the missing elements. Let the size of M be m. Then, since all permutations are possible, the probability that in the filled permutation, the value at i is less than the value at j (given that i > j) is equal to the probability that two distinct elements in M are in a certain order. For a pair of distinct elements, the probability that the one at i is less than the one at j is 0.5. Because for any two distinct elements, exactly one of the two possible orderings between them will form an inversion (i > j implies that if a_i < a_j, it's an inversion). So, for the pair of positions i and j (i > j) where both are unknown, the expected contribution is 0.5 multiplied by the number of possible pairs of elements in M. Wait, no. Wait, when both positions are filled with values from M, which is a permutation. So for all possible permutations of M, when considering the pair (i, j) where i > j, the probability that a_i < a_j is equal to the number of pairs (x, y) in M where x < y divided by the total number of possible pairs (m choose 2), multiplied by the number of permutations where those x and y are placed at positions i and j.

Wait, perhaps a better approach is to note that when both are in M, the order of the elements in the permutation is random. So for any two positions i and j, with i > j (so inversion is possible), the probability that a_i < a_j is equal to the probability that in the permutation of the unknown elements, the element at position i is less than the element at position j. But since the unknown elements are arranged uniformly at random, the probability for each pair is 1/2. Because for any two distinct elements, exactly half of the permutations will have the larger element in the earlier position (since there are two possible orderings, each equally likely). So for a pair (i, j) where i > j and both are unknown, the contribution to the expectation is 0.5 * 1 (since inversion is counted once if a_i < a_j) → 0.5.

So the total expected inversions can be broken down into three parts:

1. Inversions between known elements.
2. Inversions between a known and an unknown element.
3. Inversions between two unknown elements.

Let me structure this.

First, compute the number of known elements. Let's collect all the known elements in a set S. The unknown elements (M) are the ones not in S. Let m be the size of M. Also, collect the positions where the elements are known (fixed) and unknown (unknown_positions).

Now, for each possible pair (i, j) where i > j:

Case 1: Both i and j are known. Then, check if p_i < p_j. If yes, add 1 to the answer.

Case 2: One is known (x), the other is unknown. Let's say i is known (x), j is unknown. Then, the contribution is the probability that the unknown element (y) at j is greater than x. Since j is filled with a value from M, the probability is (number of elements in M that are > x) / m. Similarly, if j is known and i is unknown, then the contribution is (number of elements in M that are less than x) / m. But wait, in this case, i > j, so a_i is unknown. So the pair (i, j) contributes if a_i < a_j, which is a_j is known (x), and a_i is in M. So for a_i (unknown) to be less than x, the number of elements in M less than x divided by m.

Case 3: Both are unknown. Then, the contribution is 0.5.

So, the plan is:

- Precompute all the known elements and their positions, and the missing elements (M) and their count m.

Compute the sum for each possible pair (i, j) where i > j.

But for n up to 2e5, considering all possible O(n^2) pairs is impossible. So we need to find a way to calculate each case efficiently, without iterating all O(n^2) pairs.

Wait, but for m up to 2e5, this could be O(n^2), which is 4e10 operations. That's way too slow. So we need a smarter approach.

Let's think about each case:

Case 1: Both known. For each pair (i, j) where i > j, and both are known, check if p_i < p_j. Sum all such occurrences. How to compute this efficiently?

This is the standard problem of counting inversions in an array. But here, the array is the known elements. So, for the known elements, we can compute the number of inversions in O(k log k) time, where k is the number of known elements. For example, using a Fenwick tree or a Binary Indexed Tree (BIT) by processing the elements in reverse order and counting the number of elements already added that are smaller than the current element.

Yes. So that's manageable. But if the known elements are not in a contiguous part of the array, we need to process all pairs (i, j) where i > j and both are known. So the inversion count for the known elements is exactly the contribution from Case 1.

Case 2: One known and one unknown. Let's split this into two subcases:

Subcase 2a: i is known, j is unknown (i > j). We need to count the number of pairs (i, j) where i is known, j is unknown, i > j, and then for each such pair, add (number of M elements > p_i) / m.

Subcase 2b: j is known, i is unknown (i > j). For these pairs, we need to add (number of M elements < p_j) / m.

But how to compute the number of such pairs in Subcases 2a and 2b efficiently?

Wait, for Subcase 2a:

We need to count for each known position i (with value x), the number of unknown positions j that are less than i (since i > j). For each such j, the contribution is (cnt_gt_x) / m, where cnt_gt_x is the number of elements in M greater than x.

So the total contribution for Subcase 2a is (sum over all known i) [ (number of unknown j < i) * cnt_gt_x / m ].

Similarly, for Subcase 2b: for each known j (with value y), the number of unknown positions i that are greater than j (since i > j) multiplied by cnt_lt_y (number of elements in M less than y) divided by m.

So for Subcase 2a:

sum_2a = sum (for each known i) [ (number of unknown positions j < i) * (count of M elements > p_i) ) ] / m.

For Subcase 2b:

sum_2b = sum (for each known j) [ (number of unknown positions i > j) * (count of M elements < p_j) ) ] / m.

Then sum_2 = (sum_2a + sum_2b) / m.

Case 3: Both positions are unknown. For all pairs (i, j) where i > j and both are unknown. For each such pair, the contribution is 0.5. So the total contribution is 0.5 * (k choose 2), where k is the number of unknown positions.

Wait, no. Because the number of unknown positions is, say, u. Then the number of pairs (i, j) where i > j and both are unknown is C(u, 2) = u*(u-1)/2. Each contributes 0.5. So the total is 0.5 * u*(u-1)/2 = u*(u-1)/4.

Wait, 0.5 * (u choose 2) → (u*(u-1)/2) * 0.5 = u*(u-1)/4. Yes.

So for Case 3, the contribution is (u * (u-1) ) // 4, but since it's modulo 998244353 and division is involved, we need to compute it as (u*(u-1) // 2 ) * inv(2) mod MOD.

So putting all together, the total expected inversion count is:

total = (case1) + (sum_2a + sum_2b)/m + (u*(u-1)/2) * 0.5

But we need to handle all divisions modulo 998244353. So all divisions are done via multiplication by the modular inverse.

So the steps are:

1. Preprocess the known elements and the missing elements M.

   - Collect all known elements into a list, and check for duplicates (though the problem statement says that all non -1 elements are distinct, so S is a set of unique elements).
   - Compute m = n - len(S) → the number of unknown elements.
   - Compute M as the sorted list of missing elements (1 to n not in S).

2. Compute case1: the number of inversions among known elements. This can be done using a Fenwick Tree. For each element in the known array (processed in order from first to last), but perhaps we need to process in reverse order (since inversion is i > j). Wait, the standard approach is to process elements from the end and count the number of elements already in the BIT that are smaller than the current element. Let's see.

   For known elements, arrange them in their original positions. Wait, but the problem requires that the known elements are fixed in their positions, so the inversion count among them is the number of pairs (i, j) in the original array where i > j and p_i < p_j, and both are known. So the inversion count for the known elements is exactly the standard inversion count for the array formed by the known elements, considering their positions. Wait, no. Because the known elements are not contiguous. For example, if the array is [3, -1, -1], the known elements are at position 1 (3). So their inversion count is 0. But in the first example, the inversion count between known elements is zero, since there's only one.

   So to compute case1, we need to process the known elements in the order of their positions. For each known element, when processing from left to right (i increasing), we can use a Fenwick tree to count how many elements in the already processed elements (which are to the left of the current element) are greater than the current element. Because for each such element, since the current element is at a higher position, if the current element is smaller than an element to the left, then (current position, left position) is an inversion (i > j and a_i < a_j). Wait, no. For example, consider two known elements at positions j and i (i > j). The pair (i, j) is in inversion if a_i < a_j. So, when processing elements from left to right (j increases), for each element a_j, the number of elements to the left (i < j) that are greater than a_j is the number of inversions contributed by a_j. So the standard inversion count can be computed by initializing a Fenwick Tree and for each a_j in the array, add the number of elements in the Fenwick Tree that are greater than a_j (since those elements are to the left and would form an inversion with a_j). So the Fenwick Tree can be used by inserting elements in the order of the array and querying the sum of elements greater than a_j.

   Alternatively, we can process the elements in the order of their positions (as per the original array) and use a Fenwick Tree that tracks the presence of elements. For each position i (in order from 0 to n-1), if the element is known, we add its value to the Fenwick Tree. Then, for each known element, the number of elements already in the tree (to the left, i.e., positions j < i) that are greater than the current element's value is the number of inversions added by this element. Summing this over all known elements gives the case1 contribution.

   So to compute case1, the steps are:

   a. Iterate through the original array in order (from left to right, position 1 to n).

   b. For each position i, if p[i] is known (not -1), add to the Fenwick Tree the value p[i], and query the Fenwick Tree for the number of elements greater than p[i] that are already present (since those elements are in positions j < i, and thus i > j, and p[i] < p[j] would contribute to an inversion).

   But how to query the number of elements greater than x in the Fenwick Tree?

   The Fenwick Tree can be used to track the count of elements. For this, since the values can be up to n (2e5), we can coordinate compress the known elements. Wait, but the known elements are all distinct. So the values of known elements are unique and in the range [1, n]. So the maximum possible value is n.

   So the Fenwick Tree can be built for size n. When inserting a value x, we can insert at position x. The number of elements greater than x is the sum from x+1 to n.

   So the Fenwick Tree can be implemented to support:

   - update: add 1 to position x.

   - query: sum from x+1 to n.

   So for each known element x, when inserted into the Fenwick Tree, the query gives the number of elements already in the tree that are greater than x. These are the elements to the left (since we process left to right) that form inversions with x. Summing all these gives case1.

   Yes.

3. Compute case2a and case2b.

   For case2a: sum over known elements x at position i, the number of unknown positions j < i multiplied by the number of elements in M greater than x. Then divide by m.

   For case2b: sum over known elements y at position j, the number of unknown positions i > j multiplied by the number of elements in M less than y. Then divide by m.

   So how to compute these efficiently?

   Let's first precompute for all possible x, the count of elements in M greater than x (cnt_gt) and less than x (cnt_lt).

   Since M is a sorted list, for a given x, cnt_gt can be found using binary search. For example, cnt_gt = len(M) - bisect_right(M, x).

   Similarly, cnt_lt is bisect_left(M, x).

   So for each known element x, we can compute cnt_gt and cnt_lt in O(log m) time.

   So for case2a:

   For each known element x at position i, the number of unknown positions j < i is the number of unknown elements in the positions from 1 to i-1 (assuming 1-based indices). Wait, positions are 0-based or 1-based? The problem says the array is p_1, p_2, ..., p_n, so 1-based.

   So for each known element at position i (1-based), the number of unknown positions j < i is the number of -1s in positions 1 to i-1.

   Similarly, for case2b, for each known element at position j, the number of unknown positions i > j is the number of -1s in positions j+1 to n.

   So, the problem reduces to, for each position in the array, knowing how many unknown positions are before it (for case2a) and after it (for case2b).

   So, we can precompute a prefix array of the number of unknowns up to each position.

   Let's create a prefix array pre, where pre[i] is the number of -1s in positions 1 to i (assuming 1-based). Then, the number of unknowns before i is pre[i-1]. The total number of unknowns is pre[n].

   Similarly, the suffix array can be created, but perhaps using the prefix array. The number of unknowns after position j is (pre[n] - pre[j]).

   So for each known element at position i:

   case2a contribution += (pre[i-1]) * cnt_gt_x

   for case2b contribution += (pre[n] - pre[j]) * cnt_lt_y (where j is the position of known element y)

   So, first, compute the prefix array.

   pre[0] = 0.

   For each position from 1 to n:

   pre[i] = pre[i-1] + (1 if p[i-1] == -1 else 0) (since in Python, list is 0-based, so p is stored as 0-based, but the positions are 1-based in the problem description).

   Wait, in code, the input is given as p_1 to p_n, which in Python would be stored as p[0] to p[n-1]. So for the prefix array pre, which is 1-based (pre[0] = 0, pre[1] is count of -1 in first position, etc.), pre[i] is the number of -1s in the first i positions (1-based).

   So, for a known element at position i (1-based), the number of unknowns before it is pre[i-1] (since pre[i-1] is the sum up to i-1 positions). The number of unknowns after position j (1-based) is pre[n] - pre[j], since pre[j] is the number of unknowns up to j, and pre[n] is the total. So the remaining is (pre[n] - pre[j]).

   So once the prefix array is precomputed, for each known element at position i:

   case2a += pre[i-1] * cnt_gt_x

   for each known element at position j:

   case2b += (pre[n] - pre[j]) * cnt_lt_y

   Then, sum_2 = (case2a + case2b) / m, where m is the number of unknowns (pre[n]).

   But m can be zero, but in that case, there are no unknowns, so case2a and case2b would be zero.

4. Compute case3: the contribution from pairs of unknowns. This is (u choose 2) * 0.5, where u is the number of unknowns (pre[n]).

   So u = pre[n]. If u < 2, then case3 is 0. Otherwise, it's (u*(u-1)/2) * 0.5 = u*(u-1)/4.

   So in code, this is (u * (u-1) // 2) * inv(2) mod MOD. But since we're using modular inverses, it's (u * (u-1) % MOD) * inv(2) % MOD * inv(2) % MOD ?

   Wait, no. Because 0.5 is equivalent to inv(2) mod MOD. So (u choose 2) * 0.5 is (u*(u-1)//2) * inv(2). But since we can't do integer division here in the modulus world, we need to compute (u*(u-1) mod MOD) * inv(2) mod MOD, then multiply by inv(2) again. Wait, no:

   Let me re-express:

   case3 = (u * (u-1) / 2 ) * (1/2 )

   So that's u*(u-1) /4.

   So in modular arithmetic, this is equal to (u*(u-1) mod MOD) * inv(4) mod MOD.

   Since inv(4) is inv(2) * inv(2) mod MOD. So inv(2) is 499122177 mod 998244353. So inv(4) is (inv(2) * inv(2)) mod MOD.

   So in code, case3 = (u * (u-1) % MOD) * inv(4) % MOD.

   Alternatively, compute (u*(u-1) // 2) * inv(2) mod MOD. Wait, but u can be up to 2e5, so u*(u-1) can be up to 4e10, which is manageable modulo 998244353. So (u * (u-1) ) % MOD * inv(2) % MOD * inv(2) % MOD.

   Because:

   case3 = [ (u*(u-1) // 2 ) * 1/2 ] mod MOD.

   But (u*(u-1) // 2 ) is (u*(u-1) ) * inv(2) mod MOD.

   Then multiplying by 1/2 again gives (u*(u-1) ) * inv(2)^2 mod MOD.

   So yes.

Putting it all together:

The steps are:

1. Read n and the array p (0-based in code).

2. Compute the set of known elements S.

3. Check that all elements in S are unique. (Problem statement says so.)

4. Compute the list M of missing elements (those not in S). Sort M.

5. Compute m = len(M).

6. Compute case1: inversions among known elements.

   - Initialize Fenwick Tree.

   - Initialize case1 = 0.

   - For each i from 0 to n-1:

       if p[i] != -1:

           x = p[i]

           # query the Fenwick Tree for the number of elements > x.

           # the Fenwick Tree contains all known elements processed so far (to the left).

           # since we process left to right, the Fenwick Tree has elements from positions 0 to i-1.

           cnt = fenwick.query(x + 1, n)

           case1 += cnt

           # add x to the Fenwick Tree.

           fenwick.update(x, 1)

7. Compute the prefix array pre.

   pre is 0-based (pre[0] is 0, pre[i] is number of -1 in p[0..i-1] (since in code, p is 0-based).

   So:

   pre = [0] * (n+1)

   for i in range(1, n+1):

       pre[i] = pre[i-1] + (1 if p[i-1] == -1 else 0)

   So pre[i] is the number of -1 in the first i elements (1-based). So for position j (1-based), pre[j] is the count up to j. So for a known element at position j (1-based, which is p[j-1] in code), the number of unknowns before it is pre[j-1] (since pre[j-1] is the number of -1 in the first j-1 elements, which are the positions before j).

8. Compute case2a and case2b.

   For each known element x at position i (1-based), which is p[i-1] in code:

   a. The number of unknowns before i is pre[i-1].

   b. cnt_gt = len(M) - bisect.bisect_right(M, x)

   case2a += pre[i-1] * cnt_gt

   For case2b:

   For each known element y at position j (1-based):

   a. The number of unknowns after j is pre[n] - pre[j]

   b. cnt_lt = bisect.bisect_left(M, y)

   case2b += (pre[n] - pre[j]) * cnt_lt

   So sum_2 = (case2a + case2b) * inv(m) mod MOD.

   But m could be zero. So when m is zero, sum_2 is zero.

9. Compute case3:

   u = pre[n]

   if u >= 2:

       case3 = (u * (u - 1) ) % MOD

       case3 = case3 * inv(2) % MOD

       case3 = case3 * inv(2) % MOD

   else:

       case3 = 0

   Because (u choose 2) * 0.5 = (u*(u-1)/2) * 0.5 = u*(u-1)/4.

10. Sum all cases:

   total = (case1 + sum_2 + case3) mod MOD

11. Output total.

But we need to handle modular inverses for m and for case3.

Wait, for sum_2, the sum_2a and sum_2b are summed, and then divided by m. So sum_2 = (case2a + case2b) / m. But in modular terms, this is (case2a + case2b) * inv(m) mod MOD.

But m can be zero, but in that case, there are no unknowns, so case2a and case2b would be zero. So sum_2 would be zero.

But when m is zero, the code must avoid division by zero. However, when m is zero, the unknowns are zero, so case2a and case2b must be zero. So in code, when m is zero, sum_2 is zero.

So in code:

sum_2 = (case2a + case2b) * inv(m) % MOD if m != 0 else 0

But how to compute inv(m) when m is zero? But in code, m is zero only when there are no unknowns, and case2a and case2b are zero, so sum_2 is zero regardless.

So in code, we can compute sum_2 as:

if m == 0:

   sum_2 = 0

else:

   sum_2 = (case2a + case2b) * inv(m) % MOD

So, the code can handle this.

But wait, case2a and case2b can be large, but when m is zero, those terms are zero.

So, steps in code:

- Precompute inv for 2, 4, and possibly others. Or compute inv on the fly using pow(x, MOD-2, MOD).

MOD = 998244353

inv2 = pow(2, MOD-2, MOD)

inv4 = pow(4, MOD-2, MOD)

But for each division, we can compute inv(x) as pow(x, MOD-2, MOD).

So, sum_2 = (case2a + case2b) * pow(m, MOD-2, MOD) % MOD if m !=0 else 0.

Now, the problem is to implement all of this efficiently.

Now, let's think about the Fenwick Tree for case1.

Implementing a Fenwick Tree that can query the sum of elements greater than x.

The Fenwick Tree will track the count of each x. So when inserting x, we update the tree at x by 1. Then, to query the sum of elements greater than x, we compute the prefix sum from x+1 to max_val (n). So the Fenwick Tree should support:

- update(x, delta): add delta to the count at x.

- query_gt(x): sum from x+1 to n.

So the standard Fenwick Tree can be implemented with 1-based indexing, and the query_gt can be computed as query_gt(x) = get_sum(n) - get_sum(x).

Where get_sum(k) returns the sum from 1 to k.

So, for example, if x is 3, the sum of elements greater than x is sum(4..n) = total_sum - sum(1..3).

But the Fenwick Tree can be initialized with size n. For x in [1..n], the Fenwick Tree's get_sum(x) returns the sum of elements up to x.

So for query_gt(x):

sum_gt = get_sum(n) - get_sum(x)

But in code, the Fenwick Tree's get_sum is up to x.

Yes.

Thus, the Fenwick Tree code can be as follows:

class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)
    
    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx
    
    def get_sum(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res
    
    def query_gt(self, x):
        return self.get_sum(self.n) - self.get_sum(x)

So, for a known element x, when inserted into the Fenwick Tree, the query_gt(x) gives the count of elements already in the tree that are > x. Which is exactly the number of inversions contributed by this element with the elements to the left.

Now, considering that the Fenwick Tree is built for up to n elements (since the maximum possible value of a known element is n), and since all known elements are unique, the Fenwick Tree will have 0 or 1 in each position.

Now, putting this all together.

The code steps:

Read n.

Read the array p as a list of integers.

Collect the known elements S = [x for x in p if x != -1]

Check that all elements in S are unique. (The problem statement says so, so no need.)

Compute m = n - len(S)

Compute the missing elements M = sorted list of numbers in 1..n not present in S.

Compute case1 using Fenwick Tree.

Compute the prefix array pre.

Compute case2a and case2b:

case2a = 0

case2b = 0

For each i in range(n):

    if p[i] == -1:

        continue

    x = p[i]

    pos = i + 1  # 1-based

    unknowns_before = pre[pos - 1]  # pre[pos-1] is the number of unknowns before pos.

    # cnt_gt is the number of elements in M greater than x.

    cnt_gt = len(M) - bisect.bisect_right(M, x)

    case2a += unknowns_before * cnt_gt

    # case2b: for this element at position pos, the unknowns after are pre[n] - pre[pos]

    unknowns_after = pre[n] - pre[pos]

    cnt_lt = bisect.bisect_left(M, x)

    case2b += unknowns_after * cnt_lt

sum_2 = 0

if m != 0:

    sum_2 = (case2a + case2b) * pow(m, MOD-2, MOD) % MOD

u = pre[n]

case3 = 0

if u >= 2:

    term = u * (u - 1) % MOD

    term = term * pow(2, MOD-2, MOD) % MOD  # divided by 2 (since 0.5 is 1/2)

    term = term * pow(2, MOD-2, MOD) % MOD  # divided by another 2 (since 0.5 is 1/2)

    case3 = term

else:

    case3 = 0

total = (case1 + sum_2 + case3) % MOD

print(total)

But wait, case1 is computed as the sum of the counts from the Fenwick Tree, which is the actual number of inversions in the known elements. Since the answer expects modulo 998244353, case1 should be modded at each step.

But case1 can be up to O(k^2), which for k up to 2e5 is 4e10, which is bigger than MOD. So during computation of case1, we should mod the values.

Thus, in the code:

Initialize case1 = 0.

Each time case1 += cnt, then case1 %= MOD.

Similarly for case2a and case2b, since they can be up to 2e5 * 2e5 (each term can be 2e5 * 2e5 → 4e10, which is modded when added.

So, in code:

case1 = 0

for each known element:

    cnt = fenwick.query_gt(x)

    case1 = (case1 + cnt) % MOD

Similarly, for case2a and case2b:

case2a = (case2a + ...) % MOD

case2b = (case2b + ...) % MOD

But since these variables can be large, we need to take mod at each step, or accumulate the sum and then mod once. But for Python's integers, even 2e5 * 2e5 is manageable as an integer, but when multiplied by another 2e5, it can be 8e15, which is way larger than MOD. So to prevent overflow (though Python handles big integers), we can mod after each addition.

So, during the computation of case2a and case2b:

for each known element:

    ...

    case2a += unknowns_before * cnt_gt

    case2a %= MOD

    ...

    case2b += unknowns_after * cnt_lt

    case2b %= MOD

This is better.

Similarly, case3 is computed using u * (u-1) mod MOD.

Putting all together.

Now, let's test this approach with the examples.

First example:

Input:

3

3 -1 -1

So the array is [3, -1, -1]

Known elements are [3], M is [1, 2], m=2.

case1: known elements are [3]. Since only one element, no inversions. case1=0.

prefix array pre:

pre[0] =0

pre[1] =0 (since p[0] is 3, not -1)

pre[2] =1 (p[1] is -1)

pre[3] =2 (p[2] is -1)

case2a: for the known element at position 1 (1-based), unknowns_before is pre[0] =0. cnt_gt for 3 is len(M) - bisect_right([1,2], 3) → 2 - 2 = 0. So case2a +=0.

case2b: for the known element at position 1, unknowns_after is pre[3] - pre[1] = 2-0=2. cnt_lt is bisect_left([1,2],3) → 2. So 2 * 2 =4. case2b=4.

sum_2 = (0+4)/2 → 4/2=2. sum_2=2.

case3: u=2 → 2*1=2 → 2 * inv(2) * inv(2) → 2 * 499122177 * 499122177 mod MOD.

But 2 * (1/2)^2 = 2 * 1/4 = 0.5 → 499122177 mod MOD (since MOD is 998244353, 0.5 mod is 499122177).

So case3=499122177.

So total = 0 + 2 + 499122177 mod MOD.

But 2 + 499122177 = 499122179 mod MOD. Which matches the first example's output.

Yes.

Second example:

Input:

2

1 2 → known elements. m=0.

case1: check inversion between 1 and 2. Since 1 is at position 1 (1-based), 2 is at position 2. No inversion. case1=0.

sum_2 is 0 (m=0).

case3: u=0 → 0.

Total is 0.

Third example:

Input:

2

-1 -1 → known elements empty. m=2. M is [1,2].

case1: 0.

case2a and case2b: 0 (no known elements).

case3: u=2. 2*1=2. 2 * inv(2) * inv(2) → 2 * 499122177^2 → 2 * ( (1/2)^2 ) → 0.5 → which is 499122177 mod MOD. Which is the third example's output.

Yes.

So the code should handle these cases.

Now, let's code this.

But first, handle the Fenwick Tree. Let's make sure that the Fenwick Tree's size is n.

Wait, but the known elements can have values up to n. So the Fenwick Tree needs to handle up to n.

But for n up to 2e5, this is manageable.

Now, the code:

We need to read the input, process the known elements, compute M, then compute the cases.

Implementing bisect for M.

So code:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    MOD = 998244353

    class FenwickTree:
        def __init__(self, size):
            self.n = size
            self.tree = [0] * (self.n + 2)  # 1-based indexing
        
        def update(self, idx, delta):
            while idx <= self.n:
                self.tree[idx] += delta
                idx += idx & -idx
        
        def get_sum(self, idx):
            res = 0
            while idx > 0:
                res += self.tree[idx]
                idx -= idx & -idx
            return res
        
        def query_gt(self, x):
            return self.get_sum(self.n) - self.get_sum(x)

    n = int(input_stream.readline().rstrip("\n"))
    p = list(map(int, input_stream.readline().rstrip("\n").split()))

    known = [x for x in p if x != -1]
    m = n - len(known)
    M = []
    if m > 0:
        s = set(known)
        for x in range(1, n+1):
            if x not in s:
                M.append(x)
        M.sort()

    # Compute case1
    case1 = 0
    fen = FenwickTree(n)
    for x in p:
        if x == -1:
            continue
        cnt = fen.query_gt(x)
        case1 = (case1 + cnt) % MOD
        fen.update(x, 1)

    # Compute prefix array pre
    pre = [0] * (n + 1)
    for i in range(1, n+1):
        pre[i] = pre[i-1] + (1 if p[i-1] == -1 else 0)

    # Compute case2a and case2b
    case2a = 0
    case2b = 0
    for i in range(n):
        if p[i] == -1:
            continue
        x = p[i]
        pos = i + 1  # 1-based
        # case2a
        unknowns_before = pre[pos -1]
        cnt_gt = len(M) - bisect.bisect_right(M, x) if m else 0
        case2a = (case2a + unknowns_before * cnt_gt) % MOD
        # case2b
        unknowns_after = pre[n] - pre[pos]
        cnt_lt = bisect.bisect_left(M, x) if m else 0
        case2b = (case2b + unknowns_after * cnt_lt) % MOD

    sum_2 = 0
    if m != 0:
        sum_2 = (case2a + case2b) * pow(m, MOD-2, MOD) % MOD

    # Compute case3
    u = pre[n]
    case3 = 0
    if u >= 2:
        term = u * (u -1) % MOD
        inv2 = pow(2, MOD-2, MOD)
        case3 = term * inv2 % MOD
        case3 = case3 * inv2 % MOD

    total = (case1 + sum_2 + case3) % MOD
    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
1 2
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

Testing against sample input 2.

```python
import bisect


def main(input_stream, output_stream):
    MOD = 998244353

    class FenwickTree:
        def __init__(self, size):
            self.n = size
            self.tree = [0] * (self.n + 2)  # 1-based indexing
        
        def update(self, idx, delta):
            while idx <= self.n:
                self.tree[idx] += delta
                idx += idx & -idx
        
        def get_sum(self, idx):
            res = 0
            while idx > 0:
                res += self.tree[idx]
                idx -= idx & -idx
            return res
        
        def query_gt(self, x):
            return self.get_sum(self.n) - self.get_sum(x)

    n = int(input_stream.readline().rstrip("\n"))
    p = list(map(int, input_stream.readline().rstrip("\n").split()))

    known = [x for x in p if x != -1]
    m = n - len(known)
    M = []
    if m > 0:
        s = set(known)
        for x in range(1, n+1):
            if x not in s:
                M.append(x)
        M.sort()

    # Compute case1
    case1 = 0
    fen = FenwickTree(n)
    for x in p:
        if x == -1:
            continue
        cnt = fen.query_gt(x)
        case1 = (case1 + cnt) % MOD
        fen.update(x, 1)

    # Compute prefix array pre
    pre = [0] * (n + 1)
    for i in range(1, n+1):
        pre[i] = pre[i-1] + (1 if p[i-1] == -1 else 0)

    # Compute case2a and case2b
    case2a = 0
    case2b = 0
    for i in range(n):
        if p[i] == -1:
            continue
        x = p[i]
        pos = i + 1  # 1-based
        # case2a
        unknowns_before = pre[pos -1]
        cnt_gt = len(M) - bisect.bisect_right(M, x) if m else 0
        case2a = (case2a + unknowns_before * cnt_gt) % MOD
        # case2b
        unknowns_after = pre[n] - pre[pos]
        cnt_lt = bisect.bisect_left(M, x) if m else 0
        case2b = (case2b + unknowns_after * cnt_lt) % MOD

    sum_2 = 0
    if m != 0:
        sum_2 = (case2a + case2b) * pow(m, MOD-2, MOD) % MOD

    # Compute case3
    u = pre[n]
    case3 = 0
    if u >= 2:
        term = u * (u -1) % MOD
        inv2 = pow(2, MOD-2, MOD)
        case3 = term * inv2 % MOD
        case3 = case3 * inv2 % MOD

    total = (case1 + sum_2 + case3) % MOD
    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
-1 -1
""",
            "output": \
"""\
499122177
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

case2b: for the same element, pos 1. unknowns_after = pre[3] - pre[1] = 2-0=2. cnt_lt is bisect_left([1,2],3) → 2. So case2b += 2 * 2 =4.

sum_2 = (0+4)/2 → 4 * 499122177 mod MOD. 4 * 499122177 mod MOD is (4*499122177) = 1996488708 → 1996488708 mod 998244353 is 1996488708 - 2*998244353 = 1996488708 -1996488706=2. So sum_2=2.

case3: u=2. term=2*1=2. inv2=499122177. term*inv2= 2*499122177=998244354 mod MOD is 1. Then multiply by inv2 again: 1*499122177=499122177.

Total: 0+2+499122177=499122179 mod MOD. Which matches.

Third example:

Input:

2

-1 -1

known is empty. m=2. M = [1,2].

case1: 0.

pre array is [0,1,2] for n=2.

case2a and case2b: 0.

sum_2: 0.

case3: u=2. 2*1=2. 2 * inv2^2 → 2 * (499122177)^2 mod MOD. 499122177^2 mod MOD is (1/2)^2 = 1/4 mod MOD. 2*1/4 = 0.5 mod MOD → 499122177.

Which matches the third example.

Second example:

case1: no inversions. sum_2=0. case3=0. Output 0.

Yes.

So the code seems correct.

Now, considering the constraints. The code is O(n log n) for the Fenwick Tree, O(n log m) for the bisect steps (for each known element, bisect in O(log m) time), and the rest is O(n). Since n is 2e5, this should be acceptable.

Yes, because:

- The Fenwick Tree for case1 processes O(k) elements, each in O(log n) time. So O(k log n), which for k up to 2e5 is 2e5 * 20 → 4e6 operations.

- The bisect steps for case2a and case2b: O(k log m), where m can be up to 2e5. So again, 2e5 * 20 → 4e6.

Other steps are O(n) or O(m), which is acceptable.

So the code should pass all test cases within the time and memory constraints.
</think>

```python
import bisect

MOD = 998244353

class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 2)
    
    def update(self, idx, delta):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx
    
    def get_sum(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res
    
    def query_gt(self, x):
        return self.get_sum(self.n) - self.get_sum(x)

n = int(input())
p = list(map(int, input().split()))

known = [x for x in p if x != -1]
m = n - len(known)
M = []
if m > 0:
    s = set(known)
    M = [x for x in range(1, n+1) if x not in s]
    M.sort()

# Compute case1: inversions among known elements
case1 = 0
fen = FenwickTree(n)
for x in p:
    if x == -1:
        continue
    cnt = fen.query_gt(x)
    case1 = (case1 + cnt) % MOD
    fen.update(x, 1)

# Compute prefix array pre
pre = [0] * (n + 1)
for i in range(1, n+1):
    pre[i] = pre[i-1] + (1 if p[i-1] == -1 else 0)

# Compute case2a and case2b
case2a = 0
case2b = 0
for i in range(n):
    if p[i] == -1:
        continue
    x = p[i]
    pos = i + 1  # 1-based position
    # case2a: known at pos, unknown j < pos
    unknowns_before = pre[pos - 1]
    cnt_gt = len(M) - bisect.bisect_right(M, x) if m else 0
    case2a = (case2a + unknowns_before * cnt_gt) % MOD
    # case2b: known at pos, unknown i > pos
    unknowns_after = pre[n] - pre[pos]
    cnt_lt = bisect.bisect_left(M, x) if m else 0
    case2b = (case2b + unknowns_after * cnt_lt) % MOD

sum_2 = 0
if m != 0:
    sum_2 = (case2a + case2b) * pow(m, MOD-2, MOD) % MOD

# Compute case3: unknown pairs
u = pre[n]
case3 = 0
if u >= 2:
    term = u * (u - 1) % MOD
    inv2 = pow(2, MOD-2, MOD)
    case3 = term * inv2 % MOD
    case3 = case3 * inv2 % MOD

total = (case1 + sum_2 + case3) % MOD
print(total)
```
