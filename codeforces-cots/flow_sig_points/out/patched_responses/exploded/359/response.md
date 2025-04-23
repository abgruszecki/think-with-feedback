<think>
Okay, let's see. The problem is about processing multiple queries where each query reverses a segment of a permutation and then determining if the total number of inversions is odd or even. Hmm, the key is to compute the parity (odd/even) of the inversion count after each reversal efficiently because the constraints are tight, especially with m up to 2e5.

Wait, calculating inversions directly after each reversal would be O(n^2) per query, which is way too slow for n=1500 and m=2e5. That would be 1500^2 * 2e5 = 4.5e11 operations. Definitely not feasible. So we need a smarter approach to track the parity without recalculating all inversions each time.

Let me think. The parity of the inversion count changes in a predictable way when certain operations are applied. Reversing a segment might affect the inversion parity. How?

When you reverse a segment [l, r], how does the inversion count change? Let's consider the number of inversions added or removed due to the reversal. But instead of tracking the exact count, maybe we can find how the reversal affects the parity.

An important observation here is that reversing a segment of length k can contribute a certain number of inversions. Let's break it down.

First, the length of the reversed segment. Suppose the segment has length k (k = r - l + 1). When you reverse this segment, the number of inversions inside the segment changes. But how?

For a reversed segment, the inversions within it are transformed. Originally, each pair (i, j) in the segment where i < j and a[i] > a[j] contributes an inversion. After reversing, their order is reversed. So the number of such pairs becomes the number of ordered pairs (j, i) in the reversed array where j was after i in the original. Wait, maybe the number of inversions inside the segment changes to (k*(k-1)/2) - original_inversions. Because the maximum possible inversions in a segment of length k is k*(k-1)/2. So the change in inversions within the segment would be (new_inversions) - (old_inversions) = (k*(k-1)/2 - old_inversions) - old_inversions) = k*(k-1)/2 - 2*old_inversions. But since we're only interested in parity, subtracting twice the old_inversions doesn't change the parity. So the net change in inversions within the segment is equal to k*(k-1)/2 mod 2. Because 2*anything is 0 mod 2. So the parity of the change due to inversions inside the segment is equal to the parity of k*(k-1)/2.

Wait, let's see. When you reverse the segment, the number of inversions inside it becomes (k choose 2) - original_inversions. So the change is (k choose 2) - 2 * original_inversions. But modulo 2, this is equivalent to (k choose 2) mod 2. Because 2*original_inversions mod 2 is 0. So the parity of the change in internal inversions is (k*(k-1)/2) mod 2.

So that's one part. The other part is the inversions that involve elements inside and outside the reversed segment. Hmm. How does reversing a segment affect those?

Wait, when you reverse a segment, the order of elements in the segment is reversed. So pairs where one element is inside the segment and the other is outside may change. Let's think about pairs (x, y) where x is inside the reversed segment, y is outside. How does their ordering affect inversions?

For example, suppose before reversal, x is at position i (inside the segment) and y is at position j (outside). After reversal, x's position becomes l + r - i. The relative order between x and y may change. For each such pair (x, y), if x was in the segment and y is outside, their positions will swap if i was in the segment and j is not, but only if one is to the left or right of the segment.

Wait, perhaps the key is to calculate how many pairs (a, b) where a is in the reversed segment and b is not. Let's consider these pairs:

For a pair where a is in [l, r] and b is not in [l, r], the inversion status depends on the relative order of a and b. Reversing the segment changes the order of elements within [l, r], but the elements outside remain the same. So, for any a in [l, r] and b outside, after reversing, the elements in the segment are in reverse order. So the position of a (within the segment) is now mirrored. But how does this affect the inversion between a and b?

Wait, perhaps the number of such pairs (a, b) where a is in the segment and b is not, and a and b form an inversion, is equal to the number of such pairs in the original, but the parity could change. Or maybe not. Let's think.

