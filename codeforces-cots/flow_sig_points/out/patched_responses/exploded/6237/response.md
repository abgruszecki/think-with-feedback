<think>
Okay, let's tackle this problem. Hmm. The problem is about calculating the beauty degree of query rectangles. The beauty degree is the number of beautiful rectangles that share at least one square with the query rectangle. So first, I need to understand what a beautiful rectangle is.

A beautiful rectangle is one that has exactly two marked corners, and those two are opposite corners. Because the marked squares are in a grid where each row and column has exactly one marked cell. So, for any two marked cells (i, p_i) and (j, p_j), where i < j, the rectangle formed by these two as opposite corners is beautiful. The total number of such rectangles is n*(n-1)/2, which makes sense since we choose any two distinct columns (i < j) and their corresponding rows.

Now, for each query rectangle, we need to find how many of these beautiful rectangles overlap with it. The challenge is to compute this efficiently for a large number of queries (up to 2e5) and large n (up to 2e5 as well). So a brute force approach is impossible. We need an optimized way.

Let's think about the problem in terms of inclusion-exclusion. For a beautiful rectangle defined by two points (i, p_i) and (j, p_j) where i < j, this rectangle spans columns from i to j and rows from min(p_i, p_j) to max(p_i, p_j). Any query rectangle that overlaps with this beautiful rectangle will contribute to the count. But how can we represent the condition for overlap?

Alternatively, perhaps the beauty degree can be computed by considering all possible pairs of marked points (i,j) where i < j, and their corresponding rectangle overlaps with the query. So for each query, the answer is the number of such pairs where the beautiful rectangle and the query share at least one cell.

But how do we efficiently compute this for each query?

Let's model the beautiful rectangle. A beautiful rectangle is determined by two points (i, p_i) and (j, p_j) where i < j. The rectangle spans columns i to j and rows min(p_i, p_j) to max(p_i, p_j). So for each such pair, the beautiful rectangle is the minimal rectangle that contains both points.

The problem is to find all such pairs (i,j) where their beautiful rectangle overlaps with the query rectangle [L, R] (columns) and [D, U] (rows). So the question becomes: how many pairs (i,j) with i < j have their rectangle overlapping with the query's rectangle.

Let's think about overlap conditions. Two rectangles overlap if their projections on both axes overlap. So the columns of the beautiful rectangle [i, j] must overlap with [L, R], and the rows [a, b] (a <= b) must overlap with [D, U]. Wait, no. The overlap condition is that their column ranges overlap and their row ranges overlap. Because for two rectangles to share any cell, their column ranges must overlap and their row ranges must overlap.

So for a beautiful rectangle with columns i..j and rows a..b (a is min(p_i, p_j), b is max), and the query has columns L..R and rows D..U. The overlap is possible if:

i <= R and j >= L (columns overlap) AND a <= U and b >= D (rows overlap).

So for each query, we need to count the number of pairs (i,j) where i < j, columns i..j overlap with L..R, and rows a..b (from the pair) overlap with D..U.

But with n up to 2e5 and q up to 2e5, we need a way to precompute some structures that allow answering each query in O(1) or O(log n) time.

Hmm. Let's think about how the pairs (i,j) can be represented. Each pair (i,j) is a pair of columns, and their rows are determined by p_i and p_j.

So the rows a and b are min(p_i, p_j) and max(p_i, p_j). So the row interval for the pair is [min, max].

So for a query, the pairs that contribute are those where:

columns i < j, and [i, j] overlaps with [L, R] (i <= R and j >= L), and min(p_i, p_j) <= U and max(p_i, p_j) >= D.

So the problem reduces to counting all pairs (i,j) where i < j, and:

i <= R and j >= L, and min(p_i, p_j) <= U and max(p_i, p_j) >= D.

Wait, but how do we represent this? We need to count all pairs (i,j) where i < j, and the column range of the pair overlaps with the query's column range, and the row range of the pair overlaps with the query's row range.

Alternatively, the column ranges of the beautiful rectangle and the query must have an intersection (so i <= R and j >= L). Similarly, the row ranges must have an intersection (a <= U and b >= D).

So for each query, the answer is the number of pairs (i,j) where i < j, and:

i <= R, j >= L, min(p_i, p_j) <= U, max(p_i, p_j) >= D.

But how to compute this efficiently?

Let's consider that for each pair (i,j) where i < j, the column interval is [i, j], and row interval is [a, b] where a = min(p_i, p_j), b = max(p_i, p_j).

So for a query [L, R] in columns and [D, U] in rows, we need the count of pairs (i,j) where:

columns overlap: i <= R and j >= L.

rows overlap: a <= U and b >= D.

We need to count all such pairs.

This seems challenging. But perhaps we can model the problem with some inclusion-exclusion.

Alternatively, we can precompute for each possible pair (i,j) their column and row ranges, but with n up to 2e5, that's O(n^2) pairs, which is impossible.

So we need a smarter approach.

Let's think about the pairs (i,j). Each pair is determined by two columns i < j. For each such pair, the row interval is [min(p_i, p_j), max(p_i, p_j)].

So for a query, the row condition is that the row interval of the pair must intersect with [D, U]. The row interval of the pair [a,b] must satisfy a <= U and b >= D. So for the rows, the pair's a <= U and the pair's b >= D.

So the row condition is (min(p_i, p_j) <= U) AND (max(p_i, p_j) >= D).

Hmm.

Now, the column condition is that the pair's column interval [i,j] overlaps with [L, R], which is equivalent to i <= R AND j >= L.

So the problem is to count the number of pairs (i,j) where i < j, i <= R, j >= L, min(p_i, p_j) <= U, max(p_i, p_j) >= D.

Let's split this into two parts: the column conditions and the row conditions. So the total count is the number of pairs that satisfy both parts.

But how can we model this?

Alternative approach: The total number of beautiful rectangles is C(n, 2) = n(n-1)/2. For a query, the answer is the total number of beautiful rectangles that have at least one cell overlapping with the query. But the beautiful rectangles are exactly those pairs (i,j) where their columns and rows ranges intersect the query's.

Wait, but the beautiful rectangle's cells are all the cells from columns i to j and rows a to b. So to overlap with the query's rectangle, the beautiful's columns must have some overlap with the query's columns (i <= R and j >= L), and the rows must have some overlap (a <= U and b >= D). So the conditions are as before.

But how to compute this efficiently.

Let's think of the problem as the intersection between two sets of pairs:

A. Pairs (i,j) that satisfy the column conditions.

B. Pairs (i,j) that satisfy the row conditions.

We need to find the size of the intersection of A and B.

But how to compute |A ∩ B|?

The problem is to compute for each query the count of pairs in both A and B.

Let me rephrase A and B.

A is the set of pairs (i,j) with i < j, i <= R, j >= L.

B is the set of pairs (i,j) with i < j, min(p_i, p_j) <= U, max(p_i, p_j) >= D.

So the answer is |A ∩ B|.

But how to compute this?

We can model the problem as:

Answer = |A| - |A ∩ B̄| + |B̄ ∩ Ā| ... No, perhaps inclusion-exclusion is not helpful here.

Alternative approach: For each query, compute the number of pairs (i,j) that satisfy i < j, i <= R, j >= L, min(p_i, p_j) <= U, max(p_i, p_j) >= D.

But how?

We can pre-process the data in a way that allows us to answer these queries quickly.

Let's consider the column conditions first. For a query's column L and R, the pairs (i,j) that satisfy i < j, i <= R, j >= L. So j >= L and i <= R. Also, since i < j, j can be from max(L, i+1) to n, but i can be from 1 to min(R, j-1). Hmm, perhaps there's a way to model the count of pairs (i,j) in this column condition.

But for each query, how many such pairs are there?

The total number of pairs (i,j) where i < j, i <= R, j >= L is equal to the number of pairs where j >= max(L, i+1) and i <= R.

Wait, perhaps the count can be computed as the sum over j from L to n, of the number of i's such that i < j and i <= R and j >= L. Wait, but j >= L is given, so j ranges from L to n. For each j in [L, n], the i's must satisfy i <= min(R, j-1) and i < j. So for each j, the number of i's is min(R, j-1). So the sum over j from L to n of min(R, j-1) when j >= L and i < j.

But for j >= L and j >= R+1, min(R, j-1) is R. For j <= R, min(R, j-1) is j-1.

So split the sum into two parts:

j ranges from L to R: sum (j-1) from j=L to R.

j ranges from R+1 to n: sum R.

So the total is sum_{j=L}^R (j-1) + sum_{j=R+1}^n R.

The first sum is sum from j=L to R of (j-1) = sum from k=L-1 to R-1 of k = ( (R-1)*R/2 ) - ( (L-2)(L-1)/2 ) )

The second sum is (n - R) * R if R+1 <=n, else 0.

But how does this help? Because even if we can compute the total number of pairs that satisfy the column condition (A), that's one part. The row condition (B) depends on the specific pairs, so we can't precompute that.

Hmm. So perhaps the solution is to precompute for each pair (i,j) their row ranges (a, b), and then for each query, count how many pairs (i,j) satisfy the column condition and their (a, b) overlaps with [D, U].

But how to do that efficiently.

Alternative approach: For each query, the count is the number of pairs (i,j) where i < j, i <= R, j >= L, a <= U, b >= D.

We can model this as for each query, compute the number of pairs that:

i is in [1, R], j is in [max(i+1, L), n], and min(p_i, p_j) <= U, max(p_i, p_j) >= D.

But again, checking each pair is O(n^2), which is impossible.

We need a data structure that can quickly count the number of pairs (i,j) in certain ranges that meet certain conditions on p_i and p_j.

Let me think about the pairs (i,j) where i < j. For each j, i can be from 1 to j-1.

