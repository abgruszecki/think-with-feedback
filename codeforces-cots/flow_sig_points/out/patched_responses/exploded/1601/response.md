<think>
Okay, let's see. So the problem is about determining the color of a point (x, y) on this magic clock. The colors are arranged in a certain pattern, and points on the borders (which are when the distance from the origin is an integer) are considered black. So, the task is to figure out whether the given point is black, white, or on the border, which automatically makes it black.

First, I need to understand how the colors are determined. From the example given, like the first input is (-2, 1) and the output is white. The second example (2,1) is black. Hmm. Wait, maybe the colors alternate in rings. Like, each ring is a circle of radius r, and between r and r+1. Then, the color depends on the ring. But maybe the rings alternate between black and white, but how exactly?

Looking at the examples: 

In the first example, (-2, 1) has a distance squared of (-2)^2 +1^2 = 4+1=5. So the distance is sqrt(5) ≈ 2.236. So between 2 and 3. So the point is in the ring between 2 and 3. But the example output is white. So how is the color determined?

Another example: (4,3) has distance 5, which is exactly an integer, so it's on the border. So output is black. That's straightforward.

The second example (2,1) has distance sqrt(5) as well. Wait, but why is the output black? Wait, maybe I made a mistake here. Let me recheck. Wait, (2,1): x is 2, y is 1. The distance squared is 4 +1=5. So the distance is sqrt(5) ~2.236. So between 2 and 3. So why is the output black here? But the first example's output is white. Oh, wait, that's conflicting. So maybe the color depends on the ring's parity and the angle.

Wait, maybe the coloring is similar to a checkerboard, but in polar coordinates. Like, the color alternates between black and white in each ring, and also alternates in sectors. For example, each ring is divided into 8 sectors (45 degrees each), and the color alternates in each ring and sector. But how exactly?

Alternatively, maybe the color is determined by the parity of the integer part of the distance squared. Wait, perhaps the key is to compute the floor of the distance (the integer part), and then check if it's even or odd. But let's see the examples.

First example: distance is sqrt(5) ≈ 2.236. The floor is 2, which is even. So the color would be white? But in the example, it is white. Second example (2,1) is the same distance. So why the output is black here? That contradicts. So this approach can't be right.

Wait, maybe the color depends on the parity of the ring (the integer part of the distance) and the parity of the sector (like which octant the point is in). Because in the first example, the point is in (-2, 1), which is in a different quadrant than (2,1). But the problem says that the coloring extends naturally to infinity. Hmm, perhaps the coloring alternates between black and white in each ring (like, even rings are white, odd are black, or vice versa), but also alternates per sector. So maybe each ring is divided into 8 parts (45 degrees each), and each part alternates color.

