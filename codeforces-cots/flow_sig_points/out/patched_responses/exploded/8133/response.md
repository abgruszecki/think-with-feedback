<think>
Okay, let's try to figure out how to solve this problem. The problem is about a directed graph where every pair of distinct cities has a single directed edge between them. Also, there's a restriction that there are no four cities forming a certain configuration (like a forbidden subgraph), but the main task is to compute the sum of all-pairs shortest path distances, with a penalty of 614n if the path doesn't exist.

First, let's understand the input. The graph is given as a binary matrix, but stored in a compressed hexadecimal format. Each row is represented by n/4 hex digits, each of which converts to 4 bits. For example, a hex digit 'B' is 1011 in binary. So each row's entries are 4 bits each, concatenated to form the entire row of the adjacency matrix. We need to parse this correctly.

The main challenge is computing the all-pairs shortest paths efficiently. Given that n can be up to 8000, a standard Floyd-Warshall approach (O(n^3)) is definitely out of the question. That's way too slow for n=8000. So we need a smarter approach.

Wait, but the graph structure has some specific properties due to the problem's constraints. The restriction that there are no four cities forming a certain configuration probably implies some structure in the graph. Maybe the graph has a particular hierarchy or arrangement that allows us to compute distances more efficiently.

Let me think about the forbidden configuration. The forbidden subgraph involves four cities A, B, C, D such that there's a cycle of some sort. The exact configuration isn't given, but perhaps this implies that the graph is a tournament (since every pair has a directed edge) and that it's a transitive tournament. Wait, no. Transitive tournaments have a linear ordering where all edges go from earlier to later in the order. But in that case, the forbidden 4-node configuration would not exist. Maybe the graph is a transitive tournament?

Alternatively, maybe the graph is a DAG, but since every pair has an edge, it's a tournament. But tournaments can have cycles. However, in a transitive tournament (a total order), there are no cycles. So perhaps the restriction ensures that the graph is a transitive tournament. But how?

Wait, the problem says that there are no four distinct cities A, B, C, D such that a certain configuration exists. The example in the note shows a graph where some distances are 1, others are 2, and some are 614n. But in the first example, the graph isn't a transitive tournament. For example, in the first example's matrix, the adjacency matrix is:

Row 0: 0 1 1 1
Row 1: 0 0 1 0
Row 2: 0 0 0 1
Row 3: 0 1 0 0

So city 0 has edges to 1, 2, 3. City 1 has an edge to 2. City 2 has edge to 3. City 3 has edge to 1. So there's a cycle between 1,3,2. So the graph isn't transitive, but it's allowed except for some forbidden 4-node subgraphs.

Hmm. So maybe the graph's structure is such that it's a "chain" of components where each component is a strongly connected component (SCC) arranged in a linear order. And between components, all edges go from earlier components to later ones. This structure would form a DAG of SCCs. Then, within each SCC, it's a strongly connected tournament (so each pair of nodes in the component have a path between them in both directions, but since it's a tournament, perhaps each node has a path to every other within the component). If the SCCs are arranged in a linear order, then between any two nodes in different components, the distance is 1 if they are in a lower component (since all edges are from earlier to later components). But how would the forbidden subgraph affect this structure?

Alternatively, maybe the graph is such that it's a DAG with a linear order, but that's a transitive tournament. But in the first example, that's not the case. So perhaps the forbidden configuration's absence enforces that the graph's SCCs form a chain, and each SCC is a strongly connected tournament. Wait, but in that case, the entire graph would consist of a sequence of SCCs where between SCCs, all edges go from the earlier ones to the later ones. Then, for any two nodes in different SCCs, the path is straightforward. And within an SCC, the distance between any two nodes is at most 2. Because tournaments have the property that in any strongly connected tournament, the distance between any two nodes is at most 2. Wait, is that true?

Let me think. Suppose we have a strongly connected tournament. For any two nodes u and v, either there's a direct edge u→v, or there's a node w where u→w and w→v. Because if there's no edge u→v, then the edge is v→u. But since the tournament is strongly connected, there must be a path from u to v. The minimum path length is 2. So yes, in a strongly connected tournament, the distance between any two nodes is 1 or 2. So if the entire graph is a collection of strongly connected tournaments (SCCs) arranged in a linear order (DAG), then the distance between two nodes in the same SCC is 1 or 2, and between nodes in different SCCs, the distance is 1 if the source is in an earlier component and the destination is in a later component, and 614n otherwise (since there's no path in the reverse direction).

So the problem's structure is that the graph is a DAG of SCCs, each of which is a strongly connected tournament. The forbidden configuration's absence ensures that the graph can be decomposed into such a structure. So the problem reduces to:

1. Decomposing the graph into SCCs.
2. Ordering the SCCs in topological order (since the DAG is a chain).
3. For each pair of nodes, compute the distance based on their positions in the topological order and their SCC membership.

But how to compute this efficiently?

First, the SCC decomposition. Since the graph is a tournament, the SCC decomposition has a certain property. For tournaments, the SCCs form a linear order. That is, if you decompose the graph into SCCs S1, S2, ..., Sk, then all edges between Si and Sj for i < j are directed from Si to Sj. So the DAG of SCCs is a linear chain. Because in a tournament, if there are two nodes u and v in different SCCs, then the edge between them must go from the component that comes first in the topological order to the later one. Because tournaments can't have edges both ways between two components.

So once we find the SCCs, the topological order is unique. So the plan is:

- Find the SCCs in topological order.
- For each node, determine which SCC it belongs to, and the order of the SCC in the topological order.

Then, for any two nodes A and B:

- If A and B are in the same SCC:
   - If there's a direct edge A→B, distance is 1.
   - Else, the distance is 2 (since the tournament is strongly connected, so there's a node C in the same SCC where A→C and C→B).
- If A's SCC is before B's SCC in the topological order:
   - The distance is 1, because all edges from A's SCC to B's are present, so there's a direct edge.
- If A's SCC is after B's SCC in the topological order:
   - The distance is 614n, since there's no path (since the DAG of SCCs is a linear order, so there's no path from a later component to an earlier one).

Wait, but why can't there be a path through other components? For example, if the DAG is S1 → S2 → S3, then a node in S3 can't reach S1 even through S2. Because the edges between S3 and S2 are from S2 to S3. So any path from S3 to S2 would require an edge from S3 to S2, which isn't there because the SCCs are ordered. So in this case, if A is in a later component than B, there's no path, hence the distance is 614n.

So the algorithm for distance is:

distance(A,B) = 
   if A and B are in the same SCC:
       1 if there's an edge A→B, else 2
   else if A's SCC comes before B's SCC in topological order:
       1
   else:
       614 * n

So the problem reduces to:

1. Compute SCCs of the graph, ordered topologically.
2. For each node, determine its SCC and the topological order position of the SCC.
3. For each ordered pair (A,B):
   a. If A == B: skip.
   b. Else compute the distance as per above and sum.

Now, the key steps are:

- How to compute SCCs of a tournament. Because the graph is a tournament, the SCCs can be found using a specific approach. For tournaments, the strongly connected components can be found in linear time. In a tournament, the condensation (the DAG of SCCs) is a linear order. So once you have the SCCs, their order is unique.

But how to find the SCCs efficiently for a large graph (n=8000)? The standard Kosaraju's algorithm or Tarjan's algorithm can take O(n^2) time, which for n=8000 would be 64 million operations. That might be manageable, but given that the adjacency matrix is stored in a compressed format, perhaps there's a smarter way.

