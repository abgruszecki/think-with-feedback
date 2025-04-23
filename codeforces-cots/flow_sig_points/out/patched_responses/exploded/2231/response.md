<think>
Okay, let's try to figure out this problem. So the task is to find the optimal point on the grid of dividing lines (intersections) where Yura should stand so that the total time to guess all cars is minimized. The total time is calculated as the sum over all cars of c_ij multiplied by the square of the distance from Yura's point to the center of the car's square.

First, I need to understand the structure of the parking lot. Each square is 4x4 meters, right? The coordinates (i,j) for squares start at (1,1) in the northwest corner. The dividing lines are numbered from 0 to n (north to south) and 0 to m (west to east). So each intersection point is (li, lj), which are the line numbers. For example, the intersection between line i (north-south) and line j (east-west) is (i,j).

The center of each square (i,j) is located at a specific point. Let's think: each square is 4x4. The square (i,j) is bounded by lines (i-1) and i in the north-south direction, and lines (j-1) and j in the east-west direction. So the center of square (i,j) would be at ( (i-1)*4 + 2 , (j-1)*4 + 2 ) meters? Wait, no. Wait, the parking lot is 4n meters long north-south and 4m meters wide east-west. The dividing lines split this into n rows (each 4m wide) and m columns (each 4n long?), no, wait. Wait, the parking lot's dimensions: 4n meters from north to south (length) and 4m from west to east (width). So dividing lines run along the north-south direction (from west to east) and east-west direction (from north to south). Hmm, maybe I need to model this as a grid where each square is 4m wide (east-west) and 4n long (north-south), but that doesn't make sense. Wait, perhaps each square is 4x4 meters. So the lines are spaced 4 meters apart. For example, n+1 lines dividing the parking lot into n sections north-south, each 4 meters. So the total north-south length is 4n meters. Similarly, m+1 lines dividing into m sections east-west, each 4 meters. So each square is 4x4 meters.

So the dividing lines are spaced 4 meters apart. So the lines for the north-south direction (the horizontal ones, perhaps) are numbered 0 to n. For example, the northernmost line is 0, then each subsequent line is 4 meters south. So the vertical lines (east-west) are numbered 0 to m. So each intersection point (li, lj) is located at (4*li, 4*lj) meters from the northwest corner? Wait, no. Wait, the parking lot is 4n meters long (north-south) and 4m meters wide (east-west). The dividing lines run along north-south (vertical lines) and east-west (horizontal lines). The vertical lines (west-east) are numbered from 0 to m. Each vertical line is spaced 4 meters apart in the east direction. So between line j-1 and j is 4 meters. Similarly, the horizontal lines (north-south) are numbered from 0 to n, each 4 meters apart.

Wait, maybe the horizontal lines (running east-west) are the ones that determine the north-south position. So horizontal line 0 is the northern edge of the parking lot. Then line 1 is 4 meters south, up to line n, which is the southern edge. So the vertical lines (north-south) are spaced 4 meters east. So each square is between two horizontal lines (i-1 and i) and two vertical lines (j-1 and j), forming a 4x4 square. The center of this square (i,j) would then be at ( (i-1)*4 + 2, (j-1)*4 + 2 ), where the x-coordinate is east-west (so vertical lines) and y is north-south (horizontal lines). Wait, but wait, maybe the coordinates are such that the x is the east-west direction and y is north-south, but the problem's note says the first test case's sample output is (1,1), and the total time is computed based on distances.

