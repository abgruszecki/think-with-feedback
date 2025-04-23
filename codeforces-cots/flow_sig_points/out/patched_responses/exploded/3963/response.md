<think>
Okay, let's tackle this problem. Hmm. The problem is about handling a grid with garlands, each consisting of multiple bulbs. We need to process switch events that toggle garlands on and off, and answer queries about the sum of active bulbs in a rectangular area. The constraints are tight, especially with up to 2e3 garlands each with 2e3 bulbs, and queries up to 1e6 but only 2e0 ASK operations. Wait, no, the problem says there are no more than 2000 ASK events. Oh right, so for ASK events, even though the total q is 1e6, the ASKs are only up to 2000. That's a crucial point.

So, the main challenge is to efficiently handle the ASK queries. Each ASK requires summing all active bulbs in a rectangle. Since the bulbs are part of garlands, and garlands can be toggled on and off, we need a way to quickly compute the sum for the current state of garlands.

Let's think about possible approaches. The naive approach for each ASK query would be to iterate through all garlands, check if they are active, then iterate through all their bulbs and check if they are inside the query rectangle, summing up their values. But with garlands up to 2000, each with 2000 bulbs, and ASK queries up to 2000, this would be 2000 * 2000 * 2000 = 8e10 operations, which is way too slow.

So we need a more efficient way. What's the alternative? Maybe precompute for each garland the 2D prefix sums of their bulbs. Then, for each garland, we can quickly compute the sum in any rectangle. Then, for each ASK query, we can iterate over all active garlands and sum their contribution to the query rectangle using their prefix sums.

But how to handle this efficiently?

Let's break it down:

1. Preprocessing each garland's bulbs by their positions, and compute a prefix sum for their coverage in the grid. For each garland, we can create a 2D array that stores the sum of all bulbs in the garland up to each cell (like a standard 2D prefix sum). But building such an array for each garland would take O(nm) per garland, which is 2000*2000=4e6 per garland, and with 2000 garlands, that's 8e9 elements. That's way too much memory. So this approach isn't feasible.

Alternative idea: For each garland, store the coordinates and values of all its bulbs. Then, for each query, for each active garland, check how many of their bulbs fall into the query rectangle. But checking each bulb in each active garland for each query is O(k * average bulbs per garland * q_ask). For k=2000, average len=2000, q_ask=2000, that's 2000 * 2000 * 2000 = 8e9 operations. That's way too slow.

Hmm. So we need a way to, for each garland, quickly determine the sum of bulbs within a rectangle. Another approach: For each garland, precompute a list of (i,j) positions and their w values, and then build a 2D binary indexed tree (Fenwick tree) or a segment tree for that garland. But building a separate 2D BIT for each garland would again require O(k * n * m) memory, which is 2000*2000*2000=8e9 elements. Not feasible.

Alternative approach: For each garland, store the list of bulbs, and for each bulb, record its position and value. Then, for each query, iterate over all active garlands, and for each such garland, find the sum of bulbs in the query rectangle. But how to compute that sum quickly?

Wait, perhaps for each garland, we can precompute a map from (i,j) to the value w. Then, for a query rectangle, the sum would be the sum of all (i,j) in the rectangle for all active garlands. But again, this would require checking each cell in the rectangle for each active garland, which is O((x2-x1+1)*(y2-y1+1)*active_garlands). For a large rectangle, this could be up to 2000^2 cells, multiplied by 2000 active garlands and 2000 queries. That's 2e3 * 2e3 * 2e3 * 2e3 = 16e12 operations. Definitely not feasible.

So we need a way to represent each garland's bulbs in a way that allows for efficient rectangle sum queries. Let's think differently. For each garland, can we precompute a list of all their (i,j) positions and their values, then for each query, we can check each garland's active status, and for each active one, compute the sum of their bulbs that are in the query rectangle. The problem is that for each query, checking all active garlands and their bulbs is O(k * len) per query, which is 2000*2000=4e6 per query. For 2000 queries, that's 8e9 operations. That's too slow.

Wait, but in the constraints, the sum of all len across all garlands is 2000 * 2000 = 4e6. So for all garlands, the total number of bulbs is 4e6. If for each ASK query, we can iterate through all bulbs of all active garlands and check if they are inside the query rectangle, summing their values. Then, each ASK would take O(total_bulbs) time. Since total_bulbs is 4e6 and there are 2000 ASK queries, that's 8e9 operations. That's still way too slow for Python, which can handle about 1e8 operations per second. So 8e9 is way beyond that.

Thus, this approach is not feasible.

Alternative idea: For each bulb, precompute for which rectangles it would be included. But not sure.

Another approach: For each garland, precompute a list of all their (i,j) coordinates and their w, and build a data structure that can answer the sum of w's in a rectangle quickly. Since each garland's bulbs are part of a chain (adjacent cells), perhaps the list is ordered, but that might not help. The key is that for each garland, we have a list of (i,j, w) points, and for a query, we need the sum of w where (i,j) is in the query rectangle and the garland is active.

To compute this sum quickly per garland and per query, perhaps for each garland, we can precompute a 2D prefix sum array. But again, storing a 2D array for each garland is O(k * n * m) memory, which is 2000 * 2000 * 2000 = 8e9. Which is way too much.

But wait, maybe n and m are up to 2000 each, but each garland's bulbs are sparsely placed. So for a garland with len 2000 bulbs, it's only 2000 points. So for each garland, instead of a full 2D array, maybe we can represent the points in a sorted list and perform binary search for each query.

Yes! For example, for a garland, we can have a list of all its (i,j,w) and pre-sort them by row and then by column. Then, for a query rectangle [x1, y1, x2, y2], we can find all bulbs in that garland that lie within x1 <= i <=x2 and y1 <= j <=y2. Since the list is sorted, perhaps we can do a binary search to find the valid points and sum their w. But how?

Let's think: For each garland, we can pre-sort the list of (i,j) in such a way that we can quickly query the sum for a given rectangle. One way is to group the points by their i (row) and for each row, have a sorted list of j (columns) and a prefix sum. Then, for a query, we can iterate over all rows in [x1, x2], and for each such row, find the range of columns in [y1, y2] and sum the corresponding values. But this requires per garland, a structure where for each row, there's a sorted list of columns and prefix sums.

But building such a structure for each garland would take O(len) space per garland. For len up to 2000, and 2000 garlands, that's 2000 * 2000 = 4e6 total entries. That's manageable.

Here's the plan:

For each garland g:

- Create a dictionary (row_dict) where each key is a row i, and the value is a list of tuples (j, w), sorted by j. Also, for each row, create a prefix sum array of the w's in that row.

So for example, if the garland has bulbs at positions (1,2), (1,3), (2,3), then row_dict[1] has [(2, w1), (3, w2)], and row_dict[2] has [(3, w3)]. For each row's list, we can precompute a prefix sum array.

Then, for a query rectangle (x1, y1, x2, y2), to compute the sum for garland g (if active), we do the following:

Loop over all rows i in x1 to x2. For each row i in garland g's row_dict:

- Find all (j, w) in row i where j is between y1 and y2.

Since the list is sorted by j, we can perform a binary search to find the lower and upper bounds of j in the range [y1, y2]. Then, using the prefix sum array for that row, we can compute the sum of w's in that j range quickly.

The sum for the garland in the query rectangle is the sum of all such contributions across all rows in x1 to x2.

If the garland is active (turned on), we add this sum to the total.

The key is that for each ASK query, we loop through all active garlands, and for each garland, loop through the rows in the query's x range, and perform binary searches on the j's in those rows.

Now, the question is, what is the time complexity for each ASK query?

Let's break it down:

For each ASK query, for each active garland g:

- The number of rows in g's row_dict that fall within [x1, x2] is O(number of distinct rows in g that are in the query's x range). For a garland of length len, the maximum possible rows in a query is min(len, x2 -x1 +1). But worst case, for a garland that has all its bulbs in the x range, this is O(len) per garland. Which would be 2000 per garland, multiplied by 2000 garlands, leading to 4e6 per query. But ASK queries are up to 2000, so 8e9 operations. That's again way too slow.

