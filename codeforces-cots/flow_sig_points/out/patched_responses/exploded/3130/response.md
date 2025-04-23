<think>
Okay, let's tackle this problem. So, Heidi needs to split the array A into two non-overlapping contiguous parts. Each part must have at least one element. The sum S is the sum of the modulo p of each part's sum. We need to maximize this S. Hmm.

First, let's understand the problem. We need two splits. Like, split the array into a prefix and a suffix. Or maybe a first part somewhere in the middle and the second part after? Wait, the problem says the two parts must consist of contiguous elements and not overlap. So the split is into two parts where the first is a prefix and the second a suffix? Or can they be any two non-overlapping contiguous parts, but they must cover the entire array? Wait, no. Wait, the problem says: split A into two parts. Each part is contiguous, they don't overlap. So the entire array is split into two parts. So the split is at some position where the first part is from start to i, and the second part is from j to end, but that's not possible unless j = i+1. Wait, no. Wait, perhaps the two parts are two non-overlapping contiguous segments that together cover the entire array. Because the problem says "split into 2 parts". So the first part is a prefix, the second is the suffix. Because otherwise, if you split into two parts that are in the middle, how can they not overlap and cover all elements? Oh right, maybe the split is into two parts where the first part is a prefix from 0 to i, and the second part is a suffix from j to N-1, but j must be i+1. Wait, but that leaves some elements in the middle unassigned. So perhaps the problem is that the split is into two parts where the first part is the first k elements, and the second part is the last m elements, such that k + m = N? Because otherwise, the parts would have to be adjacent but not overlapping. Oh right, maybe the split is that the array is divided into two contiguous parts that are adjacent. Like, split at some index i: first part is 0..i, second part is i+1..n-1. So the split is made by splitting the array into two parts with a single split point. That makes the problem easier. But the problem statement says "split into 2 parts such that each part contains at least 1 element of A, and each part consists of contiguous elements of A. The two parts do not overlap." So perhaps the split can be any two contiguous parts that don't overlap. Wait, but how can the entire array be split into two contiguous parts that don't overlap and cover all elements? Only if they are adjacent. Like the split is at some position i, so the first part is from 0 to i, and the second part is from i+1 to n-1. That way, they don't overlap, each is contiguous, and all elements are covered. So the split is a single split point. That makes sense. So in this case, the problem reduces to finding the split point i (where 0 <= i < n-1), so that the first part is 0..i, the second part is i+1..n-1. Then, sum their mod p and find the maximum.

Wait, but the problem statement says "each part consists of contiguous elements of A". So the two parts must be contiguous in the array, and they cannot overlap. So the only way to split the array into two such parts is to split it into a prefix and a suffix. Because if you take any two non-overlapping contiguous parts, but not adjacent, then there's elements in between that are not part of either. But the problem says "split into 2 parts" which implies that the entire array is divided into two parts, not that you can select any two parts. So the split must be a single split point. So the problem is to find the split at position i (0 <= i <= n-2), so that first part is 0..i, second is i+1..n-1. Then compute the sum of (sum of first part mod p) + (sum of second part mod p), and find the maximum possible value.

So the approach would be to compute the prefix sums and suffix sums. Then, for each possible split i, compute (prefix_sum[i+1] mod p) + (suffix_sum[i+1] mod p) and take the maximum.

But wait, in the first example, the split is into the first two elements and the last two. The sum of first two is 3+4=7 mod 10 is 7. Sum of last two is 7+2=9 mod 10 is 9. Total 16. Which matches the example. So the split is between i=1 (0-based indices). So the split is after the second element (i=1) in the array of 4 elements (indices 0-3). So the first part is 0-1, sum 7 mod 10 is 7. The second part is 2-3, sum 9 mod 10 is 9. Sum is 16.

So the problem is to split the array into two parts by choosing a split point between i and i+1 (for i from 0 to n-2), compute the sum mod p for each part, add them, and find the maximum.

So the plan is:

1. Compute prefix sums array. Where prefix_sum[i] is the sum of the first i elements (0-based, sum from 0 to i-1). So prefix_sum[0] =0, prefix_sum[1] = A[0], prefix_sum[2] = A[0]+A[1], etc. Then the sum of the first part (split at i) is prefix_sum[i+1]. The sum of the second part is sum of A from i+1 to n-1, which is prefix_sum[n] - prefix_sum[i+1].

