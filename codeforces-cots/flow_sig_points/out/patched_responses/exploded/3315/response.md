<think>
Okay, I need to solve this problem where Vladik's mom sorts a subsegment of a permutation, and for each query, we have to determine if the value at position xi remains the same after the sorting. The key point is that each query is independent, so after processing each query, the permutation goes back to the original state.

First, let's understand the problem. For each query, we're given l, r, x. The subarray from l to r (inclusive) is sorted in increasing order. After sorting, we need to check if the element at position x is the same as it was originally. So, for each query, the answer is "Yes" if the original element at x is in the same position after the subarray is sorted, otherwise "No".

The challenge is to process m queries efficiently. The constraints are n and m up to 1e4. So a brute-force approach where we sort each subarray for every query would be O(m * n log n), which for 1e4 * 1e4 * log(1e4) would be around 1e8 * 14 operations. That's probably too slow for a 2-second time limit. We need a smarter way.

Let me think. For a particular query (l, r, x), when we sort the subarray from l to r, the element at position x in the original array will stay the same only if, in the original array, that element is the same as the element that would be at position x after sorting the subarray.

Wait, but how? Let's say the original subarray from l to r has elements sorted in some order. When sorted, the elements in positions l to r are rearranged in increasing order. So, for position x (which is between l and r), the element in x after sorting will be the (x - l + 1)th smallest element in the original subarray. Because the sorted subarray is ordered, the element at position x in the sorted subarray is the (x - l + 1)th element in the sorted list.

Wait, no. For example, if the original subarray is from l to r (inclusive), when sorted, the first position (l) is the smallest element in the subarray, the next is the next smallest, etc. So the element at position x (which is between l and r) after sorting is the (k)th smallest element in the original subarray, where k = x - l + 1. Because the sorted subarray has elements arranged in order, so the first element is the 1st smallest, ..., the k-th element (at position l + k - 1) is the k-th smallest.

Wait, the index in the subarray for the sorted version: the original subarray is positions l to r. After sorting, the sorted subarray is a sorted list. For example, if the original subarray is [5,4,3], sorted becomes [3,4,5]. So position l (original index 0 in the subarray) would be 3, position l+1 would be 4, etc.

So for a query l, r, x, the position x is within l and r. The original element is P[x]. After sorting, the element at x in the sorted subarray is the (x - l + 1)th element in the sorted list (since the sorted list starts at l and ends at r). So the element after sorting is the (x - l + 1)th smallest in the original subarray.

So the problem reduces to: for the query l, r, x, the original value at x is val = P[x]. We need to check if val is the (x - l + 1)th smallest element in the original subarray from l to r.

If that's the case, then after sorting, the value at position x will be val, so the answer is "Yes"; otherwise, "No".

So for each query, the answer is "Yes" if the original value at x is equal to the k-th smallest element in the original subarray [l..r], where k = x - l + 1. Otherwise, "No".

The key insight here is that the answer depends on the original array's subarray [l..r] and the position x. So for each query, we can compute the k-th order statistic of the subarray and compare it to P[x]. If they are equal, output "Yes", else "No".

Now, the problem becomes, for m queries, each asking for the k-th smallest element in a subarray [l..r], where k is x - l + 1, and compare it to the original P[x].

The challenge is to compute these k-th order statistics efficiently.

But how? For each query, we need to find the k-th smallest element in a range [l..r]. With n and m up to 1e4, and each query potentially requiring O(r - l + 1 log (r - l + 1)) time if we sort each subarray, that would be O(m * n log n) in the worst case (if each query is the entire array). But 1e4 * 1e4 * log(1e4) is around 1e8 * 14, which is 1.4e9 operations. That's way too slow for Python in 2 seconds.

So we need a more efficient way to find the k-th order statistic for multiple range queries.

Possible approaches:

1. Precompute for all possible ranges and k, but that's impossible as there are O(n^2) ranges and O(n) k per range, leading to O(n^3) precomputation, which is way too much.

2. Use a data structure that allows answering range k-th order queries efficiently. For example, a wavelet matrix or a segment tree augmented with sorted lists.

In Python, implementing a wavelet matrix might be challenging due to time constraints. Alternatively, using a segment tree where each node contains a sorted list of the elements in its range. Then, for a query [l, r], we can traverse the segment tree to collect all the elements in the range, merge them, and then find the k-th smallest. But even this approach can be O((log n)^2 * n) per query in the worst case, which for m=1e4 could be acceptable if the per-query time is manageable.