Wait, but the adjacency matrix is given in a way that each row is a binary string. So for each node A, we can check which nodes have an edge from A. But for Tarjan's algorithm, which is O(V + E), since E is O(n^2), for n=8e3, it's 64 million edges. That's way too slow.

But since the graph is a tournament, there's a property that can help. The SCCs form a chain. So perhaps there's a way to find the components in O(n) time.

Yes! For tournaments, there's an algorithm to find the SCCs in linear time. Here's how it works:

The algorithm for finding SCCs in a tournament (from Wikipedia):

The strongly connected components of a tournament are its strongly connected subtournaments. These form a sequence in which each component has edges directed to all later components. Thus, the condensation of a tournament is itself a transitive tournament, and in particular is a linear order. That is, the strong components of a tournament may be ordered in a sequence such that, for all i < j, there is an edge from every vertex of the i-th component to every vertex of the j-th component.

So the SCCs form a linear order. To find this order, we can use the following approach:

1. Initialize the first SCC as the first node.
2. For each subsequent node u:
   a. Compare u with the current last SCC in the order. Let v be any node in that SCC.
   b. If there is an edge from u to v, then u cannot be in the same SCC as v. So we check all previous SCCs until we find where u fits. Alternatively, since the SCCs are in a linear order, perhaps inserting u into the correct position can be done efficiently.

Wait, maybe another approach. Since the condensation is a linear order, the SCCs can be ordered such that for any two components S and T, all edges between them go from S to T if S comes before T. So the algorithm can be:

Start with the first node as S1. Then, for each subsequent node u, compare with the last component in the current list. For the last component S_k, check if there is a node v in S_k such that the edge between u and v is u→v. If there is such a node, then u must form a new component after S_k. Otherwise, u is part of S_k. Wait, not sure.

Alternatively, here's a method from the paper "Finding the Strongly Connected Components in a Directed Graph" by D. B. Johnson, which mentions that for tournaments, the strong components can be found in linear time.

Another approach: Since the condensation is a linear order, each component can be processed in order. For each node, the component it belongs to is determined by the earliest component where all nodes in that component have edges pointing to the node. Or something like that.

Alternatively, here's an approach that works for tournaments:

The components are ordered such that component S1 comes before S2, which comes before S3, etc. For each component S_i, all nodes in S_i have edges directed towards all nodes in S_j for j > i. Within each S_i, the tournament is strongly connected.

To find the components, we can process nodes in reverse order and maintain the components. Let me look for a linear time algorithm.

Wait, according to some references, the SCCs of a tournament can be found in linear time using the following approach:

Initialize a list of components. For each node in reverse order, check if it has edges to all existing components. If it does, then it forms a new component at the beginning. Otherwise, merge it into the first component it has an incoming edge from.

Wait, perhaps this is the correct approach. Let me think. Suppose we process the nodes in reverse order (from last to first). For each node u, we check against the current first component in the list. Let's take any node v in the first component. If there's an edge from v to u, then u must form a new component that comes before the first component. But since the components are ordered in a linear way, perhaps inserting components in reverse order.

Alternatively, here's a method from a competitive programming resource: 

In a tournament, the strongly connected components can be found by starting with a list of components. For each node, find the rightmost component that the node has an edge to, then merge all components from that point to the end into one component. This is O(n) time.

Let me see. For example, suppose we process each node in some order (like 0 to n-1). For each node u, we check the existing components. The node u will have edges to all components to the right of a certain position. So the components can be maintained in a list. For each new node u, find the leftmost component in the list such that u has an edge to a node in that component. Then, all components to the left of that component must have edges from u to them. The components to the left of that point are merged with u into a new component. Wait, perhaps not. Maybe the algorithm is as follows:

Initialize the list of components as empty.

For each node u in order 0 to n-1:

   Find the first component C in the list where u has an edge to some node in C.

   Split the list into two parts: the components before that C (including C), and the components after.

   Merge all the components up to and including C, and add u to create a new component. The new list is this merged component followed by the components after C.

   If u has no edges to any existing components, then create a new component at the end of the list.

Wait, perhaps not. Alternatively, for each node u, find the earliest component in the list that u has an edge to. Then, all components before that component must have edges from u to their nodes, and the component itself must have at least one node to which u has an edge. Then, the new component is formed by merging all components up to that point plus u, and the rest of the components stay. This way, the components are ordered such that all edges from the new component to the remaining components are present.

This approach would process each node once, and for each node, find the leftmost component where u has an edge to a node in it. Then, merge all components up to and including that one, and add u to form a new component. The time per node is O(1) if the components are maintained in a way that allows this.

But how to find the leftmost component where u has an edge to any node in it?

For each existing component in the list, we can check if u has an edge to the first node of the component. Because if there's any node in the component that u has an edge to, then since the component is a strongly connected tournament, there's a path from u to all nodes in that component. Wait, perhaps not. Wait, the component is a strongly connected tournament. So if u has an edge to any node in the component, then u can reach all nodes in that component through that node. So for the purposes of determining whether u can reach the entire component, it's sufficient to check if u has an edge to any node in the component.

But how to do this efficiently. For each component, we can track one representative node. When checking if u has an edge to that component, we can check if u has an edge to the representative.

Thus, the algorithm can be:

Initialize components as an empty list.

For each node u in order 0 to n-1:

   low = 0, high = len(components)

   while low < high:

       mid = (low + high) // 2

       if u has an edge to the representative of components[mid]:

           high = mid

       else:

           low = mid + 1

   So after the loop, low is the first index where u has an edge to the representative. So all components before low have edges from u to their representatives. Wait, no. Wait, during the binary search, we're looking for the first component where the representative has an edge from u. So if u has an edge to the mid component's representative, then we set high=mid. Else, we set low=mid+1. So after the loop, low is the first index where the representative is reachable from u.

   All components with index < low have edges from u to their representatives (so u can reach all nodes in those components via the representative). The component at index low (if any) is the first one where u has an edge to the representative.

   Then, the new component is formed by merging all components up to index low (exclusive?), and including u. Wait, I think I'm getting confused here. Let's see an example.

Suppose components are ordered as C1, C2, C3, ..., Ck. Each Ci is a strongly connected component, and all edges go from Ci to Cj when i < j.

When processing u, we want to find the first component Ci where u has an edge to Ci's representative. Then, u can reach all nodes in Ci and all later components. Because Ci is after the previous components, but if u has an edge to Ci, then since Ci's component is a strongly connected tournament, all nodes in Ci can reach each other, and u can reach all nodes in Ci. Then, the components from 0 to i-1 must have edges from u to them (since u can reach them, but how?), but that's not necessarily the case.

Wait, no. Let's say u has edges to some components and not others. For example, if the existing components are [C0, C1, C2], and when processing u, the binary search finds that u has an edge to C1's representative. Then, that implies that u has edges to C0's representative as well? Because if the components are in the order C0, C1, C2, then in the tournament, any edge between Ci and Cj (i < j) must be from Ci to Cj. So if u has an edge to C1's representative, then since C0 is before C1, C0's edges to C1's are all edges from C0 to C1. So u has an edge to C1's representative, but u's edges to C0's representative would depend on how u is positioned. Wait, perhaps not.

Alternatively, since the existing components are ordered in such a way that all edges between components go from earlier to later. So for any component Ci and Cj where i < j, all edges from Ci to Cj.

But when processing u, which is a new node, how does it fit into this structure?

The algorithm for building the component list is such that after processing u, the list of components maintains the property that all edges between components go from earlier to later. So for u, we need to find the correct position where u can be merged into the existing components.

The approach is to find the first component in the current list where u has an edge to that component. All components before that component must have edges to u. So u can be merged with those components and the component itself into a new component. Because:

