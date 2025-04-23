<think>
Okay, let's try to figure out this problem. So the problem is about a tree structure that's built incrementally. Each new level adds a new node as a child to some existing node. After each addition, we need to compute the number of nodes that are endpoints of the longest possible path in the current tree. 

The maximum distance in a tree is called its diameter. So the key here is that after each addition, we need to track the current diameter of the tree and then count how many nodes are endpoints of some longest path (diameter). Because each time a new node is added, the diameter might stay the same or increase. Then, for each step, the output is the count of nodes that are part of any such maximum-length path.

Wait, no. The problem says that for each level i, after adding the node i+1 (since the initial tree has node 1, and each level adds a new node), compute the number of nodes that have some other node at exactly the maximum possible distance. So, for each step, find all nodes that are endpoints of the current diameter. Then, the output is the count of such nodes.

But how do we track this efficiently as the tree grows?

First, let's think about the diameter of a tree. The diameter is the longest path between any two nodes. For a tree, the diameter can be found using BFS twice or using a dynamic approach. But since the tree is built incrementally, we need an efficient way to track the diameter and the nodes involved as each new node is added.

Let's think about the properties. When a new node is added, the diameter can either remain the same or increase by 1. Because the new node is a leaf, and the maximum path could be from this new node to one of the existing furthest nodes.

But how to track this? The standard approach for maintaining diameter in a dynamically growing tree might involve keeping track of the current endpoints of the diameter.

Wait, here's an idea. The diameter of a tree can be updated when adding a new node. Let's say the current diameter is D between nodes u and v. When adding a new node w as a child of some node y. The possible new diameter could be max(D, distance(w, u), distance(w, v)). Because the furthest node from w might be u or v, or the existing diameter could still be longer.

So, perhaps we can track the current endpoints of the diameter (u and v). Then, for each new node, we check the distances from the new node to u and v. The maximum of these distances is a candidate for the new diameter. If this candidate is larger than the current diameter, then the new diameter is this value, and the endpoints are the new node and whichever of u or v was further from it. Otherwise, the diameter remains the same, and the endpoints are unchanged.

But how do we compute the distance between two nodes efficiently? Since the tree is built incrementally, each node's depth and ancestors can be tracked. The distance between two nodes a and b is equal to the depth of a + depth of b - 2 * depth of their LCA (lowest common ancestor). However, finding the LCA for arbitrary nodes with O(1) or O(log n) time per query is possible with techniques like binary lifting, but building that structure incrementally for each node might be feasible.

But given that m can be up to 3e5, we need an O(1) or O(m) per operation approach. Binary lifting for LCA has O(log n) time per query, which might be acceptable for 3e5 operations, but integrating that into the solution might be manageable.

Alternatively, since the tree is a forest where each new node is added as a child to an existing node, the tree is a collection of nodes linked in a parent-child hierarchy. So, each node has a parent, and the tree is built in a way where each node's depth is known (depth of parent plus one). The LCA of two nodes can be found by moving the deeper node up until both are at the same depth, then moving both up until they meet. But this would take O(d) time per LCA query, where d is the depth difference, which could be up to O(m) in the worst case. That's not acceptable for m=3e5.

Therefore, we need a way to compute the distance between two nodes quickly. Binary lifting would allow us to compute the LCA in O(log n) time, and then the distance in O(1) time. So for each node, we can precompute ancestors at 2^k levels up, which allows us to compute the LCA efficiently.

So the plan is:

1. For each node, track its depth and build a binary lifting table for LCA queries.

2. Keep track of the current diameter's endpoints (u, v) and the current maximum distance (diam).

3. For each new node added, compute the distance from this node to u and to v. Let the maximum of these two be candidate_dist. The new diameter is the maximum between the current diam and candidate_dist. 

4. If the new diameter is larger than the current, update the endpoints. For example, if the distance from the new node (w) to u is larger than diam, then the new endpoints are w and u. Similarly for v.

5. Once the new diam is determined, the count is the number of nodes that are endpoints of any diameter path.

But how do we track the count? Because there can be multiple pairs of nodes that form the diameter. For example, in a linear tree (like a straight line), the diameter is the length of the line, and the two endpoints are the only ones. But in a tree where there's a central node with multiple branches of equal length, the diameter could be 2*max_depth, and there might be multiple nodes contributing to this.

Wait, no. The diameter is the longest path in the tree. Once the tree's diameter is determined, the endpoints are the two nodes that form this longest path. However, there can be multiple such pairs. For example, in a star-shaped tree where three leaves are at the same maximum distance from the center, but then the diameter is 2, but there are three possible pairs (each pair of leaves). But in this case, the diameter is 2. Each leaf is part of a pair that forms the diameter. So the count would be the number of nodes that are part of any such pair.

Wait, the problem says: for each level, after adding the node, compute the number of classes such that there exists some other class y where the distance between the class and y is exactly x (the maximum x). So each such class is an endpoint of a path that is a maximum-length path (diameter). So we need to count all nodes that are endpoints of any such maximum-length path.

So the count is the number of nodes that are either u, v, or any other node that is part of a pair with another node such that their distance is equal to the current diameter.

For example, in a tree where the diameter is D, and there are multiple pairs of nodes at distance D. The count is the sum of all nodes that are in any such pair.

So how to track this?

Let's think. The maximum distance x is the diameter. The nodes that contribute to the count are all nodes that are part of any pair with distance x.

So, for each node, we need to check if there exists another node such that their distance is x. If so, the node is counted.

The challenge is to efficiently compute how many such nodes there are after each addition.

But for each new node, how does the set of such nodes change?

Alternative approach: The nodes that are endpoints of the diameter can form a set. For example, if the diameter is D, then all endpoints are those nodes which are at maximum distance from one of the endpoints. For example, the endpoints are u and v (the current endpoints of the diameter). Then, any node that is at distance D from u (which would mean it's on the path from u to v, but that's impossible if u and v are the endpoints of the diameter). Wait, perhaps not. So the nodes that are in the set are those that are at one end of a maximum-length path.

But perhaps the key observation is that all maximum-length paths in a tree must pass through the middle of the diameter. So, the nodes that are endpoints of the diameter are the ones that are furthest apart, and any node that is at a maximum distance from one of the endpoints is part of a maximum-length pair.

Wait, here's an alternative way: For any node, the maximum possible distance from it is either to u or to v (the endpoints of the diameter). Because u and v are the two nodes that form the maximum path, and any other node's maximum distance is either to u or to v, whichever is further. So the diameter is the distance between u and v. Then, for any node, the maximum distance from it is max(distance(node, u), distance(node, v)). If this maximum is equal to the diameter, then the node is one of the endpoints of a maximum-length path.

