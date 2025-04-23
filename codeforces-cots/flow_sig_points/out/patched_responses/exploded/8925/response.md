<think>
Okay, I need to solve this problem where I have to find the number of intersecting pairs of wires. Let's see the problem statement again. So each wire is the line formed by two poles. But if multiple poles lie on the same line, they all share the same wire. So two different wires intersect if they are not parallel and are not the same line. The task is to count all such pairs.

Hmm, so first, I need to find all the distinct lines formed by the given points. Then, for each pair of these distinct lines, check if they intersect (i.e., they are not parallel). The total count of such pairs is the answer.

The challenge is to efficiently represent each line uniquely so that we can count how many lines there are, and then compute the pairs.

The first step is to generate all possible lines formed by every pair of points. But wait, if three points are colinear, then all pairs (like AB, AC, BC) would form the same line. So we need a way to group all points that lie on the same line and represent them with a single line entry.

So, the plan is:

1. Enumerate all lines formed by pairs of points, but in a way that each line is uniquely represented once, regardless of the pair that generated it.
2. For all unique lines, compute how many pairs of lines are intersecting (i.e., not parallel and not the same line).

So, the key steps are:

- Find all unique lines.
- For each pair of unique lines, check if they are intersecting. Sum all such pairs.

Now, how to represent a line uniquely? Because different representations might cause the same line to be stored as different entries, which would lead to incorrect counts.

The standard way to represent a line is by using a canonical form. For example, the line equation can be represented by ax + by + c = 0, but normalized so that different representations of the same line are considered the same.

But how to normalize? Let's think.

The line can be represented by its coefficients (a, b, c) such that ax + by + c = 0. However, this representation isn't unique because multiplying all three coefficients by a non-zero scalar gives the same line.

So, to normalize, we can choose the smallest possible representation where a, b, c are integers with no common divisor, and the leading coefficient (the first non-zero among a, b) is positive. Alternatively, we can compute the reduced form of a, b, c.

But handling this in code can be a bit tricky, especially for vertical lines and horizontal lines.

Let's think of another approach. For two points (x1, y1) and (x2, y2), the line can be represented in terms of direction. The direction vector is (dx, dy) = (x2 - x1, y2 - y1). To avoid division by zero, we can represent the line using the reduced form of the direction vector, along with a point (to account for the position).

Wait, but even direction vectors may not be sufficient. For example, two different lines can have the same direction but different positions, but in that case, they are parallel.

Alternatively, the line can be represented by the coefficients a, b, c in the equation ax + by + c = 0. To compute this for a pair of points (x1,y1) and (x2,y2), we can use the formula:

a = y2 - y1
b = x1 - x2
c = x2 y1 - x1 y2

Then, the equation of the line is a(x - x1) + b(y - y1) = 0, which simplifies to a x + b y + c = 0. So for two points, these a, b, c can be computed. Then, we need to normalize these coefficients to get a unique representation for the same line.

The normalization steps would be:

1. Compute the greatest common divisor (gcd) of a, b, c. But since a and b are coefficients (dx and -dy), the direction is important. Wait, maybe we should compute the gcd of a, b, c and then divide all by that. But signs matter. For example, the line 2x + 2y + 2 = 0 is the same as x + y + 1 = 0. Also, if all coefficients are multiplied by -1, it's the same line. So the normalization would involve dividing by the gcd of the absolute values of a, b, c, and then ensuring that the leading coefficient is positive.

Alternatively, perhaps we can compute the coefficients as follows:

Compute the direction vector (dx, dy) = (x2 - x1, y2 - y1). Then, the line equation can be written as dy (x - x1) - dx (y - y1) = 0. Which simplifies to dy x - dx y + (dx y1 - dy x1) = 0. So the coefficients a, b, c are (dy, -dx, dx y1 - dy x1). Then, to normalize, we can divide a, b, c by their greatest common divisor (gcd of a, b, c), and ensure that the leading coefficient is positive.

Wait, but how do we compute the GCD of three numbers? The GCD of a, b, c can be found by taking the GCD of the GCD(a, b), and c). But the GCD of three numbers may not capture all common divisors, but perhaps it's sufficient.

