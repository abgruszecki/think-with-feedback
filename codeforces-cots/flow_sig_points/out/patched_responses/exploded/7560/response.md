<think>
Okay, let's tackle this problem step by step. The problem is about finding, for each K from 1 to N, the maximum number of planets that can be controlled by placing K ships optimally. The key here is that a planet is controlled if it's either a ship's location or lies on the shortest path between two ships. Since the planets form a tree (given the unique path between any two), the shortest path is unique and determined by the tree structure.

Hmm, so the challenge is to model how placing K ships in certain nodes affects the total controlled nodes. For a tree, the controlled nodes when placing ships would form a subtree (or multiple subtrees?), but maybe not. Wait, no. Because any node on the path between any two ships is controlled. So if we have multiple ships spread out, their paths might cover a lot of nodes.

Let me think. For example, if K=2, the best is to place the two ships as far apart as possible, maximizing the number of nodes on their path. But for K>2, perhaps adding more ships in strategic positions can cover more nodes.

Wait, the optimal arrangement for K ships would be to choose a set of nodes such that the union of all paths between every pair of them is as large as possible. But how do we model that?

Another thought: the controlled nodes are exactly the nodes in the closure of the selected nodes under the condition that if two nodes are in the set, all nodes on the path between them are included. This is equivalent to the induced subtree of the selected nodes. Wait, no. Because even if you have three nodes, say A, B, C, the paths between A and B, B and C, and A and C would include all nodes in the subtree formed by these three nodes. So the controlled nodes would form the minimal subtree that contains all selected ships. Because any node in that subtree is on the path between two leaves of the subtree. Wait, perhaps. For example, if the subtree is a star shape (like a central node connected to many leaves), then the minimal subtree is just those nodes. Any node in the subtree is part of some path between two leaves. So, the number of controlled nodes is the number of nodes in the subtree induced by the selected K ships.

Wait, yes! Because when you select K nodes, the minimal subtree that connects them is exactly all the nodes on the paths between every pair of selected nodes. So, the problem reduces to selecting K nodes such that the size of the minimal subtree containing them is maximized. Then, for each K, we need to find the maximum possible size of such a subtree.

So the problem now is transformed into: find, for each K from 1 to N, the maximum possible size of a subtree that can be formed by choosing K nodes. The answer for K is this maximum size.

Therefore, the task is to compute, for each K, the maximum possible size of a subtree when selecting K nodes. Then, for K >= the size of the maximum possible subtree, the answer is N. Wait, no. Because if K is larger than the number of nodes in the maximum possible subtree, but you can select more nodes, perhaps adding nodes to a subtree that is already covering N nodes. So once a subtree covers all nodes (the entire tree), then any K >= that size (like K=N) will have answer N. But in general, how do we model this?

Wait, the problem is that the maximum possible size for a subtree when selecting K nodes is the largest possible. For K=1, it's 1. For K=2, it's the diameter of the tree. The diameter is the longest path in the tree, so the subtree formed by the two end nodes has size equal to the length of the diameter. Then, adding more nodes (for K>2) can help in expanding the subtree. But how?

Wait, perhaps the optimal way is to select the nodes in such a way that each new node added increases the size of the subtree as much as possible. So this seems like a greedy approach. For example, after selecting the two endpoints of the diameter, each subsequent node added should be the one that, when added, increases the subtree size the most.

This reminds me of a problem where the maximum coverage is achieved by a process of selecting the nodes in a certain order. For example, first select the two endpoints of the diameter (size D). Then, each next node is the one that, when added, contributes the maximum possible number of new nodes to the subtree. This could be a node that is a leaf in the current subtree, so adding it would add a path from the subtree to it, but perhaps not. Or maybe not. Hmm.

Alternatively, this process is similar to building a subtree by adding nodes in a way that each addition maximizes the incremental gain. The order of nodes added would determine the total gain. So perhaps the optimal sequence is:

1. Find the diameter (the longest path in the tree). The two ends are selected first. Subtree size is L (the length of the diameter +1, since nodes are counted, not edges). So for K=2, the maximum is L.

2. For K>2, each subsequent node added is a node that is a neighbor to the current subtree. Adding it would add a chain of nodes from the subtree to it. Wait, but how?

Alternatively, perhaps after the initial diameter, the optimal way to select nodes is to pick the nodes in the order of their "maximal distance" from the current subtree. For example, the next node to add is the one that has the longest path from the current subtree, and adding it would add all nodes along that path. But how to model this?

This seems complicated. Let's think of the problem as building a tree incrementally. The initial step is to select two nodes (the diameter), which gives a subtree of size D. Then, each next node added would contribute a certain number of new nodes. The maximum possible for K=3 would be D + (something). The idea is that each additional node can contribute a chain leading from the existing subtree.

This suggests that the optimal way is to first take the diameter, then take all the leaves in the tree, sorted by the length of their paths to the diameter. Each such leaf, when added, contributes a chain of nodes equal to the length of the path from the subtree to the leaf. So, for example, if the current subtree is a path (the diameter), and there's a node that branches off from some node in the middle of the diameter, adding that node would add some nodes. But perhaps the order in which these are added matters.

Alternatively, the problem can be viewed as finding a sequence of nodes such that each new node added (after the first two) contributes the maximum possible number of new nodes to the subtree. Then, the total for K is the sum of these contributions up to K steps.

So, the approach would be:

1. Compute the diameter of the tree. The two endpoints form the initial subtree of size D. For K=1, it's 1; for K=2, it's D.