Suppose we have two elements a and b, where a is inside the reversed segment and b is outside. Let's say that before reversal, a is in position i (within [l, r]), and b is in position j (outside [l, r]). After reversal, a moves to position l + r - i. The relative positions of a and b depend on whether j is to the left of the segment, inside (but that's not possible as j is outside), or to the right.

Wait, j is outside the segment. So j is either < l or > r.

Case 1: j < l. Then, in the original arrangement, a is in position i (>= l), so j < i. So the original pair is (i, j) with i > j. After reversal, the new position of a is l + r - i. Since j < l <= i <= r, the new position of a is l + r - i >= l (since i <= r implies r - i >=0, so l + (r -i) >= l). So j is still < new i. So the pair (a, b) in this case is ordered (new_i, j), where new_i is in [l, r], j < l <= new_i. So the new_i is still > j. So the order between a and b (positions) remains the same. But the values of a and b may have changed, but wait, no: the reversal swaps the positions of elements in the segment. So a was originally at i, and after reversal, a is replaced by the element that was at l + r - i. So the actual value of a and b (the elements) could be different. Wait, this is a confusion. Wait, the reversal swaps the elements in the segment. So after reversal, the elements in positions l to r are reversed.

So for example, if the original elements are [x1, x2, x3, x4], and we reverse positions 2-3, the new elements are [x1, x3, x2, x4]. So the elements in the reversed segment are x3 and x2 now. So any pair (a, b) where a is in the reversed segment and b is outside could have their values swapped. So the inversion count between a and b could change.

But tracking this for all pairs would be O(n^2), which is not feasible.

Hmm. So the problem is how to compute the change in inversion count parity after reversing a segment. The total inversion parity is the initial parity plus the parity of the change caused by each reversal.

So the key is to compute for each reversal, the change in the number of inversions mod 2. Then, flip the current parity if the change is odd.

So the problem reduces to, for each query, compute the parity change (delta) mod 2, and then the new parity is current_parity XOR delta.

So how to compute delta mod 2?

Let me think again. The total inversion count after reversing a segment is:

original_inversions + delta, where delta is the change in inversions.

We need delta mod 2.

Breaking delta into two parts:

1. The inversions within the reversed segment.

As discussed earlier, the change here is (k*(k-1)/2) mod 2. Because when you reverse a segment of length k, the number of inversions inside the segment becomes k*(k-1)/2 - original_internal_inversions. So the delta here is (k*(k-1)/2 - 2 * original_internal_inversions) mod 2. Since 2*original_internal_inversions is even, this delta is equal to (k*(k-1)/2) mod 2.

So for the internal inversions, the delta contributes (k choose 2) mod 2.

2. The inversions between elements inside the segment and those outside.

This is the tricky part. Let's think about how reversing the segment affects these pairs.

For a pair (x, y) where x is inside the reversed segment and y is outside. Let's denote x's original position as i (l <= i <= r), and y's position as j (either j < l or j > r).

After reversing the segment, x's new position is l + r - i. So the relative positions between x and y depend on whether y is on the left or right of the segment.

Case 1: y is on the left (j < l). Then in the original array, x is in [l, r], so i >= l. j < l <= i, so j < i. So original positions are (i, j). After reversal, x's new position is l + r - i. Since i >= l, l + r - i <= r. So new position of x is between l and r, which is still > j. So the order between x and y (positions) remains the same. However, the elements in x's position and y's position are now different. Wait no. Because during reversal, the elements in the segment are swapped. So x is the element originally at position i, and after reversal, x is at position l + r - i. But y is outside the segment, so its element is the same as before.

Wait, no. Wait, when you reverse a segment, the elements in positions l to r are reversed. So the element at position l swaps with the element at position r, l+1 swaps with r-1, etc. So for any position i in the segment, the element at i becomes the element that was at position l + r - i.

So, in terms of the elements, the pairs (a, b) where a is in the reversed segment and b is outside will now have the elements in positions (i, j) swapped in the segment. So the elements involved in the pair could change.

