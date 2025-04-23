<think>
Okay, so I need to solve this problem where I have to count the number of interesting triangular fences. Let me read the problem again carefully.

The problem says that a fence is interesting if two conditions are met: first, the number of enclosed cows (strictly inside the triangle) is odd, and second, the area of the triangle is an integer. We have to count all such possible triangles formed by three distinct fence posts, given that all coordinates are even, and no three are colinear.

Hmm. So the key here is to find for each triplet of points whether these two conditions hold. But directly checking all possible triplets would be O(n^3) which is way too slow for n up to 6000. 6000 choose 3 is about 6000*6000*6000/6 = 36e9, which is impossible. So we need a smarter approach.

First, let's think about the two conditions:

1. The area must be an integer.
2. The number of cows strictly inside the triangle must be odd.

Wait, but since all coordinates of the fence posts are even, maybe there's a way to compute these conditions based on some properties of the points.

Let me recall some computational geometry formulas and theorems that might help here.

First, the area of a triangle with vertices (x1,y1), (x2,y2), (x3,y3) is given by (1/2)| (x2 -x1)(y3 - y1) - (y2 - y1)(x3 -x1) |. Since all coordinates are even, the differences between them are even, so when we compute (x2-x1)(y3-y1) and (y2-y1)(x3-x1), both terms are even*even = multiples of 4. So the difference between those two terms is a multiple of 4. Then the absolute value of that difference divided by 2 would be a multiple of 2. So the area would be (1/2)* (some multiple of 4)/2 → that's a multiple of 1. Wait, maybe not. Let's compute.

Let me take the example from the first sample input: (0,0), (2,0), (0,4). The area is (2*4 - 0*0)/2 = 8/2 =4. So that's an integer. So in this case, the area is indeed an integer.

But wait, let's see the general case. Let's compute the area formula again. The determinant is (x2 - x1)(y3 - y1) - (y2 - y1)(x3 - x1). Since all x's and y's are even, their differences are even. Let me denote dx = x2 - x1, which is even. Similarly, dy3 = y3 - y1 is even. So dx*dy3 is 4*k. Similarly for the other term. So the determinant is 4k -4k' = 4(k -k'), so the determinant is a multiple of 4. Then the area is (1/2)* |determinant| → (1/2) * (4m) = 2m. So the area is even? Wait, but the first example's area is 4, which is even. But in that case, yes. But how does this fit with the condition for the area being an integer? Oh, wait, the area is 2m, which is an integer. So all possible triangles formed by these points have area that is even. Wait, but that can't be right. Wait, let me recheck. The determinant is (x2 - x1)(y3 - y1) - (y2 - y1)(x3 - x1). Since all coordinates are even, each difference is even. So each product is even * even = 4* something. So the determinant is 4*(something - something else), which makes it a multiple of 4. Then the area is (determinant)/2, so (4k)/2 = 2k, which is indeed an integer. So all triangles formed by three such points will have an integer area. So the area condition is automatically satisfied. Wait, that's a big insight. So the problem's first condition (area is integer) is always true. Because all coordinates are even, so the area is (even*even - even*even)/2 → 4k/2 = 2k → integer. So for all possible triplets, the area is integer. So the only condition we need to check is whether the number of enclosed cows is odd.

So the problem reduces to counting the number of triplets of points that form a triangle with an odd number of cows strictly inside it.

Now, the key is to find the number of lattice points (cows) strictly inside the triangle. But how can we compute that efficiently?

Wait, there's a theorem called Pick's Theorem. Let me recall it. Pick's theorem states that for a simple polygon whose vertices are lattice points, the area A is equal to I + B/2 - 1, where I is the number of interior lattice points and B is the number of boundary lattice points. But here, we're interested in I (the number of cows strictly inside the triangle). So for a triangle, the formula would be A = I + B/2 - 1. Rearranged, I = A - B/2 + 1.

But since we need I to be odd, substituting the formula, we get that (A - B/2 + 1) must be odd. Since A is the area of the triangle (integer), and B is the number of lattice points on the boundary.

Wait, but in our case, the triangle's vertices are at even coordinates. The edges between these points might have certain properties. Let me think.

But let's substitute the formula. We need I ≡ 1 mod 2. So:

I ≡ 1 mod 2 → (A - (B/2) + 1) ≡ 1 mod 2 → A - B/2 ≡ 0 mod 2.

But A is the area, which we know is 2k (since all coordinates are even). Wait, no. Wait earlier analysis said the area is 2k, but wait, the area formula for three points (x1,y1), (x2,y2), (x3,y3) is 1/2 | (x2 -x1)(y3 - y1) - (y2 - y1)(x3 -x1) |. The determinant is (x2-x1)(y3-y1) - (y2-y1)(x3-x1). Since all coordinates are even, each term (x2-x1) is even, (y3-y1) is even, so their product is 4k. So the determinant is 4k -4k' = 4(k -k'), which is divisible by 4. So the determinant is a multiple of 4. Then the area is (4k)/2 = 2k. So A is even.

So substituting A as even into the equation:

even - (B/2) ≡ 0 mod 2.

So even minus (B/2) is even. Which implies that B/2 must be even minus even → even? Wait, perhaps better to re-express:

A is even. So A ≡ 0 mod 2.

Then the equation becomes:

0 - (B/2 mod 2) ≡ 0 mod 2 → - (B/2 mod 2) ≡ 0 mod 2 → B/2 mod 2 must be 0.

Which implies B/2 is even → B must be divisible by 4.

Wait, because B/2 must be even → B/2 = 2m → B=4m.

So, the condition for I to be odd is that B (the number of lattice points on the boundary of the triangle) is divisible by 4.

So the problem reduces to counting the number of triplets of points (triangles) where the number of lattice points on the boundary is divisible by 4.

So now the task is: for each triplet of points, compute the number of lattice points on their triangle's boundary, and check if that number is divisible by 4. If yes, then it's an interesting fence.

So the next question is: how to compute B (the number of lattice points on the boundary of the triangle formed by three points) for each triplet, and determine whether B mod 4 is 0.

But computing B for each triplet directly is O(n^3), which is impossible for n=6000. So we need a way to compute B mod 4 for a triangle given three points, and find a way to compute this efficiently.

The number of lattice points on a line segment between two points (x1, y1) and (x2, y2) is given by the greatest common divisor (gcd) of the absolute differences in x and y coordinates, plus 1. The formula is B = gcd(dx, dy) + 1, where dx = |x2 - x1|, dy = |y2 - y1|. However, for the entire triangle, the boundary points are the sum of the points on each edge, minus the three vertices (since each vertex is counted twice, once per adjacent edge). So for a triangle with edges AB, BC, CA, the total B is (gcd(AB) + 1) + (gcd(BC) +1) + (gcd(CA) +1) - 3 → sum of the gcds of each edge. Because each vertex is counted once per edge, so sum edges' (gcd +1) gives sum(gcd) +3. Then subtract 3 for the three vertices counted once each. So total B is sum(gcd(AB), gcd(BC), gcd(CA)).

So B = (gcd(AB) + gcd(BC) + gcd(CA)).

Wait, no: let me recheck.

The number of lattice points on edge AB is gcd(dx, dy) + 1, where dx and dy are the differences between A and B. Similarly for BC and CA. The total for all three edges would be (gcd(AB) +1) + (gcd(BC)+1) + (gcd(CA)+1). But this counts each vertex (A, B, C) exactly once. Wait, no. Wait, edge AB includes points A and B. Edge BC includes B and C. Edge CA includes C and A. So when adding the three edges' counts, the points A, B, C are each counted twice. So the total number of points on the boundary is (sum (gcd(edge) +1 )) - 3*2 + 3 → because each vertex is counted twice, so subtract 2*3 (the three vertices each counted once extra), then add 3 to account for the original count. Wait, maybe this is getting too complicated. Let me think of it differently. The total number of boundary points is (gcd(AB) +1) + (gcd(BC)+1) + (gcd(CA)+1) - 3*2, because each vertex is counted twice (once for each adjacent edge). For example, point A is included in edge AB and edge CA. So when we sum all three edges, A is counted twice. Similarly for B and C. So to get the total, we subtract 3 (since each vertex is counted twice, and we need to subtract 1 per vertex to get the correct count). So total B is (sum(gcd(edge)+1)) - 3*1*3? Wait, perhaps it's easier to subtract the overlapping counts.

