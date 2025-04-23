<think>
Okay, let's tackle this problem. Hmm, the problem statement is a bit complex. Let me read it again carefully.

So, Monocarp has n dishes. For each dish, if he adds red pepper, the tastiness is a_i, otherwise black pepper gives b_i. He has to choose exactly one shop, and for that shop, buy x red packages and y black packages such that x * x_j + y * y_j = n. Then, he uses these packages to assign each dish a pepper type. The goal is to maximize the total tastiness for each shop. If it's impossible for a shop, output -1.

Wait, so for each shop j, we need to find all possible (x, y) pairs where x and y are non-negative integers, and x * xj + y * yj = n. Then, among all those possible (x, y), we need to choose which dishes get red or black pepper such that exactly (x * xj) are red and (y * yj) are black. Because each red package gives xj servings, and each black gives yj. So the total red used is x*xj, and black is y*yj, which must sum to n.

The problem is for each shop, compute the maximum possible total tastiness, given the possible x and y combinations. But how?

Let's break down the steps.

First, for each shop j, the equation x * xj + y * yj = n must be satisfied. We need to find all possible pairs (x, y) of non-negative integers that satisfy this equation. For each valid pair, we can assign x*xj dishes to red and y*yj to black. Then, to maximize the total tastiness, we want to select the top (x*xj) dishes with the highest (a_i - b_i) difference, since that's the gain from choosing red over black for that dish.

Wait, because the total tastiness is sum(b_i) + sum (a_i - b_i) for the dishes where we choose red. So, the optimal is to choose the dishes with the largest (a_i - b_i) to be red. So for a given number of red dishes (k), the maximum sum is sum(b_i) + sum of the top k (a_i - b_i). 

So, the approach would be:

1. Precompute the sorted list of (a_i - b_i) in descending order. Also compute the prefix sums of these sorted values. This way, for any k, the sum of the top k (a_i - b_i) is the prefix sum up to k. The sum of all b_i is a base value, and adding the prefix sum gives the maximum possible total when selecting k red dishes.

2. For each shop j, check all possible k (number of red dishes) that can be represented as k = x * xj, where x is a non-negative integer, and the remaining (n -k) must be equal to y * yj for some y. So, the equation is k = x * xj, and n -k = y * yj. So k must be a multiple of xj, and (n -k) must be a multiple of yj. Also, x and y must be non-negative.

But how do we efficiently find all possible k for a given xj and yj?

Wait, for each shop j, xj and yj are given. We need to find all possible k such that:

k = x * xj  
n -k = y * yj  
x >=0, y >=0  

Which can be rewritten as:

k must be a multiple of xj, and (n -k) must be a multiple of yj.

So for a given j, possible k's are those that are multiples of xj, and (n -k) is a multiple of yj, and k >=0, (n -k) >=0.

So the possible k's are the numbers in the range [0, n] that satisfy:

k ≡ 0 mod xj  
(n -k) ≡ 0 mod yj  

Which implies that:

k ≡ 0 mod xj  
k ≡ n mod yj  

So solving for k modulo LCM(xj, yj). But perhaps there's a better way.

Alternatively, for each j, we can iterate over possible x where xj *x <=n. Then for each x, compute k =x*xj, then check if (n -k) is divisible by yj, and the quotient y is >=0.

But if xj is up to n, and m is up to 3e5, then for each j, iterating x up to n/xj could be O(n) per j, which would be O(3e5 * 3e5) operations, which is 9e10—way too slow.

That's impossible. So we need a smarter approach.

Alternative approach: For a shop j, find all possible k such that k is a multiple of xj, and (n -k) is a multiple of yj. Then, among these possible k's, compute the maximum sum.

So the steps for each j are:

1. Find all k where k mod xj == 0 and (n -k) mod yj == 0, and k >=0, n -k >=0.

2. For each such k, compute the maximum sum, which is sum_b + prefix_sum[k] (since we take the top k (a_i -b_i) differences).

3. The maximum of these sums is the answer for the shop. If no such k exists, output -1.

The problem is to find all possible k's efficiently.

So, how to find all possible k for each j?

Let's consider the equation:

k = a * xj  
n -k = b * yj  
a, b >=0  

So:

a * xj + b * yj = n  
a >=0, b >=0  

This is a linear Diophantine equation. We can find all possible solutions (a, b) and then compute k from a.

But solving this for each j could be feasible if we can find the solutions quickly.

