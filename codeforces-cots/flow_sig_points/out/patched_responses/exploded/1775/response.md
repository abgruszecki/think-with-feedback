<think>
Okay, let's tackle this problem. So the task is to find the maximum sum of ti values by selecting a subset of sculptures that form a regular polygon. The key point here is that after melting some sculptures, the remaining ones must form a regular polygon, which means their arrangement has to be such that they are equally spaced around the circle. 

First, I need to understand what possible regular polygons can be formed by selecting a subset of the original n sculptures. Since the original arrangement is a regular n-gon, any regular k-gon that is a subset must have k that divides n, right? Because for the remaining sculptures to form a regular polygon, the number of vertices k must be a divisor of n. Wait, no. Wait, maybe not exactly. Let's think. 

For example, if n is 8, then possible k values are 4 (step 2), 2 (step 4), but wait, a regular polygon must have at least 3 sides. So the possible k values are all divisors d of n where d >=3. Or maybe not exactly divisors. Let's see: if the original has 8 sculptures arranged in a circle, and we want a regular k-gon, then the step between chosen sculptures must be the same. For example, in the first sample, n=8, and the chosen step is 2, which skips every other sculpture, leaving 4. So the step here is 2, and 8/step =4. So the step must be a divisor of n. Because, to form a regular k-gon, each step between consecutive selected sculptures is n/k steps apart. Because if you take every m-th step, then the total number of steps needed to wrap around is k = n/m. So m must divide n. Therefore, the possible values of k are the divisors of n, but such that k >=3 and k <=n. Wait, no. Because m is the step. So m can be any integer such that when you take steps of m, you end up with exactly k steps, which is n / gcd(n, m). Wait, maybe I'm getting confused here. Let me think again.

Suppose n is 6. If we choose a step of 2, then the selected positions are 1,3,5,1. Wait, that's only 3 distinct positions. So step 2 gives a 3-gon. So here, k is 3. So for n=6, possible k's are 3, 2 (step 3, but 2 is less than 3, so invalid). Wait, but the problem states that the remaining must form a regular polygon with at least 3 vertices. So for n=6, possible steps could be 1 (k=6), 2 (k=3), 3 (k=2, which is invalid), etc. Wait, but the step m must be such that the number of selected sculptures is at least 3. So the possible m's are those where n / gcd(n, m) >=3. Because when you take steps of m, the number of steps before you loop back is n/gcd(n,m). For example, if n=8 and m=2, then gcd(8,2)=2, so the number of distinct positions is 8/2=4, which is 4, forming a square (4-gon). So for each possible divisor d of n, such that d >=3, the step would be n/d. Wait, perhaps the correct approach is to find all possible divisors d of n where d >=3. Or maybe, all possible divisors of n that are >=3. Because when you select a step of m, the number of selected sculptures is n/gcd(n,m). So for each possible d that is a divisor of n and d >=3, we can check all possible steps that would lead to exactly d sculptures. Wait, maybe not. Let me think again. For example, if n=6, the divisors of 6 are 1,2,3,6. But when you take step 2, the number of selected is 3. So d=3, which is a divisor. So perhaps the possible values of k (number of vertices) are all the divisors of n that are >=3 and <=n. So for each possible k that divides n and is >=3, we can check all possible step sizes m where m = n/k. Because if the step is m, then since we need to end up with exactly k sculptures, then the number of steps is k. So m is such that m = n/k. But m must be an integer? Wait, no. Because when you take steps of m, the number of distinct positions you can visit is n/gcd(n, m). So for example, n=6, m=2: gcd(6,2)=2, so number of positions is 6/2=3. So here, k=3. So m can be any integer where gcd(n, m) = n/k. Wait, perhaps it's easier to iterate over all possible possible k values that are divisors of n, and for each such k, compute the maximum sum.

Wait, but how do we find all possible k values that are possible for the given n. For example, for n=8, possible k values could be 4 (step 2), 8 (step 1), but also, wait, for example, if n=6, can you have a 2-gon? But the problem requires k >=3. So the possible k values are divisors of n (including n itself) that are >=3. Wait, but n itself is allowed (since the problem says "it is allowed not to melt any sculptures at all"). So for each possible k that divides n, and k >=3, we can check the sum for all possible step sizes. Wait, but maybe there's a mistake here. Because perhaps there are other k values possible where k is not a divisor of n. For example, let's take n=6. Suppose we take step 3. Then the selected positions are 1 and 4, which is a 2-gon (invalid). So steps that don't divide n correctly can't form a polygon with k >=3. Therefore, the only possible valid k values are those that are divisors of n (since n/k must be an integer for the step m). So the correct approach is to iterate over all divisors d of n where d >=3. But wait, for example, n=8, the divisors are 1,2,4,8. So possible k values are 4,8. But the sample input 1 has a solution where k=4 (sum is 2+4+5+3=14). So that works. So for each d in the divisors of n where d >=3, we can calculate the maximum possible sum by checking all possible starting points and steps.

