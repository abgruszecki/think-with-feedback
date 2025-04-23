<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

The task is to determine the number of disconnected wall segments in a grid. A wall segment is formed by consecutive non-empty columns. So, if there are columns with bricks (B) next to each other, they form a single segment. But if there's an empty column between them, that splits into separate segments.

So, the approach is to check each column in order (from left to right, column 1 to C). For each column, determine if it's non-empty (has at least one B). Then, consecutive non-empty columns form a single segment. Whenever we encounter a column that's non-empty but the previous was empty, that's the start of a new segment.

Wait, right. Because segments are groups of consecutive columns that are all non-empty. So, if column i is non-empty, and column i-1 is empty, then this is the start of a new segment. Then, any consecutive non-empty columns after that belong to the same segment until we hit an empty column again.

So the steps are:

1. For each column, check if it's non-empty. How? For each column c, look through all the rows. If any of the rows in column c has a 'B', then the column is non-empty.

2. Then, iterate through all columns from left to right. Keep track of whether the previous column was part of a segment. When the current column is non-empty and the previous was empty, increment the count. Also, if the current column is non-empty and the previous was part of the same segment (i.e., consecutive), do not increment. But if after some empty columns, a new non-empty column starts, that's a new segment.

So the algorithm is:

Initialize count to 0. Keep a flag to track if we are in a segment. Initially false. Then, for each column in order:

- Check if column is non-empty (has at least one B).
- If yes:
   - If previous column was not in a segment (either because it was the first column, or the previous was empty), then this is a new segment. Increment count. Mark in_segment as True.
   - Else, continue (part of the same segment).
- If no:
   - Mark in_segment as False.

So the key is to process each column, check if it's non-empty, and count transitions from empty to non-empty.

So how to check if a column is non-empty? For each column c, loop through all rows r from 0 to R-1, and check if any of the cells in that column is 'B'.

Wait, the input is given as R lines. Each line represents the rows. But the description says: each of the R lines has a string of length C. The c-th character of line r is B if there's a brick in column c and row R - r + 1. Wait, that's a bit confusing. Let me parse that.

