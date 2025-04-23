<think>
Okay, let's tackle this problem. Hmm, the problem statement is a bit tricky. Let me read it again.

So, the chessboard is n x m. Initially, all black squares are painted to 0. Then, during each minute i, we repaint certain black squares to color i. The condition for a square to be repainted in the i-th minute is that exactly four of its corner-adjacent squares were painted i-1 in the previous step. And this happens simultaneously for all such squares each minute. We need to find out how many squares were painted exactly x times.

Wait, wait. Wait, each square can be repainted multiple times. Because maybe a square is repainted in minute 1, then again in minute 2, etc. But the problem says "exactly x times". So for each square, count the number of times it was repainted, and find the total number of squares where this count equals x.

First, let's model how the painting process works. Let's think about the initial setup. All black squares are painted at minute 0. Then, in each subsequent minute, some squares get repainted. The key is to find for each square, how many times it was repainted.

But how do the squares get repainted over time? Let's think about the conditions. A square is repainted at minute i if, in the previous step, exactly four of its corner-adjacent squares were painted i-1.

Wait, the corner-adjacent squares are the four squares that share exactly one corner with the current square. So for a square at (i,j), the four corner-adjacent squares are (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1). So each of these four squares must have been painted i-1 in the previous minute for the current square to be painted now.

But how does this propagate over time? Let's think of the initial step. At minute 0, all black squares are painted. Then, minute 1: for a square to be painted, all four of its corner-adjacent squares must have been painted at minute 0. But since minute 0 is the initial state, those four squares were black (so their initial color was 0). Wait, but the initial state is that all black squares are painted 0. So in the initial step (minute 0), all black squares are 0. Then, during minute 1, we look for squares that are black and whose four corner-adjacent squares were painted 0 (i.e., in the previous step, they were repainted). Wait, but during minute 0, the initial step, all black squares are 0. So during minute 1, any black square that has all four corner-adjacent squares as 0 (from minute 0) will be repainted to 1. Then, in minute 2, the squares that have four corner-adjacent squares painted 1 will be repainted, and so on.

But wait, the problem says "initially black squares". So only squares that were originally black can be repainted. So, during each minute, we are only considering the original black squares. The white squares are irrelevant here. Because even if a white square is surrounded by four painted squares, since it's white (not part of the black squares), it's not considered.

So the process is: for each original black square, we determine the times when it gets repainted. Each time, the square is painted a new color i, which increments each minute. But the count is the number of times it's been repainted. The initial painting (minute 0) counts as one repaint, right? Wait, the problem statement says "exactly x times". Let's check the first example.

In the first example input:

3 3
1

The output is 4.

So the chessboard is 3x3. The upper left square is black. Assuming a chessboard pattern, where the colors alternate. So for a 3x3 chessboard, the black squares are:

(0,0), (0,2), (1,1), (2,0), (2,2) ?

Wait, no. The problem says that the upper left square is always black. Then, in a chessboard pattern. So the squares (i,j) are black if (i + j) is even.

Wait, that's the standard chessboard pattern. So, for a 3x3 grid:

Row 0: B W B

Row 1: W B W

Row 2: B W B

So the black squares are (0,0), (0,2), (1,1), (2,0), (2,2). Wait, but 3x3 has 5 black squares. The example input's output is 4 when x is 1. So that suggests that four squares were painted exactly once. But the initial painting (minute 0) counts as the first time. Then, the squares that are repainted in minute 1 would have been painted once again. Wait, but the problem statement says "exactly x times". So how many times were each square repainted?

Wait, the initial painting (minute 0) is a repaint. So all black squares are painted once here. Then, any subsequent repaints are additional counts. So for example, a square repainted in minute 1 would have been repainted twice: once at minute 0, once at minute 1. Wait, no. Because the process is that during the i-th minute, the square is repainted to color i. So the initial step (minute 0) is the first repaint. Then, each subsequent time it's repainted adds to the count. So the total number of repaints for a square is 1 + the number of times it was repainted in subsequent steps.

Wait, the problem statement says "exactly x times". So the initial repaint (minute 0) counts as the first time. Then, any repaint in minute 1 would add another time, etc. So each time a square is repainted in a minute, it adds to the count. For example, the square in the first example's output of 4. Let's see:

