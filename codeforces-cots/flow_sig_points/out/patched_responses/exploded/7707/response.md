<think>
Okay, let's try to solve this problem. Hmm. The problem is about a chocolate bar that's an n x n grid. The initial step is that Andrew eats all pieces below the anti-diagonal. Then, he performs q actions where each action starts on the anti-diagonal (since xi + yi = n+1) and moves either up or left until he hits an already eaten piece or the edge. After each action, we need to output how many new pieces he ate in that step.

So, the main challenge is to model the state of the anti-diagonal and track which parts have been eaten, especially along the directions. Since n can be up to 1e9 and q up to 2e5, we need an efficient data structure that can handle these ranges without using too much memory or time.

Let me think. Each action starts at (xi, yi) on the anti-diagonal. The direction is either up or left. For example, if the direction is 'U', he moves up (decreasing row) until he hits an eaten piece. Similarly, 'L' direction is moving left (decreasing column). Each move in the action eats the pieces along that path. But the problem is that after each action, these paths can split the remaining area into regions. So, the key is to track, for each cell on the anti-diagonal, how far up or left he can go before hitting an already eaten region.

Wait, but each action starts on the anti-diagonal. So, for each cell (x, y) on the anti-diagonal (x + y = n+1), when an action is taken here, moving up (U) would start at (x, y) and move to (x, y-1), (x, y-2), etc., until it can't. Similarly, moving left (L) would go (x-1, y), (x-2, y), etc. Each of these directions' paths starts from the anti-diagonal and goes up or left, but the path length depends on existing eaten regions.

The initial state is that everything below the anti-diagonal is eaten. So, the anti-diagonal and above are initially uneaten except for the anti-diagonal. Wait, wait. Wait, the problem says: after eating below the anti-diagonal, he performs actions on the remaining triangular part, which includes the anti-diagonal. So the anti-diagonal is part of the remaining area. Then each action starts on the anti-diagonal. Wait, no: the problem says the chosen cell is on the anti-diagonal. So each action starts at a cell (x, y) where x + y = n+1.

When the action is 'U' (up), he starts at (x, y) and moves up (y decreases) until he hits an edge or eaten piece. Similarly, 'L' (left) moves x decreases. The count is the number of pieces eaten in this action, which includes the starting cell.

But how do we model the eaten regions along the anti-diagonal and the possible directions? For each cell on the anti-diagonal, once it's eaten in some direction, any subsequent actions that would overlap would have their paths blocked.

Wait, but when you process an action starting at (x, y), the path moves in a direction (up or left) and eats all cells along that path until a block. However, once a cell is eaten, it's considered blocked for all future actions.

So, for each cell on the anti-diagonal, we need to track whether the up or left direction from that cell has been used. Because, once a direction is used, any subsequent action in that direction from that cell will start but immediately stop (since the first cell is already eaten). Also, actions in the opposite direction can affect the available cells.

Wait, for example: consider a cell (x, y) on the anti-diagonal. Suppose the first action is 'U', which eats all cells from (x, y) upwards (i.e., moving up in the same column). The next action could be 'L' from the same cell. In that case, moving left in the same row would proceed until it hits an already eaten cell. But if the 'L' action is processed first, then the 'U' action might not be blocked until it hits the edge.

But how do the up and left directions from the same cell interfere with each other?

Alternatively, each cell on the anti-diagonal can have two possible directions. Once a direction is activated (i.e., processed), the other direction's path is limited by the initial activation. For example, if you process 'U' first from (x, y), then the path for 'L' from (x, y) would start at x and move left, but the row is fixed as y. But the 'U' path has already taken some cells in the same column, but that's in a different row. Wait, perhaps the 'U' and 'L' directions are independent except for the starting cell. Because the 'U' path is in the same column, moving up, while 'L' path is in the same row, moving left.

Wait, the starting cell is on the anti-diagonal. So, when moving 'U' from (x, y), the path is (x, y), (x, y-1), ..., up to (x, 1) if possible. But if any of those cells were already eaten by a previous action, then this path stops. Similarly for 'L' direction, moving left in the row: (x, y), (x-1, y), ..., (1, y).

But the initial state is that the cells below the anti-diagonal are already eaten. The cells on the anti-diagonal and above are uneaten initially. Wait, no. Wait, the problem says: first Andrew eats all pieces lying below the anti-diagonal. Then he performs actions on the remaining triangular part (the anti-diagonal and the area above it). So the anti-diagonal cells are part of the remaining area and are not eaten initially. So the actions are what's causing the cells (including those on the anti-diagonal) to be eaten.

Wait, that's important. So the initial state is that all cells below the anti-diagonal are eaten, and the cells on and above the anti-diagonal are uneaten. Then, each action starts from a cell on the anti-diagonal (since xi + yi = n+1) and moves in a direction, eating all cells until it hits an already eaten cell or the edge. Each action starts by eating the starting cell (since it's part of the path).

So the problem is, for each action, the number of cells eaten is the number of cells in the path starting from (x, y) in the given direction, not eaten yet. So, when processing an action, we need to find how far in the given direction the cells are uneaten.

So, for each action, the starting cell (x, y) is on the anti-diagonal. Let's model for each direction (up and left) and for each cell on the anti-diagonal, what is the maximum distance that has been already eaten.

Wait, perhaps for each cell (x, y) on the anti-diagonal, we can track two variables: the maximum number of steps taken in the 'U' direction and the 'L' direction. However, since n is up to 1e9, we can't track this for each cell. Instead, we need to model this with some intervals or structures that can be queried and updated efficiently.

Let me think. For the anti-diagonal, the cells are arranged such that x + y = n+1. Each cell on the anti-diagonal can be uniquely identified by x (since y is determined as n+1 -x). So, x ranges from 1 to n. For each x in 1..n, we can model the left and up steps taken from (x, y).

But for n up to 1e9, we can't have an array for each x. So we need a way to track these steps for the cells that have been processed. Since each action can only process a cell once (since once you process it, the next action on the same cell and direction would have zero steps), maybe we can track for each cell (x) whether it has been processed in the 'U' or 'L' direction.

Wait, but in the problem statement, the sample input shows that a cell can be processed multiple times. For example, in the second sample input, the cell (10, 1) is processed in the 2nd action (U) and again in the 5th action (L). The fifth action's output is zero because the cell was already eaten in the 2nd action. Wait, no. Let me check the second sample input:

The fifth action is at (10,1) direction L. But according to the note, the fifth action starts at cell (10,1) which was already eaten in the second action. So, when the action is processed, the starting cell is already eaten (since when you process a direction from a cell, the starting cell is eaten as part of that action). So, any subsequent action on the same cell (regardless of direction) will start from a cell that's already eaten, hence the path length is zero.

So, for each cell (x) on the anti-diagonal, each direction (U or L) can be processed at most once. Because once you process a direction, the starting cell (x) is eaten. So any subsequent action on that cell (regardless of direction) will start from an already eaten cell and thus have zero steps.

Wait, no. Let's say the first action is on cell (x, y) direction U. That action eats the starting cell (x, y) and moves up, so the next action on (x, y) in direction L would start from (x, y) which is already eaten. So the result would be zero. Therefore, each cell can be processed at most once in either direction, and once processed in either direction, no further actions on that cell can eat anything.

Wait, but that's not entirely correct. Let's think: when you process direction U from cell (x, y), you eat the starting cell (x, y) and all cells above it in the same column until a block. Then, processing direction L from the same cell (x, y) would start from (x, y) which is already eaten. So that action would result in zero.

Therefore, for each cell on the anti-diagonal, once either direction has been processed, any subsequent action on that cell will not eat any pieces (because the starting cell is already eaten). Therefore, each cell can be processed at most once, in either direction.