Alternatively, the formula for the number of boundary points B of a triangle is B = gcd(AB) + gcd(BC) + gcd(CA) + 1 - 3. Wait, no. Let's take an example.

Take the first sample input: points (0,0), (2,0), (0,4). The edges are AB (0,0)-(2,0), BC (2,0)-(0,4), CA (0,4)-(0,0).

For AB: dx=2, dy=0 → gcd(2,0)=2. So number of points is 2 +1=3 (points (0,0), (1,0), (2,0)).

For BC: dx= -2, dy=4. Absolute values 2 and 4 → gcd 2. So 2+1=3 points (2,0), (1,2), (0,4).

For CA: dx=0, dy=-4. Absolute values 0 and 4 → gcd 4. So 4+1=5 points. Wait, but CA is a vertical line from (0,4) down to (0,0). The points are (0,4), (0,3), (0,2), (0,1), (0,0). So 5 points.

Summing the three edges gives 3+3+5=11. But each vertex is counted twice. So subtract 3 (for the three vertices counted twice, so 3*1 extra counts). So total B is 11-3=8. But according to the sample input, the first example has 1 cow inside. Let's check with Pick's theorem. The area is 4. So I = A - B/2 + 1 → 4 - (8/2) +1 =4-4+1=1. Which matches. So B is 8. So for this example, B mod4 is 0, which satisfies the condition. So the formula for B is sum(gcd(AB), gcd(BC), gcd(CA)) ?

Wait in this example, sum(gcd(AB), gcd(BC), gcd(CA)) is 2 +2 +4=8. Which matches the B value. So the formula is B = sum of the gcds of each edge's dx and dy. So for the triangle, B is equal to the sum of the gcds of each of the three edges.

So yes, B = gcd(AB) + gcd(BC) + gcd(CA). Because in the example, that's 2+2+4=8, which matches.

Therefore, the problem reduces to checking whether the sum of the gcds of the three edges of the triangle is divisible by 4.

So now, the problem becomes: for each triplet of points A, B, C, compute the sum of gcd(dx_AB, dy_AB) + gcd(dx_BC, dy_BC) + gcd(dx_CA, dy_CA), and check if this sum is divisible by 4.

But for n=6000, we can't compute this for all triplets. So we need a way to compute the count efficiently.

But how?

Let me think about the properties of the gcd. Since the coordinates are even, dx and dy for each pair are even. So dx=2a, dy=2b. Then gcd(dx, dy) = 2*gcd(a,b). Because the gcd of two even numbers is twice the gcd of their halves. So for each pair of points, the gcd of their differences is even.

So for each pair (A,B), the gcd is 2*gcd((x2 -x1)/2, (y2 - y1)/2). Let me denote that as 2*g, where g is an integer.

So for any edge, the gcd is even. Then each term in B is even, so the sum of three even terms is even. But we need this sum mod4 to be 0.

So the sum S = sum of three even numbers. Each term is even, so S is even. But we need S mod4 ==0.

Each term in the sum is 2g, so S = 2g1 + 2g2 + 2g3 = 2(g1 + g2 + g3). So S mod4 is 2*(g1 +g2 +g3 mod 2). Because 2*(a) mod4 is 0 if a is even, and 2 if a is odd.

So S mod4 is 0 if (g1 +g2 +g3) mod2 is 0. So the sum S is divisible by4 if and only if (g1 +g2 +g3) is even.

So the problem reduces to, for each triplet of points (A,B,C), compute the sum of g1, g2, g3 (where each g is the gcd of (x_i -x_j)/2, (y_i - y_j)/2 for each pair in the triplet), and check if the sum is even.

So now, the key is to precompute for every pair of points the value of g = gcd((x_i -x_j)/2, (y_i -y_j)/2), and then for each triplet, compute g_AB + g_BC + g_CA mod2. If this sum is even, then the triplet is counted.

But how to compute this efficiently?

Let me note that g_AB is the gcd of the differences divided by 2. So for a pair (A,B), g_AB = gcd( (x_B -x_A)/2, (y_B -y_A)/2 ). Let's call this the "reduced gcd" for the pair.

So for each pair of points (A,B), compute the reduced gcd g_AB. Then for a triplet (A,B,C), the sum is g_AB + g_BC + g_CA. We need this sum mod2 to be 0.

But how to model this? Let's see.

The sum g_AB + g_BC + g_CA mod2.