Wait, but how? For a given d (a divisor of n, >=3), the step is m = n/d. For example, if d=4 and n=8, m=2. Then, the selected positions are 1,3,5,7. Or 2,4,6,8. Or any starting position. So for each possible divisor d, the possible step is m = n/d, and the number of possible starting positions is m. Because for each starting position from 0 to m-1 (assuming 0-based or 1-based?), the selected sculptures are s, s+m, s+2m, ..., modulo n. So for each d, we need to check all possible starting positions and compute the sum. Then take the maximum among all possible sums for all d.

Wait, but when d is fixed, the step is m = n/d. Then, for each starting position s (ranging from 0 to m-1), the sum would be the sum of t[s], t[s+m], t[s+2m], ..., up to d terms. For example, n=8, d=4, m=2. Starting positions can be 0 and 1. For starting at 0: 1,3,5,7 (indices 0-based?), so sum t[0] + t[2] + t[4] + t[6] (assuming the list is 0-based). Wait, the sample input 1 is 8 elements. The input list is 1,2,-3,4,-5,5,2,3. So indices 0-7. The solution in the sample leaves every second sculpture, which would be positions 1 (2), 3 (4), 5 (5), 7 (3). So sum 2+4+5+3=14. So in this case, the starting position is 1 (0-based?), and step 2. But for d=4 (number of selected sculptures), m=2. So starting positions can be 0 or 1. Because when m=2, the possible starting positions are 0,1, ..., m-1. So for each d, m = n/d, and for each s in 0..m-1, we can compute the sum of the d elements starting at s, stepping by m. Then, among all these sums for all d and all possible s, we take the maximum.

So the approach is:

1. Find all divisors d of n where d >=3.

2. For each such d, compute m = n/d.

3. For each starting position s from 0 to m-1:

   a. Sum the elements at positions s, s+m, s+2m, ..., s+(d-1)m. But since the list is circular (the sculptures are arranged in a circle), when the indices go beyond n, they wrap around. But since m*d = n, adding d steps of m will wrap around exactly once, so all positions are within 0 to n-1.

4. Keep track of the maximum sum encountered.

Additionally, since the problem allows not melting any sculptures (d = n), which is a divisor of n (since n/n=1, which is a divisor). So d can be n if n >=3.

So the steps are:

- Generate all possible d where d is a divisor of n, d >=3, and d <=n.

Wait, but n can be 3, so d=3 is allowed.

So first, for the given n, find all possible d's (divisors of n) that are >=3.

But how to find all divisors of n?

We can generate all divisors of n by checking from 1 to sqrt(n), and for each divisor pair (d, n/d). Then collect all divisors, and then filter those >=3.

Wait, but in the problem statement, the allowed k is between 3 and n, inclusive. So for example, if n=4, the divisors are 1,2,4. So allowed d's are 4 (since 4 >=3). So for each d, check if d is >=3.

But for n=4, the possible k is 4 (the original arrangement) or 2 (but 2 is less than 3, so invalid). So d must be 4 in this case.

So the plan is:

1. Generate all divisors of n, including n itself.

2. For each divisor d, check if d >=3. If yes, add to the list of possible d's.

3. For each such d, compute m = n/d.

4. Then, for each starting position s in 0 to m-1:

   a. Compute the sum of the elements at positions s, s + m, s+2m, ..., s + (d-1)*m.

   b. Keep track of the maximum sum.

But for large n (up to 20000), how efficient is this approach?

Let's analyze the time complexity.

Suppose n is up to 20000. The number of divisors of n is up to O(200) (since the number of divisors for a number up to 2e4 is small). For example, 20000 has divisors like 1, 2, 4, 5, 8, 10, etc. So the number of possible d's is manageable.

For each d, m = n/d. Then, for each s in 0..m-1, we have to compute the sum of d elements. For each sum, the number of elements is d, and the number of starting positions is m.

