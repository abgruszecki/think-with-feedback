<think>
Okay, so I need to solve this problem where I have to check if all junctions in a grid are reachable from each other given the directions of the horizontal and vertical streets. Let me think through this step by step.

First, let's understand the problem. The city has n horizontal streets (running west-east or east-west) and m vertical streets (running north-south or south-north). Each horizontal street is part of a row, and each vertical street is a column. The junctions are the intersections of these streets. The directions determine how you can move between junctions. The goal is to check if the entire graph (where junctions are nodes and the allowed movements are edges) is strongly connected. That is, for any two junctions A and B, there's a path from A to B and from B to A.

Hmm. Wait, no, the problem says "reach any junction from any other junction". So it's sufficient if the entire graph is a single strongly connected component. So I need to check for strong connectivity.

But checking strong connectivity for every possible pair of nodes might be computationally expensive. For each junction (i,j), we need to make sure that there's a path from (i,j) to every other junction. However, given the constraints (n and m up to 20), the total number of junctions is (n) * (m) for horizontal and vertical? Wait, wait. Wait, the horizontal streets are n in number, but each horizontal street is a line of m-1 vertical streets? Or maybe not. Let me re-read the problem statement.

The problem says: n horizontal streets crossing m vertical streets, forming an (n-1) × (m-1) grid. Wait, no. Wait, if there are n horizontal streets, they are arranged from north to south, with each being a horizontal line. Similarly, m vertical streets arranged west to east. So the grid of intersections is (n) × (m)? Because each horizontal street is crossed by m vertical streets. Wait, maybe not. Let me think again. For example, if there are 3 horizontal streets and 3 vertical streets. The horizontal streets run north to south (so the first is northernmost), and vertical streets run west to east (first is westernmost). Then, the intersections would be (n horizontal) × (m vertical) points. So each junction is the intersection of a horizontal and vertical street. So there are n × m junctions in total. Wait, no. Wait, horizontal streets are n in number, vertical m in number. Each horizontal street is crossed by m vertical streets. Each vertical street is crossed by n horizontal streets. So the total number of intersections is n * m. For example, n=3 and m=3, that's 3*3=9 junctions.

So each junction is identified by (i,j), where i is the horizontal street index (from 1 to n?), and j is the vertical street index (from 1 to m?).

Wait, but the problem's first example input is 3 3, directions "><>", and "v^v". The output is NO. So in that case, the grid is 3 horizontal streets and 3 vertical streets. Each horizontal street has direction left or right, each vertical has up or down.

So, each junction (i,j) can move to adjacent junctions based on the direction of the street. For example, in a horizontal street, if the direction is '>', then moving along that street allows you to go from (i,j) to (i,j+1) if possible. Wait, no. Wait, the horizontal street is a single direction. For example, a horizontal street i has direction '>', which means that all traffic on that street moves west to east. So, on that street, each junction (i,j) can move to (i,j+1), but only along that street. Similarly, if direction is '<', then (i,j) can move to (i,j-1).

But how about vertical streets? For vertical street j, if the direction is 'v', then movement is from north to south, so from (i,j) you can move to (i+1,j). If direction is '^', then movement is from south to north, so from (i,j) you can move to (i-1,j).

Wait, but this is about the direction of the street. So for example, for a horizontal street, the direction determines whether you can move east or west along that street. For a vertical street, the direction determines whether you can move south or north along that street.

So, the movement between junctions is as follows:

For any junction (i,j):

- Along the horizontal street i: if the direction is '>', then you can move east, so from (i,j) you can move to (i,j+1) if j+1 <= m. If the direction is '<', you can move west, so to (i,j-1) if j-1 >= 1.

- Along the vertical street j: if the direction is 'v', you can move south, from (i,j) to (i+1,j) if i+1 <= n. If the direction is '^', you can move north, to (i-1,j) if i-1 >= 1.