But for three points A,B,C, the sum is the sum of the reduced gcds of each pair in the triplet. However, each pair is considered once. So the sum is the sum of g_AB, g_AC, g_BC (since the edges are AB, BC, CA, which are pairs AB, BC, CA. Wait, in the sum for the triplet, the edges are AB, BC, CA. So the sum is g_AB + g_BC + g_CA. But for each triplet, it's three pairs.

But for three points, AB, BC, CA are the three edges. So for each triplet, the three pairs are AB, BC, CA.

So for each triplet (A,B,C), the sum is the sum of the reduced gcds of AB, BC, and CA.

But how can we compute this sum mod2 efficiently?

Let me think about parity. Each g is an integer, and the sum of three integers mod2 is 1 if the count of odds in the three is odd. So the sum is even if the three gs have even parity in their sum.

So the problem is now: count the number of triplets (A,B,C) where the sum of the three reduced gcds of AB, BC, and CA is even.

So the crux is to find, for each triplet, the sum mod2 of the three reduced gcds.

But how?

This seems challenging. Let's see if there's a pattern here.

Let's note that for a triplet (A,B,C), the three pairs are AB, BC, CA. Let's denote their reduced gcds as g_AB, g_BC, g_CA.

But the sum g_AB + g_BC + g_CA mod2 is equivalent to (g_AB mod2) + (g_BC mod2) + (g_CA mod2) mod2.

So each g can be either even or odd, and the sum mod2 is the parity of the sum of the three parities.

So the problem reduces to counting the number of triplets where the number of pairs (AB, BC, CA) with odd reduced gcd is even (even count of odds).

So for each triplet, if the sum of the parities of the three edges is even, then it's counted.

So how can we model this?

We can precompute for each pair (A,B) the parity of their reduced gcd (0 if even, 1 if odd). Let's call this parity_p(A,B). Then for a triplet (A,B,C), the sum is parity_p(A,B) + parity_p(B,C) + parity_p(C,A). We need this sum to be even.

But how to count the number of triplets where this sum is even.

But for three variables, the sum is even if there are 0 or 2 odd terms. So for each triplet, the sum is even if either all three parities are even, or exactly two are odd and one is even.

So the problem now is to count the number of triplets where the sum of the parities is even.

But how?

The straightforward approach would be O(n^3), which is impossible. So we need a smarter way.

Alternative approach: For each pair (A,B), store the parity of their reduced gcd. Then, for each triplet (A,B,C), the sum is parity_p(A,B) + parity_p(B,C) + parity_p(C,A).

But perhaps this sum can be expressed in terms of the parities of all pairs in the triplet.

Wait, but the sum includes three pairs: AB, BC, CA.

Let me think: Let's consider that for a triplet (A,B,C), the three pairs are AB, BC, and CA. Let me denote the parities as a=parity_p(AB), b=parity_p(BC), c=parity_p(CA). The sum a + b + c mod2 must be 0.

So we need a + b + c ≡0 mod2.

But how can we precompute this for all triplets?

Hmm, perhaps we can model this as a graph where nodes are points and edges have a parity (0 or 1). Then for each triplet (A,B,C), we need a (the parity of AB) + b (parity of BC) + c (parity of CA) ≡0 mod2. But CA is the same as AC. So parity_p(CA) is the same as parity_p(AC), which is the same as parity_p(CA) since gcd is commutative.

Wait, parity_p(A,B) is the same as parity_p(B,A), since the gcd is the same regardless of order. So the parity for AB is the same as BA.

So for triplet (A,B,C), the three edges are AB, BC, and CA. So the sum is parity_p(AB) + parity_p(BC) + parity_p(CA).

But how can we model this in terms of the edges between the three points?

Let me see if there's a way to represent this as a XOR operation. Since the sum mod2 is equivalent to XOR.

But for three variables, sum mod2 is the same as XOR for odd counts. So a + b + c mod2 is (a XOR b XOR c) XOR (a AND b AND c). Hmm, maybe that's complicating things.

Alternatively, perhaps the sum a + b + c mod2 is equal to (a XOR b XOR c) if exactly one or three of them are 1, and 0 otherwise. Wait, no. For example, if a=1, b=1, c=1: sum mod2 is 1+1+1 =3 mod2=1. XOR of 1,1,1 is 1. So same. If two are 1: sum is 2 mod2=0. XOR of three bits with two 1s would be 0. So yes, the sum mod2 is equal to the XOR of the three bits. So (a + b + c) mod2 = a XOR b XOR c.

Wait, let me check:

If a=0, b=0, c=0 → sum 0 mod2=0. XOR is 0^0^0=0.

a=1,0,0: sum 1 mod2=1. XOR 1^0^0=1.

a=1,1,0: sum 2 mod2=0. XOR 1^1^0=0.

a=1,1,1: sum 3 mod2=1. XOR 1^1^1=1.

So yes, the sum mod2 is the same as the XOR of the three bits.

So the condition is that the XOR of a, b, c is 0.

So the problem now is to count the number of triplets (A,B,C) where the XOR of the parities of AB, BC, and CA is 0.

But how to compute this efficiently.

This seems tricky. Let's think of the parities as edges in a graph. Each edge has a parity (0 or 1). For a triplet (A,B,C), the sum is a XOR b XOR c, where a is parity(AB), b is parity(BC), c is parity(CA). We need this sum to be 0. So a XOR b XOR c =0 → which implies a XOR b = c.

But how can we model this? For each triplet, c is the parity of CA. But CA is the same as AC, which is the same as the edge from A to C. So for a given triplet (A,B,C), the three edges AB, BC, and CA must satisfy a XOR b = c.

But how to find triplets where this condition holds.

Alternatively, for each pair of edges AB and BC, their XOR gives the required parity of CA. So for a given AB and BC with parities a and b, the parity of CA must be a XOR b. So for each pair of edges AB and BC (where B is the common point), the required parity of CA is a XOR b. If the actual parity of CA is equal to this, then the triplet (A,B,C) is counted.

But how to count this efficiently.

But the problem is that for a triplet (A,B,C), the order matters. But perhaps we can model this as a graph where for each node B, we look at all edges coming into B and edges going out of B (but the graph is undirected). Wait, but in this model, edges are undirected. So each edge between B and C is the same as between C and B. So for a triplet (A,B,C), the edges AB, BC, CA are all present in the graph. But how can we find all triplets where the sum of their parities is even.

Alternative approach: Precompute for all pairs (A,B) their parity. Then for each triplet (A,B,C), compute the parity of AB, BC, and CA. Check if their XOR is 0.

But for n=6000, this is O(n^3) operations, which is way too slow. So we need a smarter approach.

Let me think of the parity of each edge as a property. Let's imagine that each edge has a color 0 or 1. Then, for each triplet (A,B,C), the three edges AB, BC, CA form a triangle. We need the XOR of the three colors to be 0.

So the problem is to count the number of triangles in a graph where the edges are colored 0 or 1, and the triangle's edges' XOR is 0.

But even so, counting this for all possible triplets is O(n^3), which is not feasible for n=6e3.

But perhaps there's a mathematical way to compute this.

Let's denote the total number of triplets as C(n,3). The answer is the number of triplets where the sum of the three parities is even. Let's denote E as the number of edges with parity 0, and O as the number of edges with parity 1. But how does this help?

Alternatively, for each triplet, the sum of the parities can be even in two cases:

1. All three edges have parity 0 (0+0+0=0 mod2).
2. Exactly two edges have parity 1, and one has parity 0.

But how to count these cases?

Alternatively, the number of triplets with even sum is equal to (number of triplets with sum even) = (number of triplets with 0 or 2 edges of parity 1).

But again, how to compute this.

Alternatively, let's think about all possible triplets and model the parity of each pair.

Let me consider that for each node, we can track the number of edges to other nodes with parity 0 or 1.

But I'm not sure. Let's think differently.

Each triplet can be considered as three edges forming a triangle. The sum of their parities must be even.

Let me model this as:

For any three nodes A, B, C, the sum of the parities of edges AB, BC, and CA must be even.

Which is equivalent to parity(AB) XOR parity(BC) XOR parity(CA) = 0.

But how can this be transformed into something computable?

Alternatively, note that parity(AB) is equal to the parity of the reduced gcd for AB. The reduced gcd is the gcd of (dx/2, dy/2) for AB's coordinates.

Hmm. So perhaps the parity of the reduced gcd is determined by the parity of the individual components (dx/2 mod2, dy/2 mod2).

Let me think: for a pair of points (A,B), where A has coordinates (x1, y1) and B has (x2, y2). Then dx = x2 -x1, which is even. Let dx/2 = a. Similarly, dy/2 = b.

So the reduced gcd is gcd(a, b). What's the parity of gcd(a,b)?

The parity is 1 if and only if gcd(a,b) is odd, else 0.

So gcd(a,b) is odd if and only if a and b are both not divisible by 2. Because if a and b are both even, then their gcd is even. If one is even and the other is odd, then their gcd is 1. Wait no. Let's see.

Wait, the gcd of two numbers is the greatest common divisor. For example, gcd(3,5) is 1. gcd(3,6) is 3. So the parity of the gcd depends on whether the gcd is even or odd.

So for a and b (the dx/2 and dy/2), the parity of their gcd is 1 if their gcd is odd, else 0.

So, the parity of the edge AB is 1 if and only if the reduced gcd (gcd(a,b)) is odd. So when is gcd(a,b) odd?

This happens when a and b are coprime and both odd. Or when their gcd has an odd greatest common divisor.

Wait, no. The gcd(a,b) is odd if and only if a and b are not both even. Wait, no. For example, a=4 and b=6: their gcd is 2, which is even. So gcd(a,b) is even. But a and b are even. If a is even and b is odd, then their gcd is 1 (if a and b are coprime), which is odd. For example, a=2 and b=3: gcd is 1. So parity is 1.

So the parity of the edge AB is 1 if and only if the reduced dx and reduced dy (dx/2 and dy/2) are such that their gcd is odd.

But how to compute this parity for a pair (A,B)?

Let me think: the parity is 1 iff the gcd(a,b) is odd. So the parity is 1 if and only if a and b have no common factors of 2. That is, after dividing out all factors of 2 from a and b, the resulting numbers are coprime. Or, perhaps, the parity is 1 if and only if the sum of the exponents of 2 in a and b is zero. But I'm not sure.

Alternatively, we can model the parity based on the parity of a and b. Let me think:

Case 1: a is even, b is even. Then, both a and b are even. So their gcd is at least 2. So the parity is 0.

Case 2: a is even, b is odd. Then, the gcd of a and b is the same as the gcd of a/2 and b. Since b is odd, the gcd can be 1 (if a/2 and b are coprime). So the parity could be 1.

Case 3: a is odd, b is even. Similar to case 2.

Case4: a is odd, b is odd. Then, their gcd can be odd (like 3 and 5 have gcd 1, which is odd). So the parity is 1.

So the parity is 1 in cases 2,3,4. Only when both a and b are even does the parity become 0.

Wait, no. Because if a and b are even, their gcd is even. So parity is 0. Otherwise, if at least one is odd, then the gcd could be odd.

Wait, no. For example, a=4 (even) and b=6 (even). Their gcd is 2, even. So parity 0.

If a=4 (even) and b=3 (odd). Then gcd(4,3)=1 (odd), parity 1.

If a=5 (odd) and b=3 (odd). gcd is 1, parity 1.

If a=6 (even) and b=9 (odd). gcd(6,9) is 3, which is odd. So parity 1.

Wait, but 6 and 9 have gcd 3, which is odd. So the parity is 1.

So the parity is 1 in all cases where at least one of a or b is odd. Wait, no. Let's see:

No. For example, a=6 (even), b=3 (odd). Their gcd is 3, which is odd. So parity 1.

Another example: a=2 (even), b=4 (even). gcd is 2, even. Parity 0.

Another example: a=2 (even), b=3 (odd). gcd is 1, parity 1.

So, the parity of the edge AB is 1 if and only if the reduced dx (dx/2) and reduced dy (dy/2) are not both even.

Wait, dx/2 and dy/2 are the coordinates after dividing by 2, since dx and dy are even. So, for the pair AB, a = (x2 -x1)/2, b = (y2 - y1)/2. Both a and b are integers.

So, the parity is 1 iff a and b are not both even.

Because if a and b are both even, then their gcd is even (since both are even). So the parity is 0. Otherwise, if at least one is odd, the gcd is 1 (if they are coprime) or some odd number. Wait, but even if they are not coprime, if at least one is odd, the gcd could be odd.

For example, a=3 (odd), b=9 (odd). Their gcd is 3 (odd). So parity is 1.

So the parity of the edge AB is 1 if and only if (a mod 2) or (b mod 2) is 1. Because if either a or b is odd, then their gcd could be odd. Otherwise, when both are even, the gcd is even.

So, the parity is 1 exactly when (a mod2) + (b mod2) is at least 1. So when a or b is odd.

Wait, but this is not the case. Consider a=2 and b=3. a is even, b is odd. Their gcd is 1, which is odd. So parity is 1. Which fits.

If a=4 (even), b=6 (even). gcd is 2, even. Parity 0.

If a=3 (odd), b=5 (odd). gcd is 1. Parity 1.

If a=3 (odd), b=6 (even). gcd is 3 (odd). Parity 1.

Wait, but 3 and 6 have gcd 3, which is odd. So parity is 1.

So the parity is 1 whenever at least one of a or b is odd. Because if either is odd, then their gcd is odd.

Wait, is that correct?

Suppose a is even and b is even: then their gcd is even. Parity 0.

If a is even and b is odd: gcd can be 1 (if they are coprime). For example, a=2, b=3 → gcd 1. Or a=4, b=3 → gcd 1. Or a=6, b=3 → gcd 3 (odd). So yes, the parity is 1.

If a is odd and b is even: same as above.

If a is odd and b is odd: gcd can be 1 (coprime) or other odds. So parity is 1.

So the parity of the edge AB is 1 if and only if a is odd or b is odd. Which is equivalent to (a mod2) + (b mod2) >= 1. So, the parity can be computed as (a mod2) | (b mod2). Because if either is 1, the result is 1.

So, for the pair AB, the parity is 1 if and only if (a mod2) or (b mod2) is 1. Because a and b are (dx/2, dy/2), which are integers.

So, the parity for edge AB is (a mod2) | (b mod2). Which is equivalent to ((dx/2) mod2) | ((dy/2) mod2).

But dx is x2 -x1. Since x1 and x2 are even, dx is even, so dx/2 is an integer. Similarly for dy.

So, for each pair of points (A,B), compute dx = xB -xA, dy = yB - yA. Then a = dx/2, b = dy/2. The parity is (a mod2) | (b mod2). So if either a or b is odd, the parity is 1; otherwise 0.

This is a crucial insight. This means that the parity of the edge AB is determined by whether the reduced coordinates (dx/2, dy/2) are both even or not. If either is odd, parity is 1; else 0.

So now, instead of computing the gcd for each pair, which is time-consuming, we can compute the parity based on the mod2 of dx/2 and dy/2. This is O(1) for each pair, which is manageable for n=6000.

So the plan is:

1. Precompute for each pair (A,B) the parity_p(A,B) as ( ( ( (xB -xA)/2 ) mod2 ) | ( ( (yB - yA)/2 ) mod2 ) ). This is either 0 or 1.

But since xB and xA are even, xB - xA is even. So (xB - xA)/2 is an integer. Same for y.

So, for each pair (A,B), compute (dx/2) mod2 and (dy/2) mod2. If either is 1, parity_p is 1. Else 0.

Then, for each triplet (A,B,C), we need the sum of parity_p(AB), parity_p(BC), parity_p(CA) to be even.

But how to count this efficiently.

The key is that the parity_p(AB) can be determined in O(1) for each pair. So precomputing a parity matrix for all pairs, then for each triplet, compute the sum of the three parities mod2.

But n=6000, the number of triplets is 6000*5999*5998/(6) ~ 3.6e10, which is way too big.

So we need a way to compute this count without enumerating all triplets.

Alternative approach: For any three distinct points A, B, C, the sum of the three parities is even. Let's find a mathematical formula for this.

Let me think about the sum over all possible triplets of (parity_AB + parity_BC + parity_CA) mod2. We need to count the number of triplets where this sum is 0.

But how.

Let me denote the number of triplets where the sum is even as the answer.

Let me think about the total number of triplets, which is C(n,3). The answer is the number of triplets where the sum is even.

Let me denote that each edge has a parity 0 or 1.

The sum for a triplet is parity_AB + parity_BC + parity_CA mod2.

But this is equivalent to parity_AB XOR parity_BC XOR parity_CA.

Let me consider all possible triplets. Each triplet contributes 1 to the answer if the XOR is 0.

Now, the key insight: for any three distinct points A, B, C, the sum parity_AB + parity_BC + parity_CA is equal to (parity_AB + parity_BC) mod2 + parity_CA mod2. But I'm not sure.

Alternatively, think of the parity_AB as a variable for each pair. Then, the sum for a triplet is parity_AB + parity_BC + parity_CA.

But parity_AB is the same as parity_BA, since it's based on the dx and dy between A and B, which is the same as B and A. So the parity is symmetric.

So, the sum for the triplet is parity_AB + parity_BC + parity_CA.

But parity_CA is parity_AC, which is the same as parity_CA.

So, the sum is parity_AB + parity_BC + parity_AC.

So, the sum is parity_AB + parity_BC + parity_AC mod2.

But how to model this.

Another idea: For each point B, consider all pairs (A, C) where B is not equal to A or C. Then, for each such pair (A,C), the sum for the triplet (A,B,C) is parity_AB + parity_BC + parity_AC.

But how to relate this.

Alternatively, for a fixed point B, consider all pairs (A,C) such that A and C are distinct from B. Then, for each such pair (A,C), the sum is parity_AB + parity_BC + parity_AC. We need this sum to be even.

But this approach may not directly help.

Alternative approach inspired by inclusion-exclusion:

The total number of triplets is C(n,3). Let me compute the number of triplets where the sum is even as follows:

The sum is even when the number of 1's in the three parities is even. Let's consider all possible cases:

- All three parities are 0 → sum is 0.
- Exactly two parities are 1 → sum is 0 mod2.

So the total count is the number of triplets with 0 or 2 edges of parity 1.

But how to compute this.

Let me denote the total number of pairs with parity 1 as O, and parity 0 as E. Then, the total number of pairs is O + E = n*(n-1)/2.

But how to express the number of triplets with 0 or 2 edges of parity 1.

The number of triplets with 0 edges of parity 1 is the number of triplets where all three pairs have parity 0. Let's call this T0.

The number of triplets with exactly two edges of parity 1 is the number of triplets where exactly two pairs have parity 1, and the third has parity 0. Let's call this T2.

The answer is T0 + T2.

But how to compute T0 and T2.

T0 is the number of triplets where AB, BC, and CA all have parity 0.

T2 is the number of triplets where two edges are 1 and one is 0.

But how to compute these values.

But for n=6e3, this approach would require O(n^3) steps, which is not feasible.

Alternative idea: For each triplet, the sum of parities can be expressed as (parity_AB + parity_AC) + parity_BC + parity_AC. Wait, perhaps not. Maybe there's a way to express this in terms of individual points' properties.

Wait, parity_AB is the parity of the pair (A,B). So for a triplet (A,B,C), there are three pairs. But each pair is independent of the others, except that they share points.

Alternative approach: Represent the parity of each pair as a binary variable. Then, the sum for the triplet is the sum of three variables. The problem is to count the number of triplets where the sum is even.

But how to compute this.

Another idea: The sum of the three variables mod2 is the same as the product of the three variables mod2. Wait, no. For example, 1+1+1 mod2 is 1. Product mod2 is 1. But 0+0+0 mod2 is 0. Product is 0. So it's not directly the same.

But perhaps we can model this using linear algebra.

Alternatively, let's think of the sum S = a + b + c mod2. Then, the total number of triplets with S=0 is equal to (number of triplets) - (number of triplets with S=1).

But this doesn't help unless we can find a way to compute the difference.

But how to compute the number of triplets with S=1.

Another Idea: The total number of triplets where S is even can be computed as follows:

For each triplet, the sum S is even. Let's think about each triplet contributing a term (1 + (-1)^S)/2. The sum over all triplets of this term is the desired count. But integrating this into a computational approach is unclear.

But perhaps using generating functions.

Alternatively, let's note that for a given triplet, the sum S is the sum of three binary variables. So the sum is even if even number of variables are 1.

The number of such triplets can be computed as (sum over all triplets of (1 + (-1)^{a + b + c}) ) / 2, where a, b, c are the parities of the three edges.

But expanding this, we get (C(n,3) + sum_{triplets} (-1)^{a + b + c}) ) / 2.

