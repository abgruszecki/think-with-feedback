<think>
Okay, so I've got this programming problem to solve. Let me read through the problem statement carefully again to make sure I understand what's being asked.

The problem is about gluing together multiple spiders (trees) to form a single spider (another tree) such that the length of the resulting spider is as large as possible. The length here is the diameter of the tree, which is the longest path between any two nodes. So the task is to combine all the given trees into one in such a way that the diameter of the combined tree is maximized.

Hmm. So each individual spider is a tree. When we glue them together, we have to merge them by identifying some beads (nodes) from different spiders. The key is that the merged structure must also be a tree. So, when merging two trees, we can't create cycles. That means each merge must connect two trees by merging a single node from each. Because if you merge two nodes from different trees into one, then the combined structure is a tree. For example, if I have tree A and tree B, I pick a node from A and a node from B, and glue them together (i.e., make them the same node). Then the combined structure is a tree.

So the approach is to find a way to glue all the spiders into one tree such that the diameter is maximized. The maximum possible diameter would be derived by connecting the longest possible paths from each spider in a way that links them through the merged nodes.

Let me think. The maximum diameter of a tree formed by merging multiple trees can be achieved by connecting the centers of the longest paths (the diameters) of each individual tree. Wait, not sure. Let's break it down.

For each individual spider (tree), the diameter is the longest path between any two nodes. Let's call the diameter of each spider D_i. Now, when we merge all spiders into one, the total diameter will be determined by how these individual D_i's are connected.

