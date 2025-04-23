<think>
Okay, so I need to solve this problem where I have to find the optimal capital city in a tree structure such that the number of road inversions required is minimized. Let's think about this.

First, the problem states that the country Treeland has n cities connected by n-1 roads, which form a tree when directions are ignored. The task is to choose a capital city such that all roads are oriented in a way that allows moving from the capital to every other city. The roads can be reversed, and we need to minimize the number of reversals.

Hmm. So for a chosen capital, the roads need to form a directed tree with the capital as the root, and all edges pointing away from the root (but maybe not directly—since it's a tree, the paths from the root to leaves must follow the directions). Wait, no. The requirement is that from the capital, you can reach every other city by moving along the roads. So the roads must form a DAG (since it's a tree) where the capital is the root and there's a path to every node. But the roads can be in any direction, as long as the path exists. So the directions of the roads determine the possible paths. But for the capital, we can reverse some roads so that the tree becomes such that all paths from the capital to other cities are possible by traversing the roads as directed.

Wait, the problem is similar to building a directed tree (arborescence) rooted at the capital. So the key is to find a root such that the number of edges that need to be reversed is minimized. Each edge in the original tree can be thought of as either pointing towards the parent in the desired arborescence or away from it. So for each node, if we can compute the total number of edges that need to be reversed when that node is the root, then the optimal solution is the node with the minimal count.

But how do we compute that efficiently for all nodes? Because the constraints are up to 2e5 nodes, so O(n) algorithms are needed.

Let me think. Let's model the tree as undirected edges, each with a direction. When we root the tree at a particular node (the capital), the edges along the paths from the root to other nodes must be oriented such that the path is possible. For example, if the original edge is directed from parent to child in the tree (when the root is chosen), then no reversal is needed. Otherwise, it needs to be reversed.

Wait, but the direction of the original edges is fixed. So for each edge in the undirected tree, when we consider the tree as rooted at some node, each edge is part of the parent-child relationship. The original direction of the edge may or may not align with the direction required by the tree structure. For example, if in the tree structure, the parent is u and the child is v, then the edge u->v in the original setup is okay (no reversal needed), but if the original edge is v->u, then we have to reverse it (count += 1).

So the problem reduces to, for each node as root, sum the number of edges in the tree that are directed against the parent-child hierarchy in the tree structure.

But how do we compute this efficiently for all possible roots?

The key insight here is that when we switch the root from a parent to its child, only a subset of edges' contributions change. This suggests that a dynamic programming approach or a post-order traversal with some state tracking could help.

Let me consider building the tree with edges stored as bidirectional, but with each edge having a direction (original direction). Then, for a chosen root, the tree's edges form a hierarchy. The number of reversals required is the sum over all edges (u, v) where the edge in the original tree is directed against the direction of the parent in the tree (from parent to child).

