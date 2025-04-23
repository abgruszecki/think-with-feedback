<think>
Okay, let's see. The problem is to find the minimal path length for the quadcopter to make a closed loop that starts and ends at (x1, y1) and encircles the flag at (x2, y2) such that the flag is strictly inside the loop. The quadcopter moves in a grid, changing one coordinate by 1 each step. So each move is either horizontal or vertical.

Hmm. So the key is to find the smallest possible perimeter of a rectangle (or some loop) that surrounds the flag, with the starting point on the perimeter. Wait, maybe not a rectangle. But since movement is along grid lines, maybe the minimal loop is a rectangle. Because any other shape might have a longer perimeter.

Wait, but the problem says that the path is a closed cycle. So the path must form a loop. To enclose the flag strictly inside, the loop must form a polygon that contains the flag in its interior. Since movement is on grid lines, perhaps the minimal loop is the smallest possible rectangle that surrounds the flag, such that the starting point is on the perimeter of that rectangle.

Wait, but the starting point has to be part of the loop. So perhaps the minimal path is determined by finding a rectangle that contains the flag inside, and the starting point is on the perimeter of the rectangle. Then the perimeter of the rectangle would be the path length. But how?

Alternatively, maybe the minimal path is determined by creating a rectangle that is just large enough to contain the flag in its interior, and then adjusting it to include the starting point as a perimeter point.

Wait, but maybe the starting point is already part of such a rectangle. For example, in the second sample input:

Sample Input 2:
0 1
0 0

Output is 8. The loop is a rectangle that must enclose (0,0) inside and start and end at (0,1). So perhaps the minimal rectangle is one that surrounds (0,0). The flag is at (0,0), so the rectangle must be such that (0,0) is inside. The minimal rectangle would be one that has the flag inside. For example, a rectangle from (-1, -1) to (1, 1) would enclose (0,0). But the starting point (0,1) is on the edge of that rectangle, right? The perimeter of that rectangle is (width*2 + height*2). Wait, but the width here is 2 (from -1 to 1 is 2 units), height is 2. So perimeter is (2+2)*2 = 8. Which matches the sample output. So in that case, the minimal path is the perimeter of the smallest possible rectangle that contains the flag, and the starting point is on the perimeter of that rectangle.

So the approach might be: find the minimal rectangle that contains the flag (x2, y2) in its interior, and then check if the starting point (x1, y1) lies on the perimeter of that rectangle. Then the perimeter length would be 2*(width + height) + 2? Wait, no. Wait, the perimeter of a rectangle is 2*(width + height). But in the sample input 2, the rectangle's width and height would be 2 units each. 2*(2 + 2) = 8, which matches.

So the minimal path length would be the perimeter of the minimal rectangle that encloses the flag, but adjusted such that the starting point is on the perimeter. Wait, but how do we adjust the rectangle to include the starting point?

Alternatively, perhaps the minimal path is determined by the following steps:

1. The rectangle must enclose the flag (x2, y2) in its interior. So the rectangle must be such that x2 is strictly between the left and right boundaries, and y2 is strictly between the bottom and top boundaries.

2. The starting point (x1, y1) must lie on the perimeter of this rectangle.

3. The perimeter of such a rectangle is 2*(width + height), and we need to find the minimal possible perimeter.

So the problem reduces to finding the smallest possible perimeter of such a rectangle that meets these two conditions.

So how do we model this?

First, the minimal possible rectangle that encloses the flag. For a rectangle to enclose (x2, y2) strictly inside, the rectangle's left (L) must be less than x2, right (R) greater than x2. Similarly, bottom (B) less than y2, top (T) greater than y2.

But the starting point must lie on the perimeter of this rectangle. So (x1, y1) must be on one of the four edges of the rectangle. For example:

Either x1 is L or R, and y1 is between B and T (inclusive), or y1 is B or T, and x1 is between L and R (inclusive).

