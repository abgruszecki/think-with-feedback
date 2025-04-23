<think>
Okay, so I need to solve this problem where Apollinaria wants to bake as many cookies as possible using her ingredients and some magic powder. Let me read the problem again carefully.

The problem says that each cookie requires a certain amount of each ingredient. For each ingredient i, she has b_i grams. The magic powder can substitute any missing amount of any ingredient. But the magic powder is limited to k grams. The goal is to find the maximum number of cookies she can bake.

Hmm. So for each cookie we make, we need a_i grams of each ingredient. Let's say we want to make x cookies. Then, for each ingredient i, the required amount is a_i * x. But she has b_i of it already. The difference between a_i *x and b_i is how much magic powder is needed for that ingredient. But if b_i >= a_i *x, then no magic powder is needed for that ingredient. For all ingredients, we sum up the max(0, a_i *x - b_i) and check if this total is <= k. The maximum x where this holds is the answer.

So the approach is to binary search over possible x values. The minimum possible x is 0, and the maximum possible x can be determined based on the maximum possible when all k is used. Since k can be up to 1e9 and a_i can be up to 1e9, the upper bound for x could be (b_i + k) // a_i for the most limiting ingredient. Wait, but maybe the worst case is when all ingredients except one have enough, and one needs a lot. So the upper bound can be (sum of (a_i * x - b_i) for all i where a_i *x > b_i) <=k. So the maximum possible x could be up to (k + sum(b_i)) / sum(a_i) + some. But perhaps for the binary search, we can compute an upper bound.

So binary search between low=0 and high= some maximum possible x. How to find high?

Each ingredient i can contribute to the maximum x as (b_i + k) / a_i. But since k is shared among all ingredients, the actual maximum x could be higher. For example, if some ingredients have enough for a high x, and others need magic powder. But the sum of the required magic for x must not exceed k.

But for the binary search, the upper limit can be determined by considering that each x requires for each ingredient i, the max(0, x*a_i - b_i). So summing all of these for x gives the total required magic. We need to find the maximum x where this sum is <=k.

So the binary search approach is as follows:

Initialize low=0, high= some value. The maximum possible x can be when all k is used for the ingredients. The upper bound could be the current x where even if all k is allocated to one ingredient, but perhaps it's better to compute a safe upper limit. For example, considering the maximum possible x as (sum(b_i) +k) / min_a_i + 1. Wait, not sure. But in any case, binary search can handle high values efficiently as long as the high is set correctly.

Let me think: the maximum x possible is when all the magic powder is used. For each x, the sum over all max(0, a_i *x - b_i) must be <=k. So the initial high can be set to (max possible x where even if all other ingredients have enough, one is the limiting). For example, the maximum x that even if all other ingredients have enough, the sum of magic for that x is possible.