But wait, the diameter is the maximum possible distance between any two nodes. So if the distance between u and v is D, then any node that has a maximum distance to either u or v of D must lie on the path from u to v. Because if there exists a node w such that the distance from w to u is D, then the path w-u is of length D, which would make the diameter D. But since the diameter is already D (distance between u and v), then this implies that w is along the path from u to v. Similarly for distance to v.

Alternatively, perhaps the maximum distance from any node is either to u or to v. Because u and v are the endpoints of the diameter. Then, for any node, the maximum possible distance from it is either distance(u, node) or distance(v, node), whichever is larger. But the maximum of these two would be at least (distance(u, v) + 1)/2, but I'm not sure.

Wait, here's a theorem: For any tree, the diameter is D. Then, for any node x, the maximum distance from x to any other node is either the distance from x to u or the distance from x to v, where u and v are the endpoints of the diameter.

Is this true? Let's see. Suppose we have a tree with diameter u-v. Let x be some node. Let a and b be two nodes such that a and b are the farthest from x. Then, the path a-x-b must be the longest path from x. But since the diameter is u-v, which is longer than any other path. So the maximum distance from x is either to u or to v. Because if there was a node farther from x than both u and v, then x and that node would form a longer path than u and v, contradicting the fact that u and v are the diameter.

Yes! So for any node x in the tree, the maximum possible distance from x is equal to the maximum of distance(x, u) and distance(x, v). And since the diameter is distance(u, v), which is the maximum possible, then the maximum distance from x cannot exceed the diameter. So for a node to be part of a maximum-length path, the maximum of distance(x, u) and distance(x, v) must equal the diameter. But wait, if the maximum is D (the diameter), then x is either u or v, since distance(u, v) is D. So in this case, the maximum distance from u is D (distance to v), and the maximum from v is D (distance to u). For any other node x, the maximum of distance(x, u) and distance(x, v) would be less than D. Because if x is not on the u-v path, then the path from x to u and x to v would have their LCA somewhere along u's path, leading to a longer path between u and v. Wait, perhaps I need to think of it in terms of the furthest nodes.

Wait, the theorem says that for any node x, the furthest node from x is either u or v. So the maximum distance from x is the maximum of the distance to u and distance to v. So if the maximum is equal to the diameter, then x must be either u or v. Because the diameter is the maximum distance between any two nodes. For example, if x is some node not on the u-v path, then the maximum distance from x is to one of the ends (u or v), but that distance would be less than D. Because the path from x to u would go through some node on the u-v path, and the same for v. So, the maximum distance from x is the maximum of distance(x, u) and distance(x, v), which would be (distance(x, a) + distance(a, u)) where a is the LCA of x and u. But since u and v are the endpoints of the diameter, the distance from a to u would be part of the diameter. So perhaps the maximum of distance(x, u) and distance(x, v) can't be larger than D. So the only way for the maximum to be D is if x is u or v, because then the other is at distance D. So, for any x not in {u, v}, the maximum distance from x is less than D. Therefore, the number of nodes that have a maximum distance of D is exactly 2 (u and v). But wait, this contradicts the sample input.

Looking at the first sample input:

4
1
1
2
1

The output after the fourth level is 3. Let's see. The tree after each step:

Level 1 (after adding node 2 as child of 1):

Tree is 1-2. Diameter is 1. The nodes 1 and 2. Output is 2.

Level 2 (add node 3 as child of 1):

Tree is 1 connected to 2 and 3. The diameter is 2 (between 2 and 3, path 2-1-3). So the count is 2 (nodes 2 and 3). Output is 2.

Level 3 (add node 4 as child of 2):

Tree is 1-2-4, and 3. The diameter is 3 (between 3 and 4: 3-1-2-4). So the count is 2 (3 and 4).

Level 4 (add node 5 as child of 1):

Tree is 1 connected to 2,3,5. 2 connected to 4. The diameter is 3 (e.g., 4-2-1-3 (distance 3?), or 4-2-1-5 (distance 3?), etc.). So the maximum distance is 3. The nodes that are endpoints of such paths are 4, 3, 5. So the count is 3. Which matches the sample output.

So according to the theorem I thought of earlier, the count would be 2 (u and v), but in this case, after adding node 5, the count is 3. So my previous reasoning is incorrect.

Hmm. So the theorem must be wrong. Let's see. In this case, after adding node 5, the diameter is 3. The nodes 4,3,5 are the ones that are part of pairs with maximum distance. For example:

4 to 3: distance 3 (4-2-1-3)

4 to 5: 3 (4-2-1-5)

3 to 5: 2 (3-1-5)

So the maximum is 3, and the pairs are (4,3), (4,5), (3,5). Wait no, 3 and 5's distance is 2. So the maximum is 3. So the nodes that are part of some pair with maximum distance are 4 (paired with 3 or 5), 3 (paired with 4), 5 (paired with 4). So the count is 3.

But according to the theorem, the maximum distance from each node would be max(distance(u, node), distance(v, node)), where u and v are the endpoints of the diameter. But in this case, after adding node 5, the diameter is 3, and the endpoints are 4 and 3 (distance 3). So for node 5:

distance(5, 4) is 3 (5-1-2-4) → yes.

distance(5,3) is 2 (5-1-3).

So the maximum for node 5 is 3. So according to the theorem, if the diameter is 3, then node 5's maximum distance is 3, which equals the diameter. But according to the previous reasoning, this shouldn't happen. So why is this?

Ah, perhaps the theorem is not correct. Because in this case, u is 3, v is 4 (distance 3). The maximum distance from 5 is max(distance(5,3), distance(5,4)) = max(2, 3) → 3, which equals the diameter. So according to the theorem, node 5 would be counted. But according to the sample output, it is. So the theorem must be correct. So the count is the number of nodes where max(distance(u, node), distance(v, node)) equals the diameter. 

So in this case, after adding node 5:

distance(3,4) is 3 → diameter is 3. The endpoints are u=3, v=4.

Now, for each node:

- node 1: max distance is max(d(3,1)=2, d(4,1)=3) → 3. So 3 equals diameter → counted.

Wait, but the problem requires that the node has some other node at exactly x (the maximum x). So if node 1's maximum distance is 3 (distance to 4), then node 1 is part of a pair (4,1) with distance 3. But 4 is in the pair, and 1's distance to 4 is 3. So in this case, node 1 would be counted. But according to the sample output, after the fourth level, the count is 3 (nodes 3,4,5). So what's going on here?

Hmm, perhaps my understanding of the problem is wrong. Let me re-read the problem statement.

The problem says: the maximum cost x is the maximum distance between any two classes. Then, for each level, output the number of classes such that for each of these classes, there exists some other class y where the distance from this class to y is exactly x.

So the nodes that are counted are all nodes a where there exists some node b such that distance(a, b) = x (x is the maximum).

So in the sample after level 4 (current nodes are 1,2,3,4,5):

x is 3 (the maximum distance). The nodes that have at least one node at distance 3 are:

3 (distance to 4 is 3)

4 (distance to 3 is 3, distance to 5 is 3)

