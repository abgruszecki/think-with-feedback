<think>
Okay, I need to solve this problem where a ball is moving on a billiard table and I have to determine which pocket it ends up in, if any. Let's think through the problem carefully.

First, let's understand the movement of the ball. The problem states that the ball moves in a direction that's either parallel to the axes or at a 45-degree angle. Wait, no—the initial velocity components are either -1, 0, or 1. So the direction is determined by vx and vy, which can be combinations like (-1, 1) meaning moving diagonally up-left, etc. Wait, but the problem statement says the direction is such that the ball moves along a line that's parallel to the axes or 45 degrees. Because the velocity components are either -1, 0, or 1. So each step, the ball's movement is in a direction where dx and dy are either 0 or 1 in some combination, but scaled by the velocity. Wait, no—the velocity components are given as vx and vy, which can be -1, 0, or 1. But the ball moves in a straight line until it hits a wall and reflects. So the problem is about reflections.

The key here is that when the ball reflects off a wall, the direction changes according to the law of reflection. But instead of simulating the reflections, which could be infinite, we can model this using the concept of unfolding the grid. Because each reflection can be considered as mirroring the grid, so the ball's path becomes a straight line in this extended grid. The pockets are located at the corners of the original grid, so their positions in the mirrored grids would depend on the number of reflections in each direction.

So the idea is to find the least common multiple (LCM) of the number of times the ball reflects in the x and y directions. By unfolding the grid, the ball's trajectory can be represented as a straight line. The destination pocket can be determined based on the parity of the number of reflections in each direction.

Let me think. For example, if the ball moves in such a way that after even reflections in the x direction, it ends up at x=0 or x=n, and similarly for y, then the pocket depends on whether the number of reflections is even or odd. Each reflection in x direction would flip the grid, so after even reflections, the original position's x is mirrored even times, so 0 becomes 0 again. Wait, maybe not. Let me think again.

Alternatively, the ball's movement can be modeled as moving in a grid that's mirrored multiple times. The total distance traveled in x and y directions (after considering reflections) would be such that when divided by n or m, the parity of the quotient determines the final pocket.

So the process is to find the number of times the ball would bounce off the walls (even or odd) in the x and y directions, and based on that, determine the corner. But how?

Let me formalize this. Let's model the problem by unfolding the grid through reflections. The ball's path is a straight line in this extended grid. The coordinates of the pockets in this extended grid would be (k*n, l*m) where k and l are integers (positive or negative, depending on the direction). But the parity of k and l determines which original pocket the ball ends up in.

Wait, the original pockets are at (0,0), (0,m), (n,0), (n,m). Each time you reflect the grid in the x direction, a pocket at (n, y) would become (n + n, y) = (2n, y), but after an even number of reflections, the x-coordinate would be 0 mod 2n (if even reflections) or n mod 2n (if odd). Similarly for y-direction.

So the idea is to find the minimal k and l such that the ball's path, when extended straight, reaches a point (k * n, l * m), considering the direction of movement. The parity of k and l will determine the pocket.

But wait, the velocity components are given. For example, if the initial velocity is (vx, vy) = (-1, 1), the direction is towards the left and upwards. So when unfolded, the ball's path would be a straight line. The total displacement in x and y directions must be multiples of n and m, but multiplied by some factors depending on the number of reflections.

So perhaps the key is to model the problem as finding integers a and b such that the displacement in x is a*n, displacement in y is b*m, and the direction of these displacements depends on the velocity's signs.

Wait, the velocity's direction determines the direction of movement. For example, if vx is -1, then the ball is moving to the left. So each time it reflects in the x direction, the direction flips. But in the unfolded grid, the direction is considered as moving straight, and the number of reflections determines which mirrored grid the ball is in.

Alternatively, the ball's movement can be considered as follows: in the x-direction, the ball will move a distance that is a multiple of n (after some reflections), and similarly for the y-direction. The parity of the number of reflections in each direction will determine which corner it ends up in.

Let me formalize this. Suppose the ball travels a total distance in the x-direction of dx, and dy in the y-direction. Because the ball moves in a straight line (when considering reflections), dx and dy must be such that dx / dy is equal to the ratio of the velocity components. Wait, but the velocity components can be 0. Hmm. If the velocity in x is 0, then the ball moves only along the y-axis. Similarly for velocity in y 0.

So the key is to find the minimal positive integers kx and ky such that:

dx = kx * n (if the ball reflects even times in x direction) or (kx * 2 * n) (if odd?), but I'm not sure.

Alternatively, the movement can be modeled by considering that after each reflection, the direction in that axis flips. The ball's path can be represented as moving in a straight line through mirrored copies of the table. The end pocket is at a point (a * n, b * m) where a and b are integers (possibly even or odd), and the parity of a and b determine which pocket.

But how to model this? Let's see. The original table is from (0,0) to (n,m). When the ball reflects off a vertical wall (x=0 or x=n), the x direction reverses. So the mirrored grid approach would have the ball continue in a straight line into a mirrored table. For example, after one reflection in the x direction (right wall), the next grid is mirrored, so the x coordinate would be 2n - x. So, the path can be thought of as moving through these mirrored grids, and the total displacement in x and y directions would be such that x + k*2n or (k*2n - x) if the number of reflections is odd.

Wait, perhaps the correct approach is to model the ball's movement as a straight line in the extended grid, where the grid is mirrored each time. The ball's end point must be a corner (0,0), (0,m), (n,0), (n,m) in some mirrored grid. So the coordinates of the end point would be (a * n, b * m), where a and b are integers (positive or negative) such that the displacement from the starting point (x, y) to (a*n, b*m) is in the direction of the velocity vector.

