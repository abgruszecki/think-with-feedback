<think>
Okay, let's tackle this problem. Hmm. So, the problem is about determining the number of valid ways to fill in the unknown relationships between characters such that all possible triplets of characters satisfy certain conditions. The conditions are that every triplet either has exactly one pair in love or all three pairs in love. And the answer has to be modulo 1e9+7.

First, I need to understand the constraints on the relationships. Let's rephrase the problem's condition for a triplet (A, B, C). The triplet is acceptable if either:

1. Exactly one pair is in love, and the other two pairs hate each other. Or,
2. All three pairs are in love.

Wait, but wait. The problem statement says that for any three characters, the triplet should satisfy that either exactly one pair is in love (so the other two pairs are hate) OR all three pairs are in love. Because the user hates love triangles (like two pairs are love, and the third is hate) and also hates when nobody is in love (all three pairs hate each other).

So the allowed cases are:

- Exactly one love pair in the triplet (the other two are hate).
- All three love pairs.

So for any three characters, those are the only possibilities that make the user happy.

Now, how to model this. Let's think about the relationships between pairs. Each pair is either love (1) or hate (0). The constraints must hold for every possible triplet.

This seems similar to some kind of graph problem where edges have binary states, and certain structural conditions must hold. But for triplets, which are combinations of edges. So perhaps there's a structure here that can be represented in terms of graph properties.

Let me consider possible structures. Let's say that the graph is such that all the love edges form a collection of cliques. Wait, but in a clique, all pairs are love. If two people are in the same clique, their pair is love. Then, for any triplet within a clique, all three pairs are love. That's acceptable. For triplets that involve two from the same clique and one from another, maybe not.

Wait, maybe the structure must be that all love edges form a collection of cliques, and within each clique, all pairs are love. Then, any triplet that's entirely within a clique is okay. But what about triplets that cross cliques?

Alternatively, maybe the only allowed structures are that the love relationships form a graph where each connected component is a complete graph (clique), and between any two different components, all pairs hate each other.

Let's think: If the love edges form a graph where each component is a clique, and all pairs between different components are hate, then for any triplet:

- If all three are in the same clique: all three pairs are love. So that's acceptable.
- If two are in one clique and the third is in another: the two in the same clique love each other. The other two pairs (each involving the third from another clique) are hate. So in the triplet, there's exactly one love pair (the two in the same clique), and the other two pairs are hate. So that's acceptable.

So this structure would satisfy all the triplet conditions. So the problem reduces to checking if the existing relationships can be partitioned into such a structure, and then computing the number of possible valid structures.

Wait, because in this case, the way to assign relationships is to partition the nodes into some cliques (connected components, each a clique) where all edges within are love, and edges between are hate. Then, any triplet will either be all within a clique (all love) or have exactly one pair in love (if two are in a clique and the third is in another). So this structure satisfies the problem's conditions.

So the problem is equivalent to checking if the given constraints allow for such a partition. Each connected component (in the love graph) must be a clique. Because, if two nodes are in the same component (so they must love each other), but there's a pair in the component that hates, that's a contradiction.

Wait, no. Wait, the love graph is the graph where edges are love. So if two nodes are in the same component (connected via love edges), but there's a pair in the component that is not connected by a love edge (i.e., they hate), then that's a problem. Because according to the structure, all pairs within a component must love each other.

So the existing edges must form a collection of cliques, where all edges within a clique are love, and edges between cliques are hate.

So the problem reduces to:

The love edges must form a set of cliques. Moreover, any pair in the same clique must love each other, and pairs in different cliques must hate each other.

Thus, the problem is equivalent to determining if the existing constraints are compatible with this structure, and if so, how many such structures are possible (given the unknown edges) modulo 1e9+7.

So the approach is to model this as a graph where each connected component (based on love edges) is a clique. Then, the solution is the number of ways to partition the nodes into cliques such that all existing edges are satisfied.

Now, how to model this.

First, for each existing love edge (c=1), the two nodes must be in the same clique. Moreover, every pair in the same clique must have a love edge. So if there's a love edge between a and b, then a and b must be in the same clique, and all other pairs in the clique must also have love edges. If there's any existing hate edge (c=0) between two nodes in the same clique, that's impossible, so the answer is 0.

Similarly, for existing hate edges (c=0), the two nodes must be in different cliques. So if a and b have a hate edge, then they can't be in the same clique. If in our structure, they are in the same clique, that's impossible.

So the steps are:

1. Check all existing love edges to form connected components. Since all nodes in the same component must form a clique, any existing love edge between a and b implies that they are in the same clique. Moreover, all pairs in that clique must have love edges. So, for any two nodes in the same component, if there is an existing edge (either love or hate), if it's a hate edge, then it's invalid. So for all pairs in the same component, if there's a known relationship, it must be love.

2. Check all existing hate edges. For any two nodes in the same component (as determined by the love edges), the existing hate edge is invalid. Because they should love each other. So any existing hate edge between nodes in the same component (based on love edges) is invalid.

Wait, but the components are determined by the love edges. So the components are formed by connecting nodes that are connected via love edges. So if two nodes are in the same component (i.e., connected via a path of love edges), then they must be in the same clique, and thus their edge must be love. So any existing edge between them (if present) must be love. Otherwise, it's impossible.

So the approach is:

- For the love edges, model the connected components (using DSU/Union-Find). All nodes in the same component must form a clique, so any existing edge between them must be love.

- For each existing edge (ai, bi, ci):

   - If ai and bi are in the same component (based on love DSU), then ci must be 1. Otherwise, it's invalid.

   - If ai and bi are in different components, then if the edge is a love edge (ci=1), then the two components must be merged. Because, the existing love edge implies they are in the same clique. But merging may require that all existing edges between the components are love. Wait, no. Wait, if two components are connected by a love edge, then those two cliques must be merged into one big clique. But that's only possible if all existing edges between any two nodes in the merged component are love.

Wait, this is getting complicated. Let's think again.

Suppose we have a DSU structure where each component represents a clique. For two nodes u and v, if they are in the same component, then their edge must be love. If they are in different components, their edge must be hate.

But existing edges can impose constraints. For example:

- If there's an existing love edge (ci=1) between u and v, then they must be in the same component (same clique). So when processing the existing love edges, we need to merge their components.

But when merging two components, we need to check if there's any existing hate edges between nodes of these two components. Because if two components are merged, any existing edges between nodes from the two components must be love. Because, after merging, all edges within the merged component are love. So if any existing edge between nodes in the two components is hate, then merging would be invalid.

Wait, but existing edges between nodes in the two components could be love or hate. Suppose there's a love edge between u and v, which are in different components. We need to merge their components. But if there's an existing edge (ci=0) between a node in u's component and a node in v's component, that's a problem.

So the correct approach is:

- We process the existing edges in such a way that:

   a. All love edges (ci=1) must form a structure where their connected components (when merged via these edges) are cliques.

   b. All hate edges (ci=0) must be between nodes of different components (after processing all love edges and merging their components).

But how do we check this?

Here's a possible approach:

1. Use a Union-Find (DSU) data structure to track the connected components of the love edges. For each love edge (ci=1) between u and v, we merge their components. However, when merging, we need to check if all existing edges between the two components (before merging) are love. Because after merging, any pair of nodes in the merged component must love each other. So if there was a hate edge between any two nodes in the merged component, that's invalid.

Wait, but the love edges are the ones that are processed first. Wait, maybe not. Let's think: All love edges must be part of the same component. So when adding a love edge between u and v, u and v must be in the same component. However, existing edges between any two nodes in their component (after merging) must be love.

Alternatively, perhaps the process is:

- For all love edges (ci=1), we need to merge their components. But when merging, we must check that all existing edges between any two nodes in the merged component are love. Otherwise, merging is impossible.

But how to efficiently check this? Because for large n and m, checking all pairs in the merged components is O(n^2), which is not feasible.

So this suggests that the approach of processing love edges first and merging components may not be feasible, given the constraints.

So perhaps there's a different way to model this. Let's think again.

Each component (clique) must have all pairs love. So, for any two nodes in the same component, if there's a known edge (love or hate), it must be love. Otherwise, the configuration is invalid.

So the steps are:

- For each existing edge (ai, bi, ci):

   - If ai and bi are in the same component (clique), then ci must be 1.

   - If ai and bi are in different components, then ci must be 0.

But how do we model the components? Because the components are determined by the love edges. Wait, but the components are the cliques where all pairs love each other. So the components are formed such that all pairs within the same component must have love edges, and pairs between components must have hate edges.

So the components are the equivalence classes where any two nodes in the same class must have a love edge, and any two nodes in different classes must have a hate edge.

Thus, the problem is to partition the nodes into some number of components (cliques) such that:

- For every existing love edge (ci=1), ai and bi are in the same component.

- For every existing hate edge (ci=0), ai and bi are in different components.

Moreover, any two nodes in the same component must have a love edge (so if there's an existing edge between them, it must be love), and any two nodes in different components must have a hate edge (so if there's an existing edge between them, it must be hate).

So the approach is to model this as a graph where the components are determined by the existing constraints. If any of the existing edges violate the required conditions (like a love edge between two different components, or a hate edge between two nodes in the same component), then the answer is 0.

So the steps to solve this are:

1. Check all existing edges for validity. For each existing edge (a, b, c):

   a. If a and b are in the same component (clique), then c must be 1. Otherwise, invalid.

   b. If a and b are in different components, then c must be 0. Otherwise, invalid.

But how do we determine the components? Because the components are formed by the constraints that all love edges must be within a component, and hate edges must be between components.

This sounds like a bipartition problem, but generalized. The components are equivalence classes where all nodes in the same component are connected by love edges, and any two components are connected by hate edges.

Thus, the components must form a structure where the love edges form a set of cliques (each component is a clique of love edges), and between components, all edges are hate.

So the problem reduces to building such a structure based on the existing edges.

The way to model this is to use a Union-Find data structure to track the components. For each love edge (c=1), we must merge the components of a and b. For each hate edge (c=0), a and b must be in different components.

But how to handle this? Because the hate edges impose that the two nodes are in different components. So when processing a hate edge, if the two nodes are already in the same component, the answer is 0.

But for love edges, merging components. However, when merging, we need to check that there are no hate edges between any nodes in the merged components. Because once merged, any existing hate edge between any two nodes in the merged component would be invalid.

Wait, that's not correct. Suppose we have two components A and B. We merge them because there's a love edge between a node in A and a node in B. But if there was an existing hate edge between a node in A and a node in B, that's a problem because after merging, the hate edge is between nodes in the same component, which is invalid.

So when processing a love edge (a, b, 1):

   - Check if a and b are in different components. If yes, then before merging, check all existing edges between any node in a's component and b's component. For any such edge, if it's a hate edge, then merging is invalid. If any such edge is a love edge, then it's okay.

But how to check this efficiently? For example, if components are large, checking all existing edges between the two components is O(m), which is not feasible for m up to 1e5.

This seems computationally expensive. So perhaps this approach is not feasible.

Alternatively, perhaps the problem can be modeled as a graph where each component must be a clique (so all existing edges within a component are love edges), and all edges between components are hate edges.

Thus, the steps would be:

- All love edges must be within a component.

- All hate edges must be between different components.

- Additionally, for all pairs of nodes in the same component, any existing edge must be a love edge.

So the process is:

1. For each existing love edge (a, b, 1):

   a. Check if a and b are in different components. If so, check if there are any existing hate edges between any pair of nodes in a's component and b's component. If any exist, the answer is 0. Otherwise, merge the two components.

   b. If a and b are already in the same component, proceed.

2. For each existing hate edge (a, b, 0):

   a. Check if a and b are in the same component. If yes, answer is 0.

   b. Else, ensure that there are no love edges between a and b. Wait, but existing love edges between a and b would have been processed in step 1, leading to their components being merged, which would conflict with the hate edge.

Wait, maybe the steps are:

First, process all love edges, merging their components. But during merging, check that there are no existing hate edges between any nodes in the two components. Because if there is such a hate edge, then merging the components would imply that the hate edge is within the same component, which is invalid.

Similarly, process all hate edges, ensuring that their nodes are in different components. If any hate edge's nodes are in the same component, it's invalid.

But how to handle checking existing edges between two components when merging them.

This seems impossible for large n and m. So perhaps this approach is not feasible. So what's the alternative?

Alternative approach:

The problem requires that the graph is partitioned into components such that:

- All edges within a component are love.

- All edges between components are hate.

Thus, the components form a partition of the nodes where:

1. For every existing love edge (a, b), a and b must be in the same component.

2. For every existing hate edge (a, b), a and b must be in different components.

3. All pairs within the same component must have love edges (so any existing edge between them must be love).

4. All pairs between different components must have hate edges (so any existing edge between them must be hate).

So the solution is possible only if the components can be partitioned such that all existing edges are compatible with the above rules.

Thus, the problem can be modeled as a bipartition problem with constraints. The constraints are:

- All love edges are intra-component.

- All hate edges are inter-component.

Additionally, any existing edges between nodes in the same component must be love, and existing edges between different components must be hate.

So, the steps to check are:

1. Check all existing love edges. For each love edge (a, b), a and b must be in the same component. So process these edges using DSU to merge the components of a and b.

   - However, if during this process, merging two components would result in an existing hate edge between any two nodes in the merged component, the answer is 0.

But how to check for existing hate edges between any two nodes in the merged components?

This seems computationally expensive. So perhaps this is not the way.

Alternative idea: When merging two components, check if there's any hate edge between a node in the first component and a node in the second component.

If there is such a hate edge, then merging them would create a component where that hate edge is now within the component, which is invalid.

So during processing, for each love edge (a, b), check if a and b are in the same component. If not:

   - Check if there exists any hate edge between any node in a's component and any node in b's component. If yes, then merging is impossible, answer 0.

But how to check that quickly.

This requires, for each component, to track all nodes in it, and for each component pair, check if any hate edges exist between them. But with n up to 1e5 and m up to 1e5, this is not feasible.

Alternative idea: For each hate edge (x, y), store that x and y must be in different components. So when merging components via love edges, if any hate edge exists between nodes in the merged components, the answer is invalid.