So for each j, we can precompute some information about the i's in 1..j-1. But even that is O(n^2), which is not feasible.

Alternative idea: For each query, we can split the pairs (i,j) into those where i is in a certain range and j is in another, and then find how many pairs in those ranges have the row conditions.

But how to represent the row conditions.

The row conditions are min(p_i, p_j) <= U and max(p_i, p_j) >= D.

Which can be rewritten as (p_i <= U OR p_j <= U) and (p_i >= D OR p_j >= D).

But not sure if that helps.

Another approach: For the row conditions to be satisfied, the pair (p_i, p_j) must have at least one element <= U and at least one element >= D. Because min(p_i, p_j) <= U means that at least one of p_i or p_j is <= U, and max(p_i, p_j) >= D means that at least one of them is >= D. So the pair (p_i, p_j) must have at least one element <= U and at least one element >= D.

Wait, no. Let me re-express the conditions:

min(p_i, p_j) <= U → at least one of p_i or p_j is <= U. Because the min is the smaller of the two. If the min is <= U, then yes. So the first condition is satisfied if either p_i <= U or p_j <= U.

But the second condition is max(p_i, p_j) >= D. The max is the larger of the two. So the max >= D implies that at least one of them is >= D.

So the row conditions are equivalent to:

(p_i <= U OR p_j <= U) AND (p_i >= D OR p_j >= D).

Hmm, but how to model that.

Another way: the row conditions are that the pair (p_i, p_j) must have elements that cover the interval [D, U]. Because:

min(p_i, p_j) <= U → some element is <= U.

max(p_i, p_j) >= D → some element is >= D.

So, the pair must have at least one element <= U and at least one >= D. So the pair's elements must straddle the interval [D, U], such that there's at least one point below or equal to U and at least one point above or equal to D.

So the pair (p_i, p_j) must have:

(p_i <= U and p_j >= D) OR (p_i >= D and p_j <= U) OR (p_i <= U and p_j >= D) OR (p_i >= D and p_j <= U). Wait, no. Because the first condition is (p_i <= U or p_j <= U), and the second is (p_i >= D or p_j >= D). So it's possible that, for example, p_i is <= U and p_j >= D. Then both conditions are satisfied.

But the pair (p_i=3, p_j=5) with U=4 and D=4 would satisfy min(3,5)=3 <=4 and max(3,5)=5 >=4, so yes.

So the row conditions are equivalent to:

The pair (p_i, p_j) must have at least one element <= U and at least one element >= D.

So the row conditions can be rephrased as (p_i <= U OR p_j <= U) AND (p_i >= D OR p_j >= D).

But how to model this for all pairs (i,j) in the column ranges.

This is getting complicated. Let's think of it in terms of the four possibilities:

Case 1: p_i <= U and p_j >= D → satisfies the conditions.

Case 2: p_i >= D and p_j <= U → also satisfies.

Case 3: p_i <= U and p_j <= U → but then p_j >= D might not hold. So no.

Wait, but in case 3, if p_j is <= U but >= D, then the second condition (max(p_i, p_j) >= D) is satisfied. So perhaps I need to re-express.

The row conditions are:

At least one of p_i or p_j is <= U, and at least one of p_i or p_j is >= D.

So the pair must have elements in both lower and upper ranges.

So the pairs that satisfy the row conditions are those where the pair includes at least one element <= U and at least one element >= D.

So the count is the number of pairs where (p_i <= U and p_j >= D) OR (p_i >= D and p_j <= U) OR (p_i >= D and p_j >= D and p_j <= U) OR (p_i <= U and p_j >= D and p_i >= D). Wait, perhaps not. Let's think again.

The pair can have:

- One element <= U and the other >= D.

- Both elements >= D and one of them <= U.

For example, if D=3, U=5. If p_i=4 and p_j=5. Then min=4 <=5, max=5 >=3 → yes. So the row conditions are satisfied.

Alternatively, if p_i=3 and p_j=4 → min=3 <=5, max=4 >=3 → yes.

But if both elements are between D and U, then min <=U and max >= D → yes.

So the row conditions are satisfied if:

The pair's elements have at least one <= U and at least one >= D. But when both elements are between D and U, this condition is also satisfied. Because in that case, all elements are >= D (since D <= U, the elements are >= D and <= U), so max(p_i, p_j) >= D is satisfied (since both are >= D), and min(p_i, p_j) <= U is also satisfied (since both are <= U). So in this case, the row conditions are satisfied.

So the row conditions are satisfied if:

The pair (p_i, p_j) has at least one element <= U and at least one element >= D.

Wait, no. Wait, in the case where both elements are between D and U, then:

min(p_i, p_j) <= U → yes.

max(p_i, p_j) >= D → yes.

So the row conditions are satisfied.

So the row conditions are satisfied if either:

- Both elements are between D and U (so their min <= U and max >= D).

Or:

- One element is <= U and the other is >= D.

So the row conditions are satisfied in any case where the pair's elements are not both < D, not both > U, and not (one < D and the other > U, but that would still have one >= D or one <= U? Wait, no. Let's think of D=5 and U=6.

If p_i is 4 and p_j is 7 → min is 4 <=6, max is7 >=5. So row conditions are satisfied.

But if p_i is 4 and p_j is 3 (D=5), then min is 3 <=6, max is4 <5. So the max is <5. So the row conditions would be min <=U (yes), but max < D (no). So row conditions are not satisfied.

Ah, right. So the row conditions are min(p_i, p_j) <= U and max(p_i, p_j) >= D.

So in cases where both elements are >= D and <= U: yes.

If one element is < D, the other >= D and <= U: then max >= D (yes), min <= U (yes).

If one element is <= U and >= D, and the other is > U: then min <= U (yes), max >= D (yes).

If one element is <= U and < D, the other is >= D and > U: then min <= U (yes), max >= D (yes).

So the row conditions are satisfied if the pair's elements are not both < D or both > U.

Wait, no:

If both elements are < D: then their max is < D → max >= D is false → row condition is not satisfied.

If both elements are > U: then their min is > U → min <= U is false → row condition not satisfied.

If one is < D and the other is > U: min is < D (<= U) → yes. Max is > U (>= D) → yes. So row conditions are satisfied.

So the row conditions are satisfied in all cases except when:

- Both elements are < D.

- Both elements are > U.

So the row conditions are equivalent to:

not (both elements < D) and not (both elements > U).

So the count of pairs that satisfy the row conditions is equal to the total pairs (i,j) minus the pairs where both elements are < D, minus the pairs where both elements are > U.

Because the row conditions are satisfied unless the pair is entirely below D or entirely above U.

This is a crucial insight.

So, for the row conditions, the number of pairs (i,j) that satisfy the row conditions is:

total_pairs - (count_both_less_D + count_both_greater_U)

Where total_pairs is the total number of pairs (i,j) in the column condition (A) for the query.

So, the problem now reduces to:

For each query, compute:

answer = (number of pairs in A) - (number of pairs in A where both p_i and p_j < D) - (number of pairs in A where both p_i and p_j > U)

Because the row conditions are satisfied by all pairs except those two cases.

This seems manageable. Because if we can compute for each query:

1. The number of pairs in A (column condition) → call this C.

2. The number of pairs in A where both p_i < D → S1.

3. The number of pairs in A where both p_i > U → S2.

Then answer is C - S1 - S2.

So now the problem is to compute these three values for each query.

Let's see how to compute C first.

As earlier, C is the number of pairs (i,j) with i < j, i <= R, j >= L.

Which can be computed as follows:

The pairs (i,j) are those where j >= L and i <= R and i < j.

So j can range from L to n, and for each j, i ranges from 1 to min(R, j-1).

So the total is the sum over j from L to n of min(R, j-1).

But we can compute this sum mathematically.

Split the sum into two parts:

j ranges from L to R: j-1 >= i (since i <= R and j <= R → i < j → i can be up to j-1). So for j in [L, R], the number of i's is j-1.

j ranges from R+1 to n: min(R, j-1) is R. So for j in [R+1, n], the number of i's is R.

So the sum is:

sum_{j=L}^R (j-1) + sum_{j=R+1}^n R.

The first sum is the sum of integers from (L-1) to (R-1). Which is (R-1)*R//2 - (L-1)*(L-2)//2.

The second sum is (n - (R+1) + 1) * R → (n - R) * R, but only if R+1 <= n. If R+1 > n, then the second sum is zero.

So putting it all together:

C = (R*(R-1)//2 - (L-1)*(L-2)//2) + max(0, (n - R)) * R.

But we need to check if R+1 <=n. So when R < n, then (n - R) * R. Otherwise, R >=n → (n - R) is zero.

So that's how to compute C.

Now S1 is the number of pairs (i,j) in A where p_i < D and p_j < D.

Similarly, S2 is the number of pairs (i,j) in A where p_i > U and p_j > U.

So the problem is to compute S1 and S2 efficiently.

How can we compute S1 and S2?

For S1: count the number of pairs (i,j) where i < j, i <= R, j >= L, p_i < D, p_j < D.

Similarly for S2: count the number of pairs (i,j) where i < j, i <= R, j >= L, p_i > U, p_j > U.

So we need to model these two counts.

Let's think of S1 first.

For S1, the pairs (i,j) must be in A (i < j, i <= R, j >= L), and both p_i and p_j are < D.

So how can we model this?

We can pre-process for each D, the number of elements <= (D-1) in certain ranges. But with D varying per query, we need a way to count, given D, the number of pairs (i,j) in A where both p_i and p_j are < D.

This seems challenging. But perhaps we can model this with some 2D prefix sums, but given the time constraints, it's not feasible for n up to 2e5.

Alternative approach: For a given D, all elements with value < D can be considered as "active" elements. We need to count the number of pairs (i,j) in A where both i and j are active elements.

But the pairs (i,j) must satisfy i < j, i <= R, j >= L.

Wait, but j must be >= L and i <= R. So for S1, we need to count pairs (i,j) where:

i < j,

i <= R,

j >= L,

p_i < D,

p_j < D.

But how to model this.

Let's think of the elements in the column condition (i <= R, j >= L, i < j). So j can be from max(L, i+1) to n, but i must be <= R.

But perhaps for S1, the problem can be rephrased as follows:

We need to count the number of pairs (i,j) such that:

i < j,

i <= R,

j >= L,

and both p_i and p_j are < D.

This is equivalent to:

The number of elements in the set X (elements where column i <= R and p_i < D) multiplied by the elements in the set Y (elements where column j >= L and p_j < D and j > i).

But this seems like a nested problem.

Alternative approach: For each query, the set of eligible i's for S1 are those with column i <= R and p_i < D. The eligible j's for each i are those j >= max(L, i+1), j >= L, j > i, and p_j < D.

So for S1, it's the sum over all eligible i's of the number of j's >= max(i+1, L) that are in the eligible j's.

Eligible j's are columns >= L, j > i, and p_j < D.

So for each i in [1, R], p_i < D:

the j's must be in [max(L, i+1), ... , n], and p_j < D.

The count of j's is the number of elements in columns >= max(L, i+1) where p_j < D.

But how to compute this efficiently.

But with D varying per query, we need a data structure that can, for a given D, answer the number of elements in columns >= a certain value with p_j < D.

Similarly, the same for the i's.

Wait, the p array is given as the second line: p_1, p_2, ..., p_n. So for column i, the row is p_i.

So for each column j, p_j is known. So we can pre-process a structure that allows for a query of the form: given D and a range [a, b], how many columns j in [a, b] have p_j < D.

This is a standard range count problem and can be solved with a segment tree or a binary indexed tree (Fenwick tree) after sorting the elements.

But given that D can be up to n (1e5 to 2e5), and queries are up to 2e5, we need an efficient way.

An efficient way is to, for each column j, store (j, p_j). Then, for each query, to compute the count of j in [a, b] with p_j < D, we can use a binary indexed tree (Fenwick) that is built in the order of j, but with p_j sorted.

Alternatively, we can pre-sort the columns based on p_j, and for each query, use binary search to find how many in a certain column range have p_j < D.

But let's think: for each j, we have p_j. We can create an array sorted by j (since j is the column number from 1 to n). But for a given j, p_j is known.

So for each j, we can have a structure that allows us to query, for a range [a, b] of j's, the number of p_j < D.

This can be done using a prefix array sorted by j and then for each j, storing p_j, and then building a segment tree that allows range queries for the count of elements < D.

But building such a structure for n=2e5 is feasible.

Another approach is to use a binary indexed tree (Fenwick tree) but since the columns are ordered by j, which is their index, we can't directly use a Fenwick tree unless we can represent the data in a way that allows for cumulative frequency.

Alternatively, we can pre-process a list of (j, p_j) sorted by j, and for each j, store p_j. Then, for any range [a, b], the count of p_j < D is the number of j in [a, b] where p_j < D.

This is a standard range frequency problem, which can be solved with a prefix array and binary search, but only if the data is sorted. However, since j is not sorted by p_j, but j is in order, the p_j for j in [a, b] can be in any order. So a segment tree is the way to go.

So the plan is:

- Pre-process a segment tree that can, for any query range [a, b], return the number of elements with p_j < D.

Similarly for the other conditions (like p_j > U).

So for S1, the count is:

sum over i in eligible_i (i <= R, p_i < D) of count of j in [max(L, i+1), n] where j >= L, j > i, and p_j < D.

But how to compute this sum.

This sum is equivalent to:

sum_{i=1 to R} [ (p_i < D) ? (number of j in [max(L, i+1), n] where p_j < D) : 0 ]

But how to compute this efficiently.

For each query, D can vary. So for each query, we need to find all i <= R where p_i < D. For each such i, we need to find the number of j >= max(L, i+1) where j <= n and p_j < D.

This can be rewritten as:

sum_{i in [1, R], p_i < D} [ count of j in [max(L, i+1), n], p_j < D ]

To compute this sum, perhaps we can split it into two parts:

1. j >= L and j > i, so j starts at max(L, i+1).

But for each i in [1, R], p_i < D, and j >= max(L, i+1), j <=n.

So for each such i, the j's are in [a_i, n], where a_i = max(L, i+1).

The count of j's in this interval where p_j < D can be obtained via the segment tree query for [a_i, n] and D.

But summing this over all eligible i's is O(R) per query, which is O(2e5) per query and with 2e5 queries, this would be O(4e10) operations, which is way too slow.

This approach isn't feasible.

So we need a smarter way to compute S1 and S2.

Alternative idea: For S1, the eligible pairs (i,j) must satisfy i <= R, j >= L, i < j, p_i < D, p_j < D.

We can model this as the number of pairs (i,j) where i is in [1, R], j is in [L, n], i < j, p_i < D, p_j < D.

But how to compute this.

The pairs (i,j) can be represented as:

i is in [1, R], j is in [max(i+1, L), n], and p_i < D, p_j < D.

But even so, this seems difficult.

Let me consider the problem in terms of two sets:

A: all columns i <= R where p_i < D.

B: all columns j >= L where p_j < D.

We need to find the number of pairs (i,j) where i < j, i is in A, j is in B.

Because for such pairs, j >= L, i <= R, and i < j.

But j can be up to n.

But j must be in B, which is j >= L and p_j < D.

So S1 is the number of pairs (i, j) where i is in A, j is in B, and i < j.

This can be computed as the number of elements in A multiplied by the number of elements in B, minus the number of pairs where i >= j, but since i and j are in A and B, and i < j, this is not needed. Wait, no.

Wait, S1 is the count of pairs (i,j) where i is in A (i <= R, p_i < D), j is in B (j >= L, p_j < D), and i < j.

So for each i in A, the number of j in B that are > i is equal to the number of elements in B that are >= max(i+1, L).

So S1 is the sum over all i in A of the count of j in B where j >= max(i+1, L).

But again, this is O(R) per query, which is too slow.

Alternative idea: For the pairs (i,j) in A and B, the count is the number of pairs (i,j) where i <= R, j >= L, i < j, p_i < D, p_j < D.

This can be rewritten as the number of pairs (i,j) where i < j, p_i < D, p_j < D, i <= R, j >= L.

Let’s think of this as:

Total pairs in A and B (i < j, p_i < D, p_j < D) where i <= R and j >= L.

We can model this as:

The number of pairs (i,j) with p_i < D, p_j < D, i < j, i <= R, j >= L.

To compute this, perhaps we can precompute for each possible D, the count of such pairs. But D can be up to n, and there's no way to precompute for all possible D.

Alternative approach: The pairs (i,j) with i < j, p_i < D, p_j < D are the same as the pairs in the set of all elements with p < D, and we want to count the pairs that also satisfy i <= R and j >= L.

But how?

The total number of pairs (i,j) with i < j, p_i < D, p_j < D is equal to C_total = (k * (k-1)) / 2, where k is the number of elements with p < D. But this is the case when there are no restrictions on i and j. But in our problem, we need to consider i <= R and j >= L.

So S1 is the number of pairs (i,j) with i < j, p_i < D, p_j < D, i <= R, j >= L.

To compute this, we can model it as follows:

Let’s find all elements with p < D. Let's call this set S. Let the elements in S be sorted by their column indices.

For each element i in S where i <= R, count the number of elements j in S where j >= max(i+1, L).

The sum of these counts is S1.

But again, how to compute this efficiently.

If we can represent S as a sorted list (sorted by column), then for each i in S where i <= R, we can compute the lower bound for j: j >= max(i+1, L). Since S is sorted, we can find for each i the number of elements j in S that are >= lower_bound.

But this would require for each query to process all elements in S where i <= R, which is O(k) operations, where k can be up to 2e5, leading to O(4e10) operations for all queries.

This is not feasible.

Alternative idea: Precompute for each possible L and R. But since L and R can be up to 2e5, this is also not feasible.

Hmm. We need a way to compute S1 and S2 for each query in O(1) or O(log n) time.

Let’s think about S1 again. S1 is the number of pairs (i,j) where i < j, i <= R, j >= L, p_i < D, p_j < D.

We can split this into two cases:

Case 1: L <= R.

In this case, the pairs must have i <= R, j >= L, and i < j. Since L <= R, j can be >= L and >= i+1. So the pairs are i in [1, R], j in [max(i+1, L), n], and p_i < D, p_j < D.

But even this split doesn't help much.

Alternative approach: For S1, the count can be expressed as the number of elements in S (p < D) in the column range [1, R] multiplied by the number of elements in S in the column range [L, n], minus the number of pairs where j <= i or j < L.

Wait, this is a standard inclusion-exclusion approach. Let’s see:

The total number of pairs (i,j) in S where i <= R and j >= L is equal to the number of pairs (i,j) where i is in S ∩ [1, R], j is in S ∩ [L, n], and i < j.

So the count is the number of ordered pairs (i,j) in S where i <= R, j >= L, i < j.

Which can be computed as:

Let A = number of elements in S with column <= R.

Let B = number of elements in S with column >= L.

The number of ordered pairs (i,j) where i is in S ∩ [1, R], j is in S ∩ [L, n], and j > i.

This can be calculated as (A * B) - C - D, where:

C is the number of pairs where i <= R and j >= L but j <= i.

D is the number of pairs where i > R or j < L.

Wait, perhaps another approach: the total possible pairs is A * B. From this, subtract the pairs where j <= i or i >= L or j < L or i > R, but I'm getting confused.

Alternatively, the desired count is the number of pairs (i,j) where i is in S ∩ [1, R], j is in S ∩ [L, n], and i < j.

This can be computed as follows:

Let’s consider the intersection of S with [1, R] (call this set X) and S with [L, n] (call this set Y). For each i in X, the number of j in Y where j > i is equal to the number of elements in Y that are > i.

So the total count is the sum over all i in X of the count of elements in Y that are > i.

This sum can be computed using a sorted list of Y and for each i in X, the count is the number of elements in Y greater than i.

If the elements of Y are sorted, then for each i in X, the count is the number of elements in Y greater than i. This can be found using binary search.

But again, for each query, this would require O(A) operations, which is O(2e5) per query, leading to O(4e10) operations.

This is not feasible.

Alternative Idea: The number of pairs (i,j) where i < j, i in X, j in Y, and i < j can be computed using the following formula:

count = total_pairs - pairs where i >= j.

But since X and Y are overlapping, it's possible that some i in X are in Y as well.

Alternatively, let’s compute the size of X and Y.

But the sets X and Y are subsets of S (elements with p < D). X is S ∩ [1, R], Y is S ∩ [L, n].

The intersection of X and Y is S ∩ [L, R], since L <= R.

So the total number of elements in X is A = count_S_1_to_R.

The total in Y is B = count_S_L_to_n.

The elements in X and Y are:

X: elements in S with column <= R.

Y: elements in S with column >= L.

So for i in X and j in Y, j > i is required.

We can split the pairs into three parts:

1. i < L: j must be >= L.

So for these i's, j can be any in Y where j > i. Since i < L, and j >= L, j is always > i. So the number of j's is B (since Y is j >= L).

But wait, Y is elements in S with j >= L and p_j < D. So for i < L and in X, j can be any element in Y. Because j >= L > i. So each such i contributes B elements.

2. L <= i <= R: j must be > i and >= L. Since i >= L, j must be > i and <= n.

For these i's, j can be any element in Y where j > i. So for each such i in X (which is also in Y), the number of j's is the number of elements in Y greater than i.

So the total for this part is the sum over i in X ∩ Y of (number of elements in Y > i).

So combining both parts:

count = (number of X elements < L) * B + sum_{i in X ∩ Y} (number of elements in Y > i).

But how to compute this.

But even if we can compute this, the sum over i in X ∩ Y of (number of elements in Y > i) is the same as the number of pairs (i,j) in X ∩ Y where j > i.

Which is the same as (k choose 2), where k is the size of X ∩ Y, but only if the elements are sorted and j > i.

Wait, no. If X ∩ Y has elements sorted in increasing order, then the number of pairs (i,j) with j > i is k*(k-1)/2.

But this is true only if the elements are sorted. However, in our case, X ∩ Y is S ∩ [L, R], which is elements in columns [L, R] with p < D. These elements are ordered by their column numbers.

So their columns are ordered as L <= i_1 < i_2 < ... < i_k <= R.

So the number of pairs (i,j) in this list where j > i is (k choose 2).

So putting it all together:

The count is:

number of X elements < L → A1 = count_S_1_to_{L-1}.

So contribution from i < L: A1 * B.

Plus the number of pairs in X ∩ Y where j > i → (k choose 2), where k is the size of X ∩ Y.

So S1 = A1 * B + (k * (k-1)) // 2.

This is a breakthrough!

So the formula for S1 is:

A = count_S_1_to_R (number of elements in S with column <= R).

B = count_S_L_to_n (number of elements in S with column >= L).

A1 = count_S_1_to_{L-1}.

k = count_S_L_to_R (number of elements in S with column between L and R, inclusive).

So S1 = A1 * B + (k * (k-1)) // 2.

But wait, why?

Because:

- Elements i in X (columns <= R) and i < L contribute B j's each (since j >= L, and j is in Y). So A1 * B.

- Elements i in X ∩ Y (columns between L and R) contribute j's > i, which is the number of elements in Y (>= L) that are > i. But since Y includes elements >= L, and i is >= L, j must be > i and in Y. But Y is S ∩ columns >= L, and i is in S ∩ columns <= R and >= L. So Y includes elements >= L. So j can be any element in Y that is > i. But since the elements in Y are ordered by columns, the number of j's > i for a particular i is (number of elements in Y with column > i).

But when you sum this for all i in X ∩ Y (which is the same as Y ∩ X, which is S ∩ [L, R]), the sum is the number of pairs (i,j) in Y where j > i.

Which is exactly (k choose 2) where k is the number of elements in Y ∩ X.

Yes! Because for a sorted list of elements, the number of pairs where j > i is exactly k choose 2.

So S1 = A1 * B + (k choose 2).

But how to compute A1, B, and k.

A1 is the number of elements in S with column <= L-1.

B is the number of elements in S with column >= L.

k is the number of elements in S with column between L and R.

But S is the set of elements with p < D.

So for each query with D, A1 = count of p_j < D and j <= L-1.

B = count of p_j < D and j >= L.

k = count of p_j < D and j is between L and R.

So how to compute these counts.

We can pre-process a structure that allows us to query, for any D, the number of elements with p_j < D in a given range [a, b].

This can be done with a segment tree where each node stores a sorted list of the p_j's in its interval. For a query range [a, b], we can query the segment tree to collect all the relevant nodes and perform a binary search to count the number of elements less than D in those nodes.

But building such a segment tree is feasible for n up to 2e5, and each query can be answered in O(log n) time.

So the plan is:

1. Pre-process a segment tree where each node stores a sorted list of p_j in the interval it represents.

2. For a given query, compute the following for S1:

   a. A1 = query(1, L-1) for p < D.

   b. B = query(L, n) for p < D.

   c. k = query(L, R) for p < D.

   Then S1 = A1 * B + k*(k-1)//2.

3. Similarly for S2:

   S2 is the number of pairs (i,j) in A where both p_i > U and p_j > U.

   Using the same approach:

   S2 = A1 * B + k*(k-1)//2.

   But here:

   A1 is the number of elements with p_i > U in [1, R].

   B is the number of elements with p_j > U in [L, n].

   k is the number of elements with p_j > U in [L, R].

   So for S2:

   A1 = count of p_j > U in [1, R].

   B = count of p_j > U in [L, n].

   k = count of p_j > U in [L, R].

   Then S2 = A1 * B + k*(k-1)//2.

Wait, but how to compute the count of elements > U in a range. The segment tree can also be used for this. Because count of elements > U in a range [a, b] is equal to (b - a + 1) - count of elements <= U in [a, b].

But wait, the segment tree stores the sorted list of p_j's. So for a query of elements > U, we can compute the count of elements <= U and subtract from the total elements in the range.

So for a range [a, b], the count of elements > U is (b - a + 1) - query_count( [a, b], <= U).

But for S2, the elements are > U. So for S2:

A1 is the number of elements in [1, R] with p_j > U.

B is the number of elements in [L, n] with p_j > U.

k is the number of elements in [L, R] with p_j > U.

These can be computed as:

A1 = count_gt_U_1_to_R = query_gt(U, 1, R) = (R) - query_le(U, 1, R).

But wait, the count of elements in [1, R] is R, and the count of elements <= U is query_le(U, 1, R). So the count of elements > U is R - query_le(U, 1, R).

Similarly for B and k.

But wait, the count of elements in [L, n] is (n - L + 1). So count_gt_U_L_to_n = (n - L + 1) - query_le(U, L, n).

So for S2:

A1 = R - query_le(U, 1, R).

B = (n - L + 1) - query_le(U, L, n).

k = (R - L + 1) - query_le(U, L, R).

But wait, the total elements in [L, R] is R - L + 1.

So yes.

So the approach is:

For each query:

Compute C = column pairs count.

Compute S1 = A1 * B + k*(k-1)//2, where:

   A1 = number of elements with p < D in [1, L-1].

   B = number of elements with p < D in [L, n].

   k = number of elements with p < D in [L, R].

Compute S2 = A1' * B' + k'*(k'-1)//2, where:

   A1' = number of elements with p > U in [1, R].

   B' = number of elements with p > U in [L, n].

   k' = number of elements with p > U in [L, R].

