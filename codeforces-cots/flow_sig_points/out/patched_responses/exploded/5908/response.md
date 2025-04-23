<think>
Okay, so the problem is to determine the earliest point after which all the rap battles up to that point uniquely determine the ordering of the robots by skill. If even after all m battles there's still ambiguity, we return -1. 

First, let's understand the problem. Each rap battle gives a directed edge from the winner to the loser. The robots are ordered such that if a beats b, a comes before b. But since the relations are transitive, the order must form a total order. The question is, when does the set of edges added up to some k-th battle become such that there's exactly one possible topological order that respects all the constraints. And we need the smallest such k.

Hmm. So the key is to find the earliest k where the DAG (directed acyclic graph) formed by the first k edges has a unique topological sort. Because the problem states that there is at least one valid ordering after all m edges, so we don't have to worry about cycles. But during the processing of the edges, we might have a DAG that allows for multiple topological orders, and at some point, after adding enough edges, it becomes unique.

The challenge is to find the earliest k where the DAG's topological order is unique. If even after all m edges it's not unique, output -1.

So how do we check whether a DAG has a unique topological order?

I remember that a DAG has a unique topological order if and only if at every step of the topological sort, there's exactly one node with in-degree zero. Because if at any point there are two nodes with in-degree zero, then you can choose either, leading to multiple possible orderings.

So the approach would be to process the edges in order and track the DAG's structure, checking after each addition whether the current DAG meets the condition of having exactly one choice at each step of the topological sort. Once this condition is met, we can return the current k. If after all edges it's not met, return -1.

But how to do this efficiently, especially given the constraints of up to 1e5 nodes and edges?

Wait, but n can be up to 1e5, and m up to 1e5. We need an approach that can handle this efficiently. So we need an O(m) or O(m log n) solution.

The naive approach would be, after adding each edge, check if the current DAG has a unique topological order. But how to do that efficiently?

Wait, the problem is to find the earliest k where the DAG after the first k edges has a unique topological order. So for each k from 1 to m, we need to check if the DAG after k edges has a unique topological order.

But checking this each time naively would be O(n) per check, leading to O(mn) time, which is too slow for n up to 1e5 and m up to 1e5.

So we need a smarter way to track this.

Alternative approach: The uniqueness of the topological order depends on the in-degree of each node and the structure of the DAG. But how can we track when the DAG has a unique topological order incrementally?

Let me think: For a DAG to have a unique topological order, each level (step) of the topological sort must have exactly one node with in-degree zero. So whenever during the topological sort, there's a choice (multiple in-degree zero nodes), the order isn't unique.

So the problem reduces to, after each edge addition, check if the current DAG has this property.

But how to check this efficiently after each addition? Because the DAG is built incrementally, and edges are added one by one.

Hmm. Let's think of the DAG as a graph where edges are added in order, and after each addition, we need to verify if the DAG's topological sort is unique.

But even that, for each step, building the topological order and checking if there are multiple choices at any step would be O(n + m) each time, which is O(m(n + m)) total time, which is not feasible.

So this approach is not going to work. We need a way to track this information incrementally.

Alternative idea: For the DAG to have a unique topological order, the underlying graph must be such that the topological order is a linear chain. Each node (except the first) has exactly one immediate predecessor in the topological order, and each node (except the last) has exactly one immediate successor. So the DAG must form a chain where each step is determined.

Alternatively, perhaps the DAG must be such that at any point in the topological order, the next node is uniquely determined. Which would mean that during the topological sort process, each step has exactly one node with in-degree zero.

So perhaps the key is to track two things:

1. The current in-degree of each node.

2. The number of nodes with in-degree zero. If at any time, there's more than one node with in-degree zero, then the topological order is not unique.

But how can we track this efficiently as edges are added?

Wait, but the problem is that even if the in-degree becomes zero for multiple nodes after some edges are added, the DAG may still have a unique topological order. For example, suppose after some edges, two nodes have in-degree zero, but one of them has edges to the other. Then they can't both be in the same level of the topological sort. Wait, no. Because if a node A has edges to B, then B's in-degree would be increased. So if A and B both have in-degree zero, then there's no edge between them, which would allow them to be ordered either way. So that's when multiple topological orders are possible.

But in the DAG, if there's a pair of nodes with in-degree zero and no edges between them, then they can be ordered in either way, leading to multiple possible topological orders.

So the presence of two or more nodes with in-degree zero at any step implies that the topological order is not unique. Therefore, the DAG has a unique topological order if and only if, during the topological sort process, every step has exactly one node with in-degree zero.

So the way to check is to perform the topological sort and see if there's any step with more than one node with in-degree zero. However, this is O(n) per check, which is expensive.

Alternative idea: For each edge added, we can maintain the in-degrees of the nodes and track the number of nodes with in-degree zero. But when adding edges, how does that affect the count of in-degree zero nodes?

But the problem is that the order in which edges are added can affect the topological structure. For example, adding edges in a certain order can create a DAG where in-degree zero nodes fluctuate.

Wait, but even if the current DAG has in-degree zero nodes, but when we process them in topological order, the in-degrees of their neighbors are reduced, which may create new in-degree zero nodes.

But tracking this in real time for each step (each edge addition) seems challenging.

Alternative approach: We can model the problem as follows. We need to find the earliest k such that after processing the first k edges, the DAG has exactly one topological order. So, for each k, we need to check if the DAG has a unique topological order. We need to find the smallest such k, or -1 if none exists.

But how to do this efficiently.

Alternative idea inspired by the examples:

The earliest k where the DAG's topological order is uniquely determined is when the edges added up to k form a graph where the underlying relations (transitive closure) form a total order, and adding any of the remaining edges after k don't affect the order. But no, that's not necessarily true.

Alternatively, perhaps the DAG must form a linear chain where each node has exactly one predecessor and one successor, except for the ends. But I'm not sure.

Wait, perhaps the problem can be transformed into finding the earliest k where the DAG has a unique topological order. The key insight here is that the unique topological order can only exist if, after some edges are added, the DAG's structure enforces a total order with no ambiguities.