So the problem is to find L, R, B, T such that:

- L < x2 < R

- B < y2 < T

And (x1, y1) is on the perimeter of the rectangle.

Then, the perimeter is 2*( (R-L) + (T-B) ), and we need to minimize this perimeter.

So how can we compute this?

The minimal perimeter would be achieved when the rectangle is as small as possible, but still includes the flag inside and has the starting point on the perimeter.

So for each possible rectangle that encloses the flag and includes the starting point on its perimeter, compute the perimeter and choose the minimal.

But how to generate all possible such rectangles efficiently?

Alternatively, since the starting point is fixed, perhaps we can find the minimal possible rectangle that must be constructed such that the starting point is on the perimeter, and the flag is inside.

Let me think: the starting point (x1, y1) must be on the perimeter. So the rectangle must have either x1 as L or R, or y1 as B or T.

But the flag must be inside the rectangle, so the rectangle must be such that:

If the starting point is on the left edge (x1 = L), then R must be > x2. And the left edge is x1, so L = x1. Then, since x2 must be > L and < R, then R must be at least x2 + 1. Wait, no. Because if L = x1 and R must be > x2, then x2 must be between L and R. So L < x2 < R.

But L is x1. So x1 < x2 < R. Or wait, maybe the starting point is on the right edge. For example, if x1 is R, then x2 must be < R and > L. So the rectangle's left boundary L must be < x2, and R must be > x2. But if the starting point is on the right edge, then R = x1. Then x2 must be < R (since R is x1), but x2 must also be > L. So L must be < x2 < R. But R is x1, so x2 must be less than x1, and L must be less than x2. Similarly for other edges.

So perhaps the minimal perimeter can be found by considering four possible cases where the starting point is on one of the four edges of the rectangle, and then compute the minimal possible perimeter in each case, then take the minimum among all four.

So let's model each case:

Case 1: starting point is on the left edge (x1 = L). So L = x1. Then R must be > x2. Also, the rectangle must enclose the flag, so B < y2 < T. Also, the starting point's y1 must be between B and T (inclusive), because it's on the left edge.

Wait, no. Because the starting point is on the left edge (x1 = L), and the left edge runs from (L, B) to (L, T). So the starting point (x1, y1) must be between B and T in y-coordinate. So y1 >= B and y1 <= T.

But B and T must satisfy B < y2 < T.

So for case 1:

L = x1

R must be > x2 (since x2 is inside the rectangle)

B must be < y2 and <= y1 <= T (since the starting point is on the left edge, which runs from B to T in y-coordinate)

But to minimize the perimeter, what's the minimal R, B, T?

For R, since R must be > x2. The minimal R is x2 + 1 if x2 >= L (since L = x1, but x1 and x2 can be in any order). Wait, but in case x1 is the left edge, x2 could be to the left of x1. But in that case, x2 < L (since L is x1), which would violate the condition that L < x2 < R. So for case 1 to be possible, x2 must be between L and R. But L is x1, so x2 must be greater than x1. Otherwise, if x2 < x1 (so L = x1 > x2), then R would have to be > x2, but L (x1) is already greater than x2. Then x2 would be < L, so it's to the left of the rectangle. But the rectangle must enclose x2 inside, so that's impossible. Therefore, case 1 is only possible if x2 > x1.

Wait, no. Wait, in case 1, the rectangle's left edge is x1. Then, for x2 to be inside the rectangle, x2 must be between L and R. So L < x2 < R.

But L is x1, so x2 must be greater than x1. Otherwise, this case is impossible.

So if x2 is less than x1, then case 1 is impossible, and we can skip it.

So for case 1, when x2 > x1, then R can be x2 + 1 (the minimal possible R to have x2 < R). But wait, R can be any value greater than x2. So to minimize the perimeter, R should be as small as possible, which is x2 + 1. But also, the right edge must be such that the starting point is on the left edge. But R is the right edge, so that's fixed once x2 is considered.