Alternatively, perhaps the center of the square (i,j) is located at (2 + 4*(i-1), 2 + 4*(j-1)) meters from the origin (the northwest corner). Wait, no. Because if the square (i,j) is bounded by horizontal lines i-1 and i (north to south), each 4 meters apart. So the center is halfway between those lines. So the y-coordinate (north-south direction) for the center would be ( (i-1)*4 + 4/2 ) = (i-1)*4 + 2. Similarly, the x-coordinate (east-west direction) would be (j-1)*4 + 2. So the center is at ( (j-1)*4 + 2, (i-1)*4 + 2 ), assuming that the x is east-west and y is north-south. But when considering the position where Yura stands, (li, lj) is an intersection of lines. So his position would be at (4*lj, 4*li) meters from the northwest corner. Wait, because the vertical lines (east-west) are numbered from 0 to m. For example, vertical line 0 is the westernmost, then each 4 meters east. So the x-coordinate for line j is 4*j meters. Similarly, horizontal lines (north-south) are numbered from 0 to n. Each horizontal line is 4*i meters south from the northern edge. So the y-coordinate for line i is 4*i meters. So the intersection (li, lj) is at (4*lj, 4*li) meters from the northwest corner. Then the center of square (i,j) is at (4*(j-1)+2, 4*(i-1)+2) meters. So the distance between Yura's position (x, y) = (4*lj, 4*li) and the center of square (i,j) is sqrt( (4*lj - (4*(j-1)+2))^2 + (4*li - (4*(i-1)+2))^2 ). But squaring that gives ( (4(lj - (j-1) - 0.5))^2 + (4(li - (i-1) - 0.5))^2 ) which is 16*( (lj -j + 0.5)^2 + (li -i + 0.5)^2 ). The square of the distance is 16*( ... ), and then multiplied by c_ij. So the total time is sum over all squares (i,j) of c_ij * 16 * [ (lj - (j-0.5))^2 + (li - (i-0.5))^2 ].

Wait, perhaps simplifying variables would help. Let me define variables for the positions. Let me consider li and lj as the chosen coordinates. For each square (i,j), the center is at (x_j, y_i), where x_j = 4*(j-1) + 2, and y_i = 4*(i-1) + 2. Wait no, wait: j is the column index. For square (i,j), the vertical lines are j-1 and j (east-west direction), so the x-coordinate (east direction) is 4*(j-1) + 2 (since it's 2 meters from the left edge of the square). Similarly, the y-coordinate (south direction) is 4*(i-1) + 2. But Yura's position is at (4*lj, 4*li) meters from the origin. So the distance squared between Yura's point and the center is (4*lj - x_j)^2 + (4*li - y_i)^2.

Substituting x_j and y_i:

x_j = 4*(j-1) + 2 = 4j - 4 + 2 = 4j - 2.

Similarly, y_i = 4i - 2.

So the distance squared is (4*lj - (4j -2))^2 + (4*li - (4i-2))^2.

Simplify each term:

For the x-direction:

4*lj - (4j -2) = 4(lj -j) + 2.

Similarly for the y-direction: 4(li -i) +2.

So squared distance is [4(lj -j) +2]^2 + [4(li -i) +2]^2.

Expanding each term:

[4(lj -j) +2]^2 = 16(lj-j)^2 + 16(lj-j) +4.

Similarly for the other term.

So the squared distance becomes:

16[(lj-j)^2 + (li -i)^2] + 16[(lj-j) + (li -i)] + 8.

Wait, perhaps that's correct. But maybe there's a better way to model this. Alternatively, we can factor out the 16 and 4 terms.

But perhaps a better approach is to separate the variables for li and lj. Let's consider that the squared distance can be written as (dx)^2 + (dy)^2, where dx is the east-west difference and dy is the north-south difference. Each of these can be handled separately. Then the total time is sum over all (i,j) c_ij * (dx^2 + dy^2) = sum(c_ij dx^2) + sum(c_ij dy^2). Since dx and dy depend on lj and li respectively, the two parts can be optimized independently.

Wait, that's a crucial insight! Because the sum can be split into two parts: one that depends only on lj and the other only on li. So for each lj, the sum over j is sum(c_ij for i) * (dx for j)^2, and similarly for li. Wait, maybe not. Let me think again.

The total time is sum_{i,j} c_ij * (dx_j^2 + dy_i^2), where dx_j is (4(lj - j) +2) and dy_i is (4(li - i) +2). So dx_j depends on j and lj, dy_i depends on i and li. So sum(c_ij (dx_j^2 + dy_i^2)) = sum(c_ij dx_j^2) + sum(c_ij dy_i^2). But dx_j^2 is (4(lj -j) +2)^2 for column j, and dy_i^2 is (4(li -i)+2)^2 for row i. So the first term is sum over j (dx_j^2 * sum_i c_ij) ), and the second term is sum over i ( dy_i^2 * sum_j c_ij ). So the total time is sum_j ( (4(lj - j) +2)^2 * Cj ) + sum_i ( (4(li -i) +2)^2 * Ri ), where Cj is the sum of c_ij over all i for column j, and Ri is the sum of c_ij over j for row i.

