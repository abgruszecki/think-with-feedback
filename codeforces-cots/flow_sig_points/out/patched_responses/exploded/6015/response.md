<think>
Okay, let's tackle this problem. So, Maria is racing on a track made up of straight sections, and we need to find the number of dangerous turns. A dangerous turn is one where, if she doesn't turn properly, she ends up in the water. But how do we model that?

First, let's understand the problem. The track is a closed loop, starting at the southernmost (and then westernmost) point, moving north first. Each straight section is connected end to end, and adjacent sections can't be the same or opposite directions. So, each turn is a 90-degree turn either left or right, but the direction changes in a way that the path is a polygon with right angles, perhaps.

A dangerous turn is when the next straight line (if the turn wasn't made) would go into the 'inside' of the polygon. Wait, no. Wait, the track is the perimeter of the polygon. If Maria misses a turn and continues straight, she would exit the track and enter the lake. So, the dangerous turn is when the turn is such that the direction after the turn is such that the 'inside' of the polygon is on the right or left, but if she continues straight, she would be inside the lake. Hmm, perhaps the key is to model the track as a polygon and determine for each turn whether the turn is a convex or concave angle. Wait, but in a polygon, a convex turn would mean that if the direction continues, it's outside the polygon, whereas a concave turn would mean that continuing straight would go into the polygon's interior. Wait, maybe not. Let's think.

The track is a polygon, and the racers are moving around its perimeter. So, the polygon is the outline of the track. Now, the direction of movement is such that the polygon is either clockwise or counter-clockwise. When a turn is a "convex" corner (angle less than 180 degrees) versus a "concave" (angle greater than 180), that affects the direction. But how does this relate to the dangerous turns?

Wait, according to the problem statement, a dangerous turn is one where if Maria doesn't turn, she immediately enters the water. So, the 'water' is the interior of the polygon. So, the track is the perimeter of a polygon, and the lake is inside. Wait, perhaps the track is the boundary of the lake. So, the lake is the area enclosed by the polygon. If Maria doesn't turn and continues straight, she would go into the lake (the interior of the polygon) if the turn is a concave corner. Because, at a concave corner, the interior angle is such that the path that continues straight would head into the interior. So, the dangerous turns are the concave corners.

Wait, but how to determine whether a corner is convex or concave? Let's think. For a polygon, the convexity of each vertex depends on the direction in which the polygon is traversed. So, for example, if the polygon is traversed in clockwise order, then convex corners are those where the turn is to the right, and concave (if any, since polygons can be non-convex) are left turns. Wait, no. Wait, in a polygon, a convex polygon has all interior angles less than 180 degrees. A concave polygon has at least one interior angle greater than 180. So, for a polygon that is traversed in clockwise order, a left turn at a vertex indicates a concave angle, and a right turn indicates a convex angle. Because, when moving clockwise, each turn direction (right or left) determines whether the angle is convex or concave. Alternatively, perhaps we can use the cross product of the direction vectors to determine the turn direction.

So, here's the approach: For each consecutive triplet of points (prev, current, next), compute the direction of the turn. If the turn is a left turn (indicating a concave corner in a clockwise polygon), then that's a dangerous turn, because if the rider continues straight (doesn't turn), they enter the lake. Or wait, maybe the other way around. Let's think.

The track forms a simple polygon (no self-intersections). The polygon is either traversed clockwise or counter-clockwise. The starting direction is north. Let's see the first example:

Sample input 1:

6

0 0

0 1 (north)

then (0,1) to (1,1) is east.

Then (1,1) to (1,2) is north again. Wait, but the problem says adjacent sections can't be same or opposite. So perhaps the first sample's track is:

The points are:

0,0 (start)

0,1 (north)

1,1 (east)

1,2 (north again? Wait, that's same direction as previous, but adjacent sections can't be same. Wait, the problem says that adjacent sections can't be same direction or opposite. So in the first sample, the directions must alternate. Wait, let's look at the sample input.

Wait the first sample's input is:

6

0 0

0 1

1 1

1 2

2 2

2 0

0 0

So the straight sections are:

0: (0,0) to (0,1) → north.

1: (0,1) to (1,1) → east.

2: (1,1) to (1,2) → north. But wait, that's two consecutive north directions. But according to the problem statement, adjacent sections can't be same or opposite. So this would be invalid. But the first sample is given as a valid input. Wait, that's a problem. Wait, perhaps I've miscalculated the directions.

Wait, the sections are from (xi, yi) to (xi+1, yi+1). So for the first sample:

Sections:

0: (0,0) → (0,1) → direction is north.

1: (0,1) → (1,1) → east.

2: (1,1) → (1,2) → north again. So same as previous direction. Which is not allowed. So that's conflicting with the problem's constraints. Wait, but the problem says that any pair of adjacent sections can't be same direction or opposite. So perhaps the sample input is correct, but maybe I'm miscalculating the directions.

Wait, perhaps the problem's constraints are that adjacent sections can't be same or opposite. Let's look again.

The problem says: "any pair of adjacent straight sections are directed in the same direction or in opposite directions." No, the problem says: "It is guaranteed that... no two adjacent straight sections are directed in the same direction or in opposite directions." So adjacent sections must turn 90 degrees left or right. So in the first sample, how does the direction change?

Wait, after the first section (north), the next direction is east. Then next is north again. So from east to north is a left turn. Wait, but how is that possible if adjacent sections can't have same direction. Wait, perhaps I'm misunderstanding the sections. Wait, each straight section is between consecutive points. So section 0 is from (0,0) to (0,1) → direction is north. Section 1 is from (0,1) to (1,1) → east. Section 2 is from (1,1) to (1,2) → north. So sections 1 and 2 are adjacent. Their directions are east and north, which are perpendicular. So that's allowed. Because adjacent sections can't have same or opposite directions. So that's allowed. So the problem's constraints are satisfied.

So the direction changes between adjacent sections are always 90 degrees (left or right), but not same or opposite.

So now, the track is a polygon. The problem is to find all turns (vertices) where, if the rider continued straight instead of turning, they would enter the lake (the interior of the polygon). So the question becomes: for each vertex (corner) in the polygon, determine whether the interior of the polygon is to the left or right of the direction of travel. Then, if the next straight section (the actual direction after the turn) is such that the rider would be entering the interior if they didn't turn, then the turn is dangerous.

But how to model this? The key is to determine whether the polygon is being traversed in clockwise or counter-clockwise direction, and then for each vertex, determine if the turn is convex or concave. For a convex polygon, all turns are in the same direction. But since the track can be a concave polygon, we need to check each turn.

Alternatively, perhaps we can use the cross product to determine the direction of the turn (left or right) and the orientation of the polygon to determine if that turn is a concave or convex vertex.

Let's think about the polygon's winding order. The starting direction is north, then the next direction is east, then north again. Wait, the track starts at the southernmost point (0,0) and moves north. Then, after that, the directions change according to the points. The polygon formed by these points could be either clockwise or counter-clockwise. But how to determine the overall orientation?

The overall orientation (clockwise or counter-clockwise) can be determined by the sum of the cross products of consecutive edges. For a polygon, the sum of (x_i y_{i+1} - x_{i+1} y_i) divided by 2 gives the area. The sign of this sum indicates the orientation: positive for counter-clockwise, negative for clockwise.

Wait, but the track is a closed loop, starting and ending at the same point. So the sum of the cross products (the area * 2) will give the signed area. The sign tells us the winding order.

Once we know the overall orientation (clockwise or counter-clockwise), then for each consecutive triplet of points (p, c, n), we can compute the direction of the turn (left or right) and determine whether it's a convex or concave vertex. If the vertex is concave (interior angle > 180 degrees), then if the rider continues straight, they enter the lake. Hence, such a vertex is a dangerous turn.

So the plan is:

1. Read all the points (n+1 points, since each of the n sections is between consecutive points, and the last point is the same as the first).

2. Compute the overall orientation of the polygon (clockwise or counter-clockwise) using the signed area.

3. For each consecutive triplet of points (prev, current, next), compute the direction of the turn (left or right). Then, based on the overall orientation, determine if that turn is a concave or convex vertex. If concave, increment the count.

So how to compute the direction of the turn between three consecutive points.

For three consecutive points a, b, c:

Compute vectors ab (b - a) and bc (c - b). The direction of the turn from ab to bc can be determined by the cross product of these vectors. Wait, but the direction of the vectors. Let's see.

The vector ab is (bx - ax, by - ay). The vector bc is (cx - bx, cy - by). The cross product of ab and bc is (ab.x * bc.y - ab.y * bc.x). The sign of this cross product tells us the direction of the turn. If cross product is positive, the turn is counter-clockwise (left turn). If negative, it's a clockwise (right turn). If zero, colinear (but problem says no colinear adjacent edges).

But since the polygon is closed and given in order, the cross product for each edge pair can determine the direction of each bend.

But how does the overall orientation relate to the concavity of a vertex?

Suppose the overall polygon is counter-clockwise (positive area). Then, for a vertex, if the turn is a right turn (cross product < 0), that vertex is a concave (interior angle > 180 degrees) point. Because in a counter-clockwise polygon, right turns indicate concavity.

Similarly, if the overall polygon is clockwise (negative area), then left turns (cross product > 0) indicate concave vertices.

So the approach is:

- Compute the total signed area. If the sum is positive, the polygon is counter-clockwise. If negative, clockwise.

- For each triplet (a, b, c):

   - Compute the cross product of (b - a) and (c - b). The sign of this cross product indicates the turn direction.

   - Then, depending on the overall orientation:

      - If counter-clockwise: a negative cross product (right turn) implies concave vertex → dangerous.

      - If clockwise: a positive cross product (left turn) implies concave vertex → dangerous.

So the steps are:

1. Compute the total area's sign to determine the overall orientation.

2. For each triplet (except the first and last, since the last is the same as the first), compute the cross product.

3. Compare the cross product's sign to the overall orientation to determine if the turn is concave.

4. Count the number of concave turns.

Let's test this logic with the first sample.

Sample 1:

Points are:

0 0 → 0 1 → 1 1 → 1 2 → 2 2 → 2 0 → 0 0.

Wait, no. The first sample input is:

6

0 0

0 1

1 1

1 2

2 2

2 0

0 0

Wait, so the points are (0,0), (0,1), (1,1), (1,2), (2,2), (2,0), (0,0). So there are 7 points (n=6, so 6+1=7 points).

The sections are from 0 to 6 points, but the last point is the same as the first.

Now, compute the cross product sum (for the area).

The formula is sum over i of (x_i y_{i+1} - x_{i+1} y_i) for all points except the last (since the last is same as first). Then, sum / 2 is the area. The sign gives the orientation.

Let's compute this:

For each i from 0 to 5 (since points 6 is same as 0):

i=0: x0=0, y0=0 → x1=0, y1=1 → contribution 0*1 - 0*0 =0.

i=1: x1=0, y1=1 → x2=1, y2=1 → 0*1 -1*1 = -1.

i=2: x=1, y=1 → x3=1, y3=2 → 1*2 -1*1 =2-1=1.

i=3: x=1, y=2 → x4=2, y4=2 →1*2 -2*2= 2-4= -2.

i=4: x=2, y=2 →x5=2, y5=0 →2*0 -2*2=0-4= -4.

i=5: x=2, y=0 →x6=0, y6=0 →2*0 -0*0=0.

Sum all contributions:

0 + (-1) +1 + (-2) + (-4) +0 = -6.

Total sum is -6. So the area is -6/2 = -3. So the sign is negative → the polygon is traversed in clockwise direction.

Now, for each triplet (a, b, c):

But the triplet is the previous point (a), current (b), next (c). Wait, in terms of the points, each section is from point i to i+1. So the turns are at point i+1. For example, the first turn is at point 1 (0,1). The path comes from (0,0) → (0,1) (north), then turns to (1,1) (east). So the vectors are (0,1) - (0,0) = (0,1), then (1,1) - (0,1) = (1,0). The cross product is (0*0) - (1*1) = -1 (0*0 - 1*1 → cross product of (0,1) and (1,0) is 0*0 -1*1 = -1). So cross product is negative. Since the polygon is clockwise, a negative cross product indicates a right turn. But according to our earlier logic, for a clockwise polygon, left turns (positive cross product) indicate concave vertices. Wait, I'm getting a bit confused.

Wait, the overall orientation is clockwise. For a clockwise polygon, when moving along the edges, a left turn (cross product positive) would mean a concave vertex. Because in a clockwise polygon, the 'normal' direction is to turn right (convex). So if a turn is left (cross product positive), that vertex is concave.

So, for the first sample:

Overall orientation is clockwise (sum of cross products is negative). For each vertex (after the first), compute the cross product of the current edge and next edge.

Wait, perhaps the cross product is calculated between the current edge (from b to c) and the next edge (from c to d). Wait, no. The turn at point c (the point after the edges bc and cd). Wait, maybe I should model each turn as the direction between two consecutive edges. For example, for a point i (not the first or last), the edges are (points i-1 to i) and (i to i+1). So the cross product is (edge1) × (edge2), where edge1 is (i-1 to i) and edge2 is (i to i+1). For example, the first turn is at point 1 (0,1). The edges are (0,0)-(0,1) → direction (0,1), and (0,1)-(1,1) → direction (1,0). The cross product is (0,1) × (1,0) → 0*0 -1*1 = -1. The sign is negative. Since the overall orientation is clockwise, this is a right turn. So in a clockwise polygon, right turns are convex, left turns are concave. So this turn (negative cross product, right turn) is convex. So not dangerous.

The next turn is at point 2 (1,1). Edges are (0,1)-(1,1) direction (1,0), then (1,1)-(1,2) direction (0,1). Cross product is (1,0) × (0,1) → 1*1 -0*0 = 1. Positive. So this is a left turn. Since the polygon is clockwise, left turns are concave. So this is a dangerous turn.

So the sample's answer is 1, which matches the first example.

So the algorithm is correct here.

So the steps are:

1. Compute the sum of the cross products of consecutive edges (excluding the last edge that loops back) to determine the overall orientation.

2. For each point (excluding the first and last, since they are the same as the start and end), compute the cross product of the edges before and after the point.

3. For each cross product:

   a. If the orientation is clockwise (sum negative), then a positive cross product (left turn) indicates a concave vertex (dangerous).

   b. If the orientation is counter-clockwise (sum positive), then a negative cross product (right turn) indicates a concave vertex (dangerous).

4. Count all such concave vertices.

Now, let's code this.

But first, how to compute the cross product sum for the polygon. Let's process all edges except the last one (since the last point is the same as the first). For each i in 0 to n-1, the edge is from points[i] to points[i+1]. The sum is computed as (xi * yi+1) - (xi+1 * yi) for each edge. Then, the sign of the sum will tell us the orientation.

Wait, the sum for the area is sum over (xi * yi+1 - xi+1 * yi) for all i from 0 to n (since there are n+1 points, and edges 0..n). But the problem states that the last point is the same as the first. So in code, for the sum, we can iterate from 0 to n-1, because the last edge is from points[n] to points[0], but points[n] is the same as points[0]. So in the code, the points list has n+1 elements, and the last edge is from points[n-1] to points[n] (which is points[0]).

Wait, the input is given as (n+1) points, with the last point same as first.

So for example, if n=6, then there are 7 points. The edges are 0-1, 1-2, 2-3, 3-4, 4-5, 5-6 (but 6 is same as 0). So edges 0 to 5 (n edges, since n is 6). So when processing the sum for the orientation, we need to loop through all edges from i=0 to i=n-1 (since there are n edges). So the code would be:

sum_area = 0

for i in range(n):

    x_i = points[i][0]

    y_i = points[i][1]

    x_next = points[i+1][0]

    y_next = points[i+1][1]

    sum_area += (x_i * y_next - x_next * y_i)

Then, the sum_area is twice the actual area. The sign tells us the orientation.

Once sum_area is computed, the orientation is clockwise if sum_area < 0, counter-clockwise if sum_area > 0.

Now, for each turn (vertex) in the polygon. The vertices are points[1], points[2], ..., points[n-1], since points[0] is the starting point and points[n] is the same as points[0].

Wait, no. The first edge is from points[0] to points[1]. The second edge is points[1] to points[2], etc. The turn is at the end of each edge. For example, after the first edge, the direction is determined by the second edge. So the turns occur at points[1], points[2], ..., points[n-1]. Because the edge is points[i] to points[i+1], and the next edge is points[i+1] to points[i+2]. So for each i from 0 to n-2, the turn at point i+1 is determined by the edges (i to i+1) and (i+1 to i+2). Then, for i from n-1, the next edge would be from i+1 (points[n]) to points[0], but since points[n] is same as points[0], but then points[0] to points[1], but this edge is the same as the first edge. But since the track is closed, the last turn would be at points[0], but that's the same as the starting point, so perhaps not considered. So the total number of turns is n, but in the problem statement, the track is closed. Wait, but the input has n straight sections, so there are n+1 points. The sections are from points[0] to points[1], ..., points[n] to points[0] (but that's the same as points[0] to points[0], which is zero-length). Wait, no, the problem says that the track is closed, and the last point is the same as the first. So the n sections are from points[0] to points[1], points[1] to points[2], ..., points[n-1] to points[n], and points[n] is same as points[0]. So there are n sections. So for each i from 0 to n-1, the edge is between points[i] and points[i+1].

So the turns are at the points points[1], points[2], ..., points[n]. But points[n] is same as points[0], which is the starting point. So the turn at points[n] would involve the edge from points[n-1] to points[n] (same as points[0]) and the edge from points[n] to points[0+1] (points[1]). So that's a valid turn. But since the track is closed, that's part of the loop.

But in code, we need to process all the vertices except perhaps the starting point. Wait, the problem statement says that the first straight section is directed to the north. So the first section is from points[0] to points[1], direction north. Then the next direction is determined by points[1] to points[2]. The turn at points[1] is between the first and second edges. So all points except points[0] and points[n] (since points[n] is same as points[0]) are considered. Wait, but points[0] is the starting point, and the first edge is north. Then the next edge starts at points[1]. So the turns are at points[1], points[2], ..., points[n]. But points[n] is same as points[0]. So how do we handle the turn at points[n] (points[0])?

For example, in the first sample, points[6] is (0,0), same as points[0]. The edges are points[5] to points[6] (2,0 → 0,0) which is west direction, and then the next edge is points[6] to points[1] (0,0 → 0,1) north. So the turn at points[6] (which is same as points[0]) is between the edge from points[5] to points[6] (west) and points[6] to points[1] (north). So this is a left turn (cross product of (-2,0) (since edge from points[5] (2,0) to points[6] (0,0) is vector (-2, 0)), then edge points[6] to points[1] (0,0) to (0,1) is (0,1). Cross product is (-2,0) × (0,1) = (-2)*1 - 0*0 = -2. So sign is negative. Since the overall orientation is clockwise (sum_area is -6 → sum_area is negative), then a cross product of negative here would be a right turn (convex). So not a dangerous turn.

So in code, for each vertex from 0 to n-1 (since the edges are 0 to n-1?), no. Wait, the edges are 0 to n-1, but the vertices are points[1] to points[n]. So the code needs to process each point i in 0 to n (since points has n+1 elements, indices 0 to n). But for the turn at point i, it's the edge i-1 → i and edge i → i+1.

Wait, let's index the points from 0 to n (since there are n+1 points). So edges are 0-1, 1-2, ..., n-1-n. Then, the turn at point i is between edge (i-1, i) and (i, i+1). For i=0, it's edge (n-1, 0) and (0, 1). So in code, for each i in 0 to n-1:

Wait, but the edges are 0-1, 1-2, ..., (n-1)-n. Then the next edge after n would be n-0 (since n+1-th point is 0). So the code needs to consider all points from 0 to n, but for each point i, the edges are (i-1, i) and (i, i+1), where i+1 is (i+1) mod (n+1), but since the points are given in order and the last point is same as first, perhaps we can treat i+1 as (i+1) but for i=n, i+1 is 0. But the code should handle that.

Alternatively, since the points are in order, and the track is closed, for each i in 0..n (since there are n+1 points), but when i is n, the next point is 0. So in code:

for each i in range(n+1):

   a = points[i-1] if i>0 else points[-2]  ? Hmm, not sure.

Alternatively, for each i in 0..n-1 (since points[n] is same as points[0], but the edges are from 0 to 1, 1 to 2, ..., n-1 to n. Then, the next edge after that would be n to 0 (but that's the same as 0 to 0, which is zero-length. But according to the problem statement, the track is closed, so after the last edge (n-1 to n), the next edge is not part of the straight sections (n is the number of straight sections). So the code should process only the n edges. So the turns are at points 1 to n-1 (edges 0-1, 1-2, ..., n-2-n-1), and the last turn is at points n (same as points[0]).

Wait, but the edges are 0-1 (section 0), 1-2 (section 1), ..., n-1-n (section n-1). So there are n sections. So each section is between i and i+1 for i from 0 to n-1. Then, the next edge after that is not part of the track, since the track is closed. So the turns are at points 1 to n, but points[n] is the same as points[0]. So the code must process all turns except the first point (0) and including the last point (n) which is same as 0. So how to process all turns.

So for each i from 1 to n, the turn is between the previous edge (i-1 to i) and current edge (i to i+1). But for i = n, the current edge is (n to i+1) → which is (n to 0), since i+1 is 0. So code can process each i from 0 to n, but perhaps the code will have to wrap around for i+1.

Alternatively, the code can process each i in 0 to n-1, and for each i, compute the edge i and edge i+1. But that's not exactly right.

Alternatively, for each turn at point i (i from 0 to n), the edges are the edge before (i-1 to i) and edge after (i to i+1). So for i=0, the previous edge is (n to 0), and the next edge is (0 to 1). But how do we get the previous edge for i=0?

But in the problem statement, the input is given as a list of points where the last point is the same as the first. So for example, points = [p0, p1, p2, ..., pn], where pn = p0. So for the turn at p0, which is also pn, the edges are (pn-1 to pn) and (pn to p1). So in code, for each i in 0 to n (since points have indices 0 to n):

prev_point = points[i-1] if i>0 else points[n-1]

current_point = points[i]

next_point = points[i+1] if i < n else points[1]

Wait, no. For example, when i is n (which is the same as 0), points[i] is p0. The previous edge is from pn-1 to pn (which is pn-1 to p0), and the next edge is p0 to p1. So the code needs to handle the wrap-around.

But given that the input is a closed loop, the code can process each of the n turns. Wait, but there are n straight sections and n turns? Because each straight section is followed by a turn. So there are n turns. For example, the first sample has 6 straight sections (n=6) and 6 turns. So for each i in 0 to n-1, the turn is after the i-th straight section, at point i+1. So the code should process each i from 1 to n (since the turn is at point i). But points are 0 to n, with n+1 points.

So for each turn at point i (i from 1 to n), the edges are (i-1 to i) and (i to i+1 mod (n+1)).

Wait, but since points[n] is points[0], the edge after points[n] would be points[0] to points[1]. So for the turn at points[n], which is the same as points[0], the edges are (n-1 to n) and (n to 0) → which is (n-1 to 0) and (0 to 1).

So to handle all turns, the code must process all points from 1 to n (inclusive). But points[n] is same as points[0], so the code would process the turn at points[0], which is the same as points[n].

But according to the problem statement, the southernmost point is the first point (points[0]), and the track starts there. So the code must process all turns except the first one (points[0])?

No, because the track is a loop. The first section is from points[0] to points[1], then the next section is points[1] to points[2], etc. So the first turn is at points[1], between sections 0 and 1. The last turn is at points[n], which is points[0], between sections n-1 and 0 (the loop).

So, the code needs to process all n turns (each between consecutive sections), which are located at points[1], points[2], ..., points[n] (points[0]).

So, for each i in 0 to n-1, the turn is at points[i+1]. So the code can loop i from 0 to n-1, and for each, process the turn at points[i+1].

So for each i in 0..n-1:

a = points[i]

b = points[i+1]

c = points[i+2] if i+2 <=n else points[1]

Wait, no. For example, when i =n-1, then i+1 =n, and the next edge is points[n] to points[0], but points[n] is same as points[0]. So the next edge is points[n] (0) to points[1]. So for the turn at points[i+1] (points[n] for i=n-1), the edges are (i to i+1) and (i+1 to i+2), where i+2 is (n-1 +1 +1) =n+1, which is out of bounds. So in code, after points[i+1], the next point is (i+2) mod (n+1). But since the points are given as a list of n+1 elements (including the duplicate), when i+1 is n (points[n] is points[0]), then the next point is points[0+1] = points[1]. So the code needs to handle this wrap-around.

So for each turn at points[i+1], the edges are (points[i], points[i+1]) and (points[i+1], points[(i+2) % (n+1)]).

But in the given input, the points list is [p0, p1, p2, ..., pn], where pn = p0. So the next point after pn is p0, but then after p0 is p1.

So for i in 0..n-1:

current turn is at points[i+1].

previous edge: from points[i] to points[i+1].

next edge: from points[i+1] to points[i+2], if i+2 < n+1. But for i+1 =n-1, i+2 is n, which is p0. So for i+1 =n-1 (i =n-2), the next edge is from pn-1 to pn (p0) to p1.

Wait, no. Let's clarify:

For example, when i is n-1 (the last index in the edges), then the edges are points[i] (pn-1) to points[i+1] (pn = p0), and then the next edge is p0 to points[1], which is points[0] to points[1]. So the code must handle this case.

So for each i from 0 to n-1:

current turn point is points[i+1].

previous edge vector is points[i+1] - points[i].

next edge vector is points[i+2] - points[i+1], if i+2 <=n. Otherwise, if i+1 ==n, then next edge is points[0] to points[1] (vector is points[1] - points[0]).

Wait, but points[n] is same as points[0]. So when i is n-1:

points[i] is points[n-1].

points[i+1] is points[n] = points[0].

The next edge is points[0] to points[1].

So the next edge vector is points[1] - points[0].

So in code, for each i in 0 to n-1:

prev_point = points[i]

current_point = points[i+1]

next_point = points[i+2] if (i+2) <=n else points[1]

But wait, when i+1 is n-1:

i =n-2 → i+1 =n-1.

Then, next_point is points[i+2] = points[n], which is points[0]. So the next edge is from points[i+1] (n-1) to points[i+2] (n, which is 0). So the next edge vector is (0) - points[n-1]?

No. Because for i =n-1:

prev_point is points[n-1], current_point is points[n] (0). The next edge is points[0] (current_point) to points[1]. So next_point is points[1].

Wait, this is getting complicated. So perhaps the code can handle the next_point as follows:

for each i in 0 to n-1:

   a = points[i]

   b = points[i+1]

   if i+1 == n:  # current_point is the last point (same as first)

       c = points[1]

   else:

       c = points[i+2] if i+2 < len(points) else points[0]

   # Compute vectors ab and bc.

   ab = (b[0] - a[0], b[1] - a[1])

   bc = (c[0] - b[0], c[1] - b[1])

   cross = ab[0] * bc[1] - ab[1] * bc[0]

But wait, in this case, for i =n-1:

a is points[n-1]

b is points[n] (points[0])

c is points[1]

So the next edge is from b (points[0]) to c (points[1]).

So the code would correctly compute the vectors ab (points[n] - points[n-1]) and bc (points[1] - points[0]).

Yes. So this approach should work.

So in code:

n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n+1)]

sum_area = 0

for i in range(n):

    x_i, y_i = points[i]

    x_next, y_next = points[i+1]

    sum_area += x_i * y_next - x_next * y_i

orientation = 1 if sum_area > 0 else -1  # 1 for CCW, -1 for CW

count = 0

for i in range(n):

    a = points[i]

    b = points[i+1]

    if i+1 == n:

        c = points[1]

    else:

        c = points[i+2] if (i+2) < len(points) else points[0]

    # Compute vectors ab and bc

    ab = (b[0] - a[0], b[1] - a[1])

    bc = (c[0] - b[0], c[1] - b[1])

    cross = ab[0] * bc[1] - ab[1] * bc[0]

    # Check if cross product indicates a concave turn based on orientation

    if (orientation == 1 and cross < 0) or (orientation == -1 and cross > 0):

        count += 1

print(count)

Let's test this code with the first sample.

Sample 1 input:

6

0 0

0 1

1 1

1 2

2 2

2 0

0 0

sum_area calculation:

i=0: 0*1 -0*0=0.

i=1:0*1 -1*1= -1.

i=2:1*2 -1*1=1.

i=3:1*2 -2*2= 2-4= -2.

i=4:2*0 -2*2=0-4= -4.

i=5:2*0 -0*0=0.

sum_area is 0 -1 +1 -2 -4 +0 = -6. sum_area is -6 → orientation is -1 (clockwise).

Processing each i from 0 to 5 (n=6).

For i=0:

a = (0,0), b = (0,1). i+1 is 1 <6, so c is points[2] (1,1).

ab = (0,1) - (0,0) → (0,1).

bc = (1,1) - (0,1) → (1,0).

cross = 0*0 -1*1 = -1.

orientation is -1 (CW). So cross is -1 <0. So (orientation is -1 and cross >0) → false. So no count.

i=1:

a=(0,1), b=(1,1). c=(1,2).

ab=(1,0), bc=(0,1). cross is 1*1 -0*0=1>0. So orientation is -1, cross >0 → count +=1. So count becomes 1.

i=2:

a=(1,1), b=(1,2). c= points[3+1] = points[4] (2,2).

ab is (0,1), bc is (1,0). cross 0*0 -1*1 = -1. cross <0. orientation is -1 → cross>0 is false. So no count.

i=3:

a=(1,2), b=(2,2). c= points[5] (2,0).

ab=(1,0), bc=(0,-2). cross 1*(-2) -0*0 = -2. orientation -1 → cross>0 is false. no count.

i=4:

a=(2,2), b=(2,0). c= points[5+1] = points[6] (0,0).

ab=(0,-2), bc= (0-2, 0-0) → (-2,0). cross is 0*0 - (-2)*(-2) → 0 -4= -4. orientation is -1 → cross>0 false. no count.

i=5:

a=(2,0), b=(0,0). since i+1=6 (n=6), so c=points[1] (0,1).

ab= (0-2, 0-0) → (-2,0).

bc= (0,1-0) → (0,1).

cross = (-2)*1 -0*0 = -2. orientation is -1 → cross>0 is false. no count.

Total count is 1. Correct.

Sample 2 input:

16

1 1

1 5

3 5

3 7

2 7

2 9

6 9

6 7

5 7

5 3

4 3

4 4

3 4

3 2

5 2

5 1

1 1

The code should output 6. But I won't check all here, but the code should compute sum_area, determine orientation, then check each turn.

So the code should be correct.
</think>

```python
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n + 1)]

sum_area = 0
for i in range(n):
    x_i, y_i = points[i]
    x_next, y_next = points[i+1]
    sum_area += x_i * y_next - x_next * y_i

orientation = 1 if sum_area > 0 else -1

count = 0
for i in range(n):
    a = points[i]
    b = points[i+1]
    if i+1 == n:
        c = points[1]
    else:
        c = points[i+2] if (i+2) < len(points) else points[0]
    ab_x = b[0] - a[0]
    ab_y = b[1] - a[1]
    bc_x = c[0] - b[0]
    bc_y = c[1] - b[1]
    cross = ab_x * bc_y - ab_y * bc_x
    if (orientation == 1 and cross < 0) or (orientation == -1 and cross > 0):
        count += 1

print(count)
```