Wait, perhaps I need to think differently.

In case 1: the rectangle's left edge is x1. Then, for x2 to be inside the rectangle, the right edge R must be > x2. So R is at least x2 + 1 (since it's integer coordinates). Similarly, for the vertical edges, the B and T must be such that B < y2 < T.

Also, since the starting point is on the left edge (x1, y1), its y-coordinate must be between B and T (inclusive). So B <= y1 <= T.

But B must be < y2 and T must be > y2. So B can be as high as y2 - 1, but since B must be <= y1, that's only possible if y1 >= B. But B needs to be as large as possible to minimize T - B. Similarly for T.

Wait, perhaps the minimal vertical size is determined by the distance from y2 to the starting point's y1. Let me see.

The vertical dimensions of the rectangle (T - B) must be at least (y2 - B) and (T - y2). So B must be <= y2 - 1, and T >= y2 + 1. Wait no: since B < y2 < T. So B can be anything less than y2, T anything greater than y2. But also, the starting point's y1 must be between B and T (inclusive) because it's on the left edge.

So for B and T to minimize T - B, given that B < y2 < T and B <= y1 <= T.

So the minimal possible vertical size is max(y2 - B_min, T_max - y2) but perhaps it's easier to think of B and T such that B <= y1 <= T and B < y2 < T.

Wait, to minimize (T - B), we need B to be as large as possible and T as small as possible, but still satisfying B < y2 < T and B <= y1 <= T.

So B can be at maximum (y2 - 1) if y1 >= (y2 - 1). But if y1 is less than (y2 - 1), then B can't be larger than y1. Because B <= y1.

Similarly, T can be at minimum (y2 + 1) if y1 <= (y2 + 1). But if y1 is larger than (y2 + 1), then T must be at least y1.

So perhaps the minimal vertical dimension (T - B) is:

If y1 is within [B, T], then:

The minimal T - B would be max(y2 - B, T - y2). Wait, perhaps this is getting complicated.

Alternatively, B must be <= min(y1, y2 - 1). Because B has to be less than y2, and also <= y1.

Wait, let's think of B as the maximum possible value that is <= y1 and < y2. Similarly, T is the minimum possible value that is >= y1 and > y2.

Wait, for example:

If y1 is above y2:

Suppose y1 is 5, y2 is 3. Then B can be up to 2 (since B < 3), but B must be <= 5. So B can be up to 2. Then T must be >3. Also, T must be >=5 (since y1 is 5, which must be <= T). So T can be 5 (but then T must be >3, which is true). So B is 2, T is5. Then T-B=3.

But y2 is 3. So B=2 (which is <3), T=5 (>3). Then (T - B) is 3.

But is there a way to have B higher? Let's say y1=4, y2=3. Then B can be up to 2, but if B is 2, then T can be 4 (since T >=4 and >3). So T-B=2. Then T - B is 2. That's better.

So the minimal vertical dimension is (T - B) where B is the largest possible value less than y2 and <= y1, and T is the smallest possible value larger than y2 and >= y1.

So:

B = min(y2 - 1, y1) --> but wait, if y1 is less than y2 - 1, then B can be y1. But since B must be < y2, then B can be up to min(y1, y2 -1) only if y1 <= y2 -1. Otherwise, if y1 is >= y2, then B can be up to y2-1.

Wait, perhaps this can be written as B = min(y1, y2 -1) if y1 < y2.

Wait, maybe not. Let's take examples.

Example 1: y1=5, y2=3.

We need B <3 and <=5. So B can be at maximum 2. So B is 2.

T must be >=5 and >3. So T is5.

So (T - B) =3.

Example 2: y1=4, y2=3.

B can be up to 2 (since 2 <3), but y1 is4. So B can be up to 2. Then T must be >=4. So T is4. Then (4-2)=2.

But y2 is3. So T (4) is larger than 3. So that's valid.