But wait, S2 is the number of pairs (i,j) in A where both p_i and p_j > U. So the pairs (i,j) must satisfy i < j, i <= R, j >= L, p_i > U, p_j > U.

So for S2, the formula is similar to S1 but with the elements > U.

So the same formula applies:

S2 = A1' * B' + (k' choose 2).

Where:

A1' = count of elements > U in [1, R] and j >= L.

Wait, no. For S2:

The pairs (i,j) must have i <= R, j >= L, i < j, p_i > U, p_j > U.

So:

A1' is the number of elements in [1, R] with p_i > U.

B' is the number of elements in [L, n] with p_j > U.

k' is the number of elements in [L, R] with p_j > U.

Then:

S2 = (number of elements in [1, R] with p_i > U) * (number of elements in [L, n] with p_j > U) - (number of pairs where j < L) + (number of pairs in [L, R] where i < j and p_i > U and p_j > U).

Wait, no. The same approach as S1 applies here.

For S2, the formula is:

A1' = count of elements in [1, R] with p > U.

B' = count of elements in [L, n] with p > U.

k' = count of elements in [L, R] with p > U.

So S2 = (A1' * B') - (number of elements in [1, R] and >= L with p > U) * (number of elements in [L, R] with p > U) ) + (k' choose 2).

No, the same reasoning as S1 applies:

The number of pairs (i,j) where i is in [1, R] and j is in [L, n], and both p_i and p_j > U, and i < j.

This can be computed as:

number of elements in [1, R] with p > U (A1') multiplied by the number of elements in [L, n] with p > U (B'), minus the pairs where j <= i, and then adding the pairs where i and j are in [L, R].

Wait, no. Using the same approach as S1, the formula for S2 is:

A1'_part = count of elements in [1, L-1] with p > U → because for i in [1, L-1], j must be >= L. So these contribute (A1'_part) * B'.