Another point to consider: the line equation ax + by + c =0 is the same as (ka)x + (kb)y + (kc) = 0 for any non-zero k. So to normalize, we can divide a, b, c by their GCD and then make sure that the coefficients are in the simplest form with a positive leading coefficient.

So, steps for normalization:

1. For a line defined by two points (x1,y1) and (x2,y2), compute a = dy = y2 - y1, b = -dx = -(x2 - x1), c = dx * y1 - dy * x1. Then, the line is a x + b y + c = 0.

2. Compute the greatest common divisor (g) of a, b, c. But since a, b, c can be negative, we should take the absolute values first. For example, compute g = gcd(gcd(abs(a), abs(b)), abs(c)).

3. If g is not zero, divide a, b, c by g. But wait, if all are zero, but that's impossible because two distinct points can't have dx and dy both zero. So g will be non-zero.

Wait, for two distinct points, a and b can't both be zero. Because dx = x2 -x1 and dy = y2 -y1. So if dx and dy are both zero, the points are the same, but the problem states that all points are distinct. So a and b can't both be zero.

So, for each line, compute a, b, c. Then compute g as the GCD of the three. Then divide a, b, c by g to get the simplest form. But also, we need to ensure that the leading coefficient (the first non-zero among a, b, c) is positive. Wait, no. For example, the line 2x + 3y +4=0 is the same as -2x -3y -4=0. So to normalize, after dividing by g, we need to ensure that the coefficients are in a form where the greatest common divisor is 1, and the first non-zero coefficient is positive.

So the steps are:

Compute a, b, c as before.

Compute g = gcd of (a, b, c). But since a, b, c can be negative, compute the gcd of their absolute values.

Then, divide a, b, c by g. Then, find the first non-zero element among a, b. If all are zero, then c must be non-zero (but that's impossible, as two distinct points can't have a=0, b=0). Then, if the first non-zero element (a or b) is negative, multiply all by -1 to make it positive. Because, for example, a line represented by -a x -b y -c =0 is the same as a x + b y + c =0.

Wait, but c can be adjusted accordingly. For example, suppose the original line after division is a= -2, b=3, c=4. Then, multiply by -1: a=2, b=-3, c=-4. So the line equation becomes 2x -3y -4=0, which is the same as the original -2x +3y +4=0. So the sign of a and b and c needs to be adjusted so that the leading coefficient (a if a is non-zero, else b) is positive.

So, here's the normalization process:

1. Compute a, b, c as dy, -dx, dx*y1 - dy*x1.

2. Compute g = gcd of |a|, |b|, |c|.

3. Divide a, b, c by g. So now, a, b, c are in reduced form.

4. Check if the first non-zero coefficient among a and b is negative. If so, multiply a, b, c by -1. This ensures that the leading coefficient is positive.

This way, all lines that are the same will have the same normalized a, b, c.

But wait, what about the case when a and b are zero? That's impossible because two distinct points will have dx and dy not both zero. So the line's a and b can't both be zero. So in the normalized form, either a or b (or both) are non-zero.

So the steps for normalization are:

For a line defined by two points (x1,y1) and (x2,y2):

a = y2 - y1

b = x1 - x2

c = x2*y1 - x1*y2

Then, compute g as the GCD of the absolute values of a, b, c.

Then, divide a, b, c by g.

Then, determine the sign. Find the first non-zero element in a, b, c. If it's negative, multiply all by -1 to make it positive.

Wait, but c is also part of the equation. Wait, for example, if a and b are zero, then the line would be 0x +0y + c =0, but that's impossible because the two points are distinct. So a and b can't both be zero. So the line equation is either a x + b y + c =0 where at least a or b is non-zero.

So in the normalized form, after dividing by g, the a and b can't both be zero. So the first non-zero element is either a or b. So, when checking for the sign, we look at a first. If a is zero, then check b.

So the normalization steps are:

Compute a, b, c as before.

Compute the GCD of |a|, |b|, |c|. Let's call this g.

Divide a, b, c by g.

Now, check if a is non-zero. If so, if a is negative, multiply a, b, c by -1. Else, if a is zero, then check if b is non-zero. If b is negative, multiply all by -1.

This ensures that the leading coefficient (a or b) is positive.

For example:

Original a= -2, b=3, c=4. GCD of 2,3,4 is 1. After division, it's -2,3,4. Then, since a is -2 (negative), multiply by -1 to get a=2, b=-3, c=-4. Now, the line is 2x -3y -4=0.

Another example: a=0, b=-3, c=6. GCD is 3. Divide by 3: a=0, b=-1, c=2. Now, since a is zero, check b. It's -1. Multiply by -1 to get a=0, b=1, c=-2. The line equation is 0x +1y -2=0 → y=2. Which is correct.

Another example: two points (0,0) and (1,1). Then, a=1-0=1, b=0-1= -1, c=1*0 - 1*0=0. So line equation: 1x -1y +0=0 → x -y =0. GCD of 1, 1,0 is 1. So normalized a=1, b=-1, c=0. Then, check a is positive. So no change.

Wait, after dividing by g=1, the a is 1, which is positive. So no need to multiply by -1. So the line is represented as (1, -1, 0).

But another line between (1,1) and (2,2) would give the same a=1, b=-1, c=0. So they are considered the same line.

This approach should correctly group all lines that are the same.

So, the plan is:

1. For every pair of points, compute the normalized line parameters (a, b, c) as described.

2. Use a set to collect all unique lines.

3. Once all unique lines are collected, compute the number of pairs of lines that are not parallel (i.e., their direction vectors are not scalar multiples of each other).

Wait, no. Because two lines may be parallel but different (like y=0 and y=1). So, for two lines to intersect, they must not be parallel. So how do we check if two lines are parallel?

Two lines are parallel if their direction vectors are the same. Alternatively, for the line equations ax+by+c=0 and a'x +b'y +c'=0, the lines are parallel if the coefficients (a, b) are scalar multiples. So (a, b) = k*(a', b') for some k ≠0.

But since our lines are normalized, the (a, b) pairs for two parallel lines may be the same or scalar multiples? Wait, in the normalized form, the (a, b) is in the reduced form. For example, two lines that are parallel but different would have the same a and b (since they are normalized), but different c.

Wait, no. Let me think. Suppose line1 is ax + by + c1=0 and line2 is ax + by + c2=0, where c1 ≠ c2. Then these lines are parallel. But since the normalization step ensures that the leading coefficient is positive, then line1 and line2 would have the same a and b, but different c. So in the set, each line is represented as (a, b, c). So even if two lines are parallel (same a and b, different c), they are considered different entries in the set.

So, once we have all the unique lines stored as (a, b, c), the next step is to count the number of pairs of lines (L1, L2) where L1 and L2 are not parallel, i.e., their (a1, b1) is not a scalar multiple of (a2, b2). Wait, but since the lines are normalized, the (a, b) vectors are in the reduced form. So two lines are parallel if and only if (a1, b1) is equal to (a2, b2) multiplied by a positive scalar (since normalization ensures that leading coefficient is positive). But since the lines are normalized, the (a, b) vectors are in their simplest form. So for two lines to be parallel, their (a, b) must be the same.

