<think>
Okay, I need to solve this problem where I have to find the number of integer points on the fence AB (the first two points of the polygon) such that every point inside the polygon is visible from that watchtower. The visibility is such that the line of sight doesn't cross the edges of the polygon anywhere between the tower and the criminal.

First, let's understand the problem. The polygon is given in clockwise order, with the first two points being A and B, which form a horizontal fence (since AB is parallel to the x-axis). The watchtower can be placed at any integer point along AB. For each such point, we need to check if all points in the polygon are visible from it. The answer is the count of such valid points.

Hmm. Wait, no. Wait the problem says "all the criminals can be watched from there". So, the criminals are inside the polygon, and the watchtower must be placed on AB. So for each candidate point on AB, every point in the polygon must be visible from it. Because if any point in the polygon is not visible, then that's a criminal who isn't watched, so the tower can't be placed there.

Wait, but the polygon is the compound. So the criminals are inside the polygon. Wait, maybe I'm misunderstanding. The problem says that the land plot is a polygon, and the criminals are kept inside. So the watchtower must be placed on AB, and from there, every point inside (or on the boundary) of the polygon must be visible. Because otherwise, some criminals (in the parts not visible) could escape.

So the problem reduces to: find all integer points on AB such that for each such point P, every point Q in the polygon is visible from P. That is, the line segment PQ does not cross any edge of the polygon (except possibly at the endpoints).

Wait, no. The problem states that the line of visibility from the tower to the criminal (Q) must not cross the plot edges between them. So PQ must lie entirely inside the polygon. Or, perhaps, the line PQ must not exit the polygon between P and Q. So for any Q in the polygon, the line from P to Q must be entirely contained within the polygon. Or maybe, the line PQ must not intersect any edges except at P or Q.

But the exact condition here is a bit tricky. Let me re-read the problem statement.

"A criminal is watchable from the watchtower if the line of visibility from the watchtower to him doesn't cross the plot-edges at any point between him and the tower i.e. as shown in figure 1 below, points X, Y, C and A are visible from point B but the points E and D are not."

So the line from the tower to the criminal must not cross any edges of the polygon except possibly at their endpoints. So for the line PQ (P is the tower, Q is a criminal), there should be no point on the line between P and Q (exclusive) that lies on any edge of the polygon.

So the visibility condition is that the line segment between P and Q is entirely contained within the polygon. Because if any edge is crossed in between, then the line goes outside, which would block visibility.

Wait, but the polygon is a simple polygon (no self-intersections). So the line PQ must lie entirely within the polygon for all Q in the polygon. But how to check that?

Alternatively, the line segment PQ must not intersect any edges of the polygon except at P and Q themselves. Because if it does, then the visibility is blocked.

But how do I model this for all Q in the polygon?

Wait, but the problem says that all criminals (i.e., all points in the polygon) must be visible from P. So for a given P on AB, every point in the polygon must be visible from P. So the tower's visibility region must cover the entire polygon.

This seems computationally intensive. Because for each candidate P, we need to check that all points in the polygon are visible from P. But the polygon can be up to 1000 vertices, so iterating over all points is impossible.

So we need a smarter approach.

I recall that in visibility problems, the visibility polygon can be computed. The visibility polygon from a point P is the set of all points in the polygon visible from P. If the entire polygon is the visibility polygon for P, then P is a valid point. So the problem is equivalent to finding all points P on AB such that the visibility polygon of P is the entire polygon.

But how to compute this efficiently?

Alternatively, perhaps the problem can be reduced to checking that P can see all the vertices of the polygon. Because if all the vertices are visible from P, then all edges (and hence all points) are visible. But wait, that's not necessarily true. For example, imagine a polygon with a vertex that's visible, but there's an edge that's hidden between two vertices. However, in a simple polygon, maybe if all edges are visible, then the entire polygon is visible. Hmm, perhaps not. But perhaps in the problem's conditions, checking all vertices is sufficient.

Alternatively, maybe for the entire polygon to be visible from P, every edge of the polygon must be visible from P, which can be determined by checking that each edge is entirely in the visibility polygon. But again, how?

Alternatively, perhaps the polygon's edges (other than AB) form a set of walls that could block visibility. So for P to see the entire polygon, all edges of the polygon must lie on the same side of P's line of sight. Wait, not sure.

Wait, AB is part of the polygon. The polygon is given in clockwise order, starting with A and B. The problem states that all other corners lie on the same side of AB. So the polygon is a simple polygon with AB as a horizontal edge, and the rest of the polygon is on one side of AB. So the polygon is a closed shape, where AB is part of the boundary, and the rest of the polygon is on one side of AB.

So when the tower is placed on AB, the visibility is such that any line from the tower must not exit the polygon. For the entire polygon to be visible from P, any line from P to any point in the polygon must not exit the polygon.

Alternatively, since the polygon is on one side of AB (except for AB itself), perhaps the entire polygon is visible from P if and only if the polygon is convex and P is such that all edges are visible. But I'm not sure.

Another approach: For a point P on AB, the visibility is blocked if there exists an edge of the polygon (other than AB) such that the edge blocks some part of the polygon from P. So for each edge, we need to check whether it blocks any point in the polygon from P. If any edge does, then P is invalid.

