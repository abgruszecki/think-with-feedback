<think>
Okay, so I need to solve this problem where I have to find the maximum k such that the directed graph can be colored with k colors following the rule that for every arc u→v, the color of v is the next color after u's color. The colors are cyclic, so after k comes 1 again. The answer has to be the largest possible k ≤ n.

First, let's understand the problem. Each edge u->v imposes a constraint that color[v] = (color[u] + 1) mod k, but since the colors are numbered 1 to k, maybe it's better to think in terms of (color[u] mod k) + 1. Wait, the problem states that for i < k, next is i+1, and for k it's 1. So the next color of i is (i mod k) + 1. So for each edge u→v, the color of v must be exactly (color[u] + 1) mod k, except when color[u] is k, then color[v] is 1. So in terms of modulo arithmetic, color[v] ≡ color[u] + 1 (mod k).

So, for each edge u→v, color[v] ≡ (color[u] + 1) mod k. So this forms a system of constraints. The maximum possible k is the largest divisor of the cycle lengths in the graph. Wait, maybe not. Hmm.

Alternatively, this problem is similar to finding a valid assignment of colors such that for every edge u→v, the color of v is exactly one more than the color of u modulo k. So the maximum possible k is the greatest possible such that all cycles in the graph (in some sense) have lengths that divide k. Because, for a cycle of length L, the colors must increase by 1 each step, wrapping around. So the length of the cycle must be a multiple of k, but since it's a cycle, the total steps around the cycle must sum up to a multiple of k. For example, in a cycle of length L, the sum of increments is L, which must be congruent to 0 modulo k. So L ≡ 0 mod k → k divides L. Therefore, the maximum possible k is the greatest common divisor (gcd) of all cycle lengths in the graph, but also considering the dependencies between cycles. Wait, perhaps not exactly. Because the graph may have multiple cycles, and the k must divide all possible cycle lengths. So the maximum possible k is the gcd of all the possible cycle lengths in the graph. But if the graph has no cycles (i.e., is a DAG), then the only possible k is 1, since there's no cycle, but let's see.

Wait, for example, in the second test case of input 5 2, the graph is two separate edges 1→4 and 2→5. The graph has no cycles. So what's the maximum k? The answer is 5. How? Because for each node, as long as there's no constraints that form cycles, you can assign colors such that the constraints are satisfied. For a DAG, you can arrange the colors in a way that each path has colors increasing by 1 each step. But since there's no cycles, the k can be as large as possible. Wait, but in the second example, the output is 5. Since n=5, k can't exceed 5. So the maximum possible k is n if the graph is a DAG with no cycles. Because then, you can assign each node a unique color. For example, in a DAG, you can topologically sort the nodes and assign colors in the order of the sort. But wait, how do the edges affect that? Because if there's an edge from u to v, then color[v] must be color[u]+1. So if the graph is a DAG, but has edges that form a path, then the colors along that path must form a sequence increasing by 1. So the maximum possible k would be the length of the longest possible path plus 1? Or maybe not. Let's think.

In the second example, nodes are 1,2,3,4,5. Edges are 1→4 and 2→5. There are no cycles. So we can assign colors as follows: 1→4. So color[1] must be one less than color[4]. Similarly, color[2] must be one less than color[5]. But the rest of the nodes (3) have no constraints. So for example, assign color 1 to node 1, color 2 to 4. Assign color 3 to node 2, color 4 to 5. Assign color 5 to node 3. So all constraints are satisfied. So the maximum k is 5. So in this case, since the DAG allows for maximum possible k of n.

So, the problem reduces to finding the largest possible k such that all cycles in the graph have lengths that are multiples of k. So the maximum k is the greatest common divisor of all cycle lengths in the graph. If there are no cycles, then the maximum k is n (since k can be as large as possible, up to n, and the graph can be colored with all colors as per a topological order with no cycles forcing the colors to wrap around).

But how do we compute the cycles' gcd?

Wait, but the graph can have multiple cycles. For example, in the first test case, the graph has two cycles: 1→2→1 (length 2) and 3→4→3 (length 2). The gcd is 2, so the maximum k is 2.

In the third example, the output is 3. Let's see: the graph has a cycle 1→2→3→1 (length 3), and another cycle 1→2→4→1 (length 3). So the gcd is 3. So the maximum k is 3.

In the fourth example, there's a self-loop (1→1) which is a cycle of length 1, so the gcd is 1, hence k=1.

So the problem seems to be: compute the gcd of all cycle lengths in the graph, and then the maximum k is the maximum possible divisor of all cycle lengths, which is their gcd. If there are no cycles, then k is n.

But how to compute the cycles in the graph efficiently, given that n and m can be up to 1e5?

Wait, but finding all cycles in a directed graph is computationally expensive. For large graphs, that's not feasible. So there must be a smarter way.

Alternative approach: the problem requires that for every edge u→v, color[v] = color[u] + 1 mod k. So this is equivalent to the color assignment being a function that is a valid coloring with step increments mod k. So the colors form a function c: V → {1, ..., k} such that for each u→v, c(v) ≡ c(u) + 1 mod k.