But this complicates things. Because for a pair (x, y) where x is in the segment and y is outside, their values are swapped in the array. Wait, no. The elements are swapped within the segment. So suppose the original elements in the segment are [a, b, c, d]. After reversal, they become [d, c, b, a]. So each element's position is changed, but the elements themselves are the same. So the pair (d, y) where y is outside may form an inversion now, but previously it was (a, y) that formed an inversion.

But tracking this for all pairs is impossible for large n.

Alternative approach: the parity change due to the external pairs. Let's think about the number of such pairs (x in segment, y outside) that form inversions before and after the reversal.

But how can we compute the parity of the change in this count?

Hmm, maybe there's a mathematical trick here. Let's think about the pairs (x in segment, y outside) that are inversions before the reversal and not after, and vice versa.

But perhaps the total change in inversion count for these pairs can be expressed in terms of the number of such pairs that flip their inversion status. Each such pair contributes a delta of +1 or -1 mod 2.

But how to compute this delta mod 2?

Alternatively, for each such pair, after reversal, whether it's an inversion depends on the elements and their positions. But maybe the parity of the number of such flips can be computed in a smarter way.

Alternatively, think about the elements in the reversed segment. For the pairs (x in segment, y outside), the relative positions between x and y may or may not change. For example, if y is to the left of the segment (j < l), then in the original, x is to the right of y. After reversal, x's new position is l + r - i. Since i >= l, l + r - i <= r. So x is still to the right of y. So their positions' order remains the same. However, the elements in the x's position and y's position are now different (since the segment is reversed). So the inversion status could change.

Wait, but the elements in the x's original position (i) are now at l + r - i. So for a pair (i, j) where i is in the segment and j is outside, after reversal, the element at i's new position is the element that was at l + r - i. So the pair (new_i, j) is now (element at l + r - i, element at j). The original pair (i, j) was (element at i, element at j). So the inversion status (element at new_i vs element at j) may be different from the original (element at i vs element at j). But this seems hard to track.

But perhaps there's a way to model the overall effect. Let's think of the elements in the reversed segment. When we reverse the segment, the elements in the segment are now ordered in reverse. So for elements x and y inside the segment, their order is reversed. But for elements inside and outside, their order (in terms of positions) depends on whether the outside element is left or right of the segment.

Wait, perhaps the key is to realize that for all pairs (x in segment, y outside), the inversion count parity change is equal to the number of such pairs where (x, y) was an inversion in the original but not after reversal, plus the number of pairs that became inversions after reversal but not before. However, each such pair contributes a delta of 1 mod 2 (since adding or subtracting 1 is the same mod 2).

But how can we compute this?

Alternatively, let's model the parity change as follows:

The total delta is (change in internal inversions) + (change in external inversions) mod 2.

We already know that the internal inversions contribute (k choose 2) mod 2.

For the external inversions, the problem is to find how many pairs (x in segment, y outside) change their inversion status.

Let me think of the total number of such pairs that flip their inversion status. If this number is even, then it doesn't affect the parity. If it's odd, then it flips the parity.

But how to compute the parity of this number?

Wait, when you reverse the segment, the elements inside the segment are reversed. So for each element x in the segment, the elements outside are split into those left of the segment (L) and those right of the segment (R).

For elements in L (positions < l), their order relative to the segment after reversal is the same. For example, all elements in L are to the left of the segment. After reversal, each x in the segment's new position is still to the right of L elements. So the positions of x and y (y in L) are the same as before. However, the elements x and y have changed: the x's element is now the one that was in the mirror position in the segment.

But how does this affect the inversion count between x and y?

The inversion between x (now in the segment) and y (L) is determined by whether the element in x's new position is greater than y's element.

But this seems complicated. But perhaps there's a way to model the parity change.

Another approach: when you reverse a segment, the number of inversions between elements in the segment and elements outside is equal to the original count plus some delta. Let's model the delta.

But again, this seems difficult.

Alternatively, let's think about the parity of the change in inversions caused by the reversal. Let's consider that for the external pairs, the change in inversions can be determined by the number of such pairs (x, y) where x is in the segment and y is outside, and (x, y) was an inversion in the original array but is not after reversal, or vice versa. Each such pair contributes a delta of ±1.

