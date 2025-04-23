<think>
Okay, let's see. The problem is to find the minimum number of cells to paint black so that all the black cells form a square, with everything else white. And if it's impossible, return -1. Hmm.

First, I need to understand the problem correctly. So, the existing black cells plus some new ones must form a perfect square, and all cells outside this square must be white. Also, the square must have a positive side length. Oh right, so the square can't be zero.

So the steps would be:

1. Find all possible square sizes and positions that could possibly cover all existing black cells, and also when we add some cells, the square must be such that all cells inside are black and all outside are white.

Wait, but the existing cells that are outside the square would have to be white. So any existing 'B's outside the square would make it impossible, because we can't repaint them. Oh right! Because the problem says that the final square must have all cells inside black (so existing 'B's inside the square can stay, and any 'W's inside the square must be painted. But existing 'B's outside the square would violate the condition, since they would have to be white. So, the existing 'B's must all be within the square, and the square must be such that all cells outside are white. So any existing 'B's outside the square's area would mean that it's impossible for that square to be a valid solution.

So the approach would be:

- Find all possible squares (with all possible sizes and positions) that can contain all existing black cells. Then for each such square, calculate how many 'W's are inside the square (since those need to be painted to 'B'), and check if there are no existing 'B's outside the square. Then, among all valid squares, find the one that requires the least number of cells to paint.

If there are no existing black cells, then the minimal is 1 (paint any cell to form a 1x1 square). For example, the third test case has all white, so the answer is 1.

But wait, if there are existing 'B's, then we need to check if they can form a square when adding some more.

So first, let's collect all the existing 'B's. Then:

- The square must include all existing B's. So the square's boundaries (top, bottom, left, right) must enclose all the existing B's. So the minimal square that can possibly enclose them has to have a size such that the side length is max(bottom - top + 1, right - left + 1). Because the square has to cover the entire area of the B's.

Wait, but the square can be larger than that. For example, suppose existing B's form a 2x3 rectangle. Then the square must have side length at least 3, but could be larger. But since we want to minimize the number of cells to paint, maybe the optimal square is the minimal possible size that can enclose all existing B's, but maybe there's a larger square that requires fewer cells to paint. Hmm, that's possible. For example, if the existing B's are spread in a way that a larger square would have more W's inside. Wait, no. Because the minimal square would have the smallest area, thus the fewest cells to paint. Wait, no. Because perhaps the existing B's are arranged in such a way that a slightly larger square has more existing B's, thus requiring fewer new cells to paint. Hmm. So we need to check all possible square sizes and positions that can enclose all existing B's, and compute the minimal required additions.

Wait, but the square must have all B's inside, and no B's outside. So any square that is considered must:

- Encompass all existing B's. Because any existing B's outside the square would make it invalid. So the square's top-left and bottom-right coordinates must be such that all existing B's are within the square.

Wait no. Wait, the existing B's must all be inside the square, and any existing B's outside the square would be invalid. Because the problem requires that after painting, all the cells inside the square are black, and those outside are white. So existing B's outside the square would remain, which would make the condition invalid. So the square must include all existing B's. So the first step is to find all existing B's. If there are none, then the answer is 1. If there are existing B's, then the square's side must be such that all existing B's are contained within it.

But the square can't be smaller than the minimal possible to contain all B's. For example, the minimal possible square's side is the maximum of the height and width of the B's bounding box.

So, the steps would be:

1. Collect all coordinates of existing B's.

2. If there are no B's:

   a. Then the minimal is to create a 1x1 square. So the answer is 1 (unless n and m are 0, but constraints say n and m are ≥1). So output 1.

