<think>
Okay, let's tackle this problem. Hmm. The problem is about a graph where each node has some outgoing edges and a value k_i. We need to determine, for each query starting at a certain node with a starting c value, how many distinct nodes are visited infinitely often during the traversal.

First, let's understand the traversal process. The steps are:

1. Start at node x with initial c = y.
2. Upon arriving at node i, add k_i to c.
3. Choose the next node based on x ≡ c mod m_i. The next node is e_i[x mod m_i], then repeat.

The key is that the traversal can loop infinitely, and we need to find all nodes that are part of this infinite cycle.

So, the challenge is to model the state transitions and detect cycles. But with large constraints (n up to 1000, q up to 1e5), we can't simulate each query directly. We need a way to precompute some information or find patterns.

Let's think about the state. The state is determined by the current node and the value of c. But c can be very large (since each step adds k_i, which can be up to 1e9 in magnitude). So storing all possible states isn't feasible.

Wait, but perhaps there's a cycle in the state transitions. Because when the same (node, c mod m_i) pair repeats, the path from that point will repeat. So for a given node i, the next node depends on c mod m_i. Because when you add k_i to c, the next choice of edge is determined by (c + k_i) mod m_i. Wait, no. Let's see:

The next step's x is (current c) mod m_i. Because when you arrive at node i, you add k_i to c. Then, step 3 says x ≡ c (mod m_i). So after adding k_i, the new c is used to compute x. So x is (c + k_i) mod m_i? No wait, wait. Let me recheck:

No. The process is: arrive at node i. Then, add k_i to c. So step 2 happens, then step 3. So, after arriving at node i, c becomes c_prev + k_i. Then, x is determined as x ≡ c mod m_i. So the next node is e_i[x], where x is (c_prev + k_i) mod m_i. Then, the next step adds k of the next node, and so on.

