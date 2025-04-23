<think>
Okay, I need to solve this problem where I have to check if four given line segments form a rectangle with positive area and sides parallel to the axes. Let's think about what conditions must be met for this to be true.

First, the rectangle must have sides parallel to the x and y axes. That means the rectangle's sides are either horizontal or vertical. So, the four line segments should consist of two horizontal lines (same y-coordinate for both endpoints, and varying x) and two vertical lines (same x-coordinate for both endpoints, varying y). But wait, each of the four segments provided could be any orientation, so I need to check each segment's orientation.

Wait, but the problem says that the four segments form the rectangle. So each segment must be a side of the rectangle. For a rectangle with sides parallel to the axes, the four sides are two horizontal (top and bottom) and two vertical (left and right). Each of these four must be exactly one of the given four segments.

Each horizontal segment must have the same y-coordinate for both endpoints. Similarly, vertical segments must have same x-coordinate for both endpoints. So first, I need to check each segment to see if it's either horizontal or vertical. If any segment is neither, then the answer is NO.

So step 1: Check all four segments. Each must be either horizontal (y1 == y2) or vertical (x1 == x2). If any segment is neither, output NO.

But wait, the problem allows the segments to be degenerate (points). So a segment could be a point (both endpoints same), but in that case, it's considered both horizontal and vertical. But in the case of a rectangle, such a segment can't be part of the rectangle's sides, since each side must have positive length. Because the rectangle must have positive area. So the four sides must have positive length. Therefore, each of the four segments must be either a horizontal or vertical line with length greater than zero.

Wait, but the problem statement says "positive area and with sides parallel to coordinate axes." So each side must be a line segment (not a point) and contribute to forming the rectangle. So each of the four segments must be a non-degenerate line segment, either horizontal or vertical. So first, check that each segment is either horizontal (y1 == y2 and x1 != x2) or vertical (x1 == x2 and y1 != y2). If any segment is not horizontal or vertical, or is a point (same endpoints), then output NO.

Wait no: if a segment is a point, but the other segments form a rectangle with that point being one of the four sides. But that's impossible. Because the four sides of a rectangle must each have length greater than zero. So if any of the four segments is a point (same endpoints), then it's invalid. So the first check is: each segment is either horizontal (y1 == y2 and x1 != x2) or vertical (x1 == x2 and y1 != y2). If any segment fails this, output NO.

So step 1: Check each of the four segments. For each segment, if it's not horizontal and not vertical, then output NO. Also, if it's a point (start and end same), then output NO. Because that can't form a rectangle with positive area.

So that's the first condition. Then, after confirming that all four segments are either horizontal or vertical and non-degenerate, we need to check if they form a rectangle.

So the next step is to collect all the horizontal and vertical segments. Let's separate them. Suppose there are exactly two horizontal and two vertical segments. Otherwise, it's impossible to form a rectangle. Because a rectangle has two horizontal sides (top and bottom) and two vertical (left and right). So if the count isn't two each, then output NO.

Wait, but wait. For example, if three segments are vertical and one horizontal. Then it's impossible. So step 2: check that there are exactly two horizontal and two vertical segments. If not, output NO.

Once that's confirmed, then we need to check the following:

The two horizontal segments must be the top and bottom edges. Each horizontal segment must have the same x-coordinate for their endpoints (since they are horizontal). Wait, no. Wait, a horizontal segment has y1 = y2, and x1 and x2 can be any values as long as the segment is non-degenerate (x1 != x2). Wait, no: a horizontal segment has y1 == y2, and x1 and x2 can be different, which gives the length. So for the top and bottom edges, each horizontal segment must have a fixed y-coordinate, and span between the left and right x-coordinates.

Similarly, the vertical segments must be the left and right edges. Each vertical segment has x1 == x2 (since they are vertical), and their y1 and y2 span between the top and bottom y's.

So the four segments must be arranged such that:

- The two horizontal segments have the same y-coordinate. Wait no: each horizontal segment is either the top or bottom. So the two horizontal segments must have different y-coordinates. Similarly, the two vertical segments must have different x-coordinates.

Wait, the two horizontal segments are the top and bottom of the rectangle. So their y-coordinates must be different, and they must form the top and bottom. Similarly, the two vertical segments are the left and right sides, so their x-coordinates must be different.

So:

For the two horizontal segments:

- Their y-coordinates (y1 and y2 for each) are the same, since they are horizontal. So each horizontal segment has a certain y value. The two horizontal segments must have different y values. Because if they were the same, they would be overlapping (but perhaps not). For example, if two horizontal segments are at the same y, then they would be part of the same horizontal line, but that can't form the top and bottom. So the two horizontal segments must have distinct y values, and those y values must be the top and bottom of the rectangle.

Similarly for the vertical segments: each has x1 == x2, and the two vertical segments must have distinct x values (left and right).

So for the horizontal segments:

Let the two y-values be y_min and y_max, with y_min < y_max.

For the vertical segments:

The two x-values are x_min and x_max, x_min < x_max.

Then, the rectangle is formed by the four edges:

- Bottom: from x_min to x_max at y_min.
- Top: from x_min to x_max at y_max.
- Left: from y_min to y_max at x_min.
- Right: from y_min to y_max at x_max.

So each of the four input segments must exactly match one of these four edges.

But the given segments can be in any order. So how do we check that the four segments form these four edges?

First, collect all horizontal segments. There must be exactly two. Let's collect their y-coordinates. For each horizontal segment, since it's a horizontal line, it's either part of the top or bottom.

But the problem is that each horizontal segment in the input may not span the entire x range. For example, perhaps the bottom segment is split into two parts, but that's not possible because the input segments are individual. So each of the two horizontal segments must exactly match the bottom and top edges.

Wait, but how? The four input segments are the four edges of the rectangle. So for the two horizontal segments, each must be exactly the top edge (from x_min to x_max at y_max) or the bottom edge (from x_min to x_max at y_min). Similarly for the vertical segments.

But how do I check this?

Let me think. For the horizontal segments, each must have the same x1 and x2 as the full span of the rectangle. Wait no. For example, one horizontal segment is (x_min, y_min) to (x_max, y_min) — that's the bottom edge. Another is (x_min, y_max) to (x_max, y_max) — that's the top. Similarly for vertical segments.

So the steps would be:

1. Check that all four segments are horizontal or vertical, and non-degenerate.

2. Check that there are exactly two horizontal and two vertical segments.

3. For the two horizontal segments, collect their y-coordinates. They must be two distinct values. Let’s call them y1 and y2, sorted so that y1 < y2.

4. For the two vertical segments, collect their x-coordinates. Must be two distinct values. Let’s call them x1 and x2, sorted as x1 < x2.

5. Now, each horizontal segment must span exactly from x1 to x2. Because the bottom and top edges of the rectangle are from x1 to x2. So for each horizontal segment, the start and end x-coordinates must be x1 and x2 (in any order). Similarly, each vertical segment must span from y1 to y2. Because the left and right edges are from y1 to y2.

Wait, but the order of the points in the segment can be reversed. For example, a horizontal segment could be (x_max, y_min) to (x_min, y_min), but that's the same as (x_min, y_min) to (x_max, y_min).

So for each horizontal segment, after ensuring it's horizontal, check that the x-coordinates form a line from x_min to x_max (i.e., the minimum and maximum x of the vertical segments). But how do we find x_min and x_max?

Wait, the x_min and x_max are determined by the vertical segments. Because the vertical segments are the left and right edges. So the vertical segments must have x-coordinates x_min and x_max. So for example, suppose the two vertical segments are (x_a, y_start) to (x_a, y_end) and (x_b, y_start) to (x_b, y_end), where x_a < x_b. Then the rectangle's x_min is x_a, x_max is x_b. Similarly, the horizontal edges must be between x_a and x_b, and between y_min and y_max (from the horizontal edges' y-coords).

