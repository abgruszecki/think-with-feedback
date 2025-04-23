<think>
Okay, let's see. The problem is about a laser bouncing around a rectangular room and determining the first time each sensor is hit. Hmm. So the laser starts at (0,0) moving towards (1,1), which makes it move diagonally. Each time it hits a wall, it reflects with the angle of incidence equal to the angle of reflection. And if it hits a corner, it stops.

The key here is to model the path of the laser without actually simulating each bounce, which would be way too slow for large n and m. Because the constraints are up to 1e5 for n and m, and k up to 1e5 as well, we need an O(1) or O(k) solution per query.

Wait, let's think about the reflections. Since the laser is moving diagonally, each time it reflects, it's like the grid is mirrored. So perhaps we can model the problem using the least common multiple (LCM) of the room's dimensions. Because the path repeats in a pattern determined by how many times the room is mirrored in each direction.

The idea is to find how many reflections (horizontal and vertical) the laser undergoes before reaching a point (x, y) that is a mirror image of the original sensor's position. For instance, after even number of horizontal reflections, the x-coordinate is same as original; after odd, it's mirrored. Same for vertical. Then, the time would be when the laser's path in this mirrored grid crosses the sensor's coordinates.

So, the general approach is:

1. For each sensor (xi, yi), we need to find integers a and b such that:
   xi = x_coeff * (a * n - xi_orig) or xi = x_coeff * (a * n + xi_orig)
   Wait, maybe I need to model the mirrored coordinates. The laser's path can be represented as a straight line through mirrored grids, so the problem becomes finding the minimal time when the laser passes through (xi, yi) in some mirrored grid.

Alternatively, the path of the laser can be thought of as a straight line in a grid that's tiled with mirrored rooms. Each time the laser would hit a vertical wall, instead of reflecting, we imagine that the grid is mirrored, and the laser continues straight. So, the coordinates (x, y) in the original room would correspond to points (x + a*2n, y + b*2m) or similar in the mirrored grids, but maybe with parity based on how many reflections.

Wait, let me get this straight. The standard approach for such bouncing problems is to consider that the reflections can be modeled by expanding the grid into mirrored copies. Then the laser's path is a straight line in this grid. The problem then reduces to finding the earliest time when the laser passes through a point that's equivalent to the sensor's position in one of these mirrored grids.

So for example, the laser's direction is (1,1), so each step moves it by 1 in x and 1 in y. But when it hits a wall, it's reflected. Instead, imagine that the room is mirrored, and the laser continues straight. So, after each reflection, the parity of the mirrored grid in x and y directions changes.

So, for the x-direction: each time the laser crosses a vertical wall (either left or right), it's equivalent to entering a mirrored copy. So the actual x-coordinate can be represented as (a * n) ± xi, where a is the number of times we've crossed the vertical walls. Similarly for y.

But the direction of the mirroring (whether we add or subtract) depends on the parity of the number of reflections in that direction. For example, if the laser has been reflected an even number of times in the x-direction, the current x-coordinate is xi; if odd, it's (n - xi). Similarly for y.

Wait, but the direction of movement after reflections affects this. Let me think again. The original movement is in the direction of (1,1). Each vertical reflection (hitting the left or right wall) reverses the x-direction. Each horizontal reflection (hitting top or bottom) reverses the y-direction.

So, after a certain number of reflections, the direction in x and y can be either positive or negative.

But modeling the path as a straight line in a mirrored grid allows us to avoid tracking the reflections. So, the path in the original grid is equivalent to a straight line in an infinite grid of mirrored rooms. The sensor's position (xi, yi) in some mirrored room must lie on the line (t, t) (since the laser's direction is (1,1), speed sqrt(2) so in t seconds, it's at (t, t)). Wait, no. Wait, the speed is sqrt(2) meters per second. So, each second, the laser moves (1,1) in coordinates. So, after t seconds, the position is (t, t) in a straight line. But in reality, with reflections, the actual path is a series of bounces, but the mirrored grid approach can model this as a straight line.

But how do we map the actual coordinates in the original room to the mirrored grid's coordinates?

Let me think of the mirrored grid in x and y directions. Each time the laser crosses a vertical wall, it's entering a mirrored version of the room. So, the x-coordinate in the mirrored grid is determined by whether the number of vertical reflections is even or odd.

For example, after even vertical reflections, the x is same as original, and after odd, it's mirrored. Similarly for y.

So, for the mirrored grid, the x coordinate can be represented as:

x' = a * n + xi if a is even, or (a+1) * n - xi if a is odd.

Wait, perhaps more accurately, the mirrored grid in the x direction alternates between normal and mirrored. So, the x position in the grid can be represented as:

x = k * n + dx, where dx is between 0 and n. But the direction depends on whether k is even or odd. If even, dx is the actual position (from 0 to n). If odd, dx is n - dx.

Wait, perhaps the mirrored grid approach allows us to model the laser's path as a straight line in a grid where each cell is a mirrored version of the original room. Then, each reflection is equivalent to moving into the next cell in the grid. So, the laser's path is a straight line of slope 1 (since moving in direction (1,1)).

So, the problem reduces to finding the smallest t such that (x, y) = (t, t) in the mirrored grid corresponds to the original sensor's (xi, yi) in some cell (a, b) of the grid.

Wait, but how to model the cell (a, b) in terms of the mirrored grid. For example, in the x direction, the cells are arranged as 0, n, 2n, etc., but each even cell is original, and odd is mirrored. So, for a given cell (a, b) in the mirrored grid, the x-coordinate in that cell is:

if a is even: x_in_cell = xi (assuming original direction)
if a is odd: x_in_cell = n - xi

Similarly for the y direction.

But the laser's path in the mirrored grid is a straight line (t, t). So, the position (t, t) in the grid must correspond to a point (xi, yi) in one of the mirrored cells. So, t must satisfy:

t = a * n + dx, where dx is xi or (n - xi) depending on the parity of a.

Similarly, t = b * m + dy, where dy is yi or (m - yi) depending on the parity of b.

Wait, but for a given a and b, the dx and dy must satisfy:

dx = xi if a is even, else n - xi.

Similarly, dy = yi if b is even, else m - yi.

So, for the x-coordinate:

t = a * n + (xi if a even else n - xi).

Similarly, t = b * m + (yi if b even else m - yi).

But since the laser's path is t in x and y (since direction is (1,1)), these two expressions must be equal. So, we have:

a * n + (xi if a even else n - xi) = b * m + (yi if b even else m - yi) = t.

We need to find integers a and b (non-negative) such that this equation holds, and t is minimal. Also, t must be such that the laser hasn't yet hit a corner (since hitting a corner stops the laser).

So, the approach is for each sensor (xi, yi) to find all possible combinations of a and b (even and odd) parity that would allow t to be equal in both x and y expressions, and then find the minimal t among those possibilities.

But considering all possible parity combinations for a and b, there are four cases:

Case 1: a is even, b is even.

Then:

t = a*n + xi = b*m + yi

Case 2: a even, b odd.

t = a*n + xi = b*m + (m - yi)

Case 3: a odd, b even.

t = a*n + (n - xi) = b*m + yi

Case 4: a odd, b odd.

t = a*n + (n - xi) = b*m + (m - yi)

We need to solve each of these four equations for a and b (non-negative integers), find possible t's, and then select the minimal t among all possibilities. If there are no solutions in any case, output -1.

