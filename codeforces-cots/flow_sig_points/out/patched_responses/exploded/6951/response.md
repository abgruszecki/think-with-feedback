<think>
Okay, let's tackle this problem. Hmm. So the problem is about determining which player (A or B) will win a pawn chess game based on the initial board setup. Both players play optimally. Player A wants to get a white pawn to row 1, and Player B wants a black pawn to row 8. The key is to find out who can reach their goal first with optimal moves from both sides.

First, I need to understand the movement rules. Player A moves white pawns upward one step each turn, and Player B moves black pawns downward. But each move must go to an empty cell. Also, players take turns, with A going first. So the winner is the one whose pawn can reach their target row first, considering that the other player might block them.

Wait, the challenge is that when a pawn is moving towards their target, the opponent might block their path. For example, if a white pawn's path is blocked by a black pawn, then that path is invalid. Similarly, if a white pawn has a clear path but needs to take more steps than another possible path, but maybe the other path is blocked by black pawns.

So, the approach here is to find the minimal steps each player can take to get a pawn to their target row, considering that the other player can block them. But how?

Let's think for Player A. For each white pawn, we need to calculate the earliest step it can reach row 1. But during these steps, the path must be clear. Also, Player B will be moving their pawns, which could potentially block the path. But since both play optimally, Player B will try to block Player A's fastest path if possible.

Wait, but how do the movements of B's pawns affect A's path? For instance, a white pawn at (r, c) needs to move up (r-1) steps to reach row 1. But along the column c, there might be pawns blocking the way. So for each white pawn, the steps required would be the number of steps needed, considering the existing pawns in its column. But the other players' pawns can interfere by moving into the column.

Wait, but pawns can't jump over each other. So for a white pawn to reach row 1 in column c, all the cells from its current position up to row 1 must be empty of any pawns (both white and black) that are in the path. However, since pawns can move, the blocking might be possible.

Alternatively, perhaps the minimal steps for a white pawn to reach row 1 is determined by the number of white pawns in the same column above it. Because each white pawn moves up, but if there's another pawn in the way, that's a problem. Wait, but in the initial setup, pawns can be in any position except for the first row (no white) and last row (no black). So for a white pawn, the path upwards in its column might be blocked by other pawns (white or black) that are in the way.

Wait, but when the white pawn moves, the player can choose which pawn to move. So perhaps the minimal steps for a white pawn is determined by the number of empty cells in its column between it and row 1, but considering that any existing pawns (from either color) in that column would block its path.

Wait, but other pawns can move. So, for example, suppose a white pawn is at (4,5). The cells above it in column 5 are row 3, 2, 1. If those cells are empty, then the white pawn can move up each turn. But during those turns, Player B might move a black pawn into that column, but since they can only move downward, maybe that's not possible. Wait, no. Because B's pawns are moving down. So if there's a black pawn in a row below the white pawn's path, it's moving down, which could interfere.

Hmm, this is getting complicated. Let's think of each column as a possible path. For a white pawn in column c, the number of steps it needs to reach row 1 is equal to (current row - 1). But along the way, there might be other pawns in that column. For example, if there's a black pawn in row 2 of the same column, then the white pawn can't reach row 1 unless that black pawn is moved out of the way. But since B is moving their pawns down, that black pawn can't move up. So if there's a pawn in the path (regardless of color), the white pawn's path is blocked unless those pawns are in positions that can move out of the way.

Wait, but when Player B moves, they have to move a black pawn down. So, perhaps in the path of a white pawn, any black pawns that are in the same column but below the white pawn can't block the path, because they are moving down. But any black pawns above the white pawn in the same column would be in the path. Wait, no. Because if a white pawn is at (r, c), then to reach row 1, it needs to move up through r-1, r-2, ..., 1. Any pawn in any of those cells would block the path.

But during the time the white pawn is moving up, the other pawns (including black ones) can be moving. So the presence of other pawns can affect the minimal steps required.

Alternatively, perhaps the minimal steps for a white pawn to reach row 1 is the number of steps it needs to take, but each step can only be made if the cell above is empty. However, since other pawns (of either color) can be moving, but in their own directions, perhaps the only obstacles are the static pawns in the same column.

Wait, this is confusing. Let's take an example. Suppose a white pawn is at (4,5). The cells (3,5), (2,5), (1,5) must be empty for it to reach row 1 in 3 steps. If any of those cells have a pawn (black or white), then the white pawn can't proceed. But during the steps, maybe the black pawns in that column can move out of the way. For instance, if there's a black pawn at (3,5), but that's a black pawn. Since black pawns move down, that black pawn will be moving down each turn. So if the white pawn is at (4,5) and the black pawn is at (3,5), then in the first turn, Player A cannot move the white pawn up because the cell is occupied. But in the next turn, Player B could move the black pawn down to (4,5), which is the same as the white's position. That can't happen. Wait, no. Because when Player B moves, they can only move their pawns down. So that black pawn at (3,5) would move to (4,5) on B's first turn. But if Player A's white pawn is at (4,5), then after B moves, the black pawn would be at (4,5), which is occupied. So that would block the white pawn.

Hmm. So maybe the presence of any pawn in the same column above the white pawn (or in the path) will block it. But perhaps the minimal steps for a white pawn is the number of steps it needs to reach row 1, but any pawn (either color) in the path (cells (r-1, c), (r-2, c), ..., 1) will block it. Because those pawns can't be moved out of the way by either player's moves.