But what if y1 is 3?

If y1 is3, y2 is3: but in the problem statement, the starting point and flag are different. So that's impossible.

Wait, but in the input, the flag and starting point are different, so y2 can't be the same as y1 when x2 is same as x1. But in other cases, maybe.

So for the case where y1 is 2, y2 is3. Then B can be up to 2 (since 2 <3). T must be >=2 and >3. So T must be at least4. So T=4. B=2. (4-2)=2.

So vertical dimension is 2.

Hmm. So the minimal vertical dimension is (max_T - min_B) where:

B is the maximum possible less than y2 and <= y1.

T is the minimum possible greater than y2 and >= y1.

So:

B = min(y1, y2-1) if y1 < y2. Wait, no. Let's see.

If y1 is <= y2-1, then B can be y1. Because y1 is <= y2-1 (so y1 < y2) and B <= y1.

But if y1 is >= y2, then B can be at most y2-1. Because B < y2.

Similarly, T is the maximum between (y2 +1) and y1. Because T must be >= y1 (since T is the top edge, and the starting point's y is on the edge, which is between B and T). Wait, no. If the starting point is on the left edge, then its y can be between B and T. So T must be >= y1. Because the starting point is (x1, y1) on the edge. So T has to be >= y1 and B <= y1.

Wait, for case 1: the starting point is on the left edge. So y1 must be between B and T, inclusive. So B <= y1 <= T. But the rectangle must have B < y2 < T.

So for the vertical edges, we need to choose B and T such that:

B < y2 < T

B <= y1 <= T

To minimize T - B, we need to maximize B and minimize T, but under those constraints.

So, B can be as large as possible, but it must be <= min(y1, y2 - 1). Because:

B <= y1 (from B <= y1 <= T)

B < y2 → B <= y2 -1

So B's maximum possible value is the minimum of y1 and y2 - 1.

Similarly, T can be as small as possible, but must be >= max(y1, y2 + 1). Because:

T >= y1 (since T >= y1)

T > y2 → T >= y2 + 1

So T's minimum possible value is the maximum of y1 and y2 +1.

Thus, the vertical dimension (T - B) is [max(y1, y2 + 1) - min(y1, y2 -1)].

Wait, but let's compute B and T as:

B = min(y1, y2-1)

T = max(y1, y2+1)

Then the vertical dimension is T - B.

Yes. Because:

For example, in case y1 is less than y2 -1:

Example: y1=1, y2=5. Then B = min(1, 5-1)=1. T = max(1, 5+1)=6. So vertical is 6-1=5.

Which is correct, since the rectangle's B is1 (<=y1=1), T=6 (>y2=5). And the starting point's y1=1 is between B and T.

Another example: y1=4, y2=3. Then B = min(4, 2) =2. T = max(4, 4) =4. So vertical dimension is 4-2=2. Which is correct as above.

So, the vertical dimension in case 1 is (max(y1, y2+1) - min(y1, y2-1)).

Similarly for horizontal dimension in case 1, the horizontal dimension is R - L, where L =x1, R is the minimum possible to satisfy R > x2. So R must be x2 +1 if x2 >x1. Wait, no. Because R can be any value greater than x2, but to minimize the horizontal dimension (R - L), R is x2 +1. So horizontal dimension is (x2 +1 - x1).

But wait, in case 1, x1 is L. So the horizontal dimension is R -x1, and R must be >x2.

So R can be x2 +1. Because then R - L = x2 +1 -x1.

So the horizontal dimension is (x2 +1 -x1).

So for case 1 (starting point on left edge), the perimeter is 2*( (x2 +1 -x1) + (max(y1, y2+1) - min(y1, y2-1)) ) ), but only if x1 <x2. Because otherwise, x2 can't be inside the rectangle. So if x1 >=x2, case 1 is not possible.

So case 1 is possible only if x1 <x2.

