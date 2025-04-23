<think>
Okay, so I need to solve this problem where I have to calculate the number of regions formed by up to three circles on a plane. Let's think about how to approach this.

First, the problem says that each region is a connected area bounded by parts of the circles. The classic problem here is the circle division problem. I remember that the formula for the maximum number of regions created by n circles is n² - n + 2, but that's when each new circle intersects all previous circles in two points. But since circles can overlap in various ways, including not intersecting, the actual number depends on how many times each pair of circles intersect and how the intersections contribute to new regions.

So the key is to calculate the number of intersections between all pairs of circles and then use Euler's formula for planar graphs. Euler's formula is V - E + F = 2, where V is the number of vertices (intersection points), E the number of edges (arcs between intersections), and F the number of faces (regions). But since we're dealing with circles, maybe there's a way to model this.

Wait, another approach is the incremental approach. When adding each circle, the number of new regions it creates is equal to the number of times it intersects with the previous circles plus 1. For example, the first circle divides the plane into 2 regions. The second circle, if it doesn't intersect the first, adds 2 regions (total 3+1=4?), no. Wait, maybe I need to recall the formula for regions created by circles.

Alternatively, the formula for the maximum number of regions R formed by n circles is R = n(n - 1) + 2. But that's when each new circle intersects all previous circles at two distinct points, adding 2(k) new regions when adding the k-th circle. Wait, let's see:

The standard approach is that each time a new circle is added, it can intersect each existing circle in at most two points. Each intersection contributes a new region. The number of new regions added by the new circle is equal to the number of intersection points it has with all previous circles plus 1. Because each intersection splits the new circle into arcs, each of which can divide an existing region into two.

So for example, adding the first circle: splits the plane into 2 regions.

Second circle: if it doesn't intersect the first, adds 2 regions (total 3? Or wait, maybe the initial formula is different. Let me think again.

Alternatively, here's the formula:

The maximum number of regions R(n) for n circles is R(n) = n² -n +2. Let's check for n=3: 3²-3+2=8. But in the sample inputs, the third example outputs 8. So when all three circles intersect each other in two points each, but arranged such that each pair intersects twice, and the third circle's intersections with the first two are arranged in a way that adds 2*2=4 new regions, then total is 8.

So maybe the general approach is to compute the number of intersections, then use Euler's formula.

But how to model this. Let's think about Euler's formula. For planar graphs embedded in the plane, V - E + F = 1 (since the outer face is considered). Wait, but the formula is V - E + F = 2 for connected planar graphs. Hmm. But in this problem, the circles form a planar graph. The regions correspond to the faces.

Each circle contributes a cycle. Each intersection between two circles is a vertex where two edges (arcs) meet. So the graph has V vertices (each being an intersection point of two circles), E edges (each being an arc between two consecutive intersection points on a circle), and F faces (the regions we need to count).

So using Euler's formula: V - E + F = 1 (since the graph is connected? Or perhaps not. Wait, no. If the graph is not connected, then Euler's formula is V - E + F = C + 1, where C is the number of connected components. This might complicate things. Alternatively, maybe it's better to model the arrangement of circles as a planar graph and compute F using Euler's formula.

So for the circles, the number of edges E is the sum over all circles of the number of arcs they're divided into. Each intersection splits a circle into arcs. For a single circle, there are no intersections, so 1 arc. For each pair of intersections with other circles, each circle's number of arcs is equal to the number of intersection points on that circle. So for a circle that has k intersection points (each from different circles), the number of arcs is k. Because each pair of consecutive intersection points along the circle creates an arc. So for example, if a circle has 2 intersections with another circle, that's two points, which split the circle into two arcs. If a circle has 4 intersections (from two other circles, each intersecting in two points), then the circle is split into 4 arcs.

Wait, no. Let me think again. Suppose a circle intersects with two other circles, each at two points. Then those four points are arranged around the circle. So the number of arcs would be 4. Because each adjacent pair of points along the circle's circumference creates an arc. So the number of arcs per circle is equal to the number of intersection points on that circle.

So for each circle, the number of arcs (edges) is equal to the number of intersection points on that circle. So E is the sum over all circles of the number of arcs, which is the sum of the number of intersection points per circle.

But each intersection is between two circles. So each intersection contributes two points (one to each circle). Wait, no. Each intersection between two circles is a single point (if tangent) or two points. Wait, when two circles intersect, they can have 0, 1 (tangent), or 2 points of intersection. So each pair of circles can contribute 0, 1, or 2 points to V.

So let's compute V as the total number of intersection points. Each such point is where two circles meet. But each point is counted once in V. So V is the sum over all pairs of circles of the number of intersections between them. For example, if two circles intersect at two points, that's two points added to V.

Now, E is the sum over all circles of the number of arcs. Each arc is between two consecutive intersection points on the circle. So for a circle that has k intersection points, the number of arcs is k. Because each pair of consecutive points around the circle creates an arc. So if a circle has 0 intersections (no other circles intersect it), then it's a single circle with 1 arc, but wait, that would contribute 1 to E. But then, how does that fit into the model?

Wait, perhaps for a circle that is isolated (no intersections), the number of arcs is 1. So that circle contributes 1 to E. Then, E is the sum for each circle of the number of arcs, which is the number of intersection points on that circle. So if a circle has m intersection points, then it contributes m arcs. But wait, if there are m points, then the circle is split into m arcs. Because each adjacent pair of points (in circular order) defines an arc. So for m points, there are m arcs. So for example, 2 points split into 2 arcs. 4 points split into 4 arcs.

So for each circle, the number of arcs is equal to the number of intersection points on that circle. But each intersection point is shared with another circle. So each pair of circles that intersect in two points contributes two points. Each of those two points is counted once in V, and each contributes to the intersection count of both circles.

So the steps are:

1. For each pair of circles, compute the number of intersection points (0, 1, or 2). This gives V, the total number of vertices.

2. For each circle, count how many times it intersects with other circles. For example, if circle A intersects with two other circles (each in two points), then the number of intersection points on circle A is 2 + 2 = 4. Then, the number of arcs for circle A is 4, contributing 4 to E.