But how do I connect these variables?

Alternatively, after determining that there are two vertical segments with x1 and x2 (distinct), sorted as x_min and x_max. Then, the two horizontal segments must each have their x-coordinates spanning exactly from x_min to x_max. Similarly, the vertical segments must each span from y_min to y_max, where y_min and y_max are the sorted y-coordinates of the two horizontal segments.

So steps:

Collect the two vertical segments. Their x-coordinates are x1 and x2. Let x_min = min(x1, x2), x_max = max(x1, x2).

Collect the two horizontal segments. Their y-coordinates are y1 and y2. Let y_min = min(y1, y2), y_max = max(y1, y2).

Now, each horizontal segment must have start and end x coordinates equal to x_min and x_max (in any order). Because the horizontal edges are the top and bottom, which run the entire length from left (x_min) to right (x_max).

Similarly, each vertical segment must have start and end y coordinates equal to y_min and y_max (in any order). Because the vertical edges are the left and right, which run from bottom (y_min) to top (y_max).

So for each horizontal segment, check if the x coordinates are x_min and x_max. Because the horizontal segment must span the entire x range. If either of the horizontal segments doesn't cover x_min to x_max, then the answer is NO.

Similarly, for each vertical segment, check if their y coordinates are y_min and y_max. Because they must span the entire y range.

But how do we compute x_min and x_max? Because the vertical segments are the left and right edges, which have x coordinates x_left and x_right. But these are the x coordinates of the vertical segments. So for example, vertical segments could be (3, 0) to (3, 5) and (5, 0) to (5, 5). Then x_min is 3, x_max is 5.

So the vertical segments must have x coordinates x_left and x_right. So, the two vertical segments have x coordinates x1 and x2, which must be different. So x_min is the smaller of the two, x_max the larger.

But each vertical segment must span from y_min to y_max, which are the y-coordinates of the horizontal segments. So y_min is the lower of the two horizontal y's, y_max the higher.

So once we have the x_min, x_max, y_min, y_max, then:

For each horizontal segment:

Check that the x-coordinates are x_min and x_max. So the segment's x1 and x2 (after sorting) should equal x_min and x_max. Because the horizontal edges are the full length between the left and right edges.

For each vertical segment:

Check that the y-coordinates are y_min and y_max. The segment's y1 and y2 (sorted) should equal y_min and y_max. Because the vertical edges run the full height between bottom and top.

If all these conditions are met, then the four segments form a rectangle.

Additionally, the area must be positive. Which would be the case if (x_max - x_min) > 0 and (y_max - y_min) > 0. Because (x_max - x_min) is the width, (y_max - y_min) is the height. So their product is the area, which must be positive. So both (x_max - x_min) and (y_max - y_min) must be positive. So when we check x_min and x_max, x_max must be larger than x_min, and similarly y_max must be larger than y_min.

So putting all this together:

The algorithm steps are:

1. Check each segment to be horizontal or vertical and non-degenerate. If any fails, output NO.

2. Check that there are exactly two horizontal and two vertical segments. Otherwise, output NO.

3. Collect the x coordinates of the vertical segments. There are two vertical segments, each has x1 == x2. So each vertical segment's x coordinate is x_v1 and x_v2. Then x_min_v = min(x_v1, x_v2), x_max_v = max(x_v1, x_v2). But wait, no. Each vertical segment's x-coordinate is fixed (since they are vertical). So for example, vertical segment 1 is (a, y1) to (a, y2). So its x-coordinate is a. Similarly, vertical segment 2 is (b, y3) to (b, y4). So their x coordinates are a and b. So x_min is min(a, b), x_max is max(a, b). So the two vertical segments contribute x coordinates a and b.

Similarly, the two horizontal segments have y coordinates c and d. So y_min is min(c, d), y_max is max(c, d).