So, to compute the possible perimeter for case 1, check if x1 <x2.

If yes, then compute the perimeter as 2*( (x2 -x1 +1) + (max(y1, y2+1) - min(y1, y2-1)) ) )

Wait, wait. Let's recalculate:

horizontal dimension is R - L. L is x1. R is x2 +1 (since R must be >x2). So R - L = x2 +1 -x1.

Vertical dimension is T - B, which is max(y1, y2 +1) - min(y1, y2 -1).

So perimeter is 2*( (x2 +1 -x1) + (T - B) ) ).

But we need to check if the starting point's y1 is between B and T. Because B is min(y1, y2-1) and T is max(y1, y2+1). So B will be <= y1, and T >= y1. So yes, y1 is between B and T.

So for case 1, perimeter is 2 * ( (x2 +1 - x1) + (max(y1, y2 +1) - min(y1, y2 -1)) ) ) if x1 <x2.

If x1 >=x2, case 1 is impossible.

We need to repeat this for all four cases: starting point is on left, right, bottom, or top edge.

So let's model all four cases:

Case 1: starting point is on left edge (x1 = L). Conditions: x1 <x2. Then R = x2 +1. B and T computed as per vertical dimension.

Case 2: starting point is on right edge (x1 = R). Conditions: x1 >x2. Then L =x2 -1. R =x1. So horizontal dimension is x1 - (x2 -1) =x1 -x2 +1. Then B and T as before.

Case 3: starting point is on bottom edge (y1 = B). Conditions: y1 <y2. Then T =y2 +1. B =y1. Vertical dimension is T - B = y2 +1 - y1. Horizontal dimension is (max(x1, x2 +1) - min(x1, x2 -1)). Wait, similar to case 1 but for horizontal direction.

Wait, no. Let's think again.

Case 3: starting point is on bottom edge (B = y1). Then the rectangle must have B = y1. To enclose y2 inside, we need T > y2. Also, the starting point's x1 must be between L and R (since it's on the bottom edge). So L <=x1 <= R.

So in this case:

B = y1

T must be > y2. So T = y2 +1 (minimal possible).

But for B to be the bottom edge and the starting point on it, y1 must be B. So B is y1. And T is y2 +1.

But wait, if y1 is the bottom edge, then T must be >y2, but y1 can be <= y2 or not.

Wait, no. For the rectangle to enclose the flag (x2, y2) inside, B must be <y2 <T. Since B is y1 (the starting point's y), we must have y1 <y2. Otherwise, if y1 >=y2, then B =y1 >=y2, which violates B <y2.

So case 3 is possible only if y1 <y2.

So when y1 <y2:

B =y1

T =y2 +1.

Then the vertical dimension is T - B = y2 +1 -y1.

The horizontal dimension is R - L, where L and R must satisfy L <x2 <R. Also, x1 must be between L and R (inclusive) because the starting point is on the bottom edge (so x1 must be between L and R).

So L can be as large as possible, which is x2 -1 (since L <x2). But x1 must be >=L and <=R. And R must be >x2.

So R can be x2 +1 (minimal possible to satisfy R> x2). Then L can be as large as possible, but <=x2-1 and <=x1.

Wait, perhaps the minimal horizontal dimension is achieved by choosing L and R such that x1 is between them, and x2 is inside.

So for case 3:

L must be <=x1 <= R.

But the rectangle must have L <x2 <R.

So how to choose L and R to minimize (R - L).

The minimal possible R-L is (x2 +1) - (x2 -1) ) =2, but only if x1 is between x2-1 and x2+1.

But x1 can be any value. So, to minimize R-L, we need L as large as possible and R as small as possible.

So:

L is the maximum between (x2-1) and (x1's constraints). Wait, perhaps:

L can be up to min(x2-1, x1), since L must be <=x1 (since x1 is between L and R).

Similarly, R can be up to max(x2+1, x1), since R must be >=x1.

So:

L = min(x2 -1, x1) → no, because x2-1 must be >= L, but L must be <=x1.

Wait, perhaps to satisfy L <x2 < R and x1 is between L and R, the minimal R-L is:

If x1 is <=x2 -1: then L can be x1, R can be x2 +1. So R-L = (x2 +1) -x1.

But x1 could be less than x2-1. Then x2-1 is greater than x1, so L can be x2-1 (since L must be <=x1). No, that's not possible. So in that case, L must be <=x1. For example, x1 is 0, x2 is 5. Then L must be <=0. But to have L <5, so L can be 0 (x1=0), R=6. Then R-L=6.

Alternatively, if x1 is between L and R, and L <x2 < R, then the minimal possible R-L is (x2 +1) - (x2 -1) ) =2, but that's possible only if x1 is in [x2-1, x2+1].

So, for case 3:

If x1 is in [x2-1, x2+1], then L can be x2-1, R=x2+1. Then R-L=2. So horizontal dimension is 2.

But x1 must be >=L (x2-1) and <= R (x2+1). So for example, x1 =x2: then x1 is between x2-1 and x2+1.

So in that case, L=x2-1, R=x2+1. So horizontal dimension is 2.

But if x1 is outside of that interval, then the horizontal dimension will be larger.

For example, x1 is x2+2. Then, to have x1 in [L, R], R must be at least x1. So R is x2+2, L is x2-1. So R-L = (x2+2) - (x2-1) )=3. So horizontal dimension is 3.

So to minimize the horizontal dimension in case 3, we need to choose L and R such that:

L is as large as possible (to minimize R-L) but <=x1 and <=x2-1.

R is as small as possible but >=x1 and >=x2+1.

So:

L = min(x2-1, x1)

R = max(x2+1, x1)

Then R - L = max(x2+1, x1) - min(x2-1, x1)

Yes.

For example:

If x1 <=x2-1:

L =x1

R =x2+1 (since x2+1 is larger than x1)

So R - L =x2 +1 -x1.

If x1 is between x2-1 and x2+1:

L =x2-1

R =x2+1

So R-L=2.

If x1 >=x2+1:

R =x1

L =x2-1 (since x2-1 is <=x1?)

Wait, x1 >=x2+1. So x2-1 could be less than x1.

So L = min(x2-1, x1) → x2-1 (since x2-1 <=x1).

R =max(x2+1, x1) →x1.

So R-L =x1 - (x2-1) =x1 -x2 +1.

So in case 3, the horizontal dimension is:

max(x2+1, x1) - min(x2-1, x1)

So the perimeter for case 3 is 2*( (max(x2+1, x1) - min(x2-1, x1)) ) + (y2 +1 - y1) )

But only if y1 <y2.

Similarly, case 4: starting point is on top edge (y1 = T).

Conditions: y1 >y2. Then B =y2-1. T=y1. Vertical dimension is y1 - (y2-1) = y1 -y2 +1.

The horizontal dimension is similar to case 3. L and R must satisfy L <x2 <R, and x1 is between L and R.

So horizontal dimension is max(x2+1, x1) - min(x2-1, x1).

So case 4 is possible only if y1 >y2.

So the perimeter for case 4 is 2*( (max(x2+1, x1) - min(x2-1, x1)) ) + (y1 - (y2-1)) )

But only when y1 >y2.

So now, for all four cases, we can compute the possible perimeters, but only if the case is possible (based on the conditions on x1 vs x2 or y1 vs y2).

Then, among all possible cases, we select the minimal perimeter.

So the algorithm steps are:

1. For each of the four cases (left, right, bottom, top edge), compute the perimeter if the case is possible.

2. The minimal perimeter among all possible cases is the answer.

But how to compute all four cases?

Let's outline each case:

Case 1: Left edge.

Possible if x1 <x2.