So the state transitions depend on the current node and the current value of c mod (sum of m_i's?), but that's not straightforward. Wait, but each node i has m_i edges, and the next node is determined by (c mod m_i) when at node i. So for each node i, the possible x values (the edge index) is determined by c mod m_i. So the next node depends on the current node and (c mod m_i).

But c can be any integer. However, perhaps after some steps, the c mod m_i for the nodes involved in a cycle will repeat, leading to a loop.

So, maybe for each possible starting (node, c mod something) pair, there's a cycle that can be precomputed, and the answer is the size of that cycle.

But with n up to 1000 and m_i up to 10, the possible combinations of (current node, c mod LCM of m_i's) could be manageable? But LCM of m_i's up to 10 each is 2520 (since 10's LCM is 2520 for 1..10). Wait, for each node, the modulus is m_i. So when you are at node i, the next edge is chosen based on c mod m_i. So the key is that when the same (node, c mod m_i) is encountered again, the cycle will repeat from there.

But how do these mod values affect the transitions? Let's think: for each node, the c mod m_i determines the next edge. So when moving to another node j, the next step's c mod m_j is determined by (c_prev + k_i) mod m_j. Hmm.

This seems complicated. Let's think of the state as (current node, c mod L), where L is the LCM of all possible m_i's. Since m_i can be up to 10, the LCM of 1 to 10 is 2520. So L is 2520. Because for any m_i, modding c by 2520 will give the same result as modding by m_i. So (c mod 2520) mod m_i is equal to c mod m_i. So if we track c mod 2520, then when at any node i, the x is determined by (c mod 2520) mod m_i. So this reduces the state to (current node, c mod 2520). 

So the state space is n * 2520. For n=1e3, that's 1e3 * 2520 = 2.5e6 possible states. For each state, we can precompute transitions. But for each query, the starting state is (x, y mod 2520). Then, once we enter a cycle in the state transitions, the nodes visited infinitely are those in the cycle.

So the approach could be:

1. Precompute for each possible state (u, c_mod) the next state (v, (c_mod + k_u) mod 2520). Because when you are at node u, with current c_mod, you add k_u, then compute next_c_mod = (c_mod + k_u) mod 2520. Then, the next node is e_u[(c_mod + k_u) mod m_u]. Wait, because the x is (c_mod + k_u) mod m_u. So next node is e_u[ x ], and the next state is (v, next_c_mod).

So the transition function is: from (u, c_mod), compute x = (c_mod + k_u) mod m_u. Then, next node is e_u[x], and next c_mod is (c_mod + k_u) mod 2520.

Thus, each state (u, c_mod) leads to a unique next state (v, next_c_mod). Since each state has exactly one next state, the entire state space forms a collection of cycles and trees leading into cycles. So for each state, once it starts, it eventually enters a cycle.

For any starting state (x, y_initial), the traversal will eventually loop in a cycle. The nodes that are visited infinitely often are exactly the nodes in that cycle.

So for each query, we can model it as starting at (x, (y_initial) mod 2520). Then, simulate the path until a cycle is detected. The nodes in the cycle are the ones visited infinitely. But simulating for each query would be too slow for q=1e5. So we need to precompute for each state (u, c_mod) the cycle information: the set of nodes in the cycle that starts from (u, c_mod).

But precomputing all possible 2.5e6 states and their cycles is feasible. Then, each query can be answered in O(1) by looking up the precomputed answer for (x, (y_initial) mod 2520).

So the plan is:

- For each state (u, c_mod), precompute the cycle nodes and cache the count.

But how to compute this efficiently for all states?

We can perform a depth-first search (DFS) or BFS for each state, tracking visited states until a cycle is found. However, with 2.5e6 states, doing this naively could be O(n * 2520) * O(cycle length), which might be acceptable as 2.5e6 is manageable.

Alternatively, since each state has exactly one next state, the transitions form a directed graph where each node (state) has exactly one outgoing edge. So the entire graph is a collection of cycles and trees leading into cycles. Therefore, for each state, once we find the cycle it's part of, we can store the set of nodes in that cycle.

But even this, how to compute it efficiently?

We can iterate through each state. For each state that hasn't been processed yet, we follow the transitions until we find a state that has been visited before. If during this traversal, we encounter a state that is part of a cycle, we can then backtrack and assign the cycle's node set to all states in the cycle. For the states in the path leading into the cycle (the tree part), their cycles would be the same as the cycle they eventually enter.

Wait, but for the states in the tree part leading into the cycle, when you start from them, you'll eventually reach the cycle. So the nodes visited infinitely often are those in the cycle. So for those states, the answer is the size of the cycle they enter. For states that are in a cycle themselves, the answer is the size of their own cycle.

Therefore, for each state, the answer is the number of unique nodes in the cycle that it eventually enters.

So the key is to precompute for each state (u, c_mod), the set of nodes in the cycle that the traversal from (u, c_mod) will enter.

The steps could be:

1. Precompute for each state (u, c_mod) the next state (v, next_c_mod) as described.

2. For each state, determine which cycle it belongs to. For all states in a cycle, compute the set of nodes in the cycle and the count.

3. For all states not in a cycle but leading into one, their answer is the same as the cycle they eventually reach.

But how to efficiently compute this for all 2.5e6 states?

We can use a union-find (disjoint set) data structure, but since each state points to exactly one next state, the cycles can be found by tracking visited states. Alternatively, perform a traversal for each unvisited state, tracking the path until a cycle is found. Then, for all states in the path before the cycle, their answer is the cycle's node set. For the states in the cycle, the answer is the cycle's node set.

Wait, here's a standard way to process each state:

- For each state, if it's not visited, traverse the next pointers until we find a state that is already visited. If during traversal, we hit a state that is part of the current path, we have found a cycle. Then, all states in the cycle contribute their nodes, and the path leading into the cycle do as well, but their infinitely visited nodes are those in the cycle.

Wait, no. Once you start at a state S, you follow transitions until you reach a cycle. Once in the cycle, the traversal will loop infinitely. So the nodes visited infinitely often are those in the cycle. The nodes in the path leading into the cycle are only visited once. So for state S, the answer is the number of distinct nodes in the cycle that S eventually enters.

So the approach is:

For each state, find the cycle that is reachable from it. Then, collect all nodes in that cycle and count the distinct ones.

To precompute this, for each state, we can:

1. Follow transitions until we find a state that has already been processed. If during the traversal, we detect a cycle (i.e., a state is visited twice), then we can process that cycle.

But this approach might be time-consuming for each state, leading to O(2.5e6 * cycle_length) time. That's probably not feasible.

Alternative idea: since the transitions form a DAG where each node has one outgoing edge (the state transitions form a linked list that eventually enters a cycle), we can process each component (the cycle and the trees leading into it) once. For each cycle, compute the nodes in it. Then, for all states in the tree leading into the cycle, their answer is the same as the cycle's node count.

So here's the plan:

- Initialize a visited array to track processed states.
- For each state (u, c_mod) not yet processed:
   - Traverse the transitions, keeping track of the path.
   - If during traversal, a state is encountered that is already visited:
      - If it's part of the current path, then we found a cycle. The cycle is from the first occurrence of this state in the current path to the end.
      - For each state in the cycle, collect all the nodes visited along the cycle (each state's u) and store the count of distinct nodes.
      - Assign this count to all states in the cycle.
      - For the states in the path before the cycle, assign them the same count (since they eventually reach the cycle).
   - If the encountered state is not part of the current path (i.e., part of a previously processed component), then all states in the current path are part of a tree leading into that component. So their count is the same as the component's count.

But how to track this? Let's think of each state in the current path. For each state in the path, once we know the component it belongs to (the cycle), we can store the answer (the count of nodes in the cycle).

This is similar to the standard algorithm for finding strongly connected components (SCCs) in a graph, but since each node has exactly one outgoing edge, the graph is made up of chains leading into cycles. Each component is a cycle, with trees directed towards it.

So the algorithm can be:

For each unvisited state S:
   Start traversing from S, keeping a list of visited states in the path.
   For each step, check if the next state has already been visited.
   If next state is in the current path:
       The cycle starts at the index where the next state first appears in the path.
       The cycle is from that index to the end of the path.
       Compute the set of nodes in the cycle (collect all u in the states of the cycle).
       The count is the size of this set.
       Assign this count to all states in the cycle.
       Then, for the states in the path before the cycle, assign them the same count (since they eventually enter the cycle).
   If next state is not in the current path but has been visited before:
       All states in the current path are part of a tree leading into an existing component. Their answer is the same as the next state's answer.

Wait, but in this scenario, if next state's answer has already been computed, then all states in the current path can inherit that answer. Because once they follow the transitions, they reach the next state, which already has a known answer. So for each state in the current path, their answer is the same as the next state's answer.

So the algorithm can be:

Initialize a memoization array ans[u][c_mod] which stores the answer for each state.

For each state (u, c_mod) not processed yet:
   Start a new traversal, keep track of the path in a list.
   For each state in the path:
      If the next state is already in the memo:
          For all states in the current path, set their ans to memo[next_state].ans.
          Break the traversal.
      Else if the next state is in the current path (indicating a cycle):
          The cycle starts at the index where next_state is first encountered.
          The cycle part is from start_index to end of path.
          Collect all unique u's in the cycle part.
          The cycle_size is the number of unique u's.
          For each state in the cycle part, set ans[state] = cycle_size.
          For the states in the path before the cycle part, set their ans to cycle_size.
          Break the traversal.
      Else:
          Add next_state to the path and continue.

But how to track whether a state has been processed (i.e., ans is already computed)? The memo array can be initialized as -1, and once ans is set, it's marked as processed.

But during the traversal, we may encounter a state that is part of the current path but not yet processed (ans is -1). So the key is to detect if the next state is already in the current path.

So here's a possible implementation:

For each state (u, c_mod) where ans[u][c_mod] is -1:
   path = []
   current_state = (u, c_mod)
   while True:
      if ans[current_state] != -1:
          # The rest of the path can be set to this value
          for s in path:
              ans[s] = ans[current_state]
          break
      if current_state in path:
          # Found a cycle. The cycle starts at the index of current_state in path.
          start_idx = path.index(current_state)
          cycle = path[start_idx:]
          # collect unique nodes in cycle
          unique_nodes = set()
          for s in cycle:
              unique_nodes.add(s[0])
          count = len(unique_nodes)
          # set ans for cycle states
          for s in cycle:
              ans[s] = count
          # set ans for states before cycle (they lead into cycle)
          for s in path[:start_idx]:
              ans[s] = count
          break
      path.append(current_state)
      next_node = e_u[x], where x is (current_state's c_mod + k_u) mod m_u
      next_c_mod = (current_state's c_mod + k_u) mod 2520
      current_state = (next_node, next_c_mod)

But storing the path as a list and checking for current_state in path could be O(n) for each step, which is not feasible. Because for each state, path can be up to O(2.5e6) in length, leading to O(n^2) time.

This would be too slow.

Alternative approach: track visited states in a dictionary (hash map) during the traversal. But for each path, the current traversal is a linked list. So for each state in the path, we can track the order in which they are visited.

But again, checking if the current_state is in the path's dictionary is O(1), but building the dictionary for each path is O(cycle length). But since each state is processed exactly once, the total time would be O(2.5e6), which is acceptable.

Wait, here's a better way:

Use a visited set for the current path. For each traversal:

Initialize a dictionary (or a hash set) to track the states in the current path, along with their order.

But for each traversal, which could be O(cycle length) steps, and since each state is processed once, the total time would be O(2.5e6), which is manageable.

So here's a modified approach:

Initialize all ans to -1.

For each state (u, c_mod) where ans is -1:

   stack = []
   visited_in_path = {}
   current = (u, c_mod)
   while True:
      if ans[current] != -1:
          # All states in the stack can be set to ans[current]
          for s in stack:
              ans[s] = ans[current]
          break
      if current in visited_in_path:
          # Found a cycle. The cycle starts at visited_in_path[current]
          cycle_start_index = visited_in_path[current]
          # The cycle is from cycle_start_index to current index -1
          cycle = stack[cycle_start_index:]
          # Collect unique nodes in cycle
          unique_nodes = set()
          for s in cycle:
              unique_nodes.add(s[0])
          count = len(unique_nodes)
          # Assign count to all cycle states
          for s in cycle:
              ans[s] = count
          # Assign count to all states before the cycle in the stack (if any)
          for s in stack[:cycle_start_index]:
              ans[s] = count
          break
      # Add current to the stack and visited_in_path
      visited_in_path[current] = len(stack)
      stack.append(current)
      # Compute next state
      u_current, c_mod_current = current
      m_i = m[u_current-1]  # assuming 0-based storage for m and e
      k_i = k[u_current-1]
      x = (c_mod_current + k_i) % m_i
      next_u = e[u_current-1][x]
      next_c_mod = (c_mod_current + k_i) % 2520
      current = (next_u, next_c_mod)

   # After processing, mark all states in stack as processed by setting ans
   # which is already done in the loop.

Wait, but in this approach, the 'stack' is built for each traversal. For each state in the stack, once processed, their ans is set. So each state is processed exactly once.

This should be O(2.5e6) steps, which is acceptable.

Once all ans are precomputed, each query can be answered in O(1) time by:

For query (x, y):

   initial_c_mod = y % 2520
   if initial_c_mod < 0:  # handle negative mod
       initial_c_mod += 2520
   state = (x, initial_c_mod)
   return ans[state]

Now, the next step is to precompute the transitions. Let's model the nodes as 0-based or 1-based. The problem states that nodes are numbered 1 to n, so in code, perhaps the code uses 0-based by adjusting.

But code-wise, the code can read the nodes as 1-based.

Now, the steps for code:

Read n.

Read the k array: list of n integers, 1-based.

Then, read 2*n lines. For each i (1-based?), the 2i-th line is m_i, then the 2i+1-th line is the edges e_i[0..m_i-1].

Wait, input is:

After n, the second line is the k array (n integers, 1-based? Yes, because the i-th vertex is the i-th in the input, so k[0] is k_1 in the problem statement. Wait no. Let's see: the second line has n integers. The i-th integer is k_i for the i-th vertex. So for code, we can store k as a list where k[0] is k_1. Wait, no. For example, in the sample input:

Sample input 1:

4

0 0 0 0 → which are k_1, k_2, k_3, k_4.

Then, the next lines describe the edges for each vertex. For the (2i+1)-th line and (2i+2)-th line.

Wait, the problem statement says:

Next 2n lines describe the edges of each vertex. The (2i+1)-st line contains m_i. The (2i+2)-nd line contains e_i[0], etc.

So for i from 0 to n-1:

vertex 0 (in code) corresponds to the first vertex (1 in the problem).

So for code:

k = list of k_i, where k[i] is the value for vertex (i+1) in the problem.

Then, for vertex i (0-based in code, 1-based in problem), read m_i and edges.

So for code:

n = int(input())
k = list(map(int, input().split()))
edges = []
m = []
for _ in range(n):
    mi = int(input())
    m.append(mi)
    e = list(map(int, input().split()))
    # convert to 0-based in code
    e = [x-1 for x in e]
    edges.append(e)

So for vertex i (code's 0-based), m[i] is the number of edges, edges[i] is the list of destination vertices (0-based).

Then, for the transitions:

When in state (u, c_mod) (u is 0-based in code), the next state is determined as:

current node is u (code's 0-based). m_i is m[u]. k_i is k[u].

x = (c_mod + k[u]) % m[u]

next_u = edges[u][x]

next_c_mod = (c_mod + k[u]) % 2520

Because 2520 is the LCM of 1-10, which are the possible m_i values.

Now, precompute the ans for each state (u, c_mod) as described.

Once that's done, for each query (x, y):

x is 1-based in input. Convert to 0-based (x-1).

y_initial = y

c_mod_initial = (y_initial) % 2520

But note that in Python, the modulo operation with negative numbers can yield negative results. So to ensure it's positive, compute:

c_mod = (y_initial % 2520) if y_initial >=0 else (2520 + (y_initial % 2520)) % 2520

Alternatively, compute (y_initial % 2520 + 2520) % 2520.

So in code:

initial_c_mod = (y % 2520 + 2520) % 2520

Then, the ans for (x-1, initial_c_mod) is the precomputed answer.

Thus, putting it all together.

Now, the code steps:

1. Read the input.

2. Precompute the next state for each (u, c_mod).

3. Precompute the ans for each state (u, c_mod) using the DFS-like approach.

But in Python, for 2.5e6 states, the code needs to be efficient.

Implementing the DFS approach:

We can represent the ans as a list of lists. Since n can be up to 1e3 and c_mod up to 2520, ans is a list of 1000 elements, each a list of 2520 elements.

But for code, perhaps using a dictionary is not efficient. So a 2D array would be better.

But in Python, a list of lists is manageable.

Initialize ans as a list of n (each node) lists of 2520 elements, all initialized to -1.

Then, for each u in 0..n-1, and each c_mod in 0..2519:

   if ans[u][c_mod] == -1:

       proceed with the traversal.

But how to manage the traversal for each state.

But code-wise, this can be done with nested loops. But for 1e3 * 2520 = 2.5e6 iterations, each with possible traversal steps, but each state is processed once.

So the code would look something like:

MOD = 2520
n = ... # code's n (number of nodes)
ans = [[-1 for _ in range(MOD)] for _ in range(n)]

for u in range(n):
    for c_mod in range(MOD):
        if ans[u][c_mod] == -1:
            stack = []
            visited_in_path = dict()
            current = (u, c_mod)
            while True:
                if ans[current[0]][current[1]] != -1:
                    # set all in stack to this ans
                    for (nu, nc) in stack:
                        ans[nu][nc] = ans[current[0]][current[1]]
                    break
                if current in visited_in_path:
                    # found a cycle
                    start_idx = visited_in_path[current]
                    cycle = stack[start_idx:]
                    unique_nodes = set()
                    for (nu, nc) in cycle:
                        unique_nodes.add(nu)
                    count = len(unique_nodes)
                    # assign to cycle and stack
                    for (nu, nc) in cycle:
                        ans[nu][nc] = count
                    for (nu, nc) in stack[:start_idx]:
                        ans[nu][nc] = count
                    break
                visited_in_path[current] = len(stack)
                stack.append(current)
                # compute next state
                nu, nc_mod = current
                k_i = k[nu]
                m_i = m[nu]
                x = (nc_mod + k_i) % m_i
                next_u = edges[nu][x]
                next_c_mod = (nc_mod + k_i) % MOD
                current = (next_u, next_c_mod)

But this code may not be efficient enough for Python. For example, for 2.5e6 states, each potentially needing a traversal of a few steps.

But perhaps with the constraints given (n up to 1e3, MOD 2520), and the fact that each state is processed exactly once, this code can pass within the time limit.

But let's consider the sample input. For example, in the first sample, each query is answered quickly once the precomputation is done.

Potential optimizations:

- Precompute next states for all (u, c_mod) pairs, and store them in a 2D array. But even that would take 2.5e6 entries, which is manageable.

But in the code above, during the traversal, for each current state, the code computes the next state on the fly. Precomputing these next states could speed up the process.

So, precompute a next_state array, where next_state[u][c_mod] = (v, next_c_mod).

This can be done once at the beginning.

So:

MOD = 2520
n = ... 
m = ... 
edges = ... 
k = ... 

next_state = [[(0, 0) for _ in range(MOD)] for _ in range(n)]
for u in range(n):
    for c_mod in range(MOD):
        k_i = k[u]
        m_i = m[u]
        x = (c_mod + k_i) % m_i
        next_u = edges[u][x]
        next_c_mod = (c_mod + k_i) % MOD
        next_state[u][c_mod] = (next_u, next_c_mod)

Then, during the traversal, each next state is fetched from next_state[u][c_mod].

This would save computation time during the traversal steps.

Yes, this is a good idea. Because for each state (u, c_mod), the next state can be looked up in O(1) time. Precomputing this once upfront can save redundant computations during the DFS traversal.

So modifying the code to precompute next_state:

Compute next_state as a list of lists of tuples.

Once next_state is precomputed, the traversal becomes:

current = (u, c_mod)
while True:
   ...
   current = next_state[current[0]][current[1]]

This can speed up the traversal.

So in code:

precompute next_state.

Then, during the processing of each state:

current = (u, c_mod)
...
current = next_state[nu][nc_mod]

Now, the code can process each state faster.

This should reduce the time taken for the processing step.

Now, let's test the sample input.

Sample input 1:

4
0 0 0 0

Then, for each node:

node 1 (code's 0):

m=2, edges are 2 3 (code's 1 and 2?)

Wait, in code, the edges are converted to 0-based. So the input edges for node 1 (code's 0) are 2 and 3 (converted to 1 and 2 (0-based? Wait, original input is 2 and 3. Subtract 1: 1 and 2.

But in code, nodes are 0-based. So edges[0] = [1, 2].

But in code, the next state computation for node 0, c_mod:

For example, node 0's k is 0. So for any c_mod, x = (c_mod + 0) mod 2. So next node is edges[0][x], which is 1 or 2 (0-based? No, in code, edges are stored as destination nodes in 0-based. So input for node 1 (code 0) is edges 2 and 3, which after converting to 0-based are 1 and 2. So edges[0] = [1,2].

Wait, the input for edges is:

First node (code 0):

m_i is 2, edges are 2 3. Converted to 0-based: 2-1=1, 3-1=2.

So edges[0] = [1,2].

So for node 0, when x is 0, next node is 1 (code's 1 is problem's node 2).

So in the first sample query 1: starting at node 1 (code's 0) with c=0.

In code, initial_c_mod is 0 % 2520 =0.

So state is (0,0). The next state is next_state[0][0], which is (edges[0][ (0+0) mod 2 ] , (0+0) mod 2520). (0+0) mod 2 is 0, so edges[0][0] is 1. next_c_mod is 0. So next_state[0][0] is (1,0).

Then, from (1,0), next_state[1][0] depends on node 1's edges.

In the first sample, node 2 (code's 1) has m=1, edges are 2 (code's 1), so edges[1] = [1]. So next node is always 1 (code's 1).

k for code's node 1 (problem node 2) is 0. So next_c_mod is (0 + 0) mod 2520 = 0. So next_state[1][0] is (1,0). So the cycle is (1,0) → (1,0). So the cycle is size 1, node 1 (problem node 2).

So the answer is 1, which matches the first sample's first query.

Thus, the code should correctly handle this.

Another sample query: starting at node 3 (code's 2) with c=-1.

initial_c_mod is (-1) mod 2520 = 2519.

But code's node 2 (problem's node 3) has k=0, m=3, edges [2,4,1]. So in code, edges[2] = [1,3,0].

Because the input is 2 4 1. Subtracting 1 from each: 1,3,0.

But for code's node 2 (problem's node 3), m=3. So x = (c_mod + k_i) mod 3. k_i is 0. So x is (2519 +0) mod3. 2519 mod3: 2519 /3 is 839 *3 = 2517, remainder 2. So x=2. So next node is edges[2][2] which is 0 (problem's node 1). next_c_mod is (2519 +0) mod 2520 = 2519.

So next_state is (0, 2519).

Then, node 0 (problem 1) has k=0. m=2, edges are [1,2] (code's 0-based).

x = (2519 +0) mod2 = 2519 mod2 = 1. So next node is 2 (code's 2, problem's 3). next_c_mod is 2519 +0 mod2520 = 2519.

So state (0, 2519) → (2, 2519).

Thus, the cycle between (0, 2519) and (2, 2519) forms a cycle of two nodes, code's 0 and 2 (problem's 1 and 3). So each of these steps adds 0 to c, so the cycle is between nodes 1 and 3 (code's 0 and 2). So the answer would be 2 distinct nodes.

Which matches sample's third query output.

Thus, the code should correctly handle this.

Now, the code's steps:

Implement the precomputation of next_state.

Then, for each state (u, c_mod) in 0..n-1 x 0..2519:

If ans[u][c_mod] is not computed, process it with the stack and visited_in_path.

Now, in Python, for efficiency, using tuples (u, c_mod) as keys in a dictionary may be slow. So perhaps using a helper structure to track visited_in_path.

But given that each state is processed once, and each traversal is O(cycle length) steps, it's manageable.

Now, the code in Python:

But handling large n and MOD, the code must be optimized.

But in Python, even with 1e3 * 2520 = 2.5e6 states, and each state processed once, this should be manageable.

Another optimization: precompute next_state as a list of lists of tuples.

But in Python, list lookups are O(1).

Thus, here's the code:

Read n.

Read k as list of integers.

Read n times m_i and edges.

Precompute next_state for each u and c_mod.

Initialize ans as a 2D list of -1.

For each u in 0..n-1:

   for each c_mod in 0..2519:

      if ans[u][c_mod] == -1:

          process this state.

Implement the processing as described.

Once all ans are filled, read q queries.

For each query:

   x, y → x is 1-based, code uses x-1 as u.

   y_initial = y.

   initial_c_mod = (y_initial % MOD + MOD) % MOD.

   answer is ans[x-1][initial_c_mod].

   print(answer)

Now, the code.

Testing for sample input 1.

Sample input 1:

4

0 0 0 0

Then, nodes 1-4 have k=0 each.

Edges:

Node 1 (code 0):

m=2, edges 2 3 → code's 1 and 2.

Node 2 (code 1):

m=1, edges 2 → code's 1.

Node 3 (code 2):

m=3, edges 2 4 1 → code's 1, 3, 0.

Node 4 (code 3):

m=4, edges 3 1 2 1 → code's 2, 0, 1, 0.

Then, next_state for each node and c_mod.

But since k_i are all 0, the next_c_mod is (c_mod + 0) mod 2520 = c_mod.

But x is (c_mod + 0) mod m_i.

For node 0 (m=2), x = c_mod mod 2.

For example, for c_mod=0 → x=0 → next_u=1 (code's 1).

For c_mod=1 → x=1 mod2=1 → next_u=2 (code's 2).

For code's node 0, next_state[0][c_mod] is:

edges[0][ (c_mod) % 2 ] , c_mod.

So for example, when c_mod is 0 → next node is 1 (code's 1), next_c_mod=0.

But this would create a cycle between (1,0) → next_state[1][0].

For node 1 (code's 1), m=1. x = c_mod mod 1 = 0. So next node is edges[1][0] =1 (code's 1). next_c_mod remains the same.

Thus, node 1, any c_mod leads to next node 1. So ans for (1, c_mod) is 1.

Similarly, for node 3 (code's 3), m=4. x = c_mod mod4. So edges are [2,0,1,0]. So depending on c_mod mod4, next node is 2,0,1,0.

But in the first sample, when starting at node 0 (code's 0) with y=0 → initial_c_mod=0.

The traversal is:

(0,0) → (1,0) → (1,0) → cycle of size 1. So ans is 1.

Which matches the sample.

Now, the code.

But in Python, the way to handle large 2D arrays.

Implementing next_state as a list of lists of tuples.

But given that n is up to 1e3 and MOD is 2520, it's manageable.

So here's the code:
</think>

```python
import sys

def main():
    MOD = 2520
    n = int(sys.stdin.readline())
    k = list(map(int, sys.stdin.readline().split()))
    m = []
    edges = []
    for _ in range(n):
        mi = int(sys.stdin.readline())
        e = list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
        m.append(mi)
        edges.append(e)
    
    # Precompute next_state
    next_state = [[(0, 0) for _ in range(MOD)] for _ in range(n)]
    for u in range(n):
        for c_mod in range(MOD):
            k_i = k[u]
            mi = m[u]
            x = (c_mod + k_i) % mi
            next_u = edges[u][x]
            next_c = (c_mod + k_i) % MOD
            next_state[u][c_mod] = (next_u, next_c)
    
    ans = [[-1 for _ in range(MOD)] for _ in range(n)]
    
    for u in range(n):
        for c_mod in range(MOD):
            if ans[u][c_mod] != -1:
                continue
            stack = []
            visited = {}
            current = (u, c_mod)
            while True:
                if ans[current[0]][current[1]] != -1:
                    # Assign to all in stack
                    cnt = ans[current[0]][current[1]]
                    for (nu, nc) in stack:
                        ans[nu][nc] = cnt
                    break
                if current in visited:
                    # Found cycle
                    start_idx = visited[current]
                    cycle = stack[start_idx:]
                    unique_nodes = set(n for n, _ in cycle)
                    cnt = len(unique_nodes)
                    # Assign cycle
                    for (nu, nc) in cycle:
                        ans[nu][nc] = cnt
                    # Assign pre-cycle
                    for (nu, nc) in stack[:start_idx]:
                        ans[nu][nc] = cnt
                    break
                visited[current] = len(stack)
                stack.append(current)
                current = next_state[current[0]][current[1]]
    
    q = int(sys.stdin.readline())
    for _ in range(q):
        x, y = map(int, sys.stdin.readline().split())
        u = x - 1
        initial_c_mod = (y % MOD + MOD) % MOD
        print(ans[u][initial_c_mod])

if __name__ == "__main__":
    main()
```