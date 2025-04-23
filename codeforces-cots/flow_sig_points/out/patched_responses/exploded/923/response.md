<think>
Okay, let's tackle this problem. So, the task is to find for each citizen the earliest possible bus that they can take, right? The buses are sorted by their time tj, and we need the minimum tj that satisfies certain conditions for each person. Let's break down the problem.

First, let's understand the conditions. For a citizen to take bus j, the following must hold:
1. The bus's start stop (sj) must be less than or equal to the citizen's starting stop (li).
2. The bus's end stop (fj) must be greater than or equal to the citizen's destination (ri).
3. The citizen's arrival time (bi) must be less than or equal to the bus's time (tj).

And among all buses that meet these conditions, we need the one with the smallest tj. Because tj's are unique, there's a unique minimum.

Now, the problem is that with n and m up to 1e5, we need an efficient way to process each query. A naive approach where each query checks all buses would be O(nm) which is 1e10 operations and way too slow. So we need a smarter approach.

Let's think about how to structure the data. Since we need to find buses that cover the [li, ri] interval of the citizen, perhaps we can group buses by their coverage. But even that seems tricky. Another angle: since the tj's are unique and we want the smallest tj, maybe we can process the buses in order of increasing tj, but that's the opposite of what we need. Wait, no. Wait, we need the minimum tj that is >= bi and covers the route. So for each query, the answer is the earliest possible tj that is >= bi and covers the required stops.

Hmm. So maybe for each query, we need to find the bus with the earliest tj >= bi, such that sj <= li and fj >= ri. But how do we efficiently find this?

Wait, but the buses are not sorted in any particular order. So the first step might be to preprocess the buses into some data structures that allow us to query efficiently.

Let's consider that the buses are sorted by their tj. Then, for a given query, we can binary search on tj to find the earliest tj >= bi. But even then, among those buses with tj >= bi, we need to check if any of them covers the required stops.

But how do we check that efficiently?

Alternatively, for each bus, we can note that it's a candidate for a query if tj >= bi, sj <= li, and fj >= ri.

So for each query (li, ri, bi), we need the bus with the earliest tj (since we want the minimum tj) that satisfies these three conditions.

The key is to find, for the given li and ri, the earliest tj >= bi such that the bus's sj is <= li and fj >= ri.

So how can we structure the data to answer these queries efficiently?

Let's think of it this way: for all buses that have tj >= bi, we need to find if there's any bus whose sj <= li and fj >= ri, and among those, the one with the smallest tj.

But with m up to 1e5 and n up to 1e5, we need to process each query in O(log n) time or something like that.

An approach could be to pre-process the buses by grouping them based on their sj and fj. But how?

Alternative idea: For each possible (sj, fj), but that's not feasible since sj and fj can be up to 1e9. So we need a different approach.

Another approach is to process the queries offline. Let's sort both the queries and the buses in a particular order and process them in a way that allows us to answer all queries efficiently.

Wait, here's a possible plan:

1. Sort all buses in increasing order of tj. This is possible since all tj are unique.

2. Sort all queries in increasing order of bi. So for each query, when we process them in order, we can consider all buses up to a certain tj (since the queries are ordered by bi, and buses are ordered by tj, which is their sorted order).

Wait, but the queries have their own bi. So when we process a query, we can include all buses where tj >= bi. Wait, no. Because if a query has bi = 5, we need buses with tj >=5. But if another query has bi=3, we need buses with tj >=3. So processing queries in order of increasing bi may not help.

Alternatively, let's sort the buses in increasing order of tj. Then, for each query, the relevant buses are those with tj >= bi, and among them, the earliest (smallest tj) that covers the li and ri.

So for each query, the candidate buses are those in the sorted list starting from the first tj >= bi. For each such query, we need to find in that subset the bus with the earliest tj (since sorted list is in increasing tj) that has sj <= li and fj >= ri.

Wait, but since the buses are sorted by increasing tj, the earliest tj >= bi is the first occurrence in the list where tj >= bi. Then, the subset of buses from that position onwards has tj >= bi. But in that subset, we need the earliest (smallest tj) bus that covers the li and ri.

But how do we check that subset for the coverage conditions?

This is the crux of the problem. How to efficiently find, for a given li and ri, the earliest tj >= bi such that sj <= li and fj >= ri.

So here's an idea: For each bus, after sorting by tj, we can build some data structure that allows us to query, for a given li and ri, the earliest bus (smallest tj in the sorted list) where sj <= li and fj >= ri. But how to represent this data structure.

Another angle: For each possible li and ri, the required bus must have sj <= li and fj >= ri. So for a query (li, ri, bi), we can find all buses with tj >= bi, and among those, find the one with the earliest tj where sj <= li and fj >= ri.

So perhaps for the buses sorted by tj, we can pre-process them in such a way that for any li and ri, we can quickly find the minimal tj >= bi in the list where sj <= li and fj >= ri.

But even with that, how do we structure the data?

Alternative approach: For each bus, since we have them sorted by tj, we can create a structure that allows us to query, given a li and ri, the earliest bus (in the sorted list) where sj <= li, fj >= ri, and tj >= bi. But how?

This feels like a range query problem. Maybe using a segment tree or binary indexed tree (Fenwick tree) that can track for ranges of buses the minimal required sj and fj, but I'm not sure.

Wait, another idea: For each bus in the sorted list (sorted by tj), we can pre-process and store the maximum fj for each possible sj. But again, sj and fj can be up to 1e9, so that's not feasible.

Alternatively, perhaps we can model the problem as a 2D range query. For each query (li, ri), we need a bus where sj <= li and fj >= ri. So in 2D space, we can represent each bus as a point (sj, fj), and the query is a point (li, ri) where we need to find any bus in the subset tj >= bi such that sj <= li and fj >= ri. Among those, we need the one with the smallest tj.

So the problem reduces to, for each query, find the point in the set (all buses with tj >= bi) where sj <= li and fj >= ri, with the minimal tj.

