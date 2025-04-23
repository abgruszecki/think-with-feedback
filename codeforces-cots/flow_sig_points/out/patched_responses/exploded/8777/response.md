<think>
Okay, let's tackle this problem. Hmm. So the problem is about finding the minimal v such that we can present cnt1 numbers to the first friend and cnt2 to the second, with all numbers distinct and not containing any forbidden multiples. The first friend can't have numbers divisible by x, and the second can't have any divisible by y. And all presented numbers must be unique between the two friends.

So, how do we approach this? Let's think step by step.

First, the key is to model the available numbers and how they can be allocated. Since x and y are primes, that helps with certain calculations. But since x and y might be the same or different, we need to consider their LCM (least common multiple) as well, right?

Wait, the problem says x and y are primes. Oh, right. So if x and y are the same, then their LCM is x. Otherwise, it's x*y. Because primes have no common divisors except 1.

So, for a given v, how many numbers can each friend take? Let's break it down.

The first friend can take numbers not divisible by x. The second can take numbers not divisible by y. And the numbers can't overlap between them.

But how to calculate the maximum possible numbers we can assign to each, given v, and then check if that's enough to satisfy cnt1 and cnt2?

Alternatively, perhaps we can model this as a binary search problem. Since we need to find the minimal v, binary search makes sense here. We can check for a given v whether it's possible to assign the required numbers. The question is how to compute the possible maximum numbers that can be allocated for each friend given v.

So the plan is: perform a binary search on possible v values. For each candidate v, determine if it's possible to allocate cnt1 numbers to the first friend and cnt2 to the second, given the constraints.

Now, the key is to compute for a given v, the maximum possible numbers available for each friend, considering overlaps and exclusions.

Let's think about the available numbers:

Numbers not divisible by x: count is A = v - floor(v/x).

Numbers not divisible by y: count is B = v - floor(v/y).

But some numbers are not divisible by either x or y. Also, numbers that are divisible by both x and y can't be given to either friend. Wait, no. Wait, if a number is divisible by x, the first friend can't take it. If it's divisible by y, the second friend can't take it. But if a number is divisible by both x and y (since x and y are primes, this is LCM(x,y) = x*y), then neither friend can take it. So such numbers are excluded from both.

So the total numbers that can be allocated to either friend are those numbers that are not divisible by x (for the first) and not divisible by y (for the second), and each number can be assigned to exactly one friend.

Wait, but a number that is not divisible by x or y can be given to either friend, but not both. So we need to split those between the two friends.

Let me model this:

For a given v, the available numbers can be categorized into:

1. Divisible by x: cannot go to friend1.

2. Divisible by y: cannot go to friend2.

3. Divisible by both x and y: cannot go to either.

4. Not divisible by x or y: can go to either, but not both.

So let's compute:

