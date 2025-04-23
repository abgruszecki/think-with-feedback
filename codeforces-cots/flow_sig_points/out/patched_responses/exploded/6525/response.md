<think>
Okay, so I need to solve this problem where Valera is painting cells on an n x n grid, and I have to find the earliest move where a 3x3 fully black square appears. If after all m moves there's none, output -1. Let's think about how to approach this.

First, the constraints. The n can be up to 1000, and m up to 1e5. So the grid is potentially 1e6 cells (but n=1000, n² is 1e6). But m is up to 1e5, so we need an efficient way to check after each move whether a 3x3 square is formed.

The key idea here is, for each painted cell, check if it's part of a 3x3 square that's fully painted. But checking all possible 3x3 squares each time would be expensive. So maybe we can track the cells as they are painted and check only the relevant 3x3 squares that include the current cell.

Wait, but how? Let's think. Each time a new cell (x,y) is painted, we need to check all possible 3x3 squares that include this cell and see if all 9 cells in any of those squares are painted. The earliest move where any such square becomes fully painted is our answer.

But how to efficiently check this?

Each cell (x,y) can be part of several 3x3 squares. For example, if the cell is in the middle, it's part of one square. But if it's on the edge, maybe part of a few. Wait, actually, for a cell (x,y), the possible 3x3 squares that include it would have their top-left corner in a certain range.

The top-left corner of a 3x3 square must satisfy:

i <= x <= i+2
j <= y <= j+2

So for a given (x,y), the possible top-left corners (i,j) are those where i ranges from x-2 to x, and j ranges from y-2 to y, but such that i >= 1, j >=1, and i+2 <=n, j+2 <=n (since the square must fit within the grid). So for each (x,y), the possible squares it's part of are the ones where (i,j) is the top-left corner, and the square includes (x,y).

So for each new cell (x,y) added, we need to check all possible 3x3 squares that include (x,y) as part of their 9 cells. For each such square, check if all 9 cells have been painted. If any of them is complete, then the current move is the answer.

But checking all possible squares for each cell could be time-consuming. For example, for each cell (x,y), how many squares does it belong to? Let's see:

The top-left corner i can be max(1, x-2) to min(n-2, x). Similarly for j. So the number of squares a cell is part of is up to 3 (for i) times 3 (for j) = 9. But only if the cell is in a position that allows that. For example, a cell in the top-left corner of the grid (1,1) can only be part of one 3x3 square (the one starting at (1,1)).

So for each painted cell, we can generate all possible 3x3 squares that include it and check if those squares are completely filled. However, checking all 9 cells for each possible square each time a new cell is added could be expensive, especially if m is 1e5. For each of the up to 9 squares per cell, checking 9 cells each time is O(9*9) per cell, leading to 9*9*1e5 = 8.1e6 operations, which is acceptable. But maybe we can optimize this.

Alternative approach: For each 3x3 square, track how many of its cells are painted. Once any of them reaches 9, return the current move.

But the problem is how to track this. Since the squares are up to (n-2)*(n-2) possible 3x3 squares (since the square must be 3x3, the top-left can be from (1,1) to (n-2, n-2)), which for n=1000 is 998*998 ≈ 1e6 squares. For each square, track the count of painted cells. Then, when a cell (x,y) is painted, we update all the squares that include (x,y) by incrementing their count. If any of them reaches 9, return the current step.

This seems manageable.

So the steps would be:

1. Precompute all possible 3x3 squares (top-left (i,j)) that exist in the grid. For each square, track the number of cells painted (initialized to 0).

But how do we efficiently track which squares include a newly painted cell (x,y)? For each (x,y), find all squares (i,j) such that i <= x <= i+2 and j <= y <= j+2, and i and j are valid (i+2 <=n, j+2 <=n). Then, for each such (i,j), increment their count. Once any count reaches 9, return the current move.

So for each painted cell, generate all possible (i,j) squares that include (x,y), and update their counts.

This approach would require, for each cell, to generate all possible (i,j) squares that include it, then for each of those squares, check if the current count is 8 (since this new cell would be the 9th). Then, if so, the current move is the answer.