Then for elements in [L, R], the count is (k' choose 2).

So S2 = A1'_part * B' + (k' choose 2).

But how to compute A1'_part.

A1'_part is the number of elements in [1, R] with p > U and i < L.

Because i can be up to R, but j must be >= L. So the i's are in [1, min(R, L-1)].

So the number of elements in [1, min(R, L-1)] with p > U.

But if L > R, then min(R, L-1) is R, but since L <= R (given that in the query l <= r), but the input allows L and R to be 1 <= l <= r <=n.

So the code should handle cases where L > R, but according to the input constraints, l <= r. So for the query, L and R are such that L <= R.

So A1'_part is the number of elements in [1, L-1] with p > U.

But how to compute this.

A1'_part = query_gt(U, 1, L-1).

Similarly, B' = query_gt(U, L, n).

k' = query_gt(U, L, R).

So S2 = A1'_part * B' + (k' * (k' - 1)) // 2.

Yes.

So putting it all together, the steps are:

For each query L, R, D, U:

1. Compute C using the formula derived earlier.

2. Compute S1:

   a. Compute A1 = query_lt(D, 1, L-1).

   b. Compute B = query_lt(D, L, n).

   c. Compute k = query_lt(D, L, R).

   d. S1 = A1 * B + k * (k-1) // 2.

3. Compute S2:

   a. Compute A1'_part = query_gt(U, 1, L-1).

   b. Compute B' = query_gt(U, L, n).

   c. Compute k' = query_gt(U, L, R).

   d. S2 = A1'_part * B' + k' * (k'-1) // 2.

4. The answer is C - S1 - S2.

Now, the key is to implement the query_lt and query_gt functions efficiently.

To do this, we can use a segment tree where each node contains a sorted list of the p values in its interval. Then, for any query [a, b], to find the number of elements less than or equal to X, we can traverse the segment tree and for each node that is fully contained in [a, b], perform a binary search on the sorted list to count the elements <= X and sum them up.

Similarly, query_gt is (total elements in [a, b]) - query_leq(X).

But the total elements in [a, b] is b - a + 1. So for query_gt(X) in [a, b], it's (b - a + 1) - query_leq(X, a, b).

But wait, query_lt(X) is the number of elements < X, which is the same as query_leq(X-1). But in our problem, D can be up to n, which is up to 2e5. So for each query, we can compute query_lt(D, a, b) as query_leq(D-1, a, b).

Similarly, query_gt(U) is the number of elements > U, which is (b - a + 1) - query_leq(U, a, b).

So the functions are:

def query_lt(X, a, b):
    return query_leq(X-1, a, b)

def query_gt(X, a, b):
    total = max(0, b - a + 1)
    return total - query_leq(X, a, b)

But we need to handle a > b. For example, if L is 1, then L-1 is 0, and the interval [1, 0] is invalid. In such cases, query_lt(D, 1, 0) returns 0.

So the code for the queries must handle a > b by returning 0.

Thus, the segment tree must handle ranges where a > b by returning 0.

Implementing this, the segment tree can be built with each node containing a sorted list of the p values in the interval. Then, for a query, we split the query range into O(log n) segments and perform a binary search on each of those sorted lists to count the number of elements <= X.

This approach is efficient enough for the constraints.

Now, the plan is:

- Read n and q.

- Read the array p as a list (p[1...n], since columns are 1-based).

- Build a segment tree where each node contains a sorted list of p's in its interval.