But this can be rephrased as c(v) - c(u) ≡ 1 mod k. Which implies that c(v) - c(u) ≡ 1 mod k. So (c(v) - c(u) - 1) ≡ 0 mod k. So (c(v) - c(u) - 1) must be divisible by k. But how can we model this?

Alternatively, considering the colors as elements of Z/kZ (the integers modulo k), then for each edge u→v, c(v) = c(u) + 1 in Z/kZ. So the difference between c(v) and c(u) is 1 mod k. This is similar to a system of equations where each edge u→v imposes c(v) - c(u) ≡ 1 mod k.

But for such a system to be solvable, the graph must be such that all cycles in the graph have a total weight (sum of the equations along the cycle) that is congruent to 0 modulo k. Wait, in this case, each edge contributes a weight of 1 (since c(v) - c(u) = 1). So for any cycle, the sum of the weights around the cycle must be congruent to 0 mod k. Because for a cycle u1 → u2 → ... → uL → u1, the sum of the equations is (c(u2)-c(u1)-1) + (c(u3)-c(u2)-1) + ... + (c(u1)-c(uL)-1) ≡ 0 mod k. But summing all the left-hand sides gives (c(u2) - c(u1) -1) + ... + (c(u1) - c(uL) -1) = (c(u2)-c(u1) + ... + c(u1)-c(uL)) ) - L*1. But the sum of the c terms cancels out: (c(u2) - c(u1)) + (c(u3) - c(u2)) + ... + (c(u1) - c(uL)) = 0. So the total is -L ≡ 0 mod k → L ≡ 0 mod k. So the sum around the cycle is L ≡ 0 mod k. Therefore, k must divide the length L of the cycle.

Therefore, the maximum possible k is the greatest common divisor of all cycle lengths in the graph. So, if the graph has cycles with lengths L1, L2, ..., then the maximum k is the GCD of all these Ls. If there are no cycles, then the maximum k is n. But wait, in the second example, where there are no cycles, the maximum k is n (5), which aligns with this.

So the problem reduces to:

Compute the GCD of all cycle lengths in the graph. If there are no cycles, then the answer is n. Otherwise, the answer is the maximum possible k, which is the GCD of all cycle lengths. But wait, this is not exactly correct. Because the GCD of all cycle lengths may not be the maximum possible. For example, if the graph has cycles of lengths 6 and 9, their GCD is 3, but maybe the maximum k is 3. But perhaps there is a cycle of length 3 in the graph as well. Wait, but the GCD of 6 and 9 is 3, which is the largest possible number that divides both. So even if there are cycles of higher multiples, the GCD remains the same. So the maximum k is the GCD of all cycle lengths in the graph.

But how do we find the GCD of all cycle lengths in the graph? Because enumerating all possible cycles is impossible for large n and m. So we need a smarter way.

Alternative idea: each node's possible color in the system of equations depends on the path taken to reach it. For a valid color assignment, all possible paths from a node u to node v must have the same total length mod k. Otherwise, the color would be inconsistent. So the difference in color between u and v must be equal to the path length mod k. So for any two paths from u to v, their lengths must be congruent mod k. Therefore, for any two cycles in the graph, their lengths must be congruent mod k. Wait, not exactly. Let's think of the difference between two cycles.

Wait, let's consider that for any two cycles C1 and C2, their lengths must be congruent mod k. But that's not necessarily true. The GCD of all cycle lengths must divide each cycle length, so k must divide all cycle lengths. The maximum k possible is the GCD of all cycle lengths.

So the problem is to compute the GCD of all cycle lengths in the graph. But how?

But cycles in a graph can be part of the same strongly connected component (SCC). So perhaps the GCD is computed per each SCC and then the overall GCD is the GCD of all those per-component GCDs.

Wait, no. Because cycles from different components can have their lengths contribute to the overall GCD. For example, if a graph has two separate cycles of lengths 4 and 6, the overall GCD is 2. So the maximum k is 2.

So the approach is to find all cycles in the graph, compute their lengths, and take their GCD. But again, enumerating all cycles is impossible.

Alternative approach inspired by the problem's constraints: for the system of equations to be solvable, the difference between any two paths between two nodes must be congruent to 0 mod k. Therefore, the problem reduces to finding the maximum k such that for every pair of nodes u and v, the difference in path lengths from u to v is congruent to 0 mod k. Wait, no. Because for any two paths from u to v, the sum of their edges (each edge contributing 1) must differ by a multiple of k. So the difference in their lengths (number of edges) must be 0 mod k. Therefore, the value k must be a divisor of all possible differences between any two paths between the same pair of nodes. This is similar to finding the system's period.

But how to model this?

Alternatively, for each node u, the color of u is determined by the color of some other node plus the path length. So the color assignments must form a function where c(v) = c(u) + len(path) mod k for any path from u to v. Therefore, for any two cycles in the graph, their lengths must be congruent mod k, and the GCD of all cycle lengths would be the maximum possible k.

But how to compute this GCD without enumerating all cycles?

