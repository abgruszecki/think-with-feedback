<think>
Okay, let's see. We need to calculate the number of inversions in the sequence after performing a series of swap operations. The initial sequence is just the natural numbers in order, but after each swap, some elements are swapped. The problem is to find the total inversions after all swaps are done.

Hmm. The key here is that each swap affects the positions of elements. The challenge is to track which elements are where after all swaps and then compute the inversions. But since the sequence is infinite, obviously, we can't track all elements. Wait, but the swaps are only a finite number, n up to 1e5. So after all swaps, most elements are in their original positions, except those involved in the swaps. So the actual elements that are moved are the ones that have been part of any swap operation. Because each swap(a, b) swaps the elements at positions a and b. So if you swap 4 and 2, then swap 1 and 4, the elements at positions 1, 2,4 have changed. So the elements in the final sequence are the same as original except for those positions that were swapped. Wait, no. Wait, when you swap positions a and b, the elements at those positions are swapped. So each swap(a,b) exchanges the elements in positions a and b. So after all swaps, each element in the sequence is either in its original position, or has been moved via a series of swaps.

Wait, but the elements themselves are the natural numbers. So for the initial sequence, position i has element i. Then, after some swaps, the elements at positions a and b get swapped each time. So, for example, first swap(4,2): positions 4 and 2 swap. So position 2 now has element 4, position 4 has 2. Then swap(1,4): position 1 and 4 swap. So position 1 now has 2 (from position 4) and position 4 has 1 (from position 1). So after two swaps, the elements at positions 1,2,4 are 2,4,1. So the elements in the sequence are: position 1:2, position 2:4, position 3:3, position 4:1, others are same as original.

The inversions are pairs (i,j) where i<j and p_i > p_j. So in the first example, the final sequence is [2,4,3,1,5,...]. The inversions are (1,4) (since 2>1), (2,3) (4>3), (2,4) (4>1), (3,4) (3>1). So total 4.

So how do we model this? We need to track, after all swaps, which elements are at each position. Then, compute the inversions between those elements. But since the elements are up to 1e9, but the positions are also up to 1e9, but the number of swaps is 1e5, the number of positions that have been swapped is O(n) since each swap introduces two new positions into the set. So we can model the positions that have been swapped and track their current elements.

Wait, but each swap(a, b) affects positions a and b. So over n swaps, each swap adds two new positions. So after n swaps, the number of positions that have been swapped at least once is up to 2n. So for all these positions, we need to track their current elements. The rest of the positions remain as their original elements (since they were never swapped).

So the plan is:

1. Track all positions that have been involved in any swap. For these positions, track their current value. For the others, the value is their original position.

2. Once all swaps are processed, collect all the positions that are swapped. Then, for each such position, their current value is known. All other positions have value equal to their position.

3. Then, compute the number of inversions in this modified sequence.

But how to compute the inversions when there are potentially 2e5 positions (since n is 1e5) with modified values. The rest are in order and thus contribute zero inversions among themselves.

Wait, but the inversions can be of three types:

a) Both elements are in the modified positions.

b) One element is modified, the other is unmodified.

c) Both elements are unmodified. But since in the original sequence, the elements are in order, the unmodified pairs can't contribute to inversions. So only the modified elements and their interactions with others contribute to inversions.

So the problem reduces to:

Compute the inversions between the modified elements, plus the inversions between modified and unmodified elements, plus the inversions where a modified element is on the left of an unmodified element and is larger, or vice versa.

But how to handle this efficiently.

Let me think. Let's denote the set of modified positions as S. The elements in S are the only ones that differ from their original positions. The rest are in their original order.

First, for the inversions between modified elements: this is the standard inversion count among the elements in S. But since the positions in S can be in any order, we need to compute inversions based on their positions. For example, two elements x and y in S, where x is at position a and y is at position b. If a < b but x > y, then this is an inversion.

Second, for modified elements and unmodified elements. Let's consider a modified element x at position a, and an unmodified element y at position b (which is equal to b). So:

If a < b: if x > b, then inversion.