Let's think of the equation as a * xj + b * yj = n. We need to find non-negative integers a and b.

The standard approach for such equations is to find all possible a such that xj divides (n - b * yj), but perhaps there's a better way.

Alternatively, since a and b must be non-negative, we can express a as (n - b * yj)/xj. So for each possible b, (n - b * yj) must be divisible by xj and >=0. But this approach would require iterating b, which could be up to n/yj. Again, for large yj, this could be O(1), but for small yj, this would be O(n) steps per j, which is not feasible.

Another approach is to find the minimal solution and then find all possible solutions. Let's think in terms of the equation:

xj * a + yj * b = n

Let d = gcd(xj, yj). For this equation to have a solution, d must divide n. So first, check if n % d != 0. If not, then no solution exists for this shop.

Otherwise, proceed.

We can find the general solution using the extended Euclidean algorithm.

First, find x0 and y0 such that xj * x0 + yj * y0 = d.

Then, multiply both sides by (n/d) to get xj*(x0*(n/d)) + yj*(y0*(n/d)) = n.

But this gives a particular solution (a0, b0) where a0 = x0*(n/d), b0 = y0*(n/d).

The general solution is:

a = a0 + (yj/d)*t  
b = b0 - (xj/d)*t  

We need a >=0 and b >=0.

So substituting into the equations:

a0 + (yj/d)*t >=0  
b0 - (xj/d)*t >=0  

Solve for t:

t >= -a0 *d / yj  
t <= b0 *d / xj  

But t must be an integer. So find all integer t in this interval where a and b are non-negative.

Each such t gives a possible (a, b) pair, which in turn gives a possible k =a *xj.

Once we have all possible k's, compute for each the sum_b + prefix_sum[k], and take the maximum.

But how to compute this efficiently?

First, for each shop j:

1. Check if gcd(xj, yj) divides n. If not, output -1.

2. Else, find all possible a and b pairs as per the general solution.

3. For each valid a, compute k =a *xj. Check that k <=n and (n -k) is >=0 (since yj*b =n -k, and b >=0).

4. For each valid k, compute the sum and track the maximum.

But even with this approach, how many possible k's can there be per shop j? Potentially, if xj and yj are coprime and n is large, there could be O(n) solutions, which again is not feasible.

Wait, but perhaps there are only O(1) possible solutions. Let's see.

The general solution is a = a0 + (yj/d) *t  
b = b0 - (xj/d)*t  

We need a >=0 and b >=0.

So:

a0 + (yj/d)*t >=0  
b0 - (xj/d)*t >=0  

Let's express t in terms of these inequalities.

The first inequality: t >= -a0 * d / yj  
The second: t <= (b0 *d)/ xj  

But a0 and b0 are obtained from the initial solution, which may be positive or negative. So perhaps t can vary in a certain range. For each t in that range, we get a solution.

But how many integer t's are in that range?

The step between possible t's is 1. The number of possible t's is determined by the interval. For example, if t can be from t_min to t_max, inclusive, then there's t_max - t_min +1 possible values. But if this range is small (like O(1)), then this approach is feasible.

But how to compute this?

Alternatively, perhaps there's a minimal and maximal possible k for each j. For example, in the equation, when t increases, a increases by yj/d, and b decreases by xj/d. So the possible k's are a *xj = (a0 + (yj/d)*t) *xj. So the k's form an arithmetic sequence with a step of (yj/d)*xj. Similarly, the possible k's are spaced by (yj *xj)/d, but since d is the gcd, (xj/d) and (yj/d) are coprime. So the step size is (xj * yj)/d. Wait, no. Because (yj/d) multiplied by xj is xj*yj/d. So each step in t increases k by xj*yj/d.

So the possible k's are in an arithmetic sequence with step xj*yj/d. Since xj and yj can be up to 3e5, and d can be up to min(xj,yj), the step size could be up to 3e5 *3e5 /1 = 9e10. Which means that for some shops, there's only one possible k.

Wait, but this is possible. For example, if the step is larger than n, then there can be only one possible k.

So the number of possible k's per shop j is O(1) in practice, perhaps up to 2 or 3. So even for m=3e5 shops, the total number of k's across all shops is manageable.

So the plan is:

For each shop j:

1. Check if xj and yj can form a valid equation. That is, if the gcd of xj and yj divides n.

   a. Compute d = gcd(xj, yj)

   b. If n % d !=0 → no solution. Output -1.

   c. Else, proceed.