But wait, the sum of the second part (from i+1 to n-1) is sum of A[i+1 ... n-1], which is prefix_sum[n] - prefix_sum[i+1].

So for each split i (from 0 to n-2), the sum of the first part is prefix_sum[i+1], sum of the second part is prefix_sum[n] - prefix_sum[i+1]. Then we compute (sum1 mod p) + (sum2 mod p), and take the maximum.

But wait, that's the same as (sum1 + sum2) mod p? No. Because sum1 mod p can be up to p-1, and sum2 mod p up to p-1. So their sum can be up to 2(p-1). But the total sum of the array is sum_total = sum1 + sum2. sum_total mod p is (sum1 + sum2) mod p. But S is the sum of (sum1 mod p) and (sum2 mod p). Which could be as high as 2(p-1), which could be more than sum_total mod p. So that's the S we need to maximize.

So the approach is to compute for all possible split points i, the sum1 = prefix_sum[i+1], sum2 = sum_total - sum1. Then compute (sum1 mod p) + (sum2 mod p), and find the maximum of this value.

The key is to compute this for all possible split points efficiently.

But the problem is that n can be up to 1e5, and for each split point, we need to compute the sum mod p for each part. So if we precompute the prefix sums mod p, we can compute sum1 mod p, but sum2 mod p can be (sum_total mod p - sum1 mod p) mod p. But sum_total mod p is a constant. Let's see.

sum_total = sum1 + sum2. So sum2 = sum_total - sum1.

sum2 mod p = (sum_total - sum1) mod p = (sum_total mod p - sum1 mod p) mod p. Because (a - b) mod p is equal to ( (a mod p) - (b mod p) ) mod p. So sum2 mod p is ( (sum_total mod p - sum1_mod) ) mod p. But since mod p could be negative, we add p and mod p again to get the positive value.

But when you compute sum1 mod p, and sum2 mod p, their sum is (sum1 mod p) + ( (sum_total mod p - sum1_mod) % p ). But what is the maximum possible value of this sum?

So the total S for split i is (sum1_mod + sum2_mod), where sum1_mod = sum1 % p, sum2_mod = sum2 % p.

But sum2_mod can be written as (sum_total - sum1) mod p, which is ( (sum_total mod p) - sum1_mod ) mod p. Because (sum_total - sum1) mod p is equivalent to ( (sum_total mod p) - (sum1 mod p) ) mod p.

So sum2_mod is ( (sum_total_mod_p - sum1_mod) ) % p.

But since sum1_mod can be up to p-1, and sum_total_mod_p is a fixed value, how can we compute this efficiently?

Wait, sum_total_mod_p is (sum1 + sum2) mod p. So sum_total_mod_p = (sum1_mod + sum2_mod) mod p. But that's not directly helpful here.

But the S is sum1_mod + sum2_mod, which can be (sum1_mod + sum2_mod) = (sum1_mod + ( (sum_total_mod_p - sum1_mod) mod p )).

But sum1_mod can vary from 0 to p-1. So for each split i, sum1_mod is (sum of first part) mod p, and sum2_mod is (sum_total_mod_p - sum1_mod) mod p. Wait, no. sum_total is sum1 + sum2. sum_total_mod_p is (sum1 + sum2) mod p. So sum2_mod is (sum_total - sum1) mod p, which is (sum_total mod p - sum1_mod) mod p. Because sum_total mod p = (sum1 + sum2) mod p. sum2 mod p is (sum_total - sum1) mod p. Which is the same as (sum_total_mod_p - sum1_mod) mod p.

So sum2_mod can be written as (sum_total_mod_p - sum1_mod) mod p. But mod p can give a negative result if sum_total_mod_p is less than sum1_mod. So the actual sum2_mod is (sum_total_mod_p - sum1_mod + p) % p.

So S for split i is sum1_mod + ((sum_total_mod_p - sum1_mod) % p).

Wait, no. Because sum2_mod is (sum_total - sum1) mod p. Which is equal to (sum_total mod p - sum1 mod p) mod p. For example, sum_total is 10, sum1 is 7, p=10. sum_total mod p is 0. sum1 mod p is 7. 0-7 = -7 mod 10 is 3. Which is indeed (10-7) mod 10 = 3. So sum2_mod is 3. So sum1_mod + sum2_mod is 7 +3=10. Which is the example given.