4. Check that x_min < x_max and y_min < y_max. Otherwise, the area is zero.

5. For each of the two horizontal segments, check that their x coordinates span from x_min to x_max. So for a horizontal segment, the x1 and x2 must be x_min and x_max (possibly in any order). So sorted([x1, x2]) == [x_min, x_max].

6. For each of the two vertical segments, check that their y coordinates span from y_min to y_max. So sorted([y1, y2]) == [y_min, y_max].

If all these conditions are met, then output YES. Otherwise, NO.

So let's test this logic against the examples.

First example:

Input:

1 1 6 1 → horizontal, y=1. x1=1, x2=6. So x coordinates 1 and 6.

1 0 6 0 → horizontal, y=0. x1=1, x2=6.

6 0 6 1 → vertical, x=6. y from 0 to 1.

1 1 1 0 → vertical, x=1. y from 0 to 1.

So vertical segments have x=6 and x=1. x_min is 1, x_max 6. y_min is 0, y_max 1.

Check for horizontal segments: each x's are 1 and 6 → sorted to 1,6. So yes. Both horizontal segments are (1,6) in x. So they are the top and bottom.

For vertical segments: each has y from 0 to 1 → sorted 0,1. So yes.

x_max -x_min is 5, y_max - y_min is 1. Area 5>0. So output YES.

Second example:

0 0 0 3 → vertical segment (x=0, y from 0 to3). 

2 0 0 0 → this is a horizontal segment? Wait, (2,0) to (0,0) → y1 = y2 =0. So yes, horizontal. x1=2, x2=0. So x spans from 0 to 2.

2 2 2 0 → vertical segment (x=2, y from 0 to 2). 

0 2 2 2 → horizontal (y=2). x from 0 to 2.

Now, vertical segments are the first and third segments. Their x-coords are 0 and 2. So x_min=0, x_max=2.

Horizontal segments are second and fourth. Their y-coords are 0 and 2. So y_min=0, y_max=2.

Check for horizontal segments: their x spans are 0 and 2. So x_min and x_max. So sorted(2,0) is [0,2] for the second segment. Fourth segment x0 to 2 → sorted [0,2]. So both horizontal segments are okay.

Vertical segments: first segment (x=0) has y from 0 to3. sorted [0,3]. But y_min is 0, y_max 2. So 3 is larger than y_max (2). So the vertical segment's y coordinates (0 and 3) do not match the required y_min (0) and y_max (2). So this check fails. So the answer is NO.

Which matches the sample input.

Another test case: suppose one horizontal segment's x coordinates are not spanning from x_min to x_max. For example, horizontal segment is (x_min, y) to x_mid, y. Then it's not covering the full x range, so it's invalid.

Now, let's think about possible code structure.

First, for each of the four segments:

Read the four numbers x1, y1, x2, y2.

Check if the segment is horizontal (y1 == y2) or vertical (x1 == x2). Also, ensure that the segment is not a point (x1 != x2 or y1 != y2). Wait: for a horizontal segment, x1 must not equal x2. For a vertical segment, y1 must not equal y2.

So for each segment:

Check if (x1 == x2 and y1 == y2) → then it's a point. So invalid.

Else, check if horizontal (y1 == y2) or vertical (x1 == x2). If neither, invalid.

So for each segment, first check if it's a point → invalid. Then check if it's horizontal or vertical.

So for code:

segments = [list(map(int, input().split())) for _ in range(4)]

horizontal = []
vertical = []

for seg in segments:
    x1, y1, x2, y2 = seg
    if x1 == x2 and y1 == y2:
        print("NO")
        exit()
    if x1 == x2:
        # vertical
        vertical.append(seg)
    elif y1 == y2:
        horizontal.append(seg)
    else:
        print("NO")
        exit()

if len(horizontal) != 2 or len(vertical) != 2:
    print("NO")
    exit()

Then, process the horizontal and vertical segments.

