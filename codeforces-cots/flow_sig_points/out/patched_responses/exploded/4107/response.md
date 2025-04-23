<think>
Okay, I need to solve this problem where I have to count the number of triangles formed by n distinct points that have a non-zero area. The key here is that three points form a valid triangle if they are not colinear. So the problem reduces to counting all triplets of points that are not colinear.

First, let's think about the approach. The naive way would be to check all possible triplets of points and count those that form a valid triangle. However, with n up to 2000, the number of triplets is C(2000,3) which is about 1.3e10. That's way too big to handle with a O(n^3) approach. So we need a smarter way.

Wait, how can we optimize this? Maybe, instead of checking all triplets, we can find for each pair of points how many points are colinear with them and subtract that from the total possible triplets.

The total number of possible triangles is C(n,3). Then, the answer should be the total minus the number of colinear triplets. But how do we compute the number of colinear triplets?

Hmm. Let's think. For a given line (i.e., a set of colinear points), if there are k points on that line, then the number of triplets in that line is C(k,3). So if we can find all lines that have at least three points, sum their C(k,3) values, and subtract that sum from the total C(n,3), we get the answer.

Yes, that makes sense. So the plan is:

1. Calculate the total number of possible triangles: total = n*(n-1)*(n-2)//6 if n >=3, else 0.
2. For each possible line formed by pairs of points, count how many points lie on that line.
3. For each such line with m points, add C(m,3) to a sum of invalid triplets.
4. Subtract this sum from the total to get the answer.

But how to efficiently compute the number of points on each line?

The problem is that each line can be represented in multiple ways (different pairs of points can define the same line), so we need a way to group all pairs that lie on the same line and count the points on each line.

But that's computationally expensive. Let's think of another way. For each point, we can compute the slope of the line formed with every other point, and count how many points share the same slope (and same line). But even this approach might have O(n^2) time, which for n=2000 is 4,000,000 operations. That's manageable.

Wait, but even for each point, we can consider all other points and compute the slope (or some representation of the line) relative to the current point, then group the counts. Then, for each group with count m (meaning m points are colinear with the current point), we can add C(m,2) to a temporary sum. Because for each such group of m points along with the current point, there are C(m,2) pairs that form a line. Then, for each line, each pair (a,b) on that line contributes to the count when considering a and b as the current points. But this way, each line is considered multiple times. Hmm, maybe this approach would overcount.

Alternatively, here's an idea: For each point, we can compute the number of points that are colinear with it for every possible direction (slope). Then, for each such direction, if there are m points (including itself), then the line through this point with that slope has m points. But each line is considered once per point on it, so when we process all points, each line will be counted multiple times. For example, a line with k points will be processed k times. Each time, when we process one of the points, we find that there are k-1 other points on the same line. So the sum over all points of C(k-1, 2) (where k is the number of points on the line) would give us the total number of colinear triplets. But wait, let's see:

Each line with k points has C(k,3) colinear triplets. Each triplet is counted exactly once. However, if we process each point on the line, and for each such point, compute the number of pairs of other points on the same line (which is C(k-1,2)), then summing over all points on all lines would give sum_{lines} k * C(k-1,2) = sum_{lines} k*( (k-1)(k-2)/2 ) ). But for a line with k points, this term is k*(k-1)(k-2)/2 = 3 * C(k,3). So summing over all lines, this approach would give 3 times the total number of colinear triplets. Therefore, dividing by 3 would give the correct count.

Wait, let me check with an example. Suppose a line has 4 points. Then the number of colinear triplets is C(4,3) =4. For each of the 4 points, we compute C(3,2) =3. Summing 4*3=12. Then 12 /3 =4, which is correct. So yes, the sum over all points (for each point, the sum over all lines through that point of C(m,2) where m is the number of points on the line (including the current point)) would be 3* total_colinear_triplets. So the total_colinear_triplets is (sum_over_all_points_of_C(m-1,2 )) / 3.

So the approach would be:

For each point i:

   Create a dictionary to count the number of points that have the same slope relative to point i.

   For each other point j:

      compute the slope (dx, dy) between i and j, reduced to its simplest form (e.g., divide by gcd of dx and dy). Also, handle vertical lines (dx=0) and horizontal (dy=0) properly.

      For the same slope, increment the count in the dictionary.

   Then, for each key in the dictionary (which represents a group of points colinear with i):

      m = count + 1 (since point i is also on the line)

      add C(m-1, 2) to a running total (sum_colin).

