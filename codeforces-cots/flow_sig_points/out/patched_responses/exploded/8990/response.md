<think>
Okay, let's try to understand this problem. The mouse wants to go from the top-left corner (northwest) to the bottom-right corner (southeast) of a grid. She can only move right or down. The goal is to find out how many berries ('*') she will eat based on her strategy, which is to maximize the berries. But wait, the problem says she might make suboptimal decisions, but the output is the number she ends up eating. Hmm, maybe the problem is that she makes a greedy choice each step, but that doesn't necessarily lead to the maximum possible. So we need to simulate her path based on her choices, not just compute the maximum possible path.

Wait, the problem statement says that she tries to choose her path to maximize the berries, but because of her haste and hunger, she might make suboptimal decisions. So the output is the actual number of berries she eats, which might not be the optimal path. Wait, that's confusing. Wait, the problem is not asking for the maximum possible berries. Instead, perhaps the mouse's strategy is to choose each step greedily (like, choose the next step that gives the immediate best option, without considering the whole path). So for each step, she picks east or south based on which direction has more berries in the immediate next cell. But if there's a tie, then maybe she chooses either, but that could lead to different paths. So our task is to simulate the path she takes based on this greedy approach, and count the berries along that path.

Wait, the problem statement isn't exactly clear on what the mouse's strategy is. Let's read the problem again.

The problem says: "The mouse tries to choose her path so as to maximize the number of berries consumed. However, her haste and hunger might be clouding her judgement, leading her to suboptimal decisions..."

Hmm. So she is trying to choose the optimal path, but maybe she's making mistakes. But the way the problem is phrased, perhaps the actual path she takes is the one where at each step she chooses the direction (east or south) that gives the maximum possible berries in the next step, but not considering the entire path. So it's a greedy approach, not a dynamic programming one.

In other words, the mouse's path is determined by greedily choosing the next step (right or down) that has a higher berry count. If both steps (right and down) have the same number of berries, she chooses one, but the problem might not specify which. However, the sample inputs and outputs must have a unique correct answer, so perhaps there's a way the path is determined when there's a tie.

Wait, but in the first sample input:

4 3
*..
.*.
..*
...

The output is 3. Let's see. The grid is:

Row 0: * . .
Row 1: . * .
Row 2: . . *
Row 3: . . .

So the starting cell is (0,0) which is a berry, count 1. Then she can go right to (0,1) (.) or down to (1,0) (.). Both are '.' so maybe she chooses one. But how does that lead to a path with 3 berries?

Wait the sample output is 3. Let's see possible paths.

The optimal path would be 0,0 → 0,1 → 1,1 → 1,2 → 2,2 → 3,2. Wait that's not possible. Alternatively, maybe the mouse's path is such that she takes the direction that gives the maximum possible berries in the next step. Wait, perhaps the path is determined by at each step, if moving east (right) or south (down) leads to a cell that has more berries in the path. But that's not straightforward.

Alternatively, perhaps the mouse's path is the one where at each decision point (when there's a choice between right and down), she chooses the direction that leads to the maximum possible berries in that next step, but without considering the entire path. For example, if moving right leads to a cell with a berry, and moving down leads to a cell without, she will move right. If both have berries, she picks either, but the problem's sample suggests that the path is uniquely determined. Therefore, perhaps the mouse's strategy is to prefer east (right) when there's a tie. Or maybe prefer south (down). How to know?

Alternatively, maybe the mouse's strategy is to choose the direction that has the highest sum of berries in all cells that would be passed through if she continues in that direction. But that's complicated.

Wait, the problem statement says that she will only go east or south until she reaches the southeast corner. So the path is a sequence of right and down moves. The key is to determine, for each cell, which direction the mouse will take, and then follow that path to count the berries.

The problem is to model the mouse's path selection, which is supposed to maximize the number of berries she eats, but perhaps she's not doing it optimally due to haste. So this suggests that the mouse's path is not the optimal path, but some other path. But the problem statement is unclear. Wait, no: the problem says she tries to choose the path to maximize the berries, but her haste leads to suboptimal decisions. So the actual path she takes may not be the optimal one. But how to model her decision-making?

Alternatively, perhaps the mouse's path is the optimal one. But the problem's sample outputs seem to suggest that the answer is not the maximum possible. Let's check the first sample:

Sample input 1:

4 rows, 3 columns.

Row 0: * . .
Row 1: . * .
Row 2: . . *
Row 3: . . .

The optimal path would collect all the berries. Let's see. The possible paths from (0,0) to (3,2) (since H is 4 and W is 3, the bottom right is (3,2)).

The path must go down 3 times and right 2 times. The number of steps is 3+2 = 5 steps (since starting at (0,0), you need to go 3 downs and 2 rights to reach (3,2)).

So possible paths:

For example, path down, down, down, right, right. Let's see:

0,0 (berry 1) → 1,0 (no) → 2,0 (no) → 3,0 (no) → 3,1 → 3,2. Berries collected: 1.

Another path: right, right, down, down, down. That would collect the berries in (0,0), (0,1) (no), (0,2) (no?), then down steps. So no, this path may have only 1.

Wait sample input 1's output is 3. So the optimal path must collect 3 berries. Let's see:

Looking for a path that passes through (0,0) (1), (1,1) (2), (2,2) (3), and then to (3,2). How can that path be formed?

For example: down, right, down, right, down.

Wait, let's count the steps:

Start at (0,0) → down to (1,0) (no berry). Then right to (1,1) (berry). Then down to (2,1) (no). Then right to (2,2) (berry). Then down to (3,2) (no). So total is 3 berries. That matches the sample output.

So why does the mouse take this path? Because she's making choices based on immediate gains. But how?

