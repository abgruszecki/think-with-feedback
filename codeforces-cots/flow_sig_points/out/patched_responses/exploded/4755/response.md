<think>
Okay, let's tackle this problem. Hmm. The problem is about finding the minimal possible maximum value that Masha writes in her notebook after performing exactly k-1 operations. So, the notebook will have k entries, since the initial placement counts as one. The key here is to choose a starting vertex and a path of k steps (including the starting one) such that the maximum a_i in those steps is as small as possible. Also, if there's no way to make k steps (like not enough edges to move k-1 times), we return -1.

First, I need to understand the constraints. The input can have up to 2e5 vertices and edges. And k can be as big as 1e18, which is way too big for any brute force approach. So, we need an algorithm that works in O(n log something) time, or similar.

Let's think about possible approaches. Since we need the minimal maximum value, maybe binary search on the possible a_i values. For each candidate value X, check if there's a way to perform k steps where all the a_i in the path are <= X. If we can do that, then maybe X is a candidate, and we can try lower. Otherwise, we have to go higher.

But how to check if such a path exists for a given X. That's the crux.

Wait, the path can have cycles. Because Masha can loop around a cycle to get as many steps as needed. For example, if there's a cycle where all a_i <= X, then as long as we can reach that cycle within (k - len(cycle)) steps, then after that we can loop around the cycle as much as needed. So, the key is to see if there's a path that starts at some vertex, uses steps (possibly with cycles) to reach a cycle where all a_i <= X, and then cycles enough times.

Alternatively, if the required k steps can be completed by first moving to a vertex in a cycle, and then cycling until we reach k steps. But how?

Alternatively, for each candidate X, we can model the problem as a graph where only nodes with a_i <= X are allowed, and edges are present as given. Then, the problem reduces to finding a path of length at least k in this X-graph. But how?

Wait, but even if the X-graph has a path of length >=k, then it's possible. But how do we model this? Because with possible cycles, maybe the maximum length is infinite. So, the check would be: can we find a path that has length >=k in the X-graph, possibly by cycling through a cycle.

But when there's a cycle in the X-graph, then for any k, once we reach that cycle, we can loop as long as needed. So, for example, if the X-graph has a cycle, and we can reach it within s steps (s < k), then the total steps can be s + (k-s) steps in the cycle, but since the cycle's length is L, we can loop infinitely. So as long as s <=k, and there's a way to reach a cycle in the X-graph, then it's possible.

So, the check for X would be: can we start at some node with a_i <=X, and then traverse a path where all nodes are <=X, and either:

1. The path length can reach exactly k steps (if the graph is a DAG and has a path of length k-1 edges, i.e., k nodes), or

2. There's a cycle in the X-graph, and the path can reach that cycle in s steps, such that s <=k, and then the cycle can be used to fill the remaining steps.

But even this seems tricky. Let's think again. For a given X, the allowed nodes are those with a_i <= X. Let's call this the X-subgraph.

For each node in the X-subgraph, we can compute the longest possible path starting at that node. If any of those paths has length >=k, then X is feasible.

But if the X-subgraph contains a cycle, then the longest path is infinite, so X is feasible as long as there's a path of at least k steps. But how to model that.

Alternatively, if the X-subgraph has at least one cycle, then there's a way to have infinite steps. So, if k is any number, and if there's a starting node in the X-subgraph that can reach a cycle within s steps (s <=k), then X is feasible.

So for X to be feasible:

- There exists a starting node in the X-subgraph such that either:

   a) The length of the longest path starting at that node (in the X-subgraph) is >=k, or

   b) The X-subgraph contains a cycle and the path from the starting node can reach a node in the cycle in s steps where s <=k-1 (since each step is a move, so to reach the cycle in s steps and then loop through the cycle for the remaining k-1 - s steps).

Wait, maybe not. Because once you are in a cycle, you can loop around it as many times as needed. So, if you can reach the cycle in s steps (s <=k), then the total steps can be s + m*L steps, where L is the cycle length. But we need exactly k steps. Wait, the problem says exactly k-1 operations, which means exactly k steps (since the starting step is 1, then k-1 moves). So, the total number of steps is k.

Wait, the problem statement says: "Masha wants to make exactly k-1 operations in such way that the maximum number written in her notebook is as small as possible."

Each operation is moving, so the number of written numbers is 1 (initial) + (k-1) = k. So, the path length is k steps (each step is a node), connected by k-1 edges.

So, the problem is to choose a path of exactly k nodes, each connected by edges, such that the maximum a_i in those nodes is as small as possible.

But how can cycles help here? Because if there's a cycle in the graph, then Masha can loop around the cycle as many times as needed. So, if k is very large, but there's a cycle where all a_i <= X, then as long as she can reach that cycle in s steps (s <=k) and then loop around it, then the maximum would be the maximum in that cycle.

For example, in the second test case, the cycle is 2->5->6->2. The a_i values are 10,4,5. The maximum is 10. So, if she starts at 2, then the path is 2,5,6,2,5,6,2,... and so on. For k=100 steps, the max is 10.

So, for the binary search approach, for a given X, the X-subgraph consists of nodes a_i <=X and edges between them. Then, in this subgraph, we need to check if there exists a path of length k, possibly by looping cycles. But how to model that.

But when there's a cycle in the X-subgraph, then for any k >= s, where s is the minimal steps to reach the cycle, we can have a path of length k. So, the check for X is:

- The X-subgraph has at least one node (since we need to start there). Otherwise, X is invalid.

Then, either:

a) The X-subgraph contains a cycle, and the minimal steps to reach a cycle (from some starting node) is <=k. Then, if the cycle's length is L, then after reaching the cycle in s steps, the remaining steps can be filled by looping the cycle. So, as long as s <=k, and (k - s) >=0, then possible. But wait, even if (k -s) is 0, that's allowed. For example, if s =k, then we end exactly at the start of the cycle.