Another idea: the GCD can be found by considering the possible differences in cycle lengths. For example, the GCD of a set of numbers can be found as the GCD of all pairwise differences. So perhaps we can model the problem by finding the GCD of all possible cycle lengths.

But again, how to find this without enumerating cycles.

An efficient way to compute the GCD of all cycles in a graph is to model it using the concept of the "potential" function. Each node u has a potential c(u), and for each edge u → v, c(v) must equal c(u) + 1 mod k. So the potentials must satisfy this condition for all edges. The system is solvable if and only if there are no cycles where the sum of the edges (each contributing 1) is not congruent to 0 mod k. So for any cycle, the sum of edges is equal to the cycle length L, and L must be ≡0 mod k. So k must divide L.

Thus, the maximum possible k is the GCD of all cycle lengths in the graph. If there are no cycles, k can be as large as n.

So the problem reduces to finding the GCD of all cycle lengths in the graph. But how?

This seems to require finding all cycles, which is impossible for large n and m. So there's a smarter approach here.

Wait, here's a key insight: the GCD of all cycle lengths in a directed graph can be found by considering the strongly connected components (SCCs) of the graph. For each SCC, compute the GCD of cycle lengths within that component. Then, the overall GCD is the GCD of all these per-component GCDs. Because cycles in different components can't influence each other. Wait, but cycles in different components may have their lengths contribute to the overall GCD. For example, if one component has a cycle of length 4 and another has a cycle of length 6, the overall GCD is 2.

But how to compute the per-component GCD of cycle lengths?

For a strongly connected component (SCC), the GCD of all cycle lengths can be computed as follows:

In a strongly connected directed graph, the GCD of all cycles is equal to the GCD of the lengths of all cycles in a single fundamental cycle basis. But I'm not sure. Alternatively, perhaps there's a way to compute the GCD using BFS or DFS.

Another approach is to find the distances from a root node and compute the differences between the distances along different paths, which can be used to find the GCD.

For example, in a strongly connected component, pick a root node u. For each other node v in the component, compute the distance d from u to v along some path. Then, for any cycle, you can form it by going from u to v (distance d), then taking a path from v back to u (distance e), forming a cycle of length d + e. But this may not capture all possibilities. Alternatively, the difference in distances between two different paths from u to v gives a cycle.

This is similar to the way the GCD is computed in undirected graphs. For example, in an undirected graph, the GCD of all cycles can be found by finding the GCD of the differences in the bipartition of the graph. But for directed graphs, it's more complicated.

Wait, in a directed strongly connected component, for each node v, assign a potential (like distance) d[v]. For each edge u → v, the condition is d[v] ≡ d[u] + 1 mod k. So for the system to have a solution, for any cycle, the sum of 1's along the cycle (the cycle length) must be ≡0 mod k. So k must divide all cycle lengths.

So, for each strongly connected component, we can model the problem as finding the GCD of all possible cycles in that component. Then, the overall GCD is the GCD of all per-component GCDs.

But how to compute the per-component GCD?

This seems challenging. Let's think of a way to model the potentials (d[v]) and find the possible differences.

