<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

So, the problem is about Sofia drawing n squares. Each square is made of four segments, each of length 1, forming a square of side 1. The segments are either horizontal or vertical. The key point is that when she draws a segment, she can use existing segments as a guide to avoid using the ruler. The segments that require the ruler are those for which there's no existing segment in the same row (for vertical) or column (for horizontal) at the same y-coordinate (for vertical) or x-coordinate (for horizontal).

The goal is to find the minimum number of ruler-drawn segments needed to create all the squares.

Hmm. Let's think about the examples.

For n=1: she has to draw 2 segments with the ruler. Then the other two can be done quickly. So output is 2.

For n=2: the sample output is 3. So how does that happen? Maybe when the two squares are adjacent. Let's say she draws a vertical segment first, then uses it for the next. But perhaps the arrangement here is such that the two squares form a 1x2 rectangle, leading to 3 ruler segments.

Wait, maybe the optimal arrangement is to arrange the squares in a way that maximizes the reuse of existing guides. So the problem reduces to arranging the squares into a grid-like structure where each new square adds as few new ruler segments as possible.

So the problem is similar to forming a grid of connected squares, which forms a rectangle. The number of ruler segments required would then be related to the perimeter of the rectangle, but not exactly. Let's think about how the ruler segments are counted.

For vertical segments: each vertical segment at (x, y) to (x, y+1) requires a ruler if there's no other vertical segment in the same row (same y, any x). Wait, no. The problem says that when drawing a vertical segment (x,y) to (x,y+1), Sofia checks if there's any existing vertical segment with the same y (so same row, perhaps). Because if there's any such segment (like in the same row but different x), then she can use it as a guide, so she doesn't need the ruler. So the vertical segments in the same row (same y) can share the guide. So, the first vertical segment in a particular row requires the ruler. All subsequent vertical segments in that same row (same y) can be done without the ruler.

Similarly, horizontal segments: when she draws a horizontal segment from (x, y) to (x+1, y), she checks if there's any existing horizontal segment in the same column (same x, any y). If yes, no ruler needed. So the first horizontal segment in a column requires the ruler, others in the same column don't.

Therefore, the problem reduces to counting the number of rows and columns used in the arrangement of squares, and then the total ruler segments are (number of rows) + (number of columns). Because:

- For each row (y), the first vertical segment requires a ruler. All others in that row don't. So the number of vertical ruler segments is equal to the number of distinct rows (y) where vertical segments are placed.

Wait, not exactly. Because each vertical segment in a row could be part of multiple squares. For example, in a row, multiple vertical segments can be adjacent. But each vertical segment is part of a square's left or right edge. Hmm, maybe this is getting complicated.