Additionally, the laser stops when it reaches any of the four corners, which happens when t is such that the position (t, t) in the mirrored grid corresponds to (0,0), (n,0), (0,m), (n,m) (but wait, in the original grid, the corners are (0,0) and (n,m), and others are (n,0) and (0, m)). Wait, no. The laser stops when it reaches any of the four corners. So, for the laser's path (t, t), if in the mirrored grid, (t, t) is a corner of the original room. So, that would be when the current cell (a, b) in the mirrored grid has x = a*n (if a even) or (a+1)*n (if a odd) or 0, but I'm not sure.

Wait, perhaps when the laser's path (t, t) in the mirrored grid is such that t is a multiple of n and m. Wait, no. For example, if t is n * a, and also m * b, but that's the original scenario. Hmm.

Wait, the corners of the original room are (0,0), (n,0), (0,m), (n,m). The laser starts at (0,0) and stops if it reaches any of these. So, during its path in the mirrored grid, if the point (t, t) is equivalent to one of these corners in the original room, then the laser stops. So, for example, when t is equal to n * a for even a (so x is a*n + 0 = a*n), and m * b for even b (y is b*m +0 = b*m). Then, the point (t, t) would be (a*n, b*m) which is a corner if a and b are such that a*n = b*m. But perhaps more generally, when the t in x and t in y correspond to a corner.

Alternatively, the stopping condition is when (t, t) in the mirrored grid is a corner. For example, if the x-coordinate in the mirrored grid is 0, n, 0 + k*2n, etc., but this is getting complicated.

So, the key is to compute for each sensor (xi, yi) the minimal t such that the equations for x and y hold for some parity of a and b, and also that this t is not after the laser has already stopped.

So the steps are:

1. For each sensor, generate four possible equations (for the four parity combinations of a and b) and solve for a and b.

2. For each solution (a, b), compute t and check if the path reaches (xi, yi) before the laser stops at any corner.

So, the first task is to solve the four equations for each sensor.

Let's take each case one by one.

Case 1: a even, b even.

Equation: a*n + xi = b*m + yi.

We need a and b to be non-negative integers. Let's express this as:

a*n - b*m = (yi - xi).

This is a linear Diophantine equation. We can solve for a and b.

But since a and b must be integers >= 0, we need to find solutions where a is even (since in this case a is even). Similarly for other cases.

Alternatively, we can model a as 2k, but perhaps a better approach is to find all possible solutions (a, b) to the equation a*n + xi = b*m + yi, then check if a is even and b is even.

But solving for a and b here requires some math.

The same applies for other cases.

Let me think about solving the equation for case 1:

t = a*n + xi = b*m + yi.

But a and b must be even (since a is even in case 1). Wait, no: in case 1, a can be any even non-negative integer (0,2,4,...). Similarly, b can be even.

Wait, a is even, so we can set a = 2k. Then the equation becomes 2k *n + xi = b*m + yi.

But b must be even as well (since case 1 is when both are even). So set b = 2l.

So equation becomes 2k*n + xi = 2l *m + yi.

Rearranged as:

2(k n - l m) = yi - xi.

Wait, but this may not always be possible. For example, if yi - xi is odd, then the left side is even, so no solution.

So, in case 1, there are solutions only if yi - xi is even. Then, we can find k and l such that 2(kn - lm) = yi -xi.

But this seems complicated. Maybe there's a better way to model this.

Alternatively, perhaps for each case, we can model the equation as t = ... and find possible t's that satisfy both x and y equations. Then, among those t's, find the smallest one that's possible, and also check if the laser hasn't reached a corner before that t.

But how to find the possible t's for each case.

Alternatively, for each case, the equations can be rewritten as:

t ≡ xi mod n (if a is even)

t ≡ (n - xi) mod n (if a is odd)

Similarly for the y direction.

For example, in case 1:

t ≡ xi mod (2n) for x direction (since a is even, so the x component repeats every 2n steps: because even a steps add even multiples of n, and then xi. So, the x component for even a is xi, n + xi, 2n + xi, etc. So, modulo 2n, the x component is xi mod 2n. Similarly, for case 3 (a odd), the x component is (n - xi) mod 2n.

Wait, perhaps considering the x component for even a and odd a:

- For even a (a=2k), the x component is 2k * n + xi. So, modulo 2n, this is xi.

- For odd a (a=2k+1), the x component is (2k+1)*n + (n - xi) = (2k+2)*n - xi. So modulo 2n, this is (2n - xi) mod 2n → which is (2n - xi). So, xi mod 2n is (2n - xi) mod 2n?

Hmm, perhaps for even a, the x coordinate's remainder mod 2n is xi, and for odd a, it's (2n - xi) mod 2n.

Similarly for y direction.

So, for case 1 (a even, b even):

t ≡ xi mod (2n)

t ≡ yi mod (2m)

We can model this as solving for t where t ≡ xi mod (2n) and t ≡ yi mod (2m).

Similarly, for case 2 (a even, b odd):

t ≡ xi mod (2n)

t ≡ (m - yi) mod (2m)

Case3 (a odd, b even):

t ≡ (n - xi) mod (2n)

t ≡ yi mod (2m)

Case4 (a odd, b odd):

t ≡ (n - xi) mod (2n)

t ≡ (m - yi) mod (2m)

So, for each of the four cases, we can model the problem as solving a system of congruences. For each such system, we need to find the minimal t >= 0 that satisfies both congruences. Then, among all four cases, select the minimal t (if any) that is possible, and check if the laser hasn't already been stopped at a corner before that t.

But how to solve these congruence systems?

The Chinese Remainder Theorem (CRT) can be applied here if the moduli are coprime, but since 2n and 2m may not be coprime, we need to check if the congruences are compatible. For each case, we can compute the minimal t that satisfies both congruences, if such a t exists.

Once we have the possible t's from all four cases, the minimal t among them is the candidate. But we also need to ensure that at this t, the laser hasn't hit any corner before.

So, the steps for each sensor (xi, yi) are:

1. For each of the four cases (combinations of parity for a and b):

   a. Set up the congruence equations based on the case.

   b. Solve for t using CRT. If a solution exists, record the minimal positive t for this case.

2. Among all four cases' possible t's, select the smallest one.

3. Check if this t is such that the laser hasn't hit any corner before or at this t.

Wait, but how to check if the laser hits a corner before the computed t.

Because, once the laser hits a corner at some time T, it stops, so any t >= T cannot be considered. So, for a candidate t, we need to check if the laser's path would have hit a corner before or at t. If the minimal T where the laser stops is <= t, then the sensor is not hit.

So, the problem reduces to:

For each candidate t (from the four cases), if t >= T (the minimal time the laser stops), then this t is invalid. So, we need to compute the minimal T where the laser stops (hits a corner), and compare it with the candidate t.

But how to compute T?

The laser stops when the path (t, t) in the mirrored grid is a corner. The corners in the original grid are (0,0), (n, 0), (0, m), (n, m). But in the mirrored grid, the path can hit any of these in their respective mirrored copies.

So, the laser stops at time T when the following equations are satisfied:

T = a*n = b*m (for the (a*n, b*m) corner, which corresponds to (0,0) in a mirrored grid?)

Wait, perhaps not. Let me think again.

The original corners are (0,0), (n,0), (0,m), (n,m). In the mirrored grid, the path (t, t) would hit a corner if:

- x and y are multiples of n and m, respectively, in the same mirrored grid cell.

For example, T is a multiple of n and m. Because if T = LCM(n, m) * k, then T is a multiple of both n and m, so the laser would be at (T, T) which is (k*LCM(n, m), k*LCM(n, m)), which is equivalent to (0, 0) in the mirrored grid after k steps. Wait, perhaps I'm getting confused here.

Alternatively, the laser stops when T is a time such that T is a multiple of n and m, i.e., T = LCM(n, m) * k for some integer k ≥ 1.

Wait, for example, in the first sample input, n=3, m=3. LCM(3,3) is 3. So the laser would stop at T=3 seconds, as per the note. Which matches LCM(3,3) =3.

In the second sample, n=3, m=4. LCM(3,4) is 12. The note says the laser stops at 12 seconds.

So perhaps T is LCM(n, m). But wait, the laser stops at T = LCM(n, m) * k for k ≥1. The minimal T is LCM(n, m).

So, for each candidate t from the four cases, we need to check if t < T (the minimal stopping time). If t is >= T, then the sensor is not hit.

So, T = LCM(n, m). So, the minimal stopping time is LCM(n, m).

Wait, but what if LCM(n, m) is not the minimal time? For example, if n and m are not coprime. Let's see. Take n=2, m=4. LCM(2,4) is 4. But the laser would hit (2,2) at t=2, which is a corner (since (2,2) in the original room is (n, m/2), which is not a corner. Hmm, perhaps my previous reasoning is wrong.

Wait, the laser stops when it hits any of the four corners. So, for the path (t, t) in the mirrored grid, the actual position must be a corner of the original room.

So, in terms of the mirrored grid, the laser's position is (t, t). The actual coordinates in the original room can be determined by the mirrored grid cell and the direction.

For example, to check if (t, t) is a corner of the original room, we need to have:

For x:

t mod (2n) must be 0 or n.

Similarly for y:

t mod (2m) must be 0 or m.

But that's not sufficient. Let's think:

The x-coordinate in the mirrored grid can be written as:

x = a * n ± xi, depending on the parity.

Wait, but for the laser to hit a corner, say (0,0), the position in the mirrored grid must be (0,0), but after even reflections in x and y.

Alternatively, the laser's position (t, t) in the mirrored grid must be such that t is a multiple of n and m. Because then, (t, t) would be (k*n, k*m), which is a corner if k is even or odd? Wait, no. For example, if t = n, then x is n, which is a vertical wall. But in the original room, (n,0) and (n, m) are corners. So the laser would stop if it hits (n,0) or (n, m).

Hmm, this is getting a bit complicated.

Alternatively, the minimal time when the laser stops is when t = LCM(n, m), but I need to verify.

In the first sample, LCM(3,3) is 3, which is when the laser stops. In the second sample, LCM(3,4) is 12, which is when the laser stops. So perhaps the minimal T is LCM(n, m), but perhaps there are cases where the laser stops earlier.

Another example: n=2, m=4. LCM(2,4)=4. But the path would be (0,0) → (1,1) → (2,2) → (3,3) → (4,4). Wait, but the room is 2x4. So at t=2, the laser is at (2,2), which in the original room is (2,2) which is the corner (n, m) if m=2. But in this case, m=4. So (2,2) is not a corner. So at t=4, the laser would be at (4,4). The original room is 2x4. So in the mirrored grid, the x-coordinate is 4. For x, since 4 = 2*2 + 0, so a=2 (even), so x is 0 (since 2 is even, x is 0 in the mirrored cell). Similarly for y, 4 is 4 = 4*1 +0, so b=1 (odd), so y is 4 -0 =4? Wait, this is getting confusing.

Alternatively, when the laser reaches a time t where both x and y are multiples of n and m respectively, but considering the reflections. For example, if t is a multiple of LCM(n, m), then the laser's position would be (k*LCM(n, m), k*LCM(n, m)), which may correspond to a corner.

But perhaps the minimal T where the laser stops is the minimal t where t is LCM(n, m) divided by GCD(n, m). Wait, no. Let me think.

The minimal T is the minimal t such that t is a multiple of n and m. Which is LCM(n, m). Because, for example, in the first sample, LCM(3,3)=3. At t=3, the laser is at (3,3), which is (n, m) → a corner. So it stops.

In the second sample, LCM(3,4)=12. At t=12, the laser is at (12,12). But the room is 3x4. For x=12: since 3*4=12, x=12 = 3*4 → which is a multiple of 3 (n=3). So in the mirrored grid, x=12 is 4*3, which would be a corner (0,0) after even number of reflections. Similarly for y=12=4*3 → 4 is even, so y=0? So the position would be (0,0) in some mirrored cell, which is a corner. So the laser stops at 12.

So, the minimal T is LCM(n, m). Therefore, for any candidate t computed for a sensor, if t >= T, then the sensor is not hit.

So, the steps for each sensor are:

For each of four cases:

   solve the congruence equations for t.

   collect all possible minimal t's.

Find the minimal t among them.

If no t exists, output -1.

Otherwise, check if this t is less than T (the minimal stopping time). If yes, output t. Else, -1.

So, the algorithm for each sensor (xi, yi) is:

1. Compute T = LCM(n, m).

2. For each of the four cases:

   a. Compute the congruence equations for t.

   b. Find the minimal t >=0 that satisfies the equations. If no solution exists, skip.

3. Collect all four possible t's (if any).

4. Find the minimal t among them.

5. If such a t exists and t < T, output t. Else, output -1.

Now, the main challenge is to solve the congruence equations for each case.

For example, case 1: t ≡ xi mod 2n, t ≡ yi mod 2m.

We need to solve for t such that t ≡ xi (mod 2n) and t ≡ yi (mod 2m). The minimal solution t can be found using the Chinese Remainder Theorem (CRT), but only if xi ≡ yi mod gcd(2n, 2m). Let's see.

The CRT says that a solution exists if and only if xi ≡ yi mod d, where d = gcd(2n, 2m). If this is satisfied, then the solution is unique modulo LCM(2n, 2m) = (2n*2m)/d.

So, for case 1:

We compute d = gcd(2n, 2m).

Check if (xi - yi) is divisible by d.

If not, no solution for case 1.

Otherwise, compute the minimal t >=0 that satisfies the two congruences.

Similarly for the other cases.

So, for each case, we need to:

- Check if the required congruence conditions are satisfied.

- If yes, compute the minimal t that satisfies both congruences.

Thus, for each case, we can write a function that returns the minimal t or None.

Now, to implement this in Python:

First, we need a function to solve the CRT for two congruences:

t ≡ a mod m

t ≡ b mod n

The function returns the minimal non-negative t that satisfies these, or None if no solution exists.

Implementing the CRT for two congruences.

The code for this can be found in various algorithms. Let's recall.

The solution exists iff (a - b) is divisible by gcd(m, n).

The minimal solution can be computed using the extended Euclidean algorithm.

Alternatively, using the formula:

Let g = gcd(m, n)

If (a - b) % g !=0: no solution.

Else:

We can compute the solution using:

We find integers x, y such that m*x - n*y = b -a.

Then, t = a + x*m.

But perhaps using the extended Euclidean algorithm is the way to go.

Alternatively, we can compute the minimal t as follows:

Let d = gcd(m, n)

We need to solve:

t ≡ a mod m

t ≡ b mod n

We can represent t as a + k*m.

Substitute into the second congruence:

a + k*m ≡ b mod n → k*m ≡ (b -a) mod n.

Which is:

k * m ≡ (b - a) mod n.

We can write this as:

k ≡ (b -a)/m mod (n / d) ?

Wait, the equation m*k ≡ (b -a) mod n.

Since m and n may not be coprime, let's see.

The equation m*k ≡ c mod n, where c = (b -a).

This equation has a solution in k iff gcd(m, n) divides c.

In our case, c = (b -a). But in the CRT step, we already checked that (a -b) is divisible by d, where d = gcd(m, n). Wait, no. Wait, the original congruence check is that (a -b) is divisible by d, but here we have (b -a) mod n.

Hmm, maybe it's better to use the general approach.

So, the code for solving two congruences could be:

def crt(a1, m1, a2, m2):

    # solve x ≡ a1 mod m1, x ≡ a2 mod m2

    d, x, y = extended_gcd(m1, m2)

    if (a2 - a1) % d != 0:

        return None

    lcm = m1 // d * m2

    x0 = (a1 + x * (a2 - a1) // d % (m2 // d) * m1) % lcm

    return x0

But implementing this correctly is tricky. Alternatively, there's a Pythonic way.

Alternatively, use the code from the Chinese Remainder Theorem.

Alternatively, find the minimal solution using modular arithmetic.

But for the sake of time, perhaps using the extended Euclidean algorithm.

Once we have the minimal t for each case, we can collect all four possible t's and choose the minimal one that's less than T.

Now, putting it all together.

First, for each sensor (xi, yi), compute T = LCM(n, m).

Then, for each of the four cases:

Case 1: a even, b even → t ≡ xi mod 2n, t ≡ yi mod 2m.

Case 2: a even, b odd → t ≡ xi mod 2n, t ≡ (m - yi) mod 2m.

Case 3: a odd, b even → t ≡ (n - xi) mod 2n, t ≡ yi mod 2m.

Case4: a odd, b odd → t ≡ (n - xi) mod 2n, t ≡ (m - yi) mod 2m.

For each case, solve the congruence equations. For each, if a solution exists, compute the minimal t >=0. Then, collect all four t's and find the minimal one that is less than T.

The code will need to handle all four cases, compute the possible t's, and then select the minimal valid one.

But first, we need to compute LCM(n, m), which can be done using the formula LCM(a,b) = a*b // GCD(a,b).

Implementing GCD with math.gcd, but note that in Python's math.gcd, it returns the absolute value, so for positive integers it's fine.

So, T = (n * m) // gcd(n, m).

Now, let's think about the code.

First, read n, m, k.

Compute GCD_n_m = math.gcd(n, m)

T = (n * m) // GCD_n_m

For each sensor (xi, yi):

   candidates = []

   for each of the four cases:

      compute required congruence parameters a_mod and a_rem, b_mod and b_rem.

      then, solve the congruence equations.

      if solution exists:

         t = solution

         if t >=0:

             candidates.append(t)

   if no candidates:

       print(-1)

   else:

       min_t = min(candidates)

       if min_t < T:

           print(min_t)

       else:

           print(-1)

But how to compute the solution for each case.

Implementing a CRT function that returns the minimal positive solution or None.

Let's implement a helper function for solving the two congruences.

def extended_gcd(a, b):

    if a == 0:

        return (b, 0, 1)

    else:

        g, y, x = extended_gcd(b % a, a)

        return (g, x - (b // a) * y, y)

def crt(a1, m1, a2, m2):

    # Solve x ≡ a1 mod m1

    # x ≡ a2 mod m2

    g, x, y = extended_gcd(m1, m2)

    if (a2 - a1) % g != 0:

        return None

    lcm = m1 // g * m2

    # Find x0 = a1 + k * m1

    k = (a2 - a1) // g * x % (m2 // g)

    x0 = a1 + k * m1

    return x0 % lcm

But need to test this function.

For example, case 1:

n=3, m=3, xi=1, yi=1.

Case 1: congruences t ≡1 mod 6 (2n=6), t≡1 mod 6 (2m=6).

Solution is 1, which is correct.

Which matches the first sample's first sensor.

But let's see. For the first sample:

T = LCM(3,3) =3.

The first sensor's case1 gives t=1, which is <3. So valid. The answer is 1.

Another example: the fourth sensor in the first sample is (2,2). For case4:

t ≡ (3-2) mod 6 → 1 mod 6.

t ≡ (3-2) mod 6 → 1 mod6.

So congruences are t≡1 mod6 and t≡1 mod6. Solution is 1. But case4 is a and b odd. So:

In case4, the equation is:

t = a*n + (n - xi) where a is odd.

But a is odd: a=1, 3, etc.

So for a=1, t=3 + (3-2) =3+1=4.

But according to the congruence solution, the minimal t is 1, which seems incorrect.

Wait, this is a problem. Because in case4, the congruence equations are t ≡ (n - xi) mod 2n and t ≡ (m - yi) mod 2m.

In the first sample, n=3, m=3, xi=2, yi=2.

Case4:

t ≡ (3-2) mod 6 → 1 mod6.

t ≡ (3-2) mod6 → 1 mod6.

So congruence solution is t=1, 7, 13, etc.

But according to the equation:

t = a*3 + (3-2) → a is odd.

For a=1: t=3*1 +1=4.

a=3: 3*3 +1=10.

So why does the congruence solution give t=1, which doesn't satisfy the equation.

Ah, here's the mistake: the congruence equations model t as the solution to the equation, but in reality, the equations for case4 are:

t = a*n + (n - xi) where a is odd → a can be written as 2k+1.

So t = (2k+1)*n + (n - xi) = 2k*n + n + (n - xi) = 2k*n + 2n - xi.

But this can be written as t = 2n(k+1) - xi.

So, modulo 2n, this is (-xi) mod 2n. Which is the same as (2n - xi) mod 2n.

But wait, in case4, the congruence for x is t ≡ (n - xi) mod 2n.

But (n - xi) mod 2n is the same as (n - xi + 2n) mod 2n → (3n -xi) mod 2n → but (n -xi) mod 2n is the required congruence.

So, for a=2k+1, t = 2k*n + n + (n-xi) = 2(k+1)*n - xi → which mod 2n is (2(k+1)*n -xi) mod 2n = (-xi) mod 2n. Which is equivalent to (2n - xi) mod 2n. So the congruence is t ≡ (n - xi) mod 2n.

But when we solve the congruence equations, we get t values that are congruent to (n-xi) mod 2n and (m - yi) mod 2m. However, these t's must also satisfy the equation for case4: t = a*n + (n - xi) where a is odd, and t = b*m + (m - yi) where b is odd.

But solving the congruence gives a t that satisfies the modular conditions, but we need to check if the solution can be written in terms of a and b being odd integers.

So, for example, in case4 of the first sample's fourth sensor (xi=2, yi=2):

n=3, m=3.

Congruence equations: t ≡ 1 mod6 (n-xi=3-2=1 mod6), and t≡1 mod6 (m-yi=3-2=1 mod6). So solution is t=1 mod6. Minimal t is 1.

But according to the case4 equation, t = a*3 + (3-2) = 3a +1. a is odd → a=1 → t=4, a=3 → t=10, etc.

So for t=1, there is no a odd such that t=3a+1. Because 3a+1=1 → 3a=0 → a=0, which is even. So this solution is invalid.

So, the congruence equations give possible t's, but we need to check if there exists a and b (with the required parity) such that t can be represented in the form required by the case.

This is a problem. So, the earlier approach of solving the congruence equations is insufficient because it doesn't account for the parity of a and b.

So, the mistake was to assume that solving the congruence equations for mod 2n and 2m is sufficient, but even after solving, we need to ensure that a and b are such that their parity corresponds to the case's parity.

Wait, but the congruence equations in the cases are designed so that the solution t can be expressed with a and b of the required parity. Or not?

In other words, for case1:

t ≡ xi mod 2n → which means that t can be written as a even multiple of n plus xi (since even a implies a=2k → t=2k*n + xi → mod 2n, it's xi → which is why the congruence is xi mod 2n).

Similarly for other cases.

So, perhaps solving the congruence equations gives the t's that are possible for the case's parity, but we need to ensure that t >= (xi for case1, or (n-xi) for case3, etc.) ?

No, because for case1, a can be 0, which is even. So t=0*n + xi = xi. Which is possible if xi is within the room. But in the problem, sensors are strictly inside, so xi is between 1 and n-1.

So, for case1, the minimal solution is t=xi, but in the first case, xi=1, which is indeed a valid time.

So, the issue arises when the congruence solution gives a t that is less than the required minimum for the case.

Wait, in case4, the minimal solution is t=1. But according to the case4's equations:

t = a*n + (n - xi) where a is odd.

For a=1, t=3*1 +1=4. But 4 is larger than the congruence solution of t=1.

So, the congruence solution may not satisfy the parity conditions for a and b.

Thus, the approach of solving the congruence equations and taking the minimal t is not sufficient. Because even if the congruence equations are satisfied, the parity of a and b may not match the case's requirements.

This is a major flaw in the previous reasoning.

So, what's the correct way to model a and b's parity?

Perhaps for each case, the congruence equations are correct, but the solution t must also be such that:

For case1 (even a, even b):

t >= xi (since a is even, a can be 0, 2, 4, etc.)

t = a*n + xi = even_a *n + xi.

But even_a can be 0, which gives t=xi. So, in this case, a is 0 (even), and the equation is t=xi = b*m + yi (b even).

So, for case1, a can be zero (even), but then b must also be even, and yi = xi. So, if xi = yi and xi is a solution to case1.

But for the fourth sensor in the first sample (xi=2, yi=2, n=3, m=3), case4's congruence solution is t=1, which is impossible. So, how to handle this?

The problem is that the congruence solution gives t=1, but according to case4's equation, t must be >= (n - xi) +n (since a is at least 1, being odd). Because a=1 gives t=1*3 + (3-2)=4, a=3 gives t=3*3 +1=10, etc.

So, the minimal possible t for case4 is 4, but the congruence solution gives t=1, which is not possible.

So, the approach is flawed.

Alternative approach: For each case, after solving the congruence equations and getting a possible t, we need to check whether there exists integers a and b (with the required parity) such that t can be expressed as per the case's equation.

But how to check that?

For case1:

t = a*n + xi, where a is even (>=0).

Also, t = b*m + yi, where b is even (>=0).

So, for a solution t from the congruence equations of case1:

We need to check that a = (t - xi) / n is even and >=0.

Similarly, b = (t - yi)/m must be even and >=0.

But since the congruence equations are t ≡ xi mod 2n and t ≡ yi mod 2m, then:

t can be written as xi + 2n * k for some integer k >=0.

Similarly, t = yi + 2m * l for some integer l >=0.

Thus, a = (t - xi)/n = (2n*k)/n = 2k → even.

Similarly, b = (t - yi)/m = 2m*l/m = 2l → even.

So, for case1, any solution t from the congruence equations will automatically have a and b even and >=0.

Because:

t = xi + 2n *k → a*n + xi = t → a = 2k.

So, a is even.

Similarly for b.

Thus, for case1, the solution t from the congruence equations automatically satisfies a and b being even and non-negative.

Similarly for other cases:

Case2: t = a*n + xi (a even), t = b*m + (m - yi) (b odd).

But the congruence equations are t ≡ xi mod 2n (so t = xi + 2n*k → a=2k even), and t ≡ (m - yi) mod 2m (so t = (m - yi) + 2m*l → which implies b = (t - (m-yi))/m = 2l + (m - yi + 2m*l - (m - yi)) /m → wait, perhaps not.

Alternatively, t = (m - yi) + 2m * l → t - (m - yi) = 2m*l → (t - (m - yi))/m = 2l → since m is a factor of 2m*l, this is 2l → even. But in case2, b must be odd.

Wait, no. For case2, the equation is:

t = b*m + (m - yi), where b is odd.

But t ≡ (m - yi) mod 2m → t can be written as (m - yi) + 2m*l.

So, t = (m - yi) + 2m*l = m*(2l) + (m - yi) = m*(2l +1) - yi.

So, b = 2l +1 → odd.

Ah, this is correct. Because:

t = (m - yi) + 2m*l → factor m:

t = m*(2l) + (m - yi) = m*(2l +1) - yi.

So, in this case, b = 2l +1 → odd.

Thus, for case2, the solution t from the congruence equations automatically satisfies that a is even and b is odd.

Similarly, for case3:

t = (n - xi) + 2n*k → a = 2k +1 (since t = a*n + (n - xi) → a*n = 2n*k → a=2k. Wait, no.

Wait, case3: a is odd.

The equation is t = a*n + (n - xi).

a is odd → a = 2k +1.

So, t = (2k+1)*n + (n - xi) = 2k*n + n + n - xi = 2k*n + 2n - xi → t = 2n(k +1) - xi.

Which can be written as t = 2n *k' - xi, where k' =k+1.

But the congruence equations for case3 are t ≡ (n - xi) mod 2n → t = (n - xi) + 2n*k'.

Which can be written as t = 2n*k' + (n - xi) = n*(2k') + (n - xi).

This would imply that a*n = 2n*k' → a= 2k', but case3 requires a to be odd. So, this is a contradiction.

Wait, this suggests a mistake in the earlier reasoning.

Alternatively, perhaps the congruence equations are not sufficient to model the parity of a and b.

This is a critical error in the approach. So, what's the correct way to model the parity of a and b?

Maybe the congruence approach is not sufficient, and a different method is needed.

Alternative approach:

The path of the laser can be represented in the mirrored grid. The line y = x in this grid. The sensor (xi, yi) must lie on this line in one of the mirrored cells. The mirrored cell is determined by the parity of reflections in x and y directions.

So, for each possible parity of reflections (even or odd in x and y), we can generate a possible mirrored position of the sensor and check if it lies on the line y=x.

For example, for even x reflections and even y reflections, the mirrored position is (xi, yi).

For even x and odd y, it's (xi, m - yi).

For odd x and even y, it's (n - xi, yi).

For odd x and odd y, it's (n - xi, m - yi).

Each of these positions (x', y') must lie on the line y=x in the mirrored grid. So, x' = y'.

But in the mirrored grid, the line is y=x. So, for the sensor's mirrored position to lie on this line, x' must equal y'.

So, for each of the four possible mirrored positions, check if x' == y'. If yes, then compute the time t = x' (since the line is y=x) and check if this t is valid (i.e., the mirrored position is in the correct parity cell, and the t is minimal).

So, the steps are:

For each sensor (xi, yi):

   Compute four possible mirrored positions:

   1. (xi, yi) → even x, even y → x' = xi, y' = yi.

      Check if xi == yi. If yes, t = xi.

      Also, check that this t corresponds to even number of reflections in x and y directions.

      But how to model the number of reflections.

      Wait, the number of reflections in x direction is determined by how many times the laser has crossed the vertical walls. For example, to reach the cell (a, b) in the mirrored grid, the number of vertical reflections is a, and horizontal reflections is b.

      But for the parity (even/odd), the mirrored position is determined by a and b's parity.

      So, for the mirrored position (x', y') to be in a cell with a even and b even, then the number of vertical reflections is a (even), and horizontal is b (even).

      The total time t is x' = a*n + x' (if a is even) → no, wait. For even a, the x-coordinate in the mirrored grid is a*n + xi. For odd a, it's (a+1)*n - xi.

      Alternatively, the position in the mirrored grid after a vertical reflections and b horizontal reflections is:

      x = a*n + (xi if a even else n - xi).

      y = b*m + (yi if b even else m - yi).

      And this (x, y) must lie on the line y = x.

      So, x = y.

      So:

      a*n + (xi if a even else n - xi) = b*m + (yi if b even else m - yi).

      We need to find non-negative integers a and b such that this equation holds.

      The minimal t is the minimal solution to this equation.

      The problem is to find the minimal t for each of the four possible combinations of a and b parity.

      But how to find a and b for each combination.

      For example, for the case where a is even and b is even:

      a must be even, b must be even.

      So, a = 2k, b = 2l.

      The equation becomes:

      2k *n + xi = 2l * m + yi.

      Rearranged:

      2k *n - 2l *m = yi - xi.

      Or:

      k*n - l*m = (yi - xi)/2.

      So, (yi - xi) must be even for this case to have a solution.

      If that's the case, then we can find integers k and l such that this equation holds.

      The minimal solution would be the minimal non-negative k and l that satisfy this equation.

      Similarly for other cases.

      This approach is possible, but solving for k and l in each case may be computationally intensive for large constraints.

      So, for each case, we can model the equation and find the minimal t.

      However, given the problem constraints (k up to 1e5 and per-testcase processing time), this approach may be feasible.

      So, for each sensor, and for each of the four cases, we need to solve an equation of the form:

      A *k + B *l = C.

      Where A and B are coefficients derived from n and m, and C is a constant.

      This is a linear Diophantine equation, and the minimal solution can be found using the extended Euclidean algorithm.

      For example, for case1:

      equation: 2kn + 2lm = yi - xi → Wait, no, the equation is 2k*n - 2l*m = yi - xi.

      Or, 2kn = 2lm + (yi - xi).

      So, 2kn - 2lm = yi - xi.

      We can divide both sides by d = gcd(2n, 2m), and check if (yi - xi) is divisible by d.

      If yes, then solutions exist.

      But solving this for each case may be time-consuming.

      Alternatively, perhaps the only possible solution for each case is to find t = x' = y', where x' and y' are in one of the four possible mirrored positions.

      So, for each of the four possible mirrored positions (x', y'), check if x' == y', and then compute t = x'.

      Then, among these possible t's, select the minimal one that is valid (i.e., the number of reflections in x and y directions for that mirrored position is even or odd according to the case).

      For example, for mirrored position (xi, yi) → case1.

      If xi == yi → t = xi.

      Then, check if this t can be achieved with even a and b.

      So, t = xi = a*n + xi → a = 0 (even), and t = yi = b*m + yi → b = 0 (even).

      So, this is valid.

      So, in this case, the time is xi, which is valid.

      For the fourth sensor in the first sample (xi=2, yi=2), case4 mirrored position is (n - xi, m - yi) = (1, 1). So x' = y' = 1 → t=1. But this mirrored position corresponds to a odd a and b.

      So, a and b must be odd.

      So, t=1 = a*n + (n - xi) → 1 = a*3 + 1 → a*3=0 → a=0, which is even. Not valid.

      So, this t=1 is not a valid solution for case4.

      Thus, this approach of checking the mirrored positions and seeing if x' == y' gives possible t's, but some of them may not be valid because the required a and b parities are not met.

      So, the steps for each sensor are:

      1. Generate the four mirrored positions.

      2. For each mirrored position (x', y'):

         a. If x' != y', skip.

         b. Otherwise, compute t = x'.

         c. Check if this t can be represented in the form required by the case's parity.

         d. If yes, add to candidates.

      3. Collect all valid t's from the four cases.

      4. Select the minimal t that is less than T.

      5. If no such t exists, output -1.

      So, the problem reduces to checking the four possible mirrored positions and seeing if any of them lie on the line y=x and can be achieved with the required parity.

      This approach is O(1) per sensor.

      Let's see how this works for the first sample:

      Sensor (1,1):

      Mirrored positions:

      case1: (1,1) → x'=y'=1. Check if a even and b even.

      a*n + xi = 0*3 +1=1, which equals t=1.

      So a=0 even.

      b*m + yi = 0*3+1=1. So b=0 even.

      Valid. So t=1 is a candidate.

      case2: (1, 3-1=2) → x'=1, y'=2. Not equal. No.

      case3: (3-1=2, 1) → x'=2, y'=1. No.

      case4: (2, 2) → x'=2, y'=2. Check if a and b are odd.

      t=2.

      a*n + (3-1) → a*3 +2 = 2 → a*3 =0 → a=0, even. Not valid.

      So, case4's mirrored position is (2,2) but a must be odd, which is not possible.

      So, the only valid candidate is case1's t=1.

      So, the answer is 1.

      For the fourth sensor (2,2):

      Mirrored positions:

      case1: (2,2) → x'=2, y'=2.

      Check if a even and b even.

      t=2.

      a*n + xi = 2 → a*3+2=2 → a=0 even.

      b*m + yi = 2 → b*3 +2=2 → b=0 even. Valid.

      So, t=2 is a candidate.

      case4: (3-2=1, 3-2=1) → x'=1, y'=1. So t=1.

      a and b must be odd.

      a*3 +1=1 → a=0 (even) → invalid.

      So, no.

      So, the valid candidate is case1's t=2.

      But wait, the first sample's fourth sensor output is 2, which matches this.

      So, this approach seems to work.

      So, the algorithm is:

      For each sensor (xi, yi), compute four mirrored positions:

      1. (xi, yi) → even x, even y.

      2. (xi, m - yi) → even x, odd y.

      3. (n - xi, yi) → odd x, even y.

      4. (n - xi, m - yi) → odd x, odd y.

      For each of these four mirrored positions:

         a. Check if x' == y'.

         b. If yes, compute t = x'.

         c. Check if t can be expressed in the form required by the case's parity.

            For case1 (even x, even y):

               t = a*n + xi → a = (t - xi)/n.

               a must be even and >=0.

               Also, t = b*m + yi → b = (t - yi)/m must be even and >=0.

            For case2 (even x, odd y):

               t = a*n + xi → a even.

               t = b*m + (m - yi) → b must be odd.

            Similarly for other cases.

         d. If both a and b have the required parity and are >=0, then this t is a valid candidate.

      After checking all four cases, collect all valid t's.

      Find the minimal t among them that is < T (the LCM(n, m)).

      If such a t exists, output it. Else, output -1.

      This approach is O(1) per sensor and doesn't require solving Diophantine equations, which is suitable for the problem's constraints.

      Let's see how this works for the fourth sensor in the first sample:

      Sensor (2,2).

      case1: mirrored position (2, 2). x' = y' =2.

      t=2.

      case1 requires even a and even b.

      a = (2 -2)/3 = 0 → even. valid.

      b = (2-2)/3 = 0 → even. valid.

      So, valid. t=2.

      case4: mirrored position (1, 1). x'=y'=1.

      t=1.

      case4 requires a and b to be odd.

      a = (1 - (3-2))/3 = (1 -1)/3 = 0 → even. invalid.

      So, no.

      So, the valid t is 2.

      Which is correct.

      Now, let's test case4 for the fourth sensor in the second sample.

      Sample 2: n=3, m=4. Sensor (2,3).

      The output is -1.

      Let's compute.

      Mirrored case4: (3-2=1, 4-3=1). x'=1, y'=1.

      t=1.

      a is odd:

      a*n + (3-2) = 1 → 3a +1=1 → a=0 → even. invalid.

      So, case4 is invalid.

      Other cases:

      case1: (2,3). x'=2, y'=3. 2 !=3. no.

      case2: (2, 4-3=1). x'=2, y'=1. no.

      case3: (3-2=1,3). x'=1, y'=3. no.

      case4: 1,1 → already checked. no.

      So, no valid t's. Output -1.

      So this approach works.

      Thus, the correct approach is to check all four possible mirrored positions, see if x' equals y', and verify that the required a and b parity holds for those t's.

      So, the code steps are:

      For each sensor (xi, yi):

         T = LCM(n, m)

         candidates = []

         for each of four cases:

             compute x' and y' based on the case.

             if x' != y', skip.

             else, t = x'

             compute a and b for x and y directions, according to the case's parity.

             if a and b are integers >=0 and have the required parity, add t to candidates.

         find the minimal t in candidates that is < T.

         output this t or -1.

      Now, the code needs to compute for each case:

      For case1 (even x, even y):

         x' = xi

         y' = yi

         if x' == y':

             t = x'

             a = (t - xi) // n

             since case1 requires a even, and a = (t - xi)/n.

             but t = xi → (xi - xi)/n = 0 → a=0 (even).

             also, b = (t - yi)/m → (xi - yi)/m.

             but wait, for case1, the equation is t = a*n + xi (a even) and t = b*m + yi (b even).

             So, a = (t - xi)/n → since t = xi, a=0.

             b = (t - yi)/m → (xi - yi)/m.

             For case1 to be valid, (xi - yi) must be divisible by m, and b must be even and >=0.

             Similarly for other cases.

      Wait, this is more complex. Because the mirrored position is x' = y', but the way to compute a and b depends on the case.

      Let me re-express for each case:

      For case1: even x, even y.

         x' = xi

         y' = yi

         if x' != y' → skip.

         else:

             t = x'

             a = (t - xi) / n → since case1 requires a even.

             But t = xi → a = 0, which is even.

             Also, the equation for y direction is t = b*m + yi → b = (t - yi)/m.

             So, if (t - yi) is not divisible by m → no.

             Also, b must be even and >=0.

      So, for case1:

         if x' == y' (xi == yi):

             check if (t - yi) is divisible by m → (xi - yi) must be divisible by m.

             and b = (xi - yi)/m must be even and >=0.

             if yes → valid.

      For example, if xi = yi = 2, n=3, m=3.

         t=2.

         a = (2-2)/3=0 → even.

         b = (2-2)/3=0 → even. valid.

         So case1 is valid.

      Another example: xi=1, yi=1, n=3, m=3.

         a=0, b=0. valid.

      For case2 (even x, odd y):

         x' = xi

         y' = m - yi

         if x' != y' → skip.

         else:

             t = x'

             a = (t - xi)/n → must be even.

             b = (t - (m - yi))/m → must be odd.

             Also, a and b must be integers >=0.

      For example, in sample 2:

         sensor (1,3):

         case2: x' = 1, y' = 4 -3 =1 → t=1.

         a = (1-1)/3 = 0 → even.

         b = (1 - (4-3))/4 = (1-1)/4 =0 → but case2 requires b to be odd. So invalid.

         So, no.

      For case3 (odd x, even y):

         x' = n - xi

         y' = yi

         if x' == y' → t = x'.

         a = (t - (n - xi))/n → must be odd.

         b = (t - yi)/m → must be even.

      For example, sensor (n-xi, yi) must equal each other.

      For case4 (odd x, odd y):

         x' = n - xi

         y' = m - yi

         if x' == y' → t = x'.

         a = (t - (n - xi))/n → must be odd.

         b = (t - (m - yi))/m → must be odd.

      So, the code needs to check these conditions for each case.

      So, implementing this in code:

      For each sensor:

          candidates = []

          # case1: even x, even y.

          x_case1 = xi

          y_case1 = yi

          if x_case1 == y_case1:

              t = x_case1

              # check x direction: a = (t - xi)/n → 0 must be even.

              a = (t - xi) // n

              if (t - xi) % n != 0:

                  pass

              else:

                  # a is even?

                  if a % 2 ==0 and a >=0:

                      # check y direction: b = (t - yi)/m

                      b = (t - yi) // m

                      if (t - yi) % m ==0 and b % 2 ==0 and b >=0:

                          candidates.append(t)

          # case2: even x, odd y.

          x_case2 = xi

          y_case2 = m - yi

          if x_case2 == y_case2:

              t = x_case2

              # a = (t - xi)/n → even.

              a = (t - xi) // n

              if (t - xi) % n !=0:

                  pass

              else:

                  if a % 2 ==0 and a >=0:

                      # b = (t - (m - yi))/m → must be odd.

                      b = (t - (m - yi)) // m

                      if (t - (m - yi)) % m ==0 and b % 2 ==1 and b >=0:

                          candidates.append(t)

          # case3: odd x, even y.

          x_case3 = n - xi

          y_case3 = yi

          if x_case3 == y_case3:

              t = x_case3

              # a = (t - (n - xi))//n → must be odd.

              a = (t - (n - xi)) // n

              if (t - (n - xi)) % n !=0:

                  pass

              else:

                  if a % 2 ==1 and a >=0:

                      # b = (t - yi) //m → even.

                      b = (t - yi) // m

                      if (t - yi) % m ==0 and b%2 ==0 and b >=0:

                          candidates.append(t)

          # case4: odd x, odd y.

          x_case4 = n - xi

          y_case4 = m - yi

          if x_case4 == y_case4:

              t = x_case4

              # a = (t - (n - xi))//n → must be odd.

              a = (t - (n - xi)) // n

              if (t - (n - xi)) % n !=0:

                  pass

              else:

                  if a %2 ==1 and a >=0:

                      # b = (t - (m - yi))//m → must be odd.

                      b = (t - (m - yi)) // m

                      if (t - (m - yi)) % m ==0 and b%2 ==1 and b >=0:

                          candidates.append(t)

          # Now, find minimal t in candidates that is < T.

          T = (n * m) // math.gcd(n, m)

          valid = [t for t in candidates if t < T]

          if valid:

              print(min(valid))

          else:

              print(-1)

      This code handles all four cases by checking the mirrored positions and the required a and b parities.

      Testing this code with the first sample:

      Sample1:

      n=3, m=3, sensor (2,2):

      case1:

      x=2, y=2.

      t=2.

      a=(2-2)/3=0 → even.

      b=(2-2)/3=0 → even. valid.

      case4:

      x=1, y=1 → t=1.

      a = (1 - (3-2)) /3 = (1-1)/3=0 → even → invalid.

      So, case4 is not valid.

      So, valid candidate is 2.

      Which is correct.

      Another example from sample 2:

      Sample2:

      n=3, m=4.

      Sensor (2,3) in the sixth input.

      case4:

      x_case4=3-2=1, y_case4=4-3=1 → x==y.

      t=1.

      a = (1 - (3-2)) /3 = (1-1)/3=0 → even. invalid.

      So, case4 is not valid.

      Other cases:

      case1: x=2, y=3 → no.

      case2: x=2, y=1 → 2 !=1.

      case3: x=3-2=1, y=3 → 1 !=3.

      So, no candidates. Output -1.

      Which matches the sample.

      So, this code should work.

      Now, handling large values of n and m.

      For example, in sample3:

      Input:

      7 4 5

      1 3

      2 2

      5 1

      5 3

      4 3

      Output:

      13

      2

      9

      5

      -1

      Let's take the second sensor (2,2):

      case1: x=2, y=2. t=2.

      a= (2-2)/7 =0 → even.

      b=(2-2)/4=0 → even. valid. So, t=2 is a candidate. And T= LCM(7,4)=28. So 2 < 28 → valid. Output is 2.

      Which matches the sample.

      So, this code should handle all cases correctly.

      Now, implementing this in Python.

      Edge Cases:

      - sensor at (1,1) in a room with n=2, m=2. T=2. case1: t=1 <2 → valid.

      - sensor at (n-1, m-1) → possible case4.

      - sensor positioned such that x'=y' but a or b is negative.

      So, the code must check a and b are >=0.

      Now, the code.

      Also, note that in Python, integer division with negative numbers uses floor division, but since all terms are positive (xi and yi are >=1, and n and m >=2), the computed a and b should be positive or zero.

      Now, the code:

      import math

      def main():
          import sys
          input = sys.stdin.read().split()
          idx = 0
          n = int(input[idx]); idx +=1
          m = int(input[idx]); idx +=1
          k = int(input[idx]); idx +=1
          T = (n * m) // math.gcd(n, m)
          for _ in range(k):
              xi = int(input[idx]); idx +=1
              yi = int(input[idx]); idx +=1
              candidates = []
              # Case 1: even x, even y
              x1 = xi
              y1 = yi
              if x1 == y1:
                  t = x1
                  # Check a and b
                  a = (t - xi) // n
                  if (t - xi) % n == 0 and a >=0 and a % 2 == 0:
                      b = (t - yi) // m
                      if (t - yi) % m ==0 and b >=0 and b %2 ==0:
                          candidates.append(t)
              # Case 2: even x, odd y
              x2 = xi
              y2 = m - yi
              if x2 == y2:
                  t = x2
                  a = (t - xi) // n
                  if (t - xi) % n ==0 and a >=0 and a %2 ==0:
                      b_val = t - (m - yi)
                      if b_val <0:
                          continue
                      b = b_val // m
                      if b_val % m ==0 and b >=0 and b %2 ==1:
                          candidates.append(t)
              # Case 3: odd x, even y
              x3 = n - xi
              y3 = yi
              if x3 == y3:
                  t = x3
                  a_val = t - (n - xi)
                  if a_val <0:
                      continue
                  a = a_val // n
                  if a_val %n ==0 and a >=0 and a %2 ==1:
                      b_val = t - yi
                      if b_val <0:
                          continue
                      b = b_val // m
                      if b_val %m ==0 and b >=0 and b %2 ==0:
                          candidates.append(t)
              # Case4: odd x, odd y
              x4 = n - xi
              y4 = m - yi
              if x4 == y4:
                  t = x4
                  a_val = t - (n - xi)
                  if a_val <0:
                      continue
                  a = a_val // n
                  if a_val %n ==0 and a >=0 and a %2 ==1:
                      b_val = t - (m - yi)
                      if b_val <0:
                          continue
                      b = b_val // m
                      if b_val %m ==0 and b >=0 and b %2 ==1:
                          candidates.append(t)
              # Find minimal valid t < T
              valid = [t for t in candidates if t < T]
              if valid:
                  print(min(valid))
              else:
                  print(-1)

      if __name__ == "__main__":
          main()

      Now, let's test this code with the first sample:

      Input:

      3 3 4

      1 1

      1 2

      2 1

      2 2

      Output:

      1

      -1

      -1

      2

      Let's see for the fourth sensor (2,2):

      case1: x1=2, y1=2. t=2.

      a = (2-2)/3=0 even.

      b = (2-2)/3=0 even. valid. → t=2 is added.

      So, valid = [2], which is < T=3. So output 2.

      Which is correct.

      For the third sensor (2,1):

      case3: x3=3-2=1, y3=1. x3 == y3. t=1.

      a_val=1 - (3-2) =0 → a=0/3=0. a_val=0 → a=0. but case3 requires a to be odd. So invalid.

      So, no candidates. output -1.

      Which matches the sample.

      So, this code should work.
</think>

```python
import math

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx]); idx +=1
    m = int(input[idx]); idx +=1
    k = int(input[idx]); idx +=1
    T = (n * m) // math.gcd(n, m)
    for _ in range(k):
        xi = int(input[idx]); idx +=1
        yi = int(input[idx]); idx +=1
        candidates = []
        # Case 1: even x, even y
        x1 = xi
        y1 = yi
        if x1 == y1:
            t = x1
            a = (t - xi) // n
            if (t - xi) % n == 0 and a >=0 and a % 2 == 0:
                b = (t - yi) // m
                if (t - yi) % m ==0 and b >=0 and b %2 ==0:
                    candidates.append(t)
        # Case 2: even x, odd y
        x2 = xi
        y2 = m - yi
        if x2 == y2:
            t = x2
            a = (t - xi) // n
            if (t - xi) % n ==0 and a >=0 and a %2 ==0:
                b_val = t - (m - yi)
                if b_val <0:
                    continue
                b = b_val // m
                if b_val % m ==0 and b >=0 and b %2 ==1:
                    candidates.append(t)
        # Case 3: odd x, even y
        x3 = n - xi
        y3 = yi
        if x3 == y3:
            t = x3
            a_val = t - (n - xi)
            if a_val <0:
                continue
            a = a_val // n
            if a_val %n ==0 and a >=0 and a %2 ==1:
                b_val = t - yi
                if b_val <0:
                    continue
                b = b_val // m
                if b_val %m ==0 and b >=0 and b %2 ==0:
                    candidates.append(t)
        # Case4: odd x, odd y
        x4 = n - xi
        y4 = m - yi
        if x4 == y4:
            t = x4
            a_val = t - (n - xi)
            if a_val <0:
                continue
            a = a_val // n
            if a_val %n ==0 and a >=0 and a %2 ==1:
                b_val = t - (m - yi)
                if b_val <0:
                    continue
                b = b_val // m
                if b_val %m ==0 and b >=0 and b %2 ==1:
                    candidates.append(t)
        # Find minimal valid t < T
        valid = [t for t in candidates if t < T]
        if valid:
            print(min(valid))
        else:
            print(-1)

if __name__ == "__main__":
    main()
```