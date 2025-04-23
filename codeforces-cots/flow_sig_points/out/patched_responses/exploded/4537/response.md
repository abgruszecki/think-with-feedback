<think>
Okay, let's see. I have to find the sum of all 12 edges of a rectangular parallelepiped given the areas of three adjacent faces. Hmm. The problem says that each face has a common vertex, so those three faces are adjacent in such a way that their edges are the three different pairs of the dimensions of the box. Like, if the edges are a, b, c, then the three areas are ab, ac, bc. But wait, the input gives three areas, but not in order. So the three given areas could be any permutation of ab, ac, bc. But the sum of the edges is 4*(a + b + c), right? Because a rectangular box has 12 edges: 4 of each of the three lengths. So the key is to find a, b, c given the three areas.

Wait, the input is three integers which are the areas of the three faces. Let's denote the three areas as x, y, z. Then according to the problem, x = ab, y = ac, z = bc. Because those are the three possible pairs. But since the order of the input can be any permutation, I need to find a, b, c such that their pairwise products are the given x, y, z. Once I have a, b, c, multiply their sum by 4 and that's the answer.

So first step is to find a, b, c from x, y, z. How?

Let's multiply all three areas: (ab)(ac)(bc) = a² b² c². So the product of x, y, z is (abc)^2. So taking the square root gives abc. Then abc = sqrt(x*y*z). Once we have abc, then:

a = abc / (sqrt(bc)) → but bc is one of the given values. Wait, let's think again. Let's say the product x*y*z = (abc)^2. So abc = sqrt(x*y*z). Then:

If x=ab, y=ac, z=bc, then:

a = sqrt( (x*y)/z )

Wait, let's see:

x = ab, y = ac, z = bc.

Multiply x and y: ab * ac = a² bc. But bc is z. So x*y = a² z → a² = x*y / z → a = sqrt( (x*y)/z ). Similarly for b and c.

Wait, that's a good way to find a, b, c. So:

a = sqrt( (x*y) / z )

b = sqrt( (x*z) / y )

c = sqrt( (y*z) / x )

But since the input could be any permutation of the three areas, perhaps we need to first determine which of the three corresponds to which pair. Wait, but the input is given as three numbers, but they are the three possible products. For example, if the areas are 4,6,6 as in the second example, then let's see:

The three products are 4,6,6. Let's compute a, b, c.

Let's assume x=4, y=6, z=6.

Then:

a = sqrt( (4*6)/6 ) → sqrt(24/6) = sqrt(4) = 2.

b = sqrt( (4*6)/6 ) = same as a, 2.

c = sqrt( (6*6)/4 ) = sqrt(36/4) = 3. So the edges are 2,2,3. Sum is (2+2+3)*4=7*4=28. Which matches the example.

So this formula works. But wait, what if the input is not in the order of ab, ac, bc? Like, suppose the input is bc, ab, ac. Then the same approach would work. Because if x=bc, y=ab, z=ac, then:

a = sqrt( (x*y)/z ) → (bc*ab)/(ac) = (b² a c ) / (a c) ) = b² → so sqrt gives b. Wait, but that's not a. So that's a problem.

Ah, right. Because the order of x, y, z in the input could be any permutation. So my approach of taking x*y/z might not directly give a. So I need a way to find a, b, c regardless of the order of the input.

Hmm. Let's think differently. Let me denote the three given areas as s1, s2, s3. Then the three products are ab, ac, bc in some order. So we have:

ab = s1, ac = s2, bc = s3 → multiply all three: (abc)^2 = s1*s2*s3 → abc = sqrt(s1*s2*s3). Then a = abc/(bc) → which is sqrt(s1 s2 s3)/s3. But bc is s3. Wait, but if the given s3 is bc, then yes. But if the given s3 is ab, then this approach would not work.

Wait, perhaps the problem is that the order of s1, s2, s3 is arbitrary. So to find a, b, c correctly, regardless of the order, perhaps we can first compute the product of all three areas, take the square root to get abc. Then, each of the variables can be obtained by dividing abc by the product of the other two variables. Wait, no. Because if abc = sqrt(s1 s2 s3), then a = abc / (bc) → but bc is one of the s's. But which s is it?

Alternatively, perhaps the three given areas are the three possible pairs. So regardless of their order, their product is (a*b)(a*c)(b*c) = a² b² c². So the product is (abc)^2. So abc is sqrt(s1 s2 s3). Then, the individual variables can be found by:

a = abc / (b*c). But bc is one of the s's. But which one?

Wait, for example, in the first sample input: 1, 1, 1. The product is 1, sqrt is 1. Then a = 1/(b*c). But since ab=1, bc=1, etc. So maybe:

Let me think: If the three areas are ab, ac, and bc. Then:

a = abc / (bc) → bc is the third area. So if the three areas are x, y, z (in any order), then the three possible variables are abc/x, abc/y, abc/z. Wait, that's possible. Wait, abc is the product of a, b, c. So if x is ab, then c = abc/(ab) = c. So for example, x is ab, then abc/x = c. Similarly, if y is ac, then abc/y = b. And z is bc, so abc/z = a. So, for example, the variables a, b, c can be found by abc divided by each of the given areas, but in some order. But since the order of the areas is arbitrary, how do we know which is which?

Ah! So here's the key: the three given areas are all pairwise products of a, b, c. So, the product of all three is (abc)^2. So abc is sqrt(s1*s2*s3). Let's compute that. Then, the three variables a, b, c are equal to (abc) divided by each pair of the given areas. Because:

If the areas are ab, ac, bc, then:

a = (abc) / (bc) → which is a. Because bc is one of the areas.

Similarly, b = (abc)/(ac) → which is b, since ac is another area.

c = (abc)/(ab) → which is c.

But if the given areas are in a different order, like say, s1=bc, s2=ab, s3=ac. Then:

a = (abc)/s1 → abc/(bc) = a.

b = (abc)/s3 → abc/(ac) = b.

c = (abc)/s2 → abc/(ab) = c.

So regardless of the order of the three given areas, the three variables a, b, c can be calculated as (abc) divided by each of the given areas, but then taking the square root. Wait, wait. Because abc is sqrt(s1*s2*s3), which is the product of a, b, c. So for example, let's compute:

abc = sqrt(s1*s2*s3). Then:

a = sqrt( (abc) / (s2) ) * sqrt( (abc) / (s3) ) ) ?

Wait, maybe I'm getting confused here. Let's re-express this.

Alternatively, if s1, s2, s3 are the three pairwise products (ab, ac, bc in any order), then:

a = sqrt( (s2 * s3) / s1 )

Because, if s1 is bc, s2 is ab, s3 is ac:

(s2 * s3)/s1 = (ab * ac) / bc = (a² bc) / bc = a² → sqrt gives a.

Similarly, if s1 is ab, s2 is ac, s3 is bc:

(s2 * s3)/s1 = (ac * bc) / ab = (b c a c ) / (a b) ) = c² → sqrt gives c. Wait, that doesn't match. Hmm.

Wait, perhaps this approach is not correct. Let's think again.

We have three equations:

ab = s1

ac = s2

bc = s3

If we multiply all three, we get (abc)^2 = s1 s2 s3 → abc = sqrt(s1 s2 s3).

Then, a can be found by (abc) / (bc) = a. But bc is s3. So a = abc / s3.

Similarly, b = abc / s2, and c = abc / s1.

But wait, in this case:

abc = sqrt(s1 s2 s3). So a = sqrt(s1 s2 s3) / s3.

Which is sqrt( s1 s2 s3 ) / s3 = sqrt( s1 s2 / s3 ) ).

So a = sqrt( (s1 s2) / s3 )

Similarly, b = sqrt( (s1 s3)/s2 ), and c = sqrt( (s2 s3)/s1 )

Ah! So regardless of the order of the given areas, if they are the three possible pairwise products, then a, b, c can be calculated as the square roots of (s1*s2/s3), (s1*s3/s2), (s2*s3/s1) respectively.

Wait, but how can we be sure that these are the correct pairs? Let's take the example where the input is 4,6,6.

s1=4, s2=6, s3=6.

Then a = sqrt( (4*6)/6 ) = sqrt(24/6) = 2.

b = sqrt( (4*6)/6 ) = 2.

c = sqrt( (6*6)/4 ) = sqrt(36/4) = 3. Which is correct.

Another example: input 1,1,1.

a = sqrt( (1*1)/1 ) = 1. Similarly for b and c. Sum is 4*(3) =12.

Now, what if the input is given in a different order, say, s1=ac, s2=ab, s3=bc.