Wait, but how do we track the counts? Let's see. We can have a dictionary or a 2D array to track the counts for each square (i,j). For each square (i,j), the count starts at 0. Each time a cell (x,y) is painted, we find all squares (i,j) that include (x,y), and for each, increment their count. If any count reaches 9, then we return the current move.

But the problem is that n can be up to 1000, so the array for counts would be (n-2) x (n-2), which for n=1000 is 998x998 = ~1e6 elements. So using a 2D array is feasible in terms of memory (each element is an integer, 4 bytes, so 4e6 bytes = 4MB, which is acceptable).

So the steps would be:

- Initialize a 2D array (counts) of size (n-2+1) x (n-2+1) (since i can be from 1 to n-2). Wait, for i in 1 to n-2, inclusive. Because a square starting at i= n-2 will cover i, i+1, i+2 (n-2 +2 =n).

So counts is (n-2) rows and (n-2) columns.

But in Python, initializing a 2D list for n=1000 would be (1000-2)=998 rows and 998 columns. So 998*998 is around a million entries, which is manageable.

So for each new cell (x,y), we need to find all possible squares (i,j) that include (x,y). Then for each such (i,j), we increment counts[i][j] by 1. Then, check if counts[i][j] is 9. If any of them is, return the current move.

But how to find all (i,j) that include (x,y)?

The square (i,j) must satisfy:

i <= x <= i+2

j <= y <= j+2

Also, the square (i,j) must be valid, i.e., i <= n-2 and j <=n-2.

So for x, the possible i's are the starting rows of squares that include x. The i can be as low as max(1, x-2), but the square must have i+2 <=n. So the maximum possible i is x (if x+2 <=n). Wait, no. Let's see:

The square starting at i can have i, i+1, i+2 as rows. So x must be in that range.

So i can be any value from x-2 down to i where i <=x, but also i >=1 and i+2 <=n.

So the valid i's are:

i >= max(1, x-2)

i <= x

and i <=n-2.

So the possible i's are in the range [max(1, x-2), min(x, n-2)].

Similarly for j.

So for x, the possible i's are from a starting i1 to i2:

i1 = max(1, x-2)

i2 = min(x, n-2)

Similarly for j.

If i1 > i2, then there are no possible i's (so this cell can't be part of any 3x3 square). For example, if n=3, then the only possible i is 1. So for x=3, i can be 1 (since 1 <=3 <=3), but i must be <=n-2=1. So yes.

So, for a given x, the possible i's are from i1 to i2, and similar for j.

So for each (x,y), compute the possible i's and j's. For each (i,j) in that range, increment counts[i][j] and check if it's 9.

So, the algorithm would be:

Initialize a grid (a set) to track which cells are painted. But for each step, we process the cells in the order given. For each cell (x,y), we check all possible (i,j) squares that include (x,y). For each such (i,j), we check if all 9 cells in the square are painted. But tracking that with a counter is better.

Wait, but when a cell is painted multiple times, but the input says all moves are different, so each (x,y) is added once. So each cell is processed once, so no duplicates.

So here's the plan:

We need to track for each square (i,j) how many of its cells have been painted. For each new cell (x,y) added at step k, find all squares (i,j) that include (x,y). For each such square, increment their count. Then, check if any of these counts is now 9. If yes, then return k (since this is the first time this square is filled).

So, the key is that for each step, we process the cell, generate all possible squares (i,j) that include (x,y), update their counts, and check for 9.

This approach would work. Now, the steps in code:

First, read n and m.

Then, read m cells, in order. For each cell, process it step by step, and for each, check the squares.

But processing them step by step, and for each cell, compute the possible i and j ranges, then loop through all possible (i,j) in those ranges, and update their counts.

Once any of the counts reaches 9, output the current step (which is the step number from 1 to m). If after all steps, no such count reaches 9, output -1.

Now, let's think about the data structures.

We can represent counts as a 2D list (array) in Python. For n up to 1000, counts is (n-2) x (n-2). But in Python, list indices start at 0. So if the squares are indexed from (i,j) where i and j start at 1, then counts can be accessed as counts[i-1][j-1]. Alternatively, adjust the indices.

But for code clarity, perhaps it's better to use 0-based or 1-based indices. Let's see.