For a given SCC, let's choose a starting node s. We can perform a BFS or DFS to assign a distance (potential) d[v] to each node v. However, since the edges are directed, we need to track the distances such that along each edge u → v, d[v] = d[u] + 1. If this is possible, then the component's GCD is 1. But if during the BFS/DFS we encounter a contradiction (like a node v already has a distance that doesn't match d[u] + 1), then we can compute the difference and use that to find a possible cycle length, which would contribute to the GCD.

Wait, here's an approach inspired by the BFS method used to detect bipartition in graphs:

Initialize all nodes in the component with d[v] = -1. For the root node s, set d[s] = 0. Then perform a BFS. For each edge u → v, check if d[v] is not set. If not, set d[v] = d[u] + 1. If it is set, check if d[v] equals d[u] + 1. If not, then there's a discrepancy. The discrepancy implies that there's a cycle in the component. The length of this cycle can be computed as follows: the path from u to v via the edge u → v would give a path length of 1. But the existing path from s to v has length d[v], and the path from s to u is d[u], so the existing path from u to v (through other nodes) is (d[v] - d[u]). Adding the current edge u→v (length 1) gives a cycle length of (d[v] - (d[u] + 1)) + 1 = d[v] - d[u]. So the cycle is from u to v through some path (length (d[v] - d[u])) and then back via the edge u→v (length 1) → but that would form a cycle? Wait, maybe not. Let's think.

Suppose s is the root. The existing path from s to u has length d[u], and from s to v has length d[v]. So, the path from u to v in the BFS tree would have length (d[v] - d[u]). But when we encounter an edge u → v, which is not part of the BFS tree, and if d[v] != d[u] + 1, then there's a cycle that can be formed by going from u to v via the existing path (length (d[v] - d[u])) and then via the current edge (length 1). Wait, that's not correct. Let's see:

If the existing path from u to v is of length (d[v] - d[u]), then the path from u to v via that existing path plus the edge u→v would form a cycle of length (d[v] - d[u] + 1). Wait, no. Because the edge u→v would create a cycle only if there's a path from v back to u. But since we are in a strongly connected component, there exists a path from v to u.

So, the cycle can be formed by the path from u to v (existing path) plus the edge v → ... → u (some path), which may have a certain length. But this seems complicated.

Alternatively, the discrepancy (d[v] != d[u] + 1) implies that there's a cycle with length equal to (d[u] + 1) - d[v]. Because when you have a path from s to u (d[u]), then take the edge u→v (length 1), which gives a path length of d[u] + 1. But if the existing path to v is d[v], then the difference is (d[u] +1) -d[v]. So this implies that there's a cycle from v back to u, and the length of that cycle is (d[u] +1 -d[v]) + (existing path from v to u).

Wait, maybe not. Let's think: if we have two paths from s to v: one of length d[v], and another that goes through u via the edge u→v, which would be length d[u] +1. The difference between the two is (d[u] +1) - d[v]. This difference must be congruent to 0 mod k. So for the system to be solvable, k must divide this difference. But the difference is (d[u] + 1) - d[v] = (d[u] - d[v] ) +1. So the cycle formed by going from v back to u (path length L) and then taking u→v (length 1) would have a total length L +1. The difference between the two paths (d[u] +1 and d[v]) implies that L +1 ≡0 mod k. But that's not directly helpful.

But perhaps the discrepancy gives us a value that contributes to the GCD. For example, if in the BFS, we encounter a discrepancy of Δ = (d[u] +1) -d[v], then the GCD of the current component must be adjusted by taking GCD(g, abs(Δ)). This is because the cycle length in this case would have a length that is a multiple of the GCD. So every time we find such a discrepancy, we compute Δ and update the current GCD as gcd(current_gcd, Δ).

So the approach would be:

1. For each SCC in the graph:

   a. Compute the GCD of all cycle lengths within this component.

2. The overall GCD is the GCD of all component's GCDs. If there are no cycles in any component, the answer is n.

3. The maximum k is this overall GCD. However, if there is at least one cycle (i.e., the overall GCD is at least 1), then the maximum k is the overall GCD. If there are no cycles, then the maximum k is n.

But how to compute the per-component GCD?

Let's outline the steps for a single strongly connected component (SCC):

- The component is strongly connected, so there exists at least one cycle.

- We choose a starting node s.

- We perform a BFS or DFS, tracking the potential d[v] as the distance from s (with edges contributing 1). For each edge u → v, we check if d[v] is already set. If it is, we check if d[v] == d[u] + 1. If not, compute the discrepancy Δ = (d[u] + 1) - d[v]. The GCD for the component is the GCD of all such Δs.

The initial component's GCD is 0. For each discrepancy Δ, we update the component's GCD as gcd(current_gcd, abs(Δ)). The initial component's GCD can be set to 0, and then as we process discrepancies, we compute the GCD of all Δs.

Wait, but in a strongly connected component, any cycle's length must be a multiple of the component's GCD, which is the GCD of all possible Δs found during the BFS/DFS. So, the component's GCD is the GCD of all possible discrepancies encountered.

But how?

For example, consider a component with a cycle of length 3 and another cycle of length 6. The GCD would be 3. Suppose during BFS, the first discrepancy found is 3, then another discrepancy of 6. The GCD would be 3. Alternatively, discrepancies could be 3 and 3, leading to GCD 3.

But how to find these discrepancies?

Let's see an example. Take the first test case:

The graph has two cycles of length 2 each (1→2→1 and 3→4→3). Each component is a 2-node cycle.

In the first component (nodes 1 and 2):

We pick s=1. d[1] =0. Then, process edges. For example, edge 1→2: d[2] is set to 1. Then edge 2→1: when processing this edge, since d[1] is 0, we check if d[1] equals d[2]+1. d[2]+1 is 2. But d[1] is 0. So discrepancy Δ = (d[2]+1) - d[1] = (1+1) -0 = 2. So component's GCD is 2. Then, no more edges. So the component's GCD is 2. Similarly for the other component (nodes 3 and 4), the component's GCD is 2. The overall GCD is 2, which is the correct answer.

Another example: the fourth test case has a self-loop (1→1). The component is node 1. Processing this, during BFS:

d[1] =0. Edge 1→1: when processed, since d[1] is already 0, check if 0 equals 0 +1 → 1. No. So Δ = (0+1) -0 =1. Component's GCD is 1. So overall GCD is 1, which is the correct answer.

So this approach seems to work.

So the algorithm steps are:

1. Find all strongly connected components (SCCs) of the graph.

2. For each SCC, if it's a single node with no edges (no self-loops), then it's acyclic. Otherwise, compute the GCD of cycle lengths in the component.

   a. To compute the per-component GCD:

      i. Choose a starting node s in the component.

      ii. Perform BFS/DFS, assigning d[v] as the distance from s (each edge contributes 1).

      iii. For each edge u→v in the component, during BFS/DFS, if d[v] is already set, compute Δ = (d[u] +1) -d[v]. If Δ is not zero, then this contributes to the component's GCD. Compute the GCD of all such Δs.

3. The overall GCD is the GCD of all per-component GCDs. If there are any components with a non-zero GCD (i.e., they have cycles), then the maximum k is this overall GCD. If all components have no cycles (i.e., all per-component GCDs are zero), then the maximum k is n.

But wait, the per-component GCD for a component with cycles is the GCD of all cycle lengths in that component. So the initial approach is to compute this for each component and then take the overall GCD.

But how to compute the per-component GCD correctly.

Another point: when a component has no cycles, like a DAG component (but that's impossible because each component is strongly connected). So any SCC that is strongly connected must have at least one cycle. Unless it's a single node with no self-loops.

So, for each SCC:

- If the component is a single node with no self-loops: no cycle. So contribute nothing to the overall GCD.

- Else: compute the GCD of all cycles in the component.

So the steps for each component are:

- If the component has size 1:

   - If there's a self-loop (edge from the node to itself), then the cycle length is 1. So the component's GCD is 1.

   - Else, no cycle. So component's GCD is 0.

- Else:

   - Compute the GCD of cycle lengths as described earlier.

So how to handle single-node components:

For a single node u, if there are any self-edges (u→u), then the component's GCD is 1 (since the cycle length is 1). Otherwise, no cycle (contributes 0 to the overall GCD).

Now, for components with size >1:

We need to compute the GCD of all cycles in the component. As per the earlier approach, during BFS/DFS, track discrepancies and compute GCD.

So the steps for such a component:

1. Choose a node s as the starting point.

2. Initialize d[s] = 0, and all other nodes in the component as -1.

3. Use a queue to process nodes. For each node u dequeued:

   a. For each neighbor v in the component:

      i. If d[v] is -1, set d[v] = d[u] +1, and enqueue it.

      ii. Else, check if d[v] == d[u] +1. If not, compute Δ = (d[u] +1) - d[v]. Then, compute the current component's GCD as gcd(current_gcd, abs(Δ)).

4. After processing all nodes, the component's GCD is the computed GCD. If no discrepancies were found (i.e., the component's GCD remains 0 initially?), then the component's GCD is the GCD of all cycle lengths. Wait, but if there's no discrepancies, that implies that all edges are part of a tree, but the component is strongly connected, so there must be cycles and discrepancies.

Hmm, perhaps the initial component's GCD is 0. Then, whenever a discrepancy is found, we update the GCD with Δ. If no discrepancies are found, then there are no cycles (but that's impossible in a strongly connected component with size>1).