Therefore, the problem reduces to choosing lj for each column j and li for each row i such that these two sums are minimized. But since li and lj are variables (integers in 0 <= li <=n and 0 <= lj <=m), and each term is a function of li and lj respectively, the optimal li can be found independently for the rows, and the optimal lj can be found independently for the columns. Wait, but wait: this is only possible if the variables are separable, which they are here. Because the total sum is the sum of two terms, each depending on a single variable (li and lj).

So for example, the first term sum_j ( ... ) depends only on lj, and the second term sum_i ( ... ) depends only on li. Therefore, to minimize the total sum, we can minimize each part separately. So we can compute for each possible li the value of the sum over i of (4(li -i) +2)^2 * Ri, and find the li that minimizes that sum. Similarly, compute for each possible lj the sum over j of (4(lj-j)+2)^2 * Cj, and find the lj that minimizes that sum. Then, the optimal li and lj are those that minimize their respective sums. The total minimal sum is the sum of the minimal li sum and the minimal lj sum.

This is a key insight. Because it allows us to split the problem into two separate one-dimensional problems: one for li (rows) and one for lj (columns). Then, the optimal li is the one that minimizes the row-based sum, and the optimal lj is the one that minimizes the column-based sum. This reduces the problem from O(nm) possible points (li, lj) to O(n) possible li and O(m) possible lj, which is manageable since n and m are up to 1000.

So the approach is:

1. Precompute for each row i, the sum Ri = sum_j c_ij.
2. Precompute for each column j, the sum Cj = sum_i c_ij.
3. For each possible li (from 0 to n), compute the sum over i of (4*(li - i) + 2)^2 * Ri. Let's call this sum S_li.
4. For each possible lj (from 0 to m), compute the sum over j of (4*(lj -j) + 2)^2 * Cj. Let's call this sum T_lj.
5. Find the li that minimizes S_li and the lj that minimizes T_lj. Then, the minimal total sum is S_li + T_lj.
6. Among all possible (li, lj) that achieve the minimal sum, choose the one with the smallest li, then smallest lj.

So the steps are:

- Compute Ri and Cj.
- Find the best li by evaluating S_li for all possible li.
- Find the best lj by evaluating T_lj for all possible lj.
- The answer is the sum of the minimal S_li and T_lj, along with the (li, lj) that gives those minima, choosing the smallest li and lj in case of ties.

Now, how do we compute S_li and T_lj efficiently?

Let's look at S_li. For each possible li (ranging from 0 to n), we need to calculate the sum over all rows i of (4*(li -i) + 2)^2 * Ri.

Similarly for T_lj.

But for each li, the expression (4*(li -i) + 2) can be rewritten as 4*(li -i) + 2 = 4li -4i +2 = 4(li -i) + 2. For each row i, this term is squared and multiplied by Ri. So for each li, the sum S_li is sum_i [ (4(li -i) +2)^2 * Ri ]

But for each possible li, this is a sum over i from 1 to n. Wait, but the rows are from 1 to n. So i ranges from 1 to n, but li can be 0 to n. So when li is 0, and i is 1, the term is 4*(0-1) + 2 = -4 +2 = -2. Squared is 4, multiplied by R_1. And so on.