Wait, but the vertical streets are in the third line of the input, and each character represents a vertical street. The vertical streets are listed in order from west to east. So the j-th vertical street (third line's j-th character) is the one that runs vertically in the west-east direction. So for the vertical street j, the direction is given as 'v' or '^'.

So for each junction (i,j), the possible moves are:

1. Along horizontal street i: move left or right according to the horizontal direction of that street.

2. Along vertical street j: move up or down according to the vertical direction of that street.

But when you are at (i,j), you can choose to move along the horizontal or vertical street. So the movement is allowed in either direction (horizontal or vertical) from that junction.

Wait, but how? For example, if you are at (i,j), you can move along the horizontal street i (if possible) to adjacent cells, and along the vertical street j (if possible) to adjacent cells.

So for each junction (i,j), the possible next junctions are:

- For horizontal movement: if the horizontal street i's direction is '>', then (i,j) can move to (i,j+1), but only if j+1 is <= m. If it's '<', then (i,j) can move to (i,j-1) if j-1 >=1.

- Similarly, for vertical movement: if vertical street j's direction is 'v', then (i,j) can move to (i+1,j) if i+1 <=n. If it's '^', then (i,j) can move to (i-1,j) if i-1 >=1.

Wait, but (i,j) can move along both the horizontal and vertical streets. So the possible adjacent nodes are up to four possible (depending on the directions). For example, if a junction (i,j) is in a horizontal street that allows moving east (so j+1 is allowed) and vertical street allows moving south (i+1 allowed), then (i,j) can move to (i,j+1) via the horizontal street, and (i+1,j) via the vertical street.

So the movement graph is directed. Each junction (i,j) has outgoing edges based on the directions of the horizontal and vertical streets it's part of.

The problem requires that the entire directed graph is strongly connected. So, for every pair of nodes u and v, there must be a directed path from u to v.

But how to check this efficiently?

The constraints are n and m up to 20. So the total number of junctions is up to 20 * 20 = 400. For each node, we need to check reachability to all other nodes. The straightforward approach would be for each node, perform a BFS or DFS to see if all nodes are reachable. But since there are 400 nodes, and each BFS is O(400), the total time would be 400 * 400 = 160,000 operations. That's manageable within the time constraints (2 seconds), but maybe even better approaches exist.

Alternatively, perhaps there's a way to model this as a graph and check if the entire graph is strongly connected by checking if the entire graph is a single strongly connected component. To find strongly connected components (SCCs), we can use algorithms like Kosaraju's or Tarjan's. If the entire graph forms one SCC, then output YES; else, NO.

But even for 400 nodes, finding the SCCs is feasible. So the plan is:

1. Create a directed graph where each node is a junction (i,j).

2. For each junction (i,j), add edges based on the directions of the horizontal and vertical streets.

3. Compute the SCCs of this graph. If there's exactly one SCC, output YES; else, NO.

So the main steps are:

- Building the adjacency list for the graph.

- Then, checking the number of SCCs.

Now, let's think about how to model the adjacency list.

For each junction (i,j):

The possible moves are:

a) Along horizontal street i:

   If the direction is '>', then from (i,j), you can move to (i,j+1) if j+1 <= m.

   If direction is '<', then to (i,j-1) if j-1 >=1.

b) Along vertical street j:

   If direction is 'v', then from (i,j) can move to (i+1,j) if i+1 <=n.

   If direction is '^', then to (i-1,j) if i-1 >=1.

So for each (i,j), generate up to 2 possible edges (could be 0, 1, or 2 edges). Wait, no. For example, if (i,j) is on the horizontal street i which is '>', then j can be at m, which means j+1 is m+1, which is beyond the vertical street count. So (i,j) cannot move east. So in that case, the horizontal direction gives no edge. Similarly, if (i,j) is on vertical street j with direction 'v', but i is n, then moving south is impossible. So each direction can contribute 0 or 1 edge.

So for each (i,j), we check the horizontal and vertical directions and add edges accordingly.

Once the graph is built, we can compute SCCs. The standard approach for this is Kosaraju's algorithm: perform a DFS in a certain order, then transpose the graph and perform another DFS. Alternatively, Tarjan's algorithm can compute SCCs in linear time.

But implementing Kosaraju's might be easier here. Let's think.