Wait, for example, if there's a white pawn at (4,5), and another white pawn at (3,5), then the first pawn can't move up until the pawn at (3,5) moves. But since that's a white pawn, Player A can choose to move that one up first. But since the problem requires that each player must move exactly one pawn on their turn, maybe the minimal steps can be found by considering the order in which the pawns are moved.

This seems complicated. Let's think of each column as a possible path for a white pawn. For each white pawn in a column c, the earliest possible step it can reach row 1 is determined by the number of pawns (white or black) that are in the cells between it and row 1. Because each such pawn would block the path, and since they can't be moved out of the way (assuming they are in the same column), then the steps required would be (current row - 1) plus the number of pawns blocking the path. Wait, that doesn't make sense. Let me think again.

Wait, if a white pawn is at row r, then to reach row 1, it needs to move up (r-1) times. But if there's another pawn (white or black) in the same column above it, say at row k where k < r, then the white pawn can't move up until that pawn is cleared. But how?

For example, if there's a white pawn at row 4 and another white pawn at row 3 in the same column. Then Player A can first move the upper pawn (row 3) up, which would take 2 steps (to row 1). Then the lower pawn can start moving. But that's perhaps a longer path than another column.

So perhaps the minimal steps for Player A is the minimal among all possible white pawns' earliest possible steps, considering the number of blocking pawns in their column.

Alternatively, perhaps the minimal steps for a white pawn is the number of empty cells above it in its column. Because each step requires moving into an empty cell. But any pawn in the way (above it) would block the path. So the steps required would be (r-1) minus the number of empty cells in the path? Or maybe the steps required are the current row minus the number of non-empty cells above it.

Wait, for example, a white pawn is at row 4. The cells above are rows 3, 2, 1. If all those are empty, then 3 steps. If row 3 has a pawn (any color), then the white pawn can't move up until that pawn moves. But if it's a black pawn in row 3, then when Player B moves, they can move that pawn down (so from row 3 to row 4). But the white pawn is in row 4. So after the black pawn moves down to row 4, the cell at row 3 is empty. So then the white pawn can move up. But in that case, the steps would be delayed by one step. Wait, let's think step by step.

Scenario:
White pawn at (4,5), black pawn at (3,5).

Player A's turn. They can't move the white pawn up because (3,5) is blocked. So Player A must move another white pawn if possible. But suppose there are no other white pawns (for this example). Then Player A can't move, but the problem states that it's guaranteed that there's always a move available. So in this case, maybe there's another white pawn elsewhere.

Alternatively, maybe in this scenario, the white pawn can't use this column. But the problem says that the players choose which pawn to move each turn. So in this case, maybe Player A can't move the white pawn up until the black pawn moves away.

But the black pawn is moving down. So during Player B's turn, they can choose to move that black pawn from (3,5) to (4,5). Now, the cell (3,5) is empty. Then during Player A's next turn, they can move the white pawn from (4,5) to (3,5). Then Player B moves again. So for each step of the white pawn, the presence of a black pawn in the path can be moved down, but that would require some turns.

Wait, in this scenario, the steps required for the white pawn would be more than (r-1). Let's see:

Initial positions:
White at (4,5), black at (3,5).

Player A's first turn: can't move the white pawn up. So they have to move another white pawn. But in this example, perhaps there's another white pawn elsewhere. But if that's the only white pawn, then the problem statement says that a move is always available. So maybe this scenario isn't possible? Or perhaps the player can't move that pawn, but must have another pawn to move.

Hmm, perhaps the problem's constraints ensure that each player always has a move. So in any case, the code can assume that each player can make a move.

But back to the example. Let's assume that there are no other white pawns. Then Player A can't move the white pawn in column 5. But the problem states that it's impossible. So the initial setup must have at least one move available. So perhaps in this scenario, there's another white pawn in a different column.

But for the sake of this example, perhaps the code doesn't need to handle such impossible cases, since the input is guaranteed to have valid moves.

So maybe the key is to find, for each white pawn, the minimal steps needed to reach row 1, considering that all the cells in their column above them are empty. Because if there are any pawns in the same column above, then those pawns would block the path. But the problem is that Player B can move their pawns in other columns to block.

Wait, but perhaps the minimal steps for a white pawn is simply the number of steps required if there are no obstacles in the path. But how do the obstacles affect this? Because during the movement steps, other pawns can move into the path.

Alternatively, perhaps the minimal steps for a white pawn is the current row minus 1 (since they need to move up r-1 times), but each time, the cell above must be empty. However, any pawn (either color) in that cell would block the path. So for each white pawn, the steps required is r-1, but only if all the cells from (r-1, c) up to (1, c) are empty. Otherwise, that pawn can't use that column.

But that's not necessarily true. For example, a white pawn at (5,c) with a black pawn at (4,c). Then the white pawn can't move up. But during Player B's turn, the black pawn can move down to (5,c), but that's the same position as the white pawn. Which is impossible. So the black pawn would have to move elsewhere. Wait, no. Player B can't move the black pawn into a cell occupied by another pawn. So if there's a white pawn at (5,c), and a black pawn at (4,c), then during B's turn, they can choose to move that black pawn down to (5,c), but that's occupied by the white pawn. So that's invalid. So B can't move that pawn. So the black pawn is stuck. So the white pawn can't move up. So the only way for the white pawn to proceed is if there's another pawn that can be moved.

