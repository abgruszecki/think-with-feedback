<think>
Okay, let's see. The problem is about Bob's king moving from his starting position to the target without ever being in check by Alice's queen. So the queen is stationary, and Bob's king can move one step in any direction each move. The key is that during his entire path, none of the positions he steps on can be in check. Oh right, including the starting and ending positions, but the problem statement already says those are safe. So the question is: can the king find a path from (b_x, b_y) to (c_x, c_y) where all intermediate steps are also not in check?

First, I need to figure out what positions are in check. A position is in check if it's on the same row, column, or diagonal as the queen. So the queen's row is a_x, so any (a_x, y) is in check. Similarly, her column is a_y, so any (x, a_y). For the diagonals, positions where the difference in x and y coordinates are the same (like x - a_x = y - a_y) or sum is the same (x + y = a_x + a_y) are on the two diagonals.

The king's movement is blocked if any of the squares along the path are in check, and he can't move through those. So the problem reduces to checking if there's a path from B to C in a grid where all the 'blocked' cells are those in check by the queen, and the king can only move to adjacent non-blocked cells.

So the approach here is to model the grid as a graph where each cell is a node, and edges connect to adjacent cells (8 directions). The blocked cells are those in check. Then, check if there's a path from B's starting position to C's position using BFS or DFS. Since the grid can be up to 1000x1000, BFS is better here because it's more memory efficient for large grids, but wait, even 1000x1000 is a million nodes. BFS would require a visited array of size a million, which is manageable.

But wait, the problem constraints say that n can be up to 1000, so the chessboard is 1000x1000. However, checking each cell for being in check can be done in O(1) time. So the steps would be:

1. Precompute all the cells that are under check by the queen. For each cell (x, y), check if it's in the same row, column, or diagonal as (a_x, a_y).

But for large n (like 1000), we can't check every cell. Instead, we can determine for any given (x, y) whether it's in check. So during BFS, for each neighbor cell, we check if it's in check. If not, and not visited yet, we add it to the queue.

But how do we determine if a cell is in check? Let's think.

A cell (x, y) is in check if:
x == a_x (same row)
OR
y == a_y (same column)
OR
(x - a_x) == (y - a_y) (same diagonal)
OR
(x + y) == (a_x + a_y) (same anti-diagonal)

If any of these conditions are true, then the cell is blocked.

So during BFS, when considering moving to a neighboring cell (nx, ny), we first check if it's within the chessboard (1 <= nx <=n, same for ny), then check if it's not in check. Also, we need to make sure we don't revisit cells.

So the algorithm would be:

- Start from (b_x, b_y)
- Use BFS to explore all reachable cells that are not in check and not visited.
- If during BFS we reach (c_x, c_y), return YES. Otherwise, after BFS completes without finding it, return NO.

Now, the key is to implement this efficiently. Let's outline the steps.

First, read the inputs: n, a's coordinates, b's, c's.

Then, check if the start and end positions are already in check. But the problem statement says that they are not. So we don't need to check that.

But during the BFS, we need to make sure that each step's neighbor is not in check.

Implement BFS with a queue. We can represent visited as a 2D array (or a set of tuples). But for n up to 1000, a 1001x1001 array (since positions are 1-based) would take about 1MB (each cell is a boolean, 1000*1000 = 1e6 bits, which is about 125KB). So that's manageable.

So the steps:

Initialize a visited 2D array, all False. Mark (b_x, b_y) as visited.

Create a queue and add the starting position.

For each position in the queue, check all 8 neighbors. For each neighbor (nx, ny):

- Check if nx and ny are between 1 and n.
- Check if (nx, ny) is not in check (using the conditions above)
- Check if not visited.

If all conditions met, add to queue and mark as visited.

If any of the neighbors is (c_x, c_y), return YES.

Proceed until queue is empty. If not found, return NO.

So the main parts are:

- The check for a cell being in the queen's line of attack.
- Efficient BFS.

Now, let's think about possible optimizations.

The BFS will process cells that are reachable via the king's movement and are not in check. The worst case is when the queen's attack lines split the board into regions, and we need to check if the start and end are in the same region.