Perimeter = 2*( (x2 +1 -x1) + (max(y1, y2+1) - min(y1, y2-1)) )

Case 2: Right edge.

Possible if x1 >x2.

Perimeter = 2*( (x1 - (x2 -1)) + (max(y1, y2+1) - min(y1, y2-1)) )

Case 3: Bottom edge.

Possible if y1 <y2.

Perimeter = 2*( (max(x2+1, x1) - min(x2-1, x1)) + (y2+1 -y1) )

Case4: Top edge.

Possible if y1> y2.

Perimeter = 2*( (max(x2+1, x1) - min(x2-1, x1)) + (y1 - (y2 -1)) )

So for each case, compute the perimeter if the condition is met. Then take the minimum of all computed perimeters.

Now, what about cases where the starting point is on a corner (like left and bottom edge)? For example, if the starting point is on both left and bottom edges of the rectangle. Then the minimal perimeter would be considered in both case 1 and case3. But the minimal perimeter would be the minimum between the two.

But according to the algorithm, all four cases are considered, and the minimal is chosen.

Now, let's test the sample inputs.

Sample Input 1:

1 5

5 2

So x1=1, y1=5; x2=5, y2=2.

Let's compute all possible cases.

Case1: x1 <x2 (1<5) → possible.

Perimeter for case1:

horizontal dimension: 5+1 -1=5.

vertical dimension: max(5, 2+1) - min(5, 2-1) → max(5,3)=5, min(5,1)=1 →5-1=4.

Perimeter=2*(5+4) = 18. Which matches the sample output.

Case2: x1> x2? 1>5 → no.

Case3: y1 <y2? 5 <2 → no.

Case4: y1> y2 →5>2 → yes.

Compute perimeter for case4:

horizontal dimension: max(5+1,1) - min(5-1,1) → max(6,1)=6, min(4,1)=1 →6-1=5.

vertical dimension:5 - (2-1) =4.

Perimeter=2*(5+4) =18.

So in this case, both case1 and case4 give 18. So the minimal is 18.

Sample Input 2:

0 1

0 0

x1=0, y1=1; x2=0, y2=0.

Case1: x1 <x2? 0 <0 →no.

Case2: x1> x2? 0>0→no.

Case3: y1 <y2? 1 <0 → no.

Case4: y1> y2 →1>0 →yes.

Compute case4:

horizontal dimension: max(0+1, 0) - min(0-1, 0) → max(1,0)=1; min(-1,0)=-1. 1 - (-1) =2.

vertical dimension:1 - (0-1)=1+1=2.

Perimeter=2*(2 +2 )=8 → which matches sample.

Another example where the starting point is on a corner.

Example where starting point is (3,3), flag is (4,4).

Case1: x1=3 <4. So possible.

horizontal:4+1 -3=2.

vertical: max(3,4+1)=5; min(3,4-1=3). 5-3=2.

perimeter=2*(2+2)=8.

Case4: y1=3 <4 → no. But case3: y1=3 <4 → yes.

So case3:

y1 <y2 →3<4 → yes.

horizontal dimension: max(4+1,3) →5; min(4-1=3,3) →3. 5-3=2.

vertical dimension:4+1 -3=2.

perimeter=2*(2+2)=8.

So same as case1.

So the minimal is 8.

So the approach seems to handle all cases.

Now, in code:

We need to compute all four cases' perimeters if applicable, then choose the minimal one.

So code steps:

Read x1, y1.

Read x2, y2.

Compute perimeters for each case if possible.

Collect all possible perimeters, then output the minimum.

Let's code this.

First, case1:

if x1 <x2:

   h = x2 +1 - x1

   B = min(y1, y2 -1)

   T = max(y1, y2 +1)

   v = T - B

   perimeter1 = 2 * (h + v)

else:

   perimeter1 = infinity (or not considered)

Similarly for other cases.

But how to code this in Python?

Implement each case as a possible candidate, compute if possible, then take the minimal.