Kosaraju's steps:

1. Perform a DFS on the original graph, pushing nodes onto a stack in the order of completion.

2. Transpose the graph (reverse all edges).

3. Process nodes in the stack order, performing a DFS on the transposed graph. Each tree in this step is an SCC.

If there's only one SCC, output YES.

So the main task is to model the graph correctly.

Now, let's think about the code structure.

First, read n and m.

Then, read the horizontal directions (a string of length n) and vertical directions (a string of length m).

Then, for each junction (i, j) (i ranges from 1 to n, j from 1 to m?), create all possible edges.

Wait, in the problem statement, the horizontal streets are listed from north to south, so i=1 is northernmost. The vertical streets are listed from west to east, so j=1 is westernmost.

So each junction is (i,j) where 1 <= i <=n and 1 <=j <=m.

Wait, but the grid is formed as (n-1) × (m-1)? Wait, the first line says "n horizontal streets crossing m vertical streets, forming an (n - 1) × (m - 1) grid". Wait, that's confusing. Wait, for example, if there are 2 horizontal streets and 2 vertical streets, the grid is 1x1? Which makes sense. So each horizontal street is a line, and each vertical street is a line. The intersections are between each horizontal and vertical. So the number of junctions is n * m. Wait, no. Wait, if you have 2 horizontal streets (n=2) and 3 vertical streets (m=3), then each horizontal street is crossed by all 3 vertical streets, giving 2 * 3 =6 junctions. So the grid is 2 rows (horizontal) ×3 columns (vertical). So the number of junctions is n * m. But the problem statement says "forming an (n-1) × (m-1) grid." Hmm, that's conflicting. Wait, perhaps the original statement is wrong. Let's read the problem statement again.

Problem statement says: "forming an (n - 1) × (m - 1) grid." But that doesn't make sense. Because, for example, if you have n=3 horizontal streets and m=3 vertical streets, they would form a grid of 2×2 squares, leading to 3×3 junctions. So (n) × (m) junctions. So the problem statement's note about (n-1)x(m-1) is perhaps a mistake. Or perhaps it's a translation error.

But given the sample inputs, let's see. For example, the first sample input is 3 3. So n=3, m=3. The grid would have 3 horizontal and 3 vertical streets, making 3x3=9 junctions. So the code should model each (i,j) where 1<=i<=n, 1<=j<=m.

So in code, the junctions are (i,j) for i in 0-based or 1-based indices. Let's use 0-based or 1-based.

But in the code, perhaps it's easier to model with 0-based indices.

Wait, but the code needs to process the horizontal and vertical directions. For the horizontal directions, the i-th character in the string represents the direction of the i-th horizontal street (north to south). So i ranges from 0 to n-1. Similarly, the j-th character in the vertical string is the j-th vertical street, west to east, from 0 to m-1.

So for a junction (i, j) where i is the horizontal street index (0-based, from north to south) and j is the vertical street index (0-based, west to east), then:

- The horizontal direction is given by h_dirs[i], which is either '<' or '>'.

- The vertical direction is given by v_dirs[j], which is '^' or 'v'.

So, for each (i,j), the possible edges are:

1. Along horizontal street:

   If h_dirs[i] is '>', then possible to move to (i, j+1) if j+1 < m. Wait, because if there are m vertical streets, then j can be from 0 to m-1. So (i,j) can move east to (i,j+1) only if j+1 is less than m. Because j+1 represents the next vertical street to the east.

Similarly, if h_dirs[i] is '<', then move to (i, j-1) if j-1 >=0.

2. Along vertical street:

   If v_dirs[j] is 'v', then move to (i+1, j) if i+1 < n. Because i+1 is the next horizontal street to the south.

   If v_dirs[j] is '^', then move to (i-1, j) if i-1 >=0.

So for each junction (i,j), there are up to two outgoing edges.

So in code, the adjacency list can be represented as a dictionary or list of lists, where for each node (i,j), we generate the possible edges.