So, the problem reduces to: for each action, check whether the cell (x) has been processed before (in any direction). If yes, output 0. Else, process the given direction, and compute how many steps can be taken in that direction until hitting an already eaten cell or the edge.

Wait, but the edge is the boundary of the chocolate. For example, moving left from (x, y) can go to x=0 (which is beyond the grid), but the path stops at x=1. Wait, the grid is 1-based. So moving left from x=3 would go to x=2, x=1, then can't go further. Similarly, moving up from y=4 would go to y=3, 2, 1.

But when moving in the given direction, the path is from the starting cell until the edge or a previously eaten cell.

So, for a direction 'U' (up) from cell (x, y), the maximum possible steps are (y-1) steps (since the starting cell is y, and moving up each step decreases y by 1, stops at y=1). But if there are other actions in the same column that have already been processed (from cells higher up on the anti-diagonal), then the current 'U' path might hit those.

Wait, no. Because the anti-diagonal is processed in the order of the actions. Let's take an example. Suppose n=6. The anti-diagonal has cells (x, y) where x + y = 7. For example, cell (3,4) is on the anti-diagonal. Suppose the first action is 'U' at (3,4). Then, the path is (3,4), (3,3), (3,2), (3,1). So that's 4 cells. Now, suppose later there's an action 'U' at (4,3) (another cell on the anti-diagonal). The path would be (4,3), (4,2), (4,1). But in this case, since (3,4) is in a different column, the path of (4,3) in 'U' direction is not affected. However, if there's an action in the same column as (3,4), but higher up (like (5, 2)), then processing 'U' from (5,2) would start at (5,2) and go up. But the path in that column would be (5,2), (5,1). But these are in the same column as (3,4) was processed, but that's a different column. So each column's 'U' actions are independent.

Wait, but maybe not. For example, suppose you process 'U' from (3,4) (column 3), which eats cells (3,4), (3,3), ..., (3,1). Then, if you process 'L' from (3,4), which would be moving left in row 4, but since the cell (3,4) is already eaten, this action would have 0 steps. But another action in 'L' direction from (2,5) (same row as (3,4) is in the anti-diagonal) would process row 5's cells. So, different rows and columns are handled independently.

So, the key is that each cell on the anti-diagonal can be processed in either direction once. Once processed in any direction, any further actions on that cell will have zero steps.

Wait, but how about the following scenario: a cell (x, y) on the anti-diagonal is processed in 'U' direction. Then, in a later action, a cell (x', y') on the same column as (x, y) (i.e., x' = x) is processed in 'U' direction. But since (x, y) is higher up (since y' = n+1 -x', and x' =x implies y' = n+1 -x = y), so the same cell. So that can't happen. Because x' can't be x again unless it's the same cell.

So, each cell on the anti-diagonal is unique. Each action is on a unique cell (since xi + yi =n+1 and (xi, yi) is part of the input), so each cell is processed once in either direction. Wait, but the input can have multiple actions on the same cell. For example, the second sample input has two actions on (10,1) (the fifth and second actions). The fifth action's output is 0 because the starting cell was already eaten by the second action.

So, for each cell on the anti-diagonal, if any action (either U or L) has been processed on it before, then any subsequent action on it will result in 0.

Thus, for each cell, we can track whether it's been processed. If yes, output 0. Otherwise, process the direction and compute the steps.

So, the main challenge is to track which cells have been processed. Since the maximum number of queries is 2e5, we can use a hash set or a dictionary to track the processed cells. For each action, check if the cell is already in the set. If yes, output 0. Else, add it to the set and process the direction.

Now, for processing the direction, once we know the cell hasn't been processed before, we need to compute how many steps can be taken in the given direction.

For direction 'U' (up), the path is along the same column (x fixed), starting from y, moving up. The maximum possible steps is y-1 (since y starts at 1-based, so moving up to y-1, y-2, ..., 1). But if there are other cells in the same column that have been processed with 'U' direction above the current cell, then the path would be blocked.

Wait, no. Because once you process a cell (x, y) in the 'U' direction, you eat all cells from (x, y) up to (x,1). But if there's another cell (x, y') where y' < y on the same column, but processed in 'U' direction, that would have already eaten the cells up to (x,1). So, processing a higher cell (y' > y) in 'U' direction would have no effect, but since the cell (x, y) is on the anti-diagonal and any processing of that cell would have to be the first in any direction.

Wait, this seems conflicting. Let's clarify.

Each cell on the anti-diagonal can be processed once. So, for example, in column x, the cell (x, y) is part of the anti-diagonal. If you process 'U' from this cell, then you eat (x, y), (x, y-1), ..., (x,1). Now, any cell in column x that's part of the anti-diagonal below (x, y) (i.e., higher y) cannot exist, because the anti-diagonal is x + y = n+1. So, for a given x, there's exactly one cell (x, y) on the anti-diagonal. So, once that cell is processed in 'U' direction, all cells in column x from y down to 1 are eaten. Any other cells in column x that are part of the anti-diagonal cannot exist except for (x, y).

So, for direction 'U', the steps are y - 1 (since the starting cell is at y, and you can move up y-1 steps to reach y=1). But wait, the starting cell is (x, y), and moving up would take steps until the edge. So, the number of steps is y - 1. But in the first sample input:

In the first sample input, n=6. The first action is 3 4 U. The cell is (3,4) (since 3+4=7=6+1). The direction is U, so moving up. The starting y is 4, so the steps are 4-1=3 steps. So, the path is 4 cells (including the starting cell). Which matches the output of 4.

So, the formula for 'U' direction is (y steps) because from (x,y) moving up y cells: y, y-1, ..., 1. So the number is y.

Wait, 3 4 U: y is 4. So moving up, the steps are (4,3,2,1) → 4 cells. So the count is 4.

Yes. So the count for 'U' direction is y steps. But only if there are no other processed cells in that column blocking the path.

Wait, no. Because once you process 'U' from (x, y), all cells in column x from (x, y) to (x, 1) are eaten. So, any subsequent processing of 'U' in column x (but that would require another cell on the anti-diagonal in column x, which is impossible). So, each cell in the anti-diagonal is unique. So, once a cell in column x is processed in 'U', the entire column from that cell upwards is eaten. So, the steps are y.

But how about the 'L' direction. For 'L' direction, the steps are x-1. Because moving left from x to 1. So the number of steps is x steps (including x, x-1, ..., 1). For example, in the second sample input's first action: 2 9 U. The cell is (2,9), direction U. The steps are 9, so output is 9.