But how to track this.

Another approach: The problem is to find a partition of the nodes into components such that:

   a. For every love edge (u, v), u and v are in the same component.

   b. For every hate edge (u, v), u and v are in different components.

Additionally, all pairs within a component must have no existing hate edges, and all pairs between components must have no existing love edges.

So the steps are:

1. For all love edges, merge their nodes into the same component. Use DSU for this.

   - However, merging must ensure that there are no existing hate edges between any nodes in the merged components.

But how to track this.

Alternatively, the DSU is only valid if merging via love edges doesn't merge components with existing hate edges between them.

Another idea: The DSU represents the components. For any two nodes in the same component, there must be no existing hate edges between them.

So during the merging process for love edges, we must check if any of the existing hate edges in the graph connect nodes that are in the same component.

But again, how to track this.

Alternatively, process all existing edges first:

- For each existing love edge (u, v, 1):

   - If u and v are in different components, merge them. However, before merging, check if there are any existing hate edges between any nodes in u's and v's components. If yes, answer is 0.

But again, how to check this.

Alternatively, for each hate edge (u, v, 0), we can track that u and v must not be in the same component. So when merging components via love edges, we must ensure that merging doesn't connect any pair of nodes that are connected by a hate edge.

Wait, but if u and v are connected by a hate edge, then they must be in different components. So, during the DSU process for love edges, if u and v are in the same component, then the hate edge (u, v) is invalid.

So the steps could be:

1. Build the DSU structure for love edges. For each love edge (u, v), union their components.

2. Check all existing edges for validity:

   a. For each love edge (u, v, 1): if u and v are in different components, then the DSU structure is invalid. Because love edges should be within the same component. Wait, no. Because love edges are processed to merge components. So during processing, all love edges are processed first, merging their components. So after processing all love edges, any love edge must have u and v in the same component.

   b. For each hate edge (u, v, 0): check if u and v are in the same component. If yes, then invalid.

3. Additionally, check for all pairs of nodes in the same component whether there exists a hate edge between them. Because according to the problem's conditions, all pairs in the same component must love each other. So any existing hate edge between two nodes in the same component is invalid.

But how to check this.

But step 3 is O(m), but m can be up to 1e5. So for each hate edge (u, v, 0), check if u and v are in the same component. If any, answer is 0.

That's part of step 2b.

Wait, yes. Because any existing hate edge (u, v) must have u and v in different components. So during step 2b, for each hate edge, if u and v are in the same component, answer is 0.

So steps:

1. Process all love edges to build DSU. For each love edge (u, v), union u and v.

2. For all existing edges (u, v, c):

   a. If c == 1:

      - Check if u and v are in the same component. If not, answer is 0.

   b. Else (c == 0):

      - Check if u and v are in the same component. If yes, answer is 0.

3. Additionally, for all pairs of nodes u and v in the same component, check if there's an existing edge between them with c=0. But how? This is covered in step 2, because all existing edges are processed in step 2. For example, if u and v are in the same component and have a hate edge (c=0), step 2b will detect this and return 0.

Thus, steps 1 and 2 check all existing edges for validity.

Once the DSU is built and the existing edges are validated, the next step is to calculate the number of valid assignments.

The valid assignments are determined by the way we can partition the nodes into components such that:

- All existing edges are compatible (processed as above).

- All pairs in the same component are love.

- All pairs in different components are hate.

The unknown edges must be filled in a way that follows these rules.

Now, for the unknown edges (pairs not present in the input), their values are determined by whether the two nodes are in the same component (love) or different (hate). So the actual values are not variables; once the components are determined, all pairs' states are determined.

Wait, no. The problem states that the unknown relationships are the ones not given in the input. So the question is to fill in the unknown relationships such that all triplet conditions are satisfied. However, according to our analysis, the valid assignments are exactly the ones where the components form cliques (all pairs within love, pairs between hate), and the components are compatible with the existing edges.

Thus, the number of valid assignments is the number of ways to partition the nodes into components, such that:

- All existing edges are compatible (as checked in steps 1 and 2).

- The components are formed in such a way that merging via love edges (processing all love edges) has been done, and the existing hate edges have been checked.

But once the DSU structure is built (after processing all love edges and checking all existing edges), the components are fixed. Because the love edges have already been used to merge components. The existing hate edges must have been checked to ensure that they connect different components.

Wait, but the DSU structure after processing all love edges determines the components. All existing love edges are processed, merging components. So the components are fixed. Then, all existing hate edges must be between different components. So the components are determined by the love edges. Thus, the valid assignments are determined by this DSU structure.

But wait, the existing love edges may not be sufficient to determine the components. For example, if there are no existing love edges, then each node is in its own component. But for the problem's condition to hold, the components must be such that any two nodes in the same component love each other. So in this case, the components can be any possible partition into cliques. But how?

Hmm. Wait, the problem states that the existing edges are known relationships. The other edges are unknown. So the answer is the number of possible ways to assign the unknown edges such that all triplet conditions are satisfied.

But according to our analysis, the only way to satisfy the triplet conditions is to partition the graph into components where:

- All pairs within a component are love.

- All pairs between components are hate.

So, the unknown edges must be filled according to this partition. Thus, the problem reduces to counting the number of valid partitions into components (cliques) that are compatible with the existing edges.

But how to model the number of such partitions.

Wait, the DSU structure after processing the existing love edges may have multiple components. But the existing love edges are the ones that must be processed, and during merging, the components are formed. So the components are determined by the existing love edges. But what about the unknown edges?

Wait, perhaps the existing love edges must form a structure where the components are cliques, and the remaining edges (unknown) are filled according to the component structure.

But the problem allows for unknown edges. So the components must be such that:

- All existing love edges are within the same component.

- All existing hate edges are between different components.

- The unknown edges are filled according to whether the pairs are in the same component or not.

So, the number of valid assignments is determined by the number of ways to partition the nodes into components that satisfy the existing edges.

Wait, but once the existing edges are processed and validated, the components are fixed. Because the love edges are processed to merge components. So after processing all love edges, the components are fixed. Then, the existing hate edges must be between different components. So the components are fixed, and the unknown edges are filled based on the component structure.

Thus, the number of valid assignments is either 0 (if the existing edges are invalid) or 2^k, where k is the number of connected components in the DSU structure minus 1. Because each pair of components can have their love/hate relationships determined by their component membership. But wait, once the components are fixed, the assignments are determined: all pairs within a component are love, all between are hate. So the unknown edges are filled automatically. Thus, the number of valid assignments is 1.

Wait, no. Because the existing edges may not completely determine the components. For example, consider the case where there are no existing edges (like the first sample input). Then, the components can be any partition into cliques. Each such partition will result in a valid assignment. So the number of valid assignments is the number of possible ways to partition the nodes into any number of cliques, such that all existing edges (none in this case) are satisfied.

But how?

Wait, in the first sample input (n=3, m=0), the valid assignments are:

1. All three in one clique (all love each other). The triple is all loves: valid.

