<think>
Okay, let's tackle this problem. Hmm. The problem involves simulating the movement of a bread piece on a conveyor belt grid. There are two types of events: querying where a bread ends up, and changing a conveyor's direction. The challenge is to handle these efficiently, especially given the constraints of n up to 1e5 and q up to 1e5, but m is up to 10. Oh right, m is small here. That's probably a clue for the solution.

First, let's think about the naive approach. For each 'A' query, we could simulate the movement step by step. But if the grid is large and there are many steps, this would be too slow. Because for each query, in the worst case, the bread could cycle indefinitely, leading to O(cycle length) time per query. Which could be O(1e5 * 1e5) operations in the worst case, which is way beyond the time limit. So we need a smarter way.

So, how can we pre-process the grid to answer queries quickly? Since m is small (up to 10), maybe we can model the transitions for each cell as a path that eventually either exits the grid or enters a cycle. Then, for each cell (x, y), we can precompute where it will end up (either a seat or a cycle). But since the grid can be updated with 'C' commands, we need this pre-processing to be dynamic. But handling updates efficiently is tricky.

Wait, the 'C' events can change the conveyor belts. However, the number of 'C' events is up to 1e4, which is manageable. So perhaps, for each cell, we can track its dependencies and recompute the necessary parts when a cell's conveyor changes. But how?

Alternatively, given that m is small, perhaps each row can be processed independently. For each row, the columns are only 10, so maybe we can model the movement within a row. Wait, but the conveyor directions can move up or down as well. For example, a '^' conveyor moves up, so that's a row change. So perhaps each cell's path can be represented as a graph, where each node is a cell, and edges represent the movement based on the conveyor direction. However, even with that, the graph could have cycles, and for each query, we need to traverse the path until we exit or find a cycle.

But with m being small, maybe for each row and column, we can model the possible transitions and memoize the result. Let's think about memoization. For each cell (x, y), when we process an 'A' query, we can track the path as we move, and memoize the result once we find it. However, when a 'C' event happens, we need to invalidate any memoized data that depends on the changed cell. That's possible, but how?

Another angle: since m is small, for each row, we can model the possible exits. Let's think for each cell (x, y), when moving through the grid, the path may either leave the grid (reach a seat) or loop. For each cell, we can precompute the exit point or mark it as part of a cycle.

But how to precompute this efficiently, especially after updates. Hmm. Let's think: Each cell's exit depends only on the path it takes. If m is small, then for each row, the movement can be handled in a way that's O(m) per row. For example, for a '^' conveyor, the next cell is (x-1, y), which is the same column. So for a row x, if the cell (x,y) is a '^', then the next cell is (x-1, y). Similarly, for left or right, the next cell is (x, y-1) or (x, y+1), but only if within the grid.

Wait, but the problem states that the seats are around the table. So the bread leaves the grid when it moves out of the grid. So the movement stops when the bread steps into a seat. So for example, if a bread is at (x, y) and the conveyor is '^', then moving up to (x-1, y). If x-1 is 0, then that's a seat, so we output (0, y). If x-1 is within the grid, then we follow the next conveyor. So the key is to model the path from (x, y) until it either exits or loops.

Given that m is small, perhaps we can model each row as a directed graph, and precompute for each cell in the row where it will exit. But given that rows can be up to 1e5, that's not feasible for all rows. Alternatively, since m is small, maybe for each row, the number of possible configurations is manageable, and transitions can be computed quickly.

Alternatively, for each cell (x,y), the path is determined by the conveyor directions. Let's model each cell as a state. When moving from (x,y) based on the conveyor, you go to another state. The problem is to find if following this path leads to an exit (seat) or a cycle. Since each cell can be visited multiple times, we need to detect cycles during the traversal.

But doing this for each query would be O(cycle length) per query, which is not feasible. However, given that m is small (10 columns), the number of possible steps per row is manageable. For example, in a row, a cell could move left or right, leading to a cycle in that row. But how does the '^' direction affect it? For example, a cell (x, y) with '^' moves up to (x-1, y), which could be in the same column but different row. So, the movement can switch rows. So the problem is that the path could involve moving up and down rows, which complicates the state space.

Wait, but m is 10, which is small. So for each cell (x,y), when we process an 'A' query, perhaps we can track the path as it moves through cells. However, for each step, we can check if we've been to this cell before. If yes, it's a loop. Otherwise, proceed. But for a query that requires traversing many steps, this could take O(k) time, where k is the number of steps until exit or loop.

But with q up to 1e5 and each query possibly requiring O(k) steps, this could be O(1e10) operations, which is way too slow. So this approach is not feasible.

Alternative idea: memoize the result for each cell (x, y). For each cell, store whether it eventually exits, and where, or loops. Then, when a 'C' event happens, we need to invalidate the memoization for cells affected by that change. But how to track dependencies?

But with m up to 10, maybe each cell (x,y) can have dependencies only in its row, or rows above or below. But it's unclear. For example, changing a cell (x,y) to '^' would affect the path of any cell that eventually reaches (x,y). So the memoization for all cells that pass through (x,y) would need to be invalidated. But tracking this is challenging.

Hmm. Another approach: since m is small, for each row, we can model the movement in that row and the possible transitions to other rows. For example, in a row, a cell can either move left, right, or up. If a cell's conveyor is left or right, then movement is within the row until it exits left or right (columns 0 or m+1), or moves up via a '^' conveyor. So perhaps each row can be processed as a state where the movement within the row is a chain of left/right steps, leading to either exiting, moving up, or moving down.

Wait, perhaps each row can be treated as a directed graph where each node is a column (since m is 10). For each cell in the row, we can precompute where it would exit the row (left, right, or up). For example, if a cell (x, y) has a '<' conveyor, then the movement in that row would be to the left. If that cell (x, y-1) also has '<', then we continue, until we reach column 0 (exit) or a cell that has a different direction. But wait, this depends on the conveyor directions of all cells in the row from y to the left. So, for a row x, if we have a left or right direction, the path in that row can be determined by moving left or right until we hit a cell that directs us up, or exit.

