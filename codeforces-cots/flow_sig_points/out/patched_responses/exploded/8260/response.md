<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

The problem is about connecting three regions (states 1, 2, 3) on a grid map. The goal is to find the minimum number of road cells (.) that need to be built so that all states are connected. Roads can only be built on '.' cells. Also, cells with # cannot be built on.

So the main task is to connect all three states with the minimal number of roads. If it's impossible, output -1.

First, let's understand the requirements. The three states must form a connected component where any cell from any state can reach any other via passable cells (states' cells or built roads). The roads can only be built on '.' cells.

The initial setup ensures that each state is connected within itself. So the problem reduces to connecting the three states with roads, possibly through each other or via some intermediate roads.

Possible approaches:

1. Find the minimal roads needed to connect all three states. This could involve connecting pairs first, then the third, or connecting all three through a single path.

But how to model this? The problem resembles a minimum spanning tree (MST) scenario where each of the three states (or their connected regions) are nodes, and the edges are the minimal roads required to connect them. Then, the MST would connect all three with the minimal total roads.

Wait, but maybe there's a better way. For example, the minimal roads could be the sum of connecting two states (A to B) and then another (B to C), or maybe a scenario where all three are connected through a single central point (like a Steiner point).

So first, for each pair of states, compute the minimal number of roads needed to connect them. Then, the answer could be the sum of the two smallest such values (since connecting all three requires connecting each pair, but perhaps overlapping roads can be used). Alternatively, there might be a scenario where a single path connects all three states, which might be cheaper than pairwise connections.

So possible steps:

- For each pair of states (1-2, 1-3, 2-3), find the minimal roads required to connect them. Let these be d12, d13, d23.

- Then, the answer could be the minimum of (d12 + d13, d12 + d23, d13 + d23) minus the maximum of the three, but wait, that's not correct. Because if all three are connected via a single path, maybe the total is the sum of the two, but perhaps there's a scenario where a single road path connects all three, leading to a lower total.

Wait, no. Because if you connect all three via a single path, for example, a path that connects 1 to 2, and another that connects 2 to 3, but overlapping roads. But perhaps the optimal is the sum of the minimal roads for two pairs, or perhaps there's a path that connects all three with a lower total.

Alternatively, there's a scenario where all three can be connected through a common point. For example, a single road cell that connects all three regions. So the minimal roads would be the sum of the distances from each state to that point, minus overlaps.

But how do we model this?

So, the problem can be broken down into two possible approaches:

1. Connect two states first, then connect the third to the combined group. The total roads would be the sum of the two connections (d12 + d3_connected). But d3_connected could be the minimal roads from the third state to either of the two states or the existing roads.

But perhaps the minimal is min(d12 + d13 + d23 - max(d12, d13, d23), min(d12 + d13, d12 + d23, d13 + d23), ...). Not sure.

Alternatively, the optimal solution could be the minimum between:

a) The sum of the two minimal pairwise connections (like d12 + d23, assuming that the connection between 1 and 2 is via some path that can also help connect 3).

But maybe the two connections share some roads, which would allow the sum to be less than d12 + d23. However, in the problem statement, roads can be built once and used for multiple connections.

Wait, no. Once a road is built, it's part of the passable cells. So if, for example, we build roads to connect 1 and 2, then those roads can be used to connect 3 to either 1 or 2. So the third connection might be cheaper.

Alternatively, perhaps the minimal total is the sum of the two minimal pairs minus the maximum overlap, but this is getting complicated.

Alternatively, the answer is the minimum between:

- The sum of the minimal roads between each pair (but that's redundant, because connecting all three requires connecting all pairs, but maybe the sum is d12 + d13 + d23, but this is likely not the case as roads can be shared).

Alternatively, think of this as a graph where the nodes are the three states. We need to connect all three nodes. The edges are the minimal roads required to connect each pair. Then, the minimal spanning tree for this graph would be the sum of the two minimal edges. For example, if d12 is 2, d13 is 3, d23 is 4, then the MST would be 2 + 3 = 5. But maybe there's a better way by finding a point that connects all three states with a combined cost of d1_point + d2_point + d3_point - 2 (since the point is counted once, but roads can be built once and used for all three).

So the problem is to compute both possibilities and take the minimal.

So, the steps could be:

1. Compute the minimal roads for each pair (d12, d13, d23).

2. Compute the minimal roads to connect all three via a single common cell. That is, find a cell (could be a '.' cell) such that the sum of the minimal roads from each state to this cell is the smallest possible. Then, subtract 2 if the cell is counted three times (since building roads from all three to the same cell would merge into a single path).

Wait, for example, if each state has a path to the same cell, then the roads built would be the sum of the distances (number of '.' cells needed) from each state to that cell. But if all three paths meet at that cell, then the total roads would be (d1 + d2 + d3), where d1 is the distance from state 1 to the cell, etc. But since the cell itself is counted once, perhaps the actual total is (d1 + d2 + d3 - 2), assuming that the cell is included in all three paths (since each path requires the cell to be built once, but it's built once, not three times).

But how?

For example, suppose the three states can reach the same cell with minimal roads of a, b, c respectively. Then, the roads needed are the sum a + b + c, but the common cell is only built once. So the total is (a + b + c - 2), because each of a, b, c counts the cell (so 3 times), but it's only built once. So subtracting 2.

But how to compute this? For each cell in the grid, calculate the minimal distance from each state to that cell (if possible), then compute a + b + c - 2. Take the minimal such value over all cells.

So the overall minimal answer would be the minimum between:

- The sum of the two minimal pairwise distances (d12 + d13 + d23 minus the maximum pairwise distance, since MST picks the two smallest)

Wait, no. The MST for three nodes is the sum of the two smallest edges. For example, if the three pairwise distances are 2, 3, 4, then the MST would have sum 2 +3 =5. So that's one option.

The other option is the minimal a + b + c - 2, where a, b, c are the distances from each state to some common cell.

So the answer is the minimum between the MST sum (sum of two smallest pairwise distances) and the minimal (a + b + c - 2) over all possible cells.

Then, the final answer is the minimal of these two options, provided all the required connections are possible. If any of the options is impossible, then we need to consider the possible ones.

So first, we need to compute for each pair of states the minimal number of roads needed to connect them. Then, compute the minimal a + b + c - 2 for all cells. Then, the answer is the minimal between these two approaches, or -1 if none of them is possible.

But how to compute the minimal pairwise distances between states?

For each pair, say 1 and 2, we need to find the minimal number of roads (.) cells that must be built so that there's a path from any cell of 1 to any cell of 2 via passable cells (which include their own cells and the built roads). So the minimal roads required for 1 and 2 is the minimal number of '.' cells that form a path connecting the two regions.

Wait, but how?

Alternatively, for each pair of states (A and B), the minimal roads needed to connect them is the minimal number of '.' cells that need to be built to create a path between any cell of A and any cell of B. Because once such a path exists, all cells of A and B are connected (since each state is initially connected).

So this is equivalent to finding the shortest path between the two regions, where the path consists of '.' cells. Each cell in the path contributes 1 to the count (since they need to be built). So the minimal roads between A and B is the length of the shortest such path (number of '.' cells in the path).

But how to compute that? For each pair, perform a multi-source BFS, where the sources are all cells of A, and we want to find the minimal path (in terms of number of '.' cells) that reaches any cell of B. But during BFS, the allowed steps are '.' cells (since they need to be built) and the state cells (since they are already passable).

Wait, but the path can pass through state cells (their own or other states') without building roads. Because the states are already connected. So when connecting A and B, the path can go through A's cells, B's cells, or other states' cells (like C's), but the road cells (.) must be built along the path.

Wait, the passable cells are the state cells (1, 2, 3) and the roads that are built (the '.' cells that we choose to build). So for connecting A and B, we can use any existing passable cells (state cells of any state, and built roads). But since the roads are not built yet, the only passable cells initially are the state cells. So the path between A and B can be through their own cells, but perhaps the minimal path is through some '.' cells that need to be built.

So, when finding the minimal roads between A and B, the path can consist of:

- Moving through A's cells (no cost, since they are already passable)
- Moving through B's cells (no cost)
- Moving through '.' cells (each such cell adds 1 to the cost, since we have to build it)
- Moving through other state's cells (like 3's cells). But in that case, those cells are passable (since they are part of their own state), so moving through them is allowed and adds 0 to the cost. However, building roads on those cells is not possible (they are part of a state, not '.'). So the path can use other state's cells as passable, but you don't build roads there.

So the problem is to find a path from any A cell to any B cell, where the path can go through any passable cells (state 1, 2, 3, or built '.' roads). But since the roads are not built yet, the only allowed steps (without building) are the state cells. The '.' cells must be built (i.e., added to the road count) to be passable.

Wait, no. The '.' cells are not passable unless we build roads on them. So in the initial state (before building any roads), the passable cells are only the state cells (1, 2, 3). Roads ('.') are only passable if we build them.

So when trying to connect A and B, any path between them must consist of state cells (of any of the three states) and '.' cells that are built. So each '.' cell in the path contributes 1 to the cost. State cells (1, 2, 3) can be traversed for free, as they are already passable.

So, the minimal cost (number of roads to build) to connect A and B is the minimal number of '.' cells along any path from A to B that uses state cells (any) and '.' cells (which must be built).

Therefore, for each pair (A, B), the minimal roads required is the minimal number of '.' cells in any path connecting A and B, where the path can go through any state's cells (since they are passable) and '.' cells (which must be built, hence counted).

So to compute the minimal roads between A and B, we can model this as a BFS where the cost is the number of '.' cells along the path. Each state cell (1, 2, 3) can be traversed with cost 0. Each '.' cell contributes 1 to the cost. We need to find the minimal cost from any A cell to any B cell.

Yes. So for each pair (A, B), perform a Dijkstra's algorithm (since the edges have varying weights) where the priority is the sum of '.' cells along the path. Alternatively, since moving to a state cell (any) is free, and moving to a '.' cell adds 1, we can model this as a BFS where the queue is ordered by the current cost (so a 0-1 BFS).

Wait, yes. Because the transitions can have cost 0 (moving to a state cell) or 1 (moving to a '.' cell). So for each cell in the grid, when moving to a neighbor:

- If the neighbor is a state cell (1, 2, 3), then the cost to move there is 0. So this can be added to the front of the queue (since it's a 0-weight edge).

- If the neighbor is a '.' cell, then the cost increases by 1. So this is a 1-weight edge, added to the back.

- If the neighbor is a '#', then it's blocked and cannot be moved into.

So for each pair (A, B), we can perform a 0-1 BFS starting from all cells of A, and find the minimal cost to reach any cell of B.

This will give the minimal number of roads needed to connect A and B.

Similarly for the other pairs.

Then, for the three pairs, compute d12, d13, d23.

Now, for the other part: finding a common cell where the sum of the minimal roads from each state to that cell is a + b + c, and subtract 2 (since the cell is counted once in each a, b, c, but we only build it once). So the total roads would be (a + b + c - 2).

So for each cell (i, j) in the grid, we need to compute the minimal cost (roads) to reach it from each state. Then, for that cell, if all three are reachable (i.e., from state 1, state 2, state 3), then compute (a + b + c - 2). The minimal of these values across all cells is another candidate for the answer.

So how to compute this?

For each of the three states, perform a BFS (0-1 BFS again) to compute the minimal cost (number of '.' cells) from any state cell to every other cell. Then, for each cell (i,j), the sum of the three minimal costs (from each state) minus 2 is a possible candidate.

So steps:

1. Precompute the minimal distances from each state to every cell. So for state 1, compute for each cell the minimal cost (roads) to reach that cell from any state 1 cell. Similarly for states 2 and 3.

2. For each cell (i,j), if it's accessible from all three states (i.e., the distances from each state are not infinite), compute the sum (d1[i][j] + d2[i][j] + d3[i][j] - 2). The minimal of these across all cells is a candidate for the answer.

3. The other candidates are the pairwise sums (d12 + d13, d12 + d23, d13 + d23), and take the minimal of those.

The overall answer is the minimal between all these candidates. If none of the candidates is possible (e.g., some d12 is infinity, and the common cell approach is also impossible), then output -1.

So now, the plan is:

- For each of the three states, perform a 0-1 BFS to find the minimal roads required to reach each cell.

- For each pair (A,B), perform a 0-1 BFS starting from A's cells to find the minimal cost to reach any B cell. This gives dAB.

- Compute the three pairwise distances (d12, d13, d23).

- Compute the minimal possible (a + b + c - 2) for all cells.

- The answer is the minimum between the pairwise sum (d12 + d13 + d23 - max(d12, d13, d23)) [no, wait, the MST is the sum of the two smallest edges], and the minimal common cell sum.

Wait, the pairwise approach is to take the sum of the two minimal pairwise distances. For example, if d12 is the smallest, then d12 + d13 (assuming d13 is the next smallest), etc. So the MST sum is the sum of the two smallest of d12, d13, d23.

Wait, no. For three nodes, the MST has exactly two edges. So the sum is the sum of the two edges with the smallest sum. For example, for three nodes A, B, C, the MST is the minimum of (AB + AC, AB + BC, AC + BC). But the minimal of these is the sum of the two smallest edges. So the MST sum is (sum of all three pairwise distances) minus the largest pairwise distance. Because the sum of the two smallest is (sum all three) - max.

Wait, no. Let's say d12 = 2, d13 = 3, d23 = 4. Then the MST would take d12 + d13 =5. So sum is 2 +3=5. Alternatively, if the three distances are 2, 3, 5. Then sum is 2+3=5.

So the MST sum is the sum of the two smallest edges.

So the pairwise approach is to take the minimal sum of two of the pairwise distances, provided all three are connected. But if one of the pairs cannot be connected, then this approach is invalid.

So, for the pairwise approach, the answer is the sum of the two smallest pairwise distances. If any of the three pairwise distances is infinity, then this approach is not possible.

Now, the problem is to compute all the required distances.

Now, considering the constraints (n and m up to 1000), each BFS is O(n*m). Since there are three states, three pairwise BFS, and three single-state BFS (for the common cell approach), the total time would be 3 (single state) +3 (pair) + ... ?

Wait, for the three pairwise BFS (like between 1 and 2, 1 and 3, 2 and 3), each BFS is multi-source (starting from all state 1 cells and finding the minimal distance to any state 2 cell). So each pairwise BFS is O(nm).

Then, for the three single-state BFS (for each state, compute the minimal distance from any state cell to every other cell), each is O(nm). So total BFS steps would be 3 (single-state) + 3 (pair) =6 BFS operations. Each BFS is O(nm) time and space.

But for n and m up to 1e3, 1e3 *1e3 is 1e6 cells. For each BFS, we need to process each cell once, with a deque-based approach for 0-1 BFS, which is efficient. So 6 BFS passes would be manageable.

But let's check:

Each BFS for a single state (e.g., state 1) will compute for each cell the minimal roads needed to reach that cell from state 1. Similarly for pairs.

So, for each cell (i,j), during the BFS for state 1, the cost is the minimal number of roads ('.' cells) needed to build to reach (i,j) from any state 1 cell.

Now, the steps to code:

1. Read the input grid.

2. For each state (1, 2, 3), collect their coordinates.

   Also, for each pair (A, B), collect their coordinates.

3. For each state, perform a 0-1 BFS to compute the minimal cost (roads) to reach each cell from any cell of that state.

   Let's call these d1, d2, d3.

4. For each pair (A, B), perform a 0-1 BFS starting from all cells of A, and find the minimal cost to reach any cell of B. This gives dAB.

5. Compute the three pairwise distances: d12, d13, d23.

6. Compute the possible MST sum: pairwise_sum = min(d12 + d13, d12 + d23, d13 + d23). But if any of the pairwise distances is infinity, this sum is invalid.

7. Compute the common cell sum: For each cell (i,j), if d1[i][j], d2[i][j], d3[i][j] are all finite, compute sum = d1[i][j] + d2[i][j] + d3[i][j] - 2. Keep track of the minimal such sum.

8. The answer is the minimal between the pairwise_sum and the common cell sum, provided they are possible. If none are possible, output -1.

So, let's handle the code.

But first, how to represent the grid. The grid is up to 1000x1000, which is manageable.

Now, implementing the 0-1 BFS:

The 0-1 BFS is suitable for graphs where edges have weights 0 or 1. The deque is used to process nodes in order of their distance. Nodes with 0-weight edges are added to the front of the deque, and 1-weight edges are added to the back.

For each state, say state 1, the initial queue is all cells that belong to state 1, with a distance of 0. Then, for each cell, we explore its neighbors. If the neighbor is a state cell (1, 2, 3), then moving to it has cost 0. If the neighbor is '.', moving to it has cost 1. '#' is blocked.

Wait, but during the BFS for state 1, the passable cells are state cells (1, 2, 3) and '.' that have been built. But in this BFS, the '.' cells are considered as possible steps, but each such step adds 1 to the cost (since building it). The state cells are passable for free.

So for the BFS for state 1:

- Start with all state 1 cells (distance 0).

- For each cell in the queue:

   - Check all four directions.

   - For each neighbor:

      - if it's a state cell (any of 1, 2, 3), then if not visited, enqueue to front with same distance.

      - if it's '.', then enqueue to back with distance+1.

      - if it's '#', skip.

This way, the BFS finds the minimal cost (number of '.' cells) to reach each cell from state 1.

But for the pairwise BFS (like between 1 and 2), the same approach applies. The BFS starts from all state 1 cells, and we want to find the minimal cost to reach any state 2 cell.

So for the pairwise BFS between 1 and 2:

- Start with all state 1 cells (distance 0).

- For each cell processed, if it's a state 2 cell, return the current distance.

But since we're doing BFS, once any state 2 cell is found, that's the minimal distance.

Wait, but how do we handle this? Because during the BFS, we process cells in order of their distance. So the first time we encounter a state 2 cell, that's the minimal distance.

So during the BFS, as soon as a state 2 cell is found, we can return that distance.

But what if the BFS needs to explore other cells that might have a shorter path to another state 2 cell? No, because the BFS processes cells in order of their distance, the first occurrence is the minimal.

So the pairwise BFS can be optimized to stop as soon as a state 2 cell is found.

But for code purposes, it's easier to compute the distance for all cells and then find the minimal distance to any state 2 cell.

But given that n and m are up to 1e3, this could be time-consuming. So perhaps during the BFS, once a state 2 cell is encountered, we can return the current distance immediately.

Alternatively, perform the BFS for all cells, and then collect the minimal distance from any state 2 cell.

But given that the BFS for pairwise can be up to 1e6 cells, but in practice, it's manageable.

But let's proceed.

Now, code steps:

First, read the grid.

Then, collect the positions of each state.

For example:

positions_1 = list of all (i,j) where grid[i][j] == '1'

Similarly for 2 and 3.

Then, perform three 0-1 BFS for each state (to compute d1, d2, d3):

Each of these will compute for each cell (i,j) the minimal number of roads ('.' cells) needed to reach that cell from any state 1 cell. State 2 and 3 cells are considered passable, so moving through them doesn't add to the cost.

Then, perform three pairwise BFS (between 1 and 2, 1 and 3, 2 and 3).

Each pairwise BFS starts from all cells of the first state, and finds the minimal roads to reach any cell of the second state.

So for each pairwise BFS:

- Initialize a distance array with infinity.

- Enqueue all cells of the first state with distance 0.

- Process the queue as per 0-1 BFS.

- For each cell processed, check if it's part of the second state. If yes, update the minimal distance and break early (if possible).

Once the BFS is complete, the minimal distance to any second state cell is the value for d12, etc.

Once all pairwise distances are computed, compute the pairwise_sum as the sum of the two smallest pairwise distances.

If any pairwise distance is infinity, then the pairwise_sum is invalid.

Then, compute the common cell sum. For each cell (i,j):

If d1[i][j], d2[i][j], d3[i][j] are all finite, compute sum = d1[i][j] + d2[i][j] + d3[i][j] - 2. Keep track of the minimal such sum.

Now, the minimal answer is the minimum between pairwise_sum and the common cell sum.

But also, we have to consider that both options might be possible. So the overall answer is the minimum between all possible candidates.

Now, code structure:

Implement a helper function to perform the 0-1 BFS for a single state (to compute d1, d2, d3).

Implement another helper function to perform the pairwise BFS (to compute d12, d13, d23).

But for the pairwise BFS, the code is similar to the single-state BFS, but the targets are the other state's cells.

Alternatively, for the pairwise BFS, we can proceed as follows:

Function pairwise_bfs(start_states, end_states, grid):

   Initialize a deque.

   Create a distance matrix filled with infinity.

   For each cell in start_states:

      distance[i][j] = 0

      add to deque.

   while deque not empty:

      i, j = deque.popleft()

      if (i,j) is in end_states:

          return distance[i][j]

      for each direction:

          ni, nj = new coordinates

          if out of bounds or grid[ni][nj] is '#', skip.

          new_cost = distance[i][j] + (1 if grid[ni][nj] == '.' else 0)

          if grid[ni][nj] in {'1', '2', '3'}:

              # moving to state cell, cost remains same as current distance[i][j]

              new_cost = distance[i][j]

          else: # '.' cell, cost increases by 1

              new_cost = distance[i][j] + 1

          if new_cost < distance[ni][nj]:

              distance[ni][nj] = new_cost

              if new_cost == distance[i][j]: # 0 weight edge

                  deque.appendleft( (ni, nj) )

              else:

                  deque.append( (ni, nj) )

   after processing all cells:

   find the minimal distance among all end_states cells.

   if no end_states cells are reachable, return infinity.

But this code is incorrect. Because when moving to a state cell (1,2,3), the cost doesn't increase, regardless of the current cell's state.

Wait, the cost is the number of '.' cells that are built. So moving into a '.' cell requires building it, so cost increases by 1. Moving into a state cell (any) does not require building a road, so cost remains the same.

So the code should be:

For each neighbor cell (ni, nj):

   if cell is '#', skip.

   if cell is in {1, 2, 3}:

      new_cost = current distance.

   else (cell is '.'):

      new_cost = current distance + 1.

   if new_cost < distance[ni][nj], then update.

So in code, for each neighbor:

if grid[ni][nj] == '#':

   continue

if grid[ni][nj] in {'1', '2', '3'}:

   cost = distance[i][j]

else:

   cost = distance[i][j] + 1

if cost < distance[ni][nj]:

   update and add to deque.

So the code for the BFS functions is similar for both the single-state and pairwise BFS.

Thus, we can create a helper function that takes the start cells, and the grid, and returns the distance matrix. Then, for the pairwise BFS, after computing the distance matrix, we find the minimal distance among the end_states cells.

But for the pairwise BFS, since we are looking for the minimal distance to any end_state cell, perhaps during the BFS, once such a cell is found, we can return the distance immediately. Because the BFS processes nodes in order of their distance, so the first time we reach any end_state cell, that's the minimal distance.

So optimizing the pairwise BFS:

In the helper function, during the BFS processing, for each cell (i,j) that is dequeued, check if it's an end_state cell. If yes, return the current distance as the minimal.

This will save processing the entire grid when the answer is found early.

Now, for the code:

First, read the grid, then collect the positions for each state.

Then, for the pairwise BFS:

def compute_pairwise_distance(start_cells, end_cells, grid, n, m):

    from collections import deque

    INF = float('inf')

    dist = [[INF for _ in range(m)] for __ in range(n)]

    dq = deque()

    for (i,j) in start_cells:

        dist[i][j] = 0

        dq.append( (i,j) )

    dirs = [ (-1,0), (1,0), (0,-1), (0,1) ]

    while dq:

        i, j = dq.popleft()

        # Check if current cell is an end_cell

        if (i,j) in end_cells:

            return dist[i][j]

        for di, dj in dirs:

            ni = i + di

            nj = j + dj

            if 0 <= ni < n and 0 <= nj < m:

                cell = grid[ni][nj]

                if cell == '#':

                    continue

                # compute cost

                if cell in {'1', '2', '3'}:

                    new_cost = dist[i][j]

                else: # '.' cell

                    new_cost = dist[i][j] + 1

                if new_cost < dist[ni][nj]:

                    dist[ni][nj] = new_cost

                    if new_cost == dist[i][j]: # 0 cost edge

                        dq.appendleft( (ni, nj) )

                    else:

                        dq.append( (ni, nj) )

    # After BFS, find the minimal distance among end_cells

    min_dist = INF

    for (i,j) in end_cells:

        if dist[i][j] < min_dist:

            min_dist = dist[i][j]

    return min_dist if min_dist != INF else INF

But storing the end_cells as a set for O(1) lookups would be better. But for 1e3 x 1e3 grid, end_cells can be up to 1e6, so checking (i,j) in end_cells (a set) is O(1).

Alternatively, during BFS processing, for each cell being dequeued, check if it's in the end_cells.

But if the end_cells are large, this could take O(1) for each check if stored as a set.

So in code:

start_cells and end_cells are stored as sets of tuples.

But for the code to be efficient, in the pairwise BFS function, once the dequeued cell is in end_cells, return the distance immediately.

Now, for the single-state BFS (compute d1, d2, d3), the code is similar, but we need to compute the distance to all cells, not just end_cells. So for example, d1[i][j] is the minimal cost to reach (i,j) from any state 1 cell.

Thus, the code for single-state BFS:

def compute_single_state_distances(state_cells, grid, n, m):

    from collections import deque

    INF = float('inf')

    dist = [[INF for _ in range(m)] for __ in range(n)]

    dq = deque()

    for (i,j) in state_cells:

        dist[i][j] = 0

        dq.append( (i,j) )

    dirs = [ (-1,0), (1,0), (0,-1), (0,1) ]

    while dq:

        i, j = dq.popleft()

        for di, dj in dirs:

            ni = i + di

            nj = j + dj

            if 0 <= ni < n and 0 <= nj < m:

                cell = grid[ni][nj]

                if cell == '#':

                    continue

                if cell in {'1', '2', '3'}:

                    new_cost = dist[i][j]

                else:

                    new_cost = dist[i][j] + 1

                if new_cost < dist[ni][nj]:

                    dist[ni][nj] = new_cost

                    if new_cost == dist[i][j]:

                        dq.appendleft( (ni, nj) )

                    else:

                        dq.append( (ni, nj) )

    return dist

Now, let's code the entire solution.

First, read the input.

n, m = map(int, input().split())

grid = [ list(input().strip()) for _ in range(n) ]

Then, collect the positions of each state.

state1 = []

state2 = []

state3 = []

for i in range(n):

    for j in range(m):

        c = grid[i][j]

        if c == '1':

            state1.append( (i,j) )

        elif c == '2':

            state2.append( (i,j) )

        elif c == '3':

            state3.append( (i,j) )

If any of these lists is empty, but the problem says it's guaranteed that each state has at least one cell. So no need to check.

Now, compute the pairwise distances.

But first, convert the state lists into sets for O(1) lookups.

s1 = set(state1)

s2 = set(state2)

s3 = set(state3)

Compute d12 = compute_pairwise_distance(state1, s2, grid, n, m)

Similarly for d13 and d23.

But the function needs to have start_cells and end_cells.

Wait, the function compute_pairwise_distance takes start_cells (the starting positions) and end_cells (a set of positions). So for d12, start_cells is state1 (the list of positions of state1), and end_cells is s2 (the set of state2 positions).

So:

d12 = compute_pairwise_distance(state1, s2, grid, n, m)

d13 = compute_pairwise_distance(state1, s3, grid, n, m)

d23 = compute_pairwise_distance(state2, s3, grid, n, m)

Similarly, compute the single-state distances:

d1 = compute_single_state_distances(state1, grid, n, m)

d2 = compute_single_state_distances(state2, grid, n, m)

d3 = compute_single_state_distances(state3, grid, n, m)

Now, compute the minimal common cell sum.

min_common = infinity

for i in range(n):

    for j in range(m):

        if d1[i][j] != INF and d2[i][j] != INF and d3[i][j] != INF:

            total = d1[i][j] + d2[i][j] + d3[i][j] - 2

            if total < min_common:

                min_common = total

But wait, why subtract 2? Because if the cell (i,j) is a '.' cell, then building it once contributes 1 to each of the three distances. So d1[i][j] includes this cell if it's on the path from state1 to (i,j), and similarly for d2 and d3. But when the cell is part of the road (built), it's counted once. So for example, if (i,j) is a '.' cell and is part of all three paths, then d1 includes it once (if the path to here goes through it), d2 includes it once, etc. But building this cell once would cover all three. So the total is d1 + d2 + d3 - 2 * 1 (since the cell is built once, but counted three times in the sum).

But wait, in the sum d1 + d2 + d3, each of these distances represents the number of '.' cells built to reach (i,j) from each state. But the roads built for d1, d2, and d3 may overlap. However, when connecting all three through (i,j), the roads needed are the union of the paths from each state to (i,j). So overlapping roads are counted once.

So the sum d1 + d2 + d3 may count some roads multiple times, but the actual required roads are the union of those roads. However, the problem requires that roads are built once, and thus the minimal possible is the sum minus the overlapping roads.

But how to calculate this? For example, if the path from state1 to (i,j) is a -> b -> c, and the path from state2 is c -> b -> a -> (i,j), then the roads a, b, c are counted in both paths. But the actual required roads are a, b, c once.

But how can we model this? It's tricky, but the approach taken in the problem is to assume that the common cell (i,j) is the meeting point. So the paths from each state to (i,j) are independent, and their roads are summed. However, if the cell (i,j) is a '.' cell, then it's built once, but counted in each of the three paths.

So for example, if (i,j) is '.' and each path from the states passes through it, then d1[i][j] = a (including this cell), d2[i][j] = b (including it), d3[i][j] = c (including it). The total roads would be a + b + c - 2, because this cell is counted three times in the sum, but built once (so subtract 2).

But if (i,j) is a state cell (say state1), then d1[i][j] is 0 (no roads needed), but d2 and d3 would have their own roads. So the sum would be 0 + d2 + d3, and no subtraction needed.

Wait, but the code for d1[i][j] for state1's own cell is 0 (since no roads needed). So if (i,j) is in state1, then d1[i][j] is 0, d2[i][j] is the roads needed to reach from state2 to this cell, and d3[i][j] is the roads needed from state3 to this cell.

In this case, the sum is 0 + d2 + d3. The roads built would be those needed to reach state1's cell from state2 and state3. But since the cell is part of state1's territory (passable), building roads along the path from state2 to this cell and state3 to this cell is required. But since state1's cell is already passable, the roads built are the paths from state2 and state3 to this cell.

So in this case, the sum would be d2[i][j] + d3[i][j]. There's no subtraction because the cell (i,j) is a state cell (no road built there), so each path's roads are added.

So the code subtracts 2 only if the cell (i,j) is a '.' cell. Because in that case, the cell is built once, but counted once in each path.

Wait, but how to determine whether the cell is a '.' or a state cell?

Ah, the code as written subtracts 2 regardless of the cell's type. But that's incorrect.

Wait, the subtraction depends on whether the cell (i,j) is a '.' cell. Because if it is, then building it once is required, but in the sum d1 + d2 + d3, it's counted three times. So the subtraction is 2. If the cell is a state cell, then it's already passable, so it's not counted in any of the d's, so no subtraction is needed.

But wait, in the single-state BFS for d1, the cell (i,j) being part of state1 will have d1[i][j] = 0. Similarly, if (i,j) is part of state2, then d2[i][j] =0.

So when (i,j) is a state cell (say, state1), then d1[i][j] is 0. The d2[i][j] and d3[i][j] would be the roads needed to reach this cell from state2 and state3.

So the sum is d2 + d3. But if (i,j) is a state cell, then it's not a '.' cell, so no subtraction is needed.

But if (i,j) is a '.' cell, then the sum is d1 + d2 + d3, but the cell is built once, so subtract 2.

So the code should check if the cell (i,j) is '.' or not.

But how?

In the code:

for each cell (i,j):

   if d1, d2, d3 are finite:

      if grid[i][j] == '.' :

          sum = d1[i][j] + d2[i][j] + d3[i][j] - 2

      else:

          sum = d1[i][j] + d2[i][j] + d3[i][j]

      min_common = min(min_common, sum)

So this way, we subtract 2 only if the cell is '.'.

But how to implement this?

So in code:

min_common = INF

for i in range(n):

    for j in range(m):

        if d1[i][j] == INF or d2[i][j] == INF or d3[i][j] == INF:

            continue

        if grid[i][j] == '.' :

            current = d1[i][j] + d2[i][j] + d3[i][j] - 2

        else:

            current = d1[i][j] + d2[i][j] + d3[i][j]

        if current < min_common:

            min_common = current

Yes, this is correct.

So this handles both cases: whether the common cell is a '.' (requires subtraction) or a state cell (no subtraction).

Thus, the code for the common cell sum is:

min_common = INF

for i in range(n):

    for j in range(m):

        if d1[i][j] == INF or d2[i][j] == INF or d3[i][j] == INF:

            continue

        current = d1[i][j] + d2[i][j] + d3[i][j]

        if grid[i][j] == '.':

            current -= 2

        if current < min_common:

            min_common = current

Now, the answer is the minimal between:

- the pairwise_sum (sum of the two smallest pairwise distances)

- the min_common.

But need to check if any of these options are possible.

So for pairwise_sum:

pairwise_options = [d12 + d13, d12 + d23, d13 + d23]

pairwise_possible = [x for x in pairwise_options if x < INF]

if pairwise_possible:

    pairwise_min = min(pairwise_possible)

else:

    pairwise_min = INF

common_possible = min_common if min_common < INF else INF

Then, the answer is the minimal of pairwise_min and common_possible.

If both are INF, output -1.

Else, output the minimal of the two.

So code:

options = []

if d12 < INF and d13 < INF:

    options.append(d12 + d13)

if d12 < INF and d23 < INF:

    options.append(d12 + d23)

if d13 < INF and d23 < INF:

    options.append(d13 + d23)

pairwise_min = min(options) if options else INF

common_min = min_common if min_common != INF else INF

ans = min(pairwise_min, common_min)

if ans == INF:

    print(-1)

else:

    print(ans)

But in code, pairwise_min is the minimal of the possible pairwise sums. So:

if options is empty (all pairwise sums are impossible), then pairwise_min is INF.

Thus, the final answer is the minimal between pairwise_min and common_min.

Now, code.

Putting it all together:

But due to the size of the code, we need to manage the helper functions and variables.

But let's proceed.

So, the code will be:

Read the grid.

Collect state positions.

Compute d12, d13, d23.

Compute d1, d2, d3.

Compute common_min.

Compute pairwise_min.

Choose the minimal between them.

But the problem is the time and memory constraints.

For n=1000 and m=1000, each distance matrix is 1e6 elements. Three distance matrices (d1, d2, d3) will take 3 * 1e6 * 4 bytes (assuming integers), which is about 12MB, manageable.

The BFS for each of the three states and three pairs is O(nm), which for 6 passes is 6e6 operations, acceptable.

Now, code:

But in Python, using lists for distance matrices can be memory-efficient.

Now, code.

But note that the pairwise BFS may have INF if the states can't be connected.

So here's the complete code:

Read the input.

Collect the positions of each state.

Compute d12, d13, d23 using pairwise BFS.

Compute d1, d2, d3 using single-state BFS.

Compute the common_min.

Compute pairwise options.

Compare and output.

But for the helper functions, in Python, it's better to pass the grid, n, m, etc.

Now, code:

Read input:

n, m = map(int, input().split())

grid = [ list(input().strip()) for _ in range(n) ]

Collect state positions:

state1 = [ (i,j) for i in range(n) for j in range(m) if grid[i][j] == '1' ]

state2 = [ (i,j) for i in range(n) for j in range(m) if grid[i][j] == '2' ]

state3 = [ (i,j) for i in range(n) for j in range(m) if grid[i][j] == '3' ]

s1 = set(state1)

s2 = set(state2)

s3 = set(state3)

Compute pairwise distances:

from collections import deque

INF = float('inf')

def compute_pairwise_bfs(start_states, end_set, grid, n, m):

    dist = [[INF]*m for _ in range(n)]

    dq = deque()

    for (i,j) in start_states:

        dist[i][j] = 0

        dq.append( (i,j) )

    dirs = [ (-1,0), (1,0), (0,-1), (0,1) ]

    while dq:

        i, j = dq.popleft()

        if (i,j) in end_set:

            return dist[i][j]

        for di, dj in dirs:

            ni = i + di

            nj = j + dj

            if 0 <= ni < n and 0 <= nj < m:

                cell = grid[ni][nj]

                if cell == '#':

                    continue

                if cell in {'1', '2', '3'}:

                    new_cost = dist[i][j]

                else:

                    new_cost = dist[i][j] + 1

                if new_cost < dist[ni][nj]:

                    dist[ni][nj] = new_cost

                    if new_cost == dist[i][j]:

                        dq.appendleft( (ni, nj) )

                    else:

                        dq.append( (ni, nj) )

    min_dist = INF

    for (i,j) in end_set:

        if dist[i][j] < min_dist:

            min_dist = dist[i][j]

    return min_dist if min_dist != INF else INF

d12 = compute_pairwise_bfs(state1, s2, grid, n, m)

d13 = compute_pairwise_bfs(state1, s3, grid, n, m)

d23 = compute_pairwise_bfs(state2, s3, grid, n, m)

Compute d1, d2, d3:

def compute_single_state_distances(states, grid, n, m):

    dist = [[INF]*m for _ in range(n)]

    dq = deque()

    for (i,j) in states:

        dist[i][j] = 0

        dq.append( (i,j) )

    dirs = [ (-1,0), (1,0), (0,-1), (0,1) ]

    while dq:

        i, j = dq.popleft()

        for di, dj in dirs:

            ni = i + di

            nj = j + dj

            if 0 <= ni < n and 0 <= nj < m:

                cell = grid[ni][nj]

                if cell == '#':

                    continue

                if cell in {'1', '2', '3'}:

                    new_cost = dist[i][j]

                else:

                    new_cost = dist[i][j] + 1

                if new_cost < dist[ni][nj]:

                    dist[ni][nj] = new_cost

                    if new_cost == dist[i][j]:

                        dq.appendleft( (ni, nj) )

                    else:

                        dq.append( (ni, nj) )

    return dist

d1 = compute_single_state_distances(state1, grid, n, m)

d2 = compute_single_state_distances(state2, grid, n, m)

d3 = compute_single_state_distances(state3, grid, n, m)

Compute common_min:

min_common = INF

for i in range(n):

    for j in range(m):

        if d1[i][j] == INF or d2[i][j] == INF or d3[i][j] == INF:

            continue

        current = d1[i][j] + d2[i][j] + d3[i][j]

        if grid[i][j] == '.':

            current -= 2

        if current < min_common:

            min_common = current

Compute pairwise_min:

pairwise_options = []

if d12 != INF and d13 != INF:

    pairwise_options.append(d12 + d13)

if d12 != INF and d23 != INF:

    pairwise_options.append(d12 + d23)

if d13 != INF and d23 != INF:

    pairwise_options.append(d13 + d23)

pairwise_min = min(pairwise_options) if pairwise_options else INF

ans = min(pairwise_min, min_common)

if ans == INF:

    print(-1)

else:

    print(ans)

But this code has some possible optimizations.

For example, in the compute_pairwise_bfs function, when the end_set is large, checking (i,j) in end_set for each dequeued cell can be expensive. However, in Python, sets of tuples are hash tables, and checking membership is O(1).

But in the worst case, for each cell in the BFS, we check if it's in the end_set. For n=1e3 and m=1e3, this is 1e6 checks. For each check, it's O(1), so manageable.

Another optimization: in the pairwise BFS, once any cell in the end_set is found, return the distance immediately.

This is what the code does in the line:

if (i,j) in end_set:

    return dist[i][j]

So the first time any end_set cell is dequeued, return its distance, which is the minimal possible.

This can save a lot of time.

Now, let's test this code against the sample inputs.

Sample Input 1:

4 5

11..2

#..22

#.323

.#333

Sample Output: 2.

Let's see what the code would compute.

The grid has state 1 cells in the first two columns of the first row.

State 2 cells are in the last column of the first row, the last two columns of the second row, and third row's third column (but that's part of state3).

State3 cells are in the third row's third column onwards, and fourth row's third column onwards.

The optimal path is to build two roads: perhaps connecting 1 and 3 via some '.' cells, and then 3 and 2 are already connected.

But the pairwise distances:

d12: the minimal roads between state1 and state2.

Looking at the first row, state1 is in positions (0,0) and (0,1). State2 is in (0,4). To connect them, the path can be (0,1) → (0,2) → (0,3) → (0,4). These are '.' cells, so cost is 3. But in the sample output, the answer is 2, so perhaps there's a better path.

Alternatively, the code may find a different path.

Wait, but the sample output is 2, which suggests that there's a way to connect all three with two roads.

Perhaps the common cell approach is better here.

But let's proceed.

In any case, the code should compute the correct answer.

Sample Input 2:

1 5

1#2#3

Output: -1.

The states are 1, 2, 3 separated by #. There's no way to connect them.

The pairwise distances between 1-2 is blocked by #, d12 is INF. Similarly for other pairs. Also, the common cell approach would not find any cell reachable by all three.

So the code returns -1.

Thus, the code should handle these cases.

Now, the code seems correct. But need to handle the case where the common cell is a state cell.

For example, suppose the three states are connected through a state cell of state1. Then, the sum would be d2[i][j] + d3[i][j], since d1[i][j] is 0, and the cell is not a '.', so no subtraction.

Thus, the code correctly handles this.

Thus, the code should be correct.
</think>

```python
import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(n)]
    
    state1 = []
    state2 = []
    state3 = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                state1.append((i, j))
            elif grid[i][j] == '2':
                state2.append((i, j))
            elif grid[i][j] == '3':
                state3.append((i, j))
    s1 = set(state1)
    s2 = set(state2)
    s3 = set(state3)
    
    INF = float('inf')
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    
    def compute_pairwise(start_states, end_set):
        dist = [[INF]*m for _ in range(n)]
        dq = deque()
        for (i,j) in start_states:
            dist[i][j] = 0
            dq.append((i,j))
        while dq:
            i, j = dq.popleft()
            if (i,j) in end_set:
                return dist[i][j]
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    cell = grid[ni][nj]
                    if cell == '#':
                        continue
                    new_cost = dist[i][j] + (0 if cell in '123' else 1)
                    if new_cost < dist[ni][nj]:
                        dist[ni][nj] = new_cost
                        if new_cost == dist[i][j]:
                            dq.appendleft((ni, nj))
                        else:
                            dq.append((ni, nj))
        min_dist = INF
        for (i,j) in end_set:
            if dist[i][j] < min_dist:
                min_dist = dist[i][nj]
        return min_dist if min_dist != INF else INF
    
    d12 = compute_pairwise(state1, s2)
    d13 = compute_pairwise(state1, s3)
    d23 = compute_pairwise(state2, s3)
    
    def compute_single(states):
        dist = [[INF]*m for _ in range(n)]
        dq = deque()
        for (i,j) in states:
            dist[i][j] = 0
            dq.append((i,j))
        while dq:
            i, j = dq.popleft()
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    cell = grid[ni][nj]
                    if cell == '#':
                        continue
                    new_cost = dist[i][j] + (0 if cell in '123' else 1)
                    if new_cost < dist[ni][nj]:
                        dist[ni][nj] = new_cost
                        if new_cost == dist[i][j]:
                            dq.appendleft((ni, nj))
                        else:
                            dq.append((ni, nj))
        return dist
    
    d1 = compute_single(state1)
    d2 = compute_single(state2)
    d3 = compute_single(state3)
    
    min_common = INF
    for i in range(n):
        for j in range(m):
            if d1[i][j] != INF and d2[i][j] != INF and d3[i][j] != INF:
                current = d1[i][j] + d2[i][j] + d3[i][j]
                if grid[i][j] == '.':
                    current -= 2
                if current < min_common:
                    min_common = current
    
    pairwise_min = INF
    options = []
    if d12 != INF and d13 != INF:
        options.append(d12 + d13)
    if d12 != INF and d23 != INF:
        options.append(d12 + d23)
    if d13 != INF and d23 != INF:
        options.append(d13 + d23)
    if options:
        pairwise_min = min(options)
    
    ans = min(pairwise_min, min_common)
    print(-1 if ans == INF else ans)

if __name__ == "__main__":
    main()
```