Yes. So, for 'U' direction, the number of cells is y (current cell's y coordinate). For 'L' direction, it's x.

But wait, this is only true if there are no other processed cells in the same row (for 'L') or column (for 'U') that would block the path. But how?

Wait, for example, suppose in row y, there are multiple cells on the anti-diagonal. For example, in row y=5, n=6. The anti-diagonal cells are x=2 (since 2 +5=7=6+1). If you process 'L' from (2,5), then the steps are 2 (x=2, x-1=1). So, the count is 2. Then, another action on (1,6) (same row y=6?), no, wait, (1,6) is part of the anti-diagonal (since 1+6=7). So, if you process 'L' from (1,6), the steps are 1 (x=1). But in the same row y=6, but that's a different row. So, no overlapping.

So, the conclusion is that for a cell (x, y) on the anti-diagonal:

- If the direction is 'U', then the maximum possible steps is y (including the starting cell), but this is only possible if no cells in the same column and higher up (i.e., same x, lower y) have been processed. But since each column can have only one cell on the anti-diagonal (since x + y = n+1), once you process 'U' from that cell, the entire column from that cell up is eaten. So, the steps are exactly y.

Similarly, for 'L' direction, the steps are x.

But wait, what if there are other cells in the same row that have been processed with 'L' direction? For example, in row y, if another cell in the same row (but different column) processed 'L' before, then their paths might block each other.

No, because each cell on the anti-diagonal is in a unique row. Because x + y =n+1, so for a given y, x is determined. So, each row has exactly one cell on the anti-diagonal. So, when you process 'L' direction from that cell, you eat all cells in that row from x down to 1. So, the steps are x.

So, the conclusion is that for a cell (x, y) on the anti-diagonal:

- If the direction is 'U', the number of steps is y.

- If the direction is 'L', the number of steps is x.

But this is only true if the cell hasn't been processed before. If it has been processed (in any direction), then the steps are 0.

Wait, but this can't be correct. Because in the first sample input, the third action is (2,5) L. The x is 2. So the steps would be 2 (x=2, x-1=1). The output is 2, which matches. The fourth action is (1,6) U. The y is 6, so steps would be 6. But the output is 1. So this contradicts the conclusion.

Ah, wait. So this approach is wrong. Let's see why.

In the first sample input:

n=6. So the anti-diagonal is x + y =7.

The first action is 3 4 U. So x=3, y=4. 'U' direction. The steps would be 4 (y=4). Output is 4. Correct.

Second action is 6 1 L. x=6, direction L. Steps would be 6 (x=6). Output is 3. Hmm, this contradicts. So the initial approach is wrong.

Wait, the output for the second action is 3, but according to the approach, x=6 would give 6 steps. So why is the output 3?

Ah, I see. Because when you process 'L' direction from (6,1), which is x=6, direction L. The path is moving left along the same row (y=1). The cells are (6,1), (5,1), (4,1), (3,1), (2,1), (1,1). But why is the output 3?

Wait, the sample input's second action is 6 1 L, output is 3. How?

Hmm, this suggests that there's a mistake in the initial reasoning. Let's re-examine the problem statement.

Wait, the initial state is that all cells below the anti-diagonal are eaten. The anti-diagonal and the area above are uneaten. So, the anti-diagonal is part of the remaining area. So, the starting cell (x, y) is initially uneaten. The first action on that cell will eat it.

So, for the second action in the first sample:

The cell is (6,1). x=6, y=1. Direction L (left). So moving left from x=6 in row y=1. The cells to the left are x=5,4,3,2,1. But since the initial state is that all cells below the anti-diagonal are eaten. The anti-diagonal is x + y =7. So for row y=1, the cells in columns x >=7-1+1=7? Wait, no. Wait, the anti-diagonal is x + y =n+1 =6+1=7. So cells below the anti-diagonal are those where x + y >7. Because if x + y >7, then they are below the anti-diagonal.

Wait, the anti-diagonal is from lower left (n,1) to upper right (1,n). So cells below the anti-diagonal are those where the sum x + y >n+1. Wait, perhaps I have the orientation wrong.

Wait, the anti-diagonal is the line from the lower left corner (n,1) to upper right corner (1, n). So for a cell (x, y), if x + y < n+1, it's above the anti-diagonal. If x + y >n+1, it's below. Because the line x + y =n+1 is the anti-diagonal. So cells below the anti-diagonal are those where x + y >n+1. These are the ones that were eaten initially.

So, for row y=1 (n=6), the cells in columns x where x +1 >7 → x>6. So in row 1, columns 7, 8, ... but n is 6. So there are no cells below the anti-diagonal in row 1. So the entire row is above the anti-diagonal, except for the cell (6,1), which is on the anti-diagonal. So the initial state of row 1 is that all cells except (6,1) are part of the remaining triangular area. But wait, no. The cells below the anti-diagonal are those with x + y >n+1. So for y=1, x + y >7 → x>6. But since x can't exceed 6 (n=6), there are no cells below the anti-diagonal in row 1. So, all cells in row 1 (columns 1-6) are part of the remaining triangular area. However, the anti-diagonal cell (6,1) is part of the remaining area but not eaten initially.

So, the initial state is that all cells (x, y) where x + y >7 are eaten. The others (x + y ≤7) are uneaten. So the remaining area is the triangle including the anti-diagonal.

So, for the second action in the first sample: (6,1) L direction. The starting cell is (6,1), which is uneaten. The direction is left. So moving left in row 1, starting at x=6, moving to x=5,4,3,2,1. But the cells in row 1 are initially uneaten (since x + y =6+1=7 ≤7). So why is the output 3?

Ah, because when you process this action, you eat all the cells in the path until you hit an already eaten cell or the edge. But the edge here is x=1. So why isn't the output 6 (from x=6 down to x=1, which is 6 steps, including the starting cell)?

But according to the sample input, the output is 3 for the second action. So the initial reasoning is wrong. So there's something missing here.

Wait, perhaps the path is blocked by already eaten cells. For example, perhaps some cells in row 1 have been eaten by previous actions. Let's look at the first sample's actions.

First action: (3,4) U. So it's in column 3, moving up from y=4 to y=1. So in column 3, cells (3,4), (3,3), (3,2), (3,1) are eaten. So in row 1, column 3 is now eaten.

Second action is (6,1) L. So in row 1, moving left from x=6 to x=5,4,3,2,1. But when moving left, after eating x=6,5,4, the next cell is x=3. But column 3 in row 1 was already eaten by the first action. So the path stops here. So the cells eaten in this action are x=6,5,4,3. Wait, but x=3 is already eaten, so the path would stop before eating x=3.

Wait, the action starts at (6,1). It eats (6,1) → moves left to (5,1), which is uneaten. Then (4,1) → uneaten. Then (3,1) → which was eaten by the first action. So the path stops here, eating (6,1), (5,1), (4,1). That's 3 cells. Hence the output is 3.

Ah, I see. So the path can be blocked by cells eaten by previous actions in other directions. So the steps are not simply x or y. We need to track for each row and column, up to where they have been eaten.

So, for example, in the 'L' direction, moving along a row. For each row, the leftmost eaten cell in that row (closest to x=1) blocks further movement. Similarly, in the 'U' direction, moving along a column, the lowest eaten cell (closest to y=1) blocks further movement.

Thus, the problem requires for each row and column, track the furthest point that has been eaten. For example:

- For each row y, track the maximum x (call it left_bound[y]) such that all cells from x=1 up to x=left_bound[y] in row y have been eaten. So, when processing a 'L' action in row y (starting at x0), the number of steps is the minimum between x0 and the left_bound[y] +1. Or wait, perhaps not. Let's think.

Wait, when processing 'L' direction from (x, y), the path is from x down to 1. But if there's a left_bound[y] that is >=x, then all cells from x to 1 are already eaten, so the action's steps would be 0. But if left_bound[y] is less than x, then the steps would be x - left_bound[y] - 1 +1 =x - left_bound[y].

Wait, no. For example, if left_bound[y] is 3, then cells up to x=3 in row y are eaten. Now, processing 'L' from x=5. The path starts at 5, then 4, then 3. Since 3 is already eaten, the path stops. So the steps are 5-3 = 3 (cells 5,4,3). But 5-3=2 steps, but 3 cells. So the count is (5-3) +1? Or maybe it's (current x - left_bound[y]).

No. Let's see:

current x is 5. left_bound[y] is 3. So the maximum x that can be eaten is 3+1=4? Or maybe the left_bound[y] represents the rightmost eaten cell in row y. For example, if left_bound[y] is 3, it means that cells x=1 to x=3 are eaten. So any 'L' action in row y starting at x>3 would be able to eat x down to 3+1=4? No, that doesn't make sense.

Alternatively, perhaps left_bound[y] represents the maximum x in row y that has been eaten. So, if left_bound[y] is 3, then all cells in row y with x <=3 are eaten. So when processing 'L' direction from x=5, the path can be eaten until x=3+1=4 (since 3 is already eaten). So the steps would be 5-4 +1 = 2 steps (5 and 4). But in this case, the starting cell x=5 is not eaten yet. Wait, no. The left_bound[y] is the maximum x such that cells x <= left_bound[y] are eaten. So in this case, left_bound[y] is 3. Cells 1-3 are eaten. So when processing 'L' from x=5, you can eat cells 5,4,3. But cell 3 is already eaten. So the path stops at 3. So the count is 3 (5,4,3). But 5-3+1 =3. So the count is (x - new_left_bound +1), where new_left_bound is max(x, left_bound[y])?

Hmm. It's getting complicated. Maybe we need to track for each row y the maximum x such that all x' <=x are eaten. When processing 'L' direction from x0, the number of cells eaten is max(0, x0 - current left_bound[y]). Because current left_bound[y] is the current maximum x in row y that's eaten. So, the steps would be x0 - current left_bound[y], but only if x0 > current left_bound[y].

For example:

current left_bound[y] =3. processing 'L' from x0=5.

x0 is 5>3, so steps are 5-3=2 (cells 5,4,3?), but wait, 5-3 is 2. But that's 3 cells. So perhaps the count is (x0 - current_left_bound) but the actual steps are from x0 down to current_left_bound +1.

Wait, perhaps:

number of steps = x0 - new_left_bound.

Wait, if current_left_bound is 3, and x0 is5, then the new_left_bound becomes5. The steps eaten are 5,4. Because up to current_left_bound+1 (3+1=4). So the steps are 5-3=2. But in this case, the count is 2 (cells 5 and4).

But in the example from the first sample:

The second action is 'L' from x=6, y=1. Initially, left_bound[y=1] is 0 (since no action has been taken in row 1). So x0=6>0. So steps are 6-0=6. But in the sample output, the steps are3. So this model is incorrect.

Hmm, what's wrong here. Let's re-examine the first sample's second action:

The first action was (3,4) U. Which, when processed, eats column3 from y=4 down to y=1, including (3,1).

So, in row y=1, the cell x=3 is eaten. So the left_bound for row 1 is 3.

Now, the second action is (6,1) L. So processing 'L' in row1, starting at x=6. The current left_bound for row1 is3. So the steps would be 6-3=3 (cells 6,5,4,3?), but wait, 6-3=3. How many cells are eaten?

Wait, the left_bound is the maximum x in the row that is already eaten. So, in row1, all x <=3 are eaten. So when processing 'L' from x=6, the path is x=6,5,4,3. Because x=3 is already eaten, so the path stops there. So the number of steps is 4 (6-3 +1?), but according to the sample output, it's3.

Wait, the sample output for the second action is3. So this approach is not working.

Alternatively, perhaps for 'L' direction, the steps are x0 - current_left_bound. Because if current_left_bound is3, then x0=6 can process cells from x=6 down to current_left_bound+1 (4), thus steps of 6-3=3 (cells 6,5,4). Then, the new_left_bound becomes6.

Yes! That makes sense. So, for 'L' direction:

The left_bound[y] is the maximum x in row y that's been eaten. When processing 'L' from x0:

if x0 <= left_bound[y], then no steps.

Else, the steps is x0 - left_bound[y], and the new left_bound[y] becomes x0.

So, in the example:

First action: row4, column3's cells are eaten. But that's a different row. So for row1, the left_bound is0.

Wait, no. The first action is (3,4) U. So, in column3, the cells from y=4 down to1 are eaten, including (3,1). So, in row1, x=3 is eaten. So the left_bound for row1 is3.

So, when processing the second action, which is 'L' from x=6 in row1:

current left_bound is3. x0=6>3. So steps=6-3=3. The new left_bound becomes6. So the path includes x=6,5,4 (3 steps). So the count is3, which matches the sample output.

Yes! So the formula is:

For 'L' direction:

steps = x0 - left_bound[y]

For 'U' direction:

steps = y0 - down_bound[x]

where down_bound[x] is the minimum y in column x that's been eaten (since the path is moving up, which is decreasing y).

Wait, no. For 'U' direction, in a column x, the down_bound[x] would represent the lowest y in column x that has been eaten. Because when you process 'U' from (x, y), you eat all cells from y down to down_bound[x] +1. Or perhaps the down_bound[x] is the highest y in column x that has been eaten.

Wait, let's think:

For column x, down_bound[x] is the maximum y in column x that's been eaten. Because when you process 'U' from (x, y), you eat all cells from y down to1. But if there's a previous 'U' action in the same column, which started from a higher y, then the down_bound[x] is that higher y.

For example, if you process 'U' from (x,5), then down_bound[x] becomes5. Later processing 'U' from (x,3) would have steps=3 -5. But since 3<5, steps are zero.

So, for 'U' direction:

steps = max(0, y0 - down_bound[x])

But since down_bound[x] is the maximum y in column x that's been processed. If down_bound[x] is 0 initially (no processing), then steps is y0.

So, the steps for 'U' direction is max(0, y0 - current_down_bound).

So, to model this, for each row and column, we need to track:

- For row y, left_bound[y] = the maximum x eaten in this row (initially 0).

- For column x, up_bound[x] = the maximum y eaten in this column (initially 0).

Wait, but for 'U' direction, the maximum y is the lowest possible. For example, processing 'U' from (x,5) eats cells from y=5 down to1. So, the up_bound[x] would be5. Any subsequent 'U' in column x would have to start at y <5, which is already processed, so steps are0.

So, for each column x, up_bound[x] is the maximum y (highest row) that has been processed in 'U' direction.

So, for 'U' action in (x, y), if y > up_bound[x], then steps is y - up_bound[x], and up_bound[x] is updated to y. Else, steps are0.

Similarly, for 'L' action in (x, y), if x > left_bound[y], steps is x - left_bound[y], and left_bound[y] is updated to x. Else, steps are0.

So, the steps are:

For action (x, y, dir):

- Check if the cell (x, y) has been processed before (in any direction). If yes, output0.

Else:

- For dir == 'L':

   if x > left_bound[y]:

      steps =x - left_bound[y]

      update left_bound[y] to x

      output steps

   else:

      output0

- For dir == 'U':

   if y > up_bound[x]:

      steps =y - up_bound[x]

      update up_bound[x] to y

      output steps

   else:

      output0

But wait, the cell (x, y) is part of the anti-diagonal. But when you process 'L' or 'U' direction, the cell (x, y) is eaten as part of the action. So, the cell (x, y) is now marked as processed. Any subsequent action on this cell will have 0 steps.

So, the model should be:

For each action:

1. Check if the cell (x, y) has been processed (in any direction). If yes, output0.

2. Else:

   a. For 'L' direction:

      - Check if x > left_bound[y]. If yes, steps is x - left_bound[y], update left_bound[y] to x.

      - Else, steps is0.

   b. For 'U' direction:

      - Check if y > up_bound[x]. If yes, steps is y - up_bound[x], update up_bound[x] to y.

      - Else, steps is0.

   c. Mark the cell (x, y) as processed.

   d. Output steps.

Wait, but this seems redundant. Because once the cell is marked as processed, any future action on it will output0. However, the steps for 'L' or 'U' could be0 even if the cell is not processed before.

For example, suppose in row y, left_bound[y] is5. An action 'L' is processed at x=3. Since x=3 <5, steps is0, and the cell (3,y) is marked as processed. So any future action on this cell, even if the direction is 'U', would output0.

So, the correct approach is:

For each cell (x, y) on the anti-diagonal:

- If the cell is processed (in any direction), output0.

Else:

   if direction is 'L':

      steps = max(0, x - left_bound[y])

      if steps >0:

         left_bound[y] = x

   elif direction is 'U':

      steps = max(0, y - up_bound[x])

      if steps >0:

         up_bound[x] = y

   mark the cell as processed.

   output steps.

So, the steps are computed even if the cell is processed. But the cell is only processed once, so any subsequent actions on it will output0.

Wait, but the cell is processed even if the steps are0. For example, in the case where the cell is processed in 'L' direction but x <= left_bound[y], steps are0, but the cell is marked as processed. So future actions on it will output0.

So, the cell is marked as processed regardless of the steps. So, once an action is performed on a cell, even if the steps are0 (because the direction's steps are0), the cell is marked as processed, and future actions on it will output0.

But how can that be? For example, in a cell (x,y) where x=2 and left_bound[y] is3. Processing 'L' direction here would yield steps of0 (2-3= -1, max0). So steps are0, but the cell is marked as processed. Any future action (even 'U') on this cell will output0. But 'U' might have steps.

But according to the problem statement, any action on a cell that has already been processed (i.e., the starting cell has been eaten) will have steps0. Because the starting cell is eaten.

So, once a cell is marked as processed (regardless of the direction), any action on that cell will have steps0. So, even if the 'U' direction would have steps, the starting cell is already eaten, so the path starts from an eaten cell and thus steps are0.

This is correct, because the starting cell is part of the path. So, if the starting cell is eaten, the path can't proceed.

Thus, the correct steps are:

For each action:

   if cell is already processed → output0.

   else:

      compute steps based on direction and current left_bound or up_bound.

      update left_bound or up_bound if steps >0.

      mark cell as processed.

      output steps.

So, the algorithm is:

1. Use a hash set to track processed cells (x coordinate, since y is determined by x).

2. For each action, check if x is in the processed set. If yes → output0.

3. Else, add x to processed set.

4. Compute steps based on direction and current left_bound or up_bound.

5. Update left_bound or up_bound if necessary.

6. Output steps.

Now, the question is, how to efficiently track left_bound and up_bound. Since n is up to 1e9 and q is up to 2e5, we can't store arrays for left_bound and up_bound. Instead, we can use dictionaries (hash maps) to track the left_bound and up_bound only for rows and columns that have been processed.

For example:

left_bound is a dictionary where the key is row y, and the value is the current left_bound for that row. Initially, all rows have left_bound 0.

But since the initial state is that all cells below the anti-diagonal are eaten, but those are not part of the anti-diagonal. So, the left_bound and up_bound start at0.

Wait, no. The initial state is that all cells below the anti-diagonal are eaten. But those cells are not part of the remaining triangular area. So, the left_bound and up_bound are for rows and columns in the remaining triangular area.

But for 'L' direction in row y, the left_bound[y] is initially 0. Because all cells in the row y are in the remaining area (since x + y <=n+1 → x <=n+1 -y). So the initial left_bound[y] is0.

Similarly, up_bound[x] is0 for all columns x, because initially, the cells in column x that are part of the remaining area are y >= (n+1 -x). But after processing 'U' from (x, y), the up_bound[x] is updated to y.

So, for the data structures:

- processed: a set of x's (since y is determined by x).

- left_bound: a dictionary mapping row y to current left_bound. Initially, left_bound[y] =0.

- up_bound: a dictionary mapping column x to current up_bound. Initially, up_bound[x] =0.

But since the number of queries is up to 2e5, the dictionaries will have at most O(q) entries. Because we only need to track rows and columns that have been processed.

For example, when processing 'L' direction for row y, if it's the first time, we set left_bound[y] to x. For subsequent 'L' directions in the same row, if x is greater than left_bound[y], we update it.

But since the cell can be processed only once (since processed is a set), each row and column will be processed once. Wait, no. Because each row has exactly one cell on the anti-diagonal. So each row can be processed once. Similarly for each column. So, the dictionaries left_bound and up_bound can have up to q entries each, but in practice, each row and column can be processed at most once.

So, for each action:

- Check if x is in the processed set. If yes, output0.

- Else, add x to processed.

- If direction is 'L':

   row y =n+1 -x (since x + y =n+1).

   current_lb = left_bound.get(y, 0)

   steps =x - current_lb

   if steps >0:

      left_bound[y] =x

   else:

      steps =0

   output steps.

- If direction is 'U':

   column x.

   current_ub = up_bound.get(x,0)

   steps =y - current_ub

   if steps >0:

      up_bound[x] =y

   else:

      steps =0

   output steps.

Wait, y is determined by x and n. Because x + y =n+1 → y =n+1 -x.

So, for direction 'L', the row is y =n+1 -x.

Yes.

Now, let's test this logic with the first sample input.

First sample input:

n=6, q=5.

Actions:

1. 3 4 U → x=3, y=4, direction U.

Process:

Check if x=3 is processed → no. Add to processed.

Direction is 'U', so column x=3.

current_ub = up_bound.get(3,0)=0.

steps=4-0=4. So output4.

up_bound[3] becomes4.

2. 6 1 L → x=6, y=1. Direction L.

Check x=6 → not processed. Add to processed.

Direction is 'L', row y=1.

current_lb = left_bound.get(1,0)=0.

steps=6-0=6. But in the sample output, it's3. So this is a problem.

Wait, why is the sample output 3 for this action?

Ah, because the first action processed column3, which updated up_bound[3] to4. But how does that affect the row1's left_bound?

It doesn't. The first action's 'U' direction processed column3, which includes cell (3,1) (since it's part of the column). So, the cell (3,1) is eaten as part of the first action. So, in row1, cell x=3 is now eaten. So the left_bound for row1 is3.

But according to the current logic, when processing the second action (x=6, direction L), the left_bound for row1 is0. Because the left_bound is tracked per row, and the first action's processing of column3 doesn't affect row1's left_bound. But in reality, the first action's 'U' direction in column3 caused cell (3,1) in row1 to be eaten, which should update the left_bound for row1.

Ah! So the previous logic is incorrect. The 'U' direction in column x affects the row y=1 (for x=3), because cell (3,1) is in row1. So, eating cell (3,1) in row1 would update the left_bound for row1 to3.

But according to the current model, this is not tracked. Because 'U' direction only updates the up_bound for column x, which tracks the maximum y processed in that column. But 'U' direction also eats cells in row y=1 for x=3, which should affect the left_bound of row y=1.

This is a big problem. Because the initial model does not account for the fact that processing a 'U' direction in column x eats cells in multiple rows, which affects the left_bound for those rows.

Similarly, processing 'L' direction in a row y eats cells in multiple columns, which affects the up_bound for those columns.

This complicates the model significantly.

Thus, the previous approach is incorrect. Because 'U' direction in column x affects the left_bound of the rows in the same column. For example, processing 'U' from (3,4) in column3, which eats cells (3,4), (3,3), (3,2), (3,1). This affects the left_bound for rows 4,3,2,1. For row1, the left_bound should be updated to3, since x=3 is eaten.

But how can we model this? Because for each 'U' action in column x, you eat cells from y down to1, which are in different rows. Each of those cells is in a row y', and each such row's left_bound may need to be updated to x.

But this is not feasible with the current model, as it would require O(y) operations per 'U' action, which is impossible for large y (like 1e9).

Thus, the previous approach is invalid. We need a new model.

Alternative approach:

Each 'U' action in column x eats all cells (x, y) where y' ranges from y downto 1. So for each such row y', the cell (x, y') is eaten. Thus, in each row y', the left_bound[y'] should be at least x. So, for row y', left_bound[y'] = max(left_bound[y'], x).

But how to track this efficiently?

For example, if a 'U' action is processed in column x with y=4, then for rows4,3,2,1, their left_bound is set to max(left_bound[row], x). So, if x is larger than the current left_bound for these rows, the left_bound is updated.

Similarly, a 'L' action in row y and x=6 would update the up_bound for columns6,5,4,3,2,1 in row y to max(up_bound[column], y).

But this is not feasible for large y or x.

Thus, this approach is not computationally feasible.

Therefore, we need a different approach that can model the interactions between 'U' and 'L' actions.

Let's rethink the problem.

Each 'U' action from (x, y) eats all cells in column x from y down to 1. These cells are in rows y, y-1, ..., 1. For each of these rows, the left_bound for that row is the maximum x' such that all cells x <=x' are eaten. So, if a cell in row y' has x <=x, then left_bound[y'] must be at least x.

But how can we track this? Because for each 'U' action, the left_bound for all rows y' <=y in the same column x is possibly increased to x. But with y being up to 1e9, this is impossible.

Similarly, a 'L' action from (x, y) eats all cells in row y from x down to 1. These cells are in columns x, x-1, ...,1. For each of these columns, the up_bound for that column is the maximum y' such that all cells in column x' >=y' are eaten. So, for each column x' in the row y, up_bound[x'] is max(up_bound[x'], y).

But again, this is impossible for large x.

Thus, the previous approach is incorrect. We need a way to model these interactions.

Alternative idea: The steps for a 'U' action in column x, y is the number of cells in the column x from y down to the current up_bound[x]+1. But in addition, for each of these rows y', the left_bound[y'] is updated to be max(left_bound[y'], x). But this is not feasible for large y.

Thus, we need a way to represent ranges where left_bound is at least x for certain rows.

Similarly for 'L' actions.

But given the time constraints, perhaps the problem requires a different approach.

Let's think of the problem in terms of the anti-diagonal. Each action is on the anti-diagonal. The action's direction is either up or left.

For 'U' action in cell (x, y):

- Eats all cells in column x from y down to 1. So, the up_bound[x] is max(up_bound[x], y).

- For each of these rows y' (from y downto 1), the left_bound[y'] is max(left_bound[y'], x). Because these cells (x, y') are now eaten, and in their rows, the left_bound is at least x.

But how to manage this efficiently.

The key insight is that after a 'U' action in column x, any 'L' action in a row y' <=y will have their left_bound[y'] at least x. So, if a row y' has left_bound[y'] >=x, then any 'L' action in that row with x0 <=x will have steps x0 - left_bound[y'] <=0, so steps 0.

Thus, the 'U' action in column x affects the left_bound of multiple rows.

But this is not manageable for large x and y.

Alternative approach:

The maximum left_bound for a row y' is the maximum x among all columns x' where the 'U' action in x' covers y', plus any 'L' actions in row y'.

Similarly, the maximum up_bound for a column x' is the maximum y among all rows y' where the 'L' action in y' covers x', plus any 'U' actions in column x'.

But how to model this.

This seems like a problem that can be modeled with interval trees or segment trees, but for 1e9 ranges, this is impossible.

Alternative idea: The 'U' action in column x will cause all rows y' <=y in column x to have left_bound[y'] >=x. So, for any 'L' action in a row y', if there's a 'U' action in column x >=x' (x' is the x of the 'L' action), then the left_bound for row y' is at least x. So, the maximum x from 'U' actions affecting this row y' is the maximum x such that there's a 'U' action in column x where y >=y'.

