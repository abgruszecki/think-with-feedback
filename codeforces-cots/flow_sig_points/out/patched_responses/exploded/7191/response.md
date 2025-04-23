<think>
Okay, I need to solve this programming problem where the goal is to determine if the white king is in check based on the positions of various black pieces. Let's think through the problem step by step.

First, the problem statement says that the king is in check if any black piece can reach his position in one move, considering their movement rules and the presence of other pieces blocking their path. So the main task is to check each black piece and see if it can attack the king, considering possible blocks.

The constraints are up to 500,000 pieces, which is a lot. So any solution that is O(n) is acceptable, but anything higher (like O(n^2)) would be too slow. So the approach needs to efficiently check each piece in O(1) per piece, maybe with some pre-processing.

Let's break down each piece's possible attack:

1. **Bishop ('B')**: Can attack along diagonals. The king's position must be on the same diagonal (i.e., |x_king - x_bishop| == |y_king - y_bishop|). Also, there must be no pieces between the bishop and the king. If there's another piece in the line between them, the bishop can't attack.

2. **Rook ('R')**: Can attack along same row or column. The king must be in the same row or column. Again, check if any pieces are in between.

3. **Queen ('Q')**: Can attack like a rook or bishop. So need to check both possibilities.

So for each piece, depending on its type, we need to check if it's in a position that could attack the king, and then ensure that there are no other pieces in the path.

But the problem is that for each piece, checking all other pieces to see if they block the path is O(n^2), which is impossible for n=5e5.

Hmm. So how can we efficiently check if any blocking pieces exist between a given piece and the king?

The key idea here is that for each possible line (row, column, or diagonal) that the king is on, we need to track the closest piece in each direction. For example, for the row of the king, the closest rook or queen to the left and right would determine if there's a possible attack. Similarly for other directions and other lines.

But how to do this efficiently?

Let me think. The king's position is (x0, y0). For each black piece, we need to check:

- For a bishop: if (xi, yi) is on a diagonal, and between the king and the bishop there are no other pieces. But how to check that?

Wait, perhaps the approach is to track for each direction (like the four directions for rook: up, down, left, right) and the four diagonal directions (for bishop) the closest piece that can attack in that direction.

For example:

For the rook's lines (same row or column):

- For the same row (y0), check if there's a rook or queen in that row. The closest ones to the left (x < x0) and right (x > x0) of the king. If the closest piece to the left is a rook or queen, and there's no other piece between them and the king, then the king is in check. Similarly for right, up, and down.

Same for the same column (x0), check above and below.

For bishops, check the four diagonals. Each diagonal is determined by (x0 - xi) == (y0 - yi) or (x0 - xi) == -(y0 - yi). The closest pieces along each diagonal direction (like northeast, northwest, southeast, southwest) would determine if a bishop or queen is in that line and unobstructed.

So the plan is:

1. Precompute all eight possible directions (four for rook/queen, four for bishop/queen) and for each direction, track the closest black piece that can attack the king, and whether there's any blocking pieces between them and the king.

Wait, but how do we efficiently find the closest piece in each direction and check if there's any blockers?

Alternative approach:

For each piece, determine if it's in a line that can attack the king (same row, column, or diagonal), and then check if it's the closest one in that direction. If there's a closer piece in that line, then this piece is blocked by that closer piece.

Wait, but even if a piece is in the same line, but there's another piece between it and the king, then the first piece can't attack. So for each possible direction (like, for same row, left side of king), the closest piece in that direction would be the one that could attack. If that closest piece is a rook or queen (for same row/col) or bishop/queen (for diagonal), then the king is in check.

So the steps would be:

1. For all black pieces, group them into the possible lines (row, column, two diagonals) relative to the king's position.

2. For each line (direction), find the closest piece in that line towards the king. Then check if that piece is of a type that can attack via that line.

For example:

- For the same row (y0) as the king, check pieces with yi = y0. For these pieces, split into those left (xi < x0) and right (xi > x0). The closest piece to the king in the left direction (max xi) would be the one that can potentially attack if it's a rook or queen. Similarly for right (min xi) if xi is larger than x0.

But wait, in the same row (y0), the direction left is all pieces with xi < x0. The closest would be the one with the largest xi (since they are to the left of the king, the closer ones are those with higher xi). Similarly, for pieces to the right (xi > x0), the closest is the one with the smallest xi.

If any of these closest pieces in the left or right direction is a rook or queen, then that's a check.

Same logic for vertical (same column x0). The closest pieces above (yi > y0) is the one with the smallest yi (closest to the king), and below (yi < y0) is the one with largest yi.

For the two diagonals (bishop directions):

- Diagonal 1: x - x0 = y - y0. So pieces on this diagonal have (xi - x0) == (yi - y0). For these, the direction is northeast (xi > x0, yi > y0) and southwest (xi < x0, yi < y0). The closest in northeast is the one with smallest (xi - x0), which is the same as smallest (yi - y0). Similarly, southwest is the largest (xi - x0) (since xi is less than x0, so xi -x0 is negative; the largest value here is the closest to x0).

