<think>
Okay, I need to solve this problem. Let's read it carefully.

The problem is about distributing pencils into boxes such that each box has at least k pencils, and any two pencils in the same box have a saturation difference at most d. The task is to determine if such a distribution is possible.

First, let's understand the constraints. The input size can be up to 5e5, which is 500,000. So any O(n^2) algorithm is out of the question. We need something O(n log n) or O(n) time.

The key idea here is that if we sort the pencils, we can group them into consecutive sequences where the difference between the first and last in the group is <=d. But each group must have at least k pencils. Wait, but the problem allows us to split them as long as each group is a consecutive sorted sequence with max-min <=d and size >=k. Hmm, but how do we partition the sorted array into such groups optimally?

Wait, the approach would be to sort the array first. Then, we can find the earliest positions where a group can end. For dynamic programming, perhaps. Let's think of dynamic programming here.

Let me think. Let's sort the array. Then, for each position i, we want to know if it's possible to partition the first i pencils into valid groups. The valid transitions would be from j to i, where j is such that i-j+1 >=k and a[i] -a[j] <=d. Then, the DP[i] is true if there exists some j where DP[j-1] is true and the conditions are met.

But with n up to 5e5, a standard DP approach with O(n^2) transitions would be way too slow. So we need a way to compute this efficiently.

So the problem reduces to, after sorting the array, can we split the array into groups where each group is a consecutive segment of size at least k, and the max and min in the group (since the array is sorted, max is the last element and min is the first) differ by at most d. So each group must satisfy a[r] - a[l] <=d, where l and r are the start and end indices of the group, and the size r-l+1 >=k.

The DP approach can be optimized by maintaining a sliding window of possible j's. Let's see.

We can sort the array first. Then, for each i, the earliest j where a[i] - a[j] <=d is the leftmost j where a[i] -a[j] <=d. So for each i, j can be found via binary search. But even then, for each i, we need to check if there's any position j where (j-1) is a valid end (DP[j-1] is true) and j to i is a valid group (size >=k and a[i]-a[j] <=d).

So, the DP array would be as follows:

dp[i] is True if the first i elements can be partitioned into valid groups.

The base case is dp[0] = True (zero elements can be partitioned).

For i >=1, dp[i] is True if there exists a j <=i -k +1, such that j >=1, and a[i] -a[j] <=d, and dp[j-1] is True.

Because the group j..i must have at least k elements, so j can be from 1 to i -k +1. Wait, wait, the group size is i-j+1. So for group size >=k, i-j+1 >=k → j <= i -k +1. But j must be at least 1 (since the group starts at j). So j ranges from max(1, i -k +1 - ...) down to the leftmost possible j where a[i] -a[j] <=d.

So for each i, we need to check if there exists a j in the range [left, i -k +1], such that j >= left and j <= i -k +1, and dp[j-1] is True. Here, left is the smallest j where a[i] -a[j] <=d.

But checking this for each i directly would still be O(n) per i, leading to O(n^2) time. Which is not feasible.

So we need a way to compute, for each i, the maximum left j where a[i] -a[j] <=d. Then, the possible j's are from left_j to i -k +1, but j must be >=1 and i-j+1 >=k. So for each i, the valid j's are in the interval [left_j, i -k +1]. Then, we need to check if there's any j in this interval where dp[j-1] is True.

The key is to find if in that interval, there's any position where dp[j-1] is True. If yes, then dp[i] is True.

So the problem becomes, for each i, determine if there's a j in [a, b] such that dp[j-1] is True. Then, we can model this as a 1D range maximum query (or existence) problem, where we need to know if any in the range is True.

But how to compute this efficiently?

An efficient way would be to precompute a prefix array that keeps track of the positions where dp is True. Then, for a given interval [a, b], we can check if there's at least one j in this interval where j-1 is a position where dp is True. Since j ranges from a to b, then j-1 ranges from a-1 to b-1. So we need to check if any of the dp entries from (a-1) to (b-1) inclusive are True.

Wait, the j's in the interval [a, b] (for j) would correspond to j-1 in [a-1, b-1], and dp[j-1] must be True.

So for each i, the interval for j is [left_j, right_j], where right_j is i -k +1.

Then, the interval for j-1 is [left_j-1, right_j-1].

So, if the dp array is maintained as a binary array, we need to check if there's any True in this range.

