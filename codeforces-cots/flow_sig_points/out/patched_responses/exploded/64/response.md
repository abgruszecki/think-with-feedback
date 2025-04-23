<think>
Okay, let's see. The problem is to find the number of valid grids that satisfy the given r and c arrays. The constraints are h and w up to 1e3, which means that any O(hw) solution should be manageable. But how do I model this?

So, each row i must start with exactly r_i consecutive full cells. Similarly, each column j starts with c_j consecutive full cells. The rest of the cells can be anything, but they must not affect the r and c values. Wait, no. Because the r_i is the number of full cells connected to the left. So for a row i, the first r_i cells must be full. But the (r_i +1)-th cell must be empty (if r_i < w), otherwise the row is all full. Similarly for columns.

Wait, the definition says "consecutive full cells connected to the left side". So if the first cell is empty, r_i is 0. Otherwise, the first r_i cells are all full, and the cell at position r_i +1 (if it exists) must be empty. Because otherwise, the count would be higher. So for each row i, the first r_i cells are full. Then, if r_i < w, the cell (i, r_i+1) must be empty. The rest of the cells (after r_i+1) can be anything, but they don't affect the r_i value. Similarly for columns.

So the grid must satisfy:

For row i:

- Cells (i,1) to (i, r_i) must be filled.

- If r_i < w, then cell (i, r_i + 1) must be empty.

Similarly for columns:

For column j:

- Cells (1,j) to (c_j, j) must be filled.

- If c_j < h, then cell (c_j +1, j) must be empty.

But these conditions might conflict. So the problem is to check for all possible cells where the row and column constraints overlap and see if they agree. If any conflict exists, the answer is 0. Otherwise, the remaining cells (those not determined by the constraints) can be filled in 2^k ways, where k is the number of such cells.

Wait, no. The cells that are not determined by the row and column constraints are the ones that are after the r_i+1 in their row (if any), and after the c_j+1 in their column (if any). But some of these cells might be determined by both row and column. Wait, no. Because the row constraints fix the first r_i cells. The column constraints fix the first c_j cells. But a cell (i,j) could be in the first r_i of its row, or in the first c_j of its column, or both. So for each cell (i,j), we need to check whether it is covered by the row's or column's constraints, and see if all those constraints are compatible.

Alternatively, perhaps the problem can be modeled as follows:

Each cell (i,j) has a state that is determined by the row and column constraints.

For row i:

- If j <= r_i: must be 1 (filled).

- If j == r_i + 1: if r_i < w, must be 0 (empty).

For column j:

- If i <= c_j: must be 1.

- If i == c_j + 1: if c_j < h, must be 0.

So for a cell (i,j), check all the applicable conditions. If any of the conditions for the cell are contradictory (e.g., must be 1 from row and 0 from column), then it's impossible. Otherwise, if the cell's value is not determined by any constraints, then it's a free cell that can be 0 or 1, contributing a factor of 2 to the answer.

So the approach is:

1. For each cell (i,j), check the row and column constraints. If they conflict, answer is 0.

2. Otherwise, count the number of cells that are not determined by any constraints. The answer is 2^(number of such cells) modulo 1e9+7.

But wait, the cells that are determined by the row or column constraints must be checked for compatibility. For example, a cell (i,j) might be required to be 1 by the row (j <= r_i) and 0 by the column (i > c_j but i == c_j +1). Then, if the cell is required to be 1 and 0 at the same time, the answer is 0.

So the steps are:

- For each cell (i,j), determine if the row's constraints and column's constraints for that cell are compatible.

If any cell has conflicting constraints, the answer is 0.

Otherwise, compute the number of cells that are not constrained by either row or column. Each such cell can be 0 or 1, leading to 2^k possibilities.

So first, let's model the constraints for each cell.

For cell (i,j):

Row constraints:

If r_i >= j: cell must be 1.

If r_i +1 == j and j <= w: cell must be 0.