5 (distance to 4 is 3)

So three nodes. The output is 3. So node 1's maximum distance is 3 (distance to 4 is 3?), but 1's distance to 4 is 3? Let's compute:

Tree structure after fourth level:

1 is parent of 2,3,5.

2 is parent of 4.

So path from 1 to 4 is 1-2-4 (length 2). So distance between 1 and 4 is 2. So node 1's maximum distance is max(distance(1,3) [1], distance(1,4) [2] → max is 2. So no, node 1's maximum is 2, which is less than x=3. So why in the sample, node 5 is included?

Ah, node 5's distance to 4 is 3 (5-1-2-4). So yes, node 5 has a node (4) at distance 3. So it's counted.

So how do we compute for each node a, whether there exists a node b such that distance(a,b) = x (current maximum).

Thus, the problem is to compute for each step the number of nodes that are part of at least one pair (a,b) where distance(a,b) is equal to the current maximum x.

So the approach must track, for each node, whether there's a node that is at x distance from it, where x is the current maximum.

But how to compute this efficiently.

Alternative approach:

The maximum x is the diameter of the tree. So, the nodes that are in the set S are those that are endpoints of some diameter. So, if the diameter is D, then any node that is part of a pair (u, v) where distance(u, v) = D is in S.

Thus, the count is the number of nodes that are in the union of all such pairs (u, v) that form a diameter.

So the problem reduces to, for each step, find all nodes that are in any pair that achieves the current diameter, and count them.

The challenge is to track this as the tree grows.

The key insight here is that when the diameter increases by adding a new node, the possible new pairs are between the new node and one of the previous endpoints. So, the current diameter endpoints are tracked, and when a new node is added, we check if it can form a longer path with either of the existing endpoints.

So the steps would be:

- Initially, the tree has node 1. The diameter is 0 (only one node), count is 1.

- For each new node (i+1), added as a child to yi:

   - Compute the distance from the new node to each of the current diameter endpoints (u and v).

   - The maximum possible new diameter is max(old_diam, d(new, u), d(new, v)).

   - If the new diameter is larger than the old, then the new endpoints are the pair (new, u) if d(new, u) is the largest, or (new, v) if d(new, v) is the largest.

   - If the new diameter is equal to the old, then perhaps the new node can form a pair with another node not part of the existing endpoints, but this is complicated.

Wait, but according to previous analysis, the new node can only form a longer path if it's further away from either u or v than the current diameter. Otherwise, the current diameter remains.

But the problem is when adding a new node, the new diameter can be determined by considering the distances from the new node to u and v.

So the algorithm for maintaining the diameter is:

Keep track of current endpoints u and v, and the current diameter D.

When adding a new node w:

   compute distance from w to u (d1) and to v (d2).

   candidate = max(d1, d2).

   if candidate > D:

       new_D = candidate

       new_u = w

       new_v = u if d1 > d2 else v

   else:

       new_D = D

       new_u = u

       new_v = v

But what if candidate is equal to D? Then, the diameter may not change, but there could be other nodes that also form pairs with distance D. However, in this case, the existing endpoints remain.

But how does this affect the count of nodes that are part of any such pair?

For example, in the first sample after adding node 5 (fourth step):

Current diameter is 3 (distance between 3 and 4 is 3). Adding node 5 as child of 1.