But wait, how does the segment tree approach work for range k-th queries?

Each node in the segment tree represents a certain interval. For each node, we store a sorted list of elements in that interval. When querying a range [l, r], we traverse the segment tree, and for each node whose interval is entirely within [l, r], we include its sorted list. Then, we need to merge these sorted lists into a single sorted list, and then find the k-th element. However, merging multiple sorted lists and finding the k-th element efficiently is tricky.

Alternatively, we can perform a binary search on the possible values, and for each candidate value, count how many elements in the range [l..r] are <= that candidate. This is similar to the approach used in the "range median" problem.

The binary search approach for finding the k-th smallest element in a range:

- The minimum possible value is the smallest in the range, and the maximum is the largest.
- For a given candidate value mid, we can count how many elements in [l..r] are <= mid. If this count >=k, then the k-th smallest is <= mid. Otherwise, it's higher.
- We perform this binary search until we find the exact value.

To count the number of elements <= mid in [l..r], we can again use a segment tree where each node stores a sorted list. Then, for the query [l..r], we traverse the segment tree nodes that cover parts of the interval and perform a binary search in their sorted lists to count how many elements are <= mid. The total count is the sum over all relevant nodes.

Each binary search step for the candidate value takes O(log(max_val - min_val)) steps. For each step, the count operation is O(log n) per node in the segment tree traversal. Since the segment tree has O(log n) nodes per query, each count is O((log n)^2). The binary search steps are O(30) if the values are up to 1e9. So per query, this is O((log n)^2 * 30) operations.

For m=1e4, this would be 1e4 * (log n)^2 * 30. Since n is up to 1e4, log2(1e4) is about 14, so (14)^2 * 30 is around 5880 per query. For 1e4 queries, that's 5.8e7 operations, which should be manageable in Python, but maybe tight.

So this approach might work. Let's try to outline the steps.

First, build a segment tree where each node stores a sorted list of the elements in its interval. For a leaf node (single element), the sorted list is just that element. For internal nodes, the sorted list is the merge of their children's sorted lists. Building this segment tree takes O(n log n) time and O(n log n) space.

But merging the sorted lists for each node during the build could be expensive. For example, a node covering n elements would take O(n) time to merge. So the total time to build the segment tree is O(n log n), which is acceptable for n=1e4 (as 1e4 * 14 is 1.4e5 operations).

Once the segment tree is built, for each query l, r, x:

- Compute k = x - l + 1. We need to find the k-th smallest element in the range [l, r].
- Then compare it to the original P[x]. If they are equal, output "Yes", else "No".

So the key is to implement the k-th smallest query efficiently.

Implementing the binary search approach:

Initialize low as the minimum value in the array, high as the maximum.

While low < high:

   mid = (low + high) // 2

   count = number of elements <= mid in [l, r]

   if count >=k: high = mid

   else: low = mid + 1

Once low == high, that's the k-th smallest element.

So the main problem is implementing the count function efficiently.

The count function for a given range [l, r] and a value mid is the sum of the counts of elements <= mid in each segment tree node that fully lies within [l, r].

To compute this:

We can traverse the segment tree, and for each node that is fully covered by the query range [l, r], perform a binary search in the node's sorted list to find the number of elements <= mid. Sum all these counts.

For example, consider a node covering [start, end]. If [start, end] is entirely inside [l, r], then we use binary search on the node's sorted list to find the count. Otherwise, we split into left and right children and recurse.

This traversal is O(log n) steps, and each step's binary search is O(log s), where s is the size of the node's sorted list. For a node covering s elements, the sorted list has s elements, so binary search is O(log s). The sum over all nodes is O((log n)^2) per query.

