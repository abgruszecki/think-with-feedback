<think>
Okay, let's see. The problem is about determining if there's an even path between two cells in a grid. The grid is formed by R and C arrays where each cell (i,j) has value R_i + C_j. The path can only move to adjacent cells (up, down, left, right), and all cells along the path must be even.

Hmm, the key here is that all cells on the path must be even. So the first thing I need to figure out is the conditions under which a cell is even. Let's think about R_i + C_j being even. For this sum to be even, R_i and C_j must be of the same parity. Either both even or both odd. So R_i and C_j must have the same parity.

Wait, right. Because even + even = even, odd + odd = even. So for a cell (i,j) to be even, R_i and C_j must have the same parity. So the parity of R_i and C_j must match.

So the grid's parity structure is determined by the parities of R and C arrays. Each cell (i,j) can be considered as a node in a graph where edges are adjacent cells (i±1,j) and (i,j±1), but only if those adjacent cells are even. But building such a graph explicitly isn't feasible for N up to 1e5.

But maybe there's a pattern here. Let's think about how the parity of R and C affect the grid. For a cell (i,j) to be even, R_i and C_j must have the same parity. So the cell's parity is determined by the parities of R_i and C_j. Let's model each cell's parity as a pair (R_parity, C_parity). For the sum to be even, R_parity must equal C_parity.

So the grid cells can be divided into regions where adjacent cells are even and can form a path. But how?

Wait, let's think of the grid as a bipartite graph. Each cell (i,j) is even if R_i and C_j are of the same parity. So let's represent each cell by the parity of R_i and C_j. For example, if R_i is even and C_j is even, then it's even. Similarly for both odd. If R_i is even and C_j is odd, then the sum is odd, so the cell is invalid (not part of any even path).

So the valid cells are those where R_i and C_j have the same parity. So the parity of R_i and C_j must match. Now, the problem is that the path can only move through valid cells (even cells) and connect adjacent cells.

But how do these cells form connected regions? Let's see.

Suppose two cells (i,j) and (i+1,j) are adjacent. For both to be valid, R_i and C_j must have same parity, and R_{i+1} and C_j must have same parity. So R_i and R_{i+1} must have the same parity as C_j. Wait, but for both cells to be valid, R_i and C_j must have same parity, and R_{i+1} and C_j must have same parity. So R_i and R_{i+1} must have the same parity. Because if C_j's parity is p, then R_i must be p, and R_{i+1} must also be p. So R_i and R_{i+1} must have the same parity. Otherwise, moving down from (i,j) to (i+1,j) would result in a cell that is invalid (since R_{i+1} has different parity than C_j).

Wait, no. Let's take an example. Suppose R_i is even, C_j is even. So (i,j) is even. Then (i+1,j) is even only if R_{i+1} is even (since C_j is even). So if R_{i+1} is even, then (i+1,j) is even and can be part of the path. Otherwise, if R_{i+1} is odd, then (i+1,j) is odd and thus invalid. So to move vertically (from i to i+1), the R array must have the same parity in consecutive rows. Similarly for horizontal movement (from j to j+1), the C array must have same parity in consecutive columns.

So, for movement in the same row (i.e., left or right), the C array's parity for consecutive columns must be the same. Because when moving from j to j+1, the C_j and C_{j+1} must have same parity. Because, for cell (i,j) and (i,j+1) to be both even, R_i must have the same parity as C_j, and R_i must have same parity as C_{j+1}. Therefore, C_j and C_{j+1} must have same parity. Otherwise, if C_j is even and C_{j+1} is odd, then R_i would need to be even (for (i,j)) and also odd (for (i,j+1)), which is impossible. So in that case, adjacent cells in the same row would not be part of the same connected component.

Similarly, for movement in the same column (up or down), the R array's parity must be the same for consecutive rows. Because if moving from i to i+1, then R_i and R_{i+1} must have same parity. Otherwise, the cell (i+1,j) would have R_{i+1} + C_j. But since (i,j) is even, R_i and C_j have same parity. For (i+1,j) to be even, R_{i+1} and C_j must have same parity. So R_i and R_{i+1} must have same parity. Otherwise, the vertical movement would be impossible.