But how to represent the nodes (i,j) as indices in a graph? We can map each (i,j) to a unique integer. For example, for a grid of n rows and m columns, the node (i,j) can be represented as i * m + j. So the total number of nodes is n*m. This would make it easier to handle in adjacency lists.

So, let's proceed with this approach.

So, first, read n and m.

Then, read the horizontal directions string h (length n) and vertical directions string v (length m).

Then, for each node (i,j), convert to an integer index (like idx = i * m + j).

For each (i,j):

   Check the horizontal direction h[i]:

      if h[i] is '>', then j+1 must be < m. If so, add an edge from (i,j) to (i, j+1).

      if h[i] is '<', then j-1 must be >=0. If so, add an edge from (i,j) to (i, j-1).

   Check the vertical direction v[j]:

      if v[j] is 'v', then i+1 <n. If so, add edge from (i,j) to (i+1, j).

      if v[j] is '^', then i-1 >=0. If so, add edge from (i,j) to (i-1, j).

Once all edges are added, the graph is built.

Then, compute the SCCs. If the entire graph is a single SCC, output YES, else NO.

Now, let's think about implementing this.

The code structure:

Read n, m.

Read h_dirs (length n) and v_dirs (length m).

Create adjacency list: a list of lists. The size is n*m.

For each i in 0..n-1:

   for each j in 0..m-1:

       current node idx = i*m +j

       process horizontal direction:

           if h_dirs[i] == '>', check if j+1 < m:

               if yes, add edge to (i, j+1) → idx +1

           else (h_dirs[i] == '<'):

               check if j-1 >=0:

                   add edge to (i, j-1) → idx-1

       process vertical direction:

           if v_dirs[j] == 'v':

               check if i+1 <n:

                   add edge to (i+1, j) → (i+1)*m +j

           else (v_dirs[j] == '^'):

               check if i-1 >=0:

                   add edge to (i-1, j) → (i-1)*m +j

Once adjacency list is built, compute SCCs.

Then check if there's only one SCC.

So, the code's next step is to implement Kosaraju's algorithm.

Kosaraju's steps:

1. Perform a DFS on the original graph, adding nodes to a stack in the order of completion.

2. Reverse the graph (transpose all edges).

3. Process the nodes in the stack order (from top to bottom), performing DFS on the reversed graph. Each tree found in this step is an SCC.

The number of SCCs is the number of components.

So the code needs to:

- Reverse the graph.

But building the reversed graph can be done by creating a new adjacency list where for each edge u→v, we add v→u in the reversed graph.

But for Kosaraju's, during the second pass, when processing the reversed graph, we need to have the edges reversed.

Alternatively, during the second pass, for each node u, when processing edges in the original graph, for each v in adj[u], in the reversed graph, u is in adj_rev[v].

But building the reversed adjacency list can be done as follows:

Initialize a reversed_adj list of empty lists for each node.

For each u in 0..n*m-1:

   for each v in adj[u]:

       reversed_adj[v].append(u)

This way, the reversed adjacency list is built.

Once that's done, the steps are:

1. Perform DFS on the original graph, in any order, and push nodes onto a stack in the order of completion.

But according to Kosaraju's, the first DFS is in any order, but the stack is filled with nodes in order of finishing times.

Wait, no. Kosaraju's algorithm's first step is to perform a DFS in any order, and when a node is finished (all descendants processed), push to the stack.

So the first DFS is to order the nodes in decreasing order of finishing times.

Then, the reversed graph is processed in the order of the stack.

So in code, the first step is to perform a post-order traversal of all nodes (marking visited as we go) and pushing nodes to the stack when finished.

Then, process the reversed graph in the order of the stack (popping the top each time), and for each unvisited node, perform a DFS on the reversed graph. Each such DFS gives one SCC.

If the total number of SCCs is 1, output YES.

So implementing Kosaraju's requires:

- A visited array for the first DFS.

- A stack to hold the order.

- A second visited array (or reuse the same) for the second DFS.

But for code clarity, perhaps better to reset the visited array.

So, code steps:

Initialize visited as all False.

stack = []