Alternatively, think of the entire grid. Each vertical segment is part of a column x and row y (since it's between (x, y) and (x, y+1)). So for vertical segments, the number of ruler segments needed is equal to the number of unique rows (y) where there's at least one vertical segment. Because for each row y, the first vertical segment in that row requires a ruler. All others in the same row don't. So the vertical ruler count is the number of rows with at least one vertical segment.

Similarly, horizontal ruler segments are the number of columns with at least one horizontal segment. Because for each column x, the first horizontal segment in that column requires a ruler. So the horizontal ruler count is the number of columns with at least one horizontal segment.

But how do the squares' arrangement affect these counts?

Each square contributes four edges: two vertical and two horizontal. But edges are shared between adjacent squares. So, when squares are arranged in a grid (like a rectangle), the edges between adjacent squares are shared, thus minimizing the number of ruler segments.

So to model this, the problem is to arrange n squares into a grid of rows and columns such that the sum of the number of rows and columns (for vertical and horizontal ruler segments) is minimized.

Wait, no. Let's see:

Suppose the squares form a grid of h rows and w columns, but each square is 1x1. So the total number of squares would be h * w. Then, for vertical segments: the vertical edges are along the left and right of each square. But in a grid of w columns (each square in a row has columns from x to x+1), the number of vertical edges per row is (w+1). But each vertical edge in a row y is part of a vertical segment (x, y) to (x, y+1). Wait, no. For a grid of h rows and w columns, each square is at position (x, y) (bottom-left corner). Then the vertical edges are along x and x+1 for each square in row y. So each row of squares (y) contributes (w+1) vertical edges. But each vertical edge in row y is a vertical segment. So for each vertical segment in row y, we have to check if there's any other vertical segment in the same row. But since they are all in the same row, once the first vertical segment is drawn with a ruler, all others in that row can be done without. So the vertical ruler count for the entire grid is h (number of rows in the grid), since each row (y) contributes one ruler segment for the first vertical edge in that row.

Similarly, horizontal edges: each column x contributes (h+1) horizontal edges, but the first horizontal edge in column x requires a ruler. So the horizontal ruler count is w (number of columns in the grid).

So the total ruler segments would be h + w, where h is the number of rows and w is the number of columns in the arrangement, such that h * w >= n.

But wait, the squares can be arranged in any way, not necessarily a rectangle. However, the minimal ruler count would likely be achieved when the arrangement is as close to a square as possible. Because for a given area, a square has the minimal perimeter, which is 2*(sqrt(n)) + ... but here, the sum h + w for a rectangle of area h*w would be minimized when h and w are as close as possible.

Wait, for example, arranging the squares into a rectangle of h rows and w columns, such that h * w >= n, and h + w is as small as possible. Then the minimal ruler segments would be h + w.

But the problem is that when the arrangement is a rectangle, the total squares is h * w. So for n=4, h=2, w=2, sum is 4. Which matches the third sample input. For n=4, the output is 4 (2+2). So that's correct.

Similarly, for n=2, the best arrangement is 1x2 (h=1, w=2) sum 3. Which matches the second sample.

So the problem reduces to finding h and w such that h * w >= n, and h + w is minimized. Then the answer is h + w.

Wait, but the problem allows any arrangement of squares, not necessarily a rectangle. For example, perhaps arranging the squares in a spiral or other shape could use fewer rows and columns. But perhaps the minimal sum is achieved when the arrangement is a rectangle. Because any other arrangement would require more rows and/or columns to cover the same number of squares. Let's see.

Suppose n=3. The minimal h and w would be 2x2 (area 4 >=3), sum 4. But if we arrange the squares in an L-shape, perhaps 2 rows and 2 columns, but h=2, w=2. The sum is 4. Alternatively, maybe a 3x1 arrangement (sum 4) or 1x3 (sum 4). So the minimal sum is 4. So the minimal sum is achieved when h and w are the ceiling of the square root of n. But wait, for n=3, sqrt(n) is ~1.732, so ceiling is 2. So h=2 and w=2, sum 4.

So the minimal sum is indeed h + w where h and w are the minimal possible integers such that h * w >=n and h + w is minimized.

Therefore, the problem becomes equivalent to finding two integers h and w such that h * w >=n, and h + w is as small as possible. The answer is h + w.

So the problem reduces to finding the minimal possible sum of two integers h and w (h >=1, w>=1) such that h * w >=n.

Yes, that makes sense. Because the arrangement as a rectangle of h rows and w columns will require exactly h + w ruler segments. And any other arrangement would require more, because if the arrangement is not a rectangle, then the number of rows and/or columns needed to cover all squares would be larger than h and w. For example, if the squares are arranged in a way that leaves some gaps, then the required rows and columns would be more.

Thus, the problem is to find the minimal h + w where h * w >=n and h <=w (to avoid duplicates), and h and w are as close as possible.

So how do we compute h and w for a given n?

The minimal sum occurs when h and w are as close as possible to each other. So h is the floor of sqrt(n), and w is the ceiling of sqrt(n). But sometimes, we might need to adjust if h * w is not enough.

For example, n=7. sqrt(n) is ~2.645. So h=2, w=3. 2*3=6 <7. So we need to increase w to 4 (h=2, w=4, sum 6). Or h=3, w=3, sum 6. So in that case, h=3, w=3 is better.

Wait, 3*3=9 >=7. sum 6. So that's better than 2+4=6. So the sum is same. So when n is between k^2 and k*(k+1), then the optimal is either (k, k+1) sum 2k+1, or (k+1, k+1) sum 2k+2.

Wait, for example, n=5. sqrt(5)=~2.236. So k=2. So h=2, w=3. sum 5. 2*3=6 >=5. Alternatively, h=3, w=2. same sum. Alternatively, h=3, w=3 sum 6, which is worse. So for n=5, minimal sum is 5.

So the approach is to find the minimal h + w where h * w >=n. The minimal sum is achieved when h is as close as possible to the square root of n.

So the algorithm would be:

Compute the integer h = floor(sqrt(n)), then check h and w = ceil(n/h). Or find h and w such that h is the largest integer <= sqrt(n), and w is the smallest integer >= ceil(n/h). Then compute h + w. If h * (h) >=n, then the sum is 2h. Otherwise, find the minimal sum between h and ceil(n/h), or (h+1) and (h+1), etc.

Alternatively, the minimal sum is the ceiling of 2*sqrt(n), but not exactly. Let's see.

Wait, for n=1, sqrt(1)=1, sum is 2 (1+1). Which is 2*1.

For n=2, floor(sqrt(2))=1. 1*2=2 >=2. sum 1+2=3. Which is 3.

For n=3, floor sqrt is 1. 1*3=3 sum 4. But 2*2=4 >=3 sum 4. So here, the sum is same as 2*2.

So the approach is to find h as the integer part of sqrt(n). Then check h * h. If h * h >=n, then sum is 2h. Else, check if h*(h+1) >=n. If so, sum is h + (h+1) = 2h+1. Else, h+1 and h+1, sum 2h+2.

But perhaps there's a better way. Let's see:

The minimal sum h + w where h*w >=n.

The minimal sum occurs when h and w are as close as possible. So the minimal sum is the minimal integer m such that there exists h <= m/2, w >= m/2, h + w = m, and h*w >=n.

Alternatively, the minimal m is the smallest integer where m >= ceil(2*sqrt(n)).

Wait, let's test:

n=1: 2*1=2. 2=2.

n=2: 3. 2*sqrt(2) is ~2.828, ceil is 3. So 3.

n=3: ceil(2*sqrt(3))=4. sum is 4.

n=4: 4. 2*2=4.

n=5: sum 5. 2*sqrt(5) is ~4.47, ceil 5. sum 5.

n=6: 2*3=6. sum 5. 2*3=5. 5=5.

n=7: 3+3=6. 2*sqrt(7)=~5.29, ceil 6. So sum 6.

So the formula seems to be that the minimal sum is the minimal integer m such that (ceil(m/2)) * (floor(m/2)) >=n.

But how to compute m for a given n?

Alternatively, find the minimal h where h >= ceil(sqrt(n)), and then compute w = ceil(n/h). Then sum h +w. The minimal sum over h from ceil(sqrt(n)) to ... ?

Alternatively, the minimal sum is the smallest m where m >= ceil(2*sqrt(n)), and there exists h <= m/2, w = m -h, such that h*w >=n.

But how to compute this.

Alternatively, find h as the floor of sqrt(n), then check h and h+1. Then compute the minimal sum.

So the steps could be:

1. Compute h = floor(sqrt(n)).

2. If h*h >=n, then the sum is 2h.

3. Else, check h*(h+1) >=n. If yes, sum is 2h +1.

4. Else, h+1 must be the new h. So compute h+1 + ceil(n/(h+1)).

But wait, let's test for n=7:

h = 2 (since sqrt(7) ~2.645, floor is 2).

h^2 =4 <7. So step 2 no.

Check h*(h+1) =2*3=6 <7. So step 3 no.

So step4: h+1 =3. Compute ceil(7/3)=3. sum 3+3=6.

Which is correct.

Another example: n=6.

h=2. h^2=4 <6.

h*(h+1)=2*3=6 >=6. sum 2+3=5.

Yes.

So the steps are:

Compute h as the integer part of sqrt(n).

If h*h >=n, then sum is 2h.

Else, check if h*(h+1) >=n. If yes, sum is h + (h+1) = 2h +1.

Else, sum is (h+1) + ceil(n/(h+1)).

But wait, when h*(h+1) <n, then h+1 is the new h. Let's see.

For example, n=8:

h=2. h^2=4 <8.

h*(h+1) =6 <8. So proceed to h+1=3. Compute ceil(8/3) =3. sum 3+3=6.

But 3*3=9 >=8, so sum is 6. Which is correct.

But wait, another possibility is h=3 and w=3. sum 6. Correct.

Another example: n=5.

h=2. h^2=4 <5.

h*(h+1)=6 >=5. So sum is 2+3=5.

Which is correct.

So the algorithm would be:

Compute h = floor(sqrt(n)).

Check if h*h >=n:

if yes, then sum is 2h.

else:

if h*(h+1) >=n, sum is 2h+1.

else:

sum is (h+1) + (h+1) = 2h+2 ?

Wait, no. Because (h+1) * (h+1) = (h+1)^2 >=n.

Wait, no. For example, n=7: h=2. (h+1)^2=9 >=7. So sum is 3+3=6.

But another example: n=10. h=3 (3^2=9 <10). h+1=4. 4*3=12 >=10. So sum is 3+4=7. Wait, but (h+1) is 3, then h+1 is 3. Wait, no, h is 3. Then h+1 is 4. Wait, original h is 3. Wait, sqrt(10) is ~3.16. So h is 3. Then:

h^2=9 <10.

Check h*(h+1)=3*4=12 >=10. So sum is 3+4=7.

But 4*3=12 >=10. So sum is 7.

Alternatively, h=3, w=4. sum 7.

But 3+4=7. So correct.

But if we tried h+1=4, then h+1 * h+1=4*4=16 >=10, sum 8. Which is worse than 7.

So the correct approach is to compute h= floor(sqrt(n)), then:

if h^2 >=n → sum 2h.

else:

check h*(h+1) >=n. If yes, sum 2h+1.

else, sum (h+1) + ceil(n/(h+1)).

Wait, but when h*(h+1) <n, then ceil(n/(h+1)) is greater than h+1.

For example, n=7, h=2:

h+1=3.

ceil(7/3) =3. sum 3+3=6.

Which is correct.

Another example, n=11.

h=3 (3^2=9 <11).

3*4=12 >=11? No. 12 >=11 → yes. So sum 3+4=7.

But 3*4=12 >=11. So sum is 7.

Wait, 3+4=7. Which is correct.

Another example, n=12.

h=3 (3^2=9 <12).

3*4=12 >=12. sum 3+4=7.

Which is correct.

Another example, n=13.

h=3. 3^2=9 <13. 3*4=12 <13. So proceed to step else.

h+1=4. ceil(13/4) =4. sum 4+4=8.

But 4*4=16 >=13. Sum 8.

Alternatively, h=4, and w=4. sum 8. Correct.

Yes.

So the algorithm would be:

h = floor(sqrt(n))

if h * h >= n:

    return 2h

else if h*(h+1) >=n:

    return 2h +1

else:

    return (h+1) + ((n + h) // (h+1)) ?

Wait, let's see. Because when h+1 is the new h, we need to compute the minimal w such that (h+1)*w >=n. The minimal w is ceil(n/(h+1)). So sum is (h+1) + ceil(n/(h+1)).

Yes.

So for example, n=7: h=2. h+1=3. ceil(7/3)=3. sum 3+3=6.

For n=10, h=3. h+1=3 (since h=3). Wait, no, h=3, then h+1=4. ceil(10/4)=3 (since 4*2=8 <10, 4*3=12 >=10). So sum is 4+3=7.

But in the case of h+1=4 and w=3, sum is 7. Which is indeed correct.

Wait, 4*3=12 >=10, sum 4+3=7.

Yes.

So, the steps are:

Compute h = floor(sqrt(n)).

if h^2 >=n: sum 2h.

elif h*(h+1)>=n: sum 2h+1.

else:

h_new = h+1.

w = ceil(n/h_new).

sum = h_new + w.

So how to compute ceil(n/h_new)? Well, ceil(a/b) = (a +b-1) //b.

So in code:

h = int(math.isqrt(n))

if h * h >=n:

    return 2*h

elif h*(h+1) >=n:

    return 2*h +1

else:

    h_new = h+1

    w = (n + h_new -1) // h_new

    return h_new + w

So this should handle all cases.

Let's test this with some examples.

Example 1: n=1.

h=1. 1*1=1 >=1. sum 2.

Example 2: n=2.

h=1. 1*1=1 <2. Check 1*2=2 >=2. sum 1+2=3.

Example 3: n=4.

h=2. 2*2=4 >=4. sum 4.

Example 4: n=5.

h=2. 2*2=4 <5. Check 2*3=6 >=5. sum 2+3=5.

Example 5: n=7.

h=2. 2*2=4 <7. 2*3=6 <7. So h_new=3. w=(7+3-1)//3 = (9)//3=3. sum 3+3=6.

Which is correct.

Another example: n=8.

h=2. 2*3=6 <8. h_new=3. w=(8+3-1)//3 =10//3=3. sum 3+3=6. Correct.

n=10: h=3. 3*3=9 <10. 3*4=12 >=10. sum 3+4=7. Correct.

n=12: h=3. 3*4=12 >=12. sum 3+4=7. Correct.

n=13: h=3. 3*4=12 <13. h_new=4. w=(13+4-1)/4 =16/4=4. sum 4+4=8. Correct.

n=6: h=2. 2*3=6 >=6. sum 5. Correct.

n=15: h=3 (sqrt(15)=3.872). h=3. h*(h+1)=3*4=12 <15. h_new=4. w=(15 +4-1)/4=18//4=4.5 →4.5? Wait, (15+4-1)=18 →18//4=4.5? Wait, no. (15 +3) //4 =18//4=4.5 → but in integer division, it's 4.5 is 4 in Python 3 if using integer division. Wait, wait. Wait 18 divided by 4 is 4.5, but in Python, 18//4 is 4. So ceil(15/4) =4 (since 4*4=16 >=15). So w=4. sum 4+4=8.

But 4*4=16 >=15. So sum 8. Which is correct.

Another example: n=16. h=4. sum 4+4=8. Correct.

So the algorithm works.

So the code can be written as follows:

First, import math, read n.

Compute h as math.isqrt(n).

Then check the conditions.

But in Python, math.isqrt(n) returns the integer square root, which is the floor of sqrt(n).

So code:

import math

n = int(input())

h = math.isqrt(n)

if h * h >=n:

    print(2 * h)

elif h * (h +1) >=n:

    print(2 * h +1)

else:

    h_new = h +1

    w = (n + h_new -1) // h_new

    print(h_new + w)

This should handle all cases.

Testing with sample inputs:

Sample 1:

n=1 → h=1. 1*1 >=1 → print 2. Correct.

Sample 2:

n=2 →h=1. 1*1=1 <2. Check 1*2=2 >=2 → print 3. Correct.

Sample 3:

n=4 →h=2. 2*2=4 → print 4. Correct.

Another test case: n=5 → output 5. Correct.

Thus, this code should solve the problem efficiently even for n up to 1e9, as all operations are O(1), and math.isqrt is efficient.
</think>

```python
import math

n = int(input())
h = math.isqrt(n)
if h * h >= n:
    print(2 * h)
elif h * (h + 1) >= n:
    print(2 * h + 1)
else:
    h_new = h + 1
    w = (n + h_new - 1) // h_new
    print(h_new + w)
```