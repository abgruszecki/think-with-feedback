<think>
Okay, let's try to figure out this problem. So, the task is to find all edges that are part of exactly one simple cycle. A simple cycle here is one where each vertex is visited exactly once. Hmm. So, any edge that is in exactly one such cycle needs to be identified.

First, I need to think about the structure of the graph. The edges that belong to exactly one simple cycle—how can I find them efficiently?

Let me start by recalling some graph theory concepts. In a graph, edges that are part of cycles are called cyclic edges. But here, it's more specific: they must be in exactly one simple cycle. So, for example, if an edge is part of two different simple cycles, it shouldn't be counted.

But how to detect such edges?

Hmm. Let's think about the properties of such edges. Suppose there's a cycle, and the edge is in that cycle. If the edge is part of only that cycle, then removing that edge would break all cycles that it's part of. But how to find which edges are in exactly one simple cycle.

Wait, maybe we can model the problem using the concept of bridges and edges in cycles. Bridges are edges that are not part of any cycle, so they can be immediately excluded. So first step: remove all bridges. The answer edges must be among the non-bridge edges (since bridges aren't in any cycle).

But not all non-bridge edges are part of exactly one simple cycle. For example, in a graph that's a cycle, all edges are part of exactly one cycle, so they are all included. But if there's a structure where two cycles share an edge, then that edge is part of two cycles and thus should be excluded.

So the key is to find edges that are in exactly one cycle. But the problem says "exactly one simple cycle". How to model this.

Another approach: Let's think about the graph's blocks. A block is a maximal 2-connected subgraph. In a block (which is 2-connected), any two edges are part of a cycle. But how does that relate to the problem?

Wait, in a block, each edge is part of at least one cycle. But if the block is a simple cycle, then each edge is part of exactly one cycle. But if the block is more complex (like two cycles sharing a common edge), then some edges are part of multiple cycles.

So maybe the edges that are in exactly one simple cycle are those that are in a block which is a simple cycle. So, for example, if a block is a cycle (so it's a simple cycle itself), then all edges in that block are part of exactly one simple cycle. But edges in other blocks (like blocks that are 2-connected but not cycles) would have edges that are part of multiple cycles.

Wait, but a 2-connected graph (a block) can have more complex structures. For example, a theta graph: two nodes connected by three internally disjoint paths. In such a graph, any edge in one of the paths is part of multiple cycles.

So, perhaps the answer consists of edges that are part of a block which is itself a simple cycle. Because in that case, each edge is in exactly one cycle. But if a block is a larger 2-connected component (not a cycle), then the edges in it can belong to multiple cycles.

So the plan is to find all edges that are in a block which is a simple cycle. Then, all edges in such blocks are part of exactly one cycle. But edges in blocks that are not cycles (i.e., 2-connected components that have more edges) would have edges that are part of multiple cycles and thus are not part of the answer.

So the steps would be:

1. Find all the blocks (biconnected components) of the graph.
2. For each block, check if it's a simple cycle.
3. If a block is a simple cycle, then all edges in that block are part of exactly one simple cycle.
4. Collect all such edges and output them.

So the problem reduces to decomposing the graph into its biconnected components (blocks), then checking for each block whether it forms a cycle.

Now, how to check if a block is a cycle. For a block to be a cycle, it must have exactly as many edges as vertices. Because a cycle of length k has k edges and k vertices. So, for each block, if the number of edges equals the number of vertices, then the block is a cycle. Otherwise, it's a 2-connected component that's not a cycle (like a graph with a node connected to three others, etc.), and edges in such a component are part of multiple cycles.

So, the steps would be:

- For each block (biconnected component) in the graph:
   - Let the block have V vertices and E edges.
   - If E == V, then this block is a cycle. All edges in this block are part of exactly one cycle.
   - Else, edges in this block are part of multiple cycles and are excluded.

Thus, the answer is the union of all edges in blocks where E equals V.

So, the algorithm is:

1. Find all the biconnected components of the graph.
2. For each component, check if the number of edges equals the number of vertices.
3. Collect all edges in such components.

Now, the challenge is to implement this efficiently for n up to 1e5 and m up to 1e5. The standard way to find biconnected components is using Tarjan's algorithm, which runs in O(V + E) time.

But implementing Tarjan's algorithm for biconnected components in Python with 1e5 nodes and edges might be challenging, especially considering recursion depth. However, since the graph is undirected and the algorithm can be implemented with an explicit stack to avoid recursion stack overflows.

So, the steps for the code:

- Read n and m.
- Read m edges, and store them with their indices (since the output requires the original indices).
- Build an adjacency list, keeping track of the edge index for each edge.
- Perform a biconnected components decomposition to find all blocks.
- For each block, collect all edges in the block.
- For each such block, check if the number of edges equals the number of vertices in the block.
   - The number of vertices in a cycle component is equal to the number of edges. So, in a block that's a cycle, E = V.
   - But how to compute the number of vertices in a block. Each edge in the block connects two vertices, but the vertices in the block are the ones that are part of the component. For example, a block that's a cycle of 3 nodes has 3 edges and 3 nodes. So for each component (block), we can collect all unique vertices in that block and check if E == V.

But collecting all unique vertices for each block may be time-consuming. However, since each edge is part of exactly one block (except for the bridges, which are their own blocks, but bridges are not part of any cycle and thus their blocks have E=1, V=2, which is E != V (since 1 != 2?), so they are not considered). Wait, no. Bridges are part of their own block only if the block is a single edge. For example, a bridge (u, v) is a block where V=2, E=1, so E != V. So such a block would not be considered.

Wait, in the case of a bridge, the block is the edge itself. So for that block, E=1, V=2. So 1 != 2, so the edge is not part of any cycle. So, the bridge edges are automatically excluded from consideration.

So, for each block, we can collect all edges, and for each block, compute the number of unique vertices (V) and edges (E). Then, if E == V, include all edges in that block into the answer.

But how to compute V and E for each block.

Each block is a biconnected component. The number of edges in the block is the size of the edges in the component. For the number of vertices in the block, it's the number of unique vertices in the edges of the component.

But how to compute this efficiently.

Alternatively, for each block, the number of edges is the size of the edge list in that block. The number of vertices can be determined by the union of all endpoints of the edges in the block. For a cycle, each edge is part of the cycle, so each vertex is part of two edges (except in the case of a single cycle where each vertex is part of exactly two edges). Wait, for a cycle of k edges, each vertex is connected to two edges, and there are k vertices and k edges. So the number of vertices would be equal to the number of edges.

But for a general 2-connected component (not a cycle), the number of edges can be larger than the number of vertices. For example, a complete graph of 3 nodes has 3 edges and 3 vertices. So that's a cycle (triangle), which would have E=3, V=3. But a 2-connected component that is a complete graph with more nodes would have E = (n*(n-1))/2. For n=4, E=6, which is larger than V=4. So in that case, edges in such a component would not be part of the answer.

So the key is: for each block, check if the number of edges in the block equals the number of unique vertices in the block.

But how to compute the number of vertices in a block.

Each edge in the block has two endpoints. So for all edges in the block, collect all u and v, put them into a set, and the size of the set is V.

But for m up to 1e5, and per block processing, this could be O(m) time. But since each edge is in exactly one block, the total time across all blocks is O(m), which is acceptable.

So steps for the code:

- Find all blocks (biconnected components) using Tarjan's algorithm, keeping track of which edges are in each block.
- For each block, collect all edges in the block.
- For each such block:
   - Collect all vertices in the edges of the block.
   - Compute V = len(vertices)
   - E = len(edges)
   - If E == V, then add all edges in this block to the answer.
- Finally, collect all such edges, sort them by their original indices, and output.

Now, the challenge is to implement Tarjan's algorithm for biconnected components, correctly handling the edges and their indices.

Let me think about how Tarjan's algorithm works for biconnected components.

Tarjan's algorithm uses a depth-first search (DFS) approach. The key is to find articulation points and split the graph into blocks when an articulation point is found. The algorithm uses a stack to keep track of the edges. When a back edge is found, the algorithm checks if the subtree can form a biconnected component.

But implementing this in Python with 1e5 nodes and edges requires an efficient non-recursive implementation, as recursion depth would exceed Python's default stack limit (which is around 1000). So we need to implement the DFS iteratively.

So, the plan for the code:

Implement an iterative version of Tarjan's algorithm for biconnected components.

But first, let's outline the steps for the iterative DFS.

The algorithm will track for each node:

- discovery time (disc)
- low value (low)

An articulation point is a node u where there exists a child v such that low[v] >= disc[u]. Or, if it's the root and has at least two children.

But for our purposes, the main goal is to collect edges into their respective biconnected components.

The standard approach for edge-based biconnected components:

- Use a stack to keep track of edges as we visit them.
- When a back edge is encountered (indicating a cycle), we pop edges from the stack until we reach the current edge, forming a biconnected component.
- Each time we encounter an articulation point, we split the edges into a component.

But I need to make sure that each edge is part of exactly one component.

So, during the DFS:

- For each edge (u, v), when visited, we push it onto the stack.
- When a back edge is found (i.e., when v is already visited and is not the parent of u), we may start forming a component.
- When we backtrack and find that a node is an articulation point, we pop edges from the stack up to the edge (u, v), which forms a component.

But handling this correctly in iterative code can be a bit tricky.

Alternatively, there's an approach to manage the stack and track the components as they are found.

An alternative approach is to use the standard algorithm for finding biconnected components, which can be found in some references. For example, here's the outline:

Initialize a stack to keep edges.

For each node u not visited, perform a DFS.

During the DFS, for each edge (u, v):

   if v is not visited, push the edge onto the stack, and proceed.

   else if v is visited and v is not the parent of u, then this is a back edge. Push the edge onto the stack.

   Then, after visiting all children of u, if the parent of u is not None, check if low[u] >= disc[parent]. If so, then parent is an articulation point. Pop edges from the stack until the edge (parent, u) is popped. These edges form a biconnected component.

So, the key is to manage the stack correctly and collect the edges into components each time an articulation point is found.

Implementing this iteratively is going to be challenging. Let's think about how to structure the code.

In iterative DFS, we need to keep track of the state for each node. For example, when we visit a node u, we process it and then iterate through its adjacent edges. For each edge (u, v), if v is not visited, we push the current state (u, index of next edge to process, etc.) onto a stack, and then proceed to process v.

But in the case of Tarjan's algorithm, we also need to track the discovery times and low values, as well as the parent of each node.

So, for the iterative approach:

- The stack will hold the nodes to visit, along with their parent, current edge index, and any other necessary state.

But let's think of each entry in the stack as representing a node u, its parent, and the next adjacent edge to process.

The initial setup is to push the starting node (say, u) with parent None and edge index 0.

Then, for each node in the stack:

   For the current node u, we process each adjacent edge in order.

   For each edge (u, v) in the adjacency list:

      If v is not the parent (to avoid processing the parent edge again), then:

          if v is not visited:

              push the edge (u, v) onto the stack of edges.

              mark the discovery time and low value for v.

              push the state (v, u, 0) onto the stack (so that we process v next).

              then break, so that we process v first (like in recursive DFS).

          else:

              if v's discovery time is less than u's (meaning it's an ancestor), then this is a back edge.

              update u's low value with min(low[u], disc[v]).

              push the edge (u, v) onto the edge stack.

      Then, after processing all children (or when we return to the node in the stack), we check if any child's low value is >= disc[u], indicating that u is an articulation point.

      Then, we pop edges from the edge stack until we reach the edge (parent, u), and collect those edges as a biconnected component.

This is a bit vague. Let's see.

Alternatively, the iterative approach can be structured with a stack that holds the nodes and their state. For each node, after processing all its children, we can check if it's an articulation point and process the edges accordingly.

But perhaps the easiest way to proceed is to refer to the standard iterative implementation of Tarjan's algorithm for biconnected components.

Alternatively, since Python has some limitations with recursion depth, perhaps we can find a way to manage the recursive approach with increased recursion limit. However, for n up to 1e5, recursion depth could be as high as 1e5, which would cause a stack overflow. So, the recursive approach is not feasible.

Therefore, implementing the iterative version is necessary.

So, here's a rough outline of the steps for the iterative Tarjan's algorithm for biconnected components:

Initialize disc and low arrays, visited array, parent array.

Initialize a stack for DFS nodes.

For each node u in 1..n:

   if not visited:

      push (u, parent, 0) onto the stack.

      while stack not empty:

          pop (u, parent, index) from stack.

          if index == 0:

              if visited[u], continue.

              visited[u] = True.

              disc[u] = low[u] = time

              time +=1

              children = 0

              is_articulation = False

          else:

              # backtracking from child v

              v = adjacency[u][index-1] (or whatever way to track the child)

              low[u] = min(low[u], low[v])

              if low[v] >= disc[u]:

                  # u is an articulation point

                  # collect all edges from the edge_stack until (u, v) is found.

                  component = []

                  while True:

                      edge = edge_stack.pop()

                      component.append(edge)

                      if edge == (u, v) or edge == (v, u):

                          break

                  add component to the list of blocks.

              if parent is not None and low[v] >= disc[u]:

                  is_articulation = True

          # process next edge

          while index < len(adj[u]):

              v = adj[u][index]

              if v == parent:

                  index +=1

                  continue

              if not visited[v]:

                  edge = (u, v)

                  edge_stack.append(edge)

                  parent_stack.append((u, parent, index+1)) # save current state

                  stack.append( (u, parent, index+1) )

                  # push the child to process

                  stack.append( (v, u, 0) )

                  index +=1

                  break

              else:

                  # back edge

                  if disc[v] < disc[u]: # v is ancestor of u

                      low[u] = min(low[u], disc[v])

                      edge = (u, v)

                      edge_stack.append(edge)

                  index +=1

          else:

              # all edges processed

              if parent is None and children > 1:

                  is_articulation = True

              if is_articulation:

                  # collect the edges for this component.

                  pass # but how?

              # After processing all children, check if parent is articulation point.

              # This part is tricky.

Hmm. This is getting complicated. Maybe looking up an iterative implementation of Tarjan's algorithm for biconnected components.

Alternatively, perhaps using the approach where each time we visit a back edge, we collect the component.

Alternatively, I can look for existing Python code for biconnected components and adapt it.

But given time constraints, perhaps the best way is to find an iterative approach.

Alternatively, here's another approach to track the edge stack and the components:

Each time we start processing a node u (when we first pop it from the stack with index 0), we push all edges to unvisited children. When backtracking, if a child's low is >= disc[u], then u is an articulation point, and we pop edges from the edge stack until we reach the edge (u, child). These edges form a component.

But in the iterative approach, after processing all children of u, we need to check for each child whether low[child] >= disc[u], and if so, collect the edges.

But this might be tricky.

Alternatively, here's an alternative approach inspired by the standard method:

Initialize a stack that holds (u, parent, iterator over adj[u], visited_before).

The 'iterator' allows us to track which edges have been processed.

Each time we enter a node u for the first time (visited_before is False), we process it: mark as visited, record disc and low, initialize the iterator to the first edge.

Then, we process each edge in adj[u] in order, skipping the parent.

For each edge (u, v):

   if v is parent: continue.

   if v not visited:

       push (u, parent, current iterator position, True) back to the stack.

       push (v, u, adj[v], False) to the stack.

       push the edge (u, v) to the edge stack.

   else:

       if disc[v] < disc[u]:  # back edge to ancestor

           low[u] = min(low[u], disc[v])

           push the edge (u, v) to the edge stack.

Once all edges are processed (when the iterator is exhausted), we check if u is an articulation point. If u is not the root and low[u] >= disc[parent], then parent is an articulation point. Then, we pop edges from the edge stack until we reach (parent, u), and those edges form a component.

Wait, but how to track when all edges are processed. The stack approach would track the iterator's progress, allowing us to resume processing after returning from a child.

This seems manageable.

Let me try to outline the code steps:

Initialize:

- disc and low arrays, initialized to 0.

- visited array, initialized to False.

- edge_stack = []  # to collect edges as we traverse.

- components = []  # list of lists of edges, each list is a biconnected component.

- parent = {u: None for u in all nodes}.

For each node u in 1..n:

   if not visited[u]:

       stack = [ (u, None, iter(adj[u]), False) ]

       while stack:

           u, parent_u, edges, is_child_processed = stack.pop()

           if not is_child_processed:

               if visited[u]:

                   continue

               visited[u] = True

               disc[u] = low[u] = time

               time +=1

               # Push back into the stack with is_child_processed = True

               stack.append( (u, parent_u, edges, True) )

               # Now, process the edges.

               # Reset the iterator to the start.

               edges = iter(adj[u])

               # Push all the edges to unvisited children.

               # For each edge in adj[u], check if it's to parent, and process.

               # So, create a new list of edges, but in reverse order since stack is LIFO.

               # Because when we process them, we want to process in order.

               # Hmm, perhaps we need to reverse the order to process in the correct sequence.

               # Let's collect all edges except to parent.

               children = []

               for v in adj[u]:

                   if v == parent_u:

                       continue

                   children.append( (u, v) )

               # Now, we need to process them in reverse order to maintain the same order as recursion.

               # Because stack is LIFO, pushing them in reverse order ensures that the first edge is processed first.

               for edge in reversed(children):

                   v = edge[1]

                   if not visited[v]:

                       edge_stack.append( (u, v) )

                       stack.append( (v, u, iter(adj[v]), False) )

                   else:

                       # back edge.

                       if disc[v] < disc[u]:  # v is ancestor.

                           low[u] = min(low[u], disc[v])

                           edge_stack.append( (u, v) )

           else:

               # All children processed.

               # Now, check each child to update low[u]

               for v in adj[u]:

                   if v == parent_u:

                       continue

                   if low[v] < low[u]:

                       low[u] = low[v]

               # Now, check if u is an articulation point.

               if parent_u is not None and low[u] >= disc[parent_u]:

                   # pop edges until (parent_u, u) is found.

                   component = []

                   while True:

                       edge = edge_stack.pop()

                       component.append( edge )

                       if edge == (parent_u, u) or edge == (u, parent_u):

                           break

                   components.append( component )

               # Also, if root node and has more than one child, but that's handled by the first case.

This is getting a bit complex, and I'm not sure if it's correct.

Alternatively, perhaps using the code from the following resource:

https://cp-algorithms.com/graph/bridge-searching.html#implementation

The standard bridge finding algorithm can be adapted to find biconnected components.

Wait, the standard bridge-finding algorithm can be modified to collect edges into the components. Each time a bridge is found, the edges that form a component are the ones that were visited up to that bridge.

But integrating the collection of edges into components might require some changes.

Alternatively, here's a way to collect the edges in the components using the edge stack:

Each time a new edge is processed (either tree edge or back edge), it is pushed onto the edge stack.

When an articulation point is found (i.e., when a bridge is detected), the edges up to the bridge are popped and form a component.

But for biconnected components, each component is a maximal subgraph with no articulation points. So the edges between articulation points form the boundaries of the components.

Thus, during the processing of the articulation point, we can collect the edges that form a component.

In code:

Whenever during the backtracking phase, we find that low[v] >= disc[u], then u is an articulation point, and the edges from the edge stack up to (u, v) form a component.

So, the steps are:

- During DFS, each edge is pushed onto the stack when first visited (tree edges) or when a back edge is found.

- When an articulation point is found (u), and after processing a child v where low[v] >= disc[u], we pop all edges from the edge stack until (u, v) is encountered. Those edges form a biconnected component.

- Additionally, after the entire DFS is complete, if there are edges left in the stack, they form another component.

But the root node may require special handling.

But I'm not sure. This seems similar to the approach used in some implementations.

For example, here's a Python implementation idea inspired by the standard approach:

We maintain an edge_stack. Every time we traverse a tree edge (u, v), we push it onto the stack. When we find a back edge (u, v) (v is already visited and is an ancestor), we push that edge onto the stack.

When we discover that a child v of u has low[v] >= disc[u], indicating that u is an articulation point, we pop all edges from the stack until we reach (u, v). These edges form a component. Then, if (u, parent) is a bridge, that edge is a separate component.

But perhaps this is how the edge-based biconnected components are collected.

So, in code:

Initialize edge_stack as a list.

During DFS:

for each node u:

   when visiting a child v via edge (u, v):

      push (u, v) onto edge_stack.

      when backtracking from v to u:

          if low[v] >= disc[u]:

              # u is an articulation point.

              # pop all edges from stack until (u, v) is found.

              component = []

              while True:

                  edge = edge_stack.pop()

                  component.append( edge )

                  if edge == (u, v) or edge == (v, u):

                      break

              add component to components list.

This way, each time an articulation point is found, a component is formed.

Additionally, after the entire DFS, any remaining edges in the edge_stack form a component (the root's component).

But how does this handle multiple components?

Now, let's think about the example where the graph is a single cycle. Then, there are no articulation points. So, the edge_stack would contain all edges. But since there's no articulation point, the code would not collect any components during the DFS. So, after the DFS, we need to collect the remaining edges in the edge_stack as a component.

Thus, after processing all nodes, if the edge_stack is not empty, we need to pop all edges into a component.

So, after the DFS loop:

if edge_stack is not empty:

   component = list(edge_stack)

   components.append( component )

   edge_stack.clear()

So, in code:

Once all nodes have been processed, check if there are edges left in edge_stack. Those edges form a component.

So, putting this all together, the code for biconnected components would collect all components.

Now, in the problem, edges can be represented as tuples (u, v), but since edges are undirected, we need to make sure that (u, v) and (v, u) are treated as the same edge. However, the original input edges are in a certain direction. So, for the purpose of tracking which original edge index each edge has, we need to map each (u, v) and (v, u) to the correct original index.

But wait, the original edges are given in order, each with their own index. For example, if an edge is input as (u, v) as the i-th edge, then when the algorithm encounters (v, u) during traversal (since the graph is undirected), we need to correctly map it back to the original edge index.

Thus, when building the adjacency list, each edge is stored in both directions with their original index. For example, the edge (u, v) with index i is stored in adj[u] as (v, i), and in adj[v] as (u, i).

Thus, during the traversal, whenever we traverse an edge (u, v) or (v, u), we can track the original edge index.

So, the adjacency list is built as:

adj = [[] for _ in range(n+1)]

for each edge in input:

   u, v = map(int, input().split())

   adj[u].append( (v, index) )

   adj[v].append( (u, index) )

where index is the 1-based index of the edge.

Thus, during the traversal, when we process an edge (u, v), we can get the index.

But in the edge_stack, we need to track the edge in the direction it was traversed, but the original index is the same regardless of direction.

Thus, when we collect edges into a component, each edge is represented as (u, v, index), but in the stack, we can store tuples of (u, v, index). But since the edges are stored in both directions in the adjacency list, how to avoid duplicates?

Wait, perhaps during the traversal, when we visit an edge (u, v), we take the original index from the adjacency list.

But since each edge is added to the adjacency list twice (once for each direction), but each time with the same index, it's not a problem.

For example, when the edge (u, v) is processed as part of u's adjacency list, it's stored as (v, i). When processed as part of v's adjacency list, it's stored as (u, i). So, when adding the edge to the edge_stack, the index is i in both cases.

Thus, during the component collection, each edge in the component is represented by (u, v, i), but when checking for equality, it's sufficient to compare the index. Or, perhaps, just track the index.

Alternatively, when processing edges, we can store the index in the edge_stack. But how?

Wait, in the adjacency list, each entry is (v, index). So when processing an edge (u, v) in the code, the index is known. So during the traversal, when we push the edge (u, v) to the edge_stack, we can push the index.

But this requires tracking the index for each edge. So perhaps the edge_stack should contain tuples of (u, v, index) or just the index.

Wait, perhaps it's better to track the edge's index. Because during the component collection, the actual direction of the edge doesn't matter; the index is unique. So, perhaps when processing an edge (u, v) with index i, we can add i to the edge_stack, regardless of the direction. Then, when popping edges from the stack, we can collect the indices, and each index is unique and belongs to exactly one component.

But how to do that.

Let me think again. The adjacency list for each node u contains tuples (v, index). So, when we traverse from u to v, we have the index i of the edge. So, when pushing to the edge_stack, we can push i. But since each edge is bidirectional, but the same index is stored for both directions. So, even if we traverse the edge in the reverse direction, the index will be the same.

Thus, the edge_stack can be a list of indices. But we have to make sure that when traversing an edge in either direction, we add its index to the stack once.

But how to avoid adding the same edge twice. For example, when we traverse (u, v) and then (v, u), we may end up adding the same index twice to the stack.

This is a problem because during the component collection, we need to have each edge in exactly one component.

Wait, but in an undirected graph, each edge is represented twice in the adjacency list. So, during the DFS, when we traverse an edge (u, v), we may process it once as (u, v) and once as (v, u). But to avoid processing the same edge twice, during the DFS, we need to mark which edges have been processed.

But in the standard approach for undirected graphs, the DFS marks the parent node to avoid revisiting the parent. But this doesn't track the edges. So, in the case of a cycle, the edges can be processed in both directions, leading to adding their indices to the edge_stack twice. This would cause the same index to appear in multiple components, which is incorrect.

Ah, this is a problem. So the current approach would process each edge twice (once in each direction), leading to duplicate entries in the edge_stack, which would result in the same edge index being added to multiple components.

Thus, we need a way to ensure that each edge is processed exactly once, regardless of direction.

The solution is to track visited edges. But how?

Each edge has a unique index, so during the traversal, when we process an edge (u, v) with index i, we can mark that index as visited. But since the edge is undirected, we need to make sure that the same index is not processed again.

But how to track this. For example, when traversing from u to v, the edge index i is processed and added to the edge_stack. Then, when later traversing from v to u via the same index i, we should not process it again.

But how to track this. Since the edge is undirected, the code must process each edge once, in whichever direction it is first encountered.

But in the standard DFS for undirected graphs, edges are tracked by their parent. For example, when visiting node u from parent p, all edges except (u, p) are considered. But this approach doesn't track edges by their indices.

Thus, in our case, when processing an edge (u, v) with index i, we need to mark that i has been processed. But when the code traverses the edge in the reverse direction (v, u), we should not process it again.

So, perhaps during the DFS, when processing an edge (u, v) with index i, we check if i is already in a set of processed edges. If not, we add it to the edge_stack and mark it as processed. But this approach would require a way to track processed edges.

But modifying the code to track processed edges could complicate things.

Alternative approach: since each edge is represented in the adjacency list in both directions, but with the same index, when we process an edge (u, v) with index i, we can add i to the edge_stack only if it hasn't been added before. But how to check that.

Alternatively, during the traversal, when visiting an edge (u, v), we can mark the edge as visited. However, since the edge is bidirectional, we need to track it in a way that (u, v) and (v, u) are considered the same edge. But since the edge is stored with the same index in both directions, the index is sufficient.

Thus, during the traversal, whenever we process an edge (u, v) with index i, we can check if i has been visited. If not, process it, add to edge_stack, and mark as visited. Then, when the reverse edge is encountered, it's already marked as visited, so we skip it.

But how to implement this in the DFS.

Let's modify the adjacency list to include the edge index. For each edge, the adjacency list for u contains (v, i), and for v contains (u, i). So, during the traversal, when processing an edge (u, v, i), we can check if i is in a processed set. If not, process it, add to the edge_stack, and mark as processed.

But this requires maintaining a processed_edges set. However, since the algorithm needs to be O(V + E), this approach is feasible.

So, during the DFS:

processed_edges = set()

for each node u in adj:

   if not visited[u]:

       start DFS.

       for each edge (u, v, i) in adj[u]:

           if i not in processed_edges:

               processed_edges.add(i)

               push i to edge_stack.

               process the edge.

But this approach would not work with the current Tarjan's algorithm for biconnected components, as the algorithm relies on visiting edges in a certain order and adding them to the stack regardless of direction.

Alternatively, perhaps the code can be adjusted to process each edge exactly once, regardless of direction. But I'm not sure how to integrate this with the existing edge_stack management.

Alternatively, perhaps when building the adjacency list, for each edge, we only add it once. But that would not work for undirected graphs.

Hmm. This is getting quite complicated. Maybe there's another approach.

Another idea: each edge is represented in the adjacency list twice (for undirected). But during the traversal, when processing an edge (u, v), we can process it only if u < v. This way, each edge is processed once. But this requires that the graph is considered as directed edges where u < v. But this would not capture all possible back edges.

Alternatively, perhaps the edge indices are tracked in a way that each edge is processed once. For example, when processing (u, v), we can add the edge to the stack only once, based on their indices. But this requires checking the processed_edges set.

But modifying Tarjan's algorithm to track processed edges complicates the algorithm. However, given the problem's constraints, this may be necessary.

Alternatively, perhaps when processing an edge (u, v) with index i, during the DFS, we can check if the current node u has a parent. If the parent is v, then we skip the edge (since it's the reverse edge). But this is already handled in the standard DFS for undirected graphs.

Yes, in the standard approach, when processing edges during DFS, you skip the edge that leads back to the parent. So for undirected graphs, each edge is processed once in each direction, but the parent check prevents processing the same edge twice. For example, when you go from u to v, you process v's edges except for u. So when you are at v, you process all edges except for the one leading back to u.

Wait, no. The standard approach for undirected graphs is to track the parent when visiting a node. For example, when you visit v from u, you don't process the edge (v, u) again. Because when you process v's adjacency list, you skip the parent (u). So, each edge is processed exactly once during the DFS traversal.

But in this case, the edge (u, v) is processed in one direction (from u to v), and the reverse direction (v to u) is only processed if the DFS visits v from another node other than u.

But this depends on the graph's structure. For example, in a cycle, each edge is processed exactly once during the DFS traversal.

Thus, in the standard DFS for undirected graphs, each edge is processed exactly once, and the parent tracking ensures that we don't process the same edge in both directions.

So, in the code, when processing the edges of node u, we skip the parent. So, the edge (u, parent) is not processed again. Thus, each edge is processed exactly once.

Thus, in the edge_stack, each edge's index is added exactly once.

Thus, the problem of duplicate edge indices in the edge_stack is avoided.

Thus, during the traversal, each edge is processed exactly once. So, the edge_stack will contain each edge's index exactly once.

Thus, when collecting components, each edge's index is part of exactly one component.

This is critical for the correctness of the algorithm.

Thus, the code can proceed as follows:

In the adjacency list, each edge is stored with its index. For example, adj[u] contains (v, i) for each edge between u and v with index i.

During the DFS, when processing node u, for each (v, i) in adj[u], if v is not the parent of u, then process this edge. The parent of u is tracked, so the reverse edge (u, parent) is skipped.

Thus, each edge is processed exactly once during the DFS.

Thus, when building the edge_stack, each edge's index is added exactly once.

Thus, the code can proceed by pushing the index i onto the edge_stack when processing the edge (u, v, i), but only if v is not the parent.

Thus, in the code:

When processing edge (u, v, i):

   if v is not parent:

       push i onto edge_stack.

       proceed.

Thus, the edge_stack contains the index of each edge exactly once.

Thus, when we collect the components, each edge is part of exactly one component.

Thus, the code for collecting the components would work as follows:

During the DFS, when backtracking and finding that u is an articulation point (low[v] >= disc[u]), we pop edges from the edge_stack until we find the edge (u, v). But since the edge_stack contains indices, we need to track which edges are part of the component.

But how to know when we've found the edge (u, v) in the stack. Because the edge_stack contains indices, not the actual edges. So, when we process the edge (u, v), we pushed its index i into the stack. But when backtracking from v to u, how do we know which index i corresponds to the edge (u, v)?

Wait, the problem is that when we process the edge (u, v) during the forward traversal, we push its index i into the stack. Then, when we backtrack and detect that u is an articulation point (after processing v), we need to pop all indices from the stack until we find the index i of the edge (u, v).

But how to track the index i of the edge (u, v) when backtracking.

This seems challenging. Because during the backtracking phase, when we're processing the child v of u, we need to know which edge was used to reach v. But the edge's index is known at the time of processing.

So, perhaps during the DFS, when processing a child v via edge (u, v, i), we can store the index i in the stack along with other information. This way, during the backtracking phase, when we process the articulation point, we can retrieve the index i of the edge (u, v) and use it to stop popping the edge_stack.

Thus, modifying the stack entries to include the edge index when processing a child.

For example, the stack entries could be tuples representing the current node, parent, iterator, is_child_processed, and the edge index that was used to reach this node.

But this complicates the stack management.

Alternatively, during the forward processing of an edge (u, v, i), we can record the index i and push it into a separate stack that tracks the tree edges. Then, when backtracking, we can pop this stack to find the edge index i corresponding to the child v.

But this adds another data structure to manage.

Alternatively, perhaps when processing a child v via edge (u, v, i), we can push the index i into a 'tree_edge_indices' stack. Then, when backtracking from v to u, we can retrieve the index i from the top of this stack.

But this approach would require maintaining a separate stack for tree edges.

Let's outline this approach:

During the DFS:

   When processing a tree edge (u, v, i) (i.e., when v is unvisited), push i into tree_edge_indices.

   When backtracking from v to u, pop the top of tree_edge_indices to get the edge index i.

   Then, if u is an articulation point, pop the edge_stack until we encounter i.

But this requires that for each tree edge, we track its index in the tree_edge_indices stack.

Then, during backtracking, when checking if u is an articulation point, we retrieve the edge index i from the tree_edge_indices stack.

But how to handle multiple children.

For example, when processing multiple tree edges from u, each tree edge's index is pushed into tree_edge_indices stack. When backtracking from each child, we pop the index.

But the order of processing and backtracking would ensure that the tree_edge_indices stack correctly reflects the current tree edge.

This approach seems feasible.

Thus, the code can be modified as follows:

Initialize:

   tree_edge_indices = []

During the DFS:

   when processing a tree edge (u, v, i):

       push i into tree_edge_indices.

   when backtracking from v to u:

       pop i from tree_edge_indices.

       if low[v] >= disc[u]:

           component = []

           while True:

               j = edge_stack.pop()

               component.append(j)

               if j == i:

                   break

           components.append( component )

Thus, during backtracking from v to u, the index i is the tree edge's index. We pop all edges from the edge_stack until we find i.

Thus, this correctly captures the component formed by the edges up to and including the tree edge i.

Additionally, after processing all nodes, any remaining edges in the edge_stack form a component.

Thus, this approach should correctly collect all biconnected components.

Now, putting this all together into code.

The steps for the code are:

1. Read n, m.

2. Read m edges, storing them in a list with their indices (1-based).

3. Build an adjacency list where each entry is a tuple (neighbor, index).

4. Perform a DFS to find all biconnected components, tracking the edge indices.

5. For each component, check if the number of edges equals the number of vertices in the component.

6. Collect all edges from such components.

7. Output the edges in increasing order of their indices.

Thus, the code outline is:

import sys

from sys import stdin

def main():

    n, m = map(int, stdin.readline().split())

    edges = []

    adj = [[] for _ in range(n+1)]

    for i in range(1, m+1):

        u, v = map(int, stdin.readline().split())

        edges.append( (u, v) )

        adj[u].append( (v, i) )

        adj[v].append( (u, i) )

    disc = [0]*(n+1)

    low = [0]*(n+1)

    time_stamp = 1

    visited = [False]*(n+1)

    edge_stack = []

    tree_edge_stack = []

    components = []

    def dfs(u):

        nonlocal time_stamp

        stack = [ (u, -1, 0, False) ]  # (node, parent, edge_idx, visited)

        while stack:

            u, parent, edge_idx, visited_flag = stack.pop()

            if not visited_flag:

                if visited[u]:

                    continue

                visited[u] = True

                disc[u] = low[u] = time_stamp

                time_stamp += 1

                # Push back into the stack with visited_flag=True

                stack.append( (u, parent, edge_idx, True) )

                # Process all edges

                edge_list = adj[u]

                # Iterate over edges, skipping the parent

                children = []

                for (v, i) in edge_list:

                    if v == parent:

                        continue

                    children.append( (v, i) )

                # Push children in reverse order to process them in order

                for idx in reversed( range(len(children)) ):

                    v, i = children[idx]

                    if not visited[v]:

                        # Tree edge

                        tree_edge_stack.append(i)

                        edge_stack.append(i)

                        stack.append( (v, u, i, False) )

                    else:

                        # Back edge

                        if disc[v] < disc[u]:

                            edge_stack.append(i)

                            low[u] = min(low[u], disc[v])

            else:

                # After processing all children, update low[u]

                for (v, i) in adj[u]:

                    if v == parent:

                        continue

                    if visited[v] and disc[v] < disc[u]:  # back edge

                        low[u] = min(low[u], low[v])

                    elif visited[v] and disc[v] > disc[u]:  # tree edge

                        low[u] = min(low[u], low[v])

                # Check if u is an articulation point

                if parent != -1 and low[u] >= disc[parent]:

                    component = []

                    while True:

                        j = edge_stack.pop()

                        component.append(j)

                        if j == tree_edge_stack[-1]:

                            break

                    tree_edge_stack.pop()

                    components.append(component)

        # After processing root node, check if any edges are left in edge_stack

    for u in range(1, n+1):

        if not visited[u]:

            dfs(u)

    # Check if there are any edges left in edge_stack

    if edge_stack:

        components.append( edge_stack.copy() )

        edge_stack.clear()

    # Now, process each component to see if it's a cycle.

    answer_edges = set()

    for component in components:

        # Get all edges in the component.

        edge_indices = component

        # Get all vertices involved in these edges.

        vertices = set()

        for idx in edge_indices:

            u, v = edges[idx-1]  # since edges are 0-based in the list.

            vertices.add(u)

            vertices.add(v)

        V = len(vertices)

        E = len(edge_indices)

        if V == E:

            answer_edges.update( edge_indices )

    # Collect the answer edges in sorted order.

    sorted_edges = sorted( answer_edges )

    print( len(sorted_edges) )

    if sorted_edges:

        print( ' '.join( map(str, sorted_edges) ) )

    else:

        print()

if __name__ == "__main__":

    main()

Wait, but this code has several issues. For example, during the backtracking phase, the code processes each edge again, which may not be correct. Also, the way the low values are updated may be incorrect.

Another potential issue is the way the edge_stack and tree_edge_stack are handled. For example, when processing back edges, the code adds them to the edge_stack, but the tree_edge_stack only contains tree edges. So, when popping edges during articulation point processing, the code may not find the tree edge index in the edge_stack, leading to an infinite loop.

Another problem is that the code for the root node may leave edges in the edge_stack, which are then added to components after the loop. But the root node may have multiple components.

But this is getting quite complex. To ensure correctness, perhaps it's better to refer to an existing implementation or to test the code against the sample inputs.

Let's test the first sample input:

Sample Input 1:

3 3

1 2

2 3

3 1

The graph is a cycle of 3 nodes, so all edges are part of a single component.

The code should collect this component. The component has V=3 and E=3, so all edges are included in the answer.

The output should be 3 edges, which is correct.

Sample Input 2:

6 7

2 3

3 4

4 2

1 2

1 5

5 6

6 1

The components would be:

- The cycle 2-3-4-2 (edges 1, 2, 3)

- The cycle 1-2 (edge 4 is a bridge? No. Wait, the sample input includes edges 1-2, which connects the cycle 2-3-4 to the rest. But how are the components structured.

Wait, the sample input's output is 6 edges. The edges are 1, 2, 3 (the cycle 2-3-4), 5, 6, 7 (edges 1-5, 5-6, 6-1). These form two cycles. So each of these two cycles is a component with E=V.

Thus, each of these two cycles contribute their edges to the answer.

But the edge 4 (1-2) is a bridge, because removing it disconnects the two cycles. So it's not part of any cycle, and thus not included.

Thus, the code should capture these two cycles.

The code should detect that each of these two components has E=V.

So, the code's components should include the edges 1,2,3 as one component and 5,6,7 as another. Each has 3 edges and 3 vertices. So they are included in the answer.

The fourth edge is a bridge, so it's part of a component with V=2 (nodes 1 and 2), E=1. Thus, E != V, so it's not included.

Thus, the code should output 6 edges, which matches the sample.

Sample Input 3:

5 6

1 2

2 3

2 4

4 3

2 5

5 3

The edges form a more complex structure. The output is 0.

The code's components may have E > V, so no edges are included.

Thus, the code should output 0.

But the code needs to correctly process these cases.

Thus, the code's logic seems correct. However, the implementation may have bugs.

Now, considering the code's iterative DFS approach and the way components are collected.

But given time constraints, it's best to proceed with writing the code, then test it against the samples.

In the code, during the backtracking phase, after processing all children, the code checks if the current node is an articulation point by comparing low[u] >= disc[parent]. If so, it pops edges from edge_stack until the tree edge's index is found.

The tree_edge_stack is used to track the indices of tree edges. Each time a tree edge is processed (child is unvisited), the index is pushed to tree_edge_stack and edge_stack. When backtracking, after processing the child, the index is popped from tree_edge_stack.

When an articulation point is found, the code pops edges from edge_stack until it reaches the current tree edge's index, which is at the top of tree_edge_stack.

But in the code provided, during the backtracking phase, after the for loop over adj[u], the code checks if parent != -1 and low[u] >= disc[parent]. If so, it pops components.

But perhaps the code isn't correctly handling the low values.

The code for updating low[u] is:

for (v, i) in adj[u]:

    if v == parent:

        continue

    if visited[v] and disc[v] < disc[u]:  # back edge

        low[u] = min(low[u], low[v])

    elif visited[v] and disc[v] > disc[u]:  # tree edge

        low[u] = min(low[u], low[v])

But this may not be correct. The standard way to update low[u] is:

for each child v of u:

    low[u] = min(low[u], low[v])

for each back edge (u, v):

    low[u] = min(low[u], disc[v])

Thus, the code's approach to updating low[u] may be incorrect.

In the code's current implementation, during the backtracking phase (visited_flag is True), the code iterates over all edges in adj[u], including back edges. For tree edges (disc[v] > disc[u]), it updates low[u] to min(low[u], low[v]). For back edges (disc[v] < disc[u]), it updates low[u] to min(low[u], disc[v]).

But this may not be correct, because during the backtracking phase, the code is processing the children of u. For each tree edge (u, v), after v has been processed, we can update low[u] based on low[v].

But the code's approach to iterate over all edges in adj[u] during the backtracking phase may be incorrect.

Thus, the code may be incorrectly computing the low values, leading to incorrect component identification.

Thus, the code needs to be modified to correctly compute the low[u] values.

The correct way to compute low[u] is:

When processing a tree edge (u, v), after v has been processed, low[u] is the minimum of its current value and low[v].

When processing a back edge (u, v), low[u] is the minimum of its current value and disc[v].

Thus, during the forward processing of edges (when visited_flag is False), when a back edge is found, we push the edge to the edge_stack and update low[u] with disc[v].

Then, during the backtracking phase (visited_flag is True), for each tree edge (u, v), we update low[u] with low[v].

But how to track which edges are tree edges.

This suggests that during the forward processing, the code should track which edges are tree edges and which are back edges.

Thus, modifying the code:

During the forward processing (visited_flag is False):

   for each (v, i) in adj[u], if v is not parent:

       if not visited[v]:

           it's a tree edge. Process it.

       else:

           if disc[v] < disc[u], it's a back edge. Process it.

Thus, during the backtracking phase, the code can process only the tree edges.

But in the current code's backtracking phase, it's processing all edges again.

Thus, the code may be incorrect in updating the low values.

To fix this, perhaps during the backtracking phase, the code should iterate over the tree edges (children) of u and update low[u] accordingly.

But how to track which edges are tree edges.

Thus, during the forward processing, when a tree edge is processed, the code can store the children and their edge indices.

Thus, during the forward processing:

   when processing a tree edge (u, v), add v to a list of children.

Then, during backtracking, iterate over these children to update low[u].

Thus, modifying the code:

In the stack entry, store the children of u.

Thus, the code can be modified as follows:

During the forward processing (visited_flag is False):

   when u is first visited:

       disc[u] = low[u] = time_stamp

       time_stamp += 1

       stack.append( (u, parent, children, 0, True) )

       children = []

       for (v, i) in adj[u]:

           if v == parent:

               continue

           if not visited[v]:

               children.append( (v, i) )

           else:

               if disc[v] < disc[u]:

                   # back edge

                   edge_stack.append(i)

                   low[u] = min(low[u], disc[v])

       # Push tree edges in reverse order

       for (v, i) in reversed(children):

           edge_stack.append(i)

           tree_edge_stack.append(i)

           stack.append( (v, u, [], 0, False) )

       stack.append( (u, parent, children, len(children), True) )

But this is getting quite complex.

Alternatively, perhaps the code should track for each node u its children, and during backtracking, update low[u] based on the children's low values.

But this requires storing the children of each node.

Thus, modifying the code to track children during the forward phase:

In the stack entries, store the children list.

Thus, during the forward processing:

   when u is first visited:

       collect all children (tree edges) and back edges.

       process back edges.

       push the children to the stack in reverse order.

       store the children list in the stack entry.

During backtracking:

   for each child in children:

       low[u] = min(low[u], low[child])

Thus, the code can be rewritten as follows:

def main():

    n, m = map(int, stdin.readline().split())

    edges = []

    adj = [[] for _ in range(n+1)]

    for i in range(1, m+1):

        u, v = map(int, stdin.readline().split())

        edges.append( (u, v) )

        adj[u].append( (v, i) )

        adj[v].append( (u, i) )

    disc = [0]*(n+1)

    low = [0]*(n+1)

    time_stamp = 1

    visited = [False]*(n+1)

    edge_stack = []

    tree_edge_stack = []

    components = []

    for u in range(1, n+1):

        if not visited[u]:

            stack = [ (u, -1, [], 0) ]  # (node, parent, children, ptr)

            while stack:

                u, parent, children, ptr = stack.pop()

                if ptr == 0:

                    if visited[u]:

                        continue

                    visited[u] = True

                    disc[u] = low[u] = time_stamp

                    time_stamp +=1

                    # Collect children and back edges

                    new_children = []

                    back_edges = []

                    for (v, i) in adj[u]:

                        if v == parent:

                            continue

                        if not visited[v]:

                            new_children.append( (v, i) )

                        else:

                            if disc[v] < disc[u]:

                                back_edges.append( (v, i) )

                    # Process back edges

                    for v, i in back_edges:

                        edge_stack.append(i)

                        low[u] = min(low[u], disc[v])

                    # Push new children in reverse order

                    stack.append( (u, parent, new_children, 1) )

                    for idx in reversed(range(len(new_children))):

                        v, i = new_children[idx]

                        edge_stack.append(i)

                        tree_edge_stack.append(i)

                        stack.append( (v, u, [], 0) )

                else:

                    # After processing all children

                    for v, i in children:

                        low[u] = min(low[u], low[v])

                    # Check if articulation point

                    if parent != -1 and low[u] >= disc[parent]:

                        component = []

                        while True:

                            j = edge_stack.pop()

                            component.append(j)

                            if j == tree_edge_stack[-1]:

                                break

                        tree_edge_stack.pop()

                        components.append(component)

                    # Process parent's articulation point

    # After processing all nodes, check if edge_stack has remaining edges

    if edge_stack:

        components.append(edge_stack.copy())

        edge_stack.clear()

    # Now process components

    answer = set()

    for comp in components:

        edge_indices = comp

        vertices = set()

        for idx in edge_indices:

            u, v = edges[idx-1]

            vertices.add(u)

            vertices.add(v)

        V = len(vertices)

        E = len(edge_indices)

        if V == E:

            answer.update(edge_indices)

    sorted_ans = sorted(answer)

    print(len(sorted_ans))

    if sorted_ans:

        print(' '.join(map(str, sorted_ans)))

    else:

        print()

This code uses a different approach, where each stack entry tracks the current node, parent, children, and pointer to track processing. The children are collected during the initial phase, and back edges are processed. Then, the children are processed in reverse order.

During the backtracking phase (when ptr is 1), the code updates the low[u] values based on the children's low values.

This approach should correctly compute the low values.

Testing this code against the sample inputs:

Sample Input 1:

3 3

Edges form a cycle. The component has 3 edges and 3 vertices. So it's included. Output is 3 edges.

Sample Input 2:

The code should detect two components with E=V. Thus, output 6 edges.

Sample Input 3:

All components have E != V. Thus, output 0.

Thus, this code should work correctly.

But implementing this requires careful handling of the stack and edge tracking.

Overall, this code should handle the problem correctly, by decomposing the graph into biconnected components, checking each component for being a cycle (E=V), and collecting the edges from such components.
</think>

```python
import sys
from sys import stdin
from sys import setrecursionlimit

def main():
    n, m = map(int, stdin.readline().split())
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(1, m + 1):
        u, v = map(int, stdin.readline().split())
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))

    disc = [0] * (n + 1)
    low = [0] * (n + 1)
    time_stamp = 1
    visited = [False] * (n + 1)
    edge_stack = []
    tree_edge_stack = []
    components = []

    for u in range(1, n + 1):
        if not visited[u]:
            stack = [(u, -1, [], 0)]
            while stack:
                u, parent, children, ptr = stack.pop()
                if ptr == 0:
                    if visited[u]:
                        continue
                    visited[u] = True
                    disc[u] = low[u] = time_stamp
                    time_stamp += 1
                    new_children = []
                    back_edges = []
                    for (v, i) in adj[u]:
                        if v == parent:
                            continue
                        if not visited[v]:
                            new_children.append((v, i))
                        else:
                            if disc[v] < disc[u]:
                                back_edges.append((v, i))
                    for (v, i) in back_edges:
                        edge_stack.append(i)
                        low[u] = min(low[u], disc[v])
                    stack.append((u, parent, new_children, 1))
                    for idx in reversed(range(len(new_children))):
                        v, i = new_children[idx]
                        edge_stack.append(i)
                        tree_edge_stack.append(i)
                        stack.append((v, u, [], 0))
                else:
                    for (v, i) in children:
                        low[u] = min(low[u], low[v])
                    if parent != -1 and low[u] >= disc[parent]:
                        component = []
                        while True:
                            j = edge_stack.pop()
                            component.append(j)
                            if j == tree_edge_stack[-1]:
                                break
                        tree_edge_stack.pop()
                        components.append(component)
    if edge_stack:
        components.append(edge_stack.copy())
        edge_stack.clear()

    answer = set()
    for comp in components:
        edge_indices = comp
        vertices = set()
        for idx in edge_indices:
            u, v = edges[idx - 1]
            vertices.add(u)
            vertices.add(v)
        V = len(vertices)
        E = len(edge_indices)
        if V == E:
            answer.update(edge_indices)
    
    sorted_ans = sorted(answer)
    print(len(sorted_ans))
    if sorted_ans:
        print(' '.join(map(str, sorted_ans)))
    else:
        print()

if __name__ == "__main__":
    main()
```