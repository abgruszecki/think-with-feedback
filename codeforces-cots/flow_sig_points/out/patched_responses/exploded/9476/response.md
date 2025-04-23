<think>
Okay, so I need to solve this problem where I have to determine for each road whether it's part of all possible shortest paths from s to t. If not, can we repair it (reduce its length) in such a way that it becomes part of all shortest paths, and find the minimal cost (which is the original length minus the new length, but the new length has to be at least 1). Otherwise, output NO.

First, let's understand the problem step by step.

Each road can be in one of three categories:
1. Definitely used in all shortest paths: output YES.
2. Not used in all, but can be adjusted (by reducing its length) so that all shortest paths must use it: output CAN followed by the minimal cost (which is original length minus the new length, which is as large as possible but still making it required).
3. Even after reducing, it's not possible: output NO.

So for each edge (a, b, l), we need to check if it's on any of the shortest paths. If it is not, then check if there's a way to adjust l to l' (with l' >= 1) such that in the modified graph, every shortest path from s to t must include this edge. The cost is l - l', and we want the minimal possible, which would correspond to the maximum possible l' such that the edge is required.

But how to approach this?

First, compute the shortest distances from s to all nodes (d_s) and from all nodes to t (d_t). Because for any edge (a, b, l) to be on a shortest path, it must satisfy d_s[a] + l + d_t[b] = d_s[t]. Otherwise, it's not part of any shortest path.

So, the first step is to compute d_s and d_t. Then, for each edge, check if d_s[a] + l + d_t[b] == d_s[t]. If not, then even after repair, this edge can't be part of any shortest path, so it's in the NO category.

Wait, no. Because if we reduce l, then maybe d_s[a] + new_l + d_t[b] becomes equal to the new shortest path. But how?

Wait, the overall shortest path after repair might be lower. So the approach here is that after repairing the edge, we want the new edge's (a, b, l') to be such that in the new graph, the shortest path from s to t must go through this edge.

But this seems complicated. Let's think again.

The edge (a, b, original l) can be considered for repair. Let's say the current distance from s to t is D. If we change the edge's length to l', then the new shortest path could be D_new. For this edge to be required, any path from s to t must go through this edge, and the sum d_s[a] + l' + d_t[b] = D_new. Also, D_new must be the minimal possible.

But how to compute this?

Alternatively, the idea is: For the edge (a, b) to be on every shortest path after repair, two conditions must hold:

1. The new length l' must be such that d_s[a] + l' + d_t[b] is the new shortest path (so D_new = d_s[a] + l' + d_t[b]).
2. All other possible paths from s to t (without using this edge) must have a length >= D_new. But since D_new is the sum of the original shortest paths from s to a, plus l', plus from b to t, maybe the only way this can be possible is if l' is set such that D_new is less than or equal to any other possible path that doesn't go through (a, b).

Wait, but this is getting a bit complicated. Let me think differently.

The original shortest path distance is D = d_s[t].

For the edge (a, b) to be part of all shortest paths after repair, any path from s to t that doesn't use this edge must have a length >= the new distance. The new distance would be d_s[a] + l' (the new length) + d_t[b]. So to force all paths to include (a, b), this new sum must be strictly less than the original D (since if we reduce l, the sum could be less than D, but then the new D becomes the new sum. But other paths could have even shorter lengths. Wait, but if we repair the edge (a, b), but other paths might not be affected. So perhaps, the way to make sure that (a, b) is in every shortest path is to make the sum d_s[a] + l' + d_t[b] equal to the new shortest path, and that any other path from s to t (without this edge) has a length greater than or equal to this sum.

But how can we compute that?

Alternatively, the minimal possible new sum is when l' is as small as possible (1), but perhaps even then, the sum (d_s[a] + 1 + d_t[b]) might not be less than the original D. Wait, no. Because if we reduce the length of (a, b), then the new shortest path could be shorter. So the original D is d_s[t], but after repair, the new shortest path would be the minimum between D and (d_s[a] + l' + d_t[b]).

So for the edge (a, b) to be part of all shortest paths after repair, the sum d_s[a] + l' + d_t[b] must be equal to the new shortest path. Additionally, any other path from s to t (without this edge) must have a length >= this sum.

But how to model this?

Hmm. Let me think of the original distances.

In the original graph, the shortest path is D. For the edge (a, b) to be part of all shortest paths after repair, the sum (d_s[a] + l' + d_t[b]) must be <= the minimal possible new shortest path. But since we can't control other edges, the only way to make sure that this edge is in all shortest paths is that any path not using (a, b) has length >= (d_s[a] + l' + d_t[b]).

So, let me define:

current_edge_contribution = d_s[a] + l + d_t[b]

If current_edge_contribution > D, then even after reducing l, the edge can't be part of any shortest path. Because for l' < l, the new contribution is d_s[a] + l' + d_t[b]. If this new contribution is less than D, then the new shortest path would be this value, and the edge is part of some shortest path. But other paths that have length D (original shortest) would still exist. So unless the new contribution is less than D, but then the new shortest path would be this new value, and any path that uses this edge would have that length, but other paths (original ones) would have length D. So to have the edge be in all shortest paths, the new contribution must be <= D, and also all other paths (not using this edge) must have lengths >= new contribution.

Wait, no. Because if the new contribution is less than D, then the new shortest path is new_contribution. So any path that uses the edge (a, b) would contribute to the shortest path. But other paths that were part of the original shortest path (length D) would now have a longer length than the new_contribution. So, in that case, all shortest paths must go through (a, b). Because any path that doesn't use this edge would have a length >= D (original D is the shortest, but now the new shortest is even shorter). But wait, how?

Wait, if the new contribution (d_s[a] + l' + d_t[b]) is less than D, then the new shortest path is new_contribution. So any path that doesn't go through (a, b) would have length >= D (since D was the original shortest). But D is larger than new_contribution. So those paths cannot be part of the new shortest path. Therefore, all shortest paths in the new graph must use this edge (a, b).

So for such a case, repairing the edge (a, b) by reducing l to l' (so that new_contribution is less than D) would make all shortest paths include (a, b).

But in this case, the minimal cost is l - l', and l' must be as large as possible (since cost is minimized when l' is maximized). Wait, no. Because cost is the difference between original l and new l'. So to minimize the cost (since the problem says to output the minimal cost), we need l' as close to original l as possible. Wait, wait. The minimal cost is the minimal possible difference (because cost is original l minus new l', and we want to minimize this cost). Wait no, wait: the cost is l - l', which is the amount we have to reduce. So to find the minimal cost, we need the maximum possible l' such that the new_contribution (d_s[a] + l' + d_t[b]) is less than the original D. Because that gives the largest possible l' (so l - l' is minimized) such that the new_contribution is < D.

So the optimal l' is the maximum possible value such that d_s[a] + l' + d_t[b] < D. Then, the cost is l - l'.

But l' must be >=1. So for this to be possible, we need that:

d_s[a] + 1 + d_t[b] < D.

So the steps for each edge (a, b, l):

If the edge is already in some shortest path (i.e., d_s[a] + l + d_t[b] == D):

   Then, we need to check if it's in all shortest paths. If it's not, then the answer is NO for this edge. Wait, no. Wait, if the edge is on some shortest path, but not all, then the answer is not YES, but may be CAN if we can repair.

Wait, no. The first condition for outputting YES is that the edge is present in all shortest paths. So even if the edge is on a shortest path (d_s[a] + l + d_t[b] == D), but there exists another shortest path that doesn't use this edge, then the answer is not YES. So how do we check if the edge is in all shortest paths?

Ah, right. So for the edge to be in all shortest paths, any shortest path must use this edge. So even if d_s[a] + l + d_t[b] == D, if there is a way to go from a to b through other roads (but not this edge) and still get the same total distance, then the edge isn't required.

So how to check whether the edge is in all shortest paths?

This is tricky. Because even if the edge is part of some shortest path, it's possible that there are other paths from s to t that don't use this edge but are also of length D.

So to check if the edge is in all shortest paths, perhaps the edge is a necessary part of all possible paths. How?

One approach is: For edge (a, b, l), the edge is on all shortest paths if and only if the number of shortest paths from s to a multiplied by the number of shortest paths from b to t is equal to the total number of shortest paths from s to t.

But that's only possible if all shortest paths go through a -> b. But even this might not be correct.

Alternatively, perhaps we can compute for each node u, the distance from s to u (d_s[u]) and the distance from u to t (d_t[u]). Then, an edge (a, b, l) is on some shortest path if d_s[a] + l + d_t[b] == D. But to check if it's on all shortest paths, perhaps the edge is a "bridge" in the DAG of shortest paths.

But how to compute that?

Another approach: If the edge (a, b, l) is on all shortest paths, then any path from s to t must pass through this edge. This is equivalent to the edge (a, b) being the only way to reach t from a in the shortest path structure.

Alternatively, the edge (a, b) is on all shortest paths if and only if:

d_s[a] + l == d_s[b], and

d_t[b] + l == d_t[a] (no, this isn't right, because d_t is the distance from b to t, not the other way around).

Wait, no. The distance from s to b must be d_s[a] + l. Because if the edge (a, b) is on a shortest path, then d_s[b] = d_s[a] + l. But if there's another way to reach b with the same distance, then the edge (a, b) is not on all shortest paths.

So for the edge (a, b) to be on all shortest paths, two conditions must hold:

1. d_s[a] + l == d_s[b] (so that using this edge gives the shortest path to b).
2. d_t[b] + l == d_t[a] (so that to reach t from a, you have to go through this edge and then from b to t).

Wait, maybe not. Let's think again.

For the edge (a, b) to be on every s->t shortest path, the path must go through a -> b. So:

s to a is part of the path, then a to b via this edge, then b to t.

So, the distance from s to t is d_s[a] + l + d_t[b] = D.

But for this edge to be on all paths, there must be no other way to get from s to a, then to a node that can reach t in a way that sum up to D. Wait, maybe this is not the right way to model it.

Alternatively, if the edge (a, b) is part of all shortest paths, then removing it would increase the shortest path distance. So, if after removing the edge (a, b), the shortest path from s to t becomes longer than D, then the edge is on all shortest paths. But this approach is computationally expensive for large n and m.

But with n up to 1e5 and m up to 1e5, we can't do this for each edge.

So, perhaps another approach is needed.

Let me think. For the edge (a, b) to be in all shortest paths, the sum d_s[a] + l + d_t[b] = D (so it's on some shortest path) and also, any path from s to t must go through a -> b. So, the edge is a "bridge" in the DAG formed by the shortest paths.

But how to determine this.

Alternatively, in the DAG of the shortest paths, each edge (u, v, w) with d_s[u] + w == d_s[v], and the DAG consists of all such edges. Then, the edge (a, b) is on all paths from s to t if and only if every path from s to t in this DAG must pass through (a, b).

This can be checked by seeing if (a, b) is a bridge in the DAG. But finding all such bridges is computationally intensive for large n and m.

An alternative approach is to precompute the number of shortest paths from s to each node, and the number of shortest paths from each node to t. Then, for an edge (a, b) to be part of all shortest paths, the product of the number of shortest paths from s to a and from b to t must equal the total number of shortest paths from s to t. But this only holds if there are no other edges contributing to the shortest paths. However, this approach is not feasible when the number of paths is large (exponential, which is possible even for small n), so we need to use modulo arithmetic, but even that might be complicated.

Given the time constraints, perhaps we can't compute this exactly. So maybe the problem expects that the YES case is determined by the edge (a, b) being part of all possible shortest paths if and only if d_s[a] + l + d_t[b] == D, and all paths from s to a and from b to t are such that their edges are part of the shortest paths.

Wait, maybe that's not the case. For example, there might be multiple paths from s to a, but as long as the edge (a, b) is the only way to reach t from a, then all paths must go through a->b. But how to model that.

Hmm. It's getting complicated.

Alternative plan:

1. Compute d_s (shortest distances from s to all nodes) using Dijkstra's algorithm.

2. Compute d_t (shortest distances from all nodes to t). For this, reverse the graph and run Dijkstra's from t.

3. For each edge (a, b, l), check if d_s[a] + l + d_t[b] == D, where D is the original shortest path length (d_s[t]).

   a. If not, then this edge can't be part of any shortest path. So, check if it can be repaired.

   b. If yes, then check if this edge is part of all possible shortest paths. If yes, output YES. If not, then see if we can repair it.

But how to check if it's part of all possible shortest paths?

For (a, b) to be part of all shortest paths, any path from s to t must go through a->b. So, in the DAG formed by the shortest path edges (edges where d_s[u] + w == d_s[v]), the edge (a, b) must be the only way to reach some part of the graph.

Alternatively, the edge (a, b) must be such that there is no other path from a to b that doesn't include this edge and has a total length of d_s[a] + l.

But again, how to compute this efficiently.

Wait, but perhaps the edge (a, b) is not on all shortest paths if there exists another edge (a, c, l') such that d_s[a] + l' + d_t[c] == D. Or, maybe other nodes that can be used to reach t.

Alternatively, perhaps the edge (a, b) is part of all shortest paths if and only if:

d_s[a] + l == d_s[b], and

d_t[b] + l == d_t[a]

Wait, not sure. Let's see.

If d_s[a] + l == d_s[b], then the edge (a, b) is on some shortest path to b. Then, for this edge to be part of all paths from s to t, perhaps the path from a to t must go through b. So, d_t[a] = l + d_t[b]. If this is the case, then any path from a to t must go through b, which would imply that the edge (a, b) is required.

So, for the edge (a, b) to be required in all shortest paths, the following two conditions must hold:

d_s[a] + l == d_s[b]

d_t[b] + l == d_t[a]

Because this means that to reach b from s, you have to go through a and this edge (as it's the shortest path to b). Also, to reach t from a, you have to go through this edge (since the shortest path from a to t is l + d_t[b]).

If both conditions are true, then the edge is on all shortest paths.

But wait, this might not capture all cases. For example, suppose there's another path from a to b that is part of a different shortest path. But the edge (a, b) is part of the shortest path, but there's another way.

Alternatively, this approach might capture the necessary and sufficient conditions for the edge to be on all shortest paths.

Let's test with the first sample input.

Sample input 1:

6 7 1 6

Edges:

1 2 2

1 3 10

2 3 7

2 4 8

3 5 3

4 5 2

5 6 1

The shortest path from 1 to 6 is 1->2->4->5->6 (sum 2+8+2+1=13) and 1->2->3->5->6 (2+7+3+1=13). So D=13.

For the first edge (1,2,2):

d_s[1] is 0, d_s[2] is 2. So 0+2=2 = d_s[2]. Also, d_t[2] is the distance from 2 to 6. The shortest path from 2 to 6 is via 4->5->6: 8+2+1=11, or 3->5->6: 7+3+1=11. So d_t[2] = 11. The distance from 1 to 2 is 2. So d_t[2] + l (2) is 11 + 2=13, which equals d_t[1] (distance from 1 to 6 is 13). So the two conditions are met: d_s[a] + l = d_s[b], and d_t[b] + l = d_t[a]. So the edge (1,2,2) is required on all shortest paths. Hence output YES.

But in the sample output, the first line is YES, which matches.

Another example: the second edge (1,3,10). d_s[1] is 0, l=10. d_s[3] is 9 (since 1->2->3 is 2+7=9). So 0+10=10>9. So this edge is not part of any shortest path. So for this edge, can we repair it?

The original D is 13. For this edge to be part of the new shortest paths, we need to reduce its length l' such that d_s[1] + l' + d_t[3] < 13. d_s[1] is 0, d_t[3] is 3 +1 =4 (3 to 5 to 6). So 0 + l' +4 <13 => l' <9. Original l is 10. So l' can be up to 8 (since l' must be >=1). The cost is 10-8=2. So output CAN 2. Which matches the sample output.

So, for this edge, the minimal cost is 2.

But how do we compute this in code.

So, the approach for each edge is:

Compute d_s and d_t.

D = d_s[t]

For each edge (a, b, l):

Case 1: The edge is part of some shortest path (d_s[a] + l + d_t[b] == D).

   Check if the edge is part of all shortest paths. If yes: output YES.

   Else: output CAN with some cost. Wait, no. Wait, if the edge is part of some but not all shortest paths, then it's possible that even without repair, the edge is used sometimes. But the problem asks whether the president will definitely pass through it. So if it's not in all shortest paths, then the answer is not YES, but perhaps CAN or NO.

Wait, in this case, the edge is part of some shortest paths. So the president may or may not use it, depending on the path chosen. So the answer for this edge is not YES. So in this case, can we repair it so that it is required in all shortest paths?

But how?

Wait, in this case, the edge is part of some shortest paths, but not all. So, the original answer for the edge is not YES. So, for the answer to be YES, the edge must be required in all shortest paths. Otherwise, the answer is either CAN or NO.

So, for the edge that is part of some shortest paths (d_s[a] + l + d_t[b] == D), but not all, we need to check if there is a way to repair it such that after repair, the edge is part of all shortest paths.

But how?

If we reduce the length of the edge to l', then the new contribution is d_s[a] + l' + d_t[b] = D_new.

To have this edge required in all shortest paths, D_new must be the new shortest path, and all other paths (not using this edge) must have length >= D_new.

But how to compute this?

Alternatively, after repair:

D_new = min(D, d_s[a] + l' + d_t[b])

But to ensure that all shortest paths include the edge (a, b), we need D_new = d_s[a] + l' + d_t[b], and this D_new must be strictly less than the original D. Because then, any path not using this edge would have length >= original D (since D was the shortest path before repair), which is longer than D_new. Hence, all shortest paths must use the edge.

So the condition for being able to repair is that d_s[a] + d_t[b] + l' < D, and l' >=1.

The maximum possible l' that satisfies this is l' = min( l-1, (D -1 - d_s[a] - d_t[b]) )

But we can write:

required_l' = D - d_s[a] - d_t[b] - 1

But since l' must be >=1, required_l' must be >=1. So:

if (d_s[a] + d_t[b] +1) < D, then required_l' = D - d_s[a] - d_t[b] -1.

But this required_l' must be <= l-1 (since the original l is larger than required_l'), but also >=1.

Wait, let's see:

We need d_s[a] + l' + d_t[b] < D.

=> l' < D - d_s[a] - d_t[b]

The maximum possible l' is (D - d_s[a] - d_t[b] -1).

But l' must be >=1 and <= l-1 (since we can reduce the length).

So the minimal cost is l - l', where l' is the maximum possible between 1 and (D - d_s[a] - d_t[b] -1), but also <= l-1.

So for this to be possible, the following must hold:

D - d_s[a] - d_t[b] -1 >=1

=> D - d_s[a] - d_t[b] >=2

Which means d_s[a] + d_t[b] <= D -2.

In this case, the maximum l' is D -d_s[a] -d_t[b] -1.

But also, l' must be <= l-1. So:

allowed_l' = min( l-1, D -d_s[a] -d_t[b] -1 )

If allowed_l' >=1, then possible to repair. The cost is l - allowed_l'.

Else, not possible.

So for edges that are part of some shortest paths (d_s[a] + l + d_t[b] == D), but not all, we can check if D -d_s[a] -d_t[b] -1 >=1 (i.e., d_s[a] + d_t[b] +1 < D) and allowed_l' >=1. If so, then output CAN and the cost. Else, NO.

But how to check if the edge is part of all shortest paths.

Ah, right. For the edge to be part of all shortest paths, we need that any path from s to t must pass through this edge. To check this, perhaps we can check if d_s[a] + l == d_s[b] and d_t[b] + l == d_t[a].

Because:

If d_s[a] + l = d_s[b], then this edge is the only way to reach b from a in the shortest path.

Similarly, if d_t[b] + l = d_t[a], then to reach t from a, you have to go through this edge (because the shortest path from a to t is l + d_t[b]).

Wait, no. d_t[a] is the shortest distance from a to t. So if there's a path a->b followed by the shortest path from b to t, which is length d_t[b], then the total is l + d_t[b]. If this equals d_t[a], then that's the shortest path from a to t. But there could be other paths from a to t that don't go through this edge but have the same total length.

But if d_s[a] + l == d_s[b] and d_t[b] + l == d_t[a], then the edge (a, b) is the only way to reach b from a in the shortest paths, and the only way to reach t from a via this edge. Hence, any shortest path from s to t that goes through a must use this edge. And since s can reach a, the edge is required.

So, the conditions are:

1. d_s[a] + l == d_s[b]

2. d_t[b] + l == d_t[a]

If both are true, then the edge is on all shortest paths. So output YES.

Else, the edge is on some but not all shortest paths, so the answer is not YES. So, in this case, we need to check if we can repair it.

But how to compute this?

So, for the edge (a, b, l) where d_s[a] + l + d_t[b] == D:

Check if both conditions are met. If yes: output YES.

Else: check if after repairing (reducing l to l'), it can be part of all shortest paths. But the repair requires that after the reduction, the new D_new is d_s[a] + l' + d_t[b], which is less than the original D. Then, all other paths (not using this edge) would have length >= original D, which is larger than D_new. Hence, all shortest paths must use this edge.

So, for this case, the repair is possible if:

d_s[a] + d_t[b] + l' < D.

But l' must be >=1, and l' can be as large as possible (up to l-1, since we can't increase the length) such that the sum is < D.

The maximum l' is (D -1 - d_s[a] - d_t[b]).

But also l' must be <= l-1.

So allowed_l' = min( l-1, D-1 -d_s[a] -d_t[b] )

If allowed_l' >=1, then possible. Cost is l - allowed_l'.

Else, cannot repair.

But how do we compute this.

So, for the edge (a, b, l):

If d_s[a] + l + d_t[b] != D:

   Then, the edge is not part of any shortest path.

   So, check if we can repair it to be part of all shortest paths. This requires that after repair, the new contribution is < D.

   So, compute:

   required_new_contribution = d_s[a] + l' + d_t[b] < D.

   The maximum possible l' is min(l-1, D-1 -d_s[a] -d_t[b]).

   Then, check if allowed_l' >=1. If yes, then output CAN and the cost.

   Else, output NO.

Wait, but in this case, the edge is not part of any shortest path. So, the repair can only be possible if after reducing l, the new contribution is < D. Then, all paths not using this edge are >= D, which is larger than the new contribution. Hence, all shortest paths must use this edge.

So, the minimal cost is l - allowed_l', where allowed_l' is the maximum possible l' that satisfies:

l' >=1

d_s[a] + l' + d_t[b] < D

l' <= l-1

So, allowed_l' = min(l-1, D-1 -d_s[a] -d_t[b])

If allowed_l' >=1, then possible. Else, not.

So, for edges not in any shortest path (d_s[a] + l +d_t[b] > D):

   The required condition for repair is that d_s[a] +d_t[b] + l' < D, with l' >=1 and l' <= l-1.

   So allowed_l' = min( l-1, D-1 -d_s[a] -d_t[b] )

   if allowed_l' >=1 and (d_s[a] + allowed_l' + d_t[b] < D):

       then cost is l - allowed_l', output CAN cost.

   else:

       output NO.

For edges that are in some shortest path but not all (d_s[a] + l +d_t[b] == D and (d_s[a] + l !=d_s[b] || d_t[b] + l !=d_t[a]) ):

   Here, the edge is part of some shortest paths. So the president may or may not use it. So, the answer is not YES. But can we repair it such that after repair, the edge is in all shortest paths.

   To do this, the repair must make the new contribution (d_s[a] + l' +d_t[b]) < D. Then, all paths not using this edge would have length >= D, which is larger than new_contribution. Hence, the new shortest path is new_contribution, and all paths must use this edge.

   So the allowed_l' is min(l-1, D-1 -d_s[a] -d_t[b] )

   The same as the previous case. So the repair is possible if allowed_l' >=1.

So, putting it all together:

Compute d_s and d_t.

D = d_s[t]

for each edge (a, b, l):

   if d_s[a] + l +d_t[b] == D:

       check if d_s[a] + l ==d_s[b] and d_t[b] + l ==d_t[a].

       if yes: output YES.

       else:

           allowed_l' = min( l-1, (D-1 -d_s[a] -d_t[b]) )

           if allowed_l' >=1 and (d_s[a] + allowed_l' +d_t[b] < D):

               cost = l - allowed_l'

               output CAN cost

           else:

               output NO

   else:

       allowed_l' = min( l-1, (D-1 -d_s[a] -d_t[b]) )

       if allowed_l' >=1 and (d_s[a] + allowed_l' +d_t[b] < D):

           cost = l - allowed_l'

           output CAN cost

       else:

           output NO

But wait, for the case where d_s[a] + l +d_t[b] == D but the edge is not required, even after repair, perhaps reducing l to l' can make the new contribution (d_s[a] + l' +d_t[b]) < D. Then, all paths must use this edge.

So this is allowed.

So the code can proceed as follows:

For each edge:

current_sum = d_s[a] + l + d_t[b]

if current_sum == D:

   check if (d_s[a] + l == d_s[b]) and (d_t[b] + l == d_t[a])

   if yes: output YES

   else:

       allowed_l' = min(l-1, D-1 -d_s[a] -d_t[b])

       if allowed_l' >=1 and (d_s[a] + allowed_l' +d_t[b] < D):

           cost = l - allowed_l'

           output CAN cost

       else:

           output NO

else:

   allowed_l' = min(l-1, D-1 -d_s[a] -d_t[b])

   if allowed_l' >=1 and (d_s[a] + allowed_l' +d_t[b] < D):

       cost = l - allowed_l'

       output CAN cost

   else:

       output NO

But wait, in the case where current_sum < D:

No, because in the original graph, the shortest path is D. So current_sum can't be less than D, because the sum is the path via this edge, which would mean that the actual shortest path is current_sum. But since D is the shortest path, current_sum can't be less than D.

So for all edges, current_sum >= D.

Wait, no. Because D is the shortest path, any path via the edge (a, b) would have length d_s[a] + l +d_t[b]. Since the shortest path is D, this sum must be >= D.

Otherwise, that would imply that there's a shorter path via this edge.

So for all edges, d_s[a] + l +d_t[b] >= D.

So the code can be written as:

Compute d_s and d_t.

D = d_s[t]

for each edge:

a, b, l = edge

sum_ab = d_s[a] + l + d_t[b]

if sum_ab == D:

   check if d_s[a] + l == d_s[b] and d_t[b] + l == d_t[a]

   if yes: output YES

   else:

       required_sum = D - 1

       max_l' = required_sum - d_s[a] -d_t[b]

       allowed_l' = min(l-1, max_l')

       if allowed_l' >=1 and (d_s[a] + allowed_l' +d_t[b] < D):

           cost = l - allowed_l'

           print CAN cost

       else:

           print NO

else:

   # sum_ab > D

   required_sum = D - 1

   max_l' = required_sum - d_s[a] -d_t[b]

   allowed_l' = min(l-1, max_l')

   if allowed_l' >=1 and (d_s[a] + allowed_l' +d_t[b] < D):

       cost = l - allowed_l'

       print CAN cost

   else:

       print NO

But wait, in the case where sum_ab == D and the edge is not required (the two conditions are not met), we can still try to reduce the l to l' such that sum_ab_new = d_s[a] + l' +d_t[b] < D. If this is possible, then after repair, all shortest paths must use this edge.

So this case is handled by the same code.

Now, the key parts are:

1. Compute d_s and d_t.

2. For each edge, check the conditions.

Now, let's think about implementing this.

For d_s and d_t, since the graph can have up to 1e5 edges and nodes, we need an efficient Dijkstra's algorithm.

But in Python, for large n, using a priority queue with heapq is possible, but we need to use an adjacency list.

For Dijkstra's algorithm:

- To compute d_s: start from s, use a priority queue, and for each node, keep track of the shortest distance.

- To compute d_t: reverse the graph (edges are from b to a, with the same length) and run Dijkstra's from t.

Once we have d_s and d_t, process each edge.

Now, possible edge cases:

- Edges with a == s or b == t.

But the code should handle this.

Now, let's test the sample input 1.

Sample input 1:

n=6, m=7, s=1, t=6.

Edges:

1->2 (2)

1->3 (10)

2->3 (7)

2->4 (8)

3->5 (3)

4->5 (2)

5->6 (1)

d_s:

s=1.

d_s[1] =0.

d_s[2] =2.

d_s[3] = min(1->3=10, 1->2->3=2+7=9) →9.

d_s[4] = 2+8=10.

d_s[5] = min(2->4->5=10+2=12, 9+3=12) →12.

d_s[6] =12+1=13.

d_t is the distance from each node to t=6.

Reversed graph:

Edges are:

2->1 (2)

3->1 (10)

3->2 (7)

4->2 (8)

5->3 (3)

5->4 (2)

6->5 (1)

So from 6, d_t[6] =0.

From 5, you can go to 6 via 1 step (edge 5->6), so d_t[5] =1.

From 4, edge 5->4 (reversed) is 2. So 4 →5 →6: 2+1=3. So d_t[4] =3.

From 3: can go to 5 (3) →5 →6 (1) → total 4. Or other paths? So d_t[3] =3+1=4.

From 2: can go to 3 (7) →4 →5 →6 (7+3+1=11?), but reversed edges for 2 are:

From 2, reversed edges are 1->2 (original 1->2 is reversed to 2->1 in reversed graph, but we need to reverse all edges. So original edges that end at 2 are:

In original edges, which edges have bi=2?

Looking back: the original edges are:

1->2 (2)

so in reversed graph, 2->1 (length 2).

So for d_t[2], it's the shortest path from 2 to 6 in reversed graph (i.e., the original path from 6 to 2).

Wait, no. d_t is the distance from node to t. So in the original graph, to compute d_t[u], we reverse all edges and compute the distance from t to u. Because the original d_t[u] is the shortest path from u to t in the original graph, which is the same as the shortest path from t to u in the reversed graph.

So yes.

So reversed graph for d_t:

For example, edge 1->2 (original) becomes 2->1 (reversed) with length 2.

So in the reversed graph:

For node 2, the outgoing edges are 2->1 (2), 2->3 (7) (original edge is 3->2?), wait no.

Wait original edges are:

Original edge list:

1 2 2 → original direction is 1→2. Reversed for d_t is 2→1, length 2.

1 3 10 → reversed as 3→1, length 10.

2 3 7 → reversed as 3→2, length 7.

2 4 8 → reversed as 4→2, length 8.

3 5 3 → reversed as 5→3, length 3.

4 5 2 → reversed as 5→4, length 2.

5 6 1 → reversed as 6→5, length 1.

So the reversed graph for d_t:

Edges:

2 →1 (2)

3 →1 (10)

3 →2 (7)

4 →2 (8)

5 →3 (3)

5 →4 (2)

6 →5 (1)

So, for node 2, in reversed graph, edges are 2 →1 (2), 3→2 (7), 4→2 (8).

Wait no. Wait reversed graph edges are created by reversing the original edges. So each original edge a→b becomes b→a in the reversed graph.

So for example, original edge 2→3 (7) becomes 3→2 (7) in reversed graph.

So the edges in reversed graph for d_t are:

From each original edge a→b with length l, create a reversed edge b→a with length l.

So the reversed graph has edges:

2 →1 (2)

3 →1 (10)

3 →2 (7)

4 →2 (8)

5 →3 (3)

5 →4 (2)

6 →5 (1)

So to compute d_t (distance from node to t=6 in original graph) we compute the shortest path from t=6 in the reversed graph.

So starting from 6 in the reversed graph, the edges are 6→5 (1).

So d_t[6] =0.

d_t[5] =1 (from 6→5).

d_t[4] comes from 5→4 (2) →1 +2=3.

d_t[3] comes from 5→3 (3) →1+3=4.

d_t[2] can come from 3→2 (7) →4+7=11, or from 4→2 (8) →3+8=11, or from 2→1 (2) which is 2 + d_t[1]. But d_t[1] is the distance from 1 to t in original graph.

Wait, no. d_t[1] is the distance from 1 to t=6. Which in original graph is the path 1→2→3→5→6 (2+7+3+1=13) or other paths.

But in the reversed graph, to compute d_t, we find the shortest path from 6 (the original t) to all other nodes.

Wait, no. Because d_t[u] is the shortest distance from u to t in the original graph, which is the same as the shortest distance from t to u in the reversed graph.

So, for example, to compute d_t[1], we look at the reversed graph's shortest path from 6 to 1.

Let's compute the reversed graph's shortest paths from 6:

Nodes: 6's edges are 6→5 (1).

From 5, edges are 5→3 (3), 5→4 (2).

From 3, edges are 3→1 (10), 3→2 (7).

From 4, edges are 4→2 (8).

From 2, edges are 2→1 (2), 3→2 (7), 4→2 (8).

So the shortest path from 6 to 1:

6 →5 →3 →2 →1: 1 (6→5) +3 (5→3) +7 (3→2) +2 (2→1) = 1+3+7+2=13.

Or 6→5→4→2→1: 1+2+8+2=13.

So d_t[1] =13.

Similarly, d_t[2] is the distance from 6 to 2 in reversed graph. Which can be 6→5→4→2 (1+2+8=11) or 6→5→3→2 (1+3+7=11).

So d_t[2] =11.

Now, let's take the first edge (1,2,2) in the sample input.

sum_ab = d_s[1] (0) + 2 + d_t[2] (11) = 0+2+11=13 == D=13.

Check if d_s[a] + l ==d_s[b]: 0+2=2 ==d_s[2] (yes).

Check if d_t[b] + l ==d_t[a]: 11 +2=13 ==d_t[1] (13). yes.

So output YES.

Second edge (1,3,10):

sum_ab =0 +10 +4=14>13 → not part of any shortest path.

So allowed_l' = min(10-1=9, D-1 -0-4=13-1-0-4=8). So allowed_l' =8.

Then, sum_ab_new=0+8+4=12<13.

So cost is 10-8=2 → output CAN 2.

Which matches the sample.

Third edge (2,3,7):

sum_ab= d_s[2] (2) +7 +d_t[3] (4) =2+7+4=13 ==D.

Check conditions:

d_s[a] +l =2+7=9 ==d_s[3] (9). yes.

d_t[b] +l =4+7=11 ==d_t[a=2] (11). yes. So output YES?

But the sample output for third line is CAN 1.

Wait, sample input's third edge is 2→3 with l=7.

But according to our conditions, the edge would be part of all shortest paths. So why sample output is CAN 1?

Wait, sample input's third edge is 2→3,7. sum_ab=2+7+4=13=D.

Checking conditions:

d_s[a] + l=2+7=9 equals d_s[3] (9). Yes.

d_t[b] + l=4+7=11, which equals d_t[a=2] (11). Yes.

So the edge should output YES. But in the sample output, third line is CAN 1.

Wait, that's a problem. What's wrong here?

Sample input's third edge is 2→3,7.

In the sample output, the third line is CAN 1.

But according to our conditions, this edge should output YES.

But the sample output shows that the third edge is CAN 1. This suggests that our approach is incorrect.

So there's a mistake in our logic.

Let's re-examine the sample.

In the first sample input, the edge 2→3 is part of one of the two shortest paths (1→2→3→5→6). But there's another path (1→2→4→5→6) which is also a shortest path. So this edge is not part of all shortest paths, hence the answer should not be YES. But according to our conditions, the edge would output YES.

But sample output for this edge is CAN 1.

So why is this happening?

This indicates that our conditions are incorrect.

Wait, let's compute the conditions for this edge:

sum_ab =2+7+4=13=D.

Check d_s[a] +l ==d_s[b] → 2+7=9 ==d_s[3] → yes.

Check d_t[b] +l ==d_t[a] →4+7=11 ==d_t[2] (11). So both conditions are met.

But according to the sample input, the edge is not on all shortest paths. For example, the path 1→2→4→5→6 does not use this edge.

So why are our conditions suggesting that this edge is required in all shortest paths?

This is a contradiction.

So, our conditions are incorrect.

So, the logic is wrong.

Thus, the approach based on d_s[a] +l ==d_s[b] and d_t[b] +l ==d_t[a] is incorrect.

Hmm. So we need to find another way to check if the edge is part of all shortest paths.

The problem is that even if both conditions are met, the edge might not be required in all shortest paths.

In the sample input, the edge 2→3 has sum_ab=D and meets both conditions, but there exists a path from s to t that doesn't use this edge.

So why is this possible?

Because there's another path from a=2 to t that doesn't use the edge 2→3. For example, 2→4→5→6.

Wait, the edge 2→3 is part of the path 2→3→5→6. But d_t[2] is 11, which is the sum of the length of 2→4→5→6 (8+2+1=11). So the edge 2→3 is part of a shortest path, but there's another way to reach t from 2.

So the edge is part of some shortest paths but not all.

But according to our conditions, the edge should be part of all shortest paths.

So what's wrong with the conditions?

The conditions:

d_s[a] + l ==d_s[b] → ensures that this edge is part of the shortest path from s to b.

d_t[b] + l ==d_t[a] → ensures that this edge is part of the shortest path from a to t.

But even if both conditions are true, there could be other paths from a to t that also sum to the same distance. For example, a could have two edges, a→b and a→c, both of which contribute to the shortest path.

So, in the sample input's third edge (2→3):

d_t[2] =11. d_t[b=3] is4. l=7. 4+7=11 =d_t[2].

But there's another path from 2 to t: 2→4→5→6 (8+2+1=11). So the edge 2→3 is part of a shortest path from 2 to t, but so is the path through 4→5→6.

Hence, the edge 2→3 is not required for all shortest paths from s to t.

Thus, our conditions are insufficient.

This means that the current approach is incorrect.

We need a different way to determine if an edge is part of all shortest paths.

So, how can we correctly determine whether an edge is part of all shortest paths from s to t?

The correct approach is to check whether the edge is the only way to go from a to b in the shortest path structure. But even then, there might be other paths from a to b that are part of the shortest paths.

An alternative approach is to compute for each edge (a, b) that is part of some shortest path (sum_ab == D), whether there's a way to reach from s to t without passing through (a, b). But how to compute this efficiently.

An efficient way is to compute the number of shortest paths from s to a, and the number of shortest paths from b to t. If the product of these numbers is equal to the total number of shortest paths from s to t, then this edge is part of all shortest paths. But this requires counting the number of shortest paths modulo some large number, but for large graphs, this can be computationally expensive and may overflow.

Alternatively, we can model this using dominator nodes. For each node in the DAG of shortest paths, find whether the edge (a, b) is a bridge (i.e., its removal increases the number of components in the DAG).

But this is challenging.

Another approach is to perform a BFS or DFS on the DAG of shortest paths and check whether the edge (a, b) is part of all paths from s to t.

But for large graphs, this is not feasible.

Hmm. This suggests that the problem requires a different approach.

Let me think again.

The problem requires determining for each edge whether it is on all shortest paths from s to t.

An edge (a, b, l) is on all shortest paths from s to t if and only if:

1. sum_ab = D (i.e., it is on some shortest path).

2. There is no other path from s to t that does not include this edge.

But how to check condition 2.

One way to model this is that the edge (a, b) is a bridge in the shortest path DAG.

But how to find bridges in the DAG.

Bridges are edges whose removal increases the number of connected components in the DAG.

But in the case of directed graphs, bridges are more complex.

Alternatively, we can find the dominators in the DAG. A node a is a dominator of node b if every path from s to b passes through a. Similarly, an edge (a, b) is a bridge if every path from s to t passes through (a, b).

But finding such edges is not straightforward.

Another approach is to construct the shortest path DAG and check for each edge (a, b) whether the DAG is such that a is the only predecessor of b in the DAG, and b is the only successor of a, and so on. But this is not necessarily true.

Alternatively, for each edge (a, b) in the DAG, we can check if:

- All paths from s to a cannot reach t without going through (a, b).

But this is again not easy.

Perhaps the correct way to handle this is to compute the number of ways to reach each node from s in the shortest path, and the number of ways to reach t from each node. Then, for an edge (a, b), if the product of the number of ways from s to a and from b to t equals the total number of ways from s to t, then this edge is part of all shortest paths.

But this requires counting the number of paths, which can be very large. So, using a modulo is a common approach, but even that can be computationally expensive for large graphs.

But given that the problem is to be solved in Python with time constraints, perhaps this is manageable.

So, let's proceed with this approach.

Let's compute for each node u:

cnt_s[u] = the number of shortest paths from s to u.

cnt_t[u] = the number of shortest paths from u to t.

Then, for an edge (a, b) that is part of some shortest path (sum_ab == D), the edge is part of all shortest paths if and only if cnt_s[a] * cnt_t[b] == cnt_s[t].

But this is only true if every shortest path from s to t must pass through this edge. Because the number of paths through this edge is cnt_s[a] * cnt_t[b], and if this equals the total number of paths, then all paths must go through this edge.

So, this is a valid approach.

But how to compute cnt_s and cnt_t.

Computing the number of shortest paths can be done during the Dijkstra's algorithm.

Here's how:

For cnt_s[u], it's the number of shortest paths from s to u.

Initialize cnt_s[s] =1.

For each node u processed in Dijkstra's algorithm, when relaxing an edge (u, v, w):

   if d_s[v] > d_s[u] +w:

       update d_s[v] and set cnt_s[v] = cnt_s[u]

   elif d_s[v] == d_s[u] +w:

       cnt_s[v] += cnt_s[u]

Similarly for cnt_t[u], which is the number of shortest paths from u to t.

To compute cnt_t, reverse the graph and run Dijkstra's from t, counting the number of paths.

But since the numbers can be very large, we need to compute them modulo some large prime, but that's okay as long as the same modulus is used for all computations.

But the problem requires exact equality. So, if the counts are too large, this approach might not work due to overflow. However, given the problem constraints, perhaps the number of paths is manageable using 64-bit integers. But in Python, integers can be arbitrarily large, so this is feasible.

So, the steps are:

1. Compute d_s, cnt_s using Dijkstra's algorithm.

2. Compute d_t, cnt_t by running Dijkstra's on the reversed graph.

3. For each edge (a, b, l):

   if sum_ab != D:

       handle as before.

   else:

       if cnt_s[a] * cnt_t[b] == cnt_s[t]:

           output YES

       else:

           handle as before.

So, this would correctly determine whether the edge is part of all shortest paths.

Let's test this on the sample input.

Sample input 1:

The total number of shortest paths from s=1 to t=6 is 2 (two paths).

For edge 2→3 (sum_ab=13=D):

cnt_s[a=2] is the number of ways to reach 2 from s=1. Since s=1 can reach 2 directly via edge 1→2 (only one way). So cnt_s[2] =1.

cnt_t[b=3] is the number of ways to reach t=6 from 3. The shortest path from 3 to 6 is 3→5→6 (1 way). So cnt_t[3] =1.

cnt_s[2] * cnt_t[3] = 1 *1=1. But cnt_s[t=6] is 2. So 1 !=2 → edge is not part of all shortest paths. So output is not YES.

This matches the sample output (third line is CAN 1).

So the correct approach is to compute cnt_s and cnt_t, and check if the product equals the total.

Thus, the correct conditions for the edge to be in all shortest paths are:

sum_ab == D and cnt_s[a] * cnt_t[b] == cnt_s[t]

So, integrating this into the code:

Compute d_s, cnt_s using Dijkstra.

Compute d_t, cnt_t using Dijkstra on reversed graph.

For each edge:

sum_ab =d_s[a] + l +d_t[b]

if sum_ab != D:

   proceed to check repair possibilities.

else:

   if cnt_s[a] * cnt_t[b] == cnt_s[t]:

       output YES

   else:

       check if repair is possible.

So, the code now needs to compute cnt_s and cnt_t.

Now, the problem is to implement this in Python efficiently.

But for n=1e5 and m=1e5, using a standard Dijkstra's algorithm with a heap would be O(m +n log n), which is acceptable.

But implementing the count for cnt_s and cnt_t requires careful handling.

Let's outline the steps:

Implement Dijkstra's algorithm with a priority queue. For each node, when it's processed (extracted from the priority queue), we know that we have the shortest distance to it. For each neighbor, if a shorter path is found, update the distance and set the count to the current node's count. If the distance is equal, add the current node's count to the neighbor's count.

So, in code:

def dijkstra(adj, s):

    n = len(adj)

    INF = float('inf')

    d = [INF] * (n)

    cnt = [0] * (n)

    d[s] = 0

    cnt[s] = 1

    heap = [(0, s)]

    visited = [False] *n

    while heap:

        dist_u, u = heapq.heappop(heap)

        if visited[u]:

            continue

        visited[u] = True

        for (v, w) in adj[u]:

            if d[v] > dist_u + w:

                if d[v] > dist_u +w:

                    d[v] = dist_u +w

                    cnt[v] = cnt[u]

                    heapq.heappush(heap, (d[v], v))

            elif d[v] == dist_u +w:

                cnt[v] += cnt[u]

    return d, cnt

But this approach may not work correctly because the same node can be added to the heap multiple times. For example, when a node is popped from the heap, its distance is finalized. Any further processing of that node can be skipped.

This is the standard Dijkstra's approach.

So, the code for the count is correct.

But in the case of multiple edges to the same node with the same weight, the count is properly accumulated.

Now, for the sample input, let's compute the cnt_s and cnt_t.

Sample input 1:

s=1, t=6.

d_s[1] =0, cnt_s[1]=1.

Processing 1's edges:

1→2 (2), 1→3 (10).

Initially, d[2]=2, cnt[2] =1.

d[3]=10, cnt[3]=1.

Next, the heap has (2,2) and (10,3). Process (2,2) first.

Processing node 2:

Edges 2→3 (7), 2→4 (8).

For 2→3:

current distance to 3 is 10. New distance via 2 is 2+7=9 <10. So d[3] becomes 9, cnt[3] =1 (cnt[2]=1).

Push (9,3) into heap.

For 2→4: distance is 2+8=10. Push (10,4) into heap.

cnt[4] =1.

Then, next in heap is (9,3). Process node 3.

Node 3's edges: 3→5 (3).

distance to 5 is currently INF. So new distance is9+3=12. cnt[5] =1.

Push (12,5).

Next, process (10,4) (node4).

Node4's edges: 4→5 (2). distance to5 is 12. new via4 is 10+2=12. same as existing. cnt[5] += cnt[4]=1 → cnt[5] =2.

Push (12,5) into heap (but already there).

Then, process node5.

distance 12. edges 5→6 (1). distance to6 is 13. cnt[6] =2 (cnt[5] is 2).

So, cnt_s[6] =2.

So for edge 2→3:

cnt_s[2] is 1. cnt_t[3] is the number of ways to reach t from 3 in original graph. Which is the same as the number of ways to reach 3 from t in the reversed graph.

In the reversed graph, for node3:

d_t[3] is 4 (distance from 6 to3 in reversed graph is 1 (6→5) +3 (5→3) =4).

cnt_t[3] is the number of ways to reach 3 from 6 in reversed graph.

Which is: the path 6→5→3. So cnt_t[3] =1.

So product is 1*1=1. But cnt_s[6] is2. So 1 !=2 → edge is not required. Hence, output is not YES.

Thus, the code would correctly output CAN 1 for this edge.

This aligns with the sample.

So, this approach is correct.

Thus, the code needs to compute cnt_s and cnt_t, then for each edge (a, b):

if sum_ab == D:

   if cnt_s[a] * cnt_t[b] == cnt_s[t]:

       output YES

   else:

       check if repair is possible.

Else:

   check if repair is possible.

So, integrating this into the code.

Now, the code steps are:

Read n, m, s, t.

Build the adjacency list for the original graph.

Build the reversed adjacency list for the reversed graph.

Compute d_s and cnt_s using Dijkstra on the original graph.

Compute d_t and cnt_t using Dijkstra on the reversed graph.

D = d_s[t].

For each edge in the input:

a, b, l = edge

sum_ab = d_s[a] + l + d_t[b]

if sum_ab == D:

   if cnt_s[a] * cnt_t[b] == cnt_s[t]:

       print("YES")

   else:

       max_l' = D -1 -d_s[a] -d_t[b]

       allowed_l' = min(l-1, max_l')

       if allowed_l' >=1 and (d_s[a] + allowed_l' +d_t[b] < D):

           cost = l - allowed_l'

           print(f"CAN {cost}")

       else:

           print("NO")

else:

   max_l' = D -1 -d_s[a] -d_t[b]

   allowed_l' = min(l-1, max_l')

   if allowed_l' >=1 and (d_s[a] + allowed_l' +d_t[b] < D):

       cost = l - allowed_l'

       print(f"CAN {cost}")

   else:

       print("NO")

