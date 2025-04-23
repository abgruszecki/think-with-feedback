<think>
Okay, let's tackle this problem. So, the task is to find the encrypted word in an African crossword by removing all letters that are repeated in their row or column. Then, we collect the remaining letters in a specific order. Hmm.

First, I need to understand the process. The steps are: for each cell in the grid, check if that character appears more than once in its row or column. If it does, we remove it. But all such letters are removed simultaneously. Then, after removing all such duplicates, the remaining letters are ordered from top to bottom, left to right. Oh right, the order is such that higher rows come first, and within the same row, left comes first.

So the main challenge is determining for each cell whether it is a duplicate in its row or column. Once we know which characters to keep (those that are unique in both their row and column), we collect them in the correct order.

But how do we efficiently check for duplicates in rows and columns?

Let's think about the approach. For each cell (i,j), the character is kept only if in row i, the count of that character is exactly 1, and similarly in column j, the count is exactly 1. Wait, no. Wait, the problem says that a letter is crossed out if the corresponding column OR row contains at least one more. Wait, the condition is that a letter is crossed out if the row contains at least one more (i.e., the character appears more than once in the row) OR the column contains at least one more. So the letter is kept only if it appears exactly once in the row AND exactly once in the column. Wait no: because the problem says "a letter should only be crossed out if and only if the corresponding column or row contains at least one more letter that is exactly the same." So, if a letter appears more than once in the row, or more than once in the column, it is crossed out. So the letters that remain are those that are unique in their row and unique in their column.

Wait, no. Wait, the problem statement says: "a letter should only be crossed out if and only if the corresponding column or row contains at least one more letter that is exactly the same." So the cross-out happens for a letter if either the row has at least one more (so count >=2 in row), or the column has at least one more (count >=2 in column). So a letter is kept only if in its row, it's unique (count is 1), and in its column, it's also unique (count is 1). Otherwise, it's crossed out.

So for each cell (i,j), we need to check whether in row i, the count of grid[i][j] is 1, and in column j, the count is 1. If both are true, then the character is kept. Otherwise, it's removed.

Wait, but how to compute this efficiently.

So, for each row, we can precompute the frequency of each character in that row. Similarly for each column. Then, for each cell, we look up the frequency of the character in its row and column. If both frequencies are 1, then we keep the character; otherwise, we discard it.

Yes, that's the way to go.

So the steps are:

1. Read the grid.

2. For each row, create a frequency map (like a Counter in Python) for that row.

3. For each column, create a frequency map for that column.

4. Then, iterate over each cell (i,j) in row-major order (top to bottom, left to right) and check if the character at (i,j) has a row count of 1 and column count of 1. If yes, include it in the result.

5. Collect all such characters in order and output as a string.

Now, the main thing is to compute the row and column frequencies efficiently.

In Python, for rows, it's straightforward. For each row, we can use collections.Counter to count the frequency.

For columns, since columns are vertical, we can loop through each column index j, collect all the characters in column j (from each row i), then count their frequencies.

Once we have these counts, then for each cell, the row's count for the character is row_counts[i][char], and similarly column_counts[j][char].

Wait, but for each row i, the row's frequency is stored as a dictionary. For example, row_counts[i] would be a Counter for row i. Similarly for columns.

So, for example, for row i, the count of grid[i][j] in row i is row_counts[i][grid[i][j]].

Similarly, the count in column j is column_counts[j][grid[i][j]].

So, for a cell (i,j) with character c, if row_counts[i][c] == 1 and column_counts[j][c] == 1, then we keep it.

So the steps are:

Read n and m.

Read the grid as a list of strings.

Compute row_counts for each row: a list of Counters.

Compute column_counts for each column: a list of Counters.

Then, iterate through each cell in row-major order (i from 0 to n-1, j from 0 to m-1), and check if row_counts[i][c] == 1 and column_counts[j][c] == 1. If yes, add to result.

Finally, print the concatenated result.

But in Python, for each row, creating a Counter is O(m) time. For n rows, that's O(n*m). For columns, each column has n elements. Creating a Counter for each of the m columns is O(m*n) as well. So overall, the time is O(nm), which is acceptable for n and m up to 100. So even for 100x100 grid, this is manageable.