Wait, but perhaps the garlands' rows are sparse. For example, each garland's bulbs are along a path, so they are contiguous. But even so, if a query's x range is large, the number of rows in the garland that are in the x range could be up to the entire length of the garland. So this approach may not be feasible.

Alternative Idea: For each garland, precompute a list of all (i,j,w) entries, and for each, store them in a list. Then, for each query, iterate through all active garlands, and for each bulb in that garland, check if (i,j) is within the query's rectangle. Sum the w if it is. But this is O(k * len_avg) per query. For k=2000 and len_avg=2000, that's 4e6 per query. With 2000 queries, 8e9 operations. That's too slow in Python.

Wait, but the ASK queries are up to 2000. Let's see: 2000 queries * 2000 active garlands * 2000 bulbs each = 8e9 operations. Python can't handle that in 3 seconds. So this approach is not feasible.

Hmm. So we need a smarter way. Let's think again: Each bulb is part of exactly one garland. For each bulb, we can precompute for each possible query rectangle whether it's included. But that's impossible, as there are O(n^4) possible rectangles.

Alternative Idea: For each bulb, store its position (i,j) and w. Then, build a 2D prefix sum array where each cell (i,j) contains the sum of all bulbs in that cell, multiplied by the garland's current state (active or not). But the problem is that the garlands' states are dynamic, toggled by SWITCH events. So the sum for a cell depends on the state of the garland to which it belongs.

So, the sum for a cell is the sum of w * (active_status of garland) for all bulbs in that cell. Since each cell has at most one bulb (as per the problem statement), each cell's contribution is either 0 (if the garland is inactive) or the bulb's w (if active).

Thus, the total sum for a rectangle is the sum of all cells in the rectangle where the bulb's garland is active.

But building a data structure that allows for dynamic updates (toggle garland) and range queries (sum over rectangle) is exactly the kind of problem that a 2D Binary Indexed Tree (Fenwick Tree) or Segment Tree can handle. However, each toggle affects all cells that are part of the garland. So when a garland is toggled, all its bulbs' cells need to be flipped (add or subtract their w) in the 2D BIT.

But the problem is that for each garland, which has up to 2000 bulbs, a toggle would require 2000 update operations on the BIT. Since there are up to 1e6 SWITCH events, each requiring up to 2000 operations, that's 2e9 operations. Which is impossible in Python.

So this approach is not feasible.

Wait, but the number of ASK queries is small (2000). Maybe there's a way to precompute all possible active states and answer the queries accordingly. But with 2000 garlands, the number of possible active states is 2^2000, which is way too big.

Alternative Idea: Since the SWITCH events can toggle garlands multiple times, but the ASK queries are only 2000, perhaps we can process all events, track the current state of each garland, and for each ASK query, compute the sum by considering all active garlands' contributions to the query rectangle. But again, this brings us back to the problem of how to compute each garland's contribution quickly.

Let me think again: For each garland, precompute a list of all its (i,j) and w. For each query, for each active garland, sum the w for all (i,j) in the query rectangle. How can we compute this sum quickly for each garland?

Another Idea: For each garland, build a 2D prefix sum structure. Since each garland's bulbs are sparse (up to 2000), perhaps we can use a list of the bulbs sorted in a way that allows efficient range queries.

For example, for each garland g:

- Sort all bulbs' coordinates (i,j) in a list sorted by (i, j).

Then, for a query rectangle [x1, y1, x2, y2], we can use binary search to find all bulbs in g that have i between x1 and x2, and j between y1 and y2. For each such bulb, sum their w. The sum can be computed using a prefix sum array of the sorted list.

Wait, but how to handle two dimensions with binary search. Let's see:

We can sort the bulbs first by i, then by j. Then, for each garland, create a list sorted_i which is sorted by i (and j within the same i). Then, for a query x1 <=i <=x2 and y1 <=j <=y2, we can find the range of bulbs in sorted_i where i is between x1 and x2. Within those, we can then filter those j between y1 and y2, and sum their w. But even this requires for each bulb in the i range, checking the j. Which is O(k) per garland, but maybe with some optimizations.

Alternatively, for each garland, precompute a sorted list of bulbs by i. Then, for a query, we can binary search the start and end indices in the list where i is within x1 and x2. Then, within that subarray, we can binary search for j >= y1 and j <= y2. However, since the j's in the subarray are not sorted, this approach won't work. Wait, no. If the list is sorted by i and j, then for the subarray with i in [x1, x2], the j's would be sorted within each i. But within the same i, j can be in any order if the garland's path isn't sorted.

Wait, but the garland is a chain where consecutive bulbs are adjacent. So the path can snake around. For example, the garland could be arranged in a spiral. So the j's in the same i may not be sorted. So even if the list is sorted by i, within the same i, the j's may be in any order. Therefore, for the subarray with i between x1 and x2, the j's are not sorted. Thus, even after finding the i range, we would need to check each bulb's j in that range to see if it's within y1 and y2.

So for each garland, the time per query is O(number of bulbs in the garland that are in the i range) multiplied by O(1) to check j. But the number of such bulbs can be up to len of the garland (if all are in the i range). So this approach is O(len) per garland per query. Which again is 2000 * 2000 = 4e6 per query. For 2000 queries, 8e9 operations. Which is too slow.

Hmm. So we need a way to precompute for each garland a data structure that allows us to answer the sum of bulbs in a rectangle in O(log len) time.

Perhaps using a segment tree or a range tree for each garland. For example, for each garland, build a 2D range tree where each node represents a point (i,j) and we can query the sum of points within a rectangle. For each garland, building such a structure would take O(len log len) time, and querying would take O(log len) per query. Then, for each ASK query, we would loop through all active garlands and query their sum in O(log len) time, summing all the results.

This way, for each ASK query, the time is O(k log len_avg). With k=2000 and len_avg=2000, log2(2000) is about 11. So 2000 * 11 = 22,000 operations per query. For 2000 queries, 44,000,000 operations. That's manageable.

But building a 2D range tree for each garland would take O(len log len) time and space. For len up to 2000, that's 2000 * 11 = 22,000 per garland. For 2000 garlands, that's 44,000,000 elements, which is manageable.

But implementing a 2D range tree in Python is not trivial, and may be time-consuming, especially with the time constraints.

Alternative Idea: For each garland, precompute a list of all (i,j,w) sorted by i and j, and build a prefix sum array. Then, for a query rectangle, perform binary search to find the lower and upper bounds of i and j. But this only works if the points are sorted in such a way that they can be filtered by i and j ranges. For example, if the points are sorted first by i, then by j, then for a given i range, the points are contiguous. However, within that i range, the j's may not be sorted. Wait, no. If the list is sorted by i, then j, then for all points in the i range [x1, x2], the j's are sorted. So within that i range, we can perform a binary search to find the j range.

Yes! So here's the plan:

For each garland, sort all its bulbs in a list sorted by (i, j). Then, for each bulb in the sorted list, compute a prefix sum array. For a query rectangle [x1, y1, x2, y2], we can:

1. Find the first index in the sorted list where i >= x1 and j >= y1 (but this might not be correct because the i is x1, but j could be less than y1). Wait, no. Since the list is sorted by i, then j, the points are ordered first by i in ascending order, then j in ascending order. So all points with i < x1 come before the points with i >=x1. Similarly, within the same i, points are sorted by j.

So for the x1 and x2:

- Find the start index in the sorted list where i >=x1.

- Find the end index in the sorted list where i <=x2.

The sublist from start to end-1 contains all points with i in [x1, x2].

Within this sublist, the j's are sorted in ascending order. So within this sublist, we can find the first j >= y1 and the last j <= y2 using binary search.

The sum of these points' w is the sum between those indices in the prefix sum array.

So for each garland, the process is:

a. For the garland's sorted list, find the range of points where i is between x1 and x2. This can be done via binary search for x1 and x2.

b. Within that range, the j's are sorted. So find the start and end positions in that subrange where j is between y1 and y2.

c. The sum is the prefix_sum[end] - prefix_sum[start].

This would allow us to compute the sum for the garland in O(log len + log len) = O(log len) per garland per query.

If this is possible, then for each ASK query, processing all active garlands would take O(k log len_avg) time, which for k=2000 and len_avg=2000 is manageable.

So the steps are:

1. For each garland, sort its bulbs by (i, j). For each bulb, i is the row, j is the column. Then, compute a prefix sum array.

2. For each ASK query:

   a. For each active garland:

      i. Find the start and end indices in the sorted list where i is >=x1 and <=x2.

      ii. Within that sublist, find the start and end indices where j is >=y1 and <=y2.

      iii. Sum the w's in that sub-sublist using the prefix sum array.

   b. Sum all these values and output.

Now, how to implement steps i and ii.

For step i, since the list is sorted by i (then j), we can find the first index where i >=x1 and the first index where i >x2. The range between these indices gives all points with i in [x1, x2].

This can be done using bisect_left and bisect_right.

For example, the start index is bisect.bisect_left(sorted_list, (x1, 0)) (assuming j is >=0). Wait, but each element in the sorted list is a tuple (i, j, w), but for binary search purposes, we can create a list of (i, j) and a separate prefix sum array. Alternatively, when sorting, create a list of (i, j, w), sorted by i then j.

So for example, the list for a garland is sorted as per the (i, j) tuples.

Then, for x1, we can use bisect.bisect_left to find the first index where i >=x1. Similarly, for x2, find the first index where i >x2. The slice from start to end is the range of points with i in [x1, x2].

Within this slice, the j's are sorted. So we can extract the j's and perform another binary search to find the first j >=y1 and the last j <=y2.

But how to extract the j's? Well, since the slice is a list of tuples (i,j,w), we can create a sublist of j's for this slice, but in Python, list comprehensions are efficient. Alternatively, since the j's are already sorted in this slice, we can use binary search on the slice.

For example, within the slice, for each element, j is in sorted order. So for the subslice, the j's are sorted. So we can use bisect_left and bisect_right on the j's.

But in Python, for a list of tuples, bisect module functions work on the entire tuple. So perhaps the sorted list is sorted by (i, j), and for the slice between start and end, the j's are sorted. So for that slice, we can use bisect_left and bisect_right to find the indices where j is >=y1 and <=y2.

Wait, but within the slice, the j's are sorted. So for example, the slice is from index a to index b (exclusive). For each element in this slice, the j increases.

So for this slice, the j's are in ascending order. So for the j values, we can find the left and right indices using bisect.

So for the slice, the first j >= y1 is found by bisect.bisect_left on j, starting from 0. Similarly, the first j > y2 is found by bisect.bisect_right.

But how to extract the j's from the slice?

We can create a list of j's for the slice, but that would take O(k) time where k is the length of the slice. Alternatively, we can use the key parameter in bisect functions, but Python's bisect doesn't support a key function. So we need a way to binary search the slice for the minimal j >= y1.

Alternatively, since the slice is a list of tuples, we can create a helper function to generate the j's on the fly.

Wait, but for the bisect module, the list must be in a sorted order. Since the slice is sorted by (i, j), and i is fixed (since all i are in [x1, x2]), the j's are sorted. So for the slice, the j's are in ascending order.

Thus, to find the lower and upper bounds for y1 and y2 in the j's of the slice:

The left index is the first position in the slice where j >= y1.

The right index is the first position in the slice where j > y2.

The number of elements in the slice between left and right is right - left. Each of these elements has j between y1 and y2 (inclusive).

To compute the sum of w's for these elements, if we have a prefix sum array for the entire garland's sorted list, then the sum is prefix_sum[start + right] - prefix_sum[start + left].

But wait, the prefix sum array is for the entire garland's sorted list, not just the slice. So after finding the start and end indices in the entire list for i in [x1, x2], and then within that slice, the left and right indices for j in [y1, y2], the total start index is start_idx + left, and the end index is start_idx + right. Then, the sum is prefix[end] - prefix[start].

Yes.

So the steps are:

For a garland:

sorted_list = sorted by (i, j)

prefix_sum[0] = 0

prefix_sum[k] = sum(sorted_list[0..k-1].w)

Then, for a query rectangle [x1, y1, x2, y2]:

1. Find the start_idx in sorted_list where i >=x1 (bisect_left using (x1, 0)).

2. Find the end_idx in sorted_list where i >x2 (bisect_right using (x2, m+1)).

3. Slice is sorted_list[start_idx : end_idx].

4. Now, within this slice, find the left and right for j:

   a. left_j = bisect.bisect_left([j for (i,j,w) in slice], y1) → but this requires creating a list of j's, which is O(len(slice)) time.

   Alternatively, since the slice is sorted by j, we can use a custom bisect:

   low = 0

   high = len(slice)

   while low < high:

       mid = (low + high) // 2

       if slice[mid][1] >= y1:

           high = mid

       else:

           low = mid + 1

   left_j = low

Similarly for right_j:

   low = 0

   high = len(slice)

   while low < high:

       mid = (low + high) // 2

       if slice[mid][1] > y2:

           high = mid

       else:

           low = mid +1

   right_j = low

This way, no need to create a separate list of j's, but iterate through the slice's elements.

Each bisect is O(log len(slice)) time.

So for each slice (after finding start and end indices), we perform two binary searches (for y1 and y2) taking O(log len(slice)) time.

Once we have left_j and right_j, the sum for this garland is prefix_sum[start_idx + right_j] - prefix_sum[start_idx + left_j].

So the total time per garland is O(log len) for the i range, plus O(log len) for the j range. So O(log len) per garland per query.

Thus, for each ASK query, processing all active garlands would take O(k * log len_avg) time.

With k=2000 and log len_avg=11, that's 22,000 per query. For 2000 queries, 44 million operations, which is manageable in Python.

So this approach seems feasible.

Now, let's outline the steps for the code:

1. Read n, m, k.

2. For each of the k garlands:

   a. Read len, then len lines of (i,j,w).

   b. Sort the garland's bulbs by (i, j).

   c. Compute a prefix sum array for this sorted list.

   d. Store the sorted list and prefix sum array for the garland.

3. Read q events.

4. Maintain an array active_garlands (default True, initial state is all active).

5. For each event:

   a. If it's a SWITCH event, toggle the state of the specified garland.

   b. If it's an ASK event:

      i. Collect x1, y1, x2, y2.

      ii. For each garland, check if active. For active garlands:

          - Use bisect to find the start and end indices in the sorted list for i between x1 and x2.

          - Within that slice, find the left and right indices for j between y1 and y2.

          - Sum the w's in that range using the prefix sum.

      iii. Sum all such contributions and output.

Now, the key is to implement the bisect steps efficiently.

In Python, the bisect module can be used. However, since the sorted_list for each garland is a list of tuples, we need to create a helper function to perform the bisect based on the i and j.

Alternatively, for each garland's sorted list, we can precompute a list of (i,j) and a separate list of w's. But maybe not necessary.

Implementing the i-based bisect:

For a garland's sorted list, each entry is (i, j, w). So to find the first index where i >=x1, we can use bisect.bisect_left with a key. But since bisect doesn't support a key, we can create a dummy list that contains the i's. But that would take O(len) memory per garland. Alternatively, we can use a custom bisect function that works on the i values.

Alternatively, during the bisect, compare the first element of the tuple.

For example, the code for start_idx would be:

start_idx = bisect.bisect_left(g_sorted, (x1, 0, 0), lo=0, hi=len(g_sorted))

But wait, this will find the first tuple where (i,j) >= (x1, 0). But since the sorted list is sorted by i then j, this will correctly find the first entry with i >=x1. However, the j in the dummy entry (x1, 0, 0) doesn't affect since i is compared first.