Alternatively, perhaps any cycle in the X-subgraph allows us to make arbitrarily long paths. So, if the X-subgraph has a cycle, and there exists a starting node that can reach the cycle in <=k steps, then it's possible to have a path of length >=k. But we need exactly k steps. Wait, but the problem requires exactly k steps, not more. Hmm. So, perhaps if the X-subgraph contains a cycle, then any k is possible (as long as there's a path to the cycle with s <=k steps, and then you can loop around as needed to reach exactly k steps). Wait, that's not necessarily true. Because once you enter a cycle, each loop adds L steps. So, for example, if you have a cycle of length 2, and you need to reach exactly k steps. Suppose s steps to reach the cycle. Then, after that, you can take t loops (each 2 steps) such that s + 2t = k. So, if k - s is even, then possible. Otherwise, not.

Ah, right. So, cycles can only allow extending the path in multiples of their length. So, unless there's a way to adjust the steps by adding cycles. So, in order to reach exactly k steps, the existence of a cycle in the X-subgraph may not be sufficient. Because if after reaching the cycle in s steps, the remaining steps (k - s) must be equal to some multiple of the cycle's length. But that's only possible if (k-s) is a multiple of the cycle length.

Wait, but that complicates things. How can we model this?

Alternatively, perhaps when there's a cycle in the X-subgraph, then there's a way to have infinitely many steps, but only if the cycle's length divides (k-s). But that's not possible for arbitrary k. For example, in the second test case, the cycle length is 3 (2->5->6->2 is a cycle of length 3). So, once you reach the cycle in 1 step (starting at 2), then the remaining steps can be 99. So, 3 * 33 = 99 steps. So, 1 + 99 = 100 steps. So, yes, possible.

But what if k is 1 step (so 0 operations)? Then, it's allowed. So, for the binary search approach, the check would be: can we find a path of exactly k steps (k nodes) in the X-subgraph, possibly by entering a cycle and looping through it the necessary number of times.

But this seems very complicated. How can we model this?

Alternative approach: For a given X, the maximum possible path length is either:

- The length of the longest path in the X-subgraph, which is possible if the X-subgraph is a DAG. In this case, if the longest path is >=k, then possible.

Or,

- If the X-subgraph contains a cycle, then the maximum path is infinite. So, as long as there's a path from a starting node to a cycle in the X-subgraph that uses s steps (s <=k), and then after entering the cycle, the remaining steps (k-s) can be made by cycling. But to do that, the cycle's length must divide (k-s). Wait, no. Because each time you traverse the cycle, you add L steps. So, for example, if the cycle length is L, then you can choose to loop around it t times, leading to s + t*L steps. So, the total steps (k) must be >=s. But if s <=k, then s + t*L = k. So, t = (k-s)/L. But t must be >=0. So, (k-s) must be >=0 and divisible by L. But how can we ensure that?

Wait, no. Because when you are in the cycle, you can take any number of steps in the cycle. For example, if the cycle is A->B->A, length 2. Then, after entering the cycle, each loop adds 2 steps. So, if you need to reach exactly k steps, then (k-s) must be >=0 and even. Otherwise, it's not possible.

But how can we handle this in the general case?

This seems very tricky. Because for a given X, even if the X-subgraph has a cycle, but the required steps (k) can't be achieved by any combination of steps leading to the cycle and steps within the cycle, then X is invalid.

But considering that k can be up to 1e18, this approach is not feasible. So, perhaps there's a smarter way.

Alternative idea: the minimal maximum is the minimal X such that either:

1. There exists a path (without cycles) of exactly k steps in the X-subgraph.

OR

2. There exists a path that reaches a cycle in the X-subgraph in s steps (s <=k) and that the cycle has length L such that (k - s) can be adjusted by looping around the cycle. But how?

But considering that L can be any positive integer, perhaps if (k -s) >=0, then you can loop around the cycle as many times as needed. But that's only possible if you can add any number of loops. But that's not possible. For example, if L=2 and (k-s) is 3, then 2 loops (4 steps) would overshoot. So, that's not possible.

Hmm. So, this approach might not work.

Alternative plan: The problem requires exactly k steps. So, for the path to exist, there must be a path of exactly k steps. However, when there's a cycle in the X-subgraph, then it's possible to have paths of arbitrary length >= some s. But not exactly any length. So, perhaps the problem reduces to:

For a given X, can there exist a path in the X-subgraph of exactly length (k-1 edges) (k nodes), possibly involving cycles.

But how to check this efficiently for large k.

Another idea: For each node, we can compute the maximum path length possible. But for a DAG, we can compute longest paths. However, if there's a cycle, the maximum is infinite, but only for nodes that can reach the cycle. So, for each node in the X-subgraph, if it can reach a cycle in the X-subgraph, then the maximum possible steps is infinite, which would allow any k >= the steps needed to reach the cycle plus the cycle's steps.

Wait, but how?

Alternatively, if the X-subgraph contains a cycle, then any node that can reach the cycle can have infinitely many steps. So, if a starting node can reach a cycle in s steps, then for any k >=s, there exists a path of length k.

Wait, no. Because after s steps, you are in the cycle. Then, each time you go around the cycle, you add L steps. So, for example, after s steps, you can take t loops around the cycle, each loop adding L steps. So, the total steps would be s + t*L. So, if there's a way to have s + t*L =k, then yes. So, for any k >=s and k ≡ s mod L. Then, t would be (k-s)/L. So, only possible if (k-s) is divisible by L. But how can we ensure that?

This is getting complicated. Maybe we need a different approach.

Let's think about binary search. Let's say we are checking if X is a possible candidate. We need to see if there's a path of length exactly k steps (k nodes) in the X-subgraph. How can we model this?

But for large k, we can't model this with dynamic programming or BFS for each node. So, perhaps we can model the problem in terms of transitions between nodes and cycles.

Wait, but how?

Alternative approach: Since the maximum a_i in the path is the maximum of the nodes in the path, the minimal possible maximum is the smallest X such that:

Either:

- There's a path of length k in the X-subgraph (i.e., a sequence of nodes connected by edges, all with a_i <=X, and length exactly k), and the maximum in that path is <=X.

OR