So, the problem reduces to checking after each edge addition whether the current graph's topological order is unique.

But how to check this efficiently.

Let me think: The standard way to check for a unique topological order is to perform a topological sort and, during the process, check if at any step there's more than one node with in-degree zero. If yes, then there are multiple possible topological orders.

But this approach is O(n + m) per check. For n=1e5 and m=1e5, this is O(m(n + m)) = 1e10 operations, which is way too slow.

Thus, this approach is not feasible. So we need a smarter way.

Alternative idea: The minimal k where the DAG's topological order becomes unique is the earliest k where the DAG's underlying graph is such that the topological order is a linear chain, and each node (except the first) has exactly one predecessor in the topological order, and each node (except the last) has exactly one successor.

Wait, perhaps this is a necessary condition. But how to model this.

Another approach: Since the problem requires that after the first k edges, the DAG has a unique topological order, and all edges are added in order, perhaps we can model this by tracking the necessary conditions for the topological order to be unique.

The necessary and sufficient condition is that during the topological sort process, each step has exactly one node with in-degree zero.

So, for each edge added, we can track the in-degree of each node. But how to track the number of nodes with in-degree zero at each step of the topological sort.

But again, this seems impossible to track incrementally.

Alternative approach inspired by the problem's constraints: Since the edges are given in order, perhaps the earliest k where the DAG's topological order is uniquely determined is when the DAG's structure is such that there is a unique sink (node with out-degree zero) and a unique source (node with in-degree zero) at each step of the topological sort.

But I'm not sure.

Alternatively, the unique topological order can be determined if the graph's edges form a linear hierarchy. For example, in a directed path, the topological order is unique.

But adding edges that form a chain would create such a structure.

But in practice, the edges could be added in any order, and the DAG may not form a single chain, but the combination of edges enforces a unique order.

So, perhaps the way to model this is to track for each node, the maximum and minimum possible position in the topological order. If all nodes have a fixed position, then the topological order is unique.

But how to track these positions efficiently.

Alternatively, since the edges are added incrementally, perhaps the earliest k where the graph's transitive closure forms a total order. The transitive closure would require that for every pair of nodes, there is an edge (directed) between them, which would imply a unique order.

But this is not correct. For example, the sample input 1 has 4 robots and 5 edges. After 4 edges, the edges form a structure that allows the transitive closure to order all four robots. So the fifth edge is redundant. So the answer is 4.

But how to compute the transitive closure incrementally? That's not feasible for large n.

Hmm. So perhaps the key is that the graph must have a unique topological order. To have a unique topological order, all possible topological orders must be the same. Which would require that, in the DAG, the adjacency list for each node is such that each node has exactly one possible next node in the topological order.

Alternatively, each node (except the last) must have exactly one outgoing edge that is required in the topological order.

Alternatively, think of the DAG's underlying structure as a forest of chains where each node has exactly one successor and one predecessor, except the ends. But this is a tree structure, which may not be the case.

Alternatively, for each node, there must be a unique path from it to the sink node. But I'm not sure.

Alternatively, perhaps the problem can be approached by maintaining the current order of nodes and checking for uniqueness. But again, this seems difficult.

Another angle: The problem requires that after the first k edges, the DAG's topological order is unique. So, any possible topological order of the DAG up to k edges must be the same. So, the edges added up to k must have created enough constraints to eliminate all ambiguities.

But how can we find the minimal k where all ambiguities are eliminated.

Another idea: For each node, track its possible positions in the topological order. The moment when all nodes have exactly one possible position, then the order is unique.

But how to track this efficiently.

Alternatively, think of the problem as building a partial order and finding the earliest step when the partial order is a total order. But again, this is not exactly accurate, as the partial order might not be a total order, but its transitive closure may allow a unique linear extension.

Wait, the problem's note says that it's guaranteed that at least one ordering satisfies all m relations. So the DAG is acyclic. But when edges are added in order, each step's DAG is a subset of the next.

The key is to find the earliest k where the DAG's linear extensions (all possible topological orders) are exactly one.

But how to compute this.

Alternative approach inspired by the fact that the problem is similar to a tournament graph. In a tournament graph, every pair of nodes has exactly one directed edge. Such a graph has a unique topological order if and only if it is a transitive tournament, meaning that if a beats b and b beats c, then a beats c. In that case, the topological order is the sorted order of the nodes based on their wins.

But in our problem, the edges are not a tournament, but a subset of all possible edges. So, perhaps the minimal k is when the edges added form a transitive tournament, but that's not necessarily the case.

But this line of thought isn't directly helpful.

Alternative idea: We can model the problem as follows. For the topological order to be unique, every pair of nodes must have a directed edge (in either direction) that forces their order. However, this is not necessarily true. For example, if a is before b and b is before c, then a is before c even if there's no edge between a and c.

So, the uniqueness comes from the fact that for any pair of nodes, there's a directed path between them in the DAG. This would mean that the DAG's transitive closure is a complete order, and hence the topological order is unique. But even if the transitive closure is not a complete order, the topological order could still be unique. For example, consider three nodes a, b, c with edges a->b and a->c. The topological orders are a, b, c or a, c, b. So even though the transitive closure is not complete, there are two possible orders. So in this case, the DAG's transitive closure is not complete, leading to multiple orders.

Thus, the DAG must have a transitive closure that is a complete order. Because if there's any pair of nodes not connected by a directed path, then their order in the topological sort can be swapped, leading to multiple possible orders.

Wait, no. For example, suppose the DAG has a->b and c->d. Then the topological order can be a, b, c, d or c, d, a, b. So even though there's no path between a and c, their order can be swapped, leading to multiple possible orders.

So, the key is that the transitive closure of the DAG must form a complete order. So, for every pair of nodes u and v, either there is a path from u to v or from v to u. If this is the case, then the topological order is unique. Because the order must be such that for every pair, the one that can reach the other comes first.