So the sum2_mod is (sum_total_mod_p - sum1_mod) mod p. So sum1_mod + sum2_mod = sum1_mod + ( (sum_total_mod_p - sum1_mod) mod p ). But how does this simplify?

Alternatively, the sum can be sum1_mod + (sum_total_mod_p - sum1_mod + p) % p. But maybe there's a way to compute this efficiently.

But regardless, for each split point i, we can compute sum1_mod and then compute sum2_mod as (sum_total_mod_p - sum1_mod) % p. Wait, no. Because sum2_mod is (sum_total - sum1) mod p. sum_total is sum1 + sum2. So sum2_mod = (sum_total - sum1) mod p. Which is equal to ( (sum_total mod p) - (sum1 mod p) ) mod p. So yes.

So, the approach is:

1. Compute the total sum of the array.

2. Compute sum_total_mod_p = total % p.

3. Precompute the prefix sums mod p. So prefix_mod[i] is (A[0] + ... + A[i-1]) mod p.

4. For each possible split i (from 0 to n-2), the first part is 0..i (sum is prefix_mod[i+1]), the second part is i+1..n-1. sum2_mod is (sum_total_mod_p - prefix_mod[i+1]) % p.

5. Then, sum_mod_total = prefix_mod[i+1] + sum2_mod. But since sum2_mod can be negative (if sum_total_mod_p < prefix_mod[i+1]), we need to handle that. Wait, but the mod p ensures it's in the range [0, p-1], right?

Wait, no. Because (sum_total_mod_p - sum1_mod) can be negative. For example, sum_total_mod_p is 5, sum1_mod is 7. Then 5-7 = -2. mod p (assuming p=10) would be 8. So sum2_mod is 8. So sum1_mod + sum2_mod is 7+8=15. So the sum can be up to 2(p-1).

So the way to compute sum2_mod is (sum_total_mod_p - sum1_mod) % p. But in Python, the modulo operator handles negative numbers by returning a non-negative result. For example, (-2) % 10 is 8. So in Python, (sum_total_mod_p - sum1_mod) % p gives the correct sum2_mod.

Therefore, for each split i, the sum S is (prefix_mod[i+1] + ( (sum_total_mod_p - prefix_mod[i+1]) % p )).

The maximum of all these S values is the answer.

So the steps are:

- Compute the total sum mod p.

- Compute prefix sums mod p for all positions.

- Iterate over each possible split point (from 0 to n-2), calculate the sum1_mod (prefix_mod[i+1]) and sum2_mod ( (sum_total_mod_p - sum1_mod) % p ), add them and track the maximum.

This approach is O(n) time and O(n) space.

But since N is up to 1e5, O(n) is acceptable.

But wait, how to compute the prefix sums mod p? Let's see.

We can compute the prefix_mod array as follows:

prefix_mod[0] = 0

for i in 0 to n-1:

    prefix_mod[i+1] = (prefix_mod[i] + A[i]) % p

Yes.

So, for example, in the first sample input:

A = [3,4,7,2], p=10.

sum_total = 3+4+7+2=16. sum_total_mod_p = 16%10=6.

prefix_mod is [0,3,7, (3+4+7)=14 mod10=4, (14+2=16 mod10=6)].

So prefix_mod is [0,3,7,4,6].

Then, the split points are i=0 (split after first element), i=1 (split after second), i=2 (split after third).

For each i in 0..2:

i=0: split after 0, sum1 is prefix_mod[1] =3, sum2_mod is (6 -3) mod10=3. Total 6.

i=1: split after 1, sum1=7. sum2_mod=(6-7) mod10= (6-7) =-1 mod10=9. So sum1 + sum2_mod=7+9=16.

i=2: split after 2, sum1=4. sum2_mod=(6-4)=2 mod10=2. Total 4+2=6.

So the maximum is 16. Which matches the example.

Another example: in the second sample.

But let's proceed.

So the steps are:

Read n and p.

Read the array.

Compute the total sum.

Compute sum_total_mod_p = total % p.

Compute prefix_mod array.

Iterate over each split point i (0 <= i <= n-2), compute the sum for split i.

Now, the time complexity is O(n), which for 1e5 is acceptable.

Space is O(n) for the prefix_mod array, which is acceptable.

But can we optimize the space? Well, since we only need the prefix_mod up to i+1 for each split point, perhaps we can compute the prefix_mod on the fly and track the maximum as we go. Let's see.