- Diagonal 2: x -x0 = -(y - y0). So pieces on this diagonal have (xi -x0) + (yi - y0) = 0. Directions are northwest (xi > x0, yi < y0) and southeast (xi < x0, yi > y0). Closest in northwest direction is the one with smallest (xi -x0) (since yi decreases as xi increases), and closest in southeast is the one with smallest (y0 - yi) (or equivalently, largest (xi -x0) since it's negative).

Wait, this is getting a bit complicated. Let's think of each of the eight possible directions (for four lines: row, column, two diagonals) and for each direction, track the closest piece.

For each line:

1. Same row (y0):

   a. Left direction (xi < x0): the closest is the maximum xi in this group. If this piece is a rook or queen, then king is in check.

   b. Right direction (xi > x0): the closest is the minimum xi in this group. If this piece is a rook or queen, then check.

2. Same column (x0):

   a. Below (yi < y0): closest is maximum yi in this group. If rook or queen, check.

   b. Above (yi > y0): closest is minimum yi in this group. If rook or queen, check.

3. Diagonal 1 (x - x0 = y - y0):

   a. Northeast (xi > x0, yi > y0): closest is the one with smallest (xi - x0). Because as xi increases, yi also increases. So the closest is the one where xi - x0 is smallest (xi is x0 +1, etc.) So for pieces in this direction, the minimum (xi - x0) gives the closest. If this piece is a bishop or queen, check.

   b. Southwest (xi < x0, yi < y0): here, the distance from the king is (x0 - xi) = (y0 - yi). The closest here is the maximum (xi - x0) (since xi < x0, xi -x0 is negative. The maximum would be the one closest to x0). For example, if the king is at (4,2), a piece at (3,1) has (3-4) = -1, and (1-2) = -1. So xi -x0 is -1. The maximum of these values is the closest. So for southwest direction, the piece with maximum (xi - x0) is the closest. If this is a bishop or queen, check.

4. Diagonal 2 (x -x0 = -(y - y0)):

   a. Northwest (xi > x0, yi < y0): distance in x is xi -x0, and distance in y is y0 - yi. For these pieces, the sum (xi -x0) + (y0 - yi) is 0. The closest is the one with smallest (xi -x0), which corresponds to the smallest distance. For example, if xi is x0+1 and yi is y0-1, that's the closest. So in this direction, find the minimum (xi -x0), and check if that piece is a bishop or queen.

   b. Southeast (xi < x0, yi > y0): here, xi is less than x0, yi is larger. The distance is (x0 - xi) = (yi - y0). The closest is the one with maximum (xi -x0) (since xi -x0 is negative, the maximum is the least negative, i.e., closest to x0). For example, xi = x0-1, yi = y0+1: xi -x0 is -1. So the maximum of (xi -x0) here is -1 (closest). So for this direction, find the maximum (xi -x0) and check if the piece is bishop or queen.

If any of these eight directions has a piece of the correct type (rook/queen for row and column, bishop/queen for diagonals), then the king is in check.

The key here is that for each direction, among all the pieces in that direction, the closest one is the only possible attacker, because any other pieces behind it (farther from the king) are blocked by the closest one.

So the approach would be:

- For each of the eight possible directions (left, right, up, down, northeast, southwest, northwest, southeast), track the closest piece.

- For each such direction, if the closest piece exists and is of a type that can attack via that direction, return "YES".

So the steps are:

1. Read the king's position (x0, y0).

2. For each black piece, check which direction (if any) it is in relative to the king. For each direction, track the closest piece.

3. After processing all pieces, check each of the eight directions. If any direction has a closest piece of the correct type, return YES. Otherwise, NO.

So the data structures needed are variables to track the closest pieces in each of the eight directions. Each direction can be represented by a key, and for each, we keep the closest distance and the type.

But how to represent the eight directions? Let's see:

For same row (y0):

- Left: xi < x0, yi = y0. Track maximum xi (closest to x0).

- Right: xi > x0, yi = y0. Track minimum xi (closest to x0).

For same column (x0):

- Below: yi < y0, xi =x0. Track maximum yi (closest to y0).

- Above: yi > y0, xi =x0. Track minimum yi (closest to y0).

For diagonal 1 (xi -x0 = yi - y0):

- Northeast: xi > x0, yi > y0. Track the one with smallest (xi -x0) (which is the same as smallest (yi -y0)), as that's the closest.

- Southwest: xi < x0, yi < y0. Track the largest (xi -x0) (since xi is less than x0, this would be the closest to x0).

For diagonal 2 (xi -x0 = -(yi - y0)):

- Northwest: xi > x0, yi < y0. Track the smallest (xi -x0) (closest to x0).

- Southeast: xi < x0, yi > y0. Track the largest (xi -x0) (since xi < x0, largest is closest to x0).

So for each of these eight directions, we can track the best candidate (the closest piece in that direction). For each direction, we have a variable that holds the position and type of the closest piece. Then, after processing all pieces, check each direction's closest piece to see if it can attack.

Now, the problem is how to efficiently check for each piece which direction it belongs to, and update the closest candidate for that direction if needed.

Let's outline this:

Initialize variables for each direction:

For same row (y0):

- left_rook: (xi_max, type) where xi is maximum among xi < x0. Only consider pieces with yi=y0 and xi < x0. If type is R or Q, then king is in check.

- right_rook: (xi_min, type) where xi is minimum among xi > x0. Similarly.

For same column (x0):

- below_rook: (yi_max, type) for yi < y0 and xi=x0.

- above_rook: (yi_min, type) for yi > y0 and xi=x0.

For diagonal1 (xi-x0 = yi -y0):

- northeast_bishop: (delta_x, type) where delta_x is xi -x0 (positive), and delta_x is the smallest (closest). So the piece is in this direction if xi >x0 and yi >y0 and xi-x0 == yi -y0. The closest is the one with smallest delta_x.

- southwest_bishop: (delta_x, type) where xi <x0 and yi <y0 and xi-x0 = yi -y0. Since delta_x is negative, the largest delta_x (closest to 0) is the maximum of (xi -x0) values. For example, if xi is x0-3, delta_x is -3. The maximum is -1 (closer) compared to -3.

For diagonal2 (xi -x0 = -(yi -y0)):

- northwest_bishop: (delta_x, type) where xi >x0 and yi <y0. The delta_x is xi -x0. The smallest delta_x (closest) is the best.

- southeast_bishop: (delta_x, type) where xi <x0 and yi >y0. delta_x is xi -x0 (negative). The maximum delta_x (closest to 0) is the best.

Wait, for the southeast direction:

xi <x0 and yi> y0. So xi-x0 is negative. The equation is xi -x0 = -(yi - y0) => yi = y0 - (xi -x0) => since xi <x0, xi -x0 is negative, so yi = y0 + (x0 - xi). So yi increases as xi decreases.

The delta_x for southeast direction is xi -x0 (negative). The largest delta_x (closest to 0) is the maximum (xi -x0), which is the least negative. For example, xi-x0 of -1 is better (closer) than -3.

So for each of these directions, we can track the best candidate.

So for each piece, we first check which directions it's in. For example, a piece could be in the same row (left or right), same column (below or above), or one of the four diagonal directions.

For each direction that the piece is in, we compare it with the current best candidate for that direction and update if it's closer.

Let's take an example. Suppose the king is at (4, 2).

A piece at (1,1) is R. Let's see:

Check if yi = y0 (2). No, so not in same row. Check if xi =x0 (4). No, so not same column. Check diagonals:

For diagonal1: (1-4) = (1-2) → -3 = -1 → no. So not in diagonal1.

For diagonal2: (1-4) = -(1-2) → -3 = -(-1) → -3=1 → no. So not in any diagonal. So this piece is not in any direction. So it can't attack.

Wait, but in the first sample input:

Sample 1:

2

4 2

R 1 1

B 1 5

The output is YES. So the rook is at (1,1), king at (4,2). The rook is not in same row or column. So how does the rook attack?

Wait, the sample input must have a different scenario. Wait, in sample 1, the king is at (4, 2). The first piece is R at (1,1). How can that rook attack?

Wait, maybe the sample input is different. Let me check:

First sample input:

2

4 2

R 1 1

B 1 5

So the R is at (1,1). The king is at (4,2). The rook is not in the same row (2) or column (4). So the rook cannot attack. Then why is the output YES?

Ah, the other piece is B at (1,5). Let's see.

The bishop's position is (1,5). The king is at (4,2). The difference is (1-4) = -3, (5-2)=3. So the absolute differences are equal (3), so they are on the same diagonal. So the bishop could attack if there's no blocking.

So the bishop's line is diagonal2 (since (xi -x0) is -3, (yi -y0) is 3. So (xi -x0) = -(yi -y0). So it's on diagonal2. The direction is southeast (xi <x0, yi> y0). So the bishop is at (1,5), which is southeast of the king. So the bishop can attack if there are no pieces between them.

But in the first sample, the output is YES. So that bishop must be the closest in that direction, and no other pieces blocking.

So in that case, the code would track the southeast direction for the bishop. Since there's no other piece in that line, the bishop can attack.

But the first sample's output is YES, which suggests that the bishop is indeed attacking. So the code should find that.

But how to track this.

So, the plan is:

For each piece, check which of the eight directions it's in. For each direction, track the closest piece.

So for each piece:

- Check if it's in same row as king (y == y0). If yes, check if x < x0 (left direction) or x > x0 (right direction). For left, compare x with current left_rook's x. Keep the maximum x (closest to x0). Similarly for right direction, keep the minimum x.

- Check if it's in same column (x == x0). If yes, check if y < y0 (below) or y > y0 (above). For below, track the maximum y (closest to y0). For above, track the minimum y.

- Check if it's on diagonal1 (x -x0 = y - y0). For this, calculate (xi -x0) and (yi -y0). If they are equal, then it's on diagonal1. Then check if it's in northeast (xi >x0) or southwest (xi <x0). For northeast direction, track the smallest (xi -x0) (which is same as smallest (yi -y0)). For southwest, track the largest (xi -x0) (since xi <x0, the delta is negative, and the largest is the closest to 0).

- Check if it's on diagonal2 (x -x0 = -(y - y0)). So (xi -x0) + (yi -y0) = 0. Then check if it's in northwest (xi >x0, yi <y0) or southeast (xi <x0, yi > y0). For northwest, track the smallest (xi -x0). For southeast, track the largest (xi -x0) (since xi <x0, delta is negative, largest is closest to 0).

For each of these eight directions, if the piece is in that direction, and is the closest so far, then update the best candidate for that direction.

Once all pieces are processed, check each direction:

For left_rook and right_rook: if the candidate exists and is R or Q.

For below_rook and above_rook: same.

For northeast_bishop, southwest_bishop: if the candidate exists and is B or Q.

For northwest_bishop, southeast_bishop: same.

If any of these conditions is true, output YES. Else NO.

Now, the key is to efficiently process each of the n pieces and check which direction they belong to.

Let's think about possible code structure.

First, read n, x0, y0.

Then, for each of the n pieces:

Read type, xi, yi.

Check if (xi, yi) is in any of the eight directions.

For each direction, compute if it's applicable, then check if it's closer than the current best.

For example, for same row (yi == y0):

if xi < x0: left direction.

current best left is max_xi. So if this xi is larger than current max_xi, then update.

Similarly for right direction (xi > x0): track the min xi.

For same column (xi == x0):

if yi < y0: track the max yi.

if yi > y0: track the min yi.

For diagonal1: (xi -x0) == (yi -y0):

if xi >x0 and yi >y0: northeast direction.

delta = xi -x0.

current best is the smallest delta. So if this delta is smaller than current best, update.

if xi <x0 and yi <y0: southwest direction.

delta is xi -x0 (negative). current best is the maximum delta (closest to zero). So if this delta is larger than current best, update.

For diagonal2: (xi -x0) == -(yi -y0):

xi >x0 and yi <y0: northwest direction.

delta is xi -x0. current best is the smallest delta.

xi <x0 and yi >y0: southeast direction.

delta is xi -x0 (negative). current best is the maximum delta (closest to zero). So if current max delta is stored, and this delta is larger than current max, update.

But how to track the best in each direction?

We can initialize each direction's best as None. Then, for each piece, check if it's in the direction, and then compare with the current best and update if necessary.

For example:

Initialize:

left_rook = None (xi <x0, yi=y0, max xi)
right_rook = None (xi >x0, yi=y0, min xi)
below_rook = None (yi <y0, xi=x0, max yi)
above_rook = None (yi >y0, xi=x0, min yi)
northeast_bishop = None (xi >x0, yi>y0, delta=xi-x0, min delta)
southwest_bishop = None (xi <x0, yi <y0, delta=xi-x0, max delta)
northwest_bishop = None (xi >x0, yi<y0, delta=xi-x0, min delta)
southeast_bishop = None (xi <x0, yi>y0, delta=xi-x0, max delta)

For each piece (type, xi, yi):

Check if yi == y0 (same row):
   if xi <x0:
       if left_rook is None or xi > left_rook[0]:
           left_rook = (xi, type)
   elif xi >x0:
       if right_rook is None or xi < right_rook[0]:
           right_rook = (xi, type)

Check if xi ==x0 (same column):
   if yi < y0:
       if below_rook is None or yi > below_rook[0]:
           below_rook = (yi, type)
   elif yi > y0:
       if above_rook is None or yi < above_rook[0]:
           above_rook = (yi, type)

Check for diagonal1 (xi -x0 == yi - y0):
   if xi >x0 and yi >y0:
       delta = xi -x0
       if northeast_bishop is None or delta < northeast_bishop[0]:
           northeast_bishop = (delta, type)
   elif xi <x0 and yi <y0:
       delta = xi -x0
       if southwest_bishop is None or delta > southwest_bishop[0]:
           southwest_bishop = (delta, type)

Check for diagonal2 (xi -x0 == -(yi -y0)):
   if xi >x0 and yi <y0:
       delta = xi -x0
       if northwest_bishop is None or delta < northwest_bishop[0]:
           northwest_bishop = (delta, type)
   elif xi <x0 and yi >y0:
       delta = xi -x0
       if southeast_bishop is None or delta > southeast_bishop[0]:
           southeast_bishop = (delta, type)

Once all pieces are processed, check each direction:

For left_rook: if exists and (type is R or Q) --> check yes.
For right_rook: same.
For below_rook: same.
For above_rook: same.

For northeast_bishop: exists and (type is B or Q) --> check yes.
southwest_bishop: same.
northwest_bishop: same.
southeast_bishop: same.

If any of these is true, output YES. Else NO.

This approach is O(n) time, as each piece is processed once, and for each piece, we check several conditions (which are O(1) per check). Since n can be up to 5e5, this is acceptable.

Now, let's test this approach against the sample inputs.

Sample 1:

Input:

2

4 2

R 1 1

B 1 5

King is at (4,2).

Processing the first piece: R at (1,1).

Check same row: yi=1 !=2. No.

Same column: xi=1 !=4. No.

Check diagonal1: 1-4 = -3, 1-2 = -1. Not equal. No.

Check diagonal2: (1-4) = -(1-2) → -3 = -(-1) → -3 =1 → no. So not in any direction. So this R piece does not contribute to any direction.

So left_rook, right_rook, etc. remain None.

Second piece: B at (1,5).

Check same row: yi=5 !=2. No.

Same column: xi=1 !=4. No.

Check diagonal1: (1-4) =-3, (5-2)=3. Not equal. So no.

Check diagonal2: (1-4) =-3, -(5-2) =-3. So (xi-x0) = -(yi -y0). Yes. So this is on diagonal2.

xi=1 <4, yi=5>2. So it's in the southeast direction.

delta = xi -x0 = 1-4 =-3.

Check if southeast_bishop is None or delta (current) is larger than existing.

Initially, southeast_bishop is None. So set to (-3, 'B').

So southeast_bishop is (delta=-3, type B).

Now, after processing all pieces, check each direction.

Check left_rook: None. So no.

right_rook: None. No.

below_rook: None.

above_rook: None.

northeast_bishop: None.

southwest_bishop: None.

northwest_bishop: None.

southeast_bishop: exists. Type is B. So bishop can attack via diagonal2. So output YES.

So sample 1's code would return YES, which matches.

Sample 2:

Input:

2

4 2

R 3 3

B 1 5

King is at (4,2).

First piece: R at (3,3).

Check same row: yi=3 !=2. No.

Same column: xi=3 !=4. No.

Check diagonal1: (3-4) =-1, (3-2)=1. Not equal. No.

Check diagonal2: (3-4) =-1, -(3-2)= -1. So yes. So (xi-x0) = -(yi -y0) → delta =-1.

xi=3 <4? No. xi=3 is less than 4. Wait xi is 3, x0 is 4. So xi <x0? 3<4 is true. yi=3>2.

So delta=3-4 =-1. So (xi <x0, yi>y0) → southeast direction.

So check southeast_bishop.

Current southeast_bishop is None. So set to (delta=-1, type R).

Then, the second piece is B at (1,5). For this:

Check diagonal2: (1-4) =-3, -(5-2)=-3 → yes.

xi=1 <4, yi=5>2 → southeast direction.

delta =1-4=-3. Compare with current southeast_bishop's delta (-1). The current delta is -3, which is less than -1 (since we need the maximum delta). So -3 is less than -1, so not better. So southeast_bishop remains (-1, R).

Now, after processing all pieces:

Check southeast_bishop. Type is R. So since this is a diagonal2 direction (bishop/queen), but the piece is R. So R cannot attack via bishop's direction. So southeast_bishop's type is R → invalid.

So no check from this direction.

Other directions:

Check left_rook, right_rook, etc. All are None.

So output is NO.

Which matches the sample.

Another test case: a queen in the same row as king, but blocked by another piece.

For example:

King at (4,2).

Queen at (5,2) (right direction). Rook at (6,2).

The queen is right direction (xi=5>4). The rook is at 6>4. The queen is closer (xi=5 is min between 5 and 6). So the queen is the closest. Since she is queen, which is R or Q (queen can act as rook). So the king is in check.

But if there's another piece between queen and king, like queen at (5,2) and a bishop at (4,2), but the problem states that the king is at (4,2), so no piece can be there (as per input, all pieces are on different positions). So in this example, the queen is the closest and is Q, so check is yes.

But in case another piece is between queen and king. Wait, but queen is at (5,2). Suppose a bishop is at (4,2) → but that's king's position. So it's impossible. So in practice, the only possible way for a piece to block is to be between the attacker and the king.

But in the code's approach, the code only tracks the closest piece in each direction. Any pieces beyond that are ignored, as they would be blocked by the closest. So in the case where a queen is at (5,2) and a rook is at (6,2), the queen is the closest, so the rook is blocked, and queen's type (Q) is allowed. So the code would correctly report check.

Now, code implementation.

So the code will need to:

- Read n.

- Read x0, y0.

- Initialize the eight directions with None.

- For each of the n pieces:

   Read type, xi, yi.

   Check if (xi, yi) is same as (x0, y0) → but according to problem statement, all pieces are in different positions, so no.

   Then, check for same row, same column, then diagonals.

   For same row (yi == y0):

       if xi <x0:

           if left_rook is None or xi > left_rook's xi:

               update left_rook to (xi, type).

       elif xi >x0:

           if right_rook is None or xi < right_rook's xi:

               update right_rook to (xi, type).

   For same column (xi ==x0):

       if yi <y0:

           if below_rook is None or yi > below_rook's yi:

               update below_rook to (yi, type).

       elif yi >y0:

           if above_rook is None or yi < above_rook's yi:

               update above_rook to (yi, type).

   For diagonal1:

       if (xi -x0) == (yi -y0):

           if xi >x0 and yi >y0:

               delta = xi -x0

               if northeast_bishop is None or delta < northeast_bishop's delta:

                   northeast_bishop = (delta, type)

           elif xi <x0 and yi <y0:

               delta = xi -x0

               if southwest_bishop is None or delta > southwest_bishop's delta:

                   southwest_bishop = (delta, type)

   For diagonal2:

       if (xi -x0) == -(yi -y0):

           if xi >x0 and yi <y0:

               delta = xi -x0

               if northwest_bishop is None or delta < northwest_bishop's delta:

                   northwest_bishop = (delta, type)

           elif xi <x0 and yi >y0:

               delta = xi -x0

               if southeast_bishop is None or delta > southeast_bishop's delta:

                   southeast_bishop = (delta, type)

Once all pieces are processed, check each of the eight directions:

For left_rook: if exists and (type is 'R' or 'Q') → yes.

Same for right_rook, below_rook, above_rook.

For northeast_bishop: if exists and (type is 'B' or 'Q') → yes.

Same for southwest_bishop, northwest_bishop, southeast_bishop.

If any of these is true, output YES. Else NO.

Now, code this in Python.

But note that for n=5e5, the code must be efficient. So using input methods like sys.stdin.readline is better. Also, the code should avoid using too many variables, but in this case, the variables are manageable.

Now, let's code this.

We'll need variables for each of the eight directions. For example:

left_rook: (max_xi, type)

right_rook: (min_xi, type)

below_rook: (max_yi, type)

above_rook: (min_yi, type)

northeast_bishop: (min_delta, type)

southwest_bishop: (max_delta, type)

northwest_bishop: (min_delta, type)

southeast_bishop: (max_delta, type)

Initialize all to None.

Then, for each piece:

Check each possible direction and update variables accordingly.

Once all pieces are processed, check each of the eight variables.

In Python, for example:

Read n.

x0, y0 = map(int, input().split())

Then, read n lines:

for _ in range(n):

    typ, xi, yi = input().split()

    xi = int(xi)

    yi = int(yi)

    # process this piece

Now, processing each piece:

Check same row (yi == y0):

if yi == y0:

    if xi <x0:

        if left_rook is None or xi > left_rook[0]:

            left_rook = (xi, typ)

    elif xi >x0:

        if right_rook is None or xi < right_rook[0]:

            right_rook = (xi, typ)

Check same column (xi ==x0):

elif xi ==x0:

    if yi < y0:

        if below_rook is None or yi > below_rook[0]:

            below_rook = (yi, typ)

    elif yi > y0:

        if above_rook is None or yi < above_rook[0]:

            above_rook = (yi, typ)

Check diagonals:

else:

    # Check diagonal1 (xi -x0 == yi -y0)

    delta_x = xi - x0

    delta_y = yi - y0

    if delta_x == delta_y:

        if xi > x0 and yi > y0:

            # northeast direction

            if northeast_bishop is None or delta_x < northeast_bishop[0]:

                northeast_bishop = (delta_x, typ)

        elif xi < x0 and yi < y0:

            # southwest direction

            if southwest_bishop is None or delta_x > southwest_bishop[0]:

                southwest_bishop = (delta_x, typ)

    # Check diagonal2 (xi -x0 == -(yi -y0))

    elif delta_x == -delta_y:

        if xi >x0 and yi < y0:

            # northwest direction

            if northwest_bishop is None or delta_x < northwest_bishop[0]:

                northwest_bishop = (delta_x, typ)

        elif xi <x0 and yi > y0:

            # southeast direction

            if southeast_bishop is None or delta_x > southeast_bishop[0]:

                southeast_bishop = (delta_x, typ)

Once all pieces are processed, check each direction:

Check for rook directions:

if (left_rook and left_rook[1] in ('R', 'Q')) or (right_rook and right_rook[1] in ('R', 'Q')):

    print("YES")

    exit()

if (below_rook and below_rook[1] in ('R', 'Q')) or (above_rook and above_rook[1] in ('R', 'Q')):

    print("YES")

    exit()

Check for bishop directions:

if (northeast_bishop and northeast_bishop[1] in ('B', 'Q')) or (southwest_bishop and southwest_bishop[1] in ('B', 'Q')):

    print("YES")

    exit()

if (northwest_bishop and northwest_bishop[1] in ('B', 'Q')) or (southeast_bishop and southeast_bishop[1] in ('B', 'Q')):

    print("YES")

    exit()

If none of the above, print "NO".

But wait, the code must check all directions. For example, the code should check all eight directions, not in groups. Wait, for the rook directions, there are four possible directions (left, right, below, above). Each of these can independently cause a check.

Wait, in code above, for example, left_rook and right_rook are checked first. So:

If left_rook is present and is R or Q, output YES.

Similarly, check right_rook, then below, then above.

But in code, the code first checks left_rook and right_rook (same row), then same column (below and above), then the four bishop directions.

But if any of these conditions is true, the code outputs YES.

So the code will check each direction in order and return as soon as any is found.

But in code, the code can check all four rook directions in four separate conditions.

Wait, the current code structure for checking:

After processing all pieces, we check each direction:

For the same row:

Check if left_rook exists and is R/Q.

Check if right_rook exists and is R/Q.

Same for same column.

Then for the four bishop directions.

So the code would look like this:

if left_rook and left_rook[1] in ('R', 'Q'):

    print("YES")

    exit()

if right_rook and right_rook[1] in ('R', 'Q'):

    print("YES")

    exit()

if below_rook and below_rook[1] in ('R', 'Q'):

    print("YES")

    exit()

if above_rook and above_rook[1] in ('R', 'Q'):

    print("YES")

    exit()

Then check the bishop directions:

if northeast_bishop and northeast_bishop[1] in ('B', 'Q'):

    print("YES")

    exit()

if southwest_bishop and southwest_bishop[1] in ('B', 'Q'):

    print("YES")

    exit()

if northwest_bishop and northwest_bishop[1] in ('B', 'Q'):

    print("YES")

    exit()

if southeast_bishop and southeast_bishop[1] in ('B', 'Q'):

    print("YES")

    exit()

print("NO")

But in code, perhaps it's better to check each condition and return as soon as any is true.

But in Python, using multiple if statements with exit() is acceptable.

Now, let's code this.

But also, note that for the bishop directions, the code needs to check the four possible directions (northeast, southwest, northwest, southeast).

But in code, each of the eight directions is checked separately.

So, the code should work.

Now, the code must read input efficiently. For n=5e5, using input() in a loop may be slow, so better to read from sys.stdin.

But in Python, the standard input can be read via sys.stdin, which is faster.

So the code can be optimized by reading all input at once.

But in code submission, sometimes it's better to split the input into lines.

But for the code, perhaps:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    n = int(input_stream.readline())

    x0, y0 = map(int, input_stream.readline().split())

    left_rook = None  # (xi, type)

    right_rook = None

    below_rook = None

    above_rook = None

    northeast_bishop = None  # (delta_x, type)

    southwest_bishop = None

    northwest_bishop = None

    southeast_bishop = None

    for _ in range(n):

        parts = input_stream.readline().split()

        typ = parts[0]

        xi = int(parts[1])

        yi = int(parts[2])

        # Check same row

        if yi == y0:

            if xi < x0:

                if left_rook is None or xi > left_rook[0]:

                    left_rook = (xi, typ)

            elif xi > x0:

                if right_rook is None or xi < right_rook[0]:

                    right_rook = (xi, typ)

        # Check same column

        elif xi == x0:

            if yi < y0:

                if below_rook is None or yi > below_rook[0]:

                    below_rook = (yi, typ)

            elif yi > y0:

                if above_rook is None or yi < above_rook[0]:

                    above_rook = (yi, typ)

        else:

            delta_x = xi - x0

            delta_y = yi - y0

            # Check diagonal1 (delta_x == delta_y)

            if delta_x == delta_y:

                if delta_x >0:

                    # northeast

                    if northeast_bishop is None or delta_x < northeast_bishop[0]:

                        northeast_bishop = (delta_x, typ)

                elif delta_x <0:

                    # southwest

                    if southwest_bishop is None or delta_x > southwest_bishop[0]:

                        southwest_bishop = (delta_x, typ)

            # Check diagonal2 (delta_x == -delta_y)

            elif delta_x == -delta_y:

                if delta_x >0:

                    # northwest (xi >x0, yi < y0)

                    if northwest_bishop is None or delta_x < northwest_bishop[0]:

                        northwest_bishop = (delta_x, typ)

                elif delta_x <0:

                    # southeast (xi <x0, yi> y0)

                    if southeast_bishop is None or delta_x > southeast_bishop[0]:

                        southeast_bishop = (delta_x, typ)

    # Check all directions

    # Check same row left and right

    if left_rook and left_rook[1] in ('R', 'Q'):

        print("YES", file=output_stream)

        return

    if right_rook and right_rook[1] in ('R', 'Q'):

        print("YES", file=output_stream)

        return

    # Check same column below and above

    if below_rook and below_rook[1] in ('R', 'Q'):

        print("YES", file=output_stream)

        return

    if above_rook and above_rook[1] in ('R', 'Q'):

        print("YES", file=output_stream)

        return

    # Check bishops

    if northeast_bishop and northeast_bishop[1] in ('B', 'Q'):

        print("YES", file=output_stream)

        return

    if southwest_bishop and southwest_bishop[1] in ('B', 'Q'):

        print("YES", file=output_stream)

        return

    if northwest_bishop and northwest_bishop[1] in ('B', 'Q'):

        print("YES", file=output_stream)

        return

    if southeast_bishop and southeast_bishop[1] in ('B', 'Q'):

        print("YES", file=output_stream)

        return

    # If none

    print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
4 2
R 3 3
B 1 5
""",
            "output": \
"""\
NO
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

Sample 2:

Input:

2

4 2

R 3 3

B 1 5

First piece: R at (3,3).

yi=3 !=2.

xi=3 !=4.

delta_x=3-4 =-1, delta_y=3-2=1. delta_x != delta_y.

Check diagonal2: delta_x =-1, delta_y=1 → delta_x =-delta_y → yes.

delta_x=-1 <0. So southeast direction.

current southeast_bishop is None. So set to (-1, 'R').

Second piece: B at (1,5). delta_x=1-4=-3, delta_y=5-2=3. delta_x =-3 = -3 → yes.

delta_x=-3 <0. So southeast direction.

Compare delta_x=-3 with current southeast_bishop's delta_x=-1.

We want the maximum delta_x (since southeast direction tracks maximum delta_x). So current delta_x is -3, which is less than -1. So the current best remains at -1.

After processing:

southeast_bishop is (-1, 'R'). Type is R, which is not B or Q. So no.

Other directions are None.

Thus, code outputs NO.

So the code works for the samples.

Now, edge cases.

Edge case 1: A queen is in the same row, left direction, and is the closest.

Queen's type is Q, which can act as rook. So code should return YES.

Another edge case: A bishop and a queen are in the same diagonal direction, but the bishop is closer than the queen. So bishop's type is B, which can attack. So code returns YES.

Another case: A piece is in the same diagonal but blocked by another piece in the same line. For example, bishop at (x0+2, y0+2), and another piece (any type) at (x0+1, y0+1). Then, the bishop's delta_x is 2. The other piece's delta_x is 1. So the closest is the other piece. If that other piece is a rook, then bishop's attack is blocked. If the other piece is a bishop or queen, then it can attack.

So code will track the closest piece (delta_x=1) in northeast direction. If that piece is a bishop or queen, then check.

Thus, code correctly handles blocking.

Thus, the code should work.
</think>

```python
import sys

def main():
    n = int(sys.stdin.readline())
    x0, y0 = map(int, sys.stdin.readline().split())

    left_rook = None  # (xi, type)
    right_rook = None
    below_rook = None
    above_rook = None
    northeast_bishop = None  # (delta_x, type)
    southwest_bishop = None
    northwest_bishop = None
    southeast_bishop = None

    for _ in range(n):
        parts = sys.stdin.readline().split()
        typ = parts[0]
        xi = int(parts[1])
        yi = int(parts[2])

        # Check same row
        if yi == y0:
            if xi < x0:
                if left_rook is None or xi > left_rook[0]:
                    left_rook = (xi, typ)
            elif xi > x0:
                if right_rook is None or xi < right_rook[0]:
                    right_rook = (xi, typ)
        # Check same column
        elif xi == x0:
            if yi < y0:
                if below_rook is None or yi > below_rook[0]:
                    below_rook = (yi, typ)
            elif yi > y0:
                if above_rook is None or yi < above_rook[0]:
                    above_rook = (yi, typ)
        else:
            delta_x = xi - x0
            delta_y = yi - y0
            # Check diagonal1 (delta_x == delta_y)
            if delta_x == delta_y:
                if delta_x > 0:
                    if northeast_bishop is None or delta_x < northeast_bishop[0]:
                        northeast_bishop = (delta_x, typ)
                elif delta_x < 0:
                    if southwest_bishop is None or delta_x > southwest_bishop[0]:
                        southwest_bishop = (delta_x, typ)
            # Check diagonal2 (delta_x == -delta_y)
            elif delta_x == -delta_y:
                if delta_x > 0:
                    if northwest_bishop is None or delta_x < northwest_bishop[0]:
                        northwest_bishop = (delta_x, typ)
                elif delta_x < 0:
                    if southeast_bishop is None or delta_x > southeast_bishop[0]:
                        southeast_bishop = (delta_x, typ)

    # Check all directions
    if left_rook and left_rook[1] in ('R', 'Q'):
        print("YES")
        return
    if right_rook and right_rook[1] in ('R', 'Q'):
        print("YES")
        return
    if below_rook and below_rook[1] in ('R', 'Q'):
        print("YES")
        return
    if above_rook and above_rook[1] in ('R', 'Q'):
        print("YES")
        return
    if northeast_bishop and northeast_bishop[1] in ('B', 'Q'):
        print("YES")
        return
    if southwest_bishop and southwest_bishop[1] in ('B', 'Q'):
        print("YES")
        return
    if northwest_bishop and northwest_bishop[1] in ('B', 'Q'):
        print("YES")
        return
    if southeast_bishop and southeast_bishop[1] in ('B', 'Q'):
        print("YES")
        return

    print("NO")

if __name__ == "__main__":
    main()
```