But how to compute this efficiently for all possible li?

The straightforward approach would be, for each li in 0..n:

sum over i in 1..n of [ (4*(li -i) + 2)^2 * Ri ]

But for n up to 1e3, and li up to 1e3, this would take O(n^2) time. For n=1e3, that's 1e6 operations, which is acceptable given the time constraints. Similarly for m=1e3, O(m^2) is 1e6 as well. So total time would be around 2e6 operations, which is manageable.

So the plan is feasible.

So the steps in code would be:

- Read n and m.
- Read the n rows of m numbers each. For each row, compute Ri as the sum of that row. For each column j (1-based?), compute Cj as the sum of that column. Wait, the rows are from 1 to n, columns from 1 to m. But since the input is given as n lines, each with m numbers, for the i-th line (row i), the j-th number is c_ij. So for Cj (column j), sum all c_ij for i in 1..n.

Once Ri and Cj are computed, we compute for each possible li (0 <= li <=n) the sum S_li, and for each possible lj (0 <= lj <=m) the sum T_lj.

Then, find the li that gives the minimal S_li, and the lj that gives the minimal T_lj. In case of tie for li, choose the smallest li. Similarly for lj.

Then, output the sum of the minimal S_li and T_lj, and the chosen li and lj.

Now, let's think about how to compute S_li and T_lj.

For S_li:

For each li in 0 to n:

sum_i ( (4*(li - i) + 2)^2 * Ri )

Similarly, for T_lj:

sum_j ( (4*(lj - j) + 2)^2 * Cj )

But for li in 0 to n, and i ranges from 1 to n. Wait, no. The rows are i from 1 to n. So when li is 0, and i is 1, the term is (4*(0-1) +2)^2 = (-4 +2)^2 = (-2)^2=4.

But perhaps the code can loop li from 0 to n, and for each li, loop i from 1 to n, compute (4*(li - i) +2)^2 * Ri, and sum all these. Similarly for lj.

Yes.

Now, the code structure would be:

Read n, m.

Read n rows, each with m integers. For each row i, compute Ri = sum of the row's elements. For each column j, compute Cj as sum of the j-th element in each row.

Then compute for all possible li (0 <= li <=n) the sum S_li.

Then compute for all possible lj (0 <= lj <=m) the sum T_lj.

Find the li with minimal S_li. If multiple, pick the smallest.

Find the lj with minimal T_lj. If multiple, pick the smallest.

Total time is S_li + T_lj.

Output the sum and the li and lj.

So for example, in the first sample input:

n=2, m=3.

The input is:

3 4 5

3 9 1

So rows:

Row 1: [3,4,5] sum R1=12.

Row 2: [3,9,1] sum R2=13.

Columns:

C1 = 3+3=6.

C2=4+9=13.

C3=5+1=6.

Then for S_li (sum over rows):

We need to compute for each li (0,1,2):

For li=0:

i ranges 1 to 2.

For i=1: 4*(0-1)+2 = -4+2 = -2. squared is 4. multiplied by R1=12: 48.

i=2: 4*(0-2)+2 = -8+2 =-6. squared is 36. multiplied by R2=13: 468. sum is 48+468=516.

For li=1:

i=1: 4*(1-1)+2=0+2=2. squared 4. 4*12=48.

i=2: 4*(1-2)+2= -4 +2=-2. squared 4. 4*13=52. sum 48+52=100.

For li=2:

i=1: 4*(2-1)+2=4+2=6. squared 36. 36*12=432.

i=2:4*(2-2)+2=0+2=2. squared 4. 4*13=52. sum 432+52=484.

So minimal S_li is 100 (li=1).

For T_lj (columns):

C1=6, C2=13, C3=6.

Possible lj from 0,1,2,3.