Because the split points are from 0 to n-2. So for each split point i, the first part is 0..i. So the prefix_mod[i+1] is sum of first i+1 elements mod p.

So, as we iterate through the array, for each element, we can compute the prefix_mod up to that point, and for each position j (from 1 to n-1), if j is <=n-1, then j-1 is the split index. Wait, maybe not. Let me think.

Wait, the split points are between elements. So for a split after element i (0-based), the first part is 0..i, sum is prefix_mod[i+1]. The split points are i from 0 to n-2 (since the second part must have at least one element).

So for j from 1 to n-1 (since prefix_mod[j] is sum of first j elements), j-1 is the split index. Wait, no. Wait, j can be up to n-1, but the split must leave at least one element for the second part. So j can be up to n-1, but the second part is from j to n-1. So j can be up to n-1, but the second part must have at least one element, so j can be up to n-2. Because if j is n-1, then the second part is from j (n-1) to n-1, which is one element. So j can be from 1 to n-1. Wait, no. The split points are when the first part ends at index i (inclusive), and the second starts at i+1. So for an array of length n, the possible split points are i from 0 to n-2. So for each i in 0..n-2, the first part is 0..i (length i+1 elements), the second part is i+1..n-1 (length n-1 -i elements). So for each i in 0..n-2, the split is after i. The sum of the first part is prefix_mod[i+1], sum of the second part is (sum_total - sum1) mod p.

So, during the iteration of the array, when building the prefix_mod array, for each j from 1 to n, prefix_mod[j] is the sum of first j elements mod p. So the split points are j-1 from 0 to n-2. So j can be from 1 to n-1.

Thus, for each j in 1..n-1, we can compute the sum for split j-1 as (prefix_mod[j] + (sum_total_mod_p - prefix_mod[j]) % p).

So, as we compute prefix_mod in a loop, we can track the maximum value, but we need to process j from 1 to n-1.

Thus, the code can compute prefix_mod on the fly and track the maximum without storing the entire array. Let's see.

Initialize current_prefix = 0.

max_S = 0

sum_total = sum of the array.

sum_total_mod_p = sum_total % p

current_prefix starts at 0.

for j in 0 to n-1:

    current_prefix += A[j]

    current_mod = current_prefix % p

    # Now, current_mod is prefix_mod[j+1]

    if j < n-1:  # because split after j (the j-th index) requires that the second part is from j+1 to n-1 (must have at least one element). So j can be up to n-2. So for j from 0 to n-2, the split is after j, so j+1 is the split point index in the prefix_mod array (since prefix_mod[j+1] is the sum of the first j+1 elements, which is the first part).

    So, for each j from 0 to n-2:

        sum1_mod = current_mod

        sum2_mod = (sum_total_mod_p - sum1_mod) % p

        current_S = sum1_mod + sum2_mod

        if current_S > max_S:

            max_S = current_S

So, the code can be written as:

Read n, p.

A = list of integers.

sum_total = sum(A)

sum_total_mod_p = sum_total % p

current_prefix = 0

max_S = 0

for j in range(n):

    current_prefix += A[j]

    current_mod = current_prefix % p

    if j < n-1:

        sum2_mod = (sum_total_mod_p - current_mod) % p

        current_S = current_mod + sum2_mod

        if current_S > max_S:

            max_S = current_S

print(max_S)

Wait, but this is O(n) time and O(1) space. Because we don't store the entire prefix_mod array, just the current_mod as we go.

Yes! That's correct. Because for each j in 0 to n-2, the split is after j elements. So the first part is 0..j (sum is current_prefix after j+1 elements? Wait, j indexes the array from 0 to n-1. So when j is 0, the first part is the first element (0..0), and the split is after 0. So the first part is sum of first 1 element (A[0]), and the second part is sum of n-1 elements (from 1 to n-1). So yes.

Wait, in the code above, during iteration j, current_prefix is the sum of A[0] to A[j]. So after j steps (0 to j inclusive). So current_mod is (sum of first j+1 elements) mod p.

But the split is after j, which would mean that the first part is 0..j (sum j+1 elements), and the second part is j+1..n-1. So the split points are j in 0..n-2. So the code checks if j < n-1, which allows j up to n-2 (since j starts at 0). So yes.