But in this case, the code would have to consider that this white pawn's path is blocked. So for Player A to win, there must be another white pawn in a different column with a clear path.

So the conclusion is that for a white pawn to reach row 1 in k steps, it must have a clear path upwards in its column. Because if there are any pawns (of any color) in that column above it, those pawns can't be moved out of the way, and thus block the path.

Wait, but what if there's a white pawn in (3,c) and another white pawn in (4,c). Then the upper pawn (3,c) can move up, and once it's moved, the lower pawn (4,c) can then start moving. But the upper pawn can reach row 1 in 2 steps (3-1=2), and the lower pawn would need 3 steps, but it's blocked by the upper pawn. So in that case, the minimal steps would be 2, from the upper pawn.

So for each white pawn, the steps required are (r-1) minus the number of white pawns above it in the same column. Because each white pawn above must move first. For example, if a white pawn is in row 5, and there are two white pawns above it (rows 4 and 3), then each of those must move up before this pawn can move. So the total steps for this pawn would be (5-1) + 2 (the two pawns above that need to move first). Wait, maybe not. Let's see.

If the upper pawns can move first, then their movement can be handled in parallel. For example, if there are two white pawns in column c, at rows 3 and 5. Then during Player A's first move, they can choose to move the upper pawn (row 3) to row 2. Then next turn, move it to row 1. So that's two steps. The lower pawn (row 5) would have to wait until the upper pawns are moved. So in that case, the lower pawn can't reach the top until the upper ones are gone. So the minimal steps for the lower pawn is 5-1 (4 steps) plus the steps needed for the upper pawns to clear the way. But how?

Alternatively, perhaps the minimal steps for a white pawn in a column is the number of white pawns above it plus the steps needed to reach row 1. For example, if a pawn is at row r, and there are k white pawns above it in the same column, then the minimal steps would be (r - 1) + k. Because each of those k pawns must be moved out of the way (each takes one step), but since the player can choose which pawn to move each time. Wait, but if there are multiple pawns in a column, they can be moved in any order, but perhaps each one requires some steps.

Alternatively, the minimal steps for a white pawn in a column is (r - 1) minus the number of empty cells between it and row 1. Because any existing pawn (of any color) in that path blocks the way, but white pawns above can be moved first, but black pawns cannot. Wait, but black pawns can't be moved upwards. So if there's a black pawn in the same column above a white pawn, then that white pawn's path is blocked, and can't move up. So that's a problem.

So, for a white pawn at row r, column c, the steps required to reach row 1 is:

The number of steps needed is (r-1) if the path from (r-1, c) to (1, c) is clear (all '.'). But if there are any pawns (either white or black) in any of those cells, then the white pawn can't reach row 1 via this column.

Wait, but this isn't correct. Because other pawns can be moved. For example, a white pawn in row 4, column c, and a white pawn in row 3. Then Player A can move the row 3 pawn first, then the row 4. So the steps for the row 4 pawn would be 4-1 =3 steps (since each move takes a step, but the upper pawns are being moved first). Wait, but how?

If the pawns are in row 3 and 4. For the pawn in row 4 to reach row 1, it needs to move up 3 steps. But the pawn in row 3 must first move up. So during step 1, Player A moves the row 3 pawn to row 2. Step 2, moves it to row 1. So that's two steps. Then, the row 4 pawn can start moving. So in step 3, Player A moves it to row 3. Step 4, to row 2. Step 5, to row 1. So total steps is 5. But that's more than 3. Hmm.

Alternatively, maybe the minimal steps for the column is the maximum steps required by any white pawn in that column, considering that each must wait for the ones above to move.

So in the example above, the row 3 pawn requires 2 steps, the row 4 pawn requires 3 steps. So the minimal steps for the column would be the sum of (r_i - 1) for all pawns in the column, but that's not correct.

Alternatively, if there are multiple white pawns in a column, the minimal steps for the column is (r_1 -1) + (r_2 -1) ... where r_1 < r_2 < ... but that seems off.

This seems complicated. Let's think of the steps as the earliest time when any pawn reaches row 1. For each column, the earliest step a white pawn can reach row 1 is the minimal steps required for any pawn in that column, considering the number of pawns (white) above it. Because for a pawn at row r in column c, if there are k white pawns above it, then those pawns must move first. But each can be moved in their own steps. So the earliest step for this pawn is (r-1) + (number of white pawns above it). Because for each of those pawns, you have to wait for them to move. So for example, a pawn at row 5 with two pawns above it (rows 3 and 4) would have steps (5-1) + 2 = 6 steps. Because each of the two pawns above must be moved first, each taking their steps. But perhaps this isn't the case.

Alternatively, the earliest step for a white pawn in column c is the row number minus 1, minus the number of white pawns above it. Wait, that seems counter-intuitive. Let's take an example. If a pawn is at row 4 with one white pawn above it at row 3. Then the pawn at row 3 can reach row 1 in 2 steps. So the pawn at row 4 would have to wait until row 3 is cleared. So the steps would be 3 steps (since row 4 needs 3 steps, but after the pawn in row 3 is moved, the pawn in row 4 can start moving. So perhaps the total steps would be 2 (for the upper pawn) + 3 (for the lower pawn) steps. But that's 5 steps, which is higher than both. But perhaps the earliest is the upper pawn's 2 steps.

