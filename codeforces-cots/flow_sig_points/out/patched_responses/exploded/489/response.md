<think>
Okay, let's see. The problem is about simulating painting operations on a grid and then outputting the final state. But with constraints that could be up to 5000x5000 grid and 100,000 operations. Wait, but the note says that n*m is up to 100,000. Oh right, so the product of n and m can't exceed 1e5, which means even if n is 5000, m would be 20. So the maximum grid size is manageable.

But if I try to simulate each operation by updating every cell in a row or column, that's O(k*(n + m)) time. For example, if k is 1e5 and each operation is on a row of 5e3 elements, then 1e5 * 5e3 = 5e8 operations, which is way too slow. That's definitely not going to work. So we need a smarter way.

Hmm. So the key insight here is that the last operation on a row or column determines the color of the cells. For each cell (i,j), its color is determined by the last row operation on row i and the last column operation on column j. Whichever of those two operations happened later (had a higher timestamp) will set the color of the cell.

So the plan is: track for each row the last time (operation number) it was painted and its color. Similarly for each column. Then, for each cell, compare the row's last time and column's last time. The later one determines the color. If the row was updated last, use the row's color; else use the column's color. If neither was ever updated, it's 0.

So the steps are:

1. Initialize two arrays: row_ops and col_ops. Each keeps track of the latest timestamp and color for each row and column.
2. Process each operation in order, updating the corresponding row or column's last operation time (like, incrementing a counter each time, or using the order index as the timestamp).
3. After all operations, for each cell (i,j), check the latest between row i and column j. Take the color from the one with the later timestamp.

This approach is O(k + n*m), which is acceptable. Because even if n and m are up to 5e3 each, n*m would be up to 1e5 (as per constraints), and k is 1e5. So the total operations are manageable.

So how to track the timestamps? For each row, store the last operation's time (like the order in which operations were applied) and color. Same for columns. Since each operation is processed in order, the timestamp can be the step number (from 1 to k). So for each operation, whether it's a row or column, we update the row's or column's last_time and color. Then, for each cell, compare the row's last_time and column's last_time. The larger one's color is the cell's color.

Yes. So for example, in the first sample input:

3 3 3

Operations:

1 1 3 (row 1, time 1)

2 2 1 (column 2, time 2)

1 2 2 (row 2, time 3)

So row 1's last_time is 1, color 3.

Column 2's last_time is 2, color 1.

Row 2's last_time is 3, color 2.

Then, for cell (1,2):

row 1's time 1 vs column 2's time 2. So column's time is later, so color 1.

But for cell (1,3), row 1's time 1, column 3's time is 0 (if not updated), so row's color 3.

So this approach works.

So the steps for implementation are:

- Read n, m, k.

- Initialize two arrays for rows and columns. For each row i, store the last time it was updated (initially 0) and the color (initially 0). Similarly for columns.

- Then, process each of the k operations. For each, update the corresponding row or column's time (using the operation's index as the timestamp) and color.

- After processing all operations, for each cell (i,j), compare the row i's last time and column j's last time. The one with the higher time gives the color. If equal, row takes precedence? Wait, no. Wait, the timestamp is the order in which operations were done. So if a row was updated at time t and a column at time t, then whichever came later (higher t) determines the color. But if same, then the last operation is the one that happened later. Wait, but each operation is unique. So each operation has a unique timestamp. So no two operations can have the same time. Because each step is processed in order. So for each of the k operations, the timestamp can be their order (1-based). So, for example, the first operation has time 1, second time 2, etc. So for any row and column, their last_time can be compared as integers. If row's last_time is higher, then the row's color is used. Otherwise, column's.

So during the processing, for each operation, we assign a time starting from 1 to k, in the order they are processed.

Wait, but in the code, when processing the operations in order, the first one is time 1, second time 2, etc. So for each operation, whether it's row or column, we assign the current step as the time.

So in code:

Initialize step = 0.

For each operation in the k operations:

   step +=1

   if it's a row operation:

       update row_ops[ri] = (step, ai)

   else:

       update col_ops[ci] = (step, ai)

Then, when building the grid:

for each row i in 1..n:

   for each column j in 1..m:

       row_time, row_color = row_ops[i]

       col_time, col_color = col_ops[j]

       if row_time > col_time:

           color is row_color

       else:

           color is col_color

But wait, rows and columns are 1-based. So in code, the arrays for row_ops and col_ops should be 1-based as well. So for example, row_ops is a list of (time, color) for each row from 1 to n.

So in Python, perhaps we can index rows 0 to n-1, but better to use 1-based indices. So for n rows, create a list of size n+1 (indices 0 to n, but 1..n are used). Same for columns.

So in code:

n, m, k = map(int, input().split())

rows = [ (0, 0) ] * (n+1)  # (time, color) for each row, 1-based

cols = [ (0, 0) ] * (m+1)  # same for columns.

current_time = 0