So the answer is [ C(n,3) + T ] / 2, where T is the sum over all triplets of (-1)^{a + b + c}.

But how to compute T.

But T is the sum over all triplets of (-1)^(a_ab + a_bc + a_ca), where a_ab is the parity of edge AB.

But how to compute T efficiently.

If we can compute T, then the answer is (C(n,3) + T)/2.

So the problem reduces to computing T.

But how.

Let's expand T as sum_{A,B,C} (-1)^{a_AB + a_BC + a_CA}.

But summing over all ordered triplets of distinct points.

Wait, but in combinatorial terms, for each unordered triplet {A,B,C}, there are 6 ordered permutations. But in our problem, the triplet (A,B,C) is unordered. So perhaps the sum over all triplets (unordered) of (-1)^(a_AB + a_BC + a_CA) multiplied by 6? Or maybe not. Because a_AB + a_BC + a_CA is the same regardless of the order in which we visit the triplet.

Wait, for unordered triplet {A,B,C}, the sum a_AB + a_BC + a_CA is the same regardless of the order. So the term (-1)^{a_AB + a_BC + a_CA} is the same for all permutations of A, B, C.

Thus, each unordered triplet is counted once in the sum T. So T is the sum over all unordered triplets of (-1)^(sum of parities).

So now, the problem is to compute T as the sum over all unordered triplets {A,B,C} of (-1)^(a_AB + a_BC + a_CA).