If u has an edge to component C_i's representative, then since C_i is part of the existing list, and u can reach C_i, but the existing components before C_i have edges to C_i. So if u has edges to C_i, but the components before C_i have edges to u, then those components and u and C_i form a strongly connected component. Wait, perhaps not. Let me think again.

This is getting a bit complicated. Let me look up the standard algorithm for finding SCCs in tournaments.

Upon checking, I find that the algorithm for finding the SCCs in a tournament is as follows:

The algorithm processes the nodes in reverse order (from n-1 to 0). For each node u, it checks the existing components. The components are maintained in a list. For each component in the list, check if there's an edge from the component's representative to u. If there is, then u can't be part of that component or any earlier components (since those components would also have edges to u). If there is no such edge, then u must be added to a new component at the front of the list. However, if there exists a component in the list where the edge is from u to the component's representative, then u and that component (and possibly others) form a new component.

Wait, perhaps the correct approach is to process nodes in reverse order and maintain the list of components in topological order (earlier components come first in the list). For each node u, find the first component in the list where u has an edge to the component's representative. Then, merge all components up to and including that component, and add u to form a new component. This merged component becomes the first component in the list, and the remaining components follow.

This way, the algorithm processes each node in O(1) amortized time.

But how does this work? Let's think of an example.

Suppose we have nodes A, B, C, D.

Processing in reverse order D, C, B, A.

Initially, components is empty.

Process D: components is empty. Create a new component with D. components = [D].

Process C: Check if there's an edge from D to C. If yes (D→C), then C must form a new component after D. So components = [D, C]. But wait, in the algorithm, if the component's representative (D) has an edge to C, then C is added as a new component. But in the case of tournaments, the edge between D and C must be in one direction. So if D→C, then C can't reach D, so D and C are in different components. But since the algorithm is processing in reverse order, perhaps the components are built in such a way that the topological order is maintained.

Alternatively, perhaps the algorithm for building the components is as follows:

Initialize an empty list of components. For each node u in reverse order (from last to first):

   Create a new component for u.

   While the component list has at least one component, and the representative of the first component in the list has an edge to u:

       Merge the first component into u's component.

   Add the merged component to the front of the list.

This way, the algorithm merges components when the existing components have edges to u, which would imply that u is part of a component that comes before those components. Since we are processing in reverse order, perhaps this ensures that the components are ordered correctly.

Wait, this makes sense. Let's see:

Suppose we process nodes in reverse order. For each u, we create a new component. Then, check if the first component in the list (if any) has a representative that has an edge to u. If yes, then u must be part of a component that comes after that component (since in the topological order, edges go from earlier to later). But since the list is built in reverse order, the first component in the list is the last in topological order. Hmm, this is getting a bit confusing.

Alternatively, when merging the first component into u's component, it's because the first component's representative has an edge to u. Since the component list is being built in reverse order, this means that the existing component comes after u in the topological order. But merging them into u's component would create a new component that is placed before the remaining components.

Wait, perhaps not. Let's take an example.

Suppose the actual topological order of SCCs is S1, S2, S3. So edges go from S1 to S2, S1 to S3, S2 to S3.

Processing nodes in reverse order (assuming the nodes in S3 are processed first, then S2, then S1). Let's say S3 has node D, S2 has C, and S1 has A and B.

Processing D: create component [D]. The list is [D].

Processing C: check if D has an edge to C. If yes, then merge D into C's component. So now component [C, D]. But in reality, S2 and S3 are separate components, so edges from S2 to S3. So in this case, C (S2) would have edges to D (S3), which would mean that when processing C (after D), the component D's representative (D) has an edge to C. So during processing C, the existing component is [D]. The edge is from D to C, which is S3 → S2. But in reality, edges should be from S2 to S3. So this suggests that this approach may not work. Hmm.

Alternatively, perhaps the algorithm works by building the component list in reverse topological order. Then, after processing all nodes, the list is reversed to get the correct topological order.

Alternatively, perhaps the algorithm for tournaments is to process nodes in order and build the components as follows:

Initialize components as an empty list.

For each node u in order from 0 to n-1:

   Create a new component containing u.

   While the last component in the list (call it C) has a node v such that u → v:

       Merge C into u's component.

       Remove C from the list.

   Add the new component (possibly merged with previous ones) to the end of the list.

This way, whenever u can reach the entire last component (since u has edges to all nodes in it), those components are merged into u's component. Because if u has an edge to the last component's node, then since the last component is a strongly connected tournament, all edges between its nodes are present, and thus u can reach all nodes in that component. Hence, the component can be merged with u's component.

This approach would form the components in such a way that the condensation is a linear order.

Let's test this with the first example's adjacency matrix:

The adjacency matrix for the first example (4 cities) is:

Row 0: 0 1 1 1 → edges from 0 to 1,2,3.

Row 1: 0 0 1 0 → edges from 1 to 2,0; edges from 0 to 1.

Wait, no. Wait, the matrix is such that the j-th entry of the i-th row is 1 if there is a road from i to j. So for row 0 (i=0), the entries are 0,1,1,1. So node 0 has edges to 1,2,3.

Row 1: entries are 0,0,1,0. So node 1 has edges to 2. But what about other nodes? For j=0, the entry is 0 → so the road is from 0 to 1.

So the edges are:

0→1, 0→2, 0→3.