Therefore, the connected regions are determined by the parity runs in the R and C arrays. Let me think of it as:

Each valid cell (i,j) (where R_i and C_j have same parity) is part of a grid where the R array's parity changes in rows and the C array's parity changes in columns. So the connected regions are determined by the parity sequences of R and C.

For example, if in the R array, consecutive elements have the same parity, then moving up or down is allowed. Similarly, if consecutive elements in the C array have the same parity, moving left or right is allowed.

Wait, but the R array's parity for row i and i+1 must be the same to allow movement between those rows. So the R array's parity must form blocks where consecutive entries have the same parity. Similarly for the C array. 

So the connected regions would be determined by the maximal ranges in the R and C arrays where consecutive elements have the same parity. Let me see.

Suppose that in the R array, from row a to row b, all R_i have the same parity, and in the C array, from column c to column d, all C_j have the same parity. Then, in the rectangle a ≤ i ≤ b, c ≤ j ≤ d, all cells (i,j) where R_i's parity equals C_j's parity (which, since R_i is same in a-b, and C_j same in c-d, then if R_a's parity is same as C_c's parity, then all cells in this rectangle are valid. Otherwise, none are valid. But I think that's not the case. Wait, no. For example, if R has all even parities, and C has all even parities, then all cells are valid. If R is even and C is even, then all cells are valid. But if R is even and C is odd, then no cells are valid. But in the problem statement, the starting and ending cells are guaranteed to be even, so their R and C have same parity.

So, the connected regions are determined by the parities of R and C arrays. Let's model this.

Each valid cell (i,j) must have R_i and C_j with same parity. Now, even if two cells are adjacent, whether they are connected depends on the parity of their R and C arrays.

But movement between two adjacent cells (i,j) and (i,j+1) requires that both are even. For (i,j) to be even: R_i and C_j same parity. For (i,j+1) to be even: R_i and C_{j+1} same parity. So, for both to be even, C_j and C_{j+1} must have the same parity. Because R_i's parity is fixed (for the same row i). So, if C_j and C_{j+1} have different parity, then (i,j) and (i,j+1) cannot both be even, so you can't move between them. Similarly for moving between rows: if R_i and R_{i+1} have different parity, then you can't move from (i,j) to (i+1,j), because even if (i,j) is even (R_i and C_j same), (i+1,j) requires R_{i+1} and C_j same. If R_i and R_{i+1} have different parity, then C_j must have parity same as R_i (for (i,j) to be even), but then R_{i+1} has different parity, so (i+1,j) would be R_{i+1} + C_j, which would be R_i's parity (from C_j) plus R_{i+1}'s parity, which is different. So their sum is odd, thus (i+1,j) is invalid. So movement between rows i and i+1 is possible only if R_i and R_{i+1} have same parity.

So, the connected regions are determined by the maximal intervals in R and C where consecutive elements have the same parity. So, for each row i, the R array can be partitioned into intervals where consecutive elements have the same parity. Similarly for C in columns.

Wait, perhaps another approach. For a cell (i,j) to be part of an even path, the entire path must consist of cells where R and C parities match. So, movement is allowed only in directions where the adjacent cell is even. So, the connected component of (i,j) is the set of all cells (x,y) such that:

1. R_x and C_y have the same parity (so (x,y) is even).
2. (x,y) is reachable from (i,j) via moving through cells that satisfy condition 1 and adjacency.

So, how to model these connected components efficiently?

The key insight is that the connected components are determined by the parity runs in R and C arrays. Let me think:

For movement in the same row (i), moving left or right requires that the C array's parity in consecutive columns are the same. So, the C array's parity must be the same for j and j+1. So, in the C array, consecutive elements must have the same parity for movement in the same row. Similarly, for movement in the same column (j), consecutive elements in R array must have same parity.

Therefore, the connected component for a cell (i,j) can be determined by:

- The range of rows around i where R's parity is the same as R_i, and consecutive rows in this range also have the same parity (so you can move up and down through them).
- The range of columns around j where C's parity is the same as C_j, and consecutive columns in this range also have the same parity (so you can move left and right through them).

Wait, perhaps the connected component for (i,j) is the set of all cells (x,y) where:

- R_x has the same parity as R_i, and the path from x to i in the R array allows movement (i.e., consecutive Rs in the path have the same parity).
- C_y has the same parity as C_j, and the path from y to j in the C array allows movement (i.e., consecutive Cs in the path have the same parity).

But that's not entirely accurate. Because the movement could involve combining row and column steps. For example, moving up then right, etc. But perhaps the connected component is determined by the intersection of the row runs and column runs.

Alternatively, think of the connected component as the rectangle formed by the maximal row interval and column interval where:

- All R's in the row interval have the same parity as R_i.
- All C's in the column interval have the same parity as C_j.
- The row interval is a contiguous block where consecutive R's have the same parity (so you can move up and down through them).
- The column interval is a contiguous block where consecutive C's have the same parity (so you can move left and right through them).

Wait, perhaps not. Let's think of R as a series of blocks where consecutive elements have the same parity. For example, if R is [even, even, even, odd, odd], then the row blocks are the first three rows (even), then next two (odd). Similarly for C.

Each block in R and C is a maximal interval where consecutive elements have the same parity. So for row i, it's part of a row block R_block. For column j, it's part of a column block C_block.

Then, the connected component for (i,j) would be all cells (x,y) where x is in R_block and y is in C_block, and R_x's parity is same as C_y's parity. Because:

- To move between rows in R_block, since consecutive rows have same parity, you can move vertically.
- To move between columns in C_block, since consecutive columns have same parity, you can move horizontally.
- Then, any cell within this rectangle (R_block x C_block) that has R_x and C_y with same parity would be reachable.

But how about the parity condition? Let's see. For example, suppose R_block's parity is p (even or odd), and C_block's parity is q. Then, for a cell (x,y) in R_block x C_block, R_x's parity is p and C_y's parity is q. So their sum is even only if p == q. Therefore, all cells in R_block x C_block where p == q are valid and connected. Otherwise, no cells in that block are valid.

Wait, that's an important point. Because R_block has all R's with parity p. C_block has all C's with parity q. So for a cell (x,y) in R_block x C_block, R_x is p, C_y is q. So sum is p + q. So the cell is even only if p == q. So, in that case, all cells in R_block x C_block are even. Otherwise, none are. 

But the starting and ending cells are guaranteed to be even, so their R and C's parities are the same. So, for the query to be possible, the R_block of (r_a, c_a) and C_block of (r_a, c_a) must have p == q, and similarly for (r_b, c_b). Then, the connected component would be the entire R_block x C_block. So, to have a path from (ra, ca) to (rb, cb), they must be in the same connected component, which is the R_block x C_block where their row and column blocks are the same.

Wait, but in the example given in the problem:

Sample Input 1:

R = [6,2,7,8,3] → parities are even, even, odd, even, odd.

C = [3,4,8,5,1] → parities are odd, even, even, odd, odd.

So for each cell (i,j):

Check R_i's parity and C_j's parity. The cell is even if they are same.

For example, cell (2,2) → R_2 is even (2), C_2 is even (4). So even. The row block for i=2: R array is [even, even, odd, even, odd]. So the row blocks for R are:

Rows 1-2 (even), then row 3 (odd), rows 4 (even), row5 (odd).

The column blocks for C: C array parities are odd (j=1), even (j=2-3), odd (j=4-5).

So for cell (2,2), R_block is rows 1-2 (even), C_block is columns 2-3 (even). So the connected component is R_block (rows 1-2) x C_block (cols 2-3). But in this rectangle, all R_i are even and C_j are even, so all cells here are even. So cells (1,2), (1,3), (2,2), (2,3) are part of the same connected component.

But in the query (2,2) to (1,3), these are within the same connected component, so the answer is YES.

Another example in the first sample is query (4,2) to (4,3):

Looking at R[4] which is 8 (even), C[2] is 4 (even) → cell (4,2) is even. C[3] is 8 (even) → cell (4,3) is even. Now, what is the connected component for (4,2)?

Row 4 is in R_block of row4 (even). But R_block for row4 is rows 4, since row4 is even and row5 is odd. So R_block is row4. C_block for column2 is columns 2-3 (even). So connected component is row4 x columns2-3. So (4,2) and (4,3) are in the same row and same C_block, so moving right is possible. Hence path exists.

So for two cells to be connected, their row blocks and column blocks must form a connected component where:

- The row blocks of their positions are connected (i.e., same row block or part of a sequence where row blocks can be traversed via adjacent rows with same parity).
- Similarly for the column blocks.

Wait, no. Wait, in the first example, for cell (2,2), the row block is rows 1-2 (even), and column block is 2-3 (even). So the connected component is the rectangle rows 1-2, columns 2-3, and all cells there are even. So any two points in that rectangle can be reached via moving through adjacent cells, as long as the row and column blocks are connected.

So the connected components are rectangles formed by the maximal row and column blocks where R's parity in the row block and C's parity in the column block are the same.

Thus, two cells (ra, ca) and (rb, cb) are connected if and only if:

1. The row block of ra and the row block of rb are in the same row group (i.e., the row blocks are part of a contiguous region where consecutive rows have the same parity, and thus can be traversed vertically).
2. The column block of ca and cb are in the same column group (i.e., the column blocks are part of a contiguous region where consecutive columns have the same parity, and can be traversed horizontally).
3. Additionally, the row block's parity must match the column block's parity (since the cells must be even).

Wait, but the row block's parity is the parity of R in that block, and the column block's parity is the parity of C in that block. For the cells in their product to be even, the row's parity and column's parity must be the same. So if the row block's parity is p and column block's parity is q, then p must equal q for any cell in their product to be even. So for a cell (i,j) to be even, it must be in a row block with parity p and column block with parity p.

So, the connected component of (i,j) is the union of all (x,y) where x is in the row block of i, y is in the column block of j, and the row block's parity equals the column block's parity. So, if the row block and column block have same parity, then all cells in their product are valid and connected via movement (since moving up/down within row block is allowed, and left/right within column block is allowed). Otherwise, (i,j) is a single cell (if no adjacent cells are valid).

Wait, but how are these row and column blocks connected? For example, if a row block spans multiple rows (like rows 1-2 in the first example), and a column block spans multiple columns (columns 2-3), then all cells in those ranges with same parity (even and even in this case) are connected. So the connected component is a rectangle of rows 1-2 and columns 2-3, and you can move freely within this rectangle.

So for two cells to be in the same connected component, they must be in the same row group and column group (i.e., their row blocks and column blocks form a product where the parities are the same, and the row and column groups are contiguous and allow movement).

But how do you determine if two cells are in the same connected component? The key is that their row blocks must be part of the same contiguous row group (i.e., the row blocks are consecutive and have the same parity) and the column blocks must be part of the same contiguous column group (same parity and consecutive).

Wait, perhaps not. Let's think again. The row blocks are maximal sequences of consecutive rows where each row has the same parity as the next. For example, if R is even, even, even, then the row block is 1-3. Then, moving up and down within this row block is allowed. So for a cell (i,j) in a row block, any cell (k,j) in the same row block can be reached by moving vertically, provided that the column j is in a column block that allows horizontal movement (i.e., consecutive columns in the same parity as the column block).

So, the connected component is determined by the row group (maximal row blocks with same parity) and column group (maximal column blocks with same parity). But in order for a cell (i,j) to be valid, the row group's parity and column group's parity must be the same. Otherwise, the cell is invalid (so even if it's part of the row and column group product, it's not a valid cell).

So, the connected component for a valid cell (i,j) is the entire product of its row group and column group, provided that the row group's parity and column group's parity are the same. If they are not the same, then (i,j) is a single-cell component (but according to the problem statement, the starting and ending cells are guaranteed to be even, so their row and column group parities must be the same).

So, for two cells to be connected, they must be in the same row group and the same column group. Because their row groups and column groups must be connected such that the row group's parity equals the column group's parity. Wait, but if two cells are in different row groups or column groups, but those groups are adjacent and have the same parity, then perhaps they are connected?

No, because row groups are maximal. For example, if R has even, even, even, then the row group is 1-3. If the next row is odd, then the next row group is 4. So, movement between row groups is not possible. Because to move from row 3 (even) to 4 (even?), but in this example, row 4 is even (assuming R[4] is even). Wait, no. Wait, row group is determined by consecutive same parity. So, if rows 1-3 are even, row4 is even, then row group is 1-4. So row groups are determined by consecutive elements with same parity.

So, row groups are formed by consecutive rows where each consecutive pair has the same parity. So, the row groups are sequences where R_i and R_{i+1} have the same parity.

Similarly for column groups.

So, the row groups are a partition of the rows into maximal intervals where consecutive rows have same parity. Similarly for column groups.

Now, the connected component of a cell (i,j) is the product of the row group containing i and the column group containing j, provided that the parity of the row group and column group are the same. Because only then, all cells in that product are even.

Thus, for two cells (a,b) and (c,d) to be connected:

- The row group of a must be the same as the row group of c. Because if they are in different row groups, then there's no path that connects them via vertical movement (since adjacent rows in different row groups have different parity, which breaks the vertical movement).

Wait, but suppose that the row groups are adjacent but have the same parity. Wait, no. Because row groups are maximal. So consecutive row groups must have different parities. Because if two adjacent row groups have the same parity, they would have been merged into a single group. So row groups are separated by changes in parity.

Thus, row groups are sequences of consecutive rows with same parity, and adjacent row groups have different parities.

Similarly for column groups.

Therefore, the row group for a and c must be the same. Because otherwise, you cannot move between them via vertical steps. Similarly, the column groups for b and d must be the same. Because otherwise, you cannot move between them via horizontal steps.

So, the conclusion is:

Two cells (ra, ca) and (rb, cb) are connected via an even path if and only if:

1. The row group of ra and rb is the same.
2. The column group of ca and cb is the same.
3. The parity of the row group and column group is the same (which is guaranteed for the start and end points as per problem statement).

Wait, but according to the problem statement, the start and end cells are even, which implies that their row group and column group's parity is the same. So condition 3 is already satisfied.

Thus, the problem reduces to checking whether the row group of ra is the same as that of rb, and the column group of ca is the same as that of cb.

Wait, but in the first example:

The first query is (2,2) to (1,3). The row group of 2 is rows 1-2 (even parity). The row group of 1 is the same. The column group of 2 is columns 2-3 (even parity), and column group of 3 is same. So same row group and same column group. So output is YES.

In the second query (4,2) to (4,3). Row group of 4 is rows 4 (even). So both are in the same row group. Column group of 2 is 2-3 (even), column group of 3 is same. So same column group. So YES.

Third query (5,1) is row 5 (parity is 3, which is odd). Column group of 1 is columns 1 (odd). So their row group and column group parity is same (both odd), so cell (5,1) is even. Now, the row group is 5 (single row). Column group is 1 (single column). So to reach (3,4), which has row group 3 (row3 is odd), column group 4 (columns4-5, which are odd). But row group of 5 and 3 are different (since they are not in the same row group). So, no path exists.

So, the solution is to precompute for each row and column their group (the start and end indices of their group). Then, for a query, check if the two cells are in the same row group and same column group.

Wait, but how to compute the row groups and column groups?

Yes. For rows, we can precompute for each row i the start and end indices of the group it belongs to. Similarly for columns.

For example, for the R array:

R_parities = [r%2 for r in R]

Then, the row groups can be determined by finding runs of the same parity. For each i, group_row_start[i] and group_row_end[i] indicate the start and end indices of the group that row i is in.

Similarly for the C array.

Once we have these group start and end indices, for a query (ra, ca, rb, cb), we check:

group_row_start[ra-1] == group_row_start[rb-1] (since rows are 1-based in the input but 0-based in the array) and group_col_start[ca-1] == group_col_start[cb-1].

If both are true, then the two cells are in the same row group and same column group, hence connected. Otherwise, no.

Because:

- Being in the same row group means that you can move vertically between ra and rb (as the group is contiguous and consecutive rows have same parity).
- Being in the same column group means you can move horizontally between ca and cb.
- Since the parities are same (due to the cells being even), the entire product is connected.

Thus, the solution is to precompute for each row and column their group start and end indices, then for each query, check if the row group of ra and rb are the same, and column group of ca and cb are the same.

So the steps are:

1. Preprocess the R array to create for each row i (1-based), the start and end indices of its row group (0-based in the array). Similarly for C array.

2. For each query (ra, ca, rb, cb), check if:

   a. The row group of ra and rb is the same (i.e., group_row_start[ra-1] == group_row_start[rb-1])

   b. The column group of ca and cb is the same (group_col_start[ca-1] == group_col_start[cb-1])

If both are true, output YES. Else, NO.

This approach is O(N) for preprocessing and O(1) per query, which is feasible for N and Q up to 1e5.

Now, the key is to compute the group start and end indices for each row and column.

How to compute this:

For the R array:

Initialize group_start for each row.

We can iterate through R_parities from left to right. When the parity changes, we start a new group. For each position i, group_start[i] is the start of the current group, and group_end[i] is the end.

For example:

R_parities = [0,0,1,0,1]

Processing:

i=0: group starts at 0.

i=1: same as i=0, same group.

i=2: different parity, new group starts at 2.

i=3: different parity from i=2, new group starts at 3.

i=4: same as i=3? No, i=3 is 0, i=4 is 1. So new group starts at 4.

So group_start array is [0,0,2,3,4], group_end array is [1,1,2,3,4].

Wait, how to compute this.

Let's code it:

group_start = [0]*n
current_start = 0
for i in 1 to n-1:
    if R_parity[i] != R_parity[i-1]:
        current_start = i
    group_start[i] = current_start

Wait, for the first element (i=0), group_start[0] = 0.

For i >=1:

if current parity is same as previous, group_start[i] = current_start.

else, current_start = i, group_start[i] = current_start.

Similarly for group_end:

group_end[i] will be the maximum index in the group.

But perhaps for each i, group_start[i] and group_end[i] can be stored. But perhaps group_start is sufficient. Because two elements are in the same group if their group_start is the same.

For example, in the first group, group_start is 0 for i=0 and 1. So group_start array would be [0,0,2,3,4]. So, for any i, group_start[i] is the start of the group. The end can be found as the next group_start minus 1, or until the end of the array.

But for our purpose, to determine if two rows are in the same group, we just need their group_start to be equal. Because each group is a contiguous block.

Wait, no. Because the group_start[i] is the same for all elements in the same group. For example, group_start[i] for i=0 and 1 are 0. So, if two rows have the same group_start, they are in the same group.

Yes.

So, for rows i and j, if group_start[i] == group_start[j], then they are in the same row group.

Similarly for columns.

So, the steps to compute group_start for R and C are:

For R:

n = len(R)
group_start_R = [0] * n
current_start = 0
for i in range(1, n):
    if R[i] % 2 != R[i-1] % 2:
        current_start = i
    group_start_R[i] = current_start
group_start_R[0] = 0  # already handled

Wait, no, for i=0, group_start_R[0] is 0. For i=1, compare with i=0. So the code can be:

current_start = 0
group_start_R[0] = current_start
for i in range(1, n):
    if R[i] % 2 != R[i-1] % 2:
        current_start = i
    group_start_R[i] = current_start

Same for C.

Once we have group_start_R and group_start_C, then for each query:

ra, ca, rb, cb = input (1-based)

convert to 0-based:

ra -= 1
ca -= 1
rb -= 1
cb -= 1

Check:

if group_start_R[ra] == group_start_R[rb] and group_start_C[ca] == group_start_C[cb]:
    output YES
else:
    output NO

But wait, what if the row group for ra and rb is different, but there's a way to move through column groups? No, because movement is only allowed between adjacent cells in the same group.

Wait, the row groups are such that consecutive groups have different parities. So, if two rows are in different row groups, their parities are different, so you can't move vertically between them. Thus, any path between two cells in different row groups would have to find a way through other row groups, but since adjacent groups have different parities, this is impossible.

Thus, the only way for two cells to be connected is if they are in the same row group and same column group.

So this approach works.

Let's test the sample input.

First sample:

R = [6, 2,7,8,3] → parities [0,0,1,0,1]

Processing group_start_R:

i=0: group_start[0] =0

i=1: parity same as i=0 (0 vs 0), so group_start[1] =0.

i=2: parity 1 (7%2=1) vs i=1 (0). Different. current_start =2. group_start[2] =2.

i=3: parity 0 (8%2=0) vs 1. Different. current_start=3. group_start[3] =3.

i=4: parity 1 (3%2=1) vs 0. Different. current_start=4. group_start[4] =4.

So group_start_R is [0,0,2,3,4].

For columns:

C = [3,4,8,5,1] → parities [1, 0,0,1,1]

group_start_C:

i=0: 1 → group_start[0] =0.

i=1: 0 vs 1 → different. current_start=1. group_start[1] =1.

i=2: 0 vs 0 → same. group_start[2] =1.

i=3:1 vs 0 → different. current_start=3. group_start[3] =3.

i=4:1 vs 1 → same. group_start[4] =3.

So group_start_C is [0, 1,1,3,3].

Now, first query: (2,2) → (0-based (1,1)) and (1,3) → (0-based (0,2)).

Check group_start_R[1] (ra=1) is 0. group_start_R[0] (rb=0) is 0. Same row group.

group_start_C[1] (ca=1) is 1. group_start_C[2] (cb=2) is 1. Same column group. So YES.

Second query: (4,2) → (3,1) and (4,3) → (3,2).

row group for 3 is group_start_R[3] =3. row group for 3 is 3. Same.

column group for 1 (group_start_C[1] =1) and 2 (group_start_C[2] =1). Same. So YES.

Third query: (5,1) → (4,0) and (3,4) → (2,3).

group_start_R[4] is 4. group_start_R[2] is 2. Different → NO.

Which matches the sample.

Second sample:

Sample input 2:

3 2
30 40 49 → R parities [0,0,1]
15 20 25 → C parities [1,0,1]

group_start_R:

i=0: 0.

i=1: same as 0 (0). group_start[1] =0.

i=2: different. group_start[2] =2.

group_start_R is [0,0,2].

group_start_C:

i=0: 1. group_start[0] =0.

i=1: 0 vs 1. different. group_start[1] =1.

i=2: 1 vs 0. different. group_start[2] =2.

So group_start_C is [0,1,2].

Queries:

First query: (2,2) to (3,3) → 0-based (1,1) to (2,2).

group_start_R[1] is 0. group_start_R[2] is 2. Different → NO.

Second query: (1,2) → (0,1) and (2,2) → (1,1).

group_start_R[0] is 0, group_start_R[1] is 0. Same.

group_start_C[1] (1-based 2 is 0-based 1) is 1. group_start_C[1] (1-based 2) is 1. Same. So YES.

Thus, the code would correctly output the samples.

So the plan is:

- Precompute group_start_R and group_start_C.

- For each query, check if the group_start for the rows are the same, and group_start for columns are the same.

Thus, the code in Python would read as follows.

Now, considering the constraints: N up to 1e5, Q up to 1e5.

We need to read the R and C arrays, compute their group starts.

In Python, for N=1e5, this is manageable.

Implementing group_start_R:

We can process R in O(N) time. Similarly for C.

Then, for each query, O(1) time.

Now, the code:

Read N and Q.

Read R as list of integers.

Compute group_start_R:

group_start_R = list of length N.

group_start_R[0] =0.

current_start =0.

for i in 1 to N-1:

   if R[i]%2 != R[i-1]%2:

       current_start =i

   group_start_R[i] = current_start.

Similarly for C.

Then, for each query:

ra, ca, rb, cb (all 1-based).

Convert to 0-based: ra -=1, ca -=1, rb -=1, cb -=1.

Check if group_start_R[ra] == group_start_R[rb], and group_start_C[ca] == group_start_C[cb]. If yes, output YES else NO.

This should work.

Now, the code:

Read N and Q.

Read R array.

Read C array.

Compute group_start_R and group_start_C.

Then process each query.

Edge cases to consider:

- All rows are in the same group (all R have same parity).

- All columns are in the same group.

- Rows have alternating parities (e.g., 0,1,0,1...).

But the code should handle all cases.

Now, code in Python:

But note that in Python, for 1e5 elements, building lists is okay.

But in the code, group_start_R and group_start_C can be built as follows.

Sample code:

n, q = map(int, input().split())
R = list(map(int, input().split()))
C = list(map(int, input().split()))

# Compute group_start_R
group_start_R = [0]*n
current_start = 0
for i in range(1, n):
    if (R[i] %2) != (R[i-1] %2):
        current_start = i
    group_start_R[i] = current_start

# Compute group_start_C
group_start_C = [0]*n
current_start =0
for i in range(1, n):
    if (C[i] %2) != (C[i-1] %2):
        current_start = i
    group_start_C[i] = current_start

# Process queries
for _ in range(q):
    ra, ca, rb, cb = map(int, input().split())
    # Convert to 0-based
    ra -=1
    ca -=1
    rb -=1
    cb -=1
    if group_start_R[ra] == group_start_R[rb] and group_start_C[ca] == group_start_C[cb]:
        print("YES")
    else:
        print("NO")

This code should handle all test cases.

Testing sample input 1:

Sample Input 1:

5 3

6 2 7 8 3 → R parities [0,0,1,0,1]

group_start_R:

i=0:0

i=1: same as 0 → group_start[1] =0.

i=2: 1 != 0 → group_start[2]=2.

i=3: 0 != 1 → group_start[3]=3.

i=4:1 !=0 → group_start[4]=4.

C array:

3 4 8 5 1 → parities [1,0,0,1,1]

group_start_C:

i=0:0.

i=1:0 !=1 → group_start[1]=1.

i=2:0 ==0 → group_start[2] =1.

i=3:1 !=0 → group_start[3]=3.

i=4:1 ==1 → group_start[4]=3.

So group_start_C is [0,1,1,3,3].

For query 2 2 1 3 → 0-based (1,1) → group_start_R[1] =0; (0,2) → group_start_R[0] =0. So row groups same.

group_start_C[1] =1 and group_start_C[2] =1. Same column group. YES.

Second query: 4 2 → (3,1). group_start_R[3] =3. rb is 3 (4-1=3). So same row group. group_start_C[1] =1. cb is 4,3 → (3,2). ca is 1 (2-1=1), cb is 3-1=2. group_start_C[1] is 1, group_start_C[2] is 1. So YES.

Third query: (5,1) → (4,0). group_start_R[4] =4. (3,4) → (2,3). group_start_R[2] =2. So different. No.

Sample 2:

Sample Input 2:

3 2

30 40 49 → R parities [0,0,1]

group_start_R:

i=0:0.

i=1:0 same as previous → 0.

i=2:1 different → group_start[2] =2.

C is 15,20,25 → parities [1,0,1].

group_start_C:

i=0:0.

i=1:0 !=1 → group_start[1] =1.

i=2:1 !=0 → group_start[2] =2.

First query: 2,2 → (1,1). group_start_R[1] =0. 3,3 → (2,2). group_start_R[2] =2. So row groups differ. Output NO.

Second query: 1,2 → (0,1). group_start_R[0] =0. 2,2 → (1,1). group_start_R[1] =0. Same row group. column group (1,1) → group_start_C[1] =1. (1,1) → group_start_C[1] =1. So YES.

Thus, the code works.
</think>

```python
n, q = map(int, input().split())
R = list(map(int, input().split()))
C = list(map(int, input().split()))

group_start_R = [0] * n
current_start = 0
for i in range(1, n):
    if (R[i] % 2) != (R[i-1] % 2):
        current_start = i
    group_start_R[i] = current_start

group_start_C = [0] * n
current_start = 0
for i in range(1, n):
    if (C[i] % 2) != (C[i-1] % 2):
        current_start = i
    group_start_C[i] = current_start

for _ in range(q):
    ra, ca, rb, cb = map(int, input().split())
    ra -= 1
    ca -= 1
    rb -= 1
    cb -= 1
    if group_start_R[ra] == group_start_R[rb] and group_start_C[ca] == group_start_C[cb]:
        print("YES")
    else:
        print("NO")
```