2. Find the general solution to the equation xj*a + yj*b =n.

   a. Find x0, y0 such that xj*x0 + yj*y0 =d.

   b. Multiply by (n/d) to get a particular solution a0 = x0*(n/d), b0 = y0*(n/d).

3. The general solution is a = a0 + (yj/d)*t, b= b0 - (xj/d)*t.

   a. We need a >=0 and b >=0.

   b. So (yj/d)*t >= -a0 → t >= ceil( (-a0 *d)/ yj )

   c. (xj/d)*t <= b0 → t <= floor( (b0 *d)/ xj )

   d. Find all integer t in this range.

4. For each t in this range, compute a and b, then compute k =a *xj.

   a. Check if k is within 0 <=k <=n.

   b. Also check that (n -k) is divisible by yj (but this should already be ensured by the equation).

5. Collect all possible k's. For each k, compute the sum as sum_b + prefix_sum[k], and keep the maximum.

6. The answer for the shop is the maximum of these sums. If there are no valid k's, output -1.

But how to compute x0 and y0? Because using the extended Euclidean algorithm for each j could be time-consuming for m=3e5. Wait, but the extended Euclidean algorithm is O(log min(xj, yj)) per j. Since xj and yj can be up to 3e5, log is manageable, but 3e5 * log(3e5) is around 3e5*19 ≈ 5.7e6 operations, which is acceptable.

So the steps are feasible.

Now, the main steps are:

- Precompute the sorted list of (a_i -b_i) in descending order, and compute the prefix sums.

- For each shop j, compute possible k's using the extended Euclidean approach, then check which of these k's are feasible, and compute the maximum sum.

Now, the code steps:

First, read n dishes. For each dish, compute a_i and b_i, and also the difference (a_i -b_i). Then, sort the differences in descending order. Compute the prefix sums of these differences. Also compute sum_b, which is the sum of all b_i.

Then, for each shop j, process as follows:

1. Check if d = gcd(xj, yj) divides n. If not, output -1.

2. Else, compute the particular solution (a0, b0) using extended Euclidean.

3. Find the general solution's possible t values.

4. For each t in the possible range, compute a and b, then k =a*xj. Check that k is between 0 and n, and that (n -k) is divisible by yj (though this is ensured by the equation).

5. Collect all valid k's. For each k, check if it's in the allowed range (0 <=k <=n), and compute the sum.

6. Take the maximum of these sums, or output -1 if none.

But implementing the extended Euclidean part correctly is crucial.

Let me think about how to compute x0 and y0 such that xj * x0 + yj * y0 =d.

The extended Euclidean algorithm returns x and y such that xj*x + yj*y =d. So x0 is x, y0 is y.

Once we have that, then the particular solution is (x0 * (n/d), y0 * (n/d)).

But the particular solution may not have a0 and b0 as non-negative. So the general solution steps will adjust t to find all possible a and b.

But in code, how to compute x0 and y0?

We can use the extended Euclidean algorithm. Let's implement that.

But how to handle the signs?

Once x0 and y0 are found, then the general solution is a = a0 + (yj/d)*t, and b = b0 - (xj/d)*t.

So in code, for each j:

Compute d = gcd(xj, yj)

if n %d !=0 → output -1.