Wait, no. For example, a component with a cycle of length 3. Let's see:

Nodes 1→2→3→1.

Starting at node 1, d[1] =0. Process edges:

1→2: d[2]=1.

2→3: d[3]=2.

3→1: Check d[1] which is 0. Now, d[1] should be (3→1) d[3]+1=3. So Δ =3 -0=3. So component's GCD becomes 3.

Then, during processing other edges (if any), no more discrepancies. So the component's GCD is 3.

Which is correct.

But in this case, the cycle length is 3, which is the GCD.

Another example: component with two cycles of lengths 2 and 4. The GCD should be 2.

Suppose the component has nodes 1→2→1 (length 2) and 1→3→4→1 (length 3 → no, wait, no. Let's create a component with two cycles: 1→2→1 (length 2) and 1→3→4→1 (length 3). Then the cycles' lengths are 2 and 3, GCD is 1. So the maximum k would be 1.

But according to the algorithm, during BFS:

s=1.

Process edges:

1→2: d[2] =1.

1→3: d[3]=1.

Now, 2→1: check if d[1] (0) == d[2]+1 (1+1=2). No. Δ is 2-0=2. So component's GCD is 2.

Then, 3→4: d[4] =2.

4→1: check if d[1] (0) == d[4]+1 (3). No. Δ is 3-0=3. So component's GCD becomes gcd(2,3) =1.

So the algorithm computes the GCD of 2 and 3 as 1, which is correct.

So this approach works.

Therefore, the algorithm steps are:

For each SCC:

   if the component is a single node:

      if it has a self-loop, component_gcd =1.

      else, component_gcd =0.

   else:

      perform BFS/DFS to assign d[v], compute all discrepancies Δ and compute their GCD.

      component_gcd = the GCD of all Δs.

      if component_gcd ==0 (no discrepancies found → but this is impossible for a strongly connected component with size>1. So perhaps if no discrepancies are found, it implies that all cycles in the component have length 0 mod 0 → which is not possible. Hence, this case can be ignored. Or perhaps when component_gcd is 0, it's treated as no cycles, but that's impossible.)

      So, for a component of size >1, component_gcd must be at least 1 if it's strongly connected.

Once all components are processed, collect all component_gcd values that are >0 (since those components contribute to cycles). The overall_gcd is the GCD of all these component_gcd values. If there are no such values (all components are a single node without self-loops), then the answer is n. Otherwise, the answer is overall_gcd.

But wait, the component_gcd for a component can be 0 only if it's a single node with no self-loop. So when collecting the component_gcds, we can ignore the 0s (as they contribute no cycles). So the overall_gcd is the GCD of all non-zero component_gcds.

If there are no non-zero component_gcds (i.e., all components are acyclic), then the answer is n. Else, the answer is overall_gcd.

So the steps are:

1. Find all SCCs.

2. For each SCC:

   a. Compute component_gcd as per the rules above.

3. Collect all component_gcds that are >0.

4. If the list is empty → answer is n.

5. Else → answer is the GCD of all component_gcds in the list.

But wait, the example where a component's GCD is 2 and another's is 3. The overall_gcd is 1. Which is correct.

So this approach seems correct.

Now, implementing this in Python:

First, we need to find all SCCs. For that, we can use Tarjan's algorithm or Kosaraju's algorithm. Since the constraints are up to 1e5 nodes and edges, we need an O(n + m) algorithm.

Tarjan's algorithm is O(V + E), which is acceptable.

Once the SCCs are found, for each component, process them as per the rules.

For each component (SCC):

If the component has size 1:

   if there are any self-edges (u→u), then component_gcd is 1.

   else, component_gcd is 0.

Else:

   Perform BFS or DFS, assign d[v], track discrepancies.

   Compute the GCD of all discrepancies found.

Now, to track discrepancies:

We can initialize a variable current_gcd to 0. For each discrepancy Δ, we compute current_gcd = gcd(current_gcd, abs(Δ)).

Once all edges are processed, the component_gcd is current_gcd if current_gcd is non-zero. Else, it's zero (but this shouldn't happen for components with size >1 and strongly connected).