3. Else:

   a. Find the minimal and maximal row and column of the B's. Let's say min_row, max_row, min_col, max_col.

   b. The bounding rectangle is (max_row - min_row +1) rows tall and (max_col - min_col +1) columns wide.

   c. The square's side must be at least the maximum of these two values, because the square must enclose the entire bounding box.

   d. So possible square side lengths can be s, where s is ≥max( (max_row - min_row +1), (max_col - min_col +1) ), and also the square must fit into the grid (so that the square's size s is ≤ min(n,m), since it's a square on the grid with sides parallel to the edges).

   e. For each possible s (starting from the minimal possible s and up to the maximum possible s which is the minimal of n and m), check all possible positions of the square of size s that includes the entire existing B's.

Wait, but how? Because the square can be placed anywhere as long as it includes all existing B's.

Wait, for a square of side length s, the possible positions are such that the square's top-left corner (i,j) and bottom-right corner (i+s-1, j+s-1) must encompass all existing B's. So:

i ≤ min_row

i + s -1 ≥ max_row

j ≤ min_col

j + s -1 ≥ max_col

So for each possible s (starting from the minimal possible s), we need to iterate over all possible positions (i,j) where the square is placed such that all existing B's are inside it.

But how to find the possible (i,j) for a given s?

Alternatively, for each possible square of side length s in the grid, check if all existing B's are inside it. If yes, then compute the required cells (the number of W's inside the square) plus check that there are no existing B's outside of the square.

Wait, but that's O(s^2) for each possible s, and considering all s from minimal possible up to min(n,m), which could be up to 100. For each s, the number of possible squares is (n - s +1) * (m - s +1). Since n and m are up to 100, the maximum possible number of squares is 100*100=10,000 per s, and s can be up to 100. So total possible squares to check is 100 * 10,000 = 1e6, which is manageable.

But perhaps there's a smarter way. Since the square must include all existing B's, the square must be such that:

i ≤ min_row <= max_row ≤ i + s -1

j ≤ min_col <= max_col <= j + s -1

So the square must start at i <= min_row and end at i + s -1 >= max_row.

Similarly for columns.

So for a given s, the possible i and j ranges are:

i can be from max(0, max_row - s +1) down to 0? Wait, no. Let's see.

Wait, the square's top row is i, and the square's bottom row is i + s -1. So to cover the existing B's:

i ≤ min_row (because the minimal row of B's is at min_row, so the square must start at a row <= min_row)

i + s -1 >= max_row (the square's bottom row must be >= the max_row of B's)

Similarly for j:

j <= min_col (the left column of the square must be <= min_col of B's)

j + s -1 >= max_col (the right column of the square must be >= max_col of B's)

Wait, no. For example, the square can start at a row that is lower than min_row, as long as the square's bottom row is higher than or equal to the max_row. But wait, the square must include all existing B's. So the min_row of the B's must be >= i (since the square starts at row i) and the max_row of the B's must be <= i + s -1. So:

i <= min_row_b

i + s -1 >= max_row_b

Similarly for columns.

So for a given s, the possible i must satisfy i <= min_row_b and i + s -1 >= max_row_b. So the possible i's are from (max_row_b - s +1) to min_row_b, but also i >=0, and i + s -1 < n.

Wait, the square must be entirely within the grid. So i can be from 0 to (n - s), and j from 0 to (m - s). So combining these constraints.

So for the rows:

i must be <= min_row_b (since B's min row is at min_row_b)

i + s -1 >= max_row_b (since B's max row is at max_row_b)

Also, i >=0 and i + s -1 < n (since the square is within the grid)

Similarly for j:

j <= min_col_b

j + s -1 >= max_col_b

j >=0

j + s -1 < m

So for each possible s, the possible i's are in the range:

i_low = max(0, max_row_b - s +1)

i_high = min_row_b

But i_high must be <= (n - s)

Wait, because i can be at most (n - s) because the square's bottom row is i + s -1 < n. So i can be from i_low to i_high, but also i_high must be <= (n - s). So the actual i range is [i_low, min(i_high, n - s)].

Similarly for j.

So for each s, the possible i's are [max(0, max_row_b - s +1), min(min_row_b, n - s)]

But wait, the square's i must be <= min_row_b (since the B's min row is min_row_b). So i can be as low as possible as long as i + s -1 >= max_row_b.

For example, if s is such that i + s -1 >= max_row_b, then i can be as low as possible (i >= max_row_b - s +1). But also i must be >=0.

So for each s, the possible i's are in the range i_low to i_high, where:

i_low = max(0, max_row_b - s + 1)

i_high = min_row_b

But also, i_high must be <= (n - s) because the square must fit into the grid (i + s -1 <= n-1). So i_high = min(min_row_b, n - s).

If i_low > i_high, then there are no possible i's for this s. So s is not feasible.

Same for j.

So the steps for each possible s (from s_min to s_max):

s_min = max(max_row - min_row +1, max_col - min_col +1)

s_max = min(n, m)

For each s from s_min to s_max:

   if s > min(n, m): skip

   Compute possible i's: i starts from i_low to i_high, where i_low = max(0, max_row_b - s +1), i_high = min(min_row_b, n - s)

   Compute possible j's: j starts from j_low = max(0, max_col_b - s +1), j_high = min(min_col_b, m - s)

   For each i in i_low to i_high:

      For each j in j_low to j_high:

          Now, the square is from (i, j) to (i+s-1, j+s-1)

          Check if all existing B's are inside this square. Well, because the constraints were set to ensure that, but perhaps need to confirm.

          Then, check if any existing B's are outside of this square. Because that's not allowed. Because after painting, all B's must be inside the square and all outside must be W.

          So if any existing B's are outside the square, then this square is invalid.

          If all existing B's are inside and none are outside:

              Then calculate the number of W's inside the square. That's the number of cells to paint.

              Keep track of the minimal such count.

So the approach is:

- For each possible square size s (starting from the minimal required s up to the maximum possible s that can fit in the grid).

- For each possible top-left (i,j) of the square of size s that includes all existing B's.

   - Check if all existing B's are inside the square (which they should be given the constraints on i and j).

   - Check if there are any existing B's outside the square. If yes, this square is invalid.

   - If valid, compute the number of W's in the square (since those must be painted to B). The existing B's inside the square can stay, but the W's must be painted.

   - Keep track of the minimal such count.

Once all possibilities are checked, select the minimal count. If none are found, output -1.

Now, how to implement this efficiently.

First, collect all existing B's. Let's read the grid.

Then, if there are no B's, output 1 if the grid has at least one cell (which it does, since n and m >=1). So the answer is 1.

Else:

Compute min_row, max_row, min_col, max_col.

s_min is max(max_row - min_row +1, max_col - min_col +1).

s_max is min(n, m).

If s_min > s_max: then it's impossible. So output -1.

Else:

Iterate s from s_min to s_max.

For each s:

   compute possible i range:

   i_low = max(0, max_row_b - s + 1)

   i_high = min(min_row_b, n - s)

   if i_low > i_high: skip this s.

   compute j_low = max(0, max_col_b - s +1)

   j_high = min(min_col_b, m - s)

   if j_low > j_high: skip this s.

   For each i in i_low to i_high:

      For each j in j_low to j_high:

          The square is (i, j) to (i+s-1, j+s-1)

          Check two things:

              a) All existing B's are inside this square.

                 Well, since i <= min_row_b and i+s-1 >= max_row_b, and j <= min_col_b and j+s-1 >= max_col_b, all B's are inside the square. So this is guaranteed. So no need to check.

              b) There are no B's outside of this square.

              So for all B's in the list, they are inside. But are there any B's in the grid that are not in the square?

              Wait, no. Because we have all existing B's in the list. So the list contains all the B's. So the existing B's are all in the list. So, if any B in the list is outside the square, then the square is invalid. Wait, but the square is constructed to include all B's. Because i is <= min_row_b (so the square's top is <= the minimal row of B's), and the square's bottom is >= max_row_b. Similarly for columns. So all B's are in the square. So the square is guaranteed to include all B's. So condition (a) is automatically satisfied.

              So the only thing to check is that there are no B's outside the square. Which would be any cell in the grid that is B but not in the square. But how to check that.

Wait, no. Wait, the grid may have B's outside the square. Because for the square to be valid, all B's (existing and new) must be inside the square. But the existing B's must all be inside the square. Because if there's an existing B outside the square, then after painting, that B would remain, which is invalid. Because the square's outside must be all W.

So, for the square to be a valid solution, all existing B's must be inside the square (which they are, given the way we're constructing the squares), and there must be no existing B's outside the square. Because those existing B's would violate the condition that outside the square, all cells are white.

So, in other words, for the square (i,j,s), we need to check that:

All B's in the grid are inside the square. Because if there's any B outside, then even after adding new B's, those existing B's would still be present and outside the square, which is invalid.

So, the way to check is:

- All existing B's are inside the square. (Which is guaranteed by the way we generate i and j.)

- No other B's exist in the grid outside the square.

Wait, but the list of B's includes all the existing B's. So if we have all B's in the list, and the square includes all B's in the list, then there are no B's outside the square. So perhaps the check is redundant. Wait no. Because the list of B's is all B's in the grid. So if the square includes all of them, then any B outside the square is not in the list. But that's impossible. So the check is not needed. Wait, that's right.

Because the list of B's is collected by scanning the entire grid. So if the square includes all B's (as per the list), then any cell outside the square that is B would have been in the list. But the list is all B's. So if all B's are in the square, there are no B's outside the square. So the check is redundant.

So, the only thing to check is whether the square is valid (i and j are within their ranges and the square is correctly constructed), and that all B's are inside the square (which they are), and that there are no B's outside the square. But since the list includes all B's, and the square includes all B's in the list, there can't be any B's outside. So this check is automatically satisfied.

Wait, but that's not correct. Wait, the list of B's is all the B's in the grid. So if the square includes all the B's in the list, then there are no B's outside the square. So for the square (i,j,s), the only B's are those in the list, which are all inside the square. So there are no B's outside.

So, for any square that includes all B's in the list, the condition (no B's outside) is automatically satisfied. So the only thing to check is that the square is correctly formed (i.e., i and j are such that the square is within the grid and encloses all B's), which they are by construction.

So, for each possible square of size s, the square is valid (as per the i and j selection), and the only thing left is to calculate the number of W's inside the square (the cells that need to be painted).

So the steps are:

For each possible square (i,j) of size s:

   compute the number of W's in the square. The required cost is this number.

   Keep track of the minimal cost.

Once all squares are checked, return the minimal cost.

So the problem reduces to:

For each possible square (i,j,s) that encloses all existing B's, compute the number of W's inside that square, and find the minimal such number.

If there are no such squares (i.e., s_min > s_max), return -1.

But wait, how about when the existing B's form a rectangle that is not a square. Then, the minimal s is the max of the width and height of the rectangle, and the square may have some areas outside the rectangle but within the square, which are currently W. So painting those W's to B's is required.

But the existing B's must all be within the square, and the square's area is s x s.

So for example, in the first sample input:

The existing B's are in positions (assuming rows are 0-based or 1-based? The input is given as the next n lines. Let's assume 0-based for code.)

