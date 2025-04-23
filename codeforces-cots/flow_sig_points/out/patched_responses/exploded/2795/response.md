<think>
Okay, let's tackle this problem. Hmm, the problem seems a bit complex. Let's break it down.

So, the problem is about a tree structure (since there are n cities and n-1 roads, forming a tree) where each road has a capacity c and a toll t. For each query, given a number of vehicles v and a starting city x, we need to find the maximum enjoyment value e among all cities reachable from x using roads with capacity >= v. Then, among all such cities with maximum e, we need to find the maximum toll t along the path from x to that city, which will determine the per-vehicle reimbursement.

The key points here are:
1. For each query, determine all reachable cities from x when roads with capacity >= v are considered.
2. Among these cities, find the maximum e.
3. For all cities with this maximum e, find the maximum toll along their paths from x (the path must be the shortest, which in a tree is unique), then take the maximum of those max tolls.

The challenge is to do this efficiently given the constraints (n and q up to 2e5), which means O(n) per query is too slow. So we need a way to preprocess data to answer queries quickly.

Let me think about the steps needed.

First, since the roads form a tree, the path between any two cities is unique. So for any city y reachable from x via roads with capacity >=v, the path is unique. But the roads along that path must all have capacity >=v. Wait, no. Wait, the capacity of the road is the maximum number of vehicles that can be on it. So for a group of v vehicles, they can use a road only if c >=v. So to reach a city y from x, all roads along the path from x to y must have c >=v. So the reachable cities for a query (v, x) form a subtree that includes x, and all roads in the subtree have capacity >=v.

So the problem reduces to: For each query (v, x), find the connected component (subtree) containing x where all roads have c >=v. Then, among the nodes in this component, find the maximum e, and then among those nodes, find the maximum toll along the path from x to each such node, and take the maximum of those tolls.

So the steps are:

1. For each query (v, x), find the maximum e in the connected component of x when considering roads with c >=v. Let's call this max_e.

2. Then, among all nodes in this component with e = max_e, find the maximum toll t along the path from x to that node. The answer is max_e and that maximum t.

So the problem now is how to, for each query (v, x), quickly find the connected component (subtree) of x under the constraint that all roads in the path have c >=v, and then compute the required max_e and max_t.

But how do we represent these connected components efficiently?

This seems similar to Krusky's algorithm where edges are added in a certain order. Wait, perhaps if we process the roads in decreasing order of capacity, then the connected components are merged as the capacity threshold decreases. For each node, we can track the maximum e in its component and the maximum toll in the paths from the component's root (or some representative) to nodes with maximum e.

Alternatively, perhaps using a Union-Find (Disjoint Set Union - DSU) data structure, augmented with information about the maximum e in the set and the maximum toll along the path from the root to the nodes with maximum e.

Wait, but the DSU approach would require that when edges are added in order of decreasing capacity. Then, for a query (v, x), the connected component is determined by all edges with c >=v. So, if we process queries offline by sorting them in decreasing order of v, and edges in decreasing order of c, we can process the edges and answer the queries in a way similar to Krusky's algorithm.

Yes, that's a promising approach. Let's think through this.

Here's the plan:

- Preprocess all edges by sorting them in decreasing order of c. Similarly, sort all queries in decreasing order of v.

- Then, process each query in order of decreasing v. For each query (v, x), we add all edges with c >= current v (which is the query's v) that haven't been added yet. Then, the connected component of x is the maximal set of nodes reachable via edges with c >=v. Then, within this component, we need to find the maximum e and the maximum toll along the paths from x to the nodes with maximum e.

Wait, but how do we track the maximum e in each DSU set? That's manageable. For each DSU node, we can keep track of the maximum e in the set, and the count of how many nodes have that e. But for the second part, the maximum toll along the path from x (the query's starting node) to the nodes with maximum e.

Hmm, but the DSU structure doesn't track the path from x to other nodes. Because x can be any node in the DSU set. So perhaps this approach isn't sufficient for tracking the maximum toll along the path from x to the nodes with maximum e.

Alternatively, maybe we need to structure the DSU in a way that, for each node, we can track the maximum toll on the path from the root (representative) of the DSU set to that node. Then, when two sets are merged, we can compute the maximum toll for paths through the merged edges.

But how?

Alternatively, perhaps we need to model each DSU set with some additional information. Let's think. Each time we add an edge (a, b) with capacity c and toll t. For the DSU, when merging two sets, the edges that connect them are those with higher capacities. So, when handling a query (v, x), all edges in the DSU have c >=v. Then, the DSU structure represents the connected components under these edges.