So, the input lines are R lines. The first line (input line 2) corresponds to row R (since the first line after R and C is row R - r + 1 when r is 1. So for r starting from 1 to R, the row in the grid is R - r + 1. Wait, maybe not. Let's think:

The input's next R lines describe the columns. The c-th character of line r (input line 2 + r-1) is B if there is a brick in column c and row R - r + 1. Wait, for example, in the first sample input:

3 7

Then the next 3 lines:

.......
.......
.BB.B..

So R is 3. So line 1 (the third input line) corresponds to row 3 - 1 +1 = 3. Wait, no. Let's see:

The first line after R and C is r=1. So row is R - r + 1 = 3 -1 +1 =3. Then the second line (r=2) is row 3-2+1=2. The third line (r=3) is row 3-3+1=1. So the rows in the actual grid are 1, 2, 3. But the input lines are given in reverse order. So for the first sample input, the third line (r=3) is the first row (row 1) of the wall. So the wall has 3 rows, with row 1 being the bottom row (since the bricks are placed on the ground or on top of another brick).

But to check if a column is non-empty, we need to check if there's any 'B' in any row of that column. So for each column c (from 0 to C-1?), iterate through all rows (from 0 to R-1?), but the way the data is stored, perhaps each row in the input is a string. Wait, perhaps the code will read each input line as a string, and for each column c in 0..C-1, check if any of the rows (strings) at position c is 'B'.

Wait, for example, the first sample input's third line is ".BB.B..", which is the row 1 (bottom row). So in the actual grid, column 0 (if columns are 0-based) in row 1 is '.', column 1 is 'B', etc. So for each column c, if any of the R input lines has a 'B' at position c, then the column is non-empty.

Wait, no. Because each input line represents a different row. So for column c, if in any of the R input lines, the character at position c is 'B', then that column has at least one brick. Because each brick in any row of the column contributes to the column being non-empty.

Wait, yes. Because the problem says that a column is non-empty if it has any bricks. So regardless of which row the brick is in, the column is non-empty.

So for each column c, check if any of the R input lines (rows) has a 'B' at position c.

So the steps are:

Read R and C.

Read R lines, each of length C. For each line, store it as a string. Then, for each column c (0-based?), check if any of the R lines has 'B' at position c.

But in Python, we can process each column by checking each row's c-th character.

Once we have for each column whether it's non-empty (a list of booleans), then iterate through the columns left to right. Each time a column is non-empty and the previous was not, increment the count.

So, first, create a list of which columns are non-empty.

Then, process that list to count the number of consecutive groups.

So, code outline:

Read R and C.

Then read R lines. For each line, it's a string. Let's collect these lines in a list called grid.

Then, for each column c (from 0 to C-1):

non_empty = any( grid[r][c] == 'B' for r in range(R) )

So for each column c, check all R rows.

Then, iterate through columns 0 to C-1:

Initialize count = 0

prev_empty = True

for c in 0 to C-1:

   if current column is non_empty:

      if prev_empty:

          count +=1

          prev_empty = False

      else:

          continue

   else:

      prev_empty = True

So this way, every time a non-empty column is found where the previous was empty (or first column), it's a new segment.

This should correctly count the number of segments.

So the main steps are:

1. Determine for each column if it is non-empty.

2. Iterate through these columns, counting transitions from empty to non-empty.

Now, let's think about the example.

First sample input:

3 7

The next 3 lines are:

.......
.......
.BB.B..

Wait, the third line (input line after R and C is the third line here) is ".BB.B..", which has B's in columns 1, 2, 4 (0-based). So the columns with B's are 1, 2, 4. Then, when processing these columns:

columns 0: empty

columns 1: non-empty (since at least one B in any row). So the first sample's columns 1, 2 are non-empty (consecutive) and 4 is non-empty but there's an empty column (3) before. So the count is 2.

So the code would correctly count that.

Another example: input 4 has 1x1 grid with B. So one segment.

So the code seems correct.

Now, how to implement this efficiently.

Constraints: R and C up to 100. So total elements are 100*100=10,000. So even in worst case, this is manageable.

So the code can be:

Read R, C.

Read R lines, store in a list grid.

non_empty_columns = [False] * C

for c in 0 to C-1:

   for r in 0 to R-1:

       if grid[r][c] == 'B':

           non_empty_columns[c] = True

           break

Then, iterate through non_empty_columns and count the number of groups.

So in code:

count = 0

prev = False

for c in range(C):

    current = non_empty_columns[c]

    if current:

        if not prev:

            count +=1

        prev = True

    else:

        prev = False

print(count)

Yes.

Now, let's test this logic against the first sample.

Sample 1:

non_empty_columns is:

columns 0: no.

1: yes.

2: yes.

3: no.

4: yes.

5: no.

6: no.

So processing these:

c=0: no. prev becomes False.

c=1: yes. prev was False, count becomes 1. prev is True.

c=2: yes. prev is True. No change.

c=3: no. prev becomes False.

c=4: yes. prev was False. count becomes 2. prev is True.

c=5: no.

c=6: no.

Total 2. Correct.

Another sample: input 4, 1x1 B. So non_empty_columns[0] is True. So count is 1. Correct.

Another case: all empty columns. Output 0.

Another case: all columns non-empty. Then count is 1.

So this logic works.

So the code seems correct.

Now, coding this in Python.

Read R and C. Then read R lines. Then process each column.

In Python, for each line, grid.append(input().strip())

Then for each c in 0 to C-1:

Check if any grid[r][c] is 'B'.

But in Python, grid is a list of strings. So for each column c, iterate through each row r, check grid[r][c].

So for the code:

R, C = map(int, input().split())

grid = [input().strip() for _ in range(R)]

non_empty = [False] * C

for c in range(C):

    for r in range(R):

        if grid[r][c] == 'B':

            non_empty[c] = True

            break

count = 0

prev = False

for curr in non_empty:

    if curr:

        if not prev:

            count +=1

        prev = True

    else:

        prev = False

print(count)

Yes.

This should handle all cases.

Let's test against the first sample input.

Sample 1:

R=3, C=7.

grid lines are:

Line 0: ....... (all dots)

Line 1: ....... (all dots)

Line 2: .BB.B.. (so the third line in input is ".BB.B..")

So for column 0:

Check grid[0][0] is '.', grid[1][0] is '.', grid[2][0] is '.', so non_empty[0] is False.

Column 1:

grid[0][1] is '.', grid[1][1] is '.', grid[2][1] is 'B' → non_empty[1] is True.

Similarly column 2: grid[2][2] is 'B' → True.

Column 3: grid[2][3] is '.'; all others in column 3 are '.' → False.

Column 4: grid[2][4] is 'B' → True.

So non_empty is [F, T, T, F, T, F, F].

Processing: each T where previous is F increments the count. So first T (index 1) → count 1. Then next T (index 2) is part of same. Then F (index3). Then T (index4) → count 2. So output is 2. Correct.

So the code works.

Another sample: input 8 8 case. The code should correctly count 2.

Thus, this approach is correct.
</think>

```python
R, C = map(int, input().split())
grid = [input().strip() for _ in range(R)]
non_empty = [any(grid[r][c] == 'B' for r in range(R)) for c in range(C)]
count = 0
prev = False
for curr in non_empty:
    if curr:
        if not prev:
            count += 1
        prev = True
    else:
        prev = False
print(count)
```