To answer such range existence queries efficiently, we can use a segment tree or a binary indexed tree (Fenwick tree) that allows us to track the presence of True values and query ranges.

But with 5e5 elements, a segment tree would be manageable. Alternatively, we can use a prefix array that tracks the earliest position where a True occurs up to a certain index. Let's think of that.

Alternatively, we can keep track of the earliest and latest positions where True is present. Wait, no. Because we need to check for existence in a range. So for example, if the current interval is [L, R], we need to know if there's any True in that interval.

So a segment tree that can answer range OR queries would be useful. Because the OR of a range would be True if any of the elements in that range is True.

Yes. So, we can use a segment tree that supports the following operations:

1. Update a position (mark it as True)
2. Query a range [a, b] to see if any element is True.

Each query for the range [a, b] in the segment tree would take O(log n) time.

So the plan is:

- Sort the array a in non-decreasing order.
- Initialize a dp array, where dp[i] is True if the first i elements can be partitioned into valid groups.
- The base case is dp[0] = True.
- Initialize the segment tree with the initial value (all False except dp[0] which is True).
- For each i from 1 to n:
   - Find the leftmost j where a[i] - a[j] <=d. This can be done via binary search since the array is sorted.
   - The right_j for possible j is i -k +1. But j must be >=1 (since group starts at j, and j=1 implies the group starts at 1, and ends at i, which is i elements. Wait, j can be from 1 to i -k +1, but only if i -k +1 >=1. Otherwise, j is not possible. For example, if i <k, then i -k +1 is <=0, so no possible j. So for i <k, dp[i] is False.
   - So for i <k: dp[i] is False. So we can skip these i's.
   - For i >=k, compute left_j via binary search. Then, the valid j's are from left_j to right_j = i -k +1. But j must be <= i -k +1 and >= left_j. So the j's are in [left_j, right_j]. However, if left_j > right_j, then there is no possible j, so dp[i] is False.
   - Otherwise, we need to check if there's any j in [left_j, right_j], which corresponds to j-1 in [left_j-1, right_j-1], and see if any dp[j-1] is True.
   - So the query in the segment tree is for the range [left_j-1, right_j-1].
   - If the query returns True, then dp[i] = True, and we update the segment tree by setting position i to True (since dp[i] is now True).
   - Otherwise, dp[i] remains False.

This approach would have a time complexity of O(n log n) because each binary search is O(log n), and each query and update in the segment tree is O(log n), and this is done for each of the n elements.

Now, let's think about the steps.

First, sort the array. That's O(n log n) time.

Then, for each i from 1 to n:

If i <k, skip (dp[i] remains False).

Else:

Find the left_j via binary search. How?

We can compute the maximum possible j where a[i] - a[j] <=d. So for each i, the earliest j is the first position where a[j] >= a[i] -d. But since the array is sorted, a[j] increases with j. So we can find the minimum j where a[i] - a[j] <=d. Wait, no. Wait, the array is sorted in non-decreasing order. So for a[i], the leftmost j where a[i] - a[j] <=d is the smallest j such that a[j] >= a[i] -d. Because if j is the first index where a[j] >= a[i] -d, then all elements from j to i will have a[i] -a[x] <=d. So the maximum possible group is from j to i.

Wait, for example, the group j to i has a[i] -a[j] <=d. Any x >=j will have a[x] >= a[j], so a[i] -a[x] <=a[i] -a[j] <=d. So the entire group from j to i is a valid group in terms of the difference condition.

So the left_j is the smallest j such that a[i] -a[j] <=d. Then, any j in [left_j, i -k +1] is a possible start of the group. Because the group must have size >=k, so j must be <= i -k +1.

So for each i >=k:

Compute left_j as the first position where a[j] >= a[i] -d. Then, the possible j's are in [left_j, i -k +1]. But if left_j > i -k +1, then no possible j, so dp[i] is False.

Otherwise, check if there's any j in [left_j, i -k +1] such that dp[j-1] is True. If yes, then dp[i] is True.

So the steps are:

Sort the array.

Initialize dp[0] as True.

For each i from 1 to n:

   if i <k: continue (dp[i] remains False)
   else:

      left_j = binary search for the smallest j where a[j] >= a[i] -d
      right_j = i -k +1
      if left_j > right_j: continue (dp[i] is False)
      else:

          query the segment tree for the range [left_j-1, right_j-1]

          if any True in that range, then dp[i] = True, and update the segment tree.

Finally, check if dp[n] is True.

Now, implement this.

But how to handle the binary search?

In Python, the bisect module can be used. For the sorted array a, to find the leftmost j where a[j] >= a[i] -d. Wait, but the array is sorted. So for the sorted array, we can use bisect_left.

Wait, let me clarify: the array is sorted in non-decreasing order. So for a given i (0-based or 1-based?), need to check the indices.

Wait, the problem says the input is a1, a2, ..., an. Then we sort the array. So the sorted array is a sorted list, let's say in 0-based indices.

Wait, in the code, after reading the input, we sort the array, and then work with 0-based indices. So for each i in 0-based from 0 to n-1:

But in the DP approach, the positions are in 1-based? Let me think again.

Let me reindex everything as 0-based. So after sorting, the array is a[0..n-1], sorted.

The DP[i] represents the first (i+1) elements (from 0 to i) can be partitioned into valid groups.

So dp[0] is for the first 0 elements (empty set), which is True.

But the problem says, each pencil must be in exactly one box. So for the full solution, we need dp[n-1] to be True. Wait, no. Wait, if the array is 0-based sorted, then for the full n elements, the index is n-1. Wait, perhaps the DP is 1-based. Let's clarify.

Hmm, perhaps it's easier to model the DP as follows:

The sorted array is a[0], a[1], ..., a[n-1].

We want to process these in order. For each position i (0-based), the maximum index up to i, can we partition the first i+1 elements (0..i) into valid groups.

So the DP array is size n+1, where dp[i] is True if the first i elements (0..i-1) can be partitioned.

So for example, dp[0] is True (no elements). dp[n] is True if all n elements can be partitioned.

So for i from 1 to n:

   if i <k: dp[i] is False (since each group must have at least k elements, but there's i elements, which is less than k)
   else:

      find the leftmost j where a[i-1] - a[j] <=d. Because the current element is a[i-1] (since 0-based). The group must start at j and end at i-1. The size is (i-1 -j +1) = i -j. So to have size >=k, i-j >=k → j <= i -k.

Wait, j is the starting index (0-based) of the group. The group is j, j+1, ..., i-1. So the size is i-1 -j +1 = i -j. For this to be >=k: i-j >=k → j <= i -k.

So the group can start at j where j <= i -k. So the right_j is i -k.

So for the current i (the number of elements considered so far), the group can start at j, and the group must start at j (0-based) such that j <= i -k, and a[i-1] -a[j] <=d.

So the left_j is the first j where a[j] >= a[i-1] -d. Because the array is sorted, all j >= left_j will satisfy a[i-1] -a[j] <=d.

So the possible j's are in [left_j, i -k]. But j must be >=0 (since it's 0-based). So left_j can be found via bisect_left.

Wait, the sorted array is a[0..n-1]. So for i (the number of elements considered), the current last element is a[i-1].

So the group must start at j (0-based) such that j >=0, j <= i -k, and a[i-1] -a[j] <=d.

The minimal j for which a[i-1] -a[j] <=d is the first j where a[j] >= a[i-1] -d.

Wait, a[i-1] -a[j] <=d → a[j] >= a[i-1] -d. So the minimal j is the first j where a[j] >= a[i-1] -d.

So using bisect_left on the array for the value (a[i-1] -d) gives us left_j.

Then, the possible j's are from left_j to (i -k), inclusive.

But if left_j > (i -k), then no j is possible, so dp[i] is False.

Otherwise, we need to check if there exists a j in [left_j, i -k] such that dp[j] is True. Because dp[j] represents that the first j elements (0..j-1) are partitioned, and then the group j..i-1 is formed (from j to i-1, which is j elements up to i-1).

Wait, no. If j is the starting index of the group (0-based), then the group is j, j+1, ..., i-1. The number of elements is i-1 -j +1 = i -j. For this to be >=k, i-j >=k → j <= i -k.

The previous groups must have been partitioned up to j elements. Wait, dp[j] is True if the first j elements can be partitioned. So adding a group j..i-1 (i-j elements) would lead to dp[i] being True.

So for the current i, the j's are in [left_j, i -k], and for each j in that range, if dp[j] is True, then dp[i] is True.

So the problem becomes: for each i, check if there's any j in [left_j, i -k] where dp[j] is True.

So the interval in the dp array is [left_j, i -k], and we need to check if any of these positions are True.

This is where the segment tree comes in. The segment tree can answer range OR queries: is there any True in the interval [left_j, i -k]?

Wait, but the interval is from left_j to (i -k). So if left_j <= (i -k), then the query is over that range. If not, then no possible j.

So the steps are:

Sort the array.

Initialize dp[0] = True.

Build a segment tree that can answer range OR queries.

For each i from 1 to n:

   if i <k: dp[i] = False. So do not update the segment tree.

   else:

      current a[i-1] is the last element of the group.

      left_j = bisect.bisect_left(a, a[i-1] -d, 0, i)  # since we are considering j up to i-1 elements (the group is from j to i-1, which is part of the first i elements). So the j can be from 0 to i-1.

      right_j = i -k

      if left_j > right_j:

          continue (dp[i] remains False)

      else:

          # query the segment tree for [left_j, right_j]

          if segment_tree.query(left_j, right_j):

              dp[i] = True

              update the segment tree by setting position i to True.

So the segment tree is built over the dp array (0-based up to n), and each position i can be set to True once dp[i] is True. Then, for each i, the query is over the range [left_j, right_j].

Wait, no. Because in the DP step, dp[i] is True if any j in [left_j, right_j] has dp[j] True.

So the segment tree must track the dp array, and for each i >=k, we query the segment tree for the range [left_j, right_j].

But the segment tree is built on the dp array, which has indices 0 to n. For example, dp[0] is True (the first element), and the segment tree is initialized with all False except for position 0.

So for each i, during the iteration, after computing left_j and right_j, we check if the segment tree has any True in [left_j, right_j]. If yes, then dp[i] becomes True, and we update the segment tree by setting position i to True.

This approach would work.

Now, the code.

But implementing a segment tree in Python for 5e5 elements may be a bit slow, but perhaps manageable.

Alternatively, since the queries are for ranges [a, b], and we can process the elements in order, perhaps we can use a sliding window and a prefix maximum.

Another approach is to track the earliest and latest positions where dp[j] is True, but that might not work for arbitrary ranges.

Alternatively, using a Binary Indexed Tree (Fenwick Tree) for range OR queries. But BIT is not suitable for range OR queries, because OR is not invertible. For example, XOR is not, but OR is not. So it's tricky.

So a segment tree is the way to go.

Implementing a segment tree for range OR queries and point updates.

Each node in the segment tree will store the OR of its children. For a range query, the OR of the segment is computed. If any position in the range is True, the OR will be True.

The segment tree can be implemented as follows:

Each node covers a certain interval. For a query [a, b], we split the interval into the nodes that cover parts of [a, b], and compute the OR of their values.

The updates are point updates: setting a position to True. Once a position is set to True, it remains True (since once dp[j] is True, it stays True).

So the segment tree can be built with all False initially, and then we set positions to True as we process them.

Now, the code structure.

First, read the input n, k, d.

Then, read the array a, sort it.

If k ==0: but the constraints say 1 ≤k ≤n. So k is at least 1. So no need to handle that case.

Then, handle the case where d is 0. Well, the same code should handle it.

But wait, the problem says that each non-empty box must have at least k pencils. So for example, if k=1, then each box can have any number ≥1. So even if all pencils are the same, we can just have one box.

But let's proceed with the code.

After sorting the array, proceed to compute the DP.

Now, code steps:

Read n, k, d.

Read the array, sort it.

If k ==1: then the problem reduces to whether the entire array can be partitioned into groups of size ≥1. Which is possible, but wait, no. Because even though each group can be of size 1, but the condition is that each group must have all elements within d of each other. So for example, if the array is [1, 3, 5], d=1, and k=1. Then you need to put each element in separate boxes. But if the elements are 1,3,5, then |3-1|=2>1. So 1 and 3 can't be in same box. So each must be in their own box, which is allowed since k=1. So the answer is YES.

But this is allowed. So the code must handle all possibilities.

But back to the main code.

Initialize dp as a list of False of size n+1.

dp[0] = True.

Build the segment tree for the dp array. Initially, all False except index 0.

Then, for i from 1 to n:

   if i <k: continue (since group size must be at least k, and i is the number of elements. So for i <k, no way to split, so dp[i] = False. But since the initial dp array is all False, no need to do anything.)

   else:

      current element is a[i-1] (since a is 0-based, i is 1-based in the loop).

      left_j = bisect.bisect_left(a, a[i-1] -d, 0, i)

      right_j = i -k

      if left_j > right_j:

          continue

      else:

          query the segment tree for the range [left_j, right_j]

          if the query returns True:

              dp[i] = True

              update the segment tree at position i to True.

So, the code will look like:

But how to implement the segment tree?

Alternatively, we can use a binary indexed tree (Fenwick Tree) approach, but as mentioned earlier, it's not straightforward for range OR queries. So the segment tree is the way to go.

In Python, implementing a segment tree for 5e5 elements.

But for n up to 5e5, the segment tree will have O(4*5e5) nodes. Which is manageable.

Now, let's code this.

But first, let's think about the possible edge cases.

Test case 1:

n=6, k=3, d=10.

The array is [2,2,4,7,7,7] after sorting.

So for i=6 (n=6), the current element is 7.

left_j is the first index where a[j] >=7-10= -3. So all elements are >=-3. So left_j=0.

right_j =6-3=3.

So j ranges from 0 to3. The group from j to 5 (since i=6 elements, 0-based index 5) is j=0: elements 0-5 (size 6, which is >=3), and 7-2=5 <=10. So if there's any j in 0..3 where dp[j] is True.

dp[j] is True if the first j elements can be partitioned. So j=0: dp[0] is True. So the query returns True. So dp[6] is True. So the answer is YES.

Test case 3:

n=3, k=2, d=5.

array after sorting: [10,16,22]. So for i=3 (n=3):

left_j is the first j where a[j] >=22-5=17. The array is [10,16,22]. 17 is between 16 and 22. So left_j=2. right_j=3-2=1. left_j=2>1. So no j. So dp[3] is False. So answer is NO.

So the code should handle these cases.

Now, implementing the segment tree.

The segment tree can be represented as a list, with 1-based indexing. Each node represents an interval. For each node, the left and right child can be computed. The size of the segment tree is 2^ceil(log2(m)), where m is the number of elements. But for code simplicity, perhaps using a class-based segment tree.

Alternatively, here's an implementation of a segment tree for range OR and point updates.

The segment tree will have the following operations:

- __init__(size): initializes a segment tree of given size (n+1 elements, since dp is from 0 to n)
- update(pos): sets the value at pos to True
- query(l, r): returns True if any element in [l, r] is True

Implementing this:

The segment tree can be built as follows.

Each node stores whether the segment has any True. Initially, all are False except position 0, which is True.

But in the code, after creating the segment tree, we need to update the position 0 to True.

So in the code:

After initializing the segment tree with all False, we call update(0, True).

But in Python, building the segment tree can be done with a list. Here's a possible implementation.

But perhaps a more efficient way is to use a class.

Let me sketch the code.

class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.size = 1
        while self.size < self.n:
            self.size <<=1
        self.tree = [False]*(2*self.size)
    
    def update(self, pos, value):
        # set tree[pos] to value (True)
        pos += self.size
        if self.tree[pos] != value:
            self.tree[pos] = value
            while pos >1:
                pos >>=1
                new_val = self.tree[2*pos] or self.tree[2*pos+1]
                if self.tree[pos] == new_val:
                    break
                self.tree[pos] = new_val
    
    def query_range(self, l, r):
        # query [l, r] inclusive
        res = False
        l += self.size
        r += self.size
        while l <=r:
            if l%2 ==1:
                res = res or self.tree[l]
                l +=1
            if r%2 ==0:
                res = res or self.tree[r]
                r -=1
            l >>=1
            r >>=1
        return res

Wait, but this is a standard iterative segment tree implementation. However, the initial setup may be a bit tricky. Also, the positions in the segment tree are 0-based. So when we create the segment tree with size (n+1), because the dp has indices from 0 to n (inclusive), the segment tree must be initialized to handle these indices.

But in the code, when we initialize the segment tree with size (n+1), the size variable in the class is the next power of two greater than or equal to (n+1). Then, each position in the original array (0 to n) is mapped to the segment tree's leaves starting from self.size to self.size + (n+1) -1. The rest of the leaves (if any) are set to False.

But in the code, when we update a position, we first check if it's within the original size. So the code for the segment tree should be okay.

But let's test with a small example.

Suppose n=6 (max i is 6), so size is 8. Then the leaves are positions 8 to 14 (since 8+6=14?), but wait, for size=8, the leaves are 8 to 15. So for n=6, the positions 0-6 (7 positions) are mapped to 8-14.

But the code uses pos += self.size. So for a position up to n, it's correct.

But I think the code for the segment tree as written may have issues. For example, if the size of the segment tree is not sufficient to cover all positions up to (n), then the code may fail. But perhaps in the code, the segment tree is constructed with size 1 << ceil(log2(m)), where m is the initial size.

But perhaps the code should work.

Alternatively, here's an alternative approach to the segment tree.

But given time constraints, perhaps proceed with this code.

In the problem, the maximum possible n is 5e5. So the segment tree for n+1 elements (5e5+1) would require a tree of size up to 1e6 (since 5e5+1 is 500001, which is less than 2^19=524288, so the tree size would be 2^19=524288, and the total number of nodes is 2^20 = 1,048,576. Which is manageable.

Now, the code steps.

Read n, k, d.

Read the array a, sort it.

If k >n: then it's impossible, since each box has at least k pencils, but there are n pencils. So if k> n, then output NO. But according to the input constraints, k<=n. So no need to handle this.

Initialize the segment tree with size (n+1), since the dp array is 0..n.

Then, set dp[0] to True. So the segment tree's initial state is all False except for position 0.

Then, for each i in 1 to n:

   if i <k: continue (can't form a group of size >=k, so dp[i] remains False)

   else:

      current element is a[i-1]

      left_j = bisect.bisect_left(a, a[i-1] -d, 0, i)  # since in the first i elements (0..i-1), the group is j..i-1, which is part of the first i elements. So j can be 0 to i-1.

      right_j = i -k

      if left_j > right_j: continue

      else:

          # check if there's any j in [left_j, right_j] where dp[j] is True.

          # in the segment tree, query [left_j, right_j]

          if st.query_range(left_j, right_j):

              dp[i] = True

              st.update(i, True)

At the end, output "YES" if dp[n] is True else "NO".

Wait, but the code is for the dp array, where dp[i] represents the first i elements can be partitioned. So after processing all elements, the answer is dp[n].

So the code should check if dp[n] is True.

But in the code, for i from 1 to n:

   process i, and if possible, set dp[i] to True.

So for i= n, if possible, then the answer is YES.

Thus, in the code, after processing all i's, check if dp[n] is True.

Now, the code:

But let's test this.

Test case 1:

n=6, k=3, d=10.

a after sorting: [2,2,4,7,7,7]

i ranges from 1 to 6.

For i=3 (the third element in the array? No, wait, i is the number of elements. So for i=3, the first 3 elements are [2,2,4]. Then, we can check if a group of 3 elements can be formed (since i=3 >=k=3).

But wait, for i=3, right_j =3-3=0. So j can be at most 0.

left_j is the first j where a[j] >=a[2] -d → a[2] is 4. 4-10= -6. So left_j=0.

So j ranges from 0 to 0. Check if any of the j in 0 has dp[j] = True.

dp[0] is True. So the query is [0,0], which returns True. So dp[3] is set to True.

Similarly, when i=6, the right_j is 6-3=3. The left_j is the first j where a[j] >=7-10= -3 → j=0.

So query [0,3]. The dp[j] for j in 0-3. For example, j=0: True. j=3: dp[3] is True.

Thus, the query returns True, so dp[6] is set to True. So output is YES.

Thus, the code would work.

Now, code.

But in Python, the bisect module's bisect_left function is used.

So code:

Testing against sample input 1.

```python
import bisect


class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.size_tree = 1
        while self.size_tree < self.n:
            self.size_tree <<=1
        self.tree = [False]*(2 * self.size_tree)
    
    def update(self, pos, value):
        # Update the position to True (value is True)
        pos += self.size_tree
        if self.tree[pos] != value:
            self.tree[pos] = value
            pos >>=1
            while pos >=1:
                new_val = self.tree[2*pos] or self.tree[2*pos +1]
                if self.tree[pos] == new_val:
                    break
                self.tree[pos] = new_val
                pos >>=1
    
    def query(self, l, r):
        # Query [l, r] (inclusive)
        res = False
        l += self.size_tree
        r += self.size_tree
        while l <= r:
            if l %2 ==1:
                res = res or self.tree[l]
                l +=1
            if r %2 ==0:
                res = res or self.tree[r]
                r -=1
            l >>=1
            r >>=1
            if res:
                return True
        return res

def main(input_stream, output_stream):
    import sys
    input = input_stream.read().split()
    ptr =0
    n = int(input[ptr])
    ptr +=1
    k = int(input[ptr])
    ptr +=1
    d = int(input[ptr])
    ptr +=1
    a = list(map(int, input[ptr:ptr+n]))
    a.sort()
    if k ==0:
        print("YES", file=output_stream)
        return
    st = SegmentTree(n+1)
    st.update(0, True)
    for i in range(1, n+1):
        if i <k:
            continue
        current = a[i-1]
        left_j = bisect.bisect_left(a, current -d, 0, i)
        right_j = i -k
        if left_j > right_j:
            continue
        if st.query(left_j, right_j):
            st.update(i, True)
    if st.query(n, n):
        print("YES", file=output_stream)
    else:
        print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 2 3
4 5 3 13 4 10
""",
            "output": \
"""\
YES
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


class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.size_tree = 1
        while self.size_tree < self.n:
            self.size_tree <<=1
        self.tree = [False]*(2 * self.size_tree)
    
    def update(self, pos, value):
        # Update the position to True (value is True)
        pos += self.size_tree
        if self.tree[pos] != value:
            self.tree[pos] = value
            pos >>=1
            while pos >=1:
                new_val = self.tree[2*pos] or self.tree[2*pos +1]
                if self.tree[pos] == new_val:
                    break
                self.tree[pos] = new_val
                pos >>=1
    
    def query(self, l, r):
        # Query [l, r] (inclusive)
        res = False
        l += self.size_tree
        r += self.size_tree
        while l <= r:
            if l %2 ==1:
                res = res or self.tree[l]
                l +=1
            if r %2 ==0:
                res = res or self.tree[r]
                r -=1
            l >>=1
            r >>=1
            if res:
                return True
        return res

def main(input_stream, output_stream):
    import sys
    input = input_stream.read().split()
    ptr =0
    n = int(input[ptr])
    ptr +=1
    k = int(input[ptr])
    ptr +=1
    d = int(input[ptr])
    ptr +=1
    a = list(map(int, input[ptr:ptr+n]))
    a.sort()
    if k ==0:
        print("YES", file=output_stream)
        return
    st = SegmentTree(n+1)
    st.update(0, True)
    for i in range(1, n+1):
        if i <k:
            continue
        current = a[i-1]
        left_j = bisect.bisect_left(a, current -d, 0, i)
        right_j = i -k
        if left_j > right_j:
            continue
        if st.query(left_j, right_j):
            st.update(i, True)
    if st.query(n, n):
        print("YES", file=output_stream)
    else:
        print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 2 5
10 16 22
""",
            "output": \
"""\
NO
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

</think>

```python
import bisect

class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.size_tree = 1
        while self.size_tree < self.n:
            self.size_tree <<= 1
        self.tree = [False] * (2 * self.size_tree)
    
    def update(self, pos, value):
        pos += self.size_tree
        if self.tree[pos] != value:
            self.tree[pos] = value
            pos >>= 1
            while pos >= 1:
                new_val = self.tree[2*pos] or self.tree[2*pos + 1]
                if self.tree[pos] == new_val:
                    break
                self.tree[pos] = new_val
                pos >>= 1
    
    def query(self, l, r):
        res = False
        l += self.size_tree
        r += self.size_tree
        while l <= r:
            if l % 2 == 1:
                res |= self.tree[l]
                l += 1
            if r % 2 == 0:
                res |= self.tree[r]
                r -= 1
            l >>= 1
            r >>= 1
            if res:
                return True
        return res

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    k = int(input[ptr])
    ptr += 1
    d = int(input[ptr])
    ptr += 1
    a = list(map(int, input[ptr:ptr+n]))
    a.sort()
    st = SegmentTree(n + 1)
    st.update(0, True)
    for i in range(1, n + 1):
        if i < k:
            continue
        current = a[i-1]
        left_j = bisect.bisect_left(a, current - d, 0, i)
        right_j = i - k
        if left_j > right_j:
            continue
        if st.query(left_j, right_j):
            st.update(i, True)
    print("YES" if st.query(n, n) else "NO")

if __name__ == "__main__":
    main()
```
