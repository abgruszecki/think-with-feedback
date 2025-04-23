<think>
Okay, let's tackle this problem. Hmm. So the problem is about minimizing the total power of some machines after performing at most one operation. The operation involves selecting two machines, i and j, and a divisor x of a_i. Then, we divide a_i by x and multiply a_j by x. All values must remain positive integers. We need to find the minimal possible sum after doing this optimally or doing nothing.

First, I need to understand what the operation does. Let's think about the sum. The original sum is S. When we perform the operation, the sum changes by (-a_i + a_i/x) + (a_j * x - a_j) = a_i ( (1/x -1) ) + a_j (x-1). So the net difference is (a_j (x-1) - a_i ( (x-1)/x )). Wait, maybe it's easier to compute the total sum after the operation. The total sum before is sum of all a's. After the operation, two elements change: a_i becomes a_i/x, a_j becomes a_j *x. So the new sum is S - a_i + a_i/x - a_j + a_j*x. Which is S - a_i (1 - 1/x) + a_j (x - 1). So the difference is (a_j (x-1) ) - (a_i (x-1)/x ). Wait, maybe that's not the right way. Let me re-calculate:

Original sum S = a_1 + a_2 + ... + a_i + ... + a_j + ... + a_n.

After operation: a_i is divided by x, a_j is multiplied by x.

So the new sum is S - a_i + (a_i / x) - a_j + (a_j * x) = S - a_i (1 - 1/x) + a_j (x - 1).

So the difference compared to original sum is [a_j (x-1) - a_i (x-1)/x ].

We need this difference to be as negative as possible to minimize the total sum.

So our goal is to find two elements a_i and a_j, and a divisor x of a_i (x >1, since otherwise the operation does nothing), such that (a_j (x-1) - a_i (x-1)/x ) is as small as possible. Then, subtract that difference from the original sum.

Alternatively, for each possible pair (i,j) and divisor x of a_i, calculate the potential sum after the operation, and find the minimum possible.

But considering the constraints, n can be up to 5e4, and a_i up to 100. So how do we compute this efficiently?

Let's think about possible approaches.

First, the initial sum is straightforward to compute.

We need to find the maximum possible (a_i (x-1)/x - a_j (x-1)) because the difference in the sum is (a_j (x-1) - a_i (x-1)/x ), which is equivalent to (x-1)(a_j - a_i/(x)). So for the sum to decrease as much as possible, this value must be as negative as possible, so the term (a_j - a_i/x) must be as negative as possible. So (a_j < a_i/x) → x*a_j <a_i. So for each a_i, we can consider all possible x (divisors of a_i) greater than 1, and for each x, find the a_j in the array (not i) such that a_j is as small as possible. Because then, substituting a_j with a_j *x would increase a_j by (x-1)*a_j. But we also decrease a_i by a_i (x-1)/x.

Wait, perhaps another approach. For each possible x that divides any a_i, and for each a_i divisible by x, we can compute the best possible gain (i.e., the maximum reduction in sum) by moving x from a_i to some a_j.

The gain is (original sum) - (new sum) = (a_i (x-1)/x ) - a_j (x-1) ). So gain = (x-1) (a_i/x - a_j ).

We want to maximize this gain, which would minimize the sum. So for each possible a_i, x (divisor of a_i, x>1), and a_j (j !=i), compute (x-1)*(a_i/(x) - a_j). The maximum gain possible across all possible such choices will give the maximum possible reduction.

If the maximum gain is positive, then applying that operation reduces the sum. Otherwise, it's better not to perform any operation.

So the problem reduces to finding the maximum possible gain (x-1)*(a_i/x - a_j) for all possible i, x, j (j !=i).

But how do we compute this efficiently?

First, note that for each a_i, we can iterate over all possible x that are divisors of a_i and greater than 1.