Total available for friend1: numbers not divisible by x. Which is A = v - (v//x). But among these, some numbers are not allowed for friend1 (but they are allowed for friend2 if they are not divisible by y). Wait, no. Wait, the numbers available for friend1 are those not divisible by x. But among those, some might be divisible by y. Those can't go to friend2. Wait, no. For example, a number divisible by y but not x can go to friend1, because friend1's restriction is only x. But friend2 can't take it because it's divisible by y.

Wait, the problem says all presented numbers must be distinct. So each number can be in either friend1's set, friend2's set, or neither, but not both.

So for a given number, if it's divisible by x, it can't be in friend1's set. But if it's not divisible by x, friend1 can take it. However, if it's not divisible by x but is divisible by y, then friend2 can't take it. So such a number can only be given to friend1, if possible.

Similarly, if a number is not divisible by x or y, then it can be given to either, but once given to one, the other can't take it.

So the problem is to split the numbers into two groups (friend1 and friend2) such that:

- friend1's group has cnt1 numbers, none divisible by x.

- friend2's group has cnt2 numbers, none divisible by y.

- All numbers in both groups are distinct.

So how do we model the maximum possible allocation for a given v?

We can model this by considering the following steps:

The total numbers available for friend1 is A = numbers not divisible by x: A = v - v//x.

Similarly, for friend2, B = numbers not divisible by y: B = v - v//y.

But there is an overlap between A and B: numbers not divisible by x or y. Let's compute that. The count of numbers not divisible by x and not divisible by y is C = v - (v//x + v//y - v//(x*y)). Because inclusion-exclusion: numbers not divisible by x or y is total minus (divisible by x + divisible by y) plus divisible by both (since they are subtracted twice).

So C = v - (v//x + v//y - v//lcm(x,y)), where lcm(x,y) is x*y since x and y are primes.

So the numbers that can be allocated to either friend are C. But the rest (A - C) are numbers not divisible by x but divisible by y. Those can only be given to friend1. Similarly, (B - C) is the numbers not divisible by y but divisible by x, which can only be given to friend2.

Wait, wait. Let's think:

Numbers not divisible by x (A) include:

- Numbers not divisible by x, but divisible by y: count is (v//y - v//(x*y)).

Because numbers divisible by y but not x is v//y - v//(lcm(x,y)) since lcm is x*y here.

Similarly, numbers not divisible by y (B) include:

- Numbers not divisible by y but divisible by x: count is v//x - v//(x*y).

So for the numbers available to friend1 (A), some are in A only (since they are divisible by y but not x). Those numbers can only be given to friend1. Similarly, the B numbers that are in B only (divisible by x but not y) can only be given to friend2.

The C numbers (not divisible by x or y) can be given to either, but need to be split between the two friends.

So the maximum possible allocation is:

friend1 can take (A_available) = (A - C) + s, where s is the number of C numbers allocated to friend1.

friend2 can take (B_available) = (B - C) + t, where t is the number of C numbers allocated to friend2.

But s + t <= C (since each C number can go to one or none).

Moreover, to satisfy the required cnt1 and cnt2:

friend1 needs to have at least (required1) = max(0, cnt1 - (A - C)) allocated from the C pool.

Similarly for friend2: required2 = max(0, cnt2 - (B - C)).

The sum of required1 and required2 must be <= C.

Wait, perhaps not exactly. Let's model it more carefully.

The minimal numbers that need to be taken from C:

The friend1's required count is cnt1. The maximum possible numbers they can take without using C is (A - C) — which is the numbers in A but not in B (since those are in A but divisible by y, which can only be given to friend1). So the friend1 must take at least max(0, cnt1 - (A - C)) from C.

Similarly, friend2 must take at least max(0, cnt2 - (B - C)) from C.

If the sum of these two required from C is <= the total available C, then it's possible.

So the condition is:

max(0, cnt1 - (A - C)) + max(0, cnt2 - (B - C)) ) <= C.

If this is true, then the allocation is possible.

Because then, the C numbers can cover the required.

So for a given v, the check is:

Compute A = v - (v // x)

B = v - (v // y)

C = v - (v//x + v//y - v//(x*y))

Then:

required1 = max(0, cnt1 - (A - C)) --> because A - C is the numbers in A that are not in B (divisible by y but not x, so can only be given to friend1).

Wait, A - C is the number of numbers not divisible by x but divisible by y.

Because A is numbers not divisible by x. C is numbers not divisible by x and not divisible by y. So A - C is numbers not divisible by x but divisible by y. So those can only be given to friend1, since friend2 can't take them (they are divisible by y).

Similarly, B - C is numbers not divisible by y but divisible by x. So those can only be given to friend2.

So friend1 can take (A - C) numbers (those not divisible by x but divisible by y) plus some of the C numbers (not divisible by either). Similarly for friend2.

So the total numbers that friend1 can take is (A - C) + s, where s is the number of C numbers allocated to friend1. Similarly for friend2: (B - C) + t, where t is the number of C numbers allocated to friend2.

But s + t <= C. Also, friend1's total must be >= cnt1, friend2's >= cnt2.

So the minimal required from C is:

required1 = max(0, cnt1 - (A - C))

required2 = max(0, cnt2 - (B - C))

If required1 + required2 <= C, then it's possible. Otherwise, not.

So, putting it all together, the condition for v being sufficient is:

(A >= cnt1) and (B >= cnt2) and (required1 + required2 <= C)

Wait, but A is the total numbers available to friend1 (including C), but A is equal to (A - C) + C. Similarly, B is (B - C) + C.

So in order for friend1 to have enough numbers, (A - C) + s >= cnt1. But s can be up to C. So the minimal s is max(0, cnt1 - (A - C)).

Similarly for friend2.

Thus, the condition is:

max(0, cnt1 - (A - C)) + max(0, cnt2 - (B - C)) <= C.

But also, we have to make sure that friend1's (A - C) >=0, but that's already covered because A is v - (v//x), and C is v - (v//x + v//y - v//(x*y)), so A - C = (v//y - v//(x*y)) → which is the count of numbers divisible by y but not x. Which can't be negative.

But when we compute required1 and required2, they can't be negative because of the max(0, ...). So the condition is:

required1 + required2 <= C.

But also, we must have that:

A >= cnt1 → because friend1 can take up to (A - C) + s, but (A - C) + s can't exceed A, since s is part of the C which is included in A. So if A < cnt1, then even if we take all of A (including all of (A - C) and all of C), it's not enough. So the first condition is A >= cnt1 and B >= cnt2.

Wait, no. Because A is the total numbers available to friend1 (numbers not divisible by x). So the maximum possible for friend1 is A. Similarly for B. So if cnt1 > A or cnt2 > B, then it's impossible.

So the overall conditions are:

1. A >= cnt1 (friend1 can't have more than A numbers)

2. B >= cnt2 (friend2 can't have more than B numbers)

3. required1 + required2 <= C (the sum of the required numbers from C must fit into the available C)

So for a given v, all three conditions must be met.

So the binary search approach is as follows:

- Initialize low as the maximum of (the minimal possible v for cnt1 and x, and cnt2 and y). For example, the minimal v for friend1 is when all the numbers are exactly the cnt1 numbers not divisible by x. So the minimal v for friend1 would be when the first (v - v//x) >= cnt1. Similarly for friend2. So the minimal starting low would be max( (cnt1 * x) // (x-1) ), (cnt2 * y) // (y-1) )). But perhaps it's easier to start low at 1 and high at something like (cnt1 + cnt2) * max(x,y). But given the constraints, binary search is feasible.

But to find the correct high value, perhaps we can calculate a safe upper bound. Let's think: the maximum required v would be when all the numbers have to be used. For example, the worst case is when the required counts are high and x and y are 2 and 3, etc. So high can be set to something like (cnt1 + cnt2) * max(x, y) * 2, but maybe even that is not enough. Alternatively, since the maximum possible cnt1 and cnt2 can be up to 1e9 each, their sum is up to 1e9. So high can be up to 2e9 or similar. But in Python, binary search over 1e18 is manageable because it's about 60 iterations.

So the steps are:

1. Binary search between low and high, where low starts at 1 and high starts at some upper bound (like (cnt1 + cnt2) * max(x, y) * 2). But perhaps even a higher upper bound is needed, but in practice, the binary search will find the minimal v.

But how to compute the upper bound? Well, considering that in the worst case, the numbers must be allocated such that the C (shared) area is minimal. For example, if x and y are 2 and 3, then the numbers not divisible by either are ... So the upper bound would need to be high enough. However, using binary search, even if the initial high is set to something like 1e18, the binary search would take around 60 steps, which is manageable.

So the code would be:

Compute for a given v:

A = v - v//x

B = v - v//y

C = v - (v//x + v//y - v//(x*y))

required1 = max(0, cnt1 - (A - C))

required2 = max(0, cnt2 - (B - C))

if A >= cnt1 and B >= cnt2 and (required1 + required2) <= C:

   then v is possible, try to find a smaller one.

else:

   need to increase v.

So the binary search loop would proceed to find the minimal v where this condition holds.

Now, the problem is to code this correctly.

But wait, how do we compute C? Let's verify:

C = numbers not divisible by x and not divisible by y.

Which is equal to total v - (numbers divisible by x + numbers divisible by y - numbers divisible by both x and y).

Which is v - (v//x + v//y - v//(x*y)).

Yes, since x and y are primes, lcm(x,y) is x*y.

So that's correct.

Now, for example, in the first sample input:

3 1 2 3 → the answer is 5.

Let's check v=5:

A = 5 - 5//2 = 5-2=3. So friend1 can take up to 3 numbers (since cnt1 is 3).

B=5-5//3=5-1=4. cnt2 is 1.

C=5 - (2 +1 - 0) (since 5//2=2, 5//3=1, 5//6=0. So 2+1-0=3. 5-3=2. So C=2.

required1: cnt1 - (A - C) → 3 - (3 - 2) → 3-1=2. So required1 is 2.

required2: 1 - (4 - 2) → 1-2 → max(0, -1) = 0.

So sum required1+required2=2+0=2 <= C=2. So yes.

Also, A >= cnt1 (3 >=3), B >= cnt2 (4 >=1). So conditions are met.

So v=5 is acceptable.

Another sample: input 1 3 2 3 → output 4.

v=4:

A=4-2=2. cnt1 is 1.

B=4 - 4//3=4-1=3. cnt2 is3.

C=4 - (2 +1 -0) =4-3=1.

required1= max(0, 1 - (2-1))=1-1=0. required2= max(0,3 - (3-1))=3-2=1. sum 0+1=1<=1. So conditions met. So v=4 is acceptable.

So the code seems to handle these cases.

Now, code structure:

Read cnt1, cnt2, x, y.

We need to compute the minimal v where the conditions are met.

Implement binary search.

But let's handle the edge cases first.

For example, when x and y are the same. But the problem states that x < y. Because in the input, x and y are primes, and 2 <= x < y <= 3e4. So x and y are distinct primes, so their LCM is x*y.

So the code can proceed as above.

So in code:

Implement a function is_possible(v) that checks the three conditions.

Then binary search between low and high.

Now, the initial low can be 1, high can be (cnt1 + cnt2) * max(x, y) * 2. But perhaps a better high can be found. For example, the maximum required would be when the overlapping area is zero, but in that case, the required is cnt1 + cnt2. So high can be set to (cnt1 + cnt2) * max(x, y). But even with 1e18, it's manageable.

But how to compute the upper bound?

Alternatively, considering that the maximum possible v is when all the numbers up to v are required. For example, if x=2 and y=3, and cnt1 and cnt2 are both 1e9, then the required v could be up to 2e9. But that's just a rough estimate. But binary search even over 1e18 is manageable.

So code steps:

Read cnt1, cnt2, x, y.

Compute lcm_xy = x * y. Because x and y are primes.

Set low = 1, high = something like (cnt1 + cnt2) * max(x, y) * 2. But perhaps even higher. But since in the worst case, when all the numbers have to be used (i.e., C is zero), then the required v is (cnt1 + cnt2) * max(x,y). But perhaps even more.

But given that the binary search is efficient, let's set high to 2e18. Because even for 1e18, the binary search would take 60 steps.

Now, binary search loop:

while low < high:

   mid = (low + high) // 2

   if is_possible(mid):

       high = mid

   else:

       low = mid + 1

At the end, low will be the minimal v.

Now, implement the is_possible function.

In code:

def is_possible(v):

    a = v - v // x

    b = v - v // y

    c = v - (v//x + v//y - v//(x*y))

    # Compute (A - C) and (B - C)

    a_minus_c = (v // x + v // y - v//(x*y)) - (v // y) 

    # Wait, no: A is v - v//x. C is v - (v//x + v//y - v//(xy)).

    # So A - C = (v - v//x) - [v - (v//x + v//y - v//xy)] 

    # = (v - v//x) - v + (v//x + v//y - v//xy)

    # = -v//x + (v//x + v//y - v//xy)

    # = v//y - v//xy 

    # So A - C = v//y - v//xy 

    # Similarly, B - C = v//x - v//xy 

    # Because B is v - v//y. C is as before.

    # So B - C = (v - v//y) - [v - (v//x + v//y - v//xy)]

    # = -v//y + v//x + v//y - v//xy 

    # = v//x - v//xy 

    a_minus_c = (v // y) - (v // (x*y))

    b_minus_c = (v // x) - (v // (x*y))

    required1 = max(0, cnt1 - a_minus_c)

    required2 = max(0, cnt2 - b_minus_c)

    return (a >= cnt1) and (b >= cnt2) and (required1 + required2 <= c)

Wait, but a is v - v//x. So for a >= cnt1, and similarly for b >= cnt2.

Yes.

So the code can be written as follows.

Testing this function with the sample inputs.

Sample 1: v=5.

a =5-2=3, which >=3 (cnt1=3).

b=5-1=4 >=1.

a_minus_c = 5//3=1 - 5//6=0 → 1-0=1.

required1=3-1=2.

b_minus_c=5//2=2 -5//6=0 →2-0=2.

required2=1-2= max(0, -1) →0.

sum 2+0=2 <= c=2. So returns true.

Sample 2: v=4.

a=4-2=2 >=1.

b=4-1=3 >=3.

a_minus_c =4//3=1 -4//6=0 →1. cnt1=1 → required1=1-1=0.

b_minus_c=4//2=2 -4//6=0 →2. cnt2=3 →3-2=1 → required2=1.

sum 0+1=1 <= c=1. So returns true.

So the code works for these samples.

Another test case: when x and y are same? But according to the problem, x < y, so they are distinct.

Edge case when x and y are 2 and 3, and cnt1=1, cnt2=1. The minimal v is 3. Because friend1 can take 1,3 (but not 2), friend2 can take 1,3 (but not 3, since it's divisible by 3). Wait, no.

Wait, for v=3:

A =3-1=2 (numbers not divisible by 2: 1,3).

B=3-1=2 (numbers not divisible by 3:1,2).

But friend1 can take 1 and 3, friend2 can take 1 and 2.

But the numbers must be distinct. So if cnt1=1 and cnt2=1, possible options: friend1 takes 3, friend2 takes 2. So v=3 is sufficient.

So code for cnt1=1, cnt2=1, x=2, y=3.

v=3:

A=2 >=1.

B=2 >=1.

C=3 - (1 +1 -0) =1. So numbers not divisible by 2 or 3: 1, but wait:

Numbers 1: not divisible by 2 or 3.

So C is 3 - (1 +1 -0) =1? Wait, v//x is 3//2=1, v//y=3//3=1, v//xy=3//6=0. So C=3 - (1+1-0) =1. So the numbers not divisible by either are 1.

So required1 = max(0,1 - (v//y - v//xy)) → v//y is 1, v//xy is 0 → 1-0=1. So required1 =1 -1=0.

required2 = max(0,1 - (v//x - v//xy)) →v//x is 1, so 1-0=1. 1-1=0.

sum 0+0 <=1 → yes.

So the code returns true for v=3.

Thus, the code seems to handle this.

Now, code in Python.

But to handle very large values, we need to make sure that variables are computed correctly. For example, in Python, integer divisions are straightforward.

So the code:

Read the four integers cnt1, cnt2, x, y.

Compute lcm_xy = x * y.

Implement binary search.

But let's code the is_possible function as part of the binary search.

So code:

cnt1, cnt2, x, y = map(int, input().split())

low = 1

high = 2 * 10**18  # A very high value.

lcm_xy = x * y  # Since x and y are primes and x < y.

while low < high:

    mid = (low + high) // 2

    # Compute A, B, C.

    div_x = mid // x

    div_y = mid // y

    div_xy = mid // lcm_xy

    a = mid - div_x

    b = mid - div_y

    c = mid - (div_x + div_y - div_xy)

    a_minus_c = div_y - div_xy

    b_minus_c = div_x - div_xy

    required1 = max(0, cnt1 - a_minus_c)

    required2 = max(0, cnt2 - b_minus_c)

    if (a >= cnt1) and (b >= cnt2) and (required1 + required2 <= c):

        high = mid

    else:

        low = mid + 1

print(low)

Wait, but in the code above, a_minus_c is computed as div_y - div_xy. Because a is mid - div_x. C is mid - (div_x + div_y - div_xy). So a - C = (mid - div_x) - (mid - (div_x + div_y - div_xy)) ) = (mid - div_x) - mid + div_x + div_y - div_xy = div_y - div_xy → which is correct.

Similarly for b_minus_c.

So this code should work.

Testing the first sample:

input:3 1 2 3

low starts at 1, high at 2e18.

mid will eventually reach 5.

Another test case:

input:1 3 2 3 → output 4.

mid 4.

Thus, this code should handle all cases.

Now, considering the time constraints: each step of the binary search is O(1), and there are up to 60 steps (since 2^60 is way larger than 1e18). So even for the largest possible inputs, this code runs in O(1) time, which is acceptable.

Memory-wise, it's O(1) variables, so within the constraints.

Thus, this should be the optimal solution.
</think>

```python
cnt1, cnt2, x, y = map(int, input().split())

low = 1
high = 2 * 10**18
lcm_xy = x * y

while low < high:
    mid = (low + high) // 2
    div_x = mid // x
    div_y = mid // y
    div_xy = mid // lcm_xy
    a = mid - div_x
    b = mid - div_y
    c = mid - (div_x + div_y - div_xy)
    a_minus_c = div_y - div_xy
    b_minus_c = div_x - div_xy
    req1 = max(0, cnt1 - a_minus_c)
    req2 = max(0, cnt2 - b_minus_c)
    if a >= cnt1 and b >= cnt2 and req1 + req2 <= c:
        high = mid
    else:
        low = mid + 1

print(low)
```