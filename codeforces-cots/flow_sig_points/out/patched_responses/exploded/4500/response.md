<think>
Okay, so I need to solve this domino problem. Let me read the problem carefully. The task is, for each domino when pushed to the right, determine how many dominoes will fall. The dominoes are arranged along an axis, and each has a coordinate xi and height hi. When a domino falls, it affects the interval from x+1 to x + h -1. Any domino in that interval (strictly above the base) will be knocked over as well, and their effect is added. So this is a chain reaction.

Hmm. The key here is to model the chain reaction efficiently. Since each domino can trigger others, and each of those can trigger their own, the naive approach of simulating each push would be too slow for n up to 1e5. We need an O(n) or O(n log n) approach.

Let's think about the dominoes sorted by their x coordinates. Because the dominoes are arranged along the axis, the order in which they are knocked over when pushed depends on their positions. If domino A is to the left of domino B, pushing A might affect B, but pushing B can't affect A if they are in order. Wait, no. If the dominoes are sorted, then when you push domino i, the effect can only go to the right. Because the domino is pushed to the right, so the interval it affects is [xi+1, xi+hi-1]. So any domino with xj >= xi+1 and <= xi+hi-1 will be hit. And those dominoes, when they fall, will have their own intervals. So the total dominoes that fall is the number in the union of all intervals from the initial domino and the subsequent ones.

But how to model this efficiently?

This seems similar to the interval covering problem. For each domino i, when it falls, it can affect dominoes in its interval, and those dominoes will in turn affect their own intervals. But the challenge is to precompute for each domino the maximum reach to the right. Because once a domino i is pushed, the reach would be the maximum of xi + hi -1 and the reach of all dominoes that fall in between.

Wait, perhaps for each domino i, we can precompute the farthest right position that the chain reaction starting at i would reach. Then, for domino i, the number of dominoes that fall is the number of dominoes between i and the farthest domino that is within the chain.

But how to compute this efficiently?

Let me think. If the dominoes are sorted by x in increasing order, then for domino i, when it's pushed, it affects dominoes from i+1 to some j where xj is <= (xi + hi -1). Then, each of those dominoes in that range may extend the reach. For example, domino i+1 may have a reach of x_{i+1} + h_{i+1} -1, which could be further than xi + hi -1. So the maximum reach is the maximum of all such values in the affected dominoes.

This sounds like a dynamic programming problem. For each domino i, the maximum reach is max(xi + hi -1, reach[i+1], reach[i+2], ..., reach[j], where j is the farthest domino initially hit by i). But how to compute this efficiently.

If the dominoes are sorted, then for each i, we can compute the maximum reach in a way that allows us to reuse previous computations. Let's process the dominoes from right to left. For domino i, when we process it, all dominoes to the right (i+1, i+2, etc.) have already been processed. So for domino i, the initial reach is xi + hi -1. But if the next domino (i+1) is within this reach, then the reach for i is the maximum of its initial reach and the reach of i+1. But wait, what if domino i+1's x is beyond xi+hi-1? Then it's not hit, so the reach is just the initial. But if i+1 is hit, then the reach for i is the max between the initial reach and the reach of i+1. But what if domino i+1's reach is even larger, but domino i+1's x is within the initial reach? Then domino i's reach will be domino i+1's reach. Then domino i+2 and beyond would be considered if they are within domino i's reach.

Wait, perhaps the optimal approach is to process the dominoes in reverse order. For each domino i (starting from the rightmost), we can compute the farthest reach as follows:

- The initial reach is x_i + h_i - 1.