For each such x and a_i, the term (x-1)*(a_i/x - a_j) is (x-1)*( (a_i/x) - a_j ). To maximize this, given x and a_i, we need to find the smallest possible a_j (since (x-1) is positive for x>1, and (a_i/x - a_j) is as large as possible → so a_j should be as small as possible. Because (a_i/x - a_j) would be maximized when a_j is minimized. Because then (a_i/x - a_j) is largest.

Wait, no. Let's see: (a_i/x - a_j) is maximized when a_j is as small as possible. Because then (a_i/x - a_j) is as large as possible. So for each x and a_i, the best a_j is the minimal a_j in the array, provided that j is not i.

Wait, but in that case, for a given a_i and x, the best j is the one with the minimal a_j. But if the minimal a_j is from the same a_i (i.e., the minimal a_j is a_i itself), but j can't be i. So perhaps we need to handle two cases: the minimal a_j is from a different element than i, or if the minimal is in the same element. For example, if the array has multiple elements with the same minimal value. Then, even if i is part of the minimal elements, j can be another element.

So, the approach would be:

Compute for each possible a_i and x (divisor of a_i, x>1) the value (x-1)*( (a_i /x ) - min_a ), where min_a is the minimal a_j in the array (but j can be i? Wait, j must be different from i, right? Because the operation requires choosing two different machines. Wait, the problem statement says: choose two such indices i and j. So i and j must be different.

Ah, that's an important point. So j cannot be the same as i. So when we select i and j, j must be a different index.

So for each a_i and x, the best j is the index with the minimal a_j, but not i. So in this case, the minimal a_j in the array, but if the minimal a_j is at the same index as i, then we need the next minimal a_j.

So the problem is: for each a_i and x, the best possible j is the smallest a_j in the array, but not i. So we need to track the minimal a_j and the second minimal a_j, considering how many times the minimal occurs.

Alternatively, for each i, when considering x, the best j would be the minimal a_j in the entire array, but only if that a_j is not at i. Otherwise, it's the second minimal.

This seems complicated. But perhaps a way around is to precompute for each possible a_i, the minimal a_j in the array (excluding a_i itself). Then, for each a_i and x, the best possible gain is (x-1)*( (a_i/x) - min_j ), where min_j is the minimal a_j not at i.

But how do we compute this min_j efficiently?

The minimal a_j in the array is easy. Let's say the global minimum is m. If there are multiple elements with m (count >1), then for any a_i, even if a_i is m, there's another element with m, so the min_j would be m.

But if the global minimum occurs exactly once, then for the a_i that is that m, the min_j would be the second minimum. For others, it's the global min.

So the steps could be:

1. Compute the initial sum.

2. Find the minimal possible gain (i.e., maximum possible reduction) by trying all possible a_i, x, and j.

To compute this:

- Precompute the global minimum and the count of how many times it appears.

- Also compute the second minimum.

But how?

Alternatively, for each a_i, when considering x, the minimal possible a_j (j !=i) is:

if the global minimum is not at i, then it's the global minimum.

if the global minimum is at i, then we need the next minimum (the second smallest in the array).

So the approach would be:

Compute the global minimum m, its count cnt_m, and the second minimum s_m.

Then, for each a_i:

if a_i == m:

   if cnt_m > 1:

      min_j = m

   else:

      min_j = s_m

else:

   min_j = m

So for each a_i, the minimal possible a_j (j !=i) is determined as above.

Once we have min_j, then for each possible x (divisor of a_i, x>1), compute the gain (x-1)*( (a_i/x) - min_j ), and track the maximum gain.

If the maximum gain is positive, then the minimal sum is initial_sum - max_gain.

Otherwise, the minimal sum is initial_sum.

So this seems manageable.

Now, how to compute the divisors for each a_i? Since a_i is up to 100, for each a_i we can precompute all possible divisors x>1.

For example, for a_i=4, divisors x>1 are 2,4. Because 4/2=2 (integer), and 4/4=1.

Wait, x can be any divisor of a_i, including a_i itself. Because 4 is a divisor of 4, so x can be 4. Then a_i/x =1, which is positive. So x can be up to a_i.

So for each a_i, generate all possible divisors x>1.

So the steps are:

1. Compute initial sum.

2. Find the global minimum m, count of m, and the second minimum s_m.

3. For each a_i in the array:

   a. Determine the min_j (the minimal a_j not equal to i). As per above logic.

   b. For each divisor x of a_i, x>1:

      i. Compute new_ai = a_i /x.

      ii. Compute new_aj = min_j *x.

      iii. The gain is (a_i - new_ai) - (new_aj - min_j) → which is (a_i (x-1)/x ) - (min_j (x-1)).

      Or, the gain is (x-1) * (a_i/x - min_j).

      Because the sum difference is (original sum) - (new sum) = (a_i - new_ai) - (new_aj - a_j) = (a_i*(x-1)/x ) - (min_j*(x-1)).

      So gain is (x-1) * (a_i/x - min_j).

   c. Track the maximum gain.

4. After processing all possible a_i and x, if the maximum gain is positive, subtract it from the initial sum. Otherwise, the sum remains the same.

So, how do we compute the divisors for each a_i?

For a given number up to 100, this is manageable. For example:

def get_divisors(n):

    divisors = []

    for x in range(2, n+1):

        if n %x ==0:

            divisors.append(x)

    return divisors

Wait, but wait. For example, for n=4, the divisors are 2 and 4. So the function returns [2,4], which is correct.

So for each a_i, generate all possible x>1 that divide a_i.

Now, the problem is to precompute for each a_i these x's.

Then, for each a_i and x, compute the possible gain.

So, let's code this approach.

First, compute the initial sum.

Then, compute the global min m, count of m, and the second min.

But how to compute the second min when the global min is present once?

For example, in array [1,2,3], the global min is 1 (count 1), and the second min is 2.

So, to compute this:

We can collect all elements, sort them, and then:

if the first element's count is more than 1, then the second min is also the first element.

Else, the second element is the second min.

But perhaps a better approach is:

- Iterate through the array once to find the minimum and count.

- Then iterate again to find the minimum value greater than the global min.

For example, in the array:

elements = [1,1,2,3]

global min is 1, count is 2. So any a_i equal to 1 can use min_j=1, since there are others.

But for another array [1,2,3], the global min is 1, count 1. So for a_i=1, the min_j is the next min (2).

So, code steps:

Compute m = min(a), cnt_m = a.count(m)

If len(a) > cnt_m:

   # there are elements not equal to m.

   # find the second min: the smallest element greater than m.

   s_m = min( [x for x in a if x != m] )

else:

   # all elements are m, so the min_j is m (since other elements are allowed)

   s_m = m

Wait, but in the case where all elements are m, then when you choose i, j can be any other element (since n>=2). So for a_i=m, x is a divisor of m (so x must be >=2, but m is at least 1). Wait, but m can be 1. If m is 1, then x has to be a divisor of 1 greater than 1. But 1 has no divisors greater than 1. So for a_i=1, there are no possible x. So the operation can't be performed.

So in that case, the maximum gain is zero, and the initial sum remains.

So, back to the code for m, cnt_m, s_m.

Once that's done, for each a_i in the array:

if a_i == m:

   if cnt_m >=2:

       min_j = m

   else:

       min_j = s_m

else:

   min_j = m

But wait, for the case where a_i is not m, then the min_j is m (since there are at least one element with m, which is different from a_i).

So that's correct.

Now, for each a_i, generate all x>1 divisors of a_i.

Then, for each x in those divisors, compute the gain (x-1) * (a_i//x - min_j).

If this gain is larger than the current maximum gain, update the maximum gain.

After processing all possibilities, the maximum gain is the best possible reduction. If it's positive, subtract from initial sum. Else, sum remains same.

So let's proceed to code.

But how to compute the divisors for each a_i?

We can precompute them for all possible a_i (since a_i up to 100). For example, for each a in 1..100, store all x>1 divisors.

But perhaps better to compute them on the fly for each a_i.

But for a_i=1, there are no x>1 divisors, so no possible operations.

So in code:

for each a_i in the array:

   if a_i ==1:

       continue  # no x>1 divisors.

   else:

       compute divisors of a_i, x>1.

Now, code for divisors.

In Python:

def get_divisors(n):

    if n ==1:

        return []

    divisors = set()

    for i in range(2, int(n**0.5)+1):

        if n%i ==0:

            divisors.add(i)

            if (n//i) >1:

                divisors.add(n//i)

    if n>1:

        divisors.add(n)

    return sorted(divisors)

Wait, but for example, n=4: the divisors are 2,4. So the code:

Loop i from 2 to sqrt(4)=2.

i=2, 4%2 ==0 → add 2 and 4//2=2. But 2 is already added. Wait, perhaps this code needs adjustment.

Wait, for n=4:

i runs up to 2.

i=2: n%i ==0. So add i (2) and n//i (2). But since 2 is already added, it's added once. So divisors will be {2,4}?

Wait no. Let's see:

The code first adds 2 (i=2).

Then, adds n//i which is 4//2=2. But 2 is already in the set, so adding it again does nothing.

So the set has {2}.

Then, after the loop, if n>1, add n. So 4 is added. So divisors are {2,4}.

Yes.

So for n=4, the code returns [2,4].

But for n=6, divisors are 2,3,6. So when i runs from 2 to sqrt(6)~2.449, so i=2.

6%2==0 → add 2 and 3 (since 6//2=3>1). Then, i=3 is not in the loop. After loop, add 6. So divisors are 2,3,6.

But wait, 6's divisors are 2,3,6. So yes.

But wait, 6's divisors x>1 are 2,3,6.

So code seems correct.

So the code will generate all x>1 divisors of a_i.

Now, for each a_i, and x in divisors:

compute the gain: (x-1)*( (a_i //x ) - min_j )

But (a_i//x) must be an integer, since x is a divisor of a_i.

So this is okay.

Now, the maximum gain is tracked.

But in code, how do we compute min_j for each a_i?

Let's compute m, cnt_m, s_m as discussed.

So code steps:

Read n.

Read a as a list.

sum_total = sum(a)

Compute m = min(a)

cnt_m = a.count(m)

# compute s_m: the second minimum.

if cnt_m == len(a):

    # all elements are m.

    s_m = m

else:

    # find the minimum element greater than m.

    s_m = min( [x for x in a if x != m] )

max_gain =0

for i in range(n):

    ai = a[i]

    # compute min_j for this ai.

    if ai == m:

        if cnt_m >=2:

            current_min_j = m

        else:

            current_min_j = s_m

    else:

        current_min_j = m

    # now, for ai, find all divisors x>1.

    divisors = get_divisors(ai)

    for x in divisors:

        new_ai_part = ai //x

        gain = (x-1) * (new_ai_part - current_min_j)

        if gain > max_gain:

            max_gain = gain

sum_ans = sum_total - max_gain

print(sum_ans)

So this code should handle all cases.

Let's test with the examples.

First example:

Input:

5

1 2 3 4 5

Initial sum is 1+2+3+4+5=15.

m=1, cnt_m=1. s_m=2.

For each ai:

ai=1: since ai is m (1) and cnt_m is 1 (so min_j is s_m=2).

But divisors of 1 are none, so no gains.

ai=2: min_j is m=1.

divisors of 2: 2.

x=2 → new_ai_part=1.

gain = (2-1)*(1 -1) = 1*0=0.

ai=3: divisors are 3.

x=3 → new_ai_part=1.

gain = (3-1)*(1-1) = 2*0=0.

ai=4: divisors are 2,4.

For x=2:

gain = (2-1)*(2-1) →1*(2-1) =1*1=1.

But current_min_j is 1 (since ai=4 is not m).

So gain is 1* (2-1) =1*1=1.

For x=4:

gain=3*(1-1)=0.

So for ai=4, the best gain here is 1.

ai=5: divisors 5 → gain 4*(1-1)=0.

So the maximum gain is 1.

So sum_ans is 15-1=14, which matches the first example.

Second example:

4

4 2 4 4

sum is 4+2+4+4=14.

m=2, cnt_m=1. s_m is 4 (since other elements are 4,4,4).

So for each ai:

ai=4 (not m=2), min_j is 2.

divisors of 4 are 2,4.

x=2: (2-1)*(4//2 -2) →1*(2-2)=0.

x=4: (3)*(1-2) =3*(-1)=-3. So gain is -3.

So for ai=4, x=2 gives gain 0, x=4 gives -3. So best gain here is 0.

ai=2 (m=2). cnt_m=1, so current_min_j is s_m=4.

divisors of 2: 2.

gain is (2-1)*(2//2 -4) →1*(1-4) =-3.

So maximum gain is 0.

So sum remains 14.

But in the example, the output is 14. So correct.

Third example:

5

2 4 2 3 7

sum is 2+4+2+3+7=18.

m=2, cnt_m=2.

So for ai=2 (since cnt_m >=2), current_min_j is 2.

divisors of 2 is 2.

x=2: (2-1)*(1 -2) =1*(-1) =-1. So gain is -1.

So for each ai:

ai=2: divisors are 2. gain (1)*(1 -2) =-1.

ai=4: divisors are 2,4. x=2: (1)*(2 -2) =0. x=4: (3)*(1-2)=-3.

ai=2 again same as above.

ai=3: divisors 3. (2)*(1-2) =-2.

ai=7: divisors 7. (6)*(1-2)=-6.

So no gains. So the maximum gain is zero.

sum_ans=18-0=18. Which matches the third example.

Another test case: when the array has two 1s.

n=2, a=[1,1]

sum is 2.

m=1, cnt_m=2.

For each ai:

ai=1. x must be a divisor of 1>1. So no x. So no gains.

So sum remains 2.

Another case: array [3,3], n=2.

m=3, cnt_m=2.

For each ai=3:

divisors are 3.

x=3. gain (3-1)*(1 -3) →2*(-2) =-4. So gain is -4. So no gain.

So sum remains 6.

But if x=3, then the operation would be ai=3/x=1, aj=3*3=9. sum becomes 1+9=10. Which is worse. So the code correctly does not choose this.

So the code seems to handle these cases.

Now, what about when the minimal a_j is the same as i, but there's another element with same value.

Like array [2,2,3]. m=2, cnt_m=2.

For ai=2, the current_min_j is 2 (since cnt_m >=2).

So for x=2, new_ai_part=1, gain is (2-1)*(1-2)= -1. So no gain.

But if there are two 2s, then even if i is 2 (like the first element), j can be another 2. So the code correctly uses m=2 as min_j.

Thus, the code seems correct.

Now, to handle the cases where the array has multiple minima.

So the code correctly calculates the min_j as m if there are at least two minima.

Now, for the code's time complexity.

Each a_i is up to 100. So for each a_i, the number of divisors x>1 is up to O(100) (like 100's divisors are 2,4,5,10,20,25,50,100 → 8 divisors). But for numbers up to 100, the maximum possible divisors are for 60 (which has factors 2,3,4,5,6,10,12,15,20,30,60). So 11 divisors. So for each a_i, the loop for x is O(10) steps.

n is up to 5e4. So total steps are 5e4 *10=5e5, which is manageable.

The other steps are O(n) to compute m, cnt_m, s_m.

So the code should work within the time constraints.

Now, code in Python:

But note that for the second minimum, we have to process the array again. For example, for [4,2,4,4], m=2. The code needs to find the min among elements not equal to m. So in the code:

s_m = min( [x for x in a if x != m] )

But this list comprehension could be O(n) time, which for n=5e4 is manageable.

But in Python, list comprehensions are efficient.

So the code should be fine.

Now, let's code this.

Also, note that in the code, the get_divisors function must return all x>1 divisors of a_i.

Wait, but the code for get_divisors function as I wrote earlier is not correct. Let's see:

In the code:

def get_divisors(n):

    if n ==1:

        return []

    divisors = set()

    for i in range(2, int(n**0.5)+1):

        if n%i ==0:

            divisors.add(i)

            if (n//i) >1:

                divisors.add(n//i)

    if n>1:

        divisors.add(n)

    return sorted(divisors)

Wait, but for example, n=6:

Loop i from 2 to 2.

i=2: 6%2==0 → add 2. Then n//i=3, which is >1 → add 3.

divisors now {2,3}.

After loop, add n=6. So divisors {2,3,6}.

Which is correct.

But for n=12:

Loop i from 2 to 3 (sqrt(12) is ~3.464).

i=2: 12%2=0. Add 2 and 6 (since 12//2=6>1).

i=3: 12%3=0 → add 3. 12//3=4>1 → add4.

divisors now {2,6,3,4}.

After loop, add 12.

divisors are {2,3,4,6,12}.

Which is correct.

So the function works.

Thus, the code should handle all divisors correctly.

So the code seems correct.

Now, let's write the code.

Also, note that the code must read input from stdin, etc.

So the final code:

Read n.

Read the list of a.

sum_total = sum(a)

Compute m, cnt_m, s_m.

Then for each a_i, compute the possible gains.

So code:

n = int(input())
a = list(map(int, input().split()))
sum_total = sum(a)
m = min(a)
cnt_m = a.count(m)

# Compute s_m
if cnt_m == len(a):
    s_m = m
else:
    # Find the minimal element that's not m.
    s_m = float('inf')
    for num in a:
        if num != m and num < s_m:
            s_m = num

max_gain = 0

def get_divisors(n):
    if n == 1:
        return []
    divisors = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            other = n // i
            if other > 1:
                divisors.add(other)
    divisors.add(n)  # n can be a divisor of itself (x=n)
    return sorted(divisors)

for i in range(n):
    ai = a[i]
    # Determine min_j for this ai
    if ai == m:
        if cnt_m >= 2:
            current_min_j = m
        else:
            current_min_j = s_m
    else:
        current_min_j = m
    
    divisors = get_divisors(ai)
    for x in divisors:
        new_ai_part = ai // x
        gain = (x - 1) * (new_ai_part - current_min_j)
        if gain > max_gain:
            max_gain = gain

print(sum_total - max_gain)

Yes, this should work.

Let's test the code with the examples.

First example:

Input 5 1 2 3 4 5.

m=1, cnt_m=1. s_m is 2.

For ai=1: min_j is s_m=2. divisors is empty. So no gain.

ai=2: divisors are 2. current_min_j=1.

gain: (2-1)*(1-1)=0.

ai=3: divisors are 3. gain (3-1)*(1-1)=0.

ai=4: divisors are 2,4.

x=2: (2-1)*(2-1) =1*1=1. → max_gain becomes 1.

x=4: (4-1)*(1-1)=0.

ai=5: divisors 5. gain (5-1)*(1-1)=0.

So max_gain is 1. sum 15-1=14. Correct.

Second example:

4 4 2 4 4.

sum is 14.

m=2, cnt_m=1. s_m=4.

For ai=4: current_min_j=2.

divisors are 2,4.

x=2: (2-1)*(2-2)=0.

x=4: (4-1)*(1-2)=3*(-1)=-3.

For ai=2: current_min_j is s_m=4 (since cnt_m=1).

divisors are 2.

gain (2-1)*(1-4) =1*(-3)=-3.

Other elements are 4, same as first case.

max_gain is 0. sum remains 14. Correct.

Third example:

5 2 4 2 3 7.

sum is 18.

m=2, cnt_m=2.

For ai=2: current_min_j=2.

divisors are 2.

x=2: (2-1)*(1-2)= -1.

For ai=4: divisors 2,4.

x=2: (2-1)*(2-2)=0.

x=4: (4-1)*(1-2)= -3.

Others have divisors but gains are negative.

max_gain is 0. sum is 18.

Thus, correct.

Thus, the code should handle all cases.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
sum_total = sum(a)
m = min(a)
cnt_m = a.count(m)

if cnt_m == len(a):
    s_m = m
else:
    s_m = float('inf')
    for num in a:
        if num != m and num < s_m:
            s_m = num

max_gain = 0

def get_divisors(n):
    if n == 1:
        return []
    divisors = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            other = n // i
            if other > 1:
                divisors.add(other)
    divisors.add(n)
    return divisors

for i in range(n):
    ai = a[i]
    if ai == m:
        if cnt_m >= 2:
            current_min_j = m
        else:
            current_min_j = s_m
    else:
        current_min_j = m
    
    divisors = get_divisors(ai)
    for x in divisors:
        new_ai_part = ai // x
        gain = (x - 1) * (new_ai_part - current_min_j)
        if gain > max_gain:
            max_gain = gain

print(sum_total - max_gain)
```