So the minimal steps for the column is the minimal steps among all white pawns in that column, considering the number of white pawns above them.

Alternatively, perhaps the minimal steps for a column is (r - 1) - (number of white pawns above the pawn) + (number of white pawns below the pawn). Not sure.

This is getting stuck. Let's look for patterns in the sample inputs.

First sample input:

........
........
.B....B.
....W...
........
..W.....
........
........

The white pawns are at row 4 (column 5) and row 6 (column 3). For the pawn at row 4, column 5:

Looking at column 5. The cells above are rows 3, 2, 1. Are there any pawns in those cells? The third row (row 3) has a black pawn in column 2 and 7 (from input line 3: .B....B. So row 3, columns 2 and 7 are B. So column 5 in row 3 is '.'). So the path is clear. So the steps needed are 4-1=3 steps. For the pawn in row 6, column 3: the path up is rows 5,4,3,2,1. Are there any pawns in those cells? Looking at the input:

Row 6 is ..W....., which is column 3 is W. So the pawn is at row 6. The cells above in column 3: rows 5,4,3,2,1. Let's see:

Row 4 (input line 4): ....W... → column 5 is W. Other columns are '.'.

Row 5: ........ (input line 5). So column 3 in row 5 is '.'.

So the path for the pawn at (6,3) is clear. So steps needed: 6-1=5 steps.

But in the sample output, the answer is A, which means Player A can win in 3 steps. Which is the pawn at (4,5). So the minimal steps for A is 3, while B's minimal is 5 steps. So A wins.

So the key is to find the minimal steps for each player and compare.

For Player B, the steps are similar but for black pawns moving down. For each black pawn in column c, the steps required is (8 - r), where r is the current row. But again, there must be no pawns (any color) in the path (rows r+1 to 8).

So the approach would be:

1. For each white pawn, compute the minimal steps required to reach row 1, considering that the path (cells above in the same column) is empty. If there's any pawn (white or black) in the path, then this pawn can't use this column. So steps are not considered.

Wait, but that can't be right. Because in the first sample input, the white pawn at row 4, column 5 has a clear path. So steps 3. So that's why A can win in 3 steps.

But why? Because Player B can't block that path. But how? Because Player B moves their pawns down. So any black pawns in the same column can't block the path if they are below the white pawn. For example, a black pawn at row 5 in column 5 would be moving down each turn. So the white pawn's path (rows 3, 2, 1) are not blocked by that black pawn.

So, the path for a white pawn is the cells in the same column from row r-1 to row 1. If any of those cells are occupied by a pawn (white or black), then the white pawn can't move through that path, unless those pawns are moved. But white pawns can be moved by Player A, and black pawns can be moved by Player B.

But how do their movements affect each other?

Maybe the correct approach is to find for each white pawn the earliest step it can reach row 1, assuming that B does everything possible to block it, but A can choose the best path.

Alternatively, perhaps the minimal steps for a white pawn is the number of steps needed if there are no black pawns in the same column above it. Because B can't block that path once the white pawn is moving.

Wait, but B can choose to move a black pawn into the column. But since B's pawns move down, they can't move up. So for example, if a white pawn's path is clear, then B can't block it. Because B's pawns can't move upwards. So if a white pawn's path is clear, then the steps are (r-1), and Player A can win in those steps.

But if there's a black pawn in the same column but below the white pawn's path, then it's irrelevant. Because the black pawn moves down, away from the white pawn's path.

So the key is to find for each white pawn the minimal steps to row 1, given that the path (cells above) in its column is completely empty. If there's any pawn (white or black) in the same column and in any of the rows between current row-1 and 1, then that pawn blocks the path. But white pawns can be moved up by Player A, while black pawns can't be moved up by Player B.

So for a white pawn to have a clear path, the column must have no pawns (white or black) in the cells between the pawn and row 1. Because:

- Any white pawns in those cells must be moved up first, which takes steps. But if Player A chooses to move those pawns first, it might delay the current pawn's progress.

- Any black pawns in those cells can't move up, so they block the path.

So for a white pawn to reach row 1, the path in its column must be clear of any pawns. Because any pawn (white or black) in the path would block it.

Wait, but if there are white pawns in the path, Player A can move those pawns first. For example, if there's a white pawn in row 3, and another in row 4. The upper one (row 3) can be moved first, requiring 2 steps, and then the row 4 can be moved in 3 steps. So the minimal steps for the column would be 2 steps (from the upper pawn), but the lower pawn would take longer. So the minimal steps for the column is 2 steps.

Thus, for each column, the minimal steps is the minimal (r-1) among all white pawns in the column, provided that there are no pawns (white or black) in the rows between (r-1) and 1.

Wait, no. Because if there are other white pawns in the same column above, the lower pawn can't move until those are moved. So for example, if a pawn is at row 5, column c, and there is another white pawn at row 3, then the row 3 pawn can reach row 1 in 2 steps. So the minimal steps for the column is 2. The lower pawn at row 5 is blocked by the upper pawn, but since the upper pawn is moved first, the minimal steps are 2.