But how to track for each node in a DSU set the maximum e and the maximum toll along the path from x (the query's starting node) to the nodes with maximum e.

Wait, but x is variable for each query. So for each query, x is different. So this approach may not work. Because the DSU structure can't track information specific to x, which varies per query.

So perhaps the DSU approach works for determining the connected component (max e) but not for the toll part. Because the toll depends on the path from x to each node, which is unique in the tree but varies depending on x.

Hmm, this complicates things.

Alternative idea: For each node x and possible capacities v, precompute the connected component when considering all edges with c >=v. Then, within this component, find the maximum e and the maximum toll along any path from x to any node in this component with that maximum e.

But storing this for all possible x and v is impossible because v can be up to 1e9.

Alternative approach: For each edge, we can note that the edge is usable for all v <= c. So for a given x and v, the connected component is the set of nodes reachable from x via edges with c >=v. So the connected component can be determined by the maximum spanning forest where edges are added in order of decreasing c. But again, how to track the maximum toll.

Wait, perhaps the maximum toll along any path from x to other nodes in the connected component is the maximum toll of all edges in that component. Because when you have a tree, the path between x and any node y in the component is unique, and the maximum toll on that path is the maximum t of the edges along that path. So, for the connected component, the maximum toll in the entire component (the maximum t among all edges in the component) is the answer. Wait, no. Because the path from x to y may pass through edges with lower t than the maximum in the component. For example, if there's a cycle (but the tree is acyclic). Wait, but the component is a tree. So for any two nodes in the component, their path is unique. The maximum toll along the path between x and y is the maximum of the t's of the edges along that path.

But in the entire component, the maximum toll of all edges could be higher than any path from x. For example, x is connected via a path that doesn't include that edge. So the maximum toll in the component's edges is not necessarily present in the path from x to any node. Therefore, the maximum toll along the path from x to some node in the component is not the same as the maximum edge toll in the component.

So this complicates things. So, for each query (v, x), after determining the connected component C (nodes reachable via edges with c >=v), we need to find:

- The maximum e in C.

- Among all nodes in C with e = max_e, the maximum t along the path from x to that node.

So for each query, it's necessary to find all nodes in the connected component of x (under edges with c >=v) and compute these two values.

But how to do this efficiently.

Another thought: Since the roads form a tree, the original tree structure is fixed. For each node x and a query v, the connected component C is a subtree that includes x, and consists of all nodes connected via paths where each edge has c >=v. So, the subtree C is the maximal subtree containing x where all edges on the path from x to any node in C have c >=v.

Therefore, for each query (v, x), the subtree C is formed by all edges on paths from x where all edges in the path have c >=v. So, the edges in the subtree C are exactly those edges in the original tree that are on some path from x, and each such edge has c >=v.

Thus, the subtree C is the maximal connected component containing x such that all edges in the paths from x to any node in C have c >=v.

But how to compute this quickly?

An alternative idea is to preprocess for each edge, the minimum capacity along the path from x to that edge. Wait, but x varies, so this might not be feasible.

Alternatively, since the tree is static, perhaps for each edge, we can note the paths where this edge is part of the path. But again, this seems difficult.

Alternative approach inspired by Heavy-Light Decomposition (HLD): For each node, precompute for each possible path, but the problem is the capacity and v can be up to 1e9.

Wait, perhaps binary lifting. For each node, and for various thresholds, precompute the maximum e and maximum toll in the path. But with such a large range for v, this seems challenging.

Alternative idea: Since the edges in the tree can be considered in terms of their capacity. For each node x, the edges that can be traversed by a query with v is all edges in the path from x to some node y where each edge has c >=v.

So for each query (v, x), the reachable nodes are those in the subtree obtained by cutting all edges with c <v. The connected component of x in this modified graph.

But again, how to compute this.

Perhaps, for each edge, we can note the maximum capacity in the path from x to some node. But for each x, this would require O(n) storage, which is not feasible.

Alternative approach: Offline processing of queries.

Let's sort all queries in decreasing order of v. Similarly, sort all edges in decreasing order of c. Then, using a DSU structure, we can process the edges in order of decreasing c and answer the queries in order of decreasing v. For each query (v, x), we process all edges with c >=v, merging the DSU components. Then, the DSU set that x is in represents all the nodes reachable via edges with c >=v. Then, for that set, we need to know the maximum e, and among those nodes with maximum e, the maximum toll along the path from x to each such node.

Wait, but how do we track the maximum toll along the path from x to any node in the DSU set?

The DSU structure can track the maximum e in the set. But the maximum toll along the path from x (the query's x) to the nodes with maximum e is a different problem. Because x can be any node in the DSU set.

So, perhaps the DSU can track for each set:

- The maximum e in the set.

- The maximum toll in the entire set (the maximum t of all edges in the set). But that's not sufficient because the path from x to a node with maximum e may not include that edge with maximum t.

Alternatively, for each node in the DSU set, we need to track the maximum toll along the path from some root. But since the DSU is merging trees, this is possible if we use a DSU structure that tracks parents and can compute the maximum toll along the path from the root to each node.

This is similar to the DSU with path information. For example, the DSU can track for each node, the maximum toll along the path from the current root of the DSU set to that node. Then, when merging two sets, the maximum toll can be updated accordingly.

But the problem is that x can be any node in the set, and the path from x to a node with maximum e in the set is unique. So, for a given DSU set, when x is in the set, we need to find the maximum toll along the path from x to any node in the set with maximum e.

But how to track that.

Wait, maybe in the DSU structure, for each set, we can track the nodes with maximum e and the maximum toll along the paths from the root to those nodes. Then, when x is in the set, the path from x to a node y in the set is the path from x to the root, then from the root to y. But this depends on the DSU's path compression.

Alternatively, perhaps the DSU structure can track for each node, the maximum toll from the node to the root of its set. Then, for any two nodes a and b in the same set, the path from a to b is a's path to the root followed by the root's path to b (but in a tree, this might not be the case, but since the DSU is merging trees in a way that forms a forest, perhaps this approach is manageable).

Alternatively, let's model the DSU structure such that each node has a parent, and the edges between nodes in the DSU set are stored with their tolls. Then, for any node, we can compute the maximum toll along the path to the root of the DSU set. So, for each node, we can keep a value 'max_toll' which is the maximum toll along the path from that node to the root of its set.

Then, when two sets are merged, we can adjust the max_toll values for the nodes in the merged set. However, this might be complicated.

But perhaps this is manageable. Let's think:

Each time we add an edge (a, b) with toll t. Let's assume that in the DSU structure, the roots of a and b's sets are root_a and root_b. When merging them, we can attach one root to the other. For example, we make root_b the parent of root_a. Then, the edge between root_a and root_b has toll t. Then, for any node in the original set of a, their path to the new root (root_b) would go through root_a, then via the edge (root_a, root_b) with toll t. So, the max_toll for those nodes would be the maximum between their existing max_toll (from themselves to root_a) and t.

Wait, perhaps not. Let's think of node x in root_a's set. Its path to the new root (root_b) is x -> ... -> root_a -> root_b. So the max_toll for x would be max(current max_toll of x (which is the max from x to root_a), t). Similarly, nodes in root_b's set would have their max_toll unchanged.

So, when merging two sets, we can track the edge's toll and adjust the max_toll for the nodes in the merged set.

But this approach would require that whenever two sets are merged, all nodes in the merged set have their max_toll updated. Which is O(n) per merge, which is not feasible for large n.

So this approach is not feasible.

Alternative Idea: Instead of tracking the max_toll for each node to the root, track for each set the maximum toll along any edge in the set. Because the maximum toll in the entire set would be the maximum of all edges in the set. Then, for any two nodes in the set, the path between them (since it's a tree) has a maximum toll equal to the maximum edge toll in that path. However, the overall maximum edge toll in the entire set is the maximum of all edges in the set. So, if a query's connected component has maximum edge toll T_max, then the maximum toll along the path from x to any node in the component is at most T_max. But this is not necessarily equal to T_max, unless there exists a path from x to some node that includes the edge with T_max.

But how to ensure that. For example, if x is in a connected component where there's an edge with t=10, but x is in a part of the tree that's connected via edges with t=5, then the maximum toll on the path from x to any node in the component may be 5, even though the component has an edge with t=10. But the path from x to the edge with t=10 may require going through edges with capacity <v, which are not part of the current component. Wait, no. The component is built with edges of capacity >=v. So any edge in the component's set has c >=v, and the component is a connected subset of the original tree. So the component is a subtree. Therefore, any two nodes in the component are connected via edges with c >=v. So, the edges in the component form a subtree of the original tree.

So, if the component includes an edge with t=10, then there exists a path from x to that edge's nodes, and thus the path from x to either end of that edge would include that edge. So the maximum toll on the path from x to that node would be 10, which is the maximum edge in the component. Therefore, the maximum toll along any path from x to a node in the component is the maximum t of all edges in the component.

Wait, is that correct?

Suppose the component is a subtree. The edges in the component are all >=v. The component is connected. Let's say within the component, there's an edge e with t=10. Since the component is a subtree, any path from x to e's nodes must pass through e (if x is not already in e's subtree). Or perhaps not. Wait, the component is a tree. Let's imagine a scenario where x is in a part of the subtree connected via a bridge. Then, adding an edge e with higher t elsewhere in the tree, but the path from x to e's nodes may not go through e. So, the maximum t along the path from x to a node y could be the maximum of the edges in that path. So, the overall maximum t in the component is the maximum of all edges in the component, but the path from x to y may not include that edge. Thus, the maximum toll in the component's edges is not necessarily the maximum toll along the path from x to some node.

Therefore, this approach of tracking the maximum t in the DSU set is not sufficient.

Hmm, so this complicates things. So, for each query, after determining the connected component C, we need to find the maximum e in C, and among all nodes in C with e= max_e, find the maximum t along the path from x to each such node. Then, the answer is the maximum of those t's.

So, how to do this efficiently.

Another Idea: For each node, precompute the maximum e and the maximum t along the path from x to that node. But x can be any node, which makes this impossible to precompute for all possible x.

Alternatively, for each edge in the tree, determine for which queries (v, x) this edge is part of the path from x to some node. But this seems challenging.

Alternative Idea: For each query (v, x), the reachable nodes are those in the subtree formed by edges with c >=v, starting from x. So the edges in this subtree form a tree. The maximum e in this subtree is known. Now, among all nodes in this subtree with maximum e, we need to find the maximum t along the path from x to them.

The maximum t along the path from x to any node in the subtree is the maximum t of the edges along that path. So, for all nodes y in the subtree with e= max_e, the path from x to y has some maximum t. We need the maximum of these.

But how to compute this.

Let me think of the subtree as a tree rooted at x. Because the subtree is connected and x is the starting node, the subtree is a tree. So, for each node in the subtree, the path from x to that node is unique. So, for each node in the subtree, we can compute the maximum t along the path from x to it.

So, the problem reduces to:

1. For the subtree S of nodes reachable from x via edges with c >=v, find the maximum e in S.

2. Among all nodes in S with e= max_e, find the maximum of the maximum t along the path from x to each of these nodes.

So, for each query (v, x), we need to find:

- The maximum e in S.

- Among those nodes with e= max_e, the maximum t along their path from x.

But how to compute this quickly.

Hmm. For each node x, and for varying v, the subtree S is determined by the edges that are allowed (c >=v). So, for each x, the edges that can be traversed (those with c >=v) form a connected component. The subtree S is the set of nodes reachable from x via edges with c >=v.

Now, considering that each query's v is a threshold, perhaps for each node x, we can precompute for all possible v's the maximum e and the maximum t along paths from x to nodes in S. But since v can be up to 1e9, this is not feasible.

Alternative Idea: For each edge in the tree, the order in which they are included in the subtree S (as v decreases) can be used. So, for each node x, the edges along the paths from x to other nodes are processed in decreasing order of c. For each edge, when it is included (when v <= c), the subtree S expands to include nodes connected via that edge.

But how to manage this for multiple queries.

This seems similar to building a structure for each node x that allows queries of the form "what is the maximum e and maximum t in the subtree formed by edges with c >=v starting at x".

But how to represent this.

Perhaps, for each node x, we can preprocess all edges in the tree in the order of decreasing c. For each edge, we can determine if including it (i.e., when v <= c) would allow x to reach certain nodes, and track the maximum e and the maximum t along the path from x.

But again, with n up to 2e5, preprocessing for each node is O(n), which is O(n^2) total time, which is not feasible.

Alternative Idea: The problem requires that the path from x to y is the unique path in the original tree. So, for each node x, the subtree S (when v is given) is the set of all nodes y such that all edges on the path from x to y have c >=v.

Thus, for a query (v, x), the subtree S is the set of nodes y where the minimum c along the path from x to y is >=v. Because if any edge on the path has c <v, then the path is not allowed.

So, the problem reduces to:

For a given x and v, find all nodes y where the minimum c on the path from x to y is >=v. The maximum e among these nodes is required, and among those nodes, the maximum toll t on the path from x to them.

Wait, no. Because each road on the path must have c >=v. So the minimum c on the path is >=v. So for each node y, if the minimum c on the path from x to y is >=v, then y is in S.

So the problem is now to find, for each query (v, x), the maximum e in the set { y | min_c(x,y) >=v }, and the maximum t in the set { max_t(x,y) | y in that set and e(y) is maximum }.

Thus, the problem is now to compute for each query (v, x):

1. The maximum e among all nodes y where the minimum c on the path x-y is >=v.

2. The maximum t on the path x-y for all such y with e(y) equal to the first maximum.

So, how to compute these two values.

Idea: For each node x, we can precompute all possible paths and their minimum c and maximum t, then for a given v, query the maximum e where min_c >=v, and then the maximum t for those e's.

But again, this would require O(n^2) storage which is impossible.

Alternative Idea: For each node x, the set of nodes reachable in a query (v, x) forms a subtree. The edges along the path from x to each node in this subtree must all have c >=v. So the subtree can be represented as the nodes that are in the same connected component as x in the forest formed by all edges with c >=v.

But how to handle this for multiple queries.

This brings us back to the DSU approach, but with the problem of tracking the maximum e and the maximum t along the path from x to the nodes with maximum e.

Another Idea: For each query (v, x), the nodes in S are those where all edges on their path from x have c >=v. So, the subtree S can be determined by the maximum spanning tree where edges are chosen based on c >=v. Wait, but maximum spanning tree is not directly applicable here. However, the maximum spanning tree (MST) would include edges with higher c first, but we need to include all edges with c >=v. So the connected component of x in the graph formed by edges with c >=v is exactly the subtree S.

So, the DSU approach can help in finding the connected component. But again, how to track the maximum e and the required maximum t.

Let's think again about processing queries offline. We can sort all queries in decreasing order of v, and edges in decreasing order of c. Then, for each query (v, x), we process all edges with c >=v, and for each x, find the connected component and track the required information.

But what information can we track in the DSU?

For each DSU set, we can track:

- The maximum e in the set.

- The count of nodes with this maximum e.

- The maximum toll among all edges in the set.

But this gives us the maximum toll in the set, but not necessarily the maximum toll along the path from x to the nodes with maximum e.

Alternatively, perhaps we need to track for each DSU set two things: the maximum e in the set, and the maximum toll along any path in the set. Because the maximum toll in the set is the highest t of any edge in the set, and since the set is connected via edges with c >=v, the path from x to the node y with max e must include that edge. Or maybe not. For example, if the edge with the highest toll is in the set, but x is not connected to it via a path that includes that edge. But since the set is a tree, if the edge is part of the set, then there is a path from x to the nodes connected by that edge. So, the path from x to the edge's nodes must include that edge. Therefore, the maximum toll in the set is the maximum edge toll in the set, and the path from x to those nodes will include that edge. Therefore, the maximum toll along any path from x to a node in the set is the maximum toll in the set.

Wait, this might not be the case. For example, the edge with maximum toll may be in the set, but the path from x to that edge may pass through edges with lower tolls, and then the maximum toll along that path is the maximum of all edges in the path, which could be the edge with the maximum toll. So, the maximum toll along any path in the set is the maximum toll in the entire set.

Therefore, if the DSU set has a maximum toll of T, then any path from x to any node in the set can have a maximum toll of at most T. And there exists at least one path (the one that includes the edge with T) where the maximum toll is T. So, if among the nodes with maximum e, at least one is in a subtree that requires passing through the edge with T, then the maximum toll for those nodes would be T.

Therefore, the answer to the query would be (max_e, T), where T is the maximum toll in the DSU set.

But how does this hold?

Let's take the first sample input:

Sample Input 1:
5 3
2 2 3 3 3
1 2 4 7
1 3 2 8
2 4 8 2
2 5 1 1
Queries:
1 3 → output 3 8.

For this query, the edges allowed are those with c >=1. All edges are allowed. The DSU set for x=3 is the entire tree. The maximum e is 3 (nodes 3,4,5). The maximum toll in the entire set is 8 (from edge 1-3 with t=8). So the maximum toll along any path from 3 to these nodes would be 8. For example, path from 3 to 4 is 3 →1 →2 →4. The edges are (1-3, t=8), (1-2, t=7), (2-4, t=2). The max toll is 8.

Yes, so the answer is 3 and 8.

Another example from the same sample: query 6 2. The allowed edges are those with c >=6. The edges are 1-3 (c=2 → no), 1-2 (c=4 → no), 2-4 (c=8 → yes), 2-5 (c=1 → no). So the allowed edges are 2-4. So the connected component of x=2 is {2,4}. The maximum e is 3 (nodes 2 and 4). Wait, node 2 has e=2, node 4 has e=3. So the maximum e is 3 (node 4). The maximum toll in the DSU set is 2 (edge 2-4). So the answer is 3 2.

But according to the sample output, the answer is 3 2. So it's correct.

So, the maximum toll in the DSU set is the answer for the second part. So, for each query (v, x), after finding the DSU set containing x (after merging all edges with c >=v), the maximum e in the set is the first part of the answer, and the maximum toll in the set is the second part.

Thus, the DSU approach can be modified to track for each set the maximum e and the maximum toll in the set.

So, the steps are:

- Sort all edges in decreasing order of c.

- Sort all queries in decreasing order of v, keeping track of their indices to output the answers in the original order.

- For each query in this sorted order, process all edges with c >= current query's v that haven't been processed yet.

- For each DSU set, track:

   a. The maximum e in the set.

   b. The count of nodes with that maximum e.

   c. The maximum toll in the set (the maximum t of any edge in the set).

- When merging two sets during DSU union:

   a. The maximum e of the merged set is the maximum of the two sets' max e. If they are equal, the count is the sum.

   b. The maximum toll of the merged set is the maximum of the two sets' max toll and the current edge's t.

   c. Update the merged set's max e and max toll accordingly.

- For each query (v, x), after processing all edges with c >=v, the answer for that query is (max_e, max_toll), where max_e is the DSU set's max_e, and max_toll is the DSU set's max_toll.

But wait, in the first sample query, the DSU set's max_toll is 8 (from the edge 1-3). However, the path from x=3 to node 4 has a max toll of 8. Which is correct. So yes, the maximum toll in the DSU set is the required value.

Thus, this approach works.

So the steps for the DSU are:

1. Initialize each node as its own set, with max_e as e[i], count 1, and max_toll 0 (since no edges are added yet).

2. Sort the edges in decreasing order of c. For each edge in this order:

   a. Find the roots of the two nodes a and b.

   b. If they are in different sets:

      i. Check which set has higher max_e. The merged set's max_e will be the higher of the two. If equal, sum the counts.

      ii. The merged set's max_toll is the maximum of the two sets' max_toll and the current edge's t.

      iii. Attach the smaller set to the larger set (or any other union method).

3. For the queries, sorted in decreasing order of v:

   a. Process all edges with c >= current query's v.

   b. For each query, find the root of x, get the max_e and max_toll for that set.

   c. The answer is (max_e, max_toll if max_e is not the node's own e (if the set has size 1, then max_toll is 0)). Wait, no: when a node is alone in the set, it has no edges, so the toll is 0.

But during the DSU processing, when merging sets, the max_toll is updated as the maximum of the current edge's t and the max_toll of the two sets.

So, the initial max_toll for a single-node set is 0. When edges are added between nodes, the max_toll is the maximum of the existing max_toll and the new edge's t.

This seems correct.

Thus, the DSU approach can be used to track the max_e and max_toll for each set.

Now, let's think about the sample input 2:

Sample Input 2:

5 5
1 2 3 4 5
1 2 4 1
1 3 3 1
1 4 2 1
2 5 1 1
Queries:
5 1 → output 1 0.

For this query, v=5. The allowed edges are those with c >=5. The edges have capacities 4,3,2,1. None of them are >=5. So the DSU set for x=1 is just {1}, max_e=1, max_toll=0. So the answer is (1, 0). Which matches the sample.

For the query 4 1, v=4. The only edge with c >=4 is the first edge (1-2, c=4). So the DSU set for x=1 after processing this edge is {1,2}. The max_e is 2 (from node 2), max_toll is 1 (the edge's t). So the answer is (2, 1), which matches the sample.

Thus, the approach works.

Now, the code.

The plan for the code:

- Read n and q.

- Read e array.

- Read n-1 edges, store them as a list of tuples (a-1, b-1, c, t).

- Sort the edges in descending order of c.

- Read all queries, storing them as (v, x-1, index), then sort the queries in descending order of v.

- Initialize DSU structure. Each node's parent is itself. For each node, track:

   a. size of the set.

   b. max_e in the set.

   c. count_max: the number of nodes with e == max_e.

   d. max_toll: the maximum toll in the set.

- Process each query in sorted order:

   a. For the current query's v, add all edges with c >=v that haven't been added yet.

   b. Find the root of x.

   c. The answer for this query is (max_e, max_toll). But if the set's size is 1, then max_toll is 0.

But wait, the DSU's max_toll is the maximum of all edges in the set. For a singleton set, there are no edges, so the max_toll is 0. Which is correct.

Once all queries are processed, output the answers in the original order.

Thus, the code can be structured as follows:

Implement DSU with path compression and union by size. Each node has parent, size, max_e, count_max, max_toll.

The edges are sorted in descending order of c.

Queries are sorted in descending order of v, keeping their original indices.

Then, for each query, process edges in order, adding any edge with c >=v that hasn't been processed yet. Then, find the root of x and get the max_e and max_toll.

Now, let's think about the DSU implementation:

Each time two sets are merged, the new set's max_e is the max of the two old sets' max_e. If they are equal, the count_max is the sum. If one is larger, the count_max is that of the larger.

The new set's max_toll is the max of the two sets' max_toll and the current edge's t.

Wait, no. Because the merged set's edges include the current edge. So the merged set's max_toll is the maximum between the previous max_toll of both sets and the current edge's t.

Yes. For example, if two sets have max_toll 5 and 6, and the current edge has t=3. Then the new max_toll is 6. If the current edge has t=7, then it's 7.

Thus, when merging two sets, the new max_toll is max(a.max_toll, b.max_toll, edge.t).

So during the union:

new_max_toll = max(edge.t, a.max_toll, b.max_toll)

Yes.

So the code for the DSU union:

def union(a_root, b_root, edge_t):
    if a_root == b_root:
        return
    if size[a_root] < size[b_root]:
        a_root, b_root = b_root, a_root
    parent[b_root] = a_root
    size[a_root] += size[b_root]
    if max_e[a_root] < max_e[b_root]:
        max_e[a_root] = max_e[b_root]
        count_max[a_root] = count_max[b_root]
    elif max_e[a_root] == max_e[b_root]:
        count_max[a_root] += count_max[b_root]
    new_max_toll = max(edge_t, max_toll[a_root], max_toll[b_root])
    max_toll[a_root] = new_max_toll

Wait, but the edge's toll is part of the merged set. So yes.

Thus, the code needs to handle this.

Now, implementing this.

But in Python, with 2e5 nodes and edges, we need to use a DSU with path compression and union by size to keep the time manageable.

So, the code:

Read n and q.

Read e as a list.

Read the edges as a list of tuples (a, b, c, t). Then sort them in descending order of c.

Read the queries as a list of tuples (v, x, index), then sort them in descending order of v.

Initialize DSU:

parent: list where parent[i] is the parent of node i.

size: list where size[i] is the size of the set rooted at i.

max_e: list where max_e[i] is the maximum e in the set rooted at i.

count_max: list where count_max[i] is the number of nodes in the set with e equal to max_e.

max_toll: list where max_toll[i] is the maximum toll in the set.

Initially, each node is its own parent. size[i] = 1, max_e[i] = e[i], count_max[i] = 1, max_toll[i] = 0.

Process the queries in order:

We process each query in sorted order. For each query (v, x, idx), we need to add all edges with c >=v that haven't been added yet. So, we have a pointer j that starts at 0 and increments as we process edges in sorted order. For each query, we process edges until edges[j].c <v.

Once all edges are processed, find the root of x, get max_e and max_toll of the root's set.

Store the answer for this query's idx as (max_e, max_toll).

Finally, after all queries are processed, output the answers in the original order.

But wait, what about the case where a node's set has max_toll but it's a single node (no edges). For example, the first query in sample input 2: query v=5, x=1. The DSU set for x=1 is itself. Its max_toll is 0, which is correct.

Yes.

So the code should work.

Now, let's test this approach against the samples.

Sample Input 1:

5 3
2 2 3 3 3
1 2 4 7
1 3 2 8
2 4 8 2
2 5 1 1
Queries:
1 3 → sorted v=1.
9 5 → sorted v=9.
6 2 → sorted v=6.

The edges are sorted in descending order of c:

Edge 2-4: c=8, t=2.

Edge 1-2: c=4, t=7.

Edge 1-3: c=2, t=8.

Edge 2-5: c=1, t=1.

The queries are sorted in order of v: 9, 6, 1.

Processing query v=9:

Process edges with c >=9. None. So the set for x=5 (original x=5-1=4) is just {4}. max_e=3, max_toll=0. But wait, the initial max_e for node 4 (0-based index is 3?) Let me see. The input is 1-based. So city 5 is index 4. e for city 5 is 3. So DSU for node 4 has max_e=3, count_max=1, max_toll=0. So the answer is (3, 0). Which matches the sample.

Processing query v=6:

Process edges with c >=6. The first edge is c=8 (yes). So process edge between 2 and4 (original cities are 2 and4 → 0-based 1 and 3).

Union sets. The DSU set for 1 (city 2) and 3 (city4) are merged. The merged set has max_e=3 (since max_e of city2 is 2, city4 is3). So the merged set's max_e is3. count_max is 1 (from city4). max_toll is max(2 (current edge's t), 0 (from city2's set), 0 (from city4's set)) → 2.

Next, check if any other edges have c >=6. The next edge is c=4 <6. So stop.

For query x=2 (0-based is 1). The root is 1 (city2's set after merging with city4). max_e is3, max_toll is2. So answer is (3, 2), which matches the sample.

Processing query v=1:

Process all edges. For edges >=1, all edges are processed.

The edges are added in order of c=8 (added), c=4 (added), c=2 (added), c=1 (added).

After adding all edges:

The DSU structure will have all nodes merged into a single set. The max_e is3, count_max=3 (nodes3,4,5). max_toll is the maximum of all edges' t. The edges' t are 7 (1-2), 8 (1-3), 2 (2-4), 1 (2-5). The maximum is8. So the answer for x=3 (0-based 2) is (3,8). Which matches the sample.

Thus, the approach works.

Now, code in Python.

But for large n and q (2e5), the code needs to be efficient. Using path compression and union by size is O(alpha(n)) per operation.

So, implementing the DSU with arrays for parent, size, max_e, count_max, max_toll.

But in Python, using lists is feasible.

Now, the code.

First, read the input.

Then, sort edges in descending order of c.

Sort queries in descending order of v, keeping track of their original indices.

Process the queries in order, adding edges with c >=v.

Now, code:

Read n and q.

Read e as list of integers.

Read edges: n-1 lines, each a, b, c, t. Convert a and b to 0-based.

Sort edges in descending order of c.

Read q queries: each v, x (1-based x, convert to 0-based). Store as a list of tuples (v, x, original index).

Sort the queries in descending order of v.

Initialize DSU:

parent = list(range(n))

size = [1]*n

max_e = [e[i] for i in range(n)]

count_max = [1]*n

max_toll = [0]*n

Process the queries and edges:

j = 0 (pointer to edges)

answers = [(0,0)]*q

for each query in sorted order:

   v, x, idx = query

   while j < len(edges) and edges[j][2] >=v:

       a, b, c, t = edges[j]

       j +=1

       # find roots

       root_a = find(a)

       root_b = find(b)

       if root_a == root_b:

           continue

       # union

       if size[root_a] < size[root_b]:

           root_a, root_b = root_b, root_a

       parent[root_b] = root_a

       size[root_a] += size[root_b]

       # update max_e and count_max

       if max_e[root_a] < max_e[root_b]:

           max_e[root_a] = max_e[root_b]

           count_max[root_a] = count_max[root_b]

       elif max_e[root_a] == max_e[root_b]:

           count_max[root_a] += count_max[root_b]

       # update max_toll

       current_max_toll = max(max_toll[root_a], max_toll[root_b], t)

       max_toll[root_a] = current_max_toll

   # after processing edges >=v:

   root_x = find(x)

   answers[idx] = (max_e[root_x], max_toll[root_x])

Once all queries are processed, output the answers in order.

But wait, the original order of the queries is stored in the 'idx' variable. So when building the answers list, each query's answer is stored at the idx position.

Finally, output each answer in order, from 0 to q-1.

Now, implement the find function with path compression.

Implement find as:

def find(u):

   while parent[u] != u:

       parent[u] = parent[parent[u]]

       u = parent[u]

   return u

But in Python, we need to manage the parent list.

Yes.

Thus, the code should look like this.

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    import sys
    input = input_stream.read().split()
    ptr = 0
    n, q = int(input[ptr]), int(input[ptr+1])
    ptr += 2
    e = list(map(int, input[ptr:ptr+n]))
    ptr +=n
    edges = []
    for _ in range(n-1):
        a = int(input[ptr])-1
        b = int(input[ptr+1])-1
        c = int(input[ptr+2])
        t = int(input[ptr+3])
        edges.append( (a, b, c, t) )
        ptr +=4
    queries = []
    for idx in range(q):
        v = int(input[ptr])
        x = int(input[ptr+1])-1
        queries.append( (v, x, idx) )
        ptr +=2
    
    edges.sort(key=lambda x: -x[2])
    queries.sort(key=lambda x: -x[0])
    
    parent = list(range(n))
    size = [1]*n
    max_e = e.copy()
    count_max = [1]*n
    max_toll = [0]*n
    
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    
    j = 0
    answers = [ (0,0) ] * q
    for v, x, idx in queries:
        while j < len(edges) and edges[j][2] >= v:
            a, b, c_edge, t_edge = edges[j]
            j +=1
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                continue
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            parent[root_b] = root_a
            size[root_a] += size[root_b]
            if max_e[root_a] < max_e[root_b]:
                max_e[root_a] = max_e[root_b]
                count_max[root_a] = count_max[root_b]
            elif max_e[root_a] == max_e[root_b]:
                count_max[root_a] += count_max[root_b]
            new_toll = max(t_edge, max_toll[root_a], max_toll[root_b])
            max_toll[root_a] = new_toll
        root_x = find(x)
        answers[idx] = (max_e[root_x], max_toll[root_x])
    
    for ans in answers:
        print(ans[0], ans[1], file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 5
1 2 2 2 2
1 2 5 8
1 3 6 3
1 4 4 5
1 5 7 1
4 1
5 1
6 1
7 1
8 1
""",
            "output": \
"""\
2 8
2 8
2 3
2 1
1 0
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
def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n, q = int(input[ptr]), int(input[ptr+1])
    ptr += 2
    e = list(map(int, input[ptr:ptr+n]))
    ptr +=n
    edges = []
    for _ in range(n-1):
        a = int(input[ptr])-1
        b = int(input[ptr+1])-1
        c = int(input[ptr+2])
        t = int(input[ptr+3])
        edges.append( (a, b, c, t) )
        ptr +=4
    queries = []
    for idx in range(q):
        v = int(input[ptr])
        x = int(input[ptr+1])-1
        queries.append( (v, x, idx) )
        ptr +=2
    
    edges.sort(key=lambda x: -x[2])
    queries.sort(key=lambda x: -x[0])
    
    parent = list(range(n))
    size = [1]*n
    max_e = e.copy()
    count_max = [1]*n
    max_toll = [0]*n
    
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    
    j = 0
    answers = [ (0,0) ] * q
    for v, x, idx in queries:
        while j < len(edges) and edges[j][2] >= v:
            a, b, c_edge, t_edge = edges[j]
            j +=1
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                continue
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            parent[root_b] = root_a
            size[root_a] += size[root_b]
            if max_e[root_a] < max_e[root_b]:
                max_e[root_a] = max_e[root_b]
                count_max[root_a] = count_max[root_b]
            elif max_e[root_a] == max_e[root_b]:
                count_max[root_a] += count_max[root_b]
            new_toll = max(t_edge, max_toll[root_a], max_toll[root_b])
            max_toll[root_a] = new_toll
        root_x = find(x)
        answers[idx] = (max_e[root_x], max_toll[root_x])
    
    for ans in answers:
        print(ans[0], ans[1])

if __name__ == "__main__":
    main()
```
