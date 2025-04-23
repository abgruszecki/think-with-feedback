<think>
Okay, let's tackle this problem. So, the task is to determine for each edge in a graph whether it's part of all MSTs (so it's mandatory), part of at least one MST, or not part of any. Hmm. 

First, I remember that in Krusky's algorithm, edges are considered in increasing order of weight. The algorithm adds edges that connect different components. For a given edge, whether it's included in some MST depends on the existence of other edges with the same weight that could form a cycle. 

So, the approach here is probably related to Krusky's algorithm. Let me think. 

For each edge e with weight w, whether it is included in any MST depends on whether there are other edges of the same weight that could form a cycle. If e is the only bridge between the two components when considering edges up to w, then it must be included in all MSTs. Otherwise, if there are other edges of the same weight that can connect those components, then it's possible to choose any of them, so the edge is in at least one MST but not all. If the edge is not part of any MST, that means even if we consider edges up to its weight, there's already a path between its endpoints with edges of lower weight, making it redundant.

So here's the plan:

1. Sort all edges by their weight.
2. Process the edges in increasing order. For each group of edges with the same weight:
   a. Use a Union-Find (Disjoint Set Union) structure to track connected components.
   b. For each edge in the group, check if connecting its endpoints would merge two different components. If not, then this edge is not in any MST (since there's already a path using smaller edges).
   c. For edges that would connect components, determine if there are multiple edges in the same group that connect the same pair of components. If there's more than one such edge, then each of them is part of at least one MST but not all. If only one edge in the group connects those components, then it's part of all MSTs (so "any").
   
But wait, how do we track this for each edge? Because during Krusky's algorithm, once you process edges of a certain weight, you add all possible edges that connect different components. So for edges in the same weight group, if multiple edges can connect the same two components, only one (or a subset) of them is needed. But how to find for each edge whether it's mandatory.

Another approach is for each group of same-weight edges, before processing them, check which edges are actually bridges in the graph formed by all edges of weight <= current weight. The bridge edges here would be the ones that must be included in every MST, because their removal would disconnect the graph. So, edges that are bridges in the graph of edges with weight <= their own weight are mandatory (any). Otherwise, if there's a cycle involving edges of the same weight, then those edges can be either included or excluded, so they are "at least one" or "none".

But calculating bridges for each possible weight group would be computationally expensive, given that the constraints are up to 1e5 edges. So that's not feasible.

Wait, maybe there's a smarter way. Let's think about Krusky's steps. When processing edges in order of increasing weight:

At each step, all edges with weight w are considered. For each such edge (u, v), we check if u and v are in different components. If they are, then adding this edge can be part of an MST. However, if there are multiple edges in this weight group that connect the same two components, then any one of them can be chosen, so these edges are not mandatory. Only edges that are the only ones in their group that connect their respective components are mandatory.

So here's the plan:

- Sort all edges by weight, and process them in order.
- For each group of edges with the same weight:
   - First, check for each edge in the group whether u and v are already connected (using the DSU structure that has processed all edges with lower weight). Those edges that are already connected are not part of any MST (they are in a cycle of edges with smaller or equal weight). So their status is "none".
   - For the edges in the group that can connect their components (u and v are in different sets), we need to determine if there are multiple edges in the same group that connect the same pair of components. If yes, then each of them is part of at least one MST. Otherwise (if the edge is the only one in the group that connects those two components), then it's mandatory (must be in all MSTs). 
   - Then, merge the components for all edges in this group that are part of some MST (i.e., those that connect two different components in the DSU). However, merging them in a way that captures all possible edges in the group that could be part of the MST.

But how to track which edges in the group are the only ones connecting their components.

So for each group of edges with the same weight w, we can:

1. For each edge in the group, check if the two endpoints are in different DSU components. If not, the edge is "none".

2. For the edges that are possible candidates (i.e., their endpoints are in different components), we need to group them by the pair of their component roots. So, for each such edge, the root of u and root of v (as per DSU before processing this group) form a key. For each key, count how many edges in the group have this key.

3. For each such key, if the count is 1, then the corresponding edge is mandatory ("any"). If the count is more than 1, then all edges in this key's group are "at least one".

4. Then, we need to merge all the components connected by edges in this group. However, since multiple edges can connect the same components, but we only need to merge once. So, perhaps we can process each unique pair of roots in the group and merge them. But how to do this efficiently.

But here's the problem: after grouping the edges by their root pairs, for each unique root pair (a, b), where a < b to avoid duplicates, we can process them. For each such pair, we need to merge a and b. But if there are multiple edges for this pair, merging once is sufficient, but all those edges can be part of the MST, depending on which ones are selected.

So during processing the group, we can:

- For all edges in the group, precompute their root pairs (sorted to avoid duplicates, like (a, b) where a < b).

- For each unique root pair in the group that is not already connected (i.e., their roots are different), merge them. But how does this affect the DSU for the next steps.

Wait, but in Krusky's algorithm, all edges of the same weight are considered together. So when processing edges of the same weight, any edge that connects two components not yet connected by lower weight edges can be part of an MST. But when there are multiple edges between two components, any one can be chosen.

So, during processing:

For each weight group:

   a. For each edge in the group, find the current root of u and v.

   b. If the roots are the same, mark the edge as "none".

   c. Else, collect the edges grouped by their (root_u, root_v), but to avoid direction, store them as (min_root, max_root).

   d. For each (a, b) in these groups, the number of edges in this group for (a, b) is the count. If the count is 1, then the edge is mandatory. If more than 1, then all edges in this group for (a, b) are "at least one".

But how do we track this for each edge.

Wait, but how do we process the edges in the group. For example, in the same (a, b) group, suppose there are two edges. Then, in the MST, only one of them can be selected. So each of these two edges is part of at least one MST (so "at least one"), but not mandatory.

So for each edge in the group, if the count of edges in their (a, b) group is 1, then it's mandatory. Otherwise, it's "at least one".

Once we determine that, then we need to merge all the (a, b) pairs. But merging (a, b) once is sufficient. So after processing the group, for all unique (a, b) pairs in the group that were not already connected, we merge them. Because once merged, any subsequent edges in the same group would have their roots in the same component.

But here's a problem: suppose during processing the group, there are multiple (a, b) pairs. For example, after merging a and b, there might be edges in the same group that connect a and c (but after a and b are merged, the root of a is now part of a larger component). Wait, no. Because when processing a group of edges with the same weight, the DSU is in the state before processing any of them. So when you process the edges in the group, all DSU find operations are done on the DSU as it was before processing the group.

So for each edge in the group, when you compute their a and b (the roots before processing the group), they are in their original components. Then, once all the edges are processed (and the DSU is updated), the next group (higher weight) will use the updated DSU.

So the steps are:

Sort all edges in increasing order of weight.

Initialize DSU.

Sort the edges in the input by weight.

Then, for each group of edges with the same weight:

   - For each edge in the group:

      - Find the roots of u and v in the DSU (before processing this group).

   - Separate the edges into two categories: those where roots are the same (they are "none"), and those where roots are different.

   - For the edges with roots different, group them by their (a, b) pairs (sorted to a <= b).

   - For each (a, b) group:

      - If the number of edges in this group is 1: then that edge is "any".

      - Else: all edges in this group are "at least one".

   - Then, for each (a, b) in the group, we need to merge a and b in the DSU, but only once per (a, b) pair. Because once merged, any other edges in the same group with (a, b) would now have the same roots.

Wait, but merging (a, b) in the DSU may affect other edges in the same group. However, since all edges in the group are processed based on the DSU state before any of them are processed, merging (a, b) for the first time would affect subsequent edges in the group. But no, because during processing the group, the DSU is not modified until all edges in the group have been processed.

Wait, no. Because the DSU is modified as part of processing the group. But in Krusky's algorithm, all edges in the group are considered, and any that connect two components are added. However, when multiple edges in the same group connect the same components, you can choose any one. So for processing, after considering all edges in the group, you would merge all the possible pairs. But how?

Alternatively, during processing a group, you first collect all the (a, b) pairs (from the roots before processing the group). Then, for each (a, b) pair, you check if a and b are in different components (which they are, since we processed all edges in lower weights). Then, for each such (a, b), if you merge them, but how to handle multiple edges in the same group.

Wait, no. The DSU starts in a state where all edges with lower weights have been processed. When processing the current group of edges, the DSU is in the state after processing lower edges. For each edge in the current group, the a and b are the roots before processing the current group. So for edges in the same group, their a and b are determined before any merging in the group.

Thus, the merging must be done after processing all edges in the group. So for each (a, b) pair in the group (from the roots before processing), we can collect all such pairs. Then, for each unique (a, b) pair (sorted), we need to merge a and b. But even if there are multiple edges for the same (a, b) pair, merging once is sufficient. Because once merged, any subsequent edges in the same group (but with the same a and b) would have roots that are the same.

But in reality, when you have multiple edges in the same group that connect the same two components (same a and b), you can choose any one of them. So merging a and b once for each such pair.

So, here's the plan:

For each edge in the group, compute a and b (roots before processing). Then, for edges where a != b:

   - Group them by (a, b) (sorted as a <= b).

   - For each group of edges in the same (a, b) pair:

      - If the size of the group is 1: the edge is "any".

      - Else: all edges in the group are "at least one".

   - Then, for each unique (a, b) pair in this group, merge a and b in the DSU. This is done once per (a, b) pair.

Thus, the merging step is done for each (a, b) pair once, regardless of the number of edges in the group for that pair.

Now, the key steps are:

1. Sort all edges by weight, and process them in order.

2. For each group of edges with the same weight:

   a. For each edge in the group, compute a and b (the roots of u and v in DSU before processing the group).

   b. For edges where a == b: mark as "none".

   c. For edges where a != b: group them by (a, b) pairs (sorted to avoid direction issues).

   d. For each such group:

      i. If the group has exactly one edge: mark as "any".

      ii. Else: mark all edges in the group as "at least one".

   e. For each (a, b) pair in the groups (unique ones), merge a and b in the DSU.

But how to track which edges are in which group, considering that edges are processed in the group. So the steps would be:

- Process edges in order of increasing weight. For each group:

   - Collect all edges in the current group.

   - For each edge in this group, find a and b (roots before processing the group).

   - For each edge, if a and b are same: output "none".

   - Else, collect the (a, b) pairs (sorted) and map each edge to its (a, b).

   - For each (a, b) group in this collection:

      - Count how many edges are in this group.

   - Then, for each edge in the group:

      - If a == b: none.

      - Else, check if the count for (a, b) group is 1. If yes: "any". Else: "at least one".

   - After processing all edges in the group, merge all (a, b) pairs (once per pair). Because once merged, the next group will have the updated DSU.

So, the problem is how to track, for each edge in the original input, what its status is. Because the edges are processed in sorted order, but the original order is needed for output.

Wait, but the edges are given in the input in arbitrary order, and we need to output the answers in the order of the input. So the approach must process all edges first, possibly in a different order, but keep track of their original positions.

So, the plan is:

- Read all edges, and store their original indices.

- Sort the edges by weight, then process them in order. For each edge in the sorted list, during processing, determine its status and record it. Then, after processing all edges, output the results in the original order.

But the problem is that during processing, the edges are grouped by weight, but their original indices are needed to map back to the correct output order.

Yes. So, the steps would be:

1. Read all edges, along with their original index (0-based or 1-based? Probably 0-based as in the input order). So, for example, when the input is read, each edge is stored as (a, b, w, index).

2. Sort the edges by weight in increasing order, then by any other criteria (since same weight edges can be grouped).

3. Process the edges in sorted order, grouping them by their weight.

4. For each group, process as described, and for each edge in the group, determine the status (any, at least one, none) and store it in an array indexed by the original index.

5. After processing all edges, output the stored statuses in the order of original indices.

So, the main challenge is handling the original indices correctly.

Now, let's think about the data structures:

- We need a DSU (Union-Find) structure with path compression and union by rank to handle the operations efficiently.

- For each edge in the original input, we need to remember its weight and its original position.

So, during the initial processing:

edges = []
for i in range(m):
    a, b, w = map(int, input().split())
    edges.append( (w, a-1, b-1, i) )  # assuming 0-based vertices.

Then, sort the edges by weight, and then group them by weight.

But grouping can be done by iterating through the sorted list and creating a list for each weight.

Once grouped, for each group:

current_weight = edges[0][0]
group = []
for edge in sorted_edges:
    if edge[0] == current_weight:
        group.append(edge)
    else:
        process group here.

But in code, it's easier to process each group in a loop.

But perhaps, using a pointer approach. For example, sorted_edges is the list sorted by weight. Then, i starts at 0, and for each i, find j such that sorted_edges[i ... j] have the same weight. Then, process that group, and set i = j+1.

Once the group is collected, for each edge in the group:

   a. Check the DSU for a and b's roots (before processing the group).

   b. If roots are the same, mark as none.

   c. Else, collect in a dictionary grouped by (a, b) pairs (sorted).

Then, for each (a, b) group in the dictionary:

   if len(edges_in_group) == 1: each edge in the group is marked as "any"

   else: each edge is marked as "at least one"

Then, after processing all edges in the group, merge (a, b) in DSU for each (a, b) key in the dictionary.

Wait, but merging (a, b) may not be necessary. Because merging (a, b) once is sufficient for the group. Because once merged, any other edges in the same group that belong to (a, b) would have a and b in the same component in the DSU.

But during the processing of the group, the DSU is not modified until after all edges in the group have been processed. So the roots are computed based on the DSU state before processing the group.

Once the edges are processed, the DSU is updated by merging all (a, b) pairs (from the roots before processing) that were part of the group and marked as part of the MST.

Thus, the merging should be done for each (a, b) pair in the group's dictionary (the keys of the dictionary). So for each key in the dictionary, we perform a union(a, b) once.

This way, all edges that contributed to merging in the group are accounted for, and the DSU is updated for the next groups.

So the code outline would be:

Initialize DSU.

result = [None] * m  # to hold the output for each edge.

sorted_edges = sorted( (w, a, b, idx) for (a, b, w, idx) in edges )

i = 0
while i < m:
    current_weight = sorted_edges[i][0]
    j = i
    while j < m and sorted_edges[j][0] == current_weight:
        j += 1
    group = sorted_edges[i:j]

    # Process the group.
    # For each edge in the group, find their roots in DSU before processing.
    # So, process all edges in the group first, then do the merging.

    # First, collect for each edge in group their a and b roots.
    edge_roots = []
    for edge in group:
        w, a, b, idx = edge
        root_a = dsu.find(a)
        root_b = dsu.find(b)
        edge_roots.append( (root_a, root_b) )

    # Now, for each edge in group, check if roots are same.
    # Then, group by (min_root, max_root).
    groups_dict = defaultdict(list)
    none_list = []
    for k in range(len(group)):
        edge = group[k]
        ra, rb = edge_roots[k]
        if ra == rb:
            result[edge[3]] = 'none'
        else:
            # group by (min, max)
            if ra < rb:
                key = (ra, rb)
            else:
                key = (rb, ra)
            groups_dict[key].append( (edge, k) )

    # Now, process the groups_dict.
    # For each key in groups_dict, check the number of edges.
    # For each edge in the group, if the count is 1, mark as 'any', else 'at least one'.
    for key in groups_dict:
        edges_in_group = groups_dict[key]
        if len(edges_in_group) == 1:
            # only one edge, mark as 'any'
            for (edge, k) in edges_in_group:
                result[edge[3]] = 'any'
        else:
            # multiple edges, mark as 'at least one'
            for (edge, k) in edges_in_group:
                result[edge[3]] = 'at least one'

    # Now, merge all the keys in groups_dict.
    # For each key (a, b), union a and b.
    for key in groups_dict:
        a, b = key
        dsu.union(a, b)

    i = j

# After processing all groups, output the result in order.

Then, print each line of the result in the order of original indices.

Wait, but what about edges that are in the group and are part of a group where their (a, b) key has multiple edges. For example, two edges in the same (a, b) key. Then, merging a and b once is sufficient, because after that, any other edges in the same group would have a and b in the same component (but since they were processed based on the DSU state before merging, their a and b were different, but the group is part of the same processing step).

But during processing, after merging a and b once, the next edges in the same group would have their a and b roots as the same (since the DSU was modified), but those edges are not part of this group's processing. Because the group is processed in a single step, and the DSU is modified after all edges in the group are processed.

So the code should work.

Now, let's test this approach against the sample inputs.

Sample Input 1:

4 5
1 2 101
1 3 100
2 3 2
2 4 2
3 4 1

The edges sorted by weight:

Edge 4: 3-4 w=1 → sorted first.

Then edges 2,3,4 (original indices 2,3,4) with w=2.

Then edges 0,1 with w=100, 101.

Processing the group with w=1: edge (3-4, w=1, index 4). Check their roots. Initially, all nodes are separate. So roots are 3 and 4 (assuming 0-based nodes). So (3,4) group. Since count is 1, mark as 'any'. Then merge 3 and 4. Now, DSU has 3 and 4 in same set.

Next group is edges with w=2. The edges in the group are:

Edge 2: 2-3 (original nodes 1-2, since input is 1-based converted to 0-based). So their roots are 1 and 2 (original nodes 2 and 3, converted to 1 and 2? Wait, initial code converts a and b to 0-based. So original a and b in input 1,2,3,4 become 0,1,2,3.

So edge 2: original input is 2 3 2 → converted to 1-2 (0-based). So their roots before processing this group are 1 and 2 (since in DSU, after processing the first group, 3 and 4 are merged. So nodes 2 and 3 are in different components. So roots are 1 and 2.

Processing this edge: the roots are 1 and 2. So group (1,2). Next edge in this group is 2-4 (original input 2 4 → 1 and 3). Their roots are 1 and 3 (since after first group, 3 and 4 are merged, but 3's root is 3 (since DSU for 3 and 4 was merged, so find(4) gives 3, but find(3) is 3. So root for 3 is 3. So for edge 3 (input 2 4 → 1 and 3), roots are 1 and 3. So group (1,3). Then edge 3-4 (input 3 4 → 2 and 3). Their roots are 2 (for 3 is in the merged set with 3 and 4? Wait, initial DSU after first group (w=1):

- The first edge is 3-4 (0-based 2 and 3?), no. Wait, original input is 3-4 → converted to 2 and 3. So their roots are 2 and 3. So after merging, they are in the same set, root is 2 (if union by rank). So during processing the next group (w=2), the DSU for 2 and 3 would be 2. So for edge 2 (input 2-3 → 1-2), the roots are 1 and 2. So group (1,2). Edge 3 (input 2-4 → 1-3): roots 1 and 3. Edge 4 (input 3-4 → 2-3): roots are 2 (for 2) and 3 (find(3) is 2? No, after merging 2 and 3? Wait, no. Wait, after processing the first group (w=1) which is edge 3-4 (original nodes 3 and 4 → 2 and 3 in 0-based). So DSU after processing this edge: 2 and 3 are merged.

Then, during processing the next group (w=2), the edges in the group are:

Edge 2 (original index 2): 1-2 (0-based a=1, b=2). Their roots before processing the group are 1 and 2. So group (1,2).

Edge 3 (original index 3): 1-3 (a=1, b=3). Their roots are 1 and 2 (since 3's root is 2 after merging in previous step). So group (1,2).

Edge 4 (original index 4): 2-3 (a=2, b=3). Their roots are 2 and 2 (since after merging in previous step, 3's root is 2). So this edge is 'none' (roots are same). So marked as 'none'.

So in the group for w=2, the edges are:

Original index 2 (edge (1-2, w=2)), index3 (1-3, w=2), index4 (2-3, w=2). Wait, original input has edges:

Input lines after the first two:

3: 2 3 2 → a=1, b=2 (0-based).

4: 2 4 2 → a=1, b=3 (0-based).

5: 3 4 1 → but that's the first group. So for the w=2 group:

Original edges are:

Line 3: 2 3 2 → 1-2 (0-based).

Line 4: 2 4 2 → 1-3.

Line 5: 3 4 1 → processed earlier.

Wait, the first sample's input is:

4 5

Lines:

1 2 101 → a=0, b=1, w=101.

1 3 100 → a=0, b=2, w=100.

2 3 2 → a=1, b=2, w=2.

2 4 2 → a=1, b=3, w=2.

3 4 1 → a=2, b=3, w=1.

So sorted edges by weight:

w=1: edge (3-4, which is 2 and 3 in 0-based) → index 4.

w=2: edges 2,3 (indices 2,3): (1-2, w=2) and (1-3, w=2).

w=100: edge 1 (index 1).

w=101: edge0 (index0).

So in the group for w=2, the edges are indices 2 and 3 (original input lines 3 and 4).

Processing this group:

For each edge in the group:

Edge index2 (original input line3: 2-3 → a=1, b=2). DSU before processing this group: after processing w=1's edge (3-4, which is 2 and 3, merged into same component). So for a=1 and b=2 (edge index2), their roots are 1 and 2 (since DSU for 1 is 1, for 2, find gives 2 (since in the first group, we merged 2 and 3? Wait, the first group's edge is 3-4 (input line5: 3 and4, which are 2 and 3 in 0-based). So after processing that edge, DSU for 2 and3 is merged. So for example, find(2) is 2 (if union(2,3) merged 2 as the parent of 3). So during processing the group with w=2, the DSU for edge index2 (a=1 and b=2) is:

root_a = 1 (since 1 has not been merged yet).

root_b = 2 (since 2 is merged with 3).

So the pair is (1, 2). Since 1 < 2, key is (1,2). For edge index3 (a=1, b=3 in 0-based), find(3) is 2. So root_a =1, root_b=2. Key is (1,2). So both edges in this group are in the same key (1,2). So group count is 2. So both are marked as 'at least one'.

Then, after processing, merge (1,2) once. So now, the DSU has 1,2,3,4 merged (since after merging 1 and 2 (the root 2), then 2 is already merged with 3 (from previous step). Wait, no. Let me think.

The DSU after processing the first group (w=1) is:

- Nodes 2 and3 are merged. So find(2) = 2, find(3) = 2.

Then, during processing the group w=2:

The edges are (1,2) and (1,3) → which in DSU terms, their roots before processing the group are 1 and 2 (for the first edge, a=1, b=2 → roots 1 and 2). For the second edge, a=1, b=3 → roots 1 and 2 (since 3's root is 2).

So both edges are part of the key (1,2). So group count is 2 → both marked as 'at least one'.

Then, after processing this group, we merge 1 and 2. Now, the DSU's root for 1 is 2 (assuming union by rank), and 2's root is itself. Then, the next group (w=100 and w=101) will have DSU with 1,2,3,4 merged with 2 as root.

So the edges with w=100 and w=101 (indices1 and 0) are processed next. For these edges:

Edge index1: a=0, b=2. Find(0) is 0, find(2) is 2. But in the DSU, 2 is merged with 1, but 0 is separate. So roots are 0 and 2. So group key (0,2). But in the group, count is 1. So marked as 'any'.

But wait, when the group for w=100 is processed, after the DSU has merged 1,2,3,4 into 2 (since they were merged in the w=2 group). Then, the edge (0,2) (a=0, b=2) has roots 0 and 2. So key (0,2). Count is 1. So marked as 'any'.

But the correct output for the first sample is:

none → edge0 (w=101) is not in any MST. Edge1 (w=100) is in some MST. Let's see.

Wait, in the first sample's output:

The output for edge1 (the second input line) is 'none'? Wait, the first sample's output is:

none

any

at least one

at least one

any

Hmm. Let me see:

Sample input lines:

1 2 101 → index0.

1 3 100 → index1.

2 3 2 → index2.

2 4 2 → index3.

3 4 1 → index4.

The edges sorted by weight:

index4 (w=1) → output 'any'.

index2 (w=2) → output 'at least one'.

index3 (w=2) → output 'at least one'.

index1 (w=100) → output 'none'? Or 'at least one'?

Wait, according to the first sample output, the second edge (index1) is 'none'? But according to the output given, the second line (edge1) is 'none', but according to our code's processing, perhaps not.

Wait, the first sample's output is:

none → edge0.

any → edge4 (w=1).

at least one → edge2.

at least one → edge3.

any → edge4.

Wait, no, the first sample's output is:

none

any

at least one

at least one

any

Which corresponds to the five edges in the input order. So edge0 (w=101) is none. Edge1 (w=100) is any. Edge2 (w=2) is at least one. Edge3 (w=2) is at least one. Edge4 (w=1) is any.

Wait, no. Let's recheck.

Sample input's output:

Output lines:

none → edge0.

any → edge1.

at least one → edge2.

at least one → edge3.

any → edge4.

But according to the code's processing:

After processing the group w=1 (edge4), the code marks it as 'any'.

Then, group w=2: edges2 and3. Both are in key (1,2) → count 2, marked as 'at least one'.

Then, group w=100: edge1 (a=0, b=2, w=100). Check their roots: before processing this group, the DSU after processing previous groups:

After w=2's group, we merged (1,2). So the DSU now has 1 and2 merged. Also, after w=1's group, 2 and3 merged. So 1,2,3,4 (since 3 and4 are merged in w=1's group) are all connected.

So for edge1 (0-based a=0 and b=2 → which is 1 and3 in the input? Wait, no. Original input for edge1 is 1 3 100 → 0-based a=0, b=2.

In the DSU after processing groups w=1 and w=2:

- Nodes 0 is separate.

- Nodes1,2,3,4 are connected.

So when processing group w=100 (edge1):

roots of a=0 and b=2 → 0 and 2 (since 2's root is in the merged component. For example, after merging 1 and2 in the w=2 group, the root of 2 is merged into 1's set. But how the DSU is structured depends on the union by rank. Let's assume that during the group processing for w=2, the key (1,2) is merged. So dsu.union(1, 2). Since 1 and2 were roots of different sets, the DSU would merge them into one set. So, after that, the root of 2 would be 1 (if 1's rank is higher) or whatever. 

So, when processing edge1 (w=100), which is a=0 and b=2 (0-based), the roots are 0 and 2 (since in the DSU after processing w=2's group, 2's root is now merged into 1's set. So for example, find(2) would return the root of the merged component (which could be 1). So for edge1's a=0 and b=2:

root_a is 0 (since 0 hasn't been merged).

root_b is 1 (if the merged component's root is 1).

So the key is (0,1). Since it's a single edge in this group (w=100), this key's count is 1. So edge1 is marked as 'any'.

But in the sample output, edge1 (input line2) has output 'any'?

No. Wait, the sample output's first line is none (edge0), the second line (edge1) is 'any'? Let's look.

Sample input:

4 5

1 2 101 → edge0.

1 3 100 → edge1.

2 3 2 → edge2.

2 4 2 → edge3.

3 4 1 → edge4.

Sample output:

none → edge0.

any → edge1.

at least one → edge2.

at least one → edge3.

any → edge4.

Wait, the output lines are:

Line 0: none (edge0).

Line1: any (edge1).

Line2: at least one (edge2).

Line3: at least one (edge3).

Line4: any (edge4).

But according to our code's processing:

For edge1 (w=100):

During processing group w=100, which is edge1. Check roots of a=0 and b=2. What are those roots?

At that point, the DSU has:

After processing group w=1 (edge4): nodes 2 and3 are merged.

After processing group w=2 (edges2 and3): merged (1 and2), so nodes 1 and2 are merged. Also, node3 is merged with 2 (from group w=1), so nodes 1,2,3,4 are all connected.

So when processing edge1 (w=100), a=0 and b=2. The roots are 0 and 1 (since node2's root is 1, as per merging 1 and2).

So key is (0,1). Count is 1. So marked as 'any'.

Then, merge 0 and1. So in the DSU, after this, the entire graph is connected.

Then, processing the group w=101 (edge0: a=0, b=1). The roots are 0 (now merged with1) and1. So same roots. So edge0 is marked as 'none'.

So the code would mark edge0 as 'none', edge1 as 'any', edges2 and3 as 'at least one', edge4 as 'any'. Which matches the first sample's output.

Thus, the code seems to handle this case correctly.

Now, let's think about the third sample input where all edges are in at least one MST. For example, three edges of weight 1. So any two can be chosen. So all edges are 'at least one'.

In the code:

The group for w=1 has all three edges. For each edge in the group, check their roots (initially all separate).

For edge1 (a=0, b=1): roots 0 and1. Key (0,1). For edge2 (a=1, b=2): roots 1 and2. Key (1,2). For edge0 (a=0, b=2): roots 0 and2. Key (0,2). So each edge is in their own key group. But after processing:

- For edge0, the key is (0,2) → count 1 → marked as 'any'.

Wait, but this is not correct. Because the group has three edges of weight 1. But when processed, each edge is part of their own key group. So in the code, each key group has one edge, so they are all 'any'. But according to the third sample, all edges are 'at least one'.

Hmm. That's a problem. So the code's current approach would mark all edges as 'any', but the correct output is 'at least one' for all. So what's wrong here?

Third sample input:

3 3

1 2 1 → edge0.

2 3 1 → edge1.

1 3 1 → edge2.

So in sorted order, all edges are processed in the same group (w=1).

Processing this group:

Each edge is considered. For each edge, find roots before processing the group.

Initially, all nodes are separate. 

For edge0: a=0, b=1 → roots 0 and1. Key (0,1). Count 1 → marked as 'any'.

For edge1: a=1, b=2 → roots1 and2 → key (1,2). Count1 → marked as 'any'.

For edge2: a=0, b=2 → roots0 and2 → key (0,2). Count1 → marked as 'any'.

Then, merge (0,1), (1,2), (0,2).

But during the merging, after the first merge (0,1), then merging (1,2) would connect 0,1,2. Then merging (0,2) would do nothing, since they are already connected.

But according to the code's processing, all three edges are marked as 'any', but according to the sample, they are all 'at least one'.

So the code would give an incorrect output for this case.

Ah, this is a problem.

Wait, what's wrong here?

In this case, any two edges form an MST. So each edge is part of at least one MST. However, according to the code's logic, since each edge is the only one in their key group (each connects a different pair of components), they are marked as 'any'. But this is incorrect.

So the code's logic is flawed. So what's the mistake?

Ah, the code's current approach groups edges by their (a, b) pairs (the roots before processing the group). But when processing edges that form a cycle when added together, the code's logic is not capturing that.

For example, in the third sample, the edges form a triangle. When processed as a group:

Initially, all nodes are separate.

The first edge in the group (say, edge0) connects 0 and1. Marked as 'any'. Then, merging 0 and1.

The second edge (edge1) connects 1 and2. Their roots are 0 (since 1 is now merged with0) and2. Key (0,2). Count 1 → marked as 'any'. Merging 0 and2.

Now, the third edge (edge2) connects 0 and2. Their roots are 0 and0 (since after merging 0 and2). So marked as 'none'.

But this is incorrect.

Wait, no. Because during processing the group, the code processes all edges in the group based on the DSU state before any of them are processed. So in the third sample, all three edges are processed in the same group (w=1). For each edge:

Edge0 (0-1): roots 0 and1. Key (0,1). Count 1 → 'any'.

Edge1 (1-2): roots 1 and2. But since the DSU is not modified yet (all edges are processed based on DSU before processing the group), their roots are 1 and2. Key (1,2). Count1 → 'any'.

Edge2 (0-2): roots 0 and2. Key (0,2). Count1 → 'any'.

Then, after processing all edges in the group, the code merges all the keys:

- (0,1) → merged.

- (1,2) → merged.

- (0,2) → merged.

But merging (0,1), then (1,2) would connect 0,1,2. Then merging (0,2) would have no effect.

But according to the code's logic, all three edges are marked as 'any', but in reality, each of them can be part of some MST but not all. For example, the MST can choose edge0 and edge1, or edge0 and edge2, or edge1 and edge2. So all edges are 'at least one'.

But according to the code's current approach, each edge is marked as 'any' because they are the only ones in their key groups. But this is incorrect.

So the code's logic is incorrect. The error arises because the code assumes that each edge in a key group with count 1 is mandatory. However, when multiple edges in the same weight group connect different components that can be merged in different orders, those edges may not be mandatory.

The problem is that the code's approach groups edges based on their (a, b) pairs (roots before processing the group). But when multiple edges in the same group can connect different components in a way that allows for multiple MSTs, the code fails to account for this.

So what's the correct way to determine if an edge is mandatory?

An edge e is mandatory if and only if it is a bridge in the graph formed by all edges with weight ≤ e's weight, and there are no other edges with the same weight as e that can connect the same components.

Alternatively, after considering all edges with weight less than e's weight, e is the only edge with weight equal to e's weight that can connect the two components.

So the code's approach is to check if, in the current group (same weight), the edge is the only one that connects its two components (as determined by the DSU state before processing the group). If yes, then it's mandatory. But in the third sample, all three edges are processed in the same group, and each has a unique (a, b) pair, but their inclusion in the MST depends on the order in which they are processed.

Wait, but Krusky's algorithm adds edges in order of increasing weight. For edges of the same weight, the order may vary. But any of the edges can be chosen as long as they connect components.

So, in the third sample, when processing the group of weight 1 edges:

- The DSU starts as all separate.

- All three edges are in the same group.

- When processing the first edge (say, edge0), it connects components 0 and1. Since there's only one edge in this (0,1) group, it's marked as 'any'.

- Then, processing the second edge (edge1) connects components 1 and2. Marked as 'any'.

- Then, processing the third edge (edge2) would connect components 0 and2. But after merging 0 and1, and then 1 and2, the third edge's roots are 0 and2 (which are in the same component). So edge2 is marked as 'none'.

So according to this order, edge0 and edge1 are marked as 'any', edge2 is 'none'. But this is incorrect, as the sample expects all edges to be 'at least one'.

So the code's approach is incorrect because the order in which edges are processed within the group affects the outcome. But the code's logic groups edges by their (a, b) pairs (roots before processing the group) and marks them as 'any' if they are the only ones in their group, but this is not sufficient.

So the correct approach must consider that even if multiple edges in the same group connect different pairs of components, but collectively form a way to merge components that could allow different combinations, then those edges are 'at least one' rather than 'any'.

So the mistake is that the current approach groups edges by their (a, b) pairs, but in reality, edges can connect different components but still form a cycle when considered together.

Thus, the solution requires a different approach. 

Alternative approach:

The correct way to determine if an edge is mandatory is to check if the edge is a bridge in the graph formed by all edges with weight less than or equal to its weight. If it is a bridge, then it must be part of all MSTs. Otherwise, if there's at least one other edge with the same weight that can connect the same components, then it can be part of at least one MST. If it's not a bridge and there are no other edges in its weight group that can connect the same components, then it's not part of any MST.

But computing bridges for all possible subgraphs is computationally expensive. 

An alternative approach inspired by Tarjan's algorithm for bridges:

For each group of edges with the same weight, we can model them as part of a graph where all edges with weight <= current weight are considered, but the current group is the only ones with weight equal to current weight. The edges in the group are bridges in this graph if and only if they are mandatory.

But how to compute this efficiently.

An alternative approach is to use Krusky's algorithm and, for each group of edges with the same weight, to determine if any of the edges in the group are bridges in the current DSU state.

Wait, when processing edges in increasing order, after processing all edges with weight less than current, the DSU represents the components formed by those edges. The current group's edges have weight w. For each edge in the group, if the edge connects two components in the DSU (before processing this group), then it's part of some MST. For such edges, if there is at least one other edge in the same group that also connects the same two components (a and b in the DSU), then all such edges are optional (can be part of some MST but not all). If it's the only edge connecting a and b in the group, then it's mandatory.

But this is exactly what the code's current approach does. But in the third sample, this approach fails because the edges are processed in the same group but connect different pairs of components.

So why is the third sample's case failing?

In the third sample, all three edges are in the same group (w=1). Each edge connects a different pair of components. So each edge is the only one in its (a, b) group. So according to the code, each is marked as 'any'. But the correct answer is 'at least one' for all edges.

Ah, I see. Because in reality, any two edges form a spanning tree. So each edge is part of at least one MST, but not all. So the code's current logic is incorrect.

So what's the problem here?

The code's logic assumes that if an edge is the only one in its (a, b) group, then it's mandatory. But in the third sample, each edge's (a, b) group is unique, but after processing some edges, the other edges may no longer connect different components.

But the code's approach is to process all edges in the group based on the DSU state before processing the group. So all edges in the group are processed based on the same DSU state.

So in the third sample's case:

All three edges are processed in the same group. For each edge:

- For edge0 (0-1), the DSU before processing the group is all separate. So roots 0 and1. Key (0,1). Count 1 → 'any'.

- For edge1 (1-2), roots 1 and2. Key (1,2). Count1 → 'any'.

- For edge2 (0-2), roots0 and2. Key (0,2). Count1 → 'any'.

But the correct answer is that all three edges are part of at least one MST, but none are part of all MSTs. So the code's logic is incorrect.

The mistake is that the code's logic doesn't consider that once edges are merged, other edges in the same group may connect components that were merged by previous edges in the group.

But since the code's processing is based on the DSU state before the group is processed, it's possible that multiple edges in the same group connect different pairs of components, but the merging of some components allows others to form a cycle.

For example, in the third sample, the code's approach would merge (0,1), (1,2), (0,2) based on the group's edges. But after merging (0,1) and (1,2), the component 0-1-2 is connected, so merging (0,2) is unnecessary (and thus edge2 is part of an MST only if it's chosen before edge0 and edge1).

But the code's logic marks all three edges as 'any', which implies that they are all part of every MST, which is not true.

So the code's logic is incorrect.

Thus, the approach of grouping edges by their (a, b) pairs in the DSU before processing the group is not sufficient. 

Alternative idea:

An edge e is part of some MST if and only if when considering all edges with weight less than e's weight, e connects two different components. 

An edge e is part of all MSTs if and only if, when considering all edges with weight less than e's weight, e is the only edge with weight <= e's weight that connects its two components.

Wait, no. Because even if there are other edges with the same weight as e that connect the same components, but those edges are not part of the current group (e's weight), then e may still be mandatory.

Alternatively, the edge e is mandatory if and only if, in the DSU state after processing all edges with weight less than e's weight, e is the only edge in its weight group that connects its two components.

Which brings us back to the initial code's approach.

But in the third sample, each edge is part of the same group (weight 1), and each edge's a and b are different in the DSU state before processing the group (all separate). So each edge is in its own key group. Thus, according to the code's logic, each edge is mandatory, but in reality, they are not.

So why is this the case?

Because even though each edge is the only one in their key group, the combination of edges can form cycles. For example, choosing any two edges forms a cycle, but since the third edge is not in the MST, it's not part of all MSTs.

But in the code's logic, after processing the group, all three edges are merged into the DSU, but the code's merging step for each key group may merge multiple components.

Wait, for the third sample's group processing:

The code processes all three edges as follows:

For each edge:

- Edge0: key (0,1), count 1 → 'any'.

- Edge1: key (1,2), count1 → 'any'.

- Edge2: key (0,2), count1 → 'any'.

Then, for each key in groups_dict (three keys: (0,1), (1,2), (0,2)), merge the pairs.

So, during merging:

First merge (0,1) → now 0 and1 are connected.

Then merge (1,2) → now 1 and2 are connected (so 0,1,2 are connected).

Then merge (0,2) → already connected, so no change.

But merging (0,1) and (1,2) would connect all three nodes. So during the merging phase, the code would merge (0,1), (1,2), and (0,2). But merging (0,1) and (1,2) already connects all three nodes, so merging (0,2) has no effect.

But in the code's processing, the merging steps are done for each key, regardless of whether they are already connected.

But this merging is done in the DSU after all edges in the group have been processed.

But the problem is that the code's logic for merging all keys in the group may connect multiple components, but this doesn't affect the initial grouping of edges, which is based on the DSU state before processing the group.

In the third sample, the three edges each connect different components (as per the initial DSU state). So each is marked as 'any' (because their key group has count1). But in reality, any two of them can form an MST, but each individual edge is not mandatory for all MSTs.

So the code's logic is incorrect.

Thus, the approach of counting the number of edges in the same key group (based on DSU state before processing) is insufficient.

So what is the correct way to determine if an edge is mandatory?

An edge e is mandatory if and only if, in the DSU after processing all edges with weight less than e's weight, the edge e is a bridge in the graph formed by all edges with weight <= e's weight.

A bridge is an edge whose removal would increase the number of connected components. So, if e is a bridge in this graph, then every MST must include e.

But computing bridges for all edges is computationally expensive for large m.

An alternative approach is to use Krusky's algorithm with modifications to track the necessary information.

An alternative idea is inspired by the following steps:

1. For each edge e, determine if it is part of at least one MST. This is equivalent to whether, when considering all edges with weight less than e's weight, the endpoints of e are in different components. If they are, then e can be part of some MST. Otherwise, it cannot.

2. For edges that are part of at least one MST, determine whether there exists another edge e' with the same weight as e that also connects the same two components (in the DSU state after processing edges with weight less than e's weight). If such an e' exists, then e is not mandatory. Otherwise, e is mandatory.

Thus, the steps are:

- For each edge e:

   a. Check if it's part of any MST (i.e., after processing edges with weight < e.w, e's endpoints are in different components).

   b. If not, mark as 'none'.

   c. Else, check if there's another edge in the same weight group that also connects the same components (in the DSU state before processing this group). If yes, then e is 'at least one'. Else, 'any'.

This is similar to the code's original approach, but perhaps the way to group the edges needs to consider the DSU state after processing edges with lower weight.

But how to efficiently find if there's another edge in the same weight group that connects the same components (as per the DSU state before processing this group).

Thus, the code's original approach is correct, but the third sample's case is a counterexample. So why is this happening?

In the third sample's case:

Each edge is processed in the same group (w=1). For each edge, their endpoints are in different components (DSU state before processing the group is all separate). So each edge is part of at least one MST.

But since there are three edges in the group, each with different (a, b) pairs, the code's logic marks them as 'any' because their group count is 1. But in reality, they are not mandatory.

The problem is that the code's logic assumes that if a group has count 1, then the edge is mandatory. But in reality, even if there's only one edge in the group for a particular (a, b) pair, but there are other edges in the group that connect other pairs of components, the overall MST can be formed by choosing other edges, making the first edge not mandatory.

For example, in the third sample, choosing edges0 and edge1 forms a MST. Choosing edges0 and edge2 forms another MST. Choosing edges1 and edge2 forms another. So each edge is part of at least one MST, but not all. Thus, all edges should be marked as 'at least one', not 'any'.

But according to the code's logic, they are marked as 'any', which is incorrect.

So the code's logic is incorrect. The core issue is that the code assumes that a group's (a, b) pair count of 1 implies the edge is mandatory, but this is not the case when other edges in the same group can be used to merge components in a way that allows alternative paths.

Thus, the code's current approach is incorrect.

To fix this, we need to determine if there are multiple edges in the same weight group that can be used to merge the same components (a and b) in the DSU state before processing the group.

But how to model this.

Alternative approach:

For each group of edges with the same weight:

   - For all edges in the group, compute their (a, b) pairs (roots in DSU before processing).

   - For each such pair (a, b), if there's more than one edge in the group with this pair, then all such edges are 'at least one'.

   - For edges with only one edge in their pair, check if there are other edges in the group that, when processed, can connect a and b through other pairs.

For example, in the third sample's case:

The three edges form a cycle. When processed in any order, adding any two of them will merge all three components. So each edge is part of some MST, but not all.

But according to the code's logic, each edge is the only one in their (a, b) pair, so they are marked as 'any', which is incorrect.

So what's the solution?

The correct way is to consider that even if an edge is the only one in its (a, b) pair, but the group contains other edges that can form a path between a and b when combined, then the edge is not mandatory.

Thus, the code's current logic is incorrect because it doesn't account for the possibility of multiple edges in the same group forming a cycle that allows for alternative paths.

To handle this, we need to check whether the edge's (a, b) pair is part of a block where there are multiple edges in the group that can merge the same components.

But how to do this efficiently.

One possible solution is to create a new DSU for the current group. This DSU is used to track which components can be merged using edges in the group. Then, for each edge in the group:

   - If the edge's a and b are in the same component in the DSU for this group, then adding this edge is redundant, and thus the edge is part of at least one MST.

   - If the edge's a and b are in different components in the group DSU, then adding this edge would merge those components. If this is the only edge in the group that can merge these two components (in the group DSU), then it's mandatory. Otherwise, it's part of at least one MST.

But this seems a bit vague. Let me think:

For the group DSU:

- Initialize each component as a single node.

- For each edge in the group (processed in any order), check if a and b (their roots in the global DSU before processing the group) are in the same component in the group DSU.

   - If not, merge them in the group DSU.

This way, the group DSU tracks which components can be merged by the edges in the group.

Then, for each edge in the group:

   - If the edge's a and b are in the same component in the group DSU after processing all edges in the group, then there's a path of edges in the group that can merge the components, so this edge is redundant and can be part of at least one MST.

   - If the edge's a and b are in different components in the group DSU, then this edge is mandatory for merging those components (since no other edges in the group can do that).

But wait, no. Because the group DSU is built by processing all edges in the group. If after processing all edges in the group, the group DSU for a and b is merged, then there's a way to merge those components using edges from the group. So, the edge is part of at least one MST.

But if the edge's a and b are in different components in the group DSU, then no other edges in the group can merge those components, so this edge is mandatory.

So, the steps are:

For each group of edges with weight w:

   - Collect all edges in the group where a and b are in different components in the global DSU (before processing the group).

   - Create a group DSU, initialized with each node as a separate component.

   - For each such edge (processed in any order), merge their (a, b) in the group DSU.

   - Then, for each such edge, check if a and b are in the same component in the group DSU.

      - If yes, then this edge is not mandatory. It can be replaced by other edges in the group. So it's part of at least one MST but not all.

      - If no, then this edge is mandatory (because no other edges in the group can merge these components). So it's part of any MST.

This approach would handle the third sample correctly.

Let's see:

Third sample's group:

Edges are (0,1), (1,2), (0,2). All edges are in the group.

Group DSU is initialized with 0,1,2.

Processing edges:

Take edge0 (0,1). Merge 0 and1 in group DSU.

Take edge1 (1,2). Merge 1 and2 in group DSU. Now, group DSU has 0-1-2.

Take edge2 (0,2). They are already connected in group DSU. So merging them has no effect.

For each edge:

edge0: in group DSU, a and b (0 and1) are connected. So this edge is not mandatory. Marked as 'at least one'.

edge1: a and b (1 and2) are connected. So marked as 'at least one'.

edge2: a and b (0 and2) are connected. So marked as 'at least one'.

Thus, all edges are 'at least one', which is correct.

Another example: first sample's group w=2.

Edges are (1,2) and (1,3) → after converting to 0-based.

Their roots in global DSU before processing the group are (1,2) and (1,3).

Group DSU:

Initially, each node is separate.

Process edge (1,2): merge 1 and2.

Process edge (1,3): merge 1 and3. Now, group DSU has 1-2-3.

For each edge:

edge (1,2): after processing, group DSU has 1 and 2 merged. So yes. So marked as 'at least one'.

edge (1,3): group DSU has 1 and3 merged. So yes. Marked as 'at least one'.

Thus, this approach gives the correct result.

So the correct approach is:

For each group of edges with the same weight:

   a. For each edge in the group, compute their a and b roots in the global DSU (before processing the group).

   b. Collect all edges where a != b. These edges are candidates.

   c. For the candidate edges, create a group DSU. Initialize each node (from the candidate edges' a and b roots) as separate.

   d. For each candidate edge in the group, merge a and b in the group DSU.

   e. For each candidate edge, check if a and b are connected in the group DSU after processing all edges. If yes, then this edge is not mandatory (part of 'at least one'). If no, then it's mandatory ('any').

Thus, the code's logic should be adjusted to use this approach.

So the steps are:

For each group of edges:

- Process all edges where a and b are in different components in the global DSU.

- For these edges, build a group DSU. The nodes in this group DSU are the root pairs from the global DSU.

- For each such edge, merge a and b in the group DSU.

- For each such edge, if in the group DSU, a and b are in the same component after processing all edges, then the edge is 'at least one'; else, 'any'.

This will correctly handle cases where multiple edges in the same group can form a cycle, allowing edges to be optional even if they are the only ones in their initial (a, b) pair.

Thus, the code's logic should be modified to include this group DSU step.

Now, let's adjust the code accordingly.

The modified approach:

For each group of edges with weight w:

   a. For each edge in the group, compute a and b (roots in global DSU before processing the group).

   b. For edges where a == b: mark as 'none'.

   c. Collect the remaining edges into a list 'candidates'.

   d. Create a group DSU. The nodes are the unique a and b roots from the candidates.

   e. For each candidate edge, merge a and b in the group DSU.

   f. For each candidate edge, check if a and b are connected in the group DSU. 

      - If they are connected after merging (i.e., after processing all candidates in the group), then there's a path of edges in the group that can merge the components, so this edge is not mandatory. Mark as 'at least one'.

      - If they are not connected, then this edge is the only one that can merge these components in the group. Mark as 'any'.

   g. Merge all pairs (a, b) in the global DSU for each candidate edge (i.e., merge a and b once per unique pair).

But merging in the global DSU should be done once per unique (a, b) pair, to avoid redundant unions.

Wait, no. Because after processing the group, we need to merge all pairs (a, b) for the candidate edges to form the MST. But the way to do this is to collect all unique pairs and merge them. However, this is not correct, because the order of merging can affect the DSU structure. But Krusky's algorithm processes all edges of the same weight in any order, and the DSU is updated accordingly.

Thus, merging all pairs in the candidate edges' (a, b) pairs is necessary, but merging them in the global DSU in any order.

But how to collect the pairs to merge.

Alternative approach for merging in global DSU:

For each candidate edge, the (a, b) pair is merged in the global DSU. But to avoid merging the same pair multiple times, we can collect the unique pairs and merge them once.

But for efficiency, we can collect all unique (a, b) pairs and merge them in the global DSU.

But how?

Perhaps, during processing the candidate edges, for each edge's (a, b) pair (sorted), we can track which pairs have been merged already, and merge them once.

But this is not trivial.

Alternative idea:

After processing the group (determining which edges are 'any' or 'at least one'), we can iterate through all candidate edges and merge their (a, b) pairs in the global DSU. But since merging is idempotent (merging two already connected nodes has no effect), this can be done for all edges.

But this may be O(m) per group, which is acceptable since m is up to 1e5.

But in practice, merging all candidate edges' (a, b) pairs in the global DSU is redundant. For example, if a and b are already merged by processing a previous edge.

But Krusky's algorithm requires that all possible edges in the group that connect different components are considered, and their unions are processed. However, in practice, after merging a and b, any subsequent edges in the group with the same (a, b) will have a == b in the global DSU and thus not be merged.

But this approach would process all candidate edges and merge their (a, b) pairs, which is correct.

Thus, the steps are:

For each candidate edge in the group:

   - Merge a and b in the global DSU. This is done regardless of whether they are already connected, but merging connected components is a no-op.

But this would merge all edges in the group, which is incorrect. Because Krusky's algorithm requires that only edges that connect different components are added. But during processing the group, the edges are processed in any order, and once a component is merged, others in the same group may be skipped.

So, merging all candidate edges' (a, b) pairs in the global DSU may lead to merging components multiple times, but it's redundant. So to properly model Krusky's algorithm, we need to process the candidate edges' (a, b) pairs in any order and merge them once per unique pair.

But how to collect the unique pairs.

Thus, during processing the group:

After collecting the candidate edges, the unique (a, b) pairs (sorted) are collected. Then, each pair is merged once in the global DSU.

So, in code:

unique_pairs = set()

for edge in candidates:

    a = edge's a root.

    b = edge's b root.

    if a > b:

        a, b = b, a

    unique_pairs.add( (a, b) )

for a, b in unique_pairs:

    dsu.union(a, b)

This way, each unique pair is merged once, which is correct.

Thus, the modified code steps are:

Process each group as follows:

1. Sort all edges by weight.

2. For each group:

   a. For each edge in the group:

      i. Compute a and b (roots in global DSU before processing the group).

      ii. If a == b: mark as 'none'.

      iii. Else: add to candidates.

   b. If no candidates: continue.

   c. Create group DSU.

   d. For each candidate edge in candidates:

      i. In group DSU, merge a and b.

   e. For each candidate edge in candidates:

      i. Check if a and b are connected in group DSU.

      ii. If yes: mark as 'at least one'.

      iii. Else: mark as 'any'.

   f. Collect unique (a, b) pairs from candidates (sorted).

   g. Merge each pair in global DSU.

Thus, this approach correctly handles cases where edges form cycles within the group.

Testing this approach on the third sample:

Candidates are all three edges. group DSU is initialized with 0,1,2.

Process each candidate:

Edge0 (0,1): merge 0 and1 in group DSU.

Edge1 (1,2): merge1 and2 → now 0-1-2.

Edge2 (0,2): already connected.

For each edge:

Edge0: a=0 and b=1 → in group DSU, connected. 'at least one'.

Edge1: a=1 and b=2 → connected. 'at least one'.

Edge2: a=0 and b=2 → connected. 'at least one'.

Then, collect unique pairs (0,1), (1,2), (0,2). Merge them in global DSU.

After merging, global DSU has 0,1,2 connected.

Thus, all three edges are marked as 'at least one', which is correct.

In the first sample's group w=2:

Candidates are edges2 and3. Their roots are 1 and2, and 1 and3.

Group DSU is initialized with 1,2,3.

Process edge2 (1,2): merge 1 and2.

Process edge3 (1,3): merge 1 and3.

In group DSU, 1,2,3 are connected.

For each edge:

Edge2 (1,2): connected. 'at least one'.

Edge3 (1,3): connected. 'at least one'.

Thus, both are marked as 'at least one'.

Thus, this approach works.

So the code's current logic must be modified to include this group DSU step.

Now, implementing this in Python.

But how to handle the group DSU. Since the group DSU is built with nodes that are the roots of the global DSU before processing the group.

Thus, for each candidate edge, the a and b are roots from the global DSU, which may be large (up to 1e5 nodes), but the group DSU is only built for the current group's roots.

Thus, the group DSU can be implemented as a dictionary, with path compression and union by rank.

But implementing a DSU for a dynamic set of nodes.

Alternatively, for each group, collect all the roots from the candidates and create a DSU for those nodes.

Thus, the code steps for the group:

For the group:

   - Collect candidate edges (a != b).

   - Collect all unique a and b from the candidates.

   - Create a DSU for these nodes.

   - For each candidate edge, merge a and b in this DSU.

   - For each candidate edge, check if a and b are connected in this DSU.

Thus, the code for the group:

...

candidates = []

for edge in group:

    w, a, b, idx = edge

    root_a = dsu.find(a)

    root_b = dsu.find(b)

    if root_a == root_b:

        result[idx] = 'none'

    else:

        candidates.append( (root_a, root_b, idx) )

# Now, process candidates.

if not candidates:

    continue

# Collect all unique roots in the candidates.

roots = set()

for ra, rb, idx in candidates:

    roots.add(ra)

    roots.add(rb)

# Create group DSU.

parent = {}

rank = {}

def find(u):

    if parent[u] != u:

        parent[u] = find(parent[u])

    return parent[u]

def union(u, v):

    u_root = find(u)

    v_root = find(v)

    if u_root == v_root:

        return

    if rank[u_root] < rank[v_root]:

        parent[u_root] = v_root

    else:

        parent[v_root] = u_root

        if rank[u_root] == rank[v_root]:

            rank[u_root] +=1

for root in roots:

    parent[root] = root

    rank[root] = 1

for ra, rb, idx in candidates:

    union(ra, rb)

# Now, check for each candidate.

for ra, rb, idx in candidates:

    if find(ra) == find(rb):

        result[idx] = 'at least one'

    else:

        result[idx] = 'any'

# Now, merge all unique pairs in the global DSU.

unique_pairs = set()

for ra, rb, idx in candidates:

    if ra < rb:

        pair = (ra, rb)

    else:

        pair = (rb, ra)

    unique_pairs.add( pair )

for a, b in unique_pairs:

    dsu.union(a, b)

...

This code should handle the group processing correctly.

Testing this approach on the third sample:

In the candidates, all three edges are present. The roots are 0,1,2. The group DSU is created for these roots.

After processing all candidates, all three are merged. For each edge, find(ra) == find(rb), so marked as 'at least one'.

In the first sample's group w=2:

Candidates are edges2 and3. Their ra and rb are 1 and 2, 1 and3. The group DSU merges 1 and2, then 1 and3. So after processing, all are connected. Thus, each edge is marked as 'at least one'.

Thus, the code now handles the cases correctly.

Thus, the final code should be as follows.
</think>

```python
import sys
from sys import stdin
from collections import defaultdict

sys.setrecursionlimit(1 << 25)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, u):
        while self.parent[u] != u:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u
    
    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return
        if self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        else:
            self.parent[v_root] = u_root
            if self.rank[u_root] == self.rank[v_root]:
                self.rank[u_root] += 1

def main():
    n, m = map(int, stdin.readline().split())
    edges = []
    for idx in range(m):
        a, b, w = map(int, stdin.readline().split())
        a -= 1
        b -= 1
        edges.append((w, a, b, idx))
    
    sorted_edges = sorted(edges, key=lambda x: x[0])
    result = ['none'] * m
    dsu = DSU(n)
    
    i = 0
    while i < m:
        current_weight = sorted_edges[i][0]
        j = i
        while j < m and sorted_edges[j][0] == current_weight:
            j += 1
        group = sorted_edges[i:j]
        i = j
        
        candidates = []
        for edge in group:
            w, a, b, idx = edge
            root_a = dsu.find(a)
            root_b = dsu.find(b)
            if root_a == root_b:
                result[idx] = 'none'
            else:
                candidates.append((root_a, root_b, idx))
        
        if not candidates:
            continue
        
        roots = set()
        for ra, rb, idx in candidates:
            roots.add(ra)
            roots.add(rb)
        
        parent = {}
        rank = {}
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        
        def union(u, v):
            u_root = find(u)
            v_root = find(v)
            if u_root == v_root:
                return
            if rank[u_root] < rank[v_root]:
                parent[u_root] = v_root
            else:
                parent[v_root] = u_root
                if rank[u_root] == rank[v_root]:
                    rank[u_root] += 1
        
        for r in roots:
            parent[r] = r
            rank[r] = 1
        
        for ra, rb, idx in candidates:
            union(ra, rb)
        
        for ra, rb, idx in candidates:
            if find(ra) == find(rb):
                result[idx] = 'at least one'
            else:
                result[idx] = 'any'
        
        unique_pairs = set()
        for ra, rb, idx in candidates:
            if ra < rb:
                pair = (ra, rb)
            else:
                pair = (rb, ra)
            unique_pairs.add(pair)
        
        for a, b in unique_pairs:
            dsu.union(a, b)
    
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
```