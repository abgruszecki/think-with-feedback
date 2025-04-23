<think>
Okay, so I need to solve this problem where I have to count the number of right triangles in a grid where all three vertices are asterisks. The right triangles must have two sides parallel to the square sides. Hmm, right, that means the right angle is at the point where the two parallel sides meet. So the triangles are axis-aligned right triangles.

Let me think. The right triangles here can be in two possible orientations. Either the right angle is at (x,y), and there are points (x, y1) and (x1, y), forming a vertical and horizontal line. Or maybe in other directions, but wait, the problem says two sides are parallel to the square sides. Oh right, so the triangle must have one leg along a row and another along a column. So the right angle is the corner where a row and column meet. So for each '*' cell, how many such triangles can it form as the right angle vertex?

So for a cell (i,j) that is a '*', the number of triangles with right angle here is equal to the number of '*'s in the same row (to the left and right of (i,j)) multiplied by the number of '*'s in the same column (above and below (i,j)). Because for each such pair of a star in the same row and a star in the same column, those three points form a right triangle.

Wait, for example, if in row i, there are a stars to the left of (i,j), and b stars to the right. Then the total in the row is (a + b). But when combined with stars in the column, for each star in the same row (either left or right) and each star in the same column (up or down), that gives a triangle. But maybe the count is (row_count) * (column_count), where row_count is the number of stars in the same row except the current cell, and column_count is the same for the column.

Wait, no. Let's think: suppose in row i, there are k stars. Then, excluding (i,j), there are (k-1) stars in the row. Similarly for the column. Then, for each star in the row, and each star in the column, we can form a triangle. Because the right angle is at (i,j), and the other two points are (i, y) and (x, j). So the triangle has vertices (i,j), (i,y), (x,j). So the count for (i,j) is (row_count) * (column_count), where row_count is the number of stars in row i (excluding (i,j)), and column_count is the number in column j (excluding (i,j)).

Wait, but the problem states that all three vertices must be '*' cells. So for each star at (i,j), the number of triangles where (i,j) is the right angle is (row_stars[i] - 1) * (col_stars[j] - 1). Because row_stars[i] is the total number of stars in row i. So subtract 1 for the current cell, then multiply by the same for column.

So the plan is:

1. Precompute for each row, the number of stars in that row.
2. Precompute for each column, the number of stars in that column.
3. For each cell (i,j) that is a star, add (row_counts[i] - 1) * (col_counts[j] - 1) to the total.

That's the main approach.

Wait, but let's test with the examples.

First example:

2 2

**

*.

The grid is:

Row 0: **
Row 1: *.

So row_stars for row 0 is 2, row 1 is 1.

Column_stars: column 0 has 2 stars (rows 0 and 1), column 1 has 1 (row 0, column 1).

So for each star:

Looking at (0,0): row_stars[0] -1 is 1. column_stars[0] -1 is 1. So 1*1 = 1.

(0,1): row_stars[0]-1 =1. column_stars[1]-1=0. So 0. So contributes 0.

(1,0): row_stars[1]-1=0. column_stars[0]-1=1. 0*1=0.

Total is 1, which matches the example.

Yes, that works.

Second example:

3 4

*..*

.**.

*.**

Let's parse the grid:

Row 0: *..* → stars at (0,0) and (0,3) → row_stars[0] = 2.

Row 1: .** → Wait, the input is:

The input lines are:

First line: *..*

Second line: .**. → Wait, the input says:

3 4

*..*

.**.

*. **

Wait, the input is:

Line 0: *..* → four characters.

Line 1: .**. → the second line is ".**."? So four characters. So row 1 has stars at (1,1) and (1,2).

Row 2: *.** → so (2,0), (2,2), (2,3). So row_stars[2] is 3.

So column counts:

Column 0: stars at (0,0), (2,0) → count 2.

Column 1: stars at (1,1) → count 1.

Column 2: stars at (1,2), (2,2) → count 2.

Column 3: stars at (0,3), (2,3) → count 2.

Now, for each star:

(0,0): row_stars[0]-1=1. column_stars[0]-1=1. 1*1=1.

(0,3): row_stars[0]-1=1. column_stars[3]-1=1. 1*1=1.

(1,1): row_stars[1]-1=1. column_stars[1]-1=0. 1*0=0.

(1,2): row_stars[1]-1=1. column_stars[2]-1=1. 1*1=1.

(2,0): row_stars[2]-1=2. column_stars[0]-1=1. 2*1=2.

(2,2): row_stars[2]-1=2. column_stars[2]-1=1. 2*1=2.

(2,3): row_stars[2]-1=2. column_stars[3]-1=1. 2*1=2.

Adding all these: 1 +1 +0 +1 +2 +2 +2 = 9, which matches the example.

So the approach is correct.

So the steps are:

- For each row, count the number of stars and store in row_counts[i].

- For each column, count the number of stars and store in col_counts[j].

- Iterate through each cell (i,j). If it's a star, add (row_counts[i]-1)*(col_counts[j]-1) to the total.

So how to compute row_counts and col_counts efficiently?

In Python, for a grid that is up to 1000x1000, this is manageable.

We can read the grid, then for each row, count the number of '*'s. For columns, we can create a list for each column j, count the number of stars in column j.

But with n and m up to 1000, we need to process 1000 rows and 1000 columns.

For rows, it's straightforward. For each row, row_counts[i] = sum(1 for c in grid[i] if c == '*').

For columns, perhaps we can create a list of lists. But another way is to loop through each column j, iterate each row i, check if grid[i][j] is '*', sum those.

In Python, for a grid stored as a list of strings (each string is a row), then for column j, the sum is sum(1 for row in grid if row[j] == '*').