For vertical segments, collect their x coordinates. So for each vertical segment, x1 is the x-coordinate. So x_v1 = vertical[0][0], x_v2 = vertical[1][0].

x_min = min(x_v1, x_v2)
x_max = max(x_v1, x_v2)

Similarly, for horizontal segments:

y_h1 = horizontal[0][1]  # since horizontal, y1 == y2
y_h2 = horizontal[1][1]

y_min = min(y_h1, y_h2)
y_max = max(y_h1, y_max)

Check if x_max -x_min <=0 → no. But wait, x_max is max of x_v1 and x_v2, which are two different numbers (since vertical segments are x1 and x2). Because in vertical segments, each has x1 == x2 (since they are vertical). So for vertical[0], x1 is same as x2, so the x coordinate is x_v1 = vertical[0][0]. Similarly vertical[1] has x_v2 = vertical[1][0].

But since there are two vertical segments, their x coordinates must be different. Otherwise, x_min and x_max would be the same. For example, if both vertical segments are at x=5. Then x_min and x_max are 5. So x_max -x_min = 0. But the rectangle's width is zero. So area is zero. Which is invalid.

So in code, after extracting x_v1 and x_v2:

x_v1 = vertical[0][0]
x_v2 = vertical[1][0]
if x_v1 == x_v2:
    print("NO")
    exit()

x_min = min(x_v1, x_v2)
x_max = max(x_v1, x_v2)

Similarly for y:

y_h1 = horizontal[0][1]
y_h2 = horizontal[1][1]
if y_h1 == y_h2:
    print("NO")
    exit()

y_min = min(y_h1, y_h2)
y_max = max(y_h1, y_h2)

So that's another check. So after collecting the vertical and horizontal segments, check that the two vertical x are different, and the two horizontal y are different. Otherwise, output NO.

Then, check that (x_max - x_min) >0 and (y_max - y_min) >0. But since x_max is larger than x_min (since we have x_max and x_min from min and max), and y_max similarly, this is ensured.

So then, for each horizontal segment, check that their x coordinates span x_min to x_max. Because a horizontal segment in the rectangle must be either the top or bottom edge, which runs from x_min to x_max.

So for a horizontal segment, which is stored as (x1, y, x2, y), the x coordinates can be in any order. So the sorted x coordinates of the segment must be [x_min, x_max].

So for each horizontal segment in the horizontal list:

s_x1, s_y, s_x2, _ = seg  # since it's horizontal, y is same for both points.

sorted_x = sorted([s_x1, s_x2])
if sorted_x != [x_min, x_max]:
    print("NO")
    exit()

Similarly, for each vertical segment:

seg is (x, y1, x, y2). So check that the sorted [y1, y2] is [y_min, y_max].

So for vertical segments:

x, y1, x, y2 = seg
sorted_y = sorted([y1, y2])
if sorted_y != [y_min, y_max]:
    print("NO")
    exit()

If all checks pass, output YES.

So putting all this together.

Now, code steps:

Read four segments.

Check each segment is not a point, and is horizontal or vertical. Collect into horizontal and vertical lists.

Check counts are two each.

Check vertical x's are different, horizontal y's are different.

Compute x_min and x_max from vertical x's.

Compute y_min and y_max from horizontal y's.

Check each horizontal segment's x spans from x_min to x_max.

Check each vertical segment's y spans from y_min to y_max.

If all pass, output YES. Else, NO.

Now, code.

Let's code this step by step.

Read the segments:

segments = []
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    segments.append( (x1, y1, x2, y2) )

Check each segment:

horizontal = []
vertical = []
for seg in segments:
    x1, y1, x2, y2 = seg
    # check if it's a point
    if x1 == x2 and y1 == y2:
        print("NO")
        exit()
    # check horizontal or vertical
    if x1 == x2:
        # vertical
        vertical.append( seg )
    elif y1 == y2:
        horizontal.append( seg )
    else:
        print("NO")
        exit()