Alternatively, for P to be a valid watchtower point, every edge of the polygon (other than AB) must be completely visible from P. Wait, maybe. Because if an edge is not visible from P, then there's a point on that edge (hence in the polygon) that is not visible, which would invalidate P.

So the problem reduces to: for each candidate P on AB, check that every edge of the polygon (other than AB) is completely visible from P. That is, for each edge E (not AB), all points on E are visible from P.

But how do we check that?

Alternatively, for each edge E (other than AB), the edge E is a line segment. For P to see all points on E, the line segment from P to any point on E must lie within the polygon. But how can we check this?

Alternatively, perhaps for an edge E to be completely visible from P, the edge E must lie in the same half-plane relative to P as determined by some condition.

Alternatively, the edge E must not be intersected by any other edges when viewed from P. Hmm, not sure.

Wait, perhaps for all edges E (other than AB), the entire edge E must lie in the same visible region from P. So, for example, for each such E, when viewed from P, E must not be occluded by any other edges.

But considering the polygon is given in clockwise order, and that the other edges are on the same side of AB, perhaps there's a way to model this.

Another angle: The polygon is such that all other edges (apart from AB) are on one side of AB. Let's say AB is a horizontal line. The polygon is a closed shape with AB as the top edge (assuming all other points are below AB). Then, the watchtower is placed on AB. For a point P on AB, to see the entire polygon, all edges must lie in the same visible region as seen from P.

Wait, perhaps the polygon is star-shaped with respect to the segment AB. For a polygon to be star-shaped with respect to a point P, there exists a point P such that all points in the polygon are visible from P. But here, the watchtower can be placed anywhere along AB, and the entire polygon must be visible from that point.

So the problem is to find all points P on AB (integer points) such that the polygon is star-shaped with respect to P. The kernel of the polygon (the set of all points from which the entire polygon is visible) must intersect AB at those integer points.

So, how to compute the kernel's intersection with AB?

The kernel of a polygon is the set of points from which the entire polygon is visible. For a polygon to have a non-empty kernel, it must be a star-shaped polygon. The kernel is the intersection of all the half-planes defined by the polygon's edges.

Each edge of the polygon defines a half-plane. The kernel is the intersection of these half-planes.

So, the kernel is the set of all points P such that for every edge of the polygon, P lies in the interior or on the edge's corresponding half-plane.

In our case, the fence AB is part of the polygon. So, the kernel must lie in the intersection of all the half-planes defined by each edge.

So for each edge (except AB), the half-plane that includes the polygon's interior. So, for each edge (say, BC), which is part of the polygon's boundary (since the polygon is given in clockwise order), the half-plane to the left of BC (as the edges are traversed in clockwise order) is the interior of the polygon.

Thus, the kernel is the intersection of all these half-planes. The points on AB that are in this intersection are the valid points for the watchtower.

Therefore, the problem reduces to computing the intersection of all the half-planes defined by the edges of the polygon (excluding AB), and then finding the integer points on AB that lie within this intersection.

Wait, but how do we model the half-planes for the edges?

Each edge of the polygon (except AB) is part of the boundary. The half-plane for edge BC (from B to C) is the set of points that are on the interior side of the edge. Since the polygon is given in clockwise order, the interior is to the right of the edge as we move from B to C. So, for each edge BC, the half-plane is the area that is on the left side when looking from B to C. Wait, maybe I need to think about the direction.

In a clockwise polygon, the interior is to the right of each edge as you traverse them in order. For example, if you have a polygon with vertices A, B, C, D, A, and you move from A to B to C, etc., then the interior is on the right side. So for edge BC, the interior is on the right side of the edge BC. So the half-plane defined by edge BC would be the set of points that are on the interior side, i.e., the right side of the edge BC.

So, the kernel is the set of points that lie in the intersection of all these right half-planes for each edge. So, for each edge (other than AB), compute the half-plane (the right side of the edge), and the kernel is the intersection of all these.

Thus, the valid points on AB are those that lie in the intersection of all these half-planes.

So the problem is now: compute the intersection of all half-planes defined by the edges (excluding AB) and find the integer points on AB that lie within this intersection.

So, the steps to solve the problem would be:

1. For each edge of the polygon (excluding AB), compute the half-plane that represents the interior (right side) of that edge.

2. Compute the intersection of all these half-planes. The intersection is a convex region (since each half-plane is convex, and the intersection of convex regions is convex). The kernel is this intersection.

3. Find the interval (or intervals) on the fence AB where the kernel intersects AB.

4. Count the integer points in that interval.

So, the key is to model each edge's half-plane, compute their intersection, and find the overlap with AB.

Now, AB is a horizontal line segment. Let's model AB as a line from (x1, y1) to (x2, y2). Since AB is parallel to the x-axis, y1 must equal y2. Let's call this y-coordinate y_ab.

The integer points on AB are those with y = y_ab and x between min(x1, x2) and max(x1, x2), inclusive. But since the points are given in order, perhaps AB is from A (x1, y1) to B (x2, y2), and since the polygon is given in clockwise order, the direction of AB is part of the polygon's traversal.