- For each query:

   a. Read l, d, r, u. (Wait, wait, the problem statement says that the query is given as l, d, r, u, which are the leftmost column, bottommost row (d), rightmost column (r), topmost row (u). So the query rectangle is columns l to r, rows d to u.)

   So the columns in the query are L = l, R = r.

   The rows in the query are D = d, U = u.

   So the row conditions are that the beautiful rectangle's row interval must overlap with [D, U], which we've translated into S1 and S2 as described.

   So proceed with the steps outlined earlier.

   So for each query:

   L = l, R = r.

   D = d, U = u.

   Compute C as:

   sum1 = (R*(R-1)//2 - (L-1)*(L-2)//2) if L <= R else 0.

   sum2 = max(0, (n - R)) * R.

   C = sum1 + sum2.

   Then compute S1 and S2.

   Compute S1:

   A1 = query_leq(D-1, 1, L-1).

   B = query_leq(D-1, L, n).

   k = query_leq(D-1, L, R).

   S1 = A1 * B + (k * (k-1)) // 2.

   Compute S2:

   A1_part = query_gt(U, 1, L-1) → which is (L-1) - query_leq(U, 1, L-1).

   B_prime = query_gt(U, L, n) → (n - L + 1) - query_leq(U, L, n).

   k_prime = query_gt(U, L, R) → (R - L + 1) - query_leq(U, L, R).

   S2 = A1_part * B_prime + (k_prime * (k_prime - 1)) // 2.

   The answer is C - S1 - S2.

   Then, output that answer.

Now, the key part is to implement the segment tree with range queries for the count of elements <= X.

Implementing the segment tree:

Each node represents a range [start, end].

Each node has a sorted list of the p values in its range.

To build the segment tree:

- The leaves are individual elements, each with a sorted list containing just that element.

- Internal nodes are built by merging the sorted lists of their children.

But for n up to 2e5, the segment tree would have O(n) nodes, and each node's sorted list can be built in O(k log k) time, where k is the size of the node's range. However, building the segment tree this way would take O(n log n) time, which is acceptable.

But for n=2e5, the segment tree may have O(4n) nodes. However, building this with recursion might be memory intensive.

An alternative is to build the segment tree iteratively or use a list-based approach. But in Python, even with 4n nodes, each with a list of size up to n (for the root node), the memory would be O(n log n), which is manageable for n=2e5 (n log n is about 2e5 * 20 = 4e6).

But in practice, this may be tight. So perhaps a better approach is to build the segment tree as a list of nodes, where each node contains start, end, and the sorted list.

But in Python, with the given memory constraints (512MB), this should be manageable.

Another thing to note is that building the segment tree's sorted lists takes O(n log n) time and O(n log n) space.

But for n=2e5, log n is about 20, so each level of the tree would require O(n) space, leading to O(n log n) space.

Which is 2e5 * 20 = 4e6 elements, which is manageable.

Now, the code outline:

Implement the segment tree.

But in Python, implementing a segment tree for this problem can be done with a list of sorted arrays for each node.

But building the segment tree recursively may not be feasible for n=2e5. So perhaps we can build the segment tree using a bottom-up approach.

Alternatively, use a binary indexed tree for the problem. But I'm not sure.

Alternative Idea: Since the queries are for ranges [a, b], and we need to count the number of elements <= X in the range, we can pre-process a list of sorted p_j for each possible position. But that's not directly possible. So the segment tree approach is the way to go.

But in Python, even for n=2e5, the segment tree can be built with each node storing a sorted list.

Implementing the segment tree:

The segment tree can be represented as a list of nodes. Each node has a left and right index, and a sorted list.

But in Python, building such a structure may be time-consuming for large n.

Another approach is to build the segment tree using a list-based approach, where each node is stored in a flat array, and for a node at position i, the left and right children are at 2*i+1 and 2*i+2. But for n=2e5, the number of nodes can be up to 4*2e5 = 8e5, which is manageable.

But building the tree recursively may hit recursion depth issues. So an iterative approach is better.

Alternatively, use a library like bisect to perform the binary searches.

But for now, let's proceed with building the segment tree.

Here's the code outline:

Read n and q.

Read p as a list (0-based or 1-based? Let's use 1-based for the code, to match the problem statement.)

Build the segment tree.

Then, process each query.

Implement the query_leq function.

But in Python, building the segment tree can be done as follows:

Each node is responsible for a certain range. The leaves are ranges of length 1. Parents are built by merging the children's sorted lists.

For example, for the leaves, each node has a list containing the single element p[i].

For a parent node covering [a, b], its sorted list is the merge of the left child's list and the right child's list.

But merging two sorted lists can be done in O(k) time where k is the total length. For the worst case, each merge takes O(n) time, but for a balanced tree, the total time is O(n log n), which is acceptable.

But merging two sorted lists can be done using the 'sorted' function with the combined lists. Alternatively, since each list is already sorted, we can perform a manual merge.

But in Python, the fastest way is to use the heapq merge function, but that's an iterator. Or, simply concatenate and sort. But that would take O(k log k) time, which is not efficient for large k.

So merging two sorted lists can be done in O(k) time with a manual merge.

Implementing the manual merge:

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

So for each node, the sorted list is the merge of its children's lists.

But building the segment tree in this way is manageable.

But for n=2e5, the number of nodes is O(4n), and each node's list is the merged list of its children. The total time to build the tree is O(n log n).

Now, the code:

Implement the segment tree with a list of sorted lists.

But in Python, this may be too slow for the given constraints. So perhaps an alternative approach is needed.

Alternative Idea: Since the p array is given, and we can process all queries offline, but the queries are online (each query can have any L, R, D, U), we need to have a data structure that can answer range [a, b] and count elements <= X.

An alternative approach is to build a prefix sorted list and use binary search.

For example, for each position i, create a sorted list of the first i elements. Then, for a query [a, b], the number of elements <= X is the number in the first b elements minus the number in the first a-1 elements. But this is only true for ranges [1, b], but for arbitrary ranges [a, b], this approach isn't applicable.

Thus, the segment tree approach is the way to go.

So now, let's proceed with writing the code.

The code will:

1. Read n and q.

2. Read p as a list of integers.

3. Build the segment tree.

4. For each query, compute C, S1, S2, and output the result.

Now, the segment tree implementation:

But in Python, recursion depth is limited. So an iterative approach is better.

Implementing the segment tree iteratively is challenging, but possible.

Alternatively, use a list-based approach where each node stores its left and right indices and the sorted list.

But for a segment tree, the standard way is to build a list of nodes where the root is at position 0, and for a node at position i, the left child is at 2*i+1 and the right child is at 2*i+2. But this approach requires knowing the size of the segment tree in advance, which is difficult for n=2e5.

Alternatively, use a dynamic approach where each node has a start and end, left and right children pointers, and the sorted list.

But in Python, this may be memory-intensive.

Another Idea: Pre-process all possible ranges.

But for n=2e5, it's impossible.

Thus, the best way is to implement the segment tree with each node storing the sorted list of its range.

But for Python, perhaps the easiest way is to use a list-based approach with recursion.

Here's a code sketch:

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = []
        self.build(0, self.n-1, data)

    def build(self, l, r, data):
        node = {'left': l, 'right': r, 'data': []}
        if l == r:
            node['data'] = [data[l]]
        else:
            mid = (l + r) // 2
            left_child = self.build(l, mid, data)
            right_child = self.build(mid+1, r, data)
            node['data'] = merge(left_child['data'], right_child['data'])
        self.tree.append(node)
        return node

But this is a recursive approach, and for n=2e5, the recursion depth will be O(log n), which is acceptable (log2(2e5) is about 18, so the recursion depth is manageable).

But in practice, for n=2e5, this approach will have 2e5 leaves and O(4e5) nodes. But building this recursively may be slow.

Alternatively, can use a more efficient approach.

But perhaps we can proceed with this approach, and see.

But given the time constraints of the problem, we need an efficient implementation.

Alternative Idea: Pre-sort the array and build a binary indexed tree for each possible value. But this is not feasible for n=2e5.

Thus, the segment tree is the way to go.

But in Python, even with the recursive approach, it may be too slow for n=2e5.

But let's proceed.

Once the segment tree is built, each query_leq(X, a, b) can be computed by recursively querying the tree and summing the counts.

Here's the code for the query:

def query_leq_x(node, a, b, x):
    if node['right'] < a or node['left'] > b:
        return 0
    if a <= node['left'] and node['right'] <= b:
        # Binary search in node['data'] for elements <= x
        return bisect.bisect_right(node['data'], x)
    return query_leq_x(node['left'], a, b, x) + query_leq_x(node['right'], a, b, x)

But in the current setup, the nodes are built with left and right children stored as separate objects. But in the code sketch above, the nodes are stored in a list, and the build function returns a node, which is added to the tree list. This approach may not be feasible for very large n.

Thus, the code needs to manage the nodes correctly.

But this is getting quite complex. Another Idea: Use a list-based approach where each node is stored as a dictionary with left, right, left_child, right_child, and data.

But for n=2e5, this would require a lot of memory.

Alternative Idea: Use a list of tuples to represent each node. But in Python, this may be challenging.

Alternatively, use a flat list where each node is stored in a specific order, and children are calculated based on indices. But this is also complex.

But for the purpose of passing the problem, let's proceed with the following code:

Implement a segment tree where each node is stored as a dictionary with left, right, and sorted data.

But in Python, recursion depth is a problem. For n=2e5, the build function's recursion depth will be O(log n), which is about 20, which is acceptable.

But let's proceed.

But in practice, for n=2e5, building the segment tree may take too much time and memory.

Alternative Idea: Pre-sort the p array and build a binary indexed tree (Fenwick tree) with the elements sorted. This way, we can use a binary indexed tree to count the number of elements <= X in a range [a, b].

But how?

This approach is known as a 'Wavelet Tree' or 'Range Tree'. The idea is to map the elements into their sorted order and use a binary indexed tree to track their positions.

But I'm not sure.

Alternatively, we can use a binary indexed tree for each possible value. But this is not feasible for large n.

Another Idea: Since the elements are unique (because the p array has all unique elements), but that's not the case. Wait, the problem states that the p array contains all unique elements. Because in the input description, it says "all pi are different".

So p is a permutation of 1..n.

So, for each query, D can be between 1 and n.

So for a query with D, the number of elements < D in a range is the number of elements in the permutation that are less than D and lie in that range.

But since the permutation is a bijection, the elements are 1..n.

So, for example, the count of elements < D in a range [a, b] is the number of elements in the range [a, b] whose value is < D.

But since the values are 1-based and unique, this is the same as counting how many elements in [a, b] are in the set {1, 2, ..., D-1}.

But how to compute this.

Ah! Since the p array is a permutation, each value from 1 to n is present exactly once. So for each value v, there's exactly one position i where p_i = v.

So, for each value v, we can create a list that maps v to its column i.

Then, for a query D, the count of elements < D in a range [a, b] is the number of values v in 1..D-1 that are in columns [a, b].

This is equivalent to the number of v in [1, D-1] such that their column i is in [a, b].

So the problem reduces to, for each query [a, b], count the number of values in [1, D-1] that are in the columns [a, b].

This is a 2D range query problem: count the number of points (v, i) where v is in [1, D-1] and i is in [a, b].

But since the points are (v, i), where v is the value of p_i, and i is the column, and all points are unique (each v is unique), we can pre-process a structure that allows us to answer this count.

This can be done with a 2D prefix sum array, but for n up to 2e5, this is not feasible.

Alternatively, we can use a binary indexed tree where we have the values sorted, and for each value, we track the columns.

But since the values are in 1..n, we can process them in sorted order.

Here's an alternative approach:

We can pre-process an array where for each value v, we store its column i.

Then, for a query [a, b] and D, the count of elements < D in [a, b] is the number of v in 1..D-1 that have i in [a, b].

So the problem becomes, for each query [1, D-1] in the values and [a, b] in the columns, count the number of elements that are in both ranges.

This can be modeled as a 2D range query, but for offline processing.

But since the queries are online, we need an online data structure.

An efficient way to do this is to use a binary indexed tree where each node represents a value v and stores the number of columns i <= a certain value. But since the values are sorted, we can build a binary indexed tree where the indices are the values, and the BIT stores the columns for each value.

But since the values are sorted, for a query [1, D-1], we can query the BIT up to index D-1, and find how many of them are in columns [a, b].

But how to compute the number of elements with value <= D-1 and column in [a, b].

This is the same as the count of elements where value is in [1, D-1] and column in [a, b].

To compute this, we can pre-process for each column i, store the value v = p_i. Then, for each v, we have a list of columns where it appears (only one, since p is a permutation).

Then, we can build a binary indexed tree (Fenwick tree) where for each v, we insert its column i into the BIT. Then, for a query [1, D-1], the total number of elements is the sum over v=1 to D-1 of the count of columns i in [a, b].

But how to compute this.

Each query is asking for the sum of 1's where v <= D-1 and i in [a, b].

This is equivalent to the number of v in [1, D-1] with i in [a, b].

So, to count this, we can use a 2D binary indexed tree, but that's complex.

Alternative Idea: For each column i, the value is v. We can create a list sorted by v, and for each v, store the column i. Then, for a query D, the values we need are [1, D-1], which is a prefix. For this prefix, we can find the columns in [a, b] using a binary search.

For example:

Sort all the (v, i) pairs in increasing order of v.

Then, for a query [1, D-1], the relevant entries are the first D-1 entries in this sorted list.

For each of these entries, we need to count how many have i in [a, b].

But how to compute this efficiently.

We can pre-process a sorted list of i's for each v. Then, for a query D, we can perform a binary search on the sorted list of i's for all v < D and count how many are in [a, b].

But this is again a range query on the sorted list of i's.

So, we can build a prefix array of sorted i's. For example, we can have an array sorted_v, which is sorted by v. The i's are stored in this array in the order of increasing v.

Then, build a prefix array of sorted i's, and for each prefix, build a binary indexed tree or a segment tree to answer range queries.

But this is complex.

Alternatively, build a binary indexed tree where each node represents a value v, and for each v, insert its column i into the BIT. Then, for a query [1, D-1], we can query the BIT up to D-1 and count how many i's are in [a, b].

But the problem is that the BIT stores cumulative sums. So we need a way to, for a given value range [1, D-1], compute how many columns are in [a, b].

This can be done using a segment tree or binary indexed tree that allows for range queries.

But combining the two ranges (v and i) is challenging.

Alternatively, for each column i, we can store its value v. We can then build a 2D range tree, where each node in the primary BIT is a segment tree on the columns. But this is complex.

But given the time constraints, perhaps this is the way to go.

So, here's the plan:

Pre-process the permutation p, which is a list of columns where p_i is the row for column i.

Since p is a permutation, the values are unique.

For each i in 1..n, store v_i = p[i].

Create a list of pairs (v_i, i) for i in 1..n.

Sort this list by v_i. Then, for the sorted list, the values are in order 1, 2, 3, ..., n.

Now, for each element in this sorted list, the i's are in the order of their values.

For example, the first element is the column i where p_i is 1.

We can build a prefix array of i's sorted by v.

Then, for a query D, the values less than D are the first D-1 elements in this sorted list.

For these elements, we need to count how many of their i's (columns) are in [a, b].

This is a classic range count problem on the sorted i's array.

So, the steps are:

- Sort the columns by their p_i values. So we have a sorted list of (v, i) pairs, ordered by v.

- Extract the i's from this sorted list into an array called 'sorted_i'. sorted_i[k] is the column i where the value v is k+1 (since it's sorted).

- Build a prefix sum array for sorted_i, where each prefix sum can answer the number of elements <= x in the first m elements.

But to query the number of elements in the first m elements of sorted_i that are in [a, b], we can use a segment tree built on sorted_i.

For example, for each m, we can have a segment tree that represents the first m elements. But this is not feasible.

Alternative Idea: Build a binary indexed tree where each element is added in the order of sorted_i. For each query D, the relevant elements are the first D-1 elements of sorted_i. Then, the count is the number of elements in [a, b] among these first D-1 elements.

This can be computed using a binary indexed tree that supports range queries.

So:

We process the sorted_i array in order. For each position k in sorted_i (which corresponds to v = k+1), we add sorted_i[k] to a binary indexed tree (Fenwick tree).

Then, for a query D, the number of elements in [a, b] is the number of elements added to the Fenwick tree up to index D-1 that are in [a, b].

But how to compute this.

A Fenwick tree can be used to answer range sum queries. For example, for the current elements in the Fenwick tree, the number of elements <= x is the sum up to x.

So, for the Fenwick tree that has all elements up to D-1 added, the number of elements in [a, b] is sum(b) - sum(a-1).

Thus, the steps are:

1. Sort the columns by v.

2. Create sorted_i as the array of columns in this order.

3. Build a Fenwick tree that can answer range queries [a, b] for the first k elements.

But the Fenwick tree is dynamic. Each element is added sequentially.

Thus, for the query D-1, the number of elements in [a, b] is the Fenwick tree's query for [a, b] after inserting the first D-1 elements.

But how to handle this.

This approach requires that the Fenwick tree can be reset and re-built for each query, which is not feasible.

But since the elements are added in the order of sorted_i, which is the sorted order of v, and the queries are processed online, this approach is not feasible.

Alternative Idea: Pre-process the sorted_i array and build a prefix sum array of binary indexed trees. For each k, have a Fenwick tree that includes the first k elements of sorted_i. But for n=2e5, this is not feasible in terms of memory.

Thus, this approach is not feasible.

Alternative Idea: Use a segment tree that is built on the sorted_i array. Each node of the segment tree represents a range of elements in the sorted_i array and stores a sorted list of the i's in that range. Then, for a query [D-1], we can query the first D-1 elements of the sorted_i array and count how many are in [a, b].

But building such a segment tree is possible.

Here's how:

The segment tree is built on the entire sorted_i array. Each node represents a range of the array indices (like 0 to n-1), and each node's data is a sorted list of the i's in its range.

Then, for a query of the first k elements (where k = D-1), we need to query the range [0, k-1] in the segment tree and count how many i's are in [a, b].

But this requires a segment tree that can process a query [0, k-1] and return the count of elements in [a, b] within that range.

This is possible by traversing the segment tree and for each node that is fully contained within the query range, performing a binary search on its sorted list to count the elements in [a, b].

Thus, the query for the first k elements can be transformed into a range query [0, k-1] on the segment tree, and the count of i's in [a, b].

This approach allows us to answer the required count for any D, a, and b.

Thus, this is the way to go.

So the steps are:

1. Sort the columns by their p_i values to get sorted_i.

2. Build a segment tree where each node represents a range of indices in sorted_i and stores a sorted list of the i's in that range.

3. For a query D, the number of elements with v < D is k = D-1. We need to query the first k elements of sorted_i (indices 0 to k-1) and count how many of them are in [a, b].

This can be done using the same segment tree.

Thus, this approach can be used to answer query_leq(D-1, a, b) as the count of elements in the first D-1 elements of sorted_i that are in [a, b].

But sorted_i is ordered by v, which is 1, 2, 3, ..., n.

Wait, sorted_i is the list of columns sorted by their p_i values in increasing order. Since p is a permutation, the sorted_i array will be ordered as follows: the first element is the column with p_i=1, the second is the column with p_i=2, etc., up to the last element with p_i=n.

So the first D-1 elements of sorted_i are precisely the columns with p_i < D.

Thus, for a query_leq(D-1, a, b), we need to count the number of columns in the first D-1 elements of sorted_i that are in [a, b].

This can be done by querying the segment tree for the range [0, D-2] (since it's 0-based) and counting the number of elements in [a, b].

But wait, the segment tree is built on the entire sorted_i array, and each node represents a range of indices in the sorted_i array. So the segment tree is built to answer range queries on the sorted_i array's indices.

Thus, for query_leq(D-1, a, b), it's equivalent to querying the segment tree for the range [0, D-2] (if D-1 >=0) and counting the number of elements in [a, b].

But in the segment tree, each node's data is a sorted list of the i's (columns) in the node's range. So when we query the segment tree for the range [0, k], where k is D-2, and count the number of elements in [a, b], it will give us the number of columns in the first D-1 elements of sorted_i that are between a and b.

Thus, this approach works.

Similarly, for query_gt(U, a, b), since the elements are sorted in increasing order of v, the elements with v > U are the elements from the (U)th position to the end of sorted_i.

For example, for U=5, the elements with v > 5 are those in positions 5, 6, ..., n-1 in sorted_i.

Thus, query_gt(U, a, b) is the number of elements in sorted_i[U ... n-1] that are in [a, b].

Thus, query_gt(U, a, b) can be computed as query_segment_tree(U, n-1, a, b).

Thus, this approach can handle both query_lt and query_gt.

Thus, the plan is:

- Preprocess sorted_i by sorting the columns in increasing order of p_i.

- Build a segment tree on sorted_i, where each node stores a sorted list of the columns in its range.

- For query_leq(D, a, b):

   If D <= 0, return 0.

   Else, k = D-1.

   If k <0, return 0.

   Query the segment tree for the range [0, k] and count the number of elements in [a, b].

- For query_gt(U, a, b):

   k = U.

   Query the segment tree for the range [k, n-1] and count the number of elements in [a, b].

Thus, this approach can handle all the required queries.

Now, the code for the segment tree and the queries:

Implementing the segment tree:

In Python, we can build the segment tree recursively. Each node represents a range of indices in the sorted_i array and stores a sorted list of the i's (columns) in that range.

The build function:

def build_segment_tree(l, r):
    node = {'left': l, 'right': r, 'data': []}
    if l == r:
        node['data'] = [sorted_i[l]]
    else:
        mid = (l + r) // 2
        node['left_child'] = build_segment_tree(l, mid)
        node['right_child'] = build_segment_tree(mid+1, r)
        node['data'] = merge(node['left_child']['data'], node['right_child']['data'])
    return node

Where merge is the function to merge two sorted lists.

But again, for large n, building this recursively may be slow.

But given the time constraints, perhaps we can proceed.

Then, the query function:

def query_segment_tree(node, l, r, a, b):
    if node['right'] < l or node['left'] > r:
        return 0
    if l <= node['left'] and node['right'] <= r:
        # count elements in [a, b] in node['data']
        return bisect.bisect_right(node['data'], b) - bisect.bisect_left(node['data'], a)
    return query_segment_tree(node['left_child'], l, r, a, b) + query_segment_tree(node['right_child'], l, r, a, b)

This function returns the number of elements in the segment tree node's data that are in [a, b].

Now, for query_leq(D, a, b):

if D <= 0:
    return 0
k = D -1
if k <0:
    return 0
if k >= len(sorted_i):
    k = len(sorted_i)-1
return query_segment_tree(root, 0, k, a, b)

For query_gt(U, a, b):

k = U
if k >= len(sorted_i):
    return 0
return query_segment_tree(root, k, len(sorted_i)-1, a, b)

But in code, we need to ensure that the ranges are correct.

Thus, with this approach, the segment tree is built once, and each query is answered in O(log n) time.

Thus, this is feasible for the problem's constraints.

Now, putting it all together:

Read n and q.

Read p as a list (1-based index).

sorted_i is the list of columns sorted by their p_i values.

So, for example, sorted_i = sorted(range(1, n+1), key=lambda x: p[x-1])

But since p is 1-based in the problem, but Python lists are 0-based. So for i in 0..n-1, p[i] is the row for column i+1.

So, columns are 1-based. So to create sorted_i:

columns = list(range(1, n+1))

sorted_columns = sorted(columns, key=lambda x: p[x-1])

sorted_i = sorted_columns

So sorted_i is a list of columns ordered by their p_i values in increasing order.

Build the segment tree with this sorted_i.

Then, for each query L, R, D, U:

Compute C as described.

Compute S1:

A1 = query_leq(D-1, 1, L-1) → query the first D-1 elements of sorted_i, and count how many are in [1, L-1].

But wait, the columns are in sorted_i, and we need to count how many of the first D-1 elements have columns in [1, L-1].

Thus:

A1 = query_segment_tree(root, 0, D-2, 1, L-1)

But D can be 1, which would make D-1 = 0. So we need to handle D=1, which means k = D-1-1 = -1, which is invalid. So need to clamp k to >=0.

Wait, query_leq(D-1, a, b) is the number of elements in the first D-1 elements of sorted_i (which are the elements with p_i < D) that are in [a, b].

So for A1:

A1 = query_segment_tree(root, 0, D-2, 1, L-1)

But if D-1 is 0 (D=1), then D-2 is -1. So in that case, A1 is 0.

Similarly for other queries.

Thus, the code for S1:

A1 = 0

if D > 1:

    k = D-2

    A1 = query_segment_tree(root, 0, k, 1, L-1)

B = query_segment_tree(root, 0, D-2, L, n)

k = query_segment_tree(root, 0, D-2, L, R)

S1 = A1 * B + k * (k-1) // 2

Similarly for S2.

But this is not correct. Because the segment tree's query is for the first D-1 elements of sorted_i, which are the columns with p_i < D. So to compute B, which is the number of columns >= L and <=n in the first D-1 elements, we need to query the segment tree for the first D-1 elements in sorted_i and count how many are in [L, n].

So:

B = query_segment_tree(root, 0, D-2, L, n)

k = query_segment_tree(root, 0, D-2, L, R)

But again, if D-1 is 0, then B and k are 0.

Similarly for S2:

A1_part = query_gt(U, 1, L-1)

Which is the number of elements with p_i > U in the columns [1, L-1].

But p_i > U is equivalent to the elements in sorted_i that are in the range [U+1, n] of their values. So the columns in sorted_i from index U onwards have p_i > U.

Thus, to compute A1_part, we query the segment tree for the range [U, n-1] and count how many of those are in [1, L-1].

But A1_part is the number of columns in [1, L-1] that have p_i > U.

Thus:

A1_part = query_segment_tree(root, U, n-1, 1, L-1)

B_prime = query_segment_tree(root, U, n-1, L, n)

k_prime = query_segment_tree(root, U, n-1, L, R)

S2 = A1_part * B_prime + k_prime * (k_prime - 1) // 2

Thus, this approach is correct.

Now, the code can be written.

But in Python, recursion depth may be a problem for building the segment tree. So an alternative approach is to build the segment tree iteratively.

But given time constraints, perhaps it's better to proceed with the recursive approach and see.

Now, let's write the code.

But for code submission, the code must read from stdin and write to stdout.

But due to time constraints, the code may need to be optimized. For example, using a more efficient merge function, using bisect, etc.

But here's the code outline:

Read n, q.

Read p as a list.

Sort the columns in increasing order of p_i to get sorted_i.

Build a segment tree where each node's data is a sorted list of the columns in its range.

For each query:

   Read l, d, r, u.

   L = l

   R = r

   D = d

   U = u

   Compute C.

   Compute S1.

   Compute S2.

   Answer = C - S1 - S2.

   Print(answer)

Now, implementing the segment tree.

But in Python, recursive depth is limited. So for n=2e5, the build function may hit recursion depth issues.

Thus, an iterative approach is needed.

Alternatively, increase the recursion depth.

But in Python, the default recursion depth is around 1e4, which is enough for log2(2e5) = 18.

Thus, the recursive build should be acceptable.

But let's proceed.

The code:

import sys
import bisect

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged

def build_segment_tree(l, r, sorted_data):
    if l == r:
        return {'left': l, 'right': r, 'data': [sorted_data[l]]}
    mid = (l + r) // 2
    left_child = build_segment_tree(l, mid, sorted_data)
    right_child = build_segment_tree(mid+1, r, sorted_data)
    node_data = merge(left_child['data'], right_child['data'])
    return {'left': l, 'right': r, 'data': node_data, 'left_child': left_child, 'right_child': right_child}

def query_segment_tree(node, l, r, a, b):
    if node['right'] < l or node['left'] > r:
        return 0
    if l <= node['left'] and node['right'] <= r:
        left_pos = bisect.bisect_left(node['data'], a)
        right_pos = bisect.bisect_right(node['data'], b)
        return right_pos - left_pos
    return query_segment_tree(node['left_child'], l, r, a, b) + query_segment_tree(node['right_child'], l, r, a, b)

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    q = int(input[ptr])
    ptr += 1
    p = list(map(int, input[ptr:ptr+n]))
    ptr += n

    # Create sorted_i as columns sorted by p_i in increasing order
    columns = list(range(1, n+1))
    sorted_columns = sorted(columns, key=lambda x: p[x-1])

    # Build the segment tree
    root = build_segment_tree(0, n-1, sorted_columns)

    for _ in range(q):
        l = int(input[ptr])
        ptr += 1
        d = int(input[ptr])
        ptr += 1
        r = int(input[ptr])
        ptr += 1
        u = int(input[ptr])
        ptr += 1

        L = l
        R = r
        D = d
        U = u

        # Compute C
        if L > R:
            C = 0
        else:
            sum1 = R * (R-1) // 2
            if L > 1:
                sum1 -= (L-1) * (L-2) // 2
            sum2 = max(0, n - R) * R
            C = sum1 + sum2

        # Compute S1
        S1 = 0
        if D > 1:
            k = D - 1
            # A1: number of columns in [1, L-1] with p_i < D
            # query first k-1 elements (D-1 elements are 0..k-1)
            # sorted_i[0..k-1] are p_i < D
            if k-1 >= 0:
                A1 = query_segment_tree(root, 0, k-1, 1, L-1)
                B = query_segment_tree(root, 0, k-1, L, n)
                k_count = query_segment_tree(root, 0, k-1, L, R)
                S1 = A1 * B + k_count * (k_count - 1) // 2
            else:
                S1 = 0
        else:
            S1 = 0

        # Compute S2
        S2 = 0
        # A1_part: number of columns in [1, L-1] with p_i > U
        # query elements from U to n-1 in sorted_i (sorted by p_i)
        # and columns are in [1, L-1]
        # U+1 to n are p_i > U
        # sorted_i starts from p_i=1 to p_i=n
        if U < n:
            start = U
            end = n-1
            A1_part = query_segment_tree(root, start, end, 1, L-1)
            B_prime = query_segment_tree(root, start, end, L, n)
            k_prime = query_segment_tree(root, start, end, L, R)
            S2 = A1_part * B_prime + k_prime * (k_prime - 1) // 2
        else:
            S2 = 0

        answer = C - S1 - S2
        print(answer)

if __name__ == "__main__":
    main()

But there's a mistake here. The sorted_columns are sorted by p_i in increasing order. So the first element is the column with p_i=1, the next with p_i=2, etc.

Thus, for a query where we need elements with p_i < D, we take the first D-1 elements (0-based indices 0 to D-2).

For example, if D=3, the elements with p_i < 3 are the first two elements (p_i=1 and 2).

Thus, the query for S1 is correct.

Similarly, for S2, elements with p_i > U are those in the sorted_columns starting from index U.

But if U=4, sorted_columns[4] has p_i=5, sorted_columns[5] has p_i=6, etc.

Thus, the query for S2 is correct.

But let's test the first sample input.

Sample Input 1:

2 3

1 2

1 1 1 1

1 1 1 2

1 1 2 2

The p array is [1, 2], so sorted_columns is [1, 2], since p_1=1, p_2=2.

The first query is L=1, R=1, D=1, U=1.

For S1:

D=1, so D-1=0. Thus, no elements, S1=0.

For S2:

U=1. The elements with p_i > 1 are those with p_i=2, which is the second element in sorted_columns (index 1).

So start = U =1, end=1.

A1_part is query_segment_tree(root, 1, 1, 1, 0) (since L=1, L-1=0), which is 0.

B_prime is query_segment_tree(root, 1,1,1,2) → count of elements in [1,2] for the element at index 1 (column 2, which is 2). So B_prime=1.

k_prime is query_segment_tree(root, 1,1,1,1) → 1 if column 2 is in [1,1]. But column 2 is 2, which is outside [1,1]. So k_prime=0.

Thus, S2=0 * 1 + 0 = 0.

Thus, answer = C - 0 -0 = C.

What's C?

L=1, R=1.

sum1 = 1*(1-1)/2 - 0 (since L=1, L-1=0, (0-1)*(0-2)/2 is 0).

sum1 = 0.

sum2 = max(0, 2-1) * 1 → (1)*1 = 1.

C=0+1=1.

Thus, answer is 1, which matches the sample.

Thus, the code seems to work.

But in practice, for large n, the segment tree building may take a lot of time and memory.

But given the problem's constraints, this approach is the best possible and should pass.

But in Python, for n=2e5, building the segment tree recursively may be slow.

Thus, for the code to pass, we need to optimize the segment tree building.

But given the time and memory constraints, this is the correct approach.
</think>

To solve this problem, we need to determine the beauty degree of each query rectangle on a grid where certain cells are marked such that no two marked cells share the same row or column. The beauty degree is the number of beautiful rectangles that intersect the query rectangle. A beautiful rectangle is defined as having exactly two marked cells as opposite corners.

### Approach
1. **Problem Analysis**: 
   - A beautiful rectangle is formed by two marked cells (i, p_i) and (j, p_j) where i < j. This rectangle spans columns from i to j and rows from min(p_i, p_j) to max(p_i, p_j).
   - For each query, we need to count how many such beautiful rectangles overlap with the query rectangle.

2. **Key Insights**:
   - The problem can be split into counting pairs of columns (i, j) that meet specific conditions related to the query rectangle.
   - Efficient range queries using a segment tree allow us to count elements in specific ranges quickly.

3. **Algorithm**:
   - **Segment Tree**: Preprocess the columns sorted by their row values to efficiently count elements in specific ranges.
   - **Query Processing**: For each query, compute the number of valid pairs using the segment tree to handle range queries efficiently.

### Solution Code
```python
import sys
import bisect

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged

def build_segment_tree(l, r, sorted_data):
    if l == r:
        return {'left': l, 'right': r, 'data': [sorted_data[l]]}
    mid = (l + r) // 2
    left_child = build_segment_tree(l, mid, sorted_data)
    right_child = build_segment_tree(mid+1, r, sorted_data)
    node_data = merge(left_child['data'], right_child['data'])
    return {'left': l, 'right': r, 'data': node_data, 'left_child': left_child, 'right_child': right_child}

def query_segment_tree(node, l, r, a, b):
    if node['right'] < l or node['left'] > r:
        return 0
    if l <= node['left'] and node['right'] <= r:
        left_pos = bisect.bisect_left(node['data'], a)
        right_pos = bisect.bisect_right(node['data'], b)
        return right_pos - left_pos
    return query_segment_tree(node['left_child'], l, r, a, b) + query_segment_tree(node['right_child'], l,