But how to process columns? For example, for each column j, we can collect all grid[i][j] for i in 0..n-1, then make a Counter for that list.

So, for columns:

columns = []
for j in range(m):
    column = [grid[i][j] for i in range(n)]
    columns.append(column)
column_counts = [Counter(col) for col in columns]

Yes. That's O(nm) time.

Once that's done, for each cell (i,j), the character is grid[i][j], and in row_counts[i], the count is row_counts[i][c], and in column_counts[j], the count is column_counts[j][c].

So, putting it all together.

Now, edge cases: for example, when a row has all unique characters but the column has duplicates. Then the cell's character is only kept if both are unique.

Another example is when a row has duplicates but the column doesn't. Then the cell is crossed out.

But how to handle the counts correctly.

Testing with the first example:

Sample Input 1:

3 3

cba

bcd

cbc

The grid is:

Row 0: c b a

Row 1: b c d

Row 2: c b c

So row 0's counts: c:1, b:1, a:1. All 1.

Row 1: b:1, c:1, d:1. All 1.

Row 2: c:2, b:1.

So for each cell in row 0:

Check column counts.

For column 0: the column is [c, b, c]. So counts: c:2, b:1.

So cell (0,0) is 'c'. In row 0, count is 1, but column 0's count is 2. So it's crossed out.

Cell (0,1) is 'b'. Column 1 is [b, c, b]. Counts: b:2, c:1. So column count is 2. So crossed out.

Cell (0,2) is 'a'. Column 2 is [a, d, c]. Counts: a:1, d:1, c:1. So column count is 1. So row count is 1, column count is 1. So 'a' is kept.

For row 1:

Cell (1,0): 'b'. Column 0 has counts c:2. So column count is 2. So crossed out.

Cell (1,1): 'c'. Column 1's count for 'c' is 1 (since column 1 is [b, c, b], so 'c' appears once). So row count is 1, column count is 1. So kept.

Cell (1,2): 'd'. Column 2's count is 1. So kept.

Row 2:

Cell (2,0): 'c' → row count is 2, so crossed out.