2. Two in a clique, one separate. For example, {1,2} and {3}. Then, the triplet is 1-2 love, 1-3 hate, 2-3 hate. So in the triplet, exactly one love pair: valid. There are 3 such possibilities (choosing which two are in a clique).

So total 4 valid assignments.

But according to the previous model, if the components are fixed, the number of valid assignments would be 1, which is not the case. So the previous model is incorrect.

Ah, so the mistake is assuming that the DSU structure is fixed by the existing love edges. But in reality, the existing love edges impose constraints that must be part of the partition, but there could be multiple possible partitions that satisfy the constraints.

Wait, but existing love edges must be part of the same component. So for any love edge (u, v, 1), u and v must be in the same component. So the partition must include all nodes connected by love edges in the same component.

But if there are no existing love edges, then the components can be any partition. But the existing hate edges must be between different components.

Ah, this complicates things. So the existing love edges enforce that their nodes are in the same component, but other nodes can be grouped in any way as long as the existing hate edges are between components.

So the problem is similar to a graph where the love edges are required to be in the same component, and hate edges are required to be in different components. The components must be a partition that respects these constraints, and the number of valid partitions is the answer.

Thus, the problem is to find the number of ways to partition the nodes into components such that:

1. All love edges connect nodes in the same component.

2. All hate edges connect nodes in different components.

The number of such partitions is the answer.

So this is similar to a 2-coloring problem but generalized. The solution is to model this as a graph where the love edges are constraints for connected components, and hate edges are constraints for not being in the same component.

But how to compute the number of valid partitions.

This is similar to determining the number of possible ways to split the graph into components such that:

- The love edges form equivalence relations (transitive, symmetric, reflexive).

- The hate edges are cross-component.

But it's not exactly straightforward.

Let me think. For the love edges, they must form a set of equivalence classes where all nodes connected by love edges are in the same component. So the love edges imply that their endpoints are in the same component. So the components must be the connected components formed by the love edges. But wait, no. Because the existing love edges are part of the input, and the partition must include those edges in the same component, but the existing love edges may not cover all possible pairs. So perhaps the components must be a super-set of the connected components formed by the love edges.

But no. For example, if there are no love edges, the components can be any partition. But for any existing love edges, the nodes must be in the same component.

So, the components must be a partition where each connected component (according to the love edges) is a subset of a component in the partition.

Wait, no. The love edges are constraints that their two nodes must be in the same component. So the components must form a partition where each connected component (according to the love edges) is entirely contained within a single component of the partition.

Thus, the love edges form a graph where their connected components are the minimal components that must be grouped together. So the partition must be formed by merging these connected components into larger groups, but any such merge must not create any conflicts with the hate edges.

But the hate edges impose that their two nodes must be in different components. So, if two nodes are connected by a hate edge, they cannot be in the same component. Moreover, if there's a hate edge between a node in group A and a node in group B (where groups are formed by merging the love-connected components), then A and B must remain separate.

So this problem is now transformed into a graph coloring problem where the initial groups are the connected components of the love edges. Then, the hate edges must form constraints between these groups, preventing certain merges.

Thus, the problem reduces to checking if the initial love-connected components can be colored (grouped) such that any hate edge between two components means that their groups are different. Then, the number of valid colorings is 2^k, where k is the number of connected components in the hate constraint graph.

Wait, perhaps this is a bipartition problem. Let's model this:

- The initial connected components from the love edges form nodes in a new graph.

- For each hate edge (u, v) in the original graph, which connects components a and b (since u and v are in different love components), we add an edge between a and b in the new graph. This edge requires that a and b are in different groups.

Wait, no. Because the hate edge requires that u and v are in different components. But u is in component a (from the love edges), and v is in component b. So in the new graph, a and b cannot be merged into the same component.