But how to compute this sum.

Let's expand the sum T:

T = sum_{A < B < C} (-1)^{a_AB + a_BC + a_AC}.

But again, how to compute this efficiently.

Alternative Idea: Consider that each term in T is the product of three terms: (-1)^{a_AB} * (-1)^{a_BC} * (-1)^{a_AC}.

So T can be rewritten as sum_{A < B < C} product_{edges in the triplet} (-1)^{a_edge}.

So T is the sum over all triplets of the product of (-1)^{a_edge} for each edge in the triplet.

But how to compute this.

This looks like a problem where we need to compute the third moment of the variables (-1)^{a_edge} for each edge. But this seems challenging.

But perhaps, using matrix algebra or inclusion-exclusion.

Let me think of the variables x_AB = (-1)^{a_AB}. Each x_AB is either 1 or -1.

Then T is the sum over all triplets (A,B,C) of x_AB * x_BC * x_AC.

But how to compute this sum.

The sum T can be expressed as:

sum_{A,B,C distinct} x_AB * x_BC * x_AC / 6.

But since each unordered triplet is counted once, and the ordered permutations would count it 6 times. However, perhaps the original sum is over all ordered triplets, but I'm not sure.

Alternatively, since x_AB is symmetric (x_AB = x_BA), we can write:

sum_{A < B < C} (x_AB * x_AC * x_BC) * 6 (since each unordered triplet is represented in 6 ordered ways).

But this is not correct. For example, the ordered triplet (A,B,C) would have edges AB, BC, and AC. But the product x_AB * x_BC * x_AC is the same for any permutation of the triplet. So summing over all ordered triplets would be 6 times the sum over unordered triplets.

So, if we compute the sum over all ordered triplets (A,B,C) where A, B, C are distinct, then T (the sum over unordered triplets) would be equal to (sum over ordered triplets) divided by 6.

But how to compute the sum over ordered triplets.

Let's denote S as the sum over all ordered triplets (A,B,C) of x_AB * x_BC * x_AC.

Then T = S / 6.

But how to compute S.

But what is S?

S = sum_{A} sum_{B≠A} sum_{C≠A,B} x_AB * x_BC * x_AC.

Let's try to expand this.

For a fixed A, we have:

sum_{B≠A} sum_{C≠A,B} x_AB * x_BC * x_AC.

Factor out x_AB and x_AC:

sum_{B≠A} x_AB * x_AC * sum_{C≠A,B} x_BC.

But wait, C cannot be A or B, so C ranges over all points except A and B.

But x_AC is fixed for a given A and C. Hmm, perhaps this approach isn't helpful.

Alternatively, let's consider that for fixed A and C, the term x_AC is part of the product. So:

sum_{A} sum_{B≠A} sum_{C≠A,B} x_AB * x_BC * x_AC = sum_{A} sum_{C≠A} x_AC * sum_{B≠A,C} x_AB * x_BC.

So for fixed A and C, the inner sum is sum_{B≠A,C} x_AB * x_BC.

But B can't be A or C. So B can be any other point.

Now, x_AB * x_BC is the product of the x values for edges AB and BC.

But how to compute this sum for all B not equal to A or C.

Let me denote that for fixed A and C, the sum over B (B not in {A,C}) of x_AB * x_BC.

But x_AB is the x value for edge AB, and x_BC is the x value for edge BC.

But how can we compute this sum efficiently.

Note that x_AB = (-1)^{a_AB}, where a_AB is the parity of the pair (A,B).

But a_AB is 1 if and only if (dx/2 mod2) or (dy/2 mod2) is 1.

So, x_AB = 1 if parity is 0, and -1 if parity is 1.

Wait, no. x_AB is (-1)^{a_AB}, where a_AB is 0 or 1. So x_AB is 1 when a_AB is 0, and -1 when a_AB is 1.

So for each pair (A,B), x_AB is known.

But how to compute sum_{B} x_AB * x_BC.

For fixed A and C, sum_{B} x_AB * x_BC, where B is not A or C.

But x_AB * x_BC = x_AB x_BC.

But x_BC is the same as x_B C. So for each B, this product is x_AB x_BC.

But x_AB is the product for edge AB, and x_BC is the product for edge BC.

Now, considering that for each B, this product is x_AB * x_BC.

But the sum over B is sum_{B} x_AB x_BC.

But x_AB x_BC = x_AB x_B C = x_AC (x_AB x_B C / x_AC) ??? Not sure.

Alternatively, this product can be written as x_AB x_BC = x_AC x_AB x_BC x_AC^{-1}.

No, perhaps not helpful.

Alternatively, perhaps the product x_AB x_BC can be written as x_AC multiplied by x_AB x_BC x_CA.

But I'm not sure.

Alternatively, note that x_AB x_BC = x_AC multiplied by x_AB x_BC x_CA, but not sure.

Alternatively, think of x_AB x_BC as x_AB x_BC = x_A C multiplied by x_AB x_BC x_CA divided by x_A C x_CA. Not sure.

Alternatively, for fixed A and C, consider that x_AB x_BC = x_AB x_B C = x_AB x_C B.