else:

   (x0, y0) = extended_gcd(xj, yj)

   a0 = x0 * (n//d)

   b0 = y0 * (n//d)

Then find the possible t's such that a >=0 and b >=0.

But in code, the extended_gcd function returns x and y such that xj *x + yj *y =d. So x and y can be positive or negative.

So the particular solution (a0, b0) is (x0 * (n/d), y0 * (n/d)).

But a0 and b0 can be negative. So we need to adjust t to make a and b non-negative.

Now, let's proceed to find t.

The equations are:

a = a0 + (yj/d)*t >=0 → t >= (-a0) *d / yj

b = b0 - (xj/d)*t >=0 → (xj/d)*t <=b0 → t <= (b0 *d)/xj

So t must be in the interval [t_min, t_max], where:

t_min = ceil( (-a0 *d) / yj )

t_max = floor( (b0 *d) / xj )

But t must be an integer.

Wait, but the way to compute t_min and t_max correctly is a bit tricky. Let me think again.

We have:

a = a0 + (yj/d)*t >=0 → (yj/d)*t >= -a0 → t >= (-a0) *d / yj

Similarly, (xj/d)*t <= b0 → t <= (b0 *d)/xj

But since t must be an integer, t must be >= ceil( (-a0*d)/yj ) and <= floor( (b0*d)/xj )

But wait, here (yj/d) and (xj/d) are integers? Because d is the gcd. For example, since d divides xj and yj, then xj/d and yj/d are co-prime.

Yes. Because d is the gcd of xj and yj. So xj = d * x', yj = d * y', where x' and y' are coprime.

Thus, (yj/d) = y' and (xj/d) =x', which are coprime.

But in any case, the coefficients (yj/d) and (xj/d) are integers.

So in the equations:

t must be >= ceil( (-a0) *d / yj )

Wait, no. Because (yj/d) is an integer. So the equation is:

t >= (-a0) *d / yj 

But since (yj/d) is an integer, perhaps this can be simplified.

Alternatively, since (yj/d) is an integer, let's denote k_step = yj/d, which is an integer.

Then the equation becomes:

t >= (-a0) / k_step

But a0 can be negative. So for example, if a0 is negative, then (-a0) is positive. So t needs to be >= (-a0) /k_step, but since k_step is positive (as yj and d are positive), and t must be an integer.

But perhaps this is getting too complicated. Let's see with an example.

Take xj=2, yj=3, d=1. So k_step =3/1=3.

Suppose a0 is -5. Then, t >= (-a0)/k_step → 5/3 → 1.666..., so t >=2.

Wait, but the equation a0 + k_step *t >=0 → (-5) +3*t >=0 → 3t >=5 → t >= 2 (since t is integer).

Yes. So the minimal t is ceil( ( -a0 ) /k_step ), where k_step is (yj/d).

So in code:

k_step = yj // d  # since yj/d is integer

hmm, but yj is divided by d, which is the gcd. So yes, k_step is integer.

Similarly, for the other condition:

xj/d is xj_step = xj //d.

So the upper bound for t is floor( (b0 *d) / xj ) → but xj =d * xj_step. So (b0 *d)/xj = (b0 *d)/(d *xj_step) )= b0/(xj_step).

So the upper bound is floor( b0 / xj_step ).

But wait, let me re-express:

b = b0 - (xj/d)*t >=0 → (xj/d)*t <=b0 → t <= (b0 *d) / xj → t <= (b0 *d) // xj, if xj and d are positive.

But how to compute these t_min and t_max correctly.

Alternatively, in code:

t_min = (-a0) * d // yj

But since a0 can be negative, and yj is positive.

Wait, for example, a0 is -5, d=1, yj=3.

(-a0 *d) =5*1=5. yj=3.

So 5/3 is 1.666. So ceil(5/3) is 2. But how to compute this in code.

Alternatively, since we have to find t such that (a0 + (yj/d)*t) >=0, and t must be an integer.

Let me rephrase:

(yj/d)*t >= -a0 → t >= (-a0) / (yj/d)

But since yj/d is integer, let's denote y_step = yj/d.

So t >= (-a0) / y_step.

But since t must be an integer, and we can have a0 negative or positive.

Wait, for example:

If a0 is negative, then (-a0) is positive. So (-a0)/y_step could be a positive number. So t must be >= ceil( (-a0)/y_step )

If a0 is positive, then (-a0) is negative, so (-a0)/y_step is negative. So t >= negative number. Since t can be any integer greater than or equal to that, but the other condition (from b) may impose a lower bound.

But perhaps the code can compute t_min as the ceiling of ( -a0 ) / ( y_step ), where y_step = yj//d.

But handling the division correctly when dealing with negative numbers is tricky. So perhaps using the math.ceil function, but considering integer division.

Alternatively, in code, for integer division:

t_min = (-a0 + y_step -1) // y_step 

But perhaps this is not the way. Let's think:

If (-a0) is positive, then dividing by y_step (positive) gives a quotient. To find the ceiling, which is the smallest integer >= quotient.

For example, if quotient is 5/3=1.666, then ceiling is 2. Which can be computed as (5 +3-1)//3 → (7)//3=2.

So in general, for positive numbers, the ceiling of a/b is (a +b-1) //b.

But if a is negative, then a/b could be negative, and the ceiling is different.

Alternatively, to compute the minimal t such that a0 + y_step * t >=0.

Which is equivalent to t >= ceil( (-a0) / y_step )

But in code, using Python's math.ceil could be problematic if dealing with negative numbers. So perhaps better to compute it as:

t_min = max(0, ... )

Wait, perhaps not. Let's see:

If a0 is already >=0, then even t=0 makes a = a0 + y_step*0 =a0 >=0. So in that case, t can be 0.

So t_min is the minimal t where a0 + y_step*t >=0.

But when a0 is negative, then we need t >= ceil( (-a0)/y_step )

So in code:

if a0 >=0:

   t_min can be as low as possible (like negative numbers) but constrained by the other condition (b >=0).

But wait, a0 is part of the particular solution. So perhaps a0 can be negative. For example, if xj=2, yj=3, n=5. Then d=1. The equation 2a +3b=5. A solution is a=5, b= (-5), but this is not acceptable. So then other solutions are needed.

Wait, but the particular solution (a0, b0) is derived from the extended Euclidean algorithm. For example, for xj=2, yj=3, the extended Euclidean gives x0=-1, y0=1, since 2*(-1) +3*1=1. Then, multiply by 5: a0= -5, b0=5. So the particular solution is a0=-5, b0=5. Then, the general solution is a= -5 +3t, b=5 -2t. We need a >=0 and b >=0.

So:

-5 +3t >=0 → t >= 5/3 → t >= 2 (since t must be integer)

5 -2t >=0 → t <=5/2 → t <=2

So t can be 2. Then a=1, b=1. Which gives 2*1 +3*1=5 → correct.

So in this case, the code would compute t_min=2 and t_max=2.

So the code must correctly compute t_min and t_max.

Thus, in code:

We can compute t_min as the ceiling of (-a0) / y_step, where y_step is yj//d.

But how to compute ceiling in Python.

In Python, the ceiling of a division can be computed as (numerator + denominator -1) // denominator.

So for (-a0) / y_step, when (-a0) is positive, but a0 can be negative.

For example, if a0 is -5, then (-a0) is 5. y_step is 3. 5/3 is 1.666, ceiling is 2. So (5 +3-1)//3 →7//3=2.

But if a0 is positive, then (-a0) is negative. For example, a0=5. Then (-a0) is -5. y_step=3. (-5)/3 is -1.666, ceiling is -1. So how to compute that.

But the code needs to handle all possibilities.

Alternatively, perhaps to compute t_min as:

t_min = (-a0 + y_step -1) // y_step if (-a0) >=0 else 0

Wait, no. Because when a0 is negative, (-a0) is positive, and the expression would be (positive + y_step -1) // y_step, which is correct.

If a0 is positive, then (-a0) is negative. So ( -a0 + y_step-1 ) could be (negative + positive). So perhaps that's not the way.

Alternatively, use math.ceil, but handle negative numbers.

But perhaps using the formula:

t_min = (-a0 + y_step -1) // y_step

But let's test this.

Case 1: a0 = -5, y_step=3.

(-a0) =5.

5 +3-1=7 →7//3=2. Correct.

Case 2: a0 =5 → (-a0) =-5.

-5 +3-1 =-3 → -3 //3 =-1. Which is correct, as -5 /3 is -1.666, ceiling is -1.

But when a0 is positive, then a0 + y_step*t >=0.

Wait, a0 is positive, and y_step is positive.

So for t >= (-a0)/y_step → but (-a0) is negative. So (-a0)/y_step is negative.

So t can be any integer >= that negative number. But since a0 is positive, even t=-1 would give a = a0 + (-1)*y_step. For example, a0=5, y_step=3. t=-1 → 5-3=2 >=0. So t can be -1. But in this case, how does it fit with the other condition (b >=0).

So in code, the t_min is the maximum between the minimal t from a's condition and the minimal t from the other conditions.

But perhaps the code should compute t_min as the ceiling of (-a0)/y_step, using the formula (numerator + denominator -1) // denominator.

But perhaps we should compute:

t_min = (-a0 + y_step -1) // y_step

But only if (-a0) is positive. Wait, no. Let's take a0=5, which is positive. (-a0) is -5. So (-a0 + y_step -1) =-5 +3-1 =-3. //3 gives -1.

Which is the ceiling of (-5)/3 =-1.666... → -1. So that's correct.

But for a0=5 and y_step=3, t can be >=-5/3 → >=-1.666. So the minimal t is -1.666 → t >=-1.666. So t can be -1, 0, 1, etc.

So the t_min from a's condition is -1. But the other condition (b >=0) may impose a higher t.

But how to compute t_min and t_max.

Let me re-express:

t must satisfy:

t >= ceil( (-a0) / y_step )

t <= floor( (b0) / x_step )

where x_step = xj//d.

But how to compute ceil and floor correctly.

Alternatively, in code:

from math import floor, ceil

But perhaps using integer division is better.

Let's try to compute t_min and t_max:

t_min = ceil( (-a0) / y_step )

t_max = floor( (b0) / x_step )

But in Python, the division of integers with / results in a float. So perhaps using the formula for ceiling and floor.

But for example:

ceil( (-a0) / y_step ) can be computed as (-a0 + y_step -1) // y_step when (-a0) is positive.

But when (-a0) is negative, then it's equivalent to floor division.

Wait, perhaps this approach:

For any integer a and positive integer b:

ceil(a / b) = (a + b -1) // b

But when a is positive.

If a is negative, then ceil(a/b) is (a) //b.

For example, a=-5, b=3 → (-5)/3 → -1.666 → ceil is -1.

Which is (-5) //3 →-2. But wait, no. Wait, in Python, (-5)//3 is -2. So this approach doesn't work.

So perhaps the formula works only for positive a.

Alternatively, perhaps it's better to use the math.ceil function.

But in code, to compute ceil((-a0)/ y_step), where y_step is positive.

So:

import math

t_min = math.ceil( (-a0) / y_step )

Similarly, t_max = math.floor( (b0) / x_step )

But in Python, if (-a0) is negative, then dividing by a positive y_step gives a negative number, and ceil of that is the correct ceiling.

For example:

a0=5 → -a0=-5. y_step=3. (-5)/3 →-1.666. ceil → -1.

Which is correct.

a0= -5 → -a0=5. 5/3=1.666. ceil →2.

Yes.

Similarly for t_max:

b0=5, x_step=2. 5/2=2.5 → floor is 2.

Yes.

So using math.ceil and math.floor is the way to go.

But in Python, division of integers (using /) results in float, which can lead to precision issues for very large numbers. But given the constraints (xj and yj up to 3e5, n up to 3e5), this should be manageable.

So, code steps for each shop j:

Compute d = gcd(xj, yj)

if n %d !=0 → output -1.

else:

   find x0, y0 using extended Euclidean such that xj*x0 + yj*y0 =d.

   a0 = x0 * (n//d)

   b0 = y0 * (n//d)

   y_step = yj //d

   x_step = xj //d

   t_min = math.ceil( (-a0) / y_step )

   t_max = math.floor( (b0) / x_step )

   possible_ts = all integers t where t >= t_min and t <= t_max.

   for each t in possible_ts:

       a = a0 + y_step *t

       b = b0 - x_step *t

       if a <0 or b <0:

           continue

       k = a *xj

       if k <0 or k >n:

           continue

       if (n -k) % yj !=0:

           continue → but this shouldn't happen.

       possible_k.add(k)

   collect all possible k's, compute sum_b + prefix_sum[k], take maximum.

But how to generate possible_ts? Well, the possible_ts are all integers between t_min and t_max, inclusive.

But if t_min > t_max, then there are no solutions.

But how to iterate them? For example, if t_min is 2 and t_max is 5, then t can be 2,3,4,5.

But given that the step in t is 1, the code can generate all t in this range.

But in practice, the number of possible t's is small. So for each j, we can generate all t's in the range t_min to t_max, compute a and b, and check if they are non-negative.

But how to handle cases where a and b are still negative after adjusting t?

Wait, the t_min is derived to ensure a >=0, and t_max derived to ensure b >=0. So for t in [t_min, t_max], both a and b should be non-negative.

Wait, let's check:

For t >= t_min:

a =a0 + y_step *t >=a0 + y_step * t_min.

But t_min is the minimal t for which a >=0. So for t >=t_min, a >=0.

Similarly, t <= t_max → b =b0 -x_step*t >=0.

So if t is between t_min and t_max, then a and b are non-negative.

But wait, in the example where xj=2, yj=3, n=5:

a0= -5, b0=5.

y_step=3/1=3, x_step=2/1=2.

t_min = ceil(5/3)=2.

t_max = floor(5/2) =2.

So t can only be 2.

a = -5 +3*2=1 >=0.

b=5 -2*2=1 >=0.

So correct.

Another example:

xj=1, yj=1, n=5.

d=1.

x0=1, y0=0 → 1*1 +1*0=1. Then, a0=1*5=5, b0=0*5=0.

y_step=1, x_step=1.

t_min=ceil( (-5)/1 ) = ceil(-5) =-5.

t_max=floor(0 /1 )=0.

So t ranges from -5 to 0.

For each t in that range:

a =5 +1*t → a=5-5=0 (t=-5), then a increases by 1 each step.

b=0 -1*t → for t=-5: 0 - (-5)*1=5.

So possible a and b pairs:

t=-5 → a=0, b=5 → k=0*1=0. sum 0 red, 5 black. 0+5=5? n is 5. So yes.

t=0 →a=5, b=0 →k=5. sum 5 red, 0 black. 5+0=5.

So possible k's are 0 and5.

So the code would generate these and compute the sums.

So the code steps are correct.

Thus, in code:

For each shop j:

Compute d = gcd(xj, yj)

if n %d !=0 → output -1.

Else:

   using extended_gcd, compute x0 and y0.

   a0 =x0*(n//d)

   b0 = y0*(n//d)

   y_step = yj //d

   x_step = xj //d

   t_min = ceil( (-a0) / y_step )

   t_max = floor( (b0) / x_step )

   if t_min > t_max → no solution.

   else:

       collect all possible t in t_min ... t_max.

But what about when y_step is zero? No, since d is the gcd of xj and yj, and yj >=1 (from input constraints, xj and yj are >=1).

So y_step is yj//d >=1 (since yj >=d, since d is the gcd).

Thus, the code can proceed.

Now, the next step is to generate all possible t in t_min to t_max. But when t_min is very low and t_max is very high, this could be O(1) steps.

But in practice, the number of t's is very small, as the step between possible a and b is large.

Thus, the code can loop through all possible t in the range t_min to t_max.

For each t in this range, compute a and b.

But a0 can be very large (positive or negative), but with the t in the range, a and b are non-negative.

Once a and b are computed, compute k =a *xj.

Check if k is between 0 and n, and (n -k) must be divisible by yj. But since the equation is xj*a + yj*b =n, and k =xj*a, (n -k) = yj*b. Since b is non-negative, this must hold.

Thus, (n-k) must be >=0 and divisible by yj. But since yj*b =n -k, and b is non-negative, this is ensured.

So, k is valid if 0 <=k <=n.

Once k is valid, the sum is sum_b + prefix_sum[k].

But wait, prefix_sum[k] is the sum of the top k differences (a_i -b_i). So for the maximum sum, we take the top k differences, add them to sum_b.

Thus, the code can compute for each k the sum, and track the maximum.

Now, the code needs to precompute the sorted differences and their prefix sums.

So steps:

Read n.

Then read n pairs of a_i, b_i.

Compute sum_b as sum of all b_i.

Compute the differences = [a_i -b_i for each dish].

Sort the differences in descending order.

Compute prefix_sum where prefix_sum[0] =0, prefix_sum[1] = differences[0], prefix_sum[2] = differences[0]+differences[1], etc. Up to prefix_sum[n] which is sum of all differences.

Then, for each query shop j:

Process as described.

Now, implementing the extended Euclidean algorithm.

The code for extended Euclidean algorithm in Python:

def extended_gcd(a, b):
    if b ==0:
        return (a, 1, 0)
    else:
        g, x, y = extended_gcd(b, a %b)
        return (g, y, x - (a//b)*y)

This returns (g, x, y) such that a*x + b*y =g.

Yes.

So for xj and yj, compute (g, x0, y0) = extended_gcd(xj, yj).

Then, x0 and y0 are coefficients such that xj *x0 + yj*y0 =g.

But since g is the gcd of xj and yj.

Thus, the code will proceed.

But how to handle cases where xj or yj is zero? But according to the problem statement, xj and yj are >=1. So no problem.

Now, code structure:

Read n.

Read n lines, a_i and b_i.

Compute sum_b = sum(b_i).

differences = sorted([a_i - b_i for a_i, b_i in dishes], reverse=True)

Compute prefix_sum[0] =0, prefix_sum[i] = prefix_sum[i-1] + differences[i-1], for i in 1..n.

Read m.

Read m shops' xj and yj.

For each shop:

Testing against sample input 1.

```python
import sys
import math
from math import gcd


def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        g, x, y = extended_gcd(b, a % b)
        return (g, y, x - (a // b) * y)

def main(input_stream, output_stream):
    input = input_stream.read
    data = input().split()
    ptr = 0
    
    n = int(data[ptr])
    ptr +=1
    
    sum_b = 0
    diffs = []
    for _ in range(n):
        a = int(data[ptr])
        b = int(data[ptr+1])
        ptr +=2
        sum_b += b
        diffs.append(a - b)
    
    diffs.sort(reverse=True)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + diffs[i]
    
    max_prefix = max(prefix_sum)
    
    m = int(data[ptr])
    ptr +=1
    
    results = []
    for _ in range(m):
        xj = int(data[ptr])
        yj = int(data[ptr+1])
        ptr +=2
        
        if xj == 1 and yj == 1:
            results.append(sum_b + max_prefix)
            continue
        
        d = gcd(xj, yj)
        if n % d != 0:
            results.append(-1)
            continue
        
        g, x0, y0 = extended_gcd(xj, yj)
        a0 = x0 * (n // d)
        b0 = y0 * (n // d)
        
        y_step = yj // d
        x_step = xj // d
        
        numerator_t_min = -a0
        t_min = math.ceil(numerator_t_min / y_step) if y_step != 0 else 0
        numerator_t_max = b0
        t_max = math.floor(numerator_t_max / x_step) if x_step !=0 else 0
        
        if t_min > t_max:
            results.append(-1)
            continue
        
        max_sum = -float('inf')
        step_k = xj * yj // d
        
        for t in range(t_min, t_max + 1):
            a = a0 + y_step * t
            b_val = b0 - x_step * t
            if a < 0 or b_val < 0:
                continue
            k = a * xj
            if k < 0 or k > n:
                continue
            if k <= n:
                current_sum = sum_b + prefix_sum[k]
                if current_sum > max_sum:
                    max_sum = current_sum
        
        if max_sum == -float('inf'):
            results.append(-1)
        else:
            results.append(max_sum)
    
    output_stream.write('\n'.join(map(str, results)) + '\n')



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10
3 1
2 3
1 1
2 1
6 3
1 4
4 3
1 3
5 3
5 4
10
8 10
9 3
1 4
2 5
8 3
3 5
1 6
7 2
6 7
3 1
""",
            "output": \
"""\
26
-1
36
30
-1
26
34
26
-1
36
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

Thus, the code handles this case.

Thus, the code is correct.

Now, the code needs to:

- Precompute the sorted differences and prefix_sum.

- Precompute max_prefix_sum.

- For each shop, handle the case xj=1 and yj=1 specially.

Thus, the code can be written as follows.
</think>

```python
import sys
import math
from math import gcd

def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        g, x, y = extended_gcd(b, a % b)
        return (g, y, x - (a // b) * y)

def main():
    input = sys.stdin.read
    data = input().split()
    ptr = 0
    
    n = int(data[ptr])
    ptr +=1
    
    sum_b = 0
    diffs = []
    for _ in range(n):
        a = int(data[ptr])
        b = int(data[ptr+1])
        ptr +=2
        sum_b += b
        diffs.append(a - b)
    
    diffs.sort(reverse=True)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + diffs[i]
    
    max_prefix = max(prefix_sum)
    
    m = int(data[ptr])
    ptr +=1
    
    results = []
    for _ in range(m):
        xj = int(data[ptr])
        yj = int(data[ptr+1])
        ptr +=2
        
        if xj == 1 and yj == 1:
            results.append(sum_b + max_prefix)
            continue
        
        d = gcd(xj, yj)
        if n % d != 0:
            results.append(-1)
            continue
        
        g, x0, y0 = extended_gcd(xj, yj)
        a0 = x0 * (n // d)
        b0 = y0 * (n // d)
        
        y_step = yj // d
        x_step = xj // d
        
        numerator_t_min = -a0
        t_min = math.ceil(numerator_t_min / y_step) if y_step != 0 else 0
        numerator_t_max = b0
        t_max = math.floor(numerator_t_max / x_step) if x_step !=0 else 0
        
        if t_min > t_max:
            results.append(-1)
            continue
        
        max_sum = -float('inf')
        step_k = xj * yj // d
        
        for t in range(t_min, t_max + 1):
            a = a0 + y_step * t
            b_val = b0 - x_step * t
            if a < 0 or b_val < 0:
                continue
            k = a * xj
            if k < 0 or k > n:
                continue
            if k <= n:
                current_sum = sum_b + prefix_sum[k]
                if current_sum > max_sum:
                    max_sum = current_sum
        
        if max_sum == -float('inf'):
            results.append(-1)
        else:
            results.append(max_sum)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    main()
```