Wait, perhaps the color is determined by the number of the ring (floor of the distance) and the angle. For example, if the ring is even, and the sector is even (like, which 45-degree segment it's in), then it's white, else black, but I'm not sure.

Alternatively, maybe the color is determined by the parity of the ring number (the integer part of the distance) plus the parity of the sector. For instance, if the sum is even, then it's white, else black, or something like that.

Alternatively, maybe the color is white if the integer part of the distance is even, but only in certain quadrants. But how to reconcile the examples.

Wait, let's look at the first example: (-2,1). The coordinates here are in the second quadrant. The second example is (2,1) in the first quadrant. But their outputs are white and black, respectively. So the quadrant must matter. So perhaps the color depends on both the ring (integer part of distance) and the angle. But how?

Another approach: Let's think of the pattern as a checkerboard extended radially. For example, each ring (between n and n+1) is divided into 8n segments (like 8 sectors per ring?), but that might complicate things.

Alternatively, perhaps the color is determined by whether the integer part of the distance squared is even or odd. Because the distance squared is x² + y². Let's compute that.

First example: x² + y² is 4 + 1 =5. The integer part is 5. 5 is odd. So maybe the color is white if the integer part is even. But 5 is odd, so output would be black, but the first example outputs white. So that's not matching.

Alternatively, maybe the color is determined by whether the floor of the distance (the integer part) is even or odd. So for the first example, the floor is 2 (since sqrt(5) is ~2.236), which is even. So the color would be white. That matches the first example. The second example's floor is also 2, but output is black. So that doesn't fit.

Hmm, this suggests that the color depends on more than just the ring. So perhaps the angle plays a role. For example, the color alternates in each octant of each ring.

Wait, maybe the color is determined by the parity of the sum of the integer part of the distance and the octant number. Let's think. Each ring is divided into 8 octants (45 degrees each). For a given point (x,y), we compute which octant it's in. Then, if (ring + octant) is even, it's white, else black.

But how to compute the octant. Let's see. The octant can be determined based on the angle of the point. For example, in 45-degree increments. Alternatively, by comparing the absolute values of x and y, and the signs.

Let's take the first example (-2,1). The angle is in the second quadrant. Let's compute the angle. The coordinates are (-2,1). So the angle is arctan(1/-2) which is in the second quadrant, so around 153 degrees. Which octant is that? The octants are 0-45, 45-90, 90-135, etc. So 135 to 180 is the fourth octant in the second quadrant. Wait, maybe the octants are numbered 0-7 starting from the positive x-axis, going counter-clockwise. So each octant is 45 degrees. For example:

Octant 0: 0-45 degrees (x > 0, y >= 0, and y <= x)
Octant 1: 45-90 degrees (x >0, y >0, y >x)
Octant 2: 90-135 (x <0, y >0, |y| > |x|)
Wait, maybe that's getting complicated. Alternatively, for a point (x,y), the octant can be determined by the following steps:

1. Determine the quadrant (based on the signs of x and y).
2. Compute the slope (y/x) within that quadrant to determine the octant.

But perhaps there's a simpler way to compute the octant number. For example, using the atan2 function, but that might not be necessary. Alternatively, for a point (x, y), if we compute the ratio of y to x (or x to y, depending on which is larger in magnitude), we can determine which octant it's in.

Alternatively, the octant can be determined by checking which of the following conditions hold (assuming x and y are not zero):

- The point is in the first quadrant (x >=0, y >=0):

   If y <= x: octant 0 (0-45 degrees)
   Else: octant 1 (45-90 degrees)

- Second quadrant (x <0, y >=0):

   If y < -x: octant 2 (90-135 degrees)
   Else: octant 3 (135-180 degrees)

- Third quadrant (x <0, y <0):

   If -y <= -x: octant 4 (180-225)
   Else: octant 5 (225-270)

- Fourth quadrant (x >=0, y <0):

   If -y < x: octant 6 (270-315)
   Else: octant 7 (315-360)

But maybe there's a better way. For example, using the maximum of |x| and |y|, and the signs. Let's think.

For example, in the first quadrant (x,y >=0):

If x >= y: octant 0 (0-45)
Else: octant 1 (45-90)

In the second quadrant (x <0, y >=0):

If |x| > y: octant 2 (90-135)
Else: octant 3 (135-180)

Third quadrant (x <0, y <0):

If |x| >= |y|: octant 4 (180-225)
Else: octant5 (225-270)

Fourth quadrant (x >=0, y <0):

If x >= |y|: octant6 (270-315)
Else: octant7 (315-360)

But perhaps this can be computed algorithmically.

Once the octant is determined, and the ring (floor of the distance), then the color is determined by (ring + octant) mod 2.

But how do the examples fit into this?

First example: (-2,1) in second quadrant.

Compute |x| is 2, y is 1. Since |x| (2) > y (1), so octant is 2 (assuming the above approach). Ring is floor(sqrt(5)) = 2. So sum is 2+2=4, which is even. So color is white. Which matches the first example.

Second example: (2,1). First quadrant. x=2 >= y=1. So octant 0. Ring is 2. Sum is 2+0=2, even. So color is white. But the example output is black. So that contradicts. Hmm, so this approach isn't correct.

Wait, maybe the ring is computed as floor(distance) where distance is sqrt(x² + y²). So for the second example, the distance is sqrt(5) ~2.236, floor is 2. Sum 2+0=2, even, so color white. But the sample output is black. So that's not matching. So this approach is wrong.

Hmm. So perhaps the color determination is different.

Another idea: perhaps the color alternates in a checkerboard pattern, where each square is a ring and a certain angle. But how?

Alternatively, the color is determined by the parity of the number of the ring (floor of the distance) plus the parity of the number of the octant.

Wait, in the first example, ring is 2 (even), octant 2 (even). Sum even + even = even → white. Which matches.

Second example: ring 2 (even), octant 0 (even). Sum even → white, but sample output is black. So that's not matching. So this approach is wrong.

So maybe the octant is counted differently, or the ring is counted from 1 instead of 0.

Wait, perhaps the ring is considered as the integer part of the distance, but starting from 0. For example:

If the distance is between n and n+1 (for integer n), then the ring is n.

So for sqrt(5) ~2.236, ring is 2.

Then, the color is determined by (ring + octant) mod 2. But in the first example, that gives even, white. Second example: octant 0, sum 2+0=2 mod 2 is 0 → white, but sample output is black. So that's not matching.

Hmm. So this approach is incorrect.

Alternative approach: Let's look for the pattern in the examples.

First example: (-2,1). The output is white. The ring is 2. The octant is 2 (as per earlier reasoning). So maybe (ring + octant) is even → white.

Second example: (2,1) → octant 0. 2+0=2 even → white, but output is black. So that's conflicting.

Hmm. So perhaps the octant is being added to the ring, but the parity is opposite. Like, if (ring + octant) is even → black, odd → white. But then for the first example, 2+2=4 even → black. But the output is white. So no.

Alternatively, perhaps the ring is the integer part of the distance squared. Wait, distance squared is x² + y². Let's compute for the first example: 4+1=5. So the ring would be 5. If we take the ring as the distance squared, then for (2,1), it's also 5. So ring 5.

Then, the octant for first example is 2. 5+2=7. 7 mod 2 is 1 → white. Second example: same ring 5, octant 0. 5+0=5 mod 2 is 1 → white. But sample output is black. So that's not matching.

Hmm. So perhaps the color is determined in a different way. Let's think again.

The problem statement says that the coloring extends naturally. The example image probably shows a pattern where each ring is divided into 8 regions (like octants), and each region alternates color. But how to model that.

Alternatively, the color alternates per ring. For even rings (0, 2, 4), the color starts with white, and alternates per octant. For odd rings (1,3,5), the color starts with black, and alternates per octant. Or something like that.

But how to model this.

Let me think. Suppose each ring is split into 8 segments (octants). For each ring, the first octant is a certain color, then alternates. But the starting color depends on the ring's parity. For even rings (ring 0,2,4...), the first octant is white, then alternates. For odd rings (1,3,5...), the first octant is black, then alternates. So, in ring 0 (distance 0-1), the first octant is white, next black, etc. Then, for ring 1 (1-2), first octant is black, then white, etc. So for each octant in a ring, the color is determined by (octant number + ring) mod 2.

Wait, but octant numbers are 0-7, and for each ring, the color depends on (octant + ring) mod 2. So for ring 2, octant 0: (2+0) mod 2 =0 → white. Octant 1: 2+1=3 mod2=1 → black. Then in the first example, (-2,1) is in ring 2, octant 2. 2+2=4 mod2=0 → white. Which matches the first example. The second example (2,1) is in ring 2, octant 0. 2+0=2 mod2=0 → white, but sample output is black. So this approach is invalid.

Hmm. So this suggests that perhaps the octant is calculated differently, or the ring is calculated differently.

Alternatively, maybe the ring is the floor of the distance, but the octant is calculated as the angle divided by 45 degrees, but starting from a different direction.

Alternatively, perhaps the color is determined by whether the number of the ring is even or odd, and the octant number is even or odd. For example, if ring is even and octant is even → white. Or maybe ring and octant parities are XORed. So, if (ring_parity XOR octant_parity) is 0, then white; else black.

Let's test the first example:

Ring is 2 → even (parity 0). Octant 2 → even (parity 0). XOR is 0 → white. Correct.

Second example: ring 2 (even), octant 0 (even). XOR is 0 → white. But sample output is black. So this approach is wrong.

So perhaps the octant number is calculated differently. Let's re-examine how octants are numbered.

Maybe the octant numbering is such that it alternates the starting direction. For example, octant 0 is 0-45, octant 1 is 45-90, etc., but in a way that the even octants are in even directions (0, 90, 180, 270), and the odd are in between. Or perhaps the octant numbering is such that even octants are in even positions, leading to a checkerboard pattern.

Alternatively, the octant numbers are determined in such a way that for adjacent octants, the parity alternates. For example, octant 0 is even, 1 is odd, 2 even, etc. Then, the parity of the octant would be its number mod 2.

In the first example, octant 2 → even. Ring 2 even. So (even + even) mod 2 → 0 → white.

Second example, octant 0 even. Ring 2 even → 0 → white. But sample output is black. So again, this approach is incorrect.

Hmm. Let's look for other patterns. The third example is (4,3) → distance 5.0. So it's on the border, so output is black.

Another test case: (0,0) → distance 0 → black.

So, perhaps we need to find first whether the point is on a border (distance is integer). If yes, output is black. Otherwise, compute the color based on the ring and octant.

So the steps are:

1. Compute the distance squared (x² + y²). Take the square root. If the square root is integer, output black.

Else:

2. Compute the ring (floor of the distance).

3. Compute the octant.

4. Determine the color based on the ring and octant.

But the problem is to find how the ring and octant determine the color.

Let me think of another way. Maybe the color depends on the parity of the number of the ring and the parity of the octant. For example, if both are even or both are odd, then white; else black. But again, how to get the examples to fit.

Alternatively, the color is white if the sum of the ring and octant is even, else black.

First example: ring 2, octant 2 → 4 → even → white. Correct.

Second example: ring 2, octant 0 → sum 2 → even → white. But sample output is black. So this is wrong.

So perhaps the octant is computed differently. Let's re-examine how the octant is determined.

In the first example, (-2,1):

The point is in the second quadrant. The absolute values are x=2, y=1.

In the second quadrant, the angle is 180 - arctan(y/|x|) = 180 - 26.565=153.435 degrees. Divided into 45-degree segments. 135 to 180 is the third segment in the second quadrant. So octant is 3?

Wait, maybe the octants are numbered from 0 to 7 as follows:

0: 0-45 degrees (first quadrant, x >= y)

1: 45-90 (first quadrant, y > x)

2: 90-135 (second quadrant, y > |x|)

3: 135-180 (second quadrant, |x| >= y)

4: 180-225 (third quadrant, |x| >= |y|)

5: 225-270 (third quadrant, |y| > |x|)

6: 270-315 (fourth quadrant, |y| > x)

7: 315-360 (fourth quadrant, x >= |y|)

So for the first example (-2,1):

x is negative, y is positive. So in second quadrant. |x|=2, y=1. Since |x| > y, it's in the 135-180 range, which is octant 3.

In the second example (2,1): first quadrant. x=2, y=1. Since x>y, it's octant 0.

So for the first example, octant 3. Ring is 2. Sum 3 +2=5 → odd. So color is black? But sample output is white. Hmm.

But first sample's output is white. So this approach is not working.

Alternatively, maybe the octant is counted as 0 to 7, but the way it's calculated is different. For example, for the first example, maybe it's in octant 2.

Alternatively, maybe the octant is determined by the following steps:

Compute the angle theta in degrees, then divided by 45. Take the integer part. So theta ranges from 0 to 360, divide by 45, gives 8 values (0-7), but perhaps shifted.

For example, theta = 153.43 degrees. Divided by 45 gives 3.409, so integer part is 3. So octant 3.

But sum with ring 2 gives 3+2=5 mod2=1 → black, but first example's output is white.

So this approach doesn't fit.

Alternative approach: Let's think of the problem differently. The sample input (-2,1) gives white. The point is in the second quadrant, but why? Maybe the color depends on the parity of the ring and the parity of the number of the sector in that ring.

Wait, each ring is divided into 8 sectors. For example, ring 0 (distance 0-1) has 8 sectors. Ring 1 (1-2) has 8 sectors, but perhaps rotated. So for ring 0, sectors are 0-7. For ring 1, sectors start from 0, but each even ring's sectors are aligned the same way, and odd rings' sectors are offset by 45/2 degrees, leading to a checkerboard pattern.

But this is getting complicated.

Alternatively, perhaps the color is determined by the parity of the sum of the ring and the octant. But for the first example, sum is 2 (ring) + 3 (octant) =5 → odd. So color is black. But sample output is white. So this is not correct.

Hmm. I'm stuck. Let's think of another way.

Looking for patterns in the sample inputs:

First sample: (-2,1) → white. Distance squared is 5. So not on the border.

Second sample: (2,1) → distance squared same 5 → output is black. So two points in the same ring, same distance squared, but different colors. So the color can't be determined by ring or distance squared alone. The angle must be a factor.

So the color depends on both the ring and the angle. But how?

Another observation: in the first example, the point is (-2,1). The sum of absolute x and y is 2 +1 =3, which is odd. Maybe that's a clue. Second example (2,1) sum is 3, same. But output differs. So that's not it.

Alternatively, the product of x and y. For first example: (-2)*1 =-2. Even. Second example: 2*1=2, even. So that doesn't help.

Alternatively, check if x and y are even or odd. But in the examples, both x and y are even/odd. First example x is even, y is odd. Second example x even, y odd. But outputs differ. So no.

Hmm. Let's think of the first example and second example. Both have the same distance and ring. The only difference is their x coordinate's sign. So the parity of the x coordinate's sign might affect the color.

But how?

Wait, the first example's x is negative, y positive. The second's x is positive, y positive. So their positions are mirrored across the y-axis. So the color depends on which quadrant or octant the point is in.

But how does that affect the color?

Maybe the color alternates between octants. So each octant is either white or black, and the pattern repeats every two octants. For example, octant 0 is white, 1 is black, 2 is white, etc. But then the first example's octant (3) would be black. But the output is white.

Alternatively, the octant's parity (even or odd) determines the color. So even octants are white, odd are black. For first example, octant 3 (odd) → black, but sample output is white. So that's not matching.

Hmm. Let's think again of the first sample and the second sample.

In the first sample, the point is in octant 3 (assuming the previous way), and the second sample is in octant 0. So maybe the octant's parity (0 even, 3 odd) affects the color. But in first sample, ring is even (2), octant is 3 (odd). Sum 2 +3=5 (odd). So color is black. But sample output is white. So that's not.

Alternatively, perhaps the color is determined by (ring + octant) mod 2. For first sample: 2+3=5 mod2=1 → black. But sample is white. So no.

Alternatively, perhaps the color is determined by (ring + octant) mod 2. If the result is even, then white; else black. Wait, 2+3=5 mod2=1 → black, but sample is white. So that's not.

Hmm.

Alternative idea: Perhaps the color depends on the parity of the ring and the parity of the sum of the x and y coordinates.

But for the first example, x=-2 (even), y=1 (odd). Sum is -1 → odd. Ring 2 even. Even + odd is odd → color black. But sample output is white. So no.

Alternatively, product of x and y. For first example, product is -2 (even). For second example, product is 2 (even). Both even, but outputs differ. So no.

Alternative approach: Let's think of the pattern as a chessboard. The chessboard pattern is such that adjacent squares (in 8 directions) have opposite colors. In this problem, the 'squares' are rings and sectors. So for each ring and sector, the color alternates. So for example, the first ring (0-1) is divided into 8 sectors, each 45 degrees. The color starts with white in the first sector, then black, white, etc. Then the next ring (1-2) is divided into 8 sectors, but the starting color is the opposite of the previous ring's starting color. So each ring alternates the starting color.

In that case, for the first ring (0-1), sectors 0 is white, 1 black, ..., 7 black. Then ring 1 (1-2) sectors start with black, then white, etc. Ring 2 (2-3) starts with white again, and so on.

So for a given ring and octant, the color is determined by (ring mod 2) XOR (octant mod 2). If the result is 0 → white, else → black.

Let's test this:

First example: ring 2 → 0 mod2=0. octant 3 → 1 mod2=1. XOR → 1 → black. But sample output is white. So no.

Wait, but how is the octant determined here? Let's say octant 3 mod2 is 1. So 0 XOR1 is 1 → black. But sample says white. So this is not correct.

Hmm. Let's try different octant numbering.

In the first example, what if the octant is 2? Then 2 mod2=0. Ring 2 mod2=0. XOR 0 → white. That matches the sample.

So perhaps the octant for (-2,1) is 2.

How to determine that?

Let's re-examine the octant calculation. For point (-2,1), which is in the second quadrant.

The absolute values are x=2, y=1. So |x| > |y|. So in the second quadrant, when |x| > |y|, the angle is between 135 and 180 degrees. So in the octant between 135 and 180, which is octant 3? Or perhaps octant 2?

Wait, if the octants are numbered 0-7 as follows:

0: 0-45 (x >=0, y >=0, y <=x)
1: 45-90 (x >=0, y >=0, y >x)
2: 90-135 (x <=0, y >=0, |y| > |x|)
3: 135-180 (x <=0, y >=0, |x| >= |y|)
4: 180-225 (x <=0, y <=0, |x| >= |y|)
5: 225-270 (x <=0, y <=0, |y| > |x|)
6: 270-315 (x >=0, y <=0, |y| > |x|)
7: 315-360 (x >=0, y <=0, |x| >= |y|)

In this case, for the point (-2,1), x is negative, y positive. |x|=2>1= y. So this would fall into octant 3. But then, ring 2 mod2=0, octant 3 mod2=1. XOR is 1 → black, which contradicts the sample.

So perhaps this approach is incorrect.

Alternatively, maybe the octant is determined by the following steps:

Compute the angle theta in radians. Then, divide by pi/4 (45 degrees), take the integer part. That gives a number from 0 to 7 (since theta ranges from 0 to 2pi).

But for (-2,1), the angle is in the second quadrant. Let's compute the angle. The point is (-2, 1). The reference angle is arctan(1/2) ≈ 26.565 degrees. So the actual angle is 180 - 26.565 = 153.435 degrees. Divided by 45 degrees gives 3.409, so integer part is 3. So octant 3.

Ring is 2. So (3 + 2) mod2 =5 mod2=1 → black. But sample output is white.

Hmm. So no.

Alternative idea: perhaps the color is determined by the parity of the sum of the ring and the number of times the angle has passed 45-degree segments. For example, if the sum is even → white, else black.

But again, in the first sample, sum is 2+3=5 → odd → black. So not matching.

I'm stuck. Maybe there's another way to model this.

Wait, looking for the pattern in the samples:

The first sample is (-2,1) → white. Second is (2,1) → black. The only difference is the x-coordinate's sign. So perhaps the parity of the x and y coordinates plays a role.

For example, if x and y are both even or both odd, then one color, else the other. But (-2 is even, 1 is odd → sum is even + odd = even +1 → odd. So the sum is odd. Second example: 2 even, 1 odd → same sum. So same parity. But outputs differ. So this isn't the case.

Alternative approach: Let's look for some pattern.

In the first sample, the distance squared is 5. Which is between 2² and 3². So the ring is 2. So even.

The color is white. So even ring: white.

Second sample: same ring, same distance squared. But output is black. So the ring parity can't be the sole determinant.

So the angle must be playing a role. So perhaps the ring's parity and the angle's sector's parity (even or odd) are XORed.

For example, if the ring is even and the sector is even → white. If even and sector odd → black. If ring odd and sector even → black. If ring odd and sector odd → white.

But how to compute the sector's parity.

Let's consider the first sample's sector. If the sector is even, then even ring (2) → white. Which matches.

Second sample's sector is even (octant 0), even ring → white. But output is black. So this approach is wrong.

Hmm. Maybe the sector is considered even or odd based on a different criterion.

Another idea: the parity of the octant number. So if the octant number is even, the sector is even. So for first sample (octant 3, odd), even ring. So even XOR odd → odd → black. But sample output is white. So no.

This is frustrating. Maybe I should look for the correct way to determine the color.

Alternative approach: Let's look for the pattern in the samples.

In the first sample, (-2,1) → output white. Let's compute the distance squared (5) which is not a perfect square, so not on the border.

The ring is 2. So between 2 and 3.

Now, how to find the color. Maybe the color depends on whether the ring is even or odd and whether the point is in a black or white sector.

Wait, perhaps the color is white if the ring is even and the angle is in an even octant, or ring is odd and angle is in an odd octant. Otherwise, black.

But how to compute the octant.

Alternatively, perhaps the color is white if (floor of distance) is even and the point is in a white sector, or floor is odd and in a black sector. But how to define the sectors.

Alternatively, the problem's picture might show that the colors alternate every 45 degrees. So, starting from 0 degrees, the first 45 degrees is white, next 45 is black, next white, etc. But each ring's starting color alternates. For example, ring 0 starts with white, ring 1 starts with black, ring 2 starts with white, and so on.

So for ring 2 (even), the first sector (0-45) is white, next black, etc. So for a point in the 135-180 degree sector (octant 3), which is the third sector of the ring, the color is white (sectors 0: white, 1: black, 2: white, 3: black). So in ring 2, octant 3 would be black, but first sample's output is white. So this is not matching.

Hmm.

Alternative idea: Perhaps the color is determined by whether the number of the ring is even or odd and the angle is in a certain range. For example, even rings have white in even octants, odd rings have white in odd octants.

But again, how to determine the octant.

This is getting too time-consuming. Perhaps I should look for a mathematical formula that can derive the color.

Let me think: the pattern is such that each ring is divided into 8 sectors (octants). The color of each sector in a ring alternates, starting with a certain color. The starting color alternates for each ring. For even rings, the first sector is white; for odd rings, it's black.

So for even rings:

Sectors 0: white, 1: black, 2: white, 3: black, etc.

For odd rings:

Sectors 0: black, 1: white, 2: black, etc.

So, the color for a given sector in a ring is:

if ring is even:

color = (sector % 2) == 0 → white

if ring is odd:

color = (sector %2) == 1 → white

Wait, no. For even rings, sector 0 is white (even), sector 1 black (odd), etc. So sector mod 2 == 0 → white.

For odd rings, sector 0 is black, sector 1 white, etc. So sector mod 2 ==1 → white.

So the color is white when (ring mod 2 + sector mod 2) is even.

Wait:

For even ring (0,2,4...):

if sector mod 2 is 0 → white.

So (0 + 0) mod 2=0 → white. (0 +1) mod 2=1 → black.

For odd ring (1,3,5...):

if sector mod 2 is 1 → white. (1+1 mod 2=0 → white; 1+0 mod 2=1 → black).

So the color is white when (ring + sector) mod 2 == 0.

Yes. So the color is determined by (ring + sector) mod 2 == 0 → white; else black.

Now, we need to compute the sector (octant) for a given point.

So the steps are:

1. Check if the point is on a border (distance is integer). If yes, output black.

2. Else, compute the ring (floor of distance).

3. Compute the sector (octant) of the point.

4. Compute (ring + sector) mod 2. If 0 → white, else black.

So the problem reduces to correctly determining the sector (octant) of the point.

So how to compute the sector.

The sector can be determined by dividing the angle into 45-degree intervals and checking which interval the point's angle falls into.

But how to compute the angle and find the sector.

An alternative approach is to use the coordinates (x, y) to determine the sector without explicitly computing the angle.

Let me think of the eight possible sectors:

Each sector is 45 degrees. The sectors can be determined by comparing the absolute values of x and y and the signs.

For example:

Sector 0: x >=0, y >=0, x >= y

Sector 1: x >=0, y >=0, y > x

Sector 2: x <=0, y >=0, |y| > |x|

Sector 3: x <=0, y >=0, |x| >= |y|

Sector 4: x <=0, y <=0, |x| >= |y|

Sector 5: x <=0, y <=0, |y| > |x|

Sector 6: x >=0, y <=0, |y| > |x|

Sector 7: x >=0, y <=0, x >= |y|

But how to convert this into code.

Alternatively, for a given point (x,y), compute the reference angle in the first quadrant (absolute values), then determine the sector based on the reference angle and the original quadrant.

But perhaps there's a smarter way.

Another approach: the sector is determined by the following steps:

1. Determine the quadrant (based on x and y signs).

2. Compute the reference angle (absolute values of x and y).

3. In the quadrant, determine whether the reference angle is in the first or second part of the quadrant (i.e., whether y > x or x > y for first quadrant).

Let me think of this in code.

For example, for a point (x,y):

if x == 0 and y ==0: sector is 0 (but this is the origin, which is a border case).

Else:

Compute the absolute values ax = abs(x), ay = abs(y).

We need to determine which sector the point is in.

Let's define the sectors as follows:

Sector 0: x >=0, y >=0, ax >= ay, y <=x.

Sector 1: x >=0, y >=0, ay > ax.

Sector 2: x <0, y >=0, ay > ax.

Sector 3: x <0, y >=0, ax >= ay.

Sector 4: x <0, y <0, ax >= ay.

Sector 5: x <0, y <0, ay > ax.

Sector 6: x >=0, y <0, ay > ax.

Sector 7: x >=0, y <0, ax >= ay.

So for each point (x,y), we can check the signs and the relation between ax and ay to determine the sector.

Let's test this with the examples.

First example: (-2,1). x is negative, y positive. So quadrant 2.

ax=2, ay=1. ax >= ay. So sector 3.

Second example: (2,1). x positive, y positive. ax=2, ay=1. ax >= ay. So sector 0.

Third example: (4,3). distance is 5, which is integer. So output black.

Now, for first example: sector 3.

Ring is floor(sqrt(5)) = 2.

So (2 +3) mod 2 =5 mod2=1 → black. But sample output is white. Contradicts. So this approach is not correct.

Hmm. So what's wrong here?

Wait, according to this logic, the first example's sector is 3. So (2+3) mod2=1 → black. But sample output is white. So this must be wrong.

But how?

So perhaps the sector numbering is different. Maybe the sectors are ordered in a different way.

Alternatively, maybe the sector is determined by dividing the angle into 45-degree increments, but starting from the positive x-axis and moving counter-clockwise.

For example, the sectors would be:

0: 0-45 degrees.

1:45-90.

2:90-135.

3:135-180.

4:180-225.

5:225-270.

6:270-315.

7:315-360.

So for a point in sector 3 (135-180 degrees), which is the case for (-2,1), the sector is 3.

Ring is 2. Sum is 2+3=5 mod2=1 → black. But sample output is white.

So again, this approach is incorrect.

But according to the sample, the correct output is white. So where is the mistake?

Ah! Maybe the sector is computed in a different way. Perhaps the sectors are numbered in a different order. For example, perhaps after sector 3 (135-180), comes sector 4 (180-225), which is part of the third quadrant.

Alternatively, perhaps the sector numbering is different. Let's try to find another way.

Wait, perhaps the sectors are numbered such that for even rings, the starting sector is aligned with the positive x-axis, and for odd rings, it's shifted by 22.5 degrees, creating a checkerboard pattern.

But this complicates things.

Alternatively, perhaps the color is determined by the following rule: the point is white if (ring + sector) is even, but sector is computed based on the angle divided by 45 degrees and rounded down.

But for the first example:

angle is 153 degrees. Divided by 45 is 3.4 → sector 3.

ring 2 → 2+3=5 → odd → black. But sample output is white.

Hmm. So again, this approach is invalid.

Wait, perhaps I'm missing something. Let's look for a hint in the problem statement.

The problem states: "All the points between which and the origin of coordinates the distance is integral-value are painted black."

Other points are either black or white based on the pattern.

So the key is to compute whether the point is on the border (distance is integer → black) or not. If not, compute the color based on ring and sector.

But how?

Perhaps I should look for a pattern based on the parity of the ring and the parity of the sector.

In the first sample, ring 2 even, sector 3 odd. Sum 5 → odd. So color is black. But sample output is white. So this approach is wrong.

Alternatively, maybe the sector is computed as (angle + 22.5) divided by 45 degrees, then floor. This would shift the sectors by 22.5 degrees, making the boundaries between sectors at 22.5, 67.5, etc.

For example, the first sector would be from -22.5 to 22.5 degrees.

So for a point at 153 degrees:

153 + 22.5 =175.5. Divided by 45 → 3.9 → floor is 3. Sector 3.

Ring 2 → 2+3=5 mod2=1 → black. Sample output is white. No.

This is not working.

Alternatively, perhaps the sector is determined by the integer part of the angle divided by 45 degrees, but the angle is measured from 0 to 360 degrees.

For example:

angle = 153.43 degrees → 153.43 /45 =3.409 → integer part is3 → sector3.

Ring 2 → sum 5 → black. Sample output white. So no.

Hmm. I'm really stuck here. Maybe I should look for a different approach.

Alternative idea: Let's think about the chessboard pattern. Each cell is a square. But here, the pattern is radial. So perhaps each cell is a ring segment (annulus sector) between two radii and two angles.

In this case, the color of each cell would alternate between black and white. So the first ring (0-1) has 8 sectors, each 45 degrees. The color starts with white for sector 0, then black, white, etc. Then the next ring (1-2) has 8 sectors, but the starting color is opposite. So for ring 0, sector 0: white, sector 1: black, etc. For ring 1, sector 0: black, sector1: white, etc.

So for a given (ring, sector), the color is determined by (ring + sector) mod 2.

If this is the case, then for the first sample:

ring is 2 → even.

sector is 3 → 3 mod2=1.

sum 2+3=5 mod2=1 → black. But sample output is white. So this approach is not correct.

But sample output is white. So this approach must be wrong.

I must be missing something. Let's look for other examples.

For example, what if a point is (0,0.5). Distance is 0.5, so ring 0. The angle is 90 degrees. So sector 1 (45-90 degrees). So (0+1) mod2=1 → black.

Another example: (0.5, 0.5). Distance is ~0.707, ring 0. Angle 45 degrees. Sector 0. (0+0) mod2=0 → white.

But according to the chessboard pattern, perhaps the color is white for ring 0, sector 0.

But I don't have any examples to verify.

Another example: (3,0). Distance 3 → on the border → black.

(3.5,0) → distance 3.5 → ring 3. Sector 0 (0-45 degrees). Sum 3+0=3 → mod2=1 → black.

Hmm. But I'm not sure.

Perhaps the correct approach is to compute the octant based on the following method:

For a point (x,y), compute the slope = y/x, considering the signs.

The sectors can be determined by the following steps:

1. Compute the reference slope (absolute values of y and x).

2. Compare the slope to 1 and 0.

3. Determine which of the eight sectors the point falls into.

But how to code this.

Alternatively, here's a method to compute the sector:

Calculate the maximum of |x| and |y|. Then, based on which is larger and the signs, determine the sector.

For example:

If |x| >= |y|:

   if x >0:

      if y >=0 → sector 0.

      else → sector7.

   else:

      if y >=0 → sector3.

      else → sector4.

Else:

   if y >0:

      if x >=0 → sector1.

      else → sector2.

   else:

      if x >=0 → sector6.

      else → sector5.

Let's test this with the first example:

x=-2, y=1. |x|=2, |y|=1. So |x|>|y|. x is negative. y is positive. So sector3.

Ring 2. Sum 2+3=5 mod2=1 → black. Sample output is white. So this approach is wrong.

But sample output is white. So this approach is not correct.

I'm really stuck. Perhaps I should look for a correct algorithm.

Another idea: The problem's pattern is such that each square ring (like a square rotated 45 degrees) forms alternating colors. But this is a guess.

Alternatively, the color is determined by the parity of the sum of the integer parts of x and y.

For example, for (-2,1), sum is -2 +1 =-1 → odd. So white. Sample output is white. Second example (2,1) sum is 2+1=3 → odd. Sample output is black. So this approach is invalid.

Another idea: For a given point (x,y), the color is white if floor(d) is even and (x and y have the same sign), or floor(d) is odd and (x and y have different signs). Otherwise, black. But let's see.

First sample: floor(d)=2 (even). x is -2 (negative), y is 1 (positive) → different signs. So even + different signs → white? Not sure. But sample output is white. Second sample: x positive, y positive → same signs. floor(d)=2 even. So even + same signs → black. Which matches sample. Hmm, this could be a possible approach.

Let's see:

For even rings:

if x and y have the same sign → black.

else → white.

For odd rings:

if x and y have the same sign → white.

else → black.

Does this fit the samples?

First sample: even ring. x and y have different signs → white. Which matches.

Second sample: even ring. x and y have same signs → black. Which matches.

Third sample: (4,3) distance 5. On border → black.

Another test case: (0, 0.5) → ring 0. Even. x=0, y positive. Same signs? 0's sign is considered positive. So same → black.

Another test case: (1, 0.5). Ring 0. Same signs → black.

(0.5, 0.5) → ring 0. Same signs → black.

But according to this logic, the color for even rings and same signs is black. For different signs, white.

For odd rings, same signs → white.

Hmm. How to verify this.

Another test case: (1, 1). Distance is sqrt(2) ~1.414. Ring 1 (odd). x and y same signs → white. So output white.

Another test case: (1, -1). Ring 1 (odd). Different signs → black.

This seems to fit.

So the rule is:

If the distance is integer → black.

Else:

ring = floor(distance)

if ring is even:

   if x and y have the same sign → black.

   else → white.

if ring is odd:

   if x and y have the same sign → white.

   else → black.

This seems to fit the examples.

Let's check:

First example: (-2, 1). x is negative, y positive → different signs. Even ring (2) → white. Correct.

Second example: (2, 1). same signs → even ring (2) → black. Correct.

Third example: (4,3) → distance 5 → black. Correct.

Another example: (0, 0.5) → ring 0. same signs (0 is positive) → black.

(0.5, 0.5) → same signs → ring 0 even → black.

(3,4) → distance 5 → black.

(1.5, 1.5) → distance ~2.121. ring 2 (even). same signs → black.

(1.5, -1.5) → ring 2 (even). different signs → white.

This seems to work.

So the rule is:

Check if the distance is integer. If so, output black.

Else:

ring = floor(distance)

if ring is even:

   if x and y have the same sign (both positive, both negative, or one is zero), then black.

   else, white.

else (ring is odd):

   if x and y have the same sign → white.

   else → black.

Wait, but what about when x or y is zero? For example, (0, 1.5). x is zero, y positive → same sign. ring 1 (distance is 1.5). ring is odd. same signs → white.

Yes. So the rule holds.

This seems to fit all the examples and makes sense.

So the steps are:

1. Compute the distance squared = x² + y².

2. Compute the distance as sqrt(distance_squared). If distance is integer (i.e., distance_squared is a perfect square), output black.

3. Else:

   a. Compute the ring = floor(distance).

   b. Check if x and y have the same sign (including zero).

   c. If ring is even:

      i. Same sign → black.

      ii. Different signs → white.

   d. If ring is odd:

      i. Same sign → white.

      ii. Different signs → black.

This approach seems to fit all the examples.

Let's test the samples:

First sample: x=-2, y=1. Different signs. ring 2 even → output white. Correct.

Second sample: x=2, y=1. same signs. ring even → black. Correct.

Third sample: 4 and 3 → 25 → sqrt is 5 → integer. Output black. Correct.

Another test case: (1, -1). distance is sqrt(2) → ring 1 (odd). different signs → black. Which is correct.

Another test case: (3,4) → distance 5 → integer → black.

Another test case: (0, 0.5) → same signs (zero is considered positive). ring 0 even → black.

Another test case: (0, -0.5) → same signs (zero and negative: zero is considered positive? Or wait, x is 0, y is negative. What's the sign of x?

Wait, in this case, x is zero. The sign of zero can be considered as positive or negative based on the problem's handling. But according to the problem's examples, the point (-2,1) is in the second quadrant (x negative, y positive), and the color is white. So for x=0, y positive: same sign as x (zero's sign is positive) → same signs. So (0, 0.5) would be same signs → even ring → black.

But how to handle x=0 or y=0.

In programming terms, zero is considered to have a positive sign.

So, when x is zero, and y is positive, they are considered same signs. When x is zero and y is negative, same signs (since x is zero, which is considered positive, and y is negative → different signs).

Wait, no. If x is zero, its sign is considered as positive. So, if x is zero and y is positive → same signs (both positive). If x is zero and y is negative → different signs.

Similarly, if y is zero, x is positive → same signs. If y is zero and x is negative → different signs.

So the code needs to check:

if x and y are both zero → distance is zero, which is border → black.

Else:

same_sign = (x >=0 and y >=0) or (x <=0 and y <=0)

But wait, what about x positive and y negative: different signs. x negative and y positive: different signs. x zero and y positive: same. x zero and y negative: different.

So same_sign is true when x and y are both non-negative (including zero), or both non-positive (including zero).

Wait, no. For example, x=0, y=5: same_sign (both non-negative). x=0, y=-5: x is non-negative, y is negative → different.

x=5, y=0: same_sign (non-negative). x=-5, y=0: x is non-positive, y is non-negative → different.

Wait, no. If x is negative and y is zero, then x is non-positive, y is non-negative. So different signs.

So same_sign is true when:

(x >=0 and y >=0) OR (x <=0 and y <=0)

But that would include cases like x=5, y=0 (same_sign) and x=-5, y=0 (same_sign if y is zero and x is non-positive? No, because y is zero is considered non-negative.

Wait, this is getting confusing. Let's think:

same_sign = (x >=0 and y >=0) or (x <=0 and y <=0)

But this is not correct. For example, x=5, y=0 → yes (both non-negative). x=-5, y=0 → x is non-positive, y is non-negative → no. So same_sign is false.

So same_sign is true only if both are non-negative or both are non-positive.

But wait, in code:

same_sign = (x >= 0 and y >=0) or (x <=0 and y <=0)

But if x is zero and y is zero, it's included. For x=0 and y=5, same_sign is true. For x=0 and y=-5, same_sign is false.

Yes.

So in code, same_sign is true if both x and y are non-negative or both are non-positive.

So, let's test this with the sample:

First sample: x=-2, y=1. x is negative, y is positive → same_sign is false.

Second sample: x=2, y=1 → both positive → same_sign is true.

Third sample: x=4, y=3 → same_sign true. But output is black because distance is integer.

Another test case: x=0, y=5 → same_sign true.

x=0, y=-5 → same_sign false.

x=5, y=0 → same_sign true.

x=-5, y=0 → same_sign false.

So the code can compute same_sign as:

same_sign = (x >= 0 and y >= 0) or (x <= 0 and y <= 0)

Now, the code steps are:

1. Compute x and y.

2. Compute distance_squared = x*x + y*y.

3. Compute distance = sqrt(distance_squared).

4. If distance is integer (i.e., distance_squared is a perfect square and distance is integer), output 'black'.

5. Else:

   a. ring = floor(distance)

   b. same_sign = (x >=0 and y >=0) or (x <=0 and y <=0)

   c. if ring is even:

      i. if same_sign → black

      ii. else → white

   d. else (ring is odd):

      i. if same_sign → white

      ii. else → black

So this should work.

Now, the code needs to:

- Check if distance_squared is a perfect square. How to do that in Python.

We can compute the integer part of the square root and check if its square equals distance_squared.

For example:

sqrt_val = int(math.isqrt(distance_squared))

if sqrt_val * sqrt_val == distance_squared:

   output 'black'

else:

   compute ring and same_sign.

Yes.

So the code would look like:

Testing against sample input 1.

```python
import math


def main(input_stream, output_stream):
    x, y = map(int, input_stream.readline().rstrip("\n").split())

    distance_squared = x**2 + y**2

    sqrt_val = math.isqrt(distance_squared)

    if sqrt_val * sqrt_val == distance_squared:

        print("black", file=output_stream)

    else:

        distance = math.sqrt(distance_squared)

        ring = int(distance)

        same_sign = (x >=0 and y >=0) or (x <=0 and y <=0)

        if ring %2 ==0:

            print("black" if same_sign else "white", file=output_stream)

        else:

            print("white" if same_sign else "black", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 1
""",
            "output": \
"""\
black
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
import math


def main(input_stream, output_stream):
    x, y = map(int, input_stream.readline().rstrip("\n").split())

    distance_squared = x**2 + y**2

    sqrt_val = math.isqrt(distance_squared)

    if sqrt_val * sqrt_val == distance_squared:

        print("black", file=output_stream)

    else:

        distance = math.sqrt(distance_squared)

        ring = int(distance)

        same_sign = (x >=0 and y >=0) or (x <=0 and y <=0)

        if ring %2 ==0:

            print("black" if same_sign else "white", file=output_stream)

        else:

            print("white" if same_sign else "black", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 3
""",
            "output": \
"""\
black
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

Third sample:

4 3 → distance_squared 25. sqrt_val=5 → 5*5=25 → output black. Correct.

Another test case: (0,0) → distance_squared 0 → output black.

Test case (0, 0.5): 

x=0, y=0.5 (but input is integers). But the code is designed for integer inputs, but according to the problem statement, the input is two integers x and y. So all input points are integral coordinates.

So the code is correct.

Another test case: (1, -1):

distance_squared = 2. sqrt_val 1 → 1*1=1 <2. So not border.

distance is sqrt(2) ~1.414. ring is 1 (odd).

same_sign: x positive, y negative → false.

ring is odd → same_sign false → output black.

Which is correct.

Test case (1,1):

distance_squared 2 → not perfect square.

distance ~1.414. ring 1 (odd).

same_sign true → white. Correct.

Test case (3,4): distance_squared 25 → output black.

Test case (0,5): same_sign true. distance 5 → border → black.

Test case (0,-5): same_sign false. distance 5 → border → black.

Test case (5,0): same_sign true. distance 5 → border → black.

Test case (-5,0): same_sign true (x is negative, y is 0 → considered non-positive?). So same_sign is (x<=0 and y <=0). y is 0 → yes. So same_sign true. ring is 5 (odd). same_sign true → output white. But distance is 5 → border → output black.

Wait, no. Wait, for (x=-5, y=0):

distance_squared is 25. So sqrt_val is 5. 5*5=25 → output black.

Yes.

So code works.

Thus, the code is correct.
</think>

```python
import math

x, y = map(int, input().split())
distance_squared = x ** 2 + y ** 2
sqrt_val = math.isqrt(distance_squared)

if sqrt_val * sqrt_val == distance_squared:
    print("black")
else:
    same_sign = (x >= 0 and y >= 0) or (x <= 0 and y <= 0)
    ring = int(math.sqrt(distance_squared))
    if ring % 2 == 0:
        print("black" if same_sign else "white")
    else:
        print("white" if same_sign else "black")
```