Thus, the code is correct and uses O(1) space (except for the input array, but the problem says memory is 256MB, so it's manageable).

So this approach is optimal in both time and space. Because for N up to 1e5, the loop runs in O(n) time, and we only use a few variables. No need for prefix_mod array storage.

Let's test this code against the first example.

First example:

n=4, p=10.

A = [3,4,7,2]

sum_total = 16, sum_total_mod_p =6.

Loop for j from 0 to 3 (since j <4):

j=0:

current_prefix =3. current_mod=3%10=3. j <3 (n-1 is 3). sum2_mod = (6 -3) mod10=3. current_S=3+3=6. max_S=6.

j=1:

current_prefix =3+4=7. current_mod=7. sum2_mod=6-7 mod10= ( -1 ) mod10=9. current_S=7+9=16. max_S=16.

j=2:

current_prefix=7+7=14. mod10=4. sum2_mod=6-4=2 mod10=2. current_S=4+2=6. max_S remains 16.

j=3:

j is not <3 (since n-1 is 3). So no processing.

Thus, output is 16. Correct.

Second example:

input:

10 12

16 3 24 13 9 8 7 5 12 12

sum_total =16+3=19, +24=43, +13=56, +9=65, +8=73, +7=80, +5=85, +12=97, +12=109.

sum_total_mod_p=109%12= 109/12=9*12=108, 109-108=1. So sum_total_mod_p=1.

Then, during the loop:

We need to track current_mod for each j from 0 to 8 (since n-1=9, so j up to 8 is allowed).

Looking for split points after j=0 to j=8.

The correct split is first 3 elements (sum 16+3+24=43 mod12= 43 mod12= 3*12=36, 43-36=7. sum1_mod=7. sum2_mod = (1-7) mod12= (-6 mod12) =6. So sum_S=7+6=13.

Then, in the code:

At j=2 (third element), current_prefix is 16+3+24=43, mod12=7. sum2_mod = (1-7) mod12= -6 mod12=6. sum_S=13. Which is the maximum.

So during the loop, when j=2, the code will compute this and set max_S=13.

Other split points may not give higher values.

Thus, the code works.

So the code is correct. It's O(n) time and O(1) space. Which is optimal for the given constraints.

So the final code is:

Read n and p.

Read the array.

Compute sum_total.

Compute sum_total_mod_p.

Initialize current_prefix and current_mod, and max_S.

Iterate through the array, updating current_prefix and current_mod. For each j in 0 to n-2, compute sum2_mod and current_S, and update max_S.

Finally, output max_S.

Yes. Now, implement this in Python.

But in Python, sum(A) can be O(n), but for n up to 1e5, that's acceptable.

So the code is:

n, p = map(int, input().split())

A = list(map(int, input().split()))

sum_total = sum(A)

sum_total_mod_p = sum_total % p

current_prefix = 0

max_S = 0

for j in range(n):

    current_prefix += A[j]

    current_mod = current_prefix % p

    if j < n - 1:

        sum2_mod = (sum_total_mod_p - current_mod) % p

        current_S = current_mod + sum2_mod

        if current_S > max_S:

            max_S = current_S

print(max_S)

Yes. That should work.

Testing the first example:

input 4 10

3 4 7 2

sum_total is 3+4+7+2=16 mod10=6.

The loop processes j from 0 to 3.

For j=0,1,2 (since j<3 is false when j=3? Wait, n=4, so n-1 is 3. So j <3 is j=0,1,2.

Yes.

Thus, the code works.

The second example:

n=10, sum_total=109 mod12=1.

Loop j from 0 to 9. But j <9 (since n-1=9, so j can be 0..8).

At j=2 (third element), sum is 16+3+24=43 mod12=7.

sum2_mod = (1-7) mod12= (-6 mod12) =6. 7+6=13.

Other split points may have lower values.

Thus, the code works.

So this is the optimal solution.
</think>

```python
n, p = map(int, input().split())
A = list(map(int, input().split()))
sum_total = sum(A)
sum_total_mod_p = sum_total % p
current_prefix = 0
max_S = 0
for j in range(n):
    current_prefix += A[j]
    current_mod = current_prefix % p
    if j < n - 1:
        sum2_mod = (sum_total_mod_p - current_mod) % p
        current_S = current_mod + sum2_mod
        if current_S > max_S:
            max_S = current_S
print(max_S)
```