Wait, but if the DAG's transitive closure is a total order, then the topological order is unique. Because the topological order must arrange the nodes in such a way that all edges go forward. So in this case, the order is determined by the total order of the transitive closure.

So, the problem reduces to finding the earliest k where the transitive closure of the first k edges is a total order on all nodes. Because once that's achieved, all further edges are redundant (they are already implied by the existing edges), and the topological order is unique.

But how to compute this.

But calculating the transitive closure after each edge addition is computationally expensive for large n. So this approach is not feasible.

So, perhaps we need to find a way to model the minimal k where the DAG has a unique topological order by other means.

Alternative idea: Let's model the problem as tracking the in-degree and out-degree of each node. For the topological order to be unique, there must be a unique source (node with in-degree zero) at each step of the topological sort. So, the earliest k where after processing the first k edges, the DAG has a unique source, and each time after removing a source, the resulting DAG also has a unique source, and so on.

So, the algorithm would be:

1. For each k from 1 to m, check if the DAG after the first k edges has the property that during the topological sort, each step has exactly one source.

If this is true, then return k. If none are found, return -1.

But how to check this efficiently for each k.

The problem is that for each k, we need to process the first k edges and perform a topological sort to check for uniqueness. But for m=1e5, this would be O(m(n+m)) time, which is not feasible.

Alternative approach inspired by the fact that edges are added incrementally:

We can track for each node the in-degree and maintain a set of sources (nodes with in-degree zero). Whenever the size of this set is more than 1, the topological order is not unique. However, when we process edges in the order they are added, the in-degree of nodes increases, but the sources are the ones with in-degree zero.

But this is not sufficient. Because even if after adding an edge, the current in-degree of all nodes is such that the number of sources is 1, the topological sort process could have steps with multiple sources.

Wait, perhaps the initial in-degree of the DAG after k edges is such that the number of sources is 1. But during the topological sort, when we remove that source, the next step could have multiple sources.

So, the initial in-degree is not enough. We need to track the entire process.

Thus, this approach is not sufficient.

Alternative idea: We can model the DAG's structure using a Union-Find (Disjoint Set Union) structure. But I'm not sure how that applies here.

Another approach: The minimal k is the earliest point where the current DAG has a unique topological order. To check this, we can perform a Kahn's algorithm for topological sort. During this process, if at any step the queue (containing nodes with in-degree zero) has more than one element, then the topological order is not unique. So, the process for each k would be:

- Build the DAG with the first k edges.

- Compute in-degree for each node.

- Perform Kahn's algorithm, checking if at any step the queue size is greater than 1.

If during Kahn's algorithm the queue size never exceeds 1, then the topological order is unique.

But again, for m=1e5 and n=1e5, doing this for each k is O(m(n + m)) time, which is way too slow.

Thus, this approach is not feasible.

So, we need a way to model this without having to re-run Kahn's algorithm for every k.

Alternative idea inspired by the problem's constraints: The answer is the earliest k where the DAG's edges form a chain such that every node has exactly one predecessor and one successor in the topological order. This would ensure that each step in the topological sort has exactly one node with in-degree zero.

But how to track this.

Alternatively, the answer is the earliest k where the edges have formed a structure that defines a linear order. For example, edges like a1 -> a2, a2 -> a3, etc., forming a chain. But edges can be added in any order, so this may not be the case.

So perhaps the minimal k is when the DAG's edges have created a transitive closure that forms a total order, and any additional edges are redundant.

But again, checking the transitive closure for each k is not feasible.

Alternative approach inspired by the sample input:

In the first sample, after 4 edges, the DAG has edges 2->1, 1->3, 2->3, 4->2. The topological order here is 4, 2, 1, 3. But how do these edges ensure that this is the only possible order.

Let's see:

4 has no incoming edges. So it's the first in the order. Then, after removing 4, the next nodes are those with in-degree zero. In this case, 2. Then after removing 2, the next is 1 (since 1's in-degree is 1 from 2, but 2 was removed, so 1's in-degree becomes zero). Then 3.

Thus, during each step, only one node is available, leading to a unique order.

So the key is that the current DAG allows for a unique source at each step of the topological sort.

But how to track this without performing a full Kahn's algorithm each time.

Another Idea: Since the edges are added in order, maybe we can track the necessary conditions incrementally.

For example, initially, the DAG has no edges. So all nodes are sources. The number of sources is n. Obviously, the topological order is not unique. As edges are added, the in-degree of nodes increases. 

Each edge added may reduce the number of sources or not. But even if after adding an edge, the number of sources is 1, this doesn't necessarily mean that the topological order is unique.

But perhaps the answer is the earliest k where the DAG has exactly one source (in-degree zero) and all other nodes have in-degree >=1, and the same is true for each subsequent step of the topological sort.

But how to model this incrementally.

Alternative approach inspired by the problem's required output: The answer is the first k where the DAG is such that there's a unique topological order, and after that, adding more edges doesn't change the order. So once the order is fixed by the first k edges, any additional edges are redundant and the order remains the same.

Thus, the problem is to find the earliest k where the order is uniquely determined by the first k edges, and all later edges are implied by the transitive closure of the first k edges.

Thus, the problem reduces to finding the earliest k where the edges added up to k have a transitive closure that is a total order, and all subsequent edges are implied by that total order.

But how to model this.

In other words, once we have a DAG whose transitive closure is a total order, any subsequent edges that are added must be in the direction of that order. Otherwise, the order would be contradicted. But the problem states that the input is guaranteed to have at least one valid order. So the edges added after k must be consistent with the total order.

But how to find the earliest k where the first k edges have a transitive closure that forms a total order.

Because in that case, the topological order is unique, and all later edges are redundant.

So, the problem is equivalent to finding the earliest k such that the first k edges form a DAG whose transitive closure is a total order. Once that is achieved, the topological order is uniquely determined. Any further edges are part of the transitive closure (i.e., they are implied) or are added in the correct direction.

So the minimal k is the earliest point where the first k edges have a transitive closure that is a total order.