Wait, for example, consider two lines: line1 has a=2, b=3, and line2 has a=4, b=6. These are parallel. But in their normalized forms, line2 would have a=2, b=3 (since gcd(4,6, c') would be 2, divided by 2 gives a=2, b=3). Wait, but c' could be different. For example, line1 is 2x +3y +5=0 and line2 is 4x +6y +10=0. Then, line2 is normalized to 2x+3y+5=0, which is same as line1. So in that case, they are the same line. But if line2 is 4x +6y + 8=0, then after dividing by 2, it's 2x +3y +4=0. The a and b are same as line1's, but c is different. So these are two different lines that are parallel.

Wait, but how can that happen? Because for two different lines that are parallel, their (a, b) in normalized form would be the same. So in the set, they would be considered as different lines (because c is different). So when counting pairs of lines that are intersecting, we have to count all pairs where (a1, b1) is not equal to (a2, b2) (since same a and b implies they are parallel, but different c implies they are parallel and distinct, so they don't intersect). So, the lines intersect if and only if (a1, b1) is not a scalar multiple of (a2, b2). But since the lines are in normalized form, the scalar must be 1 (since (a, b) is in reduced form, and the leading coefficient is positive). So two lines are parallel if and only if (a1, b1) == (a2, b2). Otherwise, they are not parallel and thus intersect once.

Therefore, the problem reduces to:

For all pairs of distinct lines in the set, if their (a, b) vectors are different, then they form an intersecting pair. Otherwise, they are parallel and do not intersect.

So the steps are:

- Collect all unique lines (each represented as (a, b, c)).

- For each pair of lines (L1, L2), where L1 comes before L2 (to avoid duplicates), check if (a1, b1) != (a2, b2). If so, add 1 to the count.

But how do we efficiently count this?

Once we have the list of lines, we can group them by their (a, b) tuple. Then, for each group, the number of lines in that group is m. Then, the number of lines not in this group is total_lines - m. So each line in this group contributes (total_lines - m) lines that are not parallel. However, since each pair is considered once, the total count would be the sum over all groups of m * (total_lines - m) divided by 2? Wait, no. Because each pair between group A and group B is counted once.

Alternatively, the total number of pairs is (total_lines choose 2) minus the sum over each group of (m choose 2), where m is the size of the group. Because, (total choose 2) counts all possible pairs of lines. But pairs within the same (a, b) group are parallel and don't intersect. So subtract those.

So the formula is:

result = total_lines * (total_lines - 1) // 2 - sum( (m * (m-1) // 2) for each group )

Yes! Because:

- The total possible pairs is C(total, 2) = total * (total-1) / 2.

- The pairs that are parallel are the pairs within the same (a, b) group. For each group of size m, there are C(m, 2) such pairs.

So subtracting the sum of C(m, 2) for all groups from the total pairs gives the number of pairs of lines that are not parallel and thus intersect.

This is a much more efficient way to compute the answer, as we can group the lines by (a, b) and compute the sum accordingly.

So the plan is:

1. Generate all unique lines as (a, b, c) in normalized form.

2. For each line, group by (a, b). So for each group, count how many lines are in it.

3. Compute the total number of line pairs: total = len(lines) choose 2.

4. Compute the sum for each group: sum += (m choose 2) for each group of size m.

5. The answer is total - sum.

This approach is O(n^2) for generating all lines (since n is up to 50, which gives 50*49/2=1225 lines). Then, grouping and summing is O(k), where k is up to 1225. So even for n=50, this is manageable.

Now, the code steps:

First, generate all possible lines between pairs of points, then normalize them, and collect into a set to avoid duplicates.

Wait, but each line is determined by a set of points. So for example, if three points are colinear, all pairs of them generate the same line. So when we process all pairs, we may generate multiple entries for the same line. But since the problem states that each line is represented once regardless of how many points are on it, we need to collect all unique lines.

Thus, the approach is to generate all possible lines (for each pair of points) and then add their normalized forms to a set. Then, the set will contain each line exactly once, regardless of how many pairs generated it.

But wait, for three colinear points, each pair (AB, AC, BC) will generate the same line when normalized. So when we process these pairs, each will compute the same (a, b, c) and thus be added to the set once. So the set will have only one entry for that line.

So the code steps are:

Read all n points.

For each pair of points (i, j) where i < j:

   compute the line (a, b, c) using the two points.

   normalize (a, b, c) as per the steps.

   add the tuple (a, b, c) to a set.

Once all pairs are processed, the set contains all unique lines.

But wait, this is not correct. Because for lines that are the same but generated by different pairs, their (a, b, c) in normalized form will be the same, so they are added once to the set.

Thus, the size of the set is the number of unique lines.

Wait, no. Because the line is determined by the two points, but the set of points may have more than two points lying on the same line. So for example, three points on a line will generate three pairs (AB, AC, BC), but all three pairs will generate the same line (same (a, b, c) after normalization). So the set will contain only one entry for that line.

Thus, the set is correct in that each line is represented once, regardless of how many points are on it.

But wait, the problem says that a wire is a line that connects two or more poles. So even if a line is generated by multiple pairs, but all pairs are part of the same line (due to multiple points), the wire is considered once. So yes, the set correctly captures each unique wire.

So, the set of unique lines is correct.

Once we have the set of lines, we can proceed to group them by (a, b) to compute the number of non-intersecting pairs.

Thus, the code steps are:

Read n points.

Generate all pairs (i, j), i < j.

For each pair, compute the line in normalized form (a, b, c).

Add (a, b, c) to a set.

Once the set is built, group the lines by their (a, b) tuple.

Compute the sum for each group.

Compute the answer as total_lines * (total_lines -1) //2 minus the sum of (m choose 2) for each group.

Now, the code.

But first, the normalization code.

Implementing the normalization:

We need to compute a, b, c as:

dx = x2 - x1

dy = y2 - y1

a = dy

b = -dx

c = dx * y1 - dy * x1

Then compute the GCD of a, b, c.

But how to compute the GCD of three numbers?

In Python, the math.gcd function takes two arguments. So to compute the GCD of three numbers, we can compute the GCD of the first two, then the GCD of that result with the third.

But since the GCD of a, b, c is the same as the GCD of the absolute values, we can compute the GCD of |a|, |b|, |c|.

So code:

g = math.gcd(math.gcd(abs(a), abs(b)), abs(c))

But note that the GCD of (0, 0, c) is GCD(0, c) = abs(c). But since a and b can't both be zero, we can proceed.

Once we have g, we divide a, b, c by g.

Then, check the sign:

We need to find the first non-zero element in a, b. Then, if it's negative, multiply all by -1.

So code:

if a != 0:

    if a < 0:

        a = -a

        b = -b

        c = -c

else:

    if b < 0:

        b = -b

        c = -c

Wait, but what about c? For example, if a is zero and b is positive, then it's okay. But if a is zero and b is negative, we multiply by -1 to make b positive.

But in the code, after division by g, if a is zero and b is negative, then multiply all by -1.

Yes.

So the code steps:

def normalize_line(x1, y1, x2, y2):

    dx = x2 - x1

    dy = y2 - y1

    a = dy

    b = -dx

    c = dx * y1 - dy * x1

    # Compute GCD of a, b, c

    g = math.gcd(math.gcd(abs(a), abs(b)), abs(c))

    if g != 0:

        a //= g

        b //= g

        c //= g

    # Now determine the sign

    # Find the first non-zero among a and b

    if a != 0:

        if a < 0:

            a = -a

            b = -b

            c = -c

    else:

        if b < 0:

            b = -b

            c = -c

    return (a, b, c)

Wait, but what if a and b are both zero? But that's impossible since dx and dy can't both be zero (since the points are distinct). So in the code, a and b can't be both zero.

So this function should return the normalized (a, b, c) tuple.

Wait, let's test with some examples.

Test case 1: points (0,0) and (1,1):

dx =1, dy=1.

a=1, b= -1.

c =1*0 -1*0 =0.

g = gcd(gcd(1,1), 0) = gcd(1, 0) =1.

a=1/1=1, b=-1/1=-1, c=0.

Then, check a is positive (1), so no change.

So normalized is (1, -1, 0).

Another example: points (0,0) and (0,1):

dx=0, dy=1.

a=1, b=0 -0=0.

Wait, wait, dx is x2 -x1. For (0,0) and (0,1), x2 is 0, x1 is 0. So dx=0. dy=1-0=1.

So a= dy =1.

b = -dx = -0 =0.

c = dx * y1 - dy *x1 → 0*0 -1*0 =0.

So line equation is 1x +0y +0=0 → x=0.

But wait, the line through (0,0) and (0,1) is x=0. So the line equation is 1x +0y =0. Which is x=0.

So the normalized a, b, c is (1, 0, 0).

Another example: points (0,2) and (0,4):

dx=0, dy=2.

a=2, b=0.

c=0*2 -2*0=0.

g = gcd(2,0,0) → gcd(2,0) is 2, then gcd(2,0) is 2. So a=2/2=1, b=0/2=0, c=0/2=0.

Then check a is positive. So normalized is (1, 0, 0). Which is same as the previous example. So all vertical lines x= k, when normalized, will have (a=1, b=0, c=-k). Wait, no.

Wait, let's take points (0,0) and (0,3):

dx=0, dy=3.

a=3, b=0.

c=0*0 -3*0=0.

g is gcd(3,0,0) → 3.

So a=3/3=1, b=0, c=0.

So line is x=0.

Another line, points (2,0) and (2,3):

dx=0, dy=3.

a=3, b=0.

c=0*0 -3*2= -6.

g = gcd(3,0,6) → 3.

So after division: a=1, b=0, c= -2.

Then, check a is positive. So normalized is (1, 0, -2). The line equation is x -2=0 → x=2.

So the normalized (a, b, c) is (1, 0, -2).

So two different vertical lines will have the same a and b (1,0) but different c. So they are considered different lines, and are parallel.

So the code correctly captures that.

Another example: line between (1,0) and (3,1):

dx=2, dy=1.

a=1, b= -2.

c =2*0 -1*1 = -1.

g is gcd(1,2,1) → gcd(1, gcd(2,1)) → gcd(1,1) =1.

So a=1, b=-2, c=-1.

Check a is positive. So no change. So normalized is (1, -2, -1). So line equation is x -2y -1 =0.

Another line between (1,0) and (3,1) is the same line, so same (a, b, c).

Another example: points (-1,-1), (1,0), (3,1). All three are colinear.

The line between (-1,-1) and (1,0):

dx=2, dy=1.

a=1, b=-2.

c= 2*(-1) -1*(-1) = -2 +1 = -1.

g= gcd(1,2,1) →1.

So normalized is (1, -2, -1).

Line between (1,0) and (3,1):

dx=2, dy=1.

a=1, b=-2.

c=2*0 -1*1= -1.

Same as before. So normalized is same.

So all pairs generate the same line, which is added once to the set.

Thus, the code correctly captures unique lines.

Now, the code steps.

Read n points.

Read each (x_i, y_i) and store in a list.

Generate all pairs (i, j) where i < j.

For each pair, compute normalized (a, b, c) using the function.

Add to a set (to collect unique lines).

Once the set is built, group the lines by their (a, b) tuple.

Compute total_lines = len(lines).

sum_parallel_pairs = sum( m*(m-1)//2 for m in group_counts.values() )

answer = total_lines * (total_lines -1) //2 - sum_parallel_pairs.

So code:

import math

n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

lines = set()

for i in range(n):

    x1, y1 = points[i]

    for j in range(i+1, n):

        x2, y2 = points[j]

        dx = x2 - x1

        dy = y2 - y1

        a = dy

        b = -dx

        c = dx * y1 - dy * x1

        # Compute GCD of a, b, c's absolute values

        g = math.gcd(math.gcd(abs(a), abs(b)), abs(c))

        if g != 0:

            a //= g

            b //= g

            c //= g

        # Determine sign based on a and b

        if a !=0:

            if a < 0:

                a = -a

                b = -b

                c = -c

        else:

            if b <0:

                b = -b

                c = -c

        lines.add( (a, b, c) )

# Now group lines by (a, b)

from collections import defaultdict

group = defaultdict(int)

for a, b, c in lines:

    group_key = (a, b)

    group[group_key] +=1

total = len(lines)

sum_parallel = sum( m * (m-1) //2 for m in group.values() )

answer = total * (total -1) //2 - sum_parallel

print(answer)

Wait, but for the code, what if the GCD is zero? Because a, b, c can't all be zero (since the points are distinct), but when computing GCD of a, b, c, if all three are zero, then division by zero would happen. But in our case, a and b can't both be zero. Because a= dy and b= -dx. So if dx and dy are zero, the points are same, but the problem says all points are distinct. So the code will never have a=0 and b=0. So g is the GCD of (a, b, c), which can't be zero. So division by g is safe.

Testing the first sample input:

Sample input 1:

4

0 0

1 1

0 3

1 2

The lines are:

Between (0,0) and (1,1):

dx=1, dy=1 → a=1, b=-1, c=0. GCD is 1. No sign change. So (1, -1, 0).

Between (0,0) and (0,3): dx=0, dy=3. a=3, b=0, c=0. GCD is 3. After division: 1,0,0. So (1,0,0).

Between (0,0) and (1,2): dx=1, dy=2. a=2, b=-1. c=1*0 -2*0=0. GCD(2,1,0) → GCD(1,0) =1. So a=2, b=-1, c=0. Then check a is 2 (positive). So normalized as (2,-1,0).

Wait, but how many lines are there?

Wait the four points are (0,0), (1,1), (0,3), (1,2).

We need to compute all pairs:

(0,0) and (1,1): line (1,-1,0).

(0,0) and (0,3): line (1,0,0).

(0,0) and (1,2): dx=1, dy=2. a=2, b=-1. c=1*0 - 2*0=0. GCD(2,1,0)=1. So a=2, b=-1, c=0. Since a is positive, no change. So (2, -1, 0).

(1,1) and (0,3): dx =-1, dy=2. a=2, b=1. c= (-1)*1 -2*1 → -1-2= -3. GCD(2,1,3) → GCD(1,3) =1. So (2,1,-3). Then check a=2 positive. So (2,1,-3).

(1,1) and (1,2): dx=0, dy=1. a=1, b=0. c=0*1 -1*1= -1. GCD(1,0,1) → 1. a=1, b=0, c=-1. Since a is positive, no change. So (1,0,-1).

(0,3) and (1,2): dx=1, dy=-1. a=-1, b=-1. c=1*3 - (-1)*0 →3. GCD(1,1,3) →1. So (-1,-1,3). Now, a is -1. Multiply by -1: a=1, b=1, c=-3. So (1,1,-3).

So the lines set will have 6 entries?

Wait, no. Let's compute all possible pairs:

There are 4 points, so 6 pairs.

Each pair generates a line. But some pairs may generate the same line.

The sample output is 14.

Hmm, but according to the code's logic, the lines in the first sample would have:

Let's see the actual lines generated.

For the first sample input:

points are:

A(0,0), B(1,1), C(0,3), D(1,2).

Pairs:

AB: line (1,-1,0).

AC: line (3,0,0) → wait, dx is 0-0=0, dy=3-0=3. So a=3, b=0. c=0*0 -3*0=0. GCD(3,0,0) →3. So a=1, b=0, c=0. So (1,0,0).

AD: (1,2) → dx=1, dy=2. a=2, b=-1. c=1*0 -2*0=0. GCD(2,1,0) →1. So (2,-1,0).

BC: (0,3) → dx=0-1=-1, dy=3-1=2. a=2, b=1. c= (-1)*1 -2*1 →-1-2= -3. GCD(2,1,3) →1. So (2,1,-3).

BD: (1,2) → dx=0, dy=1. a=1, b=0. c=0*1 -1*1 = -1. So after normalization: (1,0,-1).

CD: (1,2) and (0,3). dx= -1, dy=1. a=1, b=1. c= (-1)*3 -1*1 →-3-1 =-4. GCD(1,1,4) →1. So (1,1,-4). Check a is positive, so no change. So (1,1,-4).

So the lines set contains:

(1,-1,0), (1,0,0), (2,-1,0), (2,1,-3), (1,0,-1), (1,1,-4).

Wait, but how many lines are there? Each pair adds a line to the set. So 6 pairs, but some pairs may have same line.

Wait, let me compute all six pairs:

AB → (1,-1,0).

AC → (1,0,0).

AD → (2,-1,0).

BC → (2,1,-3).

BD → (1,0,-1).

CD → (1,1,-4).

So the lines set has 6 unique lines.

Then, group by (a,b):

Group (1,-1,0): (1,-1) → count 1.

Group (1,0,0): (1,0) → count 1.

Group (2,-1,0): (2,-1) → count 1.

Group (2,1,-3): (2,1) → count 1.

Group (1,0,-1): (1,0) → count increases to 2.

Group (1,1,-4): (1,1) → count 1.

So group counts:

(1,-1):1

(1,0):2

(2,-1):1

(2,1):1

(1,1):1

So sum_parallel = (1*0//2) + (2*1//2) + ... → sum is (0) + 1 + 0 +0 +0 →1.

Total lines is 6. So total pairs is 6*5/2=15.

Subtract sum_parallel (1) → 14. Which matches the sample output.

So the code works for the first sample.

Another sample:

Sample input 4 points:

0 0

0 2

0 4

2 0

Sample output 6.

These four points are:

A(0,0), B(0,2), C(0,4), D(2,0).

Pairs:

AB: line vertical x=0. normalized (1,0,0).

AC: x=0 → (1,0,0).

AD: line between (0,0) and (2,0) → dy=0, dx=2. a=0, b=-2. c=2*0 -0*0=0. GCD is 2. a=0/2=0, b=-2/2=-1, c=0. Since a is zero, check b. It's -1 → multiply by -1: b=1, c=0. So (0,1,0) → line y=0.

BC: x=0 → (1,0,0).

BD: line between (0,2) and (2,0). dx=2, dy=-2. a=-2, b=-2. c=2*2 - (-2)*0 =4. GCD of 2,2,4 is 2. a=-2/2=-1 → since a is negative, multiply by -1 → a=1, b=1, c=-2. So (1,1,-2).

Bd: (0,2) and (2,0) → line equation: -2x -2y +4 =0 → which becomes x + y -2=0 after normalization.

CD: line between (0,4) and (2,0) → dx=2, dy=-4. a=-4, b=-2. c=2*4 - (-4)*0=8. GCD is 4,2,8 → GCD is 2. a=-4/2=-2 → multiply by -1: a=2, b=1, c=-4. So line equation 2x + y -4=0.

AD: line (0,0) and (2,0) → same as AD before.

BD: line (0,2) and (2,0) → (1,1,-2).

CD: line (0,4) and (2,0) → (2,1,-4).

But how many unique lines are there?

Let's list all pairs:

AB → (1,0,0).

AC → (1,0,0).

AD → (0,1,0).

BC → (1,0,0).

BD → (1,1,-2).

CD → (2,1,-4).

Wait, but wait:

Other pairs:

BA is same as AB.

But the code generates pairs (i,j) with i<j. So all 6 pairs:

AB (0,0) and (0,2) → x=0 → (1,0,0).

AC (0,0) and (0,4) → same as above → (1,0,0).

AD (0,0) and (2,0) → line y=0 → (0,1,0).

BC (0,2) and (0,4) → x=0 → (1,0,0).

BD (0,2) and (2,0) → line (1,1,-2).

CD (0,4) and (2,0) → line (2,1,-4).

So the lines set has:

(1,0,0), (0,1,0), (1,1,-2), (2,1,-4), (1,0,0), (1,0,0) → but duplicates are removed. So lines set contains:

(1,0,0), (0,1,0), (1,1,-2), (2,1,-4).

Wait, how many unique lines are there?

Wait, for AB, AC, BC pairs, they all generate the same line (1,0,0). So when processing these pairs, they all add the same entry to the set. So the lines set will have (1,0,0), (0,1,0), (1,1,-2), (2,1,-4), BD pair adds (1,1,-2), CD adds (2,1,-4). So the set has 4 lines.

Wait, AB, AC, BC are all pairs that generate the same line (1,0,0). So the set will have one entry for that line.

AD is (0,0) and (2,0) → line y=0 → (0,1,0).

BD is (0,2) and (2,0) → line (1,1,-2).

CD is (0,4) and (2,0) → line (2,1,-4).

So the set has four lines.

So group counts:

(1,0):1

(0,1):1

(1,1):1

(2,1):1

sum_parallel_pairs is sum of (1*0//2) for each group → 0.

Total lines is 4 → 4*3/2=6. So answer is 6-0=6. Which matches sample 2.

So code works.

Third sample input:

3 points:

-1 -1

1 0

3 1

These three points are colinear. So all pairs generate the same line.

So the lines set has one line.

group counts: (a,b) is same for all.

sum_parallel_pairs is 3 pairs (but since there is only one line, m=1, sum is 0). total lines is 1 → answer 0.

Which matches sample 3.

So the code seems correct.

Thus, the code should work.
</think>

```python
import math
from collections import defaultdict

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

lines = set()

for i in range(n):
    x1, y1 = points[i]
    for j in range(i + 1, n):
        x2, y2 = points[j]
        dx = x2 - x1
        dy = y2 - y1
        a = dy
        b = -dx
        c = dx * y1 - dy * x1
        
        # Compute GCD of absolute values
        g = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
        if g != 0:
            a //= g
            b //= g
            c //= g
        
        # Normalize sign
        if a != 0:
            if a < 0:
                a = -a
                b = -b
                c = -c
        else:
            if b < 0:
                b = -b
                c = -c
        
        lines.add((a, b, c))

group_counts = defaultdict(int)
for a, b, _ in lines:
    group_counts[(a, b)] += 1

total = len(lines)
sum_parallel = sum(m * (m - 1) // 2 for m in group_counts.values())
answer = total * (total - 1) // 2 - sum_parallel

print(answer)
```