Once all points are processed, sum_colin would be 3 * total_colinear_triplets. So the answer is total_triplets - (sum_colin //3).

This seems manageable. Now, the key steps are:

1. How to represent the slope in a way that can be used as a key in a dictionary. For example, two points j and k that are colinear with i would have the same slope representation.

2. How to handle vertical lines (where dx is zero) and horizontal lines (dy is zero), and also lines with positive and negative slopes. Also, need to represent them in a normalized form so that different pairs that form the same line have the same key.

So, for each pair (i,j), the direction vector (dx, dy) can be simplified by dividing both dx and dy by their greatest common divisor (gcd), but we also need to handle the sign. For example, (2,4) can be reduced to (1,2), but if dx and dy are both negative, like (-2,-4), the simplified would be (1,2) as well. Wait, no. Let's see: dx is j.x - i.x, dy is j.y - i.y.

We need to compute the delta x and delta y between i and j. Then, to normalize the direction vector, we can divide both dx and dy by their gcd. However, we need to take care of the sign. For example, dx=2, dy=4: gcd is 2, so dx/gcd=1, dy/gcd=2. Similarly, dx=-2, dy=-4: gcd is 2, dx/gcd is -1, dy/gcd is -2. But these two represent the same line. Wait, no. The direction vectors (1,2) and (-1,-2) are considered the same line in terms of slope. Because the line through i and j is the same as the line through j and i. So for the purpose of grouping points on the same line, we need to represent the direction in a way that (dx, dy) and (-dx, -dy) are considered the same.

Wait, but how? For example, if two points j and k are colinear with i, then the lines i-j and i-k must have the same slope. So the direction vector from i to j and i to k must be colinear. So the direction vectors (dx, dy) and (dx', dy') must be scalar multiples. Therefore, to normalize the direction, we can compute the gcd of dx and dy, divide both by the gcd, but also ensure that the direction is represented in a standard way, such as making the gcd positive. For example, if the gcd is positive, then the direction is (dx/gcd, dy/gcd). Otherwise, if the gcd is negative (but how?), but dx and dy are both positive or negative. Wait, the gcd is always positive. Because the gcd of two integers is the greatest positive integer that divides them. So when you compute dx and dy, you can take their absolute values for the gcd? Wait, no. Wait, gcd is computed as the greatest common divisor, considering the signs. For example, gcd(-2, 4) is 2. Because the divisors of -2 are ±1, ±2, and divisors of 4 are ±1, ±2, ±4. So the greatest common divisor in absolute terms is 2.

So to normalize dx and dy, we can compute the greatest common divisor of dx and dy (using their absolute values?), but perhaps we need to normalize the direction vector by dividing by the gcd and ensuring that the direction is represented in a standard way, such that (dx, dy) and (-dx, -dy) are considered the same direction. Wait, no. Because the line through i and j is the same as the line through j and i, but when you compute the direction vector from i to j, it's (dx, dy), and from i to k, it's (dx', dy'). So for two points j and k to be colinear with i, the vectors (dx, dy) and (dx', dy') must be colinear, i.e., scalar multiples of each other.

Therefore, the key idea is to represent the slope in a normalized way, such that all colinear vectors have the same key. So for a given delta (dx, dy), we can compute the greatest common divisor g of dx and dy. Then, we divide dx and dy by g to get (a, b). However, we have to be careful about the signs. For example, if dx is positive and dy is negative, but the gcd is positive, dividing by g would result in (dx/g, dy/g). But if dx and dy are both negative, then (dx/g, dy/g) would be (positive, positive) if g is positive. Wait, but dx and dy could be (2,4), (4,8), etc. So how to normalize?

Wait, perhaps the correct approach is to compute the gcd and divide by it, but then represent the direction as a tuple (a, b) where the greatest common divisor of a and b is 1. But in order to avoid having different representations for the same direction, for example (2,4) and (1,2) (after normalization), but wait no, if (dx, dy) is (2,4), then the gcd is 2, so a is 1, b is 2. So that's correct.

But what about (dx, dy) being (-2, -4)? The gcd is 2, so dividing gives (-1, -2). But this is a different tuple than (1, 2), but in reality, the direction is the same line. Wait, no. Because the line through i and j is the same regardless of the order of the points. So if (dx, dy) is (-2,-4) from i to j, then the line is the same as (2,4) if you go from j to i. But when considering all points j and k in relation to i, the direction from i to j and i to k must be colinear. So for the purpose of grouping all points that are colinear with i, the direction from i to j must be the same as the direction from i to k. Therefore, in this case, the normalized direction should be the same if the vectors are scalar multiples. So in this case, (dx, dy) = (2,4) and (-2,-4) would have the same normalized direction (1,2) and (-1,-2) respectively. But these are different keys in the dictionary, even though they represent colinear lines. This would be a problem.

So how to handle this? For example, if two points j and k lie on the line through i, but the direction from i to j is (2,4) and from i to k is (-2,-4), then the normalized directions would be (1,2) and (-1,-2), which would be stored as separate keys. But in reality, these points are colinear with i, so they should be counted together.

Ah, this is a problem. So the current approach of normalizing by dividing by gcd(dx, dy) may not capture all points colinear with i. Because, for example, if two points are in opposite directions from i, their normalized directions would be different, but they are still colinear. Wait, but in that case, the line through i and j is the same as the line through i and k. So if j and k are on the same line through i, then their direction vectors from i must be scalar multiples. So if the direction vectors are (a, b) and (c, d) from i, then there must be some scalar k such that c = k*a, d =k*b. So for example, (2,4) and (-2,-4) are scalar multiples (k=-1). So in this case, their normalized vectors would be (1,2) and (-1,-2). But these are different keys. So the current approach would not group them as part of the same line.

This is a problem. So how to normalize the direction vector such that opposite directions are considered the same?

Hmm. Maybe we can normalize by making sure that the greatest common divisor is positive, and then, for example, divide both dx and dy by their gcd, and then ensure that the direction is represented in a way that the denominator is positive. Wait, perhaps the key is to represent the slope as a reduced fraction, but in a normalized form where the denominator is positive. For example, for a line with dx=2, dy=4, the slope is 2/4 = 1/2. So the normalized slope is (1,2). For a line with dx=-2, dy=-4, the slope is (-2)/(-4) = 0.5 = 1/2. So the normalized slope is (1,2). So in this case, the same line would have the same key.

So the way to handle this is to compute the gcd of dx and dy, then divide both by the gcd, but then also ensure that the denominator (or numerator) is positive. Wait, perhaps we can normalize the direction vector by dividing dx and dy by their gcd, and then ensuring that the denominator is positive. Wait, not sure. Let's think of dx and dy as the direction vector. To normalize, we can compute the gcd of dx and dy. Let's call this g. Then, we divide dx by g, dy by g. Then, if g is negative, the signs of dx and dy would flip. Wait, but the gcd is always positive. Because the gcd is defined as the greatest positive integer that divides both numbers. So when we compute the gcd of dx and dy, regardless of their signs, the result is positive. For example, gcd(-2,4) is 2. So dx/gcd and dy/gcd would be (-1, 2). So to normalize, perhaps we can also ensure that either dx or dy is positive. Wait, but how?

Alternatively, to avoid having (a, b) and (-a, -b) considered different, perhaps when normalizing, we can ensure that the greatest common divisor is positive and that the direction is represented in a way that the leading term (like the x-component) is positive. For example, if the normalized x-component is zero (vertical line), then we can represent the direction as (0,1). Otherwise, if the x-component is non-zero, we can divide both components by their gcd and then make sure that the x-component is positive. If the x-component is zero, then the y-component is non-zero, and we can make sure the y-component is positive.

Yes, that makes sense. So the steps to normalize (dx, dy) are:

1. Compute g = gcd of dx and dy. Since dx and dy can be negative, but the gcd is positive.

2. If g is zero, that means dx and dy are both zero, but in our problem, points are distinct, so this case is impossible.

3. Otherwise, divide dx and dy by g to get (a, b) = (dx/g, dy/g).

4. Now, to normalize the direction, if (a, b) is (0, something), then it's a vertical line. So we can represent it as (0, 1) if b is positive, or (0, -1) if b is negative. Wait, but in that case, (0, -1) and (0, 1) are different. So perhaps for vertical lines (a=0), we can set the direction to (0, 1) if b>0, otherwise (0, -1). Then, if two points are in opposite vertical directions, they would be considered as same line? No. Because for vertical lines, all points on the same vertical line have dx=0, but dy can vary. Wait, no. If two points are on the same vertical line through point i, then their direction from i must have dx=0, but dy can be any value. So for example, point j has (dx=0, dy=2) from i, and point k has (dx=0, dy=-3) from i. Then, after normalization, j's direction is (0,1) and k's direction is (0, -1). So they would be considered different, but they are on the same vertical line. So this approach would group them as different, which is wrong.

Ah, this is a problem. So the normalization approach for vertical lines is incorrect here. Similarly for horizontal lines.

So the solution is: for any line, whether it's vertical, horizontal, or diagonal, we need to normalize the direction vector such that all points on the same line through i are grouped together.

How to do that?

An alternative approach is to represent the direction as a pair (a, b) in their simplest form, but ensuring that the direction is considered the same regardless of the sign. So, for example, (a, b) and (-a, -b) would be considered the same. But how to represent them as the same key in the dictionary?

Alternatively, for each direction (a, b), we can choose to represent it as (a/gcd, b/gcd) where the gcd is taken as a positive integer, and then ensure that either a is positive, or if a is zero, then b is positive.

Wait, perhaps the standard way to represent the direction is to divide by the gcd, then make sure that the greatest common divisor of a and b is 1, and that the direction is normalized such that the leading non-zero component is positive.

Yes. So here's the plan:

Compute dx = xj - xi, dy = yj - yi.

If dx and dy are both zero, then it's the same point, but the problem states that all points are distinct, so this can't happen.

Compute g = gcd of dx and dy. But since dx and dy can be negative, the g is positive.

Then, divide dx and dy by g, resulting in a reduced direction vector (a, b) = (dx/g, dy/g).

Now, to handle the sign: if the reduced (a, b) is such that a is 0 (vertical line), then we can represent the direction as (0, 1) if b is positive, else (0, -1). Wait, but even that would split points on the same vertical line into two groups. For example, points j and k are colinear with i in a vertical line. j is above i (dy positive), k is below (dy negative). Then, their normalized directions would be (0,1) and (0, -1), treated as different keys, leading to incorrect grouping.

That's a problem. So how to handle vertical lines?

Wait, vertical lines have dx=0, but dy can be any value. So for any two points on the same vertical line through i, their direction vectors from i would have dx=0. So the normalized direction would be (0, sign(dy)), but that's not correct.

Alternatively, for vertical lines, the direction can be represented as (0, 1), since dx is 0 and dy can be represented as 1 after division by the gcd.

Wait, let's take an example. Suppose i is at (0,0), j is at (0,2). Then dx is 0, dy is 2. The gcd is 2. So a = 0, b = 1 (since 2/2=1). So direction is (0, 1). Now, if there's another point k at (0, -3). The dx is 0, dy is -3. The gcd is 3. So a=0, b=-1. So direction is (0, -1). But these two points j and k are on the same vertical line through i, but their direction keys are different. So the approach would not group them together.

So how can we normalize vertical lines so that all points on the same vertical line are grouped together?

Perhaps for vertical lines (dx=0), we can set the direction to (0, 1) regardless of the sign. So whenever dx is 0, we normalize the direction as (0,1). How?

Let's see. For a vertical line, dx is 0. So dy can be positive or negative. Compute g = abs(dy). Then, the normalized direction would be (0, 1) if dy is positive, (0, -1) if dy is negative. But that's not right.

Alternatively, for any vertical line, the direction is (0, 1). So when dx is 0, the direction is represented as (0, 1). How?

Wait, perhaps we can make sure that for vertical lines, the direction is (0,1), regardless of the actual dy. How? Because the direction vector is (0, dy), and after dividing by gcd (which is |dy|), the direction becomes (0, 1) if dy is positive, (0, -1) if dy is negative. So in order to normalize this, perhaps for vertical lines, we can take the absolute value of dy. But that's not correct, because (0, 1) and (0, -1) are different directions.

Hmm, this is getting complicated. Maybe the problem is in the approach of normalizing the direction vectors. Because two points j and k that are colinear with i but in opposite directions would have different direction vectors, but they are on the same line. So the current approach would not group them together.

So, to solve this, perhaps we need to find for each pair (i,j), the line equation, and group all points that lie on the same line. But how to represent the line equation in a way that can be used as a key in a dictionary?

The standard way to represent a line is using the coefficients (A, B, C) of the line equation Ax + By + C =0. But the same line can be represented by multiple (A, B, C) triples (since multiplying all three by a non-zero constant gives the same line). So we need a way to normalize the coefficients.

Alternatively, we can represent the line by its reduced coefficients. For example, for the line passing through points i and j, we can compute the coefficients (A, B, C) such that:

A = yj - yi

B = xi - xj

C = xj*yi - xi*yj

Then, the line equation is Ax + By + C =0.

To normalize this, we can divide A, B, C by their greatest common divisor and ensure that the leading coefficient is positive. However, the GCD of A, B, C may not be the same as the GCD of A and B. Wait, for example, if A=2, B=4, C=6, then the GCD is 2, and dividing by 2 gives (1,2,3). So the line equation becomes x +2y +3=0. But this approach may not work when C is not a multiple of the GCD of A and B.

Alternatively, perhaps we can compute the GCD of A, B, and C, but that's complicated because C is derived from A and B. Wait, for the line through points i and j, the line equation is (yj - yi)(x - xi) - (xj - xi)(y - yi) = 0. Expanding this gives (yj - yi)x - (xj - xi)y + [ (xj - xi) yi - (yj - yi) xi ] =0. So A = (yj - yi), B = -(xj - xi), C = (xj - xi) yi - (yj - yi) xi.

The line equation can be written as A*(x - xi) + B*(y - yi) = 0. So for any point (x,y) on the line, this holds.

The coefficients A and B are the same as the direction vector (dx, dy) = (xj - xi, yj - yi), but B is -dx, and A is dy. So the line's direction is (dx, dy), and A and B are (dy, -dx). So the line equation can be represented as dy*(x - xi) - dx*(y - yi) =0.

Now, the GCD of A and B is GCD(dy, -dx) = GCD(dy, dx) (since GCD(a,b) = GCD(a, -b)). So to normalize the line equation, we can divide A, B, C by their GCD (including C?), but this might be tricky.

Alternatively, since the line is determined by (A, B, C), but for the same line, different representations can be achieved by multiplying by a non-zero scalar. So to normalize the coefficients, we can compute the GCD of A, B, and C, then divide each by it. Then, ensure that the leading non-zero coefficient is positive.

But how to compute the GCD of three numbers? Well, the GCD of A, B, and C is the same as GCD(GCD(A,B), C).

But even this approach may not be feasible for the problem's constraints. Because for each pair of points (i,j), we would have to compute the line's normalized coefficients and use them as a key in a dictionary. Then, for each line, we can track how many points are on it. But for n=2000, the number of pairs is 2000*1999/2 = ~2e6 pairs. So for each pair, compute the line's normalized representation, and then for each line, count the number of points that lie on it. But how to efficiently count the number of points on each line.

Wait, but for the problem's purposes, we need to count all triplets of points that lie on the same line. So for a line with k points, there are C(k,3) such triplets. So perhaps the correct approach is to find all lines with at least three points, compute C(k,3) for each, and sum them all. Then subtract that sum from the total number of triplets.

But the problem is how to efficiently find all lines and the number of points on each line.

The approach would be:

1. For all lines in the set of points, determine how many points lie on each line.

2. For each line with k points, add C(k,3) to the invalid count.

3. The answer is total triplets (C(n,3)) minus the invalid count.

But how to compute step 1 efficiently.

An efficient way is to, for each line, find all points that lie on it. But enumerating all lines is O(n^2) lines (since each pair defines a line), and for each line, checking all points is O(n), which would lead to O(n^3) time. Which is not feasible for n=2000 (2e9 operations).

So we need a better way.

Alternative approach: For each point, we can compute the lines that pass through that point and any other point, and track the maximum number of points on any such line. But again, this seems O(n^2) per point, leading to O(n^3) time.

Hmm.

Alternatively, for each point i, we can compute the maximum number of points colinear with i and some other point j. Then, sum for all such lines. But how?

Wait, the problem is that the same line can be considered multiple times. For example, line L is defined by points i and j, and line L is also defined by points i and k, etc. So we need to find a way to count each line exactly once.

But this seems challenging. So perhaps the previous approach of using the direction vectors, but normalizing in a way that accounts for opposite directions, is the way to go.

Let's re-examine the direction normalization. The key problem is that for a line passing through i, j, and k, the directions from i to j and from i to k may have different normalized representations if the direction vectors are in opposite directions.

So perhaps the correct way to normalize the direction is to represent it in a way that (dx, dy) and (-dx, -dy) are considered the same. So for example, for any direction (a, b), we can represent it as (a/gcd, b/gcd) if a/gcd is positive, or (-a/gcd, -b/gcd) otherwise. So we can choose to normalize the direction so that the greatest common divisor is positive and the first non-zero component is positive.

Wait, here's a possible solution:

For each pair (i, j), compute dx = xj - xi, dy = yj - yi.

If dx and dy are zero, skip (but points are distinct, so this can't happen).

Compute the greatest common divisor (g) of dx and dy. Note that g is positive.

Divide dx and dy by g to get (a, b).

Now, to handle the direction, if (a, b) is (0, 1), then it's a vertical line upwards. If (a, b) is (0, -1), then vertical line downwards. But these are the same line. Wait, no. The line passing through i and j (dx=0, dy=2) is a vertical line. The line passing through i and k (dx=0, dy=-3) is the same vertical line. So in both cases, the direction vector normalized would be (0,1) and (0,-1). But they are the same line.

So to normalize the direction for vertical lines, perhaps we should represent the direction as (0, 1) regardless of the direction. Because the line is the same. But how?

Alternatively, for vertical lines (dx=0), the direction can be represented as (0, 1), and for all points on the same vertical line, their direction from i would have dx=0 and dy can be positive or negative, but after normalization, they would all be (0,1) or (0,-1). So this approach doesn't capture that.

So perhaps the way to handle vertical lines is to represent them as (0, 1). For non-vertical lines, we can represent the direction as (1, m), where m is the slope, but reduced to simplest terms. But even this may not work.

Alternatively, the line can be represented by its reduced slope and intercept. But for vertical lines, the slope is undefined, and the intercept is the x-coordinate.

But even then, the same line can be represented in different ways. For example, the vertical line x=5 is the same for all points on it, but if we compute the line from i and j, and then from i and k, they would both be x=xi, which is the same as x=5 if i is at (5, something).

But perhaps this is manageable. So for each pair (i, j), compute the line's equation in a normalized form and use it as a key. Then, for all points k, check if they are on that line.

But again, this would require O(n^2) lines and for each line, O(n) checks, leading to O(n^3) time.

Hmm. So I'm stuck between two options: a O(n^3) approach which is too slow, or a O(n^2) approach that requires correctly normalizing the direction vectors to avoid duplicate entries for the same line.

But the direction vector approach can be made to work if we can find a way to normalize the direction vectors such that colinear directions are grouped together.

Let's think again: For the line through i and j, any other point k that is colinear with i and j will have a direction vector (xk - xi, yk - yi) that is a scalar multiple of (dx, dy), where dx = xj - xi and dy = yj - yi. So the direction vectors from i to j and from i to k must be scalar multiples.

So, to normalize the direction vector, we can represent it as (a, b), where a and b are the smallest possible integers with the same ratio as dx and dy, and with a positive leading non-zero component.

For example:

dx=2, dy=4: a=1, b=2. Leading component is a=1 (positive). So normalized to (1,2).

dx=-2, dy=-4: a=1, b=2 (since dx/gcd is -2/2= -1, dy/gcd is -4/2=-2. Then, to make the leading non-zero component positive, multiply by -1: (1,2)).

dx=0, dy=5: a=0, b=1 (since dy/gcd=5/5=1. Leading component is dy, which is positive).

dx=0, dy=-3: a=0, b=1 (since dy/gcd is -3/3= -1. Multiply by -1 to make leading component positive).

So the normalization steps would be:

Compute dx = xj - xi, dy = yj - yi.

If dx and dy are both zero, skip (but points are distinct, so this can't happen).

Compute g = gcd of dx and dy. Since dx and dy can be negative, but the gcd is positive.

a = dx / g, b = dy / g.

Now, if a ==0:

   Then, the line is vertical. The direction is (0, 1) if b>0, else (0,-1). Wait, but if dy is negative, then after dividing by g, b could be -1. So to normalize vertical lines, we can set the direction to (0,1) by taking the absolute value of b. Or, perhaps for vertical lines, regardless of the sign of b, we can set it to (0,1). Because the direction is vertical, and the line is the same whether you go up or down. So for vertical lines, the direction can be represented as (0,1).

Wait, no. Because in that case, points j and k that are on the same vertical line through i would have direction vectors (0,1) and (0,1), leading to the same key. Wait, but dx is zero for both, so after normalization, if dx is zero, then the direction is (0,1) regardless of dy's sign. How?

Let me think: For a vertical line, dx is zero. So dy can be positive or negative. For example, for dx=0, dy=5: a=0, b=5/gcd(0,5)=5. So dy/gcd is 5/5=1. So a=0, b=1. So direction is (0,1). For dx=0, dy=-3: gcd(0,3)=3. So a=0, b= (-3)/3 = -1. Then, since a is zero, we need to normalize to (0,1). So how to handle this?

Ah, perhaps the correct way is to set the direction for vertical lines as (0,1), and for non-vertical lines, to have the direction vector (a, b) where a is positive, and a and b are co-prime.

So here's the plan:

After computing a and b as dx/g and dy/g:

If a is zero (vertical line):

   Then the direction is (0, 1). Because dy is non-zero (points are distinct), so after dividing by g, b is either 1 or -1. But regardless, we can set the direction to (0,1) by taking the absolute value of b. So regardless of the direction (up or down), the vertical line is represented as (0,1).

Else (non-vertical line):

   If a < 0, multiply both a and b by -1 to make a positive.

   If a ==0 (can't happen now), handle vertical case.

   Then, ensure that the GCD of a and b is 1 (which it already is, since we divided by g).

So this way, for vertical lines, all points on the same vertical line through i will have the same direction key (0,1). For non-vertical lines, directions are normalized such that a is positive, and the direction vector is in its simplest form.

This would correctly group points that are colinear with i and j.

Let me test this:

Case 1: i is (0,0), j is (0,2). dx=0, dy=2. g=2. a=0, b=1. Since a is zero, direction is (0,1).

Case 2: i is (0,0), j is (0,-3). dx=0, dy=-3. g=3. a=0, b=-1. Since a is zero, direction is (0,1) (because we take absolute of b? Or because we set to (0,1) regardless). Wait, according to the plan, when a is zero, direction is (0,1). So regardless of the sign of b, the direction is (0,1). But wait, how?

The steps are:

If a is zero (vertical line), then set the direction to (0,1).

But how to compute that. Let's see:

dx = 0, dy = -3.

g = gcd(0, -3) = 3.

a = 0 /3 = 0.

b = (-3)/3 = -1.

But then, since a is zero, we set the direction to (0,1). So the normalized direction is (0,1), regardless of b's original value.

Yes. So in this case, j is (0,-3) would be normalized to (0,1).

Thus, any point on the same vertical line as i would have the direction (0,1) when processed with i.

Similarly, for a non-vertical line:

Case 3: i is (0,0), j is (2,4). dx=2, dy=4. g=2. a=1, b=2. a is positive, so direction is (1,2).

Case 4: i is (0,0), j is (-2,-4). dx=-2, dy=-4. g=2. a=-1, b=-2. Since a is negative, multiply by -1: a=1, b=2. So direction is (1,2).

Thus, points j and k in opposite directions from i on the same line would have the same normalized direction.

So this approach would group all points colinear with i into the same direction key.

Now, this seems correct.

So the steps are:

For each point i:

   Create a dictionary to count the number of points with each normalized direction.

   For each j != i:

      compute dx = xj - xi, dy = yj - yi.

      compute g = gcd of dx and dy. Since dx and dy can't be both zero, g is positive.

      a = dx / g, b = dy / g.

      if a ==0:

          normalized direction is (0, 1)

      else:

          if a < 0:

              a *= -1

              b *= -1

          normalized direction is (a, b)

      add this normalized direction to the dictionary, incrementing the count.

   After processing all j for i, for each direction in the dictionary:

      m = count + 1 (since i is on the line)

      sum_colin += C(m-1, 2) # because for this line through i, there are m points, and for each pair (j,k) in these m points, they form a colinear triplet with i. So the number of colinear triplets contributed by this line is C(m-1, 2).

   But wait, for each line through i with m points, the number of colinear triplets that include i is C(m-1, 2), because any two other points in the line, when combined with i, form a colinear triplet. But in the previous approach, when we process all points i, for each line through i, the sum_colin accumulates C(m-1,2) for each i. But how does this relate to the total number of colinear triplets?

Wait, each colinear triplet (i,j,k) is counted once when processing i, once when processing j, and once when processing k. So summing C(m-1,2) for all lines through all points would give 3 * total_colinear_triplets. Because each triplet is counted three times.

So, sum_colin = 3 * total_colinear_triplets.

Thus, total_colinear_triplets = sum_colin // 3.

Therefore, the answer is total_triplets - sum_colin //3.

So, the steps are:

Compute total_triplets = n*(n-1)*(n-2)//6 if n >=3 else 0.

Compute sum_colin as the sum over all points i, for each line through i, of C(m-1, 2), where m is the number of points on the line (including i).

Then, the answer is total_triplets - sum_colin //3.

Now, the code needs to implement this.

Now, let's think about the code.

First, for each point i in 0..n-1:

   Create a dictionary called slopes.

   For each j in 0..n-1, j !=i:

      dx = x[j] - x[i]

      dy = y[j] - y[i]

      compute g = gcd(dx, dy). But since dx and dy can be negative, how to compute the gcd in Python?

      In Python, the math.gcd function returns the absolute value of the gcd.

      For example:

      import math

      math.gcd(-2,4) returns 2.

      So yes, math.gcd returns the absolute value.

      So, compute g = math.gcd(dx, dy)

      if g ==0: impossible, since j !=i.

      a = dx // g

      b = dy // g

      if a ==0:

          slope = (0,1)

      else:

          if a <0:

              a = -a

              b = -b

          slope = (a, b)

          # Now, compute the GCD of a and b again?

          # Wait, no. Because dx and dy were divided by their gcd. So a and b should be coprimes.

          # For example, dx =4, dy=6. gcd is 2. a=2, b=3. Then, compute their gcd: gcd(2,3)=1.

          # So, a and b are coprimes.

      So the slope is (a, b) as computed.

      Then, increment the count for this slope in the dictionary.

   After processing all j:

      For each slope in the slopes dictionary:

          cnt = slopes[slope]

          m = cnt + 1 (because cnt is the number of other points on this line, so including i, it's cnt +1)

          sum_colin += (m-1)*(m-2)//2  # C(m-1,2)

Finally, answer = total_triplets - sum_colin //3.

So, the code would look like:

import math

n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

total = 0

if n >=3:

    total = n*(n-1)*(n-2) //6

sum_colin =0

for i in range(n):

    xi, yi = points[i]

    slopes = {}

    for j in range(n):

        if i ==j:

            continue

        xj, yj = points[j]

        dx = xj - xi

        dy = yj - yi

        g = math.gcd(dx, dy)

        a = dx // g

        b = dy // g

        if a ==0:

            # vertical line

            slope = (0,1)

        else:

            if a <0:

                a = -a

                b = -b

            slope = (a, b)

        if slope in slopes:

            slopes[slope] +=1

        else:

            slopes[slope] =1

    # Now, for each slope in slopes:

    for cnt in slopes.values():

        m = cnt +1

        sum_colin += (m-1)*(m-2)//2

ans = total - sum_colin//3

print(ans)

But wait, let's test this with the first sample input.

Sample input 1:

4

0 0

1 1

2 0

2 2

Total triplets is C(4,3) =4.

sum_colin should be 3 * (number of colinear triplets). Let's see.

For each point i:

i=0 (0,0):

   j=1: dx=1, dy=1. g=1. a=1, b=1. a is positive. slope (1,1).

   j=2: dx=2, dy=0. g=2. a=1, b=0. a is positive. slope (1,0).

   j=3: dx=2, dy=2. g=2. a=1, b=1. slope (1,1).

   So slopes for i=0: (1,1) appears twice (j=1 and j=3), (1,0) once (j=2).

   For (1,1), cnt=2. m=3. (3-1)*(3-2)/2 = 2*1/2=1. So sum_colin +=1.

   For (1,0), cnt=1. m=2. (2-1)*(2-2)/2 = 0. So sum_colin +=0.

   So sum_colin for i=0 is 1.

i=1 (1,1):

   j=0: dx=-1, dy=-1. g=2 (since dx is -1, dy -1: gcd(1,1)=1. a =-1//1= -1, dy is -1//1= -1. Since a is negative, multiply by -1: a=1, b=1. slope (1,1).

   j=2: dx=1, dy=-1. g=1. a=1, dy=-1. a is positive, so slope is (1,-1).

   j=3: dx=1, dy=1. g=1. a=1, b=1. slope (1,1).

   So slopes for i=1:

       (1,1) has cnt=2 (j=0 and j=3), (1,-1) cnt=1 (j=2).

       For (1,1): m=3. (3-1)*(3-2)/2= 1 → sum_colin +=1.

       For (1,-1): m=2. 0 → sum_colin +=0.

       Total sum_colin +=1.

   So sum_colin now is 2.

i=2 (2,0):

   j=0: dx=-2, dy=0. g=2. a=-1, dy=0. a is negative → multiply by -1: a=1, dy=0. slope (1,0).

   j=1: dx=-1, dy=1. g=1. a=-1, dy=1. a is negative → a=1, dy=-1. slope (1,-1).

   j=3: dx=0, dy=2. g=2. a=0 → slope (0,1).

   So slopes:

       (1,0): cnt=1 (j=0). m=2 → (1*0)/2=0. sum_colin +=0.

       (1,-1): cnt=1 (j=1). m=2 → 0.

       (0,1): cnt=1 (j=3). m=2 → 0.

   Sum_colin remains 2.

i=3 (2,2):

   j=0: dx= -2, dy=-2. g=2 → dx/g =-1, dy/g =-1. a is -1 → multiply by -1: a=1, b=1. slope (1,1).

   j=1: dx=0, dy=0. No, but j=1 is different. Wait, dx=2-1=1, dy=2-1=1. dx=1, dy=1. g=1. a=1, b=1. slope (1,1).

   j=2: dx=0, dy=-2. dx=0 → slope (0,1).

   So slopes:

       (1,1) cnt=2 (j=0 and j=1). m=3 → (3-1)(3-2)/2 = 1 → sum_colin +=1.

       (0,1) cnt=1 (j=2). m=2 → 0.

   So sum_colin +=1. Now sum_colin is 3.

Total sum_colin =1 (i=0) +1 (i=1) +0 (i=2) +1 (i=3) =3.

sum_colin//3=1.

Total triplets is4 → 4-1=3. Which matches the sample output.

Yes, that works.

Another sample:

Sample input 2:

3

0 0

1 1

2 0

Total triplets is 1.

sum_colin: let's see.

Each line:

For each i:

i=0:

   j=1: dx=1, dy=1. a=1/1=1, b=1/1=1. slope (1,1).

   j=2: dx=2, dy=0. g=2. a=1, dy=0. slope (1,0).

   slopes: (1,1):1 → m=2 → 0; (1,0):1 → m=2 → 0.

   sum_colin +=0+0=0.

i=1:

   j=0: dx=-1, dy=-1. a=1, b=1. slope (1,1).

   j=2: dx=1, dy=-1. a=1, dy=-1. slope (1,-1).

   sum_colin +=0 (m=2 for (1,1)) +0 (m=2 for (1,-1)).

i=2:

   j=0: dx=-2, dy=0 → a=1, dy=0. slope (1,0).

   j=1: dx=-1, dy=1. a=1, dy=-1. slope (1,-1).

   sum_colin +=0 for each.

sum_colin =0.

sum_colin//3=0. So answer is 1-0=1.

Which matches the sample.

Another sample: n=1. Output is 0.

So the code works.

Now, the code has to be efficient. For n=2000, the outer loop runs 2000 times. The inner loop for each i is 1999 iterations. Each iteration computes dx, dy, gcd, a and b, and updates the dictionary.

The gcd computation in Python is O(1) but with some cost. For 2000*2000=4e6 iterations, it's manageable.

The dictionary operations are O(1) average case. So the code should run within 4e6 operations, which should be manageable under 4 seconds.

Thus, the code should work.
</think>

```python
import math

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

if n < 3:
    print(0)
else:
    total = n * (n - 1) * (n - 2) // 6
    sum_colin = 0

    for i in range(n):
        xi, yi = points[i]
        slopes = {}
        for j in range(n):
            if i == j:
                continue
            xj, yj = points[j]
            dx = xj - xi
            dy = yj - yi
            g = math.gcd(dx, dy)
            a = dx // g
            b = dy // g

            if a == 0:
                slope = (0, 1)
            else:
                if a < 0:
                    a = -a
                    b = -b
                slope = (a, b)
            slopes[slope] = slopes.get(slope, 0) + 1

        for cnt in slopes.values():
            m = cnt + 1
            sum_colin += (m - 1) * (m - 2) // 2

    ans = total - sum_colin // 3
    print(ans)
```