Cell (2,1): 'b' → row count is 1 (row 2's count for 'b' is 1?), wait row 2 is 'c', 'b', 'c'. So 'c' appears twice, 'b' once. So row count for 'b' is 1. Column 1's count is 'b' appears 2 times (rows 0, 2). So column count is 2. So cell (2,1) is 'b', column count is 2 → crossed out.

Cell (2,2): 'c' → row count is 2, crossed out.

So the kept characters are (0,2) a, (1,1) c, (1,2) d, (2,1) b? Wait, no. Wait let's recheck.

Wait row 2's cell (2,1) is 'b'. Row count for 'b' is 1. Column 1's count for 'b' is 2. So column count is 2. So the cell is crossed out. So 'b' is not kept.

So the kept cells are:

(0,2) a → kept.

(1,1) c → row count is 1 (row 1: c appears once?), row 1 is 'bcd', so 'c' is at position 1. So row 1's count for 'c' is 1. Column 1's count for 'c' is 1 (column 1 is [b, c, b], so 'c' appears once). So both are 1. So 'c' is kept.

(1,2) d → row 1's count for 'd' is 1. Column 2's count for 'd' is 1 (column 2 is a, d, c. So d appears once). So kept.

So the result is a, c, d, and any others?

Wait let's check other cells. For row 0, j=2 is a. That's kept. For row 1, j=1 and j=2 are kept. Are there any others?

What about row 0, j=0 is c: row count 1, column count 2 → crossed.

Row 0, j=1 is b: row count 1, column count 2 (since column 1 is b, c, b → count 2 for b). So crossed.

Row 1, j=0 is b: column 0 count is c:2, b:1. So column count for b is 1. But row count for b is 1. So row count is 1, column count is 1. Wait row 1's count for b is 1? Because row 1 is 'bcd'. So 'b' appears once, 'c' once, 'd' once. So row count is 1. Column 0 is c, b, c. So 'b' appears once. So column count for 'b' in column 0 is 1. So cell (1,0) 'b' would have row count 1 and column count 1. So why isn't it kept?

Wait in the first sample input's output is 'abcd'. So let's see. The output includes a, b, c, d. So where does the 'b' come from?

Wait maybe I made a mistake in the analysis.

Wait sample input 1's output is abcd. Let's retrace.

Let me recheck all cells.

For each cell:

Row 0:

c (0,0): row count 1 (since row 0 is 'cba', c occurs once). Column 0 has ['c', 'b', 'c'], so count for c is 2. So row count 1, column count 2 → crossed.

b (0,1): row count 1 (row 0 has one 'b'). Column 1 is [b, c, b] → count 2. So column count 2 → crossed.

a (0,2): row count 1. Column 2 is [a, d, c] → a count 1. So both 1 → kept.

Row 1:

b (1,0): row count 1 (row 1 is 'bcd'). Column 0 count for 'b' is 1 (since column 0 has two c's and one b). So row count 1, column count 1 → kept. So 'b' is kept. Oh! So cell (1,0) is kept.

Wait wait, in row 1, the first character is 'b'. In row 1's row count, 'b' occurs once. Column 0's count for 'b' is 1. So both are 1. So cell (1,0) is kept. So 'b' is part of the result. Oh, that's where the 'b' comes from.

Ah! So my previous analysis was wrong. So I need to re-examine.

So for cell (1,0): row 1's count for 'b' is 1. Column 0's count for 'b' is 1. So both counts are 1. So this cell's 'b' is kept. Oh right! Because column 0 is c (from row 0), b (row 1), c (row 2). So in column 0, 'b' occurs once. So column count for 'b' is 1.

So that 'b' is kept. So the kept cells are:

(0,2) a → kept.

(1,0) b → kept.

(1,1) c → kept.

(1,2) d → kept.

Then, the order is from top to bottom, left to right. So (0,2) is first (row 0), then (1,0), (1,1), (1,2), and then any others in row 2.

Wait what about row 2's cells?

Row 2 is 'cbc'.

Cell (2,0): 'c' → row count 2 (since row 2 has two c's). So row count is 2 → crossed.

Cell (2,1): 'b' → row count 1 (row 2's count for 'b' is 1). Column 1's count is 2 (b, c, b). So column count is 2 → crossed.

Cell (2,2): 'c' → row count 2 → crossed.

So the kept cells are:

Row 0: (0,2) → a.

Row 1: (1,0) → b, (1,1) → c, (1,2) → d.

So the order is a, b, c, d → 'abcd' as in the sample output.

So that's why the code must include that cell (1,0) 'b' in the output.

So the key is to check for each cell whether the row's count and column's count for that specific character are both 1.

So in code, for each cell (i,j), c = grid[i][j]. If row_counts[i][c] == 1 and column_counts[j][c] == 1, then include in the result.

So the code steps:

Read n and m.

Read n lines, each line is a string of m characters. Let's call this grid.

Compute row_counts as a list of Counters for each row.

Compute column_counts as a list of Counters for each column.

Then, for each row i in 0 to n-1:

   for each j in 0 to m-1:

       c = grid[i][j]

       if row_counts[i][c] == 1 and column_counts[j][c] == 1:

           add c to the result string.

Finally, print the result.

Yes, that's the plan.

Now, in Python, for reading input, the first line is n and m. Then next n lines are the grid rows.

Then, for each row in grid, create a Counter. So row_counts = [Counter(row) for row in grid]

For columns, columns are created by taking the j-th character from each row. So columns = [[row[j] for row in grid] for j in range(m)]

Then, column_counts = [Counter(col) for col in columns]

Yes.

Now, in code:

n, m = map(int, input().split())

grid = [input().strip() for _ in range(n)]

from collections import Counter

row_counts = [Counter(row) for row in grid]

columns = []
for j in range(m):
    column = []
    for i in range(n):
        column.append(grid[i][j])
    columns.append(column)
column_counts = [Counter(col) for col in columns]

result = []
for i in range(n):
    for j in range(m):
        c = grid[i][j]
        if row_counts[i][c] == 1 and column_counts[j][c] == 1:
            result.append(c)

print(''.join(result))

Wait, but for the code, let's test with the first sample input.

Sample Input 1:

3 3

cba

bcd

cbc

row_counts:

row 0: Counter({'c':1, 'b':1, 'a':1})

row 1: Counter({'b':1, 'c':1, 'd':1})

row 2: Counter({'c':2, 'b':1})

column_counts:

column 0: ['c', 'b', 'c'] → Counter {'c':2, 'b':1}

column 1: ['b', 'c', 'b'] → Counter {'b':2, 'c':1}

column 2: ['a', 'd', 'c'] → Counter {'a':1, 'd':1, 'c':1}

So, for cell (1,0), c is 'b':

row_counts[1]['b'] is 1.

column_counts[0]['b'] is 1 (because in column 0, 'b' appears once). Because column 0's Counter is {'c':2, 'b':1}.

So both are 1 → included.

Similarly, other cells.

So code should produce 'abcd' as expected.

Now, another sample input:

Sample 2:

5 5

fcofd

ooedo

afaoa

rdcdf

eofsf

Output: codeforces.

So, code should process this correctly.

But let's see. The code's approach is correct.

Now, considering possible optimizations. Since n and m are up to 100, the code's O(nm) time is acceptable. For each row and column, we create a Counter. Then for each cell, two lookups in the Counter. Since Python's Counter uses dictionaries, which are O(1) lookups (average case), the total time is O(nm) which is manageable.

As for memory, for each row and column, storing a Counter. But each Counter can have up to m entries (for rows) and n entries (for columns). But for n and m up to 100, this is manageable.

So the code should work.

Now, possible edge cases: 1x1 grid. Since the code would check that the single cell's row count is 1 and column count is 1. So it's kept.

Another case: a row with all duplicates. For example, 2x2 grid with all 'a's. Then each cell is in a row and column with duplicates. So result is empty, but problem says answer is guaranteed to have at least one character.

So the code will output the correct empty string (but problem says that such cases are not present).

Another case: 1x5 grid. Each cell must be unique in the row (since row has 5 cells, but each row's count would be 1 only if all are unique). Then check for column counts. Since columns in this case are each a single cell. So column counts are all 1. So all characters in the row are kept only if they are unique in the row.

So for a row of 'abcde', all are kept.

For a row of 'aabba', then each 'a' appears 3 times, 'b' appears 2 times. So row counts are 3 for a, 2 for b. So all cells in this row would be crossed out. But since the problem says that answer has at least one character, this case is not possible.

So the code handles all possible cases.

Thus, the code is correct.
</think>

To solve this problem, we need to decode an encrypted word from an African crossword by removing letters that appear more than once in their respective row or column. The remaining letters are then concatenated in a specific order to form the encrypted word.

### Approach
1. **Problem Analysis**: The key insight is that a letter is kept only if it appears exactly once in both its row and column. This means we need to check the frequency of each letter in its respective row and column.
2. **Frequency Counting**: For each row and column, we count the frequency of each letter using a `Counter` from the `collections` module. This helps us efficiently determine if a letter is unique in its row and column.
3. **Result Construction**: After determining the frequency of each letter in its row and column, we iterate through each cell in the grid. If a letter is unique in both its row and column, it is added to the result string. The result is constructed by iterating through the grid in row-major order (top to bottom, left to right).

### Solution Code
```python
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

from collections import Counter

row_counts = [Counter(row) for row in grid]

# Prepare column data
columns = []
for j in range(m):
    column = []
    for i in range(n):
        column.append(grid[i][j])
    columns.append(column)
column_counts = [Counter(col) for col in columns]

result = []
for i in range(n):
    for j in range(m):
        c = grid[i][j]
        if row_counts[i][c] == 1 and column_counts[j][c] == 1:
            result.append(c)

print(''.join(result))
```

### Explanation
1. **Reading Input**: The grid dimensions and the grid itself are read from standard input.
2. **Row and Column Frequency Calculation**: Using the `Counter` class, we compute the frequency of each letter in every row and column. This allows us to quickly check if a letter is unique in its row and column.
3. **Constructing the Result**: By iterating through each cell in the grid, we check if the letter at that cell is unique in both its row and column. If it is, the letter is added to the result list.
4. **Output**: The result list is joined into a string and printed, forming the decrypted word.

This approach efficiently processes the grid in O(nm) time complexity, which is optimal given the constraints (n and m up to 100). The use of `Counter` ensures that frequency checks are done in constant time on average, making the solution both time and space efficient.