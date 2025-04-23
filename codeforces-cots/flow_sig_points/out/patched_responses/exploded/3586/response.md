<think>
Okay, let's try to understand this problem. So Gerald is placing chips on the border (but not corner) cells of an n x n grid. Then he moves them towards the opposite edge each minute for n-1 steps. The goal is to maximize the number of chips without any of the three failure conditions.

Hmm. So the failure conditions are:

1. Any chip lands on a banned cell.
2. Two chips are on the same cell at any time.
3. Two chips swap positions (pass each other) in a minute.

So we need to choose as many chips as possible such that their paths never overlap, don't hit any banned cells, and don't cross each other in a way that causes swapping.

Let me think about how the chips move. Each chip starts on a border (non-corner) cell. So the borders are the four edges of the square. But the corners are excluded. So each chip's path is along a straight line from one edge to the opposite. For example, a chip starting on the top edge (but not a corner) will move down each step until it reaches the bottom edge. Similarly for left to right, etc.

Wait, but movement is every minute, moving each chip into an adjacent cell. So each step, the direction is towards the opposite edge. So for example, a chip starting on the top row (but not corner) moves straight down each step. A chip on the left edge (but not corner) moves right each step, etc.

So each path is a straight line. The path of a chip is determined by its starting position. All the positions along that line must be checked for banned cells. Also, no two paths can intersect in a way that causes collisions or swaps.

So first, the problem reduces to selecting a set of such paths such that:

- None of the positions in any path are banned.
- The paths do not cross each other (i.e., their trajectories don't intersect in a way that would have two chips on the same cell or swapping).

Wait, how do the paths cross? Let's see. For example, if two chips start on the top and left edges. The top one moves down, the left one moves right. Their paths cross at (x,y) where x is the row of the left chip's path, and y is the column of the top chip's path. But when would their movement cause a swap?

Hmm, maybe we need to model each path as a line and see if any two paths cross. Also, during each step, the chips move to adjacent cells. So, for example, if two chips are moving towards each other along the same row (like one starting on the left edge and moving right, and another starting on the right edge moving left), their paths would cross. In such a case, they would pass each other at some point, leading to a swap.

So the third condition is about two chips swapping positions. So for example, if two chips are moving towards each other along the same line. Like, imagine a row with even length. Two chips start at each end. They move towards each other. At step (n-1)/2, they meet in the middle and swap positions. That's not allowed.

So the problem is to choose as many paths as possible, each starting from a non-corner border cell, such that:

1. No path includes a banned cell.
2. All paths are pairwise non-conflicting. Two paths conflict if their lines cross (i.e., share any cell during any step) or if their lines cross in a way that causes a swap.

Wait, but when do two paths cross? Let's model each path as a straight line. For a path starting on the top edge (non-corner), it moves down each step. So the path is a vertical line from top to bottom. Similarly, a path starting on the left edge (non-corner) moves right each step, forming a horizontal line.

So vertical paths (starting on top or bottom edges) are vertical lines. Horizontal paths (starting on left or right edges) are horizontal lines.

Wait, no. Wait, the starting positions are on the borders but not the corners. So for a vertical path (top to bottom), the starting position is on the top or bottom edge (but not the corner). So for example, a chip starting on (1, y), where y is not 1 or n. Then it moves down each step until it reaches row n. So the path is the column y, from row 1 to row n.

Similarly, a horizontal path starts on the left or right edge (but not corner), and moves right or left each step. So for a left edge start (x,1), where x is not 1 or n. The path is row x, moving right to column n.

So vertical paths are columns, and horizontal paths are rows.

Wait, but movement direction depends on which edge they start. For example, a chip starting on the left edge (non-corner) moves right each step. So the entire path is along that row. Similarly, a chip starting on the right edge (non-corner) moves left each step. So that's along the same row as well.

So, each vertical path is a column (since movement is vertical), each horizontal path is a row (movement is horizontal).

So for vertical paths (columns), each starts on the top or bottom edge (but not corner) and moves to the opposite edge. But wait, the direction depends on where they start. For example, a top edge start moves down, a bottom edge start moves up.

Wait, but the problem states that each chip moves from its original edge to the opposite edge. So the movement is towards the opposite edge. So for a top edge cell (row 1, column y), the movement is down, step by step, until row n. Similarly, a bottom edge cell (row n, column y) moves up to row 1.

But vertical paths (columns) and horizontal paths (rows) can't interfere with each other except at the intersection points. For example, a vertical path along column y and a horizontal path along row x will cross at (x,y). But that's only if both paths exist. If that cell (x,y) is part of both paths, then during step t, when the vertical chip is passing through (x,y) and the horizontal chip is passing through (x,y), they would collide. So that's not allowed.

Therefore, any two paths that cross at a cell (i,j) cannot both be selected. Because during their movement, their paths would meet there, leading to collision.

Additionally, two horizontal paths along the same row are impossible. Because they are moving in opposite directions (left to right vs right to left). Wait, no. For example, if two chips start on the left and right edges of the same row. Let's say row x. Then the left chip moves right, the right chip moves left. Their paths are the same row. So, during movement, they will pass each other. For example, in a row of even length, they'll swap positions in the middle. For odd length, they meet in the middle. Either way, this is not allowed. So two paths along the same row can't be selected. Similarly for two paths along the same column.

Moreover, even if two paths are in the same row but moving in the same direction (like both starting on the left edge of different rows and moving right) they are on different rows. So their paths don't interfere. Wait, no. Because each is in their own row. So their paths don't cross. So for rows, each row can have at most one path (either left to right or right to left). Wait, but if a row has a left edge start (moving right) and a right edge start (moving left), then their paths are the same row, leading to collision.

So, for rows and columns, each can have at most one path.

Wait, no. For a row x, if a chip starts on the left edge (x,1) moving right, then the path is the entire row x. Similarly, a chip starting on the right edge (x,n) moving left would have the same path. So selecting both would lead to their movement along the same row, which would collide. So for any row or column, you can select at most one path. Either a horizontal path (left to right or right to left) on that row, or a vertical path (top to bottom or bottom to top) on that column.

Wait, but vertical paths are along columns, horizontal along rows. So for a column y, if there's a vertical path, then no horizontal path can be in that column. Because if a horizontal path is in row x, column y is part of that path. But if there's a vertical path in column y, then any cell (x,y) along the horizontal path's row would be part of the vertical path's column. So when the horizontal path's chip is at (x,y) (which is part of their path), the vertical path's chip would pass through that cell at some step, leading to a collision.

Wait, perhaps not. Let's model two paths:

- A vertical path in column y: starts at (1, y) (top edge, non-corner, so y is not 1 or n). Moves down each step, so passes through all rows from 1 to n. So during step 0 (starting position), it's at (1,y). Step 1: (2,y), etc., until step n-1 (n,y).

- A horizontal path in row x: starts at (x, 1) (left edge, non-corner, so x is not 1 or n). Moves right each step. So during step 0: (x,1), step 1: (x,2), ..., step n-1: (x,n).

These two paths cross at (x, y). The vertical path's chip arrives at (x,y) at step x-1 (since it starts at row 1, and each step moves down). The horizontal path's chip arrives at (x,y) at step y-1 (since it starts at column 1, each step moves right). So if x-1 == y-1, then they arrive at the same cell at the same time. Otherwise, they arrive at different times, but the vertical path's chip is at (x,y) during step x-1, and the horizontal path's chip is at (x,y) during step y-1.

Wait, but the vertical path's chip is in column y for all steps. So during step t, it's at (1 + t, y). For t from 0 to n-1.

The horizontal path's chip is in row x, moving from column 1 to n. So during step t, it's at (x, 1 + t).

So when do they occupy the same cell? When 1 + t1 = x and y = 1 + t2. Wait, but for the vertical path, their position is (1 + t1, y), and for the horizontal path, (x, 1 + t2). So they are the same cell when 1 + t1 = x and 1 + t2 = y. But t1 and t2 can be different. So unless t1 = x-1 and t2 = y-1, but even then, unless x and y are related in some way.

Wait, for example, if x=3 and y=4. The vertical chip is at (1 + t1, 4), and the horizontal is at (3, 1 + t2). So if 1 + t1 = 3 → t1=2. Then 1 + t2 must be 4 → t2=3. So during step 2, the vertical is at (3,4), and during step 3, the horizontal is at (3,4). They are not there at the same step, so no collision. So in this case, they would not be on the same cell at the same time.

Ah, right. So two paths (vertical and horizontal) cross at (x,y), but their arrival times are different. So the vertical chip is there at t1 = x-1 steps, and the horizontal chip is there at t2 = y-1 steps. So unless x-1 = y-1, which would require x = y, they would not collide.

Wait, but if x = y, then t1 = x-1 and t2 = x-1. So both chips arrive at (x, x) at the same step. So that's a collision. So in that case, the two paths cannot coexist.

But if x != y, then the two paths cross at (x,y) but at different times, so no collision.

But the problem's second condition is that two chips cannot be on the same cell at the same time. So even if their paths cross at different times, it's allowed. Only when they are on the same cell during the same step.

So, the problem of selecting paths is such that no two paths' trajectories ever have two chips in the same cell at the same time, and also no swaps (third condition).

So let's model each possible path and check for conflicts.

But this seems complicated. How can we model all possible conflicts?

Alternative approach: each path is either a row (horizontal) or column (vertical) path. For each such possible path, check if:

1. The path does not contain any banned cells.
2. The path does not conflict with any other selected paths.

So, the problem reduces to selecting a maximum set of non-conflicting rows and columns that are not banned.

But how do we model conflicts between rows and columns?

Hmm. Let's consider that when we choose a row x (horizontal path), it's moving left to right or right to left. Similarly, a column y (vertical path) is moving top to bottom or bottom to top.

But for a row x path (left to right), it's moving through all cells (x,1), (x,2), ..., (x,n). Similarly, a vertical path in column y is moving through (1,y), (2,y), ..., (n,y).

Now, if two paths (a row x and column y) cross, then the cell (x,y) is in both paths. But the times when each chip is at (x,y) are different. The horizontal path's chip is at (x,y) at step y-1 (assuming moving from left to right). The vertical path's chip is at (x,y) at step x-1 (assuming moving from top to bottom). So unless x-1 = y-1, these steps are different, so no collision. But if x-1 = y-1 → x = y → then during step x-1 (or y-1), both chips are at (x,y) → collision.

So, in this case, a row x and column x cannot be selected together. Because their paths cross at (x,x) at the same step.

Similarly, if a row x is moving left to right (starts at (x,1)) and another row x is moving right to left (starts at (x,n)), then their paths are the same row. They would collide. So rows can't have two paths. Similarly for columns.

So, the conflict rules are:

1. For any row x, you can have at most one path (either left to right or right to left).
2. For any column y, you can have at most one path (either top to bottom or bottom to top).
3. A row x and column x cannot both be selected (their paths cross at (x,x) at the same step).
4. Additionally, the paths (rows and columns) must not contain any banned cells.

So, the problem is equivalent to choosing a subset of rows and columns such that:

- No two rows are the same, and no two columns are the same.
- For any selected row x and column y, x != y (since if x = y, their paths cross at (x,x) at the same step).
- All cells in each selected row or column are not banned.
- The maximum number of such rows and columns is achieved.

Additionally, for a row x to be selected, all cells in row x (from column 1 to n) must be allowed. Because the path is the entire row. Similarly for columns.

So the steps to solve this problem are:

1. Check all possible rows (non-corner start positions) and columns (non-corner start positions) to see if their entire path is allowed (no banned cells).

2. Then, model the problem as selecting a maximum set of rows and columns such that no row and column have the same index (x = y) and no overlapping rows or columns.

Wait, but how do we model that? Because for each row x selected, no column x can be selected, and vice versa. And rows and columns cannot have the same index. So the maximum possible is a bipartite graph where rows are one partition, columns the other, and edges between row x and column y if x != y. But that's not exactly helpful.

Alternatively, the problem is to choose a subset of rows and columns where for any row x and column y in the subset, x != y. And each row and column must be valid (all their cells are allowed).

So the maximum number of rows and columns we can choose is the maximum between:

- The number of valid rows plus the number of valid columns that are not in the valid rows' indices.

Or, more formally:

Let R be the set of valid rows (each row x is valid if all cells in row x are allowed and the start position is a non-corner border cell. Wait, no. Wait, the start positions for a row x are on the left or right edge, but not the corners. So for row x, the start positions are (x,1) if x is not 1 or n (since corners are excluded). Wait, no. Wait, the start positions must be on the border but not corners. So for a row x, the start positions are (x,1) (left edge) if x is not 1 or n. But if x is 1 or n, then (x,1) is a corner. So for a row x to be a valid horizontal path, x must not be 1 or n. So rows 1 and n can't have horizontal paths. Similarly, columns 1 and n can't have vertical paths.

Wait, the problem states that the chips are placed on border cells (non-corner). So the start positions must be on the border but not corner. So for a horizontal path (left or right edge), the row must not be 1 or n. Because, for example, (1,1) is a corner, but (1,2) is on the top edge. Wait, no. Wait, the borders are the four edges. The top edge is row 1, left edge column 1, etc. But the corners are (1,1), (1,n), (n,1), (n,n).

So for a horizontal path (left or right edge), the starting position must be (x,1) or (x,n) where x is not 1 or n. So the rows for horizontal paths are 2 ≤ x ≤ n-1. Similarly, vertical paths are columns 2 ≤ y ≤ n-1 (since the start positions are (1,y) or (n,y) where y is not 1 or n).

So a row x is valid for a horizontal path if:

- x is between 2 and n-1 inclusive.

- All cells in row x (from column 1 to n) are allowed (not banned).

Similarly for a column y to be valid for a vertical path:

- y is between 2 and n-1 inclusive.

- All cells in column y (from row 1 to n) are allowed.

So first, we need to check for each row x (2 <= x <= n-1) whether all cells in that row are allowed (not banned). Similarly for columns y (2 <= y <= n-1) whether all cells in that column are allowed.

Once we have the list of valid rows and columns, the problem becomes selecting a subset of rows and columns such that no row x and column x are both selected. The goal is to maximize the sum of the count of selected rows and columns.

Because selecting a row x and column x would have their paths cross at (x,x) during step x-1 (for row x) and step x-1 (for column x), leading to a collision.

So the problem reduces to maximum bipartite matching. Because we have a bipartition of valid rows and valid columns, and edges between row x and column y if x != y. But that's not exactly the case. Wait, no. Because rows and columns can be selected as long as their indices are different. So the constraints are that for any selected row x and column y, x can be equal to y only if neither is selected. Wait, no. Because row x and column x can't be both selected. So for each x, at most one of row x or column x can be selected.

Thus, the maximum possible sum is the sum of the number of valid rows plus the number of valid columns, minus the overlap. For example, if there are a valid rows and b valid columns, but c of them have x in both (i.e., row x and column x are both valid), then the maximum possible sum is a + b - c. Because for each x where both are valid, we can choose either the row or the column, but not both. So the maximum possible is a + b - c.

Wait, not exactly. Let's think: for each x where both row x and column x are valid, we can choose at most one (row x or column x). For other x's where only row x is valid, we choose it. For other y's where only column y is valid, we choose it.

So the maximum possible is (number of valid rows not overlapping with valid columns) + (number of valid columns not overlapping with valid rows) + max(number of overlaps where we take either row or column). Because for each x where both row x and column x are valid, we can take one. So the maximum is:

sum = (A - C) + (B - C) + C' 

where C is the number of x where both row x and column x are valid, and C' is the number of x where we take either row or column (so C' <= C). The maximum C' is C, so sum = (A - C) + (B - C) + C = A + B - C.

So the maximum possible is (A + B - C), where A is the number of valid rows, B the number of valid columns, C the number of x where both row x and column x are valid.

Wait, but how?

Let's take an example. Suppose A=3, B=3, C=2.

Then valid rows: x1, x2, x3.

Valid columns: y1, y2, y3.

But x1 = y1, x2 = y2, and x3 is not a valid column, etc. Wait, no. C is the number of x where row x is valid and column x is valid.

So if there are 2 such x's. Then, for those 2, we can take either the row or column, contributing 2. The remaining (A - C) rows (1) and (B - C) columns (1) can be taken. So total is 1 + 1 + 2 = 4. Which is A + B - C (3 +3 -2=4).

Yes. So the maximum sum is A + B - C.

So the approach would be:

1. For each row x (2 <= x <= n-1), check if all cells in row x are allowed. Collect all valid rows into a set R.

2. For each column y (2 <= y <= n-1), check if all cells in column y are allowed. Collect all valid columns into a set C.

3. Compute the number of x where x is in both R and C (C is the count of x where row x and column x are both valid).

4. The maximum possible is len(R) + len(C) - C.

So the answer is R_count + C_count - overlap_count.

But wait, this only considers the rows and columns. What about other paths?

Wait, the problem allows for chips to be placed on any border (non-corner) cells. So there are four possible edges: top, bottom, left, right. So a path can start on the top edge (non-corner) and move down (a column path), or on the left edge (non-corner) and move right (a row path), etc.

But according to the problem statement, each path is either a row or a column. Because the movement is towards the opposite edge. So a chip starting on the top edge (non-corner) must be part of a vertical path (column). Similarly, a chip starting on the left edge (non-corner) is part of a horizontal path (row).

So the maximum possible chips is the number of valid rows (horizontal paths) plus the number of valid columns (vertical paths) minus the overlaps. Because for each overlap (x exists in both R and C), we can choose to take either the row or the column, but not both.

Therefore, the answer is simply the sum of the valid rows and columns minus the number of overlapping indices.

So the steps to compute the answer are:

- For each row x in 2..n-1, check if all cells in row x are allowed (not banned). If yes, add to R.

- For each column y in 2..n-1, check if all cells in column y are allowed. If yes, add to C.

- Compute the intersection size between R and C (call this overlap).

- The answer is len(R) + len(C) - overlap.

But wait, why? Because for each x in the intersection, we can take either the row or the column, but not both. So the total is len(R) + len(C) - overlap.

Yes. For example, if x is in both R and C, then if we include both, the sum would have 2 entries, but since they are conflicting, we can only take one. So the maximum is len(R) + len(C) - overlap.

So this approach seems correct.

But then why does the second example have output 1?

In the second example, input is 3 0.

So n=3. Rows 2 is the only possible horizontal path (since x must be 2, which is between 2 and 2 (n-1=2). So for row 2, all cells (2,1), (2,2), (2,3) are allowed. So R has row 2.

Similarly, columns 2 is the only possible vertical path. Check if all cells in column 2 are allowed. Since m=0, yes. So C has column 2.

So len(R) =1, len(C)=1. Overlap is 1 (since x=2 is in both). So answer is 1+1 -1 =1. Which matches the sample.

Another sample: the third input.

n=4, m=3. Banned cells are (3,1), (3,2), (3,3).

So possible rows are 2 and 3 (since n-1=3). So check each row:

Row 2: all cells (2,1), (2,2), (2,3), (2,4). Are any of them banned? No. So row 2 is valid.

Row 3: check all cells in row 3. The cells (3,1), (3,2), (3,3) are banned. So row 3 is invalid.

So R is {2}.

Possible columns: 2,3.

Check column 2: cells (1,2), (2,2), (3,2), (4,2). (3,2) is banned. So column 2 is invalid.

Check column 3: cells (1,3), (2,3), (3,3), (4,3). (3,3) is banned. So column 3 is invalid.

So C is empty.

So len(R) =1, len(C)=0. Overlap is 0. Answer is 1+0 -0=1. Which matches the sample.

So this approach seems correct.

But what about the first sample? Input:

3 1

2 2.

So n=3. Rows possible: 2.

Check row 2: cells (2,1), (2,2), (2,3). (2,2) is banned. So row 2 is invalid. So R is empty.

Columns possible: 2.

Check column 2: cells (1,2), (2,2), (3,2). (2,2) is banned. So column 2 is invalid. So C is empty.

So answer is 0.

So the approach works.

So the steps are:

1. For each row in 2 <= x <= n-1:

   Check all cells in row x (columns 1 to n). If any cell (x, y) is banned, the row is invalid.

2. For each column in 2 <= y <= n-1:

   Check all cells in column y (rows 1 to n). If any cell (x, y) is banned, the column is invalid.

3. Count the number of valid rows (R), valid columns (C), and overlapping x where row x and column x are both valid.

4. Answer is R + C - overlap.

So now, the problem reduces to efficiently checking which rows and columns are valid, given the banned cells.

The challenge is to do this efficiently, given that n can be up to 1000, and m up to 1e5.

If m is 1e5, then for each banned cell, we can mark the row and column as invalid.

But how?

An alternative approach is:

- For each row x, track if it has any banned cells. For row x, if any cell in the row is banned, the row is invalid.

Similarly for columns.

But to check this, for each row x, we can check if the row is in the banned rows.

But how to represent this?

The banned cells can be stored in a set. Then, for each row x (2 <= x <=n-1), check for all y in 1..n, if (x, y) is in the banned set. If any, then the row is invalid.

But for n=1e3, checking each row (n-2 rows) and for each row, checking all n columns would take O(n^2) time, which is 1e6 operations. For m up to 1e5, this is acceptable.

But wait, perhaps there's a smarter way. For each banned cell (x,y), if x is in 2..n-1, then the row x is invalid. Similarly, if y is in 2..n-1, then the column y is invalid.

But that's not correct. Because a row is invalid only if at least one of its cells is banned. So for example, if a row x has at least one banned cell, then the entire row is invalid. So for each row x, we can track if there's any banned cell in that row.

Similarly for columns.

So the approach is:

- Create a set of banned cells.

- For each row x in 2..n-1:

   Check if any (x, y) in banned cells for y in 1..n.

   If any exists, mark row x as invalid.

- Similarly, for each column y in 2..n-1:

   Check if any (x, y) in banned cells for x in 1..n.

   If any exists, mark column y as invalid.

So how can we do this efficiently?

An efficient way would be to precompute for each row x, how many banned cells are in it. Similarly for columns.

But with m up to 1e5, and n up to 1e3, perhaps for each row x, we can track the count of banned cells in it. Then, if the count is >=1, the row is invalid.

But how?

We can create a dictionary or array for rows and columns.

Initialize two arrays:

row_banned = [False] * (n+1)  # row_banned[x] is True if row x has any banned cell.

col_banned = [False] * (n+1)  # col_banned[y] is True if column y has any banned cell.

Then, for each banned cell (x, y):

   if x is in 2..n-1:

      row_banned[x] = True

   if y is in 2..n-1:

      col_banned[y] = True

Wait, no. Because for a row x (which could be in 2..n-1), if any cell (x, y) is banned (for any y), then the entire row is invalid.

So, for all (x, y) in banned cells:

   if x is in 2..n-1:

      row_banned[x] = True

   if y is in 2..n-1:

      col_banned[y] = True

So after processing all banned cells, for a row x in 2..n-1, row_banned[x] is True if there's any banned cell in row x.

Similarly for columns.

This is O(m) time, which is acceptable for m=1e5.

Because for each banned cell, we check if x is in 2..n-1 and mark row x as invalid. Similarly for y.

Once we have row_banned and col_banned arrays, we can compute:

R = number of x in 2..n-1 where row_banned[x] is False.

C = number of y in 2..n-1 where col_banned[y] is False.

overlap is the number of x in 2..n-1 where row_banned[x] is False and col_banned[x] is False.

Because for x in 2..n-1, if both row x and column x are valid (not banned), then they are in the overlap.

So the answer is R + C - overlap.

So the steps are:

1. Read n and m.

2. Read m banned cells. For each (x,y):

   a. if x is between 2 and n-1 inclusive, then mark row x as banned.

   b. if y is between 2 and n-1 inclusive, then mark column y as banned.

3. Compute R: the number of x in 2..n-1 where row x is not marked as banned.

4. Compute C: the number of y in 2..n-1 where column y is not marked as banned.

5. Compute overlap: the number of x in 2..n-1 where row x is not banned and column x is not banned.

6. Answer is R + C - overlap.

Wait, but why are the overlap x's the same for row x and column x? Because for x in 2..n-1, row x and column x are separate. So the overlap is the count of x where both row x and column x are valid.

Yes.

So this approach is O(m) time (processing m banned cells) plus O(n) time for counting R and C and overlap.

Which is acceptable for n up to 1e3 and m up to 1e5.

This is a very efficient approach.

Now let's test this logic with the examples.

First example:

n=3, m=1. Banned cell (2,2).

For rows x in 2 (since 2..n-1 is 2..2). For x=2: any banned cells in row 2? Yes, (2,2). So row 2 is banned. R=0.

For columns y in 2. Any banned cells in column 2? (2,2) is banned. So column 2 is banned. C=0.

overlap=0. So answer is 0.

Second example:

n=3, m=0.

row 2 is not banned (no cells are banned). R=1.

column 2 is not banned. C=1.

overlap=1 (x=2 is in both). answer 1+1-1=1.

Third example:

n=4, m=3. Banned cells are (3,1), (3,2), (3,3).

rows are 2 and 3 (since 2..3).

Check for each row:

Row 2: banned cells? The banned cells are (3,1), (3,2), (3,3). So row 2 has no banned cells. So row 2 is valid. R=1.

Row 3: any banned cells in row 3? Yes, (3,1), (3,2), (3,3) are all in row 3, but x=3 is in 2..3 (since n-1=3 for n=4). So row 3 is banned. So R=1.

columns are 2 and 3 (since 2..3).

Check column 2:

any banned cells? (3,2) is banned. So column 2 is banned. C=0.

column 3: (3,3) is banned. So column 3 is banned. C=0.

overlap is 0. answer is 1+0-0=1.

So yes, this approach works.

Thus, the code can be written as follows.

Read n and m.

Initialize row_banned and col_banned arrays of size (n+1) (since rows and columns are 1-based) as False.

For each banned cell (x, y):

   if x >=2 and x <=n-1:

       row_banned[x] = True

   if y >=2 and y <=n-1:

       col_banned[y] = True

Then compute:

R = sum(1 for x in 2..n-1 if row_banned[x] is False)

C = sum(1 for y in 2..n-1 if col_banned[y] is False)

overlap = sum(1 for x in 2..n-1 if (row_banned[x] is False and col_banned[x] is False))

Answer = R + C - overlap

So that's the code.

But wait, for x in 2..n-1, and the same for y. For example, for n=3, 2..n-1 is 2..2.

So code can be written in Python as:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    row_banned = [False] * (n + 1)
    col_banned = [False] * (n + 1)

    for _ in range(m):
        x, y = map(int, input_stream.readline().rstrip("\n").split())
        if 2 <= x <= n-1:
            row_banned[x] = True
        if 2 <= y <= n-1:
            col_banned[y] = True

    R = 0
    for x in range(2, n):
        if not row_banned[x]:
            R += 1

    C = 0
    for y in range(2, n):
        if not col_banned[y]:
            C += 1

    overlap = 0
    for x in range(2, n):
        if not row_banned[x] and not col_banned[x]:
            overlap += 1

    print(R + C - overlap, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 0
""",
            "output": \
"""\
1
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    row_banned = [False] * (n + 1)
    col_banned = [False] * (n + 1)

    for _ in range(m):
        x, y = map(int, input_stream.readline().rstrip("\n").split())
        if 2 <= x <= n-1:
            row_banned[x] = True
        if 2 <= y <= n-1:
            col_banned[y] = True

    R = 0
    for x in range(2, n):
        if not row_banned[x]:
            R += 1

    C = 0
    for y in range(2, n):
        if not col_banned[y]:
            C += 1

    overlap = 0
    for x in range(2, n):
        if not row_banned[x] and not col_banned[x]:
            overlap += 1

    print(R + C - overlap, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 3
3 1
3 2
3 3
""",
            "output": \
"""\
1
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

Third example:

4 3.

Banned cells (3,1), (3,2), (3,3).

Processing each cell:

For (3,1):

x=3 is between 2 and 3 (since n=4, n-1=3). So row_banned[3] = True.

y=1 is not in 2..3, so col remains.

For (3,2):

x=3 → row_banned[3] already True.

y=2 is in 2..3 → col_banned[2] = True.

For (3,3):

x=3 → row_banned[3] remains True.

y=3 → in 2..3 → col_banned[3] = True.

So row_banned[2] is False.

R is for x in 2,3:

x=2 → not banned. R +=1.

x=3 → banned. So R is 1.

C is for y in 2,3:

y=2 → banned.

y=3 → banned. So C=0.

overlap for x in 2,3:

x=2: row not banned, col_banned[2] is True. So no overlap.

x=3: row is banned. So no.

overlap=0.

So answer is 1+0 -0=1.

Yes.

Thus, this code should work correctly.
</think>

```python
n, m = map(int, input().split())

row_banned = [False] * (n + 1)
col_banned = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    if 2 <= x <= n - 1:
        row_banned[x] = True
    if 2 <= y <= n - 1:
        col_banned[y] = True

R = sum(1 for x in range(2, n) if not row_banned[x])
C = sum(1 for y in range(2, n) if not col_banned[y])
overlap = sum(1 for x in range(2, n) if not row_banned[x] and not col_banned[x])

print(R + C - overlap)
```