But how to compute this?

Alternatively, let's note that when you reverse a segment, each element in the segment is moved to a new position. For the elements in the segment, their order relative to the elements outside the segment is reversed for all elements in the segment. Wait, not exactly. For example, elements to the left of the segment (L) are before the segment. When you reverse the segment, the elements in the segment are in reverse order, but the entire segment is still between L and R (R is the elements to the right of the segment). So for elements in L and R, the relative positions to the segment's elements are the same. The elements in L are still to the left of all elements in the segment, and the elements in R are to the right.

Wait, no. The positions of the elements in the segment are reversed. So, for example, if the segment was [A, B, C, D], reversing it gives [D, C, B, A]. The elements are now reversed. But their positions are still between l and r. So any elements outside the segment (L and R) are still in their original positions. So, for elements in L (positions < l), their positions are to the left of all elements in the segment. Similarly for R (positions > r).

So for a pair (x in the segment, y in L), after reversal, x is still in the segment (positions l to r), so their positions are still x > y. So the order of positions between x and y remains the same. However, the elements x and y might now form an inversion or not, depending on their values.

But this depends on the elements, not their positions, which complicates things.

Wait, but perhaps the parity of the change in inversion count for all external pairs can be determined by the number of elements in the segment and their parity.

Wait, another approach: Let's model the parity change as follows.

When you reverse a segment [l, r], the change in inversion count's parity is equal to:

delta = (k*(k-1)/2) mod 2 + (number of pairs (x, y) where x and y are in the segment and x is in L or R) ?

Not sure.

Alternatively, think about the following: For each element x in the segment, when the segment is reversed, x's new position is l + r - i (where i is the original position). So the elements in the segment are now in reverse order.

For the pairs (x, y) where x is in the segment and y is not:

If y is in L (j < l), then after reversal, x's new position is still >= l, so j < new_x. So the order of positions (new_x, j) is same as (i, j) since j < l <= i. So the positions are ordered as new_x > j. So the original pair (i, j) had i > j, and after reversal, new_x > j. So the positions are the same. However, the elements are now different. The x in the new_x position is the element that was at position l + r - i. So the pair (element at new_x, element at j) could be an inversion or not.

But how to model the parity change for all these pairs?

This seems intractable. So perhaps there's a mathematical trick here.