For example, a=2, b=3, c=4. Then the areas would be ab=6, ac=8, bc=12. Suppose the input is given as 8,6,12.

Then:

s1=8, s2=6, s3=12.

a = sqrt( (8*6)/12 ) = sqrt(48/12) = sqrt(4) =2. Correct.

b = sqrt( (8*12)/6 ) = sqrt(96/6) = sqrt(16) =4. Wait, but original b was 3. Hmm, this doesn't add up. Wait, wait, what's wrong here.

Wait, in this case, the areas are ab=6, ac=8, bc=12. So the input is [6,8,12] or any permutation. Suppose the input is given as 8,6,12.

Then:

s1=8 (ac), s2=6 (ab), s3=12 (bc).

Then according to the formula:

a = sqrt( (s1*s2)/s3 ) → (8*6)/12 = 48/12=4 → sqrt(4)=2. Which is correct.

b = sqrt( (s1*s3)/s2 ) → (8*12)/6 = 96/6=16 → sqrt(16)=4. But original b is 3. Wait, this is conflicting.

What's wrong here? Because the original variables are a=2, b=3, c=4. So ab=6, ac=8, bc=12.

But according to the formula, with s1=8 (ac), s2=6 (ab), s3=12 (bc):

a is computed as sqrt( (8*6)/12 ) → 48/12=4 → sqrt(4)=2. Correct.

b is sqrt( (8*12)/6 ) → 96/6=16 → sqrt(16)=4. But original b is 3. So why is this discrepancy?

Oh wait, because in this case, the formula is not giving the correct result. So perhaps the formula is only valid when the input s1, s2, s3 are in the order ab, ac, bc. But when the order is different, the formula may not work.

So this suggests that the approach of computing a, b, c as sqrt(s1*s2/s3), sqrt(s1*s3/s2), sqrt(s2*s3/s1) may not work when the input is not in the order ab, ac, bc.

This is a problem. So how to resolve this?

Wait, perhaps the key is that the three given areas can be any permutation of ab, ac, bc. So the formula for a, b, c should be such that the product of any two variables equals one of the given areas.

But how to find a, b, c given the three areas in any order?

Alternative approach:

Let the three input areas be x, y, z.

We need to find a, b, c such that the three pairwise products (ab, ac, bc) are exactly the three input values, in any order.

Once we have a, b, c, the sum is 4*(a + b + c).

So the problem reduces to finding a, b, c given that the three products are the input values.

But how?

The product of all three areas is (ab)(ac)(bc) = a² b² c². So abc = sqrt(x y z). Let's compute that.

Then, the variables a, b, c can be found as follows:

a = abc / (b*c) → but bc is one of the input areas. So, for example, if one of the input areas is bc, then a = abc / (bc).

But since we don't know which input area corresponds to which product, this approach requires us to find which input area is bc, which is ac, and which is ab.

But since the input can be any permutation, perhaps we can compute all possible possibilities and find the one that works.

But how?

Alternatively, since abc is known, the three variables a, b, c can be computed as abc divided by each of the three input areas, but the square root of that. Wait, perhaps:

Let's compute abc = sqrt(x y z). Then, the possible values for a, b, c could be sqrt( (abc) / x ), sqrt( (abc)/y ), sqrt( (abc)/z ), but perhaps in a different order.

Wait, let's see. Let me take the previous example where a=2, b=3, c=4. The areas are ab=6, ac=8, bc=12. The product xyz =6*8*12=576. abc=2*3*4=24. So sqrt(576)=24. Correct.

Then, abc is 24.

Then, sqrt(24 / x) for x in each area:

For x=6: sqrt(24/6) = sqrt(4) = 2 → which is a.

For x=8: sqrt(24/8) = sqrt(3) → approx 1.732. Which is not part of a, b, c.

Wait, but in this case, the correct variables a, b, c are 2,3,4. So, perhaps the three variables a, b, c are sqrt( (abc) / x ), sqrt( (abc)/y ), sqrt( (abc)/z ), but only in some order.

But how?

Wait, in the example with a=2, b=3, c=4, and the areas are 6, 8, 12.

Then:

abc = 24.

sqrt(24/6) = 2 → a.

sqrt(24/8) = sqrt(3) → not a variable.

sqrt(24/12) = sqrt(2) → not a variable.

So this approach gives only one correct value, which is a.