But wait, each intersection between two circles contributes two points. So for example, if two circles intersect in two points, each point is on both circles. So for each such pair, each circle involved in the pair gets 2 points added. Wait no. If two circles intersect in two points, then each of those points is shared between the two circles. So for that pair, each circle has two new points added. So for the pair, the total points added to each circle is 2. But for the pair, the total points in V is 2.

Wait, no. Let me clarify. Suppose circle A and circle B intersect at two distinct points. Then each of those two points is counted once in V. Each point is on both circles. So for each of those two points, the circle A has one intersection point (each point is on A and B). So for circle A, the two points contribute 2 to its count of intersection points. Similarly for circle B.

So for each pair of circles that intersect in two points, each circle in the pair gains two intersection points. So each pair contributes 2 to the sum of all the intersection points on all circles, but contributes 2 to V (the actual number of vertices). Wait, no. Because each of the two points is a single vertex. So the pair contributes 2 vertices. Each vertex is part of two circles. So for each vertex, each of the two circles involved has that point as part of their intersection points.

So for example, two circles intersecting at two points (p and q). Each of these points is a vertex. So V increases by 2. For circle A, these are two points (p and q), so the number of arcs for circle A is 2. Similarly for circle B.

So for each circle, the number of arcs is equal to the number of intersection points on that circle. If a circle has m intersection points, the number of arcs is m. If the circle is not intersected by any other circles, then m=0, and the number of arcs is 0? Wait that can't be. Because a single circle divides the plane into two regions, so how does that fit into the formula?

Ah, perhaps the formula needs to account for circles that are not intersected. Because a single circle has 2 regions, but according to the model, V=0, E=0 (since the circle has no arcs?), then V-E + F = 0 -0 + F = F. According to Euler's formula, F=2. So how?