If we have two spiders, each with diameters of length d1 and d2. The optimal way to merge them is to connect the two spiders via one node from each of their diameters. Then the total diameter could be d1 + d2. Wait, no. Wait, suppose the two spiders each have their own diameters. To merge them, you pick a node (like one end of the diameter of spider 1) and a node from spider 2 (like one end of spider 2's diameter). Then the combined diameter would be the sum of the two diameters plus 1? Wait, no. Because when merging two trees, the path would go through the merged node. For example, if spider 1 has a diameter of A-B-C (length 2), and spider 2 has X-Y-Z (length 2), merging B and X. Then the longest path could be A-B (merged with X)-Y-Z: that's A to Z which is 3 (A-B) + (X-Y-Z) which is 2 steps. Wait, but B and X are the same node, so the path from A to Z would be A-B (merged node) to Y to Z. So length is 1 (A to B) + 2 (Y to Z via X) → total 3. Which is sum of each radius? Hmm, maybe not. Maybe the maximum possible diameter when merging two trees is the maximum of the individual diameters and the sum of the two radii (half the diameter) plus 1.

Wait, perhaps the optimal way to connect two trees is to connect their centers. Wait, let's think in terms of each spider's radius. The radius is the minimal maximum distance from a node to all others. The center of a tree's diameter is the middle node (if diameter is even) or the middle two nodes (if odd). For example, if the diameter is A-B-C-D (length 3, even), the centers are B and C. So when you connect two trees via their centers, the maximum distance in the merged tree could be (d1//2) + 1 + (d2//2), and then adding that to whatever. But how does this help?

Alternatively, when merging multiple trees, the maximum possible diameter after merging all of them would be the sum of the two longest radii (half the diameters of the individual spiders) plus the sum of the next longest radii, etc. Wait, maybe not. Let's think.

Suppose we have three spiders. The best way to merge them is to link their centers in a chain. For example, spider 1's center, spider 2's center, spider 3's center. Then the maximum path would be the sum of their radii (half the diameter) plus the number of edges between the centers. But each merge between two centers adds a single edge? Or do the merged nodes become a single node?

Wait, no. When we merge two nodes from different trees, those nodes are identified. So, when we merge a node from tree A and a node from tree B, they become one node in the combined tree. So, any path that passes through this merged node will traverse through both trees.

So, if I have two trees, each with their own diameters. Let's say the first tree's diameter is D1, and the second's is D2. The best way to merge them is to connect one of the endpoints of the first diameter to one of the endpoints of the second diameter. Then the maximum path would be D1 + D2. Because the path would start at the other endpoint of D1's diameter, go through the merged node (which is part of the first diameter's path), then through the entire D2's diameter. So the total length is D1 + D2.

Wait, but if the merged nodes are endpoints, then the combined path would be D1 + D2. Let's take an example. Suppose first spider has a diameter of 2 (nodes A-B-C, path length 2). Second spider has diameter 2 (X-Y-Z). If we merge B and Y. Then the combined tree's diameter could be A-B-Y-Z, which is length 3. But that's the sum of each diameter's half? Not exactly.

Alternatively, if we merge the two trees by connecting their endpoints. For example, merge C (end of first diameter) and X (end of second diameter). Then the maximum path would be A-B-C (merged with X) - Y-Z. The path from A to Z would be A-B-C (length 2) + X-Y-Z (length 2), but since C and X are merged, the path is A-B-C (X)-Y-Z. So that's 2 + 2 =4 steps. Which is the sum of the two diameters. So in this case, the combined diameter is 4, which is the sum of the two diameters.

So that's better than merging at their centers. So in this case, if you merge two trees by their endpoints, the combined diameter is the sum of their diameters. So that's a good way to maximize the total diameter.

Wait, but in the first example, when the input is a single spider, the output is its diameter. Which is correct.

In the second sample input, there are two spiders. The first has diameter 2 (the longest path is 1-3, length 2). The second has diameter 3 (the longest path is between 1 and 4, perhaps). The output is 4. Let's see: if we merge the two trees by connecting bead 2 (from first) and bead 1 (from second). Then the combined tree's diameter would be 3 (from first tree's 3-1-2) plus 3 (from second's 1-2-3-4?), but maybe the path would be longer. Wait, perhaps the merged structure's diameter is 4, which is what the sample shows.

So maybe the approach is to find for each spider its diameter, and then the maximum possible total diameter is the sum of the two longest diameters plus the sum of the other (k-2) diameters' radii. Wait, not sure.

Alternatively, when merging multiple spiders, the total maximum diameter is the maximum between all pairs of the individual diameters plus the sum of the two maximum radii (the radius is the ceiling of the diameter divided by two). For example, when you have n spiders, you take the maximum individual diameter, and then the sum of the two largest radii plus the sum of the next largest radii, etc. Or perhaps it's the sum of the two largest radii plus the sum of all other spiders' radii.

Wait, perhaps the optimal approach is to compute for each spider its radius (diameter // 2, rounded up). Then, the total maximum possible diameter is the sum of all radii except the two largest, plus the sum of the two largest radii. Wait, no. Wait, if you have multiple spiders, each with a radius r_i (ceil(d_i/2)), then when you merge them all by their centers (so each spider is connected via their center nodes), the maximum path would be the sum of the two largest radii plus the sum of all other radii. Because each spider contributes its radius to the path. Wait, perhaps not. Let me think.

Suppose we have three spiders with radii 3, 4, and 5. The maximum possible diameter would be 5+4 + 3 = 12. Because the path would go through the centers of each spider, connecting the two spiders with the largest radii (5 and 4) and the third (3). So the path would be 5 + 4 + 3 = 12. But that's not possible. Because when you merge the spiders into a chain: each center is connected to the next. The first's radius is 5 (so the maximum distance from its center is 5), the second's 4 (so the maximum from its center is 4), and the third's 3. The path would go from the furthest point in the first spider (5 steps from center) to the furthest point in the third spider (3 steps from its center). The path would traverse the first center (distance 5), then through the second center (distance 4 steps in the other direction?), but I'm getting confused.

Alternatively, when all spiders are merged by their centers into a chain, the maximum path is the sum of the two largest radii plus the sum of all other radii. Wait, perhaps. For example, in the case of three spiders with radii 3, 4, 5. The maximum path would be 5 + 4 + 3 = 12. Because the path would start at a node 5 away from the first center, go through the first center (merged with the second center?), then the second center (merged with the third center?), then reach a node 3 away. So the total path length would be 5+4+3=12.

So the way to compute the maximum possible diameter is to take all the radii of the spiders, sort them in descending order, and sum all but the two largest, then add the sum of the two largest. Wait, no. Because in the example with two spiders, the maximum is the sum of their diameters if merged end to end. But according to this approach, the sum of their radii (d1//2 + d2//2) would be (d1 + d2)/2 if d1 and d2 are even. But that's not the case in the second sample input.

Wait, the second sample input:

Sample Input 2:
2
3 1 2 1 3
4 1 2 2 3 2 4

First spider: the edges are 1-2 and 1-3. The diameter is between 2 and 3, which is length 2 (distance 2). So the radius is 1. The second spider has edges 1-2, 2-3, 2-4. The diameter is from 3 to 4 via 2 and 2 to 1? Or perhaps the diameter is from 3 to 4, which is length 2 (3-2-4). Wait, wait the edges are 1-2, 2-3, 2-4. The possible paths are 1-2-3 (length 2), 1-2-4 (length 2), 3-2-4 (length 2). So the diameter is 2. So the radius for each is 1. Then according to the approach of summing the two largest radii (1 and 1), plus the sum of the others (none), that would be 2. But the sample output is 4. So that approach is wrong.

Ah, so this suggests that the previous reasoning is incorrect. So the correct approach must be different.

Hmm. Let's look at the second sample. The two spiders have diameters 2 and 2. The output is 4. So when merged, their combined diameter is 4. How is that possible?

In the sample explanation, they merge bead 2 of the first spider with bead 1 of the second. The first spider's diameter is between 2 and 3 (distance 2). The second's diameter is between 3 and 4 (distance 2). So when merged, the path from 3 (first spider) to 4 (second spider) would be 3-2 (merged with 1) -2-3-4. Wait, no. Let me see.

The first spider's structure: beads 1 connected to 2 and 3. The diameter is between 2 and 3 (distance 2). The second spider's beads are 1-2, 2-3, 2-4. The diameter is between 3 and 4 (distance 2). When merged by 2 (first spider) and 1 (second spider), the merged node is 2-1. So the path from 3 (first spider) to 4 (second spider) would be 3 - 2 (merged node) -2 (from second spider) -4. But that's 3 steps. Wait, but that's only length 3. But the sample output is 4.

Wait, perhaps I'm misunderstanding the structure. Let me draw the merged tree.

First spider's beads: 1 connected to 2 and 3.

Second spider's beads: 1 connected to 2, which is connected to 3 and 4.

When merged, bead 2 of first and bead 1 of second are the same. So the merged tree has:

Edges from the first spider: 1-2 (merged), 2-3.

Edges from the second spider: 2 (merged)-3, 2-4.

So the merged tree has nodes:

From first: 2 (merged), 1, 3.

From second: 2 (merged), 3, 4.

So the merged tree structure is:

The merged node is 2 (from first) and 1 (from second) → let's call this node A.

Edges from A: connected to 1 (from first spider), 3 (from first spider), 3 (from second's edges: A connected to 3 (second's 2-3?), wait no. The second spider's edges are 1-2, 2-3, 2-4. After merging, bead 1 of the second spider is merged into bead 2 of the first. So the edges of the second spider become:

2 (merged node) connected to 3, and 2 connected to 4.

So the merged tree has the following edges:

Edges from first spider: 1-2, 2-3.

Edges from second spider: 2-3 (second's 2 is merged into 2, so the edge becomes 2-3?), 2-4.

Wait, that's a bit confusing. Let me re-express.

Original first spider's edges: 1-2 and 2-3? Wait no. Wait the first input line is 3 1 2 2 3. So the edges are 1-2 and 2-3. So the first spider is a chain of 1-2-3. So its diameter is between 1 and 3, length 2.

Second spider's edges: 1-2, 2-3, 2-4. So the second spider is a star with 2 as the center. The diameter is between 3 and 4, which is a path of 2 steps (3-2-4). So diameter is 2.

When merging bead 2 of first spider (the middle node) with bead 1 of the second spider. Then the merged node is 2 (from first) and 1 (from second). So now, the merged tree's edges are:

From first spider: 2-1 (original first's 1-2?), 2-3 (original first's 2-3).

From second spider: 1 (merged) is connected to 2 (original second's 1-2?), but since 1 is merged into 2, that edge becomes 2-2 (which is a loop, but since the merged structure must be a tree, that's impossible. Wait, no. Wait, the second spider's edges after merging are: 2-3 (from second spider's 2-3?), and 2-4 (from second spider's 2-4?), and the original 1-2 of the second spider becomes 2-2 (since bead 1 is merged into 2). But that's a loop, which would not be allowed in a tree. Therefore, perhaps the merged structure is formed by taking all the edges of both trees, but with the merged nodes considered as the same. So the edges that were connected to the merged nodes in their original trees are now connected to the same node.

So for the first spider, edges are 1-2, 2-3.

For the second spider, edges are 1-2, 2-3, 2-4.

After merging the first's 2 and the second's 1, the merged node is called X. So the edges from the first spider are X connected to 1 and 3. The edges from the second spider are X connected to 2 (original second's 2?), and X connected to 3 and 4 (from the second spider's 2-3 and 2-4 edges). Wait, no. Because when merging the second spider's bead 1 into X, any edge that was connected to bead 1 in the second spider becomes connected to X.

So the second spider's edges after merging are:

Original edges: 1-2 (merged into X-2), 2-3 (becomes 2-3?), 2-4 (2-4).

Wait, I'm getting confused here. Let me think again.

Original second spider's edges:

1-2 (connecting bead 1 to 2), 2-3 (connecting bead 2 to 3), 2-4 (connecting bead 2 to 4).

After merging bead 1 (from the second spider) into bead 2 (from the first spider), which is now node X.

So in the merged tree, any occurrence of bead 1 in the second spider is replaced with X. So the edges of the second spider become:

X-2 (from 1-2), 2-3, 2-4.

But in the merged tree, the first spider's edges are X-1 (original 1-2), X-3 (original 2-3).

So the merged tree's edges are:

X connected to 1 (from first spider), X connected to 3 (from first), X connected to 2 (from second's 1-2 edge?), then 2 connected to 3 and 4 (from the second's edges).

Wait, but now node 2 from the second spider is a separate node. So the merged tree has nodes X (merged), 1, 3 (from first), 2 (from second), 3 (from second), 4 (from second). Wait, but that's possible. Wait, no. Because the beads in the second spider are numbered from 1 to 4. But after merging bead 1 into X, the bead 2 in the second spider is a separate node. So the merged tree's edges are:

- X connected to 1 (from first spider's edge 1-2, now X is the merged node).
- X connected to 3 (from first spider's edge 2-3, now X is 2).
- X connected to 2 (from the second spider's edge 1-2, now 1 is X).
- 2 connected to 3 (from second's 2-3).
- 2 connected to 4 (from second's 2-4).

So the merged tree has edges:

X-1, X-3, X-2, 2-3, 2-4.

So the merged tree's structure is:

X is connected to 1, 3, and 2. 2 is connected to 3 and 4.

So the longest path in this merged tree would be from 1 to 4. Let's calculate the distance.

Path from 1 to X (1 step), then X to 2 (1 step), then 2 to 4 (1 step). Total 3 steps. But the sample output is 4. Hmm, this is confusing. The sample output is 4. So perhaps I'm miscalculating the edges.

Alternatively, perhaps the merged structure is different. Let me re-express:

After merging bead 2 of the first spider (which is in the middle of 1-2-3) with bead 1 of the second spider (which is connected to bead 2 in the second spider), the merged tree's structure is:

The first spider's beads are 1, 2 (now merged), 3.

The second spider's beads are 1 (merged into 2), 2, 3, 4.

So the merged nodes are:

Original first spider's bead 2 and second spider's bead 1 are now the same node.

So in the merged tree, the edges are:

From first spider:

1 is connected to merged node (2).

merged node (2) is connected to 3.

From second spider:

merged node (1) is connected to 2 (original second's bead 2).

2 is connected to 3 and 4.

So the edges are:

1 - merged node.

merged node - 3.

merged node - 2 (from second's 1-2 edge).

2 - 3 (from second's 2-3).

2 -4 (from second's 2-4).

So the merged tree's structure is:

merged node connected to 1, 3, 2.

2 is connected to 3 and 4.

Now, the longest path would be from 1 (first spider) to 4 (second spider):

1 -> merged node (1 step), merged node ->2 (1 step), 2 ->4 (1 step). That's three steps. But sample output is 4. So something's wrong here.

But according to the sample explanation, the merged structure's diameter is 4. How is that possible?

Ah, perhaps I'm miscalculating the edges. Let me re-examine the sample input:

Second sample input:

The first spider is given by: 3 1 2 2 3. So the edges are (1-2), (2-3). So the first spider is a chain of 3 beads, with diameter between 1 and 3 (length 2).

The second spider is 4 1 2 2 3 2 4. So the edges are (1-2), (2-3), (2-4). So the second spider is like a star, with 2 as the center. The diameter here is between 3 and 4 (path 3-2-4, length 2). So each spider's diameter is 2.

When merged by bead 2 of first and bead 1 of second. So the merged node is the bead 2 from first (which is connected to 1 and 3) and bead 1 from second (connected to 2). So after merging, the merged node has edges:

From first spider: 1 and 3.

From second spider: 2 (since bead 1 is merged into bead 2 of first).

So in the merged tree, the edges are:

For the first spider: 1-merged node, merged node-3.

For the second spider: merged node (as bead 1) connected to 2, and 2 connected to 3 and 4.

So the merged tree has edges:

merged node connected to 1, 3, 2 (from second spider's 1-2 edge, now merged node is the 1 in that edge, so merged node connected to 2).

Then, 2 is connected to 3 and 4 (from the second spider's edges).

So the merged tree's structure is:

merged node is connected to 1, 3, 2.

2 is connected to merged node, 3, 4.

Now, the path from 3 (from first spider) to 4 (second spider) is:

3 - merged node (1 step), merged node - 2 (1 step), 2 -4 (1 step). Total 3 steps. But the sample output is 4.

Wait, this is not making sense. The sample output is 4. So where is the path of length 4?

Alternatively, perhaps the merged structure has a longer path. Let's see:

Looking for the longest path in the merged tree.

Possible paths:

1. From 1 (first spider) to 4 (second): 1 -> merged node (1) ->2 (1) ->4 (1). Length 3.

2. From 3 (first spider) to 4: 3 -> merged node (1) ->2 (1) ->4 (1). Length 3.

3. From 3 (first) to 3 (second): 3 (first) -> merged node (1) ->2 (1) ->3 (second). Length 3.

4. From 1 to 3 (second): 1 -> merged node (1) ->2 (1) ->3 (second). Length 3.

Hmm, but none of these are longer than 3. But the sample output is 4.

Ah! Wait, maybe there's another path. Wait, the merged tree's edges are:

merged node (M) connected to 1, 3 (from first spider), and 2 (from second spider).

2 is connected to M, 3 (from second spider), and 4.

So the merged tree's structure is:

M is connected to 1, 3, 2.

2 is connected to M, 3, 4.

So the tree looks like this:

M
|
1
|
M is connected to 3 (from first spider)
|
M is connected to 2 (from second spider)
|
2 is connected to 3 (from second) and 4.

So, the path from 1 (first spider) to 3 (second spider):

1 -> M ->2 ->3. That's 3 steps.

But what about the path from 1 to the other 3 (from first spider) to 4?

Wait, maybe the longest path is from 1 (first) to 4 (second), via M and 2. That's 3 steps. But where's the 4 steps?

Alternatively, perhaps the merged tree has a longer path. Let me think again.

Wait, maybe the merged tree's diameter is between 3 (first spider) and 4 (second spider). Let's see:

The path is 3 (first) -> M ->2 ->3 (second) ->4. No, that's not possible. Because 3 (second) is connected to 2, and 2 is connected to M.

Wait, another possibility: 1 -> M ->3 (from first spider) -> M ->2 ->4. Wait, but M is a single node. So the path from 1 to 3 (first) is direct via M (length 1 each way). Then from M to 2 to 4 (length 2). So total 1 (1-M) + 2 (M-2-4) = 3. No.

Hmm. Maybe I'm missing something here. The sample output is 4. So how is that possible?

Ah, perhaps when merging the spiders, the way of connecting them allows for a longer path. Let's re-express the merged tree.

Maybe after merging, the merged node is part of both spiders' structures. For example, in the merged tree, the path from the first spider's 1 to the second spider's 4 is:

1 -> merged node (M) ->3 (from first spider) -> M (again?) No, that's a loop.

Alternatively, perhaps the merged tree is a different structure. Let's re-express the merged tree's edges.

Wait, perhaps the merged tree's edges are:

M (from first spider's 2 and second's 1) is connected to 1 (from first), 3 (from first), and to 2 (from second's 1-2 edge). Then, 2 (from second) is connected to 3 (from second's 2-3 edge) and 4 (from 2-4). 3 (from second) is connected to 2 (from second), but not to M.

So the merged tree has the following nodes:

M, 1, 3 (first), 2 (second), 3 (second), 4 (second).

So the merged tree's edges are:

M-1, M-3 (first), M-2 (second), 2-3 (second), 2-4 (second).

In this case, the path from 3 (first) to 4 (second) is: 3 (first) -> M ->2 (second) ->4 (second): length 3.

But what about the path from 3 (first) to 3 (second): 3 (first) -> M ->2 (second) ->3 (second). Length 3.

Or from 1 to 3 (second): 1 -> M ->2 ->3: length 3.

But sample output is 4. So where is the path of length 4?

Ah! Maybe there's a longer path that I'm missing. For example, perhaps the path from 1 (first) to 4 (second) is longer than 3 steps. Let's see:

1 -> M (1 step) -> 3 (first) (1 step). Then from 3 (first) to M to 2 (second) to 4. That's 1+1+1+1=4 steps. Wait, but that's a cycle. So that's not allowed in a tree. So that path is invalid.

Alternatively, perhaps the merged tree has a different structure. Maybe the merging process allows for a longer path. Let me think of another approach.

Alternative approach: For each spider, compute its diameter. Then, the maximum possible merged diameter is the sum of all the diameters of the individual spiders plus the number of spiders minus 1. Because when you connect each spider's diameter end to end, each connection adds 1 (the merged node). So for two spiders, sum of diameters (d1 + d2) + 1? Or no. Wait, in the first sample, merging two spiders (d1=2, d2=2) gives a merged diameter of 4. Which is d1 + d2. So that's 2+2=4. So that's the sum. So in that case, the sum of the two diameters is the merged diameter.

So the approach for the problem is:

- For each spider, compute its diameter.

- The maximum possible merged diameter is the sum of the two largest diameters plus the sum of the other diameters.

Wait, no. Because if there are more than two spiders, how do they contribute?

Alternatively, when merging multiple spiders, the maximum possible diameter is the sum of the two largest diameters, plus the sum of the other spiders' radii (ceil(diameter/2)).

Wait, perhaps not. Let's think with an example.

If there are three spiders with diameters 4, 4, and 4. Then the sum of the two largest is 8. Then, the third spider has radius 2. So the total would be 8 + 2 = 10. But if we connect all three in a chain by their endpoints, then the merged diameter would be 4+4+4=12. Which is better. So that approach is incorrect.

Alternatively, maybe the correct approach is to connect all spiders in a chain, connecting the endpoints of their diameters. For example, for spiders A, B, C, connect the end of A's diameter to the start of B's diameter, then the end of B's to the start of C's. Then the merged diameter is sum of all diameters. But if there are more than two spiders, how does this work?

Wait, if there are three spiders each with diameter 2 (like chains of 3 nodes), and we merge them in a chain by their endpoints, the merged tree would be a chain of 3+3+3-2 nodes (since merging endpoints reduces the total nodes). Wait, but in reality, each merge of two endpoints combines two nodes into one. So the total length would be 2 + 2 + 2 = 6 steps. Because the path would be from the first end of the first spider's diameter, through all merged nodes, to the last end of the third spider's diameter.

So, for n spiders, each with diameter d_i, the maximum merged diameter is sum(d_i) + (n-1)*0? Because merging the endpoints directly connects the diameters, so each merge adds nothing. Because the merged node is part of both diameters, so the sum of the individual diameters is the merged diameter.

Wait, for example, two spiders with diameters 2 and 2. Merging endpoints gives a merged diameter of 2+2=4. Which matches the second sample. So the formula would be sum of all individual diameters. But that can't be right for three spiders. Let's take three spiders with diameters 2 each. Merging them end to end would give a merged diameter of 2+2+2=6. But according to that approach, the sum is 6. Is that correct?

Yes. For example, three spiders: each is a chain of three nodes. Merging them in a line by endpoints. So the first spider is A-B-C. The second is X-Y-Z. The third is P-Q-R. Merge C and X. Merge Z and P. The merged tree's longest path is A-B-C (merged with X) -Y-Z (merged with P) -Q-R. The path from A to R is 6 steps (A-B-C is 2 steps, C to X is merged (no step), X-Y-Z is 2 steps, Z-P is merged (no step), P-Q-R is 2 steps. So total 2+2+2 =6 steps. So yes, the merged diameter is 6.

So in this case, the sum of the individual diameters is 6. So the approach of summing all the individual diameters would work. But wait, what if there's a spider with a large diameter that is not connected in a way that contributes to the longest path.

For example, three spiders: two with diameter 4, and one with diameter 2. Merging the two larger ones first, then adding the smaller one. The merged diameter would be 4+4 +2 =10. But is that possible?

Yes, if merged in a chain. But if the third spider's diameter is added by merging to one of the endpoints, then the longest path would include all three diameters.

But maybe there's a scenario where the maximum is the sum of the two largest diameters, and the others do not contribute. For example, if you have three spiders with diameters 5, 4, and 3. The sum of all three is 12, but maybe the maximum path is 5+4=9. But merging them in a chain would give 5+4+3=12, which is better.

So the maximum possible merged diameter is the sum of all individual diameters. But this can't be correct because in the second sample, the sum of the two diameters is 2+2=4, which matches the sample output.

But how can this approach handle the first sample, where there is one spider. Then the sum is its diameter, which matches.

Another example: if there are two spiders, one with diameter 3 and another with diameter 5. Merging them via their endpoints would give a diameter of 3+5=8.

So according to this approach, the correct answer is the sum of all individual diameters. But wait, why does that work?

But what if we have two spiders with diameters d1 and d2. The maximum possible merged diameter is d1 + d2. Because we can connect the two diameters end to end. So the merged path is the concatenation of the two diameters, which is their sum.

But then why in the second sample, the two diameters are 2 each, sum is 4, which matches the sample output.

But what about the case where merging the spiders in a different way results in a longer path?

For example, spider 1 has diameter 4 (path A-B-C-D), spider 2 has diameter 3 (path X-Y-Z). Merging spider 1's B (which is in the middle) with spider 2's Y (also in the middle). The merged path would be A-B-C-D (length 3) plus B-Y-Z (length 2) → total 5. But if we merge the endpoints (D and X), the merged path would be A-B-C-D-X-Y-Z (length 6 steps). Which is larger. So merging endpoints is better.

So the optimal way to merge spiders is to connect their diameters end to end. So the sum of the individual diameters is the maximum possible merged diameter.

But how do you do this when there are more than two spiders?

For example, three spiders with diameters d1, d2, d3. Merge them in a chain: connect spider 1's end to spider 2's start, then spider 2's end to spider 3's start. The merged diameter is d1 + d2 + d3.

But wait, each merge combines two nodes. So when you merge spider 1's end (node D) with spider 2's start (node X), the combined node is D/X. Then the merged path from spider 1's start (A) to spider 2's end (Z) is d1 + d2. Then merging spider 2's end (Z) with spider 3's start (P), the merged path from A to spider 3's end (R) is d1 + d2 + d3.

Yes. So the total is sum of all diameters.

But this requires that all spiders are connected in a chain by their diameter endpoints. So each spider's diameter is connected end to end with the next.

So the algorithm would be to compute the sum of all the individual diameters of the spiders. But wait, sample input 2's sum is 2+2=4, which matches. But the first sample input's sum is 2, which matches.

But what about a case where merging in a different way gives a larger sum?

Suppose there are two spiders. Spider 1 has a diameter of 3 (path A-B-C-D), spider 2 has a diameter of 4 (path X-Y-Z-W). Merging the end of spider 1's diameter (D) with the end of spider 2's diameter (W). The merged path is A-B-C-D-W-Z-Y-X. The length is 3 +4 =7. But if we merged the end of spider 1's diameter (D) with the start of spider 2's diameter (X), then the merged path is A-B-C-D-X-Y-Z-W, length 3+4=7. Same result.

So regardless of how the diameters are connected end to end, the sum is the same.

But what if there are three spiders. For example, spider 1 has diameter 1 (path A-B), spider 2 has diameter 1 (C-D), spider 3 has diameter 1 (E-F). Merging in a chain, the merged diameter would be 1+1+1=3. Which is the sum.

But if we merge all three into a star, connecting all to a central node, the diameter would be 2 (like A-B merged with C, merged with E-F). The path from A to F would be A-B (merged node) - E-F. Length 2. So in that case, the sum approach is better.

So the maximum possible merged diameter is the sum of all individual diameters.

Wait, but this seems to contradict the first approach where merging by centers could give a different result. So which is correct?

But according to the sample inputs, the sum of the diameters is the correct approach.

But wait, what if we have a spider with a very long diameter and another with a small one. For example, spider 1 has diameter 10, spider 2 has diameter 2. Merging them end to end gives a diameter of 12, which is better than any other way of merging.

So the approach is to compute the sum of all individual diameters.

But how to handle the case when there are multiple spiders. For example, three spiders with diameters 2, 2, and 2. Summing gives 6, which would be correct.

But wait, in this case, merging all three end to end would create a path of 6 steps.

So the correct answer is the sum of all individual diameters.

So the algorithm is to compute for each spider its diameter, then sum all those diameters.

But wait, what about the third sample input?

Third sample input:

2

5 1 2 2 3 3 4 3 5

7 3 4 1 2 2 4 4 6 2 7 6 5

The first spider's edges are:

1-2, 2-3, 3-4, 3-5.

So it's a tree where node 3 is connected to 2, 4,5. Node 2 is connected to 1. The diameter is the longest path. Let's compute it.

The longest path would be between 1 and 4 (path 1-2-3-4: length 3), or 1 and 5 (1-2-3-5: length 3), or 4 and 5 (4-3-5: length 2). The diameter is 3.

The second spider's edges are:

3-4, 1-2, 2-4, 4-6, 2-7, 6-5.

Let's parse this. The edges are:

3 connected to 4.

1 connected to 2.

2 connected to 4.

4 connected to 6.

2 connected to 7.

6 connected to 5.

So the tree structure is:

- 4 is connected to 3, 2, 6.

- 2 is connected to 1, 7.

- 6 is connected to 5.

The diameter would be the longest path. Let's find it.

Possible paths:

1-2-4-6-5: length 4.

7-2-4-6-5: length 4.

3-4-6-5: length 3.

So the diameter is 4.

So sum of the two diameters is 3+4=7, which matches the sample output of 7. So the third sample's output is indeed the sum of the individual diameters.

So this suggests that the correct approach is to compute the sum of all individual diameters.

But how does this work when there are more than two spiders?

Let's take an example with three spiders:

Sample input:

3

3 1 2 2 3

3 4 5 5 6

3 7 8 8 9

Each spider has a diameter of 2. The sum is 2+2+2=6. The merged diameter would be 6.

But when merged as a chain, the merged tree's diameter is 6.

Yes.

So the solution is to compute the sum of all individual diameters of the spiders.

Thus, the steps for the solution are:

1. For each spider, compute its diameter.

2. Sum all the diameters.

3. Output that sum.

Thus, the problem reduces to computing the diameter of each spider and summing them.

So now, the key part is to compute the diameter of each tree (spider) efficiently.

The diameter of a tree can be found using BFS twice. The steps are:

1. Pick any node, find the farthest node u from it.

2. Find the farthest node v from u. The distance between u and v is the diameter.

So for each spider, we need to build its adjacency list, then perform two BFS passes to compute the diameter.

Given that each spider can have up to 100 nodes, and there are up to 100 spiders, the total computations are manageable.

Now, the code steps:

Read n.

For each spider:

   Read ni, followed by ni-1 pairs of beads (edges). Each edge is undirected.

   Build the adjacency list.

   Compute the diameter of this tree.

Sum all diameters.

Output the sum.

Now, the code in Python.

But to build the adjacency list, since the nodes are numbered from 1 to ni for each spider. So each spider's nodes are 1-based.

Now, for each spider, build the adjacency list. Then perform two BFS to find the diameter.

Let's code this.

The code for BFS to find the farthest node:

def bfs(start, adj):

    from collections import deque

    visited = {start: 0}

    q = deque([start])

    while q:

        u = q.popleft()

        for v in adj[u]:

            if v not in visited:

                visited[v] = visited[u] + 1

                q.append(v)

    max_dist = max(visited.values())

    far_node = [k for k, v in visited.items() if v == max_dist][0]

    return far_node, max_dist

Then, the diameter is computed as:

def compute_diameter(adj):

    u, _ = bfs(1, adj)

    v, max_dist = bfs(u, adj)

    return max_dist

Wait, but the first BFS starts from any node (like 1), finds the farthest node u. Then BFS from u finds the farthest node v, the distance between u and v is the diameter.

Yes.

So the code for each spider is:

Build adjacency list.

Call compute_diameter(adj) to get the diameter.

Sum all diameters.

Thus, the code is:

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    total = 0

    for _ in range(n):

        parts = list(map(int, input_stream.readline().rstrip("\n").split()))

        ni = parts[0]

        edges = parts[1:]

        adj = [[] for _ in range(ni+1)]

        for i in range(0, len(edges), 2):

            a = edges[i]

            b = edges[i+1]

            adj[a].append(b)

            adj[b].append(a)

        # Compute diameter

        def bfs(start):

            from collections import deque

            visited = {start: 0}

            q = deque([start])

            while q:

                u = q.popleft()

                for v in adj[u]:

                    if v not in visited:

                        visited[v] = visited[u] + 1

                        q.append(v)

            max_dist = max(visited.values())

            far_node = max(visited, key=lambda x: visited[x])

            return far_node, max_dist

        u, _ = bfs(1)

        v, max_dist = bfs(u)

        total += max_dist

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
5 1 2 2 3 3 4 3 5
7 3 4 1 2 2 4 4 6 2 7 6 5
""",
            "output": \
"""\
7
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

Wait, wait, the sample input for the second spider is:

4 1 2 2 3 2 4 → edges are (1,2), (2,3), (2,4).

So adj for spider 2 is:

1: [2]

2: [1, 3,4]

3: [2]

4: [2]

BFS from 1:

Farthest node is 3 or 4, distance 2.

BFS from 3:

Farthest node is 4 (path 3-2-4, distance 2). So diameter is 2.

But according to this code, the diameter of the second spider would be 2. Sum of diameters is 2+2=4, which matches the sample output. So the sample is correct.

But earlier analysis suggested that the second spider's diameter is 2, which is correct. So the code works.

In the third sample input, the first spider has a diameter of 3, the second of 4, sum 7.

Thus, the code is correct.
</think>

```python
import sys
from collections import deque

def compute_diameter(adj):
    def bfs(start):
        visited = {start: 0}
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in visited:
                    visited[v] = visited[u] + 1
                    q.append(v)
        max_node = max(visited, key=lambda x: visited[x])
        return max_node, visited[max_node]
    
    node, _ = bfs(1)
    node, max_dist = bfs(node)
    return max_dist

n = int(sys.stdin.readline())
total = 0
for _ in range(n):
    parts = list(map(int, sys.stdin.readline().split()))
    ni = parts[0]
    edges = parts[1:]
    adj = [[] for _ in range(ni + 1)]
    for i in range(0, len(edges), 2):
        a, b = edges[i], edges[i+1]
        adj[a].append(b)
        adj[b].append(a)
    total += compute_diameter(adj)

print(total)
```
