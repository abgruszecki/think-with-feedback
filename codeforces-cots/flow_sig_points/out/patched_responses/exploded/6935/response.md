<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

The task is to determine if a certain graph constructed from given segments is a tree. A tree is a connected acyclic graph. So the graph must satisfy two conditions: it's connected and has exactly n-1 edges (since a tree with n nodes has n-1 edges and is connected).

The graph is formed by connecting two vertices (segments) with an edge if their segments intersect but neither is fully contained within the other. So, two segments [a, b] and [c, d] must satisfy that they intersect (so their intervals overlap), but neither a < c and d < b nor c < a and b < d. Wait, no. Wait, for the first condition, the segments must intersect, so their intervals overlap. Then, for the edge to exist, neither can contain the other. So the condition is: (a < c < b < d) OR (c < a < d < b) OR (they cross in some way that one starts before the other and ends after the other's start but before the other's end. Wait, maybe the correct way to check is that they overlap, but neither is a subset of the other. So the segments [l1, r1] and [l2, r2] must satisfy (l1 < l2 < r1 < r2) or (l2 < l1 < r2 < r1) or (l1 < l2 < r2 < r1) is not allowed, but l1 < l2 < r1 < r2 is allowed. Wait, no. Let me think again.

The edge exists if the two segments intersect (i.e., their intervals overlap) and neither is entirely contained within the other. So, for example, if one segment is [1,5], another is [2,3], they do not form an edge because the second is contained in the first. But if the segments are [1,4] and [3,5], then they do form an edge. So the conditions are:

They overlap (so their intervals have a non-empty intersection), and neither is contained in the other.

So for two segments A and B, the intersection is non-empty, and not (A is contained in B) and not (B is contained in A).

So first, how do I compute for all pairs of segments whether they are connected by an edge. But with n up to 5e5, checking all pairs is impossible. That's O(n^2) which is way too slow.

So we need a way to find all pairs of segments that intersect but are not contained in each other, efficiently.

So the problem reduces to:

1. Check if the number of such edges is exactly n-1.
2. Check if the graph is connected.
But both conditions need to be satisfied.

But how can we compute the number of edges and the connectedness efficiently?

Hmm. Let's think about the properties of the graph. If the graph is a tree, then the number of edges must be exactly n-1. So first, we can check the number of edges. If it's not n-1, we can immediately return NO. Then, check if the graph is connected. But even this seems difficult for large n.

Alternatively, perhaps there's a way to model this problem in terms of the arrangement of the segments. Let's think about the segments and how they are arranged.

Wait, the problem says that all endpoints are distinct. So all 2n endpoints are unique. That's an important detail. So each segment is defined by two distinct integers, and no two segments share an endpoint. So for example, there's no segment that starts where another ends.

Hmm. Let's think of the segments sorted by their left endpoints. Since all left and right are unique, each segment can be sorted in a unique order.

Another observation: the problem is similar to interval graphs, where edges are between overlapping intervals. But here, the edges are between intervals that overlap but are not contained. So the graph is a subset of the interval graph's edges.

But how can we model this efficiently?

First, let's think about the structure of the graph. Let's suppose that the segments are arranged in a way that forms a tree. For example, in the first sample input, the edges form a tree. So perhaps the segments form a structure where each new segment connects to exactly one previous segment, leading to a tree.

Alternatively, maybe the graph can be represented as a tree if the segments form a certain hierarchy.

Wait, maybe the graph is a tree if and only if the segments form a certain structure where the overlapping is such that each segment (except the root) has exactly one parent that it overlaps with and is not contained within. But how to model this.

Alternatively, perhaps the graph's structure can be represented using a union-find (disjoint set) data structure. But again, how to process the edges efficiently.

But the key problem is to find all pairs of segments that overlap but neither contains the other.

Let me think about how to compute the number of edges. For each segment, how many other segments does it overlap with and are not contained.

The total number of edges is the sum over all segments of the number of such overlaps, divided by two (since each edge is counted twice).

So the approach is: compute the total number of edges, check if it's exactly n-1, and then check if the graph is connected.

But how to compute this for large n.

Alternative approach: think of the problem as building a graph where edges are between segments that cross each other (overlap but not contain). Then, the graph is a tree only if it's connected and has exactly n-1 edges.

But with n up to 5e5, we need an O(n log n) approach.

Hmm. Let's think about the arrangement of the segments.

Since all endpoints are unique and are 2n in total, perhaps they can be sorted in a particular order.

Let's sort all segments by their left endpoint. Then, for each segment, we can process them in order and determine overlapping segments that are not contained.

Wait, but even after sorting by left, how do I find which segments overlap but are not contained.

Let me think. Suppose I have a segment S with left = L and right = R. All segments that start after L but before R may overlap with S.

But some of them may end before R (so they are contained in S) or after R (so they are not contained).

Wait, for another segment T with left = L', right = R':

S and T overlap if L < L' < R and R' > L (since L' > L because S is sorted by L, so T's left is after S's left. So T's left is between L and R. For overlap, T's right must be > L (which it is, since L' < R and T's right is > L', which is > L). So if T's left is between L and R, then S and T overlap if T's right is > L (which is always true, since T's right is > L' (since L' < R and T's right is > L'). So the overlapping condition between S and T (when S is sorted before T) is L < L' < R. Then, the condition that T is not contained in S is R' > R. Because if R' is <= R, then T is contained in S. Conversely, S is contained in T if L' < L and R' > R, but since the segments are sorted by L, S is before T, so L' >= L. So S can't be contained in T. So, for S (earlier segments) and T (later segments), T can be contained in S if R' <= R. Otherwise, if R' > R, then T is not contained in S, so they form an edge.

So for each segment S (sorted by L), all segments T that have L' in (L, R) and R' > R will form an edge with S.

So, the problem reduces to, for each segment S, how many segments T have L' between L and R, and R' > R.

But how to compute this efficiently.

Wait, but this approach could miss some edges. For example, suppose a segment T comes before S in the sorted order. Because when we process S, we might not check the previous segments. But in that case, since the segments are sorted by L, S has L larger than T's L. So T's L is less than S's L. So when processing T (earlier), if S's L is in (T's L, T's R), then during T's processing, S's L would be in that interval, and if S's R > T's R, then S and T would form an edge. But since S comes after T in the sorted order, when processing T, S's L may not be considered. Wait, no. Because when processing T, we look at all segments that come after T (since sorted by L), which have L' >= T's L. But if S is after T, then S's L is >= T's L. So during T's processing, S's L is >= T's L. But for T and S to overlap, S's L must be < T's R. So during processing T, we can look for all segments S where L is in (T's L, T's R), and R > T's R. So each such pair (T, S) would form an edge.

But processing each segment and checking all subsequent segments is O(n^2), which is not feasible.

So we need a way to find, for each segment, the number of other segments that start after its L, start before its R, and have R larger than its R.

Alternatively, for each segment S (sorted by L), the number of segments T where L' is in (S.L, S.R) and R' > S.R.

But how to compute this efficiently.

If the segments are sorted by their left endpoints, then for each S, the segments T that have L' in (S.L, S.R) are the ones that come after S in the sorted list (since they have L' > S.L). Among those, which have R' > S.R.

So for each S, in the sorted list, the interval (S.L, S.R) for L' is S's L < T's L < S's R. And among those, count the number of T where T's R > S's R.

But how to find these segments quickly.

Since the segments are sorted by L, for a given S, all T's L' are >= S's L. So the segments T that satisfy L' > S.L and L' < S.R are the ones in the range [i+1, j-1], where i is the position of S in the sorted array, and j is the first segment where L' >= S.R.

So for S's position i in the sorted array, the segments T that start between S.L and S.R are those from i+1 up to the first segment with L >= S.R. Let's call this upper bound as k. So the segments in the range [i+1, k-1].

Now, among these segments, how many have R' > S.R?

If we can, for each S, find the number of T in [i+1, k-1] with R' > S.R, that's the number of edges contributed by S.

Summing all these for all S and dividing by 2 (since each edge is counted twice) would give the total number of edges.

Wait, no. Because for each S, the edges are the T that are after S (in sorted order) and meet the conditions. So each edge is counted once. Because S and T are in the sorted list, S comes before T. So when processing S, we count T, but when processing T, we are not considering S again (since T comes after S). So the total edges would be the sum over all S of the number of T's that meet the conditions. Then, the sum would be the total number of edges.

Wait no. Because each edge (S, T) where S is before T in the sorted list is only considered once when processing S. So the total number of edges is the sum for each S of the count of T's that satisfy the condition. So no division by two is needed. So, that's correct.

So the total edges are the sum of the counts for each S.

So the problem now is to compute this sum and see if it's exactly n-1, and then check if the graph is connected. But even computing the sum is a problem.

So first, for each S, find the segments T that start after S starts (L' > S.L), start before S ends (L' < S.R), and end after S ends (R' > S.R).

How can we compute this efficiently?

Let's sort the segments by their L.

Once sorted, for each S in the sorted list, the segments that start after S.L and before S.R are the ones in the range [i+1, k-1], where i is the index of S in the sorted list, and k is the first index where L' >= S.R.

So we can find k using binary search.

Then, among these segments in [i+1, k-1], how many have R' > S.R?

To compute this, we can pre-process the segments sorted by L, and for each position, keep a structure that allows us to query, in a range [a, b], how many segments have R' > x, where x is S.R.

A possible data structure for this is a binary indexed tree (Fenwick tree) or a segment tree that can answer range count queries for R' > x.

But since the segments are sorted by L, their R's can be in any order. However, for the segments in the range [i+1, k-1], which are sorted by L, their R's are not necessarily sorted. So a binary indexed tree approach may not directly work.

Alternative approach: for each segment, after sorting them by L, we can also process their R values. For each S, after finding the range [i+1, k-1], we need to count how many R's in that range are greater than S.R.

So, we can pre-process a structure that allows us to perform range maximum queries (RMQ) or some other form of query.

Wait, but a count of R's > S.R in a range can be done with a prefix array sorted by R. But since the segments are not sorted by R, perhaps we need a structure like a segment tree where each node stores a sorted list of R's. Then, for a given range [a, b], we can collect all R's in that range, sort them, and then perform a binary search for S.R to count how many are larger. But building such a structure would take O(n log n) time and O(n) space. For each query, the time is O(log n) per query (since the range can be decomposed into O(log n) nodes, each of which is a sorted list, and for each list, we perform a binary search to find the count).

This approach would be feasible for n up to 5e5. Let's see:

- Preprocessing: building a segment tree where each node has a sorted list of R's. Since each element is in O(log n) nodes, the total time is O(n log n).

- For each query (range [a, b], x=S.R), the query time is O(log^2 n), since for each of the O(log n) nodes covering the range, we perform a binary search in O(log n) time. So for 5e5 segments, 5e5 * log^2 n is about 5e5 * (20)^2 = 2e7 operations, which is manageable.

So this is a viable approach.

So here's the plan:

1. Sort all segments by their left endpoints (L) in increasing order.

2. Build a segment tree where each node in the segment tree represents an interval of the sorted list, and stores the sorted list of R's in that interval.

3. For each segment S (at index i in the sorted list):

   a. Find k, the first index in the sorted list where L' >= S.R. Since the list is sorted by L, this can be done using binary search (bisect_left on the list of L's).

   b. The range of possible T's is from i+1 to k-1.

   c. If i+1 > k-1, then there are no such T's. Continue.

   d. Otherwise, query the segment tree for the range [i+1, k-1] to find how many R's in that range are > S.R. This count is the number of edges contributed by S.

4. Sum all these counts. If the sum is not equal to n-1, output "NO".

5. Else, check if the graph is connected. But how?

Wait, even if the sum is n-1, the graph may not be connected. For example, imagine three nodes forming a cycle with two edges, but this is impossible because a tree has exactly n-1 edges. So in this case, if the sum is n-1, the graph could be a tree (connected and acyclic) or a collection of cycles and trees with exactly n-1 edges (but that's impossible because such a graph would have at least one cycle and thus the number of edges would be >= n). So the sum being n-1 implies that the graph is a tree if and only if it is connected.

So after checking the sum is n-1, we need to check connectedness.

But how to check connectedness efficiently.

The problem is that the graph has up to 5e5 nodes and 5e5 edges. So a BFS or DFS would take O(n) time, which is acceptable. But how to build the adjacency list.

But building the adjacency list is O(E) time and space, which for E up to 5e5 is manageable. But in the worst case (like when all segments are connected to each other), E could be up to O(n^2), which is impossible.

Wait, no. Because the sum of counts is n-1 (since we checked that), so the total number of edges is exactly n-1. So the graph is a tree if and only if it's connected. So once the sum is n-1, the graph is a tree if it's connected. But how to check connectivity without building the adjacency list.

But building an adjacency list for a tree is manageable. Since each node has edges to some others, but the total edges are n-1. So the adjacency list would be O(n) in size.

But how to construct the adjacency list given that the edges are determined by the conditions above.

But that's the problem. We can't store all the edges, since even n is 5e5, and each edge is stored twice (if we build an adjacency list as a list of lists). But for n=5e5, n-1 edges is manageable.

So here's the approach:

Once we confirm that the number of edges is exactly n-1, we need to check if the graph is connected. To do this, we can build a union-find (disjoint set) data structure, and for each edge, perform a union operation. Then, check if all nodes are in the same set.

But how to iterate over all edges in O(n) time.

Wait, but how to generate all edges. The edges are determined by the pairs (S, T) where S is before T in the sorted list, T is in the range [i+1, k-1] of S, and T's R > S's R.

But how to generate these pairs without storing them, which would take O(n) space (since n-1 edges).

So during the first step (counting the edges), once we confirm that the sum is n-1, we can proceed to collect all edges, then build the adjacency list, and perform BFS/DFS to check connectivity.

But the problem is that for n=5e5, even storing the edges as pairs would require O(n) space, which is feasible. But how to collect all the edges.

Alternatively, during the first step, instead of just counting the edges, we can collect them. But this would require O(n) additional time and space.

But how to collect the edges.

Wait, during the first step, for each S, we can find all T's in the range [i+1, k-1] where R' > S.R, and for each such T, record the edge (S, T). But this is time-consuming, because for each S, we need to find all such T's in the range and collect them.

But how to collect them efficiently. For that, the same approach as before can be used. For each S, after finding the range [i+1, k-1], we can query the segment tree to collect all T's in that range with R' > S.R. But this would be O(log n) per T, which for O(n) edges would be O(n log n) time.

But for n=5e5, that's manageable.

Alternatively, for each S, once we have the count, we can also collect the T's. But how.

Wait, the segment tree can be modified to return not just the count but the actual indices. For example, for each node in the segment tree, when the query is to count R's > x in a range, we can also collect the indices. But this would be very time-consuming, as it would involve traversing all the leaves in the range and checking each R. For each query, this could take O(k) time, where k is the number of elements in the range. For large ranges, this is O(n) time per query, leading to O(n^2) time overall.

This is not feasible.

Alternative approach: since during the first step (counting the edges) we have already processed each S and found the range [i+1, k-1], and the number of T's in that range with R' > S.R is known, perhaps we can use this to generate the edges in a way that allows building the adjacency list.

But how? Because the count is the number of edges for each S, but we need to know which specific T's are connected.

This seems challenging. Perhaps there's another way to model the graph's structure.

Alternative idea: since the graph is a tree if and only if the number of edges is exactly n-1 and the graph is connected. But how can we check connectivity without building the adjacency list.

Wait, in the scenario where the graph is a tree, the union-find data structure can be used. For each edge, we add it to the union-find structure. After all edges are processed, check if all elements are in the same set.

But again, the problem is generating the edges.

So, perhaps during the first pass, after verifying that the sum is n-1, we can generate all edges and then perform the union-find.

But generating the edges is the issue.

Alternative approach:

For the first part (counting the edges), we can use the same approach as before, but during the same pass, collect all edges. However, this may be possible by, for each S, finding the T's in [i+1, k-1] with R' > S.R, and for each such T, add an edge between S and T. But how to do this efficiently.

Wait, but for each S, the T's in [i+1, k-1] with R' > S.R can be found by querying the segment tree for the count, and then querying again to collect their indices. But that would require O(n) time per query in the worst case.

Alternatively, perhaps the segments in the range [i+1, k-1] can be sorted by R. Then, for each S, we can find the first index in that range where R' > S.R, and all T's from that index onward would be part of the edges. But since the segments in the range are sorted by L, their R's are not necessarily sorted.

Alternatively, we can pre-sort the segments in each node of the segment tree by R. So in the segment tree, each node's list of R's is sorted. Then, for a query range [a, b], x, we can traverse the segment tree nodes covering [a, b], and for each node's sorted list of R's, perform a binary search to find how many are greater than x. Summing across all nodes gives the count.

But how to collect the actual indices of the T's that meet the criteria.

This seems challenging. Maybe this is possible by modifying the segment tree to store not just the R's sorted, but their indices. For example, each node in the segment tree stores a list of tuples (R, index), sorted by R. Then, during a query, we can traverse the segment tree nodes, and for each node's sorted list, find all elements where R > x, and collect their indices.

But this would require storing the indices along with R in the segment tree's nodes.

But this would allow us to collect all the T's indices in O(log n + m) time per query, where m is the number of elements in the result. For each query, the number of elements is exactly the count we computed earlier. Since the sum of counts is n-1, the total time to collect all edges would be O(n log n + (n-1)), which is acceptable.

So here's the plan:

1. Sort all segments by L. Let's call this list sorted_segments. Each entry is (L, R, index).

2. Extract the L's of the sorted_segments into a separate list to facilitate binary search for k.

3. Build a segment tree where each node represents an interval of the sorted_segments. Each node's data is a list of (R, index) pairs sorted by R.

4. For the count phase:

   a. For each S in sorted_segments (at index i):

      i. Find k using binary search on the L's list to find the first index where L >= S.R.

      ii. The possible T's are in the range [i+1, k-1].

      iii. Query the segment tree for the number of elements in [i+1, k-1] with R > S.R. Add this to the total edge count.

5. If total edges != n-1, output "NO".

6. Else, collect all edges:

   a. For each S in sorted_segments (at index i):

      i. Find k again.

      ii. Query the segment tree for the elements in [i+1, k-1] with R > S.R. Collect their indices.

      iii. For each such T's index, add an edge between S's index and T's index.

7. Once all edges are collected, perform a BFS or DFS to check if the graph is connected.

But collecting the edges would take O(n log n + m) time, where m is the number of edges (n-1). For each query, we need to collect the indices of the T's. This can be done by modifying the segment tree's query function to collect the indices where R > x.

Implementing this in Python could be challenging due to time constraints, but let's proceed.

Now, let's think about the implementation steps.

First, sorting the segments by L. Then, building a segment tree where each node has a sorted list of R's.

Implementing the segment tree:

The segment tree can be represented as a list of lists. For each node covering a range [start, end], the node's data is a sorted list of R's in that range. To build the segment tree, we recursively split the array into left and right children, and each node's data is the sorted merge of its children's R lists. However, this is not efficient for large n. Wait, no. For n up to 5e5, the segment tree would be O(n log n) in space, which might be manageable. But in practice, Python may have memory issues.

Alternatively, we can use a bottom-up approach. For a segment tree with leaves being individual elements, and each internal node combines the ranges of its children and sorts their R's.

But building such a segment tree would take O(n log n) time and space.

Once the segment tree is built, each query for a range [a, b] would decompose the range into O(log n) nodes, and for each node's sorted R list, perform a binary search to find how many elements are greater than x. Summing these gives the count.

For collecting the edges, the same approach is used, but instead of counting, we collect the indices. For each node in the decomposed query range, we perform a binary search to find the starting index in the node's sorted R list where R > x. Then, all elements from that index to the end of the list are part of the result, and their indices are added to the result list.

Now, let's proceed to the code.

But first, we need to handle the indices. Each segment in the sorted list has an original index (0-based), which is needed to build the adjacency list.

Wait, the original indices are necessary because the edges are between the original segments. For example, the adjacency list should contain the original indices, not the sorted indices.

But in the sorted list, each segment has its original index. So during the collection phase, for each S (with original index s_idx), and each T (with original index t_idx), we add an edge between s_idx and t_idx.

So the segments are sorted by L, and for each S in the sorted list, we find all T's in the range [i+1, k-1] with R' > S.R, and collect their original indices.

Now, let's think about the code steps.

Implementing the segment tree for R's:

But building a segment tree for range queries of R's is going to be time-consuming. Let's see.

An alternative approach is to pre-process for each segment's R, and for the sorted list, build a binary indexed tree (Fenwick tree) that can handle range queries for R's.

But how?

Another idea: since the segments are sorted by L, but their R's are not sorted. So for the segments sorted by L, their R's can be in any order. So, for the range [i+1, k-1], the segments in this range are sorted by L (since the entire list is sorted by L), but R's are not sorted. So to count the number of R's > x in this range, we need a data structure that can answer this query.

The segment tree approach is suitable here. Each node of the segment tree stores a sorted list of R's in its range. For example, for the entire array, the root node stores a sorted list of all R's. The left child stores the sorted R's of the first half, and so on. When querying a range, we break it down into O(log n) nodes, and for each node's sorted list, perform a binary search to count how many R's are greater than x. The sum of these counts is the total.

Building such a segment tree is O(n log n) time and space. Each query is O(log^2 n) time (log n nodes, each with a binary search taking log n time).

In Python, this is feasible for n up to 5e5.

So let's proceed to code this.

But first, the steps:

1. Read n.

2. Read n segments as (L, R), along with their original indices.

3. Sort the segments by L in increasing order.

4. Extract the sorted L's into a separate list for binary searching.

5. Build the segment tree for the sorted list's R's. Each node stores a sorted list of R's in its interval.

6. For each segment S in the sorted list (index i), find k (the first index where L >= S.R). This can be found using bisect.bisect_left on the sorted L's list.

7. The range for T's is [i+1, k-1]. If this range is invalid (i+1 > k-1), skip.

8. Query the segment tree for the count of R's > S.R in this range. Add this to the total edge count.

9. After processing all segments, if the total edge count is not n-1, output "NO".

10. Else, collect all edges. For each S in sorted list, query the segment tree for the T's in [i+1, k-1] with R > S.R, collect their original indices, and add edges between S's original index and T's original index.

11. Build an adjacency list using these edges.

12. Check if the graph is connected using BFS or DFS.

13. If connected, output "YES", else "NO".

But collecting all edges (step 10) is time-consuming. However, since the total edges are n-1, it's manageable.

Now, implementing the segment tree.

But in Python, a recursive segment tree may hit recursion depth limits for large n. So an iterative approach or a bottom-up approach may be better. However, implementing a segment tree with each node's data as a sorted list can be done with a list of lists.

Alternatively, here's a way to build the segment tree:

- The segment tree is represented as a list of lists. The tree is built in a bottom-up manner. Each leaf node is a single element. Each internal node is formed by merging its children's sorted lists.

For example, for n=5, the tree would have leaf nodes at positions 4, 5, 6, 7, 8 (assuming a 1-based array). Each internal node (e.g., 2) would merge its children (4 and 5) and store the sorted list of R's.

Implementing this requires first building the leaves and then building the parents up to the root.

But for n up to 5e5, the size of the segment tree would be O(2n), but each node's list would take O(k) space, where k is the number of elements in the node's range. The total space would be O(n log n), which may be acceptable.

But in Python, for 5e5 elements, this may require a lot of memory. For example, each leaf node has a list of length 1 (the R of the segment). The next level up has nodes with lists of length 2, etc. The total memory would be O(n log n), which for n=5e5 is 5e5 * 20 ≈ 1e7, which is manageable.

So let's proceed.

Building the segment tree:

First, the sorted list of segments is sorted by L. Then, the R's are stored in a list. The segment tree is built on this list.

The code for building the segment tree:

def build_segment_tree(data):
    n = len(data)
    size = 1
    while size < n:
        size <<= 1
    tree = [[] for _ in range(2*size)]
    for i in range(n):
        tree[size + i] = [data[i]]
    for i in range(size-1, 0, -1):
        tree[i] = merge(tree[2*i], tree[2*i+1])
    return tree

But merging two sorted lists can be done efficiently. However, for Python, this would take O(k) time for each merge, where k is the total number of elements in the two children. For a bottom-up approach, each level requires merging O(n) elements. The total time to build the tree is O(n log n).

But for n=5e5, this could be time-consuming. Alternative approaches using sorted lists may not be feasible. However, for the problem's time constraints (2 seconds), it's possible.

Alternatively, we can use a different approach. For example, each time we need to process a query, we can iterate through the segments in the query range and check their R's. But this is O(n) per query in the worst case, which is not feasible.

Thus, the segment tree approach seems necessary.

But in Python, for n=5e5, building such a segment tree may be slow. Let's think of alternatives.

Another approach is to precompute a list of R's for the sorted segments, and then build a structure that allows us to perform a range query for count of elements greater than x.

A possible data structure for this is a Wavelet Tree or a Binary Indexed Tree (Fenwick Tree), but these are not straightforward to implement for range queries.

Alternatively, we can use a binary indexed tree with a coordinate compression approach, but since the R's can be up to 2n, which is manageable.

But for a range query [a, b], count of R's > x in that range.

But with the segments sorted by L, the R's are not sorted. So, we can't use a prefix array. Thus, a wavelet tree or a segment tree is needed.

Thus, the segment tree approach is the way to go.

Now, let's proceed to code.

But first, let's outline the steps again.

Code steps:

Read n.

Read n lines of l and r, storing the original index (0-based).

Sort the segments by l. Now, each segment has its original index.

Extract the sorted l's into a list, sorted_l.

Build a list sorted_r containing the r's of the sorted segments.

Build a segment tree where each node contains a sorted list of the r's in its range.

Compute the total edges:

Initialize total_edges = 0.

For each i in range(n):

    S = sorted_segments[i]

    current_l = S[0]

    current_r = S[1]

    # Find k using bisect_left on sorted_l for current_r.

    k = bisect.bisect_left(sorted_l, current_r)

    start = i + 1

    end = k - 1

    if start > end:

        continue

    # Query the segment tree for the range [start, end], count of R's > current_r.

    count = query_segment_tree(segment_tree, start, end, current_r)

    total_edges += count

Check if total_edges != n-1: output NO.

Else:

    Collect all edges:

    edges = []

    for i in range(n):

        S = sorted_segments[i]

        current_l = S[0]

        current_r = S[1]

        original_i = S[2]

        k = bisect.bisect_left(sorted_l, current_r)

        start = i + 1

        end = k - 1

        if start > end:

            continue

        # Query the segment tree for the range [start, end], and collect indices where R > current_r.

        t_indices = query_segment_tree_collect(segment_tree, start, end, current_r, sorted_segments)

        for t_idx in t_indices:

            original_j = sorted_segments[t_idx][2]

            edges.append( (original_i, original_j) )

    # Build adjacency list.

    adj = [[] for _ in range(n)]

    for u, v in edges:

        adj[u].append(v)

        adj[v].append(u)

    # Check connectivity using BFS.

    visited = [False] * n

    q = deque()

    q.append(0)

    visited[0] = True

    count_visited = 1

    while q:

        u = q.popleft()

        for v in adj[u]:

            if not visited[v]:

                visited[v] = True

                count_visited += 1

                q.append(v)

    if count_visited == n:

        print("YES")

    else:

        print("NO")

But the key part is implementing the segment tree with the query functions.

Implementing the segment tree in Python:

But in Python, building a segment tree with each node storing a sorted list can be time-consuming for large n. Let's see.

The build function:

The segments are sorted by L. For each node in the segment tree, the data is a sorted list of the R's in that node's range.

But building such a tree recursively can be done as follows:

def build_tree(data):

    n = len(data)

    size = 1

    while size < n:

        size <<= 1

    tree = [[] for _ in range(2 * size)]

    # Fill leaves

    for i in range(n):

        tree[size + i] = [data[i][1]]  # R values

    # Build parents

    for i in range(size - 1, 0, -1):

        left = tree[2 * i]

        right = tree[2 * i + 1]

        merged = merge(left, right)

        tree[i] = merged

    return tree

Where merge is a function that merges two sorted lists into one sorted list.

def merge(a, b):

    merged = []

    i = j = 0

    while i < len(a) and j < len(b):

        if a[i] < b[j]:

            merged.append(a[i])

            i += 1

        else:

            merged.append(b[j])

            j += 1

    merged.extend(a[i:])

    merged.extend(b[j:])

    return merged

But for n=5e5, the size of the tree would be 2^ceil(log2(5e5)) which is around 1e6. And each node's list is a sorted list. But building this will take O(n log n) time.

But with 5e5 elements, this would take O(n log n) time, which for Python may be tight for 2 seconds. However, perhaps it's manageable.

Once the tree is built, the query function for count is:

def query_count(tree, node, node_l, node_r, l, r, x):

    if node_r < l or node_l > r:

        return 0

    if l <= node_l and node_r <= r:

        # Binary search in the node's sorted list for elements > x.

        return len(tree[node]) - bisect.bisect_right(tree[node], x)

    mid = (node_l + node_r) // 2

    return query_count(tree, 2*node, node_l, mid, l, r, x) + query_count(tree, 2*node+1, mid+1, node_r, l, r, x)

But in Python, recursive functions are not the fastest. To handle large n, it's better to implement the query function iteratively.

Alternatively, we can implement the query function using a stack-based approach.

But this is getting complicated.

Alternatively, for the query, the segments are stored in the tree as sorted lists. For the query range [a, b], we can decompose it into nodes of the segment tree and for each node, perform a binary search to find the count of R's > x.

But how to implement this decomposition.

An alternative approach is to compute the size of the segment tree (next power of two of n), and then use the binary representation of the indices to decompose the query range.

But this is getting complicated.

Alternatively, here's an alternative implementation for the query function:

def query_count(tree, n_leaves, start, end, x):

    # Query the interval [start, end] (0-based indices) for elements > x.

    res = 0

    start += n_leaves

    end += n_leaves

    while start <= end:

        if start % 2 == 1:

            res += len(tree[start]) - bisect.bisect_right(tree[start], x)

            start += 1

        if end % 2 == 0:

            res += len(tree[end]) - bisect.bisect_right(tree[end], x)

            end -= 1

        start >>= 1

        end >>= 1

    return res

But this assumes that the segment tree is built in a way similar to a binary heap, where the leaves are at positions [n_leaves ... n_leaves + n - 1], and the tree is built with n_leaves being the next power of two of n.

So, for example, for n=5e5, the n_leaves would be 524,288 if the next power of two is 524,288.

Wait, but for n=5e5, the next power of two is 524,288 (since 2^19 = 524,288, and 5e5 is 500,000 < 524,288). Wait, no, 2^18 is 262,144, 2^19 is 524,288. So for n=5e5, the next power of two is 524,288.

So during the build phase, the segment tree is built with size as the next power of two greater than or equal to n. The leaves are from size to size + n - 1. The rest of the leaves (size + n to 2*size -1) are empty.

But during the query phase, the start and end are adjusted to be within the leaves.

But in the query function, start and end are the indices in the original array (0-based). So for a query range [a, b], we need to map them to the leaf positions, which are [size + a, size + b].

But the current code in the query function adds n_leaves to start and end, which is correct.

Thus, the query function iterates through the nodes covering the range [start, end], and for each node, checks if it's a left child or right child. If it's a left child, it moves to the next node. If it's a right child, it processes the node and moves to the left. The same for the end.

For each node processed (which fully covers a part of the query range), we perform a binary search to find how many elements are greater than x.

This approach for query is O(log n) nodes processed, each with a binary search O(log k) time, where k is the size of the node's data. Since the data in each node is a sorted list, the binary search is O(log k).

The total time for each query is O(log n * log k), which for each query is acceptable.

Thus, the code for query_count can be implemented as above.

Now, for the collection of edges, we need a similar function but instead of counting, we collect the indices.

But wait, the segment tree in this approach only stores the R values. We need to know the original indices of the segments. Thus, during the build phase, each node's data should store the R value along with their original index.

Wait, no. Because in the initial sorted_segments list, each segment has its original index. So, during the build phase, the segment tree's leaves should store the R values and their corresponding positions in the sorted list. For example, for each leaf node (representing the i-th segment in the sorted list), the data stored is (R, i).

Then, during a query, when we find R > x, we can collect the i's (sorted list indices), which can be mapped back to the original indices via the sorted_segments[i][2] (which is the original index).

So, during the build phase, the data passed to the segment tree is a list of tuples (R, i), where i is the index in the sorted list.

But the merge function for building the tree should sort the tuples by R. So the list in each node is sorted by R.

Thus, during the build phase, the leaves are created with (R, i) tuples, and each parent node's list is the merged and sorted list of its children's lists.

The query function for counting would then be modified to find the number of elements with R > x, which can be done via binary search on the sorted R list.

For collecting the indices, the query_collect function would, for each node's list, perform a binary search to find the first R > x, and then collect all the i's from that position onward.

Thus, the code for building the segment tree would be modified as follows:

sorted_segments is a list of tuples (L, R, original_index).

The data passed to the segment tree is a list of tuples (R, i) for each segment in the sorted list.

Thus:

data = [ (seg[1], idx) for idx, seg in enumerate(sorted_segments) ]

Then, the segment tree is built with these tuples, sorted by R.

The merge function would merge two lists sorted by R.

During a query, for x = S.R, we want to find all tuples (R, i) in the range where R > x. The count is the same as before, but to collect the indices, we can iterate over the tuples in the node's list where R > x, and collect the i's.

So, for the query_collect function:

def query_collect(tree, n_leaves, start, end, x):

    res = []

    start += n_leaves

    end += n_leaves

    while start <= end:

        if start % 2 == 1:

            node_list = tree[start]

            pos = bisect.bisect_right(node_list, (x, float('inf')))

            res.extend( [idx for r, idx in node_list[pos:]] )

            start += 1

        if end % 2 == 0:

            node_list = tree[end]

            pos = bisect.bisect_right(node_list, (x, float('inf')))

            res.extend( [idx for r, idx in node_list[pos:]] )

            end -= 1

        start >>= 1

        end >>= 1

    return res

But this assumes that each node_list is sorted by R. Since each tuple is (R, idx), comparing tuples is done lexicographically. So, for a given x, we can use bisect.bisect_right on the list of tuples. The key is to find the first tuple where R > x. To do this, we can search for (x, infinity), which will be inserted after all tuples with R <= x.

Once the pos is found, all elements from pos to the end of the list have R > x. We collect their indices.

Thus, the code for query_collect returns a list of indices (sorted list indices) that correspond to segments in the range [start, end] with R > x.

Once these indices are collected, we can get their original indices from sorted_segments[i][2].

Thus, the code for collecting the edges would look like this:

edges = []

for i in range(n):

    S = sorted_segments[i]

    current_l = S[0]

    current_r = S[1]

    original_i = S[2]

    k = bisect.bisect_left(sorted_l, current_r)

    start = i + 1

    end = k - 1

    if start > end:

        continue

    # Collect the sorted list indices j where R > current_r in [start, end]

    indices = query_collect(segment_tree, n_leaves, start, end, current_r)

    for j in indices:

        original_j = sorted_segments[j][2]

        edges.append( (original_i, original_j) )

Now, with this approach, the code should be manageable.

But the main problem is the time and memory usage for the segment tree.

But in Python, building the segment tree with 5e5 elements and 1e6 nodes, each storing a sorted list of (R, idx) tuples, may be feasible.

Now, let's proceed to code.

But there's one more thing: the original indices are 0-based, and the edges are added between the original indices.

Finally, the BFS for connectivity.

But in the code, the adjacency list is built as follows:

adj = [[] for _ in range(n)]

for u, v in edges:

    adj[u].append(v)

    adj[v].append(u)

Since there are n-1 edges, the adjacency list will have 2*(n-1) entries. For n=5e5, this is manageable.

The BFS is O(n) time.

Putting it all together.

Now, let's write the code.

But there are some optimizations to consider:

1. Preprocessing the sorted_l list for binary search.

2. Handling the segment tree building with the correct size.

3. Efficiently handling the merge of two sorted lists.

But in Python, merging two sorted lists can be done efficiently using the built-in sorted function, but for large lists, this may be slow. The previous merge function using two pointers is more efficient.

But for the build phase, each node's data is a sorted list of (R, idx) tuples.

Another possible optimization is to precompute the sorted list of segments by L, and their R's.

But now, let's proceed to write the code.

The code will be structured as follows:

- Read n.

- Read n segments, store as list of tuples (L, R, original index).

- Sort the segments by L.

- Extract the L's into a sorted_l list.

- Build the data for the segment tree: list of (R, idx) tuples.

- Build the segment tree.

- Compute the total edges.

- If not n-1, output NO.

- Else, collect the edges.

- Build the adjacency list.

- BFS to check connectivity.

But the code for the segment tree may be lengthy.

But given the time constraints, here's the code.

But I need to implement the segment tree.

Wait, here's a possible implementation:

import bisect
from collections import deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx +=1
    segments = []
    for i in range(n):
        l = int(data[idx])
        r = int(data[idx+1])
        segments.append( (l, r, i) )
        idx +=2

    # Sort segments by L
    segments.sort()
    sorted_l = [seg[0] for seg in segments]
    sorted_r_idx = [ (seg[1], i) for i, seg in enumerate(segments) ]

    # Build segment tree
    size = 1
    while size < n:
        size <<=1
    tree = [[] for _ in range(2 * size)]
    # Fill leaves
    for i in range(n):
        tree[size + i] = [sorted_r_idx[i]]
    # Merge parents
    for i in range(size-1, 0, -1):
        left = tree[2*i]
        right = tree[2*i+1]
        merged = []
        l_ptr = r_ptr =0
        while l_ptr < len(left) and r_ptr < len(right):
            if left[l_ptr][0] <= right[r_ptr][0]:
                merged.append(left[l_ptr])
                l_ptr +=1
            else:
                merged.append(right[r_ptr])
                r_ptr +=1
        merged.extend(left[l_ptr:])
        merged.extend(right[r_ptr:])
        tree[i] = merged

    # Function to query count
    def query_count(a, b, x):
        res =0
        a += size
        b += size
        while a <= b:
            if a %2 ==1:
                pos = bisect.bisect_right(tree[a], (x, float('inf')))
                res += len(tree[a]) - pos
                a +=1
            if b%2 ==0:
                pos = bisect.bisect_right(tree[b], (x, float('inf')))
                res += len(tree[b]) - pos
                b -=1
            a >>=1
            b >>=1
        return res

    total_edges =0
    for i in range(n):
        _, r, _ = segments[i]
        k = bisect.bisect_left(sorted_l, r)
        start = i+1
        end = k-1
        if start > end:
            continue
        cnt = query_count(start, end, r)
        total_edges += cnt

    if total_edges != n-1:
        print("NO")
        return

    # Collect edges
    edges = []
    # Function to query collect
    def query_collect(a, b, x):
        res = []
        a += size
        b += size
        while a <= b:
            if a %2 ==1:
                node = tree[a]
                pos = bisect.bisect_right(node, (x, float('inf')))
                res.extend( [idx for (r, idx) in node[pos:]] )
                a +=1
            if b%2 ==0:
                node = tree[b]
                pos = bisect.bisect_right(node, (x, float('inf')))
                res.extend( [idx for (r, idx) in node[pos:]] )
                b -=1
            a >>=1
            b >>=1
        return res

    for i in range(n):
        seg = segments[i]
        r = seg[1]
        original_i = seg[2]
        k = bisect.bisect_left(sorted_l, r)
        start = i+1
        end = k-1
        if start > end:
            continue
        indices = query_collect(start, end, r)
        for j in indices:
            original_j = segments[j][2]
            edges.append( (original_i, original_j) )

    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # BFS to check connectivity
    visited = [False]*n
    q = deque([0])
    visited[0] = True
    count =1
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                count +=1
                q.append(v)

    print("YES" if count ==n else "NO")

if __name__ == '__main__':
    main()

This code reads the input, sorts the segments by L, builds the segment tree, computes the total edges, checks if it's n-1, collects the edges if so, builds the adjacency list, and checks connectivity.

But there are potential optimizations:

- The segment tree merge function can be optimized using list extensions and pointer moves.

- The query functions are iterative and should be efficient.

Testing this code against the given examples.

First example:

Input:

6

9 12

2 11

1 3

6 10

5 7

4 8

After sorting by L:

1 3 (index 2)

2 11 (index 1)

4 8 (index 5)

5 7 (index 4)

6 10 (index 3)

9 12 (index 0)

sorted_l = [1,2,4,5,6,9]

sorted_r_idx = [ (3,0), (11,1), (8,5), (7,4), (10,3), (12,0) ]? Wait, no.

Wait, the sorted_r_idx is built as follows:

sorted_r_idx = [ (seg[1], i) for i, seg in enumerate(segments) ]

segments after sorting:

indexes 0 to 5:

segments[0] = (1,3,2)

segments[1] = (2,11,1)

segments[2] = (4,8,5)

segments[3] = (5,7,4)

segments[4] = (6,10,3)

segments[5] = (9,12,0)

so sorted_r_idx is:

(3,0), (11,1), (8,2), (7,3), (10,4), (12,5)

So for each i in the sorted list (0 to 5), sorted_r_idx[i] is (r, i), where i is the index in the sorted list.

Thus, the segment tree is built with these tuples.

When processing the first segment (i=0, L=1, R=3), k is bisect_left in sorted_l for 3. The sorted_l is [1,2,4,5,6,9]. The value 3 is between 2 and 4, so k=2. The start is i+1=1, end=2-1=1. So range [1,1].

Query the segment tree for the count of R > 3 in the range [1,1]. The R at position 1 is 11, which is >3. So count +=1.

Similarly, other segments are processed.

In the end, total_edges is 5, which is 6-1. Then edges are collected, and connectivity is checked.

This should output YES.

The other examples should be handled similarly.

But in practice, there might be bugs. For example, the indices in the segment tree are the indexes in the sorted list, and when collecting edges, the code uses segments[j][2], which is the original index.

Thus, the code should correctly collect edges between the original indices.

Overall, this code should work.
</think>

```python
import bisect
from collections import deque

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    segments = []
    for i in range(n):
        l = int(input[idx])
        r = int(input[idx + 1])
        segments.append((l, r, i))
        idx += 2

    segments.sort()
    sorted_l = [seg[0] for seg in segments]
    sorted_r_idx = [(seg[1], i) for i, seg in enumerate(segments)]

    size = 1
    while size < n:
        size <<= 1
    tree = [[] for _ in range(2 * size)]
    for i in range(n):
        tree[size + i] = [sorted_r_idx[i]]
    for i in range(size - 1, 0, -1):
        left = tree[2 * i]
        right = tree[2 * i + 1]
        merged = []
        l_ptr = r_ptr = 0
        while l_ptr < len(left) and r_ptr < len(right):
            if left[l_ptr][0] <= right[r_ptr][0]:
                merged.append(left[l_ptr])
                l_ptr += 1
            else:
                merged.append(right[r_ptr])
                r_ptr += 1
        merged.extend(left[l_ptr:])
        merged.extend(right[r_ptr:])
        tree[i] = merged

    total_edges = 0
    for i in range(n):
        _, r, _ = segments[i]
        k = bisect.bisect_left(sorted_l, r)
        start = i + 1
        end = k - 1
        if start > end:
            continue
        a = start
        b = end
        res = 0
        a += size
        b += size
        while a <= b:
            if a % 2 == 1:
                pos = bisect.bisect_right(tree[a], (r, float('inf')))
                res += len(tree[a]) - pos
                a += 1
            if b % 2 == 0:
                pos = bisect.bisect_right(tree[b], (r, float('inf')))
                res += len(tree[b]) - pos
                b -= 1
            a >>= 1
            b >>= 1
        total_edges += res

    if total_edges != n - 1:
        print("NO")
        return

    edges = []
    for i in range(n):
        seg = segments[i]
        current_r = seg[1]
        original_i = seg[2]
        k = bisect.bisect_left(sorted_l, current_r)
        start = i + 1
        end = k - 1
        if start > end:
            continue
        a = start
        b = end
        res = []
        a += size
        b += size
        while a <= b:
            if a % 2 == 1:
                node = tree[a]
                pos = bisect.bisect_right(node, (current_r, float('inf')))
                res.extend([idx for (r_val, idx) in node[pos:]])
                a += 1
            if b % 2 == 0:
                node = tree[b]
                pos = bisect.bisect_right(node, (current_r, float('inf')))
                res.extend([idx for (r_val, idx) in node[pos:]])
                b -= 1
            a >>= 1
            b >>= 1
        for j in res:
            original_j = segments[j][2]
            edges.append((original_i, original_j))

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n
    q = deque([0])
    visited[0] = True
    count = 1
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                count += 1
                q.append(v)

    print("YES" if count == n else "NO")

if __name__ == "__main__":
    main()
```