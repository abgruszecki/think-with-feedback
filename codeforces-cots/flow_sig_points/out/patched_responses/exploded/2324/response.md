<think>
Okay, so I need to solve this problem where Petya wants to swap two elements in a permutation such that the number of swaps (as per the insertion sort algorithm) is minimized. And then I have to find the number of such pairs that achieve this minimal value. 

First, I should understand how insertion sort works and how many swaps it performs for a given permutation. Insertion sort, as I remember, works by iterating through each element and moving it backward until it's in the correct position. The number of swaps for each element is equal to the number of elements before it that are greater than it. So the total number of swaps is the sum of these for all elements.

Wait, right. For each element, the number of swaps during insertion sort is the number of elements to the left that are greater than the current element. So the total swaps count is the sum of all those individual counts. So first, I need to compute the original number of swaps for the given permutation. Then, when we swap two elements, I need to find how this swap affects the total number of swaps, and find the pair that gives the maximum possible reduction (or minimal total swaps) and count all such pairs.

But how to compute the effect of swapping two elements efficiently?

Let's think. The original number of inversions (the sum) can be computed straightforwardly. Now, when we swap elements a[i] and a[j], how does this affect each element's contribution to the total swap count?

Wait, the total swaps for insertion sort is equal to the number of inversions in the array. Because each inversion (a pair i < j where a[i] > a[j]) represents a swap that needs to happen. Wait, no. Wait, insertion sort's number of swaps is exactly the number of inversions. Because for each element, the number of elements to the left that are larger than it is the number of swaps that element will undergo. Summing all of these gives the total number of inversions. So the problem is equivalent to finding a pair of elements to swap such that the number of inversions in the new array is minimized, and then find the number of such pairs.

Wait, but the problem statement says that the swap must decrease the number of swaps (inversions). And the task is to find the minimal possible swap count after exactly one swap, and how many pairs achieve that.

So the problem reduces to: given a permutation, find the pair (i,j) such that swapping a[i] and a[j] reduces the inversion count as much as possible, and then return the minimal inversion count after swap, and the number of such pairs.

But how to compute the change in inversions when swapping two elements?

Hmm. Let's denote the original array as A. The inversion count is inv.

When we swap A[i] and A[j], the new array is B. We need to compute inv' = number of inversions in B.

But computing inv' directly for every possible pair (i,j) would be O(n^2) for each pair, which for n=5000 would be O(25 million) operations. But each inversion count for a pair would take O(n^2) time, leading to O(25e6 * 25e6) operations, which is way too slow. So this approach is not feasible.

We need a smarter way to compute how the inversion count changes when two elements are swapped.

Let's think about what happens when we swap elements at positions i and j (assuming i < j, but the code can handle all pairs). Let's first assume that i < j. Let x = A[i], y = A[j]. After swapping, B[i] = y, B[j] = x.

The inversion count change is inv' = inv - delta + delta_new, where delta is the number of inversions removed by swapping x and y, and delta_new is the number of new inversions introduced.

Alternatively, the total change is inv' = inv - (original inversions involving x and y) + (new inversions created after swapping).

But this seems complicated. Let's break it down.

The original array has certain inversions. When we swap x and y, some inversions are removed and others are added.

The steps to compute the change in inversions when swapping x and y (positions i and j, i < j) are:

1. Consider all elements before i, between i and j, and after j.

We need to calculate how many inversions are affected by swapping x and y.

Let's think about the elements in the array. For each position k, how does swapping x and y affect the inversion count.

But maybe there's a formula that can compute delta, the difference in inversion count, as a function of x, y, i, j, and their positions.

Let me think: after swapping, the positions i and j now have elements y and x.

The inversions can be divided into several parts:

a) Inversions that involve elements other than i and j: these could change if the elements in i or j affect them.

b) Inversions between elements in i and j, and the rest of the array.

So let's first compute the original number of inversions contributed by x and y, and then compute how that changes after swapping.

Alternatively, perhaps we can compute the delta as follows:

Original inversions between x and elements in the array: x is at position i. So all elements to the left of i that are > x contribute to the original inversion count. Also, elements to the right of i that are < x contribute.

Wait, perhaps it's better to split the problem into parts.

Original inversion count is inv.

When we swap x and y, the new inversion count inv' can be computed as inv minus the number of inversions that are lost due to swapping x and y plus the number of inversions that are added.

So to compute delta = inv' - inv, we can calculate delta = (new_inv - old_inv) = (added_inversions - removed_inversions).

So the problem is to find the delta for each possible swap (i,j) and find the swap that gives the minimal inv' (i.e., the delta is as negative as possible).

The goal is to find the minimal possible inv' (which is inv + delta), and count all pairs (i,j) where delta is as minimal as possible.

So how do we compute delta for each possible (i,j) pair efficiently?

Let's think about the elements x = A[i], y = A[j]. After swapping, they are at positions i and j, respectively.

Original contributions from x and y:

For x (at position i):

- All elements before i that are > x contribute to inversions (counted as part of the original inv).

- All elements after i that are < x contribute to inversions (since x is after them and is smaller, so if an element at position k > i has A[k] < x, then (i,k) is an inversion).

Similarly for y (at position j):

- Elements before j that are > y.

- Elements after j that are < y.

After swapping:

The new x is at position j, and the new y is at position i.

So, for the new positions:

For the new x (originally y) at j:

- Elements before j that are > x (i.e., > y).

- Elements after j that are < x (i.e., < y).

For the new y (originally x) at i:

- Elements before i that are > y (i.e., > x).

- Elements after i that are < y (i.e., < x).

But this seems complicated. Perhaps there's a way to model the change in inversions when swapping two elements.

Let me think of delta as the difference between the new and old inversion counts.