Hmm, this suggests that the approach is incorrect.

Alternative approach:

We need to find three numbers a, b, c such that the set {ab, ac, bc} is equal to the set {x, y, z}.

So, given x, y, z, find a, b, c where {ab, ac, bc} = {x, y, z}.

But how?

An alternative idea: Let's compute the product of all three input values, take the square root to get abc. Then, for each input value s, compute (abc) divided by s, and take the square root. The three numbers obtained this way are a, b, c in some order.

Wait, let's see.

In the example where a=2, b=3, c=4:

abc = 24. The input areas are 6, 8, 12.

So for each s in 6,8,12:

sqrt(24/s) = sqrt(4) = 2 (for 6), sqrt(3) (for 8), sqrt(2) (for 12). Which gives 2, sqrt(3), sqrt(2). These do not match the original a, b, c.

Hmm. So this approach gives values that are not correct.

Wait, perhaps I made a mistake here. Let me recheck.

Original variables are a=2, b=3, c=4. So ab=6, ac=8, bc=12. So the input areas are 6,8,12.

Then, abc = 24.

sqrt(24 / 6) = sqrt(4) = 2 → which is a.

sqrt(24 / 8) = sqrt(3) → approximately 1.732.

sqrt(24 /12) = sqrt(2) → approximately 1.414.

So the three numbers are 2, sqrt(3), sqrt(2). These do not match the original variables. So this approach is not correct.

So that suggests that the previous approach is invalid.

Hmm. So what's wrong here?

Ah, perhaps the initial approach was based on the assumption that the input areas are ordered as ab, ac, bc. But when the order is different, the approach may not work.

So what's the correct way to find a, b, c given the three areas in any order?

Alternative idea: Let's suppose that the three input areas are x, y, z. Then:

We can compute a = sqrt( (x*y) / z ), but only if z is the product of the other two variables. Wait, but that's not necessarily the case.

Wait, but according to the problem statement, the input is guaranteed to have a solution. So the three given areas must be the three pairwise products of some a, b, c.

So the correct approach is:

Compute abc = sqrt(x * y * z).

Then, the variables a, b, c must be:

a = abc / (bc) → but bc is one of x, y, z. Similarly for the others.

But how to find which of x, y, z is bc?

Ah! Because the three given areas are the three pairwise products, then one of them is bc, another is ac, and another is ab. So abc is known, and for each of the three given areas s, abc / s would be the third variable.

For example, in the case where the given areas are 6,8,12 (from a=2, b=3, c=4):

abc =24.

Then, 24/6=4 → which is c. Because 6 is ab. So c =4.

24/8=3 → which is b. Because 8 is ac.

24/12=2 → which is a. Because 12 is bc.

So the three values abc/s are 4,3,2. Which are exactly the variables. So the variables a, b, c are the three values obtained by dividing abc by each of the input areas, but in a certain order.

But how to get the correct order?

Because the input can be in any order, the three numbers abc/x, abc/y, abc/z will be the variables a, b, c. But since the order of the input is not known, these three numbers can be the variables in any order. So the correct variables are (abc/x, abc/y, abc/z), but multiplied in such a way that their pairwise products are the input areas.

Wait, but how?

Wait, let's take the variables a, b, c. Then, the product of a and b is x (one of the input areas). The product of a and c is y (another input area). The product of b and c is z (the third input area). So, abc is known. So, a = (abc) / (bc) = (abc)/z. Because z is bc. Similarly, b= (abc)/y (assuming y is ac), c= (abc)/x (assuming x is ab). But again, the order of the input areas x, y, z can be any permutation of ab, ac, bc.

So, the approach would be:

Compute abc as sqrt(x*y*z).

Then, compute the three possible variables as (abc)/x, (abc)/y, (abc)/z.

But these three variables are bc, ac, ab. Because:

If x is ab, then (abc)/x = (abc)/(ab) = c.

If y is ac, then (abc)/y = b.

If z is bc, then (abc)/z = a.

So, the three variables (abc)/x, (abc)/y, (abc)/z are c, b, a. So, they are the variables in a different order.

Wait, but how can this be used to find a, b, c?

Let me see. For example, in the case where input is 6,8,12.

abc is 24.

24/6 =4 (c), 24/8=3 (b), 24/12=2 (a). So the three values are 4,3,2. Which are c, b, a. So the variables are a=2, b=3, c=4. So the correct variables are in the reverse order.

