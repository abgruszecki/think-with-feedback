<think>
Okay, let's tackle this problem. So, the task is to find the maximum distance between two nodes in a tree such that the GCD of all the nodes along their path is greater than 1. If there's no such pair, output 0.

Hmm, first, I need to understand what the problem is really asking. The distance here is the number of vertices in the path, which is the same as the number of edges plus 1. The main challenge is efficiently checking for each possible pair whether their path's GCD is greater than 1, and among those pairs, finding the maximum distance.

But with n up to 2e5, checking all possible pairs is impossible. That's O(n^2), which is way too slow. So we need a smarter approach.

Let me think. The GCD of all numbers in a path is the GCD of all a_i along that path. For this GCD to be greater than 1, there must be at least one prime factor that divides all nodes in the path. So, the problem reduces to finding the longest path where all nodes have a common prime factor. Then, among all primes, the maximum such path's length is our answer.

So the approach would be:

1. For each prime p, collect all nodes that have p as a factor.
2. For each such collection, find the longest path in the tree that uses only nodes from this collection.
3. The maximum length among all these primes gives the answer.

The maximum possible answer is the longest path (diameter) in any of these induced subgraphs (the subgraph consisting of nodes with a common prime factor). But how do we compute this efficiently?

The key steps are:

- Factorize each a_i into primes.
- For each prime p, collect all nodes that have p as a factor.
- For each such group, compute the longest path in their induced subgraph.

But even this approach could be time-consuming if done naively. Let's see.

Factorizing each a_i: Since a_i can be up to 2e5, we can precompute the smallest prime factors (SPF) for numbers up to 2e5. Then factorization can be done quickly.

Grouping nodes by primes: For each a_i, we add it to all its prime factors. For example, if a_i is 12 (primes 2 and 3), then the node is added to the groups for 2 and 3.

Now, for each prime p, the group consists of nodes where a_i is divisible by p. Then, we need to find the longest path in the original tree where all nodes in the path belong to this group. The length is the number of nodes in the path, which is the diameter of the induced subgraph.

Wait, but the induced subgraph for p is the subset of nodes in the original tree that are divisible by p. But the edges are only those present in the original tree. So the induced subgraph is a collection of trees (since the original is a tree) — the nodes are those divisible by p, and edges are between them as per the original tree. So each connected component in the induced subgraph is a subtree.

The diameter of each connected component is the longest path within it. So for each prime p, we need to find the maximum diameter among all connected components in the induced subgraph for p.

The maximum of all these across all primes is our answer. If no primes have at least two nodes (or a single node with distance 1?), then output 0.

But how do we compute the diameter for each connected component efficiently?

The standard way to compute the diameter of a tree is to perform BFS or DFS twice. First, find the farthest node from an arbitrary node (say u), then find the farthest node from u, which is the diameter.

But if the group for p has m nodes, doing BFS for each group could take O(m) time. If a node is in multiple groups (like a_i is 6, in groups 2 and 3), then each group would process it. But in the worst case, if all a_i are primes, then each group has one node. Then processing all primes would take O(n) time. But primes up to 2e5 are around 2e4 (since the number of primes below x is approx x / ln x). So 2e5's primes are around 18,000+ primes. But if each of them has one node, then processing each group would take O(1) time, so total is O(2e5) time. But if a node is part of multiple primes (like a_i=6, part of 2, 3), then the same node is processed in multiple groups. So the total sum over all primes of the group sizes could be O(n log a_i), which is manageable since a_i is up to 2e5. For example, the maximum number of primes a number can have is log_2(2e5) ≈ 18. So total sum is O(n * 18) = 3.6e6, which is acceptable.

So the plan is:

1. Precompute all primes up to 2e5 using sieve of eratosthenes for SPF.
2. Factorize each a_i into its prime factors, and for each prime, collect the nodes that have that prime as a factor.
3. For each prime p, process all nodes in its group. For each connected component in the induced subgraph (tree), compute its diameter.
4. The maximum diameter across all primes is the answer. If no such diameter is at least 1 (i.e., no nodes in any group), output 0.

Now, the main challenge is efficiently finding the connected components and computing their diameters for each group.

But how to compute connected components for a group. Since the original tree is connected, but when we take a subset of nodes, the induced subgraph may be disconnected. So for each group, we need to find all connected components.

But how? Since the original tree is a tree, the induced subgraph for the group is a forest. Each connected component is a subtree. To find the connected components, perhaps for each node in the group, we can traverse its neighbors (in the original tree) that are also in the group, and build a BFS or DFS. However, doing this for each group would be time-consuming if done naively.

Alternative approach: For each node in the group, we can check which of its adjacent nodes are also in the group, and build the adjacency list on the fly.

Wait, but for each group (prime p), the adjacency list is a subset of the original edges. So for each node in the group, their neighbors in the original tree that are also in the group are their neighbors in the induced subgraph.

So, for processing a group:

- We have a list of nodes in the group.
- For each node, collect its adjacent nodes (from the original tree's adjacency list) that are also in the group.
- This forms the adjacency list for the group's connected components.

But for each group, building this adjacency list could take O(m) time, where m is the number of nodes in the group multiplied by the average degree. However, since the original tree has O(n) edges, each node's adjacency list is O(1) on average (since it's a tree, average degree is 2). So for a group of size m, the time to build the adjacency list is O(m) in total.