But x_C B is the same as x_BC.

Hmm. Not helpful.

Alternative Idea: For each fixed A and C, the sum over B (B != A, C) of x_AB * x_BC is equal to (sum_{B} x_AB x_BC ) - x_AA x_AC - x_AC x_CC. But since x_AA is zero (a point with B=A is not allowed), and x_CC is also not allowed (B=C), but B can't be A or C. So the sum is sum_{B≠A,C} x_AB x_BC = sum_{all B} x_AB x_BC - x_AC x_BC (but B=C is not allowed). Wait, not sure.

But for B not equal to A or C, x_AB x_BC is the product for edges AB and BC.

But for B = C, it's not allowed. So sum_{B≠A,C} x_AB x_BC = sum_{B} x_AB x_BC - x_AC x_CC (when B=C) - x_AA x_AC (when B=A). But x_CC is not defined (as a pair), so maybe the original sum is just sum_{B} x_AB x_BC - x_AC x_BC (when B=C) - x_AB x_BC (when B=A). But this is unclear.

Alternatively, since B can be any point except A and C, the sum is over all B not equal to A or C. So sum_{B} x_AB x_BC, where B is in the set S = all points except A and C.

So this sum is equal to (sum_{B} x_AB x_BC) - x_AA x_AC - x_AC x_CC.

But x_AA is x_{A,A} which is not present, but since B=A is excluded, the term x_AA x_AC is zero (as B=A is not considered). Similarly for B=C, which is also excluded.

So the sum is sum_{B} x_AB x_BC - x_AC x_CC (for B=C) - x_AA x_AC (for B=A). But since B=A and B=C are not allowed, but x_AA and x_CC are not defined. So perhaps the sum is simply sum_{B} x_AB x_BC minus the terms where B=A or B=C.

But in reality, when B=A, the term x_AB is x_AA which is not part of the pairs. So perhaps it's better to assume that B is not A or C and proceed.

But this line of thinking may not lead us anywhere.

Alternative Idea: For a fixed A and C, the sum over B (B != A,C) of x_AB x_BC can be expressed as (sum_{B} x_AB x_BC) - x_AA x_AC - x_AC x_CC. But since x_AB is 0 when B is not a valid point. No, x_AB is defined for all pairs of points. So sum_{B} x_AB x_BC includes B =A and B=C, which are invalid. So to get the desired sum, we subtract those terms.

But x_AB x_BC when B=A is x_AA x_AC. But x_AA is the product for the pair (A,A), which is not part of the data. However, since all points are distinct, such pairs are not present. So perhaps we can assume that x_AB is only defined for B != A.

But according to the problem statement, the fence posts are distinct and the pairs are distinct. So for the sum, B is a different point from A and C.

So the sum over B (B != A,C) x_AB x_BC is equal to sum_{B} x_AB x_BC minus x_AC x_CC (when B=C) minus x_AA x_AC (when B=A).

But x_AA and x_CC are not part of the data, so how to handle this?

Alternatively, since B must be a different point from A and C, we can assume that in the sum, B ranges over all points except A and C. So the sum is sum_{B ∈ S} x_AB x_BC, where S is the set of points excluding A and C.

But how to compute this sum.

Let me think of x_AB as the entry in a matrix X at row A, column B. Then, x_AB x_BC is the product of X[A][B] * X[B][C]. The sum over B of X[A][B] * X[B][C] is the (A,C) entry of the matrix X squared (X^2). So sum_{B} X[A][B] * X[B][C] = (X^2)[A][C].

So the sum for fixed A and C over B of X[A][B] * X[B][C] is (X^2)[A][C]. But this includes B=A and B=C. So the desired sum is (X^2)[A][C] - X[A][A] * X[A][C] - X[A][C] * X[C][C}. But since in our case, X[A][A] is not part of the data (as the pairs are between distinct points), we can assume that X[A][A] is zero.

But wait, x_AB is defined for all pairs, including B=A. But according to the problem statement, all pairs are between distinct points, so x_AA is not considered, and thus x_AA can be treated as zero. But this is not the case. The pairs (A,B) are for distinct A and B. So in the matrix X, the diagonal entries are undefined. But in the sum, B ranges over all points except A and C.

So the sum over B (B != A, C) of X[A][B] * X[B][C] is equal to (X^2)[A][C] - X[A][A] * X[A][C] - X[C][C] * X[A][C} - X[A][C] * X[C][C} ? Not sure.

But this approach may not be feasible, as it requires matrix multiplication which is O(n^3) for n=6e3.

But matrix multiplication is O(n^3), which is way too slow for n=6e3.

So this approach isn't feasible.

Alternative Idea: Let's find a way to compute T by counting the number of triplets where the product x_AB x_BC x_CA is 1 or -1.

But this doesn't directly help.

Another Idea: Let's think about the parity of the sum. The sum T is the sum of products x_AB x_BC x_CA for all triplets.

But x_AB x_BC x_CA is equal to the product of the three edges of the triplet.

But if the sum of the parities is even, then the product is 1. If the sum is odd, product is -1.

So T is equal to the number of triplets with even sum minus the number with odd sum. Because 1 * count_even + (-1) * count_odd = (count_even - count_odd). But since the answer is count_even = (total + T)/2, and T = count_even - count_odd. So count_even = (total + T)/2.

But this is circular.

Alternatively, since the answer is (C(n,3) + T)/2, and T is the sum of the products for all triplets.

So if we can compute T, we can find the answer.

But how to compute T.

Another Idea: For each pair (A,B), the parity is 0 or 1. So x_AB is 1 or -1.

The sum T can be written as the sum over all triplets (A,B,C) of x_AB x_BC x_CA.

But this can be rewritten as the sum over all triplets of x_AB x_BC x_CA.

But x_AB x_BC x_CA = x_AB x_BC x_CA.

But since x_AB = x_BA, etc.

But I don't see a way to factor this.

Alternative Idea: Perhaps the sum T can be expressed in terms of the sum of cubes of some variables.

But I'm not sure.

Let me consider the following:

The sum T is the sum over all triplets (A,B,C) of x_AB x_BC x_CA.

This can be rewritten as sum_{A,B,C} x_AB x_BC x_CA.

But this includes all ordered triplets (including A=B, B=C, etc.), but in our case, A, B, C must be distinct. So the sum is over distinct A, B, C.

But even so, this sum is difficult to compute.

Another Idea: Consider that x_AB is a variable that is 1 or -1. Then, the product x_AB x_BC x_CA is 1 or -1.

But the sum T is the sum of these products over all valid triplets.

But again, how to compute this sum.

Alternative Idea: Since the parity of the edge AB is determined by the parities of dx/2 and dy/2 mod 2, perhaps we can precompute for each point its coordinates modulo 4.

Wait, the coordinates of the points are even. So let's represent each point (x, y) as (x/2, y/2). Let's call this (a, b). Then, a and b are integers.

The parity of the edge between two points (a1, b1) and (a2, b2) is ( (a2 - a1) mod 2 ) | ( (b2 - b1) mod 2 ).

But since a2 -a1 is (x2 -x1)/2, which is an integer.

So for each point, if we store (a mod 2, b mod 2), where a = x/2 and b = y/2, then the parity of the edge between two points depends on the differences in their a and b mod 2.

Specifically, for two points A and B with (aA mod2, bA mod2) and (aB mod2, bB mod2), the parity of the edge AB is ( (aB - aA) mod2 ) | ( (bB - bA) mod2 ). But since (aB -aA) mod2 is (aA -aB) mod2, the parity is the same as (aA XOR aB) OR (bA XOR bB).

Wait, but (aB - aA) mod2 is the same as (aA XOR aB), since subtraction mod2 is XOR.

So parity_p(AB) = ( (aA XOR aB) ) OR ( (bA XOR bB) ).

But wait, (aA XOR aB) is 1 if aA and aB are different, 0 otherwise. Similarly for (bA XOR bB). The OR of these two is 1 if either is 1. So parity_p(AB) is 1 if the two points have different a or different b mod2.