So, the three values (abc/x, abc/y, abc/z) are c, b, a. So, to get a, b, c, we need to take those three values and reverse them. Because in the example, the three values are 4,3,2, and the variables are 2,3,4. So the variables a, b, c are 2,3,4, which is the reverse of the list 4,3,2.

But how can I know that the order is reversed? Because the variables abc/x is c, abc/y is b, abc/z is a, assuming x is ab, y is ac, z is bc. So in that case, the list would be c, b, a. To get a, b, c, you reverse the list.

So, perhaps the correct variables a, b, c are (abc/z, abc/y, abc/x), which would be a, b, c. Because:

abc/z = (abc)/(bc) = a.

abc/y = (abc)/(ac) = b.

abc/x = (abc)/(ab) = c.

So, in this case, the variables are abc divided by z, y, x in that order.

But how to compute that when the order of x, y, z is unknown.

Ah, but the problem states that the input is guaranteed to have a solution. So for any input x, y, z (as the three face areas), there exists a permutation of abc/x, abc/y, abc/z that gives the variables a, b, c such that their pairwise products are the three input areas.

So, perhaps the correct approach is to compute all three possible values (abc/x, abc/y, abc/z), then check which permutation of these gives the correct pairwise products.

But how?

Alternatively, the variables a, b, c must be the square roots of (abc/x), (abc/y), (abc/z). Wait, because:

If abc = sqrt(x y z), then (abc/x) = sqrt( (y z) / x ). Hmm, not sure.

Alternatively, perhaps the variables a, b, c are sqrt( (x*y)/z ), sqrt( (x*z)/y ), sqrt( (y*z)/x ), but this is only valid if x, y, z are in the order ab, ac, bc.

But when they are in a different order, this approach gives incorrect values.

So perhaps the correct approach is to compute all possible permutations of the three input values, compute a, b, c for each permutation using the formula, and see which one satisfies the condition that their pairwise products are the input areas.

But since the problem says that there's exactly one solution, we can pick any permutation, compute a, b, c, and check if the pairwise products are the input values. Once found, return the sum.

But since the input can be up to 1e4, this approach could be feasible.

But in code, how can I do this?

Let's see. For example, given the input areas s1, s2, s3, I can generate all possible permutations of the three as x, y, z (there are 6 permutations), and for each permutation, compute a = sqrt( (x*y)/z ), b = sqrt( (x*z)/y ), c = sqrt( (y*z)/x ), then check if the pairwise products ab, ac, bc match the input set. Once found, return the sum.

But for example, in the case where the input is 6, 8, 12, the correct permutation is x=ab=6, y=ac=8, z=bc=12. Then:

a= sqrt( (6*8)/12 ) = sqrt(48/12) = 2.

b= sqrt( (6*12)/8 ) = sqrt(72/8) = sqrt(9) =3.

c= sqrt( (8*12)/6 )= sqrt(96/6) = 4.

Then, ab=6, ac=8, bc=12. Which matches the inputs. So this permutation works.

For other permutations, like x=8, y=6, z=12:

a= sqrt( (8*6)/12 ) = sqrt(48/12)=2.

b= sqrt( (8*12)/6 )= sqrt(16)=4.

c= sqrt( (6*12)/8 )= sqrt(72/8)=sqrt(9) =3.

Then, ab=2*4=8, which is x. But in the input, the areas are 6,8,12. So ab=8, which is in the input. But ac=2*3=6, which is in the input. bc=4*3=12. So the pairwise products are 8,6,12. Which is a permutation of the input. So the sum would still be (2+4+3)*4=9*4=36, but the correct answer is 2+3+4=9*4=36. Wait, but in the original example, the sum is (2+3+4)*4=9*4=36. But the correct answer for the input 6,8,12 is 28. Wait, no, the input 4 6 6 gives 28, but in this example, the input is 6,8,12. Let's see.

Wait, in the example where the input is 6,8,12, the variables would be a=2, b=3, c=4. Sum is (2+3+4)*4= 9*4=36. But the example with input 4 6 6 has a sum of 28. So in this case, the sum is 36. So if the code uses this approach, then for some permutations, the code might generate variables that don't match the input. But the problem says that it's guaranteed that there's exactly one possible solution. So perhaps the code needs to try all permutations until the correct one is found.