But how to compute this.

The challenge is to find the minimal k where the first k edges, along with their transitive closure, form a complete order where every pair of nodes is connected by a directed edge in the closure.

But how to compute this efficiently.

This seems difficult, but there's a data structure called a disjoint set union (DSU) with path compression that can help track the connected components and some order.

Alternatively, perhaps we can track for each node the set of nodes that are known to be greater than it (i.e., nodes that it can reach) and the nodes that are known to be smaller than it (i.e., nodes that can reach it). But maintaining this for each node is expensive.

Another Idea: For the transitive closure to be a total order, there must be a chain of edges that connects all nodes in a strict hierarchy. So, the nodes must form a single chain where each node has a unique predecessor and successor.

But how to track this.

Alternatively, think of it as building a linear order incrementally. Each edge added either connects two nodes that are already in the order (and thus reinforces the existing order) or connects two nodes that are not yet ordered, thereby extending the order.

For example, the first edge a->b establishes a partial order. The next edge b->c extends the chain. The next edge a->c is redundant. The next edge d->a adds to the chain, making it d->a->b->c. And so on.

But how to model this and track when the chain includes all nodes.

Alternatively, the problem is similar to finding the minimum number of edges needed to form a linear extension of the nodes. So, once the edges form a chain that covers all nodes, their transitive closure will be a total order.

But again, how to track this.

Alternatively, the problem can be viewed as a directed graph where each edge addition contributes to the hierarchy. The minimal k is when the graph's edges form a hierarchy where all nodes are connected in a single path, and the edges between nodes are such that the hierarchy is complete.

But I'm stuck.

Alternative approach: Let's think of the problem in terms of the necessary and sufficient conditions for the topological order to be unique. The necessary and sufficient conditions are:

1. The DAG has a single source (node with in-degree zero).

2. After removing that source, the resulting DAG also has a single source.

3. Repeat this process until all nodes are removed.

If all steps meet the condition of having exactly one source, then the topological order is unique.

So, the problem is to find the earliest k where the first k edges form a DAG that meets this condition.

But how to check this efficiently for each k.

This seems to require performing a modified topological sort for each k, which is O(n + m) time per k, leading to O(m(n + m)) total time. For large m and n, this is not feasible.

But perhaps we can find a way to model this incrementally.

Let's imagine that we process each edge one by one and maintain data structures that allow us to track when the DAG meets the condition.

But how.

An alternative idea inspired by the fact that the topological order is unique if and only if the DAG is a linear chain.

Wait, that's not true. For example, if the DAG has edges a->b, a->c, and b->c, the topological order is a->b->c. Here, the DAG is not a chain but the order is unique.

So that's not the case.

Hmm. So perhaps the DAG can have some branches but still enforce a unique order.

So the problem is not as simple as building a chain.

Another Idea: The answer is the first k where the edges added up to k form a DAG in which every pair of nodes is comparable (i.e., there exists a path between them in either direction). This would mean that the DAG's transitive closure is a total order.

But how to check this for each k.

For n=1e5, checking all pairs for each k is impossible.

But perhaps there's a way to track the number of pairs that are not comparable.

But this also seems challenging.

Alternative approach: We can model the problem using a bitmask for each node, indicating which other nodes it can reach. However, for n=1e5, this is impossible due to memory constraints.

So this is not feasible.

Another Idea: Let's consider that the earliest k where the DAG has a unique topological order is when the DAG has a unique topological order and this order is consistent with all edges added after k. But this is not helpful for finding k.

Alternatively, perhaps the answer is the earliest k where all edges added after k are redundant (i.e., already implied by the first k edges). So, the first k edges form a DAG whose transitive closure includes all edges added after k.

But how to compute this.

But checking whether an edge is implied by the existing edges is equivalent to checking if there's a path between the two nodes. But for each edge added after k, we would need to check if it's already in the transitive closure of the first k edges. This is again computationally expensive.

But the problem requires that all edges are compatible with the final order. So perhaps the minimal k is when the first k edges form a DAG where the topological order is uniquely determined, and any subsequent edges are consistent with that order but do not change it.

But again, this doesn't help us find k efficiently.

Another Idea: Let's think of the problem as trying to find the earliest point in time where the DAG has a unique topological order. The way to determine this is to find the first time when the following conditions are met:

- There exists a unique node with in-degree zero (the first node in the order).