Let me see: for i in 1 to n-2 (inclusive), and j in 1 to n-2 (inclusive). Then the counts can be a list of lists, with size (n-2) x (n-2), but since lists are 0-based, the actual indices would be (i-1) and (j-1) for i and j in 1..n-2.

So for example, if n is 4, then possible i values are 1 and 2. So counts would be a 2x2 array, where counts[0][0] is for i=1, j=1, etc.

So, when processing a cell (x, y), for possible i in the range:

i can be from max(1, x-2) to min(x, n-2). Because the square must start at i such that i <= x <= i+2, and i+2 <=n (so i <=n-2). Also, x must be >=i, so i can't be larger than x.

Similarly for j.

For example, if x is 3, and n is 4. So possible i ranges are max(1, 3-2) =1, and min(3, 4-2)=3? Wait, n-2 is 2. So i can be up to min(3, 2) =2. So i ranges from 1 to 2.

Wait, let's compute for x=3 in n=4:

The possible i's are from max(1,3-2)=1 to min(3,4-2)=2. So i can be 1 or 2.

So for i=1: the square is rows 1,2,3. x=3 is in that range. For i=2: rows 2,3,4. x=3 is in that range.

So for each x and y, compute the i and j ranges.

Once the ranges are determined, loop through all i and j in those ranges, and for each (i,j), increment the count.

Then, check if any of these counts reaches 9. If yes, return the current step.

But wait, each square has 9 cells. So when the count for a square reaches 9, it's fully painted. So yes.

So, the code steps:

Read n, m.

Initialize a 2D array counts with (n-2) rows and (n-2) columns, all zeros. But in Python, creating a list of lists for this can be done with:

counts = [[0]*(n-2) for _ in range(n-2)]

Wait, no. Because if n is 3, then n-2 is 1, so it's a 1x1 array. So that's correct.

Wait, the rows are for i in 1..n-2, which is n-2 elements. So the counts array should be (n-2) rows each of (n-2) columns. So yes.

Wait, no. For example, n=4: i ranges from 1 to 2 (since 4-2=2). So counts would have 2 rows (i=1 and 2) and 2 columns (j=1 and 2). So the correct code is counts = [[0]*(n-2) for _ in range(n-2)].

Wait, no. Because the number of columns is (n-2), but for each row, the j ranges from 1 to n-2, which is (n-2) elements. So for each i in 1..n-2, counts[i-1][j-1] represents the count for square (i,j).

Yes.

Then, for each step from 1 to m:

Read x, y.

Compute the possible i's (rows of the squares that include x):

i starts at max(1, x-2) and ends at min(x, n-2). But x can be up to n. For example, if x is 5 and n=5, then n-2=3, so i can be up to 3. So min(5,3) =3. So i ranges from 3 (since x-2=5-2=3) up to 3. So i=3.

So in code:

i_min = max(1, x-2)
i_max = min(x, n-2)
Similarly for j.

But wait, x can be larger than n-2. For example, n=5, x=5. Then n-2=3. So i_max is min(5, 3) =3. But i_max must be <=n-2. So this is correct.

But if i_min > i_max, then there are no i's, so this cell (x,y) is not part of any 3x3 square.

Same for j.

So, for each (x,y), first compute the i's and j's:

i_min = max(1, x-2)
i_max = min(x, n-2)

j_min = max(1, y-2)
j_max = min(y, n-2)

If i_min > i_max or j_min >j_max: then this cell is not part of any 3x3 square. So we can skip checking.

Else, loop through all i from i_min to i_max, and j from j_min to j_max.

For each (i,j) in those ranges:

In the counts array, increment counts[i-1][j-1] by 1.

Then, check if counts[i-1][j-1] is 9. If yes, return the current step (which is the step number, starting from 1).

If after processing all steps, no count reaches 9, return -1.

Wait, but how do we track the step number? Because the steps are processed in the order given. So for each of the m steps, we process the cell in order. For each, after updating the counts, check if any of the updated counts is 9. The first such occurrence is the answer.

Yes.

So in code:

Read n and m.

Initialize counts as a 2D list of (n-2) rows and (n-2) columns, initialized to 0.

Then, for each k in 1 to m:

Read x, y.

Compute i_min, i_max, j_min, j_max as above.