So the parity is 1 when the two points differ in at least one of the coordinates (a mod2 or b mod2).

So this is equivalent to the parity_p being 1 when the two points are not in the same "quadrant" mod2.

So, each point can be categorized into one of four types based on (a mod2, b mod2): (0,0), (0,1), (1,0), (1,1).

Let me call these types 0, 1, 2, 3.

For example:

Type 0: a mod2=0, b mod2=0.

Type 1: a mod2=0, b mod2=1.

Type 2: a mod2=1, b mod2=0.

Type 3: a mod2=1, b mod2=1.

Then, for any two points of types T1 and T2, the parity_p is 1 if their types are different, and 0 if their types are the same.

Because if two points are in the same type, then their a mod2 and b mod2 are the same. So the differences in a and b mod2 are 0, so the OR is 0. If the types are different, then at least one of the differences in a or b mod2 is 1, so the OR is 1.

So the parity_p(AB) is 1 if and only if the two points are of different types.

This is a crucial observation.

So, the parity_p between two points depends only on whether their types are the same or different.

So now, the problem reduces to counting the number of triplets of points (A,B,C) where the number of pairs (AB, BC, CA) that have different types is even.

But since parity_p(AB) is 1 if the types are different, and 0 if the same, the sum of the three parities is the number of edges in the triplet with different types.

We need this sum to be even.

So for a triplet (A,B,C), we need the number of edges (AB, BC, CA) with different types (i.e., parity_p=1) to be even.

But since each edge's parity is 1 if the two points are of different types, the sum is the number of edges in the triplet that connect points of different types.

We need this count to be even.

So the problem is now: count the number of triplets where the number of edges between different-type pairs is even.

But how to compute this efficiently.

This seems manageable. Because now, we can group the points by their type (0,1,2,3), and then compute the number of triplets within and between these groups that satisfy the condition.

Let's denote the counts of each type as cnt[0], cnt[1], cnt[2], cnt[3].

For example, type 0 has cnt[0] points, etc.

Now, the problem is to count all possible triplets (A,B,C) where the number of edges (AB, BC, CA) with different types is even.

This depends on the types of the three points in the triplet.

Let's consider all possible combinations of types for the three points in the triplet. For each possible combination of types (T1, T2, T3), we can compute the number of edges with different types and determine if it's even.

For example:

- If all three points are of the same type (e.g., all type 0). Then, AB, BC, CA are all same-type pairs → parity 0. So sum is 0 → even. So all such triplets contribute 1 to the answer.

- If two points are of type 0 and one is of type 1. Let's see the edges:

AB: same type (0 and 0 → parity 0).

BC: type 0 and 1 → parity 1.

CA: type 1 and 0 → parity 1.

So sum is 2 → even. So such triplets contribute 1 to the answer.

But we need to consider all possible combinations of types for the three points.

But with 4 types, there are 4^3 =64 possible ordered type combinations. But since the triplet is unordered, this can be reduced by considering combinations with multiplicities.

But this is still manageable.

Alternatively, group the triplets by the types of their three points. For each possible group (a, b, c), compute the number of triplets in this group and whether they contribute to the answer.

But how.

Let me think: for a triplet of points with types A, B, C (not necessarily distinct), the number of edges with different types is:

- edge AB: 1 if A != B.

- edge BC: 1 if B != C.

- edge CA: 1 if C != A.

Sum is the count of edges with different types.

We need this sum to be even.

So for each possible combination of types (A, B, C), compute the sum of the three edges' parities (0 or 1), and if it's even, multiply by the number of triplets in that combination.

The total answer is the sum over all such combinations.

But how to compute this for all possible combinations.

But with 4 types, this is manageable.

Let me list all possible combinations of types for three points and compute the sum of parities:

Case 1: All three points are the same type.

sum = 0 + 0 + 0 = 0 → even. So all such triplets contribute.

The number of such triplets is C(cnt[T], 3) for each type T.

Case 2: Two points of the same type, and one of a different type.

For example, types T, T, S (where S != T).

In this case, the edges between T and T are same-type (0), T and S are different (1), and S and T are different (1).

Sum is 0 +1 +1 = 2 → even. So these triplets contribute.

The number of such triplets is:

For each pair of distinct types T and S:

Choose two points from T and one from S: C(cnt[T], 2) * cnt[S].

But since the triplet can be T, T, S in any order, but in this case, the two T's are fixed. So the number of triplets is C(cnt[T], 2) * cnt[S] for each T and S != T.

But since the order of the triplet doesn't matter, this accounts for all such triplets where two are T and one is S.

So for each T and S != T, the number is C(cnt[T],2) * cnt[S], and each such triplet contributes 1.

So the total for this case is sum_{T} sum_{S != T} C(cnt[T], 2) * cnt[S}.

Case 3: All three points of distinct types. But there are various subcases here. For example, the types could be all different, or two different and one same.

Wait, no. Case 3 is when all three points are of different types.

But given four possible types, three points can't all be distinct types. So this case is not possible. Or wait, if there are four types, a triplet can have up to three distinct types.

For example, types 0,1,2. Or 0,1,3, etc.

So for a triplet with three distinct types, we need to compute the sum of the three edges' parities.

Let's take an example: types 0,1,2.

Edge 0-1: 1 (different).

Edge 1-2: 1 (different).

Edge 2-0: 1 (different).

Sum is 3 → odd. So not contributing.

Another example: types 0,1,1.

This is covered in case 2.

Another example: types 0,1,3.

Edges 0-1:1.

1-3:1 (different types).

3-0:1 (different types).

Sum 3 → odd.

So triplet with three distinct types contributes sum=3 → odd. So not counted.

Another case: types 0,0,1.

Sum is 0+1+1=2 → even. Covered in case 2.

Case 4: Two types, but three points of two types. For example, two of type T and one of type S, where T and S are different. This is covered in case 2.

Case 5: Three points of three different types, but two of them are the same in one coordinate.

For example, types 0,1,2.

0: (0,0)

1: (0,1)

2: (1,0)

Edges:

0-1: different → 1.

1-2: different → 1.

2-0: different → 1.

Sum 3 → odd.

So no contribution.

Case 6: Three points of two different types, but three points.

For example, two types T and S, and three points of which two are T and one is S. Covered in case 2.

So the only cases that contribute to the answer are:

- All three points are of the same type.

- Two points are of one type, and the third is of another type.

- Other cases where the sum of edges is even.

Wait, let's think of another example where the sum is even.

For example, three points of types 0, 1, 3.

Edges:

0-1:1.

1-3:1.

3-0:1.

Sum 3 → odd.

No.

What if the three points are of types 0, 1, 2, 3. No, it's three points. So three distinct types.

Another example: types 0, 0, 1. Sum 0+1+1=2 → even.

Another example: types 0, 1, 1. Sum 1 + 0 +1 =2 → even.

Another example: types 0,0,0. Sum 0 → even.

So the contributing cases are:

- All three of the same type.

- Two of one type and one of another type.

- Any other case where the sum of the edges' parities is even.

Wait, are there other cases where the sum is even?

For example, types 0, 2, 2.

Edges:

0-2: different → 1.

2-2: same → 0.

2-0: different →1.

Sum 1+0+1=2 → even. So this is covered in case 2.

Another example: types 0,2,3.

Edges:

0-2: different →1.

2-3: different →1.

3-0: different →1.

Sum 3 → odd.

No.

Another example: types 0,0,2.

Edges:

0-0: 0.

0-2:1.

2-0:1.

Sum 0+1+1=2 → even.

Yes, covered in case 2.

So the only contributing cases are:

1. All three points of the same type.

2. Two of one type and one of another type.

There are no other cases where the sum is even.

So the answer is the sum of:

- For each type T, C(cnt[T], 3).

- For each pair of distinct types T and S, C(cnt[T], 2) * cnt[S] + C(cnt[S], 2) * cnt[T].

Wait, because for each pair of types T and S, the number of triplets with two T's and one S is C(cnt[T],2)*cnt[S], and the number with two S's and one T is C(cnt[S],2)*cnt[T}. But wait, this is not correct.