for each node in 0 to (n*m -1):

   if not visited:

       perform DFS, mark visited, and append to stack when finished.

Then, build reversed_adj.

Initialize visited_rev as all False.

count = 0

while stack not empty:

   node = stack.pop()

   if not visited_rev[node]:

       perform DFS on reversed_adj, mark visited_rev

       count +=1

if count ==1: YES else NO.

Now, code for this.

But handling the nodes as integers.

So the code will need:

n and m are given.

h = input().strip()

v = input().strip()

Then, adj is built as a list of lists.

For example, adj = [[] for _ in range(n*m)]

Then, for each i in 0..n-1:

   for j in 0..m-1:

       idx = i*m +j

       # horizontal

       if h[i] == '>' and j+1 <m:

           adj[idx].append( idx +1 )

       elif h[i] == '<' and j-1 >=0:

           adj[idx].append( idx -1 )

       # vertical

       if v[j] == 'v' and i+1 <n:

           adj[idx].append( (i+1)*m +j )

       elif v[j] == '^' and i-1 >=0:

           adj[idx].append( (i-1)*m +j )

Wait, but for vertical direction, the code is:

For vertical direction, the direction is based on the vertical street j. So for the current (i,j), the vertical street is j. So the vertical direction is v[j].

So for vertical street j:

if direction is 'v', then moving south (i+1) if possible.

if direction is '^', moving north (i-1) if possible.

Yes.

So in code:

for each (i,j):

   current idx is i*m +j.

   check h_dirs[i] for horizontal movement.

   check v_dirs[j] for vertical movement.

So the code for building adj is:

n, m = map(int, input().split())

h = input().strip()

v = input().strip()

total = n * m

adj = [[] for _ in range(total)]

for i in range(n):

    for j in range(m):

        current = i * m + j

        # horizontal direction (h[i])

        if h[i] == '>':

            if j +1 < m:

                adj[current].append(current +1)

        else: # '<'

            if j -1 >=0:

                adj[current].append(current -1)

        # vertical direction (v[j])

        if v[j] == 'v':

            if i +1 <n:

                adj[current].append( (i+1)*m +j )

        else: # '^'

            if i-1 >=0:

                adj[current].append( (i-1)*m +j )

Once the adj is built, proceed with Kosaraju's.

Then, perform the first DFS to get the order.

Implementing the DFS:

def dfs(u, visited, adj, stack):

    visited[u] = True

    for v in adj[u]:

        if not visited[v]:

            dfs(v, visited, adj, stack)

    stack.append(u)

visited = [False] * total

stack = []

for u in range(total):

    if not visited[u]:

        dfs(u, visited, adj, stack)

Then, build the reversed adjacency list.

rev_adj = [[] for _ in range(total)]

for u in range(total):

    for v in adj[u]:

        rev_adj[v].append(u)