But the velocity vector can have components of 0. For example, if vy is 0, then the ball moves only in the x direction. So in that case, the ball would eventually hit a vertical pocket (like if it's moving along x=0 or x=n), but only if its y coordinate is 0 or m. But according to the problem statement, the ball is not initially in a pocket, but if the y coordinate is 0 or m, then it would hit the pocket when it reaches x=0 or x=n. Otherwise, it's moving along a side (y=0 or y=m) but not hitting a pocket. Wait, but the problem states that if the ball is moving along a side (like y is 0 and moving along x direction), then it will fall into the pocket at the end of the side. So for example, if the ball is at (x, 0) and moving right (vx=1, vy=0), then when it reaches (n,0), which is a pocket, it stops.

But in the case where the ball is moving along a side but the direction is not towards a pocket, it would not stop. For example, if the ball is at (x, 0) and moving left (vx=-1, vy=0), then it will reach (0,0), which is a pocket, but if x is between 0 and n, then moving left would take it to 0. So in that case, it would end up in (0,0). But if the ball is moving along the side in the opposite direction of a pocket, then it will reach the pocket.

Wait, but according to the problem statement, the ball can move along a side and will fall into the pocket at the end of the side. So for example, if the ball is moving exactly along the x-axis (y is 0, vy=0, vx is either 1 or -1), then it will end up in either (0,0) or (n,0). Similarly, if moving along the y-axis (x is 0 or n, vx=0), then it ends up in (0, m) or (n, m) if moving up, or (0,0) or (n,0) if moving down.

So first, let's handle the cases where the velocity has a zero component.

Case 1: vx is 0. Then the ball is moving purely in the y direction. So for it to end up in a pocket, its x coordinate must be 0 or n, and it must reach either 0 or m in y. Otherwise, it will keep bouncing between the top and bottom walls.

Wait, no. For example, if vy is 1 (moving up), and x is not 0 or n. Then the ball will move up and down between y=0 and y=m, but since x is not 0 or n, it's not along the edges. So in that case, the ball will never reach a pocket and will move indefinitely.

So for the velocity components to be zero in one direction:

If vx is 0:

- Then the ball's x coordinate remains x. So to hit a pocket, x must be either 0 or n (since the pockets are at 0 and n in x). If x is 0 or n, then the ball is moving along the left or right edge. Then, if vy is 1, the ball is moving up, and will reach (x, m) which is a pocket. If vy is -1, it moves down to (x, 0) which is a pocket. If x is not 0 or n, then the ball will oscillate between the top and bottom walls, never reaching a pocket. So in this case, the answer is -1 unless x is 0 or n.

Similarly, if vy is 0:

- The ball's y coordinate remains y. So to hit a pocket, y must be 0 or m. Then, depending on vx, it will move left or right to reach the end (x 0 or n). Otherwise, if y is not 0 or m, it will move back and forth between left and right walls, never reaching a pocket.

So the first step is to check for cases where either vx or vy is zero.

Let's code that. For example:

If vx is 0:

   if x is 0 or n:

      if vy is 1: y will reach m, so pocket is (x, m)

      else (vy is -1): pocket is (x, 0)

   else:

      output -1

Similarly for vy is 0.

So these are the straightforward cases.

Now, the more complex cases are when both vx and vy are non-zero. So the ball is moving diagonally.

In this case, the ball's path can be modeled as a straight line through mirrored grids. The key is to find the least common multiple of some periods in x and y directions.

Let's model the problem as follows. The ball moves with direction (vx, vy). Each time it hits a vertical wall (x=0 or x=n), the x component of velocity reverses. Similarly for horizontal walls. But instead of tracking the reflections, we can model this as the ball moving in a straight line through mirrored copies of the table. The ball's path in this extended grid is a straight line. The pockets are located at positions (k*n, l*m) where k and l are integers, and the parity of k and l determines which original pocket this corresponds to.

For example, if the ball travels to (2n, m), this would correspond to reflecting the table once in the x direction (so it's a mirror image), and the point (2n, m) in the mirrored grid corresponds to the original (0, m) pocket. Because after one reflection (k=2?), no, wait. Let me think: the original table is 0 <= x <=n. When we mirror it once in the x direction, the next copy would have x from n to 2n. So the point (2n, m) in the mirrored grid would be the same as the original (0, m) pocket. Wait, no—mirroring in x direction once would reverse the direction. Hmm, perhaps the parity of the number of mirrors determines the actual x-coordinate.

Alternatively, each time the ball crosses a vertical boundary (x=n or x=0), the x-coordinate is mirrored. So the path in the extended grid can be considered as a straight line, and the number of mirrors crossed in x and y directions is even or odd.

The key is to find the minimal distance that the ball travels such that the displacement in x and y directions are integer multiples of 2n and 2m, respectively. Or perhaps not. Let's think differently.

The ball's trajectory after any number of reflections can be represented as a straight line in the extended grid. The pockets in the extended grid are at positions (a*n, b*m), where a and b are integers, and the parity of a and b determine which pocket it is. For example:

- (even a, even b): (0,0)
- (even a, odd b): (0, m)
- (odd a, even b): (n, 0)
- (odd a, odd b): (n, m)

But how to find a and b such that the ball's path passes through (a*n, b*m)?

The ball's movement starts at (x,y) and moves in direction (vx, vy). So the parametric equations are:

x(t) = x + vx * t

y(t) = y + vy * t

We need to find t>0 such that x(t) is a*n and y(t) is b*m, for some integers a and b. Then, the parity of a and b will determine the pocket.

But also, the velocity directions must be compatible with the path leading to that point. For example, if vx is positive, then the ball is moving towards increasing x, so a must be >= 0 if x is moving in the positive direction. Wait, no: because in the mirrored grid, the direction is preserved. Hmm, perhaps a and b can be any integers, but the path must reach (a*n, b*m) given the initial velocity direction.

Wait, but the velocity components are either -1 or 1. So the direction is fixed. For example, if vx is 1, the ball is moving in the positive x direction. So in the extended grid, the path is a straight line with positive x direction. So a*n must be greater than or equal to x (if vx is 1) or less than x (if vx is -1). Wait, no. Because in the mirrored grid, when the ball reflects, the direction reverses. So in the extended grid, the path is a straight line with the same direction. But the parity of the number of reflections (a) would determine the actual direction.

Alternatively, when the ball moves in the extended grid, each time it crosses a vertical line at x=k*n, it's a reflection. So the parity of k (the number of times it crossed x) determines whether the x coordinate in the original table is (k*n - current_x) or (current_x - (k-1)*n). Not sure.

Alternatively, the ball's movement in the extended grid is a straight line with direction (vx, vy). So in this grid, the ball's path is x(t) = x + vx * t, y(t) = y + vy * t. The points where the ball would reach a pocket in the extended grid are (a*n, b*m), where a and b are integers. But the velocity directions must allow the ball to reach that point without changing direction.

So for example, if vx is 1, then the ball's x(t) is increasing. So a must be such that a*n >= x (if vx is 1) or a*n <= x (if vx is -1). Similarly for y.

Wait, but the velocity direction is fixed. So for vx=1, the ball is moving to the right. So in the extended grid, the x(t) increases, so the a*n must be >= x, and the path must pass through a*n in the x direction.

So, the problem reduces to finding integers a and b such that:

a*n = x + vx * t

b*m = y + vy * t

for some t>0.

We can solve for t in both equations:

t = (a*n - x)/vx

t = (b*m - y)/vy

So these two must be equal, so:

(a*n -x)/vx = (b*m - y)/vy

But since vx and vy can be -1 or 1, we can multiply both sides by vx * vy (which is either 1 or -1) to get:

vy*(a*n -x) = vx*(b*m - y)

This is the key equation. We need to find integers a and b such that this equation holds, and the t computed from both is positive.

Once we find such a and b, the pocket is determined by the parity of a and b. For example, if a is even, then in the x direction, the ball has undergone an even number of reflections, so the x-coordinate in the original table is (a*n) mod (2n), but perhaps the parity tells us whether it's at 0 or n. Wait, no. Let me think again.

The parity of a determines whether the number of reflections in the x direction is even or odd. For example, a=0: the ball moves to x=0 (original pocket). a=1: after crossing once, the ball is at x=n (original pocket), but that's in the first mirrored grid. Wait, perhaps when a is even, the x-coordinate is in the original grid (0 or n), and when a is odd, it's in the mirrored grid. So the parity of a and b determines which of the four pockets the ball ends up in.

For example:

If a is even: the x-coordinate is 0 or n (depending on a being even but how?), but wait, a*n must be even multiples of n. Wait, no. For example, a=0 gives x=0, a=2 gives x=2n. But in the mirrored grid, a=2n would be equivalent to x=0 in the original grid (since each mirror flips the direction). So the parity of a (even or odd) would determine whether the x-coordinate in the original grid is 0 or n. Similarly for b.

Wait, perhaps when a is even, the x-coordinate in the original table is 0 if a is even and direction is such that it ends there. For example, a=0: x=0. a=1: x=n. a=2: x=0 (but mirrored once in x and once again). So the parity of a determines whether the x-coordinate is 0 or n.

So the parity of a (even or odd) determines the x component of the pocket. Similarly for b and the y component.

So the steps to solve the problem are:

1. Handle cases where either vx or vy is zero. As discussed earlier.

2. For cases where both vx and vy are non-zero:

   a. Solve the equation vy*(a*n - x) = vx*(b*m - y) for integers a and b.

   b. Find the minimal t>0 such that t is (a*n -x)/vx and (b*m -y)/vy, and both are equal and positive.

   c. Determine the parity of a and b (even/odd) to determine the pocket.

But how to find a and b?

Let's rearrange the equation:

vy*(a*n -x) = vx*(b*m - y)

=> vy * a*n - vy*x = vx*b*m - vx*y

Rearranged:

vy * a * n - vx * b * m = vy *x - vx * y

But this is a linear Diophantine equation in variables a and b.

The equation can be written as:

(vy * n) * a - (vx * m) * b = (vy x - vx y)

Let me denote:

A = vy * n

B = -vx * m

C = vy * x - vx * y

So the equation is A*a + B*b = C.

We need to find integer solutions (a, b) to this equation.

Once we find a and b, we can compute t for each and check if they are equal and positive.

But solving this equation can be tricky. Let's see.

First, note that A and B are coefficients, and we need to find integers a and b such that A*a + B*b = C.

But since vx and vy can be -1 or 1, let's compute A and B for all possibilities.

Possible cases for (vx, vy):

(1,1), (1,-1), (-1,1), (-1,-1)

For example, if vx=1 and vy=1:

A = 1 * n

B = -1 * m

C = 1*x -1*y = x - y

Equation: n*a - m*b = x - y

Similarly for other combinations.

So the Diophantine equation needs to be solved for a and b. However, since a and b must be integers, the equation must have solutions. The equation A*a + B*b = C has solutions in integers if and only if GCD(A, B) divides C.

Once we have the solutions, we need to find the minimal positive t such that t = (a*n -x)/vx and t = (b*m - y)/vy. Since vx and vy are either 1 or -1, we can compute t and ensure it's positive.

But how to find the minimal t? Because there are infinitely many solutions once a solution exists. So we need to find the minimal t such that a and b lead to t being positive.

Alternatively, once a and b are found, the t must satisfy:

t = (a*n -x) / vx

t = (b*m - y) / vy

And since vx and vy are either 1 or -1, the denominator is ±1, so t must be equal to (a*n -x)*vx (since dividing by vx is same as multiplying by vx when vx is ±1).

Wait, because 1/vx is vx (since vx is ±1). Because if vx is 1, then 1/vx is 1. If vx is -1, then 1/vx is -1. So t can be written as (a*n -x) * vx.

Similarly for the other equation: t = (b*m - y) * vy.

So t must be the same in both expressions.

So solving for a and b such that (a*n -x)*vx = (b*m - y)*vy.

But perhaps a better approach is to express a and b in terms of t.

For example:

a = (x + vx * t) / n

b = (y + vy * t) / m

Since a and b must be integers, and t must be positive.

But this requires that x + vx*t is divisible by n and y + vy*t is divisible by m.

So t must be such that:

t ≡ ( (n - x) / vx ) mod something? Not sure.

Alternatively, t must be chosen such that (x + vx * t) is a multiple of n, and (y + vy * t) is a multiple of m.

Let's see. For example, if vx is 1:

x + t ≡ 0 mod n → t ≡ (-x) mod n. So t = k*n - x, where k is a positive integer (since t must be positive). But then, substituting into the y equation:

y + vy * t must be a multiple of m.

So for each possible t in the x direction (k*n -x for k >= 1), check if it also satisfies the y condition.

Similarly, if vx is -1:

x - t ≡ 0 mod n → t ≡ x mod n → t = x + k*n, for k >=0 (since t must be positive).

But then for t = x + k*n, we need y + vy*t must be divisible by m.

So the problem becomes finding the minimal t that satisfies both conditions. But for large n and m (up to 1e9), iterating over possible k is not feasible. So we need a mathematical approach.

The key is to model this as a system of congruences.

Let's consider the equations:

x + vx * t ≡ 0 mod n → (vx * t) ≡ (-x) mod n

y + vy * t ≡ 0 mod m → (vy * t) ≡ (-y) mod m

We need to find t that satisfies both congruences.

Let's represent these as:

t ≡ a mod n/(gcd(vx, n)) → but since vx is ±1, which is coprime with n (since n is >=1). So the modulus for the first congruence is n. Similarly for the second.

Wait, since vx is ±1 and n can be any integer >=1, but since vx is either 1 or -1, which are both coprime with any n. So the first congruence equation is:

vx * t ≡ (-x) mod n → t ≡ (-x) * vx mod n → because multiplying both sides by vx (since vx^2 =1).

Similarly for the second:

vy * t ≡ (-y) mod m → t ≡ (-y) * vy mod m.

So the two congruence equations are:

t ≡ (-x * vx) mod n

t ≡ (-y * vy) mod m

So solving these two congruences for t gives the possible solutions. The minimal positive solution t must be found, and then check if the corresponding a and b (from the equations a = (x + vx * t)/n, b = (y + vy * t)/m) are integers, and then determine their parity.

But how to solve these two congruences?

This is a classic Chinese Remainder Theorem (CRT) problem. The two congruences must be compatible (i.e., have a common solution), and the minimal positive t is the solution.

So steps:

1. Check if the two congruences t ≡ a mod n and t ≡ b mod m (where a = (-x * vx) mod n, b = (-y * vy) mod m) have a solution.

2. If there is no solution, then the ball will never reach a pocket, output -1.

3. If there is a solution, find the minimal positive t that satisfies both congruences.

4. Check if t is positive (since t must be positive), then compute a and b as (x + vx * t)/n and (y + vy * t)/m. Then, check the parity of a and b to determine the pocket.

But wait, in the congruence equations, the modulus is n and m. The CRT applies when the moduli are coprime, but in general, the solution exists if and only if a ≡ b mod gcd(n, m). So we can proceed as follows:

Compute the desired residues:

a1 = (-x * vx) % n

a2 = (-y * vy) % m

We need to solve for t such that:

t ≡ a1 (mod n)

t ≡ a2 (mod m)

The solution exists if and only if a1 ≡ a2 mod gcd(n, m). If this is not the case, then there is no solution, meaning the ball never enters a pocket.

Once a solution exists, find the minimal positive t. Then compute a = (x + vx * t) /n and b = (y + vy * t)/m. These a and b must be integers. Then, the parity of a and b (even or odd) determines the pocket.

But wait, let's verify this. For example, if vx is 1 and t is such that x + t = a*n. So a = (x + t)/n. Since t is congruent to (-x) mod n (from the congruence equation), x + t ≡ x + (-x) mod n → 0 mod n. So x + t is a multiple of n, hence a is integer.

Similarly for vy and m.

So a and b are integers.

The parity of a and b determines the pocket:

- If a is even: x-coordinate is 0 (since even number of reflections brings back to original x side). If a is odd: x-coordinate is n.

- If b is even: y-coordinate is 0. If b is odd: y-coordinate is m.

Wait, no. Because the parity of a tells us whether the number of reflections is even or odd. For example, a=1: the ball has crossed the x boundary once, so the x coordinate is n (original x=n). a=2: crossed twice (even), so x is 0 again (since after two reflections, the direction is same as original, but the position is mirrored twice). Wait, perhaps not. Let's think of a as the number of times the ball has crossed the x dimension. Each crossing (a) in the x direction would correspond to a reflection. But how does a relate to the parity?

Alternatively, a is the number of times the ball has traveled in the x direction. For example, if vx is 1 (moving right), then each time the ball reaches x=n, it reflects, which would be equivalent to moving into a mirrored grid. The parity of a (even or odd) tells us whether the current grid is mirrored an even or odd number of times in the x direction, which determines whether the x-coordinate in the original grid is 0 or n.

For example:

- a=0: t=0, x =x.

But in our case, t is the minimal positive solution. So a is (x + vx * t)/n.

Suppose t is the minimal solution. For example, if vx=1, then x + t = a*n → a = (x + t)/n. Since t is congruent to (-x) mod n, x +t is a multiple of n. So a is integer.

So when a is even, the ball has crossed an even number of n steps in x direction. So after even reflections, the x-coordinate in the original grid is 0. If a is odd, then x-coordinate is n.

Similarly for b and y direction.

So the pocket coordinates are:

x_pocket = 0 if a is even, else n

y_pocket = 0 if b is even, else m

Thus, combining x_pocket and y_pocket gives the pocket's coordinates.

So the plan is:

For the non-zero velocity cases:

1. Compute a1 = (-x * vx) mod n

2. Compute a2 = (-y * vy) mod m

3. Check if a1 ≡ a2 mod gcd(n, m). If not, output -1.

4. Else, find the minimal positive t that satisfies t ≡ a1 mod n and t ≡ a2 mod m.

5. Compute a = (x + vx * t) / n

6. Compute b = (y + vy * t) / m

7. Check that a and b are integers (they should be, since t satisfies the congruences).

8. Determine the parity of a and b to get the pocket.

But what if there are multiple solutions for t? We need the minimal t, which corresponds to the earliest time when the ball enters a pocket.

Now, how to compute the minimal t?

The CRT can be used to find the minimal solution. So implementing CRT is necessary.

But how to compute CRT when the moduli are not coprime?

The standard approach is to solve t ≡ a1 mod n

t ≡ a2 mod m

The solution exists iff a1 ≡ a2 mod d, where d is the gcd of n and m.

Let d = gcd(n, m). Let's compute whether (a1 - a2) is divisible by d. If not, no solution exists.

Else, the solution is given by:

t = a1 + k * (n/d) * m, where k is an integer.

Wait, no. Let me recall the steps.

Let’s denote d = gcd(n, m). Let n = d * n', m = d * m', so that n' and m' are coprime.

The solution exists if a1 ≡ a2 mod d. Then, we can express t as:

t = a1 + k * n, and substitute into the second congruence:

a1 + k * n ≡ a2 mod m → k * n ≡ (a2 - a1) mod m.

Since n = d * n', and m = d * m', this becomes:

k * d * n' ≡ (a2 - a1) mod d m'

But since (a2 - a1) is divisible by d (because solution exists), we can divide both sides by d:

k * n' ≡ ((a2 - a1)/d) mod m'

Since n' and m' are coprime, we can find the inverse of n' modulo m', and solve for k.

Let’s compute this step by step.

Let’s compute delta = (a2 - a1) / d.

Then, the equation becomes k * n' ≡ delta mod m'.

Since n' and m' are coprime, the inverse of n' modulo m' exists. So k ≡ delta * inv(n') mod m'.

The minimal positive k is (delta * inv(n')) mod m'.

Once k is found, the minimal t is a1 + k * n.

Then, the minimal positive solution is the smallest t >=0 such that it satisfies both congruences.

But there's a possibility that the minimal t could be zero. But since t must be positive, we need to find the smallest t>0.

Wait, in the problem statement, the ball is not initially in a pocket. So t=0 is not a solution because that's the initial position.

So in code:

Once we find t using CRT, if t is zero, we need to find the next solution (add LCM(n, m) to t), etc. But how?

Alternatively, the CRT solution gives the minimal t that is congruent to a1 mod n and a2 mod m. But we need t to be positive. So after computing the minimal t, if it is zero, we add LCM(n, m) to it. Otherwise, it's the minimal positive solution.

But in our problem, a1 is computed as (-x*vx) mod n. So a1 is in the range [0, n-1]. Similarly for a2. So t could be zero. But the ball's initial position is not a pocket. So t must be positive.

Wait, for example, if a1 is zero, then t ≡0 mod n, which could be t=0. But that's the initial time. But in that case, the ball's initial position must have x + vx *0 =x, which is not a pocket. So the solution t=0 is invalid. We need t>0.

So how to handle this?

Once we find the minimal t that satisfies the congruences, if t is zero, we need to add the period (LCM(n, m)) to it to get the next solution.

But perhaps in our case, t cannot be zero. Let me see.

Wait, the congruence is t ≡ a1 mod n, where a1 is ( -x * vx ) mod n. So a1 can be zero. For example, if x is 0 and vx is 1, then a1 is 0. So the congruence is t ≡0 mod n. So the minimal t is 0. But the ball is at x=0, which is a pocket only if y is 0 or m. But the initial position is not a pocket, so in this case, even if t=0 is a solution, it's the initial position, which is not a pocket.

So in code, after finding the minimal t via CRT, we need to check if t is zero. If so, then the next solution is t + LCM(n, m). But if even that leads to t=0 (unlikely), then perhaps there is no solution.

So the steps are:

After computing the minimal t via CRT:

if t ==0:

   check if LCM(n, m) is positive. If yes, t += LCM(n, m)

   but even that could be zero. So perhaps the minimal positive solution is LCM(n, m).

But how to handle this.

Alternatively, after finding the minimal t, check if the computed t is zero. If so, set t to LCM(n, m). Because LCM(n, m) is a multiple of both n and m, so adding LCM(n, m) to t=0 gives t= LCM(n, m), which is the next solution.

So in code:

After finding t:

if t ==0:

   t = LCM(n, m)

But wait, if the minimal solution is t=0, but the ball is not in a pocket, then the next possible solution is t= LCM(n, m), which is the period. So we need to check whether there exists a solution t>0.

But how to confirm that?

Let's consider an example where t=0 is a solution. For example:

n=4, m=3, x=0, y=0, vx=1, vy=1. But according to the problem statement, the initial position is not a pocket. So this case is invalid. But if the initial position is a pocket, then the problem says that the ball is not initially in a pocket.

But suppose a1 is 0 mod n, and a2 is 0 mod m. Then t=0 is a solution. But since the ball's initial position is not a pocket, this solution is invalid. So there must be other solutions. Are there any?

The solution exists only if a1 and a2 are congruent modulo d. So in the case where t=0 is a solution, but the initial position is not a pocket, then the next solution is t = LCM(n, m), which is the least common multiple of n and m.

So in code, after finding the minimal t (even if it's zero), we need to compute the next solution by adding LCM(n, m) / d, where d is the GCD.

Wait, perhaps the general solution is t = t0 + k * LCM(n, m), where t0 is the minimal solution. So the next solution is t0 + LCM(n, m). So if the minimal solution is t=0, then the next solution is LCM(n, m), which is positive.

But we need to ensure that t is positive.

So after finding t via CRT, if it's zero, we add LCM(n, m) to it. But LCM(n, m) can be computed as (n * m) // GCD(n, m).

But how to compute this?

So in code:

Compute t using CRT. If t is zero, replace it with LCM(n, m). Then, check if a and b (computed from t) are such that a and b are integers, and t is positive.

Wait, but when t is zero, x + vx *0 =x, y + vy *0 =y. So (x,y) must be a pocket, but the problem states that it's not. So the code can safely proceed to compute t>0.

So the steps are:

1. For non-zero velocity components:

   a. Compute a1 = (-x * vx) mod n

   b. Compute a2 = (-y * vy) mod m

   c. Check if a1 ≡ a2 mod d (d = gcd(n, m)). If not, output -1.

   d. Else, solve for t using CRT. Find the minimal t that satisfies t ≡ a1 mod n and t ≡ a2 mod m.

   e. If t ==0, set t = LCM(n, m)

   f. Check if t is positive. If not, output -1 (but since a1 and a2 are mod n and m, which are positive, t can't be negative here.)

   g. Compute a = (x + vx * t) / n

      b = (y + vy * t) / m

   h. Check if a and b are integers (should be, since t satisfies the congruence equations)

   i. Determine the parity of a and b to find the pocket.

But wait, when t is set to LCM(n, m) (if the initial solution was zero), then:

For example, if vx=1, x=0, then x + vx * t = 0 + 1 * t = t. So if t is LCM(n, m), which is a multiple of n, then (x + vx * t)/n = LCM(n, m)/n = m / d (since LCM(n, m) = n*m /d). So a would be m/d, which is an integer. Similarly for b.

But this depends on n and m.

But in code, after calculating a and b, we need to check if they are integers. But given that t satisfies the congruences, a and b should be integers.

So assuming that the code correctly computes t, then a and b will be integers.

Once a and b are integers, then the parity (even or odd) determines the pocket.

So code steps:

Implement the CRT solution for the two congruences.

Now, implementing the CRT in Python.

But how to compute the modular inverse?

We can use the extended Euclidean algorithm.

So, the code for solving the congruence equations:

d = gcd(n, m)

if (a2 - a1) % d !=0:

   no solution → output -1

else:

   Solve for t.

The steps are:

n' = n // d

m' = m // d

We need to solve:

k ≡ ( (a2 - a1)/d ) * inv(n') mod m'

Once k is found, then t = a1 + k * n

But how to compute inv(n') mod m'?

We can use the extended Euclidean algorithm.

But in Python, the pow function can compute the inverse if the modulus is coprime. So since n' and m' are coprime, inv = pow(n', -1, m').

So code:

g, x, y = extended_gcd(n', m')

But perhaps using the built-in pow with three arguments.

So let's proceed.

Implementing the code:

def extended_gcd(a, b):

    if b ==0:

        return (a, 1, 0)

    else:

        g, x, y = extended_gcd(b, a % b)

        return (g, y, x - (a//b)*y)

But perhaps using the math.gcd function.

But let's proceed.

So, after finding that (a2 -a1) is divisible by d:

Compute delta = (a2 - a1) // d

We need to solve for k in:

k * n' ≡ delta mod m'

Since n' and m' are coprime.

So inv = pow(n', -1, m')

k = (delta * inv) % m'

t = a1 + k * n

But since t needs to be the minimal positive solution, we can compute t modulo LCM(n, m) to find the minimal solution.

But once t is computed, check if it's zero, and if so, add LCM(n, m).

But how to handle this in code.

Let's put it all together.

Now, code steps:

Compute d = gcd(n, m)

if (a2 - a1) % d !=0:

   output -1

else:

   # solve CRT

   n_prime = n //d

   m_prime = m //d

   delta = (a2 - a1) //d

   # solve k * n_prime ≡ delta mod m_prime

   inv = pow(n_prime, -1, m_prime)

   k = (delta * inv) % m_prime

   t_candidate = a1 + k *n

   # t_candidate is a solution mod LCM(n, m)

   # LCM(n,m) = (n*m) //d

   # find the minimal positive solution

   lcm = (n * m) //d

   # the minimal solution is t_candidate % lcm, but if it's zero, then the minimal solution is lcm?

   # but t_candidate could be negative.

   # So compute the minimal positive solution.

   t = t_candidate % lcm

   if t ==0:

       t = lcm

   # check if t is positive

   if t <=0:

       print(-1)

   else:

       # compute a and b

       a = (x + vx * t) // n

       b = (y + vy * t) // m

       # check parity

       x_pocket = 0 if a %2 ==0 else n

       y_pocket = 0 if b %2 ==0 else m

       print(x_pocket, y_pocket)

But wait, what if t_candidate is negative? For example, if a1 is 3, n is 4, and k is -1, then t_candidate =3 + (-1)*4= -1. So after mod lcm, which could be larger, t_candidate mod lcm is positive.

But in Python, the mod operator returns a non-negative result when the denominator is positive.

So t = t_candidate % lcm will be in [0, lcm-1]. If t is zero, then the minimal solution is lcm.

So yes, the code above should handle that.

But then, after setting t to lcm, compute a and b.

But why would t_candidate mod lcm be zero? For example, when t_candidate is a multiple of lcm.

But the minimal positive solution is lcm.

But let's see. For example:

n=2, m=3, a1=0, a2=0, d=1.

The solution is t=0, which is zero. Then, set t=6 (LCM(2,3)=6).

Then a= (x + vx *6)/2, and b= (y + vy *6)/3.

Assuming vx and vy are 1.

But how to handle when t is set to lcm.

But in code, this is handled.

Now, the code for the non-zero velocity components.

But after finding the pocket, we need to output the coordinates. However, there's another condition: the ball must reach the pocket in finite time. For example, the third sample input:

10 10 10 1 -1 0

Here, vy is 0. So the ball's x component is -1 (moving left). Since x is 10 (n=10), and moving left. The velocity in x is -1, so the ball is moving left. Since x is 10 (which is n), which is a pocket's x-coordinate. But the y coordinate is 1, which is not 0 or 10. So the ball is moving along the right edge (x=10) but y=1. So the ball is moving down (since vy is 0). Wait, no. vy is 0, so the ball's y coordinate remains 1. So the ball is moving left along x=10. But since x is 10 (n=10), which is a pocket only if y is 0 or 10. So since y is 1, the ball moves to x=0 (moving left), but since x=10, moving left with vx=-1 would take the ball to x=9, then 8, etc. Wait, no. The velocity is -1, so each step, x decreases by 1. So starting at x=10, the ball moves to 9, 8, etc. So it will reach x=0 after 10 steps. But y remains 1. So the pocket is (0, 1) which is not a valid pocket. So the ball is not in a pocket and will continue moving left past x=0 (reflecting). So in this case, the answer is -1.

But according to the code, in the case where vy is 0, the code checks if x is 0 or n. If yes, then the ball is moving along the edge, and if vy is 0, then the y coordinate must be 0 or m for it to end up in a pocket. Otherwise, it's -1.

So in this case, x is 10 (n=10), which is a valid x coordinate for a pocket. But y is 1, which is not 0 or m=10. So the ball is moving left along x=10, but y is 1. So the ball will reach x=0 (after 10 steps), but y is still 1. So (0,1) is not a pocket, so the ball will continue moving left (reflecting) and oscillate between x=0 and x=10, but y remains 1. So the code correctly returns -1.

So the code for the zero velocity components must check if the ball is moving along an edge (x=0 or x=n, or y=0 or y=m), and then see if the other coordinate is 0 or m (for the case of zero velocity component).

Now, putting all the code together.

The steps are:

- Check if either vx or vy is zero.

   - For vx=0:

      - if x is 0 or n:

         - if vy is 1: the ball moves up along x edge. So y will eventually reach m. So pocket is (x, m)

         - if vy is -1: pocket is (x, 0)

      - else:

         - output -1

   - For vy=0:

      - if y is 0 or m:

         - if vx is 1: pocket is (n, y)

         - if vx is -1: pocket is (0, y)

      - else:

         - output -1

- Else (both vx and vy are non-zero):

   - Compute a1 = (-x * vx) mod n

   - Compute a2 = (-y * vy) mod m

   - Check if (a1 -a2) is divisible by d = gcd(n, m). If not, output -1.

   - Else, solve for t using CRT.

   - Compute the minimal positive t.

   - Check if t is zero. If so, set t to LCM(n, m).

   - Compute a = (x + vx * t) //n

   - compute b = (y + vy * t) //m

   - check if a and b are integers. (But since t satisfies the congruence, they should be)

   - determine parity and output pocket.

But in code, how to compute a1 and a2.

For example, a1 is (-x * vx) mod n.

But in Python, mod can be negative. So the code should use the % operator to get the correct remainder.

Yes.

So code:

n, m, x, y, vx, vy = map(int, input().split())

if vx ==0 or vy ==0:

   # handle zero cases

   if vx ==0:

       if x !=0 and x !=n:

           print(-1)

           exit()

       # x is 0 or n. Moving in y direction.

       # determine if y will reach 0 or m.

       if vy ==1:

           # moving up. Y will reach m.

           print(f"{x} {m}")

       else:

           # moving down. Y will reach 0.

           print(f"{x} 0")

       exit()

   if vy ==0:

       if y !=0 and y !=m:

           print(-1)

           exit()

       # y is 0 or m. Moving in x direction.

       if vx ==1:

           print(f"{n} {y}")

       else:

           print(f"0 {y}")

       exit()

# handle non-zero vx and vy

# compute a1 and a2

a1 = (-x * vx) % n

a2 = (-y * vy) % m

d = math.gcd(n, m)

if (a2 - a1) %d !=0:

   print(-1)

   exit()

# solve CRT

n_prime = n //d

m_prime = m //d

delta = (a2 - a1) //d

try:

   inv = pow(n_prime, -1, m_prime)

except ValueError:

   # no inverse, but this can't happen since n_prime and m_prime are coprime

   print(-1)

   exit()

k = (delta * inv) % m_prime

t_candidate = a1 + k * n

lcm = (n * m) //d

t = t_candidate % lcm

if t ==0:

   t = lcm

# compute a and b

a = (x + vx * t) //n

b = (y + vy * t) //m

# check parity

x_pocket = 0 if a %2 ==0 else n

y_pocket = 0 if b %2 ==0 else m

print(f"{x_pocket} {y_pocket}")

But wait, in the code for the non-zero cases, after solving for t, there is a possibility that a or b could be negative. For example, if t is negative. But the code checks for t being positive, but how?

In the code, after solving for t_candidate, we take t_candidate mod lcm. So t is in [0, lcm-1]. If it's zero, then we set t to lcm. So t is always positive.

But what if a1 is 0, k is 0, and n=1. Then t_candidate is 0 + 0*1=0. mod lcm is zero. Then set t to lcm. So a = (x + vx * lcm)/n.

But since vx can be -1, is x + vx * t could be negative?

No, because the initial position is x between 0 and n. But with velocity -1 and t is large, x can decrease below zero. But that's possible. But according to the congruence, the code computes a1 = (-x * vx) mod n. For vx=-1, a1 = x mod n. For x in [0, n], x mod n is x, unless x is n, which mod n is 0.

Wait, but if x is n and vx is -1, then a1 = (-n * (-1)) mod n = n mod n = 0.

But then t ≡0 mod n. So t is a multiple of n. So x + vx *t =n + (-1)*t.

If t is multiple of n: t =k*n.

So x + vx * t =n -k*n =n(1 -k).

But if k is positive, then for k=1: 0.

k=2: -n.

So a would be (n -k*n)/n = (1 -k) → which is negative.

But this would imply that a is negative. But then the parity of a is even or odd, but the code uses a%2. But negative numbers mod 2 are 0 or 1 as well. For example, -1 %2 is 1.

But how can a be negative?

For example, if x=4, n=4, vx=-1, and t=4:

x + vx * t =4 -4 =0 → a=0/4=0 (even)

But if t=8:

x + vx * t=4 -8 =-4 → a= -4/4= -1 (odd)

So x_pocket is n=4.

But how does this make sense?

In this case, the ball starts at x=4 (n=4) and moves left with velocity -1. After t=8, the ball's position in the extended grid is x=4 -8 =-4. But according to the extended grid model, this is equivalent to a ball that has reflected multiple times. The parity of a is -1, which is odd. So x_pocket is n.

But how does the ball reach the pocket in this scenario?

Hmm, perhaps this indicates a mistake in the approach.

But according to the extended grid model, the ball's path is a straight line. The point (a*n, b*m) is in the extended grid, and the parity of a and b (even/odd) determines which pocket it is in the original table.

But a can be negative. For example, a=-1. Which parity (even/odd) would that be?

Negative even/odd is same as positive even/odd. So a=-1 is odd.

So x_pocket is n.

But in this case, the ball's path in the extended grid would reach the point (-4, ...), which is a mirrored grid. So the original pocket is at x=4 (n=4), which is a valid pocket.

But how to ensure that the ball's path in the extended grid would reach such a point?

But according to the code, even if a is negative, the parity is determined by a%2. So for a=-1, a%2 is 1, so x_pocket is n.

But is this correct?

Yes. Because a is the number of times the ball has crossed the x boundary (n or 0) in the extended grid. For example, a=-1 means crossed once to the left (reflected once), which would be equivalent to x=n in the original grid.

So the code is correct in considering the parity of a and b, regardless of their sign.

Thus, the code is correct.

Now, let's test the code against the examples.

First example:

Input:4 3 2 2 -1 1

vx=-1, vy=1 (both non-zero).

Compute a1 = (-2*(-1)) mod4 = 2 mod4 = 2.

a2= (-2*1) mod3 → (-2 mod3) → 1.

d= gcd(4,3)=1.

Check (a2 -a1) mod1 → (1-2) =-1 mod1=0. So proceed.

n_prime=4/1=4.

m_prime=3/1=3.

delta= (1-2)/1 =-1.

inv= pow(4, -1, 3). Since 4 ≡1 mod3. Inverse of 1 mod3 is 1.

k= (-1 *1) mod3 → 2 mod3=2.

t_candidate=2 + 2*4=10.

t=10 mod (4*3)=12 →10.

Since 10>0.

a= (2 + (-1)*10)/4 → (2-10)/4= (-8)/4= -2. a%2=0.

x_pocket=0.

b= (2 +1*10)/3 →12/3=4. b%2=0.

y_pocket=0.

Output 0 0. Which matches the sample.

Second example:

Input:4 4 2 0 1 1.

vx=1, vy=1.

Compute a1 = (-2 *1) mod4 →-2 mod4=2.

a2= (-0 *1) mod4 →0 mod4=0.

d= gcd(4,4)=4.

Check (0-2) mod4 →-2 mod4=2 mod4=2. Not divisible by 4. So no solution. Output -1. Which matches the sample.

Third example:

Input:10 10 10 1 -1 0.

vx=-1, vy=0.

So handle vy=0.

Check if y is 0 or 10. y=1: no. So output -1. Which matches the sample.

Another test case:

Input:10 10 0 5 1 0.

vy=0. y=5 is not 0 or 10. So output -1.

Another test case:

Input:10 10 0 5 0 1. x is 0 (valid). vy=1. Output (0, 10).

Another test case where the CRT solution is zero:

Suppose n=2, m=2, x=0, y=0, vx=1, vy=1.

a1 = (-0 *1) mod2=0.

a2= (-0 *1) mod2=0.

d=2.

a1 -a2=0 mod2 →0. So proceed.

n_prime=1, m_prime=1.

delta=0.

inv=pow(1, -1, 1) →0 (since inverse of 1 mod1 is 0).

k=0 *0 mod1=0.

t_candidate=0 +0 *2=0.

t is zero → set t= LCM(2, 2)=2.

a= (0 +1*2)/2=2/2=1 → odd. x_pocket=2.

b= (0+1*2)/2=1 → odd. y_pocket=2.

Output 2 2, which is (n, m), which is a pocket.

But the initial position is (0,0), which is a pocket. But the problem states that the initial position is not a pocket. So this case is invalid.

Thus, the code handles this correctly by moving to t=2, which is a valid solution.

Thus, the code should work.
</think>

```python
import math

n, m, x, y, vx, vy = map(int, input().split())

if vx == 0 or vy == 0:
    if vx == 0:
        if x != 0 and x != n:
            print(-1)
        else:
            if vy == 1:
                print(f"{x} {m}")
            else:
                print(f"{x} 0")
    else:
        if y != 0 and y != m:
            print(-1)
        else:
            if vx == 1:
                print(f"{n} {y}")
            else:
                print(f"0 {y}")
    exit()

a1 = (-x * vx) % n
a2 = (-y * vy) % m
d = math.gcd(n, m)

if (a2 - a1) % d != 0:
    print(-1)
    exit()

n_prime = n // d
m_prime = m // d
delta = (a2 - a1) // d

try:
    inv = pow(n_prime, -1, m_prime)
except ValueError:
    print(-1)
    exit()

k = (delta * inv) % m_prime
t_candidate = a1 + k * n
lcm = (n * m) // d
t = t_candidate % lcm

if t == 0:
    t = lcm

a = (x + vx * t) // n
b = (y + vy * t) // m

x_pocket = 0 if a % 2 == 0 else n
y_pocket = 0 if b % 2 == 0 else m

print(f"{x_pocket} {y_pocket}")
```