For each lj, compute sum over j=1 to 3 of (4*(lj-j)+2)^2 * Cj.

For lj=0:

j=1: 4*(0-1)+2= -4+2=-2. squared 4. 4*6=24.

j=2:4*(0-2)+2= -8+2=-6. squared 36. 36*13=468.

j=3:4*(0-3)+2= -12+2=-10. squared 100. 100*6=600.

Sum 24+468+600=1092.

lj=1:

j=1:4*(1-1)+2=0+2=2. squared4 *6=24.

j=2:4*(1-2)+2= -4+2=-2. squared4 *13=52.

j=3:4*(1-3)+2= -8+2=-6. squared36 *6=216.

sum 24+52+216=292.

lj=2:

j=1:4*(2-1)+2=4+2=6. squared36 *6=216.

j=2:4*(2-2)+2=2. squared4 *13=52.

j=3:4*(2-3)+2= -4+2=-2. squared4 *6=24.

sum 216+52+24=292.

lj=3:

j=1:4*(3-1)+2=8+2=10. squared100*6=600.

j=2:4*(3-2)+2=4+2=6. squared36*13=468.

j=3:4*(3-3)+2=2. squared4*6=24.

sum 600+468+24=1092.

So the minimal T_lj is 292, achieved at lj=1 or 2. But since we pick the smallest lj in case of tie, lj=1.

So total sum is 100 +292=392, which matches the sample.

Thus, the approach is correct.

Now, the code needs to compute all this.

Now, handling rows and columns:

In Python, the code can read the input as follows.

Read n and m.

Then read n lines. For each line, split into m integers, store as a list.

Compute Ri for each row i (1-based?), and Cj for each column j (1-based?).

Wait, in code, indexes are 0-based for the list. So for the first row (i=1 in problem terms) would be index 0 in the list. Wait, but according to the problem statement, the first row is i=1, and the first column is j=1.

So when reading the input, row 0 in code corresponds to row 1 in the problem. But in code, perhaps it's easier to model rows as 1-based. Let's see.

In code:

rows = []
for _ in range(n):
    rows.append( list( map( int, input().split() ) ) )

So rows[0] is row i=1 in the problem. Then, Ri for i=1 is sum(rows[0]).

Similarly, columns can be built as lists. For column j (1-based), collect all rows[i][j-1] for i in 0..n-1.

So Cj for j=1 is sum( row[0] for row in rows ), etc.

But to compute Cj for each j (1-based), j ranges from 1 to m. So in code:

columns = [0]*(m)
for j in range(m):
    for i in range(n):
        columns[j] += rows[i][j]

Thus, columns[j] is C_{j+1} in the problem's terms.

Wait, no. Because j in code is 0-based (0 to m-1), so columns[0] is the sum of the first column (j=1 in problem terms). So in code, columns[j] corresponds to C_{j+1} in the problem. But perhaps I need to adjust the indices.

Alternatively, let's model the code with i and j as 1-based for rows and columns. So for the problem's row i (1..n) and column j (1..m), the code can use i-1 and j-1 as indices.

But perhaps it's easier to code with 0-based indexes.

So rows in code are 0-based (0 to n-1), columns 0-based (0 to m-1). Then:

Ri for problem's row i is sum of rows[i-1].

Cj for problem's column j is sum of rows[k][j-1] for k in 0..n-1.

But when building the code:

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append( list(map(int, input().split())) )