Wait, maybe the initial model is incorrect for isolated circles. Let's think again. Let's model each circle as a cycle. For a single circle, it's a cycle with zero vertices (since no intersections) but how many edges? Or perhaps the model needs to consider that each circle contributes a cycle. For a circle with no intersections, it's a single cycle. So in graph terms, the circle is represented as a cycle. So the number of edges E would be 1 for the circle (but edges are arcs between vertices, which in this case, there are no vertices. Wait, this is getting complicated.

Alternatively, maybe the approach to model each circle as a single cycle when it's not intersected. So, for each circle not intersected by any others, it contributes 2 regions. So for n circles not intersecting each other, the total regions would be 1 (the infinite region) plus n regions (each enclosed by a circle). Wait, no. For example, one circle divides the plane into two regions: inside and outside. Two separate circles (non-overlapping) create three regions: outside both, inside first, inside second. So for n circles, the regions are n + 1 if none overlap. But if they are nested, the regions are different. So the problem is more complicated.

So maybe the incremental approach is better. Let's think:

Each new circle can add some regions. The number of regions added by the k-th circle is equal to the number of times it intersects all previous circles multiplied by two, plus one. Or maybe it's the number of intersections plus one. Wait, let's think:

The first circle: 2 regions.

Second circle:

- If it doesn't intersect the first, then adds 2 regions (so total 4). But in reality, two separate circles would have 3 regions. Wait, perhaps the formula is different.

Wait, perhaps the formula is:

R = 2 + Σ (number of intersections created by each new circle with previous ones)

So for each new circle, the number of new regions it creates is equal to the number of times it crosses all previous circles. Each crossing adds a new region. So the formula is R = 1 + sum over all circles (number of intersections with previous circles + 1). Hmm.

Wait, here's a resource I remember: the maximum number of regions created by n circles is n(n-1) + 2. But that's when each new circle intersects all previous circles in two points each. For example:

n=1: 2 regions.

n=2: 2 + 2*1 = 4 regions (but two separate circles would be 3 regions. So this formula is for the case where each new circle intersects all previous in two points. So this is when each pair of circles intersects in two points. So in that case, the number of regions is 2 + 2*C(n, 2), but that's not matching. Wait, n(n-1) + 2 for n=2: 2*1 +2=4. But two circles that intersect in two points create 4 regions. So that formula holds. So the formula works when each new circle intersects all previous circles in two points. But if they don't, the regions can be less.

So the problem becomes, for each pair of circles, how many intersections they have (0, 1, 2), and based on that, compute the total regions.

So the approach would be:

Start with 1 region (the entire plane).

Each time a new circle is added:

- The number of regions it adds depends on how many times it crosses the existing arrangement. Each time it crosses an existing circle, it can split a region into more regions.

But how to model this.

Alternatively, for each circle added, the number of new regions created is equal to 1 plus the number of intersections it has with existing circles. But wait, perhaps each intersection with a previous circle contributes two regions. Or maybe each intersection contributes one region.

Alternatively, the formula from computational geometry says that the maximum number of regions formed by n circles is n² -n +2, but that's only when every new circle intersects all previous ones in two points each. So each new circle adds 2(k-1) new regions when added as the k-th circle. So for example:

First circle (k=1): 2 regions.

Second circle (k=2): intersects first in two points. Adds 2 regions. Total 4.

Third circle (k=3): intersects each of the two existing circles in two points each. So 2*2=4 intersections, adding 4 new regions. Total 8 regions.

Which matches the third example.

But how to compute this when circles may not intersect in two points each.

So the idea is to compute, for each new circle, how many times it intersects all previous circles. For each such intersection point, it contributes a new region. So the formula is:

regions = 1 (initial plane) + sum for each circle (1 + number of intersections with previous circles)

Wait, wait. Let's see. The initial plane is 1 region. Then, for each circle added, the number of regions added is 1 + the number of intersections with all previously added circles. So:

regions = 1 + sum_{i=1 to n} (1 + C_i), where C_i is the number of intersections between the i-th circle and all previous circles.

But how does that work for the first example:

Sample Input 1:

3 circles, all in a line, each touching the next (but not overlapping). The first and second circles are touching (so tangent?), and the second and third are also tangent.

So each pair of adjacent circles has 1 intersection point. So for three circles:

First circle (i=1): adds 1 + 0 (since no previous circles) → regions = 1 +1=2.

Second circle (i=2): intersects previous circles once (circle 1). So adds 1 +1 =2 → regions 4.

Third circle (i=3): intersects previous circles once (circle 2). So adds 1 +1=2 → regions 6. But the sample output is 4. So this approach doesn't work.

Wait, but sample input 1's output is 4. So according to this formula, it's 6. Which is incorrect. So the formula must be wrong.

Hmm. So this approach is incorrect. Let's think again.

Wait, sample input 1 has three circles arranged in a line, each touching the next. So each pair of circles is tangent (so one intersection point). The regions: the three circles are separate, but each is tangent to the next. So the first circle divides the plane into two regions. The second circle (tangent to the first) adds two regions (so total 3?), but the third circle (tangent to the second) adds another two regions (total 5?), but the sample output is 4. So clearly, this approach is wrong.

Wait, the sample input 1's output is 4. Let's see:

Three circles arranged in a line. Each is centered at (0,0), (2,0), (4,0), radius 1 each. So the first and second circles touch at (1,0), the second and third at (3,0). Each pair has one point of contact.

So the regions would be:

Outside all circles: 1 region.

Inside first circle: 1.

Inside second circle: 1.

Inside third circle: 1.

But that's four regions, hence the output is 4. So the first circle contributes 2 regions. The second circle is added. It is tangent to the first. So it adds two regions: the inside of the second circle (a new region) and splits the existing regions. Wait, no. Because when two circles are tangent, adding the second circle creates two new regions. Let me see:

Initially, first circle: two regions (inside and outside).

Add the second circle (tangent). The outside of the first circle is split into two regions: the area outside both, and the area inside the second circle. The inside of the first circle is still a region. So total regions: 3. Then adding the third circle (tangent to second) adds another region. So total 4.

So how does this fit into a formula.

In this case, for the first circle, added regions: 1 (initial +1). Then for the second circle, adds 1 (since it has one intersection with the previous circles). So 1+1=2 regions added. Then for the third, adds 1 (one intersection) → 1+1=2, but in reality it adds 1. So this approach is incorrect.

So the incremental formula must not be simply sum (1 + C_i). There's something wrong here.

Alternative approach: Use Euler's formula for planar graphs. So compute V, E, then F = E - V + 2 (since for planar graphs, V - E + F = 2 → F = E - V + 2). But how to compute V and E.

In the case of circles:

V is the number of intersection points between all pairs of circles. Each pair can contribute 0, 1, or 2 points.

E is the sum over all circles of the number of arcs (edges) per circle. Each circle is divided into arcs by its intersection points. The number of arcs for a circle is equal to the number of intersection points on it. For example, if a circle has 2 intersection points (from two other circles), it's split into two arcs. But if a circle has no intersections, then it's a single closed loop (so one arc?).

But then, for a single circle (no intersections), V=0, E=1 (one arc). Then F = E - V + 2 → 1 -0 + 2 =3, which is wrong. Because a single circle creates 2 regions. So there's a problem here.

Hmm. So perhaps the model is not capturing the fact that the outer face is counted as one region, and each circle's interior as another. So maybe the model is not directly applicable.

Alternatively, perhaps the formula should be F = E - V + C + 1, where C is the number of connected components. Because when the graph is disconnected, Euler's formula is V - E + F = C + 1.

But how to model the connected components here.

Alternatively, think of the arrangement of circles as a planar graph where each arc is an edge, each intersection point is a vertex, and the regions are the faces. Then, the number of regions is F = E - V + 2 (if the graph is connected), but if not, then F = E - V + C + 1, where C is the number of connected components.

But calculating C (connected components) could be complex.

But perhaps, given that n is up to 3, it's manageable.

So let's proceed.

Let's compute:

V = sum over all pairs of circles of the number of intersections between them.

E = sum over all circles of (number of arcs per circle). For each circle, the number of arcs is equal to the number of intersection points on it. For a circle with m intersection points, it's split into m arcs.

But for a circle with zero intersections (isolated), how many arcs? Because that circle contributes to the arrangement by dividing the plane into regions. So perhaps for such a circle, the number of arcs is 2? Because the circle is a single closed loop, but in terms of edges, perhaps it's considered as one edge that forms a cycle. Wait, but each arc is a single edge. So a circle with no intersections would have one arc (the entire circumference). So E is sum over circles of (number of arcs) = sum of (number of intersection points per circle) for all circles. But for a circle with zero intersections, that would contribute 0 to E, but that's not correct because that circle has one edge (arc) in the graph.

So the problem here is that the initial model for E is not correct for circles that are not intersected by others.

So perhaps the correct way to compute E is:

Each circle is split into as many arcs as the number of intersection points. But if a circle has zero intersections, then it is split into one arc (the entire circle). So E is the sum for each circle of (number of intersection points on it) if that number is >0, else 1.

Wait, but then for a circle with two intersection points (from one other circle), it's split into two arcs → 2 arcs. For a circle with zero, it's 1 arc.

So E is sum over all circles of (max(arcs, 1)), where arcs is the number of intersection points on the circle. No, because for a circle with zero intersection points, arcs is zero. So the max would be 1.

So the formula for E would be sum over each circle of (number of intersection points on the circle, but if zero, use 1).

But how to compute that.

Alternatively, for each circle, the number of arcs is equal to the number of intersection points if it's >=1, else 2. Because when a circle has no intersections, it's a single loop, which contributes one edge. Wait, but for a single circle, E would be 1. Then according to Euler's formula:

For a single circle:

V=0, E=1.

F = E - V + 2 → 1 +2 =3. Which is wrong. Because a single circle creates 2 regions. So the model is wrong.

Hmm. So this approach isn't working. What's wrong here.

Alternative idea: Each circle is a closed loop. Each loop has as many edges as the number of arcs. So for a circle with zero intersections, it's a single loop (one edge). So E is the sum of all edges, where each edge is an arc between two consecutive intersections on a circle. So for each circle, the number of edges is equal to the number of intersection points on that circle. If a circle has no intersections, then the number of edges is zero? Or one?

Alternatively, perhaps each circle is considered as a cycle. So for a circle with no intersections, it's a single cycle. But how does that fit into the graph.

Alternatively, perhaps the model is not suitable for circles that are not intersecting. So maybe the initial approach using Euler's formula is not applicable here.

Alternatively, perhaps the correct formula for the number of regions is:

Regions = V - E + C + 1

Where C is the number of connected components.

But I'm not sure. Let's think of some examples.

Sample Input 1:

Three circles, each tangent to the next. Each pair of circles contributes 1 intersection (tangent point). So V=3.

Each circle has two intersection points (each pair contributes 1). Wait, no. For three circles arranged in a line, each pair is adjacent and tangent. For example, circles A, B, C. A and B are tangent at one point. B and C are tangent at another point. A and C are non-intersecting. So pairs (A,B) and (B,C) each contribute 1 point. Pair (A,C) contribute 0. So total V=2.

Hmm, but the sample input's first example's output is 4. Let's compute V, E, C.

For each circle:

Circle 1 (A) has 1 intersection point (with B). So edges for A: 1 (so 1 arc? But that can't split a circle into an arc. Wait, if a circle has one intersection point, that's a tangent point. So the circle is split into one arc (the entire circle?), but that doesn't make sense. Because a tangent point is a single point where two circles touch. So the arc for circle A would be the entire circle except the tangent point? Or perhaps the model is different.

Alternatively, perhaps when two circles are tangent, each circle has one intersection point. So each such circle's count of intersection points is increased by 1. For each pair of circles that are tangent, each circle gains one intersection point.

So for sample input 1:

Each of circles A and B has one intersection point (the tangent point). So each contributes 1 intersection point. So for circles A and B, each has 1 intersection point. So their arcs would be 1 each. So edges for A: 1, edges for B: 1. Then circle C is tangent to B, so has 1 intersection point. So edges for C: 1.

So E = 1+1+1=3.

V=2 (the two tangent points between A-B and B-C).

C is the number of connected components. How?

Each circle is a separate component if they don't intersect. But if they are connected via intersections, perhaps the connected components are determined by the adjacency through intersections.

In sample input 1, the circles are arranged as A - B - C, with B connected to both A and C. So the arrangement's graph consists of three circles connected via two tangent points. Are they part of the same connected component?

But in terms of the planar graph, the connected components would depend on how the edges are connected. Each tangent point is a vertex where two edges (arcs) meet. So in the case of A and B tangent, the vertex is part of both A and B's edges.

But perhaps the connected components are separate if there's no way to reach from one edge to another via vertices. So in the case of three tangent circles arranged in a line, the graph may consist of two connected components: the chain of A-B and B-C may form a connected component, but perhaps not. Wait, A's edge is connected to the vertex between A and B, which is connected to B's edge. B's edge is connected to the vertex between B and C, which is connected to C's edge. So all three circles are connected via vertices, leading to a single connected component.

So C=1.

Then F = E - V + C + 1 → 3 - 2 + 1 +1 = 3. But the sample's output is 4. So this approach is incorrect.

Hmm, this is getting too complicated. Maybe the correct approach is to use the inclusion-exclusion based on the number of intersections between pairs of circles and the regions created when circles are added.

Alternatively, for small n (up to 3), perhaps we can handle all possible cases by considering the possible combinations of circles and their intersections.

Because n is up to 3, it's feasible to handle all possible scenarios.

So the approach would be:

For each possible number of circles (1, 2, or 3), compute the number of regions based on the intersections between each pair of circles.

For n=1: 2 regions.

For n=2:

If the two circles have 0 intersections → regions = 3 (each circle's inside plus the outside).

If they have 1 intersection (tangent) → regions = 3 (the two circles are tangent, creating three regions: outside both, inside first, inside second, but the tangent point is a single point, so no new region is created beyond that of two separate circles. Wait, no. If two circles are tangent, they split the plane into three regions. For example, two circles that touch at one point. The outside of both, the inside of the first, and the inside of the second. So regions =3.

If the two circles intersect at two points → regions=4.

So for n=2, the number of regions is:

regions = 2 (n=1) + 1 + intersections. Wait, no. For two circles:

If they are separate: 3 regions.

If they intersect at two points: 4 regions.

If tangent: 3 regions.

Wait, that's correct. So for two circles:

regions = 2 + (number of intersections between them) / 2.

Because when there are 0 intersections → 3 regions. 2 +0 → no. That doesn't fit.

Hmm. Let's think again.

Wait, for n=2:

If 0 intersections (separate circles): regions =3.

If 1 intersection (tangent): regions=3.

If 2 intersections: regions=4.

So the number of regions is 2 + (number of intersections) if the number of intersections is 2, else 3.

But this doesn't fit into a simple formula.

So for two circles, regions = 3 if 0 or 1 intersections, 4 if 2.

For three circles, it's more complicated.

So perhaps the general approach is to model the regions based on how the circles intersect, considering all pairs and their intersection counts.

For three circles, the regions can be computed as follows:

The base case is two circles. Each additional circle can intersect existing circles in 0, 1, or 2 points per circle.

Each time a new circle is added, the number of regions it adds depends on the number of intersections it has with the existing arrangement.

For example, adding the third circle:

Each intersection with an existing circle can create a new region. The number of new regions added is equal to the number of times the new circle crosses the existing arrangement. Each crossing can split an existing region into two.

But how?

Alternatively, the formula for the number of regions after adding the k-th circle is R_k = R_{k-1} + 2*C_k, where C_k is the number of existing circles that the k-th circle intersects in two points. But this is just a guess.

Alternatively, the number of regions added by the new circle is equal to the number of intersection points it has with existing circles. For each intersection point, the new circle is divided into segments, each of which can split a region into two.

For example, adding a circle that intersects two existing circles in two points each would create 4 new regions. So the third circle adds 4 regions. Which would take the total from 4 (for two intersecting circles) to 8, which matches the third sample.

But the sample input 3 has three circles, each intersecting the other two in two points. So when the third circle is added, it has 4 intersections (two with each of the two existing circles). So the number of new regions would be 4, leading to 4 (from two circles) + 4 = 8.

Which is correct.

So perhaps the formula is:

regions = 1 + sum for each circle (number of intersections with previous circles) + 1 for each circle.

Wait, for the first circle, regions = 1 + 0 (no previous) +1 → 2.

Second circle:

if it intersects the first in two points: regions = 2 + 2 +1 → 5? No. Because two circles intersecting in two points have 4 regions.

Hmm. Maybe not.

Alternative approach:

Each time a new circle is added, the number of new regions created is equal to the number of intersections between the new circle and the existing circles multiplied by 2. Then add 2.

Wait, for the first circle:

Initial regions: 1 (the entire plane).

Add the first circle → regions = 2.

Add the second circle:

If it intersects the first in two points → adds 2*2 =4 regions. So total 2+4=6. But two circles intersecting in two points create 4 regions. So this is incorrect.

So this approach is also wrong.

Perhaps the correct way to model this is to use the formula for the maximum regions and subtract the overlaps. But with n up to 3, perhaps it's feasible to consider all possible cases.

For three circles, the regions can be calculated as follows:

Start with two circles. Their regions are either 3 or 4, depending on whether they intersect in two points or not.

Then add the third circle. For each existing circle, determine how many times the new circle intersects it. The number of new regions added is 2 times the number of circles the new one intersects in two points, plus 1 times the number of circles it intersects in one point, plus 1 if it doesn't intersect any existing circles.

Wait, but this seems arbitrary.

Alternatively, for each new circle, the number of new regions it adds is equal to the number of intersection points it has with existing circles plus 1. For example:

- If the new circle doesn't intersect any existing circles → adds 1 region.

- If it intersects one existing circle in two points → adds 2 +1 =3 regions.

- If it intersects two existing circles, each in two points → adds 4 +1=5 regions.

But again, how does this fit with the sample inputs.

Sample input 1:

Third circle intersects one existing circle (the second) in one point (tangent). So adds 1 +1 =2 regions. Initial regions after two circles (A and B are tangent, B and C are tangent, but A and C are separate). So after two circles (A and B), regions are 3. Adding C (tangent to B), which has one intersection point. So adds 1 +1 =2 regions. So total 3 + 2 =5. But the sample output is 4. So this approach is incorrect.

Hmm. This is getting really tricky. Perhaps the correct way is to model the problem using Euler's formula but correctly compute V and E.

Let's try for the first sample input:

n=3.

The three circles are arranged in a line. A and B are tangent (1 intersection), B and C are tangent (1), A and C have 0.

V = 1 (A-B) + 1 (B-C) +0 (A-C) =2.

Each intersection is a single point. So V=2.

For each circle:

A has one intersection point (with B).

B has two intersection points (with A and C).

C has one intersection point (with B).

So the number of arcs per circle:

A: 1 → but 1 intersection point implies 1 arc. So edges for A is 1.

B: 2 intersection points → edges for B is 2.

C: 1 intersection point → edges for C is 1.

Total E=1+2+1=4.

Now, according to Euler's formula: V - E + F = 2 - 4 + F = C +1, where C is the number of connected components.

But what is C here? The graph consists of three circles connected via the two vertices (the tangent points). For example, the edges of A is connected to the vertex between A and B, which is connected to the edges of B, which are connected to the vertex between B and C, which is connected to edges of C. So the entire graph is connected. So C=1.

Thus, V - E + F = 1 +1 → F = E - V + C +1.

Wait, I'm getting confused. The formula for connected planar graphs is V - E + F = 2. If the graph is disconnected with C connected components, the formula becomes V - E + F = C +1.

So in this case, the graph is connected (C=1), so V - E + F = 2 → F = E - V +2.

So F=4 -2 +2=4. Which matches the sample output of 4.

So this works!

So for the first sample:

V=2, E=4, F=4. Which is correct.

Another sample: third sample's output is 8.

Let's compute V and E.

Sample Input 3:

3 circles:

A: (0,0) r=2.

B: (2,0) r=2.

C: (1,1) r=2.

Each pair of circles intersects in two points. For example, A and B: distance between centers is 2, sum of radii is 4, so they intersect in two points. Similarly for other pairs.

So each pair contributes two intersection points.

So V=3 pairs × 2 points per pair = 6 points.

Each circle is involved in two pairs, so each has 2 ×2 =4 intersection points (since each pair contributes two points).

Wait, no. Each pair contributes two points. For three pairs (A-B, A-C, B-C), each with two points. So V=6.

Each circle is part of two pairs. For example, A intersects B and C, each in two points. So circle A has 2×2=4 intersection points. So the number of arcs for A is 4. Similarly for B and C.

So E=4+4+4=12.

Then F= E - V + 2 =12 -6 +2=8. Which matches the sample's output of 8.

Yes! So this approach works.

So the correct formula is:

Regions (F) = E - V + 2.

But how to compute V and E.

Steps:

1. Compute all pairs of circles and find the number of intersection points between them. Sum these to get V.

2. For each circle, count the number of intersection points on it. This is the sum of the number of intersection points from each pair that includes this circle.

   For example, if circle A is part of two pairs that each contribute two points, then circle A has 2+2=4 points.

   The number of arcs for this circle is equal to the number of intersection points on it. So each such circle contributes that number to E.

3. Sum all these arc counts to get E.

4. Then, F = E - V + 2.

So the steps are:

- Compute all pairwise intersections.

- Sum all pairwise intersections to get V.

- For each circle, count the number of intersections (sum over pairs involving this circle).

- Sum these counts to get E.

- F = E - V + 2.

But wait, in the first sample, the sum for E is:

Circle A: 1 point (from pair A-B).

Circle B: 2 points (from A-B and B-C).

Circle C: 1 point (from B-C).

Sum E=1 +2 +1=4.

V=2 (from pair A-B and B-C, each contributing 1 point).

F=4-2+2=4.

Which is correct.

Another example: two circles intersecting in two points.

n=2.

V=2.

Each circle has two points. So E=2 + 2 =4.

F=4-2+2=4. Which is correct.

So this formula works.

So the key is to compute V and E correctly.

So the plan is:

For each pair of circles, compute the number of intersection points (0, 1, or 2). Sum all of these to get V.

For each circle, compute the sum of intersection points from all pairs it's in. This sum is the number of arcs for that circle, contributing to E.

Sum all such numbers to get E.

Then F = E - V + 2.

But wait, what if a circle has zero intersection points? Then its arcs count is zero. So in E, it would contribute zero. But that's not correct.

Wait, let's take n=1. Then V=0. The sum of arcs for the single circle is zero. So E=0. F=0-0+2=2. Which is correct.

So in that case, the formula works.

What if there's two circles that don't intersect.

n=2, two separate circles. Each pair contributes 0. So V=0.

Each circle has zero intersection points. So E=0+0=0.

F=0-0+2=2. But two separate circles would create 3 regions. So the formula is wrong.

Wait, what's wrong here?

Ah, this is the problem. For two circles that don't intersect, the formula gives F=2, but the correct answer is 3.

So what's the mistake.

Let's see:

V=0.

E=0 (each circle has zero intersection points → zero arcs).

F = 0 -0 +2 =2.

But the correct number of regions is 3. So the formula fails here.

So why is that? Because when there are no intersections, the graph consists of two separate circles (each a cycle), so E is the sum of the arcs for each circle. But in this case, each circle with zero intersections has one arc (the entire circle). So E should be 1 + 1 = 2.

Then V=0, E=2.

F=2-0+2=4. Which is incorrect.

Hmm. So the formula works when there are intersections, but not when there are none.

What's the issue?

Ah! The model assumes that each circle's arcs are determined by its intersection points. But when there are no intersections, the circle is still a single arc. So the number of arcs for a circle with zero intersections is 1, not 0.

So the correct way to compute E is:

For each circle, the number of arcs is the number of intersection points on it. If the number of intersection points is zero, then it's 1.

So the formula for each circle's arcs is:

arcs = max(number of intersection points on the circle, 1)

But how?

Wait, for a circle with zero intersections, it's a single arc. For a circle with m>0 intersections, it's m arcs.

So E is the sum for each circle of:

if (number of intersection points) >0 → add that number to E.

else → add 1.

Then for two separate circles:

Each has zero intersections. So each contributes 1 to E. E=2.

V=0.

F=2-0 +2=4. Which is still wrong. Because two separate circles have three regions.

So this suggests that the model is not correct for cases where there are non-intersecting circles.

What's wrong here?

Perhaps the model is missing some edges or vertices.

Alternatively, perhaps the formula F = E - V + 2 is only valid when the circles form a connected graph. If the circles are disconnected, then the formula must account for the number of connected components.

For example, in the case of two separate circles, the graph consists of two connected components (each circle is a separate component). So according to Euler's formula for multiple connected components, V - E + F = C + 1, where C is the number of connected components.

So in this case, V=0, E=2, C=2.

Then:

0 -2 + F = 2 +1 → F=5.

But that's not correct. The actual number of regions is 3.

So the problem is that the model doesn't correctly account for the connected components and how they contribute to the face count.

This indicates that the initial approach is not valid for cases with disconnected components.

But how to handle this? Given the time constraints, perhaps we can find a way to adjust for the non-intersecting circles.

Alternatively, perhaps the formula can be modified to account for the number of circles that are not intersecting any others. For example:

Let S be the number of circles that have no intersection with any other circles. For these circles, each contributes one region. But this is not straightforward.

Alternatively, when all circles are separate (no intersections), the number of regions is 1 + sum_{i=1 to n} 1 = n+1.

But when circles are arranged in a way that some intersect and some don't, the formula must account for both connected and disconnected components.

This seems complicated. However, since the problem has n up to 3, perhaps we can handle all possible cases.

But this would require checking all possible cases of circle intersections, which is feasible for n=3.

Alternatively, find a way to compute the number of connected components and use the correct version of Euler's formula.

But how?

Another approach:

The formula F = E - V + C + 1, where C is the number of connected components.

So in the case of two separate circles:

E=2 (each circle has 1 arc → 2 arcs).

V=0.

C=2 (two connected components, each circle is its own component).

F = 2 -0 +2 +1 → 5. Which is wrong.

But the correct answer is 3.

So this approach is not working.

Alternative idea: the formula F = E - V + 2 - (C-1).

Because when there are C components, the standard Euler's formula for each component is V_i - E_i + F_i = 2. Summing over all components: sum V_i - sum E_i + sum F_i = 2C. But the total F is sum F_i - (C-1), since the outer face is counted once for all components.

But this is getting too complicated.

Perhaps it's better to find another way to compute the correct F.

Wait, in the case of two separate circles:

The planar graph consists of two cycles, not connected.

Each cycle has V=0 (no intersections), E=1 (one arc), and F=2 (two faces) per cycle.

But combining the two cycles, the total F is 3.

But according to the formula for each cycle:

For each cycle:

V_i - E_i + F_i = 2.

For first cycle: 0 -1 + F1 = 2 → F1=3.

But this is impossible.

Alternatively, the formula for a single cycle (a circle with no intersections) is:

V=0, E=1.

V - E + F = 0 -1 + F = 2 → F=3.

Which suggests that a single circle would have 3 regions, which is incorrect. So this indicates that the model is not correct.

Thus, the model based on Euler's formula is not working for disconnected or non-intersecting circles.

So what's the solution?

The problem must have a way to compute the correct number of regions even when there are non-intersecting circles.

After some research, I found that the correct formula for the number of regions formed by circles is:

R = V - E + C + 1.

Where C is the number of connected components in the arrangement.

But how to compute C.

Connected components in the arrangement of circles are determined by the intersection graph. Each circle is a node, and two nodes are connected if the circles intersect. Then, the connected components of this graph are the connected components C_g.

But this may not directly give the connected components of the planar graph. For example, two circles that are tangent (one intersection) are connected in the intersection graph, but the planar graph may have them forming a single connected component.

Alternatively, C is the number of connected components in the planar graph formed by the arcs and vertices.

This is getting too complex.

But given that the problem's n is up to 3, perhaps we can compute C by checking if the circles form a connected arrangement.

For example:

- If all circles are isolated (no intersections), then C = n.

- If two circles are connected by an intersection, then C is less than n.

But again, this is unclear.

Alternative approach: 

Compute the correct formula for small n.

For n=1:

V=0, E=1 (one arc).

F = E - V + 2 = 1+2=3. But the correct answer is 2.

So this approach is not working.

Alternatively, perhaps the formula should be F = E - V + 1 + C, where C is the number of circles.

But this is a guess.

For n=1:

E=1, V=0, C=1.

F=1-0+1+1=3. No.

Hmm.

This suggests that the initial approach is not applicable to isolated circles. So perhaps the model needs to account for the fact that each circle, even if not intersected, contributes one edge (arc) and two regions.

But how.

Alternatively, let's consider that each circle contributes 2 regions initially, and each intersection with another circle increases the regions by some amount.

But this is not a general solution.

Given the time constraints, perhaps the correct approach is to use the formula F = E - V + 2 when there's at least one intersection, and handle the case of isolated circles separately.

But when there are circles that don't intersect any others, how to account for them.

Alternatively, the formula F = E - V + 2 + (S), where S is the number of circles that are not intersected by any other circle.

But this is a guess.

For two separate circles:

E=2 (each has one arc), V=0.

F = 2 -0 +2 + 0 (since both circles are not isolated? No. Because they are isolated (not intersected by others), so S=2.

But then F=4 + 2=6. Which is wrong.

So this approach is also incorrect.

Given the time constraints and the problem's small n (up to 3), perhaps the correct solution is to implement the formula F = E - V + 2, and then adjust for the cases where some circles are not intersected.

But how.

For example:

- If there's at least one intersection, use F = E - V + 2.

- If there are no intersections (all circles are separate), then F = 1 + sum (1 for each circle). Because each circle adds one region (the inside) and the outside is one region. So for n circles with no intersections, F = n +1.

So for the case when V=0 (no intersections), the answer is n +1.

Otherwise, compute F = E - V + 2.

Let's test this:

Sample Input 1: V=2, E=4. F=4-2+2=4. Correct.

Sample Input 3: V=6, E=12. F=12-6+2=8. Correct.

Two intersecting circles: V=2, E=4. F=4-2+2=4. Correct.

Two separate circles: V=0. So return n+1=2+1=3. Correct.

One circle: V=0 → n+1=2. Correct.

Another case: three circles, two intersecting, one separate.

V=2 (from the two intersecting circles).

E for the two intersecting circles: 2+2=4. For the third, E is 1 (no intersections). Total E=5.

F=5-2+2=5.

But the actual regions would be:

Regions from the two intersecting circles:4.

The third circle is separate, adding 1 region (inside). So total regions 4 +1 =5. Which matches F=5.

So this approach seems to work.

So the steps are:

- Compute V as the total number of intersection points between all pairs of circles.

- If V is zero, then the answer is n +1.

- Else, compute E as the sum for each circle of (number of intersection points on that circle). For a circle with no intersections, add 1.

- Then F = E - V + 2.

Wait, no. For the third circle in the previous example (three circles, two intersecting and one separate), the third circle has no intersections. So for E, we add 1 for it. The two intersecting circles have 2 points each, contributing 2 + 2 =4. So E=4+1=5. V=2. F=5-2+2=5. Correct.

Yes. So the correct approach is:

Compute V (sum of intersections between all pairs).

If V is zero → answer is n+1.

Else:

For each circle, compute the number of intersection points on it. Sum all of them. For circles with zero intersection points, add 1 to E.

So E is sum over all circles of (number of intersections on circle if it's >0, else 1).

Then F = E - V + 2.

Yes, this works.

So the steps are:

For each pair of circles, compute the number of intersections (0, 1, or 2). Sum to get V.

For each circle, count the number of intersections it has with other circles. If this count is zero, add 1 to E. Else, add the count to E.

Then F = E - V + 2.

Let's verify this:

Case: two separate circles.

V=0 → answer is n+1=3. Correct.

Case: two intersecting circles.

V=2.

Each circle's intersection count is 2. So E=2+2=4.

F=4-2+2=4. Correct.

Case: three circles, two intersecting and one separate.

V=2 (from the two intersecting circles).

Each of the two intersecting circles has 2 intersections. The third has 0, so contributes 1 to E.

E=2+2+1=5.

F=5-2+2=5. Which is correct.

Another case: three circles, all separate. V=0. Answer is 3+1=4. Correct.

Another case: three circles, A and B are intersecting (V=2), C is tangent to B (V=1).

So total V=3.

For circle A: 2 intersections with B.

For B: 2 (A) +1 (C) =3.

For C:1.

E=2+3+1=6.

F=6-3+2=5.

What's the actual regions?

A and B intersect in two points, creating 4 regions. C is tangent to B, creating an additional region (the inside of C). So total regions 4+1=5. Which matches.

Yes.

So this approach works.

So the algorithm is:

1. Compute V by checking each pair of circles and counting their intersections.

2. If V is zero, return n+1.

3. Else, compute E by:

   a. For each circle, count the number of intersections it has with other circles.

   b. If the count is zero, add 1 to E.

   c. Else, add the count to E.

4. Then, F = E - V + 2.

So now, the problem reduces to correctly:

a. Determining the number of intersections between two circles.

b. Implementing this in Python.

So, for two circles, how to compute the number of intersection points.

The two circles are given by (x1, y1, r1) and (x2, y2, r2).

Compute the distance between centers: d = sqrt( (x2-x1)^2 + (y2-y1)^2 )

The circles can:

- Be separate (d > r1 + r2 → 0 points.

- Touch externally (d == r1 + r2 → 1 point.

- Intersect ( |r1 - r2| < d < r1 + r2 → 2 points.

- One is contained within the other, and not touching (d < |r1 - r2| → 0 points.

- One is contained and touching (d == |r1 - r2| → 1 point.

So, to compute the number of intersection points:

If d > r1 + r2: 0.

If d == r1 + r2: 1.

If d < r1 + r2:

   if d < abs(r1 - r2): 0.

   elif d == abs(r1 - r2): 1.

   else: 2.

So the steps are:

Compute d squared to avoid floating points.

But since the coordinates and radii are integers, we can compute everything in integers to avoid precision errors.

So:

dx = x2 - x1

dy = y2 - y1

d_sq = dx*dx + dy*dy

sum_r = r1 + r2

sum_r_sq = sum_r * sum_r

diff_r = abs(r1 - r2)

diff_r_sq = diff_r * diff_r

Compare d_sq with sum_r_sq and diff_r_sq.

If d_sq > sum_r_sq: 0 points.

elif d_sq == sum_r_sq: 1 point.

else:

   if d_sq < diff_r_sq: 0 points.

   elif d_sq == diff_r_sq: 1 point.

   else: 2 points.

This way, we avoid floating points and use integer arithmetic.

So now, the code can be structured as follows:

Read n.

Read the n circles.

Compute V:

Initialize V =0.

For each pair of circles (i,j), i < j:

   compute the number of intersections between them.

   add that number to V.

If V ==0:

   print(n+1)

Else:

   compute E:

   For each circle:

      count = sum of intersections between this circle and all others.

      if count ==0:

          E +=1

      else:

          E += count

   F = E - V +2

   print(F)

So this is the code structure.

Now, implement this in Python.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    import sys
    input = input_stream.read().split()
    n = int(input[0])
    circles = []
    idx = 1
    for _ in range(n):
        x = int(input[idx])
        y = int(input[idx+1])
        r = int(input[idx+2])
        circles.append((x, y, r))
        idx +=3

    # Compute V
    V = 0
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            x1, y1, r1 = circles[i]
            x2, y2, r2 = circles[j]
            dx = x2 - x1
            dy = y2 - y1
            d_sq = dx*dx + dy*dy
            sum_r = r1 + r2
            sum_r_sq = sum_r * sum_r
            diff_r = abs(r1 - r2)
            diff_r_sq = diff_r * diff_r

            if d_sq > sum_r_sq:
                points = 0
            elif d_sq == sum_r_sq:
                points = 1
            else:
                if d_sq < diff_r_sq:
                    points = 0
                elif d_sq == diff_r_sq:
                    points = 1
                else:
                    points = 2
            V += points
            pairs.append((i, j, points))
    
    if V == 0:
        print(n + 1, file=output_stream)
        return

    # Compute E
    E = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            # Find pair (min(i,j), max(i,j))
            a, b = (i, j) if i < j else (j, i)
            for p in pairs:
                if p[0] == a and p[1] == b:
                    cnt += p[2]
                    break
        if cnt == 0:
            E += 1
        else:
            E += cnt

    F = E - V + 2
    print(F, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
0 0 2
3 0 2
6 0 2
""",
            "output": \
"""\
6
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
    import sys
    input = input_stream.read().split()
    n = int(input[0])
    circles = []
    idx = 1
    for _ in range(n):
        x = int(input[idx])
        y = int(input[idx+1])
        r = int(input[idx+2])
        circles.append((x, y, r))
        idx +=3

    # Compute V
    V = 0
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            x1, y1, r1 = circles[i]
            x2, y2, r2 = circles[j]
            dx = x2 - x1
            dy = y2 - y1
            d_sq = dx*dx + dy*dy
            sum_r = r1 + r2
            sum_r_sq = sum_r * sum_r
            diff_r = abs(r1 - r2)
            diff_r_sq = diff_r * diff_r

            if d_sq > sum_r_sq:
                points = 0
            elif d_sq == sum_r_sq:
                points = 1
            else:
                if d_sq < diff_r_sq:
                    points = 0
                elif d_sq == diff_r_sq:
                    points = 1
                else:
                    points = 2
            V += points
            pairs.append((i, j, points))
    
    if V == 0:
        print(n + 1, file=output_stream)
        return

    # Compute E
    E = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            # Find pair (min(i,j), max(i,j))
            a, b = (i, j) if i < j else (j, i)
            for p in pairs:
                if p[0] == a and p[1] == b:
                    cnt += p[2]
                    break
        if cnt == 0:
            E += 1
        else:
            E += cnt

    F = E - V + 2
    print(F, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
0 0 2
2 0 2
1 1 2
""",
            "output": \
"""\
8
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

Sample Input 3:

3

0 0 2

2 0 2

1 1 2

Each pair:

0 and1: distance squared = (2)^2 +0=4. sum_r=4. d_sq =4 → sum_r_sq=16. 4 <16 → check difference. sum_r is 4, diff_r=0. So d_sq (4) > diff_r_sq (0) → 2 points.

0 and2: distance squared (1)^2 + (1)^2 = 2. sum_r=4. sum_r_sq=16. 2 <16. diff_r_sq=0. 2>0 → 2 points.

1 and2: distance squared (1)^2 + (1)^2 =2. sum_r=4 → 2 points.

So each pair contributes 2 points. V=2+2+2=6.

E:

Each circle has 2+2=4 points.

So E=4+4+4=12.

F=12-6+2=8 → correct.

Another test case: two separate circles.

n=2, each has no intersections. V=0 → output 2+1=3.

Another test case: two circles intersecting in two points. V=2. E=2+2=4. F=4-2+2=4.

Another test case: three circles, two intersecting and one separate.

V=2. E=2+2+1=5. F=5-2+2=5.

Which is correct.

So the code works.
</think>

```python
def main():
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    circles = []
    idx = 1
    for _ in range(n):
        x = int(input[idx])
        y = int(input[idx+1])
        r = int(input[idx+2])
        circles.append((x, y, r))
        idx +=3

    # Compute V
    V = 0
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            x1, y1, r1 = circles[i]
            x2, y2, r2 = circles[j]
            dx = x2 - x1
            dy = y2 - y1
            d_sq = dx*dx + dy*dy
            sum_r = r1 + r2
            sum_r_sq = sum_r * sum_r
            diff_r = abs(r1 - r2)
            diff_r_sq = diff_r * diff_r

            if d_sq > sum_r_sq:
                points = 0
            elif d_sq == sum_r_sq:
                points = 1
            else:
                if d_sq < diff_r_sq:
                    points = 0
                elif d_sq == diff_r_sq:
                    points = 1
                else:
                    points = 2
            V += points
            pairs.append((i, j, points))
    
    if V == 0:
        print(n + 1)
        return

    # Compute E
    E = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i == j:
                continue
            # Find pair (min(i,j), max(i,j))
            a, b = (i, j) if i < j else (j, i)
            for p in pairs:
                if p[0] == a and p[1] == b:
                    cnt += p[2]
                    break
        if cnt == 0:
            E += 1
        else:
            E += cnt

    F = E - V + 2
    print(F)

if __name__ == "__main__":
    main()
```