So for each d, the time complexity is O(m * d) = O(n). Because m*d = (n/d)*d = n. So for each d, the time is O(n). So if the number of divisors is O(k), the total time is O(k * n). Since k is small (like up to 100), this would be acceptable for n up to 2e4. Because 2e4 * 100 = 2e6, which is manageable.

But wait, wait. Let's see. For example, for n=20000, if the divisors are d=20000, 10000, 5000, etc. For d=20000, m=1. Then for each s in 0 to 0 (since m=1), compute sum of 20000 elements. But that's just the sum of all elements. So for d=20000, we compute sum of all elements once.

But for d=10000, m=2. So m=2. So for s=0 and 1:

sum the elements at 0, 2, 4, ..., 19998 (total 10000 elements).

Similarly for s=1: 1,3,5, ..., 19999.

Each sum takes O(10000) steps for each s, but m=2, so two sums. So total steps for d=10000 is 2*10000 = 20000 steps.

Similarly for other d's. So the total steps for all d's is O(n * number of divisors). Since n is 2e4 and number of divisors is up to 100 (probably less), this would be 2e6 steps, which is acceptable.

So the approach is feasible.

Now, the next step is to generate all divisors of n, filter those >=3, then for each d, generate the possible sums and track the maximum.

But how to generate all divisors of n?

We can generate them by checking all possible numbers from 1 to sqrt(n), and for each i that divides n, add i and n/i to the list of divisors. Then, after generating all divisors, we need to process them, remove duplicates, filter those >=3.

For example, for n=8:

divisors are 1, 2,4,8. After filtering, 4 and 8 are >=3.

So possible d's are 4,8.

Wait, but 8 is allowed as well (as not melting any sculptures). So for each d, compute m = n/d. For d=4, m=2. So starting positions 0 and 1. For each starting position, sum 4 elements stepping by 2.

For d=8, m=1. So starting position is 0. Sum all 8 elements.

Now, in the sample input 1, the sum for d=8 would be 1+2-3+4-5+5+2+3= (1+2) is 3, -3 gives 0, +4=4, -5= -1, +5=4, +2=6, +3=9. So sum is 9. But the maximum in the sample is 14, which comes from d=4, starting position 1.

So the code would correctly choose that.

Now, how to generate all divisors:

Function to generate all divisors:

def get_divisors(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    return sorted(divisors)

But after generating, we need to filter the divisors >=3.

Wait, but for example, if n=6:

divisors are 1, 2, 3,6. After filtering, 3,6.

So possible d's are 3 and 6.

For each d:

d=3: m=2. starting positions 0,1.

sum for starting 0: positions 0,2,4 (elements 1, -3,5) sum 1-3+5=3.

starting 1: positions 1,3,5 (elements 2,4,-6) sum 2+4-6=0. So maximum for d=3 is 3.

d=6: m=1. sum all elements. sum 1-2+3-4+5-6= (1-2) =-1, +3=2, -4= -2, +5=3, -6= -3. sum is -3. So maximum is 3.

But the sample input 2 for n=6 has output 9. Wait, sample input 2 is:

6

1 -2 3 -4 5 -6

The output is 9. How does that happen?

Wait, sample input 2's solution is to choose every other element. Let's see. The divisors of 6 are 1,2,3,6. So allowed d's are 3,6.

For d=3, m=2.

starting positions 0 and 1.

sum for s=0: 1 +3 +5 =1+3+5=9.

sum for s=1: -2 + (-4) + (-6) =-12.

So maximum here is 9. So the maximum sum is 9, which is achieved by d=3, s=0.

So in that case, the code would find this sum.

So the approach is correct.

Now, the steps to code this:

1. Read n and the list of t_i.

2. Generate all divisors of n.

3. Filter the divisors to those >=3.

4. For each d in the filtered list:

   a. Compute m = n // d.

   b. For each s in 0 to m-1:

      i. Compute the sum of elements at positions s + k*m for k in 0..d-1.

      ii. Update the maximum sum if this sum is larger.

5. The maximum sum found is the answer.

But wait, the code needs to handle 1-based indices. Because the problem states that the sculptures are numbered 1 to n, but in code, we'll probably process as 0-based.

But when we step through the indices, adding m each time (mod n), but since the indices are arranged in a circle, and m*d =n, stepping m each time will loop after d steps.

So for example, in 0-based indices, the positions are s, s+m, s+2m, ..., s + (d-1)*m. Since m*d =n, adding m d times would be s + m*d = s +n, which mod n is s again. So the indices are correctly computed as (s + k*m) % n for k in 0 to d-1. However, since m*d =n, each step m brings us to the next position in the cycle.

But since m*d =n, the indices for s, s+m, s+2m, ... s+(d-1)*m are all within 0 to n-1. So modulo n is not needed. For example, s=0, m=2, d=4 for n=8:

0, 2,4,6: all within 0-7.

So, in code, for each s in 0 to m-1:

sum the elements at s, s+m, s+2m, ..., s + (d-1)*m.

Which is equivalent to sum( t[ s + k*m ] for k in 0..d-1 )

So the code can compute this sum by iterating k from 0 to d-1, adding m each time.

Now, for each d and s, the time is O(d). For m steps and each step O(d), the total for each d is O(m*d) = O(n).

So, the code can handle this.

Now, the problem is to implement this efficiently.

But with n up to 2e4, and for each d in the divisors, this is manageable.

So now, the code steps.

First, read n and the list t.

Then, compute the divisors of n.

Then filter the divisors >=3.

But what about the case where no divisors are >=3? For example, if n=3, then divisors are 1,3. So d=3 is allowed. So sum all elements.

If n=4, divisors are 1,2,4. So allowed d's are 4. So sum all elements.

Wait, but what if n is 2? But the constraints say n >=3.

So the code can safely proceed.

Now, code for generating the divisors:

In Python:

import math

def get_divisors(n):
    divisors = set()
    for i in range(1, int(math.isqrt(n)) +1):
        if n % i ==0:
            divisors.add(i)
            divisors.add(n//i)
    return sorted(divisors)

Then, filter the divisors to those >=3.

But in case after filtering, there are no divisors >=3, which can happen? For example, if n=3, the divisors are 1,3. So 3 is allowed.

If n=4, divisors >=3 are 4.

Wait, so for all n>=3, the divisors list will have at least one element (the n itself, which is a divisor of n and >=3). Because when you divide n by 1, you get n. So for n >=3, the list of allowed d's will have at least d =n.

So the code can proceed.

Once we have the list of allowed d's, for each d, compute m =n//d.

Wait, since d is a divisor of n, m =n//d is an integer. So for example, n=8, d=4, m=2.

Then, for each s in 0 to m-1:

sum the elements s, s+m, s+2m, ..., s + (d-1)*m.

But how to compute this sum efficiently.

The straightforward approach is for each s:

current_sum = 0

for k in 0 to d-1:

    current_sum += t[s + k*m]

But for large d (like d=20000, m=1), this would require 20000 operations. But even that is manageable.

But for Python, with list comprehensions and generators, perhaps precomputing the sum for all possible steps would be better. But given the constraints, even the straightforward approach would work.

Now, let's test the sample input 1:

Sample input 1:

8

1 2 -3 4 -5 5 2 3

t = [1,2,-3,4,-5,5,2,3]

divisors of 8 are 1,2,4,8. allowed d's are 4,8.

For d=8, m=1. s can be 0. sum all elements: 1+2-3+4-5+5+2+3 = (1+2=3) + (-3=0) +4=4 + (-5= -1) +5=4 +2=6 +3=9. sum is 9.

For d=4, m=2. s can be 0 or 1.

s=0:

sum elements 0,2,4,6: t[0]=1, t[2]=-3, t[4]=-5, t[6]=2. sum is 1-3-5+2= -5.

s=1:

sum elements 1,3,5,7: t[1]=2, t[3]=4, t[5]=5, t[7]=3. sum is 2+4+5+3=14.

So maximum is 14.

Sample input 2:

6

1 -2 3 -4 5 -6

divisors are 1,2,3,6. allowed d's are 3,6.

d=3, m=2. s can be 0 or 1.

s=0: sum 0,2,4: t[0]=1, t[2]=3, t[4]=5. sum 9.

s=1: t[1]=-2, t[3]=-4, t[5]=-6. sum -12.

d=6: sum all elements. sum 1-2+3-4+5-6 = (1-2) =-1 +3=2 -4= -2 +5=3 -6= -3.

so maximum is 9.

Sample input 3:

6

1 2 3 4 5 6.

divisors allowed are 3,6.

d=3, m=2. s can be 0 or 1.

s=0: sum 1,3,5 → 1+3+5=9.

s=1: sum 2,4,6 → 2+4+6=12.

d=6: sum all elements. 21.

so maximum is 21.

Which matches the sample.

So code seems correct.

Now, code steps:

Read n.

Read list t as integers.

Generate divisors.

filter divisors >=3.

max_sum = -infinity.

for each d in divisors:

    m = n // d

    for s in 0..m-1:

        current_sum = sum(t[s + k*m] for k in range(d))

        if current_sum > max_sum:

            max_sum = current_sum

return max_sum.

But for n=2e4 and d=2e4, m=1. Then s=0. sum all elements. So sum is O(2e4) steps.

But with n up to 2e4 and divisors up to 200 (for example), the total steps are 2e4 * 200 = 4e6, which should be manageable.

But in Python, loops can be slow. So how to optimize.

Alternative approach: precompute for each possible step m, and for each possible starting s, the sum. But perhaps we can find a way to compute the sums more efficiently.

But for each d, m =n/d. For each s in 0..m-1, the sum is the sum of t[s], t[s+m], ..., t[s + (d-1)*m].

But each of these sums is a sum of every m-th element starting at s, with a total of d elements.

In Python, list slicing with steps can be used. For example, for s and m, the indices are [s, s+m, s+2m, ...] but since m*d =n, this will wrap around. Wait, no. Because m*d =n. So for example, when s is 0 and m=2, d=4 (n=8), the indices are 0,2,4,6. So no wrapping.

So for s in 0 to m-1, the indices are s, s+m, s+2m, ..., s + (d-1)*m. Each of these is within 0 to n-1, since (d-1)*m = (n/d -1) * m = (m*d/d -1)*m = (m -1)*m. Wait, no: m =n/d. So (d-1)*m = (d-1) * (n/d). But since d is a divisor of n, (d-1)*m = (d-1)* (n/d) = (n/d)*(d-1) = n - (n/d). So for example, when d=4, m=2, (d-1)*m=3*2=6. So 0+6=6 <8.

So all indices are valid.

So in Python, for s and m, the sum can be computed as:

sum(t[s::m][:d])

Wait, because s::m gives elements starting at s, stepping by m. But when m is larger than 1, the slice would be [s, s+m, s+2m, ...]. But in Python, the step is the third parameter. So t[s::m] creates a list starting at index s, then s+m, s+2m, etc., until the end of the list. But since m*d =n, the list would have exactly d elements. So t[s::m] would be of length (n - s) // m + 1 if (n-s) % m ==0, but in our case, since m*d =n, s <m (since s ranges from 0 to m-1), so (n -s) >= m*(d-1) +1. For example, s=0, m=2, n=8. 0 + 3*2 =6 <8. So 0::2 is [0,2,4,6] → 4 elements. Which is correct.

So for s in 0..m-1, t[s::m] will have exactly d elements. So sum(t[s::m]) would give the correct sum.

Wait, but m is n/d. For example, m=2, d=4, n=8. s=0: t[0::2] → indices 0,2,4,6 → 4 elements. Which is correct.

So for each s and m, the sum can be computed as sum(t[s::m]).

But in Python, the step in slice is the third argument. So [s::m] would start at s, step by m. So this is correct.

So the code can be optimized by replacing the loop over k with a slice and sum.

So for each d in allowed_ds:

m = n // d

for s in range(m):

    current_sum = sum( t[s::m] )

    max_sum = max( max_sum, current_sum )

Wait, but for the slice s::m, the elements are s, s+m, s+2m, etc. But for m=2 and n=8, this gives 4 elements. Which is correct.

So this approach would be more efficient in Python, as it uses slicing and built-in sum, which is faster than an explicit loop.

Yes, but in the code, when m is large (like m=20000), the slice s::m would be just a single element (s) when d=1. But since d must be >=3, that case is not possible. Because m =n/d, and d >=3 → m <=n/3. So for n=20000, m can be up to 20000/3 ≈6666. So for s in 0..m-1, and m=6666, the slice s::m would start at s and step m=6666. For example, s=0: 0, 6666, 13332, ... But m*d =n →6666*d =20000 → d=20000/6666. But 20000 divided by 6666 is 3. So m=6666, d=3. So the slice would have 3 elements: 0, 6666, 13332. Which are valid indices (assuming 20000 is divisible by 3, but 20000/3 is 6666.666..., which is not possible. Wait, but in code, for d to be a divisor of n. So m =n/d must be an integer.

So in code, for allowed_ds, m is n/d, which is integer, so s::m will have exactly d elements.

So the code can be written as:

import math

n = int(input())
t = list(map(int, input().split()))

divisors = set()
for i in range(1, int(math.isqrt(n)) + 1):
    if n % i == 0:
        divisors.add(i)
        divisors.add(n // i)

allowed_ds = [d for d in divisors if d >=3]

max_sum = -float('inf')

for d in allowed_ds:
    m = n // d
    for s in range(m):
        current_sum = sum(t[s::m][:d])  # slice up to d elements to prevent issues if s + ... exceeds the list
        if current_sum > max_sum:
            max_sum = current_sum

print(max_sum)

Wait, but in the case where s::m has more than d elements, but that's not possible here. Because for d elements, m =n/d, and s <m. So s + (d-1)*m = s + (d-1)*n/d. Since s < m =n/d → s <n/d → s + (d-1)*n/d < n/d + (d-1)*n/d = d*n/d =n. So all indices are within the list. So the slice t[s::m] will have exactly d elements. So the [:d] is redundant but safe.

Alternatively, since we know the slice will have exactly d elements, we can omit it. But including it doesn't hurt.

But for code correctness, perhaps it's better to include it.

Testing sample input 1:

t = [1,2,-3,4,-5,5,2,3]

allowed_ds =4 and 8.

For d=4, m=2.

s ranges from 0 to 1.

s=0: t[0::2] → [1, -3, -5, 2], sum 1-3-5+2 =-5.

s=1: t[1::2] → [2,4,5,3], sum 14.

So correct.

Sample input 3:

t = [1,2,3,4,5,6]

allowed_ds are 3,6.

d=6: m=1.

s=0: t[0::1] is the whole list. sum is 21.

So code works.

So this code should handle all cases correctly.

But what about when n is a prime number. For example, n=5. Divisors are 1,5. So allowed_ds is 5. So m=1. So sum all elements.

Which is correct.

But what if n is 7. The divisors are 1,7. So allowed_ds is 7. So code will sum all elements.

But if there is a better way to melt some sculptures. But no, because any subset of 7 elements must form a regular polygon. So the only possible is to leave all 7, since any other subset would have a number of elements that does not divide 7. For example, 3 elements would require step 7/3, which is not integer. So not possible.

Thus, the code is correct.

Now, let's test for n=4, allowed_ds=4. m=1. So s=0: sum all elements.

So code works.

Thus, the code should handle all cases correctly.
</think>

To solve this problem, we need to find the maximum sum of attractiveness values of sculptures arranged in a regular polygon after melting some sculptures. The key insight is that the remaining sculptures must form a regular polygon, which means the number of remaining sculptures must be a divisor of the original number of sculptures, `n`, and must be at least 3.

### Approach
1. **Identify Divisors**: Generate all divisors of `n` that are greater than or equal to 3. These divisors represent the possible number of vertices in the regular polygons we can form.
2. **Check Each Divisor**: For each divisor `d`, determine the step size `m` (which is `n // d`). This step size allows us to check every possible starting position and sum the values of the sculptures at those positions.
3. **Calculate Sums**: For each starting position from 0 to `m-1`, compute the sum of the values of the sculptures that form a regular polygon. Track the maximum sum encountered.

### Solution Code
```python
import math

n = int(input())
t = list(map(int, input().split()))

divisors = set()
for i in range(1, int(math.isqrt(n)) + 1):
    if n % i == 0:
        divisors.add(i)
        divisors.add(n // i)

allowed_ds = [d for d in divisors if d >= 3]

max_sum = -float('inf')

for d in allowed_ds:
    m = n // d
    for s in range(m):
        current_sum = sum(t[s::m][:d])
        if current_sum > max_sum:
            max_sum = current_sum

print(max_sum)
```

### Explanation
1. **Divisors Identification**: We generate all divisors of `n` by iterating up to the square root of `n`. For each divisor found, both the divisor and its complement (i.e., `n // divisor`) are added to the set of divisors.
2. **Filtering Valid Divisors**: We filter out divisors that are less than 3, as the problem requires at least 3 vertices for a valid polygon.
3. **Sum Calculation**: For each valid divisor `d`, we compute the step size `m = n // d`. We then check every possible starting position from 0 to `m-1` and calculate the sum of the values of the sculptures at intervals of `m`. The maximum sum encountered during these calculations is tracked and printed as the result.

This approach efficiently checks all possible regular polygons that can be formed by the remaining sculptures, ensuring optimal performance even for the upper constraint limits.