Then, process the stack in reverse order (but since we pop from the end, it's correct).

visited_rev = [False] * total

count =0

while stack:

    node = stack.pop()

    if not visited_rev[node]:

        # perform DFS on reversed graph

        stack_dfs = [node]

        visited_rev[node] = True

        while stack_dfs:

            u = stack_dfs.pop()

            for v in rev_adj[u]:

                if not visited_rev[v]:

                    visited_rev[v] = True

                    stack_dfs.append(v)

        count +=1

if count ==1:

    print("YES")

else:

    print("NO")

Wait, but this uses iterative DFS for the reversed graph. Which is more efficient than recursive, especially for Python which has recursion depth limits. Since the maximum number of nodes is 400, even a recursive approach would work, but iterative is safer.

But for the first DFS, since it's recursive, with n*m up to 400, the recursion depth could be up to 400, which in Python's default recursion stack (which is around 1000) is okay.

But to be safe, perhaps better to implement the first DFS iteratively as well.

Alternatively, switch to iterative DFS for both passes.

So here's an alternative approach for the first DFS:

def dfs_iter(u, visited, adj, stack):

    stack_dfs = []

    stack_dfs.append( (u, False) )

    while stack_dfs:

        node, processed = stack_dfs.pop()

        if processed:

            stack.append(node)

            continue

        if visited[node]:

            continue

        visited[node] = True

        # Push the node again as processed

        stack_dfs.append( (node, True) )

        # Push children in reverse order to process them in the original order

        for v in reversed(adj[node]):

            if not visited[v]:

                stack_dfs.append( (v, False) )

So this is a standard iterative DFS where nodes are marked as processed once their children are processed. This way, the stack gets the nodes in the order of finishing times.

Using this for the first DFS:

stack = []

visited = [False] * total

for u in range(total):

    if not visited[u]:

        dfs_iter(u, visited, adj, stack)

Then, the rest is the same.

But for code efficiency, using iterative DFS is better in Python.

So putting this all together.

Now, let's test the code with the sample inputs.

Sample Input 1:

3 3

><>

v^v

Sample Output: NO.

Let's see.

n=3, m=3.

h = '><>'

v = 'v^v'

So horizontal directions:

h[0] = '>', h[1] = '<', h[2] = '>'.

vertical directions:

v[0] = 'v', v[1] = '^', v[2] = 'v'.

So for each junction (i,j):

i ranges 0-2, j 0-2.

Building adj:

For example, (0,0):

h[0] is '>', j=0. j+1=1 <3: yes. So edge to (0,1).

v[j=0] is 'v'. i+1=1 <3: yes. Edge to (1,0).

So adj[0] = [0*3+1=1, 1*3+0=3]

So node 0 (i=0, j=0) has edges to 1 and 3.

But the graph may not be strongly connected. The sample output is NO, so the code should detect that.

Another sample input:

4 6

<><>

v^v^v^

Sample Output: YES.

So the code must output YES.

So, the code should work.

Now, code-wise, what's the data structure for adj? Each node is a number from 0 to n*m-1.

Now, the code.

But now, the code needs to be optimized for speed and memory. So, let's think about possible optimizations.

In Python, using lists for adjacency lists is efficient. The code uses list comprehensions, which should be fine.

But for the first DFS, using an iterative approach is better.

So, the code steps:

Read n, m.

Read h and v.

Build adjacency list.

Build reversed adjacency list.

Compute first pass to get order.

Process reversed graph in that order.

Count SCCs.

If count is 1, output YES else NO.

Now, implement this.

So here's the code:

Read input:

n, m = map(int, input().split())

h = input().strip()

v = input().strip()

total = n * m

adj = [[] for _ in range(total)]

for i in range(n):

    for j in range(m):

        current = i * m + j

        # Horizontal direction

        if h[i] == '>':

            if j + 1 < m:

                adj[current].append(current + 1)

        else:  # '<'

            if j - 1 >= 0:

                adj[current].append(current - 1)

        # Vertical direction

        if v[j] == 'v':

            if i + 1 < n:

                adj[current].append((i + 1) * m + j)

        else:  # '^'

            if i - 1 >= 0:

                adj[current].append((i - 1) * m + j)

Then, perform the first DFS (iterative):

visited = [False] * total

stack = []

for u in range(total):

    if not visited[u]:

        stack_dfs = []

        stack_dfs.append( (u, False) )

        while stack_dfs:

            node, processed = stack_dfs.pop()

            if processed:

                stack.append(node)

                continue

            if visited[node]:

                continue

            visited[node] = True

            stack_dfs.append( (node, True) )

            # Push children in reverse order to process in original order

            for child in reversed(adj[node]):

                if not visited[child]:

                    stack_dfs.append( (child, False) )

Then, build reversed adjacency list:

rev_adj = [[] for _ in range(total)]

for u in range(total):

    for v in adj[u]:

        rev_adj[v].append(u)

Process reversed graph:

visited_rev = [False] * total

count = 0

while stack:

    node = stack.pop()

    if not visited_rev[node]:

        # BFS or DFS to visit all nodes in this SCC

        # Use a stack for DFS

        scc_stack = [node]

        visited_rev[node] = True

        while scc_stack:

            u = scc_stack.pop()

            for v in rev_adj[u]:

                if not visited_rev[v]:

                    visited_rev[v] = True

                    scc_stack.append(v)

        count += 1

if count == 1:

    print("YES")

else:

    print("NO")

This should work.

Testing the first sample input:

n=3, m=3.

h = "><>"

v = "v^v"

Building adj:

For i=0 (horizontal direction '>'):

j can be 0,1,2.

At i=0, j=0:

h[0] is '>', so j+1=1 is <3: add edge to 1.

v[j=0] is 'v', so i+1=1 <3: add edge to 3.

So adj[0] = [1,3]

j=1: h[0] '>' → j+1=2 <3: add edge to 2.

v[j=1] is '^', so i-1 can't be >=0 (i=0) → no vertical edge.

adj[1] = [2, ... ]?

Wait, j=1: i=0.

v[j=1] is '^', so i-1 would be -1. So no edge.

So adj[1] has edge 2 (from horizontal) and no vertical.

Wait, vertical street j=1 direction is '^', so moving north from (i,j) = (0,1) is impossible.

So adj[1] is [2].

Similarly, j=2: h[0] '>', but j+1=3 is >=3: no. So no horizontal edge.

v[j=2] is 'v' → i+1=1 <3: add edge to 3*3 +2? Wait, i+1=1, j=2.

So (1,2) → index is 1 *3 +2 =5. So adj[2].append(5).

So adj[2] = [5].

So for node 2 (i=0,j=2), adj[2] is [5].

And so on.

But perhaps the graph is such that not all nodes are reachable from each other.

The code would find the number of SCCs. If it's more than 1, output NO.

So the code should correctly handle this.

Another point to consider is that the reversed_adj is built correctly.

Once adj is built, reversed_adj is built by adding for each u → v in adj, reversed_adj[v] gets u.

Thus, the code builds the reversed adjacency list correctly.

Thus, the code should work.

In terms of speed, with n and m up to 20, total nodes is 400. Each node has up to 2 edges. So the adj lists are small. Kosaraju's runs in O(V + E), which is O(400 + 800) = 1200 steps. So even for multiple test cases, this is manageable.

Memory-wise, the adjacency lists for 400 nodes, each with 2 edges, are manageable. Python's lists should handle this without problem.

Thus, the code should be correct and efficient.
</think>

```python
n, m = map(int, input().split())
h = input().strip()
v = input().strip()

total_nodes = n * m
adj = [[] for _ in range(total_nodes)]

for i in range(n):
    for j in range(m):
        current = i * m + j
        # Horizontal direction
        if h[i] == '>':
            if j + 1 < m:
                adj[current].append(current + 1)
        else:
            if j - 1 >= 0:
                adj[current].append(current - 1)
        # Vertical direction
        if v[j] == 'v':
            if i + 1 < n:
                adj[current].append((i + 1) * m + j)
        else:
            if i - 1 >= 0:
                adj[current].append((i - 1) * m + j)

# First pass to determine processing order
visited = [False] * total_nodes
processing_order = []

for u in range(total_nodes):
    if not visited[u]:
        stack = [(u, False)]
        while stack:
            node, processed = stack.pop()
            if processed:
                processing_order.append(node)
                continue
            if visited[node]:
                continue
            visited[node] = True
            stack.append((node, True))
            # Process children in reverse to maintain order with stack
            for neighbor in reversed(adj[node]):
                if not visited[neighbor]:
                    stack.append((neighbor, False))

# Build reversed adjacency list
reversed_adj = [[] for _ in range(total_nodes)]
for u in range(total_nodes):
    for v_neighbor in adj[u]:
        reversed_adj[v_neighbor].append(u)

# Second pass to count SCCs
visited_rev = [False] * total_nodes
scc_count = 0

for node in reversed(processing_order):
    if not visited_rev[node]:
        scc_count += 1
        stack = [node]
        visited_rev[node] = True
        while stack:
            current = stack.pop()
            for neighbor in reversed_adj[current]:
                if not visited_rev[neighbor]:
                    visited_rev[neighbor] = True
                    stack.append(neighbor)

print("YES" if scc_count == 1 else "NO")
```