But given that there are only 6 permutations, this is manageable.

So the steps are:

1. Read the three input numbers s1, s2, s3.

2. Generate all possible permutations of these three numbers.

3. For each permutation (x, y, z):

   a. Compute a = sqrt( (x*y)/z )

   b. Compute b = sqrt( (x*z)/y )

   c. Compute c = sqrt( (y*z)/x )

   d. Check if the pairwise products ab, ac, bc are exactly x, y, z. (Since x, y, z is a permutation of ab, ac, bc, but we need to check if they are the same as the permutation chosen.)

   Wait, no. Because the variables a, b, c computed using a permutation (x, y, z) must result in ab = x, ac = y, bc = z. Otherwise, the permutation is invalid.

   So for the current permutation x, y, z, compute a, b, c as above, then check if ab == x, ac == y, bc == z.

   If so, then return the sum 4*(a + b + c).

4. Since the problem says that there is at least one solution, once a permutation is found that satisfies the conditions, return the sum.

So, in code, this can be done as follows:

Iterate through all permutations of the three input numbers, compute a, b, c for each permutation, check if ab, ac, bc match the permutation's x, y, z. If yes, return the sum.

But permutations of the input may have duplicates. For example, if two input numbers are the same, like in the first example (1,1,1), all permutations are the same. So in that case, the code would generate the same a, b, c for each permutation.

So this approach would work.

But in Python, how to generate all permutations?

We can use itertools.permutations, which generates all possible orderings. So for the list [s1, s2, s3], generate all possible permutations (each permutation is a tuple of the three elements in some order), then for each, compute a, b, c and check.

But since the product of x*y must be divisible by z, and similarly for the other terms, we need to ensure that the divisions under the square roots result in perfect squares. However, the problem statement guarantees that at least one solution exists. So for the correct permutation, these terms will be perfect squares.

So, code steps:

- Read the three input integers into a list.

- For each permutation of the list:

   - x, y, z = permutation[0], permutation[1], permutation[2]

   - compute a_sq = (x*y)/z → check if this is a perfect square. Because a must be an integer (since the problem says edge lengths are integers). But according to the problem statement, it's guaranteed that the input comes from a valid parallelepiped. So for the correct permutation, (x*y)/z must be a perfect square.

   - similarly for (x*z)/y and (y*z)/x.

But perhaps in code, even if the permutation is incorrect, (x*y)/z might not be a perfect square, but for the correct permutation, it will be.

So for each permutation:

Check if (x*y) is divisible by z, (x*z) divisible by y, (y*z) divisible by x.

Then compute a, b, c as the integer square roots of those.

Then check if ab ==x, ac == y, bc == z.

If all conditions are met, return the sum.

But this can be done in code.

But in code, we can do the following:

import math

for perm in permutations(s_list):

    x, y, z = perm

    product_xy = x * y

    if product_xy % z !=0:

        continue

    a_sq = product_xy // z

    a = int(math.isqrt(a_sq))

    if a * a != a_sq:

        continue

    product_xz = x * z

    if product_xz % y !=0:

        continue

    b_sq = product_xz // y

    b = int(math.isqrt(b_sq))

    if b*b != b_sq:

        continue

    product_yz = y * z

    if product_yz % x !=0:

        continue

    c_sq = product_yz // x

    c = int(math.isqrt(c_sq))

    if c*c != c_sq:

        continue

    # Now check if ab ==x, ac ==y, bc == z.

    if a*b == x and a*c == y and b*c == z:

        total =4*(a + b + c)

        print(total)

        exit()

But this code may work. Let's test with the sample inputs.

Sample input 1: 1 1 1.

All permutations are the same. x=1, y=1, z=1.

product_xy =1, product_xy//z=1. a=1. Similarly for b and c. Then check 1*1=1, 1*1=1, 1*1=1. Correct. Sum is 4*3=12.

Sample input 2:4 6 6.

Possible permutations include (4,6,6). Let's see:

x=4, y=6, z=6.

product_xy=24, divided by z=6 →24/6=4. a_sq=4. a=2.

product_xz=4*6=24, divided by y=6 →24/6=4. b=2.

product_yz=6*6=36, divided by x=4 →36/4=9. c_sq=9 → c=3.

Check ab=2*2=4 ==x? yes. ac=2*3=6 ==y? yes. bc=2*3=6 ==z? yes. So sum is 4*(2+2+3)=4*7=28. Correct.