- There's a path that reaches a cycle in the X-subgraph, and the maximum in the path is <=X, and the cycle's length L divides (k - s), where s is the steps taken to reach the cycle. But again, this depends on the cycle's length.

But this seems unmanageable. How can we model this for large k?

Alternatively, when there's a cycle in the X-subgraph, then if we can reach it in s steps, then as long as (k -s) is >=0, we can stay in the cycle for (k -s) steps, looping as needed. Wait, but that's not correct. Because each step in the cycle moves to the next node. For example, if the cycle is of length L, then after entering the cycle, every L steps you return to the starting node of the cycle.

So, suppose we reach the cycle after s steps. Then, the remaining steps (k -s) can be filled by moving through the cycle. Since the cycle has L nodes, we can take (k -s) steps (edges) by following the cycle. So, regardless of L, as long as (k -s) >=0, it's possible. Because even if the cycle is of length 3, and (k -s) is 4, you can take the cycle steps 4 times. The steps would be 3 + 1 steps (since after 3 steps you return to the start, then take one more step).

So, in this case, the presence of any cycle in the X-subgraph implies that for any k >=s, where s is the number of steps to reach the cycle, there exists a path of length k steps.

Wait, maybe. Because once you are in the cycle, you can walk around it as many times as needed. For example, a cycle of length L, once entered, allows you to have steps s, s+1, s+2, ..., up to any number. Because each step adds 1. So, once you are in the cycle, you can take any number of steps. So, if you have a cycle in the X-subgraph, and you can reach the cycle in s steps where s <=k, then you can take (k-s) steps in the cycle. So, if the cycle is reachable in s steps and s <=k, then possible.

Wait, no. Because the cycle's length is L. So, after entering the cycle, each step in the cycle is moving to the next node. So, if the cycle is A->B->C->A (length 3), then after entering the cycle (say at step s), you can take any number of steps. For example:

s steps (A), s+1 (B), s+2 (C), s+3 (A), etc. So, for any k >=s, there's a path of length k. Because once you are in the cycle, you can take exactly (k-s) steps through the cycle. Even if (k-s) is larger than L, you just loop around as needed.

So, in this case, if there's a cycle in the X-subgraph and a starting node that can reach the cycle in s steps where s <=k, then the answer is possible for X.

So, putting it all together, for a candidate X, the X-subgraph is the subgraph of nodes with a_i <=X and edges between them. Then, in this subgraph, the following must hold:

Either:

1. There's a path (without cycles) of length exactly k steps (k nodes). Or,

2. There exists a starting node in the X-subgraph that can reach a cycle in s steps (s <=k) and the cycle is in the X-subgraph.

In this case, even if the path length from the starting node to the cycle is s steps, and then you can take (k -s) steps through the cycle (even if (k-s) is larger than the cycle length), it's possible.

So, the check for X is:

- For the X-subgraph, there's a starting node such that either:

   a) There's a path of length k steps in the X-subgraph starting at that node, or

   b) There's a path from the starting node to a cycle in the X-subgraph, and the path's length is s <=k steps.

So, the binary search approach would proceed as follows:

- Sort all a_i and binary search through them. For each candidate X, collect all nodes with a_i <=X. Check if there's a way to have a path of k steps (as per the conditions above). If yes, try a lower X. Else, try higher.

Now, the problem is how to efficiently check these conditions for a given X.

But how to check these conditions efficiently, given the constraints.

Let's think about the X-subgraph. For each X, we can build the adjacency list for nodes in the X-subgraph.

But considering that the constraints are up to 2e5 nodes and edges, and X could be up to 1e9, the binary search approach would have O(log(1e9)) steps. For each step, we need to process the X-subgraph.

But processing the X-subgraph for each binary search step would be O(n + m) per step, which is O(2e5 * 30) = 6e6 steps. Which is manageable.

But wait, in each binary step, we need to process all nodes and edges again. But for each X, the X-subgraph includes all nodes with a_i <=X and edges between them. So, for a given X, the nodes are those with a_i <=X, and edges are those where both endpoints are <=X.

So, perhaps during the binary search, for each candidate X, we can precompute the nodes and edges that are allowed. But how?

Alternatively, pre-sort the nodes by their a_i values, and for each X, the allowed nodes are the ones up to a certain index. But that's possible only if the a_i's are sorted.

But since the a_i's can be arbitrary, we can sort the list of (a_i, node) pairs. Then, during binary search, the allowed nodes are those with a_i <=X, which can be determined using a binary search on the sorted list.

Similarly, edges between allowed nodes can be precomputed. But how to store this efficiently.

Alternatively, for each edge u->v, we can note that this edge is present in the X-subgraph only if a_u <=X and a_v <=X.

So, during the binary search step for X, the X-subgraph consists of all nodes with a_i <=X, and edges where both endpoints have a_i <=X.

So, during the check for X:

1. Collect all nodes with a_i <=X. Let's call this S.

2. For each node in S, check if it can reach a cycle within the X-subgraph. Also, compute the maximum path length in the X-subgraph for each node.

But how to compute this efficiently.

Hmm. Let's think about the possible scenarios:

If the X-subgraph has a cycle, then for any node in S that can reach the cycle, the maximum path length is infinite. So, if the node can reach a cycle in s steps, then for any k >=s, it's possible.

But for the problem's check, we need to see if there exists a node in S where:

Either:

- The maximum path length from that node is >=k. (If the X-subgraph is a DAG, then this is possible only if the DAG has a path of length k.)

OR

- The node can reach a cycle in the X-subgraph in s steps, and s <=k.

But how to check if there's a node in S that can reach a cycle in the X-subgraph, and the minimal steps to reach the cycle is <=k.

But how to compute this.