In the first example, x is 1. So the answer is the number of squares that were repainted exactly once. That implies that these squares were only repainted in minute 0 and never again. So they have a count of 1. How can that be? Because in minute 0, all black squares are painted. Then, for some of them, in subsequent minutes, they are repainted again. So the squares that are repainted only once are those that were painted in minute 0 and then never again. So the output of 4 suggests that 4 such squares exist in the 3x3 grid.

Wait, but the initial step is minute 0. So all black squares are painted once here. Then, in minute 1, some are repainted again. Then, in minute 2, perhaps some again. So the count for a square is 1 plus the number of times it was repainted in minutes 1, 2, etc. So in the first example, the answer is 4 squares with exactly 1 repaint. That would mean those four were not repainted again after minute 0.

So let's model the problem as: each square is repainted in some sequence of minutes. The count is the number of times it was repainted (including the initial minute 0). So for example, the initial repaint is one count. Then, each subsequent minute where it's repainted adds another count.

So the problem is to find how many squares have exactly x repaints.

Now, the challenge is to model the number of times each square is repainted. Let's think about how the repainting works.

The key is that a square is repainted in minute i if, during the i-th step, exactly four of its corner-adjacent squares were painted i-1. So this forms some sort of pattern, where the repainting propagates in certain ways.

But given the constraints (n and m up to 5000), we need an O(1) or O(nm) solution, possibly with some mathematical formula.

So perhaps the number of times a square is repainted depends on its position. Let's think about the chessboard coordinates.

The initial black squares are those where (i + j) is even (since upper left is (0,0), which is even). So for a square (i,j) to be a black square, (i + j) must be even.

Now, during minute 0, all black squares are repainted once. Then, during minute 1, a black square is repainted again if all four of its corner-adjacent squares were repainted in minute 0. Wait, but those corner-adjacent squares must also be black. Because in minute 0, only black squares were repainted. So for the corner-adjacent squares to have been repainted in minute 0, they must be black squares.

Wait, but the corner-adjacent squares may be white. For example, the square (0,0) in a 3x3 grid has corner-adjacent squares ( -1, -1 ), ( -1, 1 ), ( 1, -1 ), (1,1 ). But these are outside the grid except for (1,1). So (0,0) has only one corner-adjacent square (1,1) which is black. So in minute 1, the square (0,0) would not be repainted, since only one of the four corner-adjacent squares is painted 0 (since the others are out of bounds and thus not considered as painted 0, I guess? Or are the out-of-bound squares considered as not painted?)

This is a crucial point. The problem says that the four corner-adjacent squares must have been painted i-1. So for a square to be repainted in step i, all four of its corner-adjacent squares must exist (i.e., be within the grid) and have been painted in step i-1. Or is it possible that if a corner-adjacent square is outside the grid, it's considered as not being painted i-1?

Wait, the problem statement says "exactly four corner-adjacent squares painted i-1". So if a square is on the edge, then some of its corner-adjacent squares are out of the grid. So in such cases, the count of corner-adjacent squares painted i-1 would be less than four. Thus, the square cannot be repainted in that step.

So for example, the square (0,0) in a 3x3 grid has four corner-adjacent squares: (-1,-1), (-1,1), (1,-1), (1,1). The only one inside the grid is (1,1). So in any step, the square (0,0) will have only one corner-adjacent square. So it can never be repainted after minute 0, since in step 1, it would require all four corner-adjacent squares to be painted 0, but three of them are out of the grid. So (0,0) is repainted once (only in minute 0). Similarly, other edge squares may have this issue.

But squares in the interior may have all four corner-adjacent squares present. So let's model this.

Let's think of the grid. For a square (i,j) to have four corner-adjacent squares, it must be surrounded by squares on all four diagonals. So the square (i,j) must have i-1 >=0, i+1 <n, j-1 >=0, j+1 <m. So the squares that can have four corner-adjacent squares are those with i >=1, j >=1, i <=n-2, j <=m-2. Wait, no. For example, (i,j) must have (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1) all within the grid. So:

i-1 >=0 and i+1 <n

j-1 >=0 and j+1 <m

So the square (i,j) must be at least one row away from the top and bottom, and one column away from the left and right. So the valid coordinates for a square with four corner-adjacent squares are 1 <=i <=n-2 and 1 <=j <=m-2. So for example, in a 3x3 grid, only the center square (1,1) is in this region.