Thus, the problem becomes: we can merge the initial love-connected components into larger groups, but any two initial components connected by a hate edge (i.e., there's at least one hate edge between their members) must not be merged.

Thus, the initial love-connected components form a new graph where edges are hate edges between them. We need to partition this new graph into groups such that no two groups connected by an edge are merged. The number of valid such partitions is 2^c, where c is the number of connected components in the new graph (after considering the hate constraints).

Wait, but how?

Let me rephrase. The love-connected components are nodes. Between two love components, if there exists any hate edge between their members, then they cannot be merged. So, in the new graph, two love components are connected if they cannot be merged. We need to check if this new graph is bipartite. Because each connected component in the new graph must be bipartitioned into two groups, but this may not be possible. If any connected component in the new graph has an odd-length cycle, then it's impossible to partition, so the answer is 0.

Wait, but the problem is that two love components connected by a hate edge (u, v) must not be merged. But when merging love components, we can group them into larger components as long as there are no such hate edges between any of their members.

So, the way to model this is:

- The love-connected components form nodes in a new graph.

- For any two love components A and B, if there is any hate edge between a node in A and a node in B, then A and B cannot be merged. So in the new graph, A and B are connected by an edge.

- The problem is to partition the nodes of this new graph into groups such that no two nodes in the same group are connected by an edge. The number of ways to do this is 2^k, where k is the number of connected components in the new graph's bipartite decomposition.

Wait, no. Because the constraints are that two nodes (love components) connected by an edge (hate relationship) cannot be merged. Thus, the new graph's edges represent conflicts: two love components connected by an edge must be in different groups.

So the problem is to determine if this new graph is bipartite, and the number of valid colorings is 2^(number of bipartite components). If the new graph is not bipartite, the answer is 0.

But why bipartite? Because each connected component in the new graph (conflict graph) must be bipartitioned into two groups such that any two conflicting love components are in different groups. So each connected component must be a bipartite graph. The number of ways to color a bipartite graph is 2 (since each component can be colored in two ways, flipping the colors).

But how?

For example, if the conflict graph is a chain of three nodes A-B-C, then the graph is bipartite. The possible colorings are two: A and C in one group, B in the other; or B in one group, A and C in the other. But wait, the conflict graph's edges are between nodes that cannot be merged. So in this case, if we have a chain A-B-C, then merging A and C is allowed (since they are not connected by a conflict edge), but they cannot be merged if there's a path of conflict edges that require them to be in different groups.

Wait, perhaps I'm getting confused here.

Alternatively, each pair of love components connected by an edge in the conflict graph must be in different groups. So the problem is to assign a color (group) to each love component such that adjacent components (in the conflict graph) have different colors. The number of valid colorings is then 2^c, where c is the number of connected components in the conflict graph, provided that the conflict graph is bipartite. If any connected component in the conflict graph is not bipartite, then there are no valid colorings.

Thus, the steps are:

1. Process the love edges to form the initial love-connected components (using DSU).

2. Check all existing edges for validity:

   a. For each love edge (u, v), must be in the same component.

   b. For each hate edge (u, v), must be in different components. If u and v are in the same love component, invalid.

3. Build the conflict graph: nodes are love components. For each hate edge (u, v), add an edge between the love components of u and v. Note that u and v are already in different love components.

4. Check if the conflict graph is bipartite. For each connected component in the conflict graph, check if it's bipartite. If any is not, the answer is 0.

5. The number of valid colorings is 2^(number of bipartite components). So if there are k connected components in the conflict graph that are bipartite, the answer is 2^k.

But wait, no. Because each bipartition allows two colorings (the two possible color assignments). So for each connected component in the conflict graph that is bipartite, there are two possible ways to assign colors. So the total number of ways is 2^c, where c is the number of connected bipartite components.

But how does this relate to the number of valid partitions?

Each valid coloring of the conflict graph corresponds to a way to partition the love components into groups. For example, each color represents a group. Love components in the same group can be merged into a single component (since there are no conflict edges between them), while those in different groups must remain separate.

Wait, no. The conflict graph's edges represent that two love components cannot be merged. So each group in the coloring must be a set of love components that form an independent set in the conflict graph. Because if two love components are in the same group, there must be no conflict edges between them.

Thus, the groups are formed by merging love components that are not connected by any conflict edges. However, the conflict graph's edges enforce that adjacent components are in different groups. So the groups are the color assignments in a proper 2-coloring of the conflict graph.

Thus, if the conflict graph is bipartite, then there are two possible colorings for each connected component. Each coloring determines how the love components are merged into larger groups. Merging all components of the same color into a single component.

But wait, no. Each color represents a group. So love components with the same color can be merged into a single component (since there are no conflict edges between them). But for this to be allowed, there must be no conflict edges between any pair of components in the same color.

But the conflict graph's edges are between components that cannot be merged. So merging components of the same color is allowed only if there are no edges between them in the conflict graph.

Thus, the conflict graph must be bipartitioned into colors such that no two nodes in the same color are connected by an edge. Hence, the graph must be bipartite.

Thus, the number of valid ways to merge the love components into groups (which determines the final component structure) is 2^c, where c is the number of connected components in the bipartite conflict graph.

So putting it all together:

- The answer is 0 if any of the existing edges are invalid (steps 1 and 2), or if the conflict graph is not bipartite (step 4).

- Otherwise, the answer is 2^c mod 1e9+7, where c is the number of connected components in the bipartite conflict graph.

But wait, in the first sample input (3 nodes, 0 edges), the conflict graph is empty. So all love components (each node is its own component) can be merged into any groups as long as there are no conflicts. Since the conflict graph has no edges, the components can be merged in any way.

But according to the previous model, the conflict graph is empty, so the number of bipartition colorings is 2^c, where c is the number of connected components (each node is a component). So c=3. The conflict graph is empty, so each connected component is a single node. Each can be colored in two ways. So 2^3 =8? But the sample answer is 4.

Hmm, this suggests that the model is incorrect.

So what's the correct approach?

Let's go back to the sample input 1:

n=3, m=0.

Love edges: none.

Conflict graph: no edges.

So each love component is a single node (1, 2, 3).

The conflict graph has no edges, so the conflict graph is bipartite (trivially).

The number of colorings is 2^c, where c is the number of connected components in the conflict graph. But since the conflict graph has three nodes, each a connected component, c=3. 2^3=8.

But the sample output is 4. So this model is wrong.

Thus, the model is incorrect. So where is the mistake?

Ah, the previous model assumed that each color represents a group that can be merged. But merging the groups is allowed only if there are no conflict edges between them. So the valid partitions are determined by merging any subset of love components that form an independent set in the conflict graph. But that's not the case.

Wait, perhaps the correct model is that the love components can be partitioned into any number of groups, as long as no two love components in the same group have a conflict edge between them. The number of valid partitions is the product over each connected component in the conflict graph of the number of valid colorings. But if the conflict graph is bipartite, the number of valid colorings is 2 for each connected component.

But in the first sample, the conflict graph is empty (no edges). Each love component is a node in the conflict graph, but no edges. So each can be colored arbitrarily. So the number of colorings is 2^3=8. But the sample answer is 4. So this model is still incorrect.

Thus, this suggests that the model is incorrect, and we need to rethink.

Alternative approach: The answer is the number of ways to partition the love-connected components into two groups, such that any two love components connected by a hate edge are in different groups. Then, each group forms a component (clique). The number of valid such partitions is 2^k, where k is the number of connected components in the conflict graph (assuming the conflict graph is bipartite).

Wait, but in the first sample:

Conflict graph is empty. So all love components can be placed in one group. So merging all into a single component. Or, partition into groups in any way, as long as there are no conflicting edges. But since there are no edges, any partition is allowed.

But according to the problem's conditions, the way to form the components is such that any two love components in the same group are merged into a single component, and any two in different groups are separate. So the number of valid ways is the number of possible ways to split the love components into any number of groups, such that no two groups contain love components that are connected by a conflict edge.

But in the case of no conflict edges, the number of ways is the number of possible ways to partition the love components into any number of groups. But this is the Bell number, which is not 2^k.

This suggests that the previous approach is incorrect.

So perhaps the problem is not about bipartitioning, but about forming a partition where no two love components in the same group are connected by a conflict edge. So the groups must form an independent set in the conflict graph.

The number of such partitions is 2^c, where c is the number of connected components in the conflict graph. But this is only true if the conflict graph is a bipartite graph and each connected component is treated as a single unit. But this is not clear.

Alternatively, perhaps the problem is similar to a graph where the edges are constraints that two nodes cannot be in the same group. The number of valid colorings is the number of ways to assign each node to either group A or B, such that adjacent nodes are in different groups. This is possible only if the graph is bipartite, and the number of colorings is 2^c, where c is the number of connected components.

But then, each group forms a component in the final partition. So the final components are the union of the love components in group A and those in group B.

But in this case, the final components are two groups. But this is not the case in the first sample, where the valid partitions can have one group (all three merged) or three groups (each node is a group), etc.

Thus, the model is not correct.

Let's re-express the problem.

The final component structure must be a collection of cliques (love edges within), hate edges between. The existing edges must be compatible with this structure.

The components can be any partition of the nodes into cliques, as long as:

- All existing love edges are within a component.

- All existing hate edges are between different components.

The number of valid such partitions is the answer.

So, the existing love edges must form a subset of the edges within the components. The existing hate edges must form a subset of the edges between components.

Thus, the problem is to count the number of such partitions.

But how to model this.

The problem is similar to the following:

The components must be a partition of the nodes into cliques, where:

1. For every existing love edge (u, v), u and v are in the same component.

2. For every existing hate edge (u, v), u and v are in different components.

The number of such partitions is the answer.

So, the steps are:

1. Build the initial DSU based on existing love edges. For each love edge (u, v), merge their components. This ensures that all love edges are within the same component.

2. Check all existing edges for validity:

   a. For each love edge (u, v), check if they are in the same component. If not, invalid.

   b. For each hate edge (u, v), check if they are in different components. If not, invalid.

3. Now, the components are the initial DSU components. However, these components can be merged further, provided that merging them does not merge any two components that have a hate edge between them.

Thus, the problem is to find the number of ways to merge the initial DSU components into larger components, such that there is no hate edge between any two components in the same merged component.

Thus, the conflict graph is built as follows:

- Nodes are the initial DSU components.

- Edges are between any two components that have at least one hate edge between their nodes.

The valid partitions are those where merged components form an independent set in this conflict graph.

The number of such partitions is the number of possible ways to choose a collection of merged components that are independent sets in the conflict graph. But how to count this.

This is equivalent to the number of ways to choose a collection of merged components (subsets of the initial components) such that no two merged components have an edge between them. But this is the same as the number of ways to color the initial components with any number of colors, such that adjacent components (in the conflict graph) have different colors.

But this is the same as the number of possible colorings of the conflict graph where adjacent nodes have different colors. The number of colors can be arbitrary, but the number of colorings is equal to the number of possible proper colorings using any number of colors. This is a difficult problem, but perhaps in our case, the colors are used to group the initial components into merged components. The merged components can be any group of initial components that form an independent set in the conflict graph.

But this seems computationally infeasible for large n.

But perhaps the conflict graph must be bipartite, and the number of colorings is 2^c, where c is the number of connected components.

Alternatively, the conflict graph must be bipartite, and the answer is 2^(k), where k is the number of connected components in the bipartition.

But in the first sample input:

n=3, m=0.

Initial DSU components: each node is a component.

Conflict graph: no edges (no hate edges).

So merging any subset of initial components is allowed. The valid partitions are all possible partitions of the three components into any number of merged components. The number of such partitions is the Bell number of 3, which is 5. But the sample answer is 4. So this approach is incorrect.

But wait, the sample answer is 4. So the previous reasoning is incorrect.

Thus, the correct approach must be different. Let's think of the problem differently.

The problem requires that all triplets of nodes satisfy the condition. We can model the solution as a graph where the love edges form a collection of cliques (each pair within a clique loves each other), and pairs between cliques hate each other. The existing edges must be compatible with this structure.

The valid assignments are determined by the number of possible ways to partition the nodes into cliques that satisfy the existing edges.

The number of valid partitions is determined by the number of ways to split the initial DSU components into groups, such that no two initial components in the same group have a hate edge between them.

So, the initial DSU components are merged into larger cliques, but if two initial components have a hate edge between them (i.e., there exists a hate edge between any pair of nodes from these two components), they cannot be merged.

Thus, the problem reduces to counting the number of ways to merge the initial DSU components into groups such that no two initial components in the same group have a hate edge between them.

Thus, the number of valid partitions is 2^k, where k is the number of connected components in the conflict graph (the graph where nodes are initial DSU components and edges are the existence of any hate edge between them), provided that the conflict graph is bipartite.

Wait, but why 2^k?

If the conflict graph is bipartite, then each connected component can be colored in two ways (black or white), and each color represents a group. Merging all initial components in the same color into a single clique. This ensures that any two merged cliques have no hate edges between them (since conflicting initial components are in different colors and thus merged into different cliques). Thus, the number of valid partitions is 2^c, where c is the number of connected components in the conflict graph.

But in the first sample input:

Conflict graph has no edges, so each initial component is a connected component. Each can be colored in two ways. So 2^3 = 8. But the sample answer is 4. So this model is incorrect.

But sample input 1's answer is 4, which is 2^2. So where is the mistake?

Ah, perhaps the answer is 2^{c-1} where c is the number of connected components in the conflict graph. For the first sample, c=3 (each node is a connected component), so 2^{2} =4.

But why?

Perhaps the initial DSU components can be colored in two colors, but the actual number of ways is 2^{c-1} because swapping the colors doesn't create a new partition. Wait, no. Because each color represents a group. Merging all components of the same color into a single group.

For example, if all components are colored the same, they are merged into one group. If some are colored differently, they form different groups.

But in the first sample, the conflict graph is empty. So the initial components can be colored in any way. For example:

Color all three components as 0: merged into one group. So the entire graph is a single clique.

Color two components as 0 and one as 1: merged into two groups. For example, {1,2} and {3}. This results in three possible such partitions.

Color one component as 0 and two as 1: also three possible.

Color all three as 1: same as all as 0.

Thus, the total number of colorings is 2^3 =8. But the sample answer is 4.

But the sample answer is 4. So this model is incorrect.

Sample input 1's valid partitions are:

- All three in one group.

- Two in one group, one separate. There are three such possibilities.

Total 4.

So why 4? Because when merging components, the colors assigned to the initial components determine the groups. But in the case where the conflict graph is empty, any partition of the initial components into groups is allowed. So the number of valid partitions is the number of ways to partition the initial components into any number of groups. But this is the Bell number, which for three elements is 5.

But the sample answer is 4, so this is not the case.

Thus, there's a mistake in the model. Let's think again.

Each valid partition must be such that the merged components form a collection of cliques where there are no hate edges between any pair of initial components within the same merged group.

Thus, the merged groups must be independent sets in the conflict graph. Because if two initial components are in the same merged group, there must be no hate edge between them.

Thus, the number of valid partitions is the number of ways to partition the conflict graph into independent sets. This is known as the chromatic polynomial for the complement graph, but it's generally computationally expensive.

But how to compute this for large n.

But given the time constraints, perhaps the correct approach is to model the conflict graph as a bipartite graph, and the number of valid partitions is 2^c if it is bipartite, else 0.

But in sample input 1, the conflict graph is empty (thus bipartite), and the answer would be 2^c, where c is the number of connected components (3), which is 8. But the sample answer is 4.

Thus, this model is incorrect.

So, perhaps the correct model is that the answer is 2^{k}, where k is the number of connected components in the conflict graph's bipartition.

But how?

Alternative approach:

The merged groups must be independent sets in the conflict graph. Thus, the problem is to count the number of ways to partition the conflict graph into independent sets. This is equivalent to the number of colorings of the conflict graph where each color represents an independent set (merged group). The number of colorings is the product over the connected components of the number of colorings for each component.

For an empty graph (no edges), the number of colorings is the sum_{k=0}^{n} Stirling numbers of the second kind for k elements. For n=3, this is 5. But the sample answer is 4. So this is not the case.

Thus, the problem must have a different model.

After going through the examples and rethinking, perhaps the correct approach is that the merged components must form a bipartition. Because when you have a merged group, all initial components in the group can have no hate edges between them. Thus, the merged group must form an independent set in the conflict graph. But the only way this is possible for all possible merges is if the conflict graph is bipartite.

But how?

Let's take sample input 1:

Conflict graph is empty. So any partition is allowed. The sample answer is 4, which is 2^2. How to get this?

Hmm. Maybe the number of valid partitions is 2^{k}, where k is the number of nodes in the conflict graph minus the number of connected components. For sample input 1, 3 nodes, 3 connected components: 3-3=0. 2^0=1. No, sample answer is 4.

Alternatively, perhaps the answer is 2^{c}, where c is the number of connected components in the conflict graph. For sample input 1, c=3 (each node is a connected component). 2^3=8. Not correct.

Alternatively, perhaps the answer is 2^{c-1}, where c is the number of connected components in the conflict graph. For sample input 1: 3-1=2. 2^2=4. This matches the sample answer.

So why would this be the case?

If the conflict graph is bipartite and has c connected components, then the answer is 2^{c-1}.

Because for each connected component, there are two ways to color it, but the overall partition is determined up to swapping the colors. So for the entire graph, it's 2^c, but since swapping all colors gives the same partition (because merged groups are not ordered), we divide by 2, leading to 2^{c-1}.

But how?

For example, in sample input 1:

Conflict graph has 3 connected components (each node is its own component). So the total number of colorings is 2^3=8. But since swapping all colors (e.g., 0 and 1) leads to the same partition, we divide by 2, getting 4. Which matches the sample.

In the first sample, the valid partitions are:

- All components merged into one group (color 0 or 1), but this counts as one way since the merged group is the same regardless of color.

Wait, no. If all components are colored 0, they are merged into one group. If all are colored 1, also merged into one group. So these two colorings result in the same partition. Thus, for each connected component, the two colorings are symmetric. Thus, the total number of valid partitions is 2^{c}/2 = 2^{c-1}.

Thus, the correct approach is:

1. Check existing edges for validity.

2. Build the conflict graph (initial DSU components are nodes, edges are any hate edges between them).

3. Check if the conflict graph is bipartite. If not, answer is 0.

4. The number of valid partitions is 2^{k-1}, where k is the number of connected components in the conflict graph.

This would explain the first sample.

In the first sample:

Conflict graph is empty (each node is its own component). The number of connected components is 3.

So 2^{3-1} =4. Which matches the sample.

Another example: if the conflict graph has a single connected component that is bipartite. Then the answer is 2^{1-1}=1. But this would imply that there are two colorings, but they are considered the same. But perhaps in this case, the two colorings correspond to merging the two parts of the bipartition into two groups. But since merging is determined by the colors, the two colorings produce the same partition (the groups are the same, but the colors are swapped). So each connected component contributes a factor of 1 to the total.

Wait, no. For a bipartite connected component, there are two colorings. But merging all nodes of color 0 into one group and color 1 into another. Thus, the two colorings correspond to the same partition (group 0 and group 1), but the groups are swapped. So merging the same way. Thus, for each connected component, there are two colorings that produce the same partition. Thus, the number of partitions is 2^{c-1}, where c is the number of connected components in the conflict graph.

Thus, the model would be:

The answer is 2^{c-1}, where c is the number of connected components in the bipartite conflict graph. If the conflict graph is not bipartite, the answer is 0.

This would explain the first sample.

But how to verify this.

Sample input 2:

4 4

1 2 1

2 3 1

3 4 0

4 1 0

The existing love edges are between 1-2, 2-3. The existing hate edges are 3-4 and 4-1.

The initial DSU components after processing love edges:

1,2,3 are in the same component (since 1-2 and 2-3 are love edges). 4 is in its own component.

Conflict graph:

- Component 1-2-3 (A) and component 4 (B) have hate edges between 3-4 and 4-1. So the conflict graph has an edge between A and B.

Thus, the conflict graph is two nodes connected by an edge. This is a bipartite graph with one connected component. Thus, c=1. The answer is 2^{1-1} =1. Which matches the sample.

Sample input 3:

4 4

1 2 1

2 3 1

3 4 0

4 1 1

The existing love edges are 1-2, 2-3, 4-1. Existing hate edge is 3-4.

Processing love edges:

1-2 and 2-3 are merged. 4-1 is processed, merging 4 into the same component as 1,2,3.

Thus, all four nodes are in the same component.

Existing hate edge between 3 and 4. But 3 and 4 are in the same component. So this is invalid. Answer is 0.

Which matches sample input 3.

Thus, the model seems correct.

Thus, the steps are:

1. Use DSU to merge all nodes connected by existing love edges.

2. Check all existing edges for validity:

   a. For each love edge (u, v, 1): check if u and v are in the same component. If not, invalid.

   b. For each hate edge (u, v, 0): check if u and v are in different components. If not, invalid.

3. Build the conflict graph where nodes are the initial DSU components. There is an edge between two components if there is at least one existing hate edge between their nodes.

4. Check if the conflict graph is bipartite. If any connected component is not bipartite, the answer is 0.

5. The answer is 2^{k-1} mod 1e9+7, where k is the number of connected components in the conflict graph.

Now, the implementation steps:

- Implement DSU with path compression.

- Process all love edges first.

- Then, process all edges to check validity and build the conflict graph.

But how to build the conflict graph. For each existing hate edge (u, v, 0), find their components in the DSU and add an edge between them in the conflict graph.

But in the conflict graph, multiple hate edges between the same components only need to be represented once. So, for each pair of components, if there is at least one hate edge between them, add a single edge to the conflict graph.

Once the conflict graph is built, we need to check if it's bipartite. For each connected component in the conflict graph, perform a BFS or DFS to check bipartition.

Then, count the number of connected components in the conflict graph. The answer is 2^(number of connected components -1).

But how to represent the conflict graph. Since the DSU components can be numbered, we can create an adjacency list for the conflict graph.

But given that m can be up to 1e5, and n up to 1e5, it's important to process the conflict graph efficiently.

Implementation Steps:

1. Read n and m.

2. Initialize DSU.

3. Process all m edges:

   a. Separate the edges into love edges (c=1) and hate edges (c=0).

4. Process all love edges by merging their nodes in the DSU.

5. Check all edges for validity:

   a. For each love edge (u, v, 1), check if u and v are in the same component. If not, output 0.

   b. For each hate edge (u, v, 0), check if u and v are in different components. If not, output 0.

6. Build the conflict graph:

   a. For each hate edge (u, v, 0), find the root of u and the root of v.

   b. Add an edge between the two roots in the conflict graph.

   c. Use a set to avoid duplicate edges between the same pair of roots.

7. Check if the conflict graph is bipartite.

   a. For each node in the conflict graph (each root in the DSU), if not visited, perform BFS/DFS to check bipartition.

8. If any component is not bipartite, output 0.

9. Compute the answer as 2^(k-1) mod MOD, where k is the number of connected components in the conflict graph.

But how to count the number of connected components in the conflict graph.

Now, edge cases:

- If there are no hate edges, the conflict graph is empty. Each DSU component is a node with no edges. Thus, the conflict graph has as many connected components as the number of DSU components. Each is bipartite. So k is the number of DSU components. The answer is 2^{k-1}.

For the first sample:

n=3, m=0.

DSU components: 3.

Conflict graph has 3 nodes, no edges. So k=3.

Answer is 2^(3-1) =4. Which matches the sample.

Another example:

Sample input 2:

After processing love edges, DSU components are {1,2,3}, {4}.

Conflict graph has an edge between these two. So connected components in conflict graph: 1. Answer is 2^(1-1) =1. Which matches.

Thus, the model is correct.

Thus, the code can be structured as follows:

- Implement DSU with path compression and union by rank.

- Process love edges.

- Validate all edges.

- Build the conflict graph as a adjacency list.

- Check bipartition for each component in the conflict graph.

- Count the number of connected components (k) in the conflict graph.

- The answer is (2^(k-1)) mod 1e9+7.

Now, coding this in Python.

But for large n and m, we need to handle the DSU efficiently. Also, the conflict graph may have up to n nodes (each DSU component is a node).

But in practice, for m=1e5, the number of DSU components can be up to n if there are no love edges.

But with m=1e5, processing the edges and building the conflict graph may take O(m) time.

The BFS/DFS for bipartition is O(V+E), which is acceptable for up to 1e5 nodes and 1e5 edges.

But in Python, recursion depth is limited, so DFS may not be feasible for large graphs. Thus, BFS is better.

Now, let's code:

First, implement DSU.

Then, process love edges.

Then, process all edges to check validity.

Then, build conflict graph as a adjacency list.

Then, check bipartition for each component in the conflict graph.

Count the number of connected components.

Compute the answer.

But how to represent the roots of the DSU components.

We can create a set of all unique roots.

For each hate edge, add an edge between the roots of u and v.

To avoid duplicates, we can use a set of pairs.

But in Python, we can represent the conflict graph as a dictionary, where each key is a root, and the value is a list of adjacent roots.

But we can process all hate edges, and for each, get the roots of u and v, and add an edge between them, but only once.

Thus, code steps:

Read n, m.

Read m edges, and separate into love and hate edges.

Process love edges using DSU.

For each love edge, check if they are in the same component (after processing). If not, output 0.

For each hate edge, check if they are in different components. If not, output 0.

Collect all hate edges.

Build conflict graph:

Create a set of all roots.

For each hate edge, get root u and root v.

If u == v, it's a contradiction (already checked above).

Add an edge between u and v in the conflict graph.

But to avoid adding duplicate edges, we can use a set of tuples sorted, and add each pair once.

But even if multiple edges are added between u and v, in the BFS, it's handled as a single edge.

But to avoid processing the same edge multiple times, we can use a set.

Thus:

adj = defaultdict(list)

processed = set()

for each hate edge in the list:

   u = find(u)

   v = find(v)

   if u > v:

       u, v = v, u

   if (u, v) not in processed and u != v:

       adj[u].append(v)

       adj[v].append(u)

       processed.add( (u, v) )

But this is not necessary. Even if multiple edges are present between u and v, the BFS/DFS will treat them as a single edge. But for the purposes of bipartition, the presence of even a single edge between u and v requires them to be in different colors.

Thus, in the conflict graph, multiple edges between the same nodes can be treated as a single edge.

Thus, for each hate edge, add an edge between u's root and v's root, but ensure that each pair is processed once.

But since the same pair may appear multiple times (due to multiple hate edges between different nodes in the same DSU components), we need to add the edge once.

Thus, to avoid redundant edges, use a set to track pairs.

Now, after building the adjacency list, perform BFS to check bipartition.

For each root in adj:

   if not visited:

       perform BFS.

       mark visited.

       assign colors.

       if not bipartite:

           return 0.

       else:

           increment component count.

Also, roots that are not present in the adj (no edges) are considered as separate components. For example, a root with no edges in the conflict graph forms a component by itself.

Thus, after building the adj list, we need to iterate through all roots, not just those in the adj list.

Thus:

roots = set( find(i) for i in range(1, n+1) )

for root in roots:

   if root not in visited:

       increment component count.

       check bipartition.

Thus, code:

visited = set()

color = dict()

component_count = 0

bipartite = True

for root in roots:

   if root not in visited:

       component_count +=1

       queue = [root]

       visited.add(root)

       color[root] = 0

       while queue:

           current = queue.pop(0)

           for neighbor in adj.get(current, []):

               if neighbor not in color:

                   color[neighbor] = color[current] ^ 1

                   visited.add(neighbor)

                   queue.append(neighbor)

               else:

                   if color[neighbor] == color[current]:

                       bipartite = False

                       break

           if not bipartite:

               break

       if not bipartite:

           break

if not bipartite:

   print(0)

else:

   mod = 10**9 +7

   print(pow(2, component_count -1, mod))

But wait, what about the roots that have no edges in the conflict graph. For example, a root with no adj entries. Then, during BFS, they will be processed, and since there are no edges, the bipartition is trivially possible. The component count is increased by 1.

Thus, the code correctly counts all components.

But let's test the first sample.

Sample input 1:

n=3, m=0.

DSU components: 1, 2, 3.

Hate edges: none. So adj is empty.

roots = {1, 2, 3}

Processing:

component_count starts at 0.

For root=1: not in visited. component_count becomes 1. Add to visited. color[1] =0. adj.get(1) is empty. loop ends. No issues.

For root=2: not in visited. component_count becomes 2. Add to visited. color[2] =0. adj.get(2) is empty. loop ends.

For root=3: not in visited. component_count becomes 3. Add to visited. color[3] =0. adj.get(3) is empty. loop ends.

Thus, component_count is 3. The answer is 2^(3-1) =4.

Which matches.

Thus, the code is correct.

Thus, the final code should:

- Read the input.

- Process love edges with DSU.

- Check all edges for validity.

- Build the conflict graph as described.

- Check bipartition and count components.

- Compute 2^(k-1) mod MOD.

Now, the code:

But in Python, for large n and m, we need to handle the DSU efficiently.

Also, note that in Python, for DSU, it's better to use a list for parent and rank, with 1-based indexing.

Here's the code:

Read n and m.

Process m edges.

Separate into love and hate edges.

Process all love edges in DSU.

Check validity of all edges.

Build conflict graph.

Check bipartition.

Compute answer.

Now, code:
</think>

```python
import sys
from sys import stdin
from collections import defaultdict, deque

MOD = 10**9 + 7

def main():
    n, m = map(int, stdin.readline().split())
    parent = list(range(n+1))
    rank = [1] * (n+1)
    
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    
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
    
    edges = []
    love_edges = []
    hate_edges = []
    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        if a > b:
            a, b = b, a
        edges.append((a, b, c))
        if c == 1:
            love_edges.append((a, b))
        else:
            hate_edges.append((a, b))
    
    # Process love edges to merge components
    for a, b in love_edges:
        union(a, b)
    
    # Check all edges for validity
    valid = True
    for a, b, c in edges:
        if c == 1:
            if find(a) != find(b):
                valid = False
        else:
            if find(a) == find(b):
                valid = False
    if not valid:
        print(0)
        return
    
    # Build conflict graph
    adj = defaultdict(list)
    processed = set()
    for a, b in hate_edges:
        u = find(a)
        v = find(b)
        if u == v:
            print(0)
            return
        if u > v:
            u, v = v, u
        if (u, v) not in processed:
            adj[u].append(v)
            adj[v].append(u)
            processed.add((u, v))
    
    # Collect all roots
    roots = set(find(i) for i in range(1, n+1))
    color = {}
    visited = set()
    component_count = 0
    is_bipartite = True
    
    for root in roots:
        if root in visited:
            continue
        component_count += 1
        queue = deque([root])
        visited.add(root)
        color[root] = 0
        while queue:
            current = queue.popleft()
            for neighbor in adj[current]:
                if neighbor not in color:
                    color[neighbor] = color[current] ^ 1
                    visited.add(neighbor)
                    queue.append(neighbor)
                else:
                    if color[neighbor] == color[current]:
                        is_bipartite = False
                        break
            if not is_bipartite:
                break
        if not is_bipartite:
            break
    
    if not is_bipartite:
        print(0)
    else:
        print(pow(2, component_count - 1, MOD))
    
if __name__ == "__main__":
    main()
```