But how to model this in code?

So for each column, find the topmost white pawn (smallest row number) in that column, and compute (r-1) steps. But only if there are no pawns (of any color) in the rows between that pawn and row 1.

Because if there are any pawns (even white) above that pawn, then the pawn is not the topmost. So the topmost white pawn would have no pawns (of any color) between it and row 1.

Wait, but if the topmost white pawn is at row 3, and there's a black pawn at row 2, then the path is blocked, so even though the white pawn is topmost, it can't reach row 1. So for that column, the steps would be infinity (can't be used).

So the approach is:

For each column:

- Find the topmost white pawn (smallest row number) in that column.

- Check if all rows from row (r-1) down to 1 are empty (i.e., no pawns of any color).

- If yes, then the steps for this column are (r-1).

- Keep track of the minimal such step across all columns.

Similarly for Player B:

For each column:

- Find the bottom-most black pawn (largest row number) in that column.

- Check if all rows from row (r+1) up to 8 are empty.

- If yes, steps are (8 - r).

- The minimal such step across all columns is the minimal steps for B.

Then, the player with the minimal steps wins. If the minimal steps for A is <= minimal steps for B, then A wins. Else B wins.

Because both players are playing optimally, so A can choose the fastest possible path, and B can choose theirs.

Wait, but what if the minimal steps for A is 3 and B's is 3. Since A moves first, the steps would be A's steps <= B's steps. So A would win.

For example, if A's steps are 3, B's steps are 3: A moves first. So in step 3 (A's 3rd move), the pawn reaches row 1 and wins before B can complete their 3rd move (since B moves after A each turn).

So the comparison is: if A's minimal steps <= B's minimal steps, then A wins. Else B wins.

So the algorithm would be:

1. For all white pawns, for each column, find the topmost white pawn and check if the path to row 1 is clear. If so, track the minimal steps (r-1) among all such columns.

2. For all black pawns, for each column, find the bottom-most black pawn and check if the path to row 8 is clear. If so, track the minimal steps (8 - r) among all such columns.

3. Compare the minimal steps of A and B. If A's steps <= B's steps, output 'A', else 'B'.

This seems to fit the sample input.

First sample:

The white pawn in column 5 is at row 4. Check if the rows 3,2,1 are empty. Yes. So steps 3.

Other white pawn in column 3, row 6. Check rows 5,4,3,2,1. Are those empty? Let's see:

Row 5 in column 3 is empty (input line 5 is ........). Row 4 in column 3 is '.' (input line 4: ....W... → W is in column 5). So yes, the path is clear. So steps 5 (6-1). So minimal for A is 3.

For B:

Looking at black pawns. The sample input has two black pawns in row 3, columns 2 and 7.

For column 2: bottom-most black pawn is row 3. Check if rows 4-8 are empty. Row 4 in column 2: input line 4 is ....W..., so column 2 is '.'. Rows 4-8 in column 2 are empty. So steps 8-3=5.

For column 7: black pawn in row 3. Check rows 4-8. Are they empty? Let's see. The input lines:

Row 3: .B....B. → columns 2 and 7 are B. So row 3, column 7 is B. Check rows 4-8:

Row 4: ....W... → column 7 is '.'.

Row 5: ........ → column 7 is '.'.

Row 6: ..W..... → column 7 is '.'.

Row 7: ........ → column 7 is '.'.

Row 8: ........ → column 7 is '.'.

So yes, rows 4-8 in column 7 are empty. So steps 8-3=5.

So B's minimal steps is 5. Since A's is 3 (<=5), A wins.

Second sample input:

..B.....
..W.....
......B.
........
.....W..
......B.
........
........
Output B.

For Player A:

Looking for white pawns. The white pawns are at row 2 (column 3) and row 5 (column 6).

For row 2, column 3: check rows 1. It's empty. So steps 2-1=1. But wait, the pawn is at row 2. So steps is 1. But in the input, the initial setup is such that there are no white pawns in row 1. So the white pawn is in row 2. So steps 1. But why doesn't A win in 1 step?

But looking at the sample output, the answer is B. So perhaps there's a blocking pawn in the path.

Wait, in the second sample input:

The input lines are:

Line 1: ..B..... → row 1, columns 3 is B.

Wait, no. Row 1 is the first input line. Let's parse each line as rows 1 to 8.

Sample input 2:

Line 1: ..B..... → columns 3 is B. So row 1, column 3 is B. But the problem statement says that there are no white pawns in row 1. But this is a black pawn.

But for the white pawn in row 2, column 3: the path to row 1 is just row 1, which is occupied by a black pawn. So the path is blocked. So steps can't be taken. So this pawn can't reach row 1.

The other white pawn is in row 5, column 6. Let's check its column. The path is rows 4,3,2,1. Are there any pawns in those rows for column 6?

Row 5: .....W.. → column 6 is W. So row 5.

Check row 4: ........ → column 6 is '.'.

Row 3: ......B. → column 6 is '.' (since the line is 6 characters, but perhaps I should index correctly. Wait, each line is 8 characters. So line 3: "......B." → columns 1-6 are '.', column7 is B, column8 is '.'.

So row 3, column 6 is '.'.

Row 2: ..W..... → column 6 is '.'.

Row 1: ..B..... → column 6 is '.'.

So the path for row 5, column 6 is clear. So steps is 5-1=4. So A's minimal steps is 4.

For B's pawns:

Looking for black pawns. Let's see:

Row 1, column 3: B (but B's target is row 8. But this pawn is already in row 1, but the problem states that no black pawns are in row 8. So this pawn can't be considered. Wait, no. Because black pawns can't be in row 8. The initial setup has black pawns in row 1, which is allowed. Wait, the problem statement says: "It's guaranteed that there will not be white pawns on the first row neither black pawns on the last row." So black pawns can be in row 1-7.

So for B's pawns in the sample input 2:

Looking for black pawns in each column. Let's find in each column the bottom-most black pawn.

For example:

In column 3: row 1 has B, but it's the only B in that column. So check if the path from row 2 to 8 is clear. The path is rows 2-8 in column 3. Are there any pawns there?

Looking at each row's column 3:

Row 1: B.

Row 2: W (..W.....), so column 3 is W. So for the B in column 3 (row 1), the path is rows 2-8. But row 2, column 3 is W. So there's a pawn blocking. So this pawn can't use this column.

Another black pawn is in row 3, column 7. Let's see:

The bottom-most B in column 7. Row 3 has B, row 6 has B (sample input line 6: ......B. → column 7 is B). So row 6, column7 is B. Check if rows 7 and 8 are clear.

Row 7: ........ → column7 is '.'.

Row 8: ........ → column7 is '.'.

So for this pawn, steps are 8-6=2.

Another black pawn in column7 is row 3. The bottom-most is row6. So steps is 2.

Another black pawn in column 7: row6. So steps 8-6=2.

So B's minimal steps is 2. So B can reach in 2 steps, which is less than A's 4 steps. So B wins.

So the algorithm works for both samples.

So now, the plan is:

1. For each column, check if there are white pawns. Find the topmost white pawn (smallest row) and check if all rows from (r-1) down to 1 are empty. If yes, record (r-1) as a candidate for A's minimal steps.

2. Similarly, for each column, check if there are black pawns. Find the bottom-most (largest row) and check if all rows from (r+1) to 8 are empty. If yes, record (8-r) as a candidate for B's minimal steps.

3. Compare the minimal steps between A and B. If A's steps <= B's, A wins; else B.

So the code steps:

- Read the 8x8 grid.

- For each column c (0 to 7, perhaps 0-based?), process all rows to find the topmost white pawn and check the path.

- Similarly, for each column, process all rows to find the bottom-most black pawn and check the path.

Implementing this in code.

Now, how to represent the grid. Let's read each line as a list, and for each column c, iterate through the rows.

For white pawns (A's pawns):

For each column c:

- Iterate from row 0 (top row, row 1 in the problem's 1-based) to row 7 (row 8). Wait, the problem uses rows 1-8, so the input lines are rows 1 to 8.

Wait, the input is 8 lines, each line represents a row from row 1 (top) to row 8 (bottom). So the first line is row 1, the last line is row 8.

So, in code, the first element of the list is row 1.

So, for each column c in 0-7:

- For white pawns:

   - Iterate from row 0 (row 1) to row 7 (row 8) in the grid. We need to find the first 'W' encountered (since we are looking for the topmost in the column). So the first 'W' when checking from top (row 0 in the list) down to row 7.

   - Once found at row r (0-based in the list, which corresponds to row r+1 in the problem's terms), check the rows from r-1 down to 0 (since the problem's row is r+1, so the next row up is r-1 in the list). Wait, no. For example, if the white pawn is in list row 3 (problem row 4), then the cells above are list rows 2 (problem row3), 1 (problem row2), 0 (problem row1). So for the path to be clear, all those rows in column c must be '.'.

So, for a white pawn found at list row r (problem row r+1), the path is rows r-1, r-2, ..., 0 (problem rows r, r-1, ..., 1). Wait, no. Because the pawn is at problem row r+1 (since list row 0 is problem row 1). So moving up to problem row 1 requires moving through rows r (problem row r+1-1 = r), r-1, etc. So the list rows would be r-1, r-2, ..., 0.

Wait, no. Let's see: the white pawn is at list row r (0-based), which is problem row r+1. To reach row 1 (problem row 1, list row 0), it needs to move up r steps. So the cells it must pass through are problem rows r, r-1, ..., 1. But the list rows for these are r-1, r-2, ..., 0.

So for example, a pawn in list row 3 (problem row4) needs to go through list rows 2 (problem3), 1 (problem2), 0 (problem1).

So, the code for checking the path is:

For a white pawn at list row r (problem row r+1):

   For each list row i in r-1, r-2, ..., 0:

      Check grid[i][c] == '.'.

   If all are true, then steps is (r+1 -1) = r steps.

Similarly for black pawns:

For a black pawn in list row r (problem row r+1), which is bottom-most in column c (so the list row is the largest possible in the column where 'B' occurs):

   For each list row i in r+1, r+2, ..., 7 (problem rows r+2, r+3, ..., 8):

      Check grid[i][c] == '.'.

   If all are true, steps is (8 - (r+1)) = 7 - r.

So the code:

Read the grid as a list of 8 strings (each 8 characters). Then, for each column c (0-7):

A's possible steps:

   min_a = infinity

   for r in 0 to 7:

      if grid[r][c] == 'W':

          # check if all rows above (0 to r-1) in column c are empty

          # actually, the path is from row r-1 down to 0.

          # wait, the current row is r. The path to row 1 (problem row) is through list rows r-1, r-2, ..., 0.

          # So for the pawn at list row r, check rows r-1 down to 0 in column c.

          # For each row in 0 to r-1: no, wait. If the pawn is at list row r, then to move up, it has to go through list rows r-1 (problem row r), r-2 (problem row r-1), ..., 0 (problem row1).

          # So check all list rows from r-1 down to 0 in column c.

          valid = True

          for i in range(r-1, -1, -1):

              if grid[i][c] != '.' :

                  valid = False

                  break

          if valid:

              steps = r  # because problem row is r+1, steps is (r+1 -1) = r.

              if steps < min_a:

                  min_a = steps

          # since we are checking from top to bottom, the first 'W' in the column (from top) is the topmost. Once found and valid, we can break, as any lower W in the same column will have higher steps.

          break

   So, for each column c:

      find the first 'W' from top (r from 0 to 7):

          if found:

              check path from r-1 down to 0.

              if valid, compute steps as r.

              update min_a.

Similarly for B's steps:

min_b = infinity

for each column c:

   find the last 'B' in the column (r from 7 downto 0):

       if grid[r][c] == 'B':

           check rows from r+1 to 7:

               if any of them have non '.', invalid.

           if valid:

               steps = 7 - r

               if steps < min_b:

                   min_b = steps

           break

So, code steps:

Read grid as 8 lines.

min_a = infinity

for each column c in 0-7:

   for r in 0 to7:

       if grid[r][c] == 'W':

           # check path

           valid = True

           for i in range(r-1, -1, -1):

               if grid[i][c] != '.':

                   valid = False

                   break

           if valid:

               steps = r

               if steps < min_a:

                   min_a = steps

           break

Similarly for B:

min_b = infinity

for each column c in 0-7:

   for r in 7 downto 0:

       if grid[r][c] == 'B':

           # check path

           valid = True

           for i in range(r+1, 8):

               if grid[i][c] != '.':

                   valid = False

                   break

           if valid:

               steps = 7 - r

               if steps < min_b:

                   min_b = steps

           break

Once we have min_a and min_b, compare:

if min_a <= min_b:

    print('A')

else:

    print('B')

So this code should work.

Testing on the sample inputs.

First sample:

The white pawn in column 4 (assuming 0-based columns?), wait let's see. The input line 4 (problem row5) is ....W... → which is columns 0-7. The W is at position 4 (columns 0-based). So column 4. List row is 3 (since input lines are read as rows 0-7 for problem rows 1-8).

So for column 4:

r is 3 (problem row4+1=4?), no. Wait, the input is read as rows 0 to7, which correspond to problem rows 1 to8. So for the input line 3 (row4 in problem terms) is ....W... → the W is at column 4 (0-based). So list row3, column4.

So for column4, we check from top to bottom. The first 'W' is at r=3. Check rows 2,1,0 in column4. Are those '.'? Let's see:

Line 3 (row4) column4 is W. Then line 2 (row3) column4 is '.' (sample input's third line is .B....B. → column4 is '.'). Line1 (row2) column4 is '.' (second line ........). Line0 (row1) column4 is '.'.

So path is valid. Steps is 3.

Other columns: the other W is in column2, row5 (problem row6). So list row5, column2. Check rows 4,3,2,1,0. Are they '.'? Let's see:

For column2:

r=5. So check rows 4 (list row4) column2: input line4 is ........ → column2 is '.'. Row3 (list row3) column2 is '.' (third line .B....B. → B is in column1 and6). Row2 (list row2) column2: input line2 is ..W..... → no, line2 is the third line of input (problem row3). Wait, the input lines are:

Sample input 1:

Line 0: ........ (row1)

Line1: ........ (row2)

Line2: .B....B. (row3)

Line3: ....W... (row4)

Line4: ........ (row5)

Line5: ..W..... (row6)

Line6: ........ (row7)

Line7: ........ (row8)

So the other W is in line5, column2. So r=5 (list row5, problem row6). So path is rows4,3,2,1,0 in column2.

Row4 (list row4) column2: line4 is ........ → '.'.

Row3 (list row3) column2: line3 is ....W... → column2 is '.'.

Row2 (list row2) column2: line2 is .B....B. → column1 is B, column6 is B. So column2 is '.'.

Row1 (list row1) column2: line1 is ........ → '.'.

Row0 (list row0) column2: line0 is ........ → '.'.

So path is valid. Steps is 5. So min_a is min(3,5) →3.

For B's pawns: in columns1 and6.

For column1:

Looking for the last 'B' in column1. Let's see:

line2 (problem row3) column1 is B. line7 (problem row8) is all '.', so no other Bs. So r=2 (list row2) for column1. Check rows3-7 (list rows3 to7) in column1. All are '.' (since line3 and others have '.' in column1). So steps is 7-2=5.

For column6: last B is in line2 (problem row3), column6. Check rows3-7. line3 has column6 as '.' (....W...). Others are '.' So steps 5.

So min_b is5. So A's steps 3 <=5 → A wins.

Second sample input:

Sample input 2:

Line0: ..B..... → columns2 is B (row1, column3 in problem terms).

Line1: ..W..... → columns2 is W (row2, column3).

Line2: ......B. → column6 is B (row3, column7).

Line3: ........ (row4)

Line4: .....W.. → column5 is W (row5, column6).

Line5: ......B. → column6 is B (row6, column7).

Line6: ........ (row7)

Line7: ........ (row8)

For A's steps:

Looking for topmost W in each column.

For column2 (problem column3):

Check row1 (line1) column2 is W. Check path rows0 (line0, column2 is B). So path is not valid. So no steps.

For column5 (problem column6):

Check topmost W. In line4 (row5, problem row5). Check rows3,2,1,0 in column5. Are they '.'?

Row4 (line4) column5 is '.' → line4 is .....W.. → column5 is '.'?

Wait, no. Let's parse the input lines:

Line0: ..B..... → index 0: '..B.....', which is '..B.....' → columns0-7: indexes 0 is '.', 1 is '.', 2 is 'B', others '.'.

Line1: ..W..... → columns2 is 'W'.

Line4: .....W.. → columns5 is 'W'.

So for column5:

Check if there is any 'W' in column5. The W is in line4 (row5). Check rows3 (line3, column5) is '.'? Yes. Line3 is ......... So yes. Then rows2 (line2) column5 is '.'? Line2 is ......B. → columns5 is '.' (since it's the sixth character). So rows3 (line3) is '.', row2 (line2) column5 is '.' (since line2 is "......B." → columns0-5 are '.'). So rows4-1 (problem row5-1=4 down to 1) in column5 are all '.'.

So steps is 4 (problem row5-1=4 steps). So min_a is4.

For B's steps:

Looking for bottom-most B in each column.

For column3 (problem column4):

B in line0 (row1, problem row1). Check rows1-7 (list rows1-7). line1 (row2, column3) is W. So path is blocked. So not valid.

For column6 (problem column7):

Looking for bottom-most B in column6. The B's are in line2 (row3) and line5 (row6). The bottom-most is line5 (row6). Check rows6,7 (list rows5+1 to7). list row5+1 is 6 (problem row7), row7 is list row7 (problem row8). For column6:

line6 (row7) column6 is '.'.

line7 (row8) column6 is '.'.

So valid. Steps is 7-5=2. So min_b is 2. So B's steps is 2, which is less than A's 4. So B wins.

So the code works.

So now, the code can be written as:

Read the 8 lines into a list.

For each column c in 0-7:

   For A:

      find the first 'W' in the column (from top, i.e., starting from row 0).

      if found:

          check all rows above (from r-1 downto 0) in column c. If all '.', then steps is r.

          compare and update min_a.

For B:

   for each column c:

      find the last 'B' in the column (from bottom, i.e., starting from row7).

      if found:

          check all rows below (from r+1 to7) in column c. if all '.', steps is7 - r.

          compare and update min_b.

Compare min_a and min_b.

So in code:

Read the grid as:

grid = [input().strip() for _ in range(8)]

Then:

min_a = float('inf')

for c in range(8):

    for r in range(8):

        if grid[r][c] == 'W':

            # check path from r-1 downto 0

            valid = True

            for i in range(r-1, -1, -1):

                if grid[i][c] != '.':

                    valid = False

                    break

            if valid:

                min_a = min(min_a, r)

            # since we're checking from top, break after first W

            break

min_b = float('inf')

for c in range(8):

    for r in range(7, -1, -1):

        if grid[r][c] == 'B':

            # check path from r+1 to 7

            valid = True

            for i in range(r+1, 8):

                if grid[i][c] != '.':

                    valid = False

                    break

            if valid:

                min_b = min(min_b, 7 - r)

            # break after first B (bottom-most)

            break

if min_a <= min_b:

    print('A')

else:

    print('B')

This should work.

Testing the code on the samples.

Sample1:

After reading the grid, for column4 (c=4):

r loops from 0 to7. First 'W' is at r=3 (row4). Check rows 2,1,0. All are '.'.

So steps is3. min_a is3.

For B, in column1 (c=1):

r loops from7 downto0. First 'B' is at r=2 (row3). Check rows3-7. All are '.'.

Steps is7-2=5. min_b is5. A wins.

Sample2:

A's min_a is4. B's min_b is2. So B wins.

The code should handle these correctly.

Edge case: what if multiple columns have valid steps?

Like, A has steps 3 and 2. Then min_a is2.

So code correctly takes the minimum.

So this should be the correct code.
</think>

```python
grid = [input().strip() for _ in range(8)]
min_a = float('inf')
for c in range(8):
    for r in range(8):
        if grid[r][c] == 'W':
            valid = True
            for i in range(r-1, -1, -1):
                if grid[i][c] != '.':
                    valid = False
                    break
            if valid:
                min_a = min(min_a, r)
            break  # topmost W in column
min_b = float('inf')
for c in range(8):
    for r in range(7, -1, -1):
        if grid[r][c] == 'B':
            valid = True
            for i in range(r+1, 8):
                if grid[i][c] != '.':
                    valid = False
                    break
            if valid:
                min_b = min(min_b, 7 - r)
            break  # bottommost B in column
print('A' if min_a <= min_b else 'B')
```