But how to track this.

This is getting too complicated. Perhaps there's a smarter way.

Let me think differently. The 'U' action in (x, y) (y =n+1 -x) will eat the entire column x from y down to 1. This will set the left_bound for all rows y' in 1..y to be at least x.

Similarly, a 'L' action in (x, y) will eat the entire row y from x down to 1. This will set the up_bound for all columns x' in 1..x to be at least y.

But how to model this efficiently.

For example, the left_bound for a row y' is the maximum x among all 'U' actions that cover y' and any 'L' actions in row y'.

But how to compute this maximum x.

Similarly, the up_bound for a column x' is the maximum y among all 'L' actions that cover x' and any 'U' actions in column x'.

But how to track these maxima.

This seems like a problem where we need two separate data structures:

1. For 'U' actions, track the maximum x for each row y'.

2. For 'L' actions, track the maximum x for each row y'.

But this is again not feasible for large n.

Alternative approach:

We can note that 'U' actions in column x with y' =n+1 -x are processed. Each 'U' action in column x has y =n+1 -x. When processed, it affects all rows y' from 1 to y (n+1 -x). So, for each row y', the maximum x from 'U' actions is the maximum x such that n+1 -x >= y' → x <= n+1 -y'. So, x is in 1..n+1 -y'.

The maximum x among all 'U' actions where x <=n+1 -y' is the maximum x in the 'U' actions for x <=n+1 -y'.