Similarly, end_idx is bisect.bisect_right(g_sorted, (x2, m+1, 0), lo=0, hi=len(g_sorted)).

Because (x2, m+1) is larger than any possible tuple in the garland's sorted list with i=x2. So bisect_right returns the insertion point after all entries with i <=x2.

So for a garland's sorted list, the code would be:

from bisect import bisect_left, bisect_right

start_idx = bisect_left(g_sorted, (x1, 0, 0))

end_idx = bisect_right(g_sorted, (x2, m+1, 0))

Then, the slice is g_sorted[start_idx:end_idx]

Within this slice, we need to find the left and right indices for j >= y1 and j <=y2.

Since the slice is sorted by i then j, and i is between x1 and x2, the j's in the slice are sorted in ascending order.

So for the slice, we can perform a bisect_left for j >= y1 and bisect_right for j > y2.

But how to perform this in Python.

For the slice, each element is (i,j,w). So the j is element[1].

So to find the left_j in the slice where j >= y1:

left_j = 0

high = len(slice)

while left_j < high:

    mid = (left_j + high) // 2

    if slice[mid][1] >= y1:

        high = mid

    else:

        left_j = mid +1

Similarly, for right_j:

right_j = len(slice)

low =0

while low < right_j:

    mid = (low + right_j) //2

    if slice[mid][1] > y2:

        right_j = mid

    else:

        low = mid +1

Thus, after finding left_j and right_j, the sum is the sum of the w's from start_idx + left_j to start_idx + right_j -1.

Which can be computed using the prefix sum array.

So, the code for each active garland during an ASK query would be:

sum_garland = 0

start_idx = bisect.bisect_left(g_sorted, (x1, 0, 0))

end_idx = bisect.bisect_right(g_sorted, (x2, m+1, 0))

slice = g_sorted[start_idx:end_idx]

# Find left_j and right_j in slice for j in [y1, y2]

left_j = 0

high_j = len(slice)

while left_j < high_j:

    mid = (left_j + high_j) // 2

    if slice[mid][1] >= y1:

        high_j = mid

    else:

        left_j = mid +1

right_j = len(slice)

low_j = 0

while low_j < right_j:

    mid = (low_j + right_j) //2

    if slice[mid][1] > y2:

        right_j = mid

    else:

        low_j = mid +1

sum_garland = g_prefix[start_idx + right_j] - g_prefix[start_idx + left_j]

total_sum += sum_garland

But this requires that for each garland, we have a prefix sum array where g_prefix[i] is the sum of the first i elements in g_sorted.

Yes.

So for example, if the sorted list is [ (i1,j1,w1), (i2,j2,w2), ... ], then the prefix sum is [0, w1, w1 +w2, ... ].

Thus, the sum from index a to index b (exclusive) is prefix[b] - prefix[a].

So in the code:

sum_garland = g_prefix[start_idx + right_j] - g_prefix[start_idx + left_j]

But wait, the slice is from start_idx to end_idx (exclusive). So the slice has end_idx - start_idx elements. The left_j and right_j are indices within the slice. So the actual indices in the global list are start_idx + left_j and start_idx + right_j.

Thus, the sum is prefix[start_idx + right_j] - prefix[start_idx + left_j].

Yes.

Now, let's think about the time.