So putting it all together, each query is O((log n)^2 * log max_val) steps. The max_val is up to n (since it's a permutation), so log max_val is O(log n). So per query, it's O((log n)^3) steps. For n=1e4, log n is about 14, so (14)^3 is around 2744, multiplied by 1e4 queries gives around 2.7e7 operations. That should be manageable in Python.

Now, the steps to implement:

1. Preprocess the array into a segment tree where each node's data is a sorted list of the elements in its interval.

2. For each query:

   a. Compute l, r, x. Check if x is within [l, r]. If not, the answer is "Yes" because the element is not in the sorted subarray. But according to the input constraints, "xi" is between li and ri, so we can skip this check.

   b. Compute k = x - l + 1.

   c. Find the k-th smallest element in the range [l, r].

   d. Compare it to the original P[x]. Output "Yes" if they are equal, else "No".

So let's proceed to implement this.

First, building the segment tree. The segment tree can be represented as a list of lists, but for Python, recursion might be easier.

But recursion in Python for a segment tree with n=1e4 is manageable. However, for a segment tree, the size is 4*n, which for n=1e4 is 4e4. Each node's sorted list can be built by merging the children's lists.

Wait, but building the segment tree with merged sorted lists for each node can be done as follows:

The segment tree is built by splitting the array into segments. For a node covering [start, end], if start == end, then the sorted list is [P[start]]. Otherwise, split into left and right children, build them recursively, then merge the two sorted lists into a single sorted list for the current node.

But merging two sorted lists of size m and n takes O(m + n) time. For each node, the time to build is O(s), where s is the size of the interval. The total time for building the segment tree is O(n log n), since each level of the tree takes O(n) time (summing across all nodes), and there are log n levels.

For n=1e4, O(n log n) is about 1e4 * 14 = 1.4e5 operations. That's acceptable.

Once the segment tree is built, the query function for the count is implemented as follows:

def count_less_or_equal(l, r, val):
    total = 0
    # traverse the segment tree, starting from the root
    # accumulate the count of elements <= val in [l..r]
    stack = [(root_start, root_end, root_node)]
    while stack:
        start, end, node = stack.pop()
        if end < l or start > r:
            continue
        if l <= start and end <= r:
            # this node is fully covered, count elements <= val in node's sorted list
            cnt = bisect_right(node.data, val)
            total += cnt
        else:
            # split into left and right children
            mid = (start + end) // 2
            stack.append( (mid+1, end, node.right) )
            stack.append( (start, mid, node.left) )
    return total

Wait, but how are the nodes structured? Each node can have left and right children. Alternatively, the segment tree can be represented using a list-based approach. However, in Python, using a recursive approach with objects may be slow. So perhaps an array-based implementation with each node's data stored in a list. But perhaps the easiest way is to implement the segment tree as a list of sorted arrays, where for each node (index i), left child is 2i+1, right child is 2i+2, etc. But that's often memory-intensive.

Alternatively, since building the segment tree recursively and storing each node's sorted list is manageable for n=1e4.

So here's a possible structure for the segment tree node:

Each node is an object (or a tuple) containing start, end, left child, right child, and the sorted list. But in Python, creating objects for each node may be slow. Alternatively, build it as a list of nodes, where each node is a dictionary.

But perhaps a better approach is to build the segment tree using a class-based approach. However, for the sake of efficiency, perhaps it's better to precompute all the nodes and their sorted lists.

Alternatively, here's a possible code outline using a recursive function:

def build(start, end):
    if start == end:
        return Node(start, end, [P[start]])
    mid = (start + end) // 2
    left = build(start, mid)
    right = build(mid+1, end)
    merged = merge(left.sorted_list, right.sorted_list)
    return Node(start, end, merged)

But merging two sorted lists can be done with the merge process, which is O(n) for each node.

But for a node covering the entire array, the merged list is the entire sorted array. For a node covering half the array, it's the sorted left half plus the sorted right half.

Wait, but merging two sorted lists can be done efficiently in O(m + n) time, where m and n are the sizes of the two lists. For the segment tree, each node's sorted list is built by merging the left and right children's sorted lists. For n=1e4, the total time is O(n log n) as each element is in O(log n) nodes.

For example, each element is in O(log n) nodes (each level of the tree). So the total time for merging is O(n log n).

But merging in Python can be done with the standard two-pointer approach.

For example:

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

But for each node, this is O(s), where s is the size of the node's interval. So for n=1e4, the total time is acceptable.

Once the segment tree is built, the next step is to implement the count_less_or_equal function.

But building the segment tree recursively might be manageable.

But with n=1e4, and each merge step taking O(n) time for the root node (which has O(n) elements), the build time is O(n log n). For 1e4, that's acceptable.

Now, considering the code structure.

First, read n and m, then read the permutation P.

Then build the segment tree.

But in Python, recursion depth could be a problem. For n=1e4, the segment tree's height is log2(1e4) ≈ 14, so recursion depth is manageable.

Implementing the build function recursively.

But for each node, we need to store the start and end indices, and the sorted list. So perhaps the nodes are represented as a list of tuples, or as a class.

Alternatively, perhaps the easiest way is to build a list-based segment tree. Let's consider building a list of sorted arrays, where each node is stored in a list. But in practice, building such a tree recursively with Python's functions can be done.

Once the segment tree is built, for each query, perform a binary search to find the k-th smallest element.

Now, for the code:

Let's outline the steps.

Read n and m.

Read the permutation P.

Build the segment tree. Each node has a start, end, and a sorted list.

For each query l, r, x:

   k = x - l + 1

   The current element is original_val = P[x-1] (since Python is 0-based, but the problem uses 1-based indices)

   Now, find the k-th smallest element in the range [l-1, r-1] (since Python is 0-based). Let's adjust the indices to 0-based.

   Compare this element to original_val. If they are the same, output "Yes", else "No".

But how to handle the 1-based to 0-based conversion?

In the problem, the permutation is given as p1, p2, ..., pn (1-based). So in code, we can store it as a list P where the index is 0-based (0 to n-1), with P[0] being p1, etc.

So when the query comes with l, r, x (all 1-based), we convert them to 0-based by subtracting 1. So l becomes l-1, r becomes r-1, x becomes x-1.

So the code steps are:

Read n, m.

Read P as a list of integers. Convert to 0-based.

Build the segment tree.

For each of m queries:

   Read l, r, x. Convert to 0-based: l0 = l-1, r0 = r-1, x0 = x-1.

   original_val = P[x0]

   Check if x0 is between l0 and r0. According to the problem constraints, this is always true. So we can skip this check.

   k = x0 - l0 + 1. Because in the sorted subarray (from l0 to r0), the element at position x0 is the k-th element in the sorted list.

   Now, find the k-th smallest element in the range [l0, r0].

   Compare this to original_val. If equal, output "Yes", else "No".

So the key part is implementing the function to find the k-th smallest in a given range.

Implementing the binary search approach for this:

def find_kth_smallest(l, r, k):

    low = min_val (the minimum of the entire array)

    high = max_val (the maximum of the entire array)

    while low < high:

        mid = (low + high) // 2

        cnt = count_less_or_equal(l, r, mid)

        if cnt >= k:

            high = mid

        else:

            low = mid + 1

    return low

But how to get min_val and max_val? Since it's a permutation of 1 to n, min is 1, max is n. So we can precompute min_val=1 and max_val=n.

Wait, no. The permutation is a permutation of numbers from 1 to n, so the min is 1, max is n.

So the initial low can be 1, high can be n.

Now, implement count_less_or_equal(l, r, val):

This function counts the number of elements <= val in the range [l, r] of the original array.

Implementing this via the segment tree:

We can write a helper function that recursively traverses the segment tree and sums the counts from the relevant nodes.

But in Python, recursion may be slow. So perhaps an iterative approach for the traversal.

The code for count_less_or_equal:

def count_less_or_equal(l, r, val):

    # Traverse the segment tree and count elements <= val in [l, r]

    count = 0

    stack = [root_node]

    while stack:

        node = stack.pop()

        if node.start > r or node.end < l:

            continue  # no overlap

        if l <= node.start and node.end <= r:  # fully covered

            # binary search in node's sorted list

            cnt = bisect.bisect_right(node.sorted_list, val)

            count += cnt

        else:

            # push children to stack

            stack.append(node.right)

            stack.append(node.left)

    return count

But this depends on how the nodes are structured. Each node must have start, end, left, right, and sorted_list attributes.

So the root_node is the top node of the segment tree, which covers the entire array.

But building such a tree in Python requires a recursive approach. Let's see:

We can define a Node class:

class Node:
    def __init__(self, start, end, sorted_list, left=None, right=None):
        self.start = start
        self.end = end
        self.sorted_list = sorted_list
        self.left = left
        self.right = right

def build_segment_tree(start, end, array):

    if start == end:

        return Node(start, end, [array[start]])

    mid = (start + end) // 2

    left = build_segment_tree(start, mid, array)

    right = build_segment_tree(mid+1, end, array)

    merged = merge(left.sorted_list, right.sorted_list)

    return Node(start, end, merged, left, right)

But the merge function needs to combine two sorted lists into one. As before.

But for n=1e4, this recursive build may take some time, but it's manageable.

But merging the left and right's sorted lists for each node is O(n log n) time.

Once the tree is built, the count_less_or_equal function can be implemented as described.

Now, considering the time and space constraints.

Each node's sorted list is stored. For the root node, it's the entire array sorted. For each level, the sum of the sizes of the nodes' sorted lists is O(n log n). For example, the root node has n elements. The next level has two nodes, each with n/2 elements, total n elements. The next level has 4 nodes, each with n/4 elements, total n elements. And so on. So the total storage is O(n log n), which for n=1e4 is 1e4 * 14 = 1.4e5 elements. That's acceptable.

Now, putting it all together.

But in Python, recursion depth for building the segment tree for n=1e4 may be an issue. Let's see: the depth of the tree is log2(n) which is about 14. Python's default recursion depth is 1000, so 14 is fine.

But let's test with n=1e4. The build function would first split into 0-9999, then 0-4999 and 5000-9999, etc., each time splitting into two until reaching leaves. The recursion depth is O(log2(n)), which is manageable.

Now, the code.

But first, note that the problem uses 1-based indices. So converting to 0-based is essential.

Sample input 1:

5 5

5 4 3 2 1

Queries:

1 5 3 → l=0, r=4, x=2 (0-based). k = 2 -0 +1 =3. So need the 3rd smallest in [0..4]. Original sorted subarray would be [1,2,3,4,5]. The element at position x=2 (0-based) is 3. So after sorting, it's the 3rd element (0-based is 2), which is 3. So original P[x] is 3. So output Yes.

Yes, the code should handle this.

Now, the code steps:

Read n and m.

Read the permutation array as a list. Then build the segment tree.

Implement the merge function.

But in the code, we can use the bisect module for binary search.

So, code outline:

import bisect

class Node:
    def __init__(self, start, end, sorted_list, left=None, right=None):
        self.start = start
        self.end = end
        self.sorted_list = sorted_list
        self.left = left
        self.right = right

def merge(a, b):
    merged = []
    i = j = 0
    len_a, len_b = len(a), len(b)
    while i < len_a and j < len_b:
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged

def build(start, end, arr):
    if start == end:
        return Node(start, end, [arr[start]])
    mid = (start + end) // 2
    left = build(start, mid, arr)
    right = build(mid +1, end, arr)
    merged = merge(left.sorted_list, right.sorted_list)
    return Node(start, end, merged, left, right)

def count_leq(node, l, r, val):
    if node.end < l or node.start > r:
        return 0
    if l <= node.start and node.end <= r:
        return bisect.bisect_right(node.sorted_list, val)
    return count_leq(node.left, l, r, val) + count_leq(node.right, l, r, val)

def find_kth_smallest(root, l, r, k):
    low = 1  # since permutation is of 1..n
    high = root.sorted_list[-1]
    while low < high:
        mid = (low + high) // 2
        cnt = count_leq(root, l, r, mid)
        if cnt >= k:
            high = mid
        else:
            low = mid + 1
    return low

n, m = map(int, input().split())
P = list(map(int, input().split()))
# convert to 0-based indices
root = build(0, n-1, P)

for _ in range(m):
    l, r, x = map(int, input().split())
    l0 = l-1
    r0 = r-1
    x0 = x-1
    original_val = P[x0]
    # Check if x is within [l, r]. According to problem constraints, yes.
    k = x0 - l0 + 1
    # Find the k-th smallest in [l0, r0]
    kth = find_kth_smallest(root, l0, r0, k)
    print("Yes" if kth == original_val else "No")

Wait, but in the code, when building the segment tree, the permutation elements are stored as per their original order. So the segment tree is built with the original array, and the find_kth_smallest function works correctly.

But in the sample input 1, when the first query is processed:

l=1 (0-based 0), r=5 (0-based 4), x=3 (0-based 2). k is 3. The k-th smallest in the entire array is 3. So the code returns 3, which is equal to P[2] (original_val is 3), so output "Yes".

Yes.

Another test case, like the second query in the first sample input:

query 1 3 1. After converting to 0-based: l=0, r=2, x=0. k is 0 -0 +1=1. The sorted subarray is [5,4,3], sorted becomes [3,4,5]. The first element (k=1) is 3. Original value at x=0 is 5. So 3 !=5, output "No".

In code, find_kth_smallest would compute the 1st smallest in [0..2], which is the minimum of 5,4,3, which is 3. So 3 !=5 → output "No".

Yes.

So the code seems correct.

But let's test the code's performance. For n=1e4 and m=1e4, building the segment tree with O(n log n) time is acceptable. Each query is O( (log n)^3 ) time.

But in Python, recursion in count_leq can be slow. Let's see:

The count_leq function is called recursively. For each query, the function traverses the nodes of the segment tree. Each node is processed once, and for each node, we either add its contribution (if fully covered) or process its children.

But the number of nodes processed per query is O(log n), since each level of the tree has O(1) nodes that are partially covered. So the count_leq function's time per query is O(log n) steps, and each step involves a bisect operation on a sorted list. The bisect operation is O(log s), where s is the size of the node's sorted list. But for nodes that are fully covered, their size can be up to the size of the query's range. However, in the worst case, for a query covering the entire array, the root node is processed, and bisect on a list of size n (O(log n) time). For each binary search step in find_kth_smallest, which is O(log n) steps, this is O(log n * log n) steps per query. Then, multiplied by m=1e4, this is acceptable.

But in practice, the code may be too slow for Python. So perhaps an iterative approach is better.

Alternative approach: use a list-based segment tree, stored as an array, where each node is stored in a list, and left and right children are computed via indices.

But in practice, the code may work for the constraints given. Let's proceed to implement the code as described.

But wait, the build function for the segment tree may take O(n log n) time. For n=1e4, and each merge step for a node of size s taking O(s) time. Let's calculate the time:

For each level of the tree:

- At the root (level 0), the node has size n. Time to merge: O(n).

- Level 1 has two nodes, each of size n/2. Total merge time: 2*(n/2) = n.

- Level 2 has four nodes, each of size n/4. Time: 4*(n/4) = n.

- And so on, for log n levels.

Total time is O(n log n), which is acceptable.

So for n=1e4, it's about 1e4 * 14 = 140,000 operations. For Python, which can handle millions of operations per second, this is manageable.

The count_leq function for a query is O(log n) steps. For each step, the bisect takes O(log s) time. But s varies per node. For example, in the root node, s is n. For nodes at lower levels, s is smaller.

But in the worst case, each query requires O(log n) steps for each of the O(log n) binary search steps in find_kth_smallest. So total steps per query are O( (log n)^2 * log n ), which is O( (log n)^3 ). For n=1e4, log n is about 14. 14^3 is 2744, multiplied by m=1e4 gives 2.7e7 operations. Python can handle that in a few seconds.

But the code uses recursion in count_leq. Recursion in Python is slower than iteration. So to optimize, perhaps we can rewrite count_leq iteratively.

Let's modify the count_leq function to use an iterative approach:

def count_leq(root, l, r, val):
    stack = [root]
    count = 0
    while stack:
        node = stack.pop()
        if node.end < l or node.start > r:
            continue
        if l <= node.start and node.end <= r:
            cnt = bisect.bisect_right(node.sorted_list, val)
            count += cnt
        else:
            stack.append(node.right)
            stack.append(node.left)
    return count

Yes, this way, we use an explicit stack and avoid recursion. This is likely faster in Python.

So, replacing the recursive count_leq with this iterative version.

Now, the code should be:

import bisect

class Node:
    def __init__(self, start, end, sorted_list, left=None, right=None):
        self.start = start
        self.end = end
        self.sorted_list = sorted_list
        self.left = left
        self.right = right

def merge(a, b):
    merged = []
    i = j = 0
    len_a, len_b = len(a), len(b)
    while i < len_a and j < len_b:
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged

def build(start, end, arr):
    if start == end:
        return Node(start, end, [arr[start]])
    mid = (start + end) // 2
    left = build(start, mid, arr)
    right = build(mid +1, end, arr)
    merged = merge(left.sorted_list, right.sorted_list)
    return Node(start, end, merged, left, right)

def count_leq(root, l, r, val):
    stack = [root]
    count = 0
    while stack:
        node = stack.pop()
        if node.end < l or node.start > r:
            continue
        if l <= node.start and node.end <= r:
            cnt = bisect.bisect_right(node.sorted_list, val)
            count += cnt
        else:
            stack.append(node.right)
            stack.append(node.left)
    return count

def find_kth_smallest(root, l, r, k):
    low = 1  # min possible value in permutation
    high = root.sorted_list[-1]  # max value in permutation
    while low < high:
        mid = (low + high) // 2
        cnt = count_leq(root, l, r, mid)
        if cnt >= k:
            high = mid
        else:
            low = mid + 1
    return low

n, m = map(int, input().split())
P = list(map(int, input().split()))
# build the segment tree
root = build(0, n-1, P)

for _ in range(m):
    l, r, x = map(int, input().split())
    l0 = l-1
    r0 = r-1
    x0 = x-1
    original_val = P[x0]
    k = x0 - l0 + 1
    kth = find_kth_smallest(root, l0, r0, k)
    print("Yes" if kth == original_val else "No")

This code should work. Let's test it against the sample input.

Sample Input 1:

5 5

5 4 3 2 1

Queries:

1 5 3 → converted to l=0, r=4, x=2. k=3. The 3rd smallest element in [0-4] is 3. P[x0] is 3 → Yes.

Sample Output 1's first line is Yes.

Sample Input 1's second query:

1 3 1 → l=0, r=2, x=0. k=1. The 1st smallest is 3 (subarray [5,4,3]). P[x0] is 5 → 3 !=5 → No.

So the code should output "No".

But in the code, when we call find_kth_smallest(root, 0, 2, 1):

The binary search starts with low=1, high=5. Mid=3. count_leq returns the number of elements <=3 in [0-2]. The original subarray is [5,4,3]. The elements <=3 are 1. So cnt=1 >=1 → high=3. Next iteration: low=1, high=3. mid=2. count_leq returns 0. So low becomes 3. Now low == high → return 3. Compare to original_val 5 → No.

Yes.

Another test case: the fifth query in the first sample:

2 5 3 → l=2-1=1, r=5-1=4, x=3-1=2. k=2-1+1=2. The subarray is [4,3,2,1]. When sorted, it becomes [1,2,3,4]. The x is 2 (0-based), so the element at position 2 is 3. Original P[x0] is 3. But wait, the original array is [5,4,3,2,1]. After sorting positions 1-4 (which are 4,3,2,1) → sorted to 1,2,3,4. So the subarray becomes [4, 1,2,3,1]? No, the original array is 5,4,3,2,1. The query is l=2, r=5 (1-based), which is indices 1 to 4 in 0-based. The subarray is [4,3,2,1]. When sorted, it's [1,2,3,4]. So after sorting, the elements from 1 to 4 (0-based) are [1,2,3,4]. The x is 3-1=2 (0-based) in the original array. So after sorting, the element at position 2 is 3. Original value is 3. So output is "Yes"? Wait the sample's fifth query's output is "No".

Wait the sample input's fifth query is:

2 5 3 → l=2, r=5, x=3 (1-based). Converted to 0-based l=1, r=4, x=2. The original value is P[2] =3.

After sorting the subarray from l=1 to r=4 (0-based indices 1 to 4), which is [4,3,2,1], sorted to [1,2,3,4]. The x is position 2 (0-based) in the array. So after sorting, the subarray is [1,2,3,4]. The x is 2, which is the third element (0-based) in the subarray. So the value is 3, which is the same as the original. So why does the sample output say "No"?

Wait, the sample input's fifth query in the first example:

Input line 5: 2 5 3 → l=2, r=5, x=3. The original array is [5,4,3,2,1]. The subarray from l=2 to r=5 (1-based) is positions 1 to 4 (0-based), which is [4,3,2,1]. When sorted, this becomes [1,2,3,4]. The x is 3 (1-based) → 0-based is 2. In the sorted subarray, the elements at positions 1 to 4 (0-based) are [1,2,3,4]. So the element at position 2 is 3. Original P[x0] is 3. So the answer should be "Yes". But according to the sample output, it's "No".

Wait, this contradicts. What's the actual sample input?

Sample input for the fifth query in first example:

2 5 3 → l=2, r=5, x=3. The original array is 5,4,3,2,1. After sorting the subarray [4,3,2,1], sorted to [1,2,3,4]. So the entire array becomes 5,1,2,3,4. The x is position 3 (1-based), which is 2 in 0-based. The value is 2. But original value at x was 3. So the new value is 2, which is different. Hence, output "No". Oh right! I see.

Ah, I made a mistake in the earlier analysis. The x in the fifth query is 3 (1-based), which is 2 in 0-based. In the original array, P[2] is 3. After sorting the subarray from 2-5 (0-based 1-4), the entire array becomes [5,1,2,3,4]. The x is position 2 (0-based) which is 2. So the new value is 2. So 3 != 2 → output "No".

So the code should correctly find that the k-th smallest in the subarray l=1 to r=4 (0-based) is 2.

Wait, why?

In the fifth query:

l=2 (0-based 1), r=5 (0-based4), x=3 (0-based2). k = 2-1+1 =2. So the code is looking for the 2nd smallest element in the subarray [4,3,2,1] (elements are 4,3,2,1 at 0-based indices 1,2,3,4).

The subarray is [4,3,2,1]. The sorted list is [1,2,3,4]. The k=2nd smallest is 2. So the code should find 2, compare to original value 3 → outputs "No".

So the code's find_kth_smallest function, when called with l=1, r=4, k=2:

The binary search starts with low=1, high=4.

Mid=2.5 → mid=2. count_leq(1,4,2) is the number of elements <=2 in [4,3,2,1]. Elements are 4,3,2,1. Elements <=2: 2 and 1 → count is 2. So cnt >=2 → high=2.

Next iteration: low=1, high=2. mid=1.5 → mid=1. count_leq returns elements <=1: only 1. cnt=1 <2 → low=2.

Now, low=2, high=2. Return 2. Compare to original_val=3 → outputs "No". Which matches the sample.

So the code should handle this correctly.

Thus, the code is correct.

Now, the code must be optimized for speed. Let's think of possible optimizations.

In Python, the merge function can be optimized. Instead of merging two lists with the two-pointer approach, perhaps using the built-in sorted function. But for two sorted lists, merging is O(m+n), which is the same as sorted(a + b). However, sorted(a + b) would create a new list and sort it, which is O((m+n) log (m+n)) time. So the two-pointer approach is better. So the current merge function is correct.

Another optimization: precompute the min and max values. Since the permutation is of 1 to n, the min is 1 and max is n. So in find_kth_smallest, low can be 1 and high can be n. The line high = root.sorted_list[-1] would be n, but for a permutation, root's sorted list is [1,2,...,n]. So sorted_list[-1] is n. So in the find_kth_smallest function, we can replace high = root.sorted_list[-1] with high = n. This saves a little time.

Similarly, low can be set to 1.

Another optimization: in the build function, since the array is a permutation, perhaps we can avoid the merge step by knowing that it's sorted. But no, the permutation is arbitrary. So the code must proceed as is.

Another optimization is to precompute the sorted lists for all possible ranges using a different data structure, but I don't see a better way.

Another possible optimization is to use the built-in bisect module's bisect_right function. Which is already done.

In Python, the code's performance may be acceptable. For m=1e4 queries, each with O( (log n)^3 ) steps, it's manageable.

Thus, the code should work correctly and efficiently.
</think>

```python
import bisect

class Node:
    __slots__ = ['start', 'end', 'sorted_list', 'left', 'right']
    def __init__(self, start, end, sorted_list, left=None, right=None):
        self.start = start
        self.end = end
        self.sorted_list = sorted_list
        self.left = left
        self.right = right

def merge(a, b):
    merged = []
    i = j = 0
    len_a, len_b = len(a), len(b)
    while i < len_a and j < len_b:
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged

def build(start, end, arr):
    if start == end:
        return Node(start, end, [arr[start]])
    mid = (start + end) // 2
    left = build(start, mid, arr)
    right = build(mid + 1, end, arr)
    return Node(start, end, merge(left.sorted_list, right.sorted_list), left, right)

def count_leq(root, l, r, val):
    stack = [root]
    count = 0
    while stack:
        node = stack.pop()
        if node.end < l or node.start > r:
            continue
        if l <= node.start and node.end <= r:
            count += bisect.bisect_right(node.sorted_list, val)
        else:
            stack.append(node.right)
            stack.append(node.left)
    return count

def find_kth_smallest(root, l, r, k, max_val):
    low, high = 1, max_val
    while low < high:
        mid = (low + high) // 2
        cnt = count_leq(root, l, r, mid)
        if cnt >= k:
            high = mid
        else:
            low = mid + 1
    return low

n, m = map(int, input().split())
P = list(map(int, input().split()))
root = build(0, n-1, P)
max_val = n

for _ in range(m):
    l, r, x = map(int, input().split())
    l0 = l - 1
    r0 = r - 1
    x0 = x - 1
    original_val = P[x0]
    k = x0 - l0 + 1
    kth = find_kth_smallest(root, l0, r0, k, max_val)
    print("Yes" if kth == original_val else "No")
```