But how to efficiently process all edges in the component and check for discrepancies.

In practice, for each component:

- We need to iterate through all edges within the component. Wait, but the graph is directed, and each component is a strongly connected component. So for each node u in the component, all edges u→v must also be in the same component (since the component is strongly connected). So, during processing of a component, we can iterate all edges of the nodes in the component, but only consider those edges where v is also in the component.

But storing the edges per node is straightforward. For example, we have an adjacency list. For each node u in the component, we process all edges u→v. For each such edge, if v is in the same component, then we check if d[v] is set. If not, set it. If it is set, check if d[v] == d[u]+1. If not, compute Δ and update the current_gcd.

But how to check whether v is in the same component. So during the SCC decomposition, we can assign each node to a component (like a list of components, each being a list of nodes). For each node, we can have a component ID, so that we can check if u and v are in the same component.

So, steps for per-component processing (size >1):

- Assign component ID to each node in the component.

- For each node u in the component:

   - For each neighbor v in adjacency list:

      - if v is in the same component:

         - process the edge u→v.

Thus, during BFS/DFS for a component, for each edge u→v in the adjacency list, we only process it if v is in the same component.

Now, code outline:

Read n and m.

Read m edges. Build adjacency list.

Compute SCCs.

For each SCC:

   if len(SCC) ==1:

      check if any self-loop exists (u→u in edges).

      component_gcd is 1 if self-loop exists, else 0.

   else:

      perform BFS/DFS to assign d values, compute discrepancies.

      component_gcd is the GCD of all discrepancies.

Collect all component_gcds that are >0.

If none → answer is n.

Else → answer is GCD of all component_gcds.

Now, let's think about the implementation.

Implementing SCC with Tarjan's algorithm.

But in Python, for large n and m (1e5), recursion depth can be a problem for Tarjan's algorithm (which uses recursion). So better to use iterative Tarjan or Kosaraju's algorithm.

Kosaraju's algorithm is more straightforward to implement iteratively.

Kosaraju's steps:

1. Perform a DFS on the original graph, pushing nodes onto a stack in the order of completion.

2. Reverse the graph.

3. Process nodes from the stack in reverse order, performing DFS on the reversed graph to find SCCs.

So, in code:

def kosaraju(n, adj):

    visited = [False] * (n +1) # nodes are 1-based?

    order = []

    # first pass: fill order

    for node in range(1, n+1):

        if not visited[node]:

            stack = [(node, False)]

            while stack:

                u, processed = stack.pop()

                if processed:

                    order.append(u)

                    continue

                if visited[u]:

                    continue

                visited[u] = True

                stack.append( (u, True) )

                for v in adj[u]:

                    if not visited[v]:

                        stack.append( (v, False) )

    # transpose the graph

    transpose = [[] for _ in range(n+1)]

    for u in range(1, n+1):

        for v in adj[u]:

            transpose[v].append(u)

    # second pass to find SCCs

    visited = [False]*(n+1)

    sccs = []

    for node in reversed(order):

        if not visited[node]:

            stack = [node]

            visited[node] = True

            component = []

            while stack:

                u = stack.pop()

                component.append(u)

                for v in transpose[u]:

                    if not visited[v]:

                        visited[v] = True

                        stack.append(v)

            sccs.append(component)

    return sccs

This is the Kosaraju's algorithm.

Once we have the SCCs, we process each component.

For each component:

If len(component) ==1:

   check if any self-loop exists (u→u in edges). So for node u, check if there's an edge from u to u.