But perhaps the upper bound can be (max ( (b_i +k) // a_i )) + something. Wait, no. Because if you have two ingredients, one requires (x*a1 -b1) and another (x*a2 -b2), their sum could be up to k. So even if each individually could allow a high x, their sum might not.

So the binary search needs to check for each x whether the sum of the required magic for all ingredients is <=k.

So the steps:

- Binary search between low=0 and high= some upper bound.

How to find the upper bound for x?

The maximum possible x can't be more than (sum(b_i) +k) / sum(a_i) + some, but sum(a_i) could be very small. Alternatively, the maximum x could be when each a_i is 1. Then sum of required magic would be x*sum(a_i) - sum(b_i) = x*n - sum(b_i). So x can be (sum(b_i)+k)/n. So perhaps the upper bound can be (sum(b_i) +k) // min_a_i + 1? Not sure. Alternatively, compute a high that is the maximum possible x that any individual ingredient would require, plus the contribution from k. For example, initial high can be ( (b_i +k) // a_i ) for each i, take the maximum of these, and add some buffer. But maybe that's not sufficient. Alternatively, we can set high to (sum(b_i) +k) // min_a + 1, but that's not necessarily correct.

Alternatively, since each x can't be larger than (b_i +k_i)/a_i for some k_i, where sum(k_i) =k. But how to model that.

Alternatively, the maximum possible x is such that x <= (b_i +k) / a_i for each i. But that's not true because the k is distributed. For example, if one ingredient requires 0, another requires all the k. So the maximum x can be higher than (b_i +k)/a_i for some i.

So perhaps the initial high can be (max_x_initial). Let's think of the case where one ingredient requires a lot of magic. For example, in the first sample input:

n=1, k=1e9, a1=1, b1=1e9. So x can be (1e9 + 1e9)/1 = 2e9. Which is exactly the sample output. So the maximum x is (b1 +k)/a1. So perhaps the initial high can be (max ( (b_i +k) // a_i )) + 1. But that's for the case when all k is used on that ingredient. But that's a possible upper bound, right? Because if x exceeds (b_i +k)/a_i for some i, then even if all k is used for that ingredient, (a_i *x -b_i) would be more than k. So in that case, the sum would exceed k. So the maximum x possible can't be higher than (b_i +k) / a_i for all i. Wait, that's not true. For example, if some ingredients have a_i=0 (but according to the constraints, a_i >=1). Oh right, the constraints say a_i >=1. So each a_i is at least 1.

So, the maximum x can't be higher than (b_i +k) // a_i +1 for any i? Because if for some i, x is such that a_i *x > b_i +k, then even if all k is allocated to that ingredient, it's not enough. So the sum will have at least (a_i *x -b_i) which is larger than k, so sum would exceed k. So for x to be possible, it's necessary that for all i, a_i *x <= b_i +k. Because otherwise, even if all k is given to that i, it's not enough, and the sum would be at least (a_i*x -b_i) which is more than k, thus sum exceeds k.

So the maximum possible x must satisfy for all i, a_i *x <= b_i +k. So x <= floor( (b_i +k)/a_i ) for each i. Therefore, the maximum possible x is the minimum of ( (b_i +k) // a_i ) for all i. Wait, but that's not correct. Because suppose that for some other ingredients j, even if x is higher than (b_j +k_j)/a_j, but the sum of all required magic is <=k. Wait, but if x is such that for some i, a_i *x > b_i +k, then even if all k is used on i, it's not enough. So the sum would be (a_i x -b_i) >k, which can't happen. So the sum would be >k. Therefore, for x to be possible, it must satisfy that for all i, a_i x <= b_i +k. Therefore, the maximum x possible can't exceed the minimum of ( (b_i +k) // a_i ). So the initial high can be the minimum of ( (b_i +k) // a_i ) across all i. Wait, no. Wait, for each i, x must be <= (b_i +k) // a_i. Because if x exceeds that, then a_i *x >= (b_i +k) +1. So the required magic for i is at least ( (b_i +k) +1 - b_i ) = k+1. Which is more than k. So sum would be >=k+1, which exceeds the available k. So the maximum x can't be higher than the minimum ( (b_i +k) // a_i ) across all i. Therefore, the initial high can be that minimum. Wait, but in the first sample input, the minimum is (1e9 +1e9)/1=2e9. Which is the correct answer. So in that case, that is the correct maximum. So perhaps the upper bound for binary search is the minimum of ( (b_i +k) // a_i ) for all i. But is that correct?

Wait, let's think of an example. Suppose we have two ingredients.

a1=1, a2=2.

b1=5, b2=5.

k=5.

So for x=5:

a1*5 =5. b1=5. So no magic needed.

a2*5=10. b2=5. So magic needed is 5. Sum is 5, which is equal to k. So x=5 is possible.

Now, (b1 +k)/a1 = (5+5)/1=10.

(b2 +k)/a2 = (5+5)/2=5. So the minimum is 5, which is the correct answer.

So the maximum x is indeed the minimum of (b_i +k)//a_i. So in this case, the upper bound is 5. So in this case, the maximum x is 5.

But what if, for example, the sum of required magic is less than k even when x is higher than that minimum. Let's see.

Wait, according to the previous logic, x can't be higher than the minimum ( (b_i +k) //a_i ). Because if x is higher than that minimum, then there exists at least one i where x > (b_i +k)/a_i, which would require (a_i x -b_i) >k, so sum exceeds k. So x can't be higher than the minimum of ( (b_i +k)//a_i ).

Wait, but the minimum of ( (b_i +k)//a_i ) for all i is the maximum x that is allowed for all i. Because for each i, (b_i +k) is the maximum possible magic that can be used for i. So x can't exceed (b_i +k)/a_i for any i. Therefore, the maximum x possible is the minimum of ( (b_i +k) //a_i ) over all i. So why do we need binary search then? Because maybe even that x is not possible, due to the sum of magic required for all ingredients exceeding k. Wait, because the sum could be greater than k even if each individual (a_i x -b_i) is <= (b_i +k) -b_i =k, but sum across all i could be more than k. Wait, but that's impossible. Because for x <= (b_i +k)/a_i for all i, then for each i, a_i x <= b_i +k. So a_i x -b_i <=k. But if you have n ingredients, each of which contributes up to k, their sum could be up to n*k. Which could be way larger than k. So even if x is <= all (b_i +k)/a_i, the sum of required magic may exceed k. Therefore, the maximum x is not necessarily the minimum of ( (b_i +k) //a_i ), but the largest x where the sum of required magic for x is <=k, and x is <= all ( (b_i +k)/a_i ).

So the binary search is necessary. Because x can't be higher than that minimum, but even if x is lower than that, the sum might be too high.

So the approach is:

- Compute the minimum of ( (b_i +k) //a_i ), call that upper_bound.

Then binary search between low=0 and high=upper_bound.

For each mid value in the binary search, check if the sum of max(0, a_i * mid -b_i) for all i is <=k. If yes, then we can try higher. Else, try lower.

So the steps are:

1. Calculate for each i the maximum possible x that could be allowed for that ingredient if all k is given to it. The minimum of those gives the upper bound.

2. Perform binary search between 0 and upper_bound to find the maximum x where sum of required magic is <=k.

So how to compute upper_bound? For each i, (b_i +k) //a_i. The minimum of these?

Wait, no. Wait, for x to be possible, x must be <= (b_i +k) //a_i for all i. So the maximum possible x is the minimum of ( (b_i +k) //a_i ) for all i. So the upper bound is the minimum of these values.

Wait, no. Because (b_i +k) //a_i is the maximum x allowed for i. So for x to be allowed for all i, x must be <= all ( (b_i +k) //a_i ). So the maximum possible x is the minimum of all ( (b_i +k) //a_i ). So the upper bound is that minimum.

Wait, let me see. For example, in sample input 2:

n=10, k=1.

a_i are all 1e9, b_i are all 1.

So for each i, (1 +1)/1e9 = 2/1e9 = 0 (since 2//1e9 is 0). So upper_bound is 0. Then sum of required magic for x=0 is 0. So answer is 0. Which matches the sample.

Another example: sample 3.

n=3, k=1.

a = [2,1,4]

b = [11,3,16]

So for each i:

i=0: (11+1)/2=6.0 -->6.

i=1: (3+1)/1=4.

i=2: (16+1)/4=4.25 -->4.

So the minimum is 4. So upper bound is 4.

Now check sum for x=4.

For each i:

a_i *4 -b_i:

2*4=8 -11= -3 → 0.

1*4=4-3=1 → 1.

4*4=16-16=0 →0.

Sum is 1. Which is <=k=1. So x=4 is possible. So answer is 4.

Sample 4:

n=4, k=3.

a = [4,3,5,6]

b = [11,12,14,20]

For each i:

i=0: (11+3)/4 =14/4=3.5 →3.

i=1: (12+3)/3=5 →5.

i=2: (14+3)/5=3.4 →3.

i=3: (20+3)/6=23/6=3.833 →3.

So upper_bound is 3.

Check sum for x=3.

Compute each a_i *3 -b_i:

4*3=12-11=1 →1.

3*3=9-12= -3 →0.

5*3=15-14=1 →1.

6*3=18-20= -2 →0.

Sum is 1+0+1+0=2 <=3. So possible. But can we make higher x? No, because upper_bound is 3. So the answer is 3. Which matches the sample.

So in all samples, the upper_bound is correct.

So the binary search approach is:

Compute the upper_bound as the minimum of ( (b_i +k) //a_i ) for all i.

Then binary search between 0 and upper_bound.

Wait, but wait. What if the sum of required magic for upper_bound is <=k? Then upper_bound is the answer. Otherwise, we need to find the maximum x <= upper_bound where sum is <=k.

So the steps are:

1. Compute for each i the value (b_i +k) //a_i. Take the minimum of these as the upper_bound.

2. The answer is the maximum x in [0, upper_bound] such that sum over all i of max(0, a_i *x -b_i) <=k.

So the binary search is the correct approach here.

Now, considering the constraints.

n can be up to 1e5. For each binary search step, we need to compute the sum for all i. Each step is O(n). The number of steps is log2(upper_bound). Since upper_bound can be up to (1e9 +1e9)/1 → 2e9. So log2(2e9) is around 31. So total steps are 1e5 *31 =3.1e6 operations, which is acceptable for 1 second (since Python can handle about 1e8 operations per second, but even 3e6 is manageable).

But wait, in Python, even 1e6 operations per test case can be slow. Wait, but 1e5 *31 is 3.1e6, which is manageable.

But in the sample input 1, n=1e5, but for each step, we need to loop through 1e5 elements. But 3e6 steps are okay. Let's see.

But 1e5 elements for each of 30 steps is 3e6 operations. Each operation is a max(0, a_i *x -b_i) and summing. So in Python, even 3e6 operations are acceptable.

But let's see the code structure.

We need to read n and k.

Then read the a array and b array.

Compute the upper_bound as min( (b_i +k) // a_i for all i in 0..n-1 ).

Then perform binary search between low=0 and high=upper_bound.

For each mid in binary search:

Compute sum( max(0, a_i*mid -b_i) for all i )

If sum <=k → possible, check higher.

Else, check lower.

So in Python, the code would look like:

Read n, k.

a = list of a_i.

b = list of b_i.

Compute upper_bound as min( (b[i] +k) // a[i] for i in range(n) )

Set low=0, high=upper_bound.

ans=0

while low <= high:

    mid = (low + high) //2

    required = 0

    for i in range(n):

        needed = a[i] * mid

        if needed > b[i]:

            required += needed - b[i]

            if required >k:

                break

    if required <=k:

        ans = mid

        low = mid +1

    else:

        high = mid -1

return ans.

But for n=1e5, and 30 steps, this is 3e6 operations. But in Python, loops over 1e5 elements may be slow. So this approach may not be efficient enough for the time constraints.

Wait, the time limit is 1 second. Python can handle about 1e6 operations per second. So 3e6 operations would be around 3 seconds. Which would be too slow.

So the problem is that the inner loop (for each i in n) is O(n) per binary step. For n=1e5, this is O(n log x), which is 3e6 steps, but in Python, even that could be too slow.

So we need to optimize the code. How?

Hmm. We can precompute the a and b lists. Then, during each binary step, we need to calculate the sum of max(0, a_i *mid -b_i). So perhaps using list comprehensions or generator expressions to compute the sum, but that's probably not enough.

Alternative approach: precompute all a_i and b_i. Then, for each mid, the sum is sum( max(0, a_i *mid -b_i) for all i )

So in Python, perhaps using a generator expression with sum would be efficient. Let's see:

sum( max(0, a * mid - b) for a, b in zip(a_list, b_list) )

But for 1e5 elements, this is O(n) time. So for 30 steps, 3e6 operations. But in Python, each iteration in a generator is not as fast as in C++. So perhaps this is tight.

So how can we speed this up?

Alternative idea: precompute (a_i, b_i) as lists, and process them in a loop with early termination.

But even that may not help. So another approach is needed.

Wait, but what if we precompute for each ingredient the value (b_i / a_i) to find the minimal possible x?

Alternatively, perhaps precompute the minimal possible x for each ingredient. But not sure.

Alternatively, for each mid, during the binary search, we can calculate the sum as follows:

sum = 0

for a, b in zip(a_list, b_list):

    temp = a * mid - b

    if temp > 0:

        sum += temp

    if sum >k:

        break

This way, once the sum exceeds k, we can break early and not process all elements. This can optimize the average case. For example, if mid is very large, and the sum is exceeded early in the list, then processing stops quickly.

But in the worst case, this is O(n) per step. But perhaps in practice, this can help.

So code:

required =0

for i in range(n):

    a_i = a[i]

    b_i = b[i]

    needed = a_i * mid

    if needed > b_i:

        required += needed - b_i

    if required >k:

        break

if required <=k: ...

But in Python, loops are slower. So perhaps using a generator with sum is not possible here. But with early termination, this can speed up some cases.

But even then, for n=1e5, in the worst case, each step is O(n), which is 3e6 steps.

Another way to optimize is to precompute a list of (a_i, b_i) pairs, sorted in some way. But I'm not sure how that would help.

Alternatively, precompute for each a_i, the value (b_i //a_i) + (1 if b_i %a_i !=0 else 0), which is the minimal x where the ingredient i requires magic powder. Wait, but maybe not.

Alternatively, for each a_i and b_i, the x where the ingredient i starts needing magic is x_i = (b_i //a_i) + 1. Because:

if x <= (b_i //a_i) → a_i *x <=b_i → no magic needed.

x > (b_i //a_i) → a_i *x >b_i → magic needed.

So for x >= x_i, the ingredient i contributes (a_i *x -b_i) to the sum.

So for x, the sum is sum_{i} max(0, a_i x -b_i).

So perhaps, for x in the binary search, we can compute how much each ingredient contributes.

But how can this be optimized?

Alternative approach: precompute for each ingredient the x_i where magic starts being needed. Then, for a given mid in binary search, the sum is sum_{i where x_i <=mid} (a_i *mid -b_i).

So the problem reduces to, for a given mid, compute the sum over all i where x_i <=mid of (a_i *mid -b_i).

If we can precompute the x_i's and sort them, then for a given mid, we can find how many x_i's are <= mid, and compute the sum in O(1) time using prefix sums.

But how?

Let me think.

For each ingredient i, x_i is the minimal x where a_i x >b_i. So x_i = floor( (b_i -1)/a_i ) +1.

Because:

if b_i is divisible by a_i, then (b_i //a_i) is x_i-1. So x_i = (b_i //a_i) +1.

If not, then (b_i //a_i) is the floor, and x_i is (b_i //a_i) +1.

So x_i = ceil( (b_i +1)/a_i ) ?

Wait, let's see:

For example, b_i=5, a_i=2. Then 5//2=2. So x_i=3. Because 2*3=6>5.

So x_i =3. Which is (5+1) //2 =3.

Another example: b_i=6, a_i=2. 6//2=3. x_i=4. (6+1)//2=3.5 →3.5//1=3. So (6+1)//2=3.5 → floor is 3. So x_i=3+1=4.

So x_i = (b_i + a_i) //a_i.

Wait, (b_i +a_i -1) //a_i ?

Wait, (5 +2-1)//2 =6//2=3 → yes.

(6 +2-1)//2=7//2=3 →3+1=4? No, (6+2-1)//2 is 7//2=3. So x_i is 4? Wait, no. For 6, a=2, x_i is 3+1=4. So (6+2-1)//2 =7//2=3. So 3+1=4.

So x_i can be calculated as (b_i + a_i -1) //a_i +1?

Wait, no. Let's compute (b_i + a_i -1) //a_i.

For example, b_i=5, a=2. (5+2-1) =6. 6//2=3. So x_i is 3.

Which is correct. Because 3 is the x_i.

Wait, but when x=3, a_i *x=6>5. So x_i is 3. So (b_i +a_i -1) //a_i gives the correct x_i.

So x_i = (b_i +a_i -1) // a_i.

So for each ingredient, x_i is (b_i +a_i -1) //a_i.

So for x >=x_i, the ingredient i contributes (a_i *x -b_i) to the sum.

So, to compute the sum for a given mid, we need to sum (a_i *mid -b_i) for all i where x_i <=mid.

So if we can precompute all x_i's, sort them, and compute for each i, a_i and b_i, and then for a given mid, find the number of x_i's <=mid, and compute the sum of a_i*mid -b_i for those i's.

But how to compute this sum efficiently?

Let's say we have the list of ingredients sorted by x_i. For each x_i in the sorted list, we can precompute a prefix sum of a_i and a prefix sum of b_i.

For example, for all i with x_i <=mid, sum(a_i) is S_a and sum(b_i) is S_b. Then the total sum is mid * S_a - S_b.

So, the steps would be:

1. For each ingredient i, compute x_i = (b_i + a_i -1) //a_i.

   Also, compute a_i and b_i.

2. Sort the ingredients by x_i, and for each, compute the prefix sum of a_i and prefix sum of b_i.

   So after sorting, for each x in x_i sorted order, the prefix sums can be used.

3. For a given mid in binary search:

   a. Find the number of ingredients where x_i <= mid. Let's call this count m.

      This can be done via binary search in the sorted x_i list.

   b. Compute S_a = sum of a_i for first m ingredients.

   c. Compute S_b = sum of b_i for first m ingredients.

   d. The required magic is mid * S_a - S_b.

   e. Check if this value <=k.

This approach reduces the per-step computation from O(n) to O(log n), which is a massive improvement. So the binary search steps would be O(log u), and each step takes O(log n) time. So the total time becomes O(n log n + (log u) * log n), which is acceptable for n=1e5.

So this approach is feasible.

So let's outline the steps:

- Precompute x_i, a_i, b_i for each ingredient.

- Sort the list of (x_i, a_i, b_i) by x_i.

- Compute the prefix sums for a_i and b_i.

   For example, prefix_a[i] is the sum of a_0 to a_i-1.

   Similarly for prefix_b.

- Then, during binary search:

   For a given mid, perform a binary search on the sorted x_i list to find the number of x_i <= mid. Let's say m.

   Then sum_a = prefix_a[m], sum_b = prefix_b[m].

   required = mid * sum_a - sum_b.

   Check if required <=k.

But how to handle the case where m is 0? Well, sum_a and sum_b would be 0.

So, this approach reduces the per-step computation from O(n) to O(log n).

Thus, the binary search steps can be done quickly.

But wait, this approach assumes that for all ingredients where x_i <=mid, we have to include their (a_i*mid -b_i) in the sum. Which is correct, because x_i is the minimal x where a_i x >b_i. So for x >=x_i, the magic is needed.

But the sum for x is sum over all i of max(0, a_i x -b_i) → sum over i where x >=x_i of (a_i x -b_i).

Which is exactly sum (a_i x -b_i) for i where x_i <=x.

So yes.

So the approach is to precompute x_i for each i, sort the ingredients by x_i, compute prefix sums of a_i and b_i.

Then, during binary search, for each mid:

   Find the number of ingredients with x_i <= mid (using binary search in the sorted x_i list), which gives m.

   sum_a = prefix_a[m]

   sum_b = prefix_b[m]

   required = mid * sum_a - sum_b.

   if required <=k → possible.

This reduces the per-step complexity from O(n) to O(log n).

Thus, this will be efficient even for n=1e5.

So the steps for the code:

Read n and k.

Read a as a list.

Read b as a list.

Compute x_i for each i as (b[i] +a[i]-1) //a[i].

Create a list of tuples (x_i, a_i, b_i).

Sort this list by x_i.

Compute prefix sums for a and b.

Then, compute upper_bound as the minimum of ( (b[i] +k) //a[i] ) for all i.

Then binary search between low=0 and high=upper_bound.

For each mid in binary search:

   find m = number of x_i in the sorted list that are <=mid.

   sum_a = prefix_a[m]

   sum_b = prefix_b[m]

   required = mid * sum_a - sum_b.

   if required <=k → possible.

Thus, the code can be written as follows.

But how to handle the sorted x_i and the prefix sums.

Let me think.

After creating the list of tuples (x_i, a_i, b_i), sorted by x_i, we can create two arrays: x_list, a_list, b_list (sorted).

Then, compute prefix_a and prefix_b arrays.

prefix_a[0] = 0

prefix_a[i] = prefix_a[i-1] + a_list[i-1]

Similarly for prefix_b.

Then, for a given mid, find the index m where x_list[m] <=mid and x_list[m+1] >mid. This can be done via bisect_right.

So m = bisect.bisect_right(x_list, mid).

sum_a = prefix_a[m]

sum_b = prefix_b[m]

required = mid * sum_a - sum_b.

Thus, the code can use the bisect module.

So this approach will make the code run in O(n log n + log u log n) time, which is acceptable.

But we also need to compute the upper_bound correctly. So compute for each i (b_i +k) //a_i, then take the minimum.

Wait, but for each i, (b_i +k) //a_i is the maximum x that can be allowed for that i. So the upper_bound is the minimum of these values.

Yes.

So now, let's test this approach with sample input 3.

Sample 3:

n=3, k=1.

a = [2,1,4]

b = [11,3,16]

x_i for each i:

i0: (11+2-1)//2=12//2=6 →x_i=6.

i1: (3+1-1)//1=3//1=3 →x_i=3.

i2: (16+4-1)//4=19//4=4.75 →4. So x_i=4.

So sorted x_list would be [3,4,6].

prefix_a = [0,1,1+4=5,5+2=7].

prefix_b = [0,3,3+16=19,19+11=30].

Then, during binary search for mid=4.

x_list is [3,4,6]. bisect_right(4) → returns 2 (since 4 is at index 1, and bisect_right returns insertion point after existing elements equal to 4. So m=2.

sum_a = prefix_a[2] =5.

sum_b=19.

required =4*5 -19 =20-19=1 <=1. So possible.

So yes.

Another sample:

Sample 4:

n=4, k=3.

a = [4,3,5,6]

b = [11,12,14,20]

Compute x_i:

i0: (11+4-1)/4 =14//4=3.5 →3.5 →3 (wait wait, (11 +4-1) is 14. 14//4=3. So x_i=3.

i1: (12+3-1)/3=14//3=4.666 →4.

i2: (14+5-1)/5=18//5=3.6 →3.

i3: (20+6-1)/6=25//6=4.166→4.

So x_list sorted: [3,3,4,4].

prefix_a would be:

prefix_a[0] =0.

prefix_a[1] =4 → (i0's a is4? Wait, sorted by x_i, so when sorted, the x_i are [3,3,4,4], but for the ingredients, their a and b are:

Original ingredients:

i0: a=4, b=11 →x_i=3.

i1: a=3, b=12 →x_i=4.

i2: a=5, b=14 →x_i=3.

i3: a=6, b=20 →x_i=4.

When sorted by x_i, the order is i0, i2, i1, i3.

So x_list is [3,3,4,4].

a_list for these are [4,5,3,6].

prefix_a is:

0,4,4+5=9,9+3=12,12+6=18.

prefix_b is:

0,11,11+14=25,25+12=37,37+20=57.

So for mid=3, which is the upper bound.

sum_a = prefix_a[4] →18.

sum_b=57.

required =3*18 -57 =54-57= -3 →0. So it's <=3. So mid=3 is possible.

But the sample's answer is3.

But sample's answer is3.

Yes. So this approach works.

So the code should correctly compute the required sum.

Now, the code steps:

Implement the approach.

Read n and k.

Read a and b.

Compute x_i for each i as (b[i] + a[i] -1) //a[i].

Create a list of (x_i, a_i, b_i) tuples.

Sort this list by x_i.

Extract x_list, a_list, b_list from the sorted list.

Compute prefix_a and prefix_b.

Compute upper_bound as min( (b[i] +k) //a[i] for i in 0..n-1 )

Then perform binary search between 0 and upper_bound.

In each step:

mid = (low + high) //2

m = bisect.bisect_right(x_list, mid)

sum_a = prefix_a[m]

sum_b = prefix_b[m]

required = mid * sum_a - sum_b

if required <=k and sum_a*mid - sum_b >=0 → possible.

Wait, but sum_a*mid - sum_b can be negative? No, because sum_a is sum of a_i where x_i <=mid, and sum_b is sum of b_i where x_i <=mid. For those i, x_i <=mid → a_i *mid >=x_i *a_i >=b_i (since x_i = (b_i +a_i-1)//a_i → a_i x_i >=b_i). So for each i in sum_a, a_i *mid >=b_i. So mid >=x_i → a_i *mid >=x_i *a_i >=b_i. So sum_a*mid - sum_b >=0.

Thus, required is >=0.

So, if required <=k → possible.

Thus, during binary search, we can proceed.

But what about the upper_bound? Because upper_bound is the minimum of (b[i]+k)//a[i].

But for each i, (b[i]+k)//a[i] >= x_i → because:

x_i is (b_i +a_i -1)//a_i → (b_i +a_i -1)/a_i < x_i +1.

But (b_i +k) /a_i is >=x_i only if k >= a_i x_i -b_i.

But since x_i is the minimal x where a_i x >b_i, then a_i x_i -b_i <=a_i (since x_i = (b_i +a_i-1)//a_i → a_i x_i <=b_i +a_i -1 +a_i? Wait, maybe not. Let's compute x_i *a_i:

x_i = (b_i +a_i -1) //a_i → x_i *a_i = floor( (b_i +a_i-1)/a_i ) *a_i.

Which is <= (b_i +a_i-1).

So x_i *a_i <=b_i +a_i-1 →x_i *a_i -b_i <=a_i-1.

So for each i, the required magic for x_i is a_i x_i -b_i <=a_i-1.

So when k is large enough, the upper_bound could be x_i + t, where t is such that sum for x_i +t is <=k.

But the upper_bound is computed as the minimum of (b_i +k)//a_i. So the binary search is constrained within that.

Thus, the code should work.

Now, the code:

Implement this in Python.

But need to handle the sorted x_list, and prefix sums.

We'll use bisect for this.

So code outline:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    b = list(map(int, input_stream.readline().rstrip("\n").split()))

    # Compute x_i for each ingredient
    x_list = []
    for ai, bi in zip(a, b):
        if ai ==0:
            # according to constraints, ai >=1, so no need.
            pass
        xi = (bi + ai -1) // ai
        x_list.append( (xi, ai, bi) )

    # Sort by x_i
    x_list.sort()

    sorted_x = [xi for xi, ai, bi in x_list]
    sorted_a = [ai for xi, ai, bi in x_list]
    sorted_b = [bi for xi, ai, bi in x_list]

    # Compute prefix sums for a and b
    prefix_a = [0]*(n+1)
    prefix_b = [0]*(n+1)
    for i in range(n):
        prefix_a[i+1] = prefix_a[i] + sorted_a[i]
        prefix_b[i+1] = prefix_b[i] + sorted_b[i]

    # Compute upper_bound
    max_possible = []
    for ai, bi in zip(a, b):
        temp = (bi + k) // ai
        max_possible.append(temp)
    upper_bound = min(max_possible)

    low =0
    high = upper_bound
    ans =0

    while low <= high:
        mid = (low + high) //2
        # find the number of x_i <=mid
        m = bisect.bisect_right(sorted_x, mid)
        sum_a = prefix_a[m]
        sum_b = prefix_b[m]
        required = mid * sum_a - sum_b
        if required <=k:
            ans = mid
            low = mid +1
        else:
            high = mid -1

    print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10 1
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
1 1 1 1 1 1 1 1 1 1
""",
            "output": \
"""\
0
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
import bisect


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    b = list(map(int, input_stream.readline().rstrip("\n").split()))

    # Compute x_i for each ingredient
    x_list = []
    for ai, bi in zip(a, b):
        if ai ==0:
            # according to constraints, ai >=1, so no need.
            pass
        xi = (bi + ai -1) // ai
        x_list.append( (xi, ai, bi) )

    # Sort by x_i
    x_list.sort()

    sorted_x = [xi for xi, ai, bi in x_list]
    sorted_a = [ai for xi, ai, bi in x_list]
    sorted_b = [bi for xi, ai, bi in x_list]

    # Compute prefix sums for a and b
    prefix_a = [0]*(n+1)
    prefix_b = [0]*(n+1)
    for i in range(n):
        prefix_a[i+1] = prefix_a[i] + sorted_a[i]
        prefix_b[i+1] = prefix_b[i] + sorted_b[i]

    # Compute upper_bound
    max_possible = []
    for ai, bi in zip(a, b):
        temp = (bi + k) // ai
        max_possible.append(temp)
    upper_bound = min(max_possible)

    low =0
    high = upper_bound
    ans =0

    while low <= high:
        mid = (low + high) //2
        # find the number of x_i <=mid
        m = bisect.bisect_right(sorted_x, mid)
        sum_a = prefix_a[m]
        sum_b = prefix_b[m]
        required = mid * sum_a - sum_b
        if required <=k:
            ans = mid
            low = mid +1
        else:
            high = mid -1

    print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 1
2 1 4
11 3 16
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

Sample3:

As discussed, the code would return 4.

Sample4:

upper_bound is3.

mid=3.

sum_a is prefix_a[m], where m is the number of x_i <=3.

x_list is [3,3,4,4]. sorted_x is [3,3,4,4].

bisect_right(3) returns 2.

sum_a= prefix_a[2] =4+5=9.

sum_b=11+14=25.

required=3*9 -25 =27-25=2 <=3. So possible. ans=3.

Thus, code works.

Thus, this approach is correct and efficient.
</think>

```python
import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Precompute x_i for each ingredient and sort them along with a and b
ingredients = []
for ai, bi in zip(a, b):
    xi = (bi + ai - 1) // ai
    ingredients.append((xi, ai, bi))

ingredients.sort()
sorted_x = [x for x, ai, bi in ingredients]
sorted_a = [ai for x, ai, bi in ingredients]
sorted_b = [bi for x, ai, bi in ingredients]

# Compute prefix sums for a and b
prefix_a = [0] * (n + 1)
prefix_b = [0] * (n + 1)
for i in range(n):
    prefix_a[i+1] = prefix_a[i] + sorted_a[i]
    prefix_b[i+1] = prefix_b[i] + sorted_b[i]

# Determine upper bound for binary search
max_possible = []
for ai, bi in zip(a, b):
    max_possible.append((bi + k) // ai)
upper_bound = min(max_possible)

# Binary search to find the maximum x
low, high, ans = 0, upper_bound, 0
while low <= high:
    mid = (low + high) // 2
    m = bisect.bisect_right(sorted_x, mid)
    sum_a = prefix_a[m]
    sum_b = prefix_b[m]
    required = mid * sum_a - sum_b
    if required <= k:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)
```
