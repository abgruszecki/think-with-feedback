<think>
Okay, so I need to solve this problem where after each step of removing a vertex, I have to compute the sum of all pairs of shortest paths for the remaining vertices. Hmm. Let's think about this.

The problem says that each time before removing the next vertex, we calculate the sum of all d(i, v, u) where v and u are in the remaining graph. Then we remove the vertex. The order of removals is given as x1 to xn. But wait, the initial step is before deleting x1, the graph is complete. Then after deleting x1, the remaining graph is all except x1, and so on until the last step where all are deleted except xn, which is then deleted as the last step. Wait no, the input is n vertices to delete in order. So the first step is to compute the sum before the first deletion, then delete x1. Then compute the sum before the second deletion (so the remaining vertices are all except x1, x2?), wait no. Let me check the example.

In the second example input:

2
0 5
4 0
1 2

The output is 9 0. So before the first deletion (x1=1), the sum is the sum of all pairs except same. The graph is both vertices present. So from 1 to 2 is 5, and 2 to 1 is 4. Sum is 5+4=9. Then after deleting 1, the remaining graph is vertex 2, but since there's only one vertex, the sum is 0. Then when deleting 2, but that's the last step.

Wait, but the output has two numbers. The first number is the sum before the first deletion (all vertices present), then before the second deletion (after deleting x1, which was 1, so now the remaining is 2, and deleting it leaves nothing. So the sum before deleting 2 is the sum of the remaining vertices (only 2), which has no pairs, so sum is 0. So the output is 9 0.

So the steps are: before each deletion, including the first one. So for the first step, before deleting x1, all vertices are present. Then x1 is deleted, and for the second step, before deleting x2, the remaining vertices are all except x1, and x2 is the next to delete. Wait no, the x's are the sequence of deletions. So the process is: before step i, the sum is computed for the current graph, which includes all vertices except the ones deleted in the previous i-1 steps. Then, the i-th step is to delete xi. So after all n steps, all vertices are deleted.

So the output has n numbers. The first is the sum before deleting x1, when all vertices are present. The second is the sum before deleting x2, when the graph has all vertices except x1. The third is sum before deleting x3, with graph having all except x1, x2, and so on. The last output is sum before deleting xn, when the graph has only xn left, so the sum is zero.

So the key is that the order in which vertices are deleted is given, and after each deletion, the next step's sum is computed on the remaining graph.

But computing the sum after each deletion step by step seems computationally expensive. Because for each step, the graph is losing a vertex, and we have to compute the all-pairs shortest paths (APSP) for the remaining graph each time. If we do this naively, with Floyd-Warshall each time, it would be O(n^3) per step, leading to O(n^4) total time, which is way too slow for n=500 (500^4 is 6.25e10 operations, which is way beyond 3 seconds).

So we need a smarter approach.

Wait, but the order of deletions is such that each step removes a vertex. So the process is equivalent to starting with an empty graph and adding the vertices in reverse order of deletion. For example, the first step's sum is when all vertices are present. Then after deleting x1, the sum is for all except x1. Then after deleting x2, sum is all except x1 and x2. So the process is the same as building the graph by adding vertices in the reverse order of deletion. So the last step (the nth) in the problem corresponds to the sum when all vertices except the first n-1 deletions are present. But wait, the last step's sum is before deleting xn, which is the only vertex left, so sum is zero.

So the approach is to reverse the order of deletions. Instead of removing vertices one by one, we can start from an empty graph and add them back in reverse order. Then, for each addition, we can update the APSP for the new vertex. This is a common technique in problems where elements are removed incrementally, but it's easier to reverse the process and add them in reverse order.

So here's the idea: the first time in the original problem (before any deletions) corresponds to the full graph. The second sum corresponds to the full graph minus x1. And so on. The last sum is the sum for the graph with just xn (but the sum is zero). So if we reverse the order of deletions, and process them in reverse, adding the vertices one by one, then each step corresponds to a sum after adding a new vertex. Then the output can be stored in reverse order and reversed at the end.

For example, consider the second sample input where the deletion order is [1,2]. Reversing gives [2,1]. So we start with an empty graph. Then add 2, but there's only one node, sum is 0. Then add 1: the sum is the sum of 1<->2 and 2<->1, which is 5+4=9. Then the output would be [0,9], but since we process in reverse, we need to reverse the output to get [9,0], which matches the sample.

So by reversing the deletion order and adding the vertices step by step, we can compute the sum incrementally.

The key advantage is that when adding a new vertex, we can update the APSP efficiently. The standard approach for dynamic APSP with vertex additions is to use Floyd-Warshall in reverse. When adding a new vertex k, we can consider it as a new intermediate node in the Floyd-Warshall algorithm. Since the existing distances are already computed for the current graph (without k), adding k allows paths that go through k. So for each pair of nodes u and v in the current graph (including k), the new distance is the minimum of the existing distance and the path u -> k -> v. But since k is the newly added node, the existing graph's distances do not include k as an intermediate, so after adding k, we need to run the Floyd-Warshall step for k as the intermediate node.

Wait, Floyd-Warshall's approach is to compute shortest paths considering all possible intermediate nodes up to k. So adding a node in reverse order would correspond to allowing that node as an intermediate. So when we add a new node k to the existing graph, we can update all pairs (i, j) by checking if the path i -> k -> j is shorter than the current distance between i and j. But since the existing graph's distance matrix already includes all the previous nodes (those added so far), adding k and considering it as an intermediate node would allow all paths that go through k.

So the process is as follows:

1. Reverse the order of deletions. For example, the original deletion order is x1, x2, ..., xn. So the reversed order is xn, xn-1, ..., x1.

2. We start with an empty graph and add the vertices in reversed order. So the first added vertex is xn, then xn-1, ..., x1.

3. For each step after adding a vertex, we need to compute the sum of all pairs of shortest paths in the current graph.

4. To compute the sum efficiently, we can maintain a distance matrix that is updated incrementally as each vertex is added. Each time a new vertex k is added, we update the distance matrix by considering k as an intermediate node and also include all edges to and from k.

So here's the plan:

- Initialize the distance matrix as empty.

- For each vertex in reversed deletion order (let's say, processing in the order k1, k2, ..., kn):

   a. Add vertex k to the graph. The current graph includes all previously added vertices plus k.

   b. For each existing node u in the graph (including k), add the edges from u to k and from k to u. Wait, but when adding k, all possible edges between k and existing nodes are present. Because in the original graph, every pair of vertices has edges in both directions. So when adding k, all edges to and from k and the existing nodes are part of the graph.

   So when adding k, the edges between k and all existing nodes are now part of the graph.

   However, the weights for these edges are given by the original adjacency matrix. For example, the edge from existing node u to k has weight a_uk, and the edge from k to u has weight a_ku.

   So when adding k, we need to initialize the distance between k and all existing nodes (u) as a_ku (from k to u), and a_uk (from u to k). Also, the distance between each existing node u and v is already computed, but we need to check if using k as an intermediate can provide a shorter path between u and v.

   So the process is:

   - The current distance matrix (before adding k) contains all pairs of existing nodes (those added before k). When adding k, we need to:

      i. Add k to the distance matrix. Initialize all distances from k to existing nodes as the original edge weights, and existing nodes to k as their original edge weights. Also, the distance from k to itself is zero.

      ii. For all pairs (i, j) in the current graph (including k), check if going through k gives a shorter path. Since k is newly added, the Floyd-Warshall approach would consider k as the intermediate node. So for all i and j, the new distance is min(d[i][j], d[i][k] + d[k][j]).

      iii. Additionally, for all existing nodes u and v, their existing distance is already the shortest path without using k. So after adding k, we need to run the Floyd-Warshall step for the new node k as the intermediate. That is, for all i and j, d[i][j] = min(d[i][j], d[i][k] + d[k][j]).

      iv. Also, for all pairs involving k (i=k or j=k), the initial values are the direct edges, and then after considering all possible intermediates (including other nodes), we can update those distances.

   But how to structure this efficiently?

   Let's think of the reversed order. We have a list of vertices to add: say, [k_1, k_2, ..., k_n], where k_1 is the last vertex to be deleted in the original order, and k_n is the first to be deleted.

   When processing k_i, the current graph consists of vertices {k_1, k_2, ..., k_i}.

   So when we add k_i to the existing graph (which had k_1 to k_{i-1}), we need to compute the new APSP for the graph with k_i added.

   The steps to compute this would be:

   1. Initialize the new distance matrix by adding the new node and all edges to/from existing nodes.

   2. For all existing nodes u in the current graph (before adding k_i), their edges to and from k_i are added. The direct edges between k_i and existing u are a_uk_i (from u to k_i) and a_k_iu (from k_i to u).

   3. Then, for all pairs of nodes (including the new k_i), we need to update the distances considering k_i as an intermediate node.

   Wait, perhaps using the Floyd-Warshall approach in reverse. Because when adding a new node, we can treat it as the next intermediate node in Floyd-Warshall's algorithm. So the standard Floyd-Warshall algorithm processes intermediate nodes in order, and for each k, updates all pairs (i, j) by considering paths that go through k. But since we are adding nodes in a certain order, each time adding a new node, we can run the Floyd-Warshall steps for that new node.

   So here's the approach:

   - Initially, the distance matrix is empty.

   - For each new node k in reversed deletion order:

      a. Add k to the graph.

      b. Initialize the distance from k to all other existing nodes (if any) as the direct edge from k to them (from the adjacency matrix). Similarly, initialize the distance from existing nodes to k as their direct edges.

      c. For the existing nodes (those already added), update their distances to each other by considering paths that go through k. That is, for each i and j in the current graph (including k), check if i -> k -> j is a shorter path.

      d. Also, update the distances between existing nodes and k, and k and existing nodes. For example, for each existing node u, check if u -> existing node v -> k gives a shorter path to k, etc.

   Wait, perhaps the correct approach is to run three nested loops: for each k in the reversed order, when adding it, run Floyd-Warshall's step where k is the intermediate node, but considering all nodes that are already present.

   So, the order in which intermediates are considered in Floyd-Warshall is the reversed deletion order. So each time we add a new node, we run the Floyd-Warshall step for that node as the intermediate.

   Let me see:

   In standard Floyd-Warshall, the order of intermediates is 1..n, and the distance matrix is updated for each k as the intermediate. For our problem, the order in which intermediates are processed is the reversed deletion order. So when adding the nodes in order k_1, k_2, ..., k_n, each time adding k_i, we run the Floyd-Warshall step for all existing nodes, using k_i as the intermediate.

   So the algorithm would be:

   reversed_order = reversed(deletion_order)

   for k in reversed_order:
       add k to the graph
       initialize the distance matrix for all pairs involving k (direct edges)
       for i in all nodes in the graph (including k):
           for j in all nodes in the graph (including k):
               distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

   But wait, when we add k, the graph includes all nodes added so far (k_1, ..., k_i). So for each new node k, after initializing the direct edges, we need to run the Floyd-Warshall step for this new k as the intermediate. This way, all existing pairs can use the new node as an intermediate, potentially reducing their distance.

   But since the existing graph's distance matrix already includes all the previous intermediates (nodes added before k), adding the new node and running the Floyd-Warshall step for k will allow all pairs to use k as an intermediate.

   So this approach should correctly compute the APSP for the graph after each addition.

   Let's think about how this works step by step.

   For example, consider adding the first node k. The graph has only k, so the distance matrix is just 0. Sum is 0.

   Adding the second node m. We initialize distance[m][k] as a_mk, distance[k][m] as a_km. Then, for all i and j (which are m and k), check if i -> m -> j is better. But since m is the intermediate, the Floyd step for m would update:

   For i = m, j = k: d[m][k] = min( a_mk, d[m][m] + d[m][k] ) → a_mk.

   For i = k, j = m: d[k][m] = min( a_km, d[k][m] + d[m][m] ) → a_km.

   For i = k, j = k: remains 0.

   For i = m, j = m: remains 0.

   Then, for the other pairs (k and m), there's no other intermediates, so the initial edges are correct. Then, when the sum is computed, it's the sum of all pairs (k and m) which is a_km + a_mk.

   Then adding the third node l. Initialize all edges between l and existing nodes (k and m). For each existing node u (k and m), set d[l][u] = a_lu, d[u][l] = a_ul. Also, d[l][l] = 0.

   Then, run the Floyd step for l as the intermediate. For all i and j (now k, m, l), check if d[i][j] can be improved by going through l. So for each pair i, j, d[i][j] = min( current d[i][j], d[i][l] + d[l][j] )

   But since i and j are in the existing nodes (k, m) plus l, this would allow paths that go through l. For example, if there's a path from k to l to m which is shorter than the direct edge from k to m.

   So each time a new node is added, the Floyd step for that node as the intermediate is run. This should capture all possible paths that go through the new node.

   So this approach is O(n^3) total time. Since for each of the n steps (adding each node in reversed order), we run O(n^2) operations (for all i and j). Because when adding the k-th node, there are k nodes in the graph. For each addition, the nested loops for i and j would be O(k^2), but since over all additions, the sum of k^2 from 1 to n is O(n^3), the total time is O(n^3), which is acceptable for n=500 (500^3 is 125e6, manageable within 3 seconds).

   Then, after each addition, we compute the sum of all pairs (i, j) where i and j are present in the current graph, i != j. This sum is stored in a list, and at the end, we reverse this list to get the answer in the original order.

   So the steps are:

   1. Read n, adjacency matrix, and the deletion order x1, x2, ..., xn.

   2. Reverse the deletion order to get add_order = [x_n, x_{n-1}, ..., x_1].

   3. Initialize a list to store the sum after each addition (sum_list).

   4. Initialize the distance matrix (d) as empty. Since the nodes are added one by one, and each time the nodes are in the add_order up to that point, we can track the current nodes in the graph.

   5. For each step, when adding node k (from add_order):

      a. Add k to the current set of nodes. The current nodes are add_order[0..i], where i is the current step (starting from 0).

      b. Initialize the distance matrix entries for k. For all existing nodes u (those already added before k), set d[u][k] = a[u][k] (from the adjacency matrix), d[k][u] = a[k][u]. Also, d[k][k] = 0.

      Wait, but in the reversed order, the nodes are being added in the order of add_order. So when adding k, which is the next in add_order, the existing nodes are the ones added before (earlier in add_order). So for each u in the current graph (before adding k), which are the nodes in add_order up to the previous step, we need to set d[k][u] and d[u][k] based on the adjacency matrix.

      Wait, but the nodes in the original graph are numbered from 1 to n. So when we add a node, say k = x_n (the last to be deleted in the original order), then when added first, it's part of the initial graph.

      So in the code, the nodes are stored as a list, and each time a new node k is added, we need to initialize all the distances between k and existing nodes.

      So for the new node k:

      For each existing node u in the current graph:

          d[k][u] = adjacency[k-1][u-1]  # since Python uses 0-based indices, but the problem uses 1-based.

          d[u][k] = adjacency[u-1][k-1]

      Also, d[k][k] = 0.

      Then, after initializing these, run the Floyd-Warshall step for the new node k as the intermediate. So for all i in current nodes (including k), and j in current nodes (including k), check if d[i][j] can be improved by going through k.

      So the code would look something like:

      current_nodes = [ ... ]  # list of nodes added so far, including k.

      for i in current_nodes:
          for j in current_nodes:
              if d[i][j] > d[i][k] + d[k][j]:
                  d[i][j] = d[i][k] + d[k][j]

      But wait, the order of i and j is irrelevant here, since we're checking all pairs.

      So the algorithm for adding a node is:

      - Add the node to the current set.

      - Initialize the distances between this node and all existing nodes as per the adjacency matrix.

      - Then, for all pairs of existing nodes (including the new one), update their distances using the new node as an intermediate.

      This way, all possible paths that go through the new node are considered.

      Now, for the data structures, how to represent the current nodes and the distance matrix?

      Since the nodes can be added in any order (the reversed deletion order), we can track the current nodes as a list. For the distance matrix, since the nodes are added in a specific order, and each new node is added to the list, the indices can be tricky. Alternatively, we can use a dictionary or a 2D array where the indices correspond to the node labels. But for n=500, a 500x500 array is manageable. However, since the nodes added are not necessarily in order 1..n, but in the reversed deletion order, we need to track which nodes are present.

      So perhaps the best approach is:

      - Use a list called 'nodes' which holds the nodes added so far, in the order they were added.

      - For the distance matrix, we can use a dictionary where d[i][j] gives the distance from node i to node j. But for speed, using a 2D array would be better. But since node labels can be up to 500, a 501x501 array (since nodes are 1-based) would be sufficient.

      Wait, but the nodes added are not necessarily consecutive. For example, the reversed deletion order could be [4,1,2,3], so when adding 4, then 1, etc.

      So, when adding a new node k, we need to initialize the distances between k and all existing nodes. The existing nodes are those in the 'nodes' list up to the current step.

      So, for the distance matrix, perhaps a 2D array (d) of size (n+1) x (n+1) (since nodes are numbered from 1 to n) is suitable. We can initialize all distances as infinity, except for d[i][i] = 0. Then, when adding a new node k, for each existing node u in 'nodes', set d[k][u] = adjacency[k-1][u-1], and d[u][k] = adjacency[u-1][k-1]. Then, run the Floyd step for k as intermediate.

      Wait, but when a new node is added, the existing nodes are those in the 'nodes' list. So the 'nodes' list is built as we go. For example, after adding the first node (k1), the list is [k1]. Then after adding the second (k2), the list is [k1, k2], etc.

      So for each step, when adding node k, the existing nodes are those in the list before adding k. Then, after adding k, the list includes k.

      Wait, no. For the first addition, the list starts empty. Then add k1, the list is [k1]. For the next step, add k2, list becomes [k1, k2], etc.

      So, during the process of adding a new node k:

      1. Add k to the list of nodes.

      2. For all existing nodes in the list (including the new k), update the distances.

      Wait, but the existing nodes are those that were added before this step, right? Or does the list include the new node? Because after adding k, the list includes k. So for the initial step:

      When adding k1, the list is [k1]. Then, for all pairs in the list (only k1), the distance is zero.

      Then, when adding k2, the list becomes [k1, k2]. For this step, the existing nodes before adding k2 are [k1], and after adding k2, the nodes are [k1, k2].

      So during the adding process, when we add a new node k, the existing nodes are those already in the list, and the new node is added to the list.

      So the code would be:

      nodes = []
      for k in add_order:
          nodes.append(k)
          # Now, initialize distances between k and existing nodes (those in nodes[:-1])
          for u in nodes[:-1]:
              d[k][u] = adj[k][u]
              d[u][k] = adj[u][k]
          d[k][k] = 0
          # Then, run the Floyd step for k as intermediate
          for i in nodes:
              for j in nodes:
                  if d[i][j] > d[i][k] + d[k][j]:
                      d[i][j] = d[i][k] + d[k][j]

      But this would miss some paths. Because when adding k, the existing nodes include all previous nodes and k. The loop for i and j runs through all nodes in the current list (including k). For each pair (i, j), the distance is updated to see if going through k (the new node) is better.

      However, during the initial adding of k, the Floyd step would process all pairs (i, j) in the current nodes. So, for example, when adding the second node, the loop runs i and j over both nodes. For each pair (i,j), check if i to k plus k to j is shorter.

      This should correctly update the distances.

      Now, the sum of all pairs after each addition. After each step (adding a node), the current graph consists of the nodes in 'nodes', and we need to sum all d[i][j] for i != j.

      So the sum can be computed as follows:

      sum_val = 0
      for i in nodes:
          for j in nodes:
              if i != j:
                  sum_val += d[i][j]
      sum_list.append(sum_val)

      But this is O(k^2) per step, where k is the number of nodes added so far. For n=500, the total sum over all steps is O(n^3), which is acceptable.

      Now, the initial distance matrix is filled with INF, except for d[i][i] = 0. But when adding a new node k, for existing nodes u (already in the list before adding k), the distances from u to k and vice versa are initialized to the adjacency values. Then, during the Floyd step, those distances may be updated.

      For example, when adding node k2 after k1, the initial distances are:

      d[k1][k2] = adj[k1-1][k2-1]
      d[k2][k1] = adj[k2-1][k1-1]

      Then during the Floyd step, for i = k1, j = k2:

      d[k1][k2] is compared to d[k1][k2] + d[k2][k2] (which is the same as d[k1][k2]), so no change.

      But for i = k1, j = k2, during the Floyd step for intermediate k2:

      d[i][j] = min(d[i][j], d[i][k2] + d[k2][j])

      Wait, but the intermediate is k2, which is the current node being added. So during the Floyd step, for all pairs (i, j), the code is checking if i -> k2 -> j is better. But in this case, j is any node, including k2.

      Hmm, perhaps this is not sufficient. Because when adding k2, the existing nodes are k1 and k2. So the Floyd step for intermediate k2 would check all pairs (i, j) in the current nodes. For example, the pair (k1, k2) would be checked against k1 -> k2 -> j, but j is k2. So d[i][j] is min(adj[k1][k2], adj[k1][k2] + 0) → same. But other pairs may have their distances updated.

      Wait, maybe this approach is sufficient. Let's take the example where after adding k1 and k2, their initial distances are a_k1k2 and a_k2k1. Then, during the Floyd step for intermediate k2, we check all pairs (i, j). For example, i = k1, j = k2:

      d[i][j] is a_k1k2.

      The path via k2 is a_k1k2 + d[k2][k2] (which is 0). So the new distance is min(a_k1k2, a_k1k2 + 0) → same. So no change.

      But if there is a third node added later, say k3, then during the Floyd step for k3, the code may update distances between existing nodes using k3 as an intermediate.

      So the approach of adding nodes in reversed order and running the Floyd step for each new node as the intermediate is correct.

      Now, how to implement this in code.

      First, read the input:

      Read n.

      Then read n lines, each with n integers. The adjacency matrix. Note that the problem uses 1-based indices for the vertices, but in Python, we'll store them as 0-based in the adjacency matrix. So adj[i][j] is the weight from vertex (i+1) to (j+1).

      Then read the deletion order x1, x2, ..., xn. These are 1-based. For example, x1=1 refers to vertex 1.

      Reverse the deletion order to get add_order.

      Now, initialize the distance matrix. Since n can be up to 500, a 501x501 matrix (since vertices are 1-based) filled with infinity, and d[i][i] = 0.

      However, since we're adding nodes incrementally, perhaps it's better to initialize all distances as infinity, and then when adding a node, set the necessary entries.

      But in code, the distance matrix can be represented as a 2D list of size (n+1) x (n+1). Initially, all values are set to infinity. For each node, d[i][i] is 0.

      So in Python:

      INF = float('inf')

      n = int(input())
      adj = []
      for _ in range(n):
          row = list(map(int, input().split()))
          adj.append(row)
      deletion_order = list(map(int, input().split()))
      add_order = list(reversed(deletion_order))

      # Initialize distance matrix
      d = [[INF] * (n+1) for _ in range(n+1)]
      for i in range(n+1):
          d[i][i] = 0

      sum_list = []
      current_nodes = []

      for k in add_order:
          # Add k to current_nodes
          current_nodes.append(k)

          # Initialize distances between k and existing nodes (those added before)
          # existing_nodes is current_nodes[:-1]
          for u in current_nodes[:-1]:
              # u is already in the graph, now adding k.
              # distance from k to u is adj[k-1][u-1]
              d[k][u] = adj[k-1][u-1]
              # distance from u to k is adj[u-1][k-1]
              d[u][k] = adj[u-1][k-1]

          # Now, run the Floyd-Warshall step for intermediate k.
          for i in current_nodes:
              for j in current_nodes:
                  # Check if i -> k -> j is better
                  if d[i][k] + d[k][j] < d[i][j]:
                      d[i][j] = d[i][k] + d[k][j]

          # Compute the sum of all pairs in current_nodes
          total = 0
          for i in current_nodes:
              for j in current_nodes:
                  if i != j:
                      total += d[i][j]
          sum_list.append(total)

      # The sum_list is in the order of the reversed deletions. So the original problem's output is the reverse of sum_list.
      # Wait no. Let's see.

      In the original problem:

      The output is the sum before each deletion step.

      For example, after adding all nodes in add_order (which is reversed deletion order), the sum_list would be:

      sum_list[0] is sum after adding add_order[0] (the first node, which is xn).

      sum_list[1] is sum after adding add_order[1] (xn-1), etc.

      sum_list has n elements. The first element is sum when the graph has only xn, which is 0. The second is sum when the graph has xn and xn-1, etc. The last element is sum when all nodes are added, which is the first sum in the original problem.

      So the output of the original problem is sum_list reversed.

      So after building sum_list, the answer is sum_list reversed. For example, in the second sample input, sum_list would be [0,9], reversed to [9,0], which matches the sample output.

      So the code should reverse sum_list and print the elements space-separated.

      Thus, the final code would be:

      print(' '.join(map(str, reversed(sum_list))))

      But wait, what about the sample input where n=1? The add_order is [1], sum_list is [0], reversed gives [0], which matches the output.

      Now, the code.

      But there's a problem here: when initializing the distance between existing nodes and the new node k, the existing nodes are those added before k. So when adding k, current_nodes is [prev_nodes..., k]. So for u in current_nodes[:-1], which are the nodes added before k.

      But in code, for each k in add_order:

          current_nodes.append(k)

          for u in current_nodes[:-1]:
              d[k][u] = adj[k-1][u-1]
              d[u][k] = adj[u-1][k-1]

      So for u in current_nodes[:-1], which are the nodes added before the current step. This is correct.

      Then, after initializing these edges, run the Floyd step for all pairs (i, j) in current_nodes, using k as intermediate.

      Then compute the sum.

      Now, the initial distance matrix is set to INF. But for the nodes not yet added, their distances are not considered. Because current_nodes only contains the nodes added so far.

      So during the Floyd step, for i and j in current_nodes (all nodes added up to now), the code iterates over those i and j.

      Now, the code for the sum is:

          total = 0
          for i in current_nodes:
              for j in current_nodes:
                  if i != j:
                      total += d[i][j]

      But d[i][j] can be INF? No, because all nodes added so far are part of the graph, which is a complete graph. So there is a direct edge between any pair of nodes. So after initializing the edges and running the Floyd step, the distances should be valid.

      Wait, but in the initial step when adding the first node (k), the sum is 0 (since i and j are same). So correct.

      Then when adding the second node (m), sum is d[k][m] + d[m][k], which are the edges between them, possibly updated by the Floyd step. But since there are no other intermediates, those are the direct edges.

      So the code should work.

      Now, for the sample input:

      Sample 3:

      Input:

      4
      0 3 1 1
      6 0 400 1
      2 4 0 1
      1 1 1 0
      4 1 2 3

      The deletion order is [4,1,2,3]. So reversed add_order is [3,2,1,4].

      Let's see:

      The code adds 3 first. sum is 0.

      Then adds 2. Now the nodes are [3,2]. Initialize d[2][3] = adj[2-1][3-1] = 400. d[3][2] = adj[3-1][2-1] =4. Then run Floyd step for intermediate 2. So for i in [3,2], j in [3,2]:

      For i=3, j=2: d[3][2] is 4. Check if d[3][2] > d[3][2] + d[2][2] → 4+0=4. No change.

      For i=2, j=3: d[2][3] is 400. Check if d[2][3] > d[2][2] + d[2][3] → 0 +400=400. No change.

      Sum is 4+400 =404. But according to the sample output, the third step's sum is 404. But this is the sum after adding 2 nodes (3 and 2) in the reversed order. Wait, the sample's add_order is reversed deletion order [4,1,2,3] → reversed is [3,2,1,4]. So sum_list would be:

      after adding 3: sum is 0 → sum_list[0] =0

      after adding 2: sum is 4+400=404 → sum_list[1] =404

      after adding 1: sum is computed for 3,2,1.

      Then after adding 4, sum is computed for all four.

      Then sum_list is [0,404, ...], but the sample's output has the third entry as 404. But the sample input's output is:

      17 23 404 0 → which when reversed is [0,404,23,17]. So sum_list would be [0,404,23,17], and when reversed, gives the sample output.

      So the code seems to correctly compute the sum for the intermediate steps.

      Now, possible edge cases:

      - All edges are zero? No, the problem says aii=0, but other edges can be 1.

      - All edges have the same weight except for a few.

      But the code should handle all cases.

      Now, for the data structure, the distance matrix uses (n+1) x (n+1), which is manageable for n=500.

      Now, the code needs to be written.

      Also, in Python, for handling large numbers, but since the sum can be up to 500*500*1e5 = 2.5e10 per step, multiplied by n steps, it can be up to 1.25e13, which fits in Python's integers.

      Now, code:

      Read n.

      Read the adjacency matrix.

      Read the deletion order, reverse it to get add_order.

      Initialize d as a 2D list of (n+1) x (n+1) filled with INF, and d[i][i] =0.

      current_nodes = list to keep track of added nodes.

      sum_list = empty list.

      For each k in add_order:

          add to current_nodes.

          for each existing node u in current_nodes[:-1]:

              d[k][u] = adj[k-1][u-1]

              d[u][k] = adj[u-1][k-1]

          then run Floyd step for intermediate k:

              for i in current_nodes:

                  for j in current_nodes:

                      if d[i][j] > d[i][k] + d[k][j]:

                          d[i][j] = d[i][k] + d[k][j]

          compute the sum and append to sum_list.

      Then reverse sum_list and print.

      Wait, but when reversed, the first element of sum_list (sum after adding first node) becomes the last element of the output, which is correct.

      Let me see for the sample input 2:

      add_order is [2,1].

      sum_list after processing:

      after adding 2: sum is 0 → sum_list = [0]

      after adding 1: sum is 5+4=9 → sum_list = [0,9]

      reversed sum_list → [9,0], which matches the sample output.

      So code is correct.

      Now, the code in Python:

      But wait, for the current_nodes list, when adding k, existing nodes are those in current_nodes[:-1]. Because current_nodes is being appended with k.

      So during the loop for u in current_nodes[:-1], which is all elements except the last one (the new k).

      Now, the code:

      n = int(input())
      adj = []
      for _ in range(n):
          row = list(map(int, input().split()))
          adj.append(row)
      deletion_order = list(map(int, input().split()))
      add_order = list(reversed(deletion_order))

      INF = float('inf')
      d = [[INF] * (n + 1) for _ in range(n + 1)]
      for i in range(n + 1):
          d[i][i] = 0

      current_nodes = []
      sum_list = []

      for k in add_order:
          current_nodes.append(k)
          # Initialize edges between k and existing nodes
          # existing nodes are current_nodes[:-1]
          for u in current_nodes[:-1]:
              # from k to u: adj[k-1][u-1]
              d[k][u] = adj[k-1][u-1]
              # from u to k: adj[u-1][k-1]
              d[u][k] = adj[u-1][k-1]
          # Run Floyd-Warshall step for intermediate k
          for i in current_nodes:
              for j in current_nodes:
                  if d[i][j] > d[i][k] + d[k][j]:
                      d[i][j] = d[i][k] + d[k][j]
          # Compute sum
          total = 0
          for i in current_nodes:
              for j in current_nodes:
                  if i != j:
                      total += d[i][j]
          sum_list.append(total)

      # Reverse the sum_list to get the correct order
      print(' '.join(map(str, reversed(sum_list))))

      Let's test the sample input 2:

      n=2.

      adj = [
          [0,5],
          [4,0]
      ]

      deletion_order is [1,2], so add_order is [2,1].

      Processing k=2:

      current_nodes becomes [2]. Initialize edges between 2 and existing nodes (none). Then run Floyd step. Then sum is 0.

      sum_list appends 0.

      Next, k=1:

      current_nodes becomes [2,1]. existing nodes are [2].

      For u=2:

          d[1][2] = adj[0][1] =5.

          d[2][1] = adj[1][0] =4.

      Then run Floyd step for intermediate 1:

          for i in [2,1], j in [2,1]:

              check if d[i][j] > d[i][1] + d[1][j]

              For i=2, j=2: d[2][2] is 0. No change.

              i=2, j=1: d[2][1] is 4. Compare with d[2][1] + d[1][1] (4+0=4) → no change.

              i=1, j=2: d[1][2] is5. Compare with d[1][1] + d[1][2] →0+5=5 → no change.

              i=1, j=1: 0.

              i=1, j=2: no change.

              i=2, j=1: no change.

              i=1, j=2: no change.

              So distances remain 4 and5.

          sum is 4+5=9.

          sum_list is now [0,9].

      reversed sum_list is [9,0], which matches the sample.

      Another sample:

      sample 3:

      add_order is [3,2,1,4].

      The deletion order is 4,1,2,3. Reversed is 3,2,1,4.

      So the code processes adding 3, then 2, then 1, then 4.

      Let's see after adding 3: sum is 0.

      Then adding 2:

          current_nodes is [3,2].

          Initialize edges between 2 and 3:

              d[2][3] = adj[1][2] =400 (since adj is 0-based, adj[2-1][3-1] = adj[1][2] =400.

              d[3][2] = adj[2][1] =4.

          Then run Floyd step for intermediate 2.

          For i in [3,2], j in [3,2]:

              for i=3, j=2: d[3][2] is4. check if 4 > d[3][2] + d[2][2] →4+0=4 → no change.

              for i=2, j=3: d[2][3] is400. check if 400> d[2][2] +d[2][3] →0+400 → no change.

              other pairs: i=3, j=3 (0), i=2, j=2 (0).

          sum is4+400=404.

          sum_list is [0,404].

      Then adding 1:

          current_nodes is [3,2,1].

          existing nodes are [3,2].

          for u in [3,2]:

              d[1][3] = adj[0][2] =1.

              d[3][1] = adj[2][0] =2.

              d[1][2] = adj[0][1] =3.

              d[2][1] = adj[1][0] =6.

          Then run Floyd step for intermediate 1.

          For all i, j in [3,2,1]:

              For example, i=3, j=2:

                  current d[3][2] is4.

                  check if d[3][2] > d[3][1] + d[1][2] →2+3=5. 4 <5 → no change.

              i=3, j=1: current d[3][1] is2. check if 2> d[3][1] + d[1][1] →2+0=2 → no change.

              i=3, j=3: 0.

              i=2, j=3: d[2][3] is400. check if 400> d[2][1]+d[1][3] →6 +1=7 → yes. So update d[2][3] to7.

              i=2, j=1: d[2][1] is6. check if 6> d[2][1] + d[1][1] →6+0=6 → no change.

              i=1, j=2: d[1][2] is3. check if 3> d[1][1] +d[1][2] →0+3=3 → no change.

              i=1, j=3: d[1][3] is1. check if 1> d[1][3] +d[3][3] →1+0=1 → no change.

              i=2, j=3 is updated to7.

              Also, i=3, j=2:4 is less than d[3][1] +d[1][2]=2+3=5, so no change.

              But for i=2, j=3:7.

              So after this step, d[2][3] is7.

              Also, other pairs may be updated.

              For example, i=3, j=2 is still4.

              So after this step, the distances are:

              Between 3 and 2:4.

              Between 2 and3:7.

              Between 2 and1:6.

              Between 1 and2:3.

              Between3 and1:2.

              Between1 and3:1.

              sum is:

              for all pairs:

                  3-2:4, 2-3:7, 3-1:2, 1-3:1, 2-1:6, 1-2:3.

                  sum:4+7+2+1+6+3=23.

              So sum_list becomes [0,404,23].

              Then adding 4:

                  current_nodes is [3,2,1,4].

                  existing nodes are [3,2,1].

                  for u in [3,2,1]:

                      d[4][u] = adj[3][u-1] ?

                      Wait, k is4, u is3:

                          adj[4-1][3-1] = adj[3][2] =1.

                          So d[4][3] =1.

                          adj[3-1][4-1] = adj[2][3] =1.

                          So d[3][4] =1.

                      u=2:

                          adj[3][2-1] = adj[3][1] =1.

                          d[4][2] =1.

                          adj[2-1][3] = adj[1][3] =1.

                          So d[2][4] =1.

                      u=1:

                          adj[3][0] =1.

                          d[4][1] =1.

                          adj[0][3] =1.

                          So d[1][4] =1.

                  Then, run Floyd step for intermediate4.

                  For all i,j in [3,2,1,4]:

                      Check if i →4 →j is better.

                  For example:

                      i=3, j=2: current distance is4. Check if d[3][4] + d[4][2] =1 +1 =2 <4 → yes. So update to2.

                      i=2, j=3: current distance is7. Check d[2][4] +d[4][3] =1+1=2 <7 → update to2.

                      i=3, j=1: current 2. Check 1 +1=2 → no change.

                      etc.

                  After this step, many distances will be updated.

                  For example, i=3 to j=2 becomes2.

                  i=2 to j=3 becomes2.

                  i=3 to j=4:1.

                  i=4 to j=3:1.

                  i=1 to j=3:1.

                  i=3 to j=1:2.

                  etc.

                  The sum would be calculated as the sum of all pairs in the four nodes.

                  Which for this example is 17.

                  So sum_list becomes [0,404,23,17].

                  Reversed sum_list is [17,23,404,0], which matches the sample output.

      So the code should handle this correctly.

      Now, code looks correct.
</think>

```python
n = int(input())
adj = []
for _ in range(n):
    adj.append(list(map(int, input().split())))
deletion_order = list(map(int, input().split()))
add_order = deletion_order[::-1]

INF = float('inf')
d = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    d[i][i] = 0

current_nodes = []
sum_list = []

for k in add_order:
    current_nodes.append(k)
    for u in current_nodes[:-1]:
        d[k][u] = adj[k-1][u-1]
        d[u][k] = adj[u-1][k-1]
    # Floyd-Warshall step for intermediate k
    for i in current_nodes:
        for j in current_nodes:
            if d[i][k] + d[k][j] < d[i][j]:
                d[i][j] = d[i][k] + d[k][j]
    total = 0
    for i in current_nodes:
        for j in current_nodes:
            if i != j:
                total += d[i][j]
    sum_list.append(total)

print(' '.join(map(str, sum_list[::-1])))
```