But for the purposes of the fence AB, the line is horizontal, so all points on AB between A and B (inclusive) are the fence. So the fence AB is the line segment between A and B, and the integer points on AB are the ones with y = y_ab and x varying between the min and max of x1 and x2, stepping by 1.

Wait, but the problem statement says that the fence AB is a straight line with points where the watchtower can be set up. So the watchtower can be placed at any integer coordinate along the line AB, but since AB is a line segment, the integer points are those on the line AB between A and B (inclusive), with integer x and y.

But since AB is horizontal, y1 = y2. So all points on AB have y = y1. The x values are between x1 and x2 (assuming AB is from left to right). Wait, but AB could be from right to left. So for example, if A is (8,8) and B is (4,8), then AB is a line segment from x=8 to x=4. So the integer points on AB would be (8,8), (7,8), ..., (4,8).

So first, the code must generate all integer x between x1 and x2 (inclusive) along y=y1, but that's only if x1 and x2 are integers. But according to the input constraints, the coordinates can be up to 1e6, but the problem says that the watchtower can be placed on the integer points along AB. So AB's endpoints may not be integer coordinates. Wait, but the input gives the vertices as integers. Wait, looking back at the problem statement:

In the input format, each of the next n lines contains xi and yi (0 ≤ xi, yi ≤ 1e6), separated by a space. So the vertices have integer coordinates. So the fence AB is a line segment between two integer points, and AB is parallel to the x-axis. Therefore, all points on AB have the same y-coordinate (since it's horizontal), and the x-coordinates vary between x1 and x2. Since AB is a line segment between two integer points, and it's horizontal, the integer points on AB are all (x, y) where y = y1 (which is the same as y2), and x ranges from min(x1, x2) to max(x1, x2), inclusive. So for example, if AB is from (4,8) to (8,8), then the integer points are (4,8), (5,8), ..., (8,8), which are 5 points. If AB is from (8,8) to (4,8), then same 5 points.

So the first step is to collect all the integer x coordinates along AB, then for each x, check if (x, y_ab) is in the intersection of all half-planes defined by the edges (excluding AB).

Now, the edges of the polygon are given in order. The first edge is AB. The next edges are BC, CD, etc., up to the nth edge, which connects the last vertex back to A.

But since the first two points are A and B, the edges are AB, BC, CD, ..., NA. The edges other than AB are those that form the rest of the polygon. For each of these edges, we need to compute the half-plane (the right side of the edge, as the polygon is given in clockwise order), and check whether the candidate point (x, y_ab) lies in all these half-planes.

If a candidate point lies in all such half-planes, then it is in the kernel, and thus can see the entire polygon.

So, the algorithm becomes:

For each edge (other than AB) in the polygon:

   compute the equation of the line (ax + by + c = 0) that represents the edge.

   the half-plane is the set of points (x, y) such that ax + by + c >= 0 (since the interior is to the right of the edge in a clockwise polygon).

Then, for a candidate point P (x_p, y_ab) on AB, check for each edge (other than AB) whether the point P lies in the corresponding half-plane.

If P is in all half-planes, then it's a valid watchtower point.

So the problem reduces to, for each integer x_p on AB, check if for all edges (non-AB), the point (x_p, y_ab) lies in the correct half-plane.

Thus, the code can proceed as follows:

1. Read n, then the n vertices in order.

2. Determine AB (the first two points). Check that AB is horizontal (y1 == y2). Since the problem states that AB is parallel to the x-axis, this should be the case.

3. Collect all edges except AB. For each such edge (u, v), compute the line equation, and the inequality that represents the interior half-plane.

4. For each integer x_p on AB (from x_min to x_max, inclusive), create the point (x_p, y_ab), and check if this point satisfies all the half-plane inequalities.

5. Count the number of such points that satisfy all inequalities.

So the key steps are:

- generating all the integer x_p on AB.

- for each edge (non-AB), compute the inequality and check if (x_p, y_ab) satisfies it.

But how to compute the inequality for each edge?

Let's take an edge from point u (x_u, y_u) to point v (x_v, y_v), in the order of the polygon's traversal (which is clockwise). The interior of the polygon is to the right of the edge. So, for the edge uv, the half-plane is the set of points (x, y) such that the cross product (v - u) × (p - u) ≥ 0, where p is (x, y).

Alternatively, the equation of the line can be found as follows:

The line through u and v can be represented in the form ax + by + c = 0.

The direction of the inequality depends on which side is the interior.

For a clockwise polygon, the interior is on the right side of the edge. So, when moving from u to v, the interior is to the right.

The cross product approach can be used. For a point p, the cross product (v - u) × (p - u) gives the direction. If it's positive, the point is to the left of the edge; if negative, to the right. But since the polygon is clockwise, the interior is to the right. So the inequality for the edge uv is (v.x - u.x)*(p.y - u.y) - (v.y - u.y)*(p.x - u.x) <= 0.

Wait, let's think. The cross product (v - u) × (p - u) is (vx - ux)(py - uy) - (vy - uy)(px - ux). For the edge uv, in a clockwise polygon, the interior is on the right side of the edge. So, points inside the polygon are on the right side.

The cross product of (v - u) and (p - u) gives the direction. If the cross product is positive, p is to the left of the edge uv; if negative, to the right.

But since the polygon is clockwise, the interior is to the right. So for the edge uv, the half-plane is the set of points p where (v.x - u.x)*(p.y - u.y) - (v.y - u.y)*(p.x - u.x) <= 0. Because that's when p is on the right side.

So for each edge uv (other than AB), we can compute the inequality (a*x + b*y + c) <= 0, where a = (v.y - u.y), b = -(v.x - u.x), and c = u.x*(v.y - u.y) - u.y*(v.x - u.x). Wait, let's see:

The cross product can be written as (v.x - u.x)(p.y - u.y) - (v.y - u.y)(p.x - u.x) = (v.x - u.x)(y - u.y) - (v.y - u.y)(x - u.x).

We can rearrange this as (v.x - u.x) * y - (v.x - u.x) * u.y - (v.y - u.y) * x + (v.y - u.y) * u.x.

Which can be rewritten as (- (v.y - u.y)) * x + (v.x - u.x) * y + [ (v.x - u.x) * (-u.y) + (v.y - u.y) * u.x ].

So the equation becomes (- (v.y - u.y)) * x + (v.x - u.x) * y + ( - (v.x - u.x) u.y + (v.y - u.y) u.x ) = 0.

Which simplifies to (u.y - v.y) x + (v.x - u.x) y + (u.x v.y - v.x u.y) ) = 0.