Alternatively, for the X-subgraph, if it contains any cycles, then any node in a cycle can reach the cycle in 0 steps. So, if the X-subgraph contains a cycle, then the answer is possible if k >=0. Wait, no. Because the starting node must be in S (a_i <=X). So, if the X-subgraph has a cycle (which requires all nodes in the cycle have a_i <=X), then any node in the cycle can start, and loop through the cycle. So, for example, if k steps are required, starting at node u (in the cycle), then we can take k steps in the cycle, as long as the cycle's length is such that we can step through it k times. But since the cycle is a loop, you can just loop around as needed. So, even if the cycle is of length L, you can make as many steps as needed. For example, if the cycle is length L, then after 0 steps (starting at node u), you can take 1, 2, ..., any number of steps. So, for any k >=1, you can have a path of length k.

Wait, but the cycle is a loop. For example, a cycle of length 3: u->v->w->u. Starting at u, the steps are:

1: u

2: v (after one move)

3: w (two moves)

4: u (three moves)

5: v (four moves)

So, the number of steps (nodes) is exactly the number of moves (edges) plus one. So, for k steps, you need exactly (k-1) moves. So, for the cycle, any number of steps >=1 is possible, because you can loop around as needed.

Wait, yes. Because once you are in the cycle, you can keep moving through the edges. So, the path can be of any length >=1. So, if the X-subgraph has a cycle, then for any k >=1, there's a path of length k steps starting from any node in the cycle.

Therefore, for the binary search step, if the X-subgraph has any cycle (i.e., is not a DAG), then the answer is possible if there exists a node in S (a_i <=X) that can reach a cycle in s steps where s <=k.

Wait, but even if s is larger than k, then it's not possible. So, the check is whether any node in S has a path to a cycle in s steps where s <=k. Then, the total steps would be s steps to reach the cycle, and then (k - s) steps in the cycle. But how?

No. Once you reach the cycle in s steps, you can take as many steps as needed. For example, if you enter the cycle at step s, then from there, you can take any number of steps. So, for any k >=s, you can have a path of length k. So, if the X-subgraph has a cycle, and there exists a node in S that can reach the cycle in s steps where s <=k, then it's possible. Because after s steps, you have (k - s) steps to take, which can be done by cycling.

But how to compute s for all nodes in S.

Alternatively, if the X-subgraph has a cycle, then any node that can reach the cycle (even in s steps where s >k) is not useful. But if there's a node that is in a cycle, then s=0. So, for k >=1, it's possible.

So, if the X-subgraph has a cycle, then the answer is possible as long as k >=1 and there's at least one node in S. But wait, the cycle must be part of the X-subgraph. So, the X-subgraph has a cycle (i.e., is not a DAG) if and only if it contains at least one cycle. So, in this case, there's a node in the cycle. So, if the X-subgraph is not a DAG, then it has a cycle, and there's a node in S (the cycle's nodes). Then, for any k >=1, you can start at that node and walk through the cycle for k steps. So, the answer is possible.

Wait, but this is only true if k >=1 and the cycle's nodes are in S. Because the cycle's nodes are in S (since they are part of the X-subgraph). So, if the X-subgraph is not a DAG (contains a cycle), then there's a cycle in S. So, the answer is possible if k >=1. But wait, if k is 1, then you just start at the node in the cycle. That's allowed.

Wait, but the problem requires exactly k-1 moves, which is exactly k steps. So, if k=1, then you have 0 moves, and just the starting node. So, in that case, even if there's a cycle, the starting node must have a_i <=X, which is true since it's part of the X-subgraph. So, for any X, if the X-subgraph has a cycle, then there's a node in S (the cycle) which can be used as a starting node. Then, for any k >=1, it's possible to have a path of length k steps. Because you can just walk around the cycle. For example, if k=5, then starting at a node in the cycle, you can take 4 moves (5 steps) around the cycle.

So, the conclusion is: if the X-subgraph has a cycle (is not a DAG), then any k is possible as long as there exists at least one node in S (which there is, since the cycle is part of S). So, the answer for X is possible if either:

a) The X-subgraph is a DAG and has a path of length >=k steps, or

b) The X-subgraph is not a DAG (contains a cycle).

So, in the binary search step, for a candidate X:

- Check if there exists a node in S (a_i <=X). If not, X is invalid.

- Check if the X-subgraph is not a DAG (has a cycle). If yes, then X is a possible candidate.

- Else, check if the X-subgraph (DAG) has a path of length >=k steps. If yes, X is possible.

So, the steps for checking X are:

1. Check if S (nodes with a_i <=X) is empty. If empty, return false.

2. Check if the X-subgraph has a cycle. If yes, return true.

3. Else, check if the longest path in the X-subgraph (DAG) is >=k. If yes, return true. Else, return false.

This seems manageable.

Now, how to compute these steps efficiently.

First, step 1 is trivial: just check if any a_i <=X.

Step 2: check if the X-subgraph has a cycle. This can be done via topological sort. If the topological sort includes all nodes in S, then it's a DAG. Else, it has a cycle.

But topological sort for a graph with up to 2e5 nodes each time might be expensive. However, given that binary search is about 30 steps, and each step involves O(n + m) processing, it's 30 * (2e5 + 2e5) = 1.2e7 operations, which should be manageable.

Step 3: compute the longest path in the DAG. For a DAG, the longest path can be computed in O(n + m) time using topological sorting and dynamic programming.