So that's O(nm) time for both rows and columns, which is acceptable for 1e6 operations (since 1000*1000=1e6).

Then, for each cell (i,j) in the grid, if it's a star, add (row_counts[i]-1) * (col_counts[j]-1) to the total.

So the time complexity is O(nm) for all steps, which is acceptable.

Now, implementing this in Python.

Edge cases:

What if there's only one star in a row and column? Then (row_counts[i]-1) is zero, so that star contributes zero. So no triangles.

What about a grid with all stars? For each cell, (m-1)*(n-1) added. So total is n*m * (m-1)*(n-1). Which can be very large, but the code should handle that with integer types (Python's int is okay).

Now, let's code this.

First, read n and m.

Then read n lines, each line is a string. Store them as a list.

Compute row_counts: for each row, count the number of '*'s.

Compute col_counts: for each column j, count the number of '*'s in column j.

Then, iterate through each cell (i,j). If the cell is '*', add (row_counts[i]-1) * (col_counts[j]-1) to the total.

Finally, print the total.

But for columns, in Python, to compute col_counts, for j in range(m):

col_counts[j] = sum(1 for i in range(n) if grid[i][j] == '*')

Yes.

So code outline:

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

row_counts = [row.count('*') for row in grid]

col_counts = []
for j in range(m):
    cnt = 0
    for i in range(n):
        if grid[i][j] == '*':
            cnt +=1
    col_counts.append(cnt)

total = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '*':
            total += (row_counts[i]-1) * (col_counts[j]-1)

print(total)

Wait, but in Python, for the col_counts, using a loop for each j and each i. For m=1000, n=1000, that's 1e6 operations. Which is acceptable.

Testing the first example:

Input:

2 2

**

*.

Then grid is:

['**', '*.']

row_counts = [2,1]

col_counts for j=0: 2 (row 0 and 1 have j=0 as '*'), j=1: 1 (only row 0, j=1 is '*').

Then for each cell:

(0,0): (2-1)*(2-1) = 1*1=1.

(0,1): (2-1)*(1-1)=0.

(1,0): (1-1)* (2-1) = 0.

Total is 1.

Which is correct.

Second example:

3 4

*..*

.**.

*.**

Wait, the grid for the second example is:

Row 0: '*..*'

Row 1: '.**. ' ?

Wait, the input is:

*..*

.**.

*. **

Wait, perhaps the third line is "*.**" ?

So the grid is:

Row 0: '*..*' → indexes 0: *, 1: ., 2: ., 3: *

Row 1: '.**.' → indexes 0: ., 1: *, 2: *, 3: . 

Row 2: '*.**' → indexes 0: *, 1: ., 2: *, 3: *

So row_counts for row 0: 2, row 1: 2, row 2: 3.

col_counts:

col 0: rows 0, 2 → count 2.

col 1: row 1 → count 1.

col 2: rows 1, 2 → count 2 (row 1, j=2 is *, row 2, j=2 is *).

col 3: rows 0 and 2 → count 2 (row 0, j=3 is *, row 2, j=3 is *).

Then the code's calculation is as before, leading to 9.

Yes.

So the code should work.

Now, possible optimizations.

In Python, using row.count('*') is O(m) for each row, which is acceptable.

For the columns, perhaps a better way is to precompute a list of lists for each column. But in Python, using list comprehensions with loops is manageable.

Alternatively, transpose the grid and then count. But for a 1000x1000 grid, transposing is O(nm), which is acceptable.

But in Python, transposing can be done via zip(*grid), but each row is a string, so zip(*grid) would give tuples of characters.

But for columns:

col_counts = [sum(1 for c in col if c == '*') for col in zip(*grid)]

But let's see. For the first example:

grid is ['**', '*.'] → zip(*grid) gives tuples:

('*', '*'), ('*', '.')

sum(1 for c in ('*', '*') → 2 → first column.

sum(1 for c in ('*', '.') → 1 → second column.

So col_counts would be [2, 1], which is correct.

Yes. So that's a more concise way to compute col_counts.

So code can be:

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

row_counts = [row.count('*') for row in grid]
col_counts = [col.count('*') for col in zip(*grid)]

total = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '*':
            total += (row_counts[i] -1) * (col_counts[j] -1)

print(total)

Wait, zip(*grid) returns the columns as tuples. For example, if the grid is:

Row 0: 'abc'

Row 1: 'def'

Then zip(*grid) would give ('a','d'), ('b','e'), ('c','f').

So for each column in the original grid, the tuple is the characters in that column.

Thus, col_counts can be computed by taking each of these tuples and counting the number of '*'s.

So row.count('*') for each row gives row_counts.

col.count('*') for each column in zip(*grid) gives col_counts.

This is a more efficient way, as zip is handled in Python in a way that's optimized.

So the code can be written as such.

This would be efficient and concise.

So this code should work for all cases and handle the constraints.

Now, let's test for possible edge cases.

Test case: n=1, m=1. The grid is ['*'].

Then row_counts is [1], col_counts is [1]. For cell (0,0), (1-1)*(1-1) =0. So output 0.

Which is correct, since you need three points for a triangle.

Another test case: n=3, m=3. All cells are '*'. So each cell contributes (3-1)*(3-1)=4. So total 3*3*4 =36. So output is 36.

Yes. For example, for cell (0,0), there are 2 stars in the row (columns 1 and 2) and 2 in the column (rows 1 and 2). Each pair of a star in row and column gives a triangle. So 2*2=4 per cell, 9 cells → 36.

Yes.

Thus, the code seems correct.
</think>

```python
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

row_counts = [row.count('*') for row in grid]
col_counts = [col.count('*') for col in zip(*grid)]

total = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '*':
            total += (row_counts[i] - 1) * (col_counts[j] - 1)

print(total)
```