Once we have the adjacency list for the group's connected component, then to compute the diameter, we can perform BFS twice. But BFS on each connected component would take O(m) time per component. So for each group, the total time is O(m), where m is the number of nodes in the group.

But the problem is that a single node can be part of multiple groups. For example, a node with a_i=6 is part of groups 2 and 3. So when processing group 2, this node is included, and when processing group 3, it's included again. So the total processing across all groups is O(sum of m_p for all primes p), where m_p is the size of the group for p. As discussed earlier, this sum is O(n * number of primes per a_i), which for n=2e5 and up to 18 primes per a_i is manageable (3.6e6 steps).

So, the steps are feasible.

Now, the algorithm:

For each prime p:

   collect all nodes that have p as a factor → list S.

   For each node in S, build adjacency list by checking which of its original neighbors are in S.

   Then, for each connected component in this adjacency list, compute the diameter.

   Keep track of the maximum diameter found across all primes.

If the maximum diameter is at least 1 (since a single node has distance 1, but the problem requires pairs, so the minimum possible is two nodes, distance 2?), wait no. Wait, the problem says that dist(x,x) is 1, and the GCD of a single node is a_x. So if a_x >1, then the pair (x,x) is valid, with distance 1. But according to the problem statement, we need to choose pairs x,y (possibly x=y) such that g(x,y) >1. So the maximum distance can be 1 if there's a node with a_i>1 but no pair of nodes with a path's GCD>1. For example, if all a_i are primes, and no two are the same. Then the best is a single node, distance 1.

But in the first example, the input is 3 nodes with 2,3,4. The edges are 1-2-3. For primes 2, the group includes nodes 1 and 3 (since 4 is 2²). The path between 1 and 3 is 1-2-3. But node 2 has a value of 3, which is not divisible by 2. So the induced subgraph for prime 2 is nodes 1 and 3. The edges in the original tree between 1 and 2 and 2 and 3. But the induced subgraph only has nodes 1 and 3. So the edges in the induced subgraph are only if there is a path between them through nodes in the group. Wait, no. The induced subgraph consists of the nodes in the group and the edges from the original tree that connect two nodes in the group.

So for group 2, nodes 1 (a_i=2) and 3 (a_i=4). The original edges are 1-2 and 2-3. But 2 is not in the group (since a_2 is 3, not divisible by 2). So the induced subgraph has nodes 1 and 3, but no edges between them. So each is a connected component of size 1. The maximum distance in each component is 1. So the overall maximum for group 2 is 1. So in the first example, the answer is 1. So the output is 1.

Wait, but the sample input 1's output is 1. Because the only possible valid pairs are (1,1), (3,3), (2,2). But their GCD is 2,3,4 respectively. So 2 and 4 have GCD>1. But wait, the first sample's output is 1. That's because the maximum possible distance is 1. Because even though node 3's value is 4 (divisible by 2), there's no path between node 1 and 3 in the induced subgraph for 2. So their paths in the original tree would include node 2, which is not part of the group. So the GCD would include node 2's value, which is 3. So the GCD of 2,3,4 is 1. So the pair (1,3) is not a valid pair. Therefore, in the first sample, the only valid pairs are the single nodes. Hence the output is 1.

So, the approach is correct.

But how to model the induced subgraphs for each prime?

Let me think again. For a given prime p, the group S is all nodes with a_i divisible by p. The edges in the induced subgraph are the edges in the original tree between nodes in S. So, for example, if two nodes u and v are in S and are connected by an edge in the original tree, then they are connected in the induced subgraph. Otherwise, the edge is not present.