So the process is: during each step i, we repaint certain black squares. Let's model for each square (i,j) how many times it's repainted.

The initial repaint (minute 0) is for all black squares (count 1). Then, for each minute i >=1, a square is repainted if and only if:

1. It's a black square (original).

2. All four of its corner-adjacent squares are present (i.e., the square is in the inner region where all four corners are within the grid).

3. All four of those corner-adjacent squares were repainted in the previous minute (i-1).

So the repainting forms layers. For example, the center square (1,1) in a 3x3 grid may be repainted in step 1 if all four corner squares (0,0), (0,2), (2,0), (2,2) were repainted in step 0. But these squares are in the corners, which in the initial step (minute 0) were repainted. So in minute 1, the center square's four corner-adjacent squares are all 0. So the center square would be repainted in minute 1. Then, in minute 2, the same logic applies: for the center square to be repainted again, all four corner-adjacent squares must have been repainted in minute 1. But the corner-adjacent squares (0,0), (0,2), (2,0), (2,2) are on the edges. Their four corner-adjacent squares are mostly outside the grid, except for the center square. So in minute 1, the corner squares (0,0) would not be repainted again because their corner-adjacent squares are outside. So during minute 1, only the center square is repainted. Then, in minute 2, the center square's four corner-adjacent squares (the corner squares) were repainted in minute 1? Wait, no. The corner squares were repainted in minute 0, but not in minute 1. So in minute 1, the center square is repainted. Then, in minute 2, the four corner-adjacent squares (the corners) are in minute 0, not 1. So the center square would not be repainted again. So the center square is repainted in minute 0 and 1, making a total of 2 repaints. Which in the second example (input x=2) gives output 1. So the center square is the only one with exactly two repaints.

So the example makes sense. So the process is that each square can be repainted in certain steps, and the number of repaints depends on how deep the square is in the grid.

Now, the key is to model for each black square (i,j) how many times it's repainted. Let's denote k as the maximum layer such that the square is in a diamond-shaped region. For example, the initial step is layer 0 (all black squares). Then, in layer 1, the squares that can be repainted in step 1 are those that are surrounded by four squares from layer 0, which would form a diamond shape. Then, layer 2 would require being surrounded by four squares from layer 1, which forms a smaller diamond, etc. So for each square, the number of times it's repainted is equal to 1 + the number of layers it's part of. Wait, maybe the number of times a square is repainted is equal to the depth of layers it can reach. For example, the initial layer (0) is depth 0, then each subsequent step adds a depth. So a square in depth d would be repainted d+1 times (once in each step 0, 1, ..., d).

Wait, let's think. Suppose a square is repainted in steps 0, 1, 2, ..., k. Then the total number of times it's repainted is k+1. So the number of times is 1 (for step 0) plus the number of steps after step 0 in which it's repainted. How do we find k for each square?

The pattern seems to be that a square can be repainted up to a certain depth based on how far it is from the edges. For example, the center square in a 3x3 grid is depth 1 (steps 0 and 1), so repainted twice.

In a 5x5 grid, the center square (2,2) can be repainted in steps 0, 1, 2. Because after step 0, in step 1, the four corner-adjacent squares (1,1), (1,3), (3,1), (3,3) are repainted. Then, in step 2, the center square (2,2) is surrounded by those squares (repainted in step 1), so it's repainted again. So depth 2, total repaints 3.

So the maximum depth for a square (i,j) would be determined by how far it is from the edges in terms of layers.

Alternatively, for a square (i,j), the depth is the minimum of (i, j, (n-1) - i, (m-1) - j) for the original black squares. But I'm not sure.

Wait, let's see. For the original black squares (i + j even), the maximum depth possible for a square is the minimum of the distances to the top, bottom, left, and right edges, divided by 2.

Wait, maybe not. Let's take an example. Suppose we have a square in a 5x5 grid. Let's say (2,2). The distances to the top, bottom, left, and right edges are 2, 2, 2, 2. So the minimum is 2. Divided by 2 gives 1. But in that case, the square can be repainted in steps 0, 1, 2. Which is depth 2. So perhaps the formula is (minimum of (i, n-1 -i, j, m-1 -j) ) // 1? No, that doesn't fit. Hmm.