Else:

   for the component, build a subgraph (only nodes in component, edges between them).

   perform BFS/DFS to assign d[u] as the distance from a starting node.

   for each edge u→v in the component:

      if d[v] is not set → set it.

      else → check if d[v] == d[u] +1. If not, compute Δ = (d[u]+1 -d[v]), then update current_gcd.

But how to iterate all edges in the component.

But the adjacency list is for the entire graph. So for each node u in the component, we have to iterate all outgoing edges u→v, and check if v is in the same component. If yes, then process the edge.

Thus, during processing a component (size >1):

current_gcd =0

component_nodes = set(component)

start_node = component[0]

d = {node: -1 for node in component}

d[start_node] =0

from collections import deque

queue = deque()

queue.append(start_node)

while queue:

    u = queue.popleft()

    for v in adj[u]:

        if v not in component_nodes:

            continue # skip edges outside component

        if d[v] == -1:

            d[v] = d[u] +1

            queue.append(v)

        else:

            # discrepancy found

            delta = d[u] +1 - d[v]

            if delta !=0:

                current_gcd = math.gcd(current_gcd, abs(delta))

Thus, after processing all edges within the component, the current_gcd is the component's GCD.

But wait, in the code above, for each u in the queue, we process all outgoing edges. For each edge u→v in the component, if v is in the component, we check if d[v] is set. If not, set it. Else, compute delta.

But this is not correct. Because during BFS, the edges may be processed in any order. For example, an edge u→v that is not part of the BFS tree may be processed after v's d has been set by another path.

But this is exactly the case where discrepancies are found. For example, when two different paths reach v with different d values, leading to a delta.

So the code above correctly captures all such discrepancies.

But how to make sure that all edges within the component are processed.

In the code above, when u is processed (dequeued), we iterate all edges u→v. For each v in the component, we process the edge. So if v is in the component, the edge is processed.

Thus, for the component's edges, all edges are processed. Because each node in the component is processed once (since it's part of BFS), and all outgoing edges from each node are checked.

Thus, for all edges within the component, we check them during BFS.

But what about edges that are not part of the BFS tree? For example, cross edges or back edges. Those edges are still processed as part of the outgoing edges of their u nodes.

Thus, this approach should capture all discrepancies.

But wait, the code for processing the edges is part of the BFS loop. So when u is processed, we iterate all outgoing edges of u, including those that have already been processed. For example, after processing u's edges, when another node w has an edge to v that was already processed, that edge will be checked again when w is processed.

But this is redundant. For example, when u and w are both in the component and have edges to v. But the code would process each edge once when the 'u' node is dequeued.

Thus, for all edges within the component, they are processed exactly once (when their u is dequeued). So the code is correct.

Now, let's think about the time complexity. For each component, the BFS processes each node in the component once. For each edge in the component, it's processed once. So the total time for all components is O(n + m), which is acceptable for 1e5.

Thus, the code can handle the constraints.

Now, putting it all together.

But we need to process the components and track their GCDs.

In code:

import sys
import math
from sys import stdin
from collections import deque