1→2, 1→0 (since the edge from 1 to 0 is present if row 1's j=0 is 0? Wait, no. Wait, the adjacency matrix is such that M[i][j] = 1 if the road is from i to j.

So row 1 (i=1) has entries [0,0,1,0], so for j=0, M[1][0] is 0 → no edge from 1 to 0. So the edge from 1 to 0 is not present. Wait, but how does that work with the tournament property? Because the problem states that for any two distinct cities A and B, exactly one road exists between them. So for A and B, either A→B or B→A. So in row i=1, for j=0, M[1][0] is 0 → edge is from 0 to 1 (since M[i][j] is 0, which would imply that the edge is from j to i? Wait, no. Wait, the problem says:

"the j-th character of the i-th row is 1 if the one-directional road between cities i and j is directed from i to j, and 0 otherwise."

So for i=1 and j=0: M[1][0] is 0 → the road is from 0 to 1 (since 0 is not 1, and the road is directed from the other node). Wait, no. Wait, M[i][j] is 1 if the road is from i to j. So if M[i][j] is 0, then the road is from j to i. Because for any two distinct i and j, exactly one of M[i][j] or M[j][i] is 1.

So for example, in the first row (i=0) j=1: M[0][1] is 1 → edge 0→1. For i=1 and j=0: M[1][0] is 0 → the edge is from 0 to 1. So for this pair, the edge is 0→1.

So in the first example, the adjacency matrix is:

Row 0: 0 1 1 1 → edges from 0 to 1, 2, 3.

Row 1: 0 0 1 0 → edges from 1 to 2. Other edges (0 and 3) are from other nodes to 1.

So the edges are:

0→1, 0→2, 0→3.

1→2.

For node 2, row 2 is 0 0 0 1 → edges from 2 to 3.

For node 3, row 3 is 0 1 0 0 → edge from 3 to 1.

So the edges are:

0→1, 0→2, 0→3.

1→2.

2→3.

3→1.

So the graph has the following cycles:

1 → 2 → 3 → 1. So these three nodes form a strongly connected component. Node 0 has edges to all of them, but since the edges are one-way from 0 to them, they cannot reach back to 0. So the SCCs are [0], [1,2,3]. The topological order is [0], then [1,2,3].

So when processing nodes in order 0,1,2,3:

Processing 0:

Create component [0]. List is [ [0] ].

Processing 1:

Create component [1]. Check if the last component [0] has edges from 1 to 0. The edge is from 0 to 1. So M[1][0] is 0 → edge from 0 to 1. So the edge from 1 to 0 is not present. So the edge from 1 to 0 is not there. So in the component [0], the edge from 1 to 0 is not present. So the algorithm would not merge. So add [1] to the list. Now list is [ [0], [1] ].

Processing 2:

Create component [2]. Check the last component [1]. Check if 2 has an edge to 1. The edge is 1→2 (since M[1][2] is 1). So M[2][1] is 0 → edge from 1 to 2. So 2 does not have an edge to 1. So no merge. Add [2] to the list. Now list is [ [0], [1], [2] ].

Processing 3:

Create component [3]. Check last component [2]. Check if 3 has an edge to 2. M[3][2] is 0 → edge from 2 to 3. So the edge from 3 to 2 is not present. So no merge. Add [3] to the list. Now list is [ [0], [1], [2], [3] ].

But this is incorrect. Because the actual SCCs are [0], [1,2,3]. So the algorithm as described is not working.

Hmm. So perhaps this approach is not correct. Then, what is the correct way to find the SCCs for a tournament?

Alternative idea: The algorithm must be such that when processing a node u, if there's any existing component C where u has an edge to any node in C, then u can reach all nodes in C and merge with C. But how to do that efficiently.

Another approach: Since the SCCs form a linear order, we can use a greedy approach. Start by finding a node that can reach all other nodes. Then, decompose the graph into its SCCs.

But I'm not sure.

Alternatively, for each node u, the component of u is the set of nodes that can be reached from u and can reach u. For a tournament, the SCCs form a linear order. So perhaps the component of u is determined by the earliest node in the topological order that u can reach, and the latest node that can reach u.

Alternatively, perhaps the algorithm is as follows:

Find the node with the maximum out-degree. This node will be in the first component of the topological order. Then, all nodes that can reach this node form the first component. Then, proceed recursively.

But this might not be efficient.

Alternatively, considering that the components form a linear order, each component can be characterized by the minimal node in it. But again, not sure.

At this point, perhaps the best approach is to implement Tarjan's algorithm for finding SCCs, but optimize it as much as possible. However, with n=8000, the adjacency matrix storage would be O(n^2) = 64 million entries, which is about 8 MB (if stored as bits). Wait, 8000x8000 is 64 million bits, which is 8MB. So storing this as a bitmask per row is feasible. Then, Tarjan's algorithm can be implemented with adjacency lists built on the fly.

Wait, but Tarjan's algorithm is O(V + E) = O(n^2) for this case. For n=8000, that's 64 million operations. Python can handle this in under 2 seconds? Not sure. Let's see: 64 million operations in Python. Each iteration of a loop is about 0.1 nanoseconds (approximate). Wait, no. Python is slower. For example, a loop that runs 1 million times in Python can take around 0.1 seconds. So 64 million operations would take around 6.4 seconds, which is over the time limit. So Tarjan's algorithm is not feasible here.

Therefore, we need a smarter way to find the SCCs for a tournament.

Upon further research, I find that in a tournament, the strongly connected components can be found using a process similar to the following:

1. Start with an empty list of components.

2. For each node u in the order from 0 to n-1:

   a. Create a new component containing u.

   b. Iterate through the existing components in reverse order. For each component C:

       i. Check if there exists a node v in C such that u has an edge to v.

       ii. If yes, then merge all components from C onwards into u's component. Break.

   c. Insert the merged component (if any) into the list in the position where the merging started.

This way, components are merged when a new node can reach an existing component. Since the components are processed in reverse order, the merging ensures that the components are ordered correctly.

But how to implement this efficiently?

Let's think about the example again. For the first example, processing node 0:

- Component list is empty. Create [0].

Processing node 1:

- Create [1]. Check existing components (just [0]). Check if 1 has an edge to 0. The edge is from 0 to 1 (M[0][1] =1). So no, 1 does not have an edge to 0. So no merging. Add [1] to the list. Now list is [ [0], [1] ].

Processing node 2:

- Create [2]. Check existing components in reverse order: [1], then [0].

   For component [1], check if 2 has an edge to any node in it. Since component [1] has node 1. M[2][1] is 0 → edge is from 1 to 2. So 2 does not have an edge to 1. So move to next component [0]. M[2][0] is 0 → edge from 0 to 2. So no. So add [2] to the list. Now list is [ [0], [1], [2] ].

Processing node 3:

- Create [3]. Check components in reverse order: [2], [1], [0].

   For component [2], check if 3 has an edge to any node in it (node 2). M[3][2] is 0 → edge is from 2 to 3. So no.

   Next component [1]. Check M[3][1] is 1 → edge from 3 to 1. So yes. So merge components [1], [2], and [3] into a new component [3,1,2]. Then, insert this new component after [0]. So the list becomes [ [0], [3,1,2] ].

Wait, but why [1] and [2] are merged? Because when merging component [1], which is followed by [2], since the component list is [0], [1], [2], and when merging [1], the algorithm merges all components from [1] onwards. So merging [1], [2], and the new node 3 into one component.

But in reality, the component is [1,2,3], which is strongly connected. So this approach works.

But how to efficiently check if the new node has an edge to any node in a component? For each component, we can keep a representative node. For example, the first node in the component. So when checking if the new node has an edge to any node in the component, we can just check the representative.

But in reality, if there's any node in the component that the new node has an edge to, then the new node can reach all nodes in the component. Because the component is a strongly connected tournament. So if u has an edge to any node in the component, then u can reach all nodes in that component (since there's a path through that node to others). Therefore, checking the representative is sufficient.

Thus, for each component, we can track a representative node. When processing a new node u, for each existing component in reverse order (starting from the end of the list), check if u has an edge to the component's representative. If yes, then merge all components from that point onwards into a new component with u, and add this merged component to the list.

Wait, but merging from that point onwards implies that u can reach all those components. But since the components are ordered such that edges go from earlier to later, then merging them into a new component that comes before the earlier components would maintain the topological order.

This seems plausible.

So the algorithm can be:

components = list of components, each with a representative node.

For each node u in order 0 to n-1:

   new_component = [u]

   # Iterate over existing components in reverse order (from last to first)
   # Find the leftmost component where u has an edge to its representative.
   # All components to the right of this component are merged with u.
   # We need to find the first component (in reverse order) where u has an edge to the representative.
   # Once found, merge all components from that position onwards into new_component.

   merged = False

   for i in reversed(range(len(components))):
       c_rep = components[i].rep
       if adj[u][c_rep] == 1:  # u has an edge to c_rep
           # merge all components from i to end
           new_component = [u] + [node for c in components[i:] for node in c.nodes]
           components = components[:i] + [new_component]
           merged = True
           break

   if not merged:
       components.append(new_component)

   Wait, no. Because the components are processed in reverse order. So for example, if the current components are [C0, C1, C2], and during processing u, we find that u has an edge to C1's representative, then we merge C1, C2, and u into a new component. The new components list becomes [C0, new_component]. This maintains the topological order.

But how to track the representative for each component? The representative can be the first node in the component (since components are processed in order, and merging happens when u can reach their representatives).

Thus, for each component, we store a list of nodes and the representative (first node).

So during processing u, we check each component in reverse order. For each component, check if u has an edge to its representative. If yes, merge all components from that point to the end of the list (since in reverse order, these are the components that come after the current component in the list) and create a new component. Then, replace those components with the new component.

Wait, no. Because in the list, components are ordered from first to last. When processing in reversed order, the first component in reversed order is the last component in the list.

Hmm. Perhaps the correct approach is to iterate through the components in reverse order (from the last one backward to the first), and find the first component where u has an edge to its representative. Then, merge all components from that index to the end (inclusive) with u into a new component, and replace those components with the new component.

For example, components are [C0, C1, C2, C3]. Processing u:

Check C3's representative. If u has edge to C3's rep → merge C3 and u into a new component.

Check C2's representative. If u has edge → merge C2, C3, u.

But this seems conflicting. Oh, no. The idea is that once you find the first component in reverse order that u has an edge to, then all components after that (in original order) are merged with u. Because those components are in the list after the current component. So for example, if the list is [C0, C1, C2], and during processing u, we find that u has an edge to C1's rep (i=1 in reversed order would be index 1 in original list), then the merged components would be C1 and C2, along with u. So the new components list becomes [C0, new_component].

But how to find the earliest component in reverse order where u has an edge to its rep.

Let's think with the first example:

Processing node 3.

Components are [C0 (0), C1 (1), C2 (2)].

Iterate in reversed order (C2, C1, C0).

Check C2's rep is 2. Edge from 3 to 2? M[3][2] is 0 → no. So no.

Check C1's rep is 1. Edge from 3 to 1? M[3][1] is 1 → yes. So merge components C1 and C2, and add 3. New component is [3,1,2]. So the components list becomes [C0, new_component].

Which is correct.

So this algorithm seems to work.

Thus, the steps are:

- For each node u in order 0 to n-1:

   - Iterate through existing components in reverse order (from last to first).

   - For each component, check if u has an edge to its representative.

   - The first component where this is true is found. Merge all components from that index to the end of the list, along with u, into a new component. Replace those components with the new component.

   - If none are found, add u as a new component at the end.

The key is that merging the components from the found index onwards (inclusive) into a new component with u.

Now, the representative for the new component is u.

Once all nodes are processed, the components list is ordered according to the topological order of the SCCs. Each component is an SCC.

Now, the algorithm's time complexity is O(n^2), which for n=8000 is 64 million operations. But since each iteration involves checking the representatives of existing components in reverse order, the actual number of checks per node is O(k), where k is the number of components at that point. But in the worst case, each new node can trigger a linear scan through the existing components. For example, in the case of a linear tournament, each new node would merge all existing components.

But in practice, for a linear tournament, each new node would merge all existing components. Thus, for n=8000, the total number of operations would be O(n^2), which is 64 million. Python can handle this in under 2 seconds? Probably not. 64 million operations in Python are way too slow. So we need a more efficient way to find the first component in reverse order where u has an edge to the representative.

Ah, but binary search can be used here. Because the components are ordered such that any component after a certain point must have edges from u to them. Wait, no. Because the components are ordered in the list such that edges go from earlier components to later components. So for a new node u, the components in the list are ordered from first to last. For u, the edge to a component's representative can be 1 or 0. But if we can arrange to find the first component (in reverse order) where u has an edge to the representative, we can use binary search to find this component.

Wait, how? Let's see.

The list of components is ordered such that edges go from earlier components to later components. For a new node u, the edges to the components' representatives can have a pattern. For example, u may have edges to some components and not others. But since the components are in topological order, the edges from u to the components' representatives form a pattern where there's a certain point where u starts to have edges. So we can binary search for the earliest component (in reverse order) where u has an edge to its representative.

For example, the edges from u to the components' representatives could be a sequence like 0 0 0 1 1 1. Once we find the first 1 in reverse order, all components after that point (in the list) will have edges from u to their representatives.

Thus, binary search can be used to find the first component in reverse order where u has an edge to its representative. This reduces the per-node processing time from O(k) to O(log k).

For n=8000, this would be O(n log n) operations, which is manageable.

So the algorithm becomes:

For each node u in order 0 to n-1:

   low = 0, high = len(components)

   while low < high:

       mid = (low + high) // 2

       # Since we are checking in reverse order, mid is the index starting from the end.

       # Wait, no. The components are ordered from first to last. To check in reverse order, we need to check from last to first.

       # So the first component to check in reverse order is the last component in the list (index len(components)-1).

       # So binary search is performed over the indices in reverse order.

       # So we need to find the leftmost index (in reverse order) where u has an edge to the component's representative.

       # To implement binary search over the reversed list, we can map the indices.

       # Let's think of the list as being reversed. For the binary search, we can map the mid index to the reversed components.

       # For example, the reversed list is components[::-1]. The mid-th element in this list is components[len(components)-1 - mid].

       # So during binary search, we are looking for the first occurrence where u has an edge to the component's representative in the reversed list.

       # Thus, the binary search is performed over the range [0, len(components)) in the reversed list.

       # The binary search will find the smallest index in the reversed list where u has an edge to the component's representative.

       # Once found, the index in the original list is len(components)-1 - idx.

       # For example, if the reversed list is [C3, C2, C1, C0], and the found idx is 1 (C2), then in the original list it's index 2.

   Thus, the binary search is performed as follows:

   reversed_components = components[::-1]

   left = 0

   right = len(reversed_components)

   while left < right:

       mid = (left + right) // 2

       c_rep = reversed_components[mid].rep

       if adj[u][c_rep] == 1:

           right = mid

       else:

           left = mid + 1

   # After the loop, left is the first index in reversed_components where u has an edge to the component's representative.

   # If left is 0, then no such component exists.

   # The corresponding index in the original components list is len(components) - 1 - left.

   # If left is len(components), then no component found.

   # Otherwise, the component is at index len(components) - 1 - left.

   if left < len(reversed_components):

       merge_idx = len(components) - 1 - left

       # merge all components from merge_idx to end of the list.

       new_component_nodes = [u]

       for c in components[merge_idx:]:

           new_component_nodes.extend(c.nodes)

       new_component = Component(new_component_nodes, u)

       components = components[:merge_idx] + [new_component]

   else:

       components.append(Component([u], u))

This way, each node u is processed in O(log k) time, where k is the number of components at that point. For n=8000, this would be O(n log n) operations, which is acceptable for Python.

But to implement this, we need to represent each component with its nodes and representative.

So the components are stored as a list of objects, each containing the list of nodes in the component and the representative.

But in Python, using lists for each component's nodes and the representative is manageable.

Now, the problem is to read the adjacency matrix correctly.

The input is given in a compressed format. Each row is given as n/4 hexadecimal digits, each representing 4 bits. For example, the first example's input for n=4 has 4 rows, each with 1 hex digit (since n/4 = 1). The first row is '7', which is 0111 in binary. But the matrix is supposed to represent a directed graph where M[i][j] is 1 if there is an edge from i to j. So the first row is 0 1 1 1. Wait, the hex digits are converted to binary, but each hex digit represents four bits. For example, the hex digit '7' is 0111 in 4 bits. So for a row in the input, each hex digit is converted to 4 bits, and the bits are concatenated to form the entire row.

But how are the bits ordered? For example, '7' is 0x7, which is 0111 in binary. So each hex digit is padded to four bits, with leading zeros if necessary. So the first hex digit in a row represents the first four bits of the row. For example, if a row is 'A' (1010), then the first four bits are 1010. For n=4, this is four bits, so the entire row is 1010.

So the process is:

For each row i:

   Read the hex digits for the row, split into groups of 4 bits.

   For each hex digit, convert to 4 bits, then concatenate all bits to form the row's binary string.

   Then, for each j in 0..n-1:

       M[i][j] = binary_str[j]

But wait, the order of the bits? For example, hex 'B' is 1011, which is bits 8+0+2+1=11. So the first bit is the MSB (most significant bit). So when converting hex to binary, each digit is represented as four bits, MSB first. For example, 'B' is 11 in decimal, which is 1011 in binary. So the four bits are 1,0,1,1.

So for a row like 'B', the first four columns (j=0,1,2,3) of row i would have M[i][0] = 1, M[i][1] = 0, M[i][2] = 1, M[i][3] = 1.

Thus, for row i, the hex digits are converted into a binary string of length n bits, padded with leading zeros if necessary. Each hex digit represents four bits, MSB first. For example, for n=8, a row with two hex digits '7F' would be 01111111, which is the binary representation of 0x7F.

So the code to read the adjacency matrix is:

n = int(input())

adj = [[] for _ in range(n)]

for i in range(n):

   hex_row = input().strip()

   bin_str = ''.join(f"{int(c, 16):04b}" for c in hex_row)

   # bin_str is a string of 0s and 1s, length n

   # for each j in 0..n-1, adj[i][j] is bin_str[j]

   # but since it's a binary string, we can represent it as a list of integers.

   # for each j in 0 to n-1:

   for j in range(n):

       adj[i][j] = bin_str[j] == '1'

But for n=8000, storing a 8000x8000 matrix as a list of lists of booleans would take O(n^2) space, which is 64 million entries. In Python, a list of lists of booleans is manageable, but may require a lot of memory. For example, each boolean in Python is stored as a separate object, which is more memory-intensive. So perhaps a better way is to represent each row as a bitmask using integers. For example, each row is a list of integers, where each integer represents a chunk of bits. But checking adj[i][j] would require bitmask operations.

Alternatively, use a list of bitarrays for each row. The bitarray module allows efficient storage and access. But if we can't use external modules, then we can represent each row as an array of integers, where each integer represents a chunk of bits. But in Python, for n=8000, a row can be represented as a list of 250 integers (since 8000 / 32 = 250), each storing 32 bits. But checking adj[i][j] would require finding the correct integer in the list and then checking the corresponding bit.

Alternatively, for each row, store it as a single integer (for n up to 8000, which requires 8000 bits per row, which is 1000 bytes per row. But Python's integers can handle arbitrary lengths. However, checking individual bits may be time-consuming.

Alternatively, for each row i, precompute a dictionary of j where adj[i][j] is True. But for n=8000, each row would have about 4000 entries (since it's a tournament), which would take O(n) space and time.

But in practice, for the algorithm to find the SCCs, we need to check adj[u][v] for various u and v. So, for the binary search step, when processing node u, we need to check if u has an edge to the representative of each component.

Thus, the critical part is to be able to check adj[u][rep] quickly.

So storing each row as a bitmask (a list of bits) is feasible, but in Python, accessing a bit is O(1) time if stored as a string or a list. So for each row i, we can store the binary string as a list of '0's and '1's.

But for n=8000, each row is a string of 8000 characters. Each character is '0' or '1'. So for 8000 rows, this is 8000 * 8000 = 64 million characters, which is 64 MB. That's manageable.

So the code can proceed as follows:

Read each row, expand the hex digits into a binary string of length n, and store each row as a string (or list of characters).

Then, for any u and v, adj[u][v] is simply row_u[v] == '1'.

Now, the steps are:

1. Read n.

2. Read n lines, each containing n/4 hex digits. For each line, convert to a binary string of length n.

3. Build the adjacency matrix as a list of binary strings (or lists).

4. Process each node u in order 0 to n-1, using the binary search-based algorithm to build the components.

5. Once the components are built, compute for each node the SCC it belongs to and the topological order of the SCCs.

6. For each ordered pair (A, B), compute the distance as follows:

   a. If A and B are in the same SCC:

       i. If adj[A][B] is 1, distance is 1.

       ii. Else, distance is 2.

   b. Else if A's SCC comes before B's SCC in the topological order:

       i. Distance is 1.

   c. Else:

       i. Distance is 614 * n.

7. Sum all these distances.

The problem is to compute this sum efficiently. For n=8000, there are 8000*8000 = 64 million pairs. Iterating over all pairs and checking their SCCs would be O(n^2), which is manageable if the per-pair operations are O(1).

So the plan is:

- Precompute for each node its SCC's index in the topological order.

- Precompute the topological order list of components.

- For each pair (A, B):

   if A == B: skip.

   else:

       scc_a = scc_of[A]

       scc_b = scc_of[B]

       if scc_a == scc_b:

           if adj[A][B] == '1':

               sum += 1

           else:

               sum += 2

       elif scc_a < scc_b:

           sum += 1

       else:

           sum += 614 * n

This approach would be O(n^2), which is 64 million operations, acceptable in Python if the per-iteration steps are optimized.

But wait, in Python, even a loop over 64 million steps can take time. So we need to find a way to compute this sum as efficiently as possible.

For example, precompute for each SCC the number of nodes in it. Then:

The sum can be computed as:

sum = 0

for each component C in topological order:

   for each component D in topological order after C:

       sum += len(C) * len(D) * 1

   for each pair of nodes A and B in C:

       if A != B:

           sum += 1 if adj[A][B] else 2

sum += (number of pairs where A's component is after B's component) * 614 * n

But how to compute this?

Let's break it down:

The total sum is composed of three parts:

1. Pairs where A and B are in the same SCC.

   For each such pair, add 1 or 2.

2. Pairs where A's component is before B's component.

   Each such pair contributes 1.

3. Pairs where A's component is after B's component.

   Each such pair contributes 614 * n.

We can compute each part separately.

Let's compute each part:

First, compute the total number of pairs where A and B are in the same component.

For each component C of size m, there are m*(m-1) pairs.

Sum all m*(m-1) over all components C.

For each such pair, add 1 if adj[A][B] is 1, else 2. So for each component C, sum over all ordered pairs (A, B) in C, A != B:

sum_C = number of edges (A→B) in C + 2*(m*(m-1) - number of edges).

But the number of edges in a strongly connected tournament (component C) is m*(m-1)/2, since every pair has exactly one edge. So for each component C of size m, the number of ordered pairs (A,B) with A→B is m*(m-1)/2 + (number of edges where A→B in C).

Wait, no. Wait, in a tournament, the number of edges in a component C is m*(m-1)/2. So the number of ordered pairs where A→B is exactly m*(m-1)/2. The remaining ordered pairs (B→A) are also m*(m-1)/2, but only if m is even. No, for m nodes, there are m*(m-1) ordered pairs (A,B) where A != B. Exactly half of them have edges in one direction and the other half in the other direction. But this is only true for even m. Wait, no. In a tournament, for each pair (A,B), exactly one of A→B or B→A exists. So for m nodes, there are m*(m-1)/2 edges (since each unordered pair contributes one edge). But the ordered pairs are m*(m-1), each of which has exactly one edge.

But for a strongly connected tournament (which each component is), each pair of nodes has a path from A to B of length 1 or 2. So the sum of the distances for pairs in the same component is:

For each pair (A,B):

   if A→B: distance 1.

   else: distance 2.

So the sum for the component is (number of edges in the component) * 1 + (number of non-edges) * 2.

But the number of edges in the component is m*(m-1)/2 (since each unordered pair contributes one edge). But the ordered pairs (A,B) where A != B are m*(m-1). So the number of edges (A→B) is m*(m-1)/2. Because for each unordered pair (A,B), exactly one direction is present. So in ordered terms, there are m*(m-1) ordered pairs, and exactly half of them are edges (A→B) and the other half are edges (B→A). So the number of edges in the component is m*(m-1)/2.

Wait, no. Let's see: m nodes. The total number of ordered pairs (A,B) where A != B is m*(m-1). The number of edges (A→B) is exactly m*(m-1)/2. Because for each unordered pair, there's exactly one edge. For example, if m=2, there are 2 ordered pairs (A→B and B→A), but only one edge.

So yes, the number of edges (A→B) in the component is m*(m-1)/2.

Thus, for each component C of size m, the sum for pairs in C is:

number of edges (A→B) * 1 + (total pairs in C - number of edges) * 2.

But the total pairs in C is m*(m-1). The number of edges is m*(m-1)/2.

So sum_C = (m*(m-1)/2)*1 + (m*(m-1)/2)*2 = (m(m-1)/2) * (1 + 2) = (3/2) * m(m-1).

This is a key insight! For each strongly connected tournament (component), the sum of distances between all ordered pairs within the component is 3/2 * m*(m-1). Because half of the ordered pairs have distance 1, and the other half have distance 2.

Wait, but wait: if there are m nodes, then the number of ordered pairs is m*(m-1). Half of them are edges (distance 1), and the other half are not (distance 2). So sum is (m*(m-1)/2)*1 + (m*(m-1)/2)*2 = (1 + 2) * (m(m-1)/2) = 3/2 * m(m-1).

Yes! So for each component of size m, the sum of distances within the component is (3/2) * m(m-1).

This is a huge simplification. So instead of checking each pair within the component, we can calculate this directly.

This reduces the first part of the sum to summing over all components (3/2)*m(m-1).

So part1 = sum over all components C of (3 * m * (m-1)) // 2.

The second part is the sum of all pairs where A's component is before B's component. For each such pair, the distance is 1.

The number of such pairs is the sum over all pairs of components (C, D) where C comes before D, of (size of C) * (size of D).

So if the components are ordered as C0, C1, ..., Ck-1 in topological order, then the number is sum_{i=0 to k-2} sum_{j=i+1 to k-1} len(Ci) * len(Cj).

The third part is all pairs where A's component is after B's component. For each such pair, the distance is 614*n.

The number of such pairs is total_pairs - part1_pairs - part2_pairs.

Where total_pairs is n*(n-1).

Because total_pairs = part1_pairs (same component) + part2_pairs (A's component before B's) + part3_pairs (A's component after B's).

So part3_pairs = total_pairs - part1_pairs - part2_pairs.

Thus, the sum can be computed as:

sum = part1 + part2 * 1 + part3 * 614 * n.

So the problem reduces to:

1. Compute part1: sum over all components (3 * m * (m-1) // 2).

2. Compute part2: sum over all pairs of components (C, D) where C comes before D, of len(C) * len(D).

3. part3 = total_pairs - part1_pairs - part2_pairs.

Then, sum = part1 + part2 * 1 + part3 * 614 * n.

This approach is O(k^2) for part2, where k is the number of components. For n=8000 and components potentially up to 8000 (if each component is a single node), k^2 can be 64 million, which is manageable.

But wait, if the components form a chain, then part2 is the sum of len(C_i) * len(C_j) for i < j. Which can be computed as (sum_{i} len(C_i))^2 - sum_{i} len(C_i)^2) // 2. Wait, no. Because sum_{i<j} a_i a_j = (sum a_i)^2 - sum a_i^2) / 2. But sum a_i = n.

So part2 can be computed as (n^2 - sum over components len^2) // 2 - part1_pairs.

Wait, because:

sum_{i<j} len(Ci) * len(Cj) = [ (sum len(Ci))^2 - sum len(Ci)^2 ] / 2.

But sum len(Ci) is n. So part2 = (n^2 - sum_len_sq) // 2.

But part1_pairs is the sum of len(C) * (len(C)-1) for each component C. Which is sum_len_sq - n, since sum len(C) is n, sum len(C)^2 is sum_len_sq. So sum len(C)(len(C)-1) = sum (len^2 - len) = sum_len_sq - n.

Thus, part1_pairs = sum_len_sq - n.

 part2_pairs = (n^2 - sum_len_sq) / 2.

 part3_pairs = n(n-1) - (sum_len_sq - n) - (n^2 - sum_len_sq)/2.

Let me compute this:

n(n-1) = total_pairs.

part1_pairs = sum len(C) (len(C) - 1) = sum_len_sq - sum len(C) = sum_len_sq - n.

part2_pairs = (n^2 - sum_len_sq) / 2.

So part3_pairs = n(n-1) - (sum_len_sq - n) - (n^2 - sum_len_sq)/2.

Let me simplify:

part3_pairs = n(n-1) - sum_len_sq + n - (n^2 - sum_len_sq)/2.

Combine terms:

= [n(n-1) + n ] - sum_len_sq - (n² - sum_len_sq)/2 

= n² - sum_len_sq - (n² - sum_len_sq)/2 

= [ 2(n² - sum_len_sq) - (n² - sum_len_sq) ] / 2 

= (n² - sum_len_sq) / 2 

But wait, this can't be right. Because part3_pairs should be the same as part2_pairs but in reverse. If the components are ordered in a linear order, then the number of pairs where A's component is after B's component is the same as part2_pairs but reversed. So part3_pairs should be equal to part2_pairs. But according to this calculation, part3_pairs is (n² - sum_len_sq)/2.

But part2_pairs is (n² - sum_len_sq)/2. So part3_pairs is also (n² - sum_len_sq)/2.

But this would imply that part3_pairs = part2_pairs, which is only possible if the components are arranged in a way that the number of pairs (A,B) where A's component is before B's is equal to the number of pairs where A's component is after B's. Which is only true if the components form a symmetric structure, which is not the case.

But this suggests a mistake in the earlier reasoning.

Let me re-derive:

The total number of ordered pairs (A,B) where A != B is n*(n-1).

These can be partitioned into three mutually exclusive categories:

1. A and B are in the same component: sum_len_sq - n.

2. A's component is before B's: part2_pairs = (n² - sum_len_sq) / 2.

3. A's component is after B's: part3_pairs = (n² - sum_len_sq) / 2.

Because:

The sum of pairs where A and B are in different components is (n² - sum_len_sq). Because sum_len_sq is the sum of squares of component sizes. The total possible pairs for different components is n² - sum_len_sq. These are split equally between part2_pairs and part3_pairs, because for each pair of components (C, D), C != D, there are len(C)*len(D) pairs. Exactly half of these are in part2_pairs (when C comes before D) and half in part3_pairs (when C comes after D). But this is only true if the components are ordered in a way that for every pair of components C and D, exactly one is before the other. Since the components are ordered in a linear topological order, this is true. So part2_pairs and part3_pairs are each (n² - sum_len_sq)/2.

So this explains why part3_pairs = part2_pairs = (n² - sum_len_sq)/2.

But this can't be correct. Because part2_pairs is the sum of len(C)*len(D) for all C < D. part3_pairs is the sum for all C > D. So part2_pairs and part3_pairs are both equal to (n² - sum_len_sq)/2.

But this is only true if the components are ordered such that every pair of distinct components is ordered. Which they are.

So, part2_pairs = part3_pairs = (n² - sum_len_sq)/2.

But this would imply that part3_pairs = part2_pairs, but according to the problem's distance calculation, part2_pairs contribute 1, and part3_pairs contribute 614n.

Thus, the sum can be computed as:

sum = part1 + part2_pairs * 1 + part3_pairs * 614n.

But part2_pairs and part3_pairs are both (n² - sum_len_sq)/2.

So sum = part1 + (n² - sum_len_sq)/2 * (1 + 614n).

Thus, this is a key insight. By leveraging the properties of the components and their topological order, we can compute the sum in O(n) time for part1, and O(1) time for part2 and part3, once sum_len_sq is computed.

Thus, the steps are:

1. Compute the components and their sizes.

2. Compute sum_len_sq = sum of (size of component)^2 over all components.

3. part1 = 3 * sum( m*(m-1) for m in component sizes ) // 2.

4. part2 = (n^2 - sum_len_sq) // 2.

5. sum_total = part1 + part2 * 1 + part2 * 614 * n.

Because part3_pairs is part2_pairs (same value), and they contribute 614n each.

Thus, sum_total = part1 + part2 * (1 + 614n).

This reduces the problem to:

- Finding the components and their sizes.

- Calculating sum_len_sq and part1.

This is a massive optimization, as it reduces the sum calculation to O(k) time, where k is the number of components, which is O(n) in the worst case.

Thus, the plan is:

- Read the adjacency matrix.

- Find the components using the binary search algorithm.

- For each component, calculate its size.

- Compute sum_len_sq = sum(m^2 for m in component sizes).

- Compute part1 = 3 * sum(m*(m-1) for m in component sizes) // 2.

- Compute part2 = (n*n - sum_len_sq) // 2.

- Compute sum_total = part1 + part2 * (1 + 614 * n).

Thus, the code can be written as follows:

Read n.

Read the adjacency matrix.

Process the components using the binary search algorithm.

Compute sum_len_sq and sum_mm_minus_m (sum of m*(m-1) for all components).

part1 = 3 * sum_mm_minus_m // 2.

part2 = (n*n - sum_len_sq) // 2.

sum_total = part1 + part2 * (1 + 614 * n).

Output sum_total.

Thus, the key steps are:

- Efficiently finding the components.

- Efficiently reading the adjacency matrix.

Now, the code for the components:

Implement the binary search-based algorithm to find the components.

For each node u in 0 to n-1:

   binary search to find the first component in reversed order where adj[u][c_rep] is 1.

   merge the components from that index onwards, and add u to form a new component.

Implementing this requires:

- For each component, track the representative node (the first node in the component).

- For each new node u, iterate over the components in reversed order (using binary search to find the first component where u has an edge to the representative).

Let's code this.

Now, let's think about the data structures for components. Each component can be represented as a list of nodes, and the representative is the first node in the list.

Thus, during processing, we can track components as a list of lists. For example, components = [ [0], [1,2,3] ].

For each component, the representative is component[0].

Thus, during processing node u:

   reversed_components = components[::-1]

   left = 0

   right = len(reversed_components)

   while left < right:

       mid = (left + right) // 2

       c_rep = reversed_components[mid][0]

       if adj[u][c_rep] == '1':

           right = mid

       else:

           left = mid + 1

   if left < len(reversed_components):

       # merge all components from index (len(components) - 1 - left) onwards.

       merge_idx = len(components) - 1 - left

       new_component = [u]

       for c in components[merge_idx:]:

           new_component.extend(c)

       components = components[:merge_idx] + [new_component]

   else:

       components.append([u])

This code would process each node and build the components correctly.

But in Python, list operations like slicing and extending can be expensive for large lists. But with n=8000 and components being merged frequently, this should be manageable.

Once the components are built, compute sum_len_sq and sum_mm_minus_m.

sum_len_sq = sum( len(c)**2 for c in components )

sum_mm_minus_m = sum( len(c)*(len(c)-1) for c in components )

Thus, part1 = (3 * sum_mm_minus_m) // 2.

part2 = (n * n - sum_len_sq) // 2.

sum_total = part1 + part2 * (1 + 614 * n).

Print sum_total.

Now, the remaining challenge is to read the adjacency matrix correctly.

The code to read the hex digits and convert to binary:

For each row i in 0 to n-1:

   hex_str = input().strip()

   # convert each hex character to 4 bits, MSB first.

   bin_str = ''.join( [ format(int(c, 16), '04b') for c in hex_str ] )

   adj.append( bin_str )

Then, adj[i][j] is '1' if there's an edge from i to j.

But for large n, this may take some time, but it's manageable.

Finally, the code should be:

Read n.

Read n lines of hex digits, convert to binary strings of length n.

Process the components.

Compute sum_len_sq and sum_mm_minus_m.

Compute and print the sum_total.

Now, let's test this approach with the first example:

First example input:

4

7 → hex 7 is 0111.

2 → hex 2 is 0010.

1 → hex 1 is 0001.

4 → hex 4 is 0100.

The binary rows are:

Row 0: 0111 → adj[0][0] is 0, adj[0][1] is 1, etc.

Components processing:

Node 0:

components is empty. Add [0]. components = [ [0] ]

Node 1:

Process components in reverse (just [0]).

Check if adj[1][0] is '1' → row 1's binary is 0010.

adj[1][0] is 0 → no. So add [1]. components = [ [0], [1] ].

Node 2:

Process components in reverse order [1, 0].

Check component [1]: adj[2][1] is 0 (row 2's binary is 0001. j=1 is 0).

Check component [0]: adj[2][0] is 0 (row 2's j=0 is 0). So add [2]. components = [ [0], [1], [2] ].

Node 3:

Process components in reverse order [2, 1, 0].

Check component [2]: adj[3][2] is 0 (row 3's binary is 0100. j=2 is 0).

Check component [1]: adj[3][1] is 1 (row 3's j=1 is 1).

So left = 0, right = 3.

After binary search, left will be 1 (index in reversed_components is 1, which is component [1]).

merge_idx = len(components) - 1 - left = 3-1 - 1 = 1.

Merge components from merge_idx=1 onwards. components[1:] is [ [1], [2] ].

new_component is [3,1,2]. So components becomes [ [0], [3,1,2] ].

sum_len_sq = 1^2 + 3^2 = 1 + 9 = 10.

sum_mm_minus_m = 1*0 + 3*2 = 0 +6=6.

part1 = 3*6//2 =9.

part2 = (4*4 -10)/2 = (16-10)/2=3.

sum_total =9 + 3*(1 + 614*4) =9 + 3*(1+2456) =9 + 3*2457=9 + 7371=7380 → matches the first example.

Thus, the code works.

The second example would be handled similarly.

Thus, the code is correct.

Now, let's write the Python code.
</think>

```python
import sys

def main():
    n = int(sys.stdin.readline())
    adj = []
    for _ in range(n):
        hex_row = sys.stdin.readline().strip()
        bin_str = ''.join(f"{int(c, 16):04b}" for c in hex_row)
        adj.append(bin_str)
    
    components = []
    for u in range(n):
        left = 0
        right = len(components)
        while left < right:
            mid = (left + right) // 2
            c_idx = len(components) - 1 - mid
            c_rep = components[c_idx][0]
            if adj[u][c_rep] == '1':
                right = mid
            else:
                left = mid + 1
        if left < len(components):
            merge_idx = len(components) - 1 - left
            merged = [u]
            for i in range(merge_idx, len(components)):
                merged.extend(components[i])
            components = components[:merge_idx] + [merged]
        else:
            components.append([u])
    
    sum_len_sq = sum(len(c)**2 for c in components)
    sum_mm_minus_m = sum(len(c)*(len(c)-1) for c in components)
    part1 = (3 * sum_mm_minus_m) // 2
    part2 = (n * n - sum_len_sq) // 2
    total = part1 + part2 * (1 + 614 * n)
    print(total)

if __name__ == "__main__":
    main()
```