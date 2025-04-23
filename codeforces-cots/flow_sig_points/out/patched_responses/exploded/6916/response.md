<think>
Okay, let's see. I need to solve this problem where I have to count the number of winning squares on a board. A winning square is one where the sum of its column is strictly greater than the sum of its row. Hmm.

So first, the input is an n x n grid. For each cell (i,j), I have to compute the sum of the column j and compare it to the sum of row i. If the column sum is greater, then it's a winning square. The output is the total count of such squares.

Wait, but how do I efficiently calculate all the row and column sums? Because if I calculate the sum for each row and each column once, then for each cell I can just look up those sums and compare. That makes sense. Because recalculating the sum for every cell would be O(n^3), which for n=30 is 27,000 operations. But precomputing row and column sums would be O(n^2), which is manageable.

Right. So the plan is:

1. Read the grid.
2. Precompute the sum of each row.
3. Precompute the sum of each column.
4. For each cell (i,j), check if column_sum[j] > row_sum[i]. If yes, increment the count.

That's straightforward. Let's think about the steps in code.

Reading the input: The first line is n. Then n lines each with n numbers. So for each of the next n lines, split into integers and store in a 2D list.

But in Python, rows are stored as lists, and for columns, I need to sum each column. Wait, but columns are the j-th element in each row. So for example, column j would be [row[0][j], row[1][j], ..., row[n-1][j}].

So to compute column sums, I can loop through each column index j, then loop through each row i, and sum grid[i][j].

Alternatively, for each row in the grid, we can compute the row sum as sum(row). For columns, since each row is stored as a list, the j-th column is the sum of grid[i][j] for all i in 0..n-1.

So for code:

Read n.

grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

Then compute row_sums as [sum(row) for row in grid]

Then compute column_sums. For each j in 0 to n-1:

column_sums[j] = sum(grid[i][j] for i in range(n))

Once I have row_sums and column_sums, then for each cell (i,j), check if column_sums[j] > row_sums[i]. If yes, count it.

So the total count is the sum over all i and j of (1 if column_sums[j] > row_sums[i] else 0)

So the steps are:

Read the grid, compute row sums and column sums, then loop through each cell and compare.

Now, considering the constraints. n can be up to 30. So the grid is 30x30, which is 900 cells. So even a O(n^2) solution is acceptable here. No problem with time. Even if n was 1e4, this approach would still be feasible.

But for n=30, it's definitely manageable. So the code should be straightforward.

Let's test with the examples.

First example:

Input:
1
1

The grid is a single cell. Row sum is [1], column sum is [1]. For the only cell (0,0), compare 1 and 1. Since they're equal, not counted. So output 0. Correct.

Second example:

Input:
2
1 2
3 4

The grid is row 0: [1,2], row 1: [3,4].

row_sums: 3,7.

columns: column 0 is 1+3=4, column 1 is 2+4=6.

Now, check each cell:

Cell (0,0): column 0 sum 4 > row 0 sum 3? Yes. So count +=1.

Cell (0,1): column 1 sum 6 > row sum 3? Yes. Count +=1. Total 2.

Cell (1,0): column 0 sum 4 > row sum 7? No.

Cell (1,1): column sum 6 >7? No. So total 2. Output 2. Correct.

Third example: let's see. According to the note, the output is 6. The code would compute the row sums and column sums, then check each cell. So the code should handle that.

So the approach is correct.

Now, code implementation.

In Python:

Read n.

Then read n lines, each with n numbers. Then compute row sums as a list of sum of each row.

Compute column sums as a list where each element j is the sum of grid[i][j] for all i.

Then iterate through each cell (i, j) and check if column_sums[j] > row_sums[i]. Count the number of such cells.

The code could look like this:

n = int(input())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

row_sums = [sum(row) for row in grid]

column_sums = []
for j in range(n):
    total = 0
    for i in range(n):
        total += grid[i][j]
    column_sums.append(total)

count = 0
for i in range(n):
    for j in range(n):
        if column_sums[j] > row_sums[i]:
            count +=1

print(count)

Wait, but in the problem statement, the columns and rows are 1-based or 0-based? Let me check the input description.

The input says: the j-th number on the i-th line represents the number on the square that belongs to the j-th column and the i-th row. So the grid is stored as rows, and each row has the numbers for columns 1 to n. So in code, grid[i][j] is the j-th column (0-based) of the i-th row (0-based). So when we compute column_sums[j], that's correct.

Yes. So code is correct.

Testing the code with the examples:

First input:

1

1

row_sums = [1]

column_sums = [1]

Compare for i=0, j=0: 1 vs 1. Not greater. So count 0. Correct.

Second example:

n=2

rows are [1,2] and [3,4]

row_sums = 3,7.

columns:

column 0: 1+3=4, column 1: 2+4=6.

Then for each cell:

i=0 (row sum 3):

j=0: 4>3 → yes → count.

j=1:6>3 → yes → count.

i=1 (row sum 7):

j=0:4>7 → no.

j=1:6>7 → no.

Total count 2. Correct.

Third example's code would process the grid and compute the correct row and column sums, leading to 6 winning squares.

So the code is correct.

What about space? For n=30, the grid is 30x30 integers. Each is small. So no problem. The row_sums and column_sums are lists of 30 integers each. All manageable.

Time: O(n^2) for reading the grid, O(n^2) for computing column sums (since each of n columns requires n steps), then O(n^2) for checking each cell. So total O(n²). For n=30, 900 steps each part. Well within the time constraints.

So this code should work.
</think>

```python
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
row_sums = [sum(row) for row in grid]
column_sums = [sum(col) for col in zip(*grid)]
count = 0
for i in range(n):
    for j in range(n):
        if column_sums[j] > row_sums[i]:
            count += 1
print(count)
```