The new node is 5, whose parent is 1. So the depth of 5 is 2 (depth of 1 is 0? Or perhaps depth starts at 1. Wait, in the first step, when node 2 is added as child of 1 (depth 1), then node 3 is added as child of 1 (depth 1), node 4 as child of 2 (depth 2), node 5 as child of 1 (depth 1). So the distance between 5 and 3 is 2 (path 5-1-3), and between 5 and 4 is 3 (5-1-2-4).

So d1 (distance between new node 5 and u=3) is 2, d2 (distance between new node 5 and v=4) is 3. So candidate is 3, which equals D (current D is 3). So the diameter doesn't change. The endpoints remain u=3 and v=4. But the new node 5 is part of a pair (5,4) with distance 3. So the count increases by 1 (since 5 is now part of a pair with maximum distance).

So the count is 3 (3,4,5).

But according to the previous algorithm, the endpoints remain u and v, but the new node may form a pair with one of them. So, the count is the number of nodes that are in the set {u, v, any new nodes that can form a pair with either u or v with distance D}.

Wait, but in this case, the existing endpoints are u=3 and v=4. The new node 5 has a distance of 3 to v=4. So 5 is added to the count.

So the count is the number of nodes that are in the current endpoints set plus any new nodes that can form a pair with the current endpoints.

But how do we track this?

Alternative approach:

Each time a new node is added, we check if the new node can form a pair with u or v that has distance D (the current diameter). If so, then the new node is added to the count.

But wait, in the sample, after adding node 5:

The current diameter is D=3 (existing u=3, v=4).

The new node 5's distance to u is 2 (5-1-3), to v is 3 (5-1-2-4). So the new node forms a pair with v at distance 3. So the new node is added to the count.

Thus, the count becomes the existing count (2, for u and v) plus 1 (the new node) → 3.

But how to track this?

But how do we know whether the new node's maximum distance to the current endpoints is equal to D?

In the algorithm for maintaining the diameter, after adding a new node, the candidate is compared to D. If candidate is greater than D, then the diameter increases. The new count would be 2 (the new endpoints). If candidate equals D, then the new node is part of the count (if distance to either u or v is D). Also, existing nodes may now have a new pair with the new node.

But this complicates things.

Alternatively, after each step, the maximum distance x is the current diameter. We need to find all nodes a where there exists some node b such that distance(a,b) = x.

This is equivalent to finding all nodes that are endpoints of any diameter path.

The question is: how to track these nodes efficiently.

But how?

Another idea: whenever the diameter increases, the new count is 2 (the new pair of endpoints). If the diameter remains the same, but a new node can form a pair with one of the existing endpoints, then the count increases by 1. Or if existing nodes can form new pairs with the new node.

But this approach may not capture all possibilities.

Alternatively, the set of nodes that are endpoints of the diameter is either:

- The two endpoints u and v (if the diameter is D), or

- A larger set when there are multiple pairs of nodes at distance D.

But how to track this?

Let me think of the example where the tree is a star: center node 1, and nodes 2,3,4 connected to it. The diameter is 2 (between any two leaves). So the count is 3 (nodes 2,3,4), since each pair of leaves has distance 2.

So in this case, the algorithm would have to track all leaves. But when adding each new leaf, the diameter may stay the same. 

In this scenario:

- After adding node 2 (child of 1), diameter is 1 (between 1 and 2). Count is 2.

- Add node 3 (child of 1): diameter becomes 2 (between 2 and 3). Count is 2.

- Add node 4 (child of 1): diameter remains 2. But now, nodes 2,3,4 can form pairs with each other (distance 2). So count becomes 3.

Thus, each new node added to the star increases the count by 1, as long as the diameter remains the same.

So the algorithm must account for this. This suggests that the count can be more than 2 even when the diameter doesn't increase.

Thus, the previous approach of tracking u and v is insufficient. Because when the diameter is the same, but there are multiple pairs of nodes that form the diameter, the count can be more than 2.

So how to track this?

Alternative approach: The set of nodes that are part of any pair with distance equal to the current diameter.

Each time a new node is added, we need to determine if it can form a pair with any existing node (not just u and v) with distance equal to the current diameter. Additionally, existing nodes might form new pairs with each other due to the addition of the new node (but that's unlikely, since the new node is a leaf).

But given the time constraints, this approach is not feasible for m up to 3e5.

Thus, we need a way to track the count efficiently.

Alternative Idea:

The maximum diameter is D. All nodes that are at a distance D from either u or v are part of the count.

Because, as per the earlier theorem, the maximum distance from any node x is max(distance(x, u), distance(x, v)), and if this maximum is D, then x is part of a pair with distance D.

So the count is the number of nodes x where max(distance(x, u), distance(x, v)) == D.

This would include u and v (since distance(u, v) is D), and any other node that is at distance D from either u or v.

So, for example, in the star example with nodes 2,3,4 connected to 1:

u is 2, v is 3. D is 2.

distance(4, u) is 2 (4-1-2), distance(4, v) is 2 (4-1-3). So max is 2 = D → node 4 is counted.

Thus, the count is 3 (nodes 2,3,4).

So according to this approach, the count is the number of nodes where the maximum of their distances to u and v equals D.

Thus, the steps would be:

- Track u and v as the endpoints of the current diameter.

- For each new node w, compute distances to u and v. The candidate diameter is the maximum of the current D, and these two distances.

- If the candidate is greater than D, then update u and v to be the new endpoints (w and whichever of u or v gave the larger distance). The new D is candidate.

- The count is the number of nodes where max(distance to u, distance to v) == D.

Thus, the problem reduces to, after each addition, compute the new u and v (if needed), and then count the number of nodes that have their maximum distance to u or v equal to D.

This approach would work for the sample cases.

So how to implement this?

For each node, we need to store its depth and parent information. Then, for each query, when a new node is added, we can compute its depth (depth[new_node] = depth[parent] + 1).

To compute the distance between a new node and u or v, we can use the LCA approach. But for that, we need to build a binary lifting table for each node.

So, for each node, we store its depth and ancestors at 2^k levels. This allows us to compute the LCA of two nodes in O(log m) time.

Once we have the LCA, the distance between two nodes a and b is depth[a] + depth[b] - 2 * depth[lca(a, b)].

Thus, the steps for each new node are:

1. Add the new node to the tree, setting its parent and depth.

2. Build the binary lifting table for the new node.

3. Compute the distances from the new node to u and v (current endpoints of the diameter).

4. Determine the new diameter (max between current diameter and these two distances).

5. Update u and v if the new diameter is larger.

6. For all nodes, compute max(distance to u, distance to v) and check if it equals the new diameter. However, this is not feasible for large m.

Wait, but this is O(m) per step, which is not feasible for m up to 3e5.

Thus, we need a way to track the count without iterating through all nodes each time.

Alternative Idea:

The count can be maintained as the number of nodes at distance D from u plus the number of nodes at distance D from v, minus the nodes that are at distance D from both u and v.

But since the diameter is D, distance(u, v) = D. So the nodes that are at distance D from u are precisely v, and the nodes that are at distance D from v are precisely u. But this is not correct. For example, in a chain of 4 nodes: 1-2-3-4. The diameter is 3 (distance between 1 and 4). Then, nodes at distance 3 from 1 are 4, and nodes at distance 3 from 4 are 1. So count is 2.

But according to the formula, count would be 1 + 1 - 0 = 2.

Another example: the star with nodes 2,3,4 connected to 1. u=2, v=3, D=2. The nodes at distance 2 from u (2) are 3,4. The nodes at distance 2 from v (3) are 2,4. The intersection is {4}. So count is 2 (nodes 3 and 2) from u's side plus 2 (nodes 2 and 4) from v's side minus 1 (node 2). Wait, no, the count would be (number of nodes at distance D from u) + (number at D from v) - (number at D from both). So for the star example:

At distance 2 from u=2: 3 and 4. So 2 nodes.

At distance 2 from v=3: 2 and 4. So 2 nodes.

Intersection: nodes that are at distance 2 from both: 4 (distance 2 from u: 2-1-4 is 2 steps. From v: 3-1-4 is 2 steps).

So count is 2 + 2 - 1 = 3. Which matches the sample.

Thus, the formula holds.

So, the count can be computed as:

count = cnt_u + cnt_v - cnt_both

where:

cnt_u is the number of nodes at distance D from u.

cnt_v is the number of nodes at distance D from v.

cnt_both is the number of nodes at distance D from both u and v.

Thus, the problem reduces to tracking these three values.

But how to compute these efficiently.

Each time a new node is added, we can compute its distance to u and v.

If the new node's distance to u is D, increment cnt_u.

If its distance to v is D, increment cnt_v.

If both are D, increment cnt_both.

But D can change when the diameter is updated. So we need to manage these counts as the diameter changes.

But this seems tricky. Because when the diameter changes, all nodes' distances to the new u and v need to be recomputed, which is O(m) per step.

Thus, this approach is not feasible.

Alternative Idea:

The count is equal to the sum of nodes at distance D from u plus the sum of nodes at distance D from v minus twice the sum of nodes at distance D from both (since they are counted in both cnt_u and cnt_v). Wait, no. The correct formula is cnt_u + cnt_v - cnt_both, as each node counted in both is subtracted once.

So, for the new diameter D, we need to find the number of nodes x where max(dist(x, u), dist(x, v)) = D. This is equivalent to the set of nodes that have dist(x, u) = D or dist(x, v) = D. But since D is the distance between u and v, then the nodes that have dist(x, u) = D are those that are at a distance D from u, which must be along the path from u to v (since any other path would not be longer than D). Similarly for v.

But again, how to track this.

Alternative Idea:

We can track the following for each node x:

- dist(x, u): the distance from x to u.

- dist(x, v): the distance from x to v.

But storing these for each node is O(m) space, which is acceptable. But for m=3e5, it's manageable.

When a new node is added:

1. Compute its dist to u and dist to v.

2. If the new diameter is increased (based on the new node's max of dist to u or v), then update u and v to be the new endpoints.

3. For all existing nodes, recompute their dist to the new u and v.

But this is O(m) per step, which is O(m^2) total time. Not feasible.

Thus, this approach is not efficient.

Alternative Idea:

When the diameter changes, the new u and v are the new endpoints. All previous nodes' distances to the new u and v need to be computed. But for each node, this distance can be computed as the depth of the node + depth of the new u minus twice the depth of their LCA. But computing this for each node every time the diameter changes is O(m) per change, which is O(m^2) time.

Thus, this is not feasible.

So, the only way to proceed is to find a way to compute the count based on the current u and v, and the new node's distance to them.

But how?

Let's consider the following:

Whenever a new node is added, we compute its distance to u and v. The new diameter is the maximum of the previous diameter and these two distances.

If the new diameter is larger than the previous, then the new endpoints are new_node and whichever of u or v gave the larger distance. The new count is 2 (the new endpoints).

If the new diameter is equal to the previous, then:

- If the new node's maximum distance to u or v is equal to the diameter, then the new node is added to the count. Also, any existing node that is at distance D from either u or v may also form a pair with the new node.

But this seems complex.

Alternatively, after adding the new node and possibly updating u and v, the count is the number of nodes x where max(dist(x, u), dist(x, v)) == D.

Thus, the problem reduces to maintaining u, v, and D, and for each new node, compute how many nodes (including the new one) satisfy the condition.

But how to compute this without iterating through all nodes.

The answer is that when a new node is added, the only node that can contribute to the count is the new node itself, because all existing nodes have already been checked against the previous u and v. However, when u and v change, all nodes' distances to the new u and v may change, requiring a complete recompute of the count. But that's not feasible.

Thus, the only way to proceed is to find that the count can be maintained based on the new node's distances and the current u and v.

But how?

Perhaps, when the diameter increases, the count becomes 2 (the new endpoints). When the diameter doesn't increase, but the new node's maximum distance to u and v is equal to D, then the count increases by 1. But this is not always correct.

In the sample where the new node forms a new pair with one of the existing endpoints, leading to the same diameter but an increased count.

But how to track this.

Let's think of the steps:

Initially, after adding node 5 (fourth level):

Previous u=3, v=4, D=3.

New node 5's distance to u is 2, to v is 3. So candidate is 3. Since D remains the same, but new node's max distance is 3 (equal to D), so the count increases by 1. So the count becomes 3.

So the count can be tracked as:

If the new node's max distance to u or v is equal to D, then increment the count by 1. Else, no change.

But what about existing nodes that may now form pairs with the new node?

For example, suppose after adding a new node w, the new node's distance to u is D, and there's another existing node x whose distance to w is D.

But in this case, x's max distance to u or v is already considered. If x's max is D, then x is already counted. The pair (x, w) may also be a pair with distance D, but since x is already counted, adding w doesn't change x's status. But the problem statement requires counting all nodes that have at least one pair with distance D.

So if x is already in the count (because it has a pair with u or v), then adding w gives x another pair, but x is already counted. So the count for x is already included.

Thus, the only new node that may contribute to the count is the new node w, if its max distance to u or v is D.

Thus, the count can be maintained as follows:

- When the diameter increases:

   - The new count is 2 (new endpoints u and v).

- When the diameter remains the same:

   - If the new node's max distance to the current u or v is equal to D, then the count increases by 1.

But this may not capture cases where existing nodes can form new pairs with the new node. For example, if the new node has a distance to an existing node (not u or v) equal to D.

But according to the theorem, the max distance from any existing node is already considered (max distance to u or v). Thus, if the existing node x has a max distance of D (already counted), then adding a new node w that is at distance D to x would not change x's status (since x is already counted). But w's max distance to u or v may be D, in which case w is added to the count.

Thus, the only way to capture all nodes that are part of at least one pair with distance D is to count all nodes whose max distance to u or v is D.

Thus, the count is equal to the number of nodes x where max(dist(x, u), dist(x, v)) == D.

Thus, the solution is:

For each new node:

1. Compute dist to current u and v.

2. Check if the new diameter is larger than the current.

3. If yes:

   a. Update u and v to the new endpoints.

   b. The new count is 2 (the new endpoints).

4. If no:

   a. Compute the new node's max distance to u and v.

   b. If this max distance equals D, then increment the count by 1.

   c. Otherwise, the count remains the same.

But wait, this approach would fail in cases where existing nodes can form new pairs with the new node. For example:

Consider a tree where the existing diameter is between u and v (distance D). A new node w is added such that its distance to u is D and to v is less than D. So the new node is added to the count. Now, existing nodes that are at distance D from u would have their max distance as D, and are already counted. But suppose there's a node x at distance D from u. Then x is already counted. Adding w, which is at distance D from u, would create a pair (x, w) with distance D. But x is already counted, and w is now counted. So the count increases by 1, which is correct.

Thus, the approach is correct.

Another example:

After adding node 5 (sample input 1), the new node's distance to v (4) is 3 (D=3). So the count increments by 1, leading to 3.

Thus, the algorithm works.

But what about when the new node's max distance to u or v is D, but there are existing nodes that have their max distance to u or v also equal to D. For example, the star case.

Let's see:

Initially, after adding nodes 2 and 3:

u=2, v=3, D=2.

Count is 2.

Then adding node 4 as child of 1.

Distance to u=2 is 2 (4-1-2), distance to v=3 is 2 (4-1-3). So max is 2 = D. So count increases by 1 to 3.

Which is correct.

Thus, the algorithm works.

Thus, the steps are:

- Maintain u, v as the current endpoints of the diameter D.

- Maintain the count as the number of nodes where max(dist to u, dist to v) == D.

- When a new node is added:

   a. Compute dist_to_u = distance between new node and u.

   b. Compute dist_to_v = distance between new node and v.

   c. candidate = max(dist_to_u, dist_to_v)

   d. if candidate > D:

      i. D = candidate

      ii. if dist_to_u > dist_to_v:

           new_u = new_node

           new_v = u

         else:

           new_u = new_node

           new_v = v

      iii. Now, compute the new count as the number of nodes where max(dist to new_u, dist to new_v) == D.

           But this requires re-evaluating all nodes, which is O(m) per step. Not feasible.

   e. else:

      i. if candidate == D:

           count +=1

      ii. else:

           count remains.

      iii. Also, check if there are existing nodes that now have max distance to u or v == D.

           But this is not feasible.

Wait, this brings us back to the original problem. When the diameter increases, we need to re-evaluate all nodes to compute the new count, which is O(m) per step, leading to O(m^2) time. But this is not feasible for m=3e5.

Thus, we need a way to track the count for the new u and v without recomputing from scratch.

But how?

Alternative Idea:

When the diameter changes, the new u and v are the new endpoints. The count is the number of nodes where the maximum of their distance to new u and new v is equal to the new D.

But how to compute this.

In this case, the new D is the distance between new u and new v. Let's say new u is w (the new node), and new v is the previous u. The distance between them is candidate.

So for all nodes, we need to compute the maximum of their distance to new u (w) and new v (previous u).

But this is again O(m) per step.

Thus, it's impossible to compute this for large m.

Therefore, the only way to proceed is to find that whenever the diameter increases, the count is 2 (the new endpoints). And when the diameter does not increase, the count is incremented by 1 if the new node's max distance to u and v equals D.

But this may not be correct. Let's see:

Case where the diameter increases, but the new endpoints have more than 2 nodes in the count.

For example, consider a chain:

1-2-3-4. Diameter is 3 (1-4). Count is 2.

Now add node 5 as child of 4. Diameter becomes 4 (1-5). Count is 2.

Thus, when diameter increases, count becomes 2.

Another example:

After adding nodes 2,3,4 as children of 1. Diameter is 2 (between any two children). Count is 3. But if we add a new node 5 as child of 2, the distance from 5 to 3 is 3 (5-2-1-3). So the diameter increases to 3. The new endpoints are 5 and 3. Count becomes 2.

But previously, the count was 3. So when the diameter increases, the count is reset to 2.

Thus, the algorithm is:

- When the diameter increases, the count is 2.

- When the diameter remains the same, the count increases by 1 if the new node's max distance to u and v is equal to D.

Thus, the code can be written as follows:

Initialize:

- u = 1

- v = 1

- D = 0

- count = 1 (since there's only one node)

For each new node (i from 2 to m+1):

   parent = yi (the input for the i-th query)

   add node i as child of parent.

   compute dist_u = distance(i, u)

   compute dist_v = distance(i, v)

   candidate = max(dist_u, dist_v)

   if candidate > D:

       new_D = candidate

       if dist_u > dist_v:

           new_u = i

           new_v = u

       else:

           new_u = i

           new_v = v

       D = new_D

       u, v = new_u, new_v

       count = 2  # because new_u and new_v are the only nodes in the new diameter

   else:

       if candidate == D:

           count +=1

       # else: count remains

   output count

But wait, this assumes that when the diameter increases, only the new endpoints contribute to the count. But this is not correct in cases where the new endpoints are part of a larger set.

But according to previous examples, when the diameter increases, the new count is 2.

Thus, the algorithm would work for the first sample:

Sample 1:

After adding node 5:

The previous u=3, v=4, D=3.

The new node's distance to u is 2, to v is 3. Candidate is 3, which equals D. So count increases by 1 (now 3).

Which matches the sample.

Another example: star tree after adding node 4.

Initially, after adding node 3: u=2, v=3, D=2. count=2.

Add node4 as child of 1:

dist_u = distance(4, 2) = 2.

dist_v = distance(4, 3) = 2.

candidate is 2, which equals D. So count +=1 → 3.

Which is correct.

But when the diameter increases, the count is set to 2.

Thus, the algorithm seems to work.

But what about when the new node is added, the diameter doesn't increase, but there are existing nodes that now have max distance to u and v equal to D?

For example, suppose we have a tree where u and v are the current endpoints, and D=3. Then a new node is added such that its distance to u is 2, to v is 3. Thus, the new node is counted. But there's an existing node x with distance to u=3 and to v=1. So x was not counted before, but when the new node is added, the max distance from x is max(3,1) =3. Thus, x should be counted. But according to the algorithm, x was added before the new node. Thus, when x was added, if the diameter was 3 at that time, then x would have been counted. Otherwise, not.

But this scenario is impossible. Because when x was added, the diameter could have been 3. So x's max distance to u and v would have been 3, so x would have been counted.

Thus, the algorithm correctly captures all nodes that meet the condition.

Thus, the approach is:

- Maintain u and v as the current endpoints of the diameter.

- Maintain D as the current diameter.

- Maintain count as the number of nodes that have max(dist to u, dist to v) == D.

- For each new node:

   - Compute its distance to u and v.

   - candidate = max of these two distances.

   - if candidate > D:

       - update u and v to the new endpoints (new_node and whichever of u or v gave the candidate).

       - set D to candidate.

       - set count to 2.

   - else if candidate == D:

       - increment count by 1.

   - else:

       - no change to count.

   - output count.

But why is this correct?

Because when the diameter increases, the new diameter is formed by the new node and one of the old endpoints. The new count is 2 (the two new endpoints).

When the diameter remains the same, the new node may form a pair with either u or v (but not both), and thus, its max distance to u or v is D. So we increment the count by 1.

Existing nodes that have their max distance to u or v equal to D are already counted. They may form pairs with other nodes (including the new node) but they are already in the count. The new node is the only new candidate to add to the count.

Thus, this approach works.

Thus, the code can be written as follows:

Implement a binary lifting structure to compute LCA and distances.

For each node, track its depth and parents at various levels.

When a new node is added, build its binary lifting table.

Compute distances to the current u and v.

Update u, v, D, and count accordingly.

Thus, the key is to compute the distance between any two nodes quickly.

Now, let's proceed to implement this.

Steps:

1. Read m.

2. Initialize the tree structure.

3. For each node from 2 to m+1:

   a. Read yi (the parent of the new node).

   b. Add the new node to the tree.

   c. Compute its depth.

   d. Build the binary lifting table for the new node.

4. Maintain u, v, D, count.

5. For each new node, compute distance to u and v.

6. Update u, v, D, count as per the algorithm.

7. Output count after each step.

Implementing the binary lifting for LCA:

Each node will have a list of ancestors. ancestors[k][n] represents the 2^k-th ancestor of node n.

For each new node, we set its first ancestor (k=0) as its parent. Then, for higher k, we use the ancestors of the parent.

The depth of each node is stored.

The binary lifting table is built for each node up to log2(m) levels.

To compute the LCA of two nodes a and b:

- Bring the deeper node up to the same depth as the other.

- Then, simultaneously move both up until they meet.

The distance between a and b is depth[a] + depth[b] - 2 * depth[lca(a, b)].

Thus, the code will need to implement the LCA function and the distance function.

Now, let's code this.

But for m up to 3e5, the binary lifting table needs to have log2(3e5) levels (about 19). So each node will store up to 20 ancestors (2^0 to 2^19).

The code can proceed as follows:

- Precompute log2(m) or use a fixed maximum level (say 20).

Implementing binary lifting for each new node:

When adding a new node i:

- Set its parent as yi.

- ancestors[0][i] = yi.

- For k in 1 to 19:

   ancestors[k][i] = ancestors[k-1][ancestors[k-1][i]]

But how to store the ancestors. Using a list of lists, where ancestors[k][i] is the 2^k-th ancestor of i.

But in Python, it's more efficient to use a list of lists, with ancestors being a list where each element is a list of ancestors for each node.

But for m up to 3e5+1 nodes, and 20 levels, this is 3e5 * 20 = 6e6 entries, which is manageable.

Thus, the code can proceed as:

Initialize:

max_level = 20

ancestors = [[] for _ in range(max_level)]

depth = [0]*(m+2)

ancestors[0] = [0]*(m+2)  # parent of node 1 is 0 initially? Or 0-based?

Wait, nodes are numbered from 1 to m+1.

For node 1, depth is 0 (or 1? Need to check).

Let's see:

Initially, node 1 has depth 0.

When node 2 is added as child of 1, depth of node 2 is 1.

Yes.

So for node i, depth[i] = depth[parent] + 1.

Thus, the code for adding a new node i:

parent = yi

depth[i] = depth[parent] + 1

ancestors[0][i] = parent

for k in 1 to max_level-1:

   ancestors[k][i] = ancestors[k-1][ancestors[k-1][i]]

Thus, for each new node, we precompute its ancestors up to 2^20 steps.

Now, the LCA function:

def lca(a, b):

   if depth[a] < depth[b]:

       a, b = b, a

   # Bring a up to depth of b

   for k in range(max_level-1, -1, -1):

       if depth[a] - (1 << k) >= depth[b]:

           a = ancestors[k][a]

   if a == b:

       return a

   for k in range(max_level-1, -1, -1):

       if ancestors[k][a] != ancestors[k][b]:

           a = ancestors[k][a]

           b = ancestors[k][b]

   return ancestors[0][a]

Then, the distance between a and b is depth[a] + depth[b] - 2 * depth[lca(a, b)].

Thus, the code can proceed.

Now, let's handle the initial state:

Initially, the tree has node 1.

depth[1] = 0.

ancestors[0][1] = 0 (since it has no parent). But when node 1's parent is 0, which is not part of the tree. So for nodes higher up, their ancestors would be 0.

But this is handled in the LCA function.

Thus, the code for node 1:

ancestors[0][1] = 0

depth[1] = 0

Then, for each new node i starting from 2 up to m+1:

Read yi (the parent is yi).

Set parent = yi.

depth[i] = depth[parent] + 1.

ancestors[0][i] = parent.

For k in 1 to max_level-1:

   ancestors[k][i] = ancestors[k-1][ancestors[k-1][i]]

Now, the variables u, v, D, count:

Initially, after node 1 is added (level 0?), but according to the problem statement, the initial tree has node 1. So the first query (level 1) adds node 2. So the initial state before any queries is node 1. The first output is after adding node 2.

Thus, the initial state for u, v, D, count is:

u = 1

v = 1

D = 0 (distance between 1 and 1 is 0)

count = 1 (only node 1 exists)

But for the first query, after adding node 2:

- Compute distance to u (1) and v (1). Both are 1.

candidate = 1 > D (0). So D becomes 1.

new_u = 2, new_v = 1.

count = 2.

Output is 2.

Which matches the first sample.

Thus, the code must initialize u and v to 1, D to 0, count to 1.

Then, for each new node i from 2 to m+1:

process as per the algorithm.

Thus, the code should look like this.

Now, the final code:

Read m.

Initialize max_level to 20.

precompute the ancestors and depth.

But in Python, since m can be up to 3e5, and nodes are up to m+1, we can preallocate lists.

But dynamic allocation is possible.

Thus, the code:

import sys
from sys import stdin
import math

def main():
    sys.setrecursionlimit(1 << 25)
    m = int(stdin.readline())
    max_level = 20
    max_node = m + 1
    depth = [0] * (max_node + 1)
    ancestors = [[0] * (max_node + 1) for _ in range(max_level)]
    
    # Initialize node 1
    depth[1] = 0
    for k in range(max_level):
        ancestors[k][1] = 0  # No parent
    
    u = 1
    v = 1
    D = 0
    count = 1
    print(1)  # The initial state after node 1 is added. But according to the problem statement, the first query corresponds to level 1. Wait, wait.

    # Wait, the problem says: i-th line (1 ≤ i ≤ m) describes the i-th level and contains yi — the parent of class i+1. Initially, there's class 1. Then, for each level i from 1 to m, we add node i+1. So the number of nodes after m levels is m+1.

    # The output should be m lines, each corresponding to the state after each level. But according to the first sample input:

    # input:
    #4
    #1
    #1
    #2
    #1

    # The output has 4 lines.

    # So after the first level (adding node 2), the output is 2.

    # So the initial state is after 0 levels (only node 1). The first output line is after level 1 (node 2 is added). So the code should process m levels, each adding a node, and output m lines.

    # So the initial u, v, D, count are for node 1.

    # But after processing each query, we need to output the count after adding the new node.

    # So for m queries, we have m outputs.

    # So the code should not print anything for the initial state. It processes m queries, each adding a node, and outputs m lines.

    # Thus, the initial state is:

    u = 1
    v = 1
    D = 0
    count = 1

    # Then, for each of the m queries:

    for i in range(1, m+1):
        yi = int(stdin.readline())
        current_node = i+1
        parent = yi
        depth[current_node] = depth[parent] + 1
        ancestors[0][current_node] = parent
        for k in range(1, max_level):
            ancestors[k][current_node] = ancestors[k-1][ancestors[k-1][current_node]]
        
        # Compute distance to u and v
        def get_dist(a, b):
            if a == b:
                return 0
            # Find LCA
            orig_a, orig_b = a, b
            if depth[a] < depth[b]:
                a, b = b, a
            # Bring a up to depth of b
            for k in range(max_level-1, -1, -1):
                if depth[a] - (1 << k) >= depth[b]:
                    a = ancestors[k][a]
            if a == b:
                return depth[orig_a] + depth[orig_b] - 2 * depth[a]
            for k in range(max_level-1, -1, -1):
                if ancestors[k][a] != ancestors[k][b]:
                    a = ancestors[k][a]
                    b = ancestors[k][b]
            lca_node = ancestors[0][a]
            return depth[orig_a] + depth[orig_b] - 2 * depth[lca_node]
        
        dist_u = get_dist(current_node, u)
        dist_v = get_dist(current_node, v)
        candidate = max(dist_u, dist_v)
        
        if candidate > D:
            D = candidate
            if dist_u > dist_v:
                new_u = current_node
                new_v = u
            else:
                new_u = current_node
                new_v = v
            u, v = new_u, new_v
            count = 2
        elif candidate == D:
            count += 1
        else:
            pass  # count remains
        
        print(count)

But wait, in the initial state, after node 1 is added (before any queries), the output is nothing. Then, after processing the first query (adding node 2), the output is printed. The first sample input has four queries, and the first output line is 2.

In the code above, the loop runs for m queries. For each query, after adding the new node (current_node = i+1), the code computes the count and prints it.

Yes. So for the first sample input with m=4, the code will output four lines.

Now, the code for get_dist may be a bit slow for m=3e5. Let's optimize it.

But in Python, with m=3e5 and get_dist being O(log m) per call, this is O(m log m) time, which is acceptable.

But the code may need to be optimized for speed.

Alternative approach: Precompute the LCA and distance functions using binary lifting.

Another optimization is to compute the LCA in a more efficient way.

But for now, the code as written should work.

Testing the first sample:

Sample input:

4
1
1
2
1

Queries:

Level 1: add node 2 as child of 1.

dist_u = distance(2, u=1) is 1.

dist_v = distance(2, v=1) is 1.

candidate =1 > D=0.

D becomes 1.

u and v become 2 and 1.

count=2.

Output is 2.

Level 2: add node 3 as child of 1.

dist_u = distance(3, u=2) → LCA is 1.

distance: 2 (3-1-2).

dist_v = distance(3, v=1) → 1.

candidate is 2 > D=1.

D becomes 2.

u becomes 3, v becomes 2.

count=2.

Output 2.

Level 3: add node 4 as child of 2.

distance to u=3 is 3 (4-2-1-3).

distance to v=2 is 1 (4-2).

candidate is 3> D=2.

D becomes 3.

u becomes 4, v becomes 3.

count=2.

Output 2.

Level4: add node5 as child of 1.

distance to u=4:

path 5-1-2-4 → depth 5 is 1, depth 4 is 3.

LCA of 5 and 4 is 1.

distance is (1 +3) - 2*0 =4? Wait, depth of 5 is 1 (parent is 1, depth 0 +1 =1). Depth of 4 is 3 (1→2→4: 0+1=1 for 2, 1+1=2 for 4? Wait, no. Let's recheck.

When node 2 is added, parent is 1 (depth 0 → depth 1).

Node 4's parent is 2 (depth 1 → depth 2).

So depth of node 4 is 2.

Thus, when calculating distance between node 5 and 4:

depth of 5 is 1, depth of 4 is 2.

LCA is 1.

distance is 1 +2 - 2*0=3.

Thus, dist_u =3, dist_v= distance(5,3) is 2 (5-1-3).

candidate is 3 == D=3.

count +=1 → 3.

Output 3.

Which matches the sample.

Thus, the code works for the first sample.

The second sample:

Input:
4
1
1
2
3

Output:

2
2
2
2

Let's see:

After each step:

Level1: add node 2 as child of 1.

Same as before. u=2, v=1. D=1. count=2.

Output 2.

Level2: add node3 as child of 1.

distance to u=2: 2. candidate=2>1. D=2. u=3, v=2. count=2. Output 2.

Level3: add node4 as child of 2.

distance to u=3 is 3 (4-2-1-3). distance to v=2 is 1. candidate=3>2. D=3. u=4, v=3. count=2. Output2.

Level4: add node5 as child of 3.

distance to u=4: compute.

Path 5-3-2-1-4 → depth 5 is 3 (3's depth is 2, parent of 3 is 1, depth is 1, so 1+1=2, 3's depth is 2. So 5's depth is 3.

distance between 5 and 4:

LCA is 1.

depth 5 is 3, depth4 is 3. So 3+3-2*0=6. But that's not possible.

Wait, perhaps I made a mistake in the parent hierarchy.

Wait, the third query is yi=2. So node4's parent is 2. So node4's depth is depth[2] +1 = 1+1=2.

The fourth query is yi=3. So node5's parent is 3. depth[3] is 1 (parent is 1, depth 0+1=1). So node5's depth is 2.

distance between node5 and u=4:

5's parent is 3 (depth 2), 4's parent is 2 (depth 2).

LCA of 5 and 4 is 1.

distance is 2 (depth of 5) + 2 (depth of 4) - 2*0 (depth of LCA) =4.

Candidate is 4, which is larger than D=3.

Thus, D becomes 4.

u=5, v=4.

count=2.

Output is 2.

But the sample output for this case is 2 for all four steps. So perhaps I made a mistake.

But according to the sample input, the fourth query is 3, which is node5's parent is 3.

Thus, node5's depth is 2 (3's depth is 1 +1=2).

node4's depth is 2.

distance between node5 and node4 is 2+2-2*0=4.

So candidate is 4>3. Thus, D=4, count=2.

But the sample output for this case is 2 for all four steps. So this contradicts.

But according to the sample input, the fourth output is 2. So why is that?

Ah, perhaps I made a mistake in the parent for the fourth query.

Let's re-examine the input:

Sample input 2:

4

1

1

2

3

Queries:

Level 1: add node 2 as child of 1.

Level 2: add node3 as child of 1.

Level3: add node4 as child of 2.

Level4: add node5 as child of 3.

So after Level4, the tree has nodes 1, 2,3,4,5.

The diameter after level4:

The new node is 5, parent 3.

distance between 5 and u=4 (from previous step):

u=4, v=3.

distance between 5 and 4:

path is 5-3-1-2-4.

depth of 5 is 2 (3's depth is 1 +1=2).

depth of 4 is 2.

LCA is 1.

distance is 2 +2 - 2*0 =4.

Candidate is 4>3.

D becomes 4. u=5, v=4. count=2.

Thus, output is 2.

But according to the sample output, the fourth line is 2.

Thus, the code would output 2 for this fourth step. Which matches the sample.

Thus, the code works.

Thus, the code is correct.
</think>

```python
import sys
from sys import stdin

def main():
    sys.setrecursionlimit(1 << 25)
    m = int(stdin.readline())
    max_level = 20
    max_node = m + 2
    depth = [0] * (max_node)
    ancestors = [[0] * (max_node) for _ in range(max_level)]
    
    depth[1] = 0
    for k in range(max_level):
        ancestors[k][1] = 0
    
    u = 1
    v = 1
    D = 0
    count = 1

    for _ in range(m):
        yi = int(stdin.readline())
        current_node = len(depth)  # Assuming nodes are added sequentially
        current_node = _ + 2  # Correct node numbering
        parent = yi
        depth[current_node] = depth[parent] + 1
        ancestors[0][current_node] = parent
        for k in range(1, max_level):
            prev_ancestor = ancestors[k-1][current_node]
            ancestors[k][current_node] = ancestors[k-1][prev_ancestor]
        
        def get_dist(a, b):
            if a == b:
                return 0
            a_orig, b_orig = a, b
            if depth[a] < depth[b]:
                a, b = b, a
            for k in reversed(range(max_level)):
                if depth[a] - (1 << k) >= depth[b]:
                    a = ancestors[k][a]
            if a == b:
                return depth[a_orig] + depth[b_orig] - 2 * depth[a]
            for k in reversed(range(max_level)):
                if ancestors[k][a] != ancestors[k][b]:
                    a = ancestors[k][a]
                    b = ancestors[k][b]
            lca = ancestors[0][a]
            return depth[a_orig] + depth[b_orig] - 2 * depth[lca]
        
        dist_u = get_dist(current_node, u)
        dist_v = get_dist(current_node, v)
        candidate = max(dist_u, dist_v)
        
        if candidate > D:
            D = candidate
            if dist_u > dist_v:
                new_u, new_v = current_node, u
            else:
                new_u, new_v = current_node, v
            u, v = new_u, new_v
            count = 2
        elif candidate == D:
            count += 1
        
        print(count)

if __name__ == "__main__":
    main()
```