Otherwise, row doesn't impose any constraint on this cell.

Similarly for column constraints:

If c_j >= i: cell must be 1.

If c_j +1 == i and i <= h: cell must be 0.

Otherwise, column doesn't impose any constraint.

So for cell (i,j):

Check all four conditions (from row and column) and see if they are compatible.

Wait, but the conditions may overlap. For example, if the row says the cell must be 1 and the column says it must be 1: that's compatible.

But if the row says 1 and the column says 0: conflict.

So the algorithm is:

Initialize answer as 1.

For each cell (i,j):

Check the row and column constraints for this cell.

If both constraints require the cell to be 1 or 0, check if they are the same. If not, answer is 0.

If one constraint requires a certain value and the other has no constraints, then the cell is fixed to that value.

If both have no constraints, then the cell is free (contributes a factor of 2 to the answer).

Wait, no. Let me think again.

The row may impose a value on the cell, and the column may impose a value. If they are the same, it's okay. If different, it's invalid. If one imposes and the other doesn't, then the cell is fixed to the imposed value. If neither imposes, then the cell is free.

Wait, no. For example, for a cell (i,j):

If the row's r_i is 3, and j is 2. Then the cell (i,2) is part of the first 3 cells, so must be 1. So the row imposes that it must be 1.

The column's c_j is 1, so for cell (i=2, j=2), the column's condition is if i <= c_j (1), so if i is 2, then 2 >1, so column's condition is only that cell (1+1=2, j) must be 0 if c_j < h. Assuming h >=2, then c_j is 1 < h. So cell (2, j) must be 0.

But if row's r_i is 3 (so cell (2,j) is j=2, which is <=3, must be 1). But column j=2's c_j=1. So cell (i=2,j=2) must be 0 according to column, but 1 according to row. Conflict, so answer is 0.

So each cell can have at most one constraint (row or column) imposing a value. If both impose, they must agree.

So the approach is:

For each cell (i,j):

Check row's condition and column's condition.

Let row_val be the value imposed by row (if any).

Let col_val be the value imposed by column (if any).

If row_val and col_val are both not None and row_val != col_val, then answer is 0.

If one is not None and the other is None, then the cell must be set to the non-None value. No problem.

If both are None, then the cell is free.

So the steps are:

1. Iterate over all cells (i,j).

2. For each cell, compute row_val and col_val.

   a. row_val: 

      if j <= r_i: must be 1.

      elif j == r_i +1 and r_i < w: must be 0.

      else: None (no constraint from row).

   b. col_val:

      if i <= c_j: must be 1.

      elif i == c_j +1 and c_j < h: must be 0.

      else: None (no constraint from column).

3. Check if row_val and col_val conflict. If yes, return 0.

4. Otherwise, if both row_val and col_val are None, then this cell is free, contributing a multiplier of 2.

5. Else, the cell's value is determined by whichever is not None. No contribution to the multiplier.

So the total number of free cells is the number of cells where both row and column don't impose any constraints.

The answer is 2^(free_cells) mod MOD.

But how to compute row_val and col_val for each cell?

We need to process all h*w cells. For h and w up to 1e3, h*w is up to 1e6, which is manageable.

So the plan is:

Loop over each i from 0 to h-1 (assuming 0-based or 1-based?), and each j from 0 to w-1.

Wait, the problem uses 1-based indices for rows and columns. So rows 1..h and columns 1..w.

So for each cell (i,j) in 1..h and 1..w.

So, for row i:

r_i is given. So for cell (i,j):

If j <= r_i: row_val is 1.

Else if j == r_i +1 and r_i < w: row_val is 0.

Else: row_val is None.

Wait, but r_i can't be larger than w. Because according to the problem statement, r_i is the number of consecutive full cells in the row. So the maximum possible r_i is w (all cells filled). If j is up to w, then j can be equal to r_i, but if r_i is w, then j can be up to w, so r_i+1 would be w+1, which is beyond the grid. So in that case, the row_val is 1 for all j in 1..w.