Wait, the first sample input is:

5 4

WWWW

WWWB

WWWB

WWBB

WWWW

So rows are 0-based. The B's are in (1,3), (2,3), (3,2), (3,3). So min_row=1, max_row=3. min_col=2, max_col=3. The current bounding box is 3 rows (3-1+1=3) and 2 columns (3-2+1=2). So s_min is max(3,2) =3. So possible squares of size 3.

So for s=3:

The i must be <=1 (min_row), and i+3-1 >=3 (max_row) → i+2 >=3 → i >=1. So i can only be 1 (since i <=1 and i >=1). So i=1.

For j: must be <=2 (min_col), and j+3-1 >=3 (max_col) → j+2 >=3 → j >=1. So j can be 1 or 2 (since m=4, j must be <= (4-3)=1). Wait, m is 4, so j can be from 0 to 1 (since j +3-1 <=3 → j <=1). So j must be 1. Because j must be >=1 (from j >=1) and <=1 (from j <=2 and j <=1).

So the square starts at (i=1, j=1), size 3. So the square covers rows 1,2,3 and columns 1,2,3.

In this square, how many W's are there? The existing B's are (1,3), (2,3), (3,2), (3,3). The square includes cells (1,1), (1,2), (1,3); (2,1), etc. The total cells in the square is 3x3=9. Existing B's in the square are 4. So the W's are 5. Which matches the sample output.

