<think>
Okay, let's try to figure out this problem. So, the problem is about distributing pillows to hobbits in such a way that no one is hurt. The main condition is that any hobbit can't have at least two pillows less than their neighbor. And Frodo is in the k-th bed, and we need to find the maximum number of pillows he can have.

Hmm. So, the key points here are:

1. Each hobbit must have at least one pillow.
2. The pillows must sum up to exactly m.
3. The arrangement must ensure that no hobbit has at least two less than a neighbor. So, for any adjacent, the difference can't be >=2. Or wait, maybe the condition is that each hobbit's count must be >= their neighbors' -1. Because if someone's neighbor has x, then this hobbit can have x-1 or higher. Otherwise, the neighbor's x would be at least two more than this one's (x - (x-1) = 1, which is allowed. But if this one's is x-2, then the neighbor has x, which is two more. So the condition is that each hobbit's pillows can't be less than their neighbor's minus 1. So, for any i, pillows[i] >= pillows[i-1] -1 and pillows[i] >= pillows[i+1] -1, if those neighbors exist.

Wait, the problem says "if he has at least two pillows less than some of his neighbors have". So, for a hobbit to not be hurt, his count must be >= neighbor's count -1. Because if the neighbor has x, then he must have at least x-1. Otherwise, if he has x-2 or less, then the neighbor has x, which is two more. So the condition is that for all adjacent pairs, the difference between their counts is at most 1. Because if a neighbor has x, and this one has y, then y >= x-1 and x >= y-1. So the absolute difference is at most 1.

Wait, but the problem's condition is that a hobbit is hurt if he has at least two pillows less than some neighbor. So, for a hobbit i, if any of his neighbors has a count >= (i's count + 2), then i is hurt. So to avoid this, all neighbors of i must have counts <= (i's count + 1). So for each i, the counts of adjacent hobbits can be at most one more than i's count. So, the arrangement must be such that the sequence is non-decreasing or non-increasing in a way that allows only differences of at most 1 between adjacent elements.

But how do we model this? Well, perhaps the optimal arrangement is to have the pillows form a sort of "hill" where Frodo's position is the peak, and the pillows decrease by 1 as we move left or right from Frodo's position until they reach 1. But maybe there's a way to have a more efficient distribution when m is large.

Wait, let's think of the minimal case. The minimal number of pillows required is n, each getting 1. But since m >= n, we have to distribute the extra pillows (m -n) such that the constraints are met, and Frodo's count is maximized.

So, the problem is to distribute the extra (m-n) pillows in a way that maximizes Frodo's count, under the constraints that adjacent differences are at most 1, and all are at least 1.

So, the approach is to model the pillows as a sequence where Frodo's bed is the peak, and the sequence to the left and right of Frodo's bed decreases by 1 each step until it reaches 1.

For example, in the first sample input: 4,6,2. The minimal is 4 pillows. So 6-4=2 extra. So, the distribution starts as 1 for all. Then, we add the extras. The optimal is to have Frodo's bed as 2 (so 1 +1), and then adjust neighbors as needed.

Wait, the first example's output is 2. So how does that fit?

In that case, the initial allocation is 1 each. Then, adding 2 extra pillows. How?

Sample 1:

Beds: 1, 2, 3, 4 (but k=2). So the second bed is Frodo's. The distribution is:

Bed 1: 2, Frodo's (bed 2): 2, bed3:1, bed4:1. Wait, but that's total 2+2+1+1=6. Which matches m=6. But how does this satisfy the constraints? Let's see:

Bed 1 is 2, bed2 is 2: their difference is 0, okay.

Bed2 is 2, bed3 is 1: difference is 1, which is allowed. Because bed3's count is 1, which is 2-1=1. So allowed.

Bed3 is 1, bed4 is 1: okay.

So all constraints are met.

So the idea is that the pillows form a sequence that is as high as possible around Frodo, but the differences between adjacent are no more than 1.

But how to model this?

The approach is to find the maximum x such that the total pillows required when Frodo has x is <= m.

The problem reduces to a binary search problem. We can perform binary search on x (the maximum possible pillows Frodo can have), and for each x, compute the minimal number of pillows needed to satisfy the constraints. If that minimal number is <=m, then x is possible. We want the maximum x.

So, the steps would be:

1. Determine the minimal number of pillows needed for Frodo to have x pillows, given the constraints. If this sum is <=m, then x is possible.

We need to model how the other hobbits' pillows are arranged when Frodo's is x.

Let's model the left and right sides of Frodo's position.

For the left side (positions 1 to k-1):

Each position can be at most x-1, x-2, etc., but must not drop below 1. Similarly for the right side (positions k+1 to n).

But how to compute the sum required for left and right.

Let me think. Let's imagine that to the left of Frodo, each position is x-1, x-2, etc. But once we reach 1, all the positions beyond (to the left of that) must be 1.

Similarly for the right.

So for the left side (positions 1..k-1):

The sequence starts at x-1 for position k-1, x-2 for position k-2, etc., until either the position reaches 1 (so, after (x-1) steps), or until we reach the first position (position 1). The same applies to the right.

Wait, perhaps the left and right sides form a "staircase" decreasing by 1 each step from Frodo's position until they hit 1, then stay at 1.

So the sum for the left side can be calculated as follows:

The left has (k-1) positions. The maximal possible sequence starts at x-1, x-2, ..., until 1. Let's see how many steps that takes.

The maximum length of the sequence that can decrease from x-1 is (x-1) steps. For example, if x-1 is 3, then the sequence is 3,2,1. But if the left has more positions (k-1) than x-1, then the remaining positions are 1.

So the sum for the left is:

The number of terms that can be part of the decreasing sequence is the minimum between (x-1) and (k-1). Let's call this a = min(x-1, k-1). The sum of this part is a*(x-1 + (x-1 - a +1 )) / 2 → which is a*(2x -2 - a +1)/2 → a*(2x -1 -a)/2 → which is the sum of an arithmetic series from (x-1) down to (x-1 -a +1) = x - a.

Wait, the arithmetic series for the left that is decreasing from x-1, x-2, etc. The number of terms in the decreasing part is a = min(x-1, k-1). The sum of this part is (x-1 + (x-1 -a + 1)) * a / 2. Because the first term is x-1, and the last term is x-1 - (a-1) = x - a. So sum is (x-1 + x - a) * a / 2.

Then, the remaining positions on the left (if k-1 > a) would be (k-1 - a) terms of 1. So their sum is (k-1 -a)*1.

So total left sum is sum_left = ( (x-1 + (x -a)) * a ) // 2 + max(0, (k-1 -a)) *1.

Similarly for the right side (positions k+1 to n):

The right has (n -k) positions. The maximal possible sequence is x-1, x-2, ..., 1. The number of terms in the decreasing part is min(x-1, n -k). Let's call that b = min(x-1, n -k). Sum is (x-1 + (x -b)) * b / 2. Then, the remaining (n -k -b) positions are 1, sum (n -k -b)*1.

The total sum for Frodo's position is x. So the total sum for all positions is:

sum_left + sum_right + x.

We need this total to be <= m.

So, the binary search approach would be:

- Initialize low = 1 (since each hobbit must have at least 1) and high = possible maximum x. The upper bound for x could be determined. For example, the minimal possible sum when Frodo has x is when the left and right are all 1's. Then the sum is (k-1)*1 + (n -k)*1 + x = x + (n-1). So x can't be more than m - (n-1). But since m can be up to 1e9, and n up to 1e9, this could be possible. Wait, but m can be as big as 1e9. So the upper bound for x could be m - (n-1) +1. Wait, but maybe there's a better upper bound.

Alternatively, considering that when x is very large, the sum required would be x plus (x-1) terms on left and right. For example, if left and right have enough positions, the sum is x + sum left (x-1, x-2, ..., 1) + sum right (x-1, x-2, ..., 1). So sum is x + (x-1)*x / 2 * 2. But when x is large, the sum could exceed m. So the upper bound for x can be calculated as something like (m) + ... but perhaps we can set the initial high as x_max = 1 + (m -n) / (some terms), but that's not straightforward. So in binary search, perhaps high can be set as x where x is the maximum possible. Let's see: in the best case, when all other positions are as low as possible. The minimal sum for a given x is when the left and right are as small as possible. Wait, but the sum is the sum required when Frodo is x, and the left and right are arranged in the way that allows minimal sum. Wait, no, the sum for a given x is the minimal required to satisfy the constraints. So when we check if x is possible, the sum is computed as the minimal possible sum for that x. If that sum is <=m, then x is possible.

So the binary search will work as follows:

We need to find the maximum x such that compute_sum(x) <= m.

So the steps:

1. Binary search x in [1, upper_bound], where upper_bound is possibly m (since each hobbit can have at least 1, and Frodo's maximum could be up to m - (n-1)*1).

But for binary search, even if the upper bound is large (like 1e18), it's manageable because log2(1e18) is around 60 steps.

So let's proceed.

The key is the compute_sum function, which calculates the minimal sum needed for Frodo's x.

So for a given x, compute sum_left, sum_right, sum all.

Let's code compute_sum(x):

def compute_sum(x, n, k):

    # left sum (positions 1..k-1)

    left = k-1

    a = min(x-1, left)

    sum_left = a*(x-1 + (x - a)) // 2

    sum_left += max(0, left - a) * 1

    # right sum (positions k+1..n)

    right = n -k

    b = min(x-1, right)

    sum_right = b*(x-1 + (x -b)) // 2

    sum_right += max(0, right - b) *1

    total = sum_left + sum_right + x

    return total

Wait, but in code, the variables left and right are the number of positions. For left, it's k-1, right is n-k.

So, for example, if x is 2, k=2, n=4:

sum_left: left is 1 (positions 1). a is min(1, 1) =1. sum_left =1*(1 + (2-1 -1 +1))? Wait, maybe the formula is:

Wait, a is min(x-1, left). For left=1, x=2: x-1=1, so a=1. sum_left is a*(x-1 + (x-1 - a +1 )) // 2 ?

Wait, the arithmetic sequence starts at x-1 (which is 1) and has a terms (1 term). So the sum is 1.

sum_left =1*(1 + (1 -1 +1 )) / 2 → 1*(1+1)/2 =1. Then, left -a is 0. So sum_left is 1 + 0 =1.

sum_right: right is 2 (positions 3 and 4). x=2, x-1=1. min(1, 2)=1. sum_right is 1*(1 + (2-1 -1 +1 )) → 1*(1 +1)/2 =1. Then, right -b is 2-1=1. So sum_right is 1 + 1*1=2. Total is 1 +2 +2=5. But m is 6 in the first example. Wait, but the sample input was 4 6 2, which gives sum 2+2+1+1=6. So in this case, when x=2, compute_sum returns 5? That's conflicting. So where is the mistake?

Wait, perhaps my formula is incorrect.

Wait, let's take the first example:

n=4, m=6, k=2. x=2.

left is k-1 =1 positions (position 1).

sum_left for x=2:

x-1=1. a is min(1,1) =1.

sum_left is (1 + (x -a)) * a / 2. x=2, a=1 → (1 + (2-1)) *1 /2 → (1+1)*1/2 =1. Then, left -a is 0. So sum_left is 1 +0=1. So position 1 gets 1.

sum_right: positions 3 and 4. x=2, x-1=1. right=2.

b=min(1,2)=1.

sum_right is (1 + (2-1)) *1 /2 → (1+1)*1/2=1. Then, right -b is 2-1=1. So sum_right is 1 +1*1=2. Positions 3 and 4 get 1 and 1.

Frodo's position is x=2.

Total sum is 1+2+2=5. But sample input has m=6, but according to this sum, x=2 is possible with sum 5, but the sample output is 2. So why is that?

Wait, this suggests that the formula is wrong. Because the sample input's sum when x=2 is 6.

Ah! Oh right! Because in the sample, the left side (position 1) is 2, which is x-0, not x-1. So the formula is not capturing the correct arrangement.

Wait, this is a problem. So the model I have here is incorrect.

Wait, the formula for sum_left and sum_right is wrong.

Because in the first example, when x is 2, sum_left is 1, but in the correct arrangement, position 1 has 2 pillows. So according to the formula, sum_left is 1, but that's not correct.

So why is that?

Ah! Because the formula is modeling the left side as a sequence decreasing by 1 starting from x-1, but in reality, when Frodo's position is x, the adjacent positions can be up to x-1, but perhaps higher. Wait, no. Because the condition is that adjacent positions must not have more than one less than their neighbor.

Wait, the condition is that each neighbor of Frodo can have at most x-1. Because Frodo has x, his left neighbor can have at least x-1 (since x - (x-1) =1, which is allowed. But wait, wait. Let me think again.

The problem states that a hobbit is hurt if he has at least two pillows less than any of his neighbors. So, for any adjacent pair, the difference in their counts must be at most 1. Because if a neighbor has x, then this hobbit must have at least x-1. Otherwise, if this one has x-2, then the neighbor's count is two higher, leading to this hobbit being hurt.

So, to avoid any hurt, the counts of adjacent hobbits can differ by at most 1.

So, in order to maximize Frodo's count, the optimal arrangement would have the neighbors of Frodo (left and right) as x-1, their neighbors as x-2, etc., until they reach 1. Because this way, each step is 1 less than the previous, so the difference is allowed. But if Frodo's neighbors are higher than x-1, then Frodo's count is x, which would be two less than the neighbor's count, leading to Frodo being hurt. So that's not allowed.

Wait, no. Frodo's neighbors can have at most x+1. But Frodo's count is x. So if a neighbor has x+1, Frodo has x, which is two less. So that's not allowed. Hence, the neighbor's count must be at most x+1-1 =x. Or wait, the neighbor can have x-1, x, or x+1. Wait, the problem is that the neighbor's count cannot be two more than Frodo's. So Frodo's count is x. For a neighbor (say left neighbor) to not have Frodo being hurt, the left neighbor's count must be <=x+1. Because Frodo's count is x, if the neighbor's count is x+1, then Frodo's count is x, which is exactly one less than the neighbor's. That's allowed. Wait, the neighbor's count is x+1. Frodo's count is x. Then, the neighbor's count is one more than Frodo's. So Frodo is allowed. But then, the neighbor's count can be x+1, but then the neighbor's neighbor must be at least x+1-1 =x. So how does that fit into the arrangement?

Wait, perhaps the optimal arrangement is to have a non-decreasing sequence towards Frodo's position, and then non-increasing. But this seems complicated.

Alternatively, perhaps the arrangement must be such that all positions are at most x, and the sequence increases by 1 towards Frodo. So, the left side (positions 1..k-1) can form a sequence that starts at x- (k-1 - i) for position i, but that's getting complicated.

Wait, perhaps the correct model is that each position's maximum allowed value is determined by their distance from Frodo. For example, the left neighbor of Frodo (position k-1) can have at most x. Because Frodo's position is x, and the left neighbor can't be more than x+1. Wait, but that would allow the neighbor to be x+1, which would make Frodo's count x, which is one less than the neighbor. Which is allowed. So in that case, the neighbor can have x+1, but then that would require the neighbor's neighbor (position k-2) to be at least x+0 (since neighbor's x+1, so position k-2 must be at least x+1 -1 =x). So this could lead to a higher sum.

Wait, this is getting confusing. Let's think of another approach.

The problem requires that no hobbit has at least two pillows less than any neighbor. So, for any two adjacent hobbits, the absolute difference between their pillows must be <=1.

In order to maximize Frodo's pillows, we want his count as high as possible, and all other counts arranged such that they can be as high as possible without violating the constraints.

So, the optimal arrangement would be to have the pillows form a "pyramid" with Frodo at the peak. Then, the counts to the left and right of Frodo decrease by 1 each step until they reach 1.

But perhaps when there's enough pillows, the counts can be higher. For example, if m is very large, then after filling the pyramid, we can add extra pillows to some positions without violating the constraints.

Wait, but how?

Alternatively, the optimal arrangement is that Frodo's pillows is x. Then, the left side is a sequence that can be at most x, x-1, x-2, ..., until 1, but also considering the positions available. Similarly for the right side. But how to model this.

Alternatively, for each position i, the maximum possible pillows it can have is determined by its distance from Frodo's position. For example, the leftmost position can be x - (k-1 - (i-1)), but this may not hold.

Wait, perhaps the minimal sum for a given x is such that:

For the left side (positions 1 to k-1):

The maximum possible value for position j (j <k) is x - (k -j). But that's only if x - (k -j) >=1. Otherwise, it's 1.

Similarly for the right side (positions k+1 to n):

The maximum possible value is x - (j -k), but again, not less than 1.

Wait, that makes sense. Because for position j where j is on the left of k (j <k), the distance to k is (k-j). For each step away from k, the maximum possible value decreases by 1, but not below 1.

So, for example, position k-1 is at distance 1 from k. So maximum x-1. Position k-2 is at distance 2, so x-2, etc. But once x- distance is less than 1, it's capped at 1.

So the sum for the left is the sum for each position j from 1 to k-1:

max(1, x - (k-j)).

Similarly for the right sum.

So, the sum for a given x is:

sum_left = sum_{d=1 to k-1} max(1, x -d)

sum_right = sum_{d=1 to n-k} max(1, x -d)

sum_total = sum_left + sum_right + x

We need sum_total <= m.

So this is the correct formula. The previous approach of considering the left and right as sequences that decrease by 1 until reaching 1, then stay at 1 is correct.

So, the correct way to compute sum_left and sum_right is as follows:

sum_left is the sum for the left positions, which are (k-1) positions. For each position j (from 1 to k-1), the maximum allowed is x - (k-j), which is x - (distance). For example, the first position to the left of k (distance 1) is x-1, next is x-2, etc., until x-d reaches 1. Any positions beyond that (if the distance is larger than x-1) will be 1.

So, for the left sum:

The distance ranges from 1 to (k-1). So the maximum possible value for each is x -d, but not less than 1.

So sum_left is sum_{d=1 to (k-1)} max(1, x -d).

Similarly for sum_right: sum_{d=1 to (n-k)} max(1, x-d).

So how to compute these sums efficiently.

Let's take sum_left:

The sum is the sum of (x-d) for d from 1 to t, where t is the maximum d where x-d >=1. Then the remaining terms (from t+1 to k-1) are 1.

So t is the maximum d where x-d >=1 → d <=x-1. So t = min(x-1, k-1).

So for sum_left:

If x-1 >= k-1 → all terms are (x-1) down to x - (k-1) → sum is sum from a= x-1 - (k-1-1) to a=x-1 → which is (x-1 + (x - (k-1))) * (k-1) / 2.

Wait, for d from 1 to (k-1):

x-d >=1 → for d <= x-1. So if k-1 <= x-1 → sum from d=1 to d=k-1 is x-1, x-2, ..., x - (k-1). Which is an arithmetic sequence with first term x-1, last term x - (k-1), number of terms k-1.

Sum = ( (x-1) + (x - (k-1)) ) * (k-1) / 2 → (2x -k) * (k-1)/2.

If x-1 < k-1, then sum from d=1 to d=x-1 is (x-1) + (x-2) + ... +1 → sum is x*(x-1)/2. Then, the remaining (k-1 - (x-1)) terms are 1. So sum_left = x(x-1)/2 + (k-1 -x +1)*1 = x(x-1)/2 + (k -x) *1.

Similarly for sum_right.

So the code to compute sum_left and sum_right is:

sum_left:

t = min(x-1, k-1)

sum_part1 = t*(x-1 + x - t) // 2

sum_part2 = max(0, (k-1) - t) *1

sum_left = sum_part1 + sum_part2

Similarly for sum_right:

t = min(x-1, n -k)

sum_part1 = t*(x-1 + x -t) //2

sum_part2 = max(0, (n-k) -t)*1

sum_right = sum_part1 + sum_part2

So the total sum is sum_left + sum_right +x.

Now, let's check the first sample input.

Sample 1: n=4, m=6, k=2. So k=2, n-k=2.

x=2.

sum_left:

k-1 =1. x-1=1. t=min(1,1)=1.

sum_part1 = 1*(2-1 + 2-1) //2 → (1 +1) *1/2 =1.

sum_part2 is 0.

sum_left=1.

sum_right: n-k=2. x-1=1. t=min(1,2)=1.

sum_part1=1*(1 + (2-1 -1 +1 )) → wait, no. Let's re-calculate:

sum_part1 for the right:

t=1. x-1=1. x-t=2-1=1.

sum_part1=1*( (x-1) + (x -t) ) * t //2 → (1 +1)*1//2=1.

sum_part2 is max(0, 2-1) =1*1=1.

sum_right=1+1=2.

Total sum=1+2+2=5. But sample input's m is 6, and the correct answer is 2. But according to this formula, when x=2, sum is 5. So the formula is still not correct.

Wait, what's wrong here?

In the first sample input, when x=2, the sum is 2 (Frodo's) + 2 (left) + 1 (right) +1 (right) → total 6. But according to the formula, sum_left is 1 (sum_part1=1, sum_part2=0). So sum_left is 1 (position 1 has 1 pillow). But according to the sample explanation, position 1 has 2 pillows.

So there's a mistake in the model. So why is that?

Ah! Because the model is incorrectly assuming that the left side's maximum possible value is x-1 for the first position, but perhaps the correct model allows the left neighbor to be x, and the next to be x-1, etc.

Wait, perhaps the mistake is in the way the distances are computed. Because for the left side, the distance from Frodo's position is (k-j), not d=1,2,... For example, position k-1 is distance 1 from k, position k-2 is distance 2, etc. So the model is correct. But according to this, the left position (k-1=1) when x=2 is allowed to have x-1=1. But the sample solution gives it 2.

Wait, this seems to indicate that the model is incorrect.

Wait, perhaps the formula for the left sum is not max(1, x-d), but max(1, x - (d-1)).

No, that's not the case. Let me think again.

Each position j on the left (j <k) is at a distance of (k-j) from Frodo. For example, j=k-1 is distance 1.

The maximum possible value for j is x - (k-j). Because each step away from Frodo can decrease by 1.

So for x=2, j=1 (k=2, j=1) → distance is 1. x -1=1. So j's maximum is 1. But in the sample solution, j=1 has 2 pillows. Which would violate the condition. Because Frodo has 2, j=1 has 2. The difference is 0. So allowed. So why can't j=1 have 2?

Ah, here's the mistake! The model is assuming that the left positions can be at most x-1, but that's not the case. The condition allows for the left neighbor to have x, x+1, etc., as long as Frodo's count is not two less than the neighbor's.

Wait, but the model was based on the idea that Frodo's neighbor can't have more than x+1. Because if Frodo's neighbor has x+1, then Frodo's count is x, which is two less than the neighbor's. So that's invalid. So the neighbor can't have x+1. So the maximum allowed for the neighbor is x. Because x+1 is forbidden.

So, the model is correct. The left neighbor can be at most x. But wait, how?

Wait, the condition says that any hobbit cannot have at least two less than their neighbor. So, if Frodo's left neighbor has x+1, then Frodo has x, which is two less than the neighbor. So that's invalid. Hence, the left neighbor can't have x+1. So the maximum allowed for the left neighbor is x. Because if the neighbor is x, then Frodo's x is allowed (difference of zero).

But how does that fit into the model?

Wait, the model was based on the left positions being x-1, x-2, etc. But this is only if the sequence is arranged in a way that each step from the neighbor to Frodo's position is at most 1. But perhaps the model is wrong because the left neighbor can be x, and the next position can be x-1, which is allowed (difference 1), and so on.

Wait, this is possible. So the model should allow the left neighbor to be x, the next x-1, etc. But then, the distance from Frodo's position would dictate how much each position can have.

So perhaps the correct model is that each position j on the left can have up to x + (k-j) - 1. No, that's not right.

Alternatively, the correct model is that each position j can have up to x + (k-j) - d, but this is not clear.

This suggests that the previous approach is incorrect. So why in the first sample, the left neighbor has 2 pillows, which is x=2.

So according to the model, the left neighbor can have x-1=1, but in the sample solution, it's 2. So the model is wrong.

So what's the correct way to model this?

Ah! The problem is that the model is based on the idea that the left neighbor must be at most x-1. But that's incorrect.

The correct model is that the left neighbor can be up to x+1, but Frodo's count is x. That's allowed only if the neighbor's count is x+1. But then, Frodo's count is two less than the neighbor's (x+1 -x=1), which is allowed. Wait, no. If Frodo's count is x, and the neighbor's count is x+1, then Frodo's count is 1 less than the neighbor's. Which is allowed. Because the neighbor's count is only one more than Frodo's. So that's acceptable.

So, the model was wrong because it assumed that the left neighbor must be x-1. But actually, the left neighbor can be x+1, x, or x-1, as long as the differences between adjacent positions are at most 1.

But this complicates the model. How to model this in order to maximize Frodo's pillows.

Wait, perhaps the optimal arrangement is to have Frodo's count as high as possible, with the sequence increasing to the left and right, but this depends on how much m allows.

Alternatively, the optimal arrangement is to form a "mountain" where Frodo's position is the peak. But the peak can be surrounded by increasing values if possible.

But this seems tricky.

Alternatively, perhaps the maximum possible x is determined by the following approach:

We can arrange the pillows such that all positions to the left of Frodo are as high as possible, forming a sequence that increases by 1 towards Frodo's position, and similarly for the right. But this is allowed because the differences between adjacent positions are 1.

For example, if Frodo has x pillows, then the left neighbor can have x-1, x-2, etc., but also can have x+1, x, x-1, etc., as long as the sequence is non-decreasing.

Wait, but this is getting too vague.

Perhaps the correct model is to arrange the sequence such that each position's count is as high as possible given the constraints. So, for position j, the maximum possible count is the minimum between:

- The maximum allowed by the left neighbor (prev[j-1] +1)

- The maximum allowed by the right neighbor (next[j+1] +1)

But since we want to maximize Frodo's count, perhaps the optimal arrangement is to have the sequence to the left of Frodo be a non-decreasing sequence ending at Frodo's x, and similarly for the right.

But this seems unclear.

Another approach is to model the problem as follows:

We need to maximize x, such that the sum of all pillows is <=m, and the sequence of pillows is such that the difference between any two adjacent positions is at most 1.

The way to model this is that the pillows form a sequence where each position i can be as high as possible, given the constraints, and Frodo's position is x. The minimal sum for x is when the sequence is as "steep" as possible, i.e., each step away from Frodo decreases by 1 until reaching 1.

So the previous model is correct.

But according to the first sample, when x=2, the sum computed by the model is 1+2+2=5, but the sample input requires sum 6. So why is that?

Because the model is wrong. So there's a mistake in the model.

Wait, sample input 4 6 2. The correct distribution is:

Bed 1: 2, bed 2:2, bed3:1, bed4:1. Sum is 6.

So according to this, the left neighbor of Frodo has 2 pillows. So in the model, for x=2, the left neighbor can have 2 pillows, which is allowed because the difference between Frodo's and the left is 0. So how does this fit into the model?

Ah! The model's mistake is that it restricts the left neighbor to x-1=1, but the correct model allows the left neighbor to be x, as long as the sequence from the left neighbor to its left doesn't violate the constraints.

So the model's formula for sum_left is incorrect.

So why is the left neighbor allowed to have x?

Because the condition allows adjacent positions to differ by 0 or 1. So, if Frodo's position is x, the left neighbor can be x, x-1, or x+1. But if it's x+1, then Frodo's count is one less than the left neighbor's, which is allowed. But then, the next neighbor to the left can be x+2, which would make the left neighbor's count x+1, which is allowed. But this would require that the sum increases, but we are trying to find the minimal sum for a given x. So to find the minimal sum for a given x, the left neighbor should be as small as possible, but not violate the constraints.

Wait, but to find the minimal sum for a given x, we need to arrange the other positions in a way that uses as few pillows as possible. So the minimal sum for x is achieved when the other positions are as small as possible, given the constraints.

So for example, if Frodo's position is x=2, the left neighbor can be 2 or 1. But if we set it to 1, the sum is minimized. But in the sample input, the left neighbor is 2, leading to a higher sum. So why is that possible?

Ah! Because the model is trying to find the minimal sum required for x. If the minimal sum is <=m, then x is possible. But in the sample input, x=2's minimal sum is 5, but the sample's sum is 6. So why is x=2 allowed?

Because the minimal sum for x=2 is 5, which is <=6. So even if there's extra pillows, it's possible to distribute them in such a way that the sum is increased without violating the constraints.

Wait, but how? Because once the minimal sum is achieved, adding more pillows requires that you distribute them in a way that doesn't violate the constraints. For example, you can increase the pillows of some positions, but each increase must be in a way that adjacent constraints are maintained.

So, the minimal sum is computed as the sum when all other positions are as small as possible. But there might be ways to have a higher sum (but still <=m) for the same x. However, the binary search approach is to check whether the minimal sum for x is <=m. Because if the minimal sum is <=m, then x is possible. Because you can always add the remaining pillows (m - minimal_sum) to some positions without violating the constraints. For example, you can distribute the extra pillows as follows: add 1 to Frodo's pillows, but wait, that would increase x. So no, because x is fixed in the binary search step.

Wait, no. The binary search is for x, the number of pillows Frodo has. So when you compute x's minimal sum, if it is <=m, then x is possible. The remaining pillows (m - minimal_sum) can be distributed to other positions as long as the constraints are maintained. But how?

Ah, this is the key mistake in the previous model. The model assumes that the minimal sum is the only possible sum for x. But in reality, when you have extra pillows, you can increase other positions' counts as long as the constraints are met. For example, in the first sample, the minimal sum for x=2 is 5, but m=6. The extra 1 can be added to the left neighbor (position 1), which increases its count from 1 to 2. Now, the sum is 6, which is allowed.

So the previous model's approach is incorrect. Because the model computes the minimal sum for x, but the actual sum can be increased by distributing the remaining pillows. However, this distribution has to maintain the constraints. So the model's assumption that the minimal sum is the sum used to check x's possibility is wrong.

So the binary search approach is incorrect. Because the minimal sum for x may be less than m, but there's no way to distribute the remaining pillows without increasing x.

So what's the correct way to compute the required sum for x?

Ah! The correct approach is to compute the maximal sum possible for x. Because once x is fixed, the other positions can be adjusted as long as they meet the constraints, but to have the sum as large as possible (up to m). But this is not correct either. Because we need the total sum to be exactly m.

Wait, the problem requires that all pillows are distributed. So the sum must be exactly m.

So the binary search approach must find the maximum x such that there exists a valid distribution with sum exactly m, and Frodo's count is x.

But how to model this?

This makes the problem more complex, as the sum can vary for a given x.

So, for a given x, there's a minimal sum and a maximal sum. If m is between these two, then x is possible.

So, the approach should be to binary search x, and for each x, check whether m is between the minimal and maximal sum for x.

But how to compute the minimal and maximal sum for x.

The minimal sum for x is as previously computed (each position to the left and right is as low as possible).

The maximal sum for x is when each position to the left and right is as high as possible, given the constraints.

So, for the maximal sum, the left and right positions would form a sequence that increases by 1 as they approach Frodo's position.

For example, for the left side, the maximal possible sequence is x+1, x, x-1, etc. Wait, but Frodo's count is x. If the left neighbor has x+1, then Frodo's count is x, which is one less than the neighbor. This is allowed. Then the next neighbor can be x+2, which is allowed as long as the next neighbor's count is x+2, which is one more than the previous.

But this would create a sequence like x+2, x+1, x, which has differences of 1 between adjacent positions. So it's allowed.

But this would require that the left side's sequence increases by 1 as you move away from Frodo. Which would require more pillows, increasing the sum.

But how to model this.

Alternatively, the maximal sum for x is when the left and right sequences form increasing sequences away from Frodo's position. But how to compute this.

This is getting extremely complicated. So perhaps the correct approach is to model the problem in terms of the minimal sum for x and the maximal sum for x, and check if m is between them.

But how?

Alternatively, perhaps the minimal sum is not the correct approach. Perhaps the correct way to model the problem is to find the maximal x such that the minimal sum required for x is <=m, and there exists a way to distribute the remaining pillows (m - minimal_sum) to the other positions without violating the constraints.

But how can we distribute the remaining pillows?

This seems very challenging. Perhaps the correct way is to realize that the minimal sum is the only possible sum for x, and that the binary search approach is incorrect. But this is not the case.

Alternatively, perhaps the initial model was correct, and the sample input was being computed incorrectly.

Let's re-calculate the first sample:

n=4, m=6, k=2.

x=2.

sum_left:

left positions: 1.

distance d=1.

max(1, x-d) → max(1, 2-1=1) → 1. sum_left=1.

sum_right: right positions 3 and 4. distance 1 and 2.

For d=1: max(1, 2-1=1) →1.

For d=2: max(1, 2-2=0) →1.

sum_right =1+1=2.

sum_total=1+2+2=5.

But m is 6. So the minimal sum is 5, which is <=6. So x=2 is possible. But then, where do the extra pillows go?

In this case, there's an extra 1 pillow. We need to distribute it among the positions in such a way that the constraints are maintained.

For example, we can add 1 to position 1 (left of Frodo). So position 1's count becomes 2. Now, the sequence is:

Position 1:2, Frodo:2, position 3:1, 4:1.

This sum is 2+2+1+1=6.

The constraints are satisfied. Position 1 and Frodo: difference 0. Frodo and position 3: difference 1. So this is valid.

So, the model's initial approach was correct. Because the minimal sum for x=2 is 5 <=6. So x=2 is possible. Hence, the binary search will select x=2 as the maximum possible.

So the code is correct, and the sample input's x=2 is indeed allowed.

So why does the sample input have sum 6, which is higher than the computed minimal sum? Because the minimal sum is the sum required to meet the constraints, but there can be ways to distribute the remaining pillows (m - minimal_sum) in a way that increases some of the counts without violating the constraints.

Thus, the binary search approach is correct. Because the minimal sum for x is <=m, x is possible. The code will find the maximum x for which the minimal sum is <=m.

So the binary search approach is valid.

Let's see for the first sample:

The code would binary search x. Let's see the possible x's.

The initial low is 1, high is m - (n-1) +1 =6-3+1=4.

But let's compute the possible x's.

x=2: sum 5 <=6 → possible.

x=3: sum_left:

left is 1 position. d=1: x-1=2. So sum_left is min(2,1) → sum_part1= (2+ (3-1)) *1 / 2 → (2+2)*1/2=2. sum_part2=0 → sum_left=2.

sum_right: n-k=2. x-1=2. t=2. sum_part1=2*(2 + (3-2)) /2 → 2*(2+1)/2 →3. sum_part2=0. sum_right=3.

total sum=2+3+3=8>6 → not possible.

Thus, x=3 is not possible.

So the maximum x is 2.

Which matches the sample.

So the code works.

Now, the code's binary search approach is correct.

Thus, the correct way to solve the problem is to perform a binary search on x, compute the minimal sum for x, and check if it's <=m. The maximum x for which this holds is the answer.

So the code will be:

Read n, m, k.

Compute the minimal pillows required: n.

If m ==n, output 1.

Else, perform binary search between low=1 and high= (m -n) +1.

Wait, no. The maximum possible x is when all other positions are 1. Then sum is x + (n-1). So x can be up to (m - (n-1)). So initial high can be m - (n-1) +1, but since m can be up to 1e9 and n up to 1e9, we can set high to 1e18, which is a safe upper bound.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m, k = map(int, input_stream.readline().rstrip("\n").split())

    low = 1

    high = m  # initial high, but can be higher. But binary search is efficient.

    max_pillows = 0

    def compute(x):

        # compute sum for left and right.

        left = k-1

        a = min(x-1, left)

        sum_left = a*( (x-1) + (x - a) ) //2

        sum_left += max(0, left - a) *1

        right = n -k

        b = min(x-1, right)

        sum_right = b*( (x-1) + (x -b) ) //2

        sum_right += max(0, right -b)*1

        total = sum_left + sum_right + x

        return total

    while low <= high:

        mid = (low + high) //2

        required = compute(mid)

        if required <= m:

            max_pillows = mid

            low = mid +1

        else:

            high = mid -1

    print(max_pillows, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 10 3
""",
            "output": \
"""\
4
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
    n, m, k = map(int, input_stream.readline().rstrip("\n").split())

    low = 1

    high = m  # initial high, but can be higher. But binary search is efficient.

    max_pillows = 0

    def compute(x):

        # compute sum for left and right.

        left = k-1

        a = min(x-1, left)

        sum_left = a*( (x-1) + (x - a) ) //2

        sum_left += max(0, left - a) *1

        right = n -k

        b = min(x-1, right)

        sum_right = b*( (x-1) + (x -b) ) //2

        sum_right += max(0, right -b)*1

        total = sum_left + sum_right + x

        return total

    while low <= high:

        mid = (low + high) //2

        required = compute(mid)

        if required <= m:

            max_pillows = mid

            low = mid +1

        else:

            high = mid -1

    print(max_pillows, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 6 1
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

Third sample:

3 6 1.

Frodo is in position 1. left=0, right=2.

x=3.

sum_left=0.

sum_right: right=2. x-1=2. min(2,2)=2.

sum_part1=2*(2 + (3-2))//2 →2*(2+1)/2=3. sum_right=3+0=3.

total=0+3+3=6 <=6. So x=3 is possible. Check x=4:

sum_right: x-1=3. right=2.

sum_part1=2*(3 + (4-2))//2 →2*(3+2)/2=5. sum_right=5+0=5.

total=0+5+4=9>6. So no. Hence, x=3 is the answer.

So the code works for the samples.

Thus, the code is correct.
</think>

```python
n, m, k = map(int, input().split())

def compute(x):
    left_count = k - 1
    a = min(x - 1, left_count)
    sum_left = a * (x - 1 + x - a) // 2
    sum_left += max(0, left_count - a) * 1

    right_count = n - k
    b = min(x - 1, right_count)
    sum_right = b * (x - 1 + x - b) // 2
    sum_right += max(0, right_count - b) * 1

    return sum_left + sum_right + x

low, high = 1, m
max_pillows = 0

while low <= high:
    mid = (low + high) // 2
    required = compute(mid)
    if required <= m:
        max_pillows = mid
        low = mid + 1
    else:
        high = mid - 1

print(max_pillows)
```