Similarly, for 'L' actions in row y, x is in 1..y' (since y =n+1 -x → x =n+1 -y). For 'L' actions in row y, the maximum x is the maximum x in the 'L' actions for row y.

But this is not helpful for querying.

Another idea: For 'U' actions, the maximum x that affects row y' is the maximum x among all 'U' actions where x <=n+1 -y'.

For example, if row y'=3 (n=6), then x <=n+1 -y' =7-3=4. So, the maximum x from 'U' actions where x <=4 is the maximum x in 'U' actions with x <=4.

This can be tracked with a data structure that allows querying the maximum x in a range [1, x_max].

Similarly, for 'L' actions in row y', the maximum x is the maximum x in 'L' actions for that row.

So, the steps for an action (x0, y0, dir) are:

If the cell is already processed → 0.

Else:

For 'L' direction:

   max_u = maximum x in 'U' actions where x <=n+1 -y0.

   max_l = maximum x in 'L' actions for row y0.

   steps =x0 - max(max_u, max_l).

   if steps >0:

      add to 'L' actions for row y0.

   output steps.

For 'U' direction:

   max_l = maximum y in 'L' actions where y <=n+1 -x0.

   max_u = maximum y in 'U' actions for column x0.

   steps =y0 - max(max_l, max_u).

   if steps >0:

      add to 'U' actions for column x0.

   output steps.