if i_min >i_max or j_min>j_max: continue processing (this cell is not part of any 3x3 square).

Else, loop over i from i_min to i_max:

   loop over j from j_min to j_max:

       counts[i-1][j-1] +=1

       if counts[i-1][j-1] ==9:

           print(k)

           exit.

After processing all steps, print -1.

This should work.

Now, let's test this approach against the examples.

First example:

Input:

4 11

Then 11 cells.

The output is 10.

Let's see. The counts array is (4-2)x(4-2) =2x2. So counts is for squares (1,1), (1,2), (2,1), (2,2).

Each square has 9 cells, but in the first example, after 10 steps, one of these squares is filled.

Looking at the steps, after step 10, the cell (3,3) is painted. Let's see which squares include this cell.

x=3, y=3.

i_min = max(1, 3-2) =1.

i_max = min(3, 4-2=2) => 2.

j_min = max(1, 3-2=1) →1.

j_max= min(3, 4-2=2) →2.

So i ranges 1 to 2, j 1 to 2.

So squares (1,1), (1,2), (2,1), (2,2).

For each of these, we increment the count by 1. Suppose that for square (1,1), the count was 8 before step 10, and after increment becomes 9. Then step 10 is the answer.

But how to track that?

In any case, the code would check all possible squares that include the new cell, and return the first time any of them reaches 9.

So the code works.

Second example:

After 12 steps, all cells are painted, but no 3x3 square. The code returns -1.

Now, for possible issues:

Edge cases:

n <3 → no 3x3 square possible. So answer is -1.

Wait, the problem says 1<=n <=1000. So if n is 1 or 2, then it's impossible to form a 3x3 square. So in such cases, regardless of m, output is -1.

So in code, before anything else, check if n <3. If so, output -1.

Yes. Because even if n is 2 and m is 4 (the maximum possible), there's no 3x3 square possible.

So code must handle that.

Another edge case: n=3. Then the only possible square is (1,1). So after all 9 cells in that square are painted, the answer is the step when the 9th is added.

So in code, the code will check all cells in (1,1) square. For example, if the first 9 steps paint all cells in that square, the 9th step is the answer.

But what if some cells are painted outside of the square? Those don't affect the counts for (1,1).

So code handles that.

So, code steps:

First check if n <3. If yes, output -1.

Else, proceed with the rest.

So that's an important check to add.

So modifying the code:

Read n and m.

if n <3:

   after reading m cells (since input requires m lines), output -1.

Because even if m is 9, the grid is 3x3, but for n=3, the possible square is 1,1. So code would proceed.

Wait, no. For n=3, n-2=1. So i can be 1, j can be 1. So the code will check the square (1,1). So when n is 3, the code will work as expected.

So the code needs to handle the case where n >=3.

But if n is 3, and m is 9, but the 9 steps are all in the 3x3 square, then the code will output 9. Correct.

But if n is 2, then the code will output -1 regardless of m. So in code, first check if n <3. If yes, output -1.

So code:

n, m = map(int, input().split())

if n <3:

    # read all m lines, but ignore them

    for _ in range(m):

        x, y = map(int, input().split())

    print(-1)

    exit()

Then, proceed with the rest.

Yes.

Another edge case: m <9. Then, even if all cells are in the same 3x3 square, the count can't reach 9. So output -1.

But code handles that automatically, because counts start at 0 and increments. So even if m is 8 and all are in a square, counts would be 8, and not trigger the 9 condition.

So code is correct.

Now, let's test the first example:

Input:

4 11

Then the code initializes a 2x2 counts array.

Each square is (1,1), (1,2), (2,1), (2,2).

Each step adds a cell and checks the possible squares. Let's see step 10:

The 10th move is (3,3).

For this cell, x=3, y=3.

i_min = max(1, 3-2)=1.

i_max = min(3, 4-2=2) →2.

j_min = max(1,3-2=1) →1.

j_max = min(3,4-2=2) →2.

So the squares are (1,1), (1,2), (2,1), (2,2).

Each of these squares will have their count incremented by 1.

If any of these squares had 8 cells before, then after increment, they reach 9.

In the example, the output is 10, which suggests that at step 10, one of the squares reached 9.

So code would output 10, which matches the example.

The second example's output is -1. So after all 12 steps, none of the squares have all 9 cells.