- Then, we check the next domino (i+1, but since we're processing from the right, i+1 is to the left of i. Wait, no. Wait, when sorted, dominoes are in increasing order of x. So the rightmost domino is the last in the array. So processing from the right (starting with the last domino) and moving left. So for each i (right to left), the next domino to the right (i+1 in the array) has a higher x coordinate.

Wait, no. If the dominoes are sorted in increasing order of x, then domino 0 is leftmost, domino n-1 is rightmost. So when processing from right to left, for domino i (array index i), the next domino to the right is i+1 (but if i is the rightmost, then there is no i+1). Wait, no, the sorted order is such that x0 < x1 < ... < xn-1. So when i is the rightmost (n-1), there are no dominoes to the right. Then, domino i-1 is to the left of i.

So processing from right to left: for each domino i (starting at n-1), compute the farthest reach. The reach of domino i is max(xi + hi -1, reach[i+1]) if there's a domino to the right (i+1) that is within the initial reach. But how to find which dominoes are in the initial reach of i?

Wait, perhaps for domino i, after the initial reach, any domino j where xj is <= reach_i_initial would be hit. But domino j may have a reach that extends further. So the maximum reach for domino i is the maximum between reach_i_initial and the reach of the first domino to the right of i, but only if that domino is within reach_i_initial.

Wait, but the dominoes are sorted. So if i is processed in reverse order, then for domino i, the reach can be computed as follows:

The initial reach is xi + hi -1. Then, the dominoes to the right (i+1, i+2, etc.) are in x order. So the first domino to the right is i+1. If x_{i+1} is <= reach_i_initial, then domino i+1 is hit. Then the reach of domino i would be the maximum of reach_i_initial and the reach of i+1. But domino i's reach is the maximum of all reach of dominoes that are hit by the chain starting at i. So perhaps the reach of i is the maximum between xi + hi -1 and the reach of the next domino that is in the initial interval. But how to find the next domino that's beyond the initial reach.

Alternatively, since the dominoes are sorted, for domino i, the dominoes that are hit by it are those from i+1 up to j, where j is the largest index such that xj <= xi + hi -1. So the maximum reach for domino i is the maximum between xi + hi -1 and the maximum reach of all dominoes from i+1 to j. But how to compute this efficiently.

Wait, but if we process the dominoes from right to left, then for domino i, any domino j >= i+1 that is within the initial reach of i's interval will have their reach already computed. So for domino i, the reach would be the maximum between its initial reach and the reach of the first domino in the interval. But that's not sufficient. For example, domino i's initial reach may include multiple dominoes, each of which may have their own reach. The maximum reach would be the maximum of all these dominoes' reaches and the initial.

But how to find the maximum in the range [i+1, j], where j is the maximum index where xj <= xi + hi -1. Since the dominoes are sorted, j can be found via binary search. Once j is found, we need the maximum reach in the interval i+1 to j. Then, the reach for i is the maximum between its initial reach and this maximum.

If we can precompute for each i the maximum reach in the range from i to j, then we can compute this quickly. But for that, we need a data structure that allows range maximum queries in O(1) or O(log n) time. But since we are processing the dominoes in reverse order, perhaps we can keep track of the maximum as we go.

Alternatively, since we process dominoes from right to left, for each i, once we find j (the rightmost domino within the initial reach of i), the maximum reach for i is the maximum between xi + hi -1 and the maximum reach in the dominoes from i+1 to j.

But how to find that maximum. One approach is to use a segment tree or a sparse table for range maximum queries. Then, once j is found, we can query the maximum in O(log n) time. However, building a sparse table for 1e5 elements is feasible, and each query is O(1). Then, the total time would be O(n log n), which is acceptable.

So the steps could be:

1. Sort the dominoes by their x-coordinates in increasing order.

2. For each domino i, compute the initial reach as x_i + h_i - 1.

3. Precompute a sparse table for range maximum queries on the reach array.

4. Process dominoes from right to left (i from n-1 down to 0):

   a. Find j, the largest index where x_j <= (x_i + h_i -1).

   b. If j <= i, then domino i's reach is its initial reach. The count is 1.

   c. Otherwise, the maximum reach in the interval [i+1, j] is obtained via the sparse table.

   d. domino i's reach is max(initial_reach, max_reach_in_interval). 

   e. Then, the number of dominoes that fall is the number of dominoes from i to the index where x is <= i's reach. Wait, no. Because the reach is the maximum x covered. So the count is the number of dominoes from i to k, where x_k is <= the reach of i. But how to compute that?

Wait, perhaps the reach for i is the maximum x that can be covered by pushing i. Then, the number of dominoes that fall is the number of dominoes from i to the rightmost domino whose x is <= the reach of i. Because dominoes are sorted, so once reach is known, we can binary search to find the rightmost x in the sorted list that is <= the reach. The count is (rightmost_idx - i + 1).

But how to compute that.

Wait, for each domino i, after computing the reach, we can find how many dominoes are in the interval from x_i to reach[i]. Because dominoes are sorted, this can be done via binary search. The rightmost index is the maximum j where x_j <= reach[i]. Then, the count is j - i + 1.

But that would require for each i, two binary searches: one when computing j during the reach step, and another to compute the count. Hmm. But perhaps there's a way to compute the count during the same step.

Alternatively, perhaps the reach array can directly give us the maximum x covered, and then for each i, the number of dominoes is the number of dominoes from i to the largest j where x_j <= reach[i].

So here's the plan:

Sort the dominoes by x in increasing order.

For each i, precompute the reach as follows:

Processing from right to left.

For i = n-1 down to 0:

   reach[i] = x[i] + h[i] - 1.

   find the maximum j where x[j] <= reach[i].

   if j > i:

       reach[i] = max(reach[i], the maximum reach in [i+1, j])

       (this is done via the sparse table)

   Then, the count for i is the number of dominoes from i to the j where x[j] <= reach[i]. But how to find j again?

Wait, perhaps during the processing of reach[i], we can track not only the maximum reach but also the farthest index. Wait, but the reach[i] is the maximum x that can be covered. So once we have reach[i], the number of dominoes is the number of dominoes in the interval x_i to reach[i]. So after sorting, the rightmost index for i is the maximum j where x_j <= reach[i]. Then, the count is j - i + 1.

So for each i, the steps are:

1. Compute the initial reach (x_i + h_i -1).

2. Find j where x_j is the maximum <= initial reach.

3. If j > i, then the reach of i is max(initial_reach, max_reach of i+1 to j).

   So the max_reach is obtained by querying the sparse table for the range [i+1, j].

4. Then, after reach[i] is determined, the final j is the maximum index where x_j <= reach[i], and the count is j -i + 1.

But this approach requires for each i, two binary searches: once during step 2 (to find j for initial reach), and another after reach[i] is computed (to find the final j for the count). But that's O(n log n) time, which is acceptable.

But wait, how is the reach[i] computed? Let me think again.

The problem is that the reach[i] is the maximum x that is covered by pushing domino i. So after processing i, the reach[i] is the maximum between x_i + h_i -1 and the reach of the dominoes in the initial interval.

So when processing i from right to left:

For i, the initial reach is x_i + h_i -1. The dominoes that are hit by i's initial reach are from i+1 to j_initial, where j_initial is the largest index with x_j <= initial_reach.

If j_initial > i, then the reach of i will be the maximum between initial_reach and the maximum reach of the dominoes in [i+1, j_initial].

But to find that maximum, we can use a segment tree or a sparse table. Then, we can update reach[i] accordingly.

Once reach[i] is determined, the count is the number of dominoes from i to j_final, where j_final is the largest index with x_j <= reach[i].

So the steps for each i are:

1. Compute initial_reach = x_i + h_i -1.

2. Find j_initial via binary search (the rightmost index where x_j <= initial_reach).

3. If j_initial <= i: then reach[i] is initial_reach, and j_final is i. So the count is 1.

4. Else:

   a. Find the maximum reach in the interval [i+1, j_initial]. Let's call this max_reach_interval.

   b. reach[i] = max(initial_reach, max_reach_interval)

   c. Then, find j_final via binary search as the rightmost index <= reach[i].

5. The count for i is j_final - i + 1.

But how to compute max_reach_interval quickly. Here, a sparse table for range maximum query can help. Since we're processing the dominoes from right to left, when processing i, all j >= i have their reach already computed. So the reach array is filled from the end towards the start. Thus, the sparse table can be built once, after all reach values are computed, but that's not possible. Wait, no. Because processing is done right to left. So for i from n-1 downto 0:

   For each i, compute reach[i], and then add it to the sparse table. Wait, but building a sparse table incrementally is not feasible. So perhaps a better approach is to precompute a sparse table once all reach values are computed. But in this scenario, since the reach[i] for i depends on the reach of higher indices, which are processed first, we can compute reach[i] in reverse order, and then after processing all reach[i], build a sparse table for range maximum queries.

Wait, but that would require building the sparse table after all reach[i] are computed, which is possible. Let me see.

But the problem is that when processing i, we need to compute the maximum reach in the interval [i+1, j_initial]. But if the reach array is being filled from right to left, then when processing i, all reach[j] for j > i are already known. So for example, when i is processed, the reach[i+1] to reach[j_initial] are already computed. So we can build a sparse table as we go, or perhaps use a segment tree that allows for range maximum queries in O(log n) time. But building a segment tree dynamically as we process the elements is possible.

Alternatively, since the processing is done from right to left, and the queries are for ranges [i+1, j_initial], which are to the right of i, which have already been processed, we can use a binary indexed tree (Fenwick tree) for range maximum queries. However, binary indexed trees are more suited for prefix maxima rather than arbitrary ranges. So perhaps a segment tree would be better here.

But considering the time constraints, for n=1e5, a segment tree with O(n) build time and O(log n) per query would be feasible. So here's the plan:

1. Sort the dominoes by x in increasing order.

2. For each domino, compute x_i and h_i.

3. Precompute the sorted x array.

4. Precompute for each i, the initial_reach = x_i + h_i - 1.

5. Create a segment tree that can query the maximum reach in a range [l, r].

6. Process the dominoes in reverse order (from i = n-1 downto 0):

   a. Compute initial_reach for i.

   b. Find j_initial via binary search (the largest index where x[j] <= initial_reach).

   c. If j_initial <= i:

       reach[i] = initial_reach

       count[i] = 1

   d. Else:

       query the segment tree for the maximum reach in [i+1, j_initial]. Let this be max_reach.

       reach[i] = max(initial_reach, max_reach)

       then, find j_final via binary search (largest index where x[j] <= reach[i])

       count[i] = j_final - i + 1

   e. Update the segment tree with reach[i] at position i.

But wait, the segment tree needs to be built incrementally as we process the dominoes. Because when processing i (right to left), the reach[i] is determined, and then we need to insert this into the segment tree so that subsequent queries (for i-1, etc.) can access it.

So the segment tree is initially empty. For each i processed in reverse order:

   compute reach[i]

   then, update the segment tree at position i with reach[i]

   then, when processing i-1, any query for a range [i, ...] would have the reach[i] available.

Yes, this makes sense. Because when processing i-1, the reach for i has already been computed and inserted into the segment tree.

So the steps would be:

- Initialize a segment tree with all values set to -infinity or zero.

- Process i from n-1 downto 0:

   compute initial_reach.

   find j_initial.

   if j_initial <= i:

       reach[i] = initial_reach

       count is j_final (which is i) -i +1 =1.

   else:

       query the segment tree for the maximum reach in i+1 to j_initial.

       reach[i] = max(initial_reach, that max_reach)

       then find j_final via binary search.

       count is j_final -i +1.

   then, update the segment tree with reach[i] at position i.

But how to implement this?

The problem is, the segment tree would need to support range maximum queries and point updates. So each time we process a domino, we update the segment tree with the reach[i] at position i. Then, when processing a domino to the left, during the query phase, we can query the range [i+1, j_initial] which has already been updated with their reach values.

Yes, this approach should work.

Now, the key steps are:

Sort the dominoes by x.

Then, for each domino in reverse order:

- Compute the initial_reach.

- Find j_initial (binary search in x array for x_i + h_i -1).

- If j_initial is <=i, then no dominoes are hit except possibly itself. But wait, the domino i's initial_reach is x_i +h_i-1. So if there's no dominoes to the right (j_initial <=i), then the reach is initial_reach. The count is the number of dominoes from i to the rightmost that is <= reach[i]. But since the dominoes are sorted, the rightmost domino in x <= reach[i] is j_final. So even if j_initial is <=i, we have to compute j_final again.

Wait, perhaps the initial_reach could be larger than x_i + h_i -1. But no, the initial_reach is exactly x_i +h_i -1. So in that case, j_initial is the rightmost domino in x <= initial_reach.

But for the final reach, after considering the dominoes in the initial interval, the reach[i] could be larger than initial_reach, which would extend the j_final. For example, if domino i's initial_reach includes domino j_initial, and the maximum reach in that interval is larger than initial_reach, then j_final would be the rightmost domino in x <= reach[i] (which is now larger than initial_reach).

So for each i, after computing reach[i], we need to compute j_final via a binary search for x <= reach[i]. Then the count is j_final -i +1.

But the problem is, how to compute j_final. The x array is sorted, so binary search is possible. For each i, j_final is the maximum j where x[j] <= reach[i].

So for each i, after computing reach[i], perform a binary search on the x array from i to n-1 (since dominoes to the left of i can't be in the reach of i) to find the maximum j where x[j] <= reach[i].

But how to do this efficiently. Let's see.

The x array is sorted. For each i, the reach[i] is known. So the binary search can be done as:

low = i

high = n-1

result = i

while low <= high:

   mid = (low + high) // 2

   if x[mid] <= reach[i]:

       result = mid

       low = mid + 1

   else:

       high = mid -1

So j_final is result.

Yes. So for each i, we perform this binary search to find j_final.

Putting this all together:

1. Sort the dominoes by x.

2. Precompute x array.

3. For each i, compute initial_reach = x[i] + h[i] -1.

4. Initialize a segment tree that can handle range max queries and point updates.

5. Process i from n-1 downto 0:

   a. initial_reach = x[i] + h[i] -1.

   b. j_initial = binary search x for the largest index where x <= initial_reach.

   c. if j_initial >i:

       query the segment tree for the max in [i+1, j_initial]

       current_max = max(initial_reach, queried_max)

   else:

       current_max = initial_reach

   d. compute reach[i] = current_max.

   e. update the segment tree with reach[i] at position i.

   f. compute j_final via binary search on x array from i to n-1 for x[j] <= reach[i].

   g. count[i] = j_final -i +1.

6. After processing all dominoes, output the counts in the original order.

But wait, the original order is not the same as the sorted order. So we need to sort the dominoes but also keep track of their original indices so that we can output the counts in the correct order.

Yes. So when we read the dominoes, we need to store their x, h, and original index. Then, after sorting by x, we process and compute the counts, and then arrange the counts according to the original indices.

For example:

- Read all dominoes into a list of tuples (x, h, original_index).

- Sort the list by x.

- Compute the x array as [domino.x for domino in sorted list].

- Then, process the sorted list in reverse order, compute count[i] (the count for the i-th domino in the sorted list).

- Create an output array where output[original_index] = count[i].

So in code:

original_indices = [domino[2] for domino in sorted_dominoes]

Then, when processing each domino in the sorted list (i from 0 to n-1), but in reverse order (processing i from n-1 downto 0 in the sorted list), compute count[i], and then store it in an array. Then, after processing all, create the output array in the original order by using the original indices.

So, for example, after sorting, the sorted_dominoes list is sorted by x. Each domino in this list has an original index (from 0 to n-1). When processing, for the i-th domino in the sorted list, the count is stored in a list counts_sorted[i]. Then, the output array is built by placing counts_sorted[i] in the original index of the domino.

So, steps:

Read n.

dominoes = []

for each of the next n lines:

   x, h = map(int, input().split())

   dominoes.append( (x, h, i) )

sorted_dominoes = sorted(dominoes, key=lambda x: x[0])

x = [d[0] for d in sorted_dominoes]

h = [d[1] for d in sorted_dominoes]

original_indices = [d[2] for d in sorted_dominoes]

Then, process the sorted list in reverse order, compute counts_sorted[i], then create an output array where output[original_indices[i]] = counts_sorted[i].

Then, print the output array in order.

Now, the main challenge is implementing the segment tree for range maximum queries.

So, the segment tree needs to support:

- Point updates: set the value at a position to a new maximum.

- Range max queries: get the maximum value in [l, r].

Implementing a segment tree for this is straightforward. The standard implementation can be used.

But for n up to 1e5, the segment tree will have 4 * 1e5 nodes, which is acceptable.

Now, let's code this step by step.

First, sort the dominoes.

Then, create the x array and the h array.

Then, process in reverse order, for each i from n-1 downto 0.

But when processing i, we need to handle:

- initial_reach = x[i] + h[i] -1.

- find j_initial via binary search in x for x[j] <= initial_reach.

   j_initial can be found using bisect_right.

   For example:

   j_initial = bisect.bisect_right(x, initial_reach) -1

   Because bisect_right returns the insertion point, so the largest index where x[j] <= initial_reach is bisect_right(x, initial_reach) -1.

But the x array is sorted, so this will work.

Once j_initial is found, if j_initial <=i, then the initial_reach is not affected by other dominoes. So reach[i] = initial_reach.

Otherwise, query the segment tree for the maximum reach in [i+1, j_initial], then reach[i] is the maximum of initial_reach and this queried value.

Then, update the segment tree with reach[i] at position i.

Then, compute j_final via binary search again, this time looking for x[j] <= reach[i], and the count is j_final -i +1.

So the code outline is:

Initialize a segment tree.

counts_sorted = [0] * n

reach = [0] * n

for i in reversed(range(n)):

    xi = x[i]

    hi = h[i]

    initial_reach = xi + hi -1

    # find j_initial

    j_initial = bisect.bisect_right(x, initial_reach) -1

    if j_initial <=i:

        current_max = initial_reach

    else:

        # query [i+1, j_initial]

        max_in_interval = segment_tree.query(i+1, j_initial)

        current_max = max(initial_reach, max_in_interval)

    reach[i] = current_max

    # update the segment tree with current_max at position i

    segment_tree.update(i, current_max)

    # find j_final

    # binary search in x from i to n-1 for x[j] <= current_max

    low = i

    high = n-1

    j_final = i

    while low <= high:

        mid = (low + high) //2

        if x[mid] <= current_max:

            j_final = mid

            low = mid +1

        else:

            high = mid -1

    counts_sorted[i] = j_final -i +1

Then, after processing all i, we need to map the counts_sorted to the original order.

output = [0]*n

for i in range(n):

    original_idx = original_indices[i]

    output[original_idx] = counts_sorted[i]

print(' '.join(map(str, output)))

But wait, sorted_dominoes is sorted by x. For each i in 0..n-1 (sorted list), original_indices[i] is the original index of the i-th domino in the sorted list. So in the counts_sorted array, counts_sorted[i] is the count for the i-th domino in the sorted list. Then, output[original_indices[i]] = counts_sorted[i] fills the output array in the original order.

Yes.

Now, the implementation of the segment tree.

Implementing a segment tree for range max queries and point updates.

Here's a Python implementation:

class SegmentTree:

    def __init__(self, size):

        self.n = 1

        while self.n < size:

            self.n <<=1

        self.size = size

        self.data = [0] * (2 * self.n)

    def update(self, pos, value):

        pos += self.n

        if self.data[pos] >= value:

            return

        self.data[pos] = value

        while pos >1:

            pos >>=1

            new_val = max(self.data[2*pos], self.data[2*pos+1])

            if self.data[pos] == new_val:

                break

            self.data[pos] = new_val

    def query_range(self, l, r):

        res = 0

        l += self.n

        r += self.n

        while l <= r:

            if l %2 ==1:

                res = max(res, self.data[l])

                l +=1

            if r %2 ==0:

                res = max(res, self.data[r])

                r -=1

            l >>=1

            r >>=1

        return res

But wait, the initial size may be larger than the required size. For example, if the actual size is 1e5, but self.n is the next power of two. But the indices from 0 to size-1 are mapped to self.n to self.n + size -1. So for the query function, when l and r are beyond the actual size, the code may return incorrect results. So the segment tree should be built with the exact size, or the query should be adjusted to handle the actual indices.

Alternatively, perhaps using a 0-based segment tree where the leaves correspond to the actual indices.

But perhaps it's easier to implement the segment tree with 0-based indices and size equal to the next power of two. Then, when querying, the range is [l, r], and positions beyond the actual size (like, if the size is 1e5 and the next power is 131072) would have values 0 (since they are not updated). But since the dominoes are processed from 0 to n-1, and the segment tree is updated for these positions, the query for l and r within 0..n-1 is valid.

So for example, if the actual size is n=1e5, then the segment tree leaves are 0..n-1 mapped to self.n ... self.n + n-1. Any positions beyond n-1 (like self.n +n) would have initial 0, but since they are not part of the dominoes, their reach is 0, which doesn't affect the max.

But in our case, when processing i in 0..n-1, we are only updating those positions. So during the query, l and r are between 0 and n-1, so the segment tree will correctly query the max.

Thus, the segment tree implementation should work.

Now, putting all together.

But wait, in the code, when initializing the segment tree, we pass the size as n. So for the example where n=4, the segment tree is size 4, and the leaves are 4..7 (since the next power of two after 4 is 4, so self.n is 4. Wait, no. Let's see.

Wait, the segment tree code in __init__:

def __init__(self, size):

    self.n =1

    while self.n < size:

        self.n <<=1

    self.size = size

    self.data = [0] * (2*self.n)

So for size=4, self.n is 4. So the data array is size 8.

But the leaves (positions 4 to 7) correspond to the input positions 0 to 3.

So when the code calls update(0, value), it will set data[4] to value. Then, for a query of [0,3], which in the segment tree is positions 4 to 7, the code correctly checks each.

So the code should work.

But testing is needed.

Now, let's test with the first example.

First example input:

4

16 5

20 5

10 10

18 2

After sorting by x:

The dominoes are sorted as:

10 10 (x=10)

16 5

18 2

20 5

So the sorted x array is [10, 16, 18,20]

h array is [10,5,2,5]

original indices (assuming input order is 0,1,2,3):

sorted_dominoes will be:

index 0: (10,10,2)

index 1: (16,5,0)

index 2: (18,2,3)

index 3: (20,5,1)

So original_indices is [2,0,3,1]

Processing in reverse order (i=3 downto 0):

i=3:

x=20, h=5. initial_reach=20+5-1=24.

binary search for x <=24 in [10,16,18,20]. j_initial is 3 (since x[3]=20 <=24).

j_initial=3. Since i=3, j_initial is equal to i. So no interval to query. current_max=24. reach[3] =24.

update segment tree at position 3 with 24.

then, j_final is found via binary search for x <=24. The maximum is 3. So count is 3-3 +1=1.

counts_sorted[3] =1.

i=2:

x=18, h=2. initial_reach=18+2-1=19.

binary search for x <=19: x[3]=20 is >19. So j_initial is 2 (x[2]=18 <=19). So j_initial=2.

since i=2 and j_initial=2, current_max is 19. reach[2]=19. update segment tree at 2 with 19.

j_final: search x <=19. x[3] is 20>19. So j_final=2. count is 1.

counts_sorted[2]=1.

i=1:

x=16, h=5. initial_reach=16+5-1=20.

binary search x <=20. x[3]=20 is <=20. j_initial=3.

i=1 < j_initial=3.

query the segment tree for [i+1=2, j_initial=3]. The current segment tree has positions 2 and 3 updated to 19 and 24. So the max is 24. current_max = max(20,24)=24. reach[1] =24.

update segment tree at 1 with 24.

j_final: x <=24. All 4 dominoes x is 10,16,18,20 <=24. j_final=3. count is 3-1 +1=3.

counts_sorted[1]=3.

i=0:

x=10, h=10. initial_reach=10+10-1=19.

binary search x<=19. j_initial=2 (x[2]=18 <=19, x[3]=20>19). j_initial=2.

i=0 < j_initial=2.

query segment tree for [1,2]. The segment tree has positions 1,2,3 updated. The values are 24,19,24. Wait, positions 1 is 24, 2 is 19. So the max in [1,2] is max(24,19) =24. current_max is max(19,24)=24. reach[0] =24.

update segment tree at 0 with 24.

j_final: binary search for x <=24. j_final=3. count is 3-0 +1=4.

counts_sorted[0] =4.

Then, the counts_sorted is [4,3,1,1]. The original_indices are [2,0,3,1]. So the output array is:

output[2] =4

output[0] =3

output[3] =1

output[1] =1

Which is arranged as output[0]=3, output[1]=1, output[2]=4, output[3]=1. So the output is 3 1 4 1, which matches the first example.

So the code works for the first example.

Another example:

Input:

4

0 10

1 5

9 10

15 10

sorted x array is [0,1,9,15]

h: [10,5,10,10]

original_indices after sorting: assume input order is 0,1,2,3. So sorted dominoes are (0,10,0), (1,5,1), (9,10,2), (15,10,3). original_indices = [0,1,2,3].

Processing in reverse order:

i=3:

x=15, h=10. initial_reach=15+10-1=24.

j_initial is 3. count is 1.

reach[3]=24. counts_sorted[3]=1.

i=2:

x=9, h=10. initial_reach=9+10-1=18.

j_initial is the largest j where x[j] <=18. x[3]=15 <=18. j_initial=3.

since i=2 <3, query [3,3]. segment tree for i=3 is 24. current_max = max(18,24)=24. reach[2]=24. update segment tree.

j_final: x<=24. j_final=3. count=3-2 +1=2. counts_sorted[2]=2.

i=1:

x=1, h=5. initial_reach=1+5-1=5.

j_initial is 1 (x=1). i=1. So current_max=5. reach[1]=5.

update segment tree. j_final is 1. counts_sorted[1]=1.

i=0:

x=0, h=10. initial_reach=0+10-1=9.

j_initial is the largest j where x[j] <=9. x[2]=9 is <=9. j_initial=2.

i=0 <2.

query segment tree for [1,2]. position 1 has 5, position 2 has 24. max is 24. current_max= max(9,24)=24. reach[0]=24. update segment tree.

j_final: x<=24. j_final=3. count=3-0 +1=4. counts_sorted[0]=4.

original_indices is [0,1,2,3]. So output array is [4,1,2,1], which matches the second example.

So the code works for these cases.

Now, handling edge cases.

Edge case 1: n=1.

Input: 1

5 5

Output: 1.

Processing:

sorted x is [5]. initial_reach is 5+5-1=9. j_initial=0 (i=0). j_final=0. count=1.

Edge case 2: dominoes arranged such that each domino's initial_reach does not reach the next.

E.g., n=3, x=[1,3,5], h=[1,1,1]. Each initial_reach is 1+1-1=1, 3+1-1=3, 5+1-1=5. But since x increases by 2, no domino is in another's initial_reach. So each domino's count is 1.

Another case: dominoes arranged in a line where each domino's initial reach covers the next, and their reach is the same.

E.g., n=3, x=0, 1, 2. h=2, 2, 2.

Processing i=2: initial_reach=2+2-1=3. j_initial=2. count 1.

i=1: initial_reach=1+2-1=2. j_initial=2. query [2,2] which is 3. current_max=3. reach[i]=3. j_final=2. count=2-1 +1=2.

i=0: initial_reach=0+2-1=1. j_initial=0. count 1.

But wait, no. For i=1, j_initial is 2. So during processing i=1, j_initial=2. Then the query is from i+1=2 to j_initial=2. The reach[2] is 3. So current_max is max(2, 3)=3. reach[1] becomes 3. Then j_final is the max j where x[j] <=3. All three dominoes x are <=3. j_final=2. count is 2-1 +1=2.

So domino 1's count is 2 (dominoes 1 and 2).

But domino 1's initial reach is 2, which covers domino 2 (x=2 is 1+2-1=2. So x=2 is <= 2. So domino 2 is hit. So when domino 1 is pushed, it hits domino 2. But domino 2's reach is 3. So domino 1's reach becomes 3. So the count is the number of dominoes from 1 to 2 (which is 2).

But domino 0's reach is 1, which does not reach domino 1 (x=1>0+2-1=1? No, x=1 is equal to 1. So domino 1 is hit. Because the problem statement says the fall is triggered if the domino is touched strictly above the base. So the interval is [x_i+1, x_i + h_i-1]. So for domino 0, x=0, h=2. The interval is [1, 1]. So domino 1's x is 1, which is in the interval. So domino 0's initial_reach is 0+2-1=1. So j_initial is the largest index with x[j] <=1. x[1] is 1, x[2] is 2>1. So j_initial=1. i=0 < j_initial=1.

Query the segment tree for [1,1] (reach[1] is 3). current_max = max(1,3) =3. reach[0] =3. j_final is 2 (x[2] is 2 <=3). count=3.

So the counts are 3, 2, 1.

So output is 3 2 1.

But according to the code:

i=0:

initial_reach=1.

j_initial=1.

query [1,1] (which is reach[1] =3). current_max=3.

j_final is 2. count=0->2: 3.

So yes.

Thus, the code should handle this correctly.

Now, the segment tree implementation in Python needs to handle the queries and updates efficiently. For n=1e5, each update and query is O(log n), which is acceptable.

But in Python, a standard segment tree may be too slow for 1e5 elements, especially with 1e5 operations. So perhaps using a binary indexed tree (Fenwick tree) is not possible here, because it can't handle range maximum queries. So a segment tree is the way to go.

Alternatively, since we process the dominoes from right to left, and for each i, the query is always to the right of i (i+1 to j_initial), which has been processed. Also, the reach of these dominoes is already known.

Wait, but when processing i, the reach for i+1 and so on have been processed and stored in the segment tree.

But in the code, after processing i, we update the segment tree with reach[i]. So for i+1, the segment tree has already been updated with reach[i+1], and when processing i, the query is for [i+1, j_initial], which is the same as the next domino.

Thus, the segment tree approach is correct.

Now, the code.

Now, implementing the segment tree:

In Python, the segment tree can be implemented as a class with the following methods:

- __init__: initializes the segment tree.

- update: updates a position with a new value (if the new value is larger than the current one).

- query: returns the maximum in a range [l, r].

But in the code, the segment tree for max queries must have the ability to update a position to a new maximum if the new value is larger than the existing one. Because in this problem, the reach[i] is determined, and once set, it cannot be changed (since we process from right to left, each i is processed once). So each update is a one-time operation. But in the code, the segment tree's update function can just set the value, since each position is updated once.

Wait, no. For example, during the processing of i=0, we set reach[0], and it's updated in the segment tree. But no other domino will update position 0 again.

Thus, each position in the segment tree is updated exactly once. Therefore, the update function can safely set the value, without checking whether the new value is larger than the previous one. Because when processing i, the segment tree's position i is initialized to 0 (or whatever initial value), and during processing, we set it to reach[i]. Since the segment tree is initialized with all zeros, and reach[i] can be larger than zero.

Wait, no. Because the initial value of the segment tree's data is zero. So if a domino's reach is zero, but the maximum is taken, but in reality, reach[i] can't be zero unless x_i +h_i-1 is negative. But the problem statement says h_i >=2, and x_i can be negative. For example, x_i = -1e8 and h_i=2. Then initial_reach is -1e8 +2-1 = -1e8 -1 +2 = -1e8 +1.

But in this case, j_initial would be the largest index where x_j <= initial_reach, which could be -infinity, so j_initial would be -1. But dominoes are sorted by x, so if x[0] is -1e8, and initial_reach is even lower, then j_initial could be -1, which is handled in code.

But in the segment tree, if a position is not updated, it will have a zero. But in our case, all positions are processed from right to left. So when processing i, all positions >=i are updated in the segment tree. So during processing i, the segment tree for positions i+1 to j_initial will have been updated.

Thus, the initial values are zero, but when processing i from right to left, each position is updated exactly once. Thus, the segment tree's update function can simply set the value, without checking for the maximum. Because when i is processed, the segment tree's position i is updated to reach[i], and since it's processed once, no future updates will overwrite it.

Thus, the code for the segment tree's update can be:

def update(self, pos, value):

    pos += self.n

    self.data[pos] = value

    while pos >1:

        pos >>=1

        new_val = max(self.data[2*pos], self.data[2*pos+1])

        if self.data[pos] == new_val:

            break

        self.data[pos] = new_val

But in the previous example, when a position is updated, we set the leaf node to the new value, then propagate up.

Thus, the update function is correct.

Thus, the code for the segment tree is as follows.

Finally, putting all together.

The code will:

Read the dominoes, sort them by x.

Process each domino in reverse order, updating the segment tree.

Compute the counts.

Arrange them in the original order.

Now, the code:

But in Python, for the binary search, we can use the bisect module.

Here's the code:

Testing against sample input 1.

```python
import bisect


class SegmentTree:

    def __init__(self, size):

        self.n = 1

        while self.n < size:

            self.n <<= 1

        self.size = size

        self.data = [0] * (2 * self.n)

    def update(self, pos, value):

        pos += self.n

        self.data[pos] = value

        while pos > 1:

            pos >>= 1

            new_val = max(self.data[pos * 2], self.data[pos * 2 + 1])

            if self.data[pos] == new_val:

                break

            self.data[pos] = new_val

    def query(self, l, r):

        res = 0

        l += self.n

        r += self.n

        while l <= r:

            if l % 2 == 1:

                res = max(res, self.data[l])

                l += 1

            if r % 2 == 0:

                res = max(res, self.data[r])

                r -= 1

            l >>= 1

            r >>= 1

        return res

def main(input_stream, output_stream):
    import sys

    input = input_stream.read().split()

    ptr = 0

    n = int(input[ptr])

    ptr +=1

    dominoes = []

    for i in range(n):

        x = int(input[ptr])

        ptr +=1

        h = int(input[ptr])

        ptr +=1

        dominoes.append( (x, h, i) )

    dominoes.sort()

    x = [d[0] for d in dominoes]

    h = [d[1] for d in dominoes]

    original_indices = [d[2] for d in dominoes]

    size = len(x)

    st = SegmentTree(size)

    counts_sorted = [0] * size

    for i in reversed(range(size)):

        xi = x[i]

        hi = h[i]

        initial_reach = xi + hi -1

        # Find j_initial

        j_initial = bisect.bisect_right(x, initial_reach) -1

        if j_initial > i:

            max_reach = st.query(i+1, j_initial)

            current_max = max(initial_reach, max_reach)

        else:

            current_max = initial_reach

        st.update(i, current_max)

        # Find j_final

        low = i

        high = size -1

        j_final = i

        while low <= high:

            mid = (low + high) //2

            if x[mid] <= current_max:

                j_final = mid

                low = mid +1

            else:

                high = mid -1

        counts_sorted[i] = j_final - i +1

    output = [0] *n

    for i in range(size):

        output[original_indices[i]] = counts_sorted[i]

    print(' '.join(map(str, output)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
0 10
1 5
9 10
15 10
""",
            "output": \
"""\
4 1 2 1
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

Second example:

Input:

4

0 10

1 5

9 10

15 10

Sorted dominoes: (0,10,0), (1,5,1), (9,10,2), (15,10,3)

counts_sorted after processing:4,1,2,1. output array:4 1 2 1, which matches.

Thus, the code should work.
</think>

```python
import bisect

class SegmentTree:
    def __init__(self, size):
        self.n = 1
        while self.n < size:
            self.n <<= 1
        self.size = size
        self.data = [0] * (2 * self.n)

    def update(self, pos, value):
        pos += self.n
        self.data[pos] = value
        while pos > 1:
            pos >>= 1
            new_val = max(self.data[pos * 2], self.data[pos * 2 + 1])
            if self.data[pos] == new_val:
                break
            self.data[pos] = new_val

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l <= r:
            if l % 2 == 1:
                res = max(res, self.data[l])
                l += 1
            if r % 2 == 0:
                res = max(res, self.data[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    dominoes = []
    for i in range(n):
        x = int(input[ptr])
        ptr += 1
        h = int(input[ptr])
        ptr += 1
        dominoes.append((x, h, i))
    
    dominoes.sort()
    x = [d[0] for d in dominoes]
    h = [d[1] for d in dominoes]
    original_indices = [d[2] for d in dominoes]
    size = len(x)
    
    st = SegmentTree(size)
    counts_sorted = [0] * size
    
    for i in reversed(range(size)):
        xi = x[i]
        hi = h[i]
        initial_reach = xi + hi - 1
        j_initial = bisect.bisect_right(x, initial_reach) - 1
        
        if j_initial > i:
            max_reach = st.query(i + 1, j_initial)
            current_max = max(initial_reach, max_reach)
        else:
            current_max = initial_reach
        
        st.update(i, current_max)
        
        low = i
        high = size - 1
        j_final = i
        while low <= high:
            mid = (low + high) // 2
            if x[mid] <= current_max:
                j_final = mid
                low = mid + 1
            else:
                high = mid - 1
        counts_sorted[i] = j_final - i + 1
    
    output = [0] * n
    for i in range(size):
        output[original_indices[i]] = counts_sorted[i]
    
    print(' '.join(map(str, output)))

if __name__ == "__main__":
    main()
```