So, the induced subgraph is a forest (since the original is a tree), and each connected component is a subtree (the original tree's edges between nodes in S).

Now, to compute the connected components for S, we can perform BFS or DFS. For each node in S, if not visited, we start a BFS/DFS, adding all reachable nodes in S via edges in the original tree that connect nodes in S.

But how do we efficiently check if a neighbor is in S?

Hmm. For each neighbor of a node u, we need to check whether that neighbor is in the group S. Since S is a set (or a hash set), checking membership is O(1). But for 2e5 nodes, and for each group S, this could be O(1) per neighbor check.

But building a hash set for each group S would take O(m) time per group, which is acceptable.

Alternatively, during preprocessing, for each node u, for each prime p in its prime factors, we can add u to a list for p. Then, for each p, the list is S_p. Then, to check if a node v is in S_p, we can precompute for each node a set of primes that divide it, and then check if p is in that set. But for each node, the set of primes is stored, so for a neighbor v of u, we can check if p is in the primes of v.

Wait, but that would require for each node u, a set of primes that divide a_u. So during the factorization step, for each a_i, we collect all its prime factors (without duplicates) and store them in a list for node u. Then, when processing a group for prime p, to check if a neighbor v is in the group, we can check if p is in the prime factors of v.

So for example, during the group processing for p:

- For a node u in S_p (group p), we iterate through all its neighbors in the original tree. For each neighbor v, if p is in the prime factors of v's a_i, then we include v as a neighbor in the induced subgraph.

This way, for each group p, when building the adjacency list for the induced subgraph, we can check for each neighbor v of u if v is in S_p by checking if v's primes include p.

But storing for each node u a set of primes (as a list, maybe) allows us to check if p is present.

So the steps would be:

1. Precompute SPF (smallest prime factor) for numbers up to 2e5.

2. For each a_i in the input, factorize into primes (using SPF), and collect the unique primes. For example, a_i=12 factors into 2 and 3.

3. For each node u (0-based or 1-based?), store a set (or list) of primes that divide its a_i.

4. For each prime p, collect all nodes u where p is in their prime factors. So S_p is the list of nodes for p.

5. For each S_p, if the size is 0 or 1, skip (since the maximum possible distance in such a group is 1, but we need to check if there's at least one node. If size 1, then distance 1. If size 0, nothing.)

6. For S_p with size >= 1:

   a. For each node in S_p, create a list of adjacent nodes (from the original tree's adjacency list) that are also in S_p. This can be done by checking if the neighbor's primes include p.

   b. Find connected components in this induced subgraph.

   c. For each connected component, compute its diameter.

   d. Keep track of the maximum diameter found.

So the main challenge is efficiently building the adjacency list for each S_p and then finding the diameters.

But how to handle this without using too much time and memory.

Alternative idea: instead of building the adjacency list for S_p, we can traverse the original tree but only visit nodes in S_p. For example, during BFS for a connected component in S_p, when we visit a node u, we look at all its neighbors in the original tree and check if they are in S_p. If yes, add to the queue if not visited.

But this way, we don't need to build an explicit adjacency list. For each node in S_p, when processing it, we check each neighbor in the original tree's adjacency list. If the neighbor is in S_p (i.e., has p as a factor), then it's part of the same connected component.

This approach would avoid building separate adjacency lists for each group. Instead, during BFS/DFS for a group's connected component, we just check the neighbors on the fly.

This seems more efficient. Because building adjacency lists for each group would take O(m_p * avg_degree) time, but avg_degree in a tree is O(1) (since each node has up to, say, 100 children, but average is 2). So for each group, the time is O(m_p) steps, but each step involves checking each neighbor in the original adjacency list, and checking if that neighbor is in S_p.

But checking if a neighbor is in S_p can be done by looking up whether the neighbor's primes include p. So for each neighbor v of u, we check if p is in the list of primes for v. So for each such check, we can do a linear scan through the primes of v. Wait, but that's O(k) time, where k is the number of primes of v. For example, if v has 3 primes, this check takes O(3) time.

But since each node has at most log2(2e5) primes (since each prime factor is at least 2), the number of primes per node is O(1). So each check is O(1) time.

Wait, for example, the maximum number of distinct primes for a number up to 2e5 is 5 (like 2*3*5*7*11=2310, which is much smaller than 2e5). So each number can have up to 5 distinct primes. So checking if a node's primes include p is O(5) per check, which is acceptable.

Thus, during BFS traversal for a group p's connected component:

- For each node u in the group, when processing its neighbors, for each neighbor v in the original tree, check if p is in v's primes. If yes, and if v hasn't been visited, then add to the queue.

This way, the BFS is performed efficiently.

So the steps for a group p would be:

- Initialize a visited set (could be a boolean array) to track which nodes in the group have been processed.

- For each node u in S_p:

   if not visited:

      perform BFS or DFS starting at u, traversing only nodes in S_p.

      during traversal, for each node in the queue, iterate through its original neighbors, and check if the neighbor is in S_p (by checking if p is in the neighbor's primes).

      collect all nodes in this connected component.

      compute the diameter of this component.

      update the maximum diameter if necessary.

So the question is: how to compute the diameter of a connected component (which is a tree) efficiently.

The standard approach for diameter is:

1. Perform BFS from any node to find the farthest node, say u.

2. Perform BFS from u to find the farthest node, say v. The distance between u and v is the diameter.

But in this case, the connected component is a tree (since the original graph is a tree, and the induced subgraph is a forest of trees). So each connected component is a tree.

So, for each connected component, we can compute the diameter using BFS twice.

But since each connected component can have up to m_p nodes (which could be up to 2e5, but likely much smaller), the time per connected component is O(m_p).

So for all primes, the total time is O(sum_p (m_p * log m_p))? No, because for each group p, the sum of m_p over all primes p is O(n * average number of primes per node), which is manageable.

Now, putting this all together.

The steps in code:

1. Precompute SPF.

   Use sieve of eratosthenes to precompute the smallest prime factor for each number up to 2e5.

2. For each a_i in the input, factorize into primes, collect the unique primes.

   For example, a_i=12 → factors 2 and 3.

   Store for each node u (0-based?), a list of primes.

3. For each prime p, collect all nodes u that have p as a prime factor.

   So, for each p, S_p is a list of nodes.

   We can use a dictionary (prime_to_nodes) where the key is p, and the value is a list of nodes.

   For example, during preprocessing:

   for each node u in 0..n-1:

       for p in primes_list[u]:

           if p not in prime_to_nodes:

               prime_to_nodes[p] = []

           prime_to_nodes[p].append(u)

4. For each prime p in prime_to_nodes:

   S_p = prime_to_nodes[p]

   if len(S_p) == 0: skip

   else:

       compute the maximum diameter among all connected components in S_p.

       for each connected component in S_p:

           compute its diameter.

           if diameter > current_max:

               update current_max.

5. After processing all primes, output the maximum diameter found. If no primes have any nodes, output 0.

But wait, if a node has a_i=1, it has no prime factors. So S_p for any p would not include it. So if all a_i are 1, then output 0.

Now, let's see how to implement the BFS for connected components and diameter.

Implementing BFS for connected components:

For a given p and S_p:

visited = array of booleans, initialized to False for all nodes.

for each node u in S_p:

   if not visited[u]:

       # start BFS from u

       queue = deque([u])

       visited[u] = True

       component = []

       while queue:

           current = queue.popleft()

           component.append(current)

           for neighbor in original_adj[current]:

               if not visited[neighbor] and (p is in primes_list[neighbor]):

                   visited[neighbor] = True

                   queue.append(neighbor)

       # component contains all nodes in this connected component

       # compute the diameter of component

       if len(component) == 0:

           continue

       # compute diameter here

So, once the component is collected, compute its diameter.

To compute the diameter:

The standard approach is to do BFS twice.

But how to handle this for the component.

But the component is a tree. So, the steps would be:

Within the component:

1. Pick any node u.

2. BFS to find the farthest node v from u.

3. BFS again from v to find the farthest node w. The distance between v and w is the diameter.

But how to compute the distance, which is the number of nodes in the path (including both ends). Wait, the distance here is the number of nodes on the path. So, the standard BFS gives the number of edges. So the distance in edges is (number of nodes - 1). So, for example, a path of 3 nodes (u-v-w) has distance 3 (nodes) → 2 edges.

But according to the problem statement, dist(x, y) is the number of vertices in the path. So for a path of two nodes (x and y connected by an edge), the distance is 2.

In the code for diameter calculation, after finding the BFS levels (distance in edges), the maximum distance in edges would be (diameter_edges), and the node count is diameter_edges + 1.

So, when computing the diameter, the maximum number of edges in the path is found, and the node count is edges +1.

So, in code:

For a connected component (a tree):

def compute_diameter(component_nodes, original_adj, primes_list, p):

   # component_nodes is a list of nodes in the component.

   # But we need to traverse only within the component.

   # So, during BFS, when visiting a node, check if it's in the component.

   # Wait, but component_nodes is all nodes in the component, so perhaps we can precompute a set for O(1) lookups.

   # Alternatively, during BFS, check if the neighbor is in the component.

   # But component_nodes could be a set for O(1) lookups.

   # So, first, create a set for the component.

   component_set = set(component_nodes)

   # Now, pick a starting node (component_nodes[0])

   start_node = component_nodes[0]

   # BFS to find farthest node from start_node.

   max_dist = 0

   farthest_node = start_node

   visited = {node: False for node in component_nodes}

   q = deque([(start_node, 1)])  # distance in nodes is 1 initially (start_node itself)

   visited[start_node] = True

   while q:

       current, dist = q.popleft()

       if dist > max_dist:

           max_dist = dist

           farthest_node = current

       for neighbor in original_adj[current]:

           if neighbor in component_set and not visited[neighbor]:

               visited[neighbor] = True

               q.append( (neighbor, dist +1) )

   # Now BFS again from farthest_node to find the maximum distance.

   max_dist = 0

   visited = {node: False for node in component_nodes}

   q = deque([(farthest_node, 1)])

   visited[farthest_node] = True

   while q:

       current, dist = q.popleft()

       if dist > max_dist:

           max_dist = dist

       for neighbor in original_adj[current]:

           if neighbor in component_set and not visited[neighbor]:

               visited[neighbor] = True

               q.append( (neighbor, dist +1) )

   # The maximum distance in nodes is max_dist.

   return max_dist

Wait, but the component_set is the set of nodes in the component. So, during BFS, we can only move to neighbors that are in the component.

But how is the original_adj structured? The original_adj is the adjacency list of the original tree. So for each node in the component, their neighbors in the original tree may or may not be in the component. So during BFS, when moving to a neighbor, we check if it's in the component_set.

But creating a component_set for each component may take O(m) time, where m is the size of the component. Which is acceptable.

But given that component_nodes is a list, converting to a set is O(m) time. For large components (like 2e5 nodes), this could take time. So perhaps, during the BFS traversal for the component, we can track visited nodes, and during the diameter computation, we can use the same approach.

Alternatively, during the initial BFS to collect the component, we can track which nodes are in the component. So, for each node in the component, we can mark it as part of the component (using a visited array).

Wait, but for each group p, the visited array is for that group. So perhaps using a global visited array is possible.

But the code for processing each group p would have:

visited_p = a boolean array of size n, initialized to False.

But for n up to 2e5, creating a new array for each group is O(n) time, which is O(2e5 * 2e4) = 4e9 operations, which is way too slow.

So we need a way to handle visited arrays efficiently.

Alternative approach: use a hash set to track visited nodes for the component.

But even that might be slow. So perhaps, during the BFS for the component, we can collect all the nodes in the component, and during the diameter computation, use a visited dictionary (or a per-component visited array).

Alternatively, during the component collection, we can store the nodes in a list. Then, during the diameter computation, for each step, we check if the neighbor is in the component (using the list, but that's O(m) time for each check). So that's not feasible.

So the correct approach is to create a component_set as a set, which allows O(1) lookups. For example:

component_nodes = list of nodes in the component.

component_set = set(component_nodes)

Then, during BFS for diameter computation, when checking a neighbor, we check if it's in component_set.

Yes, this is manageable.

But building component_set for each component is O(m) time. For large components, this can be expensive. But considering that each component's nodes are part of the group S_p, and for each group p, the sum of m_p is acceptable, this should be manageable.

Now, putting this all together.

But how to handle the primes?

First, the code outline in Python:

Read n.

Read a list of a_i.

Read n-1 edges, build the adjacency list.

Factorize each a_i into primes, store for each node.

Build a dictionary (prime_to_nodes) mapping each prime to a list of nodes.

For each prime p in prime_to_nodes:

   S_p = prime_to_nodes[p]

   if len(S_p) <= 1:

       current_max = max(current_max, len(S_p))  # if len(S_p) is 1, distance is 1.

       continue

   else:

       process the nodes in S_p.

       find all connected components.

       for each component:

           compute its diameter.

           current_max = max(current_max, diameter)

Finally, output current_max if current_max >=1, else 0.

But wait, the problem requires that the GCD is >1. So for a single node, the GCD is a_i, which is >1 if a_i>1. So for S_p with len(S_p) =1, the maximum distance is 1 (node to itself). So in this case, it's a valid pair. But the problem statement says, pairs x and y. So x can be equal to y. So for example, if a_i is 2, then (x,x) is a valid pair with distance 1, and GCD 2>1. So this should contribute to the maximum.

But in the third example, all a_i are 1, so output is 0.

So in the code, for each prime p, even if the group S_p has size 1, then the maximum possible distance is 1 (node to itself). So the current_max should be the maximum of all such possibilities. But in code, for S_p with size 1, the maximum distance is 1.

But when processing S_p with size >=1, the maximum possible distance is the maximum between the diameters of the components and 1 (since a single node can contribute 1).

Wait, no. For example, if S_p has size 2, but the two nodes are in different components (each size 1). Then the maximum distance is 1. So, for each group p, the maximum possible distance is the maximum between the diameters of the connected components and 1 (if any component has at least one node, since the node can form a pair (x,x) with distance 1). But wait, the problem requires that the GCD of the path is >1. For a single node, the GCD is a_i, which must be divisible by p. So if the group S_p is non-empty, then each node in S_p has a_i divisible by p. So the GCD of a single node's path (x,x) is a_i, which is divisible by p>1. So (x,x) is valid, contributing distance 1. Therefore, even if the group has components with only single nodes, the maximum distance for this group is 1.

But when a group has a component of size 2, connected, then the diameter is 2 (distance between the two nodes). So for such a group, the maximum distance is 2.

So, the code needs to consider the maximum between the diameter of the component and 1 (since even if the component's diameter is 1 (two nodes connected, but the distance is 2?), wait, no.

Wait, for a component of size m, the diameter is the maximum distance between any two nodes in the component. For example, a component of size 1 has diameter 1 (distance between the node and itself). A component of size 2 connected by an edge has a diameter of 2 (distance between the two nodes). So, the code for computing the diameter of the component should return the correct value.

But when a component has size 1, the BFS from the node (u) would find that the farthest node is u, with distance 1. Then the BFS from u again would also find distance 1. So the diameter is 1.

If the component has size 2 (connected), the first BFS finds the farthest node as the other node (distance 2). Then BFS from that node finds the farthest node is the first one, distance 2. So the diameter is 2.

So, the code for compute_diameter() as written earlier returns the correct maximum distance in nodes.

So for a component of size 1, the diameter is 1. For a component of size 2 connected, the diameter is 2. For a component of size 3 in a chain (A-B-C), the diameter is 3 (distance between A and C).

So, the code is correct.

Thus, in the code, for each component, compute its diameter and compare with the current_max.

Therefore, the code should process all groups and components, and track the maximum diameter found.

Now, let's code this.

But first, handling the factorization.

Implementing the SPF sieve:

We can precompute the smallest prime factor for each number up to 2e5.

Then, for each a_i, factorize into primes by dividing by the smallest prime factor until 1.

But we need to collect the unique primes.

For example, for a_i=12, the SPF is 2, divide 12 by 2 to get 6. SPF of 6 is 2, divide by 2 to get 3. SPF of 3 is 3. So the primes are 2 and 3.

So, the code for factorization:

def get_primes(x, spf):

   primes = set()

   while x > 1:

       p = spf[x]

       primes.add(p)

       while x % p == 0:

           x = x // p

   return primes

But wait, for x=1, returns empty set.

Thus, for a_i=1, no primes are added.

Now, in code:

n = int(input())

a = list(map(int, input().split()))

edges = [[] for _ in range(n)]

for _ in range(n-1):

   u, v = map(int, input().split())

   u -=1

   v -=1

   edges[u].append(v)

   edges[v].append(u)

# Precompute smallest prime factors (SPF) up to 2e5.

max_a = 2 *10**5

spf = list(range(max_a +1))

for i in range(2, int(max_a**0.5) +1):

   if spf[i] == i:

       for j in range(i*i, max_a+1, i):

           if spf[j] == j:

               spf[j] = i

# Function to get unique primes of x

def get_primes(x):

   primes = set()

   if x ==1:

       return primes

   while x !=1:

       p = spf[x]

       primes.add(p)

       while x % p ==0:

           x = x//p

   return primes

# For each node, get its primes.

primes_list = [get_primes(x) for x in a]

# Build prime_to_nodes dictionary.

from collections import defaultdict

prime_to_nodes = defaultdict(list)

for i in range(n):

   for p in primes_list[i]:

       prime_to_nodes[p].append(i)

max_diameter = 0

# For each prime in prime_to_nodes, process its nodes.

for p, nodes in prime_to_nodes.items():

   m = len(nodes)

   if m ==0:

       continue

   # The maximum possible diameter for this group is at least 1 (if m >=1)

   # But maybe there's a larger one.

   # We need to process connected components.

   # Create a visited array for this group.

   visited = [False]*n

   # Iterate through all nodes in nodes.

   for u in nodes:

       if not visited[u]:

           # BFS to find connected component.

           component = []

           q = deque([u])

           visited[u] = True

           component.append(u)

           while q:

               current = q.popleft()

               for v in edges[current]:

                   if not visited[v] and p in primes_list[v]:

                       visited[v] = True

                       q.append(v)

                       component.append(v)

           # Compute diameter of this component.

           # component is a list of nodes.

           # component_set = set(component)

           # compute diameter.

           if not component:

               continue

           # First BFS to find farthest node.

           start = component[0]

           max_dist = 1

           farthest_node = start

           visited_bfs = {node:False for node in component}

           q = deque([(start, 1)])

           visited_bfs[start] = True

           while q:

               node, dist = q.popleft()

               if dist > max_dist:

                   max_dist = dist

                   farthest_node = node

               for v in edges[node]:

                   if v in component and not visited_bfs[v]:

                       visited_bfs[v] = True

                       q.append( (v, dist +1) )

           # Second BFS from farthest_node.

           max_dist = 1

           visited_bfs = {node:False for node in component}

           q = deque([(farthest_node, 1)])

           visited_bfs[farthest_node] = True

           while q:

               node, dist = q.popleft()

               if dist > max_dist:

                   max_dist = dist

               for v in edges[node]:

                   if v in component and not visited_bfs[v]:

                       visited_bfs[v] = True

                       q.append( (v, dist +1) )

           # Update max_diameter.

           if max_dist > max_diameter:

               max_diameter = max_dist

print(max_diameter if max_diameter >=1 else 0)

Wait, but in this code, the 'component' is a list of nodes. Then, when checking if v is in component, since 'component' is a list, checking 'v in component' is O(m), which is not acceptable for large m.

So, to optimize, we need to create a set for the component to allow O(1) lookups.

So, in the code:

component = list of nodes.

component_set = set(component)

Then, in the BFS steps:

for v in edges[node]:

   if v in component_set and not visited_bfs[v]:

       ...

Yes. So modifying the code:

           component = list(component)

           component_set = set(component)

           # First BFS to find farthest node.

           start = component[0]

           max_dist = 1

           farthest_node = start

           visited_bfs = {node: False for node in component}

           q = deque([(start, 1)])

           visited_bfs[start] = True

           while q:

               node, dist = q.popleft()

               if dist > max_dist:

                   max_dist = dist

                   farthest_node = node

               for v in edges[node]:

                   if v in component_set and not visited_bfs.get(v, False):

                       visited_bfs[v] = True

                       q.append( (v, dist +1) )

           # Second BFS from farthest_node.

           max_dist = 1

           visited_bfs = {node: False for node in component}

           q = deque([(farthest_node, 1)])

           visited_bfs[farthest_node] = True

           while q:

               node, dist = q.popleft()

               if dist > max_dist:

                   max_dist = dist

               for v in edges[node]:

                   if v in component_set and not visited_bfs.get(v, False):

                       visited_bfs[v] = True

                       q.append( (v, dist +1) )

This should reduce the time for checking if a neighbor is in the component.

But in Python, set lookups are O(1), so this is manageable.

But for large components, this code may still be slow. Let's test with the first example.

First example input:

3

2 3 4

Edges between 1-2 and 2-3 (nodes 0,1,2 in 0-based).

For prime 2, the nodes are 0 (a_i=2) and 2 (a_i=4).

The component for prime 2:

nodes 0 and 2. But in the original tree, node 0 is connected to node 1 (a_i=3), which is not in the group. Node 2 is connected to node 1. So the induced subgraph for prime 2 has nodes 0 and 2, but no edges between them. So each is a separate component.

So during processing:

component for 0 is size 1 → diameter 1.

component for 2 is size 1 → diameter 1.

So max_diameter is 1.

Which matches the sample output.

Another sample:

Second input:

3

2 3 4

Edges are 1-3 and 2-3 (nodes 0, 1, 2).

In this case, the tree is 0 connected to 2, and 1 connected to 2.

For prime 2:

nodes 0 and 2.

In the induced subgraph, 0 is connected to 2 (since in the original tree, 0 is connected to 2 (third node?), wait, let's see:

Original edges are between 1-3 and 2-3. Wait, in the input, the edges are:

First edge is 1 and 3 → nodes 0 and 2 (0-based: 1 becomes 0, 3 becomes 2).

Second edge is 2 and 3 → node 1 (2) and node 2 (3).

Wait, no. The input is for 3 nodes. The first edge is 1-3: but in 0-based terms, nodes are 0, 1, 2. So input 1 and 3 would be out of range. Wait, the input is probably 1-based. So in code, after reading u and v, subtract 1 to convert to 0-based.

So the input edges for the second sample:

1 3 → but n=3, so nodes 1 and 3 are out of range. So probably, the input is:

Sample input 2:

3

2 3 4

1 3

2 3

Which in 0-based becomes nodes 0-2 and 1-2.

So the tree is:

0 connected to 2.

1 connected to 2.

So node 2 (a_i=4) is connected to nodes 0 and 1.

For prime 2, the nodes are 0 (a_i=2) and 2 (a_i=4).

In the original tree, node 0 is connected to 2. So in the induced subgraph for prime 2, the component includes both nodes 0 and 2, connected by an edge. So the diameter is 2 (distance between 0 and 2 is 2 nodes). So the output is 2.

Which matches the sample.

But according to the code, when processing the component containing 0 and 2:

start is 0.

First BFS finds that the farthest node is 2, distance 2.

Second BFS from 2 finds the farthest node is 0, distance 2. So max_dist is 2. Thus, the code would set max_diameter to 2.

Which is correct.

So the code should handle this correctly.

But what about the third sample, where all a_i are 1. Then, each node's primes_list is empty. So prime_to_nodes is empty. So the loop over primes does nothing. Thus, max_diameter remains 0, and output is 0.

Which is correct.

So the code seems to handle the sample cases correctly.

Now, let's think about time constraints.

For n=2e5, the code's preprocessing steps (SPF, factorizing each a_i) are O(max_a log log max_a) for SPF sieve, which is manageable.

Factorizing each a_i takes O(log a_i) time per a_i. For 2e5 a_i's, this is O(2e5 * 18) = 3.6e6 steps.

Building the prime_to_nodes dictionary is O(2e5 * 18) = 3.6e6 steps.

Then, for each prime p in prime_to_nodes:

The code processes each connected component by BFS once to collect the component, and then two BFSes for diameter. Each BFS is O(m) steps, where m is the size of the component.

The sum over all primes p of the sum over all components in p of 3m (one for collecting component, two for BFSes) is O(3 * sum_p m_p) = O(3 * 3.6e6) = 1e7 steps.

Which is acceptable for Python's time constraints (4.5 seconds).

But the problem is that in Python, even O(1e8) operations can be tight. But here, it's O(1e7), which is manageable.

But the code can be optimized further.

Some optimizations:

1. Instead of using a dictionary for visited_bfs, use a list and index by node.

But in Python, list lookups are O(1).

But for each component, the nodes are a list. For example, if the component is [5, 100], then visited_bfs is a list where visited_bfs[5] is True, but for nodes not in the component, it's not tracked. But the component's nodes are limited, and during BFS, we only check nodes in the component.

Alternatively, during the component collection, we can track visited using a global visited array for the group p.

But for each group p, the visited array is reused. For example:

visited_p = [False] * n

for u in nodes:

   if not visited_p[u]:

       # BFS and mark visited_p for all nodes in this component.

       ...

So in the code:

max_a = 2 *10**5

...

for p, nodes in prime_to_nodes.items():

   m = len(nodes)

   if m ==0:

       continue

   visited_p = [False]*n

   current_max_p = 0

   for u in nodes:

       if not visited_p[u]:

           # BFS to collect component.

           component = []

           q = deque([u])

           visited_p[u] = True

           component.append(u)

           while q:

               current = q.popleft()

               for v in edges[current]:

                   if not visited_p[v] and p in primes_list[v]:

                       visited_p[v] = True

                       q.append(v)

                       component.append(v)

           # compute diameter.

           component_set = set(component)

           # first BFS.

           start = component[0]

           max_dist = 1

           farthest = start

           visited_bfs = [False] *n

           q = deque([(start, 1)])

           visited_bfs[start] = True

           while q:

               node, dist = q.popleft()

               if dist > max_dist:

                   max_dist = dist

                   farthest = node

               for v in edges[node]:

                   if v in component_set and not visited_bfs[v]:

                       visited_bfs[v] = True

                       q.append( (v, dist +1) )

           # second BFS.

           max_dist = 1

           visited_bfs = [False]*n

           q = deque([(farthest, 1)])

           visited_bfs[farthest] = True

           while q:

               node, dist = q.popleft()

               if dist > max_dist:

                   max_dist = dist

               for v in edges[node]:

                   if v in component_set and not visited_bfs[v]:

                       visited_bfs[v] = True

                       q.append( (v, dist +1) )

           # update current_max_p.

           current_max_p = max(current_max_p, max_dist)

   # update global max_diameter.

   if current_max_p > max_diameter:

       max_diameter = current_max_p

But using a list for visited_bfs and component_set for faster lookups.

But in this code, for each component, visited_bfs is a list of size n, which is O(n) memory. But n is 2e5, which for Python's memory is 2e5 booleans per BFS. But for two BFS steps per component, this could use a lot of memory. For example, for each component, two lists of size 2e5, which is 2*2e5 = 4e5 per component. For 1e4 components, this would be 4e9 elements, which is impossible.

So this approach is not feasible.

Thus, the correct approach is to use a dictionary or a set to track visited_bfs nodes for the component.

But using a dictionary for visited_bfs with keys being the nodes in the component is more efficient.

Alternatively, since the component is a list of nodes, we can create a visited list that only contains those nodes. For example:

visited_bfs = { node: False for node in component }

This is O(m) memory for each component.

But in Python, dictionaries have some overhead. Another approach is to use a set to track visited nodes.

But for each BFS, we need to track which nodes have been visited. Using a set:

visited_bfs = set()

At each step, when visiting a node, add it to the set.

But for the first BFS:

start = component[0]

visited_bfs.add(start)

q = deque([(start, 1)])

max_dist = 1

farthest = start

while q:

   node, dist = q.popleft()

   if dist > max_dist:

       max_dist = dist

       farthest = node

   for v in edges[node]:

       if v in component_set and v not in visited_bfs:

           visited_bfs.add(v)

           q.append( (v, dist +1) )

This way, visited_bfs is a set of nodes visited.

This is O(m) time for each BFS, and the 'in' operation is O(1) because component_set is a set.

Yes, this approach is better, as it uses less memory and is faster.

So modifying the code:

           component_set = set(component)

           # first BFS.

           start = component[0]

           max_dist = 1

           farthest = start

           visited_bfs = set()

           visited_bfs.add(start)

           q = deque([(start, 1)])

           while q:

               node, dist = q.popleft()

               if dist > max_dist:

                   max_dist = dist

                   farthest = node

               for v in edges[node]:

                   if v in component_set and v not in visited_bfs:

                       visited_bfs.add(v)

                       q.append( (v, dist +1) )

           # second BFS.

           max_dist = 1

           visited_bfs = set()

           visited_bfs.add(farthest)

           q = deque([(farthest, 1)])

           while q:

               node, dist = q.popleft()

               if dist > max_dist:

                   max_dist = dist

               for v in edges[node]:

                   if v in component_set and v not in visited_bfs:

                       visited_bfs.add(v)

                       q.append( (v, dist +1) )

This way, the visited_bfs is a set, and checking membership is O(1).

Thus, the code is optimized.

Now, putting it all together.

Final code:

Read the input, precompute SPF, factorize each a_i into primes, build prime_to_nodes.

Process each prime's nodes, find connected components, compute diameters.

Finally, output the maximum diameter.

But there's one more thing: when all primes have components with diameter 1 (like all a_i are primes, and no two nodes share the same prime), then the maximum diameter is 1, which is the correct answer.

But in the first sample, the answer is 1, which is correct.

Another case: if there's a node with a_i=6 (primes 2 and 3). If there's another node with a_i=4 (primes 2), then for p=2, their component may be connected if the nodes are connected in the original tree. So the code should correctly find the diameter.

Thus, the code should handle all cases.

But in Python, for large inputs, the code may be slow due to the use of dictionaries and sets, which have higher overhead.

But given the time constraints (4.5 seconds), and the code's complexity being around O(1e7) operations, it should pass.

Now, the final code.
</think>

```python
import sys
from sys import stdin
from collections import deque, defaultdict

def main():
    sys.setrecursionlimit(1 << 25)
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    edges = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = map(int, stdin.readline().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)
    
    # Precompute smallest prime factors (SPF)
    max_a = 2 * 10**5
    spf = list(range(max_a + 1))
    for i in range(2, int(max_a**0.5) + 1):
        if spf[i] == i:
            for j in range(i*i, max_a+1, i):
                if spf[j] == j:
                    spf[j] = i

    # Function to get unique primes of x
    def get_primes(x):
        primes = set()
        if x == 1:
            return primes
        while x != 1:
            p = spf[x]
            primes.add(p)
            while x % p == 0:
                x //= p
        return primes

    # Get primes for each node
    primes_list = [get_primes(num) for num in a]

    # Build prime_to_nodes dictionary
    prime_to_nodes = defaultdict(list)
    for idx, primes in enumerate(primes_list):
        for p in primes:
            prime_to_nodes[p].append(idx)

    max_diameter = 0

    # Process each prime's nodes
    for p, nodes in prime_to_nodes.items():
        if not nodes:
            continue
        visited = [False] * n
        current_max = 0
        for u in nodes:
            if not visited[u]:
                # BFS to find the component
                component = []
                q = deque([u])
                visited[u] = True
                component.append(u)
                while q:
                    current = q.popleft()
                    for v in edges[current]:
                        if not visited[v] and p in primes_list[v]:
                            visited[v] = True
                            q.append(v)
                            component.append(v)
                if not component:
                    continue
                component_set = set(component)
                # First BFS to find farthest node
                start = component[0]
                max_dist = 1
                farthest = start
                visited_bfs = {start}
                q = deque([(start, 1)])
                while q:
                    node, dist = q.popleft()
                    if dist > max_dist:
                        max_dist = dist
                        farthest = node
                    for v in edges[node]:
                        if v in component_set and v not in visited_bfs:
                            visited_bfs.add(v)
                            q.append((v, dist + 1))
                # Second BFS from farthest
                max_dist = 1
                visited_bfs = {farthest}
                q = deque([(farthest, 1)])
                while q:
                    node, dist = q.popleft()
                    if dist > max_dist:
                        max_dist = dist
                    for v in edges[node]:
                        if v in component_set and v not in visited_bfs:
                            visited_bfs.add(v)
                            q.append((v, dist + 1))
                current_max = max(current_max, max_dist)
        if current_max > max_diameter:
            max_diameter = current_max

    print(max_diameter if max_diameter >= 1 else 0)

if __name__ == "__main__":
    main()
```