If a > b: if x < b, then inversion (since a > b implies b < a, and in this case, the original element at b is b, which is less than x if x < b. So b < a and original b < x, so the pair (b,a) would have b < a but element b (original) is b, which is less than x. So no inversion. Wait, this is getting complicated. Let's rephrase.

For a modified position a, and an unmodified position b (b not in S):

Case 1: a < b.

If the element at a (x) is greater than b, then inversion (since the element at a is x > b, which is the element at b. So a < b but x > b → inversion).

Case 2: a > b.

If the element at a (x) is less than b, then inversion (since the element at a is x, which is less than the element at b (which is b). So since b < a, and x < b → the element at b (b) is larger than x, and since b < a, the pair (b, a) is an inversion (b < a but element at b is b, which is larger than x. So if x < b, then (b, a) is an inversion.)

So for each modified position a, we need to calculate how many unmodified positions b satisfy:

Either (a < b and x > b) → contributes 1 inversion.

Or (a > b and x < b) → contributes 1 inversion.

But since the unmodified positions are all except those in S, which can be up to 2e5, but the positions can be up to 1e9, we need an efficient way to compute this.

Additionally, the inversions between two modified elements are straightforward if we can list all modified elements sorted by their positions and then compute inversions in their values.

So the steps are:

1. Process all swaps to track the current element at each position involved in swaps.

2. Collect all modified positions (S) and their current elements.

3. Compute the inversions among the modified elements.

4. Compute the inversions between modified elements and unmodified elements.

5. Compute the inversions between modified elements and the unmodified elements, considering all possible positions not in S.

But how?

Let's tackle each part.

First, processing the swaps. For each swap(a, b), we need to swap the elements at positions a and b. So for each swap, we need to look up the current elements at a and b, swap them, and then update our data structure.

So the way to track the elements is using a dictionary (hash map) where the keys are the positions, and the values are the elements at those positions. For any position not in the dictionary, the element is the position's value (since it's never been swapped).

So for example, initially, the dictionary is empty. When we process swap(a, b), we look up the elements at a and b. If a is not in the dictionary, then its element is a. Similarly for b. We then swap the elements, and update the dictionary. So after the swap, the element at a becomes the previous element at b, and the element at b becomes the previous element at a.

This way, after processing all swaps, the dictionary contains all the positions that have been involved in at least one swap, along with their current elements.

That makes sense. So the processing of swaps is manageable in O(n) time, since each swap requires looking up two keys in the dictionary, which is O(1) per operation (assuming average case for hash maps). Since n is up to 1e5, this is acceptable.

Now, once we have the dictionary of modified positions, the next step is to compute the inversions.

Let's first compute the inversions between modified elements.

For modified elements, the positions are a1, a2, ..., am (m up to 2e5). Let's sort them in increasing order of position. Then, the elements at these positions are x1, x2, ..., xm. We need to find the number of pairs (i, j) where i < j (since the positions are sorted) and xi > xj. That's a standard inversion count problem, which can be solved with a Fenwick Tree (BIT) or a merge sort-based approach. The Fenwick Tree approach is O(m log m), which should be acceptable for m up to 2e5 (since 2e5 log 2e5 is about 2e5 * 20 = 4e6, which is manageable).

So that part is doable.

Now, the next part is the inversions between modified elements and unmodified elements.

Let's split this into two cases:

A) Modified elements compared to unmodified elements that are to the right (i.e., unmodified positions larger than the modified position).

B) Modified elements compared to unmodified elements that are to the left (i.e., unmodified positions smaller than the modified position).