But how to track the maximum x in 'U' actions where x <=k.

This sounds like a problem that can be addressed with a segment tree or a binary indexed tree (Fenwick tree) that can track the maximum in a range.

But given that n can be up to 1e9, a segment tree is not feasible. However, since the number of 'U' actions is up to q, we can use a sorted list to track the x's of 'U' actions and use binary search to find the maximum x <=k.

Similarly for 'L' actions.

So, for 'U' actions:

We maintain a sorted list of x's where 'U' actions have been performed. For each query on max x <=k, we can binary search this list.

For 'L' actions:

We maintain a dictionary where for each row y, we track the maximum x. For rows not in the dictionary, the maximum x is0.

Additionally, the 'U' actions contribute to the max x for rows y' in their range (1..y).

But how to track the max x from 'U' actions for a row y'.

Wait, for a row y', the maximum x from 'U' actions is the maximum x in 'U' actions where x <=n+1 -y'.

So, this is the maximum x in the 'U' actions list that is <= (n+1 -y').

Similarly, for 'L' action in row y', the maximum x is the current max in the 'L' dictionary for row y' (if any).

Thus, for 'L' direction action (x0, y0):

max_u = the maximum x in 'U' actions list <= (n+1 -y0).

max_l = the 'L' dictionary.get(y0, 0).

steps =x0 - max(max_u, max_l).

If steps >0, then we add this x0 to the 'L' dictionary for y0.

But how to efficiently find max_u.

The 'U' actions are stored in a sorted list. For example, if the list is sorted in ascending order, we can binary search for the largest x <=k (n+1 -y0).

Thus, for each 'L' action, we perform a binary search on the sorted list of 'U' x's.

This is possible with O(q) space for the 'U' list and O(log q) time per query.

Similarly, for 'U' actions:

For a 'U' action in column x0, y0 =n+1 -x0.

The steps are y0 - max(max_l, max_u), where:

max_l = maximum y in 'L' actions where y <=n+1 -x0.

max_u = maximum y in 'U' actions for column x0.

But for 'L' actions, the maximum y for column x0 is the maximum y in 'L' actions where the row y' has x >=x0. Hmm, this is getting complicated.

Alternatively, for 'U' action in column x0, the steps are:

max_l is the maximum y in 'L' actions where the 'L' action's x >=x0. Because when 'L' action is in row y' with x >=x0, that action's row y' has y' =n+1 -x. So, the 'L' action's x >=x0 → y' =n+1 -x <=n+1 -x0 =y0.

Thus, for 'U' action in column x0, the steps are:

max_u = current up_bound for column x0 (max y from previous 'U' actions).

max_l = maximum y' from 'L' actions where x >=x0. This y' =n+1 -x. So, for 'L' actions with x >=x0, y' <=y0.

The steps are y0 - max(max_u, max_l).

But how to compute max_l.

The 'L' actions are stored in a dictionary with row y' and x. For a 'U' action in x0, y0 =n+1 -x0.

The 'L' actions that have x >=x0 are those where y' =n+1 -x <=y0.

We need to find the maximum y' among all 'L' actions where x >=x0 → y' <=y0, and y' =n+1 -x.

The maximum y' would be the maximum such y' that has an 'L' action with x >=x0.

But how to track this.

Alternatively, for 'L' actions, we can track the x values in a sorted list, and for each x in 'L' actions, the corresponding y' is n+1 -x.

To find the maximum y' for 'L' actions with x >=x0, we need to find the minimum x in 'L' actions that is >=x0. Then, the corresponding y' is n+1 -x. The maximum y' would be n+1 -x_min.

But this is not correct. Because for x >=x0, y' =n+1 -x <=y0. The maximum y' would be the maximum of all y' =n+1 -x where x >=x0. Which is the same as the minimum x in the 'L' actions that is >=x0. Because the smallest x would have the largest y'.

So, to find the maximum y' for 'L' actions with x >=x0, we need to find the minimum x in 'L' actions' x list that is >=x0. Then, the corresponding y' is n+1 -x_min. If x_min exists, then y' is n+1 -x_min. Otherwise, no such 'L' action exists.

Thus, the maximum y' from 'L' actions is max(y_L_max, n+1 -x_min), where y_L_max is the maximum y from 'L' actions where x >=x0.

Wait, this seems a bit complicated. Let's think of it this way:

The 'L' actions are stored as a sorted list of x's. For 'U' action in x0, we need to find the minimum x in the 'L' list that is >=x0. Because this x has the smallest possible x >=x0, which gives the largest possible y' =n+1 -x.

Thus, the maximum y' from 'L' actions is n+1 -x_min.

But we can also have other 'L' actions with x >=x0, but their y' would be <=n+1 -x_min.

Thus, the maximum y' is n+1 -x_min.

So, the steps for 'U' action in x0 are:

max_u = up_dict.get(x0, 0).

max_l =0.

x_min = find the minimum x in 'L' list >=x0.

if x_min exists:

   max_l =n+1 -x_min.

steps =y0 - max(max_u, max_l).

if steps >0:

   up_dict[x0] =y0.

output steps.

But again, how to track the 'L' actions' x's in a sorted list.

Thus, the algorithm would be:

For each action:

1. Check if the cell is already processed. If yes, output0.

2. Add the cell to processed.

3. If direction is 'L':

   a. Compute y0 =n+1 -x.

   b. Find the maximum x_u from 'U' actions where x_u <= (n+1 -y0) = x (since y0 =n+1 -x → x= n+1 -y0).

      This is the maximum x_u in 'U' list <=x.

   c. max_l = the maximum x_l for 'L' actions in row y0.

      This is stored in the 'L' dictionary for row y0.

   d. steps =x - max(x_u, max_l).

   e. If steps >0:

      update 'L' dictionary for row y0 to x.

      add x to the 'L' sorted list.

   f. output steps.

4. If direction is 'U':

   a. y0 =n+1 -x.

   b. Find the minimum x_l in 'L' list >=x.

      If x_l exists, then max_l_y =n+1 -x_l.

      Else, max_l_y =0.

   c. max_u = up_dict.get(x, 0).

   d. steps =y0 - max(max_l_y, max_u).

   e. If steps>0:

      update up_dict[x] =y0.

      add x to 'U' sorted list.

   f. output steps.

This seems manageable. Now, the data structures needed are:

- processed: a set to track processed cells (x coordinates).

- 'U' list: a sorted list of x's where 'U' actions were performed.

- 'L' list: a sorted list of x's where 'L' actions were performed.

- 'L' dict: a dictionary mapping row y to the maximum x processed in 'L' actions.

- 'U' dict: a dictionary mapping column x to the maximum y processed in 'U' actions.

But for each 'U' action, the x is added to the 'U' list, and for each 'L' action, x is added to the 'L' list. These lists are sorted and allow binary search.

Additionally, for 'L' actions, each x is added to the 'L' list and the 'L' dict for row y0 is updated.

Now, let's test this with the first sample input.

First sample input:

n=6, q=5.

Action 1: 3 4 U.

processed is empty. x=3 not processed. add to processed.

direction 'U':

y0 =6+1 -3 =4.

Find the minimum x_l in 'L' list >=3. 'L' list is empty. So max_l_y=0.

max_u =up_dict.get(3,0) →0.

steps=4- max(0,0) =4.

update up_dict[3]=4.

add 3 to 'U' list → 'U' list is [3].

output4.

Action 2:6 1 L.

x=6 not processed. add to processed.

direction 'L':

y0=6+1 -6 =1.

Find maximum x_u in 'U' list <=6. 'U' list is [3]. max x_u=3.

max_l = 'L' dict for y=1 is 0.

steps=6 - max(3,0) =3.

update 'L' dict for y=1 to6.

add6 to 'L' list → 'L' list is [6].

output3.

This matches the sample.

Third action:2 5 L.

x=2 not processed. add.

direction 'L':

y0=6+1 -2=5.

x_u is max in 'U' list <=2. 'U' list has3. 3>2 → no x_u. So x_u is 0.

max_l for y=5 is0.

steps=2-0=2.

update 'L' dict for y=5 to2.

add2 to 'L' list. 'L' list is [6,2] but needs to be sorted. Wait, the 'L' list needs to be sorted in ascending order for binary search. So inserting 2 into [6] would require maintaining the list sorted. So, for 'L' list, we need to keep it sorted.

So, after adding 6 and 2, the 'L' list becomes [2,6].

Fourth action:1 6 U.

x=1. add to processed.

direction 'U':

y0=6+1-1=6.

find min x_l in 'L' list >=1. 'L' list is [2,6]. min x_l >=1 is2.

max_l_y=6+1 -2=5.

max_u =up_dict.get(1,0)=0.

steps=6 - max(5,0) =1.

update up_dict[1]=6.

add1 to 'U' list → sorted as [1,3].

output1.

Fifth action:4 3 U.

x=4. add to processed.

direction 'U':

y0=6+1-4=3.

find min x_l in 'L' list >=4. 'L' list is [2,6]. min x_l >=4 is6.

max_l_y=6+1 -6=1.

max_u = up_dict.get(4,0)=0.

steps=3 - max(1,0) =2.

update up_dict[4]=3.

add4 to 'U' list → sorted as [1,3,4].

output2.

Which matches the sample.

This model works for the first sample. Now, check the second sample input.

Second sample input:

n=10, q=6.

Actions:

1. 2 9 U →x=2, y=9. 'U' direction.

2. 10 1 U →x=10, y=1.

3. 1 10 U →x=1, y=10.

4. 8 3 L →x=8, y=3.

5. 10 1 L →x=10, y=1.

6.6 5 U →x=6, y=5.

Output:9,1,10,6,0,2.

Let's process the first action:

x=2, direction U.

y0=10+1 -2=9.

Check if x=2 is processed → no.

Add to processed.

Find min x_l in 'L' list (empty) → none.

max_l_y=0.

max_u =0.

steps=9-0=9.

Add x=2 to 'U' list. up_dict[2]=9.

Output9.

Second action:10 1 U.

x=10. Add to processed.

y0=10+1 -10=1.

Find min x_l in 'L' list (empty) → none. max_l_y=0.

max_u=0.

steps=1-0=1.

Add x=10 to 'U' list. up_dict[10]=1.

Output1.

Third action:1 10 U.

x=1. Add to processed.

y0=11 -1=10.

Find min x_l in 'L' list (empty) → none.

max_l_y=0.

max_u=0.

steps=10-0=10.

Add x=1 to 'U' list. up_dict[1]=10.

Output10.

Fourth action:8 3 L.

x=8. Add to processed.

y0=11-8=3.

Find max x_u in 'U' list <=8. 'U' list has [1,2,10]. sorted as [1,2,10]. Find x_u<=8 → 2 is the largest.

max_l in 'L' dict for y=3: 0.

steps=8-2=6.

Add to 'L' dict y=3 →8. Add x=8 to 'L' list (sorted).

Output6.

Fifth action:10 1 L.

x=10. Check if processed → yes (processed in action2). output0.

Sixth action:6 5 U.

x=6. Add to processed.

y0=11-6=5.

Find min x_l in 'L' list (contains 8). x_l>=6 is8.

max_l_y=11-8=3.

max_u=0 (no 'U' in x=6 before).

steps=5-3=2.

Add x=6 to 'U' list. up_dict[6]=5.

Output2.

Which matches the sample.

Thus, this model works.

Now, the data structures needed are:

- processed: a set.

- 'U' list: sorted list of x's where 'U' actions were performed.

- 'L' list: sorted list of x's where 'L' actions were performed.

- 'L' dict: dictionary mapping y to max x.

- 'U' dict: dictionary mapping x to max y.

To perform the binary searches:

For 'L' actions:

- For the 'U' list, find the largest x <= current x (which is n+1 -y0 =x0).

For 'U' actions:

- For the 'L' list, find the smallest x >= current x0.

Implementing this in Python:

For sorted lists, we can use the bisect module.

For 'U' list:

- To find the largest x <=k, use bisect_right to find the insertion point and get the element before.

For 'L' list:

- To find the smallest x >=k, use bisect_left to find the insertion point and get the element at that index.

Now, implementing this:

The code steps are:

Read n and q.

Initialize:

processed = set()

u_list = sorted list (initially empty).

l_list = sorted list (initially empty).

l_dict = dict()

u_dict = dict()

For each query:

x, y, dir = input.

But according to the input format, the third part is direction (U or L).

Wait, the input lines are "xi and yi (1 ≤ xi, yi ≤ n, xi + yi = n + 1) — the numbers of the column and row of the chosen cell and the character that represents the direction (L — left, U — up)."

So, for each query, the line is xi, yi, dir.

But since xi + yi =n+1, we can compute y =n+1 -xi to verify.

But the code can use xi and dir.

So, for each query:

x = xi

y = yi

But we can verify x + y ==n+1, but per problem statement, the inputs are valid.

Now, code:

import bisect

n, q = map(int, input().split())

processed = set()

u_list = []  # sorted list of x's for 'U' actions

l_list = []  # sorted list of x's for 'L' actions

l_dict = dict()  # maps row y to max x

u_dict = dict()  # maps column x to max y

for _ in range(q):

    x, y, dir = input().split()

    x = int(x)

    y = int(y)

    dir = dir.strip()

    if x in processed:

        print(0)

        continue

    processed.add(x)

    if dir == 'L':

        # Compute y0 =n+1 -x

        y0 = n + 1 - x

        # Find the maximum x_u in u_list <=x

        max_u = 0

        idx = bisect.bisect_right(u_list, x) -1

        if idx >=0:

            max_u = u_list[idx]

        # max_l in l_dict.get(y0, 0)

        max_l = l_dict.get(y0, 0)

        steps = x - max(max_u, max_l)

        if steps >0:

            l_dict[y0] = x

            # Insert x into l_list in sorted order

            bisect.insort(l_list, x)

        print(steps)

    else: # 'U'

        # y0 =n+1 -x

        y0 = n +1 -x

        # Find the minimum x_l in l_list >=x

        max_l_y =0

        idx = bisect.bisect_left(l_list, x)

        if idx < len(l_list):

            x_l = l_list[idx]

            max_l_y = (n+1) - x_l

        # max_u in u_dict.get(x,0)

        max_u = u_dict.get(x,0)

        steps = y0 - max(max_l_y, max_u)

        if steps >0:

            u_dict[x] = y0

            bisect.insort(u_list, x)

        print(steps)

This should work.

Testing with sample inputs:

Sample input 1:

6 5

3 4 U

6 1 L

2 5 L

1 6 U

4 3 U

The code should process as follows:

Action 1: dir U.

y0=7-3=4.

l_list is empty, so idx=0 in bisect_left. len(l_list) is0 → no x_l.

max_l_y=0.

max_u=0.

steps=4-0=4.

Add x=3 to u_list.

Output4.

Action2: x=6, dir L.

y0=7-6=1.

max_u is largest x in u_list <=6. u_list is [3]. idx=1-1=0. max_u=3.

max_l = l_dict.get(1,0)=0.

steps=6-3=3.

Add to l_dict[1]=6. Insert 6 into l_list → [6].

Output3.

Action3: x=2, dir L.

y0=7-2=5.

max_u is largest x in u_list <=2. u_list [3]. bisect_right(u_list,2) is0. idx=-1 → no max_u.

max_u=0.

max_l = l_dict.get(5,0)=0.

steps=2-0=2.

Add l_dict[5]=2. Insert 2 into l_list → [2,6].

Output2.

Action4: x=1, dir U.

y0=7-1=6.

Check l_list for x >=1. l_list [2,6]. bisect_left(l_list,1) is0. x_l=2.

max_l_y=7-2=5.

max_u= u_dict.get(1,0)=0.

steps=6-5=1.

Add to u_dict[1]=6. Insert 1 into u_list → [1,3].

Output1.

Action5: x=4, dir U.

y0=7-4=3.

Check l_list for x >=4. l_list [2,6]. bisect_left returns 1. x_l=6.

max_l_y=7-6=1.

max_u=0.

steps=3-1=2.

Add to u_dict[4]=3. Insert4 into u_list → [1,3,4].

Output2.

Which matches the sample.

Thus, the code is correct.
</think>

```python
import bisect

n, q = map(int, input().split())

processed = set()
u_list = []
l_list = []
l_dict = dict()
u_dict = dict()

for _ in range(q):
    x, y, direction = input().split()
    x = int(x)
    y = int(y)
    if x in processed:
        print(0)
        continue
    processed.add(x)
    if direction == 'L':
        y0 = n + 1 - x
        max_u = 0
        idx = bisect.bisect_right(u_list, x) - 1
        if idx >= 0:
            max_u = u_list[idx]
        max_l = l_dict.get(y0, 0)
        steps = x - max(max_u, max_l)
        if steps > 0:
            l_dict[y0] = x
            bisect.insort(l_list, x)
        print(steps)
    else:
        y0 = n + 1 - x
        max_l_y = 0
        idx = bisect.bisect_left(l_list, x)
        if idx < len(l_list):
            x_l = l_list[idx]
            max_l_y = (n + 1) - x_l
        max_u = u_dict.get(x, 0)
        steps = y0 - max(max_l_y, max_u)
        if steps > 0:
            u_dict[x] = y0
            bisect.insort(u_list, x)
        print(steps)
```