So the approach is correct.

So the code steps:

Read n and m.

Read the grid, collect all B's coordinates.

If no B's:

   The minimal is 1. So output 1.

Else:

   Compute min_row, max_row, min_col, max_col.

   s_min = max(max_row - min_row +1, max_col - min_col +1)

   s_max = min(n, m)

   if s_min > s_max:

      output -1

   else:

      minimal_paint = infinity

      for s in s_min to s_max:

          # Compute possible i range

          i_low = max(0, max_row - s +1)

          i_high = min( min_row, n - s )

          if i_low > i_high:

              continue

          j_low = max(0, max_col - s +1)

          j_high = min( min_col, m - s )

          if j_low > j_high:

              continue

          for i in range(i_low, i_high +1):

              for j in range(j_low, j_high +1):

                  # The square is from (i, j) to (i+s-1, j+s-1)

                  # Now count the number of W's inside this square

                  # Also, check if there are any existing B's outside the square

                  # Wait, but existing B's are all in the list, and the square includes all of them. So no B's outside.

                  # So only count the W's in the square.

                  # To count W's in the square:

                  # Iterate over each cell in the square and count the W's.

                  # But this can be O(s^2) per square. For s up to 100, and squares up to 1e4, this could be 1e6 * 1e4 = 1e8 operations, which is too slow.

                  # So this approach is not efficient enough. Need a faster way.

                  # Precompute a 2D prefix sum array for the number of B's.

                  # Then, the number of B's in the square can be computed in O(1), and the number of W's is s*s - num_B_in_square.

                  # So we need a prefix sum array.

So precompute a prefix sum array for B's.

For example, prefix[i][j] is the number of B's in the rectangle from (0,0) to (i-1, j-1). Then, the sum in a square from (x1,y1) to (x2,y2) (inclusive) is sum = prefix[x2+1][y2+1] - prefix[x1][y2+1] - prefix[x2+1][y1] + prefix[x1][y1]

So the number of B's in the square is sum, and the number of W's is s*s - sum. So the required number of W's is the number of cells to paint.

So, precomputing the prefix sum array allows O(1) per square.

So steps:

- Precompute prefix sum of B's.

Then, for each square (i, j, s):

   x1 = i

   y1 = j

   x2 = i + s -1

   y2 = j + s -1

   sum_b = prefix[x2+1][y2+1] - prefix[x1][y2+1] - prefix[x2+1][y1] + prefix[x1][y1]

   num_w = s*s - sum_b

   if num_w < current minimal, update.

So the code can be optimized with prefix sum.

So the code steps:

Read the grid, collect all B's positions and build a grid (array of arrays) where 1 is B, 0 otherwise. Or, create a 2D array where grid[i][j] is 1 if it's B, else 0.

Then compute the prefix sum.

Once that's done, for each possible square (i,j,s), compute the sum of B's in the square, subtract from s*s to get the number of W's (cells to paint).

Now, the time complexity would be:

- Precompute prefix sum: O(n*m)

- For each s in s_min to s_max: O(s_max - s_min +1) → up to 100.

   For each i in i_low to i_high: O( (i_high - i_low +1) ) → up to 100.

      For each j in j_low to j_high: O( (j_high - j_low +1) ) → up to 100.

          O(1) per square.