For case A: For a modified position a with element x, any unmodified position b > a that has value b (since it's unmodified). The inversion is when x > b. So how many such b's are there where b > a and x > b.

But since b can be up to 1e9, how do we compute this?

Wait, for a given x and a, the number of b's that satisfy b > a and b < x. Because x > b implies b < x.

So the count is the number of integers b in (a, x) such that b is not in the modified positions. Because if b is modified, then it's part of the modified set and handled in other steps.

So the number of such b is max(0, x-1 - a) - (number of modified positions in (a, x)).

Wait, let me think:

The total numbers between a+1 and x-1 is (x-1) - (a+1) + 1 = x - a -1.

But among these, some positions might be modified (i.e., present in S). So the count is (x- a -1) minus the number of modified positions in (a, x-1).

But this is only possible if x > a+1. Otherwise, there are no such positions.

So for each modified position a with x = current element, the number of unmodified positions b > a where x > b is:

max(0, x - a - 1) - count_modified_in_range(a+1, x-1).

But how do we compute this efficiently?

Similarly, for case B: modified position a with element x, and unmodified positions b < a. The inversion occurs when x < b. Because the element at a is x, the element at b is b. So for b < a, x < b implies that x < b < a. So the pair (b, a) is an inversion because b < a but the element at b (b) is larger than x (element at a). So the count here is the number of b in (x, a) where b is unmodified and < a.

So for each modified a, the count is the number of b in (x, a-1) that are unmodified.

Which is (a-1 - x) if a > x, else zero.

But again, subtract the number of modified positions in that interval.

So again, the count is max(0, (a-1 - x)) - count_modified_in_range(x+1, a-1).

But how to compute count_modified_in_range(L, R) efficiently.

The way to do this is to sort all modified positions. Then, for any query L to R, we can perform a binary search to find the number of positions in S that are in [L, R].

So if the modified positions are sorted, then for any a and x, we can compute the required counts.

So the steps are:

- Sort the modified positions in a list, say sorted_S.

Then, for a modified position a and element x:

Case A (b > a and x > b):

The number of unmodified positions is max(0, x- a -1) - (number of modified positions in (a, x-1)).

Which is:

if x <= a: 0.

Else:

number_of_unmodified = (x-1) - (a +1) + 1 = x - a -1.

But subtract the count of modified positions in (a, x-1).

Similarly, case B (b < a and x < b):

The number of unmodified positions is max(0, (a-1) - x) - (number of modified positions in (x+1, a-1)).

So, the total inversions from modified to unmodified elements is the sum over all modified positions a of (case A count + case B count).

So the key is to pre-sort the modified positions and then for each a and x, compute these two counts using binary search.

Now, the third component is the inversions between modified elements and unmodified elements. So combining the two cases.

Additionally, there's the inversions between modified elements, which is the first component.

So overall, the total inversions are:

inversion_among_modified + sum for each modified a (caseA + caseB).

Now, the problem is to compute all of this efficiently.

Let's outline the steps:

1. Process all swaps to build the dictionary of modified positions and their elements.

   - For each swap(a, b):

      - Get the current elements of a and b (from the dict, default to a and b respectively).

      - Swap them and update the dict.

2. Collect all modified positions into a sorted list sorted_S.

3. Compute inversion_among_modified using a Fenwick Tree:

   - Iterate through the sorted_S in order (which is increasing in position, which is important because in the inversion count, the positions are ordered, so pairs (i,j) where i<j (positions) and x_i > x_j.

   - For each x in the elements of sorted positions (sorted_S), we can process them in the order of sorted positions (so position a1 <= a2 <= ... <= am).

   - Then, for each x_i (element at position a_i), the number of elements already processed (to the left) that are greater than x_i is the inversion count added for this element. This can be tracked using a Fenwick Tree that keeps the frequency of elements. But since elements can be up to 1e9, we need to coordinate compress the elements.

   - Wait, but the elements in the modified positions are the original elements from their positions, but swapped. So each element is either a position's original element (i.e., the element was not involved in any swap) or was swapped. Wait, no. For example, after a swap(a,b), the elements at a and b are the original elements from b and a. Then, if another swap happens involving a, the elements are swapped again.

   - So the elements in the modified positions can be any of the original elements (since each swap exchanges elements between two positions). So the elements in the modified positions can be up to 1e9, but there are only O(n) such elements (since each swap affects two elements, and n is 1e5). So the number of unique elements in the modified positions is up to 2e5.

   So coordinate compression is possible here. We can collect all the elements present in the modified positions, sort them, assign a rank to each, and then use a Fenwick Tree based on the ranks.

   So step 3a: collect all elements in the modified positions, sort and assign ranks.

   Then, for inversion_among_modified:

   Initialize a Fenwick Tree with the maximum rank.

   Iterate through the sorted_S (sorted by position) in order. For each element x in the current modified positions, we need to find how many elements already added to the Fenwick Tree are greater than x. This is equivalent to the number of elements in the Fenwick Tree that are > x. To compute this, if the Fenwick Tree has elements sorted, we can query the sum of elements with rank > x's rank. So the inversion count for each x is (current number of elements in the Fenwick Tree) - query sum of elements <= x.

   So for each x in the sorted_S elements (sorted by position), add to inversion_among_modified the number of elements already in the Fenwick Tree that are greater than x. Then, insert x into the Fenwick Tree.

4. Compute the sum over all modified positions of caseA and caseB.

   For this:

   a. Sort the modified positions sorted_S.

   b. For each a in sorted_S, x is the element at a (from the dictionary).

      i. Compute caseA: a < b (unmodified) and x > b.

         - The range for b is (a, x-1). So count how many integers are in (a, x-1) that are not in S.

         - The number of integers in (a, x-1) is (x-1 - a) if x > a+1. Otherwise zero.

         - Then subtract the count of modified positions in (a, x-1).

      ii. Compute caseB: a > b (unmodified) and x < b.

         - The range for b is (x+1, a-1). So count how many integers are in (x+1, a-1) that are not in S.

         - The number is (a-1 - (x+1) + 1) = a - x - 1, if a-1 >= x+1. Else zero.

         - Then subtract the count of modified positions in (x+1, a-1).

      iii. Sum caseA and caseB for each a, add to the total.

5. Sum inversion_among_modified and the sum from caseA and caseB.

So all the steps are manageable, but let's see how to implement them.

First, handling the Fenwick Tree for inversion_among_modified:

We need to collect all the elements from the modified positions, then assign ranks. For example, if the elements are [5,3,1,4], sorted as [1,3,4,5], then rank 1 is 1, etc.

But the elements can be up to 1e9. However, since there are up to 2e5 elements, we can collect all of them, sort, deduplicate, and assign a unique rank.

So:

modified_elements = list of elements in S (values of the dictionary).

sorted_unique = sorted(list(set(modified_elements)))

rank = {v: i+1 for i, v in enumerate(sorted_unique)}  # ranks start from 1.

The Fenwick Tree's size is len(sorted_unique).

For each element x in the modified elements (in the order of sorted_S's positions), we get its rank, then query the number of elements with rank > current_rank. Which is the same as the total elements so far minus the number of elements <= x.

So for inversion_among_modified, each step:

count = fenwick.query(rank[x] - 1)  # number of elements <= x-1? Wait, no. Wait, the Fenwick Tree stores the count of each element. So when we insert x, the Fenwick Tree at position rank[x] is incremented by 1.

Then, the number of elements greater than x is (current size of Fenwick Tree) - (number of elements <= x).

Because the current size is the number of elements added so far (before this x). Because we process in order of positions, which is sorted, so inserting a_i's x_i in order.

Wait, let me clarify:

We process the modified elements in the order of their positions (sorted_S). For each x_i (element at a_i), we need to find how many elements already in the Fenwick Tree are greater than x_i. Since the Fenwick Tree contains all elements processed before (i < j, since a_i < a_j), which have positions to the left, but their x's can be anything. So for x_i, the number of elements already in the Fenwick Tree with value > x_i is the inversion count for this step.

To compute this, the Fenwick Tree can support a query for the sum of elements > x_i. Which is the same as the sum of elements in (x_i+1, max_element).

But since the elements are coordinate compressed, the Fenwick Tree can be queried for the sum from rank_x+1 to max_rank.

But how?

Alternatively, since the Fenwick Tree is built with the ranks sorted, for a given x, the number of elements greater than x is the total elements added so far (count) minus the number of elements <= x.

Because the Fenwick Tree is 1-based, the elements are stored in their rank positions.

So the query for sum up to rank_x gives the number of elements <= x. So the number of elements > x is (count_so_far) - query(rank_x).

So during processing:

Initialize inversion_among_modified = 0.

count_so_far = 0.

For each x in sorted_S (ordered by position):

   current_rank = rank[x]

   inversion_among_modified += count_so_far - fenwick.query(current_rank)

   fenwick.update(current_rank, 1)

   count_so_far += 1

So that's manageable.

Now, for the caseA and caseB computations.

First, sorted_S is the list of modified positions sorted in increasing order. So for a given a in sorted_S, we can find the number of modified positions in a certain interval using binary search.

For example, to find the number of modified positions in (L, R), we can use bisect_left and bisect_right on sorted_S.

Like:

left = bisect.bisect_right(sorted_S, L) 

right = bisect.bisect_left(sorted_S, R + 1)

count = right - left

Wait, no. Wait, sorted_S is sorted. For example, to find the number of elements in [a+1, x-1], since in caseA, the interval is (a, x-1), which is a+1 <= b <= x-1.

Wait, caseA's interval for b is a < b < x. So the b's are in (a, x). Since b is integer, it's a+1 <= b <= x-1.

So for caseA, the number of modified positions in (a, x-1) is the number of elements in sorted_S that are >a and <= x-1.

Which can be computed as:

left = bisect.bisect_right(sorted_S, a)

right = bisect.bisect_right(sorted_S, x-1)

count_modified_in_caseA = right - left

Similarly for caseB, the interval is (x+1, a-1). So x+1 <= b <= a-1.

So:

left = bisect.bisect_left(sorted_S, x+1)

right = bisect.bisect_left(sorted_S, a)  # since a is a modified position, sorted_S contains a. So the elements <= a-1 are before the first occurrence of a.

count_modified_in_caseB = right - left

So for each a in sorted_S, x is the element at a.

CaseA:

If x > a:

   the total numbers in (a, x-1) is (x-1 - a) → (x-1 - a) = (x - a -1) → since integers a+1 to x-1.

   but if x <= a, then this is zero.

So caseA_count = max(0, x - a - 1) - count_modified_in_caseA.

CaseB:

If x < a:

   the numbers in (x+1, a-1) is (a-1 - (x+1) + 1) = (a-1 -x -1 +1) = a -x -1.

   if a <= x+1, then zero.

So caseB_count = max(0, a - x -1) - count_modified_in_caseB.

So for each a in sorted_S, x is the element at a:

sum += caseA_count + caseB_count.

So the steps are:

For each a in sorted_S:

   x = dict[a]

   # compute caseA:

   if x > a:

       possible_b_count = x - a - 1

       if possible_b_count > 0:

           # find how many modified positions are in (a, x-1)

           left = bisect.bisect_right(sorted_S, a)

           right_pos = x-1

           right = bisect.bisect_right(sorted_S, right_pos)

           count_modified = right - left

           caseA = possible_b_count - count_modified

       else:

           caseA = 0

   else:

       caseA = 0

   # compute caseB:

   if x < a:

       possible_b_count = a - x -1

       if possible_b_count >0:

           # find modified positions in (x+1, a-1)

           left_pos = x +1

           right_pos = a-1

           left = bisect.bisect_left(sorted_S, left_pos)

           right = bisect.bisect_left(sorted_S, a)  # since sorted_S contains a, and a-1 < a.

           count_modified = right - left

           caseB = possible_b_count - count_modified

       else:

           caseB =0

   else:

       caseB=0

   total_case += caseA + caseB

But how to compute this efficiently.

For each a in sorted_S, these operations are O(log m), since bisect is O(log m) per step, and m is up to 2e5. So 2e5 * log 2e5 is acceptable.

So putting it all together.

Now, the next challenge is handling all these steps correctly, especially edge cases.

For example, if x == a, then caseA and caseB are zero. Similarly, if x is just a+1, then caseA's possible_b_count is zero.

Another edge case is when x is 1e9 and a is small. Then, x -a -1 could be a huge number. But since x can be up to 1e9, subtracting a (which can be up to 1e9 as well) could result in possible_b_count up to 1e9. But if there are many modified positions in that range, the count_modified can be subtracted, but how to handle the possible_b_count?

Wait, but for possible_b_count, which is the total numbers in (a, x-1), but x can be up to 1e9, and a can be up to 1e9 as well. So possible_b_count can be up to 1e9, but subtracting the count_modified (which is up to 2e5) is manageable, because the possible_b_count could be up to 1e9, which is way too big to compute.

Wait, but how can that be possible? For example, suppose a is 1 and x is 1e9. Then possible_b_count is 1e9 -1 -1 = 999999998. But the problem is that this is a huge number, and subtracting the count_modified (number of modified positions in (1, 999999999-1) = (1, 999999998)), which could be up to 2e5. But 999,999,998 is way larger than 2e5, so possible_b_count - count_modified is 999,999,998 - O(2e5), which is about 999 million. But the answer would be the sum of all such terms. But if there are 2e5 such a's, each contributing up to 1e9, the sum would be 2e5 * 1e9 = 2e14, which is way beyond the memory and computational limits.

But that's impossible, because the time limit is 2 seconds, which allows about 4e8 operations. So how to handle this.

Wait, but this suggests that the approach is not feasible. Because for each modified a, caseA and caseB can involve numbers up to 1e9, leading to O(2e5 * 1e9) operations, which is impossible.

But there's a mistake here.

Wait, the possible_b_count is the number of unmodified positions in the interval. But the way we compute possible_b_count is (x - a -1) for caseA. But x is the element at position a. So what is the maximum possible x?

Wait, the elements are the original elements (which are their positions) after swapping. So for example, if a is 1, and during the swaps, it's been swapped with other positions. The element at a can be up to 1e9 (the maximum possible position in the swaps). So x can be up to 1e9.

So in the case where a is 1 and x is 1e9, the possible_b_count is 1e9 -1 -1 = 999,999,998, but how do we compute that without iterating through all those numbers?

But the problem is that the number of unmodified positions in the interval (a, x-1) is (x - a -1) - count_modified_in_interval. So if x is large, but the modified positions in the interval are few, this could be a huge number.

But how can we compute this quickly? Because for each a, x is known, and the number of modified positions in the interval can be found via binary search. But (x - a -1) can be up to 1e9, and subtracting a small count_modified (like 2e5) would still result in 1e9, which is impossible to handle as a 64-bit integer.

But the problem statement says that the output can be up to whatever, but in Python, integers are arbitrary precision, so the code can handle it. But how to compute (x - a -1) when x is 1e9 and a is 1.

But that's manageable, because (x - a -1) is computed as a simple arithmetic operation. For example, 1e9 -1 -1 is 999,999,998.

So the sum for all a's can be as large as 2e5 * 1e9 = 2e14, which is a very large number, but Python can handle it.

But how to compute this in O(1) time per a.

Yes, because (x -a -1) is a simple subtraction. Then, subtract the count_modified_in_interval (which is found via binary search in O(log m) time).

So the sum can be computed as a sum of O(2e5) terms, each of which is O(1) plus O(log m) time. That's acceptable.

So the approach is feasible.

Now, the steps for the code:

First, process the swaps.

Implement a dictionary to track the current elements.

For each swap a and b:

   current_a = the element at a (if not in the dictionary, it's a).

   current_b = the element at b (if not in the dictionary, it's b).

   swap them: set the element at a to current_b, and element at b to current_a.

Then, collect all keys in the dictionary (the modified positions), and sort them into sorted_S.

Then, for each position in sorted_S, collect the elements into a list of x's.

Then, compute inversion_among_modified using a Fenwick Tree with coordinate compression.

Then, compute the sum of caseA and caseB for each a in sorted_S.

Sum everything and output.

Now, code.

Let's start coding.

But how to handle the Fenwick Tree.

Implement a Fenwick Tree:

class FenwickTree:

    def __init__(self, size):

        self.size = size

        self.tree = [0]*(size + 1)

    def update(self, idx, delta):

        while idx <= self.size:

            self.tree[idx] += delta

            idx += idx & -idx

    def query(self, idx):

        res = 0

        while idx > 0:

            res += self.tree[idx]

            idx -= idx & -idx

        return res

But for coordinate compression, we need to collect all elements in the modified positions, then sort and assign ranks.

So:

modified_positions = list of a's in the dictionary.

sorted_S = sorted(modified_positions)

elements = [d[a] for a in sorted_S]

unique_elements = sorted(list(set(elements)))

rank = {v:i+1 for i, v in enumerate(unique_elements)}  # ranks start from 1.

max_rank = len(unique_elements)

fenwick = FenwickTree(max_rank)

Then, inversion_among_modified is computed as:

inv_mod = 0

count_so_far = 0

for x in elements:

    r = rank[x]

    # elements added so far is count_so_far.

    # query the number of elements <= x: fenwick.query(r)

    # elements greater than x: count_so_far - fenwick.query(r)

    inv_mod += count_so_far - fenwick.query(r)

    fenwick.update(r, 1)

    count_so_far += 1

So that's the inversion_among_modified.

Then, compute the sum_case:

sum_case = 0

for a in sorted_S:

    x = d[a]

    # caseA: a < b, b is unmodified, x > b.

    # b is in (a, x-1)

    if x > a:

        possible = x - a -1

        if possible > 0:

            # find modified positions in (a, x-1)

            L = a

            R = x-1

            # number of modified positions in (L, R) is bisect_right(R) - bisect_right(L)

            left = bisect.bisect_right(sorted_S, L)

            right = bisect.bisect_right(sorted_S, R)

            count_modified = right - left

            sum_case += possible - count_modified

    # caseB: a > b, b is unmodified, x < b.

    if x < a:

        possible = a - x -1

        if possible >0:

            # b is in (x+1, a-1)

            L = x+1

            R = a-1

            left = bisect.bisect_left(sorted_S, L)

            right = bisect.bisect_left(sorted_S, a)  # since a is in sorted_S, elements <= a-1 are before the first occurrence of a.

            count_modified = right - left

            sum_case += possible - count_modified

So sum_case is the sum of caseA and caseB for all a in sorted_S.

Then, total_inversions = inv_mod + sum_case.

Now, let's test with the first sample input.

Sample 1:

Input:

2

4 2

1 4

Processing swaps:

Swap 4 and 2:

dict after first swap: {4:2, 2:4}.

Swap 1 and 4:

elements at 1 (not in dict, so 1) and 4 (value is 2).

swap them: set 1 to 2, set 4 to 1.

dict is {1:2, 2:4,4:1}

So modified positions are [1,2,4], sorted_S = [1,2,4].

elements = [2,4,1]

unique_elements sorted: [1,2,4], rank is {1:1, 2:2,4:3}.

Processing inversion_among_modified:

elements in order 2,4,1.

First x=2 (rank 2):

count_so_far=0 → inv_mod += 0 -0 =0.

fenwick updated with 2.

count_so_far=1.

Second x=4 (rank3):

query(3) is 1 (only 2 is in the tree, which is rank 2 <=3). So count_so_far is 1. 1 -1 =0. inv_mod remains 0.

fenwick has 2 and 4. count_so_far=2.

Third x=1 (rank1):

query(1) returns 0. count_so_far=2 → 2-0=2. inv_mod +=2 → total 2.

So inversion_among_modified is 2.

sum_case:

For a=1, x=2:

caseA: x=2 >a=1.

possible =2-1-1=0. so no contribution.

caseB: x=2 <a=1? No. So caseB=0.

sum_case +=0.

For a=2, x=4:

caseA: x=4> a=2.

possible=4-2-1=1. possible is 1.

Check modified positions in (2, 3). sorted_S is [1,2,4]. So L=2, R=3.

bisect_right(sorted_S, 2) → index 2 (since sorted_S[1] is 2, bisect_right returns 2.

bisect_right(sorted_S, 3) → 3 (since 3 is between 2 and4, so returns index2 (if sorted_S is [1,2,4], then indices are 0,1,2. 3 is inserted at index 3? No. Wait, 3 is less than 4, so bisect_right(sorted_S,3) returns 2.

So count_modified=2-2=0. possible - count_modified=1-0=1. sum_case +=1.

caseB: x=4> a=2 → no.

sum_case becomes 1.

For a=4, x=1:

caseA: x=1 < a=4. So no.

caseB: x=1 < a=4 → possible=4-1-1=2. interval is x+1=2 to a-1=3. So L=2, R=3.

bisect_left(sorted_S, 2) is index1 (sorted_S[1] is 2.

bisect_left(sorted_S, 4) is 2.

count_modified=2-1=1.

possible is 2, sum_case += 2-1=1.

sum_case +=1. So sum_case is 1+1=2.

Total sum_case is 1 (from a=2) + 1 (from a=4) → 2?

Wait, let's recheck.

For a=4, x=1.

caseB: x=1 <4. possible is 4-1-1=2.

The interval is (1+1,4-1) → (2,3).

Modified positions in this interval are 2 (since sorted_S is [1,2,4]. So positions in (2,3) are 2 (since 2 is in the interval? Wait, 2 is in sorted_S. So in the interval [2,3], the modified positions are 2.

bisect_left(sorted_S, L=2) → returns index1 (since sorted_S[1] is 2).

bisect_left(sorted_S, a=4) → returns index2.

count_modified = 2-1=1.

possible - count_modified is 2-1=1. So sum_case +=1.

So sum_case is 1 (a=2) +1 (a=4) =2.

So total inversions is inv_mod (2) + sum_case (2) =4, which matches the sample.

Yes.

So code seems correct.

Now, implement this in Python.

Now, the code steps:

Read n.

Process n swaps, building the dictionary.

Collect sorted_S and elements.

Compute inversion_among_modified.

Compute sum_case.

Output total.

Now, code.

But also, we need to handle the case where the same position is swapped multiple times.

For example, swap(1,2), then swap(1,3). The dictionary will track the current elements at 1,2,3.

So the code should correctly process all swaps.

Now, code:

Testing against sample input 1.

```python
import bisect


class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 2)  # 1-based indexing

    def update(self, idx, delta=1):
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

def main(input_stream, output_stream):
    import sys
    input = input_stream.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr +=1
    swaps = []
    d = dict()
    for _ in range(n):
        a = int(input[ptr])
        b = int(input[ptr+1])
        ptr +=2
        # Process swap(a, b)
        # Get current elements of a and b
        val_a = d.get(a, a)
        val_b = d.get(b, b)
        # Swap them
        d[a] = val_b
        d[b] = val_a

    sorted_S = sorted(d.keys())
    elements = [d[a] for a in sorted_S]
    # Compute inversion among modified elements
    # Coordinate compression
    unique_elements = sorted(list(set(elements)))
    rank = {v:i+1 for i, v in enumerate(unique_elements)}  # ranks start from 1
    max_rank = len(unique_elements)
    ft = FenwickTree(max_rank)
    inv_mod = 0
    count_so_far = 0
    for x in elements:
        r = rank[x]
        inv_mod += count_so_far - ft.query(r)
        ft.update(r)
        count_so_far +=1
    # Compute sum_case
    sum_case =0
    # sorted_S is the sorted list of modified positions
    for a in sorted_S:
        x = d[a]
        # caseA
        if x > a:
            possible = x - a -1
            if possible >0:
                L = a
                R = x-1
                # modified positions in (L, R)
                left = bisect.bisect_right(sorted_S, L)
                right = bisect.bisect_right(sorted_S, R)
                count_modified = right - left
                sum_case += possible - count_modified
        # caseB
        if x < a:
            possible = a - x -1
            if possible >0:
                L = x +1
                R = a -1
                left = bisect.bisect_left(sorted_S, L)
                right = bisect.bisect_left(sorted_S, a)
                count_modified = right - left
                sum_case += possible - count_modified
    total = inv_mod + sum_case
    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
1 6
3 4
2 5
""",
            "output": \
"""\
15
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

The second sample:

Input:

3

1 6

3 4

2 5

Let's see:

Process swaps:

swap(1,6):

d[1] =6, d[6]=1.

swap(3,4):

d[3]=4, d[4]=3.

swap(2,5):

d[2]=5, d[5]=2.

sorted_S = [1,2,3,4,5,6]

elements = [6,5,4,3,2,1]

unique_elements sorted is [1,2,3,4,5,6], so ranks are 1:1, 2:2, etc.

For inversion_among_modified:

elements are [6,5,4,3,2,1]

Processing each x:

x=6: rank 6. query(6) returns 0. inv_mod +=0.

x=5: rank5. query(5) returns 0. inv_mod +=1 (count_so_far is 1). Total 1.

x=4: rank4. query(4) returns 0. inv_mod +=2 (count_so_far is 2). Total 3.

x=3: rank3. query(3) returns0. inv_mod +=3 (count_so_far 3). Total 6.

x=2: rank2. query(2) returns0. inv_mod +=4 (count_so_far 4). Total 10.

x=1: rank1. query(1) returns0. inv_mod +=5. Total 15.

So inversion_among_modified is 0+1+2+3+4+5 =15.

sum_case:

For each a in sorted_S [1,2,3,4,5,6], x is 6,5,4,3,2,1 respectively.

For a=1, x=6:

caseA: x=6>1. possible=6-1-1=4. interval (1,5). Check modified positions in (1,5).

sorted_S is [1,2,3,4,5,6]. bisect_right(1) is 1 (since sorted_S[0]=1, bisect_right returns 1). bisect_right(5) is 5 (since 5 is in the list, and bisect_right returns the index after 5's first occurrence. But sorted_S has 5 at index4. So bisect_right(5) returns5.

count_modified =5-1=4. possible (4) -4 =0. sum_case +=0.

caseB: x=6>1, no.

For a=2, x=5:

caseA: x=5>2. possible=5-2-1=2. interval (2,4). modified positions in this range are 3,4.

bisect_right(2) returns2 (sorted_S[1]=2, bisect_right returns2). bisect_right(4) is4. count_modified=4-2=2. 2-2=0. sum_case +=0.

caseB: x=5 <2? No.

For a=3, x=4:

caseA: 4>3. possible=4-3-1=0. no contribution.

caseB:4<3? No.

For a=4, x=3:

caseA:3>4? No.

caseB:3<4. possible=4-3-1=0. no.

For a=5, x=2:

caseA:2>5? No.

caseB:2<5. possible=5-2-1=2. interval is (3,4). modified positions are 3,4.

bisect_left(3) is2 (since sorted_S[2]=3). bisect_left(5) is4. count_modified=4-2=2. possible (2) -2=0. sum_case +=0.

For a=6, x=1:

caseA:1>6? No.

caseB:1<6. possible=6-1-1=4. interval is (2,5). modified positions are 2,3,4,5.

bisect_left(2) is1. bisect_left(6) is5. count_modified=5-1=4. possible (4) -4=0.

So sum_case is 0 for all a's. So total is 15+0=15. Which matches the sample.

Thus, the code works for the second sample.
</think>

```python
import bisect

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 2)

    def update(self, idx, delta=1):
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & -idx

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    d = {}
    for _ in range(n):
        a = int(input[ptr])
        b = int(input[ptr+1])
        ptr += 2
        val_a = d.get(a, a)
        val_b = d.get(b, b)
        d[a] = val_b
        d[b] = val_a

    sorted_S = sorted(d.keys())
    if not sorted_S:
        print(0)
        return

    elements = [d[a] for a in sorted_S]
    unique_elements = sorted(set(elements))
    rank = {v: i+1 for i, v in enumerate(unique_elements)}
    max_rank = len(unique_elements)
    ft = FenwickTree(max_rank)
    inv_mod = 0
    count_so_far = 0

    for x in elements:
        r = rank[x]
        inv_mod += count_so_far - ft.query(r)
        ft.update(r)
        count_so_far += 1

    sum_case = 0
    for a in sorted_S:
        x = d[a]
        if x > a:
            possible = x - a - 1
            if possible > 0:
                left = bisect.bisect_right(sorted_S, a)
                right = bisect.bisect_right(sorted_S, x-1)
                sum_case += possible - (right - left)
        if x < a:
            possible = a - x - 1
            if possible > 0:
                left = bisect.bisect_left(sorted_S, x + 1)
                right = bisect.bisect_left(sorted_S, a)
                sum_case += possible - (right - left)

    print(inv_mod + sum_case)

if __name__ == "__main__":
    main()
```