But given that n is up to 1000, the BFS may take O(1e6) steps, which is acceptable for the time limit. Each step has 8 directions, but even 8 million operations are manageable in Python, as per the time constraints (1 second). Python can handle about 1e6 operations per second, but BFS with 1e6 nodes and 8e6 edges might be tight. However, given that in practice, the BFS might terminate early once the destination is found, it's manageable.

Another thing to consider is that the queen's attack lines form cross and diagonals. So the board is divided into regions separated by these lines. The king cannot cross these lines. So perhaps the problem can be rephrased as: are B and C in the same region, where the regions are the connected components formed by the non-attacked cells.

If that's the case, then BFS is the way to go.

But how to model the regions. For example, if the queen is in the center, the attack lines divide the board into four quadrants. But the regions could be more complex depending on the queen's position.

Alternatively, maybe the BFS approach is the most straightforward and efficient given the constraints.

Now, let's code this.

First, read the inputs:

n = int(input())
a_x, a_y = map(int, input().split())
b_x, b_y = map(int, input().split())
c_x, c_y = map(int, input().split())

Then, check if (b_x, b_y) is (c_x, c_y). But the problem says they are not, so we can ignore that.

Then, implement the BFS.

We need a visited array. Since n is up to 1000, perhaps use a 2D list of size n+1 (since 1-based) for visited.

But in Python, for n=1000, creating a list of lists would take O(n^2) time and memory. However, 1000x1000 is 1e6 elements. Each boolean is 1 byte in a list, so that's 1MB, which is acceptable.

So:

visited = [[False]*(n+1) for _ in range(n+1)]

Then, the queue. We can use deque from collections for efficient pops from the front.

So:

from collections import deque

queue = deque()
queue.append( (b_x, b_y) )
visited[b_x][b_y] = True

Then, the BFS loop:

directions = [ (-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1) ]

while queue:
    x, y = queue.popleft()
    if x == c_x and y == c_y:
        print("YES")
        exit()
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 1 <= nx <= n and 1 <= ny <= n:
            # Check if (nx, ny) is not in check
            if (nx == a_x or ny == a_y or (nx - a_x) == (ny - a_y) or (nx + ny) == (a_x + a_y)):
                # In check, skip
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append( (nx, ny) )

After processing all directions, if the queue is empty and not found, print "NO".

So that's the code.

But let's test against the sample inputs.

Sample 1:

8
4 4
1 3
3 1

Queen is at (4,4). So the attack lines are row 4, column 4, diagonals where x-y=0 and x+y=8.

Bob starts at (1,3). Target is (3,1).

The BFS would check possible paths. The king can't cross row 4, column4, or the diagonals. So possible path is moving around those lines.

In the sample, the path is possible, so output is YES.

Sample 2:

8
4 4
2 3
1 6

Queen's row is 4. So the king is at (2,3), needs to get to (1,6). To get there, perhaps he needs to cross row4, which is blocked. So he can't cross, hence output is NO.

Sample 3:

Queen is (3,5). King starts at (1,2), target is (6,1). The queen's column is 5. So to move from (1,2) to (6,1), the king would have to cross column5. But the path would require moving through that column, which is under attack, so it's blocked.

So output is NO.

So the code should handle these cases.

Now, edge cases to consider:

Case where the start and end are in the same region. For example, queen is at (500,500), n=1000. Start is (1,1), end is (1000,1000). The attack lines are row500, column500, and diagonals. The path from (1,1) to (1000,1000) would require moving along the edge of the board, avoiding the attack lines.

But the code should handle that.

Another edge case: n=3. Queen is at (2,2). The attack lines are row2, column2, and diagonals. So the available cells are (1,1), (1,3), (3,1), (3,3). So if start is (1,1), end is (3,3), the king can't move directly, since the diagonals are blocked. But (1,1) can't move to (3,3) in steps because each step would have to pass through (2,2), which is the queen's position. Wait, but the queen's position is blocked, but the problem statement says that the king's start and end are not on the same square as the queen. So perhaps in that case, the king can't move, but the sample input 3 has a queen's column blocked, etc.