How to perform this efficiently.

But with 1e5 buses and queries, we need a data structure that can handle these 2D range queries with dynamic insertion (since we process buses in order of tj and may want to add them to the data structure as we process queries in some order).

Alternatively, since the buses are sorted by tj, perhaps we can process the queries in order of increasing bi. Let's think:

Sort the buses in increasing order of tj. Let's say we have them ordered as t1 < t2 < ... < tn.

Sort the queries in increasing order of bi. Then, for each query, when we process it, we can have all buses with tj >= bi added to some data structure. Because once we process a query with bi = x, all subsequent queries with bi >= x will include buses that were added for x. But no, that's not correct. Because if a query comes with a higher bi, we need to include more buses. Wait, no: for a query with bi = x, any bus with tj >= x is a candidate. So if we process queries in order of increasing bi, then for each query, the set of possible buses is those with tj >= bi. As bi increases, the required tj is higher, so the set of candidate buses is a subset of those for lower bi. Wait, no: if bi is higher, the tj must be >= higher value, so the candidate buses are a subset of the ones that would have been considered for lower bi.

Wait, perhaps not. Let's see: suppose buses are sorted as t1 < t2 < ... < tn. For a query with bi = 3, candidate buses are t3, t4, ..., tn. For a query with bi = 5, candidate buses are t5, t6, ..., tn. So as bi increases, the starting index of candidate buses in the sorted list moves to the right. So if we process the queries in the order of increasing bi, we can process them by moving a pointer through the sorted buses list, adding buses to a data structure when their tj is >= the current query's bi.

Wait, this might work. Let's outline the steps:

1. Sort all buses in increasing order of tj. Keep track of their original indices (since we need to output the bus number).

2. Sort all queries in increasing order of bi. Also, keep track of their original order so we can output the answers correctly.

3. Initialize a pointer (say, 'bus_ptr') at the end of the sorted buses list. Or maybe start from the beginning and move forward. Wait, no. Let's see. Since buses are sorted by tj in increasing order, the first bus has the smallest tj, and the last has the largest. For a query with bi, the candidate buses are those with tj >= bi. So in the sorted list, the first bus that meets tj >= bi is found via binary search, and all buses from that index to the end are candidates. But if we process queries in increasing order of bi, then for each query, the next query's bi could be higher, meaning we need to find a new starting point. However, processing queries in this order allows us to use a pointer that starts at the beginning of the buses list and moves forward as we process higher bi's, adding buses to a data structure when their tj is >= the current query's bi.

Wait, perhaps not. Let's think again. Suppose we have buses sorted by tj: t1, t2, t3, ..., tn (t1 < t2 < ... < tn).

When processing a query with bi = x, we need to consider all buses where tj >= x, which would be the buses from the first one where tj >=x (found via binary search) to the end.

If we process the queries in increasing order of bi, then for each query, x is increasing. So the starting point in the buses list (the first tj >=x) is moving to the right (higher indices) as x increases.

So, for example, for the first query with bi = 5, we might start at bus index 10. The next query with bi = 7 starts at bus index 15, etc. So each time, the buses added to the data structure are those between the previous starting index and the new starting index.

But since the buses are sorted by tj in increasing order, once we process a query with bi = x, any query with a larger bi will require us to start at a higher index in the buses list. So, we can process the buses in the order of their tj, and for each query, find the first bus with tj >= bi using binary search, then include all buses from that index to the end.

But how do we handle the data structure for these buses?