for _ in range(k):

   parts = input().split()

   type_op = int(parts[0])

   idx = int(parts[1])

   a = int(parts[2])

   current_time +=1

   if type_op == 1:

       rows[idx] = (current_time, a)

   else:

       cols[idx] = (current_time, a)

Then, for each cell (i,j):

row_time, row_color = rows[i]

col_time, col_color = cols[j]

if row_time > col_time:

   output row_color

else:

   output col_color

This is O(k) to process the operations, and O(n*m) to build the output. Which fits the constraints.

Now, considering that n and m can be up to 5000 each, but their product is up to 1e5. So for 1e5 cells, iterating through them is manageable.

In Python, for generating the output, we need to create each row as a string. Since for each row, we have to loop through m columns, and for each, check the row and column's time.

But for Python, creating a list of strings and then printing them with ' '.join is the way to go.

But how to handle the 1-based indices. For example, rows is 1-based. So for row 1 to n, and column 1 to m.

So in code:

for i in range(1, n+1):

   row = []

   r_time, r_color = rows[i]

   for j in range(1, m+1):

       c_time, c_color = cols[j]

       if r_time > c_time:

           row.append(str(r_color))

       else:

           row.append(str(c_color))

   print(' '.join(row))

Yes. But for m=5000, each row has 5000 elements, which could be a problem in terms of time. But considering that n*m is up to 1e5, the total number of elements is 1e5. So for 1e5 elements, building strings and printing is manageable.

But in Python, appending to a list and then joining is O(m) per row, which for 1e5 elements is acceptable.

But let's think of the first sample input, which is 3 rows, each with 3 elements. So for each row, loop through 3 columns.

But for a larger example, like 5000 rows and 20 columns (since 5000*20=1e5), then each row has 20 elements. So 5000 rows, each with 20 elements: 1e5 total elements.

So the code should handle that.

So the code is:

Read n, m, k.

Initialize rows and cols as 1-based arrays of tuples (time, color), initially (0,0) for all.

Process each operation, incrementing current_time each time. For row operations, update the row's entry. For columns, update the column's entry.

Then, for each cell, compare times and choose color.

Yes.

Now, possible edge cases:

- When no operations are done on a row or column. Then their time is 0, color 0.

So, for a cell (i,j) where neither row i nor column j was ever painted, the row's time is 0, column's time is 0. So 0 <=0, so we take column's color, which is 0. So the cell is 0. Correct.

Another case: a cell where the row was painted once (time 5) and column was painted once (time 3). Then row's time is higher, so color is row's.

Another case: row and column both painted, same time? No, because each operation is processed in order, and each step's current_time is unique. So no two operations can have the same time.

So the code is correct.

Now, let's test the first sample input.

Sample Input 1:

3 3 3

1 1 3 → time 1: row 1 is 3.

2 2 1 → time 2: column 2 is 1.

1 2 2 → time 3: row 2 is 2.

Processing:

rows[1] = (1,3), rows[2] = (3,2), rows[3] = (0,0).

cols[2] = (2,1), others are (0,0).

For each cell:

Row 1:

cells (1,1): row time 1 vs col 1 (0). So 1>0 → 3.

cell (1,2): row time 1 vs col 2 time 2 → 1 < 2 → 1.

cell (1,3): row time 1 vs col 3 (0) → 3.

So first row is 3 1 3.

Row 2: row time 3, color 2.

cells (2,1): col 1 time 0 → 2.

cell (2,2): col 2 time 2 < 3 → 2.

cell (2,3): col 3 time 0 → 2.

So row 2 is 2 2 2.

Row 3: row time 0.

cells (3,1): col 1 time 0. So max is 0 vs 0 → take column's color (0). But wait, columns for j=1: col_ops[1] is (0,0). So time 0. So row's time is 0, column's is 0. So column's color is 0. But in the sample output, the third row is 0 1 0.

Wait, because in the third row, j=2: column 2's time is 2. row 3's time is 0. So column's color 1 is used. So the third row's cells:

cell (3,1): col 1's time 0, row time 0 → color 0.

cell (3,2): column's time 2, color 1.

cell (3,3): column's time 0, so color 0.

Thus, the third row is 0 1 0. Which matches the sample output.

So code works.

Another sample input:

5 3 5

1 1 1 → row 1, time 1.

1 3 1 → row 3, time 2.

1 5 1 → row 5, time 3.

2 1 1 → column 1, time 4.

2 3 1 → column 3, time5.

So rows 1,3,5 are painted at times 1, 2, 3. Columns 1 and 3 at times4 and5.

Then, for each cell:

Row 1: last time 1. For columns 1,2,3.

cell (1,1): column 1's time4>1 → color 1.

cell (1,2): column 2's time0 → row's time1>0 → color1.

cell (1,3): column3's time5>1 → color1. So row1: 1 1 1.

Row2: no row operation. So row time 0.