But we need to handle cases where allowed_l' could be negative.

For example, if D -1 -d_s[a] -d_t[b] is negative.

In that case, allowed_l' is min(l-1, something negative). But since allowed_l' must be >=1, the condition would fail.

So, the code should check allowed_l' >=1 and (d_s[a] + allowed_l' +d_t[b] < D).

But in code, how to compute this.

In Python, for allowed_l' = min(l-1, D-1 -d_s[a] -d_t[b]).

Then, allowed_l' is the maximum possible l' that is <= l-1 and <= (D-1 -d_s[a] -d_t[b]).

But allowed_l' could be negative. For example, if D-1 -d_s[a] -d_t[b] is negative.

So, after allowed_l' is computed, check if allowed_l' >=1 and (d_s[a] + allowed_l' +d_t[b] < D).

But even if allowed_l' is >=1, it's possible that D-1 -d_s[a] -d_t[b] is very negative, so that allowed_l' could be l-1, which may still not satisfy d_s[a] + allowed_l' +d_t[b] < D.

For example, suppose l is 1, allowed_l' =0 (which is <1), so not allowed.

Or l is 2, allowed_l' =1, and d_s[a] +1 +d_t[b] >=D.

But that's why the code has to check both conditions.

Now, implementing this in Python.

But note that the reversed graph is needed for the d_t computation.

Now, code:

Implement Dijkstra's with cnt.

So, the code in Python would be:

Testing against sample input 1.

```python
import heapq


def main(input_stream, output_stream):
    import sys

    input = input_stream.read().split()

    ptr = 0

    n = int(input[ptr])

    ptr +=1

    m = int(input[ptr])

    ptr +=1

    s = int(input[ptr])-1

    ptr +=1

    t = int(input[ptr])-1

    ptr +=1

    adj = [[] for _ in range(n)]

    reversed_adj = [[] for _ in range(n)]

    edges = []

    for _ in range(m):

        a = int(input[ptr])-1

        ptr +=1

        b = int(input[ptr])-1

        ptr +=1

        l = int(input[ptr])

        ptr +=1

        adj[a].append( (b, l) )

        reversed_adj[b].append( (a, l) )

        edges.append( (a, b, l) )

    # Compute d_s and cnt_s

    def dijkstra(adj, start, n):

        INF = float('inf')

        d = [INF]*n

        cnt = [0]*n

        d[start] =0

        cnt[start] =1

        heap = [ (0, start) ]

        visited = [False]*n

        while heap:

            dist_u, u = heapq.heappop(heap)

            if visited[u]:

                continue

            visited[u] = True

            for v, w in adj[u]:

                if d[v] > dist_u + w:

                    d[v] = dist_u +w

                    cnt[v] = cnt[u]

                    heapq.heappush(heap, (d[v], v))

                elif d[v] == dist_u +w:

                    cnt[v] += cnt[u]

        return d, cnt

    d_s, cnt_s = dijkstra(adj, s, n)

    d_t, cnt_t = dijkstra(reversed_adj, t, n)

    D = d_s[t]

    for a, b, l in edges:

        sum_ab = d_s[a] + l + d_t[b]

        if sum_ab == D:

            if cnt_s[a] * cnt_t[b] == cnt_s[t]:

                print("YES", file=output_stream)

            else:

                # Check repair possibility

                max_reduce = D -1 -d_s[a] -d_t[b]

                allowed_l_prime = min(l-1, max_reduce)

                if allowed_l_prime >=1 and (d_s[a] + allowed_l_prime +d_t[b] < D):

                    cost = l - allowed_l_prime

                    print(f"CAN {cost}", file=output_stream)

                else:

                    print("NO", file=output_stream)

        else:

            # sum_ab > D

            max_reduce = D -1 -d_s[a] -d_t[b]

            allowed_l_prime = min(l-1, max_reduce)

            if allowed_l_prime >=1 and (d_s[a] + allowed_l_prime +d_t[b] < D):

                cost = l - allowed_l_prime

                print(f"CAN {cost}", file=output_stream)

            else:

                print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 3 1 3
1 2 10
2 3 10
1 3 100
""",
            "output": \
"""\
YES
YES
CAN 81
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

Another test case is the third sample input:

Sample input3:

2 2 1 2

1 2 1

1 2 2

Output:

YES

NO

For the first edge (1→2,1):

sum_ab=0+1+0=1 == D=1.

cnt_s[a=0 (s)] * cnt_t[b=1 (t)] =1 *1=1 == cnt_s[1] (1). So output YES.

For the second edge (1→2,2):

sum_ab=0+2+0=2>1. So check repair.

max_reduce=1-1-0-0=0-0=0-1=0-0-0= ?

Wait, D=1.

max_reduce = D-1 -d_s[a] -d_t[b] =1-1 -0 -0=0-0=0.

allowed_l_prime = min(2-1=1, 0) →0.

allowed_l_prime >=1? No → output NO.

So correct.

Thus, the code should work.
</think>

```python
import heapq

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1
    s = int(input[ptr]) - 1
    ptr += 1
    t = int(input[ptr]) - 1
    ptr += 1

    adj = [[] for _ in range(n)]
    reversed_adj = [[] for _ in range(n)]
    edges = []

    for _ in range(m):
        a = int(input[ptr]) - 1
        ptr += 1
        b = int(input[ptr]) - 1
        ptr += 1
        l = int(input[ptr])
        ptr += 1
        adj[a].append((b, l))
        reversed_adj[b].append((a, l))
        edges.append((a, b, l))

    def dijkstra(adj_list, start, num_nodes):
        INF = float('inf')
        dist = [INF] * num_nodes
        count = [0] * num_nodes
        dist[start] = 0
        count[start] = 1
        heap = [(0, start)]
        visited = [False] * num_nodes

        while heap:
            current_dist, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            for v, weight in adj_list[u]:
                if dist[v] > current_dist + weight:
                    dist[v] = current_dist + weight
                    count[v] = count[u]
                    heapq.heappush(heap, (dist[v], v))
                elif dist[v] == current_dist + weight:
                    count[v] += count[u]
        return dist, count

    d_s, cnt_s = dijkstra(adj, s, n)
    d_t, cnt_t = dijkstra(reversed_adj, t, n)
    D = d_s[t]

    for a, b, l in edges:
        sum_ab = d_s[a] + l + d_t[b]
        if sum_ab == D:
            if cnt_s[a] * cnt_t[b] == cnt_s[t]:
                print("YES")
            else:
                max_reduce = D - 1 - d_s[a] - d_t[b]
                allowed_l_prime = min(l - 1, max_reduce)
                if allowed_l_prime >= 1 and (d_s[a] + allowed_l_prime + d_t[b] < D):
                    print(f"CAN {l - allowed_l_prime}")
                else:
                    print("NO")
        else:
            max_reduce = D - 1 - d_s[a] - d_t[b]
            allowed_l_prime = min(l - 1, max_reduce)
            if allowed_l_prime >= 1 and (d_s[a] + allowed_l_prime + d_t[b] < D):
                print(f"CAN {l - allowed_l_prime}")
            else:
                print("NO")

if __name__ == "__main__":
    main()
```