So the line equation is (u.y - v.y) x + (v.x - u.x) y + (u.x v.y - v.x u.y) ) = 0.

The cross product is (v.x - u.x)(y - u.y) - (v.y - u.y)(x - u.x). For points in the interior (right side), this cross product is <= 0.

So for each edge uv (non-AB), the inequality is (v.x - u.x) * (y_p - u.y) - (v.y - u.y) * (x_p - u.x) <= 0.

But the candidate points are all on AB, which is horizontal. So y_p is fixed as y_ab (y1, which is the same as y2 of AB). So for each candidate point (x_p, y_ab), we can compute for each edge uv (non-AB) whether (v.x - u.x) * (y_ab - u.y) - (v.y - u.y) * (x_p - u.x) <= 0.

If this is true for all edges, then the point is valid.

So, the steps are:

- For each edge in the polygon, except AB, compute the coefficients of the inequality.

But since all candidate points have y = y_ab, we can substitute that into the inequality and get an inequality in x_p.

So for each edge uv (non-AB):

   compute A = (v.x - u.x) * (y_ab - u.y) - (v.y - u.y) * (x_p - u.x) <= 0.

But substituting x_p is the variable here. So for each edge, we can compute the inequality as a linear function of x_p.

For example:

Let's expand A:

A = (v.x - u.x) * (y_ab - u.y) - (v.y - u.y) * (x_p - u.x)

= [ (v.x - u.x)(y_ab - u.y) + (v.y - u.y) u.x ] - (v.y - u.y) x_p

So the inequality becomes:

[ (v.x - u.x)(y_ab - u.y) + (v.y - u.y) u.x ] - (v.y - u.y) x_p <= 0

Which can be rearranged as:

- (v.y - u.y) x_p + [ (v.x - u.x)(y_ab - u.y) + (v.y - u.y) u.x ] <= 0