- For every node except the first, there exists exactly one node that is its immediate predecessor in the order (i.e., there's a directed edge from the predecessor to the node, and no other node can come between them in the order).

This seems like a possible approach. But how to track this.

Alternatively, for each node, we can track its possible predecessors and possible positions in the topological order. But again, this is not feasible for large n.

Alternative approach inspired by the sample input:

In the first sample, after four edges, the DAG has a unique topological order. The edges are 2->1, 1->3, 2->3, 4->2. So the order is 4, 2, 1, 3.

When we process these edges, the in-degrees are:

4: 0

2: 0 (but edge 4->2 contributes to in-degree of 2?)

Wait, no. Each edge contributes to the in-degree of the destination.

So edge 2->1: in-degree of 1 increases by 1.

Edge 1->3: in-degree of 3 increases by 1.

Edge 2->3: in-degree of 3 increases by 1 (now 2).

Edge 4->2: in-degree of 2 increases by 1 (now 1).

So after four edges, the in-degrees are:

1: 1 (from 2)

2: 1 (from 4)

3: 2 (from 1 and 2)

4: 0

So the sources are node 4 (in-degree 0). Processing node 4.

After removing 4, the edges from 4 are processed. The only edge is 4->2. So in-degree of 2 decreases by 1 to 0. Now, the sources are node 2.

Processing node 2. Its edges are 2->1 and 2->3. When processed, in-degree of 1 becomes 0, and in-degree of 3 becomes 1.

Now, sources are node 1. Process it. Its edge is 1->3. In-degree of 3 becomes 0. Process 3. All nodes are processed.

At each step, only one source. So topological order is unique.

So the key is that during the topological sort, after each step, there's exactly one source.

Thus, the problem reduces to finding the earliest k where the DAG formed by the first k edges has this property.

But how to track this without performing a full topological sort for each k.

An alternative Idea: Since the edges are added in order, perhaps we can keep track of the current in-degree of each node and the set of sources. For each edge added, we can update the in-degrees and sources. Then, after each addition, perform a check to see if the sources are unique and that each subsequent step also has unique sources.

But how to perform this check efficiently.

This seems tricky. Because even if the current sources are unique (like after adding four edges, the sources are [4]), after processing that node, the next sources may have multiple nodes.

But the only way to know is to perform a topological sort.

Thus, this brings us back to the problem of needing to perform a topological sort for each k, which is not feasible for large n.

But perhaps we can find a way to model the necessary conditions incrementally.

Wait, perhaps when we add edges, the DAG becomes more constrained. So the earliest k where the DAG's topological order is unique is when the topological order becomes forced, and any edges added after k do not change this.

But how to model this.

Another Idea: For the topological order to be unique after k edges, all the edges added up to k must form a DAG where all pairs of nodes have a defined order. This can be achieved if for each pair of nodes, there is a path in one direction between them in the first k edges. Thus, the first k edges must form a DAG whose transitive closure is a total order.

But again, checking this is O(n^2) per k, which is not feasible.

Alternative Idea inspired by the sample input 2:

In sample 2, after two edges (1->2 and 3->2), the DAG has two sources (1 and 3). So during the topological sort, you can choose either first, leading to multiple orders. Thus, the answer is -1.

So, the key is that if at any step during the topological sort there are multiple sources, the order is not unique.

Thus, to find the earliest k where the DAG's topological order is unique, we need to find the earliest k where during the topological sort of the DAG formed by the first k edges, each step has exactly one source.

But how to find this efficiently.

This suggests that the algorithm should process each edge, build the DAG incrementally, and after each addition, check if the DAG's topological sort has exactly one choice at each step. Once such a k is found, return it. If after all edges are processed, no such k exists, return -1.

But the problem is the time complexity. For each k, performing a topological sort is O(n + m). With m up to 1e5, this is O(1e5*(1e5)) = 1e10 operations, which is way too slow.

Thus, we need a more efficient way.

Alternative Idea inspired by the fact that the edges are added in order and the answer must be the earliest k where the DAG's topological order is unique. So, perhaps the answer can be determined by tracking the earliest point where the DAG's topological order becomes unique and remains so even after adding more edges.

But how.

Wait, once the topological order is unique for k edges, adding any new edges that are consistent with the order (i.e., edges from a higher node to a lower node in the order) will not change the order. Only edges that are between nodes not yet ordered would potentially allow for a different order. But once the order is unique for k edges, adding edges that are implied by the order (i.e., edges in the same direction) won't affect the order. So once the order is uniquely determined by the first k edges, any subsequent edges are either redundant or would not change the order.

Thus, once we find the earliest k where the DAG's topological order is unique, that's the answer.

But how to find this k efficiently.

Another Idea: Let's model the problem by maintaining the current possible order. As edges are added, they constrain the possible orders. The earliest k where only one order remains is the answer.

But how to model the possible orders. This seems impossible for large n.

Alternative Idea inspired by the fact that the answer is determined by the last edge added that resolved an ambiguity in the order. For example, in the first sample, after the fourth edge (4->2), the order becomes fixed. All previous edges allowed some ambiguity, but this edge resolved it.

But how to identify such edges.

Another Idea: The answer is the earliest k where the DAG's topological order has a unique linear extension. To check this, perhaps we can track the number of possible linear extensions and see when it becomes 1. But computing this number is #P-complete, which is not feasible.

Thus, this approach is not helpful.

After struggling for a while, perhaps the only feasible approach is to process the edges in order and after each addition, perform a topological sort using Kahn's algorithm, and check if at any step there's more than one node in the queue. If not, record k as the possible answer. But this approach is O(m(n + m)) time, which is way too slow for n=1e5.

But given the problem's constraints (n and m up to 1e5), the solution must be O(m) or O(m log n) time.

So perhaps there's a smarter way to model the required condition.

Wait, perhaps the earliest k where the DAG's topological order is unique is when the DAG is such that there's a unique node with in-degree zero, and this node has exactly one outgoing edge to another node with in-degree zero after processing, and so on. But this seems unlikely.

Alternatively, think of the problem as requiring that the topological order is a linear sequence, and each node (except the first) has exactly one incoming edge from the previous node in the sequence. But this is not the case. For example, a node can have incoming edges from multiple previous nodes as long as they are all ordered before it.

But I'm stuck.

Another Idea: Let's think of the problem in reverse. Suppose we have a DAG with a unique topological order. The last node in this order must have in-degree zero in the reversed graph. So, perhaps the problem can be modeled by maintaining the in-degree of each node and the sources.

But this brings us back to the same issue.

Alternative Idea inspired by the fact that the minimal k is when the DAG has exactly one source and exactly one sink. But I'm not sure.

After hours of thinking, I think I need to look for a solution approach used in similar problems.

Searching for similar problems: This problem is similar to finding the earliest point in a sequence of edges where the DAG's topological order is unique. The solution for this would involve a smart way to track the necessary conditions.

After some research, I find that a way to determine if a DAG has a unique topological order is to check if during Kahn's algorithm, each step has exactly one node with in-degree zero.

But implementing this for each k is O(m) per k, which is not feasible.

But perhaps the answer can be determined by the earliest k where the number of edges added is sufficient to form a DAG that is a chain.

But how.

Alternatively, the answer is the earliest k where the DAG has a unique source, and every node except the source has exactly one incoming edge from its predecessor in the topological order. This would form a chain.

But this is not the case, as shown in the first sample.

So, I'm stuck. Perhaps I need to look for a different approach.

Wait, perhaps the answer is the earliest k where the DAG has a unique topological order, which can be determined by the following conditions:

1. All nodes have in-degree <= 1.

2. There's exactly one node with in-degree 0 (the first node).

But this is not sufficient. For example, consider a graph with edges a->b, a->c, b->c. Here, a has in-degree 0, b has in-degree 1, c has in-degree 2. The topological order is a->b->c, which is unique. So condition 1 is not met.

Thus, this approach is incorrect.

Alternative Idea: Let's model the problem as a directed graph and track for each node the earliest time when it becomes fixed in the topological order. For example, a node is fixed in position when all other nodes are either known to be before or after it.

But how to track this.

Another Idea: The answer is the earliest k where the DAG's edges form a linear extension, and every node has exactly one predecessor and one successor (except the first and last). But this is not necessarily true.

Another Idea: The problem requires that the DAG's edges form a structure where there is a unique Hamiltonian path. Because the topological order must be a permutation of all nodes, and if there's only one such permutation, then it's the unique topological order.

Thus, the problem reduces to finding the earliest k where the DAG has exactly one Hamiltonian path.

But finding this is not straightforward.

But how to model this.

After more research, I find that the problem is similar to determining when a DAG has a unique topological order. The standard approach is to perform a topological sort and check if at each step there's exactly one node with in-degree zero. But as discussed earlier, this is O(n + m) per check.

Thus, given the problem's constraints, we need to find a way to process this in O(m) time overall.

But how.

Perhaps, the key is to process the edges in order and track the necessary conditions incrementally. Let's think about how adding an edge can change the DAG's structure in a way that affects the uniqueness of the topological order.

When an edge is added from u to v:

- The in-degree of v increases by 1.

- This might reduce the number of sources (nodes with in-degree zero).

But how does this affect the topological sort steps.

Alternatively, perhaps the answer is the first k where the DAG after k edges has a single source, and the number of sources after each step of the topological sort is 1.

But how to track this without performing the topological sort.

But perhaps during the process of adding edges, we can track the in-degrees and the current set of sources. However, this is not sufficient, as the order in which sources are processed can affect the subsequent sources.

Thus, it's not possible to track this incrementally.

Another Idea: Once all edges are added, the DAG has a unique topological order. The problem asks for the earliest k where this order is determined. Thus, the answer is the earliest k where the first k edges form a DAG whose topological order is the same as the final topological order after all edges.

But how to find this.

But how to compute the final topological order. Since the input is guaranteed to have at least one valid order, we can compute the final topological order using all edges.

Once we have this order, the earliest k is the earliest point where the first k edges form a DAG that forces this order. But how to compute this.

For example, in the first sample, the final order is 4, 2, 1, 3. The earliest k is 4, where the edges up to 4 form a DAG whose topological order is 4, 2, 1, 3.

But how to find the earliest k where all edges up to k are compatible with the final order and enforce that order.

So, the approach would be:

1. Compute the final topological order (after processing all edges).

2. For each edge in the input order, check if the edge is in the direction of the final order.

3. Find the earliest k where all edges up to k are such that:

   a. They form a DAG that is compatible with the final order.

   b. The DAG formed by these edges has a unique topological order (the final order).

But how to compute this.

Step 1: Compute the final topological order.

This can be done using Kahn's algorithm on the entire DAG.

Step 2: For each edge in the input order, check if it's in the direction of the final order (u comes before v in the final order).

For the DAG formed by the first k edges, all edges must be in the direction of the final order (i.e., for each edge u->v, u is before v in the final order).

If any edge in the first k edges is in the reverse direction, then the DAG's topological order would differ, but this contradicts the problem statement's guarantee. So perhaps this is not the case.

Alternatively, the final order is the one that satisfies all edges. So, for every edge u->v in the input, u comes before v in the final order.

Thus, when processing the first k edges, the final order is a valid topological order for the first k edges. But other orders may also be possible.

But the first k edges may have a unique topological order, which must be the final order.

Thus, the earliest k where the first k edges form a DAG whose only possible topological order is the final order.

So, the problem reduces to finding the earliest k where the first k edges form a DAG that, when processed using Kahn's algorithm, has exactly one source at each step, and the order is the same as the final order.

But how to compute this.

Once we have the final order, we can process the edges in the input order and track for each node its in-degree and the number of incoming edges processed so far. Then, for each step k, we can check whether the first k edges have formed a DAG where the in-degree of each node in the final order is zero when processed in that order.

Alternatively, during processing the edges in the input order, we can track for each node in the final order whether all of its predecessors in the final order have been processed in the first k edges.

But I'm not sure.

Let's think of the final order as a list T = [t1, t2, ..., tn], where t1 is the first node, t2 is the second, etc.

For the DAG to have a unique topological order (the final order), each node ti must have all of its predecessors in the final order already processed, and the only node with in-degree zero at each step is ti.

But how to model this.

Another Idea: For the DAG to have the final order as its unique topological order, each node ti (for i >= 1) must have an incoming edge from ti-1 (the previous node in the final order). This way, the nodes must be processed in order. But this is not necessarily true, as other edges can also enforce the order.

For example, in the first sample, the final order is 4, 2, 1, 3. The edges between these nodes are 4->2, 2->1, 1->3, and others. But 2 has an incoming edge from 4, 1 has incoming from 2, 3 has incoming from 1 and 2. So the existence of edges between consecutive nodes in the final order is not required, but they can help.

But even without such edges, the order can be enforced by other edges. For example, if 4->1 and 4->2 and 2->3, the order may still be 4, 2, 3, 1 if the edges enforce it. So this approach is not directly applicable.

Alternative Idea: To ensure that the topological order is unique and matches the final order T, for each node ti (i >= 2), there must be at least one incoming edge from a node tj where j < i. Furthermore, for each node ti, all of its incoming edges must come from nodes tj where j < i. This is already guaranteed since the final order is a topological order of all edges.

But this is not sufficient for uniqueness. 

But for uniqueness, each ti (i >= 2) must have exactly one node in {t1, ..., ti-1} that has no outgoing edges to any of {t1, ..., ti-1} except ti. This is not clear.

Another Idea: For the topological order to be unique, each node ti must have all of its incoming edges from nodes that are in the previous positions in the order. So, if a node ti has multiple incoming edges from nodes before it, but they are all in the order before ti, this is allowed. But to have uniqueness, perhaps each node ti must have exactly one incoming edge from the previous node ti-1. But this is not necessarily true.

But how to model this.

An alternative approach inspired by the solution to the problem:

The solution involves two parts:

1. Compute the final topological order T using all edges.

2. For each k, check if the first k edges form a DAG that forces the order T to be the only possible topological order.

The check for each k can be done by verifying that, for each node ti in T, all edges from nodes after ti to ti in the final order are not present in the first k edges. Additionally, the first k edges must include enough constraints such that in the DAG formed by them, the order T is the only possible topological order.

But how to compute this efficiently.

But given that the edges are processed in the order they are added, and the final order T is known, the earliest k where all edges up to k are such that they form a DAG where the order T is the only possible topological order.

Thus, the steps are:

- Compute the final order T using all edges.

- For each edge in the input order, check if it is a "necessary" edge that contributes to enforcing the order T. The necessary edges are those that, if omitted, would allow a different topological order.

- The earliest k is the point where all necessary edges up to that point have been added.

But how to determine which edges are necessary.

Alternatively, the necessary edges are those that prevent certain nodes from being ordered differently. For example, an edge u->v in the final order (u comes before v) may be necessary if there is no other path from u to v in the DAG formed by the first k edges.

But again, this is computationally expensive.

Another Idea inspired by the fact that for the order to be unique, each node ti must have at least one incoming edge from a node tj where j < i (to ensure that ti cannot be placed before tj). But this is already ensured by the final order T.

But this is not sufficient for uniqueness.

The correct approach seems to be to compute the earliest k where the DAG formed by the first k edges allows for only the final order T as the topological sort. This can be checked by ensuring that for each consecutive pair (ti, ti+1) in T, there is a path from ti to ti+1 in the first k edges. Because this would force ti to come before ti+1 in any topological order, thus ensuring that the order T is the only possible one.

But this is not correct. For example, if there is a path from ti to ti+2, but not to ti+1, then ti+1 can come after ti+2. 

Alternatively, the condition for the order to be unique is that for every pair of consecutive nodes ti and ti+1 in T, there is an edge from ti to ti+1 in the first k edges. But this is not necessarily the case.

In the first sample, the consecutive pairs are (4, 2), (2, 1), (1, 3). The edges that connect these pairs are 4->2, 2->1, 1->3. Additionally, there is 2->3 and 4->3. So the edges between consecutive pairs are present, but other edges are also present. But this is not the case for all consecutive pairs. For example, between 2 and 1 there is an edge, but between 1 and 3 there is also an edge. So perhaps the presence of edges between consecutive pairs ensures that the order is unique.

But this is not necessarily sufficient. For example, if there are consecutive pairs with edges, but some other pairs not connected, but the transitive closure forms a total order, then the order is unique.

But how to model this.

An alternative Idea: For each node ti in the final order T (except the first), the earliest k must include at least one edge that comes from a node tj where j < i. Among all such edges, the earliest edge that connects to ti and comes from the latest possible tj (i.e., ti-1) is the one that enforces the order.

But I'm not sure.

After some research, I find that the solution to this problem involves two steps:

1. Compute the final topological order T using all m edges.

2. For each node in T, track the maximum position of any node that has an edge to it in the first k edges. The earliest k where, for every node ti (i >= 2), the maximum position of its incoming edges is i-1.

This ensures that each node ti has an incoming edge from ti-1, which forces ti-1 to come before ti in the topological order. If this is true for all nodes, then the topological order is fixed as T.

So, the approach is as follows:

- Compute the final topological order T.

- For each node ti in T (except the first), find the earliest edge in the input sequence that connects from ti-1 to ti. The maximum k among all these edges is the answer. If no such edge exists for any node, then output -1.

But this is not correct. For example, in the first sample, the edges between consecutive pairs are present. The maximum k among these edges is 4 (4->2 is edge 4, 2->1 is edge 1, 1->3 is edge 2. So the maximum is 4). Which matches the sample's output.

In the second sample, the final order could be 1, 3, 2 or 3, 1, 2. But the edges are 1->2 and 3->2. For the final order to be 1, 3, 2, consecutive pairs are 1->3 (no edge) and 3->2. So the earliest edge for 3->2 is edge 2. For 1->3, there is no edge, so this condition is not met, so the answer is -1.

Thus, this approach seems to work.

So, the steps are:

1. Compute the final topological order T using all edges.

2. For each i from 1 to n-1, check if there's an edge from T[i] to T[i+1] in the input. If any such edge is present, record the earliest occurrence in the input.

3. For each i, the earliest occurrence of an edge from T[i] to T[i+1] is the position in the input where this edge was added.

4. The answer is the maximum of all these positions. If any i has no such edge, output -1.

This approach ensures that for all consecutive pairs in T, there's an edge between them, which forces the order. Because if each consecutive pair has an edge, then during the topological sort, each step has exactly one node with in-degree zero (the first node in T), then the next node in T, and so on.

This is because, for each node T[i], the edge from T[i-1] to T[i] ensures that T[i-1] must be processed before T[i]. And since there are no edges from T[j] to T[k] where j > k (since T is a topological order of all edges), the in-degree of T[i] is determined by edges from T[0..i-1].

Thus, the earliest k is the maximum of the positions where the consecutive edges are added.

So, the solution is to:

- Compute the final topological order T.

- For each consecutive pair in T, find the earliest occurrence of an edge between them.

- The maximum of these positions is the answer. If any consecutive pair has no edge between them, return -1.

But wait, the sample input 1 has consecutive pairs 4-2, 2-1, 1-3. The edges between 4 and 2 are added at position 4, between 2 and 1 at position 1, and between 1 and 3 at position 2. The maximum is 4, which is the correct answer.

In sample 2, the final order is either 1-3-2 or 3-1-2. Let's say it's 1-3-2. The consecutive pairs are 1-3 (no edge) and 3-2 (edge at position 2). So since there's no edge between 1 and 3, the answer is -1. Which matches the sample.

Thus, this approach seems correct.

So, the steps are:

1. Perform a topological sort on the entire DAG to get the final order T.

2. For each consecutive pair (T[i], T[i+1]) in T, check if there's an edge from T[i] to T[i+1] in the input. If any pair lacks such an edge, output -1.

3. For each such pair, record the earliest position in the input where this edge was added.

4. The answer is the maximum of these positions.

But why is this correct?

Because the edges between consecutive pairs in T are the critical edges that force the order. If all consecutive pairs have edges in the input, then the topological order must be T. Because during the topological sort, the first node is T[0] (since all edges are from T[0] to other nodes), and each consecutive node must be processed next due to the edge between them.

This ensures that the topological order is unique. Thus, the earliest k where all consecutive pairs' edges are included up to k is the answer.

Thus, the solution involves:

- Finding the final topological order T.

- Checking for each consecutive pair in T if there's an edge between them. If any pair is missing, output -1.

- Otherwise, take the earliest occurrence of each consecutive edge and find the maximum k among them. This is the earliest k where all consecutive edges up to that point have been added, thus ensuring a unique topological order.

Thus, this approach is O(m + n), which is feasible for the problem's constraints.

Now, the steps to implement this are:

1. Compute the final topological order T.

2. For each edge in the input, note the order in which they were added, and for each edge u->v, record the earliest occurrence of u and v being consecutive in T.

3. For each consecutive pair in T, check if there's an edge between them. If any pair has no such edge, output -1.

4. Otherwise, for each consecutive pair, find the earliest edge in the input that matches, and take the maximum of these positions.

The answer is that maximum position.

Thus, the code can be written as follows:

First, build the DAG from all edges and perform a topological sort to get T.

Then, create a dictionary to map each pair (u, v) to the earliest occurrence in the input.

Then, iterate through T's consecutive pairs and check if they exist in the dictionary. If any pair is missing, output -1.

Otherwise, collect the earliest positions and find the maximum.

Now, to implement this:

Implementing Kahn's algorithm to compute the final topological order T.

Then, for each edge in the input, we need to note their positions and check if they are between consecutive pairs in T.

But how to check if an edge u->v is between consecutive pairs in T.

We can precompute a dictionary that maps each node to its position in T. Then, for each edge u->v in the input, if pos[u] + 1 == pos[v], then this edge is a consecutive edge in T.

Thus, for each consecutive pair in T, we can collect all edges in the input that match this pair and track their earliest occurrence.

Finally, for each consecutive pair in T, we need to have at least one edge in the input, and the earliest occurrence of such an edge is recorded. The maximum of these earliest occurrences is the answer.

So, the code steps are:

- Read n and m.

- Read the m edges and store them in a list. Also, build the adjacency list and in-degree array.

- Compute the topological order T using Kahn's algorithm.

- Create a dictionary pos to map each node to its index in T.

- For each consecutive pair (T[i], T[i+1]) in T, check if there's an edge in the input from T[i] to T[i+1]. For this, we need to track all edges that are between consecutive pairs.

- For each edge in the input, check if it's between consecutive nodes in T. For each such edge, record the earliest occurrence.

- For each consecutive pair in T, if there's no such edge, output -1.

- Otherwise, collect the earliest occurrence for each consecutive pair, and the maximum of these is the answer.

Thus, this approach has a time complexity of O(m + n), which is acceptable.

Now, let's test this approach against the samples.

Sample 1:

n=4, m=5.

Edges:

2 1

1 3

2 3

4 2

4 3

The final topological order T is [4, 2, 1, 3].

Consecutive pairs are (4,2), (2,1), (1,3).

The edges that match consecutive pairs:

Edge 4->2 is the fourth edge.

Edge 2->1 is the first edge.

Edge 1->3 is the second edge.

Thus, the earliest positions are 4, 1, 2. The maximum is 4. Hence, output 4.

Sample 2:

n=3, m=2.

Edges: 1->2, 3->2.

The final topological order could be [1,3,2] or [3,1,2], but according to the input, both are possible. However, when we compute T using Kahn's algorithm, the order would depend on the implementation. For example, during Kahn's algorithm, the initial sources are 1 and 3.

Thus, the final order could be [1,3,2], leading to consecutive pairs (1,3) and (3, 2). There is no edge from 1 to 3, so the answer is -1.

Another possible final order is [3,1,2], consecutive pairs (3,1) and (1,2). Edge 3->1 does not exist, so the answer is -1.

Thus, this approach correctly outputs -1.

Thus, this approach works for the samples.

Thus, the code will be:

1. Compute T using Kahn's algorithm.

2. Check consecutive pairs in T for edges between them.

3. If any pair has no edge, output -1.

4. Else, take the maximum of the earliest positions.

Thus, the code will be as follows.
</think>

```python
import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    for idx in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(v)
        in_degree[v] += 1

    # Compute the final topological order using Kahn's algorithm
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
    T = []
    temp_in_degree = in_degree.copy()
    while q:
        u = q.popleft()
        T.append(u)
        for v in adj[u]:
            temp_in_degree[v] -= 1
            if temp_in_degree[v] == 0:
                q.append(v)

    pos = [0] * (n + 1)
    for i in range(n):
        pos[T[i]] = i

    # Check consecutive pairs and track earliest occurrence
    earliest = {}
    for idx, (u, v) in enumerate(edges):
        if pos[u] + 1 == pos[v]:
            pair = (u, v)
            if pair not in earliest:
                earliest[pair] = idx + 1  # 1-based k

    max_k = 0
    for i in range(n - 1):
        u = T[i]
        v = T[i + 1]
        if (u, v) not in earliest:
            print(-1)
            return
        max_k = max(max_k, earliest[(u, v)])

    print(max_k)

if __name__ == "__main__":
    main()
```