cells (2,1): column1's time4>0 → color1.

cell (2,2): column2's time0 → color0.

cell (2,3): column3's time5>0 → color1. So row2: 1 0 1.

Row3: row time2.

cells (3,1): column1's time4>2 → color1.

cell (3,2): column2's time0 <2 → row's color1.

cell (3,3): column3's time5>2 → color1. So row3:1 1 1.

Row4: row time0.

cells (4,1): column1's time4 → color1.

cell (4,2): column2's time0 → color0.

cell (4,3): column3's time5 → color1. So row4:1 0 1.

Row5: row time3.

cells (5,1): column1's time4>3 → color1.

cell (5,2): column2's time0 <3 → row's color1.

cell (5,3): column3's time5>3 → color1. So row5:1 1 1.

Which matches the sample output.

So code works.

Now, considering memory. For n and m up to 5e3, the rows and cols arrays would be size 5e3 +1 each. Which is acceptable. For Python, each entry is a tuple of two integers. So negligible.

Thus, the code should handle all cases efficiently.

Now, implementing this in Python. But in Python, for rows and columns, we need to create lists of size (n+1) and (m+1). So rows is [ (0,0) ] * (n+1) would not work because tuples are immutable. Wait, no. Wait, when you do rows = [ (0,0) ] * (n+1), this creates a list where all elements are references to the same tuple. So when you try to assign rows[idx] = (current_time, a), then each row entry is a separate tuple. But initializing a list where all elements are (0,0) is okay. For example:

rows = [ (0,0) for _ in range(n+1) ]

But the code as written in the draft would create a list of (n+1) elements, each being the same tuple. But in Python, when you modify it, since tuples are immutable, you replace the element with a new tuple, so it's okay. Wait, no. Because in Python, the initial code rows = [ (0,0) ] * (n+1) creates a list of n+1 references to the same tuple. But when you do rows[idx] = (new_time, new_color), it changes the reference at that index to a new tuple. So that's okay. So initializing as [ (0,0) ] * (n+1) is acceptable. Because each assignment replaces the tuple at that index.

Wait, no. For example:

a = [ (0,0) ] * 3

a[1] = (1,2)

Then a will be [ (0,0), (1,2), (0,0) ]

Yes. So the code is correct.

But in Python, list multiplication for mutable elements can be dangerous, but tuples are immutable. So it's safe here.

So the code can be written as:

rows = [ (0,0) ] * (n+1)

But wait, no. Because when you multiply a list of a single tuple, you create a list with multiple references to the same tuple. But when you assign rows[i] = (x, y), you are replacing the ith element with a new tuple. So that's okay.

So in Python, the code:

rows = [ (0,0) ] * (n+1)

is acceptable for initializing a list of (n+1) elements, each (0,0). Then, each row is updated by assigning to rows[i], which replaces that element with a new tuple.

Yes.

So in code:

rows = [ (0, 0) ] * (n+1)

But wait, no. For example, if n+1 is 4, then rows will be [ (0,0), (0,0), (0,0), (0,0) ] (indexes 0,1,2,3). Wait, no. Wait, n+1 is 4, so [ (0,0) ] *4 creates a list with four elements, indexes 0,1,2,3. So for rows, indexes 0 to n. But in code, rows are 1-based. So for row 1 to n, indexes 1 to n. That's correct.

So the code is okay.

Thus, the code should work.

Now, considering that in Python, for large n and m, creating a list of (n+1) elements is feasible. Since n can be up to 5e3, which is manageable.

So the code should be correct.

Testing the code with the sample inputs.

Sample 1:

n=3, m=3, k=3.

rows = [ (0,0) ] *4 → indexes 0,1,2,3.

Processing the three steps:

Step 1: row 1 → rows[1] becomes (1,3).

Step 2: column 2 → cols[2] becomes (2,1).

Step3: row2 → rows[2] becomes (3,2).

Then, for row 1, j from 1 to 3.

For j=1: col 1's time is 0. So row's time 1>0 → color3.

j=2: col 2's time 2>1 → color1.

j=3: col3's time 0 → color3.

So the first row is 3 1 3.

Which matches.

Yes.

Thus, code is correct.
</think>

```python
n, m, k = map(int, input().split())
rows = [(0, 0)] * (n + 1)
cols = [(0, 0)] * (m + 1)
current_time = 0

for _ in range(k):
    parts = input().split()
    op_type = int(parts[0])
    idx = int(parts[1])
    a = int(parts[2])
    current_time += 1
    if op_type == 1:
        rows[idx] = (current_time, a)
    else:
        cols[idx] = (current_time, a)

for i in range(1, n + 1):
    row_time, row_color = rows[i]
    output = []
    for j in range(1, m + 1):
        col_time, col_color = cols[j]
        if row_time > col_time:
            output.append(str(row_color))
        else:
            output.append(str(col_color))
    print(' '.join(output))
```