Alternatively, maybe the mouse's decision is based on the current cell's berries. Wait, perhaps at each step, she can choose to go right or down (if possible). She chooses the direction that leads to the cell with a berry. If both are berries, choose either. But how does that path accumulate to 3 in sample 1.

Alternatively, perhaps the mouse's decision is based on the sum of berries along all possible paths starting with that direction. But that's the same as the optimal path. So maybe that's not the case.

Alternatively, the problem might have a mistake in the description, and the actual problem is to find the maximum possible berries the mouse can collect, but the sample outputs suggest otherwise. For example, sample input 1's maximum possible path is 3, which is the output. So perhaps the problem is to compute the maximum possible berries, not considering the mouse's possible suboptimal decisions. But why does the problem mention that she may choose suboptimal paths?

Wait, looking back at the problem statement:

"The mouse tries to choose her path so as to maximize the number of berries consumed. However, her haste and hunger might be clouding her judgement, leading her to suboptimal decisions..."

This is confusing. So perhaps the problem is to compute the maximum possible berries she can collect, but due to her haste, she might not take the optimal path. But the sample outputs don't support that. For example, in the first sample, the output is 3, which seems like the maximum possible. Let's see if there is a path that collects more than 3 berries.

In the first sample's grid, possible path:

Right, down, right, down, down.

0,0 (1) → right to 0,1 (no) → down to 1,1 (1) → right to 1,2 (no) → down to 2,2 (1) → down to 3,2 (no). Total 3.

Another path: down, right, right, down, down.

0,0 → down (1,0) (no), right (1,1) (1), right (1,2) (no), down (2,2) (1), down (3,2). Total 3.

Another possible path: down, down, right, right, down.

0,0 → down to 1,0 → down to 2,0 → right to 2,1 (no), right to 2,2 (1), down to 3,2. Total 2.

So the maximum possible is 3, which is what the sample output shows. So perhaps the problem is indeed to compute the maximum possible berries. Then why the mention of suboptimal decisions? Maybe it's a red herring, and the problem is just to compute the maximum path.

But in that case, the problem statement's first paragraph is misleading. Let's check the second sample:

Sample input 2:

4 4
.*..
*...
...*
..*.

The output is 2. Let's see.

The grid is:

Row 0: . * . .
Row 1: * . . .
Row 2: . . . *
Row 3: . . * .

The maximum path would have 2 berries. Let's see possible paths.

For example, perhaps the path must take steps that collect two berries. Let's see:

Start at (0,0) (no berry). Then, possible directions: right (0,1) is *, or down (1,0) is *. So the optimal path would take one of these. Let's say right:

0,0 → 0,1 (1) → then possible directions right (0,2) . or down (1,1) . So either way, the next steps are not berries. So the total so far is 1. Then maybe down to (1,1) (.), right to (0,2) (.), etc. Not sure. The output is 2, so there's a path that gets 2 berries.

Wait, the sample output is 2. How? Let's think of another path. Maybe start with down (1,0) which is * → then maybe right to (1,1) (.), then down to (2,1) (.), then right to (2,2) (.), then down to (3,2) (*) → total 2. So that's two berries. So that's the maximum. So the answer is 2.

So the problem is to find the maximum possible berries along any path from top-left to bottom-right, moving only right or down. Then the initial confusion in the problem statement is perhaps a mistake. The mouse's strategy is to choose the optimal path, but the problem says that she may not. But the sample outputs indicate that the correct answer is the maximum possible. So perhaps the problem is simply to compute the maximum number of berries along such a path.

Therefore, the solution is to model this as a dynamic programming problem, where for each cell (i,j), we compute the maximum number of berries collected to reach (i,j), and then the value at (H-1, W-1) is the answer.

Yes, that makes sense. So the approach is to use DP.

The steps are:

- Create a DP table where dp[i][j] is the maximum berries collected to reach cell (i,j).

- The base case is dp[0][0] = 1 if the cell has a berry, else 0.

- For each cell (i,j), dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + (1 if current cell has a berry, else 0).

- Since the movement is only right or down, each cell (i,j) can be reached from (i-1,j) (up) or (i,j-1) (left).

- We need to process the cells in such an order that when computing dp[i][j], the cells (i-1,j) and (i,j-1) have already been computed.

- The order could be row-wise, left to right, and for each row, process from top to bottom. Or in a way that processes each cell after its top and left neighbors.

But with H and W up to 5, the maximum grid is 5x5, which is very small. So even a BFS approach would work.

But the DP approach is straightforward and efficient for this problem.

So the code would:

- Read H and W.

- Read H lines, each line is a string of W characters.

- Create a DP table of size H x W.

- Initialize dp[0][0] as 1 if grid[0][0] is '*', else 0.

- For each cell (i,j), starting from (0,0), iterate through each cell in row-major order (or in a way that ensures that the top and left cells are processed before current cell).

- For each cell (i,j), compute the maximum of the top cell (if exists) and left cell (if exists), then add the current cell's value (1 if '*', else 0).

- The answer is the value in dp[H-1][W-1].

Wait, but the problem's sample input 3:

3 4

..**

*...

....

Output is 1.

Let's compute the DP for this case.

The grid is:

Row 0: . . * * → cells (0,0) '.', (0,1) '.', (0,2) '*', (0,3) '*'

Row 1: * . . . 

Row 2: . . . .

So starting at (0,0): 0 berries.

For cell (0,0), dp[0][0] = 0.

Then for (0,1), can only come from left (0,0) which is 0. So dp[0][1] = 0 + (0 if '.', else 1) → 0.

For (0,2), comes from left (0,1) → 0 + 1 → 1.

For (0,3), comes from left (0,2) → 1 + 1 → 2.

Now row 1:

(1,0): can come from above (0,0) → 0 + 1 (since grid[1][0] is '*' → dp[1][0] = 1.

(1,1): can come from above (0,1) 0 or left (1,0) 1. So max is 1. Current cell is '.' → 0. dp[1][1] = 1 + 0 =1.

(1,2): can come from left (1,1) 1 or above (0,2) 1. Max is 1. Current cell is '.' → 0. dp[1][2] = 1.

(1,3): comes from left (1,2) 1 or above (0,3) 2. Max is 2. current cell is '.' → 2+0=2. So dp[1][3] is 2.

Row 2:

(2,0): comes from above (1,0) 1. current cell '.' → 1 + 0 =1.

(2,1): comes from above (1,1) 1 or left (2,0) 1. max is 1. current cell '.' → 1.

(2,2): comes from above (1,2) 1 or left (2,1) 1. max 1. current cell '.' → 1.

(2,3): comes from above (1,3) 2 or left (2,2) 1. max 2. current cell '.' → 2.

So the final dp[2][3] is 2. But the sample output is 1.

Wait, this contradicts the sample input 3. So this suggests that the DP approach is not correct, which implies that the problem is not about finding the maximum path but something else.

Wait sample input 3's output is 1. So according to the sample, the correct answer is 1. But according to the DP approach, it's 2. So there's a problem here.

Hmm, this is a critical point. Let's re-examine sample input 3.

Sample input 3:

3 4

..**

*...

....

The grid:

Row 0: ..** → (0,0) is '.', (0,1) is '.', (0,2) is '*', (0,3) is '*'

Row 1: *... → (1,0) is '*', (1,1) is '.', etc.

Row 2: .... → all '.'.

The output is 1.

So according to the sample, the maximum path is 1. But according to the DP approach, the path would be:

0,0 → 0,1 → 0,2 → 0,3 → 1,3 → 2,3. But that's impossible because from 0,3, the next steps can be down. Let's see the movement possibilities.

Wait, to go from 0,3 to 1,3, that's a down move. Then from 1,3 to 2,3. So the path would have (0,3) (value 1), (1,3) (value '.'), (2,3) ('.'), but how does the DP approach get 2?

Wait the DP approach would track the maximum berries along any path to (i,j). So for cell (0,3), the path comes from (0,2), which is a '*', so dp[0][3] is 2 (two stars). Then, when moving down to (1,3), the maximum is the max of (0,3) (2) and (1,2) (1) → 2. So dp[1][3] is 2 + 0 (since it's a '.'), so 2. Then moving to (2,3), the max is from (1,3) (2) and (2,2) (1) → 2. So dp[2][3] is 2 + 0 = 2. But the sample output is 1.

This suggests that the problem is not to find the maximum path. So what's wrong here?

Alternatively, perhaps the problem statement's description is correct, and the mouse is taking a path that is not the maximum. So the problem is to simulate the path the mouse takes based on a certain decision-making process, not the maximum possible.

This is a key point. So why does the sample input 3's output differ from the maximum path's sum?

In sample input 3, according to the DP approach, the maximum is 2. But the sample output is 1. Therefore, the problem is not to compute the maximum path. So the initial understanding was wrong.

Therefore, the problem is to model the mouse's path selection according to her decision-making process, which may not be optimal.

So the question is: how does the mouse choose between moving east or south at each step?

The problem statement says that she tries to maximize the number of berries, but her haste leads to suboptimal choices. So perhaps she makes a greedy choice at each step, looking at the next possible steps, but not the entire path.

For example, at each step, she can choose to move east or south (if available), and she picks the direction that gives the higher immediate gain. If the next cell in one direction has a berry, and the other doesn't, she chooses the berry. If both are the same, she chooses one (maybe east first, or south first?).

But how to model this choice.

Let's think of the sample input 3.

In the sample input 3, the mouse starts at (0,0) ('.', no berry). Then she can move east to (0,1) ('.') or south to (1,0) ('*'). Since south has a berry, she would choose to move south. Then at (1,0), she can move east to (1,1) ('.') or south to (2,0) ('.'). Both are '.', so perhaps she chooses east. Then, moving east to (1,1), then she can go east to (1,2) ('.') or south to (2,1) ('.'). Again, same. She may choose east. Then (1,2) → east to (1,3) ('.'), or south to (2,2) ('.'). Then (1,3) → east is not possible (since W=4, j=3 is the last column), so she has to move down to (2,3). So the path is (0,0) → (1,0) → (1,1) → (1,2) → (1,3) → (2,3). The berries collected are (1,0) has one, and the others have none. So total is 1. Which matches the sample output.

So the problem is to model the path that the mouse takes, which is determined by making greedy choices at each step. So when at a cell (i,j), she can choose to move east or south. She chooses the direction (if possible) that leads to a cell with a berry. If both are berries, she chooses one (perhaps east first). If neither is a berry, she chooses either. So the path is built step by step based on the immediate next cell.

But how to handle when moving east or south leads to a cell with a berry. For example, if moving east leads to a cell with a berry, and moving south leads to a cell with a berry, which direction does the mouse take?

The problem's sample input 1 has a path that collects 3 berries, which implies that she chooses directions that lead to the maximum possible in each step.

Alternatively, perhaps the mouse's decision is to choose the direction that leads to the cell with the maximum possible berries in the entire path. But that's not possible unless she can look ahead, which would make it the optimal path again.

But according to sample input 3, the maximum path is 2, but the mouse's path yields 1, which is not optimal. So the problem is to model the path where the mouse makes choices based on the current possible moves' immediate next cell.

So the approach is to simulate the path step by step, choosing at each step east or south based on the next cell's berry count. Here's how:

At each step (current cell (i,j)), the mouse can move east (to (i, j+1)) or south (to (i+1, j)), provided these are within the grid.

If east and south are both possible (i.e., not at the bottom row and rightmost column), then she compares the next cells.

She prefers to move in the direction where the next cell has a berry. If only one direction has a berry in the next cell, she takes that. If both have a berry, she chooses one (but which one? The problem samples must have a unique correct answer, so perhaps she prefers east (right) in case of a tie). If neither has a berry, she may choose either direction.

But the sample input 3's path requires that she moves south first. Let's see:

In sample input 3:

Starting at (0,0), can move east (0,1) which is '.' or south (1,0) which is '*'. She chooses south (since next cell has a berry). Then at (1,0), can move east to (1,1) ('.') or south to (2,0) ('.'). Both are '.'; she chooses east (assuming she prefers east when there's a tie in the next cells' berries). Then (1,1) can move east to (1,2) ('.') or south to (2,1) ('.'). Again, both are '.'; choose east. Then (1,2) can move east to (1,3) ('.') or south to (2,2) ('.'). East again. Then (1,3) can only move south to (2,3) ('.'). So berries collected: (1,0) is 1. The other cells are '.'. So total is 1. Which matches the sample.

So the decision is made by checking the next cell in each possible direction. She chooses the direction where the next cell has a berry. If both have berries, she chooses east. If neither has a berry, she chooses east (right) first. Or maybe the other way around. But how to determine the tie-breaker.

But how to model the tie-breaker when both directions have berries. For example, if both east and south next cells have berries, which direction does she choose?

In the first sample input, let's see:

The path taken is the one where she moves down, right, down, right, down. So let's see why.

At (0,0) (berry), she can move east to (0,1) ('.') or south to (1,0) ('.'). Both are '.', so she chooses east? But the path in sample 1's explanation has her moving down first. Wait that can't be. Wait sample input 1's path is:

0,0 → down to (1,0) (no), then right to (1,1) (yes), then down to (2,1) (no), then right to (2,2) (yes), then down to (3,2) (no). So total 3.

But according to the decision logic, when at (0,0), the next steps are (0,1) and (1,0), which are both '.', so she chooses east. But in the sample's path, she goes down first. This suggests that in the case of a tie (both next cells are '.'), she prefers south (down) instead of east.

Wait, that's confusing. How to resolve this.

Alternatively, perhaps the tie-breaker is to prefer east (right) when possible. Let's see.

In sample input 1:

At (0,0), after moving east to (0,1), which is '.', then she can move east again (0,2) which is '.' or down to (1,1). But in the path that gets 3 berries, she must have moved down from (0,0) to (1,0), then right to (1,1), etc. So that suggests that when there is a tie (both next cells are '.'), she moves down.

Hmm. But how to model this.

Alternatively, perhaps the mouse always moves as far east as possible, then south. Or vice versa. But that's not indicated by the problem statement.

This is a problem. Because the way the mouse chooses between directions when there's a tie (both next cells are '.' or both are '*').

The problem statement says that she will only go east or south. So the path is determined by a series of choices between east and south. But the problem is to model her decision-making process.

The key here is to find out the rules that the mouse uses to choose between east and south when both options are available.

The sample input 3 shows that when the mouse has a choice between east ('.') and south ('*'), she chooses south. Because in sample input 3, moving south from (0,0) leads to a berry.

In sample input 1, after the initial move, the path goes down first. But in that case, the next cells (0,1) and (1,0) are both '.'.

So why does she choose down in that case?

This suggests that in the case of a tie (both next cells are '.'), she chooses south.

But how to confirm this.

Alternatively, perhaps the mouse's choice is based on which path allows her to collect more berries, but she can only look ahead one step. For example, at each step, she looks at all possible paths that start with east or south, but only one step ahead, and chooses the direction that gives the maximum berries in the next step.

Wait, but in the case of a tie (both next steps have a '.', or both have a '*'), she has to choose one.

If the next cells are both '.', she chooses east. Or south.

To resolve this, perhaps the problem uses the following rules for the mouse's decision:

At each step, she can choose to move east or south (if possible). She will prefer east if the next cell in the east direction has more berries than the south, or if they are equal. Or perhaps she prefers south when the next cells are equal.

But this is unclear.

Alternatively, perhaps the problem assumes that the mouse uses a priority of directions. For example, she always prefers east over south, unless moving south leads to a berry and east doesn't.

Let's look at sample input 1:

After (0,0), she can move east to (0,1) (.) or south to (1,0) (.). Both are '.', so she chooses east. But according to the sample's path, she must have moved south. So this contradicts.

Alternatively, perhaps the problem is that the mouse's decision is to prefer south when possible. For example, when both directions are possible and the next cells are equal, she moves south.

But sample input 3's initial step, the mouse moves south, which is the correct choice (since south's next cell is a berry).

So perhaps the decision rule is:

At each step, the mouse can move east or south (if possible). She looks at the next possible cells in east and south directions. She will choose the direction that leads to a cell with a berry. If both have a berry, she chooses south. If neither has a berry, she chooses south.

Alternatively, perhaps the tie-breaker is to choose south (down) when both next cells are equal.

But how to confirm this.

Alternatively, perhaps the mouse's decision is based on the sum of berries along all possible cells she can reach via each direction, but limited to the current row and column. For example, moving east allows her to collect all berries in the current row to the east, and moving south allows her to collect all berries in the current column to the south. But this is speculative.

This is a critical point. Without knowing the exact decision rules of the mouse, it's impossible to model the correct path.

Given that the problem's samples have unique outputs, the decision rules must be well-defined. So we need to deduce the rules from the samples.

Let's take sample input 3 and see why the path leads to 1 berry.

The mouse starts at (0,0), which is '.'.

She has two options:

- East (0,1): '.'.
- South (1,0): '*'.

She chooses the direction with a berry. So she moves south to (1,0), which has a berry. Count is 1.

At (1,0), options are east (1,1) '.' and south (2,0) '.'.

Both are '.', so she has to choose between them. The sample's path leads her east (1,1), then east to (1,2), then east to (1,3), then south to (2,3).

So in this case, after (1,0), she chooses east. So in case of a tie (both next cells are '.'), she chooses east.

In sample input 1, after (0,0) (which is a berry), she moves south to (1,0), which is '.'.

But in that case, the next options are east (0,1) and south (1,0) is the current cell. Wait, perhaps I'm getting the steps wrong.

Sample input 1's grid is 4 rows, 3 columns:

Rows:

0: * . .
1: . * .
2: . . *
3: . . .

So the path taken is:

0,0 → 1,0 → 1,1 → 2,1 → 2,2 → 3,2.

But (3,2) is the destination.

So from (0,0) (berry), the next step is down to (1,0) ('.'). So why did she move down here? Because at (0,0), she had to choose between east (0,1) (.) and south (1,0) (.). Both are '.', so she chooses south.

But according to sample input 3's decision, when next cells are equal, she chooses east. But in sample input 1, she chooses south. So this contradicts.

Hmm. This is a problem. The decision rule isn't clear.

Alternatively, perhaps when the current cell is (i,j), she will prefer to move east (right) if possible, unless moving south (down) leads to a cell with more berries.

But how.

Alternatively, perhaps the mouse uses the following priority:

At each step, she considers the next possible directions (east and south), and for each direction, she looks at the cell in that direction. She prefers the direction where the cell has a berry. If both directions have berries, she chooses east. If neither, she chooses east.

Wait, in sample input 3's first step, she chooses south because it has a berry, and east does not. So that's correct.

In sample input 1's first step, the mouse is at (0,0), which is a berry. Next cells are east (0,1) . and south (1,0) . So both are '.', so she chooses east. But according to the sample's path, she moves south. This is conflicting.

Alternatively, perhaps when both directions are possible and have the same value, the mouse prefers south.

In sample input 1, after (0,0) she chooses south. Which would explain why she moves down. But why? Because in case of a tie in the next cells (both '.'), she prefers south.

So the decision rule could be:

At each step, the mouse evaluates the next cell in east and south directions.

If one direction's next cell is '*' and the other is '.', she chooses the direction with '*'.

If both are '*' or both are '.', she prefers south over east.

But in sample input 3's second step, after (1,0), both next cells are '.', so she chooses east. According to this rule, she would choose south, but in the sample, she chooses east. So that's a contradiction.

Alternatively, maybe she prefers east in case of a tie.

But then in sample input 1's first step, she would choose east, but the sample's path requires her to move south.

So this is very confusing.

Perhaps the problem's actual rule is that when both directions are possible, she prefers east (right) first. Only if the east direction is not possible (e.g., at the right edge) does she move south.

But let's see.

Sample input 3's first step: she has east and south available. South's next cell is a berry, so she chooses south. Correct.

At (1,0), she can move east or south. Both are '.', so she chooses east. So the path is east, east, east, then south.

Which matches the sample.

Sample input 1's initial steps:

At (0,0), she can choose east or south. Both next cells are '.', so she chooses east. Then east is not possible (after (0,0) to east (0,1), then what next steps? Let's see.

Wait, if she moves east from (0,0) to (0,1), then next steps can be east to (0,2) or south to (1,1). (0,2) is '.' and (1,1) is '*'. So she would choose south to (1,1). Then, from (1,1), she can move east to (1,2) (.) or south to (2,1) (.). Both are '.', so she chooses east. Then, from (1,2) she can move east to (1,3) (.) or south to (2,2) ('*'), so she chooses south. Then from (2,2), she can move east to (2,3) (but W=3, so j=2 is the maximum) or south to (3,2) ('.'). So she moves south. So the path would be:

0,0 → 0,1 → 1,1 → 1,2 → 2,2 → 3,2. Berries collected: (0,0) is 1, (1,1) is 1, (2,2) is 1. Total 3, which matches the sample output. So the path is possible.

So according to this decision rule, when both directions are possible and next cells are '.', she chooses east first.

So the rules are:

At each step, the mouse can move east or south. She prefers to move east if possible, but:

- She will choose the direction (east or south) that leads to a cell with a berry. If both have berries, choose east.

- If neither has a berry, choose east.

Wait, but in the case where both next cells are '.', she moves east. But in sample input 3's second step, after (1,0) (the cell with '*'), the next cells are (1,1) '.' and (2,0) '.'. She chooses east (right), which is allowed.

So according to this rule, the decision is to choose east first if possible.

But how to model this decision-making process.

The code needs to simulate the mouse's path step by step, choosing at each step whether to move east or south based on the next cells' berries and the tie-breaker.

So the approach is:

1. Start at (0,0).

2. At each step, check possible directions (east and south).

3. For each possible direction, check if the next cell is within the grid.

4. Among the valid directions, compare the next cells' berries.

5. Prefer the direction with more berries. If equal, choose east.

6. Move to the chosen direction.

7. Repeat until reaching (H-1, W-1).

So for each cell (i,j), the mouse will check east (i,j+1) and south (i+1,j).

If both are possible:

- If one is '*' and the other is '.', choose the one with '*'.

- If both are '*' or both are '.', choose east.

If only one direction is possible, take that.

So the code needs to simulate this process.

So the algorithm is:

Initialize current position (i,j) = (0,0). Count berries in current cell.

While not at (H-1, W-1):

- Check possible directions east and south.

- For each direction, check if it's within the grid.

- Collect the valid directions.

- For each valid direction, note if the next cell has a berry.

- Choose the direction with the highest priority:

   - Directions with a berry are preferred over those without.

   - Among directions with the same berry status, east is preferred.

- Move to the chosen direction.

- Add the berry count of the new cell.

So the code will have to track the current position, and for each step decide which direction to take based on the next cells' berries.

Let's test this logic against the samples.

Sample input 3:

Path:

0,0 (.) → south (1,0) ('*') → count 1.

At (1,0):

Possible directions: east (1,1) '.', south (2,0) '.'.

Both are '.', so choose east.

Move to (1,1), count remains 1.

At (1,1):

Possible directions: east (1,2) '.', south (2,1) '.'.

Choose east.

Move to (1,2), count remains 1.

At (1,2):

Possible directions: east (1,3) '.', south (2,2) '.'.

Choose east.

Move to (1,3), count remains 1.

At (1,3):

Only possible direction is south to (2,3). Move there, which is '.'.

So total berries is 1. Which matches the sample.

Sample input 1:

Path:

0,0 ('*') → count 1.

Possible directions: east (0,1) '.', south (1,0) '.'.

Both are '.', so choose east.

Wait no. According to the rules:

At (0,0), east and south are possible. Next cells are '.' and '.'.

So the mouse chooses east. So she moves to (0,1). But (0,1) is '.'.

Then next step: from (0,1), can move east to (0,2) '.' or south to (1,1) '*'. South's next cell is '*', so choose south. Move to (1,1) → count increases by 1 (now 2).

From (1,1), can move east to (1,2) '.' or south to (2,1) '.'.

Both are '.', choose east. Move to (1,2) '.' → count remains 2.

From (1,2), can move east to (1,3) (but W=3, so j+1 is 3 which is beyond the width). So east is not possible. Only possible direction is south to (2,2) '*'. Move there → count increases by 1 (now 3).

From (2,2), can move east to (2,3) (but W=3) → not possible. So move south to (3,2). Count remains 3.

So total is 3, which matches the sample.

But according to this path, the mouse moves east from (0,0) to (0,1), but the sample's path was supposed to be down first. This suggests a contradiction.

Wait, sample input 1's output is 3, but according to this simulation, the path is:

(0,0) → (0,1) → (1,1) → (1,2) → (2,2) → (3,2). Berries in (0,0), (1,1), (2,2) → 3.

Which matches the sample's output. But according to the initial analysis, the sample's path was thought to be different. So why is this possible?

Because there are multiple paths that collect 3 berries. The mouse's choice in each step leads to one of them, but the code's simulation must capture that.

So the code's logic for choosing directions based on the next cell's berries and tie-breakers is correct.

Another example: sample input 4:

5 5

..*..

.....
**...
**...
**...

The output is 1.

Let's see:

The mouse starts at (0,0) '.', which is no berry. So initial count 0.

Possible directions: east (0,1) '.' and south (1,0) '*'. South has a berry, so move south to (1,0) (count 1).

From (1,0) (which is '*'), possible directions: east (1,1) '.' or south (2,0) '*'.

South has a berry, so move south to (2,0) (count 2).

From (2,0) ('*'), possible directions east (2,1) '.' or south (3,0) '*'. Choose south → (3,0), count 3.

From (3,0) ('*'), possible directions east (3,1) '.' or south (4,0) '*'. Choose south → (4,0), count 4.

From (4,0) ('*'), can move east (4,1) '.' or south (but it's the last row). So east is possible. Next cell (4,1) '.' → choose south is not possible, so east. But east's next cell is '.'.

But wait, after (4,0), she can move east. But east is (4,1), which is '.'.

But she is at (4,0) which is the last row. So she must move east until she reaches (4,4).

But according to the sample output, the answer is 1. So perhaps the initial analysis is wrong.

Wait sample input 4's output is 1. Let's see:

The grid is:

Row 0: . . * . .
Row 1: . . . . .
Row 2: * * . . .
Row 3: * * . . .
Row 4: * * . . .

The mouse starts at (0,0) '.', count 0.

She can move east (0,1) '.' or south (1,0) '.'.

Both next cells are '.'.

According to the tie-breaker, she chooses east. So she moves east to (0,1), count remains 0.

From (0,1), she can move east to (0,2) '*' (which is a berry) or south to (1,1) '.'.

So the next cell in east is '*', which is better. So she moves east to (0,2), count 1.

From (0,2) (berry), she can move east to (0,3) '.' or south to (1,2) '.'.

Both are '.'; choose east. Move to (0,3), count 1.

From (0,3), can move east to (0,4) '.' or south to (1,3) '.'.

Choose east. Move to (0,4), count 1.

From (0,4), must move south to (1,4), then continue moving south until (4,4).

But along this path, the only berry is at (0,2). So the total is 1, which matches the sample output.

But why didn't she choose south from (0,0) to (1,0) (which is '.', but then maybe move further south to (2,0) which is a '*'?

Ah, because according to the decision rules, at (0,0), she can move east or south. Both next cells are '.' so she chooses east. Then from (0,1), east to (0,2) (berry), and so on. So the path collects 1 berry.

But according to the grid, there's a path that collects more. For example, if she moves south from (0,0) to (1,0) ('.'), then south to (2,0) ('*'), then south to (3,0) ('*'), then south to (4,0) ('*'), then east to (4,1) ('*'), etc. But that path would collect 4 berries.

But according to the decision rules, at (0,0), she moves east because both next cells are '.' and she chooses east. So she never takes the path south.

So the sample input 4's output is 1, which is because the mouse's decision-making process leads her to the path with 1 berry, even though there exists a path with more.

This confirms that the problem is to simulate the mouse's path based on her decision rules, which prioritize the next cell's berry status and prefer east in case of a tie.

Therefore, the code must simulate the mouse's path according to the following rules:

At each step:

1. Check possible directions (east and south).

2. For each direction, if the next cell is within the grid, note whether it has a berry.

3. Among the possible directions:

   a. Prefer directions that lead to a berry.

   b. If there's a tie (both or neither have berries), choose east.

4. Move to the chosen direction.

5. Repeat until the bottom-right cell is reached.

So the code will:

- Initialize current position (i,j) as (0,0).

- Initialize the count as 1 if (0,0) is a berry, else 0.

- While (i,j) is not (H-1, W-1):

   - Determine possible next directions: east (i, j+1) and south (i+1, j).

   - Check which directions are valid (within grid).

   - For valid directions, check if their next cell has a berry.

   - Among valid directions, select the one with the highest priority:

      - Directions that lead to a berry are preferred over those that don't.

      - Among directions with the same berry status, east is preferred.

   - Move to the chosen direction.

   - Add 1 to count if the new cell has a berry.

So the code needs to implement this logic.

Now, the code steps:

Read H and W.

Read H lines, each as a string. So the grid is a list of lists, grid[i][j] is the cell at row i, column j.

current_i = 0, current_j = 0.

count = 1 if grid[0][0] is '*' else 0.

while current_i != H-1 or current_j != W-1:

   possible directions: east (current_i, current_j+1) and south (current_i+1, current_j).

   valid_directions = list of directions that are within the grid.

   berries_east = False

   berries_south = False

   east_possible = False

   south_possible = False

   for each direction in east and south:

      check if it's within the grid.

   east_valid = (current_j + 1 < W) → yes, east is possible.

   south_valid = (current_i + 1 < H) → yes, south is possible.

   if east is valid:

      east_has_berry = grid[current_i][current_j+1] == '*'

   else:

      east_has_berry = False

   if south is valid:

      south_has_berry = grid[current_i+1][current_j] == '*'

   else:

      south_has_berry = False

   # collect valid directions

   valid = []

   if east_valid:

      valid.append( ('east', east_has_berry) )

   if south_valid:

      valid.append( ('south', south_has_berry) )

   # select the best direction.

   # sort the valid directions: first those with berry, then east.

   # create a list of tuples, where each tuple is (has_berry, is_east, direction)

   # then choose the one with highest priority.

   # priority: has_berry (True > False), then is_east (True > False).

   candidates = []

   for direction in valid:

      dir_name, has_berry = direction

      is_east = (dir_name == 'east')

      candidates.append( (-has_berry, not is_east, dir_name) )

   # sort the candidates. The smallest tuple will be chosen (since for has_berry=True, the first element is -1; for False, 0).

   # so sorting in ascending order will put higher priority first.

   candidates.sort()

   chosen_dir = candidates[0][2]

   # move to the chosen direction.

   if chosen_dir == 'east':

      current_j +=1

   else:

      current_i +=1

   # add to count if new cell has berry.

   if grid[current_i][current_j] == '*':

      count +=1

return count.

So this code will correctly simulate the mouse's path based on the decision rules.

Now, let's test this code against the sample inputs.

Sample input 1:

4 3

*..

.*.

..*

...

The grid is:

Row 0: * . .

Row 1: . * .

Row 2: . . *

Row 3: . . .

The path is:

(0,0) → east (0,1) (.) → south (1,1) (*) → east (1,2) (.) → south (2,2) (*) → south (3,2) (.) → count is 3.

But according to the code's simulation:

Initial position (0,0) → count 1.

At (0,0):

Possible directions: east (0,1) '.', south (1,0) '.'.

Both are valid. East_has_berry: (0,1) is '.', south_has_berry: (1,0) is '.'.

So valid directions are east and south, both with no berry.

Candidates are:

For east: (False, False, 'east') → tuple is (0, False, 'east').

For south: (False, True, 'south') → tuple is (0, True, 'south').

When sorted, (0, False) comes before (0, True). So the code will choose east.

So current_j becomes 0+1=1. Check (0,1) is '.', no count change.

Now, current_i=0, current_j=1.

Possible directions: east (0,2) '.', south (1,1) '*'.

east_has_berry: (0,2) is '.', south_has_berry: (1,1) is '*'.

Valid directions: east and south.

For east: no berry. South: has berry.

So the code will choose south.

 current_i becomes 1, current_j remains 1. Check (1,1) is '*', count becomes 2.

Then, current_i=1, current_j=1.

Possible directions: east (1,2) '.', south (2,1) '.'.

Both are valid. Both have no berries.

Candidates: east and south.

Sorting, east comes first.

 current_j becomes 2. Check (1,2) is '.', count remains 2.

Now, current_i=1, current_j=2.

Possible directions: east (1,3) which is out of bounds (W=3), so invalid. South (2,2) '*' → valid.

So direction is south. current_i becomes 2, current_j=2.

Check (2,2) is '*', count becomes 3.

Next, current_i=2, current_j=2.

Possible directions: east (2,3) invalid. South (3,2) '.'.

So direction is south. current_i becomes 3, current_j=2. Check '.' → count remains 3.

Now, current_i=3, current_j=2 → which is the destination. Loop ends.

So total count is 3 → correct.

Sample input 3:

3 4

..**

*...

....

The code simulation:

current_i=0, current_j=0 → '.' → count 0.

Possible directions: east (0,1) '.', south (1,0) '*' → south has berry.

So choose south. current_i becomes 1, current_j=0. Check '*', count becomes 1.

Now, current_i=1, current_j=0.

Possible directions: east (1,1) '.', south (2,0) '.'.

Both are valid, no berries.

Candidates: east and south.

Sorting, east comes first. Move east to (1,1). Check '.', count remains 1.

current_i=1, current_j=1.

Possible directions: east (1,2) '.', south (2,1) '.'.

Move east → (1,2) → '.'.

current_i=1, current_j=2.

Possible directions: east (1,3) '.', south (2,2) '.'.

Move east → (1,3) → '.'.

current_i=1, current_j=3.

Possible directions: east invalid. south (2,3) '.'.

Move south → (2,3) → '.' → count remains 1.

So total is 1 → correct.

Sample input 4:

5 5

..*..

.....
**...
**...
**...

Grid:

Row 0: . . * . .

Row 1: . . . . .

Row 2: * * . . .

Row 3: * * . . .

Row 4: * * . . .

Simulation:

current_i=0, current_j=0 → '.' → count 0.

Possible directions: east (0,1) '.', south (1,0) '.'.

Both are '.' → choose east.

current_j=1 → '.'.

Possible directions: east (0,2) '*' → has berry. south (1,1) '.'.

Choose east (0,2) → count becomes 1.

current_i=0, j=2 → '*' (already counted).

Possible directions: east (0,3) '.', south (1,2) '.'.

Choose east.

current_j=3 → '.'.

Possible directions: east (0,4) '.', south (1,3) '.'.

Choose east → j=4 → '.'.

Now, at (0,4). Must move south until (4,4).

No more berries. So count remains 1.

Thus, the code returns 1 → correct.

So this code should correctly handle all the samples.

The code will read the grid, then simulate the path step by step, following the decision rules.

Now, to implement this in Python.

The code steps:

Read H, W.

Read H lines, each line is a string.

Convert the grid into a list of lists.

Initialize current_i and current_j as 0.

Compute initial count.

Loop until current is the bottom-right cell.

For each step:

Check possible directions east and south.

Check if each is valid.

Check their berry status.

Collect valid directions.

Sort the directions based on priority.

Choose the first direction.

Move, and update count.

Finally, print the count.

Now, the code:

Read H and W.

Then H lines.

current_i, current_j = 0, 0.

count = 1 if grid[0][0] == '*' else 0.

while not (current_i == H-1 and current_j == W-1):

   # get possible directions.

   east_valid = current_j + 1 < W

   south_valid = current_i + 1 < H

   east_has_berry = False

   south_has_berry = False

   if east_valid:

       east_has_berry = grid[current_i][current_j + 1] == '*'

   if south_valid:

       south_has_berry = grid[current_i + 1][current_j] == '*'

   # collect valid directions.

   valid_directions = []

   if east_valid:

       valid_directions.append(('east', east_has_berry))

   if south_valid:

       valid_directions.append(('south', south_has_berry))

   # Sort the directions based on priority.

   # Create a list of tuples where each tuple is (-has_berry, is_south, direction).

   # Because we want to sort by highest priority: first by has_berry (True comes first, which is -True=-1 < -False=0), then is_south (False is east, which comes first).

   # So for each direction:

   # priority key is (-has_berry, is_south)

   candidates = []

   for direction, has_berry in valid_directions:

       is_east = (direction == 'east')

       # When sorted in ascending order, the tuple with lower value comes first.

       # For has_berry True: -1, else 0.

       # is_east is True → is_south is False → 0.

       # For east: is_south is False → 0.

       # For south: is_south is True → 1.

       key = (-has_berry, not is_east)  # not is_east is True for south.

       candidates.append( (key, direction) )

   # Sort the candidates. The smallest key comes first.

   candidates.sort()

   chosen_dir = candidates[0][1]

   # Move.

   if chosen_dir == 'east':

       current_j += 1

   else:

       current_i += 1

   # Update count.

   if grid[current_i][current_j] == '*':

       count += 1

print(count)

This should handle all cases correctly.

Testing against sample inputs 1, 2.

```python
def main(input_stream, output_stream):
    h, w = map(int, input_stream.readline().rstrip("\n").split())
    grid = [input_stream.readline().rstrip("\n").strip() for _ in range(h)]
    current_i, current_j = 0, 0
    count = 1 if grid[0][0] == '*' else 0

    while (current_i != h - 1) or (current_j != w - 1):
        east_valid = current_j + 1 < w
        south_valid = current_i + 1 < h
        east_berry = grid[current_i][current_j + 1] == '*' if east_valid else False
        south_berry = grid[current_i + 1][current_j] == '*' if south_valid else False

        valid = []
        if east_valid:
            valid.append(('east', east_berry))
        if south_valid:
            valid.append(('south', south_berry))

        candidates = []
        for direction, berry in valid:
            key = (-berry, direction != 'east')
            candidates.append((key, direction))
        candidates.sort()
        chosen = candidates[0][1]

        if chosen == 'east':
            current_j += 1
        else:
            current_i += 1

        if grid[current_i][current_j] == '*':
            count += 1

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 4
.*..
*...
...*
..*.
""",
            "output": \
"""\
2
""",
        }, 
        {
            "input": \
"""\
3 4
..**
*...
....
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

</think>

```python
h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]
current_i, current_j = 0, 0
count = 1 if grid[0][0] == '*' else 0

while (current_i != h - 1) or (current_j != w - 1):
    east_valid = current_j + 1 < w
    south_valid = current_i + 1 < h
    east_berry = grid[current_i][current_j + 1] == '*' if east_valid else False
    south_berry = grid[current_i + 1][current_j] == '*' if south_valid else False

    valid = []
    if east_valid:
        valid.append(('east', east_berry))
    if south_valid:
        valid.append(('south', south_berry))

    candidates = []
    for direction, berry in valid:
        key = (-berry, direction != 'east')
        candidates.append((key, direction))
    candidates.sort()
    chosen = candidates[0][1]

    if chosen == 'east':
        current_j += 1
    else:
        current_i += 1

    if grid[current_i][current_j] == '*':
        count += 1

print(count)
```