So for example, if the original edge is from u to v, but in the tree structure (as rooted at the root), the parent is v and the child is u, then this edge needs to be reversed (since the path from root to u must go through v, but the edge is v->u, which is allowed. Wait, no. Wait, let me think again.

Suppose the tree is rooted at node r. For each edge in the tree (when considered as a tree rooted at r), each edge connects a parent to a child. The original direction of the edge (s, t) is either from parent to child or child to parent. So if in the tree structure, the parent is s and the child is t, then if the original edge is s->t, no reversal is needed. Otherwise (if the original edge is t->s), then we need to reverse it, contributing 1 to the count. Similarly, if in the tree structure, the parent is t and the child is s, then the original edge t->s would require no reversal, but s->t would need to be reversed.

So the problem is to find the root that minimizes the sum of reversals over all edges based on their parent-child direction in the tree.

The challenge is to compute this sum for all possible roots efficiently.

Let's consider an arbitrary root (say, root 1). We can compute the initial reversal count for root 1 by traversing the tree (DFS or BFS), and for each edge in the tree, checking if the original direction matches the parent-child direction. For example, during the traversal, for each node u, when we visit its child v via an edge that was originally s -> t, if in the tree structure (rooted at 1) the parent is u and the child is v (so the edge is u->v), then if the original edge is u->v, no reversal. If the original edge is v->u (i.e., s = v, t = u), then we have to reverse it. So during the initial traversal, for each edge, we can compute whether it contributes 0 or 1 to the reversal count.

Once we have the initial count for root 1, we need to find a way to compute the counts for all other roots by reusing this information.

This is similar to the problem of finding the sum of subtree sizes for all nodes, which can be done with a post-order traversal and dynamic programming. The idea here is that when we change the root from a parent to a child, the reversal count can be updated based on the original edge's direction.

Let's suppose we have an edge between u and v. Let's assume that in the original tree (rooted at 1), u is the parent of v. When we switch the root to v, the parent of u becomes v. So the edge direction (u <-> v) in the tree structure is reversed. So for this edge, if the original direction was u->v, then when the root is u (parent) and v is child, it contributed 0. But when the root is v (parent) and u is child, the original direction is u->v, which would now be child to parent. So this edge would contribute 1 (since we need to reverse it to make it v->u). Similarly, if the original direction was v->u, when the root is u (parent), this contributes 1 (since the edge is reversed to u->v). But when the root is v (parent), the original edge is v->u, which is parent to child (so no reversal needed).

So when changing the root from u to v (assuming they are connected by an edge), the reversal count for the entire tree can be adjusted by considering this edge. The reversal count for the new root (v) is equal to the reversal count for root u minus the contribution of the edge u-v in the original tree plus the contribution in the reversed scenario.

Wait, perhaps the reversal count for root v is equal to the reversal count for root u minus the contribution of the edge (u, v) when u was the parent, plus the contribution when v is the parent.

So, for example, let's say when u is the parent of v, the edge contributes 'cost'. Then when v becomes the parent of u, the edge contributes '1 - cost' (since if the original direction is s->t, when the parent is u, cost is 0 if s is u and t is v, otherwise 1. If the parent is v, then the cost is 1 if s is u and t is v (original direction is u->v, but now parent is v and child is u, so the edge direction is u->v, which is child to parent. So to have parent to child direction, we need to reverse it (so cost is 1)). Alternatively, if original edge was v->u, then when parent is u, the cost is 1 (since the edge is v->u, which is child to parent, but in the tree structure, u is parent. So original edge is child to parent, so to have parent to child direction, we need to reverse it (so cost is 1). If now parent is v, then original edge is v->u, which is parent to child, so cost is 0.

So for the edge between u and v, the cost depends on which direction the tree traversal takes (i.e., which is parent and which is child). The total reversal count is the sum of all edges' costs based on their position in the tree structure.

So when we re-root the tree from u to v (assuming they are adjacent), the reversal count for v is the reversal count for u minus the cost of the edge (u, v) in the original direction (u as parent) plus the cost when the edge is reversed (v as parent). So delta is (new_cost - old_cost).

This suggests that after computing the initial reversal count for a root (say, root 1), we can perform a post-order traversal and compute the reversal counts for all other nodes by adjusting the count based on the edges.

So the algorithm steps would be:

1. Build the tree as an adjacency list, with each edge having a direction (original direction and the reverse). For each edge, we need to track whether it's in the original direction (s, t) or not.

2. Choose an initial root (like 1), and perform a DFS or BFS to compute the initial reversal count. For each edge in the tree (as determined by the traversal), check the original direction and add 1 to the count if the direction is against the parent-child relationship.

3. Then, perform another traversal (post-order or similar) to compute the reversal counts for all other nodes. For each node, when moving the root from its parent to itself, adjust the reversal count based on the edge between them. For example, if moving from parent u to child v, the reversal count for v would be the reversal count for u minus the cost of the edge (u as parent) plus the cost when the edge is reversed (v as parent).

But how do we model the direction of the edges in the adjacency list?

Let me think about how to represent the edges. Each undirected edge in the tree can be traversed in either direction. For each edge (s, t) in the input, which is directed from s to t, when building the adjacency list, we can note for each direction whether the original edge exists. For example, if we have an edge s->t, then in the adjacency list for s, we can have a neighbor t with a direction 0 (no cost if s is parent and t is child), and for the adjacency list for t, we can have a neighbor s with direction 1 (if t is parent and s is child, the original edge is s->t, which is the reverse of t->s, so cost is 1).

Wait, perhaps for each node u, in its adjacency list, each neighbor v has a flag indicating whether the original edge was u->v (so if in the tree structure u is the parent of v, then this edge contributes 0 to the reversal count; if the original edge is v->u, then when u is parent of v, the edge needs to be reversed (contribution 1)).

So when building the adjacency list, for each edge in the input (s, t), we can add to s's adjacency list an entry (t, 0) which means that if s is the parent of t, then the original edge is in the correct direction (no reversal needed). Also, add to t's adjacency list an entry (s, 1) which means that if t is the parent of s, then the original edge was s->t (so in the tree structure, the edge would be from t to s, but the original edge is s to t, so to have the edge from t to s, we need to reverse it, hence cost 1).

Yes, this makes sense. So the adjacency list entries for each node will have, for each neighbor, a direction flag that indicates the cost if the current node is the parent in the tree.

So for example, when building the adjacency list:

For input edge s -> t:

- For node s, add neighbor t with cost 0 (if s is parent, t is child, no reversal needed).
- For node t, add neighbor s with cost 1 (if t is parent, s is child, then the original edge is s->t, which is the reverse of t->s, so reversal needed, cost 1).

So during the initial traversal (rooted at 1), when we visit a node u and its child v, the cost contributed by the edge u->v is the value stored in u's adjacency list for v (which is 0 if the original edge is u->v, since s is u and t is v).

Once the initial count is computed for root 1, then for each other node, when we re-root the tree to v, which is a neighbor of u (the parent in the initial tree), the reversal count for v can be computed as:

count[v] = count[u] - cost_of_edge_u_to_v + (1 - cost_of_edge_v_to_u)

Wait, because when the root was u, the edge u-v was considered as u being the parent. The cost for this edge is the value stored in u's adjacency for v (which is 0 if original edge is u->v). When we re-root to v, the edge now is considered as v being the parent of u. The cost for this edge is the value stored in v's adjacency for u (which is 1 if original edge is u->v, since in this case, the original edge is u->v, and if v is parent, the edge is from v to u (which requires reversal, so cost 1)).

So the delta when switching root from u to v is (new_cost - old_cost). The old cost was the cost stored in u's adjacency for v (old_cost = 0). The new cost is the cost stored in v's adjacency for u (new_cost = 1). So the delta is (1 - 0) = 1, so the total count for v is count[u] + 1.

Wait, no. Wait, the initial count for u is sum of all edges in the tree. When we re-root to v, the edge between u and v now has the direction reversed in the tree structure. So for that edge, the contribution changes from old_cost (u as parent) to new_cost (v as parent). So the delta is (new_cost - old_cost). So the new count is count[u] - old_cost + new_cost.

So in the example where original edge is u->v (so s=u, t=v):

For root u, the edge u-v contributes 0 (old_cost = 0). For root v, the edge u-v now is part of the tree where v is the parent of u. The cost here is the cost stored in v's adjacency for u, which is 1 (since the original edge is u->v, and if v is parent of u, the required edge direction is v->u, which requires reversing the original edge. So new_cost is 1). So the delta is 1 - 0 = 1. So the count for v is count[u] + 1.

Wait, but wait. The original count was sum of all edges in the tree (as rooted at u). When we re-root to v, the entire tree is reoriented. But how many edges change their contribution? Only the edge between u and v. Because the rest of the tree is now part of the subtree of u (since when we re-root to v, u becomes a child of v, and the rest of the tree is now part of u's subtree). Wait, no. When you re-root the tree from u to v, the parent of u becomes v, and all the other subtrees of u (except the subtree containing v) are now part of u's subtree. But in terms of the reversal counts, the only edge whose direction (parent-child) changes is the u-v edge. All other edges in the tree retain their parent-child relationships, except those in the path from the original root (u) to the new root (v). Wait, no. Re-rooting changes the parent-child relationships for all nodes along the path from the old root to the new root.

Wait, no. When you re-root a tree to a node, the parent-child relationships for all nodes except those along the path between the old and new roots remain the same. For example, suppose the original tree is a chain 1-2-3-4, rooted at 1. If we re-root at 4, the parent of 4 becomes 3, the parent of 3 becomes 4, etc. All the edges along the path from 1 to 4 (i.e., 1-2, 2-3, 3-4) have their direction reversed. So the reversal counts for each of these edges would change. Therefore, when re-rooting the tree, the reversal count is affected not just by the edge between u and v, but by all edges along the path from the original root to the new root.

But that would be computationally expensive if we have to process all such edges each time. However, this suggests that the initial approach of using a dynamic programming approach with a single edge adjustment is not sufficient.

Hmm. This complicates things. Because if the root is changed to a node that's not adjacent to the original root, then the adjustment would involve multiple edges along the path from the original root to the new root.

But how can we compute this efficiently for all nodes?

Wait, perhaps the initial approach can be adjusted. Let me think again. The idea is that for any node, the reversal count can be computed based on its parent's reversal count. But this requires that when moving from parent to child, only the edge between them affects the reversal count.

But in the tree, when you re-root from a parent to a child, the reversal count changes only for the edge between them. Because the rest of the tree's edges are in the same parent-child relationships. Wait, is that true?

Let's take an example. Suppose we have a tree rooted at u. The edge u-v is part of the tree, with u as parent. The rest of the tree is in the subtree of u. When we re-root to v, the parent of u becomes v, and the rest of the tree (other than the subtree of v) is now part of u's subtree. So for all edges in the rest of the tree (apart from the edge u-v), their parent-child relationships remain the same as before. So their contribution to the reversal count remains the same.

Only the edge between u and v changes direction. So the reversal count for the new root (v) is the reversal count of u minus the contribution of the edge u-v (as u was parent) plus the contribution when the edge is considered as v being the parent of u.

This suggests that the initial approach is correct, and that when re-rooting from u to v (adjacent nodes), the reversal count can be adjusted by the delta from that single edge. Then, this can be propagated to all nodes via a post-order traversal.

Wait, but how do we handle nodes that are not adjacent to the current root? For example, if the root is node 1, and we want to compute the reversal count for node 3, which is two edges away (1-2-3), then re-rooting from 1 to 3 would involve two edges: 1-2 and 2-3. Each of these edges would change direction. So the reversal count for 3 would be the count for 1 minus the old cost of 1-2 plus the new cost (for 2 as parent of 1), then minus the old cost of 2-3 (when 2 was parent of 3) plus the new cost (when 3 is parent of 2). But how can this be handled efficiently?

Ah, but in the tree structure, when re-rooting, each node can be processed in a way that allows the reversal count to be computed based on its parent. So the initial approach of using a dynamic programming approach where each node's reversal count is computed based on its parent's reversal count plus or minus the delta from their connecting edge.

But how does this work for the entire tree?

Let's imagine that we first compute the reversal count for the initial root (say, node 1). Then, we perform a post-order traversal where for each node, after processing all its children, we can compute the reversal counts for those children by adjusting the parent's count.

Wait, no. Because when you re-root from a parent to a child, the parent becomes the child, and the child becomes the parent. So for each child of the initial root, their reversal count is computed based on the initial root's count. Then, for their children, their reversal counts are computed based on their parent's count (the child of the initial root), and so on.

This way, the process propagates through the tree, and each node's count is computed once, based on the parent's count and the delta of the edge between them.

So the algorithm steps would be:

1. Build the adjacency list with each edge's cost (0 or 1) for both directions.

2. Perform a post-order traversal starting from the initial root (e.g., node 1), computing the initial reversal count.

3. Then, perform a pre-order traversal (or another traversal) where, for each node, after processing the parent, we compute the reversal count for the current node based on the parent's reversal count and the delta from their connecting edge.

This way, for each node, the reversal count is computed in O(1) time once the parent's count is known. The total time is O(n), which is acceptable for n up to 2e5.

So the process is as follows:

- Compute the initial count for the root (say, node 1) via a post-order traversal. During this traversal, for each node, accumulate the sum of reversal costs for all edges in the subtree.

- Then, perform a second traversal (like a BFS or DFS) to compute the counts for all other nodes. For each node, when moving from the parent to the child, the reversal count is computed as parent_count - cost(parent -> child) + (1 - cost(child -> parent)), where cost(parent -> child) is the contribution when the parent is the parent of the child, and (1 - cost(child -> parent)) is the contribution when the child is the parent of the parent.

Wait, the cost when the child becomes the parent's parent. So for the edge between u (original parent) and v (child), when we re-root to v, the edge now is v as parent of u. So the cost for this edge is the cost stored in v's adjacency list for u. Which is the cost if v is the parent of u.

So the delta is (cost_v_u - cost_u_v). So the new count is parent_count - cost_u_v + cost_v_u.

Yes. So for each node v (child of u in the initial tree), the reversal count when v is the root is equal to the reversal count of u minus the cost of the edge u->v (as u was the parent) plus the cost of the edge v->u (as v is now the parent of u). Because all other edges' contributions remain the same, except for this edge.

So this way, once the initial root's count is computed, all other nodes' counts can be computed in O(n) time by traversing the tree again and applying this delta for each parent-child edge.

So the steps in code would be:

- Build the adjacency list with direction costs.

- Compute the initial count for root (node 1) using a DFS or BFS.

- Then, perform another traversal (BFS or DFS) to compute the counts for all other nodes based on their parent's count.

Now, the key is to model the adjacency list properly, so that for any edge between u and v, we can quickly look up the cost for u as parent of v, and v as parent of u.

So for each edge (s, t) in the input, we can add two entries:

- For s's adjacency list: a tuple (t, 0) → because if s is the parent, then the original edge is s->t, which contributes 0 reversals.

- For t's adjacency list: a tuple (s, 1) → because if t is the parent of s, then the original edge s->t would need to be reversed (contribution 1).

Wait, no. Let me think again. The original edge is s -> t. So:

- If the edge is part of the tree as u -> v (i.e., u is the parent of v), then the cost is 0 if the original edge is u->v, else 1.

So for example, the original edge is s->t.

- In the adjacency list of s, the entry for t is (t, 0) → if s is the parent of t, then the original edge is correct, so cost 0.

- In the adjacency list of t, the entry for s is (s, 1) → if t is the parent of s, then the original edge is s->t, which is the reverse of t->s. So this edge must be reversed, cost 1.

Similarly, for an original edge t->s:

- In s's adjacency list, the entry for t is (t, 1) → if s is the parent of t, then original edge is t->s (reverse), cost 1.

- In t's adjacency list, the entry for s is (s, 0) → if t is the parent of s, original edge is t->s, cost 0.

So for each input edge s->t, we add two entries in the adjacency lists:

s's adj list: (t, 0)

t's adj list: (s, 1)

Wait, no. Because the original edge is s->t. So when s is the parent of t in the tree, the original direction is correct (no reversal needed → cost 0). When t is the parent of s, the original direction is s->t, which is the reverse of the required direction (t->s). So in that case, the cost is 1 (reversal needed). So for the adjacency lists:

For s's adjacency list entry for t: when s is the parent of t, cost is 0.

For t's adjacency list entry for s: when t is the parent of s, cost is 1.

Yes. So when building the adjacency list, for each original edge s->t:

adj[s].append( (t, 0) )

adj[t].append( (s, 1) )

That's the correct way to model it.

Once the adjacency list is built, the initial count can be computed via a DFS starting from the initial root. For each node, when visiting its children (as per the tree structure), we add the cost stored in the adjacency list for that edge.

Then, during the second traversal (which is a BFS or DFS), for each node, when moving from parent u to child v (in the initial tree), we compute the count for v as count[u] - cost (u to v) + (1 - cost (v to u)).

Wait, the cost (v to u) is the cost stored in v's adjacency list for u. So for example, when u is the parent of v in the initial tree, the edge is u->v. The cost in u's adjacency for v is 0. When we re-root to v, the edge becomes v->u. The cost is the value in v's adjacency list for u, which is 1 (as per the example). So the delta is 1 - 0 = 1. So the count for v is count[u] - 0 + 1 = count[u] + 1.

But wait, how is that possible? Let's take the first sample input:

Sample Input 1:

3

2 1

2 3

Sample Output:

0

2

So the tree structure when directions are ignored is 2 connected to 1 and 3. The edges are 2->1 and 2->3. So when the root is 2, the edges are directed from 2 to 1 and 2 to 3. So no reversals are needed. Hence count is 0.

But according to the algorithm:

The adjacency list would be:

For edge 2->1:

adj[2] has (1, 0)

adj[1] has (2, 1)

For edge 2->3:

adj[2] has (3, 0)

adj[3] has (2, 1)

Initial root is 1. Let's compute the count for root 1.

But wait, the initial root is chosen as 1. How is the tree structured? The tree is built as a normal tree, but the initial root is 1. But the actual tree (as per the edges) may not allow for a tree rooted at 1. Wait, but since the tree is undirected, the structure is built as a tree with parent-child relationships according to the traversal.

Wait, no. The problem is that when you build the tree (as an undirected tree), the parent-child relationships are determined by the traversal. So when the initial root is 1, the tree is built such that 1's children are those nodes connected via edges, except for the parent (which is none in the case of the root). But in the original sample input, the edges are 2->1 and 2->3. So the undirected tree is 1 connected to 2 connected to 3. So when the root is 1, the tree structure is 1 as root, with child 2, and 2 has child 3.

But the original edges are 2->1 and 2->3. So for the edge between 1 and 2 in the tree (rooted at 1), 1 is the parent and 2 is the child. The original edge is 2->1, so the direction is from child to parent. So in the adjacency list, for node 1's entry for 2: since the edge is 2->1, when 1 is the parent of 2 (as per the initial traversal), the original direction is 2->1. So the cost is 1 (since the edge is child to parent; the required direction is parent (1) to child (2), so the original edge is reversed, cost 1).

Wait, but the adjacency list for node 1's neighbors includes 2, and the cost stored is 1 (since the edge is 2->1, so when 1 is the parent of 2, the original direction is 2->1 → which is opposite to parent to child, so cost is 1).

So during the initial traversal (root 1), the edge between 1 and 2 contributes 1. Then, the edge between 2 and 3 (original direction 2->3, when 2 is the parent of 3) contributes 0. So the initial count for root 1 is 1 + 0 = 1.

Then, when re-rooting to 2, the count is computed as count[1] - cost_1_2 (1) + cost_2_1 (which is the cost when 2 is the parent of 1. The original edge is 2->1, so for the edge 2-1 when 2 is parent, the cost is 0 (since original direction is 2->1, which is parent to child). So the delta is 0 - 1 = -1. So count[2] = 1 -1 + 0 (wait, no: count[2] = count[1] - cost_1_2 + cost_2_1. So count[1] is 1. cost_1_2 is 1 (the contribution when 1 is parent of 2). cost_2_1 is the contribution when 2 is parent of 1, which is 0 (original edge is 2->1). So count[2] = 1 -1 + 0 = 0. Which matches the sample.

Then, when re-rooting to 3, the count is computed based on 2's count. The edge between 2 and 3 in the initial tree has cost 0 (original edge is 2->3, so when 2 is parent of 3, cost 0). When re-rooting to 3, the cost becomes the contribution from 3's adjacency list for 2, which is 1. So the delta is 1 - 0 = 1. So count[3] = 0 -0 +1 = 1.

So the counts for all nodes are:

1: 1

2:0 

3:1 

Hence the minimum is 0, and the only node is 2. So the sample is correct.

This suggests that the algorithm works.

So the steps are:

1. Build adjacency list with cost for each direction.

2. Choose an initial root (like 1) and compute the initial count via DFS.

3. Use a BFS or DFS to propagate the count to all other nodes.

Now, the code steps:

We need to:

- Read n.

- Read n-1 edges, build the adjacency list.

- Build a tree structure (as adjacency list with parent pointers).

But how to build the tree structure? Because when we traverse, we need to avoid cycles. So during the initial DFS for the first root (1), we can track parents and children.

But for large n (2e5), recursive DFS may hit stack limits. So better to use iterative DFS or BFS.

Let's proceed step by step.

First, build the adjacency list. For each edge s, t:

adj[s].append( (t, 0) )

adj[t].append( (s, 1) )

Then, we need to compute the initial count for root 1.

To do this, perform a BFS or DFS starting from 1, building the tree structure (parent pointers), and summing the costs.

Initialize the count as 0.

Then, for each node in the tree (starting from 1), iterate over its children (excluding the parent), and add the cost stored in the adjacency list for that edge.

Once the initial count is computed, perform a BFS (or DFS) to compute the counts for all other nodes.

In this BFS, we start from the initial root and process each child. For each child, compute the count using the parent's count.

For example, in code:

We have a queue (for BFS) starting with the initial root. For each node u dequeued, we iterate over its adjacency list. For each neighbor v, if v is not the parent of u (in the initial tree), we skip (since in the initial tree, u's parent is already processed). Wait, no. Because when we are re-rooting, the parent and child relationships are reversed. So in the initial tree, each node's children are stored, and during the BFS for re-rooting, when processing u, we need to visit all its children (as per the initial tree) and compute their counts.

Alternatively, during the initial BFS/DFS to build the tree, we can track the children of each node (excluding the parent). Then, during the second traversal, for each node u, we can iterate over all its children in the initial tree, and compute their count as count[u] - cost_u_v + cost_v_u.

Wait, but in the second traversal, the tree structure is not the same as the initial tree. The initial tree is built with the first root, and the children are determined accordingly. However, during the second traversal, when we re-root to a child, the parent becomes the child. So for each node, when we compute its count, we can process all of its neighbors (excluding the parent in the initial tree) as possible children in the re-rooted tree.

Alternatively, during the second traversal (for propagating the counts), we can process each node and iterate through all of its adjacent edges (excluding the parent in the initial tree). But in the adjacency list, the parent is known.

But perhaps the simplest way is to first build a parent array for the initial tree. Then, for each node u, during the second traversal, its children in the initial tree are those nodes v where parent[v] == u. For these nodes, we can compute their counts as count[u] - cost_u_v + cost_v_u.

But then, for nodes that are not children in the initial tree (like the parent of u in the initial tree), how do we process them?

Ah, because the re-rooting process allows for the parent to be any node. So, for example, when processing a node u, which was a child of node p in the initial tree, we can compute the count for p by using u's count. But how?

Wait, no. Because once the count for u is computed, we can process all of its neighbors. For example, after computing count[u], for each neighbor v, if v is not the parent in the initial tree, then we can process them as children. But this approach would process all nodes multiple times.

Alternatively, the second traversal should be a BFS that starts from the initial root and propagates to all nodes. For each node u, when we process it, we have already computed its count, and we can compute the counts for all of its adjacent nodes (except the parent in the initial tree) by adjusting the delta for the edge between u and v.

Wait, but in the initial tree, the parent of u is p. So when processing u, the nodes that are children of u in the initial tree can be processed as follows: their count can be computed based on u's count. For the parent p of u in the initial tree, their count can be computed by u's count, but how?

This suggests that the second traversal should process all edges once, but this is not feasible. So perhaps the correct way is to perform a BFS that starts from the initial root and visits all nodes. For each node u, we process all its adjacent nodes v. For each v, if v is not the parent of u in the initial tree, we can compute v's count as count[u] - cost (u to v) + cost (v to u). But then, how do we avoid reprocessing edges? Because when we visit v, we might reprocess the edge back to u.

This is a problem because the BFS could potentially process each edge twice, leading to O(n) time but with higher constants.

Alternatively, during the initial BFS/DFS to build the tree, we can record for each node u its parent and children. Then, during the second traversal, for each node u, we can process all its children in the initial tree (as per the parent array). For the parent of u in the initial tree, we can compute the count for u by adjusting the parent's count, and then process the parent's other children.

Wait, but the parent of u in the initial tree (p) would have their count computed first. When processing p, we can process all of its children (including u) and compute their counts. But for u, when we process it, we can process all of its children (in the initial tree) and compute their counts. The parent of u (p) is already processed, so we don't need to process it again.

So the algorithm would be:

1. Build adjacency list with cost for each edge direction.

2. Perform a BFS/DFS starting from the initial root (say 1) to build the parent array and compute the initial count.

3. Initialize a queue with the initial root.

4. For each node u in the queue:

   a. For each child v in u's children (as per the parent array):

      i. Compute count[v] = count[u] - cost_u_v + cost_v_u.

      ii. Add v to the queue.

So this way, each node is processed once, and the counts are propagated correctly.

But in this approach, the parent array is built from the initial BFS/DFS. The children are those nodes v where parent[v] == u. So during the second traversal (the queue processing), we process each node's children in the initial tree.

But this will not process nodes that are parents in the initial tree, but when re-rooted, become children. For example, if u is a child of p in the initial tree, then p's count can be computed based on u's count. But in the queue processing as described, u's children (initial tree's grandchildren) are processed, but not the parent p.

So this approach will miss the parent nodes.

Wait, no. Because the initial root is 1, and the queue starts with 1. 1's children are processed, their counts are computed, and added to the queue. Then, when processing those children, their children are processed, and so on. This way, all nodes are processed once. But this only works for the initial tree's children. For example, in the first sample, the initial tree has root 1, which has child 2. Then 2 has child 3. The queue processes 1, then 2, then 3. So when processing 2, the count for 2 is computed (0). Then, when processing 3, it has no children (as per the initial tree), so nothing is done.

But what about when a node is not a child of the initial root? For example, consider a tree where the initial root is 1, and there is a node 4 that is a child of 2. When processing 2, the children (4) are processed. But when re-rooting to 4, the count is computed based on 2's count. So this works.

But what about nodes that are parents in the initial tree? For example, if the initial tree is a chain 1-2-3-4, and we re-root to 3, which is a child of 2 in the initial tree. Then, 3's count is computed based on 2's count. When processing 3, its children (4) are processed. But the parent 2's count could be updated based on 3's count. However, in this approach, 2's count is already computed before 3 is processed, and there is no way to propagate the count back up.

Wait, this suggests that the approach only works for the initial tree's structure and its children. But when a node's parent in the initial tree is processed after the node, their counts cannot be updated.

But this is incorrect. Because in the initial tree's structure, the parents are processed before the children. So for example, when processing node 2 in the initial tree (child of 1), its count is computed based on 1's count. Then, when processing node 3 (child of 2), its count is computed based on 2's count. But what if re-rooting to node 3's child (4) allows for a lower count? The algorithm would process 4's count based on 3's count, but there's no way to propagate back to 3.

But that's not the case. The algorithm correctly computes the counts for all nodes as follows:

- The initial root's count is computed.

- For each node in the initial tree, the count is computed based on its parent's count.

So, in the example of a chain 1-2-3-4:

Initial count for 1 is computed (sum of edges in the tree when rooted at 1).

Count for 2 is computed as count[1] - cost_1_2 + cost_2_1.

Count for 3 is computed as count[2] - cost_2_3 + cost_3_2.

Count for 4 is computed as count[3] - cost_3_4 + cost_4_3.

This way, all counts are computed correctly.

So the approach works.

Thus, the code steps are:

- Read input, build adjacency list with direction costs.

- Build parent array and children lists via BFS/DFS from the initial root.

- Compute initial count via BFS/DFS.

- Initialize a queue with the initial root.

- For each node u in the queue:

   - For each child v in u's children (from the initial tree):

      - Compute count[v] = count[u] - cost_u_v + cost_v_u.

      - Add v to the queue.

- Find the minimum count among all nodes.

- Collect all nodes with the minimum count, sort them, and output.

But how do we track the cost_u_v and cost_v_u for each edge between u and v?

The adjacency list stores for each node u, a list of (v, cost). When u is the parent of v in the initial tree, the cost_u_v is the cost stored in u's adjacency list for v.

But during the initial BFS/DFS to build the parent array, we can also track the cost for each edge between parent and child.

For example, during the initial BFS:

For each node u, when we visit a neighbor v which is not the parent, we record v as a child of u and store the cost of the edge from u to v (i.e., the cost stored in u's adjacency list for v).

So, during the initial BFS, we can build a list for each node's children and the corresponding cost.

This way, during the second traversal, for each child v of u (in the initial tree), we can look up the cost_u_v (the cost stored in u's adjacency list for v) and cost_v_u (the cost stored in v's adjacency list for u).

But how?

Wait, during the initial BFS, when building the parent array, we can also build a cost array. For each node v, parent_cost[v] is the cost of the edge from parent[v] to v.

So for example, parent[v] = u, and parent_cost[v] = cost_u_v.

Then, when processing the children of u in the initial tree, the cost_u_v is parent_cost[v], and cost_v_u is the cost stored in v's adjacency list for u.

But how to find cost_v_u quickly?

Because in the adjacency list of v, we can find the entry for u and get the cost.

So for each node v, when we have parent[v] = u, then in v's adjacency list, the entry for u will have the cost for when v is the parent of u.

But to find that entry, we can iterate through v's adjacency list until we find the entry where the neighbor is u. However, this is O(1) if we build a dictionary for each node's adjacency.

But for large n, iterating through the adjacency list of v to find u would take O(1) time on average, but in the worst case, it's O(1) if each adjacency list is stored as a dictionary.

So to optimize, for each node u, we can create a dictionary that maps each neighbor to its cost.

Alternatively, during the initial BFS, when building the parent and parent_cost array, we can also build a dictionary for each node that stores the cost for each neighbor.

But with n up to 2e5, building such a dictionary may not be feasible in terms of memory. However, for each node, the number of entries in the dictionary is equal to its degree, which is O(1) on average for a tree.

So, the plan is:

For each node u, during the initial BFS:

- For each neighbor v in adj[u], if v is not the parent[u], then v is a child of u. We can store the cost of the edge from u to v (i.e., the cost stored in adj[u] for v).

But during the initial BFS, for each node u, when visiting a neighbor v, if v is not the parent of u, then we set parent[v] = u and parent_cost[v] = the cost of the edge from u to v (adj[u]'s entry for v).

But how do we find that entry?

In the adjacency list of u, each entry is a tuple (v, cost). When processing u, we can iterate over all its adj entries. For each (neighbor, cost), if neighbor is not parent[u], then neighbor becomes a child of u, and we record the cost.

So during the initial BFS:

Initialize parent array and parent_cost array.

queue = deque([1])

parent = [0]*(n+1)

parent_cost = [0]*(n+1)

parent[1] = -1 (or 0, but we need to mark the root)

But for example:

parent = [0]*(n+1)

parent[1] = 0

visited = [False]*(n+1)

visited[1] = True

queue.append(1)

while queue not empty:

    u = queue.popleft()

    for (v, cost) in adj[u]:

        if not visited[v]:

            parent[v] = u

            parent_cost[v] = cost

            visited[v] = True

            queue.append(v)

This way, for each node v, parent[v] is its parent in the initial tree, and parent_cost[v] is the cost of the edge from parent[v] to v (i.e., the cost when the edge is part of the tree with parent[v] as parent of v).

Then, during the second traversal (computing counts for all nodes), for each node u, its children are those nodes v where parent[v] == u.

So during the second traversal:

count array is initialized with the initial count for root 1.

count = [0]*(n+1)

count[1] is computed during the initial BFS.

Wait, no. The initial count is computed during the initial BFS. How?

Wait, during the initial BFS, the initial count is the sum of parent_cost[v] for all nodes v except the root.

Because for the root, there's no parent. For all other nodes, the parent_cost[v] is the cost of the edge from parent[v] to v. So the total count is the sum of parent_cost[v] for all v from 2 to n.

So initial_count = sum(parent_cost[2..n])

This is O(n) time, but for n up to 2e5, this is acceptable.

Alternatively, during the initial BFS, we can accumulate the count.

Yes. For example:

count = 0

queue = deque([1])

parent = [0]*(n+1)

parent[1] = 0

visited = [False]*(n+1)

visited[1] = True

while queue not empty:

    u = queue.popleft()

    for (v, cost) in adj[u]:

        if not visited[v]:

            parent[v] = u

            count += cost

            visited[v] = True

            queue.append(v)

So this way, during the initial BFS, we compute the initial count as the sum of all parent_cost[v] (i.e., the cost of the edges in the initial tree).

So the initial count is correct.

Then, the second traversal is a BFS starting from the initial root. For each node u, we process its children in the initial tree (those v where parent[v] = u). For each such child v, compute count[v] = count[u] - parent_cost[v] + cost_v_u.

But how to find cost_v_u?

cost_v_u is the cost stored in v's adjacency list for u.

But the adjacency list for v is a list of tuples. So for each v, to find the cost for u (which is the parent of v in the initial tree), we can loop through v's adjacency list until we find the entry for u, then get the cost.

But this is O(1) per edge on average, since each node's adjacency list has O(1) entries (tree structure).

But for each child v of u, we need to find the cost of the edge from v to u (which is the cost stored in v's adjacency list for u).

So during the second BFS:

We have a queue initialized with root (1).

count[1] = initial_count.

For each u dequeued:

   for v in children of u (from parent array):

       # compute cost_v_u: cost when v is parent of u.

       # iterate through v's adjacency list to find the entry for u.

       for (neighbor, cost) in adj[v]:

           if neighbor == u:

               cost_v_u = cost

               break

       # compute count[v]

       count[v] = count[u] - parent_cost[v] + cost_v_u

       queue.append(v)

But for each v, this loop through adj[v] can take O(1) time on average. For example, in a tree, each node has O(1) adj entries, so the loop is O(1).

But for 2e5 nodes, this is acceptable.

So this approach is feasible.

Now, the code:

Implement the steps:

Read n.

Read n-1 edges, build adjacency list with cost for each direction.

Build parent array and initial count via BFS.

Compute cost_v_u for each child v of u.

Perform second BFS to compute counts for all nodes.

Find the minimum count.

Collect all nodes with minimum count.

Sort them and output.

Now, the code in Python.

But for Python, handling 2e5 nodes with BFS and adjacency lists can be efficient if implemented properly.

But for the adjacency list, perhaps using a list of lists is sufficient.

Now, let's test with the first sample:

Sample Input 1:

3

2 1

2 3

Adjacency list for 1:

[(2, 1)] (since the edge is 2->1. So for 1's adj list, the entry for 2 is 1: because if 1 is the parent of 2, the original edge is 2->1. So cost is 1.)

Adjacency list for 2:

[(1, 0), (3, 0)] (because the edges are 2->1 and 2->3. So for 2's adj list, entry for 1 is 0 (if 2 is parent of 1, cost is 0 because original edge is 2->1), and entry for 3 is 0 (original edge is 2->3).

Adjacency list for 3:

[(2, 1)] (edge is 2->3. So for 3's adj list, the entry for 2 is 1: if 3 is parent of 2, the original edge is 2->3, which requires reversal, cost 1.

Initial BFS:

Starts at 1. Visits 1's adj entries. For each entry (2, 1), if not visited, set parent[2] =1, parent_cost[2] =1. count +=1.

Then 2 is processed. Its adj entries are (1,0) and (3,0). 1 is already visited (parent). For 3: not visited. parent[3]=2, parent_cost[3]=0. count +=0.

count becomes 1.

Initial count is 1.

Second BFS:

queue starts with 1. count[1] =1.

Processing 1:

children are 2.

For v=2:

Find cost_v_u (u=1). Look through adj[2] for 1. The entry is (1, 0).

So cost_v_u =0.

count[2] = count[1] - parent_cost[v] (which is 1) + cost_v_u (0) → 1 -1 +0=0.

Add 2 to queue.

queue now has 2.

Processing 2:

children are 3.

For v=3:

Look through adj[3] for 2: the entry is (2, 1).

cost_v_u =1.

count[3] = count[2] -0 (parent_cost[3] is 0) +1 →0 -0 +1=1.

Add 3 to queue.

Processing 3:

No children (parent[3] is 2, so no other children).

So counts are:

1:1, 2:0, 3:1.

Minimum is 0, nodes is 2.

Sample Input 2:

4

1 4

2 4

3 4

Output:

2

1 2 3

Let's see:

The edges are directed to 4. So the undirected tree is 4 connected to 1, 2, 3.

If we choose 4 as the capital, all edges are directed away from 4. So no reversals needed. But the output of the sample is 2, with the possible capitals 1,2,3. So perhaps I made a mistake in the initial analysis.

Wait the sample input's output is:

2

1 2 3

So when the capital is 1, 2, or 3, the number of reversals is 2. How?

Wait, the input is:

Edges are 1->4, 2->4, 3->4.

The undirected tree is a star with 4 at the center.

If the capital is 1, then all roads must allow movement from 1 to every other city.

So the roads need to form a tree where 1 is the root. The path from 1 to 4 must be directed towards 4 (since 1 is the root). Then, from 4, the paths to 2 and 3 must be directed towards 2 and 3.

But the original edges are 1->4, 2->4, 3->4.

So when choosing 1 as the capital:

- The edge 1->4 is correct. No reversal.

- The edges 2->4 and 3->4 must be reversed to 4->2 and 4->3. But for 1 to reach 2 and 3, the path is 1->4->2 and 1->4->3.

But the edges 2->4 and 3->4 are directed into 4. So to have the path from 4 to 2, we need to reverse 2->4 to 4->2. Similarly for 3->4.

So total reversals: 2.

Hence the sample's output.

So according to the algorithm:

Initial root is 1.

But in the initial tree, when rooted at 1, the tree would have 1 as root with child 4. Then, 4 has children 2 and 3.

Wait, no. The initial tree is built via BFS from 1. So the adjacency list for 1 includes 4 (edge 1->4, cost 0). So during the initial BFS, 4's parent is 1, and parent_cost[4] is 0.

Then, 4's adj list entries are 1 (cost 1), 2 (cost 1), 3 (cost 1), and 4's children in the initial tree are 2 and 3.

Wait, no. During the initial BFS, when processing 1:

neighbors are 4. So 4 is added to the queue, parent is 1, parent_cost[4] is 0 (since the original edge is 1->4).

Then, processing 4:

adj entries are 1 (cost 1), 2 (cost 1), 3 (cost 1).

For each neighbor:

- 1 is already visited.

- 2 is not visited. parent[2] =4, parent_cost[2] =1. count +=1.

- 3 is not visited. parent[3] =4, parent_cost[3] =1. count +=1.

So initial count is 0 (from 4) +1 (from 2) +1 (from3) = 2.

Then, during the second BFS:

Processing 1:

children are 4.

count[1] = 2.

For v=4:

cost_v_u (u=1) is the cost in 4's adj list for 1, which is 1.

count[4] = count[1] - parent_cost[4] (0) + 1 → 2 -0 +1=3.

Add 4 to queue.

Processing 4:

children are 2 and 3.

For v=2:

parent_cost[v] =1. cost_v_u is the cost in 2's adj list for 4. Original edge is 2->4. So in 2's adj list, 4 has cost 1 (if 2 is parent of 4, the original edge is 2->4, which is correct, cost 0. Wait no. The original edge is 2->4. So when building the adjacency list:

For edge 2->4:

adj[2].append( (4, 0) )

adj[4].append( (2, 1) )

So for 4's adj entry for 2: (2, 1).

For 2's adj entry for 4: (4, 0).

So during the initial BFS, when 4's parent is 1, and the edge is 1->4, the parent_cost[4] is 0.

But when processing v=2 (child of 4 in the initial tree):

the parent_cost[2] is 1 (because the edge 4->2 is the original edge 2->4. So when 4 is parent of 2, the cost is 1 (original edge is 2->4. So for the tree edge 4->2, the original edge is 2->4. So the cost is 1 (need to reverse)).

So during the initial BFS, the count is 0 (4's parent) +1 (2's parent) +1 (3's parent) = 2.

Then, during the second BFS:

Processing 1:

count[1] = 2.

Processing child 4:

cost_v_u is cost in 4's adj list for 1: 1.

count[4] = 2 - 0 (parent_cost[4] is 0) + 1 →3.

Then, processing 4's children: 2 and 3.

For v=2:

cost_v_u is the cost in 2's adj list for 4: 0.

count[2] = count[4] (3) - parent_cost[2] (1) + 0 →3-1+0=2.

Similarly for v=3: count[3] =3-1+0=2.

So the counts are:

1: 2

4:3

2:2

3:2

So the minimum count is 2, achieved by nodes 1,2,3.

Hence the sample's output.

Thus, the algorithm works.

So now, the code in Python:

Implement the steps.

But to handle the adjacency list efficiently, for each node, when looking for the cost of an edge to a neighbor, we need to find it in the adjacency list. To make this efficient, perhaps preprocess each adjacency list into a dictionary.

Alternatively, during the initial BFS, we can build a dictionary for each node's adjacents.

But for Python, with n up to 2e5, building a list of dictionaries is feasible.

So, during reading the input:

adj = [[] for _ in range(n+1)]

for each edge s, t:

   adj[s].append( (t, 0) )

   adj[t].append( (s, 1) )

But to look up the cost from v to u quickly, we can create a dictionary for each node v that maps neighbor u to cost.

So:

adj_dict = [dict() for _ in range(n+1)]

for each edge s, t:

   adj_dict[s][t] = 0

   adj_dict[t][s] = 1

But this requires O(n) space and is manageable.

Yes, this would allow O(1) lookups for the cost between any two nodes.

Thus, during the second traversal, for a node v and its parent u, to get cost_v_u (the cost when v is the parent of u), we can just do adj_dict[v][u].

So the code steps in Python:

Read n.

Read n-1 edges, build adj_dict.

Perform BFS to find parent and parent_cost.

Compute initial count.

Perform BFS to compute counts for all nodes.

Collect results.

Now, code:

import sys
from collections import deque

n = int(sys.stdin.readline())

adj_dict = [dict() for _ in range(n+1)]
for _ in range(n-1):
    s, t = map(int, sys.stdin.readline().split())
    adj_dict[s][t] = 0
    adj_dict[t][s] = 1

parent = [0]*(n+1)
parent_cost = [0]*(n+1)
visited = [False]*(n+1)
q = deque()
q.append(1)
visited[1] = True
parent[1] = 0
count = 0

while q:
    u = q.popleft()
    for v in adj_dict[u]:
        if not visited[v] and v != parent[u]:
            visited[v] = True
            parent[v] = u
            cost = adj_dict[u][v]
            parent_cost[v] = cost
            count += cost
            q.append(v)

# Now compute the counts for all nodes
counts = [0]*(n+1)
counts[1] = count

q = deque()
q.append(1)

while q:
    u = q.popleft()
    for v in adj_dict[u]:
        if parent[u] != v and parent[v] == u:  # v is a child in the initial tree
            # compute cost_v_u
            cost_v_u = adj_dict[v][u]
            counts[v] = counts[u] - parent_cost[v] + cost_v_u
            q.append(v)

# Now find the minimum count and collect the nodes
min_count = min(counts[1:])
result = [i for i in range(1, n+1) if counts[i] == min_count]
result.sort()

print(min_count)
print(' '.join(map(str, result)))

Wait, but wait. The line:

if parent[u] != v and parent[v] == u:

This is checking that v is a child of u in the initial tree (since parent[v] == u), and that v is not the parent of u (which is redundant since parent[v] == u implies u is parent of v, and parent[u] can't be v unless it's a cycle, which is impossible in a tree).

But this line is trying to find the children of u in the initial tree.

Yes. Because parent[v] == u implies that v is a child of u.

So the code processes all children of u in the initial tree.

But for each child v, during the second BFS, the count is computed and the child is added to the queue.

This way, all nodes are processed in BFS order.

Testing this code with the first sample:

Sample Input 1:

3

2 1

2 3

adj_dict is:

adj_dict[2][1] =0, adj_dict[1][2]=1.

adj_dict[2][3]=0, adj_dict[3][2]=1.

Initial BFS:

Process 1.

Check its adj_dict entries: 2.

parent[2] =1, parent_cost[2] = adj_dict[1][2] →1.

count is 1.

Then process 2.

Check adj_dict[2] entries: 1 and 3.

1 is parent. 3 is not visited.

parent[3] =2, parent_cost[3] = adj_dict[2][3] →0.

count increases by 0 → total 1.

Then process 3.

No children.

Initial count is 1.

counts[1] =1.

Then, second BFS:

Process 1.

For v in adj_dict[1] (2).

Check if parent[u] (0) != v (2) and parent[v] ==u (yes).

cost_v_u = adj_dict[2][1] →0.

counts[2] = counts[1] (1) - parent_cost[2] (1) +0 →0.

Add 2 to queue.

Process 2.

Check adj_dict[2] entries 1 and 3.

For v=1: parent[2] is 1, so v=1 is not child.

For v=3: parent[3] is 2 → child.

cost_v_u = adj_dict[3][2] →1.

counts[3] =0 -0 +1 →1.

Add 3 to queue.

Process 3: no children.

counts are 1,0,1.

Sample 1's output is 0 and node 2.

Correct.

Sample 2:

Input:

4

1 4

2 4

3 4

adj_dict:

adj_dict[1][4] =0, adj_dict[4][1] =1.

adj_dict[2][4]=0, adj_dict[4][2]=1.

adj_dict[3][4]=0, adj_dict[4][3]=1.

Initial BFS:

Process 1.

adj_dict[1] has 4. Not visited.

parent[4] =1, parent_cost[4] =0. count +=0.

Process 4.

adj_dict[4] has 1 (cost 1), 2 (cost 1), 3 (cost 1).

Check 2: not visited. parent[2] =4, parent_cost[2] =1. count +=1.

Check 3: not visited. parent[3] =4, parent_cost[3] =1. count +=1.

Process 2: adj_dict[2] has 4 (cost 0). No children.

Process 3: same.

Initial count is 0 +1 +1 = 2.

counts[1] =2.

Second BFS:

Process 1.

child is 4.

cost_v_u = adj_dict[4][1] →1.

counts[4] =2 -0 +1=3.

Process 4.

children are 2 and 3.

For v=2:

cost_v_u = adj_dict[2][4] →0.

counts[2] =3 -1 +0=2.

For v=3:

cost_v_u = adj_dict[3][4] →0.

counts[3] =3-1+0=2.

Process 2 and 3: no children.

counts[1]=2, counts[4]=3, counts[2}=2, counts[3}=2.

Thus, the minimum is 2, nodes 1,2,3.

Correct.

Thus, the code should work.
</think>

```python
import sys
from collections import deque

def main():
    n = int(sys.stdin.readline())
    adj_dict = [dict() for _ in range(n + 1)]
    for _ in range(n - 1):
        s, t = map(int, sys.stdin.readline().split())
        adj_dict[s][t] = 0
        adj_dict[t][s] = 1

    parent = [0] * (n + 1)
    parent_cost = [0] * (n + 1)
    visited = [False] * (n + 1)
    q = deque([1])
    visited[1] = True
    count = 0

    while q:
        u = q.popleft()
        for v in adj_dict[u]:
            if not visited[v] and v != parent[u]:
                visited[v] = True
                parent[v] = u
                cost = adj_dict[u][v]
                parent_cost[v] = cost
                count += cost
                q.append(v)

    counts = [0] * (n + 1)
    counts[1] = count
    q = deque([1])

    while q:
        u = q.popleft()
        for v in adj_dict[u]:
            if parent[v] == u:
                cost_v_u = adj_dict[v][u]
                counts[v] = counts[u] - parent_cost[v] + cost_v_u
                q.append(v)

    min_count = min(counts[1:])
    result = [i for i in range(1, n + 1) if counts[i] == min_count]
    result.sort()

    print(min_count)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
```