But for the X-subgraph, which could have up to 2e5 nodes and edges, this could be expensive. However, since in step 2 we already compute the topological order (if it's a DAG), we can reuse that order to compute the longest path.

So, the plan for checking X is:

1. Collect all nodes where a_i <=X. Let S be this set.

   If S is empty, return false.

2. Collect all edges between nodes in S (u and v must be in S).

3. Check if this subgraph has a cycle. To do this, compute the in-degree of each node in S, then perform Kahn's algorithm for topological sort. If during this process, some nodes are not processed, then there's a cycle.

   So, during Kahn's algorithm:

   - Initialize a queue with nodes with in-degree zero.

   - For each node in the queue, process it, decrementing the in-degree of its neighbors.

   - If the total number of processed nodes is less than |S|, then the graph has a cycle.

   If a cycle is found, return true (as per step 2 of the check).

4. If the graph is a DAG, then compute the longest path.

   - Using the topological order obtained from Kahn's algorithm, compute for each node the maximum path length starting from that node.

   - The maximum among all these values is the longest path in the DAG.

   If this value >=k, return true. Else, return false.

Now, the challenge is to implement this efficiently.

But considering that for each binary search step, the time is O(n + m), this is feasible for the given constraints.

So, the binary search approach is:

- Sort all possible a_i values and perform binary search on them.

- For each candidate X, perform the check as described.

The minimal X for which the check returns true is the answer.

Now, let's think about the edge cases.

For example, when k=1. Then, we need exactly 0 operations, so the path is just the starting node. So, the minimal X is the minimal a_i among all nodes. But the check for X would require that there exists a node with a_i <=X (which is always true if X is >= the minimal a_i). But since k=1, even if the subgraph has a cycle, it's allowed as long as there's a node in S (since you can take 0 steps, just the starting node). So, the check would return true for X >= minimal a_i.

Another example: when the graph has no edges (m=0). Then, any path can have only 1 step. So, for k=1, answer is the minimal a_i. For k>1, it's impossible (output -1).

Another example: when m=0 and k=1. Then, the answer is the minimal a_i.

Now, let's test the approach against the examples.

First example:

Input:

6 7 4

1 10 2 3 4 5

Edges as described.

When X=4, the nodes in S are 1,3,4,5. Wait, a_i for nodes are 1, 10, 2, 3,4,5. So, nodes with a_i <=4 are 1 (a=1), 3 (a=2), 4 (a=3), 5 (a=4). Node 6 has a=5, which is excluded.

The edges in the X-subgraph are those between these nodes.

Looking at the edges:

The edges between these nodes are:

1->2 (but node 2's a_i is 10, which is not in S. So, this edge is excluded.

Similarly, edges between nodes in S:

Looking at the original edges:

1 2: no.

1 3: yes (both in S).

3->4: yes.

4->5: yes.

5->6: no.

6->2: no.

2->5: no.

So, edges in X-subgraph are:

1->3.

3->4.

4->5.

So, the X-subgraph is a DAG (no cycles). The longest path is 1->3->4->5, which is 4 steps (k=4). So, this meets the condition. So, X=4 is valid.

The binary search would find this.

The second example:

k=100. The X-subgraph for X=10 includes all nodes. The graph contains cycles. So, since the X-subgraph contains a cycle, the answer is possible. So, X=10 is the minimal possible.

Third example:

2 nodes, edge 1->2. a_i are 1 and 1. k=5 steps (4 moves). Since each move can only be 1->2. The path is 1,2, then no further moves (since there's no edge from 2). So, the maximum path length is 2. So, for k=5 steps, it's impossible.

Fourth example:

1 node, no edges. k=1. So, start at the node. Valid.

So, the approach seems to handle these cases.

Now, implementing this in Python.

But the problem is handling large graphs efficiently. Let's think about the steps.

Implementing the binary search:

- Sort the unique a_i values. For each candidate X, we can binary search in this sorted list.

But how to collect all nodes and edges for the X-subgraph.

But storing all edges for each X is expensive. So, perhaps during preprocessing, for each edge u->v, we can check if u and v are in the X-subgraph. But in code, for each X, the X-subgraph's edges are those where a_u <=X and a_v <=X.

So, during the check for X:

1. Collect all nodes where a_i <=X.

   We can do this by checking each node's a_i.

2. For each edge in the original graph, check if both u and v are in the X-subgraph. If yes, include it in the adjacency list for the X-subgraph.

But for each binary search step, this requires iterating over all m edges, which can be 2e5. For 30 steps, this is 6e6 operations. Which is manageable.

So, the code steps:

Read n, m, k.

Read a list (0-based or 1-based? Probably 1-based, as input uses 1-based indices.)

Read m edges. Store as a list of edges, but also build an adjacency list for the original graph.

Sort the unique a values. Or, create a sorted list of a's, then binary search on this.

For each binary search step (mid X):

   S is the set of nodes (0-based or 1-based?) where a_i <=X.

   If S is empty: continue (invalid X).

   Now, build the adjacency list for the X-subgraph:

      adj = [[] for _ in range(n+1)]

      for each edge u, v in original edges:

          if u is in S and v is in S:

              adj[u].append(v)

   Now, compute in-degree for all nodes in S.

   Then, perform Kahn's algorithm to check if the subgraph is a DAG.

   in_degree = defaultdict(int)

   for u in S:

       for v in adj[u]:

           in_degree[v] +=1

   queue = deque()

   for u in S:

       if in_degree.get(u, 0) ==0:

           queue.append(u)

   processed =0

   top_order = []

   while queue:

       u = queue.popleft()

       top_order.append(u)

       processed +=1

       for v in adj[u]:

           in_degree[v] -=1

           if in_degree[v] ==0:

               queue.append(v)

   if processed != len(S):

       # has a cycle

       return True for this X.

   else:

       # DAG. Compute longest path.

       # Initialize dp[u] as 1 for all u (since each node is a path of length 1).

       dp = [1]*(n+1)

       for u in top_order:

           for v in adj[u]:

               if dp[v] < dp[u] +1:

                   dp[v] = dp[u] +1

       max_len = max(dp[u] for u in S)

       if max_len >=k:

           return True

   else:

       return False

But in Python, for large n (2e5), using lists for adj and in_degree can be slow. Also, for each X, building the adjacency list by checking all edges is O(m), which for 2e5 edges and 30 steps is manageable.

But what if m is 2e5 and 30 steps? 6e6 operations.

But considering Python's speed, this may be tight. Let's see.

Alternative optimizations:

- Precompute for each edge, the minimum X required for this edge to be present in the X-subgraph. But that's (max(a_u, a_v)), since both nodes must be <=X. So, the edge is included if X >= max(a_u, a_v). But storing this for each edge would allow us to, during binary search steps, quickly find which edges are included. But in practice, during each step, we still have to iterate through all edges and check if X >= max(a_u, a_v). Which is O(m) per step.

But in Python, even 2e5 *30 is 6 million operations, which is manageable.

Another thing to consider is the nodes' a_i values. For each node, we can precompute whether a_i <=X. So, during each binary search step, we can precompute a list of nodes in S.

But for large n, this is O(n) per step, which for 30 steps is 6e6 operations.

So, the code outline is as follows.

But there's a problem: in Python, for each binary step, building the adjacency list for the X-subgraph would require checking all m edges. Which is O(m) per step. For m=2e5 and 30 steps, this is 6e6 steps. Which is manageable.

So, the code:

But wait, in the code, nodes are 1-based (as per the input).

Now, let's proceed.

First, read n, m, k.

Then read a list of a_i, which is 1-based.

Then read the m edges. For each edge, store u and v (as integers).

Then, sort the list of a_i to create a sorted list of possible X candidates.

But the binary search can be done on the sorted unique list of a_i's. But since duplicates are possible, it's better to collect the unique values and sort them. Let's call this sorted_a.

But for binary search, the initial left is the minimum a_i, and the right is the maximum a_i. But maybe the optimal X is not in the a_i list, but somewhere in between. For example, if all a_i are even and the optimal X is an odd. Wait, but since the problem requires the minimal possible maximum of the selected a_i's in the path, the optimal X must be the maximum of the a_i's in the path. So, the optimal X is the minimal possible value such that there exists a path where all a_i's are <=X. Therefore, the optimal X is the minimal possible value for which the check returns true, which must be one of the a_i's. Because if there's a path where all a_i's are <=X, but X is not an a_i in the path, then the maximum in the path is less than X, which would allow a lower X. So, the binary search can be done on the sorted list of a_i's.

Wait, no. For example, suppose a_i's are 1,3,5. Suppose the optimal path has a maximum of 4, but that's not possible. Because the nodes in the path must have a_i <=X, and the maximum is the largest a_i in the path. So, X must be at least the maximum a_i in the path. Therefore, the minimal X is the maximum of the a_i's in the path. So, the optimal X is the minimal maximum a_i of some path of k steps. So, this must be one of the a_i's. Because the maximum in the path is one of the a_i's. So, the binary search can be done over the sorted list of a_i's.

So, we can collect all a_i's, sort them, and perform binary search on this array.

Thus, in code:

sorted_a = sorted(a) (after reading a as a list).

But since a can have duplicates, sorted_a may have duplicates. So, we can create a list of unique a_i's, sorted. Or not. It's not necessary, as binary search can handle duplicates.

So, the binary search would proceed as follows:

low = 0, high = len(sorted_a) -1.

But perhaps a better way is to use the actual values.

But in Python, the bisect module can help. But perhaps we can binary search between the minimum and maximum a_i.

Wait, but the minimal X can be as low as the minimal a_i (if there's a path of k steps with all a_i equal to the minimal one), or as high as the maximal a_i.

So, the binary search's initial left is the minimal a_i, right is the maximal a_i.

But perhaps the optimal X is not in the a_i's. For example, if the minimal possible path has a maximum of 4, but no node has a_i=4. But according to the problem statement, all a_i are positive integers, but the X in the problem can be any integer. So, for example, if the path includes nodes with a_i=3 and 5, then the maximum is 5. So, the binary search must find the minimal X such that X is >= the maximum a_i in the path, and the path exists.

But how can X be not in the a_i list? It's impossible, since the maximum a_i in the path must be one of the a_i's. Therefore, the minimal X is the maximum a_i in the path. So, the optimal X must be one of the a_i's. Hence, binary search can be done over the sorted list of a_i's.

Therefore, sorted_a is the sorted list of a_i's.

Now, the code:

Read n, m, k.

Read a list (assuming 1-based nodes? Or 0-based? The code should manage indices properly.)

Read edges, stored as a list of tuples (u, v).

Sort the list a into sorted_a.

If k ==1:

   We can just take the minimal a_i. So, the answer is min(a).

But we need to check if m >=0 and k==1. Because even if m=0, as long as we can choose a starting node (which is always possible), then it's allowed.

Wait, k=1 means 0 operations. So, the starting node is the only node. So, the answer is the minimal a_i.

Wait, but according to the problem statement, Masha can choose any starting node. So, the minimal maximum is the minimal a_i. So, in this case, the answer is min(a). So, we can handle this as a special case.

But in the code, the binary search will naturally handle this. For example, when X is the minimal a_i, the X-subgraph contains all nodes with a_i <=X. Which is the nodes with a_i equal to X (since X is the minimal). So, if k=1, the answer is the minimal a_i.

So, no need to handle this case separately.

But let's proceed.

Implement the binary search.

Initialize low = 0, high = len(sorted_a) -1.

But sorted_a is a sorted list of all a_i's. So, the minimal X is the minimal a_i, and the maximum X is the maximum a_i.

But the code can use left=0 and right=len(sorted_a)-1 indices, and select the minimal X.

Wait, the binary search code should find the smallest X in sorted_a such that the check returns true.

Wait, no. Because sorted_a may have duplicates. For example, if sorted_a is [1,2,2,3,3,3], the minimal X is the smallest value for which the check is true.

But how to handle this.

Alternatively, binary search over the possible X values, not just the a_i's. Because the X can be any value, not just the a_i's. But the optimal X is the minimal possible maximum of the path. So, the minimal X is the minimal value such that there exists a path with maximum a_i <=X.

But since the a_i's are integers, and the problem's a_i's are given as integers, the possible X's are integers.

But the binary search can be done on the entire range from min_a to max_a, where min_a is the minimal a_i and max_a is the maximal.

But how to find the minimal X that satisfies the check.

For example, suppose the sorted_a is [1,3,5]. The optimal X could be 3 if there's a path of k steps with all a_i's <=3, and the maximum is 3. So, binary search between 1 and 5.

But how to manage this.

But according to the problem statement, the X in the solution must be the maximum a_i in the path. So, the minimal possible X is the minimal maximum a_i among all possible paths of k steps.

Thus, the binary search can be over all possible X values (not necessarily a_i's), but for each X, the check is as described.

But for efficiency, we can collect the sorted list of a_i's and binary search over them. Because the optimal X is the minimal a_i that is >= the maximum a_i of some path.

So, for example, if the a_i's are [1,2,3,4,5], and the optimal path has a maximum a_i of 3, then X=3 is the minimal possible.

But if there is no path with maximum 3, but there's a path with maximum 4, then X=4 is the answer.

So, the binary search can proceed over the sorted_a list.

Thus, the code for binary search would be:

low = 0

high = len(sorted_a) -1

answer = -1

while low <= high:

    mid = (low + high) //2

    X = sorted_a[mid]

    if check(X):

        answer = X

        high = mid -1

    else:

        low = mid +1

But this may not work, because sorted_a may have multiple copies of the same X, and the minimal X may be the first occurrence. For example, sorted_a could be [1,2,2,3], and the answer is 2. So, the code would find the first 2.

But if we are binary searching for the minimal X, this is correct.

Alternatively, we can collect the unique sorted list of a_i's and binary search over that.

But in Python, we can use the bisect module to find the minimal X.

Alternatively, the code can proceed with the binary search over the entire possible range of X's.

But given the time constraints, the binary search over the sorted a_i's is better.

Now, code:

Read the input.

Then, handle the case where k=0? No, k is at least 1.

But according to the problem statement, k is at least 1.

But wait, in the problem statement, k is given as the number of steps (including the initial placement). So, k can be 1, which requires 0 operations.

But the code should handle this.

Now, let's proceed to write the code.

But the main challenge is the check function.

Implementing the check function for a given X:

def check(X):

    S = [i for i in range(1, n+1) if a[i] <=X]

    if not S:

        return False

    # build adjacency list for S

    adj = [[] for _ in range(n+1)]

    for u, v in edges:

        if a[u] <=X and a[v] <=X:

            adj[u].append(v)

    # compute in_degree

    in_degree = defaultdict(int)

    for u in S:

        for v in adj[u]:

            in_degree[v] +=1

    # Kahn's algorithm

    q = deque()

    for u in S:

        if in_degree.get(u, 0) ==0:

            q.append(u)

    processed =0

    top_order = []

    while q:

        u = q.popleft()

        processed +=1

        top_order.append(u)

        for v in adj[u]:

            in_degree[v] -=1

            if in_degree[v] ==0:

                q.append(v)

    if processed != len(S):

        # has a cycle

        return True

    else:

        # compute longest path

        dp = [1]*(n+1)

        for u in top_order:

            for v in adj[u]:

                if dp[v] < dp[u] +1:

                    dp[v] = dp[u] +1

        max_len = max(dp[u] for u in S)

        return max_len >=k

But this is O(n + m) per check.

But for large n and m, this can be time-consuming.

But let's see:

In Python, for n=2e5 and m=2e5, each check is O(n + m) = 4e5 steps. For 30 steps, this is 1.2e7 steps. Which is manageable.

But some optimizations can be made. For example, precomputing for each edge whether it's included in the X-subgraph.

But in code, for each edge, check if a[u] <=X and a[v] <=X.

This is manageable.

But in Python, using lists and loops for large data may be slow.

Another optimization: precompute for each node whether a[i] <=X. For example, for the current X, create a boolean array.

But in Python, list comprehensions are fast.

Another thing: the code uses 1-based node numbering.

Now, the code.

But let's think about the sample input.

Sample input 1:

6 7 4

1 10 2 3 4 5

Edges: as given.

So, the a list is [1,10,2,3,4,5] for nodes 1-6.

When X=4, the S is nodes where a_i <=4: nodes 1 (1), 3 (2),4 (3),5 (4).

The edges in the X-subgraph are 1->3, 3->4, 4->5. So, adjacency list for these nodes.

Kahn's algorithm processes these nodes:

In-degree for nodes:

node 1: 0.

node3: 1 (from 1).

node4: 1 (from 3).

node5: 1 (from4).

So, initial queue has node 1.

Process node1: add to top_order. Processed=1.

Node1's neighbors are 3. Decrement in_degree of 3 to 0.

Add node3 to queue.

Process node3: add to top_order. Processed=2. Its neighbor is 4. Decrement in_degree of 4 to 0. Add to queue.

Process node4: add to top_order. Processed=3. Neighbor is 5. Decrement to 0. Add to queue.

Process node5: add to top_order. Processed=4.

All nodes processed. So, no cycle.

Longest path:

dp[1] =1.

When processing node1: dp[3] = max(1, dp[1]+1) = 2.

When processing node3: dp[4] = 2+1=3.

When processing node4: dp[5] =3+1=4.

max_len is 4, which equals k=4. So, return True.

Thus, X=4 is valid.

Now, the code would find this.

So, the code should work.

But what about the second sample:

Sample input 2:

6 7 100

a is same as before.

X=10. All nodes are in S.

Check if the X-subgraph contains a cycle.

Yes. For example, nodes 2,5,6 form a cycle.

So, the code would detect that the graph has a cycle, so return True. Thus, X=10 is valid.

Third sample:

2 nodes, a=[1,1]. Edge 1->2.

k=5.

For X=1, the subgraph includes both nodes. The edge is included.

The subgraph is 1->2. This is a DAG. Longest path is 2 steps. Which is less than 5. So, returns False.

So, the code would return -1.

Fourth sample:

1 node, a=1e9, k=1.

X=1e9 is valid. The subgraph is the node itself. The check is:

S has one node. The subgraph has no edges. So, Kahn's algorithm processes 1 node. processed=1. No cycle. Longest path is 1, which equals k=1. So, returns True.

So, code returns 1e9.

Now, implementing the code.

But the code needs to read the input correctly.

Now, let's write the code.

But in Python, reading 2e5 edges can be slow with input(). So, using sys.stdin.

So, the code:

Read n, m, k from input.

Read a as a list of integers (assuming 1-based index).

Read m edges as a list of tuples (u, v).

sorted_a = sorted(a).

Then, binary search over the sorted_a.

But for the binary search, the code should find the smallest X in sorted_a where check(X) is True. If none, return -1.

But wait, the code should also handle the case where even the maximum a_i is not sufficient. For example, when there's no path of length k steps.

So, after binary search, if no X is found, return -1.

But how to determine that.

Wait, the binary search is over the sorted_a. But if the maximum a_i is not sufficient, then there's no solution.

So, in code:

sorted_a = sorted(a)

left =0

right = len(sorted_a) -1

ans = -1

while left <= right:

    mid = (left + right) //2

    x_candidate = sorted_a[mid]

    if check(x_candidate):

        ans = x_candidate

        right = mid -1

    else:

        left = mid +1

But after this, need to verify whether the ans is valid. Because, for example, if the binary search finds an ans, but the check returns True, but there's no way to reach the cycle in s steps <=k. But according to the check function, this case is handled.

But after the binary search, if ans is found, then the minimal X is ans. Else, output -1.

But the check function may return True for some X, but not for others.

Now, the code:

But the code must also handle the case where even the maximum a_i is not sufficient. For example, when there's no path of length k steps, and no cycles in the X-subgraph for any X.

But in this case, the check for the maximum a_i would return False, and the code would return -1.

So, the code.

Now, implementing the check function.

But in Python, for large n, using defaultdict for in_degree can be slow. So, perhaps pre-initializing a list.

But for each check, S is the list of nodes with a_i <=X. So, the code can create a list of nodes in S.

But in code:

def check(X):

    S = [u for u in range(1, n+1) if a[u] <= X]

    if not S:

        return False

    # build adjacency list for S

    adj = [[] for _ in range(n+1)]

    for u, v in edges:

        if a[u] <= X and a[v] <= X:

            adj[u].append(v)

    # compute in_degree

    in_degree = [0]*(n+1)

    for u in S:

        for v in adj[u]:

            in_degree[v] +=1

    # Kahn's algorithm

    q = deque()

    for u in S:

        if in_degree[u] ==0:

            q.append(u)

    processed =0

    top_order = []

    while q:

        u = q.popleft()

        top_order.append(u)

        processed +=1

        for v in adj[u]:

            in_degree[v] -=1

            if in_degree[v] ==0:

                q.append(v)

    if processed != len(S):

        return True

    else:

        # compute longest path

        dp = [0]*(n+1)

        max_len =0

        for u in S:

            dp[u] =1

        for u in top_order:

            for v in adj[u]:

                if dp[v] < dp[u] +1:

                    dp[v] = dp[u] +1

        max_len = max(dp[u] for u in S)

        return max_len >=k

But in this code:

- adj is a list of lists for nodes 1..n.

- in_degree is initialized for all nodes (up to n+1), but only nodes in S are considered.

- For the longest path, dp is initialized to 1 for all nodes in S.

But for nodes not in S, dp is 0. But since S is the list of nodes in the X-subgraph, we can ignore them.

But in the code, during the longest path computation, the code iterates over nodes in top_order, which are all in S. So, this is correct.

Now, in the code, the sorted_a is sorted. The binary search proceeds to find the smallest X in sorted_a.

But what if the minimal X is not present in sorted_a? For example, when the minimal X is 2, but sorted_a contains 1,3. But according to earlier reasoning, the minimal X must be one of the a_i's, since the maximum in the path is one of the a_i's.

So, this code should work.

But let's test the third sample input:

Sample input 3:

2 1 5

1 1

Edge 1 2.

k=5.

The code will sorted_a be [1,1].

The binary search will check X=1 (the first mid is 0).

Check function:

S is [1,2].

adj includes edge 1->2.

in_degree for 1 is 0, for 2 is 1.

Kahn's algorithm processes 1 first. Then, 2.

Processed=2 == len(S) (2), so no cycle.

Longest path is 2 steps. Which is less than 5.

So, returns False.

Thus, the code will not find any X and output -1.

Thus, correct.

Another test case: sample input 4.

n=1, m=0, k=1.

sorted_a is [1e9].

check(X=1e9):

S is [1].

adj is empty.

in_degree for 1 is 0.

Kahn's algorithm processes 1. processed=1.

No cycle.

Longest path is 1 >=1. So, returns True.

Thus, code returns 1e9.

Thus, correct.

Now, the code seems correct.

But for the first sample, when X=4, which is not present in the a_i list (the a_i's for nodes are 1,10,2,3,4,5. So, X=4 is present in node 5. So, in the sorted_a list, sorted_a is [1,2,3,4,5,10]. So, the code would find X=4 as the fifth element in the sorted_a.

Thus, the code will find X=4.

Thus, correct.

So, the code seems correct.

Now, the code needs to read inputs properly.

But note that the nodes are 1-based.

Now, let's write the code.
</think>

```python
import sys
from collections import deque

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a = [0] + a  # 1-based indexing
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    
    sorted_a = sorted(a[1:])  # Exclude the dummy 0th element
    
    def check(X):
        S = [u for u in range(1, n+1) if a[u] <= X]
        if not S:
            return False
        # Build adjacency list for S
        adj = [[] for _ in range(n+1)]
        for u, v in edges:
            if a[u] <= X and a[v] <= X:
                adj[u].append(v)
        # Compute in_degree
        in_degree = [0] * (n+1)
        for u in S:
            for v in adj[u]:
                in_degree[v] += 1
        # Kahn's algorithm
        q = deque()
        for u in S:
            if in_degree[u] == 0:
                q.append(u)
        processed = 0
        top_order = []
        while q:
            u = q.popleft()
            top_order.append(u)
            processed += 1
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        if processed != len(S):
            return True
        else:
            # Compute longest path
            dp = [0] * (n+1)
            max_len = 0
            for u in S:
                dp[u] = 1
            for u in top_order:
                for v in adj[u]:
                    if dp[v] < dp[u] + 1:
                        dp[v] = dp[u] + 1
            max_len = max(dp[u] for u in S)
            return max_len >= k
    
    left = 0
    right = len(sorted_a) - 1
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        x_candidate = sorted_a[mid]
        if check(x_candidate):
            answer = x_candidate
            right = mid - 1
        else:
            left = mid + 1
    print(answer if answer != -1 else -1)

if __name__ == "__main__":
    main()
```