Alternatively, for each original black square (i,j), the maximum number of times it's repainted is 1 + the number of layers it can be part of. Let's model the layers.

Layer 0: all original black squares.

Layer 1: squares that are in the original black squares and are surrounded by four squares from layer 0 (i.e., their four corner-adjacent squares are all in layer 0).

Layer 2: squares surrounded by four squares from layer 1.

And so on. So the maximum possible layer for a square is determined by how "deep" it is in the grid.

But how to model this for a square (i,j). Let's think of the layers as diamond-shaped regions. Each layer corresponds to a square's distance from the borders in a certain way.

For example, the squares in layer k must be at least k units away from all four edges. But wait, in terms of the original grid coordinates. Suppose we have a grid where the square (i,j) is such that i >=k and i <=n-1 -k, and j >=k and j <=m-1 -k. Then, the square can be in layer k. But I'm not sure.

Alternatively, the maximum layer a square can reach is determined by the minimal number of steps required to reach a border in all four diagonal directions. For example, for a square (i,j), the minimal distance to the top, bottom, left, right edges in terms of steps where each step moves two units (since each layer reduces the possible area by two in each dimension). For example, the maximum k for a square is determined by how far it can be from the edges such that in all four directions (left, right, up, down), the square is at least k steps away, where each step is two units.

Alternatively, for a square (i,j) which is a black square, the maximum number of times it's repainted is equal to the minimum of (i, j, (n-1)-i, (m-1)-j) + 1. Wait, let's see.

In the first example, the 3x3 grid. The center square (1,1) has i=1, j=1. The minimal of (1,1, 1,1) is 1. Adding 1 gives 2. Which matches the second example where x=2, output is 1. The square (0,0) has minimal 0, so 0+1=1. So for x=1, it's counted. So in the first example, the squares (0,0), (0,2), (2,0), (2,2), and (1,1) are the original black squares. The minimal for (0,0) is 0, so 1 repaint. The center (1,1) has 1, so 2 repaints. So the first example's x=1 would have the four corners and the center's 1 repaint? Wait no. Wait, the minimal for the corners (0,0) is 0, so their maximum repaint count is 1. The center has 1, so 2. So when x=1, the answer is 4 (the four corners) plus (the center? No, because the center has 2 repaints). Wait, no. The first example's output is 4. So perhaps the minimal is (i, j, (n-1-i), (m-1-j)) for a square. Then, the maximum k is the minimal of those four values. The number of repaints is k + 1.

Wait, for the square (0,0) in a 3x3 grid:

i=0, (n-1-i)=2, j=0, (m-1-j)=2. The minimal is 0. So the number of repaints is 0+1=1. So this square is repainted once.

The square (1,1) has min(i, (n-1-i), j, (m-1-j)) = 1. So 1+1=2 repaints.

The squares (0,2) would have i=0, (n-1-i)=2, j=2, (m-1-j) =0. So minimal is 0. So 0+1=1 repaints.

So the four corners (0,0), (0,2), (2,0), (2,2) have 1 repaint each, and the center has 2. So for x=1, the answer is 4 (four squares), which matches the first example. For x=2, the answer is 1 (the center), which matches the second example. So this seems to fit.

Another example: the 1x1 grid. The minimal is 0 (since i=0, (n-1-i)=0, j=0, (m-1-j)=0). So the number of repaints is 0+1=1. Which matches the third example where input x=1 gives output 1.

So the formula seems to be: for each black square (i,j) (i.e., (i + j) even), compute k = min(i, (n-1 - i), j, (m-1 -j)), then the number of repaints is k + 1. Because during each layer up to k, the square is repainted. For example, k=0 implies the square is in layer 0 only, so repainted once. k=1 implies layers 0, 1, so repainted twice, etc.

So the steps to solve the problem are:

1. For each black square (i,j) (i.e., (i+j) is even), compute k = min(i, (n-1 -i), j, (m-1 -j)).

2. The number of repaints for the square is (k + 1).

3. Count how many such squares have (k + 1) == x.

So the problem reduces to counting the number of black squares (i,j) where the minimal of i, (n-1 -i), j, (m-1 -j) is equal to x-1.

So how to compute this efficiently given n and m up to 5000?

The approach is:

- For each possible (i,j) where (i + j) is even, compute the minimal of the four values. Then, check if this minimal equals x-1. If yes, count it.

But for n and m up to 5000, the total number of squares is up to 25 million. But since we only need to process the black squares (half of them), it's 12.5 million. For Python, processing 12 million elements in a loop may be feasible, but perhaps there's a smarter way.

But even 12 million iterations could be time-consuming in Python. So we need a mathematical formula to calculate the count without iterating all squares.

Let's think about the possible values of k = x-1. We need to find the number of black squares where the minimal of i, (n-1 -i), j, (m-1 -j) is exactly k.

Let's denote:

a = min(i, n-1 -i)

b = min(j, m-1 -j)

Then, k = min(a, b)

So for a square to have min(a, b) = k, it's required that both a >=k and b >=k, and at least one of a ==k or b ==k.

But since k is the minimal of a and b, then the minimal is k. So a >=k, b >=k, and the minimal between a and b is k. So either a is k and b >=k, or b is k and a >=k. But wait, no. Because the minimal of a and b is k. So (a >=k and b >=k) and (a ==k or b ==k). So the possible cases are:

Either a ==k and b >=k, or b ==k and a >=k. But in both cases, the minimal is k.

But this could include cases where both a and b are k, which are counted in both cases. So we need to avoid double-counting.

Alternatively, the count is equal to the number of squares where min(a, b) ==k.

Which can be calculated as the number of squares where a >=k and b >=k, minus the number of squares where a >=k+1 and b >=k+1. Because the minimal is >=k if a and b are >=k. But the minimal is exactly k if (a >=k and b >=k) and not (a >=k+1 and b >=k+1).

Wait, another approach: the number of squares where min(a, b) >=k is equal to the number of squares where a >=k and b >=k. The number of squares where min(a, b) >=k+1 is the number where a >=k+1 and b >=k+1. So the count of squares where min(a, b) ==k is equal to (number where a >=k and b >=k) - (number where a >=k+1 and b >=k+1).

So this gives us the formula for the count.

So the problem now reduces to:

For each black square (i,j), compute the number of such squares where a >=k and b >=k, and (i +j) is even. Then subtract the same for k+1.

But how to compute this efficiently?

First, let's separate the problem into two parts: compute the total number of black squares (i,j) where a >=k and b >=k. Then, subtract the number where a >=k+1 and b >=k+1. The result is the number of squares where min(a, b) ==k.

But how to compute the number of black squares with a >=k and b >=k.

Let's first compute a and b for each (i,j).

a = min(i, n-1 -i)

b = min(j, m-1 -j)

But a >=k means that i >=k and (n-1 -i) >=k. Which implies that i >=k and i <= (n-1 -k). So the range for i is [k, n-1 -k]. The number of i's in this range is (n-1 -k -k +1) = (n - 2k) if n >=2k+1, else zero. Similarly for j: the range is [k, m-1 -k], and the count is (m - 2k) if m >=2k+1, else zero.

So the number of squares where a >=k is (n - 2k) * (m - 2k) if n >=2k+1 and m >=2k+1, else zero. But wait, this is the number of squares (i,j) where a >=k and b >=k, regardless of their color. But we need to count only the black squares (i+j even).

So the total squares with a >=k and b >=k is:

number_of_squares = (n_available_i) * (m_available_j)

where n_available_i is the count of i's in [k, n-1 -k], which is max(0, n - 2k) if n >=2k+1.

Similarly for m_available_j.

But within these i's and j's, we need to count how many are even (i+j even).

So the problem is to find, given a rectangle of size (a x b), how many cells (i,j) in that rectangle have (i+j) even. The answer is ceil(a*b / 2) if the top-left corner is (k,k), which is (i,j) such that i and j start at k. Wait, the parity of i and j depends on k. For example, if k is even, then i ranges from even to even, etc.

But perhaps the number of even cells is (total_cells + 1) // 2 if the total is even, but depends on the parity of the start and end.

Alternatively, the number of even cells in a rectangle from i_min to i_max (inclusive), and j_min to j_max (inclusive), where i_min and j_min are even, and i_max and j_max are even as well. Wait, perhaps the pattern is such that in a grid, half the cells are even and half are odd. Except when the total number of cells is odd, in which case there's one more of one parity.

