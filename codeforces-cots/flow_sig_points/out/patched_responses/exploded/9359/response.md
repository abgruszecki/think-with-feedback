<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

The problem is about finding the minimum number of cells the Evil Witch needs to block so that Vasya can't reach the treasure. The grid is n x m, and Vasya can only move right or down. The start is (1,1), and the end is (n,m). The cells (1,1) and (n,m) are always passable. The Witch can block any other cells except these two. The task is to find the minimal number of cells to block so that there's no path from start to end using only right and down moves.

Hmm, the key here is that Vasya's movement is restricted to right and down. So the problem is similar to finding a minimal vertex cut in a directed acyclic graph (DAG) where edges are right and down moves. But since the movement is only right or down, perhaps there's a pattern or a way to model this more efficiently.

In graph theory terms, the minimal number of nodes to remove to disconnect two nodes is equal to the maximum number of node-disjoint paths (Menger's theorem, but for node cuts). So if we can find the maximum number of such node-disjoint paths from start to end, then the minimal cut is that number. But how do we compute that here?

Wait, but in this problem, each path can't share any cells except start and end, because blocking a cell removes it from all paths. So the minimal number of cells to block is the number of node-disjoint paths. Wait no, Menger's theorem says that the minimal vertex cut (for two nodes) is equal to the maximum number of vertex-disjoint paths between them. So the answer should be the maximum number of such paths. Because if there are k node-disjoint paths, then the Witch needs to block at least k nodes (one from each path) to block all paths. And the minimal required is exactly k.

So the problem reduces to finding the maximum number of vertex-disjoint paths from (1,1) to (n,m) where each path consists of right and down moves. Then the answer is that number. But how to compute this?

But how to model the paths. Let's think about the grid and possible paths. Since the paths can only move right or down, the structure of the paths might have certain properties.

Another way to approach this: The problem is equivalent to finding the minimal number of cells that lie on all possible paths. If there's a cell that is part of every possible path, then blocking that cell would stop all paths. So the minimal answer would be 1. If there are two cells such that every path goes through at least one of them, then the answer is 2, and so on.

Alternatively, the answer is the number of such critical points in the grid that every path must go through them. But how to find these points?

Alternatively, perhaps the problem can be transformed into a graph where nodes are the cells, and edges are the possible moves. Then, we can model the problem as finding the minimal s-t vertex cut in this graph, where s is (1,1) and t is (n,m). The minimal vertex cut is the answer.

But how to compute this for large grids (up to 1e6 cells)? Standard algorithms for vertex cuts are not feasible for such large sizes. So we need a smarter approach.

Wait, considering that all paths are from (1,1) to (n,m) moving only right and down, each path can be represented as a sequence of steps. Let's think about layers. For example, the sum of the coordinates (i + j) determines the layer. Each step increases this sum by 1. All paths go through layers 2, 3, ..., (n+m-1). The start is at (1,1) which is layer 2, and the end is layer (n+m). Wait, no. (1,1) is i=1, j=1: sum is 2. Then each move either increases i by 1 (sum increases by 1) or j by 1 (sum increases by 1). So each path is a sequence of layers from 2 to (n+m). The end is (n,m), sum is n+m.

So for each layer k (from 2 to (n+m-1)), the number of cells in that layer that are on some path from (1,1) to (n,m) and are passable (i.e., not blocked by forest). Then, the minimal number of cells to block is the minimum over all layers (from 2 to n+m-1) of the number of cells in that layer that are on some path. Because if a layer has x cells in it that are on some path, then the Witch can block all x-1 cells except one, but to ensure that all paths are blocked, she must block all cells in that layer, but that's not efficient. Wait, maybe not. Wait, if there's a layer where there are only y cells that are on any path, then the minimal number of cells to block is y. Because in that layer, every path must pass through one of these cells. So if the Witch blocks all y cells in that layer, then no path can exist. But the minimal k is the minimal such y across all layers.

Wait, that's the key insight! Let me rephrase.

Each path from (1,1) to (n,m) must pass through exactly one cell in each layer between 2 and (n+m). So for each layer k (sum i+j), the number of cells in that layer that are reachable (i.e., part of some path from start to end) is the number of cells in that layer that are on any possible path. The minimal number of such cells across all layers is the answer. Because if there's a layer where there are only 2 cells, then the Witch can block those 2, but wait, no. Wait, the minimal number of cells to block is the minimal count of cells in any layer. Because in that layer, every path must pass through one of those cells. So if the Witch blocks all of them except one, then there's a way. Wait, no. Wait, the idea is that the minimal number of cells to block is the minimal number of cells in any such layer. Because if there's a layer with x cells in it, then by blocking all x cells in that layer, Vasya can't proceed. But since the Witch can't block cells (1,1) or (n,m), but all other cells can be blocked. So the answer is the minimal x over all layers (from 2 to n+m-1) of the number of cells in that layer that are part of some path.

Wait, for example, in the first sample input:

2 2

..

..

The grid is 2x2. The possible paths are right then down, or down then right. The layers are:

sum=2: (1,1) only.

sum=3: (1,2) and (2,1).

sum=4: (2,2) only.

So the layers between 2 and 4-1=3 are sum 3. The sum 3 has two cells. So the minimal count is 2. So the answer is 2, which matches the first sample.

In the second sample:

4x4 grid. The layers sum=2, 3, ..., 8. The layers sum=3 to sum=7 (since 4+4=8, sum up to 7). So the minimal count among these layers is the answer.

Looking at the sample output of 1, that suggests that there's a layer with only 1 cell. So the answer is 1.

So this approach seems to hold.

So the plan is:

1. For each cell (i,j), determine whether it is part of any path from (1,1) to (n,m) using only right and down moves, and not passing through any blocked cells (original grid's blocked cells). Because the original grid may have blocked cells, which are not passable. So even if a cell is not blocked (i.e., '.'), but it's impossible to reach it from (1,1) moving right/down, then it's not part of any path.

2. For each layer (sum of i+j), count the number of cells in that layer that are reachable from (1,1) and can reach (n,m) (i.e., are on some path from (1,1) to (n,m)).

3. The minimal such count across all layers (excluding the first and last layers, which are (1,1) and (n,m)) is the answer. But wait, the first layer is sum 2 (i=1, j=1). The layers we consider are those between sum 2+1=3 and sum (n+m-1). Wait, no. Let me see: each path starts at (1,1) (sum 2) and ends at (n,m) (sum n+m). The layers in between are sum 3, 4, ..., (n+m-1). For each of these layers, we count the number of cells that are on some path. The minimal of these counts is the answer. Because blocking all cells in that layer would require exactly that number of blocks, but since the Witch wants the minimal, the answer is the minimal count across those layers.

So the steps are:

- Precompute for each cell (i,j) whether it can be reached from (1,1) by moving only right and down, and whether the cell can reach (n,m) by moving right and down. Because a cell is on some path if and only if it is reachable from (1,1) via right/down, and can reach (n,m) via right/down.

So we can:

- Perform a forward BFS (or dynamic programming) from (1,1) moving right and down, marking cells reachable from start.

- Perform a backward BFS (or dynamic programming) from (n,m) moving left and up, marking cells that can reach the end.

The intersection of these two sets (cells reachable from start and can reach end) are the cells that are on some path from start to end.

Then, for each cell in this intersection (excluding (1,1) and (n,m)), we group them by their layer (i+j). For each such layer, count the number of cells. The minimal such count across all layers is the answer.

But how to compute reachability?

Since the movement is only right and down, for the forward pass, we can compute reachability using dynamic programming:

reachable_from_start[i][j] = (cell (i,j) is .) and (reachable_from_start[i-1][j] or reachable_from_start[i][j-1]), with the base case being reachable_from_start[1][1] = True.

Similarly, for the backward pass:

reachable_to_end[i][j] = (cell (i,j) is .) and (reachable_to_end[i+1][j] or reachable_to_end[i][j+1]), with the base case reachable_to_end[n][m] = True.

But since the grid can be up to 1e6 cells (n*m <= 1e6), we need an efficient way to compute this. Both passes can be done in O(nm) time, which is acceptable.

Once we have both reachability matrices, the cells that are on some path are those that are reachable from start and can reach the end. Then, for each such cell (excluding start and end), compute their i + j. The layers between 3 (since 1+1=2 is the start, next is sum 3) and (n+m-1) (since end is sum n+m). For each layer in this range, compute the count of cells in this layer. The minimal such count is the answer.

But wait, what if there's a layer with zero cells? Then the answer is zero. But since the problem states that the start and end are passable, but perhaps there's no path. For example, if the grid is already blocked. But the input says that (1,1) and (n,m) are empty, but there may be no path. So in such a case, the answer is zero. But according to the problem statement, the input is such that initially, there exists at least one path? Because otherwise, the answer is zero.

Wait, the problem statement says: "It's guaranteed that cells (1,1) and (n,m) are empty." But not that there's a path. So in the input, there could be cases where no path exists. In that case, the Witch doesn't need to do anything. So the answer is zero.

So, first, we need to check if there's any path from (1,1) to (n,m) given the original grid. If not, then output 0.

Otherwise, proceed to find the minimal layer count.

So the steps are:

1. Check if (1,1) and (n,m) are connected via right/down paths. If not, output 0.

2. Else, compute for each cell (i,j) whether it's on some path (reachable from start and can reach end).

3. For each layer (sum i+j), collect the count of such cells, except (1,1) and (n,m).

4. The minimal count among all layers (from sum=3 to sum =n+m-1) is the answer.

If the minimal count is zero, that means there's a layer with no cells, which can't happen because then the original path would not exist. But perhaps, if during the processing, after considering the original blocked cells, some layers may have zero cells. For example, if all cells in a certain layer are blocked except the ones that are not on any path. But in that case, the initial path would have to avoid that layer. Wait, but if the original path exists, then there's at least one cell in each layer between 2 and n+m. Because each path must pass through each layer once. So after considering the original blocked cells, but if the path exists, then for each layer sum from 3 to n+m-1, there must be at least one cell in that layer that is on some path. So the minimal count would be at least 1.

Wait, no. Suppose the original grid has a path, but after considering reachable_from_start and reachable_to_end, there exists a layer where all cells in that layer are blocked (original #). Then the minimal count would be zero. But that's impossible because the original path would have to pass through that layer. So the cells in that layer along the original path are passable. So in the initial grid, the original path must have passable cells in each layer. So after processing, there's at least one cell in each layer sum (from 3 to n+m-1) that is on some path. Therefore, the minimal count is at least 1.

So, in code:

- Compute reachable_from_start and reachable_to_end.

- For each cell (i,j), if reachable_from_start[i][j] and reachable_to_end[i][j], then it's part of the possible paths.

- Collect these cells (excluding start and end) into layers (i+j).

- For each layer between 3 and (n+m-1), count the number of such cells in that layer.

- The answer is the minimal such count.

But wait, the start and end cells are part of their layers (sum 2 and sum n+m), but they are excluded. So the layers considered are sum 3 up to sum (n + m -1).

So, code steps:

Read n and m.

Read the grid. Note that the input rows are from 1 to n, each of length m. So for Python, the grid is stored as a list of lists, with grid[i][j] being row i (0-based?), or maybe 1-based? Need to adjust for 0-based indexing.

Wait, in the problem statement, rows are numbered from 1 to n, columns from 1 to m. So (1,1) is the first row, first column. So in code, perhaps the grid is stored as a list of strings, each of length m, with grid[i] being row i+1 (since input is read as n lines, the first line is row 1, etc.). So for code, 0-based indices:

i ranges from 0 to n-1, j from 0 to m-1. So (i+1, j+1) in the problem's terms corresponds to grid[i][j].

But during the reachability processing, the code will use 0-based indices.

So:

Initialize a grid with n rows, each of length m.

Compute the forward reachability (from (0,0)) and backward reachability (from (n-1, m-1)).

Forward reachability:

reachable_from_start is a 2D array of size n x m.

reachable_from_start[0][0] is True if the cell is '.'.

Then, for each cell (i,j), if grid[i][j] is '.', then reachable_from_start[i][j] is True if either (i-1,j) is reachable (from above) or (i,j-1) is reachable (from left). Since we process in order, perhaps we can compute this by iterating through the grid row by row and column by column.

But for the forward direction, since movement is only right and down, the order can be from top-left to bottom-right. For each cell (i,j), if (i,j) is '.' and (i==0 and j ==0) → reachable, else check if (i-1,j) is reachable (if i>0) or (j-1, i) is reachable (if j>0).

Wait, for (0,0), reachable is True if it's '.' (which is guaranteed by problem statement).

For other cells:

reachable_from_start[i][j] = (grid[i][j] is '.') and ( (i>0 and reachable_from_start[i-1][j]) or (j>0 and reachable_from_start[i][j-1]) )

Similarly for backward reachability:

reachable_to_end[i][j] = (grid[i][j] is '.') and ( (i < n-1 and reachable_to_end[i+1][j]) ) or ( j < m-1 and reachable_to_end[i][j+1] )

But to compute reachable_to_end, we start from (n-1, m-1) and move left and up. So we can process the grid in reverse order, from (n-1, m-1) towards (0,0).

So for code:

Initialize reachable_from_start as a 2D array of False.

reachable_from_start[0][0] = (grid[0][0] == '.')

Then, for each i in 0..n-1:

   for each j in 0..m-1:

      if (i == 0 and j == 0):

          continue (already set)

      if grid[i][j] is '#', then continue.

      if i > 0 and reachable_from_start[i-1][j] is True:

          reachable_from_start[i][j] = True

      if j > 0 and reachable_from_start[i][j-1] is True:

          reachable_from_start[i][j] = True

Wait, but this way, the cell is checked for possible paths. For example, for cell (i,j), if either (i-1,j) or (i,j-1) is reachable, then (i,j) is reachable.

Similarly for the backward pass.

Once we have both reachable_from_start and reachable_to_end, check if reachable_from_start[n-1][m-1] is True. If not, then output 0.

Else, collect all cells (i,j) where reachable_from_start[i][j] and reachable_to_end[i][j], and (i,j) is not (0,0) and (n-1, m-1).

For each such cell, compute s = (i+1) + (j+1) (since in the problem's terms, sum is i+1 + j+1 = (i+j+2)). Wait no. Wait in code, the cell is (i,j) (0-based). The sum in the problem's terms is (i+1) + (j+1) = i+j+2.

So the sum for a cell (i,j) in code is i + j + 2.

Wait, (i+1) is the row number, (j+1) is the column. So sum is (i+1)+(j+1) = i+j+2.

So the layers for (i,j) are from 2 (start cell: 0,0 → 0+0+2=2) to (n-1 + m-1 + 2) = (n + m) (end cell). So the layers to consider are from 3 (2+1) to (n+m-1) (since the end is (n+m) and we are considering layers up to (n+m-1)).

So for each cell (i,j) in the intersection (reachable from start and end, not start or end), compute s = i + j + 2.

We need to count the number of such cells in each layer s, where s ranges from 3 to (n + m -1).

Then, find the minimal count among these layers.

The answer is that minimal count.

So for example, in the first sample:

n=2, m=2. The cells (0,0) is start, (1,1) is end.

The other cells are (0,1) and (1,0). Their sum (i+j+2) is (0+1+2=3) and (1+0+2=3). So the layer 3 has 2 cells. So answer is 2.

In the second sample, the answer is 1. So there's a layer with only 1 cell.

So the code steps are:

Read n and m.

Read the grid as a list of strings.

Compute reachable_from_start and reachable_to_end.

Check if the end is reachable (reachable_from_start[n-1][m-1] is True). If not, output 0.

Else, collect all cells (i,j) (excluding start and end) that are reachable in both directions.

Group them by s = i + j + 2.

For each s in 3 to (n + m -1), compute the count.

The minimal count is the answer.

Now, the code needs to handle large grids efficiently. For n*m up to 1e6, using two 2D arrays (reachable_from_start and reachable_to_end) would take O(nm) space each. But for 1e6, that's 1e6 * 2 * 1 byte (assuming booleans stored as bits, but Python lists of booleans may take more space). However, for 1e6 elements, that's manageable.

But in Python, using lists of lists for reachability may be feasible.

Alternatively, for space optimization, perhaps we can compute the forward and backward passes using a single array, updating in place, but that's possible.

But for code clarity, better to create two separate 2D arrays.

But for n and m up to 1e6 (but n*m <= 1e6), we can handle it.

So let's code this.

First, read the grid.

Then compute reachable_from_start:

Initialize a 2D array of size n x m, filled with False.

Set reachable_from_start[0][0] to True if grid[0][0] is '.' (which it is, per problem statement).

Then for each cell (i,j) in order, perhaps row-wise and column-wise.

But in code, for each row i in 0 to n-1:

   for each column j in 0 to m-1:

      if (i, j) is (0,0):

          continue (already set)

      if grid[i][j] is '#', skip.

      check if the cell is reachable from up or left.

      reachable_from_start[i][j] = ( (i > 0 and reachable_from_start[i-1][j]) ) or ( (j > 0 and reachable_from_start[i][j-1]) )

But the order in which we process the cells matters. For example, processing in row-major order (left to right, top to bottom) ensures that when we process cell (i,j), the cells above and to the left have already been processed.

Yes, that's correct.

Similarly for the backward pass: reachable_to_end.

Initialize reachable_to_end as a 2D array of False.

Set reachable_to_end[n-1][m-1] to True.

Then process the cells in reverse order. For example, process rows from bottom to top, and columns from right to left.

So:

for i in range(n-1, -1, -1):

   for j in range(m-1, -1, -1):

      if (i,j) is (n-1, m-1):

          continue.

      if grid[i][j] is '#', skip.

      reachable_to_end[i][j] = ( (i < n-1 and reachable_to_end[i+1][j]) ) or ( (j < m-1 and reachable_to_end[i][j+1]) )

Once both arrays are computed, check if reachable_from_start[n-1][m-1] is False. If so, output 0.

Else, collect all cells (i,j) where reachable_from_start[i][j] and reachable_to_end[i][j], and (i,j) is not (0,0) or (n-1, m-1).

For each such cell, compute s = i + j + 2.

Count the number of cells per s.

Then, find the minimal count in the range of s from 3 to (n+m-1).

If there are no cells in any of these layers, then the answer is 0, but that can't happen since the start and end are connected.

Wait, but if the only path is through the start and end, which are excluded. But in that case, the layers between must have at least some cells. For example, in a 2x2 grid, the only possible path is start → right → end. So layers 3 (sum i+j+2 = 3 for (0,1) and (1,0)), but the code would include those cells. Wait, but in this case, (0,1) and (1,0) are in layer 3. So the minimal count is 2.

So, the code should proceed.

Now, code.

But in Python, creating two 2D arrays (each of size n x m) could be memory intensive for n*m up to 1e6, but for 1e6 elements each, it's manageable.

But in Python, a list of lists for n=1e3 and m=1e3 (n*m=1e6) would take O(nm) space. Each list is a list of booleans, but in Python, each boolean is stored as a reference, which may take more space. So perhaps using a list of bitsets would be better, but that's complicated.

Alternatively, use a single list for each row, which is manageable.

But for code simplicity, better to use lists of lists, even if it takes more memory.

But in practice, for 1e6 elements, each boolean takes about 28 bytes in a list (since each list element is a separate object). Wait no, perhaps in Python, a list of booleans is optimized. For example, using a list of True/False entries would take about 1 bit per entry in a more optimized structure, but in reality, Python's list of booleans uses a lot of memory. For 1e6 elements, each stored as a separate bool object, that's 1e6 * 28 bytes (assuming each bool takes 28 bytes), which is 28MB, which is manageable.

But wait, in Python, the bool type is a subclass of int, and each instance is 28 bytes. So a list of 1e6 booleans would take 1e6 * 28 bytes, which is 28MB. Two such lists would be 56MB. For the given memory limit of 512MB, this is acceptable.

So proceed.

Now, code:

Read n, m.

Read n lines of the grid.

Compute reachable_from_start.

Compute reachable_to_end.

Check if reachable_from_start[-1][-1] is False → output 0.

Else:

   create a dictionary to count the layers.

   for i in 0 to n-1:

      for j in 0 to m-1:

         if (i ==0 and j ==0) or (i == n-1 and j == m-1):

             continue.

         if reachable_from_start[i][j] and reachable_to_end[i][j]:

             s = (i + j) + 2  # since (i+1) + (j+1) = i+j+2.

             if s <3 or s > (n + m -1):

                 # but since the start is at sum 2, and end is sum n+m.

                 # the layers are 3 to (n+m-1). So s must be in that range.

                 # But (i,j) is part of a path from start to end. So the sum must be in 3 to (n + m -1).

                 # So perhaps no need to check.

             else:

                 add to the counts.

   if no counts (i.e., the only path is start → end directly, but that's only possible if n=1 and m=1, but the problem says n and m are at least 1, but in the input examples, the first sample is 2x2. So in general, for a grid larger than 1x1, the layers would exist.

   find the minimal value in the counts.

   output that value.

But how to handle the layers? For example, if some layers have no cells (count 0), but according to the problem, the original path exists, so each layer must have at least one cell. But perhaps in the code, the minimal count could be zero, which would imply that the answer is zero. But in reality, that's possible only if there are no cells in some layer. But since the original path exists, there must be cells in each layer between sum 3 and (n+m-1). Because each step in the original path moves from sum k to sum k+1, so the original path's cells are in each layer. But those cells may not be in the intersection (reachable_from_start and reachable_to_end). For example, if the original path is through a cell that is not reachable from the end. So the code must handle that.

But the code will check for reachable_from_start and reachable_to_end. So if in the original path, a cell is reachable from start, but not from the end, then it's not considered. So layers that are part of the original path may have no cells in the intersection.

But in that case, the answer would be 0. Because the code's first check is if the end is reachable. If yes, then the code proceeds to compute the minimal count. So if the original path exists, but some layers have no cells in the intersection, then the code would return 0. But that's not possible. Because the original path's cells are all reachable_from_start (since they are on a path), and can reach the end (since the path goes to the end). So each cell in the original path is in reachable_from_start and reachable_to_end. So their sum would be in the layers from 3 to (n+m-1), and those cells would be counted. Therefore, the layers in the original path are all accounted for, so each layer in the sum from 3 to (n+m-1) has at least one cell. So the minimal count is at least 1.

But perhaps there's a case where the original path is blocked by the existing forests. But the problem states that the input has start and end as passable, but there may be no path. But the code first checks if the end is reachable. So if the code proceeds to collect the cells, then the original path exists, and the code's collected layers have at least one cell in each layer.

Thus, the minimal count is at least 1.

So in code, after collecting the counts, the minimal is either 1, 2, etc.

But in code, when the counts dictionary is empty, the answer is zero. Which can only happen if the end is not reachable (handled earlier). So in the code, after the initial check, the counts must not be empty.

But wait, no. For example, a grid where n=2 and m=2. The start is (0,0), end is (1,1). The cells (0,1) and (1,0) are blocked. So the only path is through these cells. But they are blocked, so the path doesn't exist. So the code would output 0. But according to the problem statement, the input ensures that the start and end are passable. But in this case, the code would output 0.

But the code's first check is whether reachable_from_start[-1][-1] is True. If it's False, output 0. So that's correct.

So, the code is correct.

Now, let's code this.

Testing the code against the samples.

First sample:

Input:

2 2

..

..

So grid is ['. .', '. .'].

reachable_from_start for all cells:

(0,0) is True.

(0,1): check left (0,0) is True → True.

(1,0): check up (0,0) is True → True.

(1,1): up (0,1) is True, left (1,0) is True → True.

reachable_to_end:

(1,1) is True.

(0,1): right (1,1) is True → True.

(1,0): down (1,1) is True → True.

(0,0): down (1,0) is True → True.

So cells (0,1) and (1,0) are in the intersection (reachable_from_start and reachable_to_end).

sum for (0,1) is 0+1+2 =3.

sum for (1,0) is 1+0+2=3.

count for sum 3 is 2 → answer is 2.

Second sample:

4 4

....
#.#.
....
.#..

The grid is:

Row 0: '....'

Row 1: '#.#.'

Row 2: '....'

Row 3: '.#..'

reachable_from_start:

Processing row 0:

cells (0,0) is True.

cells (0,1): left is True → True.

cells (0,2): left is True → True.

cells (0,3): left is True → True.

Row 1:

cell (1,0) is '# → no.

cell (1,1) is '.' → check up (row 0, j=1) is True → yes. So reachable.

cell (1,2) is '# → no.

cell (1,3) is '.' → check up (row 0, j=3) is True → yes. So reachable.

Row 2:

cell (2,0): up (row 1, j=0) is no. left (row 2, j-1) is j-1 is -1. So no → not reachable.

But wait, for row 2, cell (2,0) can be reached via up (row 1, j=0) is blocked. So no. So cell (2,0) is not reachable.

cell (2,1): check up (row 1, j=1) is True → yes. So reachable.

cell (2,2): check left (cell (2,1) is reachable) → yes.

cell (2,3): left (cell (2,2) → yes. So reachable.

Row 3:

cell (3,0) is '.' → check up (row 2, j=0) which is not reachable. So no.

cell (3,1) is '# → no.

cell (3,2) is '.' → check up (row 2, j=2) is reachable → yes. Or left (cell 3,1) is blocked. So yes.

cell (3,3) is '.' → check up (row 2, j=3) is reachable → yes. Or left (cell 3,2) is reachable → yes. So reachable.

But in row 3, cell (3,3) is the end.

So for reachable_from_start, the end is reachable.

Now, reachable_to_end:

starting from (3,3) (row 3, column 3).

Processing in reverse.

row 3:

cell (3,3) is True.

cell (3,2) is '.' → right (3,3) is True → yes.

cell (3,1) is '# → no.

cell (3,0) is '.' → right (3,1) is no, down (row 4 is out of bounds) → no.

row 2:

cell (2,3) → down (row 3, j=3) → yes → True.

cell (2,2) → right (cell (2,3) is True → yes.

cell (2,1) → right (cell (2,2) is True → yes.

cell (2,0) → right (cell (2,1) is True → yes.

row 1:

cell (1,3) → down (row 2, j=3) → yes → True.

cell (1,2) → '# → no.

cell (1,1) → down (row 2, j=1) → yes → True.

cell (1,0) → '# → no.

row 0:

cell (0,3) → down (row 1, j=3) → yes → True.

cell (0,2) → right (cell 0,3) → yes.

cell (0,1) → right (0,2) → yes.

cell (0,0) → right (0,1) → yes.

So cells that are in both reachable_from_start and reachable_to_end:

For example, cell (0,3) is reachable from start and end. So (0,3) is part of the paths.

But wait, the code will collect all cells (i,j) that are reachable in both directions.

For example, in the sample's third example:

3 4

....

.##.

....

The code should compute layers and find that the minimal count is 2.

But regardless, the code is correct.

So, the code will compute the counts for each layer and return the minimal.

Now, code:

The code must read from stdin, compute everything, and output the answer.

Now, writing the code.

First, read n and m:

n, m = map(int, input().split())

grid = [input().strip() for _ in range(n)]

Then compute reachable_from_start:

reachable_from_start = [[False]*m for _ in range(n)]
reachable_from_start[0][0] = grid[0][0] == '.'  # which is True.

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        if grid[i][j] == '#':
            continue
        up = reachable_from_start[i-1][j] if i > 0 else False
        left = reachable_from_start[i][j-1] if j > 0 else False
        reachable_from_start[i][j] = up or left

Then compute reachable_to_end:

reachable_to_end = [[False]*m for _ in range(n)]
reachable_to_end[-1][-1] = grid[-1][-1] == '.'  # True.

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if i == n-1 and j == m-1:
            continue
        if grid[i][j] == '#':
            continue
        down = reachable_to_end[i+1][j] if i < n-1 else False
        right = reachable_to_end[i][j+1] if j < m-1 else False
        reachable_to_end[i][j] = down or right

Then check if the end is reachable:

if not reachable_from_start[-1][-1]:
    print(0)
    exit()

Now, collect the layers:

from collections import defaultdict

layer_counts = defaultdict(int)

for i in range(n):
    for j in range(m):
        if (i == 0 and j == 0) or (i == n-1 and j == m-1):
            continue
        if reachable_from_start[i][j] and reachable_to_end[i][j]:
            s = i + j + 2
            if 3 <= s <= (n + m - 1):
                layer_counts[s] += 1

if not layer_counts:
    print(0)
else:
    min_count = min(layer_counts.values())
    print(min_count)

Wait, but what if layer_counts is empty? For example, when n=1 and m=1. But the problem says n and m are at least 1, but the first sample is 2x2. In the case where n=1 and m=1, the code would output 0. But according to the problem, the start and end are same cell, but the input is guaranteed to have them passable. So the answer is 0, which is correct.

But in the code, when n=1 and m=1, the layers considered are 3 to 1+1-1=1, which is invalid. So the loop for s in 3 to ... is not executed, layer_counts is empty, so code outputs 0. Which is correct.

But for the problem statement's constraints, n and m are such that n*m >= 3. Wait, the constraints say 3 <= n * m <= 1e6. So in the code, when n*m >=3, but for example n=3 and m=1, sum can be up to 3+1=4. Layers from 3 to 3+1-1=3, which is sum 3. So in this case, there's at least one layer.

But when n=3 and m=1, the start is (0,0), end is (2,0). The sum layers are 2 (start), 3 (cell (1,0)), 4 (end). So the layers to consider are sum 3. The cell (1,0) must be part of the path. So if it's reachable, then the layer_counts will have 1 cell. So the answer is 1.

So the code is correct.

Testing against sample inputs 1, 2.

```python
import sys
from collections import defaultdict


def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().split())
    grid = [input_stream.readline().strip() for _ in range(n)]

    # Compute reachability from start (0,0)
    reachable_from_start = [[False]*m for _ in range(n)]
    reachable_from_start[0][0] = grid[0][0] == '.'  # Always true per problem statement

    for i in range(n):
        for j in range(m):
            if (i == 0 and j == 0) or grid[i][j] == '#':
                continue
            up = reachable_from_start[i-1][j] if i > 0 else False
            left = reachable_from_start[i][j-1] if j > 0 else False
            reachable_from_start[i][j] = up or left

    # Check if end is not reachable
    if not reachable_from_start[-1][-1]:
        print(0, file=output_stream)
        sys.exit()

    # Compute reachability to end (n-1, m-1)
    reachable_to_end = [[False]*m for _ in range(n)]
    reachable_to_end[-1][-1] = grid[-1][-1] == '.'  # Always true

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if (i == n-1 and j == m-1) or grid[i][j] == '#':
                continue
            down = reachable_to_end[i+1][j] if i < n-1 else False
            right = reachable_to_end[i][j+1] if j < m-1 else False
            reachable_to_end[i][j] = down or right

    # Count cells in each layer
    layer_counts = defaultdict(int)
    for i in range(n):
        for j in range(m):
            if (i == 0 and j == 0) or (i == n-1 and j == m-1):
                continue
            if reachable_from_start[i][j] and reachable_to_end[i][j]:
                s = i + j + 2  # sum of (i+1) + (j+1)
                if 3 <= s <= (n + m - 1):
                    layer_counts[s] += 1

    print(min(layer_counts.values()) if layer_counts else 0, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 4
....
#.#.
....
.#..
""",
            "output": \
"""\
1
""",
        }, 
        {
            "input": \
"""\
3 4
....
.##.
....
""",
            "output": \
"""\
2
""",
        }, 
    ]

    for i, test_case in enumerate(TEST_CASES):
        in_stream = io.StringIO(test_case["input"])
        expected_output = test_case["output"].rstrip()

        out_stream = io.StringIO()
        main(in_stream, out_stream)
        real_output = out_stream.getvalue().rstrip()

        assert real_output == expected_output, \
            f'Test case {i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}'

    print('Tests passed 😎')


if __name__ == '__main__':
    test()


```

<RUN_SNIPPET>
```output
Tests passed 😎

```

Third sample:

Sample input:

3 4

....
.##.
....

The code computes the layers. The answer is 2. So the code must find a layer with count 2.

Thus, the code should be correct.
</think>

```python
import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
grid = [sys.stdin.readline().strip() for _ in range(n)]

# Compute reachability from start (0,0)
reachable_from_start = [[False]*m for _ in range(n)]
reachable_from_start[0][0] = grid[0][0] == '.'  # Always true per problem statement

for i in range(n):
    for j in range(m):
        if (i == 0 and j == 0) or grid[i][j] == '#':
            continue
        up = reachable_from_start[i-1][j] if i > 0 else False
        left = reachable_from_start[i][j-1] if j > 0 else False
        reachable_from_start[i][j] = up or left

# Check if end is not reachable
if not reachable_from_start[-1][-1]:
    print(0)
    sys.exit()

# Compute reachability to end (n-1, m-1)
reachable_to_end = [[False]*m for _ in range(n)]
reachable_to_end[-1][-1] = grid[-1][-1] == '.'  # Always true

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if (i == n-1 and j == m-1) or grid[i][j] == '#':
            continue
        down = reachable_to_end[i+1][j] if i < n-1 else False
        right = reachable_to_end[i][j+1] if j < m-1 else False
        reachable_to_end[i][j] = down or right

# Count cells in each layer
layer_counts = defaultdict(int)
for i in range(n):
    for j in range(m):
        if (i == 0 and j == 0) or (i == n-1 and j == m-1):
            continue
        if reachable_from_start[i][j] and reachable_to_end[i][j]:
            s = i + j + 2  # sum of (i+1) + (j+1)
            if 3 <= s <= (n + m - 1):
                layer_counts[s] += 1

print(min(layer_counts.values()) if layer_counts else 0)
```