Wait, let's think about the parity of the number of pairs (x, y) where x is in the segment and y is not, and (x > y) in the original array, and (x' < y) in the reversed array (where x' is the element that replaces x after reversal).

But this is complicated.

Alternative idea: For the external pairs, the parity change is equal to the number of pairs (x, y) where x is in the segment and y is not, and (x and y form an inversion) in the original but not after reversal, plus those that didn't form an inversion before but do after. The parity of this sum is the delta for external pairs.

But how to compute this sum mod 2?

Another observation: the elements in the segment are reversed, so for each x in the segment, the elements that were after x (within the segment) become before x, and vice versa. But for external elements, their positions relative to the entire segment are the same.

Wait, but the elements in the segment are now in reverse order. So for elements outside the segment, the elements in the segment have their order reversed among themselves, but their collective order relative to the outside elements remains the same. So for example, any element y outside the segment (either left or right) will have all elements in the segment either all to the right or left, but their order among themselves is reversed.

But how does that affect the inversions with y?

For a y in L (left of the segment), all elements in the segment are to the right of y. So for each such y, the elements in the segment form a group. The inversion count between y and the segment is the same as the number of elements in the segment that are less than y (if y is to the left, then inversions would be pairs (element in segment, y) where element in segment < y, leading to inversion because i > j but a[i] < a[j]).

Wait, but after reversal, the elements in the segment are reversed, but their values are the same as before. So for a y in L, the number of elements in the segment that are less than y is the same as before. So the inversion count between y and the segment remains the same. Because the elements are the same, just their order is reversed.

Wait, that's a key insight! Because the elements in the segment are reversed, but the elements themselves are the same. So for any y outside the segment, the number of elements in the segment that are less than y (for y in L) or greater than y (for y in R) is the same as before. Therefore, the inversion count between y and the segment remains the same. Therefore, the external pairs (elements in the segment and outside) do not contribute any change to the inversion count.

Wait, but this can't be right. Because for example, if y is in L and the elements in the segment are [3, 1, 2], then after reversal, the segment becomes [2, 1, 3]. So for y=4 (in L), the original segment has elements 3,1,2. The inversions between y=4 and the segment are (3,4) (since 3 <4), (1 <4), (2 <4). So three inversions. After reversal, the segment elements are 2,1,3. The inversions are (2 <4), (1 <4), (3 <4) — same count. So the count remains the same.

But what if y is in R? Suppose y is in R (to the right of the segment). For example, y=0 (assuming original elements are [3,1,2], y is in R (to the right of the segment, which is in positions 1-3). So after reversal, the segment becomes [2,1,3]. The original inversions between elements in the segment and y=0 (assuming it's larger than all) would be elements in the segment that are larger than y. Wait, no. If y is to the right of the segment, then for inversion count between elements in the segment and y, since the segment is left of y, any element in the segment greater than y would form an inversion (since i < j, a[i] > a[j] is an inversion). Wait, no. The inversion is when i < j and a[i] > a[j]. So if the segment is to the left of y, then for each element x in the segment, if x > y, then it's an inversion (since x is in i < j and x > y). So the number of such x is the count of elements in the segment that are greater than y.

After reversal, the elements in the segment are reversed, but the count of elements greater than y remains the same. Because you're just reordering the elements in the segment. So the total number of x in the segment where x > y is the same as before. Therefore, the inversion count between y and the segment remains the same.

So the conclusion is that reversing a segment does not change the inversion count between elements in the segment and elements outside the segment. Therefore, the only change in inversion count is due to the inversions within the segment and the inversions caused by the reversal of the segment's elements.

Wait, this is a critical insight. Because if the inversion count between the segment and the rest remains the same, then the total change in inversion count is only due to the internal inversions in the segment. And the change there is (k choose 2) mod 2, as discussed earlier.

So the delta parity is (k choose 2) mod 2.

Wait, then the parity of the inversion count after each reversal is the previous parity XOR (k*(k-1)/2) mod 2.

Because when you reverse a segment of length k, the number of inversions within the segment changes by (k choose 2) - 2*original_internal_inversions. Since modulo 2, the -2*... term is 0, so the delta is (k choose 2) mod 2. The external pairs contribute 0 mod 2. So the total delta is (k choose 2) mod 2.

Thus, the overall parity after each reversal is the previous parity XOR (k*(k-1)/2 mod 2).

So this simplifies the problem a lot! Because for each query, we just need to compute the length of the reversed segment (k = r - l + 1), calculate k*(k-1)/2 mod 2, and flip the current parity accordingly.

But wait, let's test this with the examples.

First example:

Input:
3
1 2 3
2
1 2
2 3

Initial permutation is [1,2,3], which has 0 inversions (even).

First query: reverse [1,2] (k=2). k*(k-1)/2 = 1. So delta is 1 mod 2. So parity becomes even XOR 1 = odd. Which matches the first output 'odd'.

Second query: reverse [2,3] (k=2). Again, delta is 1. So parity becomes odd XOR 1 = even. Which matches the output.

Second example:

Input:

4

1 2 4 3

4

1 1

1 4

1 4

2 3

Initial permutation [1,2,4,3], which has 1 inversion (4 and 3) → odd.

First query: reverse [1,1]. k=1. k*(k-1)/2 is 0 → delta 0. Parity remains odd. Output 'odd'.

Second query: reverse [1,4] (k=4). k*(4-1)/2 = 4*3/2 =6 → 6 mod 2 is 0. So parity is odd XOR 0 → odd. Output is 'odd'.

Third query: reverse [1,4] again. k=4, delta 0. Parity remains odd → output 'odd'.

Fourth query: reverse [2,3]. k=2. delta is 1. So parity becomes odd XOR 1 → even. Output 'even'.

But according to the sample output, after the fourth query, the result is even, which matches. So this approach works for the sample.

So the solution is:

- Compute the initial inversion parity (even or odd) of the permutation.

- For each query, calculate k = r - l + 1.

- Compute delta = (k * (k-1) // 2) % 2.

- Flip the current parity by XOR with delta.

- Output 'odd' or 'even' based on the new parity.

This approach is O(n^2) for initial inversion count (since n is up to 1500, n^2 is 2.25 million, which is manageable), and O(1) per query (since m is 2e5, which is acceptable).

So the steps are:

1. Compute the initial inversion count parity.

2. For each query, compute k = r - l + 1.

3. delta = k*(k-1) // 2 mod 2.

4. current_parity ^= delta.

5. Output 'even' or 'odd' based on current_parity.

So the problem reduces to just calculating the initial parity and then handling each query in O(1) time.

Now, the only thing left is to compute the initial parity. For that, we need to compute the number of inversions in the initial permutation modulo 2.

How to compute the inversion count modulo 2 efficiently.

For n up to 1500, a straightforward O(n^2) approach is feasible. We can loop through all pairs i < j and check if a[i] > a[j], incrementing the count. Then mod 2. For 1500 elements, that's 1500*1499/2 = about 1.1 million operations. Which is acceptable.

So the plan is:

- Read the permutation.

- Compute the initial inversion count parity.

- For each query, compute k and delta, update the parity.

Implementing this.

Testing the first example:

Initial permutation is [1,2,3]. Inversion count is 0 → even. So initial parity is 0 (even). After first query (k=2, delta=1), parity becomes 1 (odd). Output 'odd'. Second query (k=2, delta=1 → parity 0) → 'even'.

Second example:

Initial permutation [1,2,4,3]. Inversion count is 1 (4 and 3) → odd. Initial parity is 1. The first query is l=1, r=1 → k=1, delta 0 → parity remains 1. Second query is l=1, r=4 → k=4 → delta 6 mod 2=0. parity remains 1. Third query same as before. Fourth query is l=2, r=3 → k=2 → delta 1. parity becomes 0 → 'even'.

So this approach works.

Thus, the code will:

Read n, read the permutation, compute initial inversion count mod 2.

Read m, then for each query compute k = r - l +1, delta is (k*(k-1)//2) mod2, flip the parity.

So code in Python:

Read n.

a = list(map(int, input().split()))

Compute initial_parity.

Read m.

For each query, l, r:

k = r - l +1

delta = (k*(k-1) //2) %2

current_parity ^= delta

print 'odd' if current_parity else 'even'

So the code's main part is to compute the initial parity.

Implementing that:

initial_parity = 0

for i in range(n):

    for j in range(i+1, n):

        if a[i] > a[j]:

            initial_parity +=1

initial_parity %= 2

Yes.

But wait, in Python, for n=1500, this is 1500*1500/2 = ~1 million iterations. Which is acceptable.

Thus, the code is manageable.

So, putting it all together.

Testing the sample input:

Sample 1:

3

1 2 3

Inversion count 0 → parity 0.

Queries:

1 2 → k=2 → delta 1 → parity 0 ^1 =1 → 'odd'.

2 3 → k=2 → delta 1 → 1^1=0 → 'even'.

Sample 2:

4

1 2 4 3 → inversions: (4,3) → 1 → parity 1.

Queries:

1 1 → k=1 → delta 0 → parity 1.

1 4 →k=4 → 4*3/2=6 →6 mod2=0 → parity 1^0=1.

1 4 → same as before. parity remains 1.

2 3 →k=2 → delta 1. parity 1^1=0 → 'even'.

Which matches the sample outputs.

So this approach is correct.

Thus, the code will work.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
parity = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i] > a[j]:
            parity ^= 1
m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    k = r - l + 1
    delta = (k * (k - 1) // 2) % 2
    parity ^= delta
    print('odd' if parity else 'even')
```