def main():
    n, m = map(int, stdin.readline().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, stdin.readline().split())
        adj[u].append(v)

    # Compute SCCs using Kosaraju's algorithm
    visited = [False] * (n +1)
    order = []
    for node in range(1, n+1):
        if not visited[node]:
            stack = [(node, False)]
            while stack:
                u, processed = stack.pop()
                if processed:
                    order.append(u)
                    continue
                if visited[u]:
                    continue
                visited[u] = True
                stack.append( (u, True) )
                for v in adj[u]:
                    if not visited[v]:
                        stack.append( (v, False) )

    # Build transpose graph
    transpose = [[] for _ in range(n+1)]
    for u in range(1, n+1):
        for v in adj[u]:
            transpose[v].append(u)

    visited = [False]*(n+1)
    sccs = []
    for node in reversed(order):
        if not visited[node]:
            stack = [node]
            visited[node] = True
            component = []
            while stack:
                u = stack.pop()
                component.append(u)
                for v in transpose[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            sccs.append(component)

    component_gcds = []
    for component in sccs:
        if len(component) ==1:
            # Check for self-loop
            u = component[0]
            has_self_loop = False
            for v in adj[u]:
                if v == u:
                    has_self_loop = True
                    break
            if has_self_loop:
                component_gcds.append(1)
            else:
                continue # no contribution to GCD
        else:
            component_set = set(component)
            start_node = component[0]
            d = {u: -1 for u in component}
            d[start_node] =0
            current_gcd =0
            queue = deque([start_node])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if v not in component_set:
                        continue
                    if d[v] == -1:
                        d[v] = d[u] +1
                        queue.append(v)
                    else:
                        delta = (d[u] +1) - d[v]
                        if delta !=0:
                            current_gcd = math.gcd(current_gcd, abs(delta))
            # After processing all edges, component's GCD is current_gcd
            if current_gcd ==0:
                # No cycles? Impossible for strongly connected component with size>1.
                # So this must have at least one cycle. But how?
                # Maybe all cycles have length 0 mod current_gcd (0), which is impossible. So this case is invalid.
                # But current_gcd is 0 only if no discrepancies were found. But in a strongly connected component of size>1, there must be cycles.
                # So this situation is impossible. Hence, current_gcd must be at least 1.
                # So perhaps we should set current_gcd to some value.
                # But how to handle this?
                # For example, a component where all cycles have length 0 mod k. But k=0 is not possible. So this case is impossible.
                # So perhaps this situation indicates that there's a cycle with length 0, which is impossible. So this code must not be reachable.
                # So for safety, we can skip adding component_gcd if current_gcd is 0.
                # But this is a problem.
                # For example, a component of two nodes: 1 → 2 → 1. The BFS would process 1, then 2, then when processing 2 →1, delta is (d[2]+1) -d[1] = (1+1) -0 =2. So current_gcd is 2.
                # So current_gcd can't be zero.
                # So the case where current_gcd is zero can't happen. Hence, we can safely add current_gcd to the list.
                # So in code, even if current_gcd is zero, add it. But this shouldn't happen.
                pass
            else:
                component_gcds.append(current_gcd)
    if not component_gcds:
        print(n)
    else:
        overall_gcd = component_gcds[0]
        for g in component_gcds[1:]:
            overall_gcd = math.gcd(overall_gcd, g)
        print(overall_gcd if overall_gcd !=0 else n)
        
if __name__ == "__main__":
    main()

Testing this code against the examples.

First example:

Input:

4 4
1 2
2 1
3 4
4 3

The code should output 2.

The SCCs are [1,2], [3,4]. Each has component_gcd 2.

Overall GCD is 2.

Second example:

5 2
1 4
2 5

The SCCs are [1], [2], [3], [4], [5]. All components have size 1. Check for self-loops: none. So component_gcds is empty. Thus, output is 5.

Third example:

4 5
1 2
2 3
3 1
2 4
4 1

SCC is [1,2,3,4]. Processing this component:

During BFS:

start_node=1.

d[1]=0.

Process edges 1→2: d[2] becomes 1.

Process edges 2→3: d[3]=2.

3→1: delta is (2+1) -0=3. current_gcd is 3.

Then, 2→4: d[4] is -1, set to 2.

4→1: delta is (2+1) -0=3. current_gcd is gcd(3,3)=3.

So component_gcd is 3. So output is 3.

Fourth example:

4 4
1 1
1 2
2 1
1 2

The SCCs are [1,2], [3], [4]. 

The component [1,2]:

Processing edges:

start_node=1.

d[1] =0.

1→1: v is in component. d[1] is 0. So delta is (0+1) -0=1. current_gcd is 1.

Then, 1→2: d[2] is -1, set to 1.

2→1: delta is (1+1) -0=2 → current_gcd becomes gcd(1,2)=1.

Thus, component_gcd is 1.

Also, the self-loop in component [1,2] is processed.

So component_gcds is [1], which is the output.

So the code works for the examples.

But in the fourth example, there is also a self-loop in component [1], which has component_gcd 1. But the component [1,2] is processed as a single component. So the code should correctly output 1.

Yes.

Thus, the code should be correct.
</think>

```python
import sys
import math
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
    
    # Kosaraju's algorithm to find SCCs
    visited = [False] * (n + 1)
    order = []
    for node in range(1, n+1):
        if not visited[node]:
            stack = [(node, False)]
            while stack:
                u, processed = stack.pop()
                if processed:
                    order.append(u)
                    continue
                if visited[u]:
                    continue
                visited[u] = True
                stack.append((u, True))
                for v in adj[u]:
                    if not visited[v]:
                        stack.append((v, False))
    
    transpose = [[] for _ in range(n+1)]
    for u in range(1, n+1):
        for v in adj[u]:
            transpose[v].append(u)
    
    visited = [False] * (n + 1)
    sccs = []
    for node in reversed(order):
        if not visited[node]:
            component = []
            stack = [node]
            visited[node] = True
            while stack:
                u = stack.pop()
                component.append(u)
                for v in transpose[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            sccs.append(component)
    
    component_gcds = []
    for component in sccs:
        if len(component) == 1:
            u = component[0]
            if any(v == u for v in adj[u]):
                component_gcds.append(1)
        else:
            component_set = set(component)
            start = component[0]
            d = {u: -1 for u in component}
            d[start] = 0
            current_gcd = 0
            q = deque([start])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if v not in component_set:
                        continue
                    if d[v] == -1:
                        d[v] = d[u] + 1
                        q.append(v)
                    else:
                        delta = (d[u] + 1) - d[v]
                        if delta != 0:
                            current_gcd = math.gcd(current_gcd, abs(delta))
            if current_gcd != 0:
                component_gcds.append(current_gcd)
    
    if not component_gcds:
        print(n)
    else:
        overall_gcd = component_gcds[0]
        for g in component_gcds[1:]:
            overall_gcd = math.gcd(overall_gcd, g)
        print(overall_gcd)

if __name__ == "__main__":
    main()
```