Thus, the code will not find any counts reaching 9, so outputs -1.

So the code should handle these cases.

Now, code optimization.

In Python, creating a 2D list for n=1000 (so counts is 998x998) is feasible. But for each step, looping through up to 3x3=9 squares is manageable. So the code's time complexity is O(m * 9) = 9e5 operations, which is acceptable.

Space-wise, for n=1000, the counts array is 998x998= ~1e6 integers. Each integer is 4 bytes (if using a list of lists of integers in Python, which may actually take more memory, but Python's lists are stored as pointers, but for 1e6 elements, each is a small integer. However, even with 1e6 elements, it's manageable within the 256MB limit.

So the code should work.

Another possible optimization is to precompute the squares that each cell (x,y) can be part of, but perhaps the code as written is sufficient.

Now, implementing the code:

Read n and m.

Check if n <3 → output -1.

Else, proceed.

Initialize the counts array as (n-2)x(n-2) of zeros.

Then, for each step (from 1 to m):

Read x, y.

Compute i_min = max(1, x-2).

i_max = min(x, n-2).

j_min = max(1, y-2).

j_max = min(y, n-2).

If i_min >i_max or j_min >j_max → continue.

Loop i from i_min to i_max:

   loop j from j_min to j_max:

       counts[i-1][j-1] +=1.

       if counts[i-1][j-1] ==9:

           print(current step)

           exit.

After all steps, print -1.

Yes.

Now, code:

In Python:

n, m = map(int, input().split())

if n < 3:
    for _ in range(m):
        x, y = map(int, input().split())
    print(-1)
    exit()

# Initialize counts as (n-2) x (n-2) grid
counts = [[0]*(n-2) for _ in range(n-2)]

result = -1

for step in range(1, m+1):
    x, y = map(int, input().split())
    # Compute possible i range
    i_min = max(1, x - 2)
    i_max = min(x, n - 2)
    if i_min > i_max:
        continue  # no possible squares for rows
    # Compute possible j range
    j_min = max(1, y - 2)
    j_max = min(y, n - 2)
    if j_min > j_max:
        continue  # no possible squares for columns
    # Iterate over all possible (i,j)
    for i in range(i_min, i_max + 1):
        for j in range(j_min, j_max + 1):
            # Update counts for this square (i,j)
            # counts is 0-based, so i-1 and j-1
            row = i - 1
            col = j - 1
            counts[row][col] += 1
            if counts[row][col] == 9:
                print(step)
                exit()

print(-1)

Yes. Let's test this code with the first example.

Sample input 1:

4 11

Then 11 lines of cells. Let's see the steps. The 10th step is when the 10th cell is added.

In code, for each step from 1 to 11:

At step 10, when the cell (3,3) is added.

i_min = max(1, 3-2) =1.

i_max = min(3, 4-2) →2.

j_min = max(1,3-2)=1.

j_max = min(3,4-2)=2.

So loop i from 1 to 2, j from 1 to 2.

So squares (1,1), (1,2), (2,1), (2,2).

For each of these squares, increment the counts. Suppose after incrementing, one of them reaches 9.

So the code will output 10.

In the second example, after 12 steps, no square reaches 9, so output is -1.

This code should handle all cases correctly.

Another test case: n=3, m=9, and all 9 cells are in the 3x3 square.

Then the code should output 9.

Another test case: n=3, m=8, cells all in the square except one. Output -1.

So the code seems correct.
</think>

```python
n, m = map(int, input().split())

if n < 3:
    for _ in range(m):
        x, y = map(int, input().split())
    print(-1)
    exit()

counts = [[0] * (n - 2) for _ in range(n - 2)]

for step in range(1, m + 1):
    x, y = map(int, input().split())
    i_min = max(1, x - 2)
    i_max = min(x, n - 2)
    if i_min > i_max:
        continue
    j_min = max(1, y - 2)
    j_max = min(y, n - 2)
    if j_min > j_max:
        continue
    for i in range(i_min, i_max + 1):
        for j in range(j_min, j_max + 1):
            row = i - 1
            col = j - 1
            counts[row][col] += 1
            if counts[row][col] == 9:
                print(step)
                exit()

print(-1)
```