Multiply both sides by -1 (which reverses the inequality if (v.y - u.y) is positive or negative. So this step could complicate things. Alternatively, let's write it as:

Coefficient * x_p <= Constant.

Let's compute:

The inequality is:

A = (v.x - u.x)(y_ab - u.y) - (v.y - u.y)(x_p - u.x) <= 0.

Expand:

A = (v.x - u.x)(y_ab - u.y) - (v.y - u.y) x_p + (v.y - u.y) u.x <=0.

Rearranged:

- (v.y - u.y) x_p + [ (v.x - u.x)(y_ab - u.y) + (v.y - u.y) u.x ] <= 0.

Let's call:

coeff = -(v.y - u.y)

const_term = (v.x - u.x)*(y_ab - u.y) + (v.y - u.y)*u.x

So the inequality becomes:

coeff * x_p + const_term <= 0.

But this depends on the edge uv.

For each edge, we can compute coeff and const_term. Then, the inequality for x_p is:

coeff * x_p + const_term <= 0.

But depending on the sign of coeff, this can be rewritten as x_p >= ( - const_term ) / coeff (if coeff is positive) or x_p <= ( - const_term ) / coeff (if coeff is negative).

Wait, solving for x_p:

coeff * x_p <= -const_term

So if coeff is positive:

x_p <= (-const_term)/coeff

If coeff is negative (since multiplying both sides by 1/coeff which is negative reverses the inequality):

x_p >= (-const_term)/coeff

But each edge defines a constraint on x_p. The valid x_p values must satisfy all such constraints.

So, for each edge, we can compute a lower bound or upper bound on x_p. Then, the intersection of all these bounds gives the range of x_p values that are valid.

So for all edges, we compute the constraint on x_p and combine them.

The final valid x_p is the intersection of all the intervals determined by these constraints.

So, for example, some edges may impose a lower bound (x >= a), others may impose an upper bound (x <= b). The overall valid interval is the intersection of all these.

Thus, the steps are:

1. For each edge (non-AB):

   compute coeff and const_term.

   Then, compute the inequality in terms of x_p.

   Depending on coeff, derive the inequality as:

   if coeff > 0:

      x_p <= (-const_term) / coeff

   else if coeff < 0:

      x_p >= (-const_term) / coeff

   else (coeff == 0):

      if the inequality is const_term <=0 → either always true or false.

      if coeff is zero, then the term is (0)*x_p + const_term <=0 → const_term <=0.

      So if const_term >0, the inequality is false → no solution.

      So for coeff ==0, the edge's constraint is either invalid (the point (x_p, y_ab) is not in the half-plane, so the entire AB is invalid) or the constraint is always satisfied (so no effect on the interval).

2. For all edges, compute the inequalities and collect the lower and upper bounds.

3. Find the maximum of all lower bounds and the minimum of all upper bounds. The valid x_p must be in [max_lower, min_upper], and also within the x range of AB.

If the max_lower > min_upper, then there's no solution.

Additionally, any edge with coeff =0 and const_term >0 makes the entire AB invalid.

So, the steps in code:

Initialize lower = -infinity, upper = +infinity.

For each edge (u, v) in the polygon (excluding AB):

   u = (u_x, u_y), v = (v_x, v_y)

   coeff = -(v_y - u_y)  # because coeff = -(v.y - u.y)

   const_term = (v.x - u.x) * (y_ab - u.y) + (v.y - u.y) * u.x 

   # since (v.x - u.x) * (y_ab - u.y) is (v.x -u.x) multiplied by (y_p - u.y), which is (y_ab - u.y) here.

   # (v.y - u.y) * u.x → part of the const_term.

   # the original inequality: coeff * x_p + const_term <=0 → which is equivalent to (v.x - u.x)*(y_ab - u.y) - (v.y - u.y)*(x_p - u.x) <=0.

   # So coeff is -(v.y - u.y)

   if coeff == 0:

       # Then the inequality is 0 * x_p + const_term <=0 → const_term <=0.

       if const_term > 0:

           # This edge's constraint is impossible. So no points on AB are valid.

           So the entire AB is invalid. So lower = infinity, upper = -infinity. break.

       else:

           # const_term <=0 → no constraint on x_p. So skip this edge.

           continue

   else:

       # Solve coeff * x_p <= -const_term.

       rhs = (-const_term) / coeff

       if coeff >0:

           # x_p <= rhs → upper bound.

           upper = min(upper, rhs)

       else:

           # coeff <0: x_p >= rhs → lower bound.

           lower = max(lower, rhs)

   # Also, during processing, check if upper < lower → no solution.

   if lower > upper:

       break

After processing all edges, also consider the original AB's x range. The x_p must be between x_min and x_max, inclusive, where x_min = min(A.x, B.x), x_max = max(A.x, B.x).

So the final valid interval is the intersection of [x_min, x_max] and [lower, upper].

Thus:

x_start = max( lower, x_min )

x_end = min( upper, x_max )

if x_start > x_end → no points.

Otherwise, the integer points are all x in [x_start, x_end], inclusive.

But x_start and x_end can be real numbers. We need to find the integer x in the range [ceil(x_start), floor(x_end)].

Wait, but x_p must be integers. So the valid x_p are those integers x where x >= x_start and x <= x_end.

But x_start and x_end may not be integers. So the integer x_p must satisfy x_start <= x_p <= x_end.

So for example, if x_start is 3.2, then the minimum x_p is 4. If x_end is 5.8, then the maximum x_p is 5. So the valid integers are 4 and 5.

But how to compute this?

The code can compute the floor and ceiling as follows:

x_start_ceil = math.ceil( x_start )

x_end_floor = math.floor( x_end )

count = max( 0, x_end_floor - x_start_ceil + 1 )

But need to handle edge cases where x_start is integer, etc.

So the steps are:

After computing x_start and x_end:

if x_start > x_end → count is 0.

else:

   x_start_ceil = ceil( x_start )

   x_end_floor = floor( x_end )

   if x_start_ceil > x_end_floor → 0.

   else → x_end_floor - x_start_ceil + 1.

But also, need to make sure that x_start_ceil is <= x_end_floor.

So, the code can proceed with that.

But we need to compute x_start and x_end as:

x_start = max( lower, x_min )

x_end = min( upper, x_max )

But what about the edges that may have introduced coeff ==0 and const_term >0? For those edges, during processing, if any such edge is found, the code would set lower = inf and upper = -inf, leading to x_start > x_end, hence count 0.

So the code must handle all cases.

Now, the code steps:

Read n.

Read n points, stored in a list.

A is the first point, B is the second. Check that A.y == B.y (since AB is horizontal).

Compute x_min = min(A.x, B.x), x_max = max(A.x, B.x)

y_ab = A.y.

For each edge in the polygon, except the first (AB):

   The edges are from points[i] to points[i+1], for i from 1 to n-2 (since the first edge is AB, which is points[0] to points[1]). Then the last edge is points[-1] to points[0].

Wait, the polygon is given in clockwise order as per the input. So the edges are:

Edge 0: points[0] → points[1] (AB)

Edge 1: points[1] → points[2]

Edge 2: points[2] → points[3]

...

Edge n-1: points[n-1] → points[0]

So edges 0 is AB, edges 1 to n-1 are the other edges.

So, for all edges except edge 0 (AB), we need to process them.

So, in code:

edges = list of all edges except edge 0.

For each edge in edges:

   u = points[i], v = points[j], where i and j are consecutive indices (mod n).

But since the edges are from the list of vertices in order, the code can loop from i in 1 to n-1:

Wait, vertices are 0-based. So:

edges to process are:

for i in 1 to n-1: edge is (points[i], points[i+1]) if i < n-1, else (points[n-1], points[0]).

But since the first edge is points[0] to points[1] (AB), the edges to process are:

- points[1] to points[2]

- points[2] to points[3]

...

- points[n-1] to points[0]

But points[n-1] to points[0] is the edge closing the polygon.

So, the code can loop over all edges except the first (AB). So for each edge in the list of edges starting from index 1 (since edge 0 is AB):

Wait, in code:

vertices = list of points (each is a tuple (x, y)).

edges = [ (vertices[i], vertices[(i+1) % n]) for i in range(1, n) ]

So edges are:

i=1 → (v1, v2)

i=2 → (v2, v3)

...

i =n-1 → (v_{n-1}, v0).

But wait, for i from 1 to n-1:

the edges are (v1, v2), (v2, v3), ..., (v_{n-1}, v0). Yes.

So for each of these edges (u, v), compute the inequality.

Now, for each edge (u, v):

u_x, u_y = u

v_x, v_y = v

coeff = -(v_y - u_y)  # because coeff is -(v.y - u.y)

const_term = (v_x - u_x) * (y_ab - u_y) + (v_y - u_y) * u_x

So the inequality is coeff * x_p + const_term <= 0.

Then:

if coeff is 0:

   if const_term > 0 → invalid → no possible points. So set lower and upper to break.

else → no constraint.

else:

   rhs = (-const_term) / coeff

   if coeff >0 → x_p <= rhs → upper = min(upper, rhs)

   else → x_p >= rhs → lower = max(lower, rhs)

But all variables are in integers, but rhs could be a float.

But wait, in the problem statement, the coordinates are integers, but the edges may have arbitrary slopes.

So, the code must handle this with floating points.

Once all edges are processed, the code computes x_start = max(lower, x_min), x_end = min(upper, x_max).

Then, the valid x_p are integers between x_start and x_end, inclusive.

Now, code steps:

Read the input:

n = int(input())

vertices = [tuple(map(int, input().split())) for _ in range(n)]

A = vertices[0]

B = vertices[1]

y_ab = A[1]

x_min = min(A[0], B[0])

x_max = max(A[0], B[0])

lower = -infinity (start with the minimal possible lower bound)

upper = infinity (start with the maximal possible upper bound)

But in Python, we can represent lower as -inf and upper as inf.

edges = list of all edges except AB.

Then, process each edge:

for each u, v in edges:

   compute coeff and const_term.

   if coeff is 0:

      if const_term >0 → no solution. So set lower = inf, upper = -inf. break loop.

      else → continue.

   else:

      rhs = (-const_term) / coeff

      if coeff >0:

          upper = min(upper, rhs)

      else:

          lower = max(lower, rhs)

      if lower > upper:

          break

After processing all edges:

Then, x_start = max(lower, x_min)

x_end = min(upper, x_max)

if x_start > x_end → 0.

else:

   compute the number of integer x_p in [x_start, x_end]

But how?

For example, x_start is 4.2 → ceil is 5.

x_end is 8.8 → floor is 8.

So the integers are 5, 6, 7, 8 → 4 numbers.

But how to calculate this in code.

The formula is:

x_start_ceil = math.ceil(x_start)

x_end_floor = math.floor(x_end)

if x_start_ceil > x_end_floor → 0.

else → x_end_floor - x_start_ceil + 1.

But all in integers.

So, code:

import math

...

x_start = max(lower, x_min)

x_end = min(upper, x_max)

if x_start > x_end:

    print(0)

else:

    x_start_ceil = math.ceil(x_start)

    x_end_floor = math.floor(x_end)

    if x_start_ceil > x_end_floor:

        print(0)

    else:

        print(x_end_floor - x_start_ceil + 1)

But wait, x_start and x_end can be integers. For example, x_start = 4, x_end =8 → ceil(4) is 4, floor(8) is 8 → 8-4+1 =5.

Which is correct.

So this formula works.

Now, let's test this approach against the examples.

First example:

Input:

5

4 8

8 8

9 4

4 0

0 4

AB is from (4,8) to (8,8). So x_min=4, x_max=8.

y_ab =8.

Other edges are:

B (8,8) → C (9,4)

C → D (4,0)

D → E (0,4)

E → A (4,8)

Wait, the vertices are in order: A(4,8), B(8,8), C(9,4), D(4,0), E(0,4). So edges:

B→C (8,8→9,4)

C→D (9,4→4,0)

D→E (4,0→0,4)

E→A (0,4→4,8)

A→B is the first edge, which is excluded.

So the edges to process are B→C, C→D, D→E, E→A.

For each edge, compute the constraint.

Let's process each edge:

Edge B→C (u=(8,8), v=(9,4)).

coeff = -(4-8) =4.

const_term = (9-8)*(8-8) + (4-8)*8 = (1 * 0) + (-4)*8 = -32.

Inequality: 4 * x_p -32 <=0 → x_p <= 8.

So upper is min(inf, 8) → 8.

lower remains -inf.

Next edge C→D (9,4) → (4,0):

coeff = -(0-4) =4.

const_term = (4-9)*(8-4) + (0-4)*9 → (-5)*4 + (-4)*9 → (-20) + (-36) = -56.

Inequality:4x_p -56 <=0 → x_p <=14. So upper is min(8, 14) →8.

Lower remains -inf.

Next edge D→E (4,0) → (0,4):

coeff = -(4-0) =-4.

const_term = (0-4)*(8-0) + (4-0)*4 → (-4)*8 +4*4 →-32+16= -16.

Inequality: -4x_p -16 <=0 → -4x_p <=16 →x_p >=-4.

So lower is max(-inf, -4) →-4.

Now, upper is8, lower is-4. So x_p must be >=-4 and <=8.

Next edge E→A (0,4)→(4,8):

coeff = -(8-4) =-4.

const_term = (4-0)*(8-4) + (8-4)*0 →4*4 +4*0 →16+0=16.

Inequality: -4x_p +16 <=0 →-4x_p <=-16 →x_p >=4.

So lower is max(-4,4) →4.

Now, upper is8, lower is4.

So after processing all edges, x_start is max(4,4) →4.

x_end is min(8,8) →8.

The integer points are 4,5,6,7,8 →5 points. Which matches the first example.

Second example:

Input:

5

4 8

5 8

5 4

7 4

2 2

AB is from (4,8) to (5,8). x_min=4, x_max=5. y_ab=8.

Other edges:

B(5,8) →C(5,4)

C(5,4) →D(7,4)

D(7,4) →E(2,2)

E(2,2) →A(4,8)

Process each edge:

Edge B→C (5,8→5,4):

coeff = -(4-8) =4.

const_term = (5-5)*(8-8) + (4-8)*5 →0 + (-4)*5 =-20.

Inequality:4x_p -20 <=0 →x_p <=5. So upper becomes5.

lower is -inf.

Edge C→D (5,4→7,4):

coeff = -(4-4) =0.

const_term = (7-5)*(8-4) + (4-4)*5 →2*4 +0=8.

Since coeff is0 and const_term>0 → invalid. So set lower=inf, upper=-inf. Break processing edges.

Thus, x_start = max(inf,4) →inf.

x_end = min(-inf,5) →-inf.

So x_start >x_end →0.

Which matches the second example.

Thus, the code should work.

Now, the code must read all the edges except the first, compute their constraints, and then count the valid x_p.

Potential issues to consider:

- Precision issues with floating points. For example, when rhs is an integer, but due to floating-point division, it's not represented exactly. For example, if x_p <=5.0, but due to calculation, it's stored as 4.999999999999, then math.ceil(x_start) would be 5. So need to handle this carefully.

But since all the coefficients and const_terms are integers (since the vertices are integers), the rhs could be a rational number.

For example, if coeff is 3 and const_term is 4 → rhs = (-4)/3 → -1.333… → x_p >= -1.333. So the ceil is -1.

But in code, using floating points may have precision issues. However, since the code checks for >= and <=, any x_p in integer that is >= rhs would satisfy.

But using math.ceil and floor should handle this correctly.

Another example: rhs is 5.0 → ceil(5.0) is5, floor(5.0) is5. So x_p can be 5.

Another example: rhs is 5.9999999999999 → floor(5.999999999) is5. But if x_p must be <=5.999..., then x_p can be 5. So math.floor(rhs) is5.

So code handles this correctly.

Another possible issue is when the edge is vertical. For example, u=(5,8), v=(5,4). Then the edge is vertical. The coeff is -(4-8)=4. The const_term is (5-5)*(8-8) + (4-8)*5 →0 + (-4)*5= -20. The inequality is4x_p -20 <=0 →x_p <=5.

But since the edge is vertical, the right side is to the left. So the code correctly computes the constraint.

Now, let's implement the code.

The code steps:

Read n.

Read n points.

Check if n <3 → but problem says n≥3.

AB is the first two points.

Check if AB is horizontal (A.y == B.y). According to problem statement, AB is parallel to x-axis, so this is guaranteed.

Compute x_min = min(A.x, B.x), x_max = max(A.x, B.x)

y_ab = A.y.

Initialize lower =-inf, upper =inf.

For i in 1 to n-1 (since the edges are from points[i] to points[i+1], except for i=n-1 which connects to points[0].

Wait, in code:

edges = []

for i in range(1, n):

    u = vertices[i]

    v = vertices[i+1] if i+1 <n else vertices[0]

    edges.append( (u, v) )

Wait, but the last edge is vertices[n-1] → vertices[0], which is for i =n-1.

Yes.

So for each edge in edges:

u = edge[0], v = edge[1]

compute coeff and const_term.

Then proceed.

So code:

import math

n = int(input())

vertices = [tuple(map(int, input().split())) for _ in range(n)]

A = vertices[0]

B = vertices[1]

y_ab = A[1]

x_min = min(A[0], B[0])

x_max = max(A[0], B[0])

lower = -math.inf

upper = math.inf

# Process all edges except AB (which is first edge)

for i in range(1, n):

    u = vertices[i]

    if i == n-1:

        v = vertices[0]

    else:

        v = vertices[i+1]

    u_x, u_y = u

    v_x, v_y = v

    coeff = -(v_y - u_y)

    const_term = (v_x - u_x) * (y_ab - u_y) + (v_y - u_y) * u_x

    if coeff == 0:

        if const_term > 0:

            # No solution

            lower = math.inf

            upper = -math.inf

            break

        else:

            # No constraint

            continue

    rhs = (-const_term) / coeff

    if coeff > 0:

        # x_p <= rhs

        upper = min(upper, rhs)

    else:

        # x_p >= rhs

        lower = max(lower, rhs)

    # Check if current bounds are invalid

    if lower > upper:

        break

x_start = max(lower, x_min)

x_end = min(upper, x_max)

if x_start > x_end:

    print(0)

else:

    x_start_ceil = math.ceil(x_start)

    x_end_floor = math.floor(x_end)

    if x_start_ceil > x_end_floor:

        print(0)

    else:

        print(x_end_floor - x_start_ceil + 1)

Testing this code against the first example:

Sample input 1:

5

4 8

8 8

9 4

4 0

0 4

Processing edges:

i=1: u = (8,8), v=(9,4)

coeff = -(4-8) =4

const_term = (9-8)*(8-8) + (4-8)*8 → 1*0 + (-4)*8 =-32.

rhs = (- (-32)) /4 → 32/4=8.0. Since coeff>0 → upper =8.0.

i=2: u=9,4 → v=4,0.

coeff= -(0-4)=4.

const_term= (4-9)*(8-4) + (0-4)*9 → (-5)*4 + (-4)*9 →-20-36= -56.

rhs= (-(-56))/4 →56/4=14 → upper = min(8,14) →8.

i=3: u=4,0 → v=0,4.

coeff= -(4-0) =-4.

const_term= (0-4)*(8-0) + (4-0)*4 → (-4)*8 +4*4 →-32+16= -16.

rhs = (-(-16)) / (-4) →16/-4= -4.

coeff is -4 <0 → so lower = max(-inf, -4) →-4.

i=4: u=0,4 →v=4,8.

coeff= -(8-4) =-4.

const_term= (4-0)*(8-4) + (8-4)*0 →4*4 +4*0 →16 +0=16.

rhs= (-16)/ (-4) →4 → lower becomes max(-4,4) →4.

Now x_start is max(4,4) →4.

x_end is min(8,8) →8.

x_start_ceil is4, x_end_floor is8. Count is 8-4+1=5.

Which is correct.

Sample input 2:

5

4 8

5 8

5 4

7 4

2 2

Processing edges:

i=1: u=(5,8) →v=(5,4).

coeff= -(4-8)=4.

const_term= (5-5)*(8-8) + (4-8)*5 →0 + (-4)*5= -20.

rhs= (20)/4=5.0 →upper =5.0.

i=2: u=(5,4) →v=(7,4).

coeff= -(4-4)=0.

const_term= (7-5)*(8-4) + (4-4)*5 →2*4 +0=8.

coeff is0 and const_term>0 → no solution. So lower=inf, upper=-inf. Break.

Thus, x_start=inf, x_end=-inf. So output 0.

Thus, code works.

Another test case:

Sample where AB is from x=5 to x=8, and the constraints are x >=4 and x <=7. So the valid x is 4,5,6,7.

But AB's x_min is5, x_max is8. So x_start = max(4,5)=5. x_end= min(7,8)=7. So valid x_p:5,6,7 →3 points.

Thus, code would return3.

Thus, the code should handle all cases correctly.
</think>

```python
import math

n = int(input())
vertices = [tuple(map(int, input().split())) for _ in range(n)]
A = vertices[0]
B = vertices[1]
y_ab = A[1]
x_min = min(A[0], B[0])
x_max = max(A[0], B[0])

lower = -math.inf
upper = math.inf

valid = True

for i in range(1, n):
    u = vertices[i]
    if i == n - 1:
        v = vertices[0]
    else:
        v = vertices[i + 1]
    ux, uy = u
    vx, vy = v
    coeff = -(vy - uy)
    const_term = (vx - ux) * (y_ab - uy) + (vy - uy) * ux
    
    if coeff == 0:
        if const_term > 0:
            valid = False
            break
        continue
    
    rhs = (-const_term) / coeff
    if coeff > 0:
        if rhs < upper:
            upper = rhs
    else:
        if rhs > lower:
            lower = rhs
    
    if lower > upper:
        valid = False
        break

if not valid:
    print(0)
else:
    x_start = max(lower, x_min)
    x_end = min(upper, x_max)
    
    if x_start > x_end:
        print(0)
    else:
        x_start_ceil = math.ceil(x_start)
        x_end_floor = math.floor(x_end)
        
        if x_start_ceil > x_end_floor:
            print(0)
        else:
            print(x_end_floor - x_start_ceil + 1)
```