Wait, the queen's own position is (a_x, a_y). Any cell that is (a_x, a_y) is the queen's position, but the problem says that the start and end positions are not on that cell, so the king can't step there. But according to the code, the queen's cell is considered in check (since it's same row, etc.), so the code will block it. But in the problem, the king can't step on the queen's cell. So the code correctly skips that.

So the code's logic should be correct.

Now, for the code. Let's write it in Python.

But wait, in Python, for a 1000x1000 grid, the visited list as a list of lists is manageable.

But in the code, for each nx and ny, we check if (nx, ny) is in check. Let's code that part correctly.

The condition is:

if (nx == a_x) or (ny == a_y) or (nx - a_x == ny - a_y) or (nx + ny == a_x + a_y):

If any of these is true, then the cell (nx, ny) is under attack. So the code skips it.

Yes.

So the code will correctly avoid all cells under attack.

Now, the code should read the inputs, and proceed with the BFS.

So putting it all together:

Import deque, read inputs, set up visited, queue, directions, loop, etc.

Here's the code:

Read all the inputs.

Then, check if (b_x, b_y) is (c_x, c_y). But according to the problem statement, it's not. So no need.

So the code is:

import sys
from collections import deque

n = int(sys.stdin.readline())
a_x, a_y = map(int, sys.stdin.readline().split())
b_x, b_y = map(int, sys.stdin.readline().split())
c_x, c_y = map(int, sys.stdin.readline().split())

visited = [[False]*(n+1) for _ in range(n+1)]
queue = deque()
queue.append( (b_x, b_y) )
visited[b_x][b_y] = True

directions = [ (-1, -1), (-1, 0), (-1, 1),
               (0, -1),          (0, 1),
               (1, -1),  (1, 0), (1, 1) ]

found = False

while queue:
    x, y = queue.popleft()
    if x == c_x and y == c_y:
        found = True
        break
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 1 <= nx <= n and 1 <= ny <= n:
            # Check if (nx, ny) is under attack
            if nx == a_x or ny == a_y:
                continue
            if (nx - a_x) == (ny - a_y):
                continue
            if (nx + ny) == (a_x + a_y):
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append( (nx, ny) )

print("YES" if found else "NO")

Wait, but in the code above, the check for the attack is using the four conditions. But the code here is using four separate if statements. Wait, no: the code checks each condition. Let's see:

The code first checks if nx == a_x (same row) or ny == a_y (same column). If either is true, then continue (skip this neighbor).

Then, check if (nx -a_x) == (ny - a_y) (same diagonal). If so, continue.

Then check if (nx + ny) == (a_x + a_y) (same anti-diagonal). If so, continue.

Only if none of these conditions are true, then proceed.

Yes. So this correctly skips cells in check.

But wait, in the code, after checking the first two conditions (same row or column), it then checks the diagonals. So if any of the four conditions are met, the cell is blocked. So the code is correct.

So, the code will process the BFS, and for each neighbor cell, check if it's in the attack line. If not, and not visited, add to queue.

Now, for the sample input 1, the code should return YES.

But let's test sample input 1:

Sample 1:

n=8

Queen at (4,4)

King starts at (1,3), target at (3,1).

Check the attack lines. The queen's row is 4, column 4. Diagonals: x-y=0 (for example, 4-4=0). So cells like (5,5) are on the diagonal. The anti-diagonal is x + y = 8.

The king's path can go via (2,3) and (3,2). Let's see:

From (1,3), possible moves are to (0,2) [invalid], (0,3) [invalid], (0,4) [invalid], (1,2), (1,4), (2,2), (2,3), (2,4).

Wait, the king can move to (2,3) first. Check if (2,3) is under attack.

Check:

2 ==4? No. 3 ==4? No. 2-4 = -2, 3-4 = -1. Not equal. 2+3=5, 4+4=8. Not equal. So (2,3) is safe.

Add to queue.

Then from (2,3), explore all directions. One possible direction is (3,2).

Check (3,2):

3 !=4, 2 !=4. 3-4 = -1, 2-4=-2. Not same. 3+2=5 !=8. So safe.

Then from (3,2), next step to (3,1). (3,1) is the target. So the code would find this path and return YES.

Yes.

So the code works for sample 1.

Sample 2:

Queen is at (4,4). King starts at (2,3), target at (1,6).

The queen's row is 4, column4. The path requires moving from (2,3) to (1,6). Let's see if the code can find a path.

But the king is at (2,3). To get to (1,6), he would need to move up (from (2,3) to (1,3)), then right. But row1 is not under attack. Wait, (1,3) is in row1, which is not the queen's row (4). So (1,3) is safe. Then, from (1,3), he can move to (1,4), but (1,4) is in the queen's column (a_y=4). So that's blocked. Alternatively, maybe other paths.

But in sample 2, the output is NO. The code would detect that the path is blocked by the queen's row 4. Because to reach (1,6) from (2,3), the king would have to cross row4. For example, moving east from (2,3) to (3,4), but (3,4) is in the queen's row? No, a_x=4. So (3,4) is row3, which is safe. Wait, perhaps the problem is that the queen's row is in the middle, and the king is in a region that's separated from the target by the queen's row.

In sample 2, the queen's row is 4. The king starts at (2,3), which is in row2. The target is (1,6) in row1. So perhaps the path can go around the row4. But wait, the queen's row is 4. So any cell in row4 is blocked. So to go from (2,3) to (1,6), the king can move through rows 1-3, columns ... So perhaps the code would find a path.

But according to the sample, the output is NO. So perhaps the code correctly finds that there's no path.

Wait, in the sample explanation, the queen watches the fourth rank (row4). So the king can't cross row4. But in this case, the start is in row2 and the target is in row1, so maybe there's another blocking.

Wait, perhaps the queen's column is 4. So any cell in column4 is blocked. The king's start is (2,3) (column3), target (1,6) (column6). To get from 3 to 6, the king might need to pass through columns 4 or 5. But if column4 is blocked, then the king can't cross it.

So (1,6) is in column6. The king is in column3. To reach column6, he has to move through columns 4 or 5. But column4 is blocked. So moving east from (2,3) to (2,4) is blocked. So he can't get to column4. So how can he reach column6?

Alternative path: move north to (1,3), then east to (1,4) (blocked). So can't. So maybe the king can go south to (3,3), then east to (3,4) (blocked). So stuck. So the path is blocked. Hence, output NO.

So the code would correctly return NO for sample 2.

So the code works.

Thus, the code should handle all the sample cases correctly.

Now, considering memory constraints. The visited array is a 2D list of size (n+1)x(n+1). For n=1000, that's 1001x1001 booleans. Each boolean in Python takes about 28 bytes (if stored as a list of lists of booleans, but in practice, a list of lists uses a lot more memory). Wait, no: in Python, each element in a list is a reference, and for a list of booleans, each element is a separate Python bool object, which takes up more space. However, for n=1000, 1001*1001= 1,002,001 elements. Each boolean in Python takes 28 bytes (as per some references), but that's way more than the memory limit. Wait, this would be 1e6 * 28 bytes = 28MB. But the memory limit is 256MB. So this is acceptable.

Alternatively, perhaps using a more memory-efficient structure, like a bitmask. But for Python, it's easier to use a list of lists. However, in practice, for Python, using a list of lists of booleans for 1000x1000 is manageable. So the code should pass.

Another optimization is to precompute the attack conditions for each cell during BFS, but the current approach checks each cell on the fly, which is O(1) per check and thus efficient.

So the code should be correct and efficient.
</think>

```python
import sys
from collections import deque

n = int(sys.stdin.readline())
a_x, a_y = map(int, sys.stdin.readline().split())
b_x, b_y = map(int, sys.stdin.readline().split())
c_x, c_y = map(int, sys.stdin.readline().split())

visited = [[False] * (n + 1) for _ in range(n + 1)]
queue = deque()
queue.append((b_x, b_y))
visited[b_x][b_y] = True

directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),           (0, 1),
              (1, -1),  (1, 0), (1, 1)]

found = False

while queue:
    x, y = queue.popleft()
    if x == c_x and y == c_y:
        found = True
        break
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 1 <= nx <= n and 1 <= ny <= n:
            if nx == a_x or ny == a_y:
                continue
            if (nx - a_x) == (ny - a_y):
                continue
            if (nx + ny) == (a_x + a_y):
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

print("YES" if found else "NO")
```