Another permutation: (6,4,6). Let's see:

x=6, y=4, z=6.

product_xy=24. z=6 →24/6=4. a=2.

product_xz=6*6=36 /4 →9. b_sq=9 →b=3. product_yz=4*6=24 /6=4 →c_sq=4 →c=2.

Check ab=2*3=6 ==x=6 → yes. ac=2*2=4 ==y=4 →yes. bc=3*2=6 ==z=6 → yes. So variables a=2, b=3, c=2. Sum is (2+3+2)*4=7*4=28. But this sum is same as before. But wait, but the variables would be a=2, b=3, c=2. Then the three areas are ab=6, ac=4, bc=6. Which matches the input permutation (6,4,6). But the sum is (2+3+2) *4=28, which is correct.

So regardless of the permutation, the code finds a valid solution and returns the correct sum.

Another example with input 6,8,12. The correct permutation is 6,8,12.

x=6, y=8, z=12.

product_xy=48, divided by z=12 →48/12=4. a=2.

product_xz=6*12=72 /8=9 →b=3.

product_yz=8*12=96 /6=16 →c=4.

Check ab=6, ac=8, bc=12. Correct. Sum 4*(2+3+4)=36.

So this code would work.

But generating all permutations may not be the most efficient, but given that there are only 6 permutations, it's acceptable.

But in Python, the itertools.permutations function can generate all possible permutations, but for a list with duplicates (like when two inputs are the same), it will generate duplicate permutations. However, in the code above, once a valid permutation is found, the code returns immediately, so duplicates are not a problem.

Thus, the code should work.

Now, how to handle floating point operations? Since all divisions must result in integer values, the code uses integer division and checks if the product is divisible by the denominator. This avoids floating point inaccuracies.

Another optimization: The code can compute a, b, c for each permutation and check if the variables are integers and the products match.

Thus, the code should work correctly.
</think>

To solve this problem, we need to determine the sum of all 12 edges of a rectangular parallelepiped given the areas of its three adjacent faces. The key insight is to derive the edge lengths from the given areas and then compute the sum of these edges efficiently.

### Approach
1. **Problem Analysis**: The given areas are the products of the pairs of edge lengths (a, b, c) of the parallelepiped. The sum of all edges can be derived once we find the individual edge lengths.
2. **Mathematical Insight**: The product of the three given areas equals \((a \cdot b \cdot c)^2\). Taking the square root of this product gives us the product of the edge lengths \(abc\). Using this, we can derive each edge length by dividing \(abc\) by each of the given areas and taking the square root.
3. **Permutations Check**: Since the given areas can be in any order, we check all permutations of the input areas to find the correct edge lengths. This ensures that we handle any valid input configuration.

### Solution Code
```python
import math
from itertools import permutations

s = list(map(int, input().split()))

for perm in permutations(s):
    x, y, z = perm
    product_xy = x * y
    if product_xy % z != 0:
        continue
    a_sq = product_xy // z
    a = math.isqrt(a_sq)
    if a * a != a_sq:
        continue
    
    product_xz = x * z
    if product_xz % y != 0:
        continue
    b_sq = product_xz // y
    b = math.isqrt(b_sq)
    if b * b != b_sq:
        continue
    
    product_yz = y * z
    if product_yz % x != 0:
        continue
    c_sq = product_yz // x
    c = math.isqrt(c_sq)
    if c * c != c_sq:
        continue
    
    if a * b == x and a * c == y and b * c == z:
        total = 4 * (a + b + c)
        print(total)
        break
```

### Explanation
1. **Reading Input**: The input consists of three integers representing the areas of the three adjacent faces.
2. **Generating Permutations**: We generate all permutations of the input areas to account for any possible order of the given areas.
3. **Edge Length Calculation**: For each permutation, we check if the derived values for edges a, b, and c are integers and if their products match the given areas. This involves checking divisibility and perfect square conditions to ensure valid edge lengths.
4. **Sum Calculation**: Once valid edge lengths are found, the sum of all edges is computed as \(4 \times (a + b + c)\) and printed.

This approach efficiently checks all possible permutations and ensures the correct edge lengths are found using integer arithmetic, avoiding floating-point inaccuracies. The solution is optimized to handle the maximum input constraints within the given time and memory limits.