2. For each K >=3, the maximum possible size is D + sum of the (K-2) largest possible increments. Each increment is the length of a chain that can be added to the subtree.

So, the key is to find all possible chains that can be added to the diameter's subtree and then take the largest ones.

But how do these chains look?

In a tree, after selecting the diameter (the longest path), any other node not on the diameter is part of some subtree branching off from a node on the diameter. For each such node, the maximum depth of the subtree is the length of the path from the branch point to the deepest node in that subtree.

For example, suppose the diameter is a path from A to B. Any node C not on the diameter is part of a subtree that branches off from some node D on the diameter. The depth of this subtree from D is the maximum number of nodes in that branch. For each such branch, the possible contribution when adding a node is the depth of that branch. Because when you add the deepest node in that branch, you add all nodes along the path from D to that node. So each such branch contributes a certain number of nodes when you select a node from it.

But how?

Wait, when you add a new node to the subtree, the subtree expands to include all nodes on the path between any two nodes in the subtree. So if the subtree is already S, and you add a node that's at a distance d from S, then the new subtree will include all nodes along the path from S to the new node. So the number of new nodes added is d.

But how is d calculated? The distance from the node to the subtree S is the minimum number of edges from the node to any node in S. So the path from the node to S is length d, which would add d new nodes (the nodes along the path from the node to S, excluding those already in S).

So for example, if a node is at distance 3 from the current subtree S, then adding that node would add 3 new nodes to the subtree.

Therefore, the optimal strategy after the initial diameter is to select the nodes in the order of the largest possible distances to the current subtree. But since the subtree is expanding each time, the distances for the remaining nodes would need to be recalculated. But that's computationally expensive for large N.

But perhaps there's a way to model all possible contributions as a set of "available" chain lengths, which are the depths of the subtrees branching off from the diameter. Then, the sum of the (K-2) largest chain lengths (if possible) would give the maximum total.

Wait, let's think. Once the diameter is selected (the longest path), the remaining nodes are in subtrees branching off from the nodes along the diameter. For each such branch, the maximum possible depth (distance from the branch node on the diameter to the deepest node in that branch) represents the number of nodes that can be added by selecting the deepest node in that branch. Because adding that node would add all nodes along that branch's path to the diameter.

So, for each branch along the diameter, the depth is the maximum length of the branch. All these branches can contribute their depths as possible increments. So, the maximum possible subtree size for K ships is the sum of the diameter length (D) plus the sum of the (K-2) largest branch depths.

But how to calculate this?

The steps would be:

1. Find the diameter of the tree. Let's say it's a path of L nodes (so L = D +1 if D is the edge count). For example, in the first sample input, the diameter is 3 nodes (1-2-3), so L=3.

2. For each node on the diameter, compute the maximum depth of the branches (subtrees) that branch off from that node, excluding the nodes on the diameter itself. For example, if a node on the diameter has a branch leading to a subtree of depth 2 (like 2 nodes), then the depth is 1 (since the branch has one edge, leading to a node, adding 1 new node when the deepest node is selected).

3. Collect all these depths, sort them in descending order. Then, for each K >=2, the maximum controlled nodes is L + sum of the first (K-2) elements in this sorted list. But wait, L is the size of the diameter (the initial subtree for K=2). For K=3, adding the largest depth would add that number of nodes to the total.

But how does this work?

Let's take the second sample input:

4 nodes connected as a star. The diameter is 2 (nodes 1-2-3? Or perhaps 2 is the central node). Wait, the input is:

4
1 2
3 2
4 2