Each ASK query involves looping through all active garlands. For each garland, the bisect steps take O(log len) time for i and then O(log len_slice) time for j. Since len_slice is up to len (the garland's length), the total is O(log len) per garland.

Thus, for each ASK query, the time is O(k * log len_avg). With k=2000, len_avg=2000, and log2(2000)≈11, that's 2000 * 11 = 22,000 operations per query. For 2000 queries, that's 44 million operations. Which should be manageable in Python.

Now, the code.

First, read the input.

But note that the input is large. So in Python, using sys.stdin.readline and reading all input at once may be more efficient.

But with the constraints, for each garland, reading len lines of i,j,w is manageable.

So steps for code:

Read n, m, k.

For each garland in 0..k-1:

   read len.

   read len lines of i, j, w. (1-based to 0-based? Or keep as 1-based?)

   since the problem statement says the grid is 1-based, but the code can handle 1-based or convert to 0-based. But since the garlands are stored with their original coordinates, which are 1-based, no conversion is needed.

   sort the list of (i, j, w) tuples by i, then j.

   compute prefix sum array.

   store sorted list and prefix sum.

Then, process the events.

But in Python, reading a lot of data with input() can be slow. So it's better to read all input at once.

Thus, the code will use sys.stdin.read() and split it into tokens for faster processing.

Yes.

So code outline:

Testing against sample input 1.

```python
import sys, bisect


def main(input_stream, output_stream):
    data = input_stream.read().split()

    ptr =0

    n = int(data[ptr]); ptr +=1

    m = int(data[ptr]); ptr +=1

    k = int(data[ptr]); ptr +=1

    garlands = []

    for _ in range(k):

        length = int(data[ptr]); ptr +=1

        bulbs = []

        for _ in range(length):

            i = int(data[ptr])

            j = int(data[ptr+1])

            w = int(data[ptr+2])

            ptr +=3

            bulbs.append( (i, j, w) )

        # Sort the bulbs by i, then j.

        bulbs.sort(key=lambda x: (x[0], x[1]))

        # Compute prefix sum.

        prefix = [0]*(len(bulbs)+1)

        for i in range(len(bulbs)):

            prefix[i+1] = prefix[i] + bulbs[i][2]

        garlands.append( (bulbs, prefix) )

    active = [True]*k  # initially all active

    q = int(data[ptr]); ptr +=1

    output = []

    for _ in range(q):

        event = data[ptr]

        if event == 'SWITCH':

            idx = int(data[ptr+1]) -1  # convert to 0-based.

            ptr +=2

            active[idx] = not active[idx]

        elif event == 'ASK':

            x1 = int(data[ptr+1])

            y1 = int(data[ptr+2])

            x2 = int(data[ptr+3])

            y2 = int(data[ptr+4])

            ptr +=5

            total =0

            for garland_idx in range(k):

                if not active[garland_idx]:

                    continue

                bulbs, prefix = garlands[garland_idx]

                # Find start and end indices in bulbs for i in [x1, x2]

                # Using bisect to find left and right.

                # start_idx is first i >=x1

                start_idx = bisect.bisect_left(bulbs, (x1, 0, 0))

                # end_idx is first i >x2

                end_idx = bisect.bisect_right(bulbs, (x2, m+1, 0))

                # slice is bulbs[start_idx:end_idx]

                slice_len = end_idx - start_idx

                if slice_len ==0:

                    continue

                # Now find left_j and right_j in slice where j is between y1 and y2.

                # Binary search for left_j:

                left_j = 0

                high = slice_len

                while left_j < high:

                    mid = (left_j + high) //2

                    if bulbs[start_idx + mid][1] >= y1:

                        high = mid

                    else:

                        left_j = mid +1

                # Binary search for right_j:

                right_j = slice_len

                low =0

                while low < right_j:

                    mid = (low + right_j) //2

                    if bulbs[start_idx + mid][1] > y2:

                        right_j = mid

                    else:

                        low = mid +1

                # Sum from start_idx + left_j to start_idx + right_j -1.

                # The sum is prefix[start_idx + right_j] - prefix[start_idx + left_j]

                sum_garland = prefix[start_idx + right_j] - prefix[start_idx + left_j]

                total += sum_garland

            output.append( str(total) )

        else:

            # invalid event, but problem says input is valid.

            pass

    print('\n'.join(output), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 4 1
8
4 1 1
3 1 2
2 1 1
1 1 7
1 2 5
2 2 4
2 3 1
1 3 1
3
ASK 1 1 3 2
SWITCH 1
ASK 1 1 3 2
""",
            "output": \
"""\
19
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
Traceback (most recent call last):
  File "/workdir/snippet.py", line 212, in <module>
    test()
    ~~~~^^
  File "/workdir/snippet.py", line 205, in test
    assert real_output == expected_output, \
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Test case 0 failed.
Expected: '19\n0'
Got: '18\n0'

```

Wait, but how? The garland's bulbs are placed in a chain where consecutive bulbs are adjacent. So the path can go up, down, left, right, but for a given i, the j's can increase or decrease. So when sorted by i and j, the list would have j in order for the same i. Wait, no. The sorted list is sorted by i first, then j. So for bulbs in the same i, their j's are in ascending order. So in the sorted list, for a given i, the j's are sorted in ascending order. So within the slice for i in [x1, x2], the j's are sorted.

But in the first sample, the third garland's sorted list has i=3, j=2, then 3, then 4. Then i=4, j=1, 2, 3, 4. So for that garland, the j's are sorted for each i.

But in the first garland's sorted list, after i=2, j is 1 and 2, which are in order. Then i=3, j=1. So the j's in the slice [i=2,3] would be 1, 2, 1. Which is not sorted. So the previous approach is incorrect.

Wait, but this is impossible because the sorted list is sorted by i and j. So in the sorted list, for bulbs with i=2, j=1 comes first, then j=2. Then for i=3, j=1. So when sorted, the bulbs are ordered as (2,1), (2,2), (3,1). Thus, within the slice for i between 2 and 3, the j's are 1, 2, 1. Which is not sorted. So the previous approach of treating the j's in the slice as sorted is incorrect.

This is a critical flaw in the approach.

So the assumption that the j's in the slice are sorted is wrong. Because the slice includes multiple i values, the j's can vary.

Thus, the previous approach will not work.

This is a major problem. So the approach of sorting the bulbs by i and j, then assuming that within the slice of i between x1 and x2, the j's are sorted, is incorrect. Because the slice can contain multiple i values, and within each i, the j's are sorted, but between i's, the j's can be in any order.

For example, consider a garland with bulbs:

(2, 1, w1), (2,3, w2), (3, 2, w3). When sorted by i and j, the list is [(2,1, w1), (2,3, w2), (3,2, w3)]. So the slice for x1=2 to x2=3 includes all three bulbs, and the j's are 1,3,2. Which is not sorted.

Thus, the j's in the slice are not sorted. Hence, the binary search approach for j in the slice is incorrect.

Thus, the previous approach is invalid.

This is a critical error. So the previous code would produce incorrect results.

We need a new approach.

Alternative Idea: For each garland, precompute for each bulb its i and j, and build a structure that allows for O(1) lookups whether the bulb is in the query rectangle. But this again requires O(len) per query.

So what can we do now?

Hmm. Let's think differently. Since the problem allows for up to 2000 ASK queries, each with up to 2000 active garlands, and each garland has up to 2000 bulbs, perhaps we can precompute for each garland a 2D array of the cumulative sum within their own bulbs, but this is not feasible.

Another Idea: For each garland, precompute a list of all (i,j,w) entries. For each ASK query, iterate through all active garlands, and for each bulb in the garland, check if it is inside the query rectangle. If yes, add its w to the total sum.

But with 2000 ASK queries, each requiring up to 2000 * 2000 = 4e6 operations, this totals 8e9 operations. Which is way too slow for Python.

But wait, the sample input shows that the first ASK query returns 15. Let's see:

First ASK is 2 2 3 3. So x1=2, y1=2, x2=3, y2=3.

Garland 1 has bulbs in this rectangle:

Looking at their bulbs:

(2,2,1) → yes, in the rectangle.

(3,1,7) → j=1 < 2 → no.

Garland 1 contributes 1.

Garland 2:

bulbs in i=2, j=3 (yes), j=4 (no). So bulb (2,3,3) → included. So sum is 3.

Garland3:

Looking for i between 2 and 3, j between 2 and 3.

Garland3's bulbs:

i=3, j=2,3,4:

j=2 is in [2,3] → w=8.

j=3 is in [2,3] → w=3.

i=4 is outside x range.

So sum is 8+3=11.

Total sum is 1+3+11=15. Which matches the sample.

But in the previous approach, the code for garland 1 would process the slice [(2,1,4), (2,2,1), (3,1,7)] → j's are 1,2,1. So during the binary search for j in [2,3], the code would look for j >=2 and <=3. In the slice:

The j's are 1,2,1. The j's in the slice are not sorted. So binary search would not find the correct j's.

Thus, the code's binary search for j would fail in this case.

Thus, the approach is invalid.

So what's the solution?

We need a different data structure for each garland that allows for efficient querying of the sum in a rectangle.

Alternative Idea: For each garland, precompute a list of all (i,j,w) and store them in a list. Then, for each query, for each active garland, iterate through all bulbs in the garland and check if they are in the query rectangle. This is O(k * len_avg) per query.

For k=2000, len_avg=2000, this is 4e6 per query. For 2000 queries, 8e9 operations, which is too slow in Python.

But perhaps there's a way to optimize this by precomputing for each garland a list of all (i,j,w) and, for each ASK query, precompute the rectangle's bounds and loop through each garland's bulbs.

But in Python, even with 8e9 operations, it's impossible to handle this within the time limit.

Thus, another Idea: For each bulb, store the garland index and its (i,j,w). Then, for each ASK query, iterate through all bulbs in the query rectangle and check if their garland is active. But this requires an efficient way to find all bulbs in the query rectangle. But how?

This would require a 2D range tree or a spatial index that allows efficient querying. But building such a structure for all bulbs is possible.

The total number of bulbs is up to 2000 * 2000 = 4e6. For each bulb, we can store it in a list sorted by i and j. Then, for a query, find the range of i and j, and iterate through those bulbs. But again, this would require O(number of bulbs in the rectangle) per query, which could be up to 4e6 per query, leading to 8e9 operations for 2000 queries. Not feasible.

Alternative Idea: For each cell (i,j), store a list of bulbs (w and garland index) in that cell. Since each cell can have at most one bulb (as per the problem statement), each cell has either zero or one bulb. Thus, for a query rectangle, we can iterate through all cells in the rectangle, and for each cell, if it contains a bulb and the garland is active, add its w to the sum.

But the number of cells in the rectangle can be up to 2000 * 2000 =4e6 per query, leading to 8e9 operations for 2000 queries. Again, not feasible.

But the ASK queries are up to 2000, so 2000 * 4e6 = 8e9 operations. Which is way too slow.

Thus, the only feasible way is to find an approach that allows per garland O(1) or O(log len) time per query.

Another Idea: For each garland, precompute a list of all possible rectangles and their sums. But this is impossible due to the number of possible rectangles.

Alternatively, precompute for each garland the minimum and maximum i and j of its bulbs. Then, for a query rectangle, if the garland's min_i > x2 or max_i <x1 or min_j>y2 or max_j<y1, then it contributes nothing. This allows early pruning.

But even with this, the worst case is still O(k) per query.

Thus, this is not helpful.

Alternative Idea: For each garland, precompute a list of all (i,j,w) and build a prefix sum array sorted by i and j. Then, during a query, use binary search to find the first and last i in [x1, x2], and within that range, the j in [y1, y2], but since j's are not sorted, this is not possible.

Thus, I'm stuck. Maybe I need to think outside the box.

Wait, the problem requires that each ASK query is answered correctly, but the number of ASK queries is small (2000). Meanwhile, the number of SWITCH events is up to 1e6, but each is O(1) to process.

Thus, perhaps we can precompute for each garland and each possible rectangle the sum, but that's impossible. Alternatively, precompute for each garland and each possible ASK query. But since the queries are not known in advance, this isn't feasible.

Alternative Idea: For each ASK query, track all active garlands, and for each, iterate through all their bulbs and check if they are in the rectangle.

But with 2000 ASK queries, each with 2000 garlands active, each with 2000 bulbs, this is 2000 * 2000 * 2000 = 8e9 operations. Which is too slow in Python.

But maybe in practice, it's manageable for the problem's constraints. Let's see: 8e9 operations in Python would take way more than 3 seconds. So it's not feasible.

But the sample inputs suggest that this approach might be manageable for the given constraints. For example, in the first sample, the first ASK query would process 3 active garlands. Each with 5, 4, and 7 bulbs respectively. So 5+4+7=16 checks per query.

But for 2000 queries, this would be 32,000 operations. Which is manageable.

But in the worst case, each ASK query has 2000 active garlands, each with 2000 bulbs, leading to 4e6 operations per query and 8e9 for all queries. Which is way too slow.

But according to the problem statement, the sum of len across all garlands is up to 2000 * 2000 =4e6. So for all ASK queries, the total number of operations would be 2000 * 4e6 =8e9, which is way too slow.

Thus, this approach is not feasible.

So what's the correct approach?

The correct approach must leverage the fact that the number of ASK queries is small (2000). So precompute for each garland a 2D array, but this is impossible due to memory.

Another Idea: For each garland, precompute a list of (i,j,w) and build a 2D prefix sum array, but only for the specific garland's bulbs. This way, each garland's prefix sum is a sparse matrix.

Wait, but how? For example, for each garland, the prefix sum would be a list of their bulbs sorted by (i,j), and for any rectangle, the sum can be computed as the sum of all bulbs in the rectangle.

This brings us back to the initial approach, but the problem is that the j's in the slice are not sorted. So the previous approach's binary search for j is invalid.

But what if we preprocess each garland into a structure where for each i, the j's are sorted and have a prefix sum?

Yes. This would allow for each garland to have a dictionary mapping i to a list of (j, w), sorted by j, and a prefix sum array for each i's list.

For example, for each garland:

row_dict = defaultdict(list)

for bulb in garland:

    i, j, w = bulb

    row_dict[i].append( (j, w) )

for each i in row_dict:

    sort the list of (j, w) by j.

    compute a prefix sum array for this list.

Then, for a query rectangle [x1, y1, x2, y2], the sum for the garland is the sum over i from x1 to x2 of the sum of w in row_dict[i] where j is between y1 and y2.

For each i in x1 to x2:

   if i is not in row_dict, skip.

   else, for the list of (j, w) in row_dict[i], sorted by j, find the indices where j is between y1 and y2.

   sum the corresponding w's using the prefix sum array.

This way, each garland's contribution is O( (x2 -x1 +1) * log len_i ), where len_i is the number of j's in row i.

But x2 -x1 +1 can be up to 2000, which for 2000 active garlands and 2000 queries, leads to 2000 * 2000 * 2000 = 8e9 operations. Which is again too slow.

But perhaps, for each garland, the number of rows that have bulbs is small. For example, if a garland is a single row, then for a query covering many rows, this approach would not help.

But this seems like the only feasible way.

Thus, the code would:

For each garland, build a row_dict where for each row i, there's a list of (j, w) sorted by j, and a prefix sum array.

Then, for each ASK query:

for each active garland:

   sum_garland = 0

   for i in x1 to x2:

       if i not in row_dict:

           continue

       j_list = row_dict[i]  # sorted by j.

       prefix = prefix_dict[i]

       # find left and right in j_list for y1 and y2.

       left = bisect.bisect_left(j_list, (y1, 0))  # using j as the key.

       right = bisect.bisect_right(j_list, (y2, float('inf')) )

       sum_garland += prefix[right] - prefix[left]

   total += sum_garland

But in Python, for each garland and each row in x1 to x2, this would take O(1) to check if i is in the row_dict, and O(log len_i) to compute the sum.

The problem is that x1 to x2 can be up to 2000 rows. For each garland, even if row_dict has entries for all rows, this would be O(2000) per garland per query. For 2000 garlands and 2000 queries, that's 2000 * 2000 * 2000 = 8e9 operations. Which is too slow.

But if the garland's row_dict is sparse, this could be manageable. For example, if each garland's row_dict has only 2000 entries (rows), then for a query spanning all rows, this would be 2000 iterations per garland per query. Which is again too slow.

Thus, this approach is also not feasible.

So what's left?

Given the time constraints, perhaps the intended solution is to use the initial approach but use 4 binary searches per garland per query.

Wait, perhaps the initial approach can be fixed. Because in the initial approach, the j's in the slice are not sorted. So the binary search approach for j is incorrect.

But maybe the bulbs in the garland are sorted by i and j. So in the garland's sorted list, for each bulb, i is non-decreasing, and for bulbs with the same i, j is non-decreasing.

Yes. Because the bulbs are sorted by (i, j), so the j's for bulbs in the same i are in non-decreasing order.

Thus, when we have a slice of bulbs with i between x1 and x2, the bulbs are sorted by i and j. Thus, within the slice, the i's are in non-decreasing order. However, when i changes from x to x+1, the j's can be in any order. So the entire slice is sorted by i and j, but for the entire slice, the j's are not sorted. However, for each individual i in the slice, the j's are sorted.

So, to find all bulbs in the query rectangle [x1, y1] to [x2, y2], we need to consider all bulbs in the slice (i between x1 and x2) and j between y1 and y2.

But since the entire slice is sorted by i and j, and j is sorted within each i, the j's in the entire slice are not necessarily sorted. So the previous approach of binary searching the entire slice for j is incorrect.

But how to handle this?

Alternative Idea: For each garland's sorted list, during a query, iterate through each i in the slice and perform a binary search on the j's for that i.

But this requires knowing which i's are present in the slice and their ranges.

But the slice is a sorted list of (i, j, w), sorted by i and j. So the slice is a contiguous block of the sorted list. For each i in the slice, all bulbs with i=current_i are consecutive in the list.

Thus, the slice is a sorted list, and within it, all bulbs with i=x1 are first, then i=x1+1, etc. For each i in x1 to x2, the j's are sorted.

Thus, the slice can be divided into groups of bulbs with the same i. For each group, the j's are sorted. Thus, for each i group in the slice, perform a binary search for j in [y1, y2].

But how to split the slice into i groups?

The sorted list is ordered by i and j. So all bulbs in the same i are grouped together in the list. Thus, in the slice, the bulbs are grouped by i.

For example, the slice could be:

i=2, j=1

i=2, j=2

i=3, j=1

Thus, the groups are [i=2, j=1], [i=2, j=2], and [i=3, j=1].

So during the query, for each group of i in the slice, we can find the j range and sum the corresponding w's.

But how to find the groups of i in the slice?

The slice is a contiguous part of the sorted list. Thus, the i's in the slice are non-decreasing. So the groups are contiguous ranges in the slice.

Thus, to process the slice, we can iterate through the slice and group by i. For each group with i between x1 and x2, process the j's.

But this approach would take O(len(slice)) per garland per query, which is again O(len_avg) per garland per query. Which is not feasible for large len_avg.

But this seems like the only correct approach.

Thus, the correct code would:

For each garland's sorted list:

1. Find the start and end indices for i between x1 and x2.

2. Iterate through the slice, grouping the bulbs by i.

3. For each group of bulbs with i = current_i:

   a. Check if current_i is within x1 and x2.

   b. The j's are sorted, so perform a binary search to find the range of j's in [y1, y2].

   c. Sum the w's for those j's.

But this requires iterating through the entire slice for each garland per query, which is O(len(slice)) per garland per query. Which is again O(len_avg) time.

But if the average len is 2000, and k is 2000, this is 4e6 operations per query. For 2000 queries, 8e9 operations. Which is way too slow.

Thus, this problem requires a different approach.

After struggling, perhaps the correct approach is to realize that each cell contains at most one bulb. Thus, for each cell, we can track which garland's bulb is present and its w. Then, during ASK queries, iterate through each cell in the rectangle and check if the garland is active.

But the number of cells in the rectangle can be up to 2000*2000=4e6 per query, leading to 8e9 operations for 2000 queries.

But this is not feasible.

Thus, the problem requires a way to precompute for each garland a data structure that allows O(1) or O(log len) time per query.

The correct approach is to use the initial idea, but with a mistake in the binary search for j's. However, perhaps the mistake can be fixed.

Wait, in the initial approach, the j's in the slice are not sorted, but the code assumes they are. Thus, the code would not correctly find the j's in the query rectangle.

Thus, the code is incorrect.

But how to handle this?

Another Idea: For each garland's sorted list, during preprocessing, create for each bulb a tuple (i, j), sorted by i and j. Then, for a query, find the start and end indices for i between x1 and x2. Then, within that slice, the j's are not sorted, so we need to iterate through each bulb in the slice and check if j is between y1 and y2.

This approach would take O(len(slice)) per garland per query. Which is O(len_avg) per garland per query.

But for 2000 active garlands and 2000 queries, this is 8e9 operations. Which is too slow.

Thus, this problem is very challenging.

But according to the sample input, the correct answer is obtained when considering all active garlands and summing the bulbs in the query rectangle.

Perhaps the only feasible way in Python is to precompute for each garland a list of (i, j, w), and for each ASK query, iterate through all active garlands and their bulbs, checking if they are in the query rectangle.

But given the time constraints, this approach is not feasible for the worst case, but perhaps the problem has len for garlands that are small, or the ASK queries are not worst-case.

But the problem's constraints state that len can be up to 2000, and ASK queries can be 2000.

Thus, the correct approach must be to use the initial idea but with the correct binary search.

But how?

Wait, perhaps the initial mistake was in assuming that the slice includes all bulbs with i >=x1 and <=x2. But in reality, the sorted list is sorted by i and j, so the slice will have all bulbs in i between x1 and x2, and within those, the j's are sorted for each i.

But how to process the j's in each i group?

For example, in the first sample garland, the slice for x1=2, x2=3 includes:

i=2, j=1 → (2,1,4)

i=2, j=2 → (2,2,1)

i=3, j=1 → (3,1,7)

The j's for i=2 are 1 and 2 (sorted), and for i=3, j=1.

Thus, within each i group, the j's are sorted. So for each i group, we can perform a binary search on the j's.

But how to find the i groups in the slice.

The slice is a sorted list of (i, j, w). So, the groups are consecutive entries with the same i. For example, in the slice, the first two entries are i=2, j=1 and j=2, then i=3.

Thus, the code can iterate through the slice and process each group of bulbs with the same i.

For each group:

- Check if i is between x1 and x2 (which it is, by construction).

- For the j's in this group, perform a binary search to find the range [y1, y2].

But how to split the slice into groups of the same i.

This can be done by iterating through the slice and grouping by i.

For example:

current_i = None

current_group = []

for bulb in slice:

    if bulb[0] != current_i:

        if current_i is not None:

            process current_group

        current_i = bulb[0]

        current_group = [bulb]

    else:

        current_group.append(bulb)

process current_group

But this iteration takes O(len(slice)) time per garland per query. Which is again O(len_avg) time.

But len_avg is up to 2000. For 2000 active garlands and 2000 queries, this is 8e9 operations. Which is not feasible.

Thus, the problem is very difficult.

After struggling for a long time, I think the correct approach is to use the initial code but with the realization that the j's in the slice are not sorted. Therefore, the code would be incorrect. But given the time constraints, perhaps the problem expects this approach, even though it's incorrect in some cases.

But the sample input demonstrates that the code would fail.

Alternatively, perhaps the problem has a mistake in the way the garlands are described, and the j's in the sorted list for the slice are actually sorted. But this is not the case.

Thus, I'm stuck. Perhaps the correct approach is to realize that the garland's path is contiguous, and thus, the sorted list by i and j will have j's in order for each i.

But this is not necessarily true. For example, a garland can have i=2, j=3, then i=3, j=2, then i=3, j=3. So in the sorted list, the j's for i=3 are 2 and 3, which is sorted.

Yes! Because when sorted by i and j, the j's for each i are in ascending order. Thus, within the slice (i between x1 and x2), the j's for each i are in sorted order. But the j's for different i's can vary.

Thus, the code can process each i group in the slice, and for each, perform a binary search on the j's.

But how to split the slice into i groups?

The slice is sorted by i and j, so all bulbs with the same i are grouped together. Thus, the code can iterate through the slice and for each i group, process the j's.

But this requires iterating through the slice, which is O(len(slice)) time per garland per query. Which is not feasible for large len(slice).

But perhaps the code can be optimized by finding the first and last occurrence of each i in the slice.

But this is not possible without iterating through the slice.

Thus, I think the correct approach is to use the initial code but with the mistake in handling the j's. But in the sample input, the code would give the correct result.

Wait, in the first sample's garland 1:

The slice is bulbs[2:5], which includes:

(2,1,4), (2,2,1), (3,1,7).

For the query j between 2 and 3.

So for this slice:

left_j is the first j >=2.

The j's in the slice are 1, 2, 1.

So binary search for j >=2.

The code would do:

left_j =0

high_j =3

mid = (0+3)/2=1.

slice[1][1] is 2 >=2 → high_j =1.

mid = (0+1)/2=0. slice[0][1] is 1 <2 → left_j=1.

loop ends, left_j is 1.

right_j is looking for j >3. The j's are 1, 2, 1. All are <=3 → right_j=3.

sum_garland = prefix[start_idx +3] - prefix[start_idx +1] → prefix[2+3=5] - prefix[2+1=3] → prefix[5] is 10 (from the sample's first garland's prefix array), prefix[3] is 5. So 10-5=5.

But the correct sum for garland 1 is 1 (only (2,2,1) is in the rectangle). So the code returns 5, which is incorrect.

Thus, the code is wrong.

Thus, the initial approach is invalid.

Thus, the correct approach is to process each bulb in the slice and check if j is in [y1, y2]. But this is O(len(slice)) per garland per query.

But how else?

Thus, the correct code would be:

For each active garland:

sum_garland = 0

start_idx = bisect_left(g_sorted, (x1, 0, 0))

end_idx = bisect_right(g_sorted, (x2, m+1, 0))

for bulb in g_sorted[start_idx:end_idx]:

    if bulb[1] >= y1 and bulb[1] <= y2:

        sum_garland += bulb[2]

total_sum += sum_garland

But this code is O(len(slice)) per garland per query. Which is again O(k * len_avg) per query.

But for k=2000 and len_avg=2000, this is 4e6 per query, leading to 8e9 operations for 2000 queries. Which is too slow for Python.

Thus, I'm stuck. Perhaps there's a way to precompute for each garland a 2D prefix sum array. But this requires storing n*m entries per garland, which is 2000*2000=4e6 per garland. With k=2000, this is 8e9 entries, which is not feasible.

Thus, the only possible way is to use the initial approach but with a mistake, but given that the problem's test cases may not trigger the error, or there's a different way to model the problem.

But according to the problem statement, the bulbs are part of a chain where consecutive bulbs are adjacent. Thus, the path is a connected sequence of cells. But this doesn't help in the data structure.

After a long time of thinking, I think the correct solution is to use the initial approach but process each bulb in the slice and check j. This is O(len(slice)) per garland per query. But given the constraints of 2000 ASK queries and 2000 active garlands, but the sum of all bulbs is 4e6, this would take 4e6 * 2000 = 8e9 operations. Which is too slow.

But perhaps the problem's constraints are designed to allow this approach. For example, the sum of len across all garlands is 4e6, and for 2000 ASK queries, the total operations would be 4e6 * 2000 = 8e9. But in practice, Python can't handle this.

But the problem's time limit is 3 seconds. In Python, even 1e8 operations take around 10 seconds, so 8e9 is impossible.

Thus, there must be another approach.

Alternative Idea: Precompute for each garland a list of (i,j,w) and build a 2D prefix sum for the entire grid. For each garland, the 2D prefix sum allows querying the sum of the garland's bulbs in a rectangle in O(1) time. For each garland, this requires O(nm) memory. But with n and m up to 2000, and k up to 2000, this is 2000*2000*2000=8e9 entries. Which is impossible.

But perhaps each garland's bulbs are sparse, so using a sparse prefix sum. For example, a dictionary where for each (i,j) we store the sum up to (i,j). But for each garland, this is O(len) space.

But then, how to query the sum for a rectangle. For example, for a garland's prefix sum, the sum in the rectangle is the sum of all bulbs in the rectangle. But without a 2D structure, this is not possible.

Thus, this is not feasible.

Thus, after trying various approaches and not finding a feasible solution, I think the correct approach is to use the initial code, but due to time constraints, proceed with that code and see if it passes the sample test cases.

But in the first sample, the code will fail.

But the sample input's first ASK query returns 15. The code for garland 1:

sum_garland is 5-5=0. Because start_idx is 2, end_idx is 5. slice is bulbs[2:5], which is:

(2,1,4), (2,2,1), (3,1,7)

left_j is 1 (since j >=2 is 2 at index 1 in the slice), right_j is 2 (j <=3 is 2, j=1 is excluded). So sum is prefix[2+2] - prefix[2+1] = prefix[4] - prefix[3] = 10-5=5.

Garland 2's sum is 3 (the bulb (2,3,3) is in the slice). Garland3's sum is 8+3=11. So total is 5+3+11=19. But the sample output is 15. So the code is incorrect.

Thus, the code is wrong.

Thus, the only correct approach is to process each bulb in the slice and check if j is in the query's j range. Which is O(len(slice)) per garland per query.

But how to do this efficiently in Python.

Thus, the code would be:

For each active garland during an ASK query:

sum_garland = 0

start_idx = bisect_left(g_sorted, (x1, 0, 0))

end_idx = bisect_right(g_sorted, (x2, m+1, 0))

for bulb in g_sorted[start_idx:end_idx]:

    if bulb[1] >= y1 and bulb[1] <= y2:

        sum_garland += bulb[2]

total += sum_garland

This code would work correctly, but is it fast enough?

With 4e6 bulbs in total and 2000 ASK queries, this is 8e9 operations. Which is impossible.

But perhaps the sum of len across all garlands is 4e6, but the number of bulbs in each slice for each query is small. For example, if each query's slice has 100 bulbs per garland, then 2000 * 2000 * 100 = 4e8 operations. Which is manageable.

But this depends on the queries.

Thus, the correct code would be this approach.

But how to optimize it in Python.

In Python, list comprehensions and generator expressions are faster than explicit for loops. So the code can be written as:

sum_garland = sum(w for i, j, w in g_sorted[start_idx:end_idx] if y1 <= j <= y2)

This may be more efficient.

Thus, the code would be:

for garland_idx in range(k):

    if not active[garland_idx]:

        continue

    bulbs, prefix = garlands[garland_idx]

    start_idx = bisect.bisect_left(bulbs, (x1, 0, 0))

    end_idx = bisect.bisect_right(bulbs, (x2, m+1, 0))

    sum_garland = sum(w for (i,j,w) in bulbs[start_idx:end_idx] if y1 <= j <= y2)

    total += sum_garland

This code is correct but may be too slow for large inputs.

But given that the problem's ASK queries are up to 2000, and the sum of len across all garlands is 4e6, this code would process 4e6 * 2000 = 8e9 operations. Which is impossible in Python.

But perhaps the problem's actual test cases have len_avg much smaller than 2000, or the queries are such that the slices are small.

Thus, this is the correct approach, and the code must be written in this way.

But the code will not pass the sample input.

In the first sample:

Garland 1's slice for the first ASK query (2,2,3,3):

bulbs[start_idx:end_idx] is bulbs[2:5] → [(2,1,4), (2,2,1), (3,1,7)].

sum_garland for this garland is sum(w where j is between 2 and3 → only (2,2,1) contributes. Sum is 1.

Garland 2's slice is bulbs[0:4] → i between 2 and 3. Their bulbs are [(1,3,1), (1,4,1), (2,3,3), (2,4,3)].

i ranges from 1 to 2, but x1=2. So start_idx is bisect_left for i >=2. Which is index 2 (bulbs[2] is (2,3,3). end_idx is bisect_right for i <=3. bulbs[2:4] is [(2,3,3), (2,4,3)].

sum is j >=2 and <=3 → (2,3,3) → sum is 3.

Garland3's slice: x1=2, x2=3. The sorted list for garland3 is [(3,2,8), (3,3,3), (3,4,1), (4,1,1), (4,2,9), (4,3,4), (4,4,1)].

start_idx is bisect_left for (2,0,0) → 0, since the first bulb is i=3.

end_idx is bisect_right for (3,5,0) → 3 (bulbs up to i=3 are the first three). slice is bulbs[0:3] → [(3,2,8), (3,3,3), (3,4,1)]. j between 2 and3 → 8 and 3 → sum 11.

Total sum is 1+3+11=15. Which matches the sample.

Thus, the code with the sum of bulbs in the slice where j is in the range is correct.

Thus, the correct approach is to iterate through the bulbs in the slice and check j.

Thus, the code must be written as follows.

The final code would be:

import sys, bisect

def main():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr]); ptr +=1
    m = int(data[ptr]); ptr +=1
    k = int(data[ptr]); ptr +=1

    garlands = []
    for _ in range(k):
        length = int(data[ptr]); ptr +=1
        bulbs = []
        for _ in range(length):
            i = int(data[ptr])
            j = int(data[ptr+1])
            w = int(data[ptr+2])
            ptr +=3
            bulbs.append( (i,j,w) )
        bulbs.sort()
        garlands.append( bulbs )
    
    active = [True]*k
    q = int(data[ptr]); ptr +=1
    output = []
    for _ in range(q):
        if data[ptr] == 'SWITCH':
            idx = int(data[ptr+1])-1
            active[idx] = not active[idx]
            ptr +=2
        else:
            ptr +=1
            x1 = int(data[ptr]); ptr +=1
            y1 = int(data[ptr]); ptr +=1
            x2 = int(data[ptr]); ptr +=1
            y2 = int(data[ptr]); ptr +=1
            total =0
            for garland_idx in range(k):
                if not active[garland_idx]:
                    continue
                bulbs = garlands[garland_idx]
                start = bisect.bisect_left(bulbs, (x1,0,0))
                end = bisect.bisect_right(bulbs, (x2, m+1, 0))
                total += sum(w for i,j,w in bulbs[start:end] if y1 <= j <= y2)
            output.append(str(total))
    print('\n'.join(output))

if __name__ == "__main__":
    main()
</think>

```python
import sys
import bisect

def main():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr]); ptr += 1
    m = int(data[ptr]); ptr += 1
    k = int(data[ptr]); ptr += 1

    garlands = []
    for _ in range(k):
        length = int(data[ptr]); ptr += 1
        bulbs = []
        for _ in range(length):
            i = int(data[ptr])
            j = int(data[ptr+1])
            w = int(data[ptr+2])
            ptr += 3
            bulbs.append((i, j, w))
        bulbs.sort()
        garlands.append(bulbs)
    
    active = [True] * k
    q = int(data[ptr]); ptr += 1
    output = []
    for _ in range(q):
        if data[ptr] == 'SWITCH':
            idx = int(data[ptr+1]) - 1
            active[idx] = not active[idx]
            ptr += 2
        else:
            ptr += 1  # Skip 'ASK'
            x1 = int(data[ptr]); ptr += 1
            y1 = int(data[ptr]); ptr += 1
            x2 = int(data[ptr]); ptr += 1
            y2 = int(data[ptr]); ptr += 1
            total = 0
            for garland_idx in range(k):
                if not active[garland_idx]:
                    continue
                bulbs = garlands[garland_idx]
                start = bisect.bisect_left(bulbs, (x1, 0, 0))
                end = bisect.bisect_right(bulbs, (x2, m + 1, 0))
                total += sum(w for i, j, w in bulbs[start:end] if y1 <= j <= y2)
            output.append(str(total))
    print('\n'.join(output))

if __name__ == "__main__":
    main()
```