Then Ri for row i (problem's i, 1-based) is sum(grid[i-1]).

Similarly, for column j (problem's j, 1-based), Cj is sum( grid[i][j-1] for i in range(n) )

But in code, the code will loop through all rows and columns, so:

Compute R as list of R_i for problem's i from 1 to n:

R = [sum(row) for row in grid]

Compute C as list of C_j for problem's j from 1 to m:

C = [0]*m
for j in range(m):
    total = 0
    for i in range(n):
        total += grid[i][j]
    C[j] = total

Then, for S_li, the sum for li (problem's li ranges 0..n), for each row i (1..n), compute (4*(li - i) +2)^2 * R[i-1]. Because in code, i ranges from 1 to n (problem's i), and R[i-1] is the sum for that row.

Wait, but in code, li can be from 0 to n (problem's li, 0-based). For example, if li=0 (problem's 0), then for each row i (problem's 1..n), which is code's i in 1..n, but code uses 0-based for R (R is len n).

Wait, code's R is a list of len n, where R[0] is the sum of the first row (problem's i=1). So when problem's row i is 1, code's R[i-1] is R[0].

So for code's li in 0..n (problem's li can be 0..n), and for each problem's row i (1..n):

term = (4*(li - i) +2)^2 * R[i-1]

So code for calculating S_li for all possible li:

min_S = infinity
best_li = 0
for li in range(n+1):  # problem's li ranges from 0 to n
    current_sum = 0
    for i in range(1, n+1):  # problem's i is 1..n
        delta = li - i
        val = 4 * delta + 2
        current_sum += (val * val) * R[i-1]
    if current_sum < min_S or (current_sum == min_S and li < best_li):
        min_S = current_sum
        best_li = li

Similarly for T_lj.

But wait, in code, for the j in the columns, for problem's j (1..m), code's C[j-1] is the sum. So for lj in 0..m (problem's lj), and j in 1..m (problem's j), code's C[j-1] is the sum.

So the code for T_lj would be:

min_T = infinity
best_lj = 0
for lj in range(m+1):
    current_sum = 0
    for j in range(1, m+1):
        delta = lj - j
        val = 4 * delta + 2
        current_sum += (val * val) * C[j-1]
    if current_sum < min_T or (current_sum == min_T and lj < best_lj):
        min_T = current_sum
        best_lj = lj

This would compute the minimal S and T sums, along with the best li and lj.

Then the total is min_S + min_T, and the best_li and best_lj.

So, the code seems manageable.

Now, considering the constraints. For n=1e3 and m=1e3, the code's loops for S_li and T_lj are O(n^2) and O(m^2), which would be 1e6 + 1e6 = 2e6 operations. Which is acceptable for Python in 2 seconds.

But wait, 1e3 for n, looping 1e3 times (li in 0..n, which is 1001 possibilities for n=1e3). For each li, looping i from 1 to n (1e3), which is 1e3 iterations per li. So total for S_li is 1e3 * 1e3 = 1e6 operations. Same for T_lj: 1e3 * 1e3 = 1e6. So total 2e6 operations, which should be manageable.

But in Python, each loop is a bit slow, but 2e6 steps should be okay.

But maybe there's a way to optimize this.

Alternative approach: precompute for each possible delta (li - i) and (lj - j) the value (4*delta +2)^2, then multiply by the corresponding R or C.

But the code as written is straightforward.

Let's see for the sample input:

Sample 1:

n=2, m=3.

R is [3+4+5=12, 3+9+1=13]

C is [3+3=6,4+9=13,5+1=6]

Processing li from 0 to 2:

For li=0:

i runs 1,2.

i=1: delta = 0-1=-1. val=4*(-1)+2=-2. squared is4. *12=48.

i=2: delta=0-2=-2. val=4*(-2)+2=-6. squared 36. *13=468.

sum 516.

li=1:

i=1: delta=0. val=2. squared4*12=48.

i=2: delta=-1. val=-2. squared4*13=52. sum 100.

etc.

So code is correct.

Now, for the code to work, need to:

- Read the input correctly.

- Compute R and C correctly.

- Loop through all possible li and lj.

Now, code:

Read n and m.

Read grid as list of lists.

Compute R as list of sum of each row.

Compute C as list of sum of each column.

Compute best_li and min_S.

Compute best_lj and min_T.

Output sum and (best_li, best_lj).

Now, code.

But in code, for the sum of columns:

For example, in Python:

C = [0] * m
for j in range(m):
    for i in range(n):
        C[j] += grid[i][j]

Yes.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    grid = []
    for _ in range(n):
        grid.append( list(map(int, input_stream.readline().rstrip("\n").split())) )

    # Compute R for rows
    R = [sum(row) for row in grid]

    # Compute C for columns
    C = [0] * m
    for j in range(m):
        for i in range(n):
            C[j] += grid[i][j]

    # Find best li
    min_S = float('inf')
    best_li = 0
    for li in range(n + 1):
        current_sum = 0
        for i in range(1, n + 1):  # problem's i is 1-based
            delta = li - i
            val = 4 * delta + 2
            current_sum += (val ** 2) * R[i - 1]
        if current_sum < min_S or (current_sum == min_S and li < best_li):
            min_S = current_sum
            best_li = li

    # Find best lj
    min_T = float('inf')
    best_lj = 0
    for lj in range(m + 1):
        current_sum = 0
        for j in range(1, m + 1):  # problem's j is 1-based
            delta = lj - j
            val = 4 * delta + 2
            current_sum += (val ** 2) * C[j - 1]
        if current_sum < min_T or (current_sum == min_T and lj < best_lj):
            min_T = current_sum
            best_lj = lj

    print(min_S + min_T, file=output_stream)
    print(best_li, best_lj, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 4
1 0 0 0
0 0 3 0
0 0 5 5
""",
            "output": \
"""\
240
2 3
""",
        }, 
    ]

    for i, test_case in enumerate(TEST_CASES):
        in_stream = io.StringIO(test_case["input"])
        expected_output = test_case["output"].rstrip()

        out_stream = io.StringIO()
        main(in_stream, out_stream)
        real_output = out_stream.getvalue().rstrip()

        assert real_output == expected_output, \
            f'Test case {i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}'

    print('Tests passed 😎')


if __name__ == '__main__':
    test()


```

<RUN_SNIPPET>
```output
Tests passed 😎

```

Another test case:

Second sample input:

3 4

1 0 0 0

0 0 3 0

0 0 5 5

n=3, m=4.

Rows:

Row 1: 1+0+0+0=1.

Row2:0+0+3+0=3.

Row3:0+0+5+5=10.

So R = [1,3,10].

Columns:

column 1:1+0+0=1.

column2:0+0+0=0.

column3:0+3+5=8.

column4:0+0+5=5.

So C = [1,0,8,5].

Now, compute S_li for li in 0..3.

For each li, compute sum for i=1,2,3 of (4*(li -i)+2)^2 * R[i-1].

Let's find the best li.

Looking for li that minimizes this sum.

Let's compute for all li:

li=0:

i=1: 4*(0-1)+2 =-2. squared 4 *1=4.

i=2:4*(0-2)+2 =-6. squared 36 *3=108.

i=3:4*(0-3)+2 =-10. squared 100 *10=1000.

sum 4+108+1000=1112.

li=1:

i=1:4*(1-1)+2=2. squared 4 *1=4.

i=2:4*(1-2)+2= -2. squared4 *3=12.

i=3:4*(1-3)+2= -6. squared36 *10=360.

sum 4+12+360=376.

li=2:

i=1:4*(2-1)+2=6. squared36 *1=36.

i=2:4*(2-2)+2=2. squared4 *3=12.

i=3:4*(2-3)+2= -2. squared4 *10=40.

sum 36+12+40=88.

li=3:

i=1:4*(3-1)+2=8+2=10. squared100 *1=100.

i=2:4*(3-2)+2=4+2=6. squared36 *3=108.

i=3:4*(3-3)+2=2. squared4 *10=40.

sum 100+108+40=248.

So the minimal S_li is 88 (li=2).

For T_lj (columns):

columns C are [1,0,8,5].

Possible lj ranges 0..4 (since m=4).

For each lj in 0..4:

sum j=1..4 (4*(lj -j) +2)^2 * C[j-1].

Compute for each lj:

We need to find lj that minimizes this sum.

Looking for lj=3:

j=1:4*(3-1)+2=8+2=10. squared 100 *1=100.

j=2:4*(3-2)+2=4+2=6. squared36 *0=0.

j=3:4*(3-3)+2=2. squared4 *8=32.

j=4:4*(3-4)+2= -4+2= -2. squared4 *5=20.

sum 100+0+32+20=152.

But wait, for lj=3:

For j=1: lj -j =3-1=2. 4*2+2=10. 10^2 *1=100.

j=2:3-2=1. 4*1+2=6. 6^2 *0=0.

j=3:3-3=0. 2. 2^2*8=32.

j=4:3-4=-1. 4*(-1)+2= -2. (-2)^2=4. *5=20.

Sum is 152.

Is there a better lj?

Check lj=3 and others.

lj=2:

j=1:4*(2-1)+2=6. 36 *1=36.

j=2:4*(2-2)+2=2. 4 *0=0.

j=3:4*(2-3)+2= -4+2= -2. 4 *8=32.

j=4:4*(2-4)+2= -8+2= -6. 36 *5=180.

sum 36+0+32+180=248.

Not better than lj=3's 152.

lj=4:

j=1:4*(4-1)+2=14. 14^2=196 *1=196.

j=2:4*(4-2)+2= 10. 100*0=0.

j=3:4*(4-3)+2=6. 36 *8=288.

j=4:4*(4-4)+2=2. 4 *5=20.

sum 196+0+288+20=504.

Not better.

lj=3 is better than these.

What about lj=3, sum is 152.

What about lj=4?

No, sum 504.

Other possibilities:

lj=3 is better than lj=2 (248), lj=1:

lj=1:

j=1:4*(1-1)+2=2. squared 4 *1=4.

j=2:4*(1-2)+2= -2. squared4 *0=0.

j=3:4*(1-3)+2= -6. squared36 *8=288.

j=4:4*(1-4)+2= -12+2=-10. squared100*5=500.

sum 4+0+288+500=792.

lj=0:

sum j=1-4:

j=1:4*(-1)+2= -2. 4 *1=4.

j=2:4*(-2)+2= -6. 36*0=0.

j=3:4*(-3)+2= -10. 100*8=800.

j=4:4*(-4)+2= -14. 196*5=980.

sum 4+0+800+980=1784.

So best lj is 3, sum 152.

Total sum is 88 (S_li) + 152 (T_lj) = 240. Which matches the sample output.

The best_li is 2, best_lj is3. Which matches the sample.

Thus, the code works.

Now, the code needs to handle the 0-based and 1-based correctly, which it does.

Now, in terms of code optimization, perhaps precomputing the (4*delta +2)^2 terms or vectorizing could help, but in Python, given the constraints, the code should work as is.

Thus, the code is correct.
</think>

```python
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# Compute row sums R and column sums C
R = [sum(row) for row in grid]
C = [0] * m
for j in range(m):
    for i in range(n):
        C[j] += grid[i][j]

min_S = float('inf')
best_li = 0
for li in range(n + 1):
    current_sum = 0
    for i in range(1, n + 1):
        delta = li - i
        val = 4 * delta + 2
        current_sum += (val ** 2) * R[i - 1]
    if current_sum < min_S or (current_sum == min_S and li < best_li):
        min_S = current_sum
        best_li = li

min_T = float('inf')
best_lj = 0
for lj in range(m + 1):
    current_sum = 0
    for j in range(1, m + 1):
        delta = lj - j
        val = 4 * delta + 2
        current_sum += (val ** 2) * C[j - 1]
    if current_sum < min_T or (current_sum == min_T and lj < best_lj):
        min_T = current_sum
        best_lj = lj

print(min_S + min_T)
print(best_li, best_lj)
```