So, delta = (number of inversions in B) - (number of inversions in A) = (inv' - inv).

We need to compute delta for each possible swap (i,j).

But how?

An alternative approach: delta can be computed by considering all possible pairs (k,l) in the array and see how their order changes after the swap.

But this is again O(n^2) for each swap, which is O(n^4) overall, which is way too slow.

We need a way to compute delta in O(1) or O(n) per swap.

Another idea: the delta can be broken down into parts based on the positions and elements involved.

Let me consider the swap of elements x and y at positions i and j (i < j). Let's assume i < j for now.

In the original array, the elements are x at i and y at j.

After swapping, elements are y at i and x at j.

The change in inversions can be broken down into several components:

1. Inversions between x and the elements in the ranges [0, i-1], (i+1, j-1), [j+1, n-1].

Similarly for y.

Alternatively, perhaps the following formula can be derived:

The delta can be computed as the sum of:

- The number of elements between i and j that are in between x and y, considering their new positions.

Wait, maybe this is a known formula. Let me think.

The change in inversions when swapping elements at positions i and j can be calculated using the following approach:

The original inversions involving x and y:

- For x (A[i]), the elements before i that are larger than x contribute to inversions. The elements after i that are smaller than x also contribute.

Similarly for y (A[j]).

After swapping, the new elements at i and j are y and x. So, for the new elements, the inversions involving i and j.

But perhaps the delta can be calculated as follows:

Original contributions from x and y:

Total inversions involving x in original array: (number of elements before i that are > x) + (number of elements after i that are < x).

Similarly for y: (elements before j that are > y) + (elements after j that are < y).

After swapping, the new contributions from y (now at i) and x (now at j):

For y at i: (number of elements before i that are > y) + (elements after i that are < y).

For x at j: (elements before j that are > x) + (elements after j that are < x).

So the delta is:

[new_contributions - original_contributions] + [other inversions that are affected by the swap].

But this is not sufficient. Because swapping x and y can also affect inversions between other elements. For example, consider an element z that is between i and j. If z is between x and y in value, swapping x and y might create new inversions between z and the new elements at i and j.

So the main problem is to account for all the pairs that involve elements in the array except i and j, but are affected by the swap.

Let me try to model this.

The delta can be split into two parts:

1. The change in inversions due to the elements x and y themselves (the direct effect).

2. The change in inversions due to other elements in the array that form pairs with x and y (the indirect effect).

Wait, perhaps the delta can be computed as follows:

Original inversions between x and elements in the array (other than y) and between y and elements in the array (other than x), plus the inversion between x and y (if x > y).

After swapping, the inversions between y and other elements (other than x) and between x and other elements (other than y), plus the inversion between y and x (if y > x).

Then, we also need to account for the inversions between other elements (not x or y) that involve the positions i and j. Wait, but swapping x and y could affect elements that are in between i and j. For example, if there's an element z between i and j. When x and y are swapped, z's relation to x and y could change.

Alternatively, perhaps the delta can be broken down into:

delta = (after swap) - (before swap) = [ (inversions not involving i or j) + (inversions involving i or j) ] - [ (original inversions) ]

But the inversions not involving i or j would remain the same, except for those that involve elements between i and j.

Wait, this is getting complicated. Let me try to find a formula.

The key idea is that when we swap two elements x and y at positions i and j (i < j), the inversion count delta is equal to:

delta = (number of elements between i and j that are between x and y in value) * 2 - (j - i - 1) - (x < y ? 1 : -1) )

But I'm not sure. Let me look for references.

Upon some research, I recall that there's a formula for the change in inversion count when swapping two elements. Let me try to derive it.

Suppose we have two elements x and y at positions i and j (i < j). After swapping, the inversion count changes by:

delta = (number of elements in the range (i, j) that are between x and y) * 2 - (j - i - 1) + (x < y ? -1 : 1) )

Wait, here's a possible approach:

The change in inversion count when swapping x and y can be computed as follows:

Original inversions between x and elements in the array: count of elements before i that are larger than x (contributing to inversions), plus elements after i (including j) that are smaller than x.

Similarly for y: elements before j that are larger than y, plus elements after j that are smaller than y.

After swapping:

For x now at j:

elements before j that are larger than x (including the new element y at i), plus elements after j that are smaller than x.

For y now at i:

elements before i that are larger than y, plus elements after i (including j) that are smaller than y.

But this is getting too detailed. Maybe there's a better way.

Alternatively, the delta can be calculated as follows:

The inversion count after swapping is equal to:

original_inversions - (number of inversions involving x and elements between i and j) - (number of inversions involving y and elements between i and j) + (number of new inversions after the swap between y and elements between i and j) + (number of new inversions after the swap between x and elements between i and j) + (if x > y then -1 else 1) )

But this is not precise.

Another approach: Let's consider all pairs (k, l) where k < l. The inversion is if a[k] > a[l]. After swapping a[i] and a[j], we need to see how this affects each pair.

But for pairs (k, l) that do not involve i or j, the swap has no effect. So only pairs that include i or j, or both, can be affected.

Wait, but even this: if k is in [0, i-1] and l is in [i+1, j-1], then the elements a[k] and a[l] are not swapped, but the elements at i and j may affect pairs where one is in i or j.

So the delta can be calculated by considering all pairs that involve i or j, or lie between them.

Alternatively, we can split the problem into three parts:

1. Inversions where one of the elements is at position i or j.

2. Inversions where both elements are between i and j.

3. Inversions involving elements outside the i and j ranges.

Wait, maybe it's better to model the delta as follows:

When we swap elements at positions i and j (i < j), the change in inversions can be computed by considering the following:

- All pairs (i, k) for k in [i+1, j-1] and (k, j) for k in [i+1, j-1].

- The pair (i, j) itself.

- All pairs (k, i) for k < i and (j, l) for l > j.

- All pairs (k, j) for k < i and (j, l) for l > j.

This seems complicated, but perhaps we can find a way to compute delta by considering:

- The original relations between x (a[i]) and the elements between i and j.

- The original relations between y (a[j]) and the elements between i and j.

- The original relation between x and y.

Then, after swapping, these relations change.

Let me think:

Original array: x is at i, y is at j.

After swapping: y is at i, x is at j.

The elements between i and j (call them the segment S) are the elements at positions i+1 to j-1.

For each element z in S, in the original array:

- If x > z, then (i, z's position) is an inversion.

After swapping, the element at i is y. So if y > z, then (i, z's position) is an inversion.

So for each z in S, the contribution to delta is: (if y > z) - (x > z) ?

Similarly, for each z in S, in the original array, (z's position, j) is an inversion if z > y.

After swapping, the element at j is x, so (z's position, j) is an inversion if z > x.

So for each z in S, the contribution is (z > x) - (z > y).

Additionally, the pair (i, j) in the original array contributes 1 if x > y, and 0 otherwise. After swapping, it contributes 1 if y > x. So the delta here is ( (y > x) - (x > y) ).

So combining these contributions:

delta = [sum over z in S ( (y > z) - (x > z) + (z > x) - (z > y) ) ] + ( (y > x) - (x > y) )

Let me simplify this sum term.

For each z in S:

(y > z) - (x > z) + (z > x) - (z > y) 

Let me rearrange the terms:

[ (y > z) + (z > x) ] - [ (x > z) + (z > y) ]

But (y > z) + (z > x) is equal to (y > z or z > x) if there's no overlap. Wait, not exactly. For example, if x < z < y, then (y > z) is true and (z > x) is true, so their sum is 2. But in the original scenario, x and y could be in any order.

Alternatively, perhaps this sum can be rewritten as (y > z) - (x > z) + (z > x) - (z > y) = (y > z - x > z) + (z > x - z > y) ?

Wait, perhaps we can combine terms:

(y > z) - (x > z) = (y > z) ? 1 : 0 minus (x > z ? 1 : 0). So this is 1 if y>z and x <= z, 0 if both or neither, etc.

Similarly, (z > x) - (z > y) = 1 if z >x and z <=y, etc.

But perhaps there's a way to find a pattern here.

Let's consider four cases based on the value of z relative to x and y.

Case 1: z < min(x, y)

Then:

(y > z) is true (1), (x > z) is true (1), so (y>z - x>z) is 0.

(z >x) is false (0), (z>y) is false (0), so (z>x - z>y) is 0.

So sum for this z: 0 + 0 = 0.

Case 2: z is between x and y. Suppose x < z < y.

Then:

(y>z is true (1), x>z is false (0). So difference is 1.

(z >x is true (1), z>y is false (0). Difference is 1.

Total for this z: 1 + 1 = 2.

Case 3: z > max(x, y).

(y>z is false (0), x>z is false (0). Difference is 0.

(z>x is true (1), z>y is true (1). Difference is 0.

Sum is 0.

Case 4: z is between y and x. Suppose y < z < x.

Then:

(y>z is false (0), x>z is true (1). Difference is -1.

(z >x is false (0), z>y is true (1). Difference is -1.

Sum is -2.

So combining these:

For each z in S, the contribution is:

if z < min(x, y) → 0.

if z is between x and y (assuming x < y) → 2.

if z > max(x, y) → 0.

if z is between y and x (assuming y < x) → -2.

So the sum over S is 2 * (number of elements in S between x and y) if x < y, or -2 * (number of elements between y and x) if x > y.

But wait, the sum for all z in S is 2 * (count of z in S where (x < z < y)) if x < y, or -2 * (count of z in S where (y < z < x)) if x > y.

So this sum is equal to 2 * (c) if x < y, where c is the number of elements in S between x and y. Or 2 * (-d) if x > y, where d is the number of elements in S between y and x.

Alternatively, the sum can be written as 2 * ( (x < y) ? (count of z in S where z is in (x, y)) : - (count of z in S where z is in (y, x)) ) )

So the sum over S is 2 * ( (x < y) ? (number of elements in S between x and y) : - (number of elements in S between y and x) ) )

Then, the delta is this sum plus ( (y > x) - (x > y) )

Because the pair (i, j) contributes 1 if x>y before the swap, and 1 if y>x after the swap. So the change is (y > x) - (x > y) which is equal to 1 if y >x, -1 if x>y.

So putting it all together:

delta = 2 * (number of elements in S between min(x,y) and max(x,y)) * (1 if x < y else -1) ) + (1 if y > x else -1)

Wait, no. Let's think:

If x < y:

sum_S = 2 * c, where c is the number of elements in S between x and y.

plus (y > x) is true → 1. So delta = 2c + 1.

Wait, no:

Wait, for x < y:

sum_S is 2c, and (y >x) → 1. So (y >x) - (x > y) is 1 - 0 = 1.

So delta is sum_S (which is 2c) plus 1.

If x > y:

sum_S is -2d, where d is the number of elements in S between y and x.

And (y >x) is false, so (y> x) - (x> y) is 0-1= -1.

So delta = sum_S + (-1) → -2d -1.

So overall:

delta = (x < y) ? (2 * c + 1) : (-2 * d -1 )

But wait, in the case where x < y, the sum_S is 2c, and the (y> x) - (x> y) is 1. So delta = 2c + 1.

In the case where x > y, sum_S is -2d, and (y> x) - (x> y) is -1. So delta = -2d -1.

But what is c and d in terms of x and y?

In the case x < y:

c is the number of elements in S (i.e., between positions i and j) that are between x and y. So elements z where x < z < y.

In the case x > y:

d is the number of elements z in S where y < z < x.

So the delta can be calculated as:

delta = (if x < y) (2 * (number of elements in S between x and y) +1) 

else ( -2 * (number of elements in S between y and x) -1 )

Additionally, when i > j, we can swap i and j, so the positions are always ordered.

So the steps to compute delta for a pair (i, j) (possibly with i > j) are:

1. Swap i and j if needed to ensure i < j.

2. x = a[i], y = a[j].

3. Compute the number of elements in the range (i, j) (positions i+1 to j-1) that are between min(x, y) and max(x, y).

4. If x < y:

delta = 2 * count + 1

else:

delta = -2 * count -1 

But wait, the delta is the change in inversion count. So when we swap elements, the new inversion count is original_inversion + delta.

Wait, no. Because delta is (new_inv - old_inv). So if delta is positive, the new inversion count is higher. So to minimize the inversion count after the swap, we need to find the delta that is as negative as possible.

But the problem says that Petya wants to swap two elements such that the number of swap function calls is minimized. So the minimal possible inversion count after the swap.

So for each pair (i,j), compute delta and find the pair with the minimal (original_inv + delta).

But original_inv is the same for all pairs, so we can compute the minimal (delta) and find which pairs give the most negative delta.

Thus, the problem reduces to finding the minimal delta (since original_inv is fixed) and then count all pairs (i,j) that achieve this delta.

So now the challenge is to compute delta for all possible pairs (i,j) efficiently.

But how?

For n=5000, there are about 12.5 million pairs (since n*(n-1)/2 for 5000 is about 12,497,500). So we need an O(1) or O(n) per pair approach.

Let's see: For each pair (i,j), we need to compute:

count = number of elements in S (positions between i and j) that are between x and y.

But even this, if we can compute count efficiently for all pairs, then delta can be computed.

But how?

Another idea: For all pairs (i,j), precompute for each possible i and j the count of elements between them that are in the range (min(x,y), max(x,y)).

But for n=5000, this would be O(n^2) operations. Which is 25 million, which is manageable.

But how to compute the count efficiently.

One way is for each pair (i,j), iterate over all elements between i and j and count those that are in the interval. But for j-i up to 5000, this is O(n^3), which is 125e9 operations, which is way too slow.

So this approach is not feasible.

We need a better way to compute, for any i < j, the number of elements between i and j (positions i+1 to j-1) that are between x and y (where x is a[i], y is a[j]).

So the problem is: for a given interval (i, j) and values x and y (a[i] and a[j]), count the number of elements in positions i+1 to j-1 that lie in the interval (min(x,y), max(x,y)).

But how to compute this quickly for all i < j.

Hmm.

An alternative approach is to precompute for each element, its position. Since it's a permutation, each value corresponds to exactly one position.

So pos[v] is the index of value v.

But I'm not sure how that helps.

Another idea: For each pair (i,j) where i < j:

x = a[i], y = a[j].

min_val = min(x, y)

max_val = max(x, y)

We need to count the number of elements in a[i+1..j-1] that are in (min_val, max_val).

But how to compute this efficiently.

This is equivalent to a range query problem. For each query [L, R], find the number of elements in the subarray a[L..R] that are in the range (A, B), where A and B are parameters that vary per query.

But with L and R varying (since for each pair i,j, L is i+1, R is j-1), and A and B vary as min(x,y) and max(x,y), this is a difficult problem.

To answer these range queries efficiently, we need a data structure that allows us to compute the count of elements in a subarray within a certain range.

One possible approach is to use a 2D prefix sum array, where for each position and value, we have a prefix sum. But with n=5000, a 2D array of 5000x5000 is 25 million entries, which is manageable.

Alternatively, we can precompute for each value v, a prefix array that tells us how many times v appears up to each position. But for ranges, it's better to have a 2D array where cnt[i][j] is the number of elements <= j in the first i elements.

But building a prefix sum for all possible values (since values are up to n-1) would take O(n^2) space. For n=5000, this is 25 million entries, which is manageable.

But building such a prefix sum array:

We can create a 2D array where prefix[k][v] is the number of elements in the first k elements (0..k-1) that are <= v.

Then, for any range [L, R], the number of elements in [L, R] that are between (A, B) (exclusive) is equal to prefix[R+1][B-1] - prefix[R+1][A] - (prefix[L][B-1] - prefix[L][A]).

Wait, but the range is (A, B), which includes elements > A and < B.

So the count is (number of elements <= B-1) minus (number of elements <= A).

Thus, for the interval [L, R], the count is (get(R, B-1) - get(L-1, B-1)) ) - (get(R, A) - get(L-1, A))).

Which can be computed using prefix arrays.

So precomputing prefix arrays for each position and value would allow us to answer each query in O(1) time.

Yes. Let's see:

We can precompute a prefix sum array where for each index i (0-based up to n), and for each value v (0-based up to n-1), prefix[i][v] is the number of elements in the first i elements (indices 0..i-1) that are <= v.

Then, for any range [L, R] (0-based indices), the number of elements <= v in this range is prefix[R+1][v] - prefix[L][v].

So to compute the number of elements in [L, R] that are between A and B (exclusive), where A < B, the count would be:

count = (prefix[R+1][B-1] - prefix[L][B-1]) - (prefix[R+1][A] - prefix[L][A])

So this is O(1) per query.

So for each pair (i, j), where i < j:

L = i + 1

R = j - 1

if L > R, then there are no elements in between, so the count is 0.

Otherwise, A = min(x, y), B = max(x, y). The count is (number of elements in [L, R] that are > A and < B).

Thus, using the prefix array, this can be computed in O(1) time.

Once we have the count, we can compute delta as follows:

if x < y:

delta = 2 * count + 1

else:

delta = -2 * count -1 

Then, the new inversion count after swapping i and j would be original_inversion + delta.

We need to find the pairs (i,j) that give the minimal new_inversion (original_inversion + delta), and count how many such pairs there are.

But wait, since the original_inversion is fixed, the minimal new_inversion corresponds to the minimal delta.

So the approach is:

1. Compute the original_inversion count (inv).

2. Precompute the prefix sum array.

3. For each pair (i, j), compute delta and find the minimal delta.

4. Count the number of pairs (i,j) that achieve this minimal delta.

So the steps are:

Compute the original inversion count.

Precompute the prefix array for range count queries.

Iterate all pairs (i, j) (i can be larger than j), compute for each the delta, then track the minimal delta and the count of pairs that achieve it.

Once all pairs are processed, the minimal new_inversion is inv + minimal_delta, and the count is the number of pairs.

Now, the question is: how to compute the original inversion count efficiently.

Computing the original inversion count can be done with a Fenwick Tree (Binary Indexed Tree) in O(n log n) time. For each element from right to left, we count the number of elements to the left that are greater than current element. Summing these gives the inversion count.

Yes, that's manageable.

So now, the plan is:

Implement the steps:

1. Read n and the permutation array a.

2. Compute the original inversion count (inv) using a Fenwick Tree.

3. Precompute the prefix sum array.

   - For each position i (from 0 to n), and for each value v (from 0 to n-1), prefix[i][v] is the number of elements in a[0..i-1] that are <= v.

   Since the values are up to 5000, and n is 5000, this is feasible.

4. For all pairs (i, j) where i != j:

   a. Ensure i < j by swapping them if needed.

   b. x = a[i], y = a[j].

   c. Compute A = min(x, y), B = max(x, y).

   d. L = i+1, R = j-1.

   e. count = 0 if L > R else (prefix[R+1][B-1] - prefix[L][B-1]) - (prefix[R+1][A] - prefix[L][A])

   f. compute delta:

      if x < y:

          delta = 2 * count + 1

      else:

          delta = -2 * count -1 

   g. Now, delta is the change in inversion count. So new_inversion = inv + delta.

   h. Keep track of the minimal new_inversion and the number of pairs achieving this.

But wait, the code must consider all pairs (i, j), including i > j. Because swapping i and j where i > j is the same as swapping j and i. So, to avoid double-counting, perhaps in the code we should iterate all ordered pairs (i, j) where i < j, and then for each pair, compute delta for both (i,j) and (j,i) ?

Wait, no. Because when we swap i and j (i < j), the delta for (i,j) is the same as the delta for (j,i), because swapping j and i (if i < j) is the same as swapping i and j. So for the code, it's better to process all pairs (i, j) with i < j, compute delta once, and then add both (i,j) and (j,i) to the possible pairs. Wait, but no. Because for the pair (i,j) and (j,i), the swap is the same. So each unordered pair {i,j} is considered once. So the code should iterate all unordered pairs once, compute the delta once, and then the pair can be considered as (i,j) and (j,i) leading to the same delta. But no: the delta is computed based on the positions i and j. If i < j, then the calculation is correct. If j < i, we have to swap them first. So, the code should handle all ordered pairs (i,j) where i and j are distinct, and compute the delta for each ordered pair. However, swapping i and j would give the same delta as the original (i,j) pair, but inverted.

Wait, no. Because the delta is dependent on the positions i and j. For example, if i and j are swapped, then x and y are swapped, and the positions are j and i, which would affect the calculation.

Wait, no. Because when i and j are swapped, the positions are j and i, but x and y are now a[j] and a[i], which is the same as the original pair (i,j) but swapped.

So, for ordered pairs (i,j) and (j,i), the delta is the same if x and y are swapped and the positions are swapped. But this is not the case. So the code should process all ordered pairs (i,j) where i and j are any distinct indices.

But that would be O(n^2) pairs, which for n=5000 is 25 million pairs. For each pair, the code has to compute the delta.

But for each ordered pair (i,j), whether i < j or j < i, we need to compute delta for that particular swap.

But this is redundant. Because swapping i and j (i < j) is the same as swapping j and i. So, when you process (i,j) where i < j, you can compute delta once, and that represents the delta for swapping the elements at positions i and j. The same delta applies to the pair (j,i), but since swapping i and j is the same as swapping j and i, perhaps the code should consider each unordered pair once, and account for that.

Wait, but when you swap (i,j) and (j,i), you are swapping the same two elements. So each unordered pair {i,j} (i != j) can be considered once. However, the problem requires that pairs (i,j) and (j,i) are considered the same pair. But according to the problem statement, the pairs are (i,j) where i and j are indexes, and the order matters. For example, in the first sample input, the pairs (0,3) and (3,0) are the same swap. But in the output, they are considered as one pair. Wait, no. The problem statement says "the number of such pairs (i, j) that swapping the elements of the input permutation with indexes i and j leads to the minimum number of executions."

So the order of i and j doesn't matter. Because swapping i and j is the same as swapping j and i. So pairs (i,j) and (j,i) are considered the same and should be counted once. So the code should iterate over all unordered pairs {i,j} (i != j) and compute delta once per unordered pair.

Thus, the code should process all unordered pairs (i,j) with i < j, compute delta once, and count each such pair once.

So the total pairs to process are n*(n-1)/2 ≈ 12.5 million for n=5000.

This is manageable.

So, the code steps are:

Loop over all i from 0 to n-1:

   loop over j from i+1 to n-1:

       compute delta for swapping i and j.

       new_inversion = inv + delta.

       track the minimal new_inversion and the count.

Once all pairs are processed, output the minimal new_inversion and the count.

But wait, in the first sample input, the correct pairs are (0,3) and (0,4). So when i=0 and j=3, j=4, these are two separate pairs. So the code should process all pairs where i < j.

Thus, the code needs to process each unordered pair once, compute the delta once, and track the minimal new_inversion and count.

So now, the code can proceed as follows.

Now, the next steps are:

Implement the Fenwick Tree for inversion count.

Precompute the prefix sum array.

Process all pairs i < j, compute delta, and track minimal delta and count.

But how to compute the original inversion count.

The inversion count can be computed by iterating through the array and for each element, count the number of elements to the right that are smaller than it. Sum all these.

Wait, but that's O(n^2), which for n=5000 is 25 million operations. Which is manageable, but for n=5e4 it's not. But since n is up to 5000, it's okay.

But using a Fenwick Tree is more efficient. Let's use that.

Yes. So the Fenwick Tree approach:

Initialize a Fenwick Tree of size n (values can be up to n-1).

We process the array from right to left. For each element a[i], the number of elements to the left of i that are greater than a[i] is the number of elements already in the Fenwick Tree (those to the right of i) that are less than a[i].

Wait, no. Wait, the standard approach for counting inversions using a Fenwick Tree is to process the array from right to left, and for each a[i], query the sum of elements less than a[i], which gives the number of elements to the right of i that are less than a[i]. These are the elements that form inversions with a[i]. Summing these gives the total inversion count.

Wait, yes. So the steps are:

Initialize a Fenwick Tree that can store frequencies of values.

Initialize inversion count as 0.

For i from n-1 downto 0:

   inversion_count += query_Fenwick(a[i] - 1)  # number of elements already in the tree less than a[i], which are the elements to the right of i that are smaller than a[i].

   update_Fenwick(a[i], 1)  # add a[i] to the tree.

Thus, the inversion count is the sum of elements to the right of each element that are smaller than it.

Which is exactly the number of swaps insertion sort makes.

Yes.

So this code can compute the inversion count in O(n log n) time.

Once the inversion count is computed, we need to compute the prefix sum array.

Now, the prefix sum array is a 2D array of size (n+1) x n. For each index i (from 0 to n), and value v (from 0 to n-1), prefix[i][v] is the number of elements in a[0..i-1] that are <= v.

So to build this:

prefix = [[0]*(n) for _ in range(n+1)]

for i in range(1, n+1):

   for v in 0..n-1:

      prefix[i][v] = prefix[i-1][v] + (1 if a[i-1] <= v else 0)

Wait, no. Because for each position i (prefix array index), the elements up to position i-1 in the array a. So for i=0, prefix[0][v] =0. For i=1, prefix[1][v] is 1 if a[0] <=v. For i=2, it's prefix[1][v] plus 1 if a[1] <=v, etc.

But building this with nested loops would be O(n^2), which is 25 million for n=5e3. Which is manageable.

But perhaps there's a smarter way.

Wait, for each i from 0 to n:

   for each v from 0 to n-1:

      prefix[i][v] = prefix[i-1][v] + (a[i-1] <= v) if i >=1 else 0.

But for each i, to compute all v's:

But a[i-1] is a fixed value. So for each i, when we process a[i-1], for all v >= a[i-1], prefix[i][v] = prefix[i-1][v] +1. For v < a[i-1], prefix[i][v] = prefix[i-1][v].

But this can be optimized using cumulative sums.

Alternatively, since the values are up to n-1, for each i, we can create a copy of the previous row and increment all entries >= a[i-1] by 1.

But this would be O(n^2) time and space, which for n=5e3 is 25 million per step, leading to O(12.5e9) operations, which is way too slow.

Thus, the straightforward approach of building the prefix array with O(n^2) time is manageable for n=5e3.

Wait, no. For each i, we have to loop through all v (n values) and compute prefix[i][v] as prefix[i-1][v] + (a[i-1] <= v). So for each i, this is O(n) time. For n=5e3, this is 5e3 * 5e3 = 25 million operations. Which is acceptable.

So for code:

n = 5000:

prefix = [[0] * (n) for _ in range(n + 1)]

for i in range(1, n+1):

    current_element = a[i-1]  # since a is 0-based, prefix[i] represents first i elements (indices 0..i-1)

    for v in range(n):

        if v < current_element:

            prefix[i][v] = prefix[i-1][v]

        else:

            prefix[i][v] = prefix[i-1][v] + 1

But this is O(n^2) time, which for n=5e3 is 25 million steps, which is acceptable.

But in Python, loops over 25 million steps can be a bit slow. So perhaps we can find a way to optimize this.

But given the problem constraints, perhaps this is manageable.

Once the prefix array is built, processing each pair (i,j) with i < j:

x = a[i], y = a[j]

A = min(x, y)

B = max(x, y)

L = i+1

R = j-1

if L > R:

    count =0

else:

    # compute count of elements in a[L..R] where A < z < B

    count = (prefix[R+1][B-1] - prefix[L][B-1]) - (prefix[R+1][A] - prefix[L][A])

if x < y:

    delta = 2 * count +1

else:

    delta = -2 * count -1 

new_inv = inv + delta

track the minimal new_inv and the count of pairs that achieve it.

Once all pairs are processed, output the minimal new_inv and the count.

Now, let's test this approach against the sample inputs.

Sample Input 1:

5

4 0 3 1 2

Original array a = [4,0,3,1,2]

Compute inversion count:

Processing from right to left.

elements: 2,1,3,0,4.

For each element:

element 2 (index 4): number of elements to the right (none) → 0. Fenwick has 2.

element 1 (index 3): elements to right (index 4: 2). 2 > 1 → inversion. So query for 0 → 0. Fenwick has 1,2.

element 3 (index 2): elements to right (1,2). numbers less than 3 are 1 and 2 → 2. Fenwick adds 3.

element 0 (index 1): elements to right (3,1,2). numbers less than 0 → 0. Fenwick adds 0.

element 4 (index 0): elements to right (0,3,1,2). numbers less than 4 → 4. So inversion count is 0 + 0 +2 +0 +4 =6? But the sample output says the original swap count was 3. Wait, this indicates a mistake.

Wait, sample input 1's output after swap is 3. So the original swap count must have been higher. But according to the problem statement, the sample input's original swap count must be 3 plus the delta. Wait, no. The sample input's output is 3, which is the minimal swap count after the swap. So the original swap count must have been higher than 3, and after swapping, it's reduced to 3.

But according to the sample input 1's explanation, the original array is 4 0 3 1 2.

The insertion sort swaps would be:

Let's think:

For insertion sort, the number of swaps is the sum of the number of elements to the left that are larger than current element.

Let's compute this:

element 0 (4): no elements to left → 0 swaps.

element 1 (0): there are 1 element to left (4) which is larger → 1 swap.

element 2 (3): elements to left are 4 and 0. 4 >3 → 1 swap.

element 3 (1): elements to left are 4,0,3. 4>1, 3>1 → 2 swaps.

element 4 (2): elements to left are 4,0,3,1. 4>2, 3>2 → 2 swaps.

Total swaps: 0+1+1+2+2=6. So original_inv is 6.

But sample input 1's output is 3, which is the new swap count after swapping. So delta for the best swap must be 6 + delta =3 → delta =-3.

So according to the formula, delta should be -3.

In the first sample, the best swap is swapping elements 0 and 3 (indices 0 and 3). Let's compute delta for i=0, j=3.

x=4, y=1 (since a[0]=4, a[3]=1).

A=1, B=4.

L=0+1=1, R=3-1=2. So elements between positions 1 and 2 (inclusive) are a[1]=0, a[2]=3.

So the elements are 0 and 3.

We need to count elements between 1 and 4 (exclusive), i.e., 0 < z <4. So elements 0 is less than 1, so no. 3 is in (1,4), so count=1.

x=4 > y=1.

So delta =-2*count -1 → delta =-2*1 -1 =-3.

Which is correct. So new_inv =6-3=3.

So the code correctly computes this.

So the code works for this case.

Similarly, for other pairs.

Now, for the code's efficiency.

The inversion count is computed in O(n log n) time.

The prefix sum array is built in O(n^2) time.

Processing all pairs is O(n^2) time.

So overall O(n^2) time.

Which for n=5000 is acceptable.

Now, memory-wise, the prefix array for n=5000 is (5001)*5000 = ~25 million integers. Each integer is 4 bytes, so ~100 MB. Which is manageable within the memory constraints (256 MB).

But in Python, this may be tight, but manageable.

So the code can proceed.

Now, implementing this in Python.

First, the Fenwick Tree for the inversion count.

But since the elements are a permutation of 0..n-1, their values are in 0..n-1, so the Fenwick Tree can be of size n.

Then, the code for the inversion count.

Then, the prefix array.

Then, process all pairs.

Now, let's proceed to write the code.

But in Python, loops can be slow. So for the prefix array, perhaps using a list of lists and precomputing row by row.

But for n=5000, it's manageable.

Testing the code with the first sample:

Sample Input 1:

5

4 0 3 1 2

Original a = [4,0,3,1,2]

Inversion count: computed as 6.

Then, the prefix array:

prefix[i][v] for i from 0 to 5, and v from 0 to 4.

For example:

prefix[1][v] is the count of elements in a[0..0] (a[0]=4) that are <=v.

So for v <4: 0. For v >=4:1.

prefix[1][0] =0, prefix[1][1]=0, ..., prefix[1][4] =1.

prefix[2][v] is count of elements in a[0..1] (4,0) that are <=v.

For v=0: 1 (element 0).

For v=1: 1.

For v=2:1.

etc.

So when processing pairs i=0 and j=3:

x=4, y=1.

A=1, B=4.

L=1, R=2.

elements in a[1..2] are 0,3.

count of elements between 1 and 4: 3 is between 1 and 4 → count=1.

x=4 > y=1 → delta =-2*1 -1 =-3.

new_inv=6-3=3.

So this pair contributes to the minimal delta.

Similarly for other pairs.

Now, the code.

But the code should read the input, compute the inversion count, build the prefix array, process all pairs (i,j) where i < j, compute delta for each, track the minimal new_inv and count.

Then, output the minimal new_inv and the count.

Now, the code:

Implement Fenwick Tree:

class FenwickTree:

    def __init__(self, size):

        self.n = size

        self.tree = [0]*(self.n +1)

    def update(self, idx, delta=1):

        # idx is 1-based

        while idx <= self.n:

            self.tree[idx] += delta

            idx += idx & -idx

    def query(self, idx):

        # sum from 1 to idx

        res =0

        while idx >0:

            res += self.tree[idx]

            idx -= idx & -idx

        return res

But note that in the FenwickTree, the indices are 1-based. So when the elements are 0-based, we have to add 1.

So for each a[i] in the permutation (which is 0..n-1), when inserting into the FenwickTree, we can add 1 to make them 1-based.

So for a[i] = x, in the FenwickTree, we store x+1 as the index.

But this depends on how the FenwickTree is designed. Let me adjust the code.

But wait, in the original array, the elements are 0-based (0..n-1).

The FenwickTree needs to handle values from 0 to n-1.

But the standard FenwickTree implementation uses 1-based indices.

So when inserting an element x (0-based), we can represent it as x+1 in the FenwickTree.

So for example, to query the number of elements <=x, we can query up to x+1.

So in the code:

When inserting x, we call ft.update(x+1).

When querying for elements less than x, we call ft.query(x).

Because the FenwickTree is 1-based, and elements are stored as x+1.

But this may need to be adjusted.

Alternatively, since the elements are 0..n-1, the FenwickTree can be initialized with size n, and when inserting x, we insert x+1.

But perhaps it's better to adjust the code.

Alternatively, the FenwickTree can be zero-based. But for now, let's proceed.

For the inversion count:

ft = FenwickTree(n)

inv =0

for i in reversed(range(n)):

    # number of elements to the right (already processed) that are less than a[i]

    # query for a[i] -1.

    count = ft.query(a[i])

    inv += count

    ft.update(a[i] + 1)

Wait, no. Because the FenwickTree is 1-based. So when a[i] is 0-based (0..n-1), adding 1 to make it 1-based (1..n).

So the FenwickTree's size is n+1 (since the maximum possible element is a[i] +1 =n).

But then, when querying for elements less than a[i], we need to query up to a[i] -1 +1 (since in 1-based, a[i] is stored as a[i]+1).

Wait, perhaps it's better to think that the FenwickTree's indices are 1-based. So for an element x (0-based), we index it as x+1. So when we insert x, we call update(x+1).

Then, when we want to find the number of elements less than x, we call query(x).

Because elements inserted are x+1, so elements <= x-1 in 0-based are stored as <= x in 1-based.

Wait, this is getting complicated.

Let's take an example.

x is 0 (0-based). We store it as 1.

x is 4 (0-based) in a 5-element array. stored as 5.

To query the number of elements less than 3 (0-based), we query up to 3 (0-based) → 3+1=4 in 1-based. So query(3) returns the sum of elements inserted with index <=3. Which are elements 0,1,2 in 0-based, stored as 1,2,3. So the query(3) gives 3 elements if all are inserted.

So perhaps the code should be:

count = ft.query(a[i] -1 +1) → a[i].

Wait, no. Because a[i] is the current element. We want to find the number of elements to the right (already inserted into the FenwickTree) that are less than a[i].

So elements less than a[i] in the FenwickTree are those elements x where x < a[i].

In the FenwickTree, these are stored as x+1. So for x < a[i], x+1 ranges from 1 to a[i].

So the number of elements less than a[i] is ft.query(a[i]).

Because:

x ranges from 0 to a[i]-1.

x+1 ranges from 1 to a[i].

So query(a[i]) returns the count of elements inserted with indices up to a[i], which corresponds to elements 0 to a[i]-1 in the original array.

Thus, the code for the inversion count:

inv =0

ft = FenwickTree(n)

for i in reversed(range(n)):

    # query the number of elements inserted so far that are less than a[i]

    count = ft.query(a[i])

    inv += count

    # insert a[i] into the tree

    ft.update(a[i] + 1)

But wait, the FenwickTree is initialized with size n. But a[i] can be up to n-1. So a[i]+1 can be up to n, which is within the tree's size.

Yes.

So this should correctly compute the inversion count.

Now, the code for the prefix array.

Building the prefix array:

n = len(a)

prefix = [[0]*(n) for _ in range(n+1)]

for i in range(1, n+1):

    current = a[i-1]

    for v in range(n):

        if current <= v:

            prefix[i][v] = prefix[i-1][v] + 1

        else:

            prefix[i][v] = prefix[i-1][v]

But this is O(n^2), which is manageable.

Then, processing all pairs (i,j) with i < j:

min_new_inv = float('inf')

count_pairs =0

for i in range(n):

    for j in range(i+1, n):

        x = a[i]

        y = a[j]

        if x < y:

            A = x

            B = y

            L = i+1

            R = j-1

            if L > R:

                c =0

            else:

                c = (prefix[R+1][B-1] - prefix[L][B-1]) - (prefix[R+1][A] - prefix[L][A])

            delta = 2 * c +1

        else:

            A = y

            B = x

            L = i+1

            R = j-1

            if L > R:

                c =0

            else:

                c = (prefix[R+1][B-1] - prefix[L][B-1]) - (prefix[R+1][A] - prefix[L][A])

            delta = -2 * c -1

        new_inv = inv + delta

        if new_inv < min_new_inv:

            min_new_inv = new_inv

            count_pairs =1

        elif new_inv == min_new_inv:

            count_pairs +=1

So after processing all pairs, output min_new_inv and count_pairs.

But wait, in the code above, for x < y, we compute A=x, B=y. For x > y, we compute A=y, B=x. Then, the count is the number of elements in L..R between A and B (exclusive).

But when x > y, then the code for c is (prefix[R+1][B-1] - prefix[L][B-1] ) - (prefix[R+1][A] - prefix[L][A] ), where B is x and A is y.

But when x > y, then B is x, A is y. So the elements between A and B are y < z < x.

So the code correctly computes the count of elements in (y, x).

Then, delta is -2*c -1.

Yes.

Testing this with sample input 1:

i=0, j=3.

x=4, y=1. x > y.

A=1, B=4.

L=1, R=2.

c = (prefix[3][3] - prefix[1][3]) - (prefix[3][1] - prefix[1][1]) 

prefix[3] is the first 3 elements (a[0], a[1], a[2] =4,0,3)

prefix[3][3] is the number of elements in first 3 elements (4,0,3) <=3: 0,3 → 2.

prefix[1][3] is the number of elements in first 1 element (4) <=3: 0.

So 2 -0 =2.

prefix[3][1] is the number of elements in first 3 elements <=1: 0.

prefix[1][1] is 0.

So 0-0=0.

c= 2-0=2.

Wait, but the elements between i+1 and j-1 are positions 1 and 2 (elements 0 and3). How many are between y=1 and x=4?

Elements between 1 and4 are 3. So count is1.

But according to the code's calculation, c=2-0 - (0-0) = 2.

Which would be incorrect.

Wait, what's wrong here?

Ah, wait:

When x=4 and y=1, A=1, B=4.

We need to compute elements in L..R that are between A and B (1 < z <4).

The elements in positions 1 and 2 are a[1]=0 and a[2]=3.

0 is not between 1 and4. 3 is.

So count is1.

But according to the code:

prefix[R+1][B-1] is prefix[3][3] (B is 4, B-1 is3).

prefix[3][3] is the count of elements in a[0..2] (4,0,3) <=3: 0 and3 are <=3. So 2.

prefix[L][B-1] is prefix[1][3] → elements in a[0..0] (4) <=3:0.

So prefix[R+1][B-1] - prefix[L][B-1] is 2-0=2.

prefix[R+1][A] is prefix[3][1] → elements in a[0..2] <=1: 0 and1. But a[0..2] is4,0,3. So 0 is <=1. So 1.

prefix[L][A] is prefix[1][1] → elements in a[0..0] (4) <=1: 0.

So 1-0=1.

Thus, c=2 -1=1.

Which matches the expected count.

So the code's calculation is correct.

But wait, the code's code for x> y is:

c = (prefix[R+1][B-1] - prefix[L][B-1]) - (prefix[R+1][A] - prefix[L][A])

Which for B=4, A=1:

prefix[R+1][B-1] = prefix[3][3] =2.

prefix[L][B-1] = prefix[1][3] =0.

prefix[R+1][A] = prefix[3][1] =1.

prefix[L][A] = prefix[1][1] =0.

So c= (2-0) - (1-0) =2-1=1.

Which is correct. Then delta is -2*1 -1= -3.

Thus, new_inv =6 -3=3.

Which is correct.

So the code works.

Similarly, for other pairs.

Now, the code.

But wait, in the code, when x < y, the delta is 2*c +1. When x>y, it's -2*c -1.

But in the code, the variables A and B are correctly set.

Thus, the code should work.

Finally, the code outputs min_new_inv and count_pairs.

But wait, the problem requires that the minimal new_inv is found, and the number of pairs (i,j) (i and j can be any order) that achieve this.

But the code processes pairs (i,j) with i < j, and counts each pair once.

But in the sample input 1, the correct pairs are (0,3) and (0,4), which are processed once each.

Thus, the code's count_pairs would be 2.

Which matches the sample output.

Thus, the code is correct.

Now, putting it all together.

The code:

class FenwickTree:

    def __init__(self, size):

        self.n = size

        self.tree = [0]*(self.n + 2)  # +2 to avoid issues with 1-based indexing

    def update(self, idx, delta=1):

        while idx <= self.n:

            self.tree[idx] += delta

            idx += idx & -idx

    def query(self, idx):

        res = 0

        while idx >0:

            res += self.tree[idx]

            idx -= idx & -idx

        return res

n = int(input())

a = list(map(int, input().split()))

# Compute original inversion count

ft = FenwickTree(n)

inv =0

for num in reversed(a):

    # query the number of elements inserted so far that are < num

    # which are the elements to the right in the original array

    inv += ft.query(num)

    ft.update(num +1)  # since elements are 0-based, stored as 1-based in FenwickTree

# Precompute prefix array

prefix = [[0]*(n) for _ in range(n+1)]

for i in range(1, n+1):

    current = a[i-1]

    for v in range(n):

        if current <= v:

            prefix[i][v] = prefix[i-1][v] +1

        else:

            prefix[i][v] = prefix[i-1][v]

min_new_inv = float('inf')

count_pairs =0

for i in range(n):

    for j in range(i+1, n):

        x = a[i]

        y = a[j]

        if x < y:

            A = x

            B = y

        else:

            A = y

            B = x

        L = i +1

        R = j -1

        if L > R:

            c =0

        else:

            # compute elements in [L, R] where A < z < B

            # which is elements <= B-1 and > A

            # count = (number of elements <= B-1) - (number of elements <= A)

            part1 = prefix[R+1][B-1] - prefix[L][B-1]

            part2 = prefix[R+1][A] - prefix[L][A]

            c = part1 - part2

        if x < y:

            delta = 2 * c +1

        else:

            delta = -2 * c -1

        new_inv = inv + delta

        if new_inv < min_new_inv:

            min_new_inv = new_inv

            count_pairs =1

        elif new_inv == min_new_inv:

            count_pairs +=1

print(min_new_inv, count_pairs)

Testing this code with sample input 1:

Sample Input 1:

5

4 0 3 1 2

Original inversion count is 6.

Processing pairs:

Pair (0,3):

x=4, y=1. x>y. A=1, B=4. L=1, R=2.

c=1.

delta= -2*1-1= -3. new_inv=6-3=3.

Pair (0,4):

x=4, y=2. x>y. A=2, B=4. L=1, R=3.

Elements between 0+1=1 and 4-1=3: positions 1,2,3: elements 0,3,1.

A=2, B=4.

Elements between 2 and4: 3.

So c=1.

delta= -2*1 -1= -3. new_inv=3.

Thus, there are 2 pairs, so code outputs 3 2.

Which matches the sample.

Sample Input 2:

5

1 2 3 4 0

Original array is [1,2,3,4,0]. The inversion count for this array is:

Elements to the right of 1 (4 elements): 0. So 1 contributes 1.

Elements to the right of 2 (3 elements): 0. So 0.

Elements to the right of 3 (2 elements): 0. So 0.

Elements to the right of 4 (1 element): 0. So 0.

Element 0: contributes 4 elements to the left that are larger.

Total inversion count: 1+0+0+0+4=5?

Wait, no. Let's compute it properly.

Insertion sort swaps:

For each element:

element 1 (index 0): no elements to left. swaps 0.

element 2 (index 1): elements to left (1). 2>1 → 0 swaps.

element 3 (index 2): elements to left (1,2). 3>2 →0.

element4 (index3): elements to left (1,2,3).4>3→0.

element0 (index4): elements to left are all larger. 4 swaps.

Total swaps:0+0+0+0+4=4.

But according to the sample input 2's output, after swapping, the swap count is3. So original_inv must have been 4.

But sample input 2's output is 3 4. So the code must have found delta= -1 for the best pairs.

But let's see:

In sample input 2's case, swapping index 4 (element0) with index0,1,2,3.

For example, swapping 4 and 0.

After swapping, array becomes [0,2,3,4,1].

The insertion sort swaps for this array:

element0: 0 swaps.

element2: 1 swap (0 <2 →0).

element3: 1 swap (2 <3 →0).

element4:1 swap (3 <4 →0).

element1: must be inserted into [0,2,3,4], so 4 swaps.

Total swaps:0+0+0+0+4=4? No, this is not correct.

Wait, perhaps the original inversion count is computed correctly.

Alternatively, perhaps the original inversion count is computed as follows:

Using the Fenwick Tree approach.

Elements processed in reverse order:

0,4,3,2,1.

Processing 0:

insert 0+1=1. query(0) returns 0.

inv +=0.

Processing4:

insert 4+1=5. query(4) returns 0 (no elements inserted yet).

inv remains 0.

Processing3:

query(3) returns 0. insert 3+1=4. inv 0.

Processing2:

query(2) returns 0. insert 2+1=3. inv 0.

Processing1:

query(1) returns 0. insert 1+1=2. inv 0.

Total inv is 0. But that's wrong.

Wait, no. The array is [1,2,3,4,0]. When processed in reverse:

Processing 0 (index4): no elements to the right. query returns 0. inv is 0.

Processing4 (index3): elements to right are 0. 4>0 → inv +=1. insert 4+1=5.

Processing3 (index2): elements to right are 4,0. 3>0 → inv +=1. insert 3+1=4. inv is 0+1+1=2.

Processing2 (index1): elements to right are 3,4,0. 2>0 → inv +=1. insert 2+1=3. inv 3.

Processing1 (index0): elements to right are 2,3,4,0. 1>0 → inv +=1. insert 1+1=2. inv 4.

So original_inv is4.

Which matches our manual calculation.

Then, after swapping, the new_inv is 3.

For example, swapping index4 with index0:

x=1, y=0. x>y.

A=0, B=1.

L=0+1=1, R=4-1=3.

elements in positions 1..3: 2,3,4.

Count of elements between 0 and 1 (exclusive): 0 < z <1 → none. So c=0.

delta= -2*0 -1= -1. new_inv=4-1=3.

So this pair contributes.

Similarly, swapping index4 with index1:

x=2, y=0. x>y.

A=0, B=2.

elements between 2 and 4-1=3: position2 and3: 3,4.

elements between 0 and2: 0 <z <2 → 1 is not present. So elements 3 and4 are not in this range. So c=0.

delta= -1. new_inv=3.

Similarly for swapping index4 with index2,3.

So the code would find four pairs (i,j) where j=4 and i=0,1,2,3.

Thus, the code would output 3 4.

Which matches the sample.

Thus, the code is correct.
</think>

```python
class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 2)

    def update(self, idx, delta=1):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

n = int(input())
a = list(map(int, input().split()))

# Compute original inversion count using Fenwick Tree
ft = FenwickTree(n)
original_inv = 0
for num in reversed(a):
    original_inv += ft.query(num)
    ft.update(num + 1)  # Shift to 1-based index

# Precompute prefix sum array for range queries
prefix = [[0] * n for _ in range(n + 1)]
for i in range(1, n + 1):
    current = a[i - 1]
    for v in range(n):
        if current <= v:
            prefix[i][v] = prefix[i - 1][v] + 1
        else:
            prefix[i][v] = prefix[i - 1][v]

min_new_inv = float('inf')
count_pairs = 0

for i in range(n):
    for j in range(i + 1, n):
        x, y = a[i], a[j]
        if x < y:
            A, B = x, y
        else:
            A, B = y, x
        L = i + 1
        R = j - 1
        if L > R:
            c = 0
        else:
            part1 = prefix[R + 1][B - 1] - prefix[L][B - 1]
            part2 = prefix[R + 1][A] - prefix[L][A]
            c = part1 - part2
        delta = 2 * c + 1 if x < y else -2 * c - 1
        new_inv = original_inv + delta
        if new_inv < min_new_inv:
            min_new_inv = new_inv
            count_pairs = 1
        elif new_inv == min_new_inv:
            count_pairs += 1

print(min_new_inv, count_pairs)
```