But how to model this efficiently for each row. Let's think for a row x, and for each column y, the exit from that row. For example, in row x, if you start at column y and follow the left/right directions, where do you end up. If during this traversal, you hit a '^', then you exit the row and move to (x-1, y). Similarly, if you hit a 'v' (but there's no 'v' in the problem), but in our case, the only directions are '<', '>', and '^'.

Wait, the '^' direction moves up. So, for a cell (x,y) with direction '^', the next cell is (x-1, y). So, if during the traversal within the row, you hit a '^', then you exit the current row and move to the row above.

So, for a row x, the movement within the row (columns 1 to m) can be modeled as a path that either:

- Exits left (column 0)
- Exits right (column m+1)
- Moves up to row x-1 (if any)
- Or enters a loop (if the path cycles within the row)

But since m is small (up to 10), perhaps for each row, we can precompute for each column y in the row, the result of moving through the row until we exit left/right, or move up. This can be done by simulating the movement for each column in the row. However, since each row can have up to 1e5 rows, and each row has m columns, this would require O(n * m) time, which for m=10 and n=1e5 is 1e6 operations. But when there are updates (C events), this could be manageable as each C event affects only one cell, and we can recompute the row's precomputed data when that cell is modified.

Wait, but in a row x, if a cell (x, y) is changed, then for all columns in that row that were dependent on y's previous state, their precomputed data would need to be updated. But how can we track this?

Alternatively, for each row x, and each column y in that row, we can precompute the exit direction when moving through the row. For example, for row x, starting at y:

- If the cell (x,y) is '^', then the exit is (x-1, y)
- If it's '<' or '>', then simulate moving left or right through the columns, keeping track of visited positions to detect cycles. If during this movement, we find that we loop (i.e., visit a column we've already been to), then the bread is in a loop. Otherwise, exit left, right, or hit a '^' cell which exits to the row above.

But this simulation would be O(m) per row and per column. Since m is 10, this is feasible for a single row. But if we have to do this for all 1e5 rows, that's 1e6 operations. Which is manageable for the initial setup. But when a 'C' event occurs, we need to recompute the row's data. Since there are at most 1e4 'C' events, each requiring O(m) work for their row, that's 1e4 * 10 = 1e5 operations. That's acceptable.

So here's the plan:

1. For each row x, precompute for each column y in that row:

   a. The exit status: whether moving from (x,y) leads to an exit (left/right seat), moving up to (x-1, y), or entering a loop.

   b. If the exit is left, right, or up, then the final seat coordinates (e.g., if exit left, then (x, 0), exit right (x, m+1), up (x-1, y)).

   c. If there's a loop, mark it as such.

   However, how do we model the movement through the row for left and right directions?

   Let's think about how the bread moves in a row when the direction is left or right.

   For example, in row x, starting at column y:

   - If direction is '>', next is (x, y+1). But if y+1 > m, then exit right (row x, column m+1). If the next cell's direction is '>', then continue. But if it's '<', then you start moving left. So this could form a cycle.

   So, for each row, and each starting column y, the movement is a path through the columns in that row. The path can be determined by following the directions until you hit a '^' (which moves up), exit the row (left or right), or enter a loop.

   The key is to model this for each row. Since m is small (up to 10), for each row, we can precompute for each starting column y:

   - The result (exit left, right, up, or loop)

   So, the approach is:

   For each row x, and each column y in that row:

   - Simulate the movement in the row. Track the columns visited. If during the simulation, we revisit a column, it's a loop. Otherwise, until we exit left, right, or hit a '^'.

   For example, for a cell (x,y) with direction '>', we move to (x, y+1). Check if y+1 > m: exit right. Else, check the direction of (x,y+1). If it's '>', continue. If it's '<', then we move back to (x,y), which would create a loop between y and y+1. So the simulation would detect that.

   So for each row x and column y, the movement within the row can be simulated in O(m) steps. Since m is up to 10, this is manageable.

   Then, when a 'C' event occurs (changing a cell in row x, column y), we need to re-simulate the entire row x. Because changing a cell in the row could affect all columns in that row that pass through it.

   Wait, but how? For example, if a row x has cells arranged such that changing a cell (x, y) could affect multiple starting columns. For example, if the row is all '>' except for the last cell which is '<', then changing the last cell to '>' would change the exit for all columns in that row. So when a cell in row x is modified, the entire row's precomputed data needs to be recomputed.

   But since m is small (10), recomputing the entire row is O(m^2) per 'C' event. For 1e4 'C' events, that's 1e4 * 100 = 1e6 operations, which is acceptable.

   So the steps would be:

   Preprocess each row by simulating all columns in the row. For each column, precompute the exit (left, right, up, or loop) and the final seat coordinates.

   Then, for an 'A' query (x, y):

   - Start at (x, y).

   - For each step:

      a. Check if current cell is outside the grid (i.e., a seat). If yes, return the current position.

      b. Get the current row x and column y.

      c. Check the precomputed exit for row x, column y.

      d. If the exit is a loop, return (-1, -1).

      e. If the exit is left, right, or up, move to that position and repeat.

   However, this approach may have steps that cross multiple rows. For example, moving up from row x to x-1, then processing that row, etc. But each row's exit is precomputed, so moving up would just take us to the next row's precomputed exit.

   Wait, but the precomputed exit for row x-1's column y is the exit from that row. So when we move up to (x-1, y), we process that row's precomputed exit. So each time we process a cell (x, y), we can use the precomputed data for that row to find where it exits the row. Then, if the exit is up, we proceed to the next row (x-1, y) and repeat the process.

   This way, each step involves processing a row, which may take O(1) time per row (since the precomputed data tells us where we exit the row). However, the problem is that moving up can take us through multiple rows. For example, if each row's cell y is a '^', then the bread would exit upwards row by row until it reaches row 0 (a seat) or gets stuck in a cycle.

   Wait, but in the precomputed data for row x, if a cell y's exit is up, then when processing that cell, we move to (x-1, y). Then, we process (x-1, y), which has its own precomputed exit. So each 'A' query would involve processing O(k) rows, where k is the number of rows traversed upwards (or downwards, but the problem says that row n+1 is not possible to exit). However, the maximum number of rows is up to 1e5, but in practice, each 'A' query would process O(1) rows if the exit is left or right. But in the worst case, it's possible to have a path that goes through all rows upwards, which would be O(n) steps. Which is 1e5 steps per query, leading to 1e10 operations for 1e5 queries. Which is way too slow.

   Hmm, that's a problem. Because the precomputed data per row tells us the exit from the row, but moving up to the next row could require another check. So the total steps could be O(n) in the worst case, which is not feasible.

   So, how can we optimize this? We need to find a way to model the entire path from the starting cell to the exit, considering that moving up may involve other rows. But with m being small, perhaps for each row and column, we can model the entire path up to the exit or loop.

   Alternatively, for each cell (x, y), we can precompute the entire path until exit or loop. But since there are 1e5 * 10 = 1e6 cells, and each path could be O(k) steps, this is not feasible for initial pre-processing.

   Wait, but when m is small, maybe for each cell (x, y), the path can be determined by a combination of moving through rows and columns. For example, when moving up through rows, each row's exit for column y is precomputed. So the path can be a sequence of row exits. For example:

   Start at (x, y). The row x's exit for y is up. So move to (x-1, y). Then, the row x-1's exit for y is up. Move to (x-2, y), etc. This continues until either a row's exit for y is not up (left, right, or loop), or until row 0 is reached (exit).

   So the number of steps is O(k), where k is the number of consecutive rows with '^' in column y. If column y in all rows is '^', then the path would exit at row 0, y. Otherwise, it would hit a row where column y's exit is left, right, or loop.

   So, the key is to model the '^' directions as a chain leading upwards. For each column y, perhaps we can precompute for each row x the earliest row above it where the exit for column y is not up. For example, for row x and column y, if the exit is up, then the next row is x-1. So for all rows from x upwards, if they all have '^' in column y, then the exit is (0, y). Otherwise, the first row where the exit is not up.

   So, perhaps we can precompute for each row x and column y, the exit after all possible upward moves. That is, for (x, y), the exit is determined by moving up as much as possible until a row is found where the exit for column y is not up, and then the exit is determined by that row's exit. If all rows above x have '^' in column y, then the exit is (0, y).

   How can we model this efficiently?

   For each column y, create a structure that allows us to quickly find the next row x' where the exit for column y is not up. Then, for a cell (x, y) where the exit is up, the actual exit is determined by the exit of the first row x' < x where the exit for column y is not up, or (0, y) if all are '^' in column y up to row 1.

   But how to precompute this for all columns and rows?

   Let's consider each column y separately. For column y, the rows can be processed from top (row 1) to bottom (row n). For each row x in column y, if the exit is up (i.e., the cell is '^'), then the exit for row x, y is the same as the exit for row x-1, y. Otherwise, the exit is whatever is computed for that row x, y.

   So for column y, the exit for row x, y is:

   if cell (x, y) is '^', then exit is the same as exit for x-1, y.

   else, the exit is the exit computed for row x's simulation.

   Wait, but that's not entirely accurate. For example, if cell (x, y) is '^', then the exit is (x-1, y). Then, the exit for (x-1, y) depends on that cell's direction. If that is also '^', then we go up further. So the exit for (x, y) is the exit of (x-1, y), and so on.

   So, for column y, the exit for row x, y can be represented as the exit of the first row x' <= x where the cell (x', y) is not '^'. If all cells from x down to row 1 are '^', then the exit is (0, y). Otherwise, the exit is the exit of row x' for that column y.

   So, for each column y, we can precompute for each row x the exit after considering all possible upward moves. But how to compute this efficiently.

   For column y, we can process the rows from top to bottom. For each row x in 1..n:

   if cell (x, y) is not '^', then the exit for x, y is the exit from row x's simulation (left, right, loop).

   else, the exit for x, y is the exit for x-1, y. If x-1 is 0, then exit is (0, y).

   Wait, but this only holds if the cell (x, y) is '^'. So for each column y, we can track the current 'base' row, which is the first row x' <=x where the cell is not '^'. Then, for all rows >=x' and cell is '^', their exit is the exit of x'.

   So, for column y, we can process each row x in order from top (1) to bottom (n):

   - For row x, check the cell (x, y) direction.

   - If it's not '^', then the exit is determined by the row x's simulation (left, right, loop). So we compute that and store it. Also, set the current 'base' for column y to x.

   - If it is '^', then the exit for row x, y is the same as the exit for row x-1, y. So we can store that.

   So, for each column y, we can precompute for each row x:

   exit_row[x][y] = if cell (x,y) is '^', then exit_row[x-1][y], else the computed exit for row x's simulation.

   So, for example, if in column y, rows 3 to 5 are '^', and row 2's exit is (0, y), then exit_row[5][y] is (0, y).

   But how to handle this when the cell directions change due to 'C' events. For example, if a cell (x, y) is changed to '^', then all rows below x in column y may have their exit_row changed.

   Wait, this approach would require that for each column y, the exit_row for each x is determined by the first non-'^' cell above. However, when a cell (x, y) is updated, it could affect all rows below x in column y. For example, if x was the first non-'^' cell in column y for rows x and below, then changing x's direction to '^' would cause the rows below x to look for the next non-'^' cell above x.

   This suggests that for each column y, the exit_row is a chain that depends on the cell directions above. Maintaining this chain dynamically with updates is challenging.

   So, perhaps this approach is not feasible given the time constraints.

   Alternative idea: When processing an 'A' query (x, y), the path can be divided into two parts:

   1. Moving upwards through rows via '^' directions.

   2. Once a row is found where the exit is not up, then the exit is determined by that row's simulation.

   So, the first step is to find the first row x' <= x where the cell (x', y) is not '^', or reach row 0. Then, the exit is determined by the exit of that row x', y. If all rows from x down to 1 have '^' in column y, then exit at (0, y).

   So, for example, if the starting cell (x, y) is '^', then we move up to x-1, y. If that cell is also '^', continue up until we find a row x' where the cell is not '^', or reach 0.

   How to find this x' efficiently?

   Since m is small, perhaps for each column y, we can precompute a data structure that allows us to query the first row <=x where the cell is not '^'. This can be done using a binary indexed tree or a segment tree. However, with n up to 1e5 and m up to 10, building a segment tree for each column is feasible.

   For each column y, we can maintain a list of rows where the cell is not '^', sorted in decreasing order. Then, for a given x, the first row x' <=x with cell not '^' can be found using binary search. If there are no such rows, then the exit is (0, y).

   For example:

   Column y has cells:

   rows 1: '<'

   rows 2-5: '^'

   row 6: '>'

   So the list for column y is [6, 1]. For a query x=5, y: binary search to find the largest x' <=5 in the list. The list is sorted in decreasing order, so the first element is 6 (which is larger than 5), so we look for the next element, which is 1. So the first x' is 1. Then, the exit is the exit for row 1, y.

   So, for each column y, we can maintain a sorted list of rows where the cell is not '^', sorted in descending order. When processing an 'A' query (x, y):

   - Perform a binary search on the list for column y to find the largest row x' <=x where the cell is not '^'. If such x' exists, then the exit is determined by row x' and y. If not, exit is (0, y).

   Then, for row x' and column y, we need to have precomputed whether it leads to an exit (left, right, up) or loop.

   Wait, but row x' could have a conveyor that is '<', '>', or '^'. But in this case, x' is the first row where the cell is not '^', so in row x', the cell's direction is either '<' or '>'.

   Wait no. Because when we processed the list for column y, the rows added are those where the cell is not '^'. So in row x', the cell's direction is '<' or '>'. So in row x', the exit for (x', y) is determined by the row's simulation (which may be left, right, or loop). But how is this handled?

   So, for each row x, and each column y, we precompute the exit data (left, right, loop, or up). But for rows where the cell is '^', the exit data is up, but in that case, the exit is determined by the first row x' <x where the cell is not '^'.

   So, the plan is:

   For each row x and column y, precompute:

   - If the cell (x,y) is '^', then the exit for (x,y) is the same as the exit for (x-1, y). If x-1 is 0, then exit (0, y).

   - If the cell (x,y) is '<' or '>', then simulate the movement within the row to determine the exit (left, right, loop, or up). Wait, no: for cells that are '<' or '>', the exit for the row is determined by the simulation within the row. But if during that simulation, a '^' is encountered, then the exit is up (x-1, y).

   So, for rows with '<' or '>' in column y, the row's exit for (x,y) is determined by the simulation within the row. If during the simulation, the bread moves up (via a '^'), then the exit is up (x-1, y), which again would trigger another lookup in the column y's list.

   Hmm. This approach may not capture all possible cases. For example, a row x has a cell (x, y) with '>', which leads to a cell (x, y+1) with '^'. Then, the exit for (x,y) would be (x-1, y+1), which may have its own exit.

   So this seems to bring us back to the original problem of simulating the path step by step, which is not feasible for large n.

   Therefore, perhaps the only feasible way given the problem constraints is to memoize the result for each cell (x,y) and handle 'C' events by invalidating the memoized entries that are affected by the change. However, the number of memoized entries could be large, and the dependencies are not clear.

   Alternatively, given that m is small, for each 'A' query, simulate the path until we either exit, detect a loop, or exceed a certain number of steps (like 4 * m steps per row) since with m small, the steps per row are limited. For example, in a row, if the path is longer than 2m steps, there must be a loop.

   So, for each 'A' query:

   - Track the current cell (x, y).

   - Keep a visited set of cells we've been to during this query.

   - For each step:

      a. If (x, y) is already in visited, return loop.

      b. Add (x, y) to visited.

      c. Check if (x, y) is a seat. If yes, return it.

      d. Get the conveyor direction.

      e. Compute the next cell based on direction.

      f. Update x and y to the next cell.

   The problem with this approach is that for a query that takes O(k) steps, where k is large, this would be too slow. However, given that m is small, the maximum number of steps per query is bounded by O(m * log n), since moving up through rows can be done quickly by finding the first non-'^' row in column y.

   So, here's the plan:

   For each 'A' query (x, y):

   1. Use the column y's list to find the first non-'^' row x' <= x. If this exists, then process row x', y. Else, return (0, y).

   2. In row x', simulate the movement within the row (left/right) until it exits, moves up, or loops.

   3. If during simulation, it moves up, repeat the process for the new row x'-1.

   But simulating the row's movement can be done quickly since m is small (up to 10). For example, simulating a row's movement takes O(m) steps. And the number of rows visited is O(k), where k is the number of '^' transitions.

   So for each 'A' query:

   - Find the first non-'^' row x' in column y. O(log k) time, where k is the number of non-'^' rows in column y.

   - Simulate the row x' movement: O(m) steps.

   - If during the simulation, the movement is up (i.e., to (x'-1, y)), then repeat the process for that row.

   So, the total steps would be O(m) per row visited. The number of rows visited is O(1) in practice, but in the worst case, could be O(n) if each row has a '^' in column y. But this is not feasible.

   So, how to optimize the '^' transitions. For example, if we have a chain of '^' cells in column y, then moving up from row x would require moving all the way to row 0. So, for a column y, if the cell is '^' in rows x down to x', then the exit is determined by row x' or row 0.

   So, the approach would be:

   For each column y, maintain a data structure that allows us to find the first row x' <=x where the cell is not '^'. If such a row exists, then the exit is determined by row x', y. Otherwise, exit is (0, y).

   Then, for the row x', simulate the movement within the row, which is O(m) steps.

   So, for example:

   For 'A x y' query:

   - Find x' using column y's list.

   - If x' exists, simulate row x' starting at y.

     a. During simulation, if the exit is up (e.g., a '^' is encountered in row x'), then x' is decremented by 1, and repeat.

     Wait, no. Because x' is the first row where the cell is not '^'. So in row x', the cell (x', y) is either '<' or '>'. So during simulation in row x', the movement is left or right. But during that simulation, other cells in row x' may have '^' directions. For example, row x' may have a '^' in cell (x', y+1), which would move up to row x'-1.

   So the initial approach of finding x' (the first row where cell (x', y) is not '^') is not sufficient, because during the simulation of row x', other cells may have '^' directions leading to more upward movements.

   So, this approach does not capture all possible cases. So, perhaps the only way to handle all cases is to simulate each step for the 'A' query, but with optimizations.

   Let's think: for each step in the simulation, track the current cell (x, y). For each cell, the next step is determined by the conveyor direction.

   However, with n up to 1e5 and m up to 10, the maximum number of steps per query is O(n + m) in the worst case (e.g., moving up through all rows, then moving through m columns). Which is 1e5+10 steps per query. For 1e5 queries, this is 1e10 steps, which is way too slow.

   So, we need a way to model the path in such a way that we can find the exit or loop in O(1) or O(m) steps per query.

   Let's think about the possible cycles. Since m is small (10), the number of possible cells in a row is small. So, when a bread is in a row x, moving left/right, it can form a cycle in that row. For example, in a row with directions '><', moving between two cells. So during simulation, if we detect that a cell in the same row is visited again, then it's a loop.

   So, during the simulation of an 'A' query:

   - Track the current position (x, y).

   - For each step, check if (x, y) is a seat. If yes, return it.

   - Check if we've visited (x, y) before. If yes, return loop.

   - Add (x, y) to visited.

   - Move according to the conveyor direction.

   However, this can be optimized by tracking the current row and checking for cycles within that row. For example, when moving left/right in a row, keep track of the columns visited in that row. If a column is revisited in the same row, then it's a loop.

   So, the steps would be:

   For 'A x y' query:

   current_x = x

   current_y = y

   visited = set()

   while True:

      if (current_x, current_y) is a seat:

          return (current_x, current_y)

      if (current_x, current_y) is in visited:

          return (-1, -1)

      visited.add( (current_x, current_y) )

      dir = grid[current_x][current_y]

      next_x, next_y = move according to dir

      current_x, current_y = next_x, next_y

   The problem is that this can take O(k) steps per query, which is not feasible for large k.

   However, considering that m is small (10), perhaps the number of steps within a row is limited. For example, when moving left/right in a row, the number of steps before exiting or looping is O(m). Once the movement leaves the row (via '^'), the next steps are handled by the column's data structure.

   So, the overall steps for a query can be broken into:

   1. Moving up through rows via '^' directions.

   2. Once a row is found where the exit is not up, simulate the left/right movement in that row, which is O(m) steps.

   But how to handle cases where the movement within a row leads to an upward move (e.g., a cell in the row is '^').

   For example, during simulation of row x', y', the path could hit a '^' conveyor, leading to x' - 1, y'. This would require moving up again, which could involve another row. So this seems to complicate the steps again.

   So, perhaps the only way is to accept that for some queries, the path can be long, but given that m is small, and 'C' events are up to 1e4, the average steps per query may be manageable.

   Let's consider the constraints:

   - n is up to 1e5.

   - q is up to 1e5.

   - Each query can take O(k) steps, where k is the path length.

   The worst case is 1e5 * 1e5 = 1e10 steps, which is way too slow.

   So, we need to find a way to model the path more efficiently.

   Let's think again about the problem. The key is that m is small. So for each cell (x, y), when you are in that cell, the next cell depends on the conveyor direction. The possible transitions can be modeled as a directed graph. Each node is a cell (x,y), and edges are determined by the conveyor directions.

   For each query, we need to find the path from (x,y) until we exit or loop.

   But with up to 1e5 * 10 = 1e6 cells, building this graph is possible. But how to handle updates (C events) which change the edges.

   For each cell (x,y), we can track:

   - the next cell it points to.

   So, for each cell, next_cell[x][y] is computed based on its direction.

   For example:

   if direction is '^', then next_cell[x][y] = (x-1, y)

   if direction is '<', then next_cell[x][y] = (x, y-1)

   if direction is '>', then next_cell[x][y] = (x, y+1)

   But we have to check if these next cells are within the grid. For example:

   if direction is '<' and y-1 is 0, then next_cell is (x, 0) which is a seat.

   So, for each cell (x,y), next_cell is:

   if direction is '^':

      if x-1 == 0: next is (0, y)

      else: next is (x-1, y)

   elif direction is '<':

      if y == 1: next is (x, 0)

      else: next is (x, y-1)

   elif direction is '>':

      if y == m: next is (x, m+1)

      else: next is (x, y+1)

   Wait, but this depends on the grid's conveyor directions. So, when a cell (x,y) is updated, we need to recompute its next_cell.

   Once we have this next_cell map, each query can be simulated by following the next_cell pointers until a seat is found or a cycle is detected.

   However, this again could take O(k) steps per query, which is not feasible.

   So, we need to find a way to detect cycles quickly. One approach is to find the successor of each cell and compute the path using memoization. For example, using a visited set during each query to track if we've visited a cell before. However, this is O(k) per query.

   Alternatively, we can precompute for each cell the exit or loop status. But this is challenging with updates.

   Another idea: Since the 'C' events are up to 1e4, and the grid is up to 1e5 rows, but m is 10, the total number of cells is 1e5 * 10 = 1e6. So, if each 'C' event affects a single cell, and for each 'A' query we process O(m) steps, the total number of steps across all queries is 1e5 * 10 = 1e6 steps, which is manageable.

   Wait, but for an 'A' query that requires moving up through 1e5 rows, this is 1e5 steps per query, which is not feasible.

   So, this approach works only if the path length is O(m) per query on average.

   But how to handle the upward movement. For example, if a column y has all cells '^', then the exit is (0, y). So, for a query (x, y), where all cells from x down to 1 are '^', the path is x steps to reach (0, y). This is O(x) steps, which is up to 1e5 per query. So for 1e5 queries, this is 1e10 steps.

   So this is not feasible.

   So, how to handle the upward movement efficiently.

   Another idea: For each column y, precompute the first row x' <=x where the cell is not '^'. This can be done using a binary indexed tree or a sorted list.

   For example, for each column y, maintain a list of rows where the cell is not '^', sorted in descending order. When processing an 'A' query (x, y), perform a binary search on this list to find the largest x' <=x. If found, then the exit is determined by the row x', y. Otherwise, the exit is (0, y).

   Then, for the row x', simulate the movement within the row, which is O(m) steps. If during this simulation, a '^' is encountered, leading to (x'-1, y), we repeat the process: find the first row x'' <=x'-1 where the cell is not '^' in column y. But since x' is the first row where the cell is not '^', x'' would be x' again. So this would result in an infinite loop.

   Wait, no. Because in row x', the cell (x', y) is not '^'. So during simulation of row x', the movement would be left or right. Only if during that simulation, the bread steps into a cell (x', y') where the direction is '^' would it move to (x'-1, y').

   So, the process is:

   - Find x' for column y.

   - Simulate movement in row x' starting at y. During this simulation, the bread may move left/right and encounter '^' directions in other cells, leading to upward movement. So after each upward move, repeat the process for the new column.

   For example:

   Start at (x, y). Find x' (first non-'^' row in column y). Simulate row x' starting at y. During simulation, if you hit a '^' in (x', y'), then move to (x'-1, y'), and repeat the process for column y'.

   So, this can be handled recursively. Each time we enter a new column, we find the first non-'^' row in that column, then simulate the row.

   The number of such steps is bounded by the number of column changes. Since m is small, the number of column changes is limited. For example, each column change can happen at most m times per query.

   So, for each query:

   - While True:

      a. Find x' in current column y.

      b. If x' is not found, return (0, y).

      c. Simulate the row x' movement starting at y. During simulation, track visited positions in this row.

      d. If during simulation, the bread exits left/right, return the seat.

      e. If during simulation, the bread enters a cell with '^' in this row, move to (x'-1, y'), set y = y', and repeat.

      f. If during simulation, the bread enters a loop, return (-1, -1).

   But simulating the row x' can be done in O(m) steps. And the number of such row simulations per query is O(1) in practice, but in theory could be O(m) if the path involves switching columns each time.

   However, with m up to 10, this could be manageable.

   So, the steps are:

   1. For each 'A' query (x, y):

      a. While True:

         i. Find the first non-'^' row x' in column y that is <= current x.

         ii. If x' not found, return (0, y).

         iii. Simulate the movement in row x' starting at current y.

         iv. During simulation, track visited cells in row x' to detect loops.

         v. If simulation leads to exit (left/right), return the seat.

         vi. If simulation leads to a '^' conveyor in row x', move to x'-1 and new y, then repeat the process.

         vii. If simulation leads to a loop, return (-1, -1).

   The key is that each row simulation is O(m) steps, and the number of row simulations per query is O(1) on average.

   Now, the problem is to implement this efficiently.

   Now, let's think about how to implement the simulation of a row x' starting at y.

   For row x', simulate the movement:

   current_col = y.

   visited_in_row = set()

   while True:

      if current_col is 0 or m+1: return exit (x', current_col).

      if current_col in visited_in_row: return loop.

      visited_in_row.add(current_col)

      cell = grid[x'][current_col]

      if cell is '^':

          return next cell is (x'-1, current_col). Break and process this new cell.

      elif cell is '<':

          current_col -=1

      elif cell is '>':

          current_col +=1

   So, during the simulation of row x', current_col is tracked. If it leaves the row (left/right), return the seat. If during the simulation, we hit a '^', then the next cell is (x'-1, current_col), which requires processing that column (current_col) and row x'-1.

   So, the code for the 'A' query would look like:

   def process_A(x, y):

       while True:

           # Find first non-^ row x' <=x in column y.

           # Using the column's list.

           x_prime = find_first_non_hat_row(y, x)

           if x_prime is None:

               return (0, y)

           # Simulate row x_prime, starting at column y.

           # Simulate until exit left/right, ^, or loop.

           visited = set()

           current_col = y

           while True:

               if current_col <1 or current_col >m:

                   return (x_prime, current_col)

               if current_col in visited:

                   return (-1, -1)

               visited.add(current_col)

               dir = grid[x_prime][current_col]

               if dir == '^':

                   x = x_prime -1

                   y = current_col

                   break  # Exit the row simulation and process new x, y.

               elif dir == '<':

                   new_col = current_col -1

               else: # '>'

                   new_col = current_col +1

               # Check if new_col is out of bounds.

               if new_col <1:

                   return (x_prime, 0)

               elif new_col >m:

                   return (x_prime, m+1)

               else:

                   current_col = new_col

   So, the find_first_non_hat_row function is critical. For each column y, we need to maintain a list of rows where the cell is not '^', sorted in descending order. When a 'C' event changes a cell (x, y) to a direction other than '^', it is added to the list if it wasn't there before. If it's changed to '^', it's removed from the list.

   So, for each column y, the list is a sorted (descending) list of rows where the cell is not '^'. For example, if column y has non-'^' cells in rows 5, 3, 1, then the list is [5,3,1].

   For a query (x, y), to find x_prime, we need the largest row <=x in the list. This can be done via binary search.

   For example, in the list [5,3,1], if x=4, then x_prime is 3.

   So, for each column y, we can maintain the list as a list sorted in descending order. For each 'C' event in (x, y), we check if the new direction is '^' or not, and update the list accordingly.

   The steps for handling 'C' events:

   When a 'C x y c' event occurs:

   - Check if the previous direction was '^' and new direction is not '^':

       if yes: add x to column y's list (if not already present).

   - Or, if the previous direction was not '^' and new direction is '^':

       remove x from column y's list.

   - Then, the list is kept sorted in descending order. Insertion and deletion can be done efficiently using binary search.

   So, for each column y, the list is maintained as a sorted list. Inserting and deleting can be done in O(log k) time, where k is the number of non-'^' rows in the column.

   Now, to implement this, for each column y, we can store a list and keep it sorted in descending order. For example, in Python, using a list and the bisect module.

   So, for each column y:

   non_hat_rows[y] = sorted list of rows (in descending order) where the cell is not '^'.

   When we process a 'C' event for (x, y):

   - Check the previous direction and new direction.

   - If the new direction is not '^', and the previous direction was '^' (or the cell was not in the list):

       add x to non_hat_rows[y] if not present.

   - If the new direction is '^', and the previous direction was not '^':

       remove x from non_hat_rows[y].

   - After adding/removing, ensure the list remains sorted in descending order.

   For example, in Python:

   from bisect import bisect_left, insort

   # For adding a row x to the list:

   # To insert x in descending order:

   # Find the position where x should be inserted to keep the list sorted descending.

   # Since the list is sorted descending, we can use bisect_right with a reverse=True.

   # Or, we can use the bisect module with a key.

   # Alternatively, since the list is maintained in descending order, to insert x:

   # find the first index where the element is <= x.

   # Then insert x at that index.

   # For example, list is [5,3,1], inserting x=4:

   # bisect_left for x in reversed list would give the position 1 (since 4 >3 but <5).

   # So, inserting at index 1, the list becomes [5,4,3,1].

   # In Python, bisect module has bisect_right with a key, but for simplicity, we can reverse the list.

   # Alternatively, use the fact that the list is in reverse order.

   So, when inserting x into a list sorted in descending order:

   pos = bisect.bisect_left(non_hat_rows[y], x, lo=0, hi=len(non_hat_rows[y]), key=lambda a: -a)

   non_hat_rows[y].insert(pos, x)

   Similarly, when removing x:

   pos = bisect.bisect_left(non_hat_rows[y], x, key=lambda a: -a)

   if pos < len(non_hat_rows[y]) and non_hat_rows[y][pos] == x:

       non_hat_rows[y].pop(pos)

   So, this would maintain the list in descending order.

   Once the list is maintained, for each 'A' query, finding x_prime is done via binary search on the list.

   Now, let's put this all together.

   The steps are:

   1. Read n, m, q.

   2. Read the grid. For each row, store as a list of characters.

   3. For each column y, initialize the non_hat_rows[y] list by checking each row x from 1 to n. If the cell is not '^', add x to non_hat_rows[y], then sort in descending order.

   4. For each query:

      a. If it's a 'C' event:

         i. Update the grid cell (x, y) to c.

         ii. Check if previous direction was '^' and new direction is not '^', or vice versa.

         iii. Update the non_hat_rows[y] list accordingly.

      b. If it's an 'A' event:

         i. Start at (x, y).

         ii. Loop:

             A. Find the first non-'^' row x' <= current x in column y.

             B. If none, return (0, y).

             C. Simulate the movement in row x':

                 - Track current_col, visited columns in the row.

                 - For each step in row x':

                     * If current_col is out of bounds, return (x', current_col).

                     * If current_col is in visited, return (-1, -1).

                     * Add to visited.

                     * Get direction.

                     * If direction is '^', set new x and y, break out of this loop, and continue processing.

                     * Else, move left or right.

             D. Repeat until exit or loop.

   Now, implementing this in Python.

   Handling the simulation within a row:

   def simulate_row(x, start_col, grid_row):

       visited = set()

       current_col = start_col

       while True:

           if current_col < 1 or current_col > m:

               return ('exit', x, current_col)

           if current_col in visited:

               return ('loop', 0, 0)

           visited.add(current_col)

           dir = grid_row[current_col - 1]  # assuming grid_row is 0-based

           if dir == '^':

               return ('up', x-1, current_col)

           elif dir == '<':

               new_col = current_col - 1

           else:

               new_col = current_col + 1

           if new_col < 1:

               return ('exit', x, 0)

           elif new_col > m:

               return ('exit', x, m+1)

           else:

               current_col = new_col

   So, this function returns the outcome of simulating the row x starting at start_col. Possible outcomes:

   - ('exit', x, col): exited the row to seat (x, col).

   - ('loop', 0, 0): entered a loop within the row.

   - ('up', new_x, new_col): moved up to (new_x, new_col).

   Now, for each 'A' query:

   x, y = initial position.

   while True:

       # Find x_prime in column y <=x.

       column_list = non_hat_rows[y]

       idx = bisect.bisect_left(column_list, x, key=lambda a: -a)  # since list is sorted descending.

       if idx < len(column_list):

           x_prime = column_list[idx]

       else:

           # No rows in column y with non-^, so exit to (0, y).

           print(0, y)

           break

       # Simulate row x_prime, starting at y.

       outcome = simulate_row(x_prime, y, grid[x_prime-1])  # grid is 0-based.

       if outcome[0] == 'exit':

           print(outcome[1], outcome[2])

           break

       elif outcome[0] == 'loop':

           print(-1, -1)

           break

       elif outcome[0] == 'up':

           # new x and y are (x_prime-1, new_col)

           x = outcome[1]

           y = outcome[2]

   So, this loop repeats until the outcome is exit or loop.

   Now, the key is that when moving up, the new y is the current_col where the '^' was encountered. For example, if in row x', the simulation moves to column new_col and hits a '^', then the new x is x'-1 and new y is new_col. Then, the process repeats for column new_col.

   This handles the cases where the bread moves up into a new column.

   Now, the code should handle all cases.

   Let's test this approach against the sample input.

   First sample:

   Input:

   2 2 3

   >>

   ^^

   Events:

   A 2 1

   C 1 2 <

   A 2 1

   Sample output:

   1 3

   -1 -1

   Let's see.

   For the first 'A 2 1':

   y =1.

   column_list for y=1 is rows where cell is not '^'.

   The initial grid row 1 is '>>', so cell (1, 1) is '>', which is not '^'. So non_hat_rows[1] contains [1, 2]. Wait, no. Wait, the rows are 1 and 2 (since n=2). Let's see:

   For column y=1:

   row 1, cell (1,1) is '>', so non_hat_rows[1] includes row 1.

   row 2, cell (2,1) is '^', so not included.

   So non_hat_rows[1] is [1].

   So x=2, y=1.

   Find x_prime in non_hat_rows[1] which is <=2. The list is [1]. So x_prime=1.

   Simulate row 1, starting at column 1.

   row 1 is '>>'.

   current_col =1.

   dir is '>', new_col=2.

   current_col=2.

   dir is '>', new_col=3, which is > m (2). So return exit (1,3). So output is 1 3.

   For the second event: C 1 2 <.

   So, row 1, column 2 was '>', now changed to '<'. For column y=2, we need to update non_hat_rows[2]. Before the change, if the cell was '>', which is not '^', so it was in the list. Now, changed to '<', which is not '^', so no change to the list. So non_hat_rows[2] remains.

   For the third event: A 2 1.

   y=1.

   non_hat_rows[1] is still [1].

   x_prime=1.

   simulate row 1, starting at column 1.

   row 1's cells are '><' (since after change, cell (1,2) is '<'.

   current_col=1.

   dir is '>', new_col=2.

   current_col=2.

   dir is '<', new_col=1.

   Now, current_col=1 is in visited (visited is {1, 2}), loop detected. Return loop.

   So output is -1 -1.

   Which matches the sample.

   So, the approach works for this case.

   Another sample:

   Second sample input:

   The code would need to handle multiple transitions, but the logic should hold.

   So, the code should correctly process all cases.

   Now, considering all edge cases and optimizations, the code should be as follows.
</think>

To solve this problem, we need to simulate the movement of a bread piece on a conveyor belt grid efficiently, even with updates to the grid. The key challenge is to handle large input sizes while ensuring optimal performance for both queries and updates.

### Approach
1. **Grid Representation**: Use a list of lists to represent the grid, where each cell contains a direction ('^', '<', '>').
2. **Non-'^' Rows Tracking**: For each column, maintain a sorted list of rows where the cell is not '^'. This helps quickly determine the first valid row to process when moving upwards.
3. **Binary Search for Efficiency**: Use binary search to efficiently find the first valid row (non-'^') for a given column and starting row.
4. **Simulation of Movement**: For each query, simulate the movement within a row until an exit, loop, or upward movement is detected. This simulation is optimized by leveraging the small column size (up to 10).

### Solution Code
```python
import bisect

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    m = int(input[ptr+1])
    q = int(input[ptr+2])
    ptr +=3
    
    grid = []
    for _ in range(n):
        row = input[ptr].strip()
        grid.append(list(row))
        ptr +=1
    
    # Initialize non_hat_rows for each column (1-based)
    non_hat_rows = [[] for _ in range(m+2)]  # columns 1..m
    for y in range(1, m+1):
        for x in range(n, 0, -1):
            if grid[x-1][y-1] != '^':
                non_hat_rows[y].append(x)
    
    for _ in range(q):
        event = input[ptr]
        ptr +=1
        if event == 'C':
            x = int(input[ptr])
            y = int(input[ptr+1])
            c = input[ptr+2]
            ptr +=3
            # Update grid
            prev_c = grid[x-1][y-1]
            grid[x-1][y-1] = c
            # Check if the change affects the non_hat_rows[y]
            # For column y
            lst = non_hat_rows[y]
            if prev_c != '^' and c == '^':
                # Remove x from lst
                idx = bisect.bisect_left(lst, x, key=lambda a: -a)
                if idx < len(lst) and lst[idx] == x:
                    lst.pop(idx)
            elif prev_c == '^' and c != '^':
                # Add x to lst if not present
                idx = bisect.bisect_left(lst, x, key=lambda a: -a)
                if idx >= len(lst) or (idx < len(lst) and lst[idx] != x):
                    lst.insert(idx, x)
        else:
            # 'A' event
            x = int(input[ptr])
            y = int(input[ptr+1])
            ptr +=2
            current_x = x
            current_y = y
            result = None
            while True:
                # Find first non '^' row in current_y <= current_x
                lst = non_hat_rows[current_y]
                idx = bisect.bisect_left(lst, current_x, key=lambda a: -a)
                if idx < len(lst):
                    x_prime = lst[idx]
                else:
                    # All rows in current_y are '^', exit to 0, current_y
                    result = (0, current_y)
                    break
                # Simulate row x_prime
                visited = set()
                current_col = current_y
                exit_found = False
                while True:
                    if current_col < 1 or current_col > m:
                        result = (x_prime, current_col)
                        exit_found = True
                        break
                    if current_col in visited:
                        result = (-1, -1)
                        exit_found = True
                        break
                    visited.add(current_col)
                    dir = grid[x_prime -1][current_col -1]
                    if dir == '^':
                        # Move up to x_prime-1, current_col
                        current_x = x_prime -1
                        current_y = current_col
                        break
                    elif dir == '<':
                        new_col = current_col -1
                    else:
                        new_col = current_col +1
                    if new_col <1:
                        result = (x_prime, 0)
                        exit_found = True
                        break
                    elif new_col >m:
                        result = (x_prime, m+1)
                        exit_found = True
                        break
                    else:
                        current_col = new_col
                if exit_found:
                    break
                # Continue processing with current_x and current_y
            print(result[0], result[1])

if __name__ == '__main__':
    main()
```

### Explanation
1. **Grid Initialization**: The grid is read and stored, and each column's non-'^' rows are tracked.
2. **Event Handling**: For each 'C' event, the grid is updated, and the non-'^' rows list is adjusted if necessary.
3. **Query Handling**: For each 'A' query, the movement is simulated by finding the first valid row using binary search, then simulating within that row. The simulation handles exits, loops, and upward movements efficiently.

This approach ensures that both queries and updates are handled efficiently, leveraging the constraints (especially the small column size) to optimize performance.