So total time is O( (100) * 100 * 100 ) = 1e6 operations. Which is acceptable.

So this approach is feasible.

So now, the code:

First, read the input.

Then, collect all B's, compute min_row, max_row, etc.

If no B's, output 1.

Else compute s_min, s_max.

Check if s_min > s_max → output -1.

Else, precompute prefix sum.

Then, for each s in s_min to s_max:

   compute i's and j's ranges.

   for each i and j in the ranges:

      compute x2 = i + s -1, y2 = j + s -1.

      if x2 >=n or y2 >=m → invalid. But since i and j are chosen such that i + s -1 <n and j + s-1 <m, this check is redundant.

      compute sum_b using prefix sum.

      num_w = s*s - sum_b.

      if this num_w is less than current minimal, update.

Once all squares are processed, if the minimal is found, output it, else -1.

But wait, there is another condition: the square must have all existing B's inside. Which is guaranteed by the way i and j are chosen. So the sum_b would include all existing B's. Wait, no. Because the sum_b is the number of B's in the square. But the existing B's may have some in the square and some outside.

Wait, no. The existing B's are all in the list. The list is all B's in the grid. So the sum_b is the total number of B's in the square. But for the square to be valid, all existing B's must be in the square. So sum_b must equal the total number of B's.

Because if any B is outside the square, then the square is invalid (since those B's would remain). So sum_b must be equal to the total number of B's in the grid.

So for a square to be valid, sum_b must equal the total B's. Otherwise, there are B's outside the square.

Ah, that's a crucial point. So even if the square encloses all B's (as per the i and j selection), but the sum of B's in the square is less than the total B's, that means there are B's outside the square, which is invalid.

Wait, but how? Because the i and j are chosen such that the square includes the B's. So why would the sum_b be less than the total B's?

Ah, because the existing B's may not all be in the square.

Wait, no. Because the way i and j are chosen ensures that the square includes all B's. Because i <= min_row and i+s-1 >= max_row. So the square's rows range includes all rows from min_row to max_row, which includes all B's. Similarly for columns.

But then, why would the sum_b be less than total B's? Because the B's are in the square's rows and columns, but maybe not all of them are in the square's columns. For example, if the B's are spread in such a way that some are in columns outside the square's columns.

Wait, no. Because the j ranges are chosen such that j <= min_col and j + s-1 >= max_col. So the square's columns must include from min_col to max_col, hence all B's.

So the square's rows and columns are guaranteed to include all B's. So any B in the list will be inside the square.

But sum_b is the number of B's in the square. So sum_b must equal the total B's. So in code, for each square (i,j,s), compute sum_b. If sum_b != total_b → invalid. So only squares where sum_b == total_b are considered valid.

So that's an additional check that needs to be made.

So the code must compute the sum_b for the square, and check if it's equal to the total number of B's. If not, this square is invalid and cannot be considered.

So the steps are:

For each square (i,j,s):

   compute sum_b.

   if sum_b != total_b → skip.

   else:

      compute num_w = s*s - sum_b.

      compare to minimal_paint.

So this is an essential check.

So the code must compute the total number of B's (total_b). If sum_b == total_b, then the square is valid.

So the code's steps:

Read grid, collect all B's, compute min_row, max_row, min_col, max_col, total_b = len(bs).

If total_b ==0 → output 1.

Else:

   compute s_min = max(...), s_max = min(...).

   if s_min>s_max → output -1.

   else:

      precompute prefix sum.

      minimal_paint = infinity.

      for s in s_min to s_max:

          i_low = max(0, max_row - s +1)

          i_high = min( min_row, n - s )

          if i_low > i_high: continue.

          j_low = max(0, max_col - s +1 )

          j_high = min( min_col, m - s )

          if j_low > j_high: continue.

          for i in i_low ... i_high:

              for j in j_low ... j_high:

                  x1 = i

                  y1 = j

                  x2 = i + s -1

                  y2 = j + s -1

                  sum_b = prefix[x2+1][y2+1] - prefix[x1][y2+1] - prefix[x2+1][y1] + prefix[x1][y1]

                  if sum_b != total_b:

                      continue

                  num_w = s*s - sum_b

                  if num_w < minimal_paint:

                      minimal_paint = num_w

      if minimal_paint is still infinity → output -1.

      else → output minimal_paint.

So this is the correct approach.

Now, let's test the second example:

Input:

1 2

BB

So the existing B's are at (0,0) and (0,1). min_row=0, max_row=0. min_col=0, max_col=1.

s_min is max(0-0+1=1, 1-0+1=2) → 2.

s_max is min(1, 2) →1.

So s_min=2> s_max=1 → output -1. Which matches the sample.

Third example:

3x3 grid, all W. So total_b=0 → output 1.

Another test case: all B's. For example, a 3x3 grid filled with B's. Then the square must be 3x3, and the number of W's is 9 - 9=0. So output 0.

Another test case: some B's and existing B's outside the square. For example, if there are B's in a 2x2 area, but another B outside. Then no square can include all B's, so output -1.

So the code should handle these cases.

Now, the code in Python.

Implementing prefix sum:

The grid is 0-based. So for a grid of size n rows, m columns, the prefix sum is a (n+1) x (m+1) array, initialized to 0.

prefix[i][j] is the sum of the submatrix from (0,0) to (i-1, j-1).

So, for each cell (i,j) in the grid (0-based):

prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + (1 if cell is 'B' else 0).

So code for prefix sum:

n, m = map(int, input().split())
grid = []
total_b = 0
bs = []
for i in range(n):
    row = input().strip()
    grid_row = []
    for j, c in enumerate(row):
        if c == 'B':
            total_b +=1
            bs.append( (i,j) )
    grid.append(row)

if not bs:
    print(1)
    exit()

min_row = min( i for i,j in bs )
max_row = max( i for i,j in bs )
min_col = min( j for i,j in bs )
max_col = max( j for i,j in bs )

s_min = max( (max_row - min_row +1), (max_col - min_col +1) )
s_max = min(n, m)

if s_min > s_max:
    print(-1)
    exit()

# Precompute prefix sum of B's.
prefix = [ [0]*(m+1) for _ in range(n+1) ]

for i in range(n):
    row_sum = 0
    for j in range(m):
        # compute prefix[i+1][j+1]
        current = 1 if grid[i][j] == 'B' else 0
        row_sum += current
        prefix[i+1][j+1] = prefix[i][j+1] + row_sum

minimal_paint = float('inf')

for s in range(s_min, s_max +1):
    # compute possible i's and j's
    i_low = max(0, max_row - s +1)
    i_high = min( min_row, n - s )

    if i_low > i_high:
        continue

    j_low = max(0, max_col - s +1)
    j_high = min( min_col, m - s )

    if j_low > j_high:
        continue

    for i in range(i_low, i_high +1):
        for j in range(j_low, j_high +1):
            x1, y1 = i, j
            x2 = x1 + s -1
            y2 = y1 + s -1

            # calculate sum_b
            sum_b = prefix[x2+1][y2+1] - prefix[x1][y2+1] - prefix[x2+1][y1] + prefix[x1][y1]

            if sum_b != total_b:
                continue

            num_w = s*s - sum_b
            if num_w < minimal_paint:
                minimal_paint = num_w

if minimal_paint == float('inf'):
    print(-1)
else:
    print(minimal_paint)

Wait, but the code for the prefix sum is incorrect. The way the code is written:

prefix[i+1][j+1] = prefix[i][j+1] + row_sum

But row_sum is the sum of the current row up to column j. This is incorrect. Because the correct formula for the prefix sum is:

prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + current.

But in the code, the row_sum is added. So perhaps the code is not correctly calculating the 2D prefix sum.

Yes, the code for the prefix sum is wrong. Let's correct it.

The correct way to compute the prefix sum is:

for i in range(n):
    for j in range(m):
        prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + (1 if grid[i][j] == 'B' else 0)

So each cell's prefix is the sum to the left, sum above, subtract the overlap, then add the current cell.

So the code needs to be:

prefix = [ [0]*(m+1) for _ in range(n+1) ]
for i in range(n):
    for j in range(m):
        current = 1 if grid[i][j] == 'B' else 0
        prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + current

Yes.

So in the previous code, the code for building the prefix is incorrect. So that's a bug.

So the code must be adjusted to compute the prefix sum correctly.

So the corrected code for the prefix sum is as above.

This is critical to get right.

Testing the first sample input:

After building the prefix sum, the sum_b for the square (i=1, j=1, s=3) should be 4 (since the existing B's are 4, and the square includes all of them and no others).

But in the grid, there are 4 B's. So sum_b=4, which equals total_b=4. So the square is valid.

Then, the number of W's is 3*3 -4=5. Which matches the sample.

So the code with the corrected prefix sum should work.

Another example: the third test case, all W. total_b=0, so output 1.

Another example: if a grid has a single B. Then s_min=1, s_max= whatever. The code will compute for s=1. The i ranges and j ranges will be set to the B's position. So the square will be 1x1, sum_b=1. num_w=1-1=0. So the minimal_paint is 0. Wait, but the problem states that existing B's are already in the square, and all other cells are white. So the answer would be 0, but wait, that's correct.

But what if the existing B is in a 3x3 grid. Then the minimal square is 1x1, and no new cells needed.

So the code would output 0.

Yes.

So the code is now correct.

So the full code is:

Read n and m.

Read the grid.

Collect B's, compute min_row, etc.

If no B's, output 1.

Else compute s_min and s_max.

If s_min> s_max, output -1.

Else compute prefix sum.

Loop over s, i, j, check sum_b == total_b, compute num_w.

Finally, output minimal_paint.

Now, the code.

Let's write the code correctly.

Here's the Python code:

Read the input, build grid, collect B's.

Compute prefix sum correctly.

Then proceed as described.
</think>

```python
n, m = map(int, input().split())
grid = []
total_b = 0
bs = []

for i in range(n):
    row = input().strip()
    grid.append(row)
    for j in range(m):
        if row[j] == 'B':
            total_b += 1
            bs.append((i, j))

if not bs:
    print(1)
    exit()

min_row = min(i for i, j in bs)
max_row = max(i for i, j in bs)
min_col = min(j for i, j in bs)
max_col = max(j for i, j in bs)

s_min = max(max_row - min_row + 1, max_col - min_col + 1)
s_max = min(n, m)

if s_min > s_max:
    print(-1)
    exit()

# Precompute prefix sum of B's
prefix = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(m):
        current = 1 if grid[i][j] == 'B' else 0
        prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + current

minimal_paint = float('inf')

for s in range(s_min, s_max + 1):
    i_low = max(0, max_row - s + 1)
    i_high = min(min_row, n - s)
    if i_low > i_high:
        continue

    j_low = max(0, max_col - s + 1)
    j_high = min(min_col, m - s)
    if j_low > j_high:
        continue

    for i in range(i_low, i_high + 1):
        for j in range(j_low, j_high + 1):
            x1, y1 = i, j
            x2 = x1 + s - 1
            y2 = y1 + s - 1
            sum_b = prefix[x2 + 1][y2 + 1] - prefix[x1][y2 + 1] - prefix[x2 + 1][y1] + prefix[x1][y1]
            if sum_b != total_b:
                continue
            num_w = s * s - sum_b
            minimal_paint = min(minimal_paint, num_w)

print(minimal_paint if minimal_paint != float('inf') else -1)
```