The tree is a star with 2 as the center. The diameter is between any two leaves, like 1 and 3. So the diameter has 3 nodes (1-2-3). So L=3. The branches off the diameter are from node 2 (the center). The branches are 4 (which is connected to 2). So the maximum depth for this branch is 1 (since adding node 4 would add 1 node to the subtree. The initial subtree is 1-2-3. Adding 4 would make the subtree include 2-4, adding 1 node. So the sorted list of depths is [1].

For K=3, the sum would be 3 (L) + 1 (the first K-2=1 elements) =4. Which matches the sample output. For K=4, we add another, but there are no more depths, so the sum remains 4. So that's correct.

Another example: first sample input.

3 nodes in a line. The diameter is 3 nodes. There are no branches off the diameter. So the list of depths is empty. So for K=3, adding another node (but there are none left), so the maximum is 3. Which is correct.

So this approach seems to work. Then the steps are:

1. Find the diameter (the longest path in the tree). Let the number of nodes in the diameter be L. This is the maximum possible when K=2.

2. For each node on the diameter, compute the maximum depth of each subtree that branches off the diameter (excluding the diameter's path). Collect all these depths. Sort them in non-increasing order.

3. The maximum controlled nodes for K is:

   For K=1: 1

   For K=2: L

   For K>2: L + sum of the first (K-2) depths in the sorted list (if any). However, each depth can be added once. But once all depths are used, adding more K beyond that won't increase the sum. Also, once K exceeds the number of available depths + 2, the sum would be L plus sum of all depths. Then, for K >= 2 + len(depths), the maximum controlled is L + sum(depths) + min( (K - 2 - len(depths)), (N - (L + sum(depths))) ) ? Wait, no. Because once all the depths are added, adding any new node that is already in the subtree doesn't contribute. So once the sum of L + sum(depths) equals N, then adding more ships can't contribute anything. So for K >= 2 + len(depths), the answer is min(N, L + sum(depths) + (K - 2 - len(depths)) * 0 ), which is just min(N, L + sum(depths)).

Wait, but what if the sum of L and the depths is less than N? Then, adding more ships (beyond the 2 + len(depths)) would have to add nodes that are already in the subtree. But those nodes are already controlled. So their inclusion doesn't add any new nodes to the controlled set. So for K >= 2 + len(depths), the answer is the sum of L + sum(depths) plus 0 for each additional K. But wait, maybe the sum of L and the depths is already N. Because all nodes in the tree are part of the diameter or one of the branches. Then adding more ships can't add anything. So, for example, in the first sample, L=3 (the entire tree), sum(depths)=0. So for K=3, the sum is 3, which is N. So the answer is 3. For K=4, since N=3, it's impossible, but in the problem statement, K ranges up to N.

So the formula for the maximum controlled nodes when K ships are used is:

ans[K] = min(1 + sum_{i=1}^{K-1} (1 + ... ), but perhaps the correct formula is:

ans[K] = 1 for K=1

ans[K] = L for K=2

for K >= 3:

ans[K] = L + sum of the first (K-2) elements in the sorted list of depths (sorted in descending order)

But we also need to cap this sum at N. Because once the sum of L plus all the depths is equal to N, then any additional K beyond that will not increase the answer.

So the plan is:

- Compute the diameter (the longest path in the tree) and get L as the number of nodes in that path.

- For each node in the diameter, compute the maximum depth of their subtrees that are not part of the diameter. Collect all these depths into a list, then sort this list in descending order.

- Precompute the prefix sums of this sorted list.

- For each K from 1 to N:

   if K ==1: 1

   else if K ==2: L

   else:

      if (K-2) <= len(depths):

          current = L + prefix[K-2]

      else:

          current = L + prefix[-1]

      ans[K] = min(current, N)

But wait, what if L + sum of all depths is less than N? For example, if there are nodes not covered by the diameter and the branches. But how? The diameter is the longest path. Any other node in the tree must lie on a branch from the diameter. Because the tree is connected, and the diameter is the longest path, so any node not on the diameter must be in a subtree branching off from some node on the diameter.

Wait, yes. Because if there's a node not in the diameter, then it's connected via some path to the diameter. So all nodes not on the diameter are part of subtrees branching off from the diameter nodes. So the sum of L (number of nodes in the diameter) plus all the depths (each depth is the maximum number of nodes in a branch from a diameter node) would be equal to N. Because each depth is the maximum depth of a branch, and when we add all those depths, we are considering all possible nodes in the branches. Or is that not the case?

Wait, no. For each node on the diameter, the branches are the subtrees that are not part of the diameter. For example, if a node on the diameter has a branch that splits into two paths (like a Y-shape), then the depth for that node is the maximum length of those branches. But the other path (the non-maximal one) is not considered. So the sum of the depths for each diameter node may not account for all nodes. Hmm, this is a problem.

Ah, right. Because when we take the maximum depth of each branch from a node on the diameter, we are only considering the deepest path. But other branches from the same node may have their own depths, which are not accounted for. For example, a node on the diameter may have two branches: one of depth 3 and another of depth 2. The maximum depth here is 3. But the other branch (depth 2) could contribute 2 more nodes. However, in our current approach, only the 3 is added as a possible depth. The 2 is not considered. So the sum of all maximum depths may not account for all nodes. Thus, the current approach would miss some nodes.

Wait, but how? Because when you select a ship in a branch, the entire path from that node to the subtree (the current subtree) is added. So in the scenario where a node has two branches (depth 3 and 2), the first time you select a node from the depth 3 branch, you add 3 nodes. Then, selecting a node from the depth 2 branch would add 2 nodes (since the current subtree includes the node on the diameter, so the distance is 2). So those 2 nodes are added. Thus, the depths for the branches would be 3 and 2, and they are part of the sorted list. So in the sorted list, the depths would include both 3 and 2, sorted in descending order.

Wait, but in this case, the node on the diameter has two branches. The maximum depth for that node is the depth of the first branch (3). But the other branch (depth 2) is a separate branch. How do we account for that?

Ah, perhaps I made a mistake in the earlier reasoning. For each node on the diameter, the maximum depth is the maximum of all the depths of its branches. But other branches from the same node can be considered as separate contributions.

Wait, no. For a node u on the diameter, the branches are the subtrees that are not part of the diameter. For each such branch, the depth is the number of nodes in that branch (or the length of the path from u to the deepest node in that branch). However, each such branch is a separate entity and can contribute its depth when a node from it is added. So for each branch (not just the deepest one) from a node on the diameter, we need to add the depth of that branch to the list.

So, the earlier approach is incorrect. Instead, the list of depths should include all possible branch depths for all branches from all nodes on the diameter. For example, if a node on the diameter has two branches of depths 3 and 2, then both 3 and 2 are added to the list.

Thus, the correct way is:

For each node u on the diameter:

   For each subtree branch of u that is not part of the diameter:

       compute the depth (number of nodes in the branch, or the length of the path from u to the deepest node in the branch).

       add that depth to the list of depths.

Then, sort this list in descending order.

So in the previous example with two branches (3 and 2), the depths list would include 3 and 2, and sorted as [3,2].

Then, when adding K-2 nodes, we can take the first (K-2) elements, summing them to L (the diameter size) to get the maximum controlled nodes.

So the initial steps are:

1. Find the diameter path (nodes in the path).

2. For each node in the diameter path:

   a. For each child that is not part of the diameter path, compute the depth of that subtree (the maximum depth from the node to any leaf in that subtree).

   b. Collect all these depths into a list.

3. Sort the list in descending order.

4. Compute the prefix sums.

Then, the answer for each K is:

if K ==1: 1

if K ==2: L (number of nodes in the diameter)

else:

   take the sum of L + sum of first (K-2) depths in the sorted list. If there are not enough depths, then the sum is L + sum of all depths. Then, the answer is the minimum between this sum and N.

But how to compute the depths correctly?

Let's take the example where a node on the diameter has multiple branches. For example, node A on the diameter has two branches: one with depth 3 (nodes B, C, D) and another with depth 2 (nodes E, F). The depths list would include 3 and 2. So when K=3, the sum is L + 3. For K=4, it's L +3 +2. For K=5, there are no more depths, so sum is L+3+2. But if L+3+2 < N, then how?

But in reality, L + sum of all depths should be equal to N. Because each node in the tree is either in the diameter or in a branch from the diameter. So for example:

L is the number of nodes in the diameter.

Each depth in the list is the number of nodes in a branch from a node on the diameter. But wait, no. Because the depth is the maximum depth of the subtree. Wait, perhaps the depth is counted as the number of nodes in that branch. Or maybe the depth is the number of edges (distance from the node on the diameter to the deepest node in the branch). For example, a branch that is a single node (directly connected to the diameter node) would have depth 1 (number of nodes) or 0 (edges). This is crucial.

In the problem statement, the depth is the number of nodes added when selecting the deepest node in that branch. For example, if a branch has a path from the diameter node u to v to w, then selecting w would add two nodes (v and w). So the depth here is 2. Therefore, the depth should be the number of nodes in the branch minus 1 (the node u is already part of the diameter).

Wait, but the branch includes nodes that are not part of the diameter. So, the branch is a subtree where the root is u (on the diameter), and the depth is the maximum number of nodes from u to any leaf in the subtree. So for a branch u -> v -> w, the depth is 2 (u is not counted because it's part of the diameter). So in this case, the depth is 2, which is the number of nodes in the branch (excluding u) that form the longest path from u in that branch. So when we select a ship in the deepest node (w), adding it to the subtree would add v and w, which is 2 nodes. So the depth for this branch is 2.

Therefore, the correct way to compute the depths is for each branch (subtree not part of the diameter), the maximum number of nodes that can be added by selecting the deepest node in that branch. Which is equal to the depth of the branch (number of nodes in the path from the root u to the deepest node, excluding u).

So, for each node on the diameter, for each of its branches (subtrees not part of the diameter), compute the depth (number of nodes in the longest path from u to a leaf in that branch, excluding u). Then, collect all these depths into the list.

Once we have this list, sorted in descending order, the sum of L (number of nodes in the diameter) plus the sum of the first (K-2) depths (for K >=2) gives the maximum controlled nodes. But this sum can't exceed N.

But since L is the number of nodes in the diameter, and each depth in the list is the number of nodes in a branch (not part of the diameter), the sum of L and all depths in the list is exactly N. Because each node is either in the diameter or in exactly one branch (since the tree is connected and the diameter is the longest path). Therefore, the sum of L and all depths is N. So when K-2 >= the number of depths, the sum is L + sum(depths) = N. So for K >= 2 + len(depths), the answer is N.

So putting it all together:

- Compute the diameter path.

- For each node in the diameter, compute all possible branch depths (excluding the diameter path), and collect them into a list.

- Sort the list in descending order.

- Precompute the prefix sums.

- For each K from 1 to N:

   if K ==1: ans[K] =1

   else:

      if K ==2: ans[K] = L

      else:

          t = K-2

          if t <= len(prefix):

              total = L + prefix[t-1]

          else:

              total = L + prefix[-1]

          ans[K] = min(total, N)

So the steps are:

1. Find the diameter.

2. Collect all branch depths.

3. Sort and compute prefix sums.

Now, how to implement this efficiently, given that N can be up to 1e5.

First, finding the diameter of a tree can be done using BFS twice:

- Pick any node u, find the farthest node v from u.

- Then find the farthest node w from v. The path from v to w is the diameter.

But to find the nodes along the diameter path, we need to track parents during BFS.

Once we have the path from v to w, we can mark all nodes in the diameter and collect their branches.

But this requires tracking the parent pointers and reconstructing the path.

Once the diameter is found, the nodes along the path can be stored in a list.

Then, for each node in the diameter list, we need to traverse all its adjacent nodes, excluding those that are in the diameter (since they are part of the diameter path). For each such adjacent node, compute the depth of the subtree.

But how to compute the depth of the subtree for each branch?

For each node u in the diameter, when processing its adjacent nodes, we need to exclude the adjacent nodes that are part of the diameter (i.e., the previous and next nodes in the diameter path). For example, if the diameter is [v, a, b, c, w], then node a's adjacent nodes are v, b, and possibly other nodes. So when processing a, the branches are all adjacent nodes except v and b.

For each such branch (subtree), compute the depth as the maximum number of nodes from that branch (excluding u) when traversing away from the diameter.

This can be done using a DFS or BFS for each branch. But for large N, this approach could be O(N) per branch, leading to O(N) total time.

But perhaps there's a smarter way.

Alternatively, we can perform a BFS from the diameter nodes, and for each node not in the diameter, compute the depth of the branch it belongs to.

Wait, but perhaps we can compute the depth for each branch as follows:

Once the diameter path is known, all nodes not in the diameter are part of a branch. For each such node, the depth of its branch is the maximum distance from the diameter node to any node in the branch.

But this would require processing each node once.

Alternatively, for each node in the diameter, we can perform a BFS/DFS to compute the maximum depth in each branch.

So for a node u in the diameter:

   For each neighbor v of u that is not in the diameter:

      The maximum depth of the subtree rooted at v (excluding u) is computed as 1 (for v) plus the maximum depth of its children (excluding u). So this can be done via DFS.

But this would take O(M) time overall, where M is the number of edges in the tree (which is O(N)). Since each node not in the diameter is processed exactly once.

So for each branch from a diameter node u:

   The depth is the maximum number of nodes in that branch (excluding u).

So the approach is:

- For each node in the diameter:

   For each of its adjacent nodes that are not in the diameter:

      Perform a BFS or DFS to compute the maximum depth of that subtree.

But this could be O(N) time in total, which is acceptable for N up to 1e5.

But how to implement this efficiently.

Let's outline the steps:

1. Find the diameter path. Let's say it's stored as a list of nodes, diam.

   For example, diam = [v, a, b, c, w], where v and w are the endpoints.

2. Create a set of nodes in the diameter for O(1) lookups.

3. For each node u in diam:

   For each neighbor v of u:

      if v is not in the diam set or (if u is not the first node, v is the previous in diam) or (if u is not the last node, v is the next in diam):

          skip. Because these are part of the diameter path.

      else:

          process this neighbor as the root of a branch. Compute the maximum depth of the subtree starting at v, with parent u. The depth is the number of nodes in the longest path from v to a leaf, excluding u.

          Add this depth to the list.

Wait, perhaps not. Because when u is in the diam, and v is a neighbor not in the diam, then the subtree starting at v (excluding u) is the branch. The maximum depth of this branch is the maximum distance from v to any leaf in this subtree. So for this subtree, the depth is the number of nodes in the longest path from v to a leaf.

So for example, if the subtree is v -> a -> b, then the depth is 3 (nodes v, a, b). When added as a branch of u (the diam node), this contributes a depth of 3. But since the ship is placed at b, adding it would add v, a, b to the controlled nodes. So the depth here is 3, which is the number of nodes added.

So for each branch, the depth is the number of nodes in the longest path from the branch root (v) to any leaf in the subtree. Which is equivalent to the maximum depth of the subtree rooted at v.

Therefore, to compute this for each branch, we can perform a BFS or DFS starting at v, and compute the maximum depth.

But doing this for each branch could be expensive. However, considering that each node is processed exactly once (since all branches are part of the tree outside the diameter), the total time would be O(N), which is acceptable.

So, the plan is:

For each node u in the diam:

   For each neighbor v of u:

      if v is in the diam set, and is the next or previous node in the diam path → skip.

      else:

          compute the maximum depth of the subtree rooted at v (excluding u).

          add this depth to the list.

Now, how to efficiently check whether v is the next or previous node in the diam path.

For example, diam is a list. For each node u at index i in diam:

   previous node is diam[i-1] (if i>0)

   next node is diam[i+1] (if i < len(diam)-1)

So when u is diam[i], its neighbors in the diam path are diam[i-1] and diam[i+1], if they exist.

Therefore, when processing a neighbor v of u, if v is diam[i-1] or diam[i+1], then it's part of the diam path and should be skipped. Other neighbors (not in diam, or in diam but not adjacent in the path) are considered as branches.

Wait, but the diam is a path. So each node in the diam has exactly two adjacent nodes (except the endpoints). So for example, the diam is a list of nodes connected in a chain. So, any node in the diam (except endpoints) has two neighbors in the diam (previous and next). Endpoints have one.

So for a node u in the diam, its neighbors are:

- Previous in diam (if exists)

- Next in diam (if exists)

- Other neighbors (which are part of branches).

So for each neighbor v of u:

   if v is either the previous or next node in the diam → skip (since it's part of the diam path)

   else → process as a branch.

So for each such v, we need to compute the maximum depth of the subtree rooted at v, which is the maximum distance from v to any leaf in that subtree (counted in nodes).

So for example, if the subtree rooted at v has a longest path of 3 nodes (v → a → b → c), then the depth is 3.

To compute this, we can perform a BFS for each branch. However, this may be time-consuming for large N.

Alternatively, perform a DFS for each branch, tracking the maximum depth.

But this would take O(N) time in total. Because each node not in the diam is part of exactly one branch. So each such node is processed once.

So the steps are:

Once the diam is found and stored as a list:

   mark all nodes in diam in a set.

   for each node u in diam:

      for each neighbor v of u:

          if v is the previous or next node in the diam → skip

          else:

              if v is not in diam:

                  perform a BFS/DFS starting at v, with parent u.

                  compute the maximum depth of this subtree.

                  add the depth to the list.

But wait, nodes in the diam can have other neighbors in the diam (but not adjacent in the path). No, because the diam is a path, so each node in the diam (except endpoints) has exactly two neighbors in the diam. So any other neighbor must be part of a branch.

Wait, no. For example, consider a tree where the diam is a path like A-B-C-D. Then B's neighbors are A and C (both in the diam). So any other neighbor of B must be part of a branch. So in this case, when processing B's neighbors, any neighbor other than A and C are branches.

So the code for each u in diam:

   for each neighbor v of u:

      if v is in the diam and (v is prev or next in the path):

          continue

      else:

          compute the depth of the subtree starting at v.

Thus, this approach correctly identifies the branches.

Now, implementing this in Python.

First, we need to find the diameter.

Finding the diameter involves two BFS passes.

First, pick a random node (say, 0), find the farthest node from it (say, u).

Then, perform BFS again from u to find the farthest node v. The path from u to v is the diameter.

But how to reconstruct the path?

To do this, during BFS, we can track the parent of each node. Then, once we find the farthest node v, we can backtrack using the parent pointers to reconstruct the path.

So, code steps:

def bfs(start):

    parent = [ -1 for _ in range(n+1) ]

    distance = [ -1 for _ in range(n+1) ]

    q = deque()

    q.append(start)

    distance[start] = 0

    while q:

        u = q.popleft()

        for v in adj[u]:

            if distance[v] == -1:

                distance[v] = distance[u] +1

                parent[v] = u

                q.append(v)

    max_dist = max(distance)

    far_node = distance.index(max_dist)

    return far_node, parent

So:

start with node 1.

u = farthest node from 1.

v = farthest node from u.

Then, the path from u to v is the diameter.

Reconstructing the path:

path = []

current = v

while current != u:

    path.append(current)

    current = parent[current]

path.append(u)

path = reversed(path) → but this may vary based on implementation.

Wait, no. The parent pointers are from the BFS starting at u. So during BFS from u, the parent of v would be the node that led to v. So backtracking from v to u gives the path in reverse order.

So the code would be:

start_node = 1

u, _ = bfs(start_node)

v, parent = bfs(u)

path = []

current = v

while current != -1:

    path.append(current)

    current = parent[current]

path = path[::-1]

But if the parent is -1 (for u), then the loop may break. So the code should be:

current = v

path = []

while current != u:

    path.append(current)

    current = parent[current]

path.append(u)

path = path[::-1]

Wait, not sure. Depends on the parent array.

Alternatively, after the BFS from u, the parent array gives the parents for all nodes. To reconstruct the path from u to v, the path is v, parent[v], parent[parent[v]], ..., u.

But since the BFS was done from u, the parent of u is -1, so the loop should stop when current is u.

Wait, during BFS from u, the parent of u is -1, but for all other nodes, parent is set.

So to get the path from u to v:

current = v

path = []

while current != -1:

    path.append(current)

    current = parent[current]

But this gives the path in reverse order (v → ... → u). So path would be [v, p1, p2, ..., u]. But reversed.

Wait, no. For example, if the path is u → a → b → v, then parent[v] = b, parent[b] = a, parent[a] = u, parent[u] = -1. So current starts at v, appends v, then b, then a, then u. The list is [v, b, a, u]. Then, reversing gives [u, a, b, v], which is the correct path.

So code:

path = []

current = v

while current != -1:

    path.append(current)

    current = parent[current]

path.reverse()  # Now path is u → ... → v

But wait, no. Because the path starts at v and moves towards u. So when you reverse, the path becomes u's parent, etc. Wait, no. For example:

If the parent array is such that parent[v] = b, parent[b] = a, parent[a] = u, parent[u] = -1.

current = v:

path becomes [v, b, a, u], then reversed → [u, a, b, v].

Yes. So the path is the correct order from u to v.

Once we have the path, we can collect all nodes in the diameter.

Now, for each node in the path, process its branches.

For each node u in the path:

   for each neighbor v in adj[u]:

      if v is the previous or next node in the path → skip.

      else:

          compute the depth of the subtree rooted at v.

So how to check if v is the previous or next node in the path?

We can create a dictionary or list that stores the index of each node in the path. For example:

diam_nodes = {node: index for index, node in enumerate(path)}

Then, for a node u in path, its previous node (if exists) is path[index-1], and next node is path[index+1] (if exists).

So for each neighbor v of u:

   if v in diam_nodes:

       if diam_nodes[v] == diam_nodes[u] -1 or diam_nodes[v] == diam_nodes[u]+1:

           continue

   else:

       process the subtree.

Wait, but if a node v is in the path but not adjacent to u (which shouldn't happen, since the path is a chain), then it's part of the path but not adjacent. But in the tree, the path is a simple path, so each node in the path (except endpoints) has exactly two neighbors in the path.

So for a node u in the path (not an endpoint), its neighbors in the path are the previous and next nodes. Any other neighbor is part of a branch.

So, for each neighbor v of u:

   if v is in the path and (v is previous or next) → skip.

   else → process.

So, to implement this:

For each u in path:

   index = diam_nodes[u]

   prev_node = path[index-1] if index >0 else None

   next_node = path[index+1] if index < len(path)-1 else None

   for v in adj[u]:

       if v == prev_node or v == next_node:

           continue

       else:

           compute the depth of the subtree rooted at v, with parent u.

So, now the question is, how to compute the depth of the subtree rooted at v, with parent u.

This is the maximum depth of the subtree, which can be found by performing a BFS or DFS to find the longest path from v (excluding u) to any leaf.

But to compute this efficiently, we can perform a post-order traversal and keep track of the maximum depth.

Alternatively, for each node in the branch (rooted at v), compute the depth recursively.

But recursion depth can be a problem for large N. So an iterative approach is better.

Here's an approach:

def compute_depth(root, parent_node):

    max_depth = 0

    stack = [(root, parent_node, 0)]

    while stack:

        node, parent, depth = stack.pop()

        current_depth = depth +1

        max_depth = max(max_depth, current_depth)

        for neighbor in adj[node]:

            if neighbor != parent:

                stack.append( (neighbor, node, current_depth) )

    return max_depth

Wait, but this returns the maximum depth from the root (v) to any leaf, measured in terms of the number of nodes (depth+1?), or edges (current_depth)?

Wait, the initial call is compute_depth(v, u). So for the first call, the depth is 0, which represents the depth of the root (v). Then, for each child, we add 1.

Wait, for example:

v is the root. Its child is a. The depth from v to a is 1. Then a's child is b. The depth is 2. So the max depth is 2, which represents the number of nodes (v, a, b). So when adding this branch, the depth is 2. So when a ship is placed in b, adding this to the subtree contributes 2 nodes (a and b), since v is already part of the subtree (the diam node u is part of the diameter, which is included in the initial subtree when K=2).

Wait, no. Because when K=2, the initial subtree is the diam path. The node u is part of the diam. So the branch rooted at v (which is a neighbor of u but not part of the diam) is part of the subtree when a ship is placed in v. So the depth is the number of nodes in the longest path from v (excluding u). So the compute_depth function should return the maximum number of nodes in that path, which is the number of nodes in the branch. For example, if the branch is v -> a -> b, then the depth is 3 (nodes v, a, b). But since u is part of the diam, and when we add a ship in b, the path from u to b is u-v-a-b, so the subtree now includes u, v, a, b, adding 3 new nodes (v, a, b) when K increases by 1 (from K=2 to K=3). So the depth for this branch is 3.

But according to the compute_depth function above, if the root is v, and parent is u, then the depth would be 3 (nodes v, a, b). So yes, the function returns the correct depth.

Therefore, the function compute_depth returns the number of nodes in the longest path from the root (v) to any leaf in its subtree. This is exactly what we need.

But for large N, this approach can be slow. Because for each branch, we are doing a traversal of the entire subtree. For example, if the tree is a star with a long branch, this would take O(N) time.

But in practice, since each node not in the diam is processed exactly once (as part of exactly one branch), the total time is O(N), which is acceptable for N up to 1e5.

So, with this approach, we can collect all the depths.

Once we have the depths list, we sort it in descending order, compute prefix sums, and then compute the answers for each K.

Now, let's test this approach against the sample inputs.

Sample Input 1:

3

1 2

2 3

The diam path is [1, 2, 3]. So len(diam) =3.

For each node in the diam:

Node 1:

   neighbors are 2 (next node) and others (none).

   So no branches.

Node 2:

   neighbors are 1 and 3 (prev and next in diam), so no branches.

Node 3:

   neighbors are 2 (prev in diam), no other branches.

So the depths list is empty. So for K=3, ans is 3.

Sample Input 2:

4

1 2

3 2

4 2

The diam is between 1 and 3: path is [1,2,3]. len(diam)=3.

For each node in the diam:

Node 1: neighbors is 2 (next node). No other neighbors.

Node 2: neighbors are 1 (prev), 3 (next), and 4 (branch).

So for neighbor 4:

compute_depth(4, 2). The subtree is just node 4. Depth is 1 (only one node). So the depths list is [1].

Node 3: neighbors is 2 (prev). No other branches.

So depths list is [1].

Sorted: [1].

For K=3, sum is 3 (diam) + 1 (K-2=1) → 4. Which matches the sample output.

Another example: the star-shaped tree where the center is 2, connected to 1,3,4,5. Diam is between 1 and 3 (path 1-2-3), len=3. The branches are 4 and 5. Each branch from node 2 has depth 1.

So depths list is [1,1]. Sorted as [1,1].

For K=2, ans=3.

For K=3, ans=3+1=4.

For K=4, 3+1+1=5.

But N=5. So for K=4, ans=5.

For K=5, ans=5.

So this approach works.

Now, the code.

But how to handle the tree structure?

First, read N.

Then, build adjacency list.

Then find the diam.

Then process each node in the diam to collect depths.

Then sort and compute prefix sums.

Then compute answers.

Now, implementing in Python.

But for large N (1e5), Python's recursion depth is limited, so we need to use iterative DFS/BFS.

Now, code:

Testing against sample input 1.

```python
import sys
from collections import deque


def main(input_stream, output_stream):
    def input():
        return input_stream.read()

    data = input_stream.read().split()
    n = int(data[0])
    adj = [[] for _ in range(n+1)]
    ptr =1
    for _ in range(n-1):
        u = int(data[ptr])
        v = int(data[ptr+1])
        adj[u].append(v)
        adj[v].append(u)
        ptr +=2

    # Function to perform BFS and return the farthest node and parent array
    def bfs(start):
        parent = [-1]*(n+1)
        distance = [-1]*(n+1)
        q = deque()
        q.append(start)
        distance[start] =0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] +1
                    parent[v] = u
                    q.append(v)
        max_dist = max(distance[1:n+1]) # assuming nodes are 1-based
        far_node = distance.index(max_dist)
        return far_node, parent

    # Find the diameter path
    u, _ = bfs(1)
    v, parent = bfs(u)
    # Reconstruct path
    path = []
    current = v
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    diam_len = len(path)
    diam_set = set(path)

    depths = []

    # Create a dictionary to map each node in diam to its index
    diam_nodes = {node: idx for idx, node in enumerate(path)}

    for node in path:
        idx = diam_nodes[node]
        prev_node = path[idx-1] if idx >0 else None
        next_node = path[idx+1] if idx < len(path)-1 else None
        for neighbor in adj[node]:
            if neighbor == prev_node or neighbor == next_node:
                continue
            if neighbor in diam_set:
                # this can happen if the neighbor is in diam but not prev or next (unlikely)
                # but perhaps possible in some cases?
                # in a tree, the path is a simple path, so neighbor in diam implies it's either prev or next.
                # so this case shouldn't happen.
                continue
            # Compute the depth of this branch
            max_depth =0
            stack = [(neighbor, node, 1)] # (current_node, parent, depth)
            while stack:
                u_current, u_parent, current_depth = stack.pop()
                if current_depth > max_depth:
                    max_depth = current_depth
                for v_neighbor in adj[u_current]:
                    if v_neighbor != u_parent:
                        stack.append( (v_neighbor, u_current, current_depth +1) )
            depths.append(max_depth)

    # Sort depths in descending order
    depths.sort(reverse=True)
    prefix = []
    current_sum =0
    for d in depths:
        current_sum += d
        prefix.append(current_sum)

    ans = [0]*(n+1) # ans[K] for K=0 to N, but we'll ignore K=0.

    ans[1] =1
    ans[2] = diam_len

    for K in range(3, n+1):
        if K-2 <= len(prefix):
            if K-2 ==0:
                total = diam_len
            else:
                total = diam_len + prefix[K-3]
        else:
            total = diam_len + (prefix[-1] if prefix else 0)
        ans[K] = min(total, n)

    # Now, handle K=2 and higher
    # Also, after processing all K, we need to output the maximum between the computed value and the previous ones.

    # Wait, no. The current approach computes for each K the maximum possible.

    # However, there's a case where for K=4, the sum could be less than N, but adding another ship would include more nodes.

    # Wait, no. Because according to our earlier reasoning, the sum of diam_len and all depths is N.

    # So for K >=2 + len(depths), ans[K] = N.

    # So the code should handle this.

    # But how?

    # Because after K exceeds 2 + len(depths), the sum is diam_len + sum(depths) = N.

    # So the code computes total = diam_len + sum(depths) (if K-2 >= len(depths)), and then ans[K] is min(total, N), which is N.

    # So it's correct.

    # Now, build the output list.

    output = []
    for K in range(1, n+1):
        if K ==1:
            output.append(str(1))
        else:
            output.append(str(ans[K]))

    print(' '.join(output), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
1 2
3 2
4 2
""",
            "output": \
"""\
1 3 4 4
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

Sample 2:

4

Edges: 1-2, 3-2, 4-2.

diam path is [1,2,3]. diam_len=3.

depths is [1], prefix is [1].

For K=3: K-2=1 →3 +1=4.

For K=4: K-2=2 > len(prefix)=1 →3+1=4. Which is N=4.

So code outputs 1 3 4 4. Correct.

Another test case where there are multiple branches.

For example, a tree where the diam is 4 nodes (A-B-C-D). Node B has a branch of depth 2 (B-E-F), and node C has a branch of depth 3 (C-G-H-I). The depths list would be 2 and 3. sorted as [3,2].

So for K=2: ans=4.

For K=3:4+3=7. But if N is 4+3+2+ ... ?

Wait, diam_len is 4. The sum of depths is 3+2=5. So N=4+5=9.

For K=3: ans=4+3=7.

K=4:4+3+2=9.

K=5:9 (since sum of depths is 5, which equals N=9).

So code would correctly handle this.

Thus, the code should be correct.
</think>

```python
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    ptr = 1
    for _ in range(n - 1):
        u = int(data[ptr])
        v = int(data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2

    # BFS to find the farthest node from 'start' and return it along with parent pointers
    def bfs(start):
        parent = [-1] * (n + 1)
        distance = [-1] * (n + 1)
        q = deque([start])
        distance[start] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    parent[v] = u
                    q.append(v)
        max_dist = max(distance[1: n + 1])
        far_node = distance.index(max_dist)
        return far_node, parent

    # Find the diameter path
    u, _ = bfs(1)
    v, parent = bfs(u)
    path = []
    current = v
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    diam_len = len(path)
    diam_set = set(path)
    diam_nodes = {node: idx for idx, node in enumerate(path)}

    # Calculate depths of all branches from the diameter
    depths = []
    for node in path:
        idx = diam_nodes[node]
        prev_node = path[idx - 1] if idx > 0 else None
        next_node = path[idx + 1] if idx < len(path) - 1 else None
        for neighbor in adj[node]:
            if neighbor == prev_node or neighbor == next_node:
                continue
            if neighbor in diam_set:
                continue
            max_depth = 0
            stack = [(neighbor, node, 1)]  # (current, parent, depth)
            while stack:
                curr, par, depth = stack.pop()
                if depth > max_depth:
                    max_depth = depth
                for child in adj[curr]:
                    if child != par:
                        stack.append((child, curr, depth + 1))
            depths.append(max_depth)

    # Sort depths and compute prefix sums
    depths.sort(reverse=True)
    prefix = []
    current_sum = 0
    for d in depths:
        current_sum += d
        prefix.append(current_sum)

    # Prepare the answer array
    ans = [0] * (n + 1)
    ans[1] = 1
    ans[2] = diam_len
    for K in range(3, n + 1):
        t = K - 2
        if t <= 0:
            total = diam_len
        elif t <= len(prefix):
            total = diam_len + prefix[t - 1]
        else:
            total = diam_len + (prefix[-1] if prefix else 0)
        ans[K] = min(total, n)

    # Generate the output
    output = [str(ans[K]) for K in range(1, n + 1)]
    print(' '.join(output))

if __name__ == "__main__":
    main()
```
