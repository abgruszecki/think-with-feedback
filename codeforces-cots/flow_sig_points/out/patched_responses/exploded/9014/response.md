<think>
Okay, so I need to solve this problem where Pearlo has to check if the password entered is symmetric with respect to the center of the 3x3 keypad. The input is a 3x3 grid where X represents a pressed button and . not pressed. The password consists of distinct digits (so each X is a unique digit). The question is whether the pattern of Xs is symmetric around the center.

Let me think about what central symmetry means here. Central symmetry here would imply that for every X in position (i,j), there must be an X in the position that's symmetric to it relative to the center. The center of the 3x3 grid is (2,2) if we consider rows and columns starting at 1, but wait, indexing in code might start from 0. Wait, the grid is 3x3, so the positions are (0,0) to (2,2). The center would be at (1,1), right? So the symmetric point of any (i,j) is (2-i, 2-j). Because the center is (1,1), the reflection would be such that the center is the midpoint. For example, for (0,0), the symmetric point would be (2,2). For (0,1), symmetric is (2,1). For (0,2), symmetric is (2,0). Similarly for (1,0), it's (1,2), and so on.

So the algorithm would be: check for every cell (i,j) in the grid, if the cell contains an X, then its symmetric counterpart (2-i, 2-j) must also contain an X. If this is true for all Xs, then the pattern is symmetric, so output YES. Otherwise, output NO.

But wait, what about the case where an X is at the center? Because the symmetric point of the center is itself. So the center must have an X if it's part of the password, but since the password consists of distinct digits, the center can't be in the password more than once. But since the problem says the password has distinct digits, each X represents a distinct digit. So in the grid, each X is a unique digit, but the symmetry requires that each X's symmetric counterpart is also present. However, the center is its own symmetric point, so if it's pressed (i.e., has an X), then there's no problem because its symmetric counterpart is itself. So the center can be part of the password, but it's allowed as long as the X is present.

So the steps to solve the problem are:

1. Read the 3x3 grid.
2. For each cell (i,j) in the grid:
   a. If the cell is X, check that the cell (2-i, 2-j) is also X.
   b. If any X does not have its symmetric counterpart, output NO.
3. If all Xs have their symmetric counterparts, output YES.

Wait, but how do we avoid checking each pair twice? Like, when we check (i,j) and then (2-i, 2-j), which is the same as the original cell's symmetric. So for example, checking (0,0) and (2,2) would check each other. If we process all cells, this would check each pair twice, except for the center. So perhaps the approach is to check all cells, but once. But in code, perhaps we can iterate through all cells and for each X, check if the symmetric cell is also X. But if we check all cells, including when we process the symmetric cell, then we might get redundant checks. However, even if we process all cells, as long as any X fails the check, we can return NO.

Alternatively, perhaps a better approach is to check each cell once, and for each cell (i,j), if it's an X, check that its symmetric (2-i, 2-j) is also X. But this could lead to checking the same pair twice. For example, (0,0) and (2,2) would each check the other. But in code, even if both are checked, the first time (0,0) is X, we check (2,2) is X. Then when processing (2,2) as X, check (0,0) is X. But if all cells are properly symmetric, this is redundant but correct. However, if in any case, the symmetric cell is not X, the code will immediately return NO.

But perhaps the code can process all cells, and for each X, check if the symmetric cell is also X. If any X's symmetric is not X, return NO. Otherwise, return YES.

But how to implement this efficiently.

Let's think about the sample input.

First sample input:

XX.
...
.XX

Which is:

Row 0: X X .
Row 1: . . .
Row 2: . X X

So the X positions are (0,0), (0,1), (2,1), (2,2). Let's check their symmetric positions.

For (0,0): symmetric is (2,2) → which is X. Good.
For (0,1): symmetric is (2,1) → which is X. Good.
For (2,1): symmetric is (0,1) → which is X. Good.
For (2,2): symmetric is (0,0) → which is X. So all are symmetric.

Hence output YES.

Second sample input:

X.X
X..
...

Row 0: X . X
Row 1: X . .
Row 2: . . .

X positions are (0,0), (0,2), (1,0).

Check (0,0) → symmetric (2,2) which is . → Not X. So this fails. Hence output NO.

So the algorithm needs to check for each X in the grid, whether its symmetric counterpart is also X.

So the code can be structured as follows:

Read the grid as a list of 3 strings.

For each i in 0..2, for each j in 0..2:

if grid[i][j] is 'X', then check if grid[2-i][2-j] is 'X'.

If any of these checks fail, output NO.

Else, output YES.

But how to avoid checking the same pair twice? For example, (0,0) and (2,2) are each other's symmetric. When i=0, j=0, check 2,2. Then when i=2, j=2, check 0,0. So both check each other. But if one is X and the other is not, then the first check will catch it and return NO.

So even if processing all cells, the code will work correctly.

So in code:

grid = [input().strip() for _ in range(3)]

for i in range(3):
    for j in range(3):
        if grid[i][j] == 'X':
            # find symmetric position
            ni = 2 - i
            nj = 2 - j
            if grid[ni][nj] != 'X':
                print("NO")
                exit()
print("YES")

Wait, but this approach has a problem. Suppose there's an X in (i,j) and the symmetric is not X. Then we immediately return NO. That's correct.

But what if the symmetric cell hasn't been checked yet? For example, suppose in the grid, (0,0) is X and (2,2) is not. Then when processing (0,0), it checks (2,2) and returns NO. That's correct. If (2,2) is X but (0,0) is not, then when (2,2) is processed, it checks (0,0) and returns NO.

But what if the code processes all cells, and in the case where (i,j) is X but (2-i,2-j) is not. Then even if (2-i,2-j) is not X, when processing (i,j), the code will catch it.

So this approach works.

But wait, what about the center cell? For example, if the center cell is X, then the symmetric cell is itself. So when processing (1,1), it checks itself. So if (1,1) is X, then code checks if (1,1) is X, which it is. So that's okay.

Another example: input where all X's are symmetric.

Another case: a single X in the center. Then code processes (1,1), checks (1,1) which is X. So returns YES.

Another case: X at (0,1) and (2,1). Then symmetric is correct. So code returns YES.

So the code seems to handle all cases.

So the code would read the 3 lines of input, process each cell. For each X in the cell, check the symmetric cell. If any X's symmetric is not X, output NO. Else, output YES.

This approach is O(1) time since there are only 9 cells to check. So for any input size, it's acceptable.

Now, let's test the code against the sample inputs.

First sample input:

XX.
...
.XX

The grid is:

Row 0: 'XX.' → indexes 0,0; 0,1; 0,2.

Row 1: '...'

Row 2: '.XX' → indexes 2,0 (.), 2,1 (X), 2,2 (X).

Processing each cell:

i=0, j=0: X. Check (2,2) which is X. Good.

i=0, j=1: X. Check (2,1) which is X. Good.

i=0, j=2: . → skip.

i=1, j=0: . → skip.

etc. For all Xs, their symmetric positions are X. So code returns YES.

Second sample input:

X.X
X..
...

Row 0: 'X.X' → 0,0 is X; 0,2 is X.

Row 1: 'X..' → 1,0 is X.

Row 2: '...' → all . 

Processing:

i=0, j=0 → X. Check (2,2) which is . → returns NO. So code outputs NO.

Yes.

Another test case: center cell is X.

Input:

...
.X.
...

Processing:

Only (1,1) is X. Check symmetric (1,1) which is X. So code returns YES.

Another test case: X at (0,0) and (2,2), but (0,0) is X and (2,2) is not. Then code checks (0,0) → check (2,2) is . → returns NO.

So code seems correct.

So the code is correct.

Now, the code must read input from standard input, output to standard output. Let's write the code.

Read three lines, each line is stripped of whitespace. Then loop through each cell. For each cell, if it's X, check the symmetric cell.

The code in Python:

grid = [input().strip() for _ in range(3)]

for i in range(3):
    for j in range(3):
        if grid[i][j] == 'X':
            ni = 2 - i
            nj = 2 - j
            if grid[ni][nj] != 'X':
                print("NO")
                exit()
print("YES")

Yes, that's the code. Let's see. For each cell, if it's X, check the symmetric. If any fails, output NO. Otherwise, output YES.

This should handle all cases correctly.
</think>

```python
grid = [input().strip() for _ in range(3)]
for i in range(3):
    for j in range(3):
        if grid[i][j] == 'X':
            ni, nj = 2 - i, 2 - j
            if grid[ni][nj] != 'X':
                print("NO")
                exit()
print("YES")
```