But in the given rectangle, the parity of (i +j) is even. Let's consider the rectangle where i ranges from i_start to i_end, and j ranges from j_start to j_end.

The parity of i and j will alternate. So the count of even (i+j) is (total_cells + parity) // 2, where parity is 1 if the top-left corner is even, else 0.

Alternatively, the count can be computed as follows:

If the total number of cells in the rectangle is even, then exactly half are even and half are odd. If the total is odd, then there's one more of one parity.

So for example, if the rectangle starts at (i_start, j_start) where i_start + j_start is even, then in a rectangle with even number of cells, half are even. If the number of cells is odd, then (cells+1)/2 are even.

But this depends on how the rectangle's dimensions. Let's model the problem.

The total number of cells in the rectangle is rows * cols, where rows = i_end - i_start + 1, cols = j_end - j_start + 1.

The number of cells where (i +j) is even can be computed as:

even_count = (rows * cols + (i_start + j_start) % 2) // 2

Wait, let's see. For example, if the top-left cell is even (i_start +j_start even), then in a 2x2 rectangle, there are 2 even and 2 odd. So (4 + 0) /2 =2 even. For a 1x1 rectangle, (1 +0)/2=0.5, but floor or ceil? Wait, the formula (rows*cols + p) //2, where p is 1 if the top-left cell is even, else 0. Wait, perhaps not. Let's think of another way.

The parity of i+j alternates with each step in i or j. So for a rectangle with rows rows and cols columns:

The first row has (cols + (i_start + j_start) % 2) // 1 cells of even parity.

Alternatively, the count can be derived as follows:

For each row i, the parity of i + j alternates with each column. So the number of even parities in row i is (cols + (i + j_start) % 2) // 2 * 2 + ...? Maybe not. Let's think of the row i. j ranges from j_start to j_end. The number of even j's in this row is ceil(cols / 2) if (i + j_start) is even, else floor(cols / 2). So for each row, the even count depends on the parity of (i + j_start).

So the total even count is the sum over all rows i in [i_start, i_end] of ceil( cols / 2 ) if (i + j_start) is even, else floor( cols / 2 ).

This can be simplified:

If cols is even, then ceil and floor are equal. So each row contributes cols/2 even parities. So total even count is rows * (cols / 2).

If cols is odd, then each row alternates between (cols +1)/2 and (cols-1)/2 even parities. The sum depends on the number of rows and the parity of the first row.

So overall, the formula for even_count is:

if rows * cols is even:

   even_count = (rows * cols) // 2

else:

   even_count = (rows * cols) // 2 + ((i_start + j_start) % 2 == 0)

But perhaps there's a better way.

Alternatively, the even_count can be computed as:

even_count = ((rows * cols) // 2) + ( (rows * cols) % 2 ) * ((i_start + j_start) % 2 == 0 )

This formula works because when the total number of cells is even, it's exactly half even and half odd. When it's odd, the extra cell is even if the top-left cell is even.

So putting this together:

rows = max(0, i_end - i_start + 1)

cols = max(0, j_end - j_start + 1)

if rows ==0 or cols ==0:

   even_count =0

else:

   total = rows * cols

   even_count = total // 2

   if total % 2 ==1:

       if (i_start + j_start) %2 ==0:

           even_count +=1

So for each rectangle defined by i_start, i_end, j_start, j_end, we can compute the number of even (i+j) cells.

Now, returning to the problem. For a given k, the rectangle of i is from k to (n-1 -k), and j from k to (m-1 -k). So the number of cells in this rectangle is (n_available) * (m_available), where n_available = max(0, n - 2k -1), etc. Wait, wait. Because the number of i's in the range [k, n-1 -k] is (n-1 -k) -k +1 = n - 2k. So if n >= 2k +1, else 0.

So the number of rows is n_available = max(0, (n-1 -k) -k +1 ) = max(0, n - 2k )

Similarly for columns: m_available = max(0, m - 2k )

So the i starts at k, ends at (n-1 -k), j starts at k, ends at (m-1 -k). So the i_start =k, i_end =n-1 -k. j_start=k, j_end =m-1 -k.

So rows = i_end - i_start +1 = (n-1 -k) -k +1 = n - 2k.

Similarly for cols.

Now, the number of even cells in this rectangle is:

if (n_available * m_available) ==0: 0

else:

compute even_count as per the formula above.

So, for a given k, the number of even cells in the rectangle is:

even_count = (total_cells // 2) + ( (total_cells % 2) ) * ( (k + k) %2 ==0 )

Because i_start =k, j_start=k. So (i_start +j_start) is 2k, which is even. So (i_start + j_start) mod2 is 0.

So in the case where the total_cells is odd, even_count is (total_cells //2) +1.

So, the formula simplifies to:

even_count = (total_cells +1) // 2 if total_cells is odd.

Otherwise, even_count = total_cells // 2.

Which can be written as:

even_count = (total_cells + 1) // 2 if (total_cells %2 ==1) else (total_cells//2).

But since 2k is even, k can be any integer, but (k +k) is even, so (i_start +j_start) is even. So when the total_cells (rows * cols) is odd, we add 1.

So even_count = (rows * cols + 1) // 2 when rows * cols is odd, and even_count = rows * cols //2 otherwise.

So combining all this:

for a given k, the number of black squares where a >=k and b >=k is:

if n_available <=0 or m_available <=0: 0

else:

compute rows =n_available, cols =m_available.

total_cells = rows * cols.

even_count = (total_cells +1) //2 if total_cells %2 else total_cells//2.

So for the given k, the even_count is the number of black squares in the rectangle.

Now, the problem requires us to compute the number of squares where min(a,b) =k. Which is (even_count(k) - even_count(k+1)).

So for x, we need to compute k =x-1. Then, compute even_count(k) - even_count(k+1).

But what if k is such that even_count(k) or even_count(k+1) is zero?

So the steps are:

1. Check if x is zero. But according to the input constraints, x >=1. So no.

2. Compute k =x-1.

3. Compute the number of squares where min(a,b) =k. Which is even_count(k) - even_count(k+1).

But how to compute even_count(k):

Compute the number of i's in [k, n-1 -k], which is n_available =n - 2k.

Similarly, m_available =m -2k.

If either n_available <=0 or m_available <=0, then even_count(k) is zero.

Else, rows =n_available, cols =m_available.

Compute total_cells = rows * cols.

even_count = (total_cells +1) //2 if total_cells is odd else total_cells//2.

Similarly for even_count(k+1).

Then, the answer is even_count(k) - even_count(k+1).

So now, the code can be written as follows.

But we need to compute even_count for k and k+1.

Now, let's code this.

First, read n, m, x.

Compute k =x-1.

Then, compute even_count(k) and even_count(k+1).

The answer is max(0, even_count(k) - even_count(k+1)).

So in Python:

def compute_even_count(n, m, k):
    rows = n - 2 * k
    cols = m - 2 * k
    if rows <=0 or cols <=0:
        return 0
    total = rows * cols
    if total %2 ==0:
        return total //2
    else:
        return (total +1) //2

Then, for x:

k = x-1

count_k = compute_even_count(n, m, k)

count_k_plus_1 = compute_even_count(n, m, k+1)

result = max(0, count_k - count_k_plus_1)

But wait, what about the cases where k is negative? Well, since x >=1, k=x-1 can be zero. So for x=1, k=0.

But in compute_even_count, if k is negative, then rows and cols would be larger than n and m, which would be impossible. So the code checks for rows and cols being <=0. So for k negative, rows =n - 2*k would be n + positive number, which is greater than n. But in the code, rows is n -2*k. But if k is negative, then 2k is negative, so rows =n + |2k|. Which would be larger than n. But the i's are from k to (n-1 -k). If k is negative, then k can be less than zero, but then (n-1 -k) would be larger than n-1. So i ranges would be invalid, leading to rows = (n-1 -k) -k +1 =n-1 -2k +1 =n -2k. But if k is negative, this becomes n -2k >=n +2|k|, which can't be valid as i must be <=n-1. So in code, rows would be negative if k is negative? Let's see:

For example, k =-1:

rows =n - 2*(-1) =n+2.

But then, in compute_even_count, rows =n+2, but cols =m -2*(-1) =m+2. Then, since rows and cols are positive (since n and m are at least 1), compute_even_count returns ( (n+2)*(m+2) +1 )//2 if odd. But this is not the case. Because in reality, the i's would start at k=-1, which is outside the grid. So for k <0, the code would compute rows and cols as n-2k and m-2k. For k =-1, rows =n +2. But the actual i's would be from -1 to (n-1 +1) =n. Which is beyond the grid's i (0-based). So the code's compute_even_count is incorrect for k <0.

But in our problem, k can't be less than zero. Because x >=1 implies k=x-1 >=0. So for the problem's input, k is always >=0. So no need to handle negative k.

Thus, the code is correct.

Testing the first example:

n=3, m=3, x=1. So k=0.

compute_even_count(3,3,0):

rows =3-0=3, cols=3-0=3.

total=3*3=9, which is odd. So even_count=(9+1)/2=5.

Then compute_even_count(3,3,1):

rows=3-2=1, cols=3-2=1. rows*cols=1. even_count=(1+1)/2=1.

result=5-1=4. Which matches the first example.

Another example: x=2. k=1.

compute_even_count(3,3,1) is 1. compute_even_count(3,3,2):

rows=3-4= -1, cols=3-4=-1. So even_count=0. result=1-0=1. Which matches the second example.

Third example: n=1, m=1, x=1. k=0.

rows=1-0=1, cols=1-0=1. total=1, even_count= (1+1)/2=1. k+1=1: rows=1-2= -1, even_count=0. result=1-0=1. Correct.

So this works.

Now, the code can be written as follows.

Read n, m.

Read x.

Compute k = x-1.

Compute count_k = compute_even_count(n, m, k)

count_k_plus_1 = compute_even_count(n, m, k+1)

result = max(0, count_k - count_k_plus_1)

Print result.

So the code is straightforward.

Now, handling large x. For example, if x is 1e9, then k=999,999,999.

But in compute_even_count(n, m, k), rows =n - 2k. For n up to 5000, if k is 1e9, then rows would be 5000 - 2e9, which is negative, so compute_even_count returns 0. Similarly for cols. So the code can handle very large x values efficiently.

Thus, this approach works for all cases.

Now, let's code this.

The code will read n, m from input, then x. Then compute the result as described.

Here's the code:

Read n, m:

n, m = map(int, input().split())

Read x:

x = int(input())

k = x -1

Then compute the even counts.

Implement compute_even_count as a function.

But in Python, functions are allowed.

But to optimize for speed, perhaps inline the computation.

But for code clarity, it's better to write a helper function.

But the code needs to be in a single code block. So let's code it.

Putting it all together:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    x = int(input_stream.readline().rstrip("\n"))

    k = x - 1

    def compute(k_val):
        rows = n - 2 * k_val
        cols = m - 2 * k_val
        if rows <=0 or cols <=0:
            return 0
        total = rows * cols
        if total % 2 == 0:
            return total // 2
        else:
            return (total + 1) // 2

    count_k = compute(k)
    count_k_plus_1 = compute(k + 1)

    print(max(0, count_k - count_k_plus_1), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 3
2
""",
            "output": \
"""\
1
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    x = int(input_stream.readline().rstrip("\n"))

    k = x - 1

    def compute(k_val):
        rows = n - 2 * k_val
        cols = m - 2 * k_val
        if rows <=0 or cols <=0:
            return 0
        total = rows * cols
        if total % 2 == 0:
            return total // 2
        else:
            return (total + 1) // 2

    count_k = compute(k)
    count_k_plus_1 = compute(k + 1)

    print(max(0, count_k - count_k_plus_1), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 1
1
""",
            "output": \
"""\
1
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

Third example:

1 1 1 → k=0. rows=1, cols=1. total=1 → (1+1)/2=1. compute(1) returns 0. 1-0=1.

All correct.

Thus, this code should handle all cases efficiently, even for large n and m up to 5000 and x up to 1e9. The time complexity is O(1) as it's a few arithmetic operations, regardless of the input size. So it's optimal.
</think>

```python
n, m = map(int, input().split())
x = int(input())

k = x - 1

def compute(k_val):
    rows = n - 2 * k_val
    cols = m - 2 * k_val
    if rows <= 0 or cols <= 0:
        return 0
    total = rows * cols
    return (total + 1) // 2 if total % 2 else total // 2

count_k = compute(k)
count_k_plus_1 = compute(k + 1)

print(max(0, count_k - count_k_plus_1))
```