Similarly for column j's c_j: if c_j is h, then all cells in the column are 1. Else, the cell at (c_j+1, j) must be 0.

So how to compute row_val and col_val for each cell (i,j):

Row part:

row_r = r[i-1] (since input is 0-based list for the second line, but the rows are 1-based in the problem's variables). Wait, the input is given as h integers r_1 to r_h. So for Python, when read as a list, the first element is r_1, which is the first row. So for row i (1-based), r[i-1] gives the value of r_i.

Similarly for c_j: input is w integers, so for column j (1-based), c[j-1] is the value of c_j.

So for cell (i,j):

Row constraints:

if j <= r_i: (since r_i is the number of consecutive full cells starting at the left). So if j is <= r_i, then cell must be 1.

Else, if j == r_i + 1 and r_i < w: cell must be 0.

Else: no constraint from the row.

Similarly for column constraints:

if i <= c_j: cell must be 1.

Else, if i == c_j +1 and c_j < h: cell must be 0.

Else: no constraint from column.

So for each cell (i,j), compute row_val and col_val.

Now, how to handle the possible cases:

Case 1: row_val is not None and col_val is not None. Then, they must be equal. If not, answer is 0.

Case 2: row_val is not None, col_val is None. So the cell is set to row_val. No problem.

Case 3: col_val is not None, row_val is None. So cell set to col_val.

Case 4: both None. Then cell is free.

So the steps are:

Initialize free = 0.

For each i from 1 to h:

   for each j from 1 to w:

      compute row_val and col_val.

      if row_val and col_val are not None and row_val != col_val:

          return 0

      elif row_val is not None:

          check if col_val is not None and col_val != row_val → handled above.

          else, no problem. cell is fixed to row_val.

      elif col_val is not None:

          cell is fixed to col_val.

      else:

          free +=1

So, after processing all cells, the answer is 2^free mod 1e9+7.

But wait, how to compute row_val and col_val properly?

Let's code this.

For row i (1-based):

r_i = r_list[i-1]

So, for cell (i,j):

row_val = None

if j <= r_i:

    row_val = 1

elif r_i < w and j == r_i +1:

    row_val = 0

Else:

    row_val is None.

Similarly for column j:

c_j = c_list[j-1]

if i <= c_j:

    col_val = 1

elif c_j < h and i == c_j +1:

    col_val = 0

Else:

    col_val is None.

So now, for each cell (i,j), compute these two values.

Check for conflicts.

If any cell has row_val and col_val both not None and different, then answer is 0.

Now, the problem also has to check if the r_i and c_j are valid. For example, if r_i is larger than w, then the row cannot be satisfied. Because the row has only w cells. So if r_i > w, then it's impossible.

Wait, the problem's input constraints for r_i are 0 ≤ r_i ≤ w. So we can assume that the input is correct. So the code does not need to check this.

Wait, according to the problem statement:

Input for the second line contains h integers r_1 ... r_h (0 ≤ r_i ≤ w). So each r_i is between 0 and w.

Similarly for c_j: 0 ≤ c_j ≤ h.

So the code can assume that all r_i and c_j are valid. So for example, r_i can be up to w. If r_i is w, then for any j in 1..w, j <= r_i (since r_i =w). So all cells in the row are 1. The next cell (w+1) is beyond the grid, so no constraint.

So in code, we can safely process.

So the code steps:

Read h, w.

Read r list: h integers.

Read c list: w integers.

Initialize free =0.

For each i in 1..h:

   for j in 1..w:

      compute row_val.

      compute col_val.

      if row_val is not None and col_val is not None and row_val != col_val:

          print(0)

          exit.

      elif row_val is not None and col_val is not None and row_val == col_val:

          continue. (no problem)

      else:

          if row_val is None and col_val is None:

              free +=1

          else:

              # one is not None, but no conflict.

              pass.

So the code needs to process each cell, check for conflict, and count the free cells.

But how to loop through i and j? For h and w up to 1e3, this is O(1e6) steps, which is acceptable.

Once all cells are checked, the answer is pow(2, free, MOD).

But we need to compute this modulo 1e9+7.

But wait, are there any other cases where the answer is 0?

Yes. For example, if the row's r_i is 3, but in that row, the cell (i,3) is supposed to be 1. But the column's constraint for (i,3) may require it to be 0. Then that's a conflict.

But the code checks for all cells.

Another example: the row's r_i is 3, but the cell (i,3) is required by column j=3's constraints to be 0. So conflict.

So the code checks all possible cell conflicts.

So that's the plan.

Now, code:

Read h, w.

r = list of h integers.

c = list of w integers.

MOD = 10**9 +7.

free =0

for i in 1 to h:

   for j in 1 to w:

      # compute row_val

      ri = r[i-1]

      if j <= ri:

          r_val = 1

      elif ri < w and j == ri +1:

          r_val =0

      else:

          r_val = None

      # compute column_val

      cj = c[j-1]

      if i <= cj:

          c_val =1

      elif cj < h and i == cj +1:

          c_val =0

      else:

          c_val = None

      # check conflict

      if (r_val is not None) and (c_val is not None):

          if r_val != c_val:

              print(0)

              exit()

      # if no conflict, check if free.

      if r_val is None and c_val is None:

          free +=1

So after all cells are processed, the answer is 2^free mod MOD.

But wait, in Python, pow(2, free, MOD) is efficient even for large exponents.

So the code would be:

Read h, w.

r = list(map(int, input().split())) → but second line is r list.

Wait, input first line is h and w.

Second line is h integers: r_1 ... r_h.

Third line is w integers: c_1 ... c_w.

So code:

h, w = map(int, input().split())

r = list(map(int, input().split()))

c = list(map(int, input().split()))

MOD = 10**9 +7

free = 0

for i in range(1, h+1):

    for j in range(1, w+1):

        # compute row_val for cell (i,j)

        ri = r[i-1]

        if j <= ri:

            r_val = 1

        else:

            if ri < w and j == ri +1:

                r_val = 0

            else:

                r_val = None

        # compute column_val

        cj = c[j-1]

        if i <= cj:

            c_val = 1

        else:

            if cj < h and i == cj +1:

                c_val = 0

            else:

                c_val = None

        # check conflict

        if r_val is not None and c_val is not None:

            if r_val != c_val:

                print(0)

                exit()

        # count free cells

        if r_val is None and c_val is None:

            free +=1

print(pow(2, free, MOD))

Wait, but in Python, exiting the code with exit() may not be straightforward. So perhaps, after checking all cells, we can compute the answer. But how to check for conflicts during the loop.

Wait, during the loop, once any cell has a conflict, the answer is 0. So in that case, the code can print 0 and exit immediately. Otherwise, proceed to compute the answer.

But in the code above, as soon as a conflict is found, print 0 and exit. So that's correct.

But in Python, how to exit. The code uses exit(), which is equivalent to sys.exit(). But to use exit(), we need to import sys, or perhaps in some environments, it's allowed. Wait, in Python, 'exit()' is a function in the sys module. So to use exit(), we need to import sys and call sys.exit(). Otherwise, using exit() would raise a NameError.

So the code needs to import sys and call sys.exit().

So code should be modified:

import sys

h, w = map(int, input().split())

r = list(map(int, input().split()))

c = list(map(int, input().split()))

MOD = 10**9 +7

free = 0

for i in range(1, h+1):

    for j in range(1, w+1):

        ri = r[i-1]

        if j <= ri:

            r_val = 1

        else:

            if ri < w and j == ri +1:

                r_val = 0

            else:

                r_val = None

        cj = c[j-1]

        if i <= cj:

            c_val = 1

        else:

            if cj < h and i == cj +1:

                c_val = 0

            else:

                c_val = None

        if r_val is not None and c_val is not None:

            if r_val != c_val:

                print(0)

                sys.exit()

        if r_val is None and c_val is None:

            free +=1

print(pow(2, free, MOD))

But wait, in the code above, the loops are in 1-based indices. For example, i ranges from 1 to h inclusive. j ranges from 1 to w inclusive. For each i and j, the code accesses r[i-1] and c[j-1], which is correct because the lists are 0-based.

Testing the first sample input:

Sample input 1:

3 4

0 3 1

0 2 3 0

So h=3, w=4.

r = [0, 3, 1]

c = [0,2,3,0]

Let's process each cell.

For cell (1,1):

i=1, j=1.

ri = 0.

j=1 <= ri (0): No. So else. ri is 0 <4? yes. j=0+1=1? yes. So r_val is 0.

cj is c[0] =0.

i=1 <=0? No. So else. cj=0 <3? yes. i=0+1=1. So c_val=0.

So r_val and c_val are 0 and 0. No conflict. Not free. So no.

Other cells:

Let me think about row i=2, j=1.

ri=3.

j=1 <=3: yes. r_val=1.

cj is c[0] (j=1 is first column, cj is 0).

i=2 <=0? No. cj=0 <3 (h=3). i=0+1=1? 2 is not 1. So c_val is None.

So row_val is 1, col_val is None. So cell must be 1. No problem.

No conflict. Not free.

Another example: cell (2,2).

i=2, j=2.

ri=3. j=2 <=3 → r_val=1.

cj = c[1] (j=2-1=1? Wait, j runs from 1 to 4. So for j=2, c[j-1] is c[1]. In the sample input, c is [0,2,3,0].

So for j=2, cj is 2.

i=2 <=2 → yes. So column_val is 1.

So r_val=1, c_val=1. No conflict.

Another cell (2,4).

i=2, j=4.

ri=3. j=4 <=3 → no. ri is 3 <4? yes. j=3+1=4? yes. So r_val=0.

cj is c[3] (j=4 → index 3) which is 0.

i=2 <=0? No. cj=0 <3 → yes. i=0+1=1 → 2 !=1. So column_val is None.

So row_val is 0, column_val is None. So cell is 0. No problem.

Another cell (3,3):

i=3, j=3.

ri=1. j=3 >1. ri <4 (w=4) → j=1+1=2. Not equal to j=3. So r_val is None.

cj is c[2] (j=3 → index 2). c[2] is 3.

i=3 <=3 → yes. So column_val is 1.

So row_val is None, column_val is 1. So cell must be 1. No conflict.

So the code would process all cells. For the sample input, how many free cells?

Let's see.

In the first sample, the output is 2, so free must be 1. Wait, but according to the sample, the other possible case contributes 1, but maybe in the sample there's one free cell. Wait, 2^1=2, which matches the sample's answer.

So let's see:

In the first sample, what cells are free?

The grid after the constraints is:

Row 1 (r_i=0):

j=1 must be 0 (since r_i=0 <4 → j=1=0+1 → 0. So cell (1,1) is 0.

Row 2 (r_i=3): cells 1-3 are 1, cell 4 must be 0.

Row 3 (r_i=1): cells 1 is 1, cell 2 must be 0.

Columns:

Column 1 (c_j=0): cell 1 must be 0 (since c_j=0 <3 → cell 1 is 0+1=1 → cell (1,1) is 0.

Column 2 (c_j=2): cells 1-2 must be 1, cell 3 must be 0.

Column 3 (c_j=3): cells 1-3 must be 1 (since h=3, which is equal to c_j=3. So no cell after that.

Column4 (c_j=0): cell 1 must be 0.

So after applying all constraints, the cells determined are:

For row 1:

cell (1,1)=0.

For row 2:

cells 1-3=1, cell4=0.

Row3:

cell1=1, cell2=0.

For columns:

Column2:

cells1-2=1, cell3=0.

Column3: cells1-3=1.

So overlapping constraints:

Looking for cells not determined by row or column.

For example, cell (3,3):

Row3's r_i=1. j=3>1. r_i+1=2 <4? yes. j=2 is 2, but j=3 is not. So row has no constraint here.

Column3's c_j=3. i=3 <=3 → yes. So column requires 1. So cell (3,3) is 1.

So that's determined by column.

Another example: cell (3,4).

Row3: j=4. r_i=1. 4>1. r_i+1=2. j=4 !=2. So no row constraint.

Column4: c_j=0. i=3. i <=0? no. c_j=0 <3. i=0+1=1? i=3 !=1. So column has no constraint. So this cell is free.

So cell (3,4) is free.

So in the first sample, how many free cells?

Looking for cells where both row and column have no constraints.

For example:

Row1: only cell (1,1) is 0. The rest (j=2-4) are not in row's constraints. But let's check column constraints.

For cell (1,2):

row1's r_i=0 <4 → j=1 is 0+1=1. cell (1,2) is j=2. So row has no constraint here.

Column2: c_j=2. i=1 <=2 → yes. So cell (1,2) must be 1. So column imposes 1. So this cell is not free.

Another example: cell (3,4):

row has no constraint, column has no constraint → free.

Another cell (3,3): column requires 1. So not free.

Other cells:

Let's see:

Cell (2,3):

Row2: j=3 <=3 → 1. So row requires 1. Column3: i=2 <=3 → 1. So both require 1. No conflict. Not free.

Cell (3,2):

Row3: j=2. r_i=1. j=2 is 1+1=2, and r_i <4. So row_val is 0. Column j=2: c_j=2. i=3. i <=2? No. c_j=2 <3 → yes. i=2+1=3 → cell (3,2) must be 0. So row and column agree. So no conflict. Not free.

So the only free cell in the first sample is cell (3,4), and perhaps cell (3,4) and (3,3) ?

Wait, cell (3,3) is determined by column3 (i=3 <=3 → 1). So not free.

Cell (3,4):

row3's r_i=1. j=4 is >1. r_i+1=2 <4. j=4 is not 2. So row has no constraint. column4: i=3, c_j=0. i=3>0. c_j <3 → yes. i=0+1=1. 3 !=1. So column has no constraint. So cell is free.

So free is 1. 2^1=2. Which matches the sample.

So code works for sample 1.

Sample 2:

Input:

1 1

0

1

h=1, w=1.

r is [0], c is [1].

Process cell (1,1):

row_val: j=1 <=0? No. r_i=0 <1? Yes. j=0+1=1. So row_val=0.

column_val: i=1 <=1 → yes. c_j=1. So column_val=1.

row_val and column_val are 0 and 1. Conflict → answer 0.

Sample3:

The output is a modulo answer. So code would handle that.

Thus, the code should be correct.
</think>

```python
import sys

MOD = 10**9 + 7

h, w = map(int, sys.stdin.readline().split())
r = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

free = 0

for i in range(1, h + 1):
    for j in range(1, w + 1):
        # Calculate row value constraints
        ri = r[i - 1]
        if j <= ri:
            row_val = 1
        else:
            if ri < w and j == ri + 1:
                row_val = 0
            else:
                row_val = None
        
        # Calculate column value constraints
        cj = c[j - 1]
        if i <= cj:
            col_val = 1
        else:
            if cj < h and i == cj + 1:
                col_val = 0
            else:
                col_val = None
        
        # Check for conflict
        if row_val is not None and col_val is not None:
            if row_val != col_val:
                print(0)
                sys.exit()
        
        # Count free cells
        if row_val is None and col_val is None:
            free += 1

print(pow(2, free, MOD))
```