Check counts:

if len(horizontal) != 2 or len(vertical) != 2:
    print("NO")
    exit()

Check vertical x's are different:

x_coords_vertical = [seg[0] for seg in vertical]  # x1 for vertical segments
if x_coords_vertical[0] == x_coords_vertical[1]:
    print("NO")
    exit()
x_min = min(x_coords_vertical)
x_max = max(x_coords_vertical)

Check horizontal y's are different:

y_coords_horizontal = [seg[1] for seg in horizontal]  # y1 is same as y2
if y_coords_horizontal[0] == y_coords_horizontal[1]:
    print("NO")
    exit()
y_min = min(y_coords_horizontal)
y_max = max(y_coords_horizontal)

Now, check each horizontal segment's x span:

for seg in horizontal:
    x1, y1, x2, y2 = seg
    sorted_x = sorted([x1, x2])
    if sorted_x != [x_min, x_max]:
        print("NO")
        exit()

Check each vertical segment's y span:

for seg in vertical:
    x1, y1, x2, y2 = seg
    sorted_y = sorted([y1, y2])
    if sorted_y != [y_min, y_max]:
        print("NO")
        exit()

All checks passed:

print("YES")

So this is the code.

Testing the first example:

Vertical segments: two segments with x=6 and 1. x_min=1, x_max=6.

Horizontal segments: y=1 and 0. y_min=0, y_max=1.

Each horizontal segment's x's are 1 and 6 → sorted [1,6] → matches x_min and x_max. Vertical segments' y's sorted are 0 and 1 → which matches y_min and y_max. So YES.

Second example:

Vertical segments have x=0 and 2. x_min=0, x_max=2.

Horizontal segments: y=0 and 2. y_min=0, y_max=2.

Check vertical segments: first vertical segment is (0,0,0,3). sorted y is [0,3]. Which is not [0,2]. So check fails. Output NO.

Another test case: segments that form a rectangle but one vertical segment's y is not spanning the entire y range. For example:

Horizontal1: (0,0,5,0) → y=0. Horizontal2: (0,3,5,3) → y=3.

Vertical1: (0,0,0,3). Vertical2: (5,0,5,3).

Then x_min=0, x_max=5. y_min=0, y_max=3. Each horizontal segment's x is 0 and 5. Each vertical's y is 0 and 3. So YES.

Another test case: vertical segments have x 0 and 5. But one vertical segment spans from y=0 to y=2, and another from y=1 to y=3. So sorted ys are [0,2] and [1,3]. The y_min is 0, y_max is 3. So for each vertical segment, sorted y should be [0,3]. The first vertical segment's sorted y is [0,2], which is not equal to [0,3]. So check fails.

Thus, code is correct.
</think>

```python
segments = []
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    segments.append((x1, y1, x2, y2))

horizontal = []
vertical = []

for seg in segments:
    x1, y1, x2, y2 = seg
    if x1 == x2 and y1 == y2:
        print("NO")
        exit()
    if x1 == x2:
        vertical.append(seg)
    elif y1 == y2:
        horizontal.append(seg)
    else:
        print("NO")
        exit()

if len(horizontal) != 2 or len(vertical) != 2:
    print("NO")
    exit()

x_coords = [vertical[0][0], vertical[1][0]]
if x_coords[0] == x_coords[1]:
    print("NO")
    exit()
x_min, x_max = min(x_coords), max(x_coords)

y_coords = [horizontal[0][1], horizontal[1][1]]
if y_coords[0] == y_coords[1]:
    print("NO")
    exit()
y_min, y_max = min(y_coords), max(y_coords)

for seg in horizontal:
    x1, y1, x2, y2 = seg
    if sorted([x1, x2]) != [x_min, x_max]:
        print("NO")
        exit()

for seg in vertical:
    x1, y1, x2, y2 = seg
    if sorted([y1, y2]) != [y_min, y_max]:
        print("NO")
        exit()

print("YES")
```