Once we have all the candidate buses (those with tj >= bi) for a query, we need to find among them the earliest tj (since they are sorted, that's the first one that meets the conditions) which also has sj <= li and fj >= ri.

But how can we efficiently find such a bus?

This is the key problem. We need a way to query, among a subset of buses (those with tj >= bi), the earliest tj (smallest tj in the subset) where sj <= li and fj >= ri.

Wait, but the subset is sorted by tj in increasing order. So the earliest tj in the subset is the first bus in the subset that meets the conditions. So for each query, once we have the subset (from index 'start' to the end), we need to find the first bus in this subset where sj <= li and fj >= ri.

So the problem reduces to, for each query, after finding the start index in the buses list (sorted by tj) where tj >= bi, iterate through the buses from start to end (in order of increasing tj) and find the first bus where sj <= li and fj >= ri. The first such bus will have the minimum tj, which is the answer.

But if we do this naively for each query, in the worst case, each query could scan O(n) buses, leading to O(nm) time again.

This is not feasible. So we need a way to answer these conditions quickly for each query.

Alternative idea: For the buses in the subset (tj >= bi), we can pre-process them in a way that allows us to query for the earliest bus with sj <= li and fj >= ri.

But how? Let's think about the conditions:

We need sj <= li and fj >= ri. So for a given li and ri, a bus must cover the interval [sj, fj] such that it contains [li, ri]. So the bus's interval must start before or at li and end after or at ri.

So for each query (li, ri), we need to find a bus in the subset where sj <= li and fj >= ri.

But how can we structure the data to find this efficiently.

Another approach is to note that for each query, the required buses have fj >= ri and sj <= li. So the fj must be at least ri, and sj at most li. So perhaps for each possible ri, we can have a data structure that stores the buses with fj >= ri, and among them, find the one with sj <= li and the earliest tj.

But again, ri can be up to 1e9, so this approach isn't directly feasible.

Alternative idea: For the buses sorted by tj, and given a query (li, ri, bi), we can find the earliest tj >= bi, and check if there exists a bus in that subset with sj <= li and fj >= ri. The first such bus in the subset would be the answer.

But again, how to find this quickly.

Wait, perhaps the key is to process the buses in order of tj (since they are sorted) and for each query, process the buses in order of tj (starting from the first that is >= bi) and find the first one that satisfies the conditions.

But how to do this efficiently.

If for each query, we can find the first bus in the subset where sj <= li and fj >= ri, then we can answer the query. To find this efficiently, perhaps we can use a 2D range minimum query structure.

Alternatively, since the buses are in order of increasing tj, perhaps we can pre-process for each bus, the maximum fj that can be found for buses up to that point with sj <= certain values.

But this seems complicated.

Let's think of the buses sorted by tj. For each bus j, we can note that buses after j in the list have higher tj. So when we process a query, the subset is a consecutive range in the list (from start to end). For this range, we need the earliest (first) bus where sj <= li and fj >= ri.

So if we can, for each possible (li, ri), find the first bus in the range that satisfies both conditions, then we can answer the query.

But how to do this.

Let's consider that for each bus in the subset (tj >= bi), we can check if sj <= li and fj >= ri. We need the first such bus in the subset (i.e., the earliest tj). So in the sorted list of buses (by tj), the earliest one that meets the conditions is the first occurrence in the subset.

So the problem reduces to, for each query (li, ri, bi), find the first bus in the list (starting from index 'start') where sj <= li and fj >= ri.

But how to find this quickly.

Here's an idea: For each bus, we can pre-process two separate sorted arrays. One sorted by sj, and another sorted by fj. But that might not help directly.

Alternatively, for the subset of buses (from start to end), we can build a structure that allows us to query for buses where sj <= li and fj >= ri. But with such a structure, how do we find the earliest tj.

Alternatively, since the subset is sorted by tj in increasing order, the earliest tj is the first occurrence in the subset that meets the conditions. So the problem is to find the first bus in the subset (from start to end) where sj <= li and fj >= ri.

So the question is, can we efficiently find the first occurrence in a range of a list that satisfies two conditions: sj <= li and fj >= ri.

This seems like a problem that could be addressed with a segment tree. Each node in the segment tree represents a range of buses. For each node, we can precompute some information that allows us to quickly check if any bus in the range meets the conditions. Then, when querying, we can perform a binary search through the segment tree to find the first bus in the range that meets the conditions.

But building such a segment tree would require each node to store information that allows checking for the presence of a bus in its range with sj <= li and fj >= ri. However, this is challenging because the conditions depend on the parameters li and ri, which vary per query.

Alternatively, for each query, we can perform a binary search on the subset of buses (start to end) to find the first bus that satisfies the conditions. For each candidate bus in the binary search, we check if sj <= li and fj >= ri. If yes, we move left to find an earlier one; if not, we move right. But this approach would take O(log n) per query for the binary search, and for each step in the binary search, we need to check the conditions, which are O(1). However, the problem is that the binary search would check O(log n) buses, but each query could have a different subset (start to end). So for each query, the subset is from start index to end index. The binary search would need to be done within that subset.

But how to handle varying start indices for each query.

Wait, the subset for a query is from start index (found via binary search on tj) to the end of the list. So the start index is the position where buses start to have tj >= bi.

So the subset is buses[start ... n-1], sorted by increasing tj.

So for each query, we need to find the first occurrence in this subset where sj <= li and fj >= ri.

We can model this as follows:

For each query, the buses to consider are in a suffix of the sorted list. We need the first bus in this suffix where sj <= li and fj >= ri.

So for each query, we can perform a linear scan from start to end, checking each bus. But this is O(k) per query, where k is the number of buses in the suffix. In the worst case, this is O(n) per query, leading to O(nm) time, which is too slow.

Thus, we need a way to answer these suffix range queries efficiently.

Another Idea: For each bus in the sorted list, precompute a data structure that allows queries like, "given li and ri, what is the earliest bus in the suffix starting at position s where sj <= li and fj >= ri".

But how to precompute such a structure.

Perhaps we can use a segment tree where each node contains the maximum fj for buses in that node's interval with sj <= li. But again, li varies per query, making this approach difficult.

Alternative Idea: For each bus in the sorted list, store sj and fj. Then, for a given query, we can process the buses in the subset (start to end) and for each, check if sj <= li and fj >= ri. We need the first one in the list that satisfies this.

The key is to process the buses in order of increasing tj (since the subset is sorted by tj), and find the first one that meets the conditions. So perhaps for each query, the answer is the first bus in the subset where sj <= li and fj >= ri.

To find this efficiently, perhaps we can pre-process for each position in the list, a structure that allows us to quickly query the first occurrence of a bus in the range [start, end] that meets the conditions.

But how?

Alternatively, for each bus, we can represent it as a point (sj, fj), and for the subset of buses [start, end], we need the earliest bus (smallest index in the subset) where sj <= li and fj >= ri.

But this is a 2D range query problem, which is challenging.

An alternative approach is to pre-process the buses in such a way that for a given li and ri, we can query the earliest tj >= bi where sj <= li and fj >= ri.

Here's a possible plan:

1. Sort all buses by tj in increasing order. This allows us to process queries in a way that we can binary search for the start index of tj >= bi.

2. For each bus in the sorted list, we can note that once we have the start index (s), the buses from s to n-1 are the candidates.

3. For these candidates, we need to find the first one (in order) where sj <= li and fj >= ri.

The problem now is how to efficiently find this first occurrence in the candidate list.

Let's think about using a binary indexed tree or a segment tree. For example, if we can build a segment tree where each node stores the minimum sj and maximum fj in its interval. Then, for a given query, we can check the intervals in the segment tree in order (from left to right) to find the earliest bus that meets the conditions.

But even that approach may not be efficient enough. For example, during a query, we would need to traverse the segment tree from left to right, checking each interval's min sj and max fj. If the interval's min sj <= li and max fj >= ri, then there might be a bus in that interval that meets the conditions. We would need to recursively check its children to find the earliest one.

This way, we can find the earliest bus in O(log n) time per query.

Yes, this seems promising. Let's think through this.

The segment tree nodes each cover a range of the buses sorted by tj. Each node stores two values: the minimum sj in the interval and the maximum fj in the interval. For a query (li, ri), we need to find the first bus in the candidate range (start to end) where sj <= li and fj >= ri. We can traverse the segment tree from left to right (since we want the earliest bus), checking if the current node's min sj <= li and max fj >= ri. If so, we need to check the left child first, since we want the earliest bus. If the left child doesn't contain such a bus, we check the right child. If neither does, then backtrack.

Wait, but the candidate range is from start to end. So the segment tree is built for the entire list of buses sorted by tj, and each query's candidate range is a suffix (start to n-1). So we need to query the segment tree for the range [start, n-1], and find the earliest index in that range where sj <= li and fj >= ri.

But how can we do that with a segment tree.

The segment tree can be built for the entire array. Each node covers a range [l, r]. For each node, we store the min sj and max fj in that range.

Then, for a query [start, end] (the entire list from start to end), we can query the segment tree to find the earliest index in [start, end] where sj <= li and fj >= ri.

This can be done by recursively checking the left and right children of the current node, but ensuring that we visit the leftmost possible nodes first.

Here's how the query would work:

function find_earliest(node, query_start, query_end, li, ri):
    if node's range is outside [query_start, query_end]:
        return -1
    if node's min sj > li or node's max fj < ri:
        return -1
    if node is a leaf node:
        return node's position if sj <= li and fj >= ri
    res_left = find_earliest(left child, query_start, query_end, li, ri)
    if res_left != -1:
        return res_left
    res_right = find_earliest(right child, query_start, query_end, li, ri)
    return res_right

This way, the query returns the earliest position in the query range where the conditions are met, or -1 if none exists.

Each such query would take O(log n) time, since each level of the segment tree is visited once, and in the worst case, all nodes in the path are checked.

Building such a segment tree would take O(n) time for the initial construction. Each node's min sj and max fj can be computed during the build phase.

Once we have this segment tree, for each query, we can:

1. Binary search to find the start index (s) in the sorted buses list where tj >= bi.

2. Query the segment tree for the range [s, n-1] to find the earliest index where sj <= li and fj >= ri.

3. If such an index exists, the answer is the original index (bus number) of that bus. Otherwise, -1.

This approach seems feasible. Let's outline the steps in code:

First, we need to sort the buses by tj. Then, build a segment tree for these sorted buses, storing min sj and max fj for each node.

Then, for each query:

- Binary search to find the earliest bus where tj >= bi. Let's call this index s.

- If s is beyond the last index (no such bus), answer is -1.

- Else, query the segment tree on the range [s, n-1] to find the earliest bus in this range with sj <= li and fj >= ri.

- If found, return the original index of that bus.

Now, considering the time complexity:

- Sorting the buses takes O(n log n).

- Building the segment tree takes O(n).

- Each query involves a binary search (O(log n)), a segment tree query (O(log n)), and sorting the queries (O(m log m)).

So the total time complexity is O(n log n + m log m + m log n), which should be acceptable for n and m up to 1e5.

Now, let's think about the data structures.

Implementing the segment tree:

Each node will have:

- min_sj: the minimum sj in the interval.

- max_fj: the maximum fj in the interval.

For a leaf node (single bus), min_sj and max_fj are the bus's sj and fj.

For internal nodes, min_sj is the minimum of the left and right child's min_sj, and max_fj is the maximum of the left and right child's max_fj.

The query function as described earlier will recursively check the left and right children, returning the earliest index in the range that meets the conditions.

Now, let's code this.

But wait, in Python, implementing a segment tree with 1e5 elements may have some overhead, but since each query is O(log n), it's manageable.

But perhaps there's a more efficient way.

Alternative Idea: Offline Processing.

If we can process all queries and buses in an order that allows us to use a more efficient data structure.

Let's consider that the buses are sorted by increasing tj. Queries are also sorted by bi in increasing order.

We can process each query in the order of increasing bi. For each query, we add all buses with tj <= bi to some data structure. Wait, no. Because a query requires buses with tj >= bi. So as we process queries in increasing order of bi, the required tj for the buses is also increasing. So, for example, when we process a query with bi = x, all buses with tj >=x are candidates. But since the buses are sorted by tj, the next query with a higher bi will require tj >= bi, which is a subset of the previous candidates.

Wait, no. If we process queries in increasing order of bi, then for each query, the required tj is >= bi. But since the buses are sorted by tj, the buses that are candidates for a query are those from s (binary search) to the end. As bi increases, the s increases (since the first bus with tj >= bi is higher up in the list).

So, if we process the buses in sorted order (tj increasing), and process queries in sorted order (bi increasing), then for each query, the s (start index) is the first bus in the sorted list with tj >= bi.

But as bi increases, the s moves to the right.

Now, if we process the queries in sorted order of bi, then for each query, the s is the current position in the sorted buses list.

So, perhaps we can process the buses in the sorted order, and for each bus, we add it to a data structure, and then process any queries whose bi is <= tj of the current bus.

But I'm not sure how to model this.

Alternatively, here's a plan:

1. Sort the buses by tj in increasing order.

2. Sort the queries by bi in increasing order, but keep track of their original indices to output the answers correctly.

3. For each query in the sorted order, we need to find all buses with tj >= bi. Since the buses are sorted by tj, this is a suffix of the buses list. But we can't precompute all possible suffixes.

Alternatively, perhaps for each query in the sorted list, we can find the buses with tj >= bi and then query the data structure for the earliest bus in that suffix.

But how to manage the data structure.

Another Idea: Use a binary indexed tree (Fenwick tree) to track the minimum tj for certain conditions. But again, it's not clear.

Alternatively, for each bus in the sorted list, when processed in order of increasing tj, we can insert them into a structure that allows us to query for sj <= li and fj >= ri. However, this seems tricky.

Wait, here's an alternative approach. Since the buses are sorted by tj in increasing order, for each query, the earliest possible tj that is >= bi is the first bus in the sorted list with tj >= bi. And among the buses from that index onwards, we need to find the first one that covers li and ri.

But how to pre-process the buses to answer this quickly.

Maybe for each possible li and ri, but this is impossible due to their size.

Alternatively, for each bus in the sorted list, we can pre-process a structure that allows us to answer for a given li and ri, the earliest bus in the list that has sj <= li and fj >= ri.

But how.

Hmm. Another Idea: For each bus in the sorted list, we can track the maximum fj for buses up to that point with sj <= li. But again, li varies per query.

Alternatively, since the buses are sorted by tj, and the earliest tj is the first one in the subset that covers the query's li and ri, perhaps we can use a binary indexed tree to track for each sj the maximum fj. But how.

Alternatively, we can use a binary indexed tree that is indexed by sj, and for each sj, we store the maximum fj. Then, for a given li, we can query the maximum fj where sj <= li. If this maximum fj >= ri, then there exists a bus that covers the query.

But this approach only gives the maximum fj for sj <= li. However, the earliest tj may not be the one with the maximum fj, since there may be multiple buses with sj <= li and fj >= ri, but with varying tj.

Wait, but the buses are sorted by tj in increasing order. So the first bus that satisfies sj <= li and fj >= ri will have the smallest tj. So for each query, we need the earliest bus in the subset (tj >= bi) that satisfies the conditions.

But how can we use a binary indexed tree here.

Another Idea:

We can process the buses in order of increasing tj (sorted list), and for each bus, when we process it, we insert its sj and fj into a data structure. Then, for a query with bi <= tj, we can query this data structure for the earliest tj >= bi where sj <= li and fj >= ri.

But this approach would require processing queries after inserting all buses up to a certain tj, which is not feasible.

Alternatively, since we have the buses sorted by tj, and the queries sorted by bi, perhaps we can process the queries in order of increasing bi, and for each query, add all buses with tj >= bi (from the sorted list) that haven't been added yet to the data structure. Then, for each query, we can query the data structure for the earliest bus (smallest tj) that covers li and ri.

But how to manage this.

Let's try to formalize this:

- Sort buses by tj in increasing order.

- Sort queries by bi in increasing order, keeping track of their original indices.

- Initialize a pointer to 0 in the buses list.

- For each query in sorted order:

   a. While the pointer is less than n and buses[pointer].tj < bi: increment pointer.

   b. Now, all buses from pointer to n-1 have tj >= bi. We need to insert them into a data structure that allows us to query for buses with sj <= li and fj >= ri, and find the one with the smallest tj.

   c. But how to insert them. Since the buses are processed in order of increasing tj, inserting them into the data structure in this order ensures that when we query for buses with sj <= li and fj >= ri, the earliest one in the data structure (smallest tj) is the first one inserted that meets the conditions.

But how to manage the data structure.

The data structure needs to support adding buses and querying for the earliest bus (smallest tj) where sj <= li and fj >= ri.

This is a dynamic data structure problem. But with 1e5 buses and queries, the operations must be O(log n) time each.

But what data structure allows this?

Perhaps, for each bus, we can store it in a structure that allows us to query the minimal tj where sj <= li and fj >= ri.

But this is a 2D range query problem, and such queries are not trivial to handle.

Alternative Idea:

For each query, after adding the relevant buses (those with tj >= bi) into the data structure, we can query for the minimal tj bus that has sj <= li and fj >= ri.

But how to structure this data.

An alternative approach is to pre-process for each bus, but I'm not seeing it.

Wait, let's think again. For each bus, we can note that it is relevant for queries with bi <= tj.

But if we process the queries in order of increasing bi, and the buses in order of increasing tj, then for each query, all buses with tj >= bi can be added to the data structure. But how to manage this.

Let me think:

Initially, the data structure is empty. The buses are sorted by tj in increasing order. Queries are sorted by bi in increasing order.

For each query in sorted order of bi:

   a. We need to add all buses with tj >= bi that haven't been added yet. Since the buses are sorted by tj in increasing order, we can use a pointer that starts at the first bus and moves forward as we process queries. But wait, no. Because for a query with bi = x, the required buses are those with tj >=x. But since the buses are sorted by tj, the buses with tj >=x are the ones from some index s to n-1.

But the pointer approach would need to add all buses from s onwards, but how to track which buses have already been added.

Alternatively, here's the process:

- buses are sorted by tj in increasing order: t1 < t2 < ... < tn.

- queries are sorted by bi in increasing order: q1 <= q2 <= ... <= qm.

- We initialize a pointer 'bus_ptr' to 0.

- For each query q in sorted order:

   a. While bus_ptr < n and buses[bus_ptr].tj < q.bi: increment bus_ptr.

   b. The buses from bus_ptr to n-1 have tj >= q.bi and have not been processed yet. We need to add them to the data structure.

   c. But once added, they are part of the data structure for all subsequent queries (since their tj >= q.bi, and the next queries have higher or equal bi, so their tj will be >= as well).

But this is not correct. For example, if a query has bi=5, and a bus has tj=5, then any subsequent query with bi=6 will not include this bus (since 5 <6), but according to the problem, the bus's tj must be >= bi. So, when we process queries in order of increasing bi, the buses added to the data structure must have tj >= current query's bi. But the previous buses added may have tj < current query's bi. So the approach of adding all buses with tj >= q.bi is incorrect.

This approach is flawed. Because when we process query q with bi=x, and then process query q' with bi=y where y >x, the buses added for q (tj >=x) may include buses with tj >=x but <y. These buses would not be valid for q'.

So this approach won't work. Thus, the initial idea of using the segment tree seems more promising.

So back to the segment tree approach.

Steps:

1. Sort buses by tj in increasing order, and assign them indices 0 to n-1.

2. Build a segment tree where each node stores the min sj and max fj in its interval.

3. For each query:

   a. Binary search to find the smallest index s where buses[s].tj >= bi. Let's call this s.

   b. If s >=n, output -1.

   c. Else, query the segment tree for the earliest index in [s, n-1] where sj <= li and fj >= ri.

   d. If found, output the original bus index. Else, -1.

Now, the key is to implement the segment tree query correctly.

Let's proceed to code.

First, the segment tree node structure.

But in Python, we can represent the segment tree using a list. Each node will store the min sj and max fj for its range.

But for a segment tree in Python, the standard approach is to use a list where each node is represented by an index, and the children of node i are 2i+1 and 2i+2. However, for large n (1e5), this approach can be memory-intensive, but manageable.

Alternatively, we can implement a more efficient segment tree using a class-based approach.

But for the purposes of code brevity and efficiency, perhaps the recursive approach is easier to implement.

Let's outline the code:

Sort the buses by tj, store their sj, fj, and original index.

Build a segment tree where each node stores min_sj and max_fj.

Implement the query function to find the earliest index in [s, n-1] where sj <= li and fj >= ri.

Now, code for the segment tree.

Wait, but building a segment tree for n=1e5 may take O(4n) space, which is acceptable.

But in Python, recursion depth can be a problem. For n=1e5, the recursion depth could be log2(1e5) ≈ 17, which is manageable.

So, the code steps:

- Read n and m.

- Read n buses: s, f, t. Store along with their original index (1-based). Then sort these by t in increasing order.

- Read m queries: l, r, b. Store along with their original index.

- For each query, perform a binary search on the sorted buses to find the first bus with t >=b. Let's call this s.

- Then, query the segment tree in the range [s, n-1] to find the earliest index where sj <= l and fj >= r.

- If such an index exists, the answer is the original index of that bus. Else, -1.

Implementing the segment tree:

The segment tree is built over the sorted buses. Each node represents a range [l, r]. For each node, min_sj is the minimum of the sj in the range, and max_fj is the maximum of the fj in the range.

The query function for the segment tree will traverse the tree and find the earliest index in the query range that satisfies the conditions.

Here's the code for the segment tree:

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.min_sj = [0]*(4*self.n)
        self.max_fj = [0]*(4*self.n)
        self.data = data
        self.build(0, 0, self.n-1)

    def build(self, node, l, r):
        if l == r:
            self.min_sj[node] = self.data[l][0]
            self.max_fj[node] = self.data[l][1]
        else:
            mid = (l + r) // 2
            left_child = 2*node +1
            right_child = 2*node +2
            self.build(left_child, l, mid)
            self.build(right_child, mid+1, r)
            self.min_sj[node] = min(self.min_sj[left_child], self.min_sj[right_child])
            self.max_fj[node] = max(self.max_fj[left_child], self.max_fj[right_child])

    def query_earliest(self, l_query, r_query, li, ri, node, l_current, r_current):
        # returns the earliest index in [l_query, r_query] where sj <= li and fj >= ri, or -1 if not found
        if r_current < l_query or l_current > r_query:
            return -1
        if self.min_sj[node] > li or self.max_fj[node] < ri:
            return -1
        if l_current == r_current:
            return l_current if (self.data[l_current][0] <= li and self.data[l_current][1] >= ri) else -1
        mid = (l_current + r_current) // 2
        left_child = 2*node +1
        right_child = 2*node +2
        # Check left child first
        left_res = self.query_earliest(l_query, r_query, li, ri, left_child, l_current, mid)
        if left_res != -1:
            return left_res
        # If left child has no answer, check right child
        right_res = self.query_earliest(l_query, r_query, li, ri, right_child, mid+1, r_current)
        return right_res

But wait, the way the query_earliest function is implemented, it checks the left child first, then the right child. Since the left child covers the earlier part of the array (since the data is sorted by tj in increasing order), this will return the earliest possible index that meets the conditions.

Yes, because the left child's range is before the right child's range. So if the left child's range contains a valid bus, the earliest one will be in the left child.

Thus, this query_earliest function will correctly return the earliest index in the query range that satisfies the conditions.

Now, putting it all together.

Read the input:

n, m = map(int, input().split())
buses = []
for i in range(n):
    s, f, t = map(int, input().split())
    buses.append( (t, s, f, i+1) )  # store tj first for sorting

Sort the buses by tj:

buses.sort()

Then, create the data for the segment tree. Each element is (s, f, original_index). Wait, no. The sorted buses list is sorted by tj. For each bus in this list, we need to store s, f, and original index.

Wait, after sorting, each bus in the list has tj in increasing order. So for the segment tree, the data array will be a list of tuples (s, f), since for each bus, we need to track sj and fj.

So:

data = [ (s, f) for (t, s, f, idx) in sorted_buses ]

Wait, no. The buses are sorted by tj. So:

sorted_buses = sorted(buses, key=lambda x: x[0])

Then, data is:

data = [ (s, f) for (t, s, f, idx) in sorted_buses ]

Then, build the segment tree with this data.

For each query:

li, ri, bi = ... 

We need to find the earliest bus in the sorted list where tj >= bi, s <= li, and f >= ri.

First, find the start index s using binary search on the sorted_buses' tj.

In Python, we can use bisect_left.

But since sorted_buses are sorted by tj, we can extract the tj list and perform a bisect.

t_list = [t for (t, s, f, idx) in sorted_buses]

s = bisect.bisect_left(t_list, bi)

if s >= n: answer is -1.

Else, query the segment tree for the range [s, n-1], passing li and ri.

If the query returns an index, then the original bus index is sorted_buses[index][3].

Else, -1.

Now, putting it all together.

But in Python, implementing the segment tree with a class and recursive functions may be too slow for 1e5 elements. Let's test.

But given the time constraints, perhaps the code can be optimized.

Alternatively, an iterative segment tree implementation could be used, but that's more complex.

Alternatively, precompute the sorted buses and their tj, and for each query, perform the binary search, then use the segment tree to find the earliest index.

Now, let's code the entire solution.

Wait, but the segment tree's query_earliest function needs to accept a query range [l_query, r_query], which is the start index and end index (n-1) of the buses list.

In the code above, the query_earliest function is designed to handle any range. So for each query, the range is [s, n-1], and the function is called with l_query = s, r_query = n-1.

But the code for the segment tree may need to be adjusted.

Let me check the parameters of query_earliest:

def query_earliest(self, l_query, r_query, li, ri, node, l_current, r_current):

This function is called recursively, checking if the current node's range [l_current, r_current] overlaps with the query range [l_query, r_query], and then proceeds to check the left and right children.

But in the initial call, we start with node 0, l_current=0, r_current =n-1.

So for example, if the query is [s, n-1], the function will check the entire tree but only return indices in that range.

This seems correct.

Testing this code with the first example:

Sample Input 1:

4 3

1 10 10

5 6 2

6 7 3

5 7 4

Queries:

5 7 1

1 2 1

1 10 11

Sorted buses by tj:

The buses are:

(2,5,6,2), (3,6,7,3), (4,5,7,4), (10,1,10,1)

So sorted by tj (2,3,4,10).

So the data array for the segment tree is:

[(5,6), (6,7), (5,7), (1,10)]

The min_sj and max_fj for the segment tree nodes will be built accordingly.

For the first query: 5 7 1. bi=1. So s is the index where tj >=1, which is 0. The query is from 0 to 3.

We need to find the earliest bus where sj <=5 and fj >=7.

Looking at the buses:

0: s=5, f=6 → fj=6 <7 → no.

1: s=6, f=7 → fj=7 >=7. s=6>5 → no.

2: s=5, f=7 → s=5<=5, f=7>=7 → yes. So index 2.

So the answer is bus 4.

Which matches the sample output.

The segment tree query would return 2 (index 2 in the sorted list), which corresponds to the original index 4.

But in the sorted_buses list, the fourth bus (original index 4) is the third in the sorted list (as per the example's input). Wait, the sample input's buses are:

Bus 1: 1 10 10 → tj=10.

Bus 2:5 6 2 → tj=2.

Bus 3:6 7 3 → tj=3.

Bus4:5 7 4 → tj=4.

Sorted by tj: bus2 (tj=2), bus3 (tj=3), bus4 (tj=4), bus1 (tj=10).

So sorted_buses is [ (2,5,6,2), (3,6,7,3), (4,5,7,4), (10,1,10,1) ]

So data is [(5,6), (6,7), (5,7), (1,10)].

For the first query (li=5, ri=7, bi=1), the s is 0. The query is [0,3]. The earliest index in this range where s_j <=5 and fj >=7 is index 2 (bus4), since:

bus0: s=5 <=5, fj=6 <7 → no.

bus1: s=6>5 → no.

bus2: s=5 <=5, fj=7 >=7 → yes. So index 2.

So the answer is the original index of sorted_buses[2], which is 4.

Yes.

Thus, the code should work.

Now, handling the queries and their original indices.

We need to read all queries, then sort them by bi, process them, then output the answers in the original order.

So, steps:

Read m queries, store as a list of tuples (bi, li, ri, original_index).

Sort the queries by bi.

Process each query in this sorted order.

For each query, perform the steps outlined, then store the answer in an array indexed by the original_index.

Finally, output the answers in the original order.

But wait, no. Because in the code outline above, the queries are processed in sorted order of bi, but the segment tree is built once, and the binary search is performed for each query's bi.

So for each query, regardless of order, we can binary search the sorted buses for the start index s, then query the segment tree.

Thus, the order in which queries are processed is irrelevant for the correctness. The only thing that matters is that the buses are sorted by tj, and the segment tree is built accordingly.

But for the code, it's more efficient to process the queries in any order, as each query is handled independently.

Thus, no need to sort the queries.

But this approach would require for each query to perform a binary search on the tj list (O(log n)), then a segment tree query (O(log n)), which is acceptable.

Thus, the code can process each query in the original order.

But in Python, with 1e5 queries and each query requiring two log n operations, this should be manageable.

Thus, the code can be written as follows:

Read the buses, sort them by tj.

Build a list of tj for binary search.

Build the segment tree.

For each query:

   binary search to find s.

   if s >=n: ans is -1.

   else: query the segment tree for the earliest index in [s, n-1] where sj <= li and fj >= ri.

   if found: ans is the original index.

   else: -1.

Store the answers in a list and output.

Thus, the code should look like:

Testing against sample input 1.

```python
import bisect


class SegmentTree:
    def __init__(self, data_sj, data_fj):
        self.n = len(data_sj)
        self.min_sj = [0] * (4 * self.n)
        self.max_fj = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1, data_sj, data_fj)
    
    def build(self, node, l, r, data_sj, data_fj):
        if l == r:
            self.min_sj[node] = data_sj[l]
            self.max_fj[node] = data_fj[l]
        else:
            mid = (l + r) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(left_child, l, mid, data_sj, data_fj)
            self.build(right_child, mid + 1, r, data_sj, data_fj)
            self.min_sj[node] = min(self.min_sj[left_child], self.min_sj[right_child])
            self.max_fj[node] = max(self.max_fj[left_child], self.max_fj[right_child])
    
    def query(self, l_query, r_query, li, ri):
        return self._query_helper(0, 0, self.n - 1, l_query, r_query, li, ri)
    
    def _query_helper(self, node, l_current, r_current, l_query, r_query, li, ri):
        if r_current < l_query or l_current > r_query:
            return -1
        if self.min_sj[node] > li or self.max_fj[node] < ri:
            return -1
        if l_current == r_current:
            return l_current if (self.min_sj[node] <= li and self.max_fj[node] >= ri) else -1
        mid = (l_current + r_current) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_res = self._query_helper(left_child, l_current, mid, l_query, r_query, li, ri)
        if left_res != -1:
            return left_res
        return self._query_helper(right_child, mid + 1, r_current, l_query, r_query, li, ri)

def main(input_stream, output_stream):
    import sys
    input = input_stream.read
    data = input().split()
    ptr = 0
    n = int(data[ptr])
    ptr +=1
    m = int(data[ptr])
    ptr +=1
    
    buses = []
    for i in range(n):
        s = int(data[ptr])
        ptr +=1
        f = int(data[ptr])
        ptr +=1
        t = int(data[ptr])
        ptr +=1
        buses.append( (t, s, f, i+1) )  # store tj, sj, fj, original index
    
    # Sort buses by tj
    buses.sort()
    # Prepare data for segment tree
    data_sj = []
    data_fj = []
    tj_list = []
    for bus in buses:
        tj_list.append(bus[0])
        data_sj.append(bus[1])
        data_fj.append(bus[2])
    
    # Build segment tree
    st = SegmentTree(data_sj, data_fj)
    
    # Process queries
    output = [-1] * m
    for q in range(m):
        li = int(data[ptr])
        ptr +=1
        ri = int(data[ptr])
        ptr +=1
        bi = int(data[ptr])
        ptr +=1
        
        # Find first bus with tj >= bi
        s = bisect.bisect_left(tj_list, bi)
        if s >= n:
            output[q] = -1
            continue
        
        # Query the segment tree in [s, n-1]
        idx = st.query(s, n-1, li, ri)
        if idx == -1:
            output[q] = -1
        else:
            output[q] = buses[idx][3]
    
    # Print the output in the order of queries
    print(' '.join(map(str, output)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 1
1 1000000000 1000000000
1 1000000000 1000000000
""",
            "output": \
"""\
1
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

Thus, the code should work.

But wait, the data_sj and data_fj arrays are the s and f of the sorted buses.

Yes.

Thus, this code should handle the problem correctly.

Now, test the second sample input:

Input:
1 1
1 1000000000 1000000000
1 1000000000 1000000000

The bus is sorted with tj=1e9.

The query is bi=1e9.

bisect_left finds s=0.

Query the segment tree for [0,0], with li=1, ri=1e9.

The bus's s=1 <=1, fj=1e9 >=1e9 → yes. So answer is 1.

Thus, code outputs 1.

Thus, the code works.

This should handle all cases.
</think>

To solve this problem, we need to determine the earliest bus each citizen can take to reach their destination without changing buses, considering both the route coverage and the departure time constraints. 

### Approach
1. **Sort Buses by Departure Time**: We first sort all buses based on their departure times. This allows us to efficiently find the earliest possible bus for each citizen using binary search.
2. **Segment Tree for Range Queries**: We construct a segment tree to store the minimum start stop (sj) and maximum end stop (fj) for each segment of buses. This helps in quickly determining if any bus in a given range covers the required route.
3. **Binary Search for Eligible Buses**: For each citizen query, we use binary search to find the earliest bus that departs at or after the citizen's arrival time.
4. **Efficient Query Handling**: Using the segment tree, we check if there exists a bus in the identified range that covers the citizen's start and end stops. The segment tree allows us to efficiently query the minimum and maximum values required to determine route coverage.

### Solution Code
```python
import bisect

class SegmentTree:
    def __init__(self, data_sj, data_fj):
        self.n = len(data_sj)
        self.min_sj = [0] * (4 * self.n)
        self.max_fj = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1, data_sj, data_fj)
    
    def build(self, node, l, r, data_sj, data_fj):
        if l == r:
            self.min_sj[node] = data_sj[l]
            self.max_fj[node] = data_fj[l]
        else:
            mid = (l + r) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(left_child, l, mid, data_sj, data_fj)
            self.build(right_child, mid + 1, r, data_sj, data_fj)
            self.min_sj[node] = min(self.min_sj[left_child], self.min_sj[right_child])
            self.max_fj[node] = max(self.max_fj[left_child], self.max_fj[right_child])
    
    def query(self, l_query, r_query, li, ri):
        return self._query_helper(0, 0, self.n - 1, l_query, r_query, li, ri)
    
    def _query_helper(self, node, l_current, r_current, l_query, r_query, li, ri):
        if r_current < l_query or l_current > r_query:
            return -1
        if self.min_sj[node] > li or self.max_fj[node] < ri:
            return -1
        if l_current == r_current:
            return l_current if (self.min_sj[node] <= li and self.max_fj[node] >= ri) else -1
        mid = (l_current + r_current) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_res = self._query_helper(left_child, l_current, mid, l_query, r_query, li, ri)
        if left_res != -1:
            return left_res
        return self._query_helper(right_child, mid + 1, r_current, l_query, r_query, li, ri)

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1
    
    buses = []
    for i in range(n):
        s = int(input[ptr])
        ptr += 1
        f = int(input[ptr])
        ptr += 1
        t = int(input[ptr])
        ptr += 1
        buses.append((t, s, f, i + 1))
    
    buses.sort()
    tj_list = []
    data_sj = []
    data_fj = []
    for bus in buses:
        tj_list.append(bus[0])
        data_sj.append(bus[1])
        data_fj.append(bus[2])
    
    st = SegmentTree(data_sj, data_fj)
    
    output = []
    for _ in range(m):
        li = int(input[ptr])
        ptr += 1
        ri = int(input[ptr])
        ptr += 1
        bi = int(input[ptr])
        ptr += 1
        
        s = bisect.bisect_left(tj_list, bi)
        if s >= n:
            output.append("-1")
            continue
        
        idx = st.query(s, n - 1, li, ri)
        if idx == -1:
            output.append("-1")
        else:
            output.append(str(buses[idx][3]))
    
    print(' '.join(output))

if __name__ == "__main__":
    main()
```

### Explanation
1. **Sorting Buses**: Buses are sorted by their departure time to facilitate efficient range queries.
2. **Segment Tree Construction**: The segment tree is built to store the minimum start stop and maximum end stop for each segment, enabling quick checks for route coverage.
3. **Binary Search**: For each citizen query, we use binary search to find the earliest possible bus that departs after their arrival time.
4. **Efficient Range Query**: The segment tree allows us to efficiently check if any bus in the identified range covers the required route, ensuring optimal performance even for large input sizes.