Initialize min_perimeter as a very large number.

Then for each case, if the condition is met, compute the perimeter, and update min_perimeter if it's smaller.

So code:

x1, y1 = map(int, input().split())

x2, y2 = map(int, input().split())

min_perim = float('inf')

# Case 1: starting on left edge (x1 is L)

if x1 < x2:

    h = (x2 +1) - x1

    B = min(y1, y2 -1)

    T = max(y1, y2 +1)

    v = T - B

    perim = 2 * (h + v)

    if perim < min_perim:

        min_perim = perim

# Case 2: starting on right edge (x1 is R)

if x1 > x2:

    h = x1 - (x2 -1)

    B = min(y1, y2 -1)

    T = max(y1, y2 +1)

    v = T - B

    perim = 2 * (h + v)

    if perim < min_perim:

        min_perim = perim

# Case 3: starting on bottom edge (y1 is B)

if y1 < y2:

    # compute horizontal dimension

    L = min(x2 -1, x1)

    R = max(x2 +1, x1)

    h = R - L

    v = (y2 +1) - y1

    perim = 2 * (h + v)

    if perim < min_perim:

        min_perim = perim

# Case4: starting on top edge (y1 is T)

if y1 > y2:

    L = min(x2 -1, x1)

    R = max(x2 +1, x1)

    h = R - L

    v = y1 - (y2 -1)

    perim = 2 * (h + v)

    if perim < min_perim:

        min_perim = perim

print(min_perim)

Testing sample input 1:

Case1 is possible. h=5+1-1=5. B= min(5,2-1=1) →1. T= max(5,2+1=3) →5. v=5-1=4. perim=2*(5+4)=18.

Case4 is possible. y1=5>2. L = min(5-1=4,1) →1? Wait, x2 is5 in sample1. So x2-1=4. x1 is1. So L = min(4,1) →1. R= max(5+1=6,1) →6. h=6-1=5. v=5 - (2-1)=4. perim=2*(5+4)=18.

So min_perim is 18.

Sample2: case4.

y1=1>0. So L= min(0-1= -1, 0) →-1. R= max(0+1=1,0) →1. h=1 - (-1) =2. v=1 - (0-1)=2. perim=2*(2+2)=8.

So code works.

Another test case where starting point is on multiple edges.

For example, x1= x2, y1> y2.

Let's say x1=3, y1=5. x2=3, y2=4.

Case4: y1> y2. So compute L=3-1=2, x1=3. So min(x2-1, x1) is min(2,3) →2. R= max(3+1=4,3)=4. h=4-2=2. v=5 - (4-1)=5-3=2. perimeter=2*(2+2)=8.

But the minimal path would be a rectangle from (2,3) to (4,5), which has perimeter 8.

Which is correct.

So the code should handle all cases correctly.

Thus, the code should work.
</think>

```python
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

min_perim = float('inf')

# Case 1: left edge
if x1 < x2:
    h = (x2 + 1) - x1
    B = min(y1, y2 - 1)
    T = max(y1, y2 + 1)
    v = T - B
    min_perim = min(min_perim, 2 * (h + v))

# Case 2: right edge
if x1 > x2:
    h = x1 - (x2 - 1)
    B = min(y1, y2 - 1)
    T = max(y1, y2 + 1)
    v = T - B
    min_perim = min(min_perim, 2 * (h + v))

# Case 3: bottom edge
if y1 < y2:
    L = min(x2 - 1, x1)
    R = max(x2 + 1, x1)
    h = R - L
    v = (y2 + 1) - y1
    min_perim = min(min_perim, 2 * (h + v))

# Case 4: top edge
if y1 > y2:
    L = min(x2 - 1, x1)
    R = max(x2 + 1, x1)
    h = R - L
    v = y1 - (y2 - 1)
    min_perim = min(min_perim, 2 * (h + v))

print(min_perim)
```