Because in the case of two T's and one S, the sum is 2, which is even and contributes 1 per triplet. Similarly, for two S's and one T, the sum is also 2. So both are counted.

So the total number of triplets in case 2 is the sum over all ordered pairs (T, S) where T < S of [ C(cnt[T],2)*cnt[S] + C(cnt[S],2)*cnt[T} ].

But for unordered pairs (T, S), T != S.

But since in the sum, T and S can be swapped, we can compute it for all T and S pairs where T != S.

So the total number of triplets in case 2 is sum_{T} sum_{S != T} C(cnt[T],2) * cnt[S}.

Because for each T, and for each S != T, there are C(cnt[T], 2) * cnt[S} triplets with two T's and one S.

But this counts for T and S as distinct, e.g., T=0, S=1 and T=1, S=0 are both considered. But in reality, when T=0 and S=1, we get triplets with two 0's and one 1, and when T=1 and S=0, we get triplets with two 1's and one 0. So these are different scenarios, and we need to count both.

So the total for case 2 is sum_{T} sum_{S != T} C(cnt[T], 2) * cnt[S}.

So putting it all together:

answer = sum_{T=0 to 3} C(cnt[T], 3) + sum_{T=0 to3} sum_{S != T} C(cnt[T], 2) * cnt[S}.

This is the formula for the answer.

So the steps to compute the answer are:

1. Precompute the types of each point based on (x/2 mod 2, y/2 mod 2).

2. Count the number of points in each of the four types.

3. Compute the sum of C(cnt[T],3) for each type T.

4. Compute the sum of C(cnt[T],2)*cnt[S] for all T and S where S != T.

5. The total answer is the sum of these two sums.

This approach is O(n) time for steps 1 and 2, and O(1) for steps 3 and 4.

So this is the optimal approach.

Now, the code can be written as follows:

For each point, compute a = x//2, b = y//2.

Then, compute a mod 2 and b mod 2. This gives the type of the point.

We then count how many points are in each of the four types.

Then compute the sum of C(cnt[t],3) for each t in 0-3.

Then compute the sum over all pairs of types T and S (T != S) of C(cnt[T], 2)*cnt[S.

Finally, add these two sums and output.

But wait, let's verify this with the sample inputs.

Sample input 1:

3

0 0 → (0,0) → a=0, b=0 → type 0 (0 mod 2, 0 mod 2).

2 0 → (1,0) → a=1, b=0 → type 2.

0 4 → (0,2) → a=0, b=2 → a mod2=0, b mod2=0 → type 0.

So types:

0: 2 points.

2: 1 point.

The counts are:

type 0: 2

type 1: 0

type 2: 1

type 3: 0.

Sum of C(cnt,3):

C(2,3) = 0.

For each T and S != T:

For T=0:

C(2,2) * sum_{S !=0} cnt[S} = 1 * (0 + 1 + 0) = 1.

For T=1:

C(0,2) * sum of others is 0.

For T=2:

C(1,2) is 0.

For T=3: 0.

So sum for case 2 is 1.

So total answer is 0 +1 =1, which matches the sample.

Another sample input:

Sample 2:

5

0 0 → type 0.

2 16 → (1, 8) → a=1 mod2=1, b=8 mod2=0 → type 2.

30 14 → (15,7) → 15 mod2=1, 7 mod2=1 → type 3.

4 6 → (2,3) → 2 mod2=0, 3 mod2=1 → type 1.

2 10 → (1,5) → 1 mod2=1, 5 mod2=1 → type 3.

So types:

Point 0: type 0.

Point 1: type 2.

Point 2: type 3.

Point 3: type 1.

Point 4: type 3.

So counts:

type 0: 1

type 1: 1

type 2: 1

type 3: 2.

Sum of C(cnt,3) for all types:

type 0: C(1,3)=0.

type 1: 0.

type 2: 0.

type3: C(2,3)=0.

Total sum is 0.

Sum for case 2:

For each T:

For T=0:

C(1,2) =0, so contributes 0 for all S.

For T=1:

C(1,2) =0.

For T=2:

C(1,2)=0.

For T=3:

C(2,2) =1. sum_{S !=3} cnt[S} =1 +1 +1 =3. So 1 *3 =3.

So case 2 sum is 3.

Total answer is 0 +3 =3, which matches the sample.

So this approach works.

Thus, the code can be written as:

- Read all points, compute their type.

- Count the number of points in each type.

- Compute the sum of combinations for each type.

- Compute the sum for case 2.

- Output the total sum.

Now, the code in Python:

We can use the following steps:

Read n.

For each of the next n lines, read x and y.

Compute a = x //2, b = y //2.

Compute a mod 2 and b mod 2.

The type is (a%2)*2 + (b%2), which gives 0,1,2,3.

Count the number of points in each type.

Then compute sum_1: sum over t in 0-3 of combinations(cnt[t],3).

sum_2: sum over t in 0-3, sum over s in 0-3 where s != t: combinations(cnt[t], 2) * cnt[s}.

Then the answer is sum_1 + sum_2.

In Python, combinations can be computed using math.comb, which is available in Python 3.10+. Since the code must be compatible with older versions, but given that it's a programming competition, it's safe to assume that math.comb is available.

But for n=6000, math.comb(6000,3) is manageable.

But for the sample inputs, this approach works.

So the code:

Read n.

Initialize a list counts = [0, 0, 0, 0].

For each point:

x, y = map(int, input().split())

a = x // 2

b = y // 2

type_ = (a % 2) * 2 + (b % 2)

counts[type_] +=1

Then compute sum_1 and sum_2.

sum_1 = 0

for cnt in counts:

sum_1 += math.comb(cnt, 3)

sum_2 = 0

for t in range(4):

c = counts[t]

if c >= 2:

term = math.comb(c, 2)

for s in range(4):

if s != t:

sum_2 += term * counts[s]

print(sum_1 + sum_2)

But wait, this loop for t and s is O(4*4) operations, which is negligible.

Yes.

So the code should work.

Testing against sample input 1.

```python
import math


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    counts = [0, 0, 0, 0]

    for _ in range(n):
        x, y = map(int, input_stream.readline().rstrip("\n").split())
        a = (x // 2) % 2
        b = (y // 2) % 2
        typ = a * 2 + b
        counts[typ] += 1

    sum_case1 = 0
    for cnt in counts:
        sum_case1 += math.comb(cnt, 3)

    sum_case2 = 0
    for t in range(4):
        c_t = counts[t]
        if c_t >= 2:
            combinations = c_t * (c_t - 1) // 2  # math.comb(c_t, 2)
            for s in range(4):
                if s != t:
                    sum_case2 += combinations * counts[s]

    print(sum_case1 + sum_case2, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
0 0
2 16
30 14
4 6
2 10
""",
            "output": \
"""\
3
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

Sample 2:

counts: [1,1,1,2]

sum_1 = 0.

sum_2:

t=3:

c=2 >=2 → comb(2,2)=1.

sum s !=3 → s=0,1,2.

counts[0] =1, counts[1]=1, counts[2]=1.

sum_2 += 1*(1+1+1) =3.

Other t's:

t=0: c=1 <2 → no.

t=1: c=1 <2 → no.

t=2: c=1 <2 → no.

So sum_2 is 3.

Total 0+3=3.

So this works.

Thus, the code is correct.
</think>

```python
import math

n = int(input())
counts = [0, 0, 0, 0]

for _ in range(n):
    x, y = map(int, input().split())
    a = (x // 2) % 2
    b = (y // 2) % 2
    typ = a * 2 + b
    counts[typ] += 1

sum_case1 = 0
for cnt in counts:
    sum_case1 += math.comb(cnt, 3)

sum_case2 = 0
for t in range(4):
    c_t = counts[t]
    if c_t >= 2:
        combinations = c_t * (c_t - 1) // 2  # math.comb(c_t, 2)
        for s in range(4):
            if s != t:
                sum_case2 += combinations * counts[s]

print(sum_case1 + sum_case2)
```
