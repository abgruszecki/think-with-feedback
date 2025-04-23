<think>
Okay, I need to solve this programming problem. Let's see what the problem says. The task is to compute the sum of d(i*j*k) for all i from 1 to a, j from 1 to b, and k from 1 to c. And d(n) is the number of divisors of n. The result should be modulo 2^30, which is 1073741824.

Hmm. The constraints for a, b, c are up to 100 each. So the maximum possible total triplets (i,j,k) is 100*100*100 = 1,000,000. But for each triplet, calculating d(i*j*k) directly would be expensive. Wait, if i, j, k are each up to 100, their product could be up to 1e6, and for each product, we need to find the number of divisors.

But calculating d(n) for each n up to 1e6 might be manageable. But even that, multiplied by 1e6 triplets, could be slow. Because for each triplet, calculating the product and then the number of divisors on the fly would be O(1e6 * sqrt(n)) operations. Wait, sqrt(1e6) is 1e3, so 1e6 * 1e3 = 1e9 operations. That's way too slow for a 2-second time limit. So we need a smarter approach.

Alternative approach: precompute the number of divisors for all possible products. But the product can be up to 1e6 (100*100*100), but precomputing d(n) for all n up to 1e6 is feasible. Then, for each triplet, compute the product and look up d(n) in a precomputed array. That would reduce the per-triplet cost to O(1), but the precomputation of d(n) for n up to 1e6 needs to be efficient.

But even that, precomputing d(n) for n up to 1e6 is manageable. How to do that efficiently? The standard way is to use the sieve of Eratosthenes approach to compute the number of divisors. For example, we can initialize an array div_counts where div_counts[n] is the number of divisors of n. Then, for each d from 1 to 1e6, iterate through all multiples of d and increment their divisor count by 1. But that would take O(1e6 log 1e6) time, which should be okay.

Wait, but 1e6 is manageable. Let's calculate: for d from 1 to 1e6, for each multiple m of d, add 1 to div_counts[m]. The total number of operations is the sum_{d=1 to 1e6} (1e6 / d) ≈ 1e6 ln(1e6) ≈ 1e6 * 14 ≈ 1.4e7 operations. That's acceptable.

So first step: precompute d(n) for all n up to 1e6. Then, iterate through all possible triplets (i,j,k) and sum d(i*j*k) modulo 2^30.

Wait, but even with a precomputed d(n), the triplets are 1e6, and each requires computing i*j*k. But 1e6 iterations is manageable in Python, right? Let's see: 1e6 iterations in Python take maybe a second or so. But wait, 1e6 is manageable. Let's check: 1e6 iterations of a simple loop would take around 0.1 seconds. But in Python, perhaps a bit more, but with a 2-second time limit, it's acceptable.

But wait, the product i*j*k can be up to 1e6. So for each triplet, compute the product, then look up the precomputed d array. So the code would be:

sum = 0
for i in 1..a:
  for j in 1..b:
    for k in 1..c:
      product = i*j*k
      sum += d[product]

But the problem is that in Python, triple loops (a, b, c up to 100 each) would be 1e6 iterations, which is manageable. However, nested loops in Python can be slow. For example, 100*100*100 = 1e6 loops. Each loop iteration is very simple (multiply three numbers, access an array, add to sum). But even in Python, 1e6 operations take about a second, which is okay.

So the plan is:

1. Precompute the number of divisors for all numbers up to 1e6 (since 100*100*100=1e6).
2. Iterate through all possible i, j, k in the ranges [1,a], [1,b], [1,c], compute the product, and add d[product] to the sum.
3. Take the sum modulo 2^30.

But wait, maybe there's a way to optimize this by precomputing some parts. For example, since i, j, k are each up to 100, perhaps we can precompute all possible products and their divisor counts. But that's not necessary, because the product can be up to 1e6, which is manageable.

So the steps are:

- Precompute the divisor counts.
- Iterate through all triplets and sum the divisor count of their product.

But let's think about the precomputation.

Implementing the sieve for divisor counts:

Initialize an array div_count of size MAX+1 (where MAX is 1e6) to zero.

Then for each d from 1 to MAX:
   for multiple in d, 2d, 3d, ..., up to MAX:
       div_count[multiple] += 1

Yes. Because each divisor d contributes to the count for its multiples.

So this will correctly compute the number of divisors for each number. For example, 6's divisors are 1,2,3,6. So during the sieve, when d=1, we increment all multiples (including 6), adding 1. When d=2, we increment multiples of 2 (including 6), adding another 1. Similarly for 3 and 6. So 6 will have a div_count of 4, which is correct.

So this method works.

So precomputing the div_count array is correct.

Now, the problem is how to handle the triple loops efficiently in Python.

But in Python, nested loops can be slow. So perhaps using itertools.product might not be faster, but for 1e6 iterations, even a triple loop with for i in range(1, a+1), etc., is manageable.

Alternatively, perhaps using list comprehensions or other optimizations. But for now, let's think about code structure.

Sample code outline:

Compute the maximum possible product: max_product = a*b*c.

But a, b, c can be up to 100 each, so max_product is 1e6.

So precompute div_count up to 1e6.

Then, sum all div_count[i*j*k] for i, j, k in their ranges.

But in Python, the triple loops can be written as:

sum_ = 0
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            product = i * j * k
            sum_ += div_count[product]

But even with 1e6 iterations, this might be slow in Python.

Alternative approach: precompute all possible i*j values first, then multiply by k and accumulate.

But even that, it's still O(abc) time.

Another idea: since the order of i, j, k doesn't matter (they are all multiplied together), maybe we can precompute the frequencies of each possible product after each step. For example, first compute all possible products of i and j (for i in 1..a, j in 1..b), count how many times each product occurs. Then multiply each product by k (for k in 1..c), and accumulate the counts. Then, for each possible product up to a*b*c, multiply the count by its divisor count and sum all.

This could reduce the computation time by breaking the problem into steps, but the first step (computing the product frequencies for i and j) would be O(ab) time, then for each of those products, multiply by each k in 1..c. So the total time is O(ab + (number of distinct i*j products) * c). But in the worst case, the number of distinct i*j products is up to a*b, which for a=100 and b=100 is 10,000. Then multiplying by c=100 gives 1e6 again, same as before. So no time saved.

But perhaps in practice, using this approach can avoid the nested loops in Python, which are slow.

Let's think: for each i in 1..a, j in 1..b, compute i*j and track the frequency. Then, for each possible product ij, multiply by each k in 1..c and accumulate the count. Then sum over all (ij *k) the count multiplied by d(ij*k).

But how?

Alternatively, the frequencies of each ij product can be stored in a dictionary or array. Then, for each possible ij value, we have the number of (i,j) pairs that produce it. Then, for each such ij, multiply by each possible k, and for each resulting product, multiply the count by the frequency of ij and add to the sum.

But perhaps this can be optimized.

For example:

- Precompute the frequency of each possible product of i and j. Let's call this freq_ij. freq_ij[x] is the number of (i,j) pairs where i is in 1..a, j in 1..b, and i*j =x.

Then, for each x in freq_ij, for each k in 1..c, compute y =x *k. Then, the total contribution to the sum is freq_ij[x] * d(y). Summing over all x and k.

This way, the total number of operations is (number of distinct x in freq_ij) * c. If the number of distinct x is less than a*b (which it is), this could be faster.

But how to compute freq_ij efficiently?

Let's see: For a=100, b=100, there are 100*100=10,000 possible (i,j) pairs. But the number of distinct x (products) is less than 10,000. For example, 1*100=100, 2*50=100, etc. So the actual number of distinct products would be O(ab) but perhaps with some duplicates.

But even if it's 10,000 distinct x's, then for each x, multiply by 100 k's (c=100) gives 1e6 operations again. So same as before.

But perhaps in Python, using this approach could be faster, as it replaces the triple nested loops with a double loop over i and j, then another loop over x and k.

But how to compute freq_ij?

We can compute it by initializing a dictionary and for each i and j, increment the count of i*j by 1.

So code steps:

Compute freq_ij:

freq_ij = defaultdict(int)
for i in 1..a:
    for j in 1..b:
        product = i*j
        freq_ij[product] += 1

Then, for each product in freq_ij, and for each k in 1..c, compute the total contribution: freq_ij[product] * d(product *k). Sum all these contributions.

This approach is O(ab + (number of distinct products) * c). Let's compare with the original O(abc). For a=100, b=100, c=100: original approach is 1e6 steps, this approach is 10,000 (for ab) + 10,000 *100 = 1.1e6 steps. But in Python, perhaps using loops with ab and then another step with x and k is faster than triple nested loops. Because the triple loops are in pure Python, which is slow.

So this approach could save time. Let's see:

Original approach: 1e6 triple loops in Python. Each iteration: product = i*j*k, sum += div_count[product]

Alternative approach: two loops (a and b), then for each product in the freq_ij, loop over k (c steps). But in the alternative approach, the two loops are a*b steps (1e4), and then for each product in freq_ij (say, 5e3), then 1e2 steps, leading to 5e3 *1e2= 5e5 steps. Total 1e4 +5e5= 5.1e5 steps, which is about half the original steps. But how much does that help in Python?

In Python, for loops are slow. So replacing 1e6 steps with 5.1e5 steps could save time.

So the code would be something like:

sum_ = 0
for x in freq_ij:
    count_ij = freq_ij[x]
    for k in range(1, c+1):
        product = x * k
        sum_ += count_ij * div_count[product]

sum_ %= MOD

This would be O(ab + (number of x) * c) steps, which may be better.

But what's the number of x in freq_ij for a=100 and b=100?

It's hard to say. For example, i ranges from 1 to 100, j from 1 to 100. The number of possible products could be around O(ab) but with many duplicates. For example, 1*2=2, 2*1=2. So for a=100, b=100, the number of distinct products could be approximately (100*100)/2 (if all products are unique except for order, but that's not the case). For example, 2*3=6, 3*2=6. So the actual number of distinct products could be around 50,000? Wait, no. Because for a=100 and b=100, the maximum product is 100*100=1e4. So x can be up to 1e4. So the number of possible x's is up to 1e4. So for a=100, b=100, the number of x's is at most 1e4. So the total steps for the x loop is 1e4 * c (1e2) = 1e6 steps again. So no gain here. Wait, but in the alternative approach, the inner loop is over k, and for each x, we process c steps. So for 1e4 x's and 1e2 k's, that's 1e6 steps again. So the total steps are same as the original approach. But in Python, perhaps the way of processing this is faster.

Alternatively, maybe using list comprehensions or other vectorized operations. But I'm not sure.

Wait, but in the alternative approach, the two loops (a and b) are 1e4 steps, which in Python is manageable. Then, for each x in freq_ij, which is 1e4 steps, multiplied by 1e2 steps (k), again 1e6 steps. But the inner loop (k) can be optimized. For example, precompute for each x, the sum over k of d(x*k), and multiply by count_ij.

But how?

For each x, compute the sum of d(x*k) for k=1..c. Then multiply that sum by count_ij and add to the total.

So for each x, we need to compute sum_d = sum_{k=1 to c} d(x*k). Then, the contribution is count_ij * sum_d.

So the code would be:

sum_ = 0
for x in freq_ij:
    sum_d = 0
    for k in 1..c:
        sum_d += div_count[x *k]
    sum_ += freq_ij[x] * sum_d

But this is the same as before. But maybe, for each x, we can compute x*k for k up to c, and sum the div_count of those products. But this is O(c) per x.

Alternatively, perhaps precompute for all possible x (up to 1e4) and for each x, precompute the sum of d(x*k) for k from 1 to c. But this would require precomputing for x up to 1e4 and k up to 1e2, which is 1e4 * 1e2 = 1e6 entries. But since x can be up to 1e4, and the product x*k can be up to 1e4 * 1e2 = 1e6, which is within the precomputed div_count array.

But this approach doesn't save steps, but perhaps in Python, precomputing a cache for x and k would be slower.

So, perhaps the alternative approach is better, but it's not clear. Let's proceed with implementing it.

Now, the next step is to code this.

But first, the sieve for div_count.

The maximum possible product is a*b*c, which can be up to 1e6 (since a, b, c <= 100). So we need to precompute div_count up to 1e6.

Wait, 100*100*100=1,000,000. So yes.

So the sieve code would be:

max_n = a * b * c
div_count = [0] * (max_n + 1)
for d in range(1, max_n + 1):
    for multiple in range(d, max_n + 1, d):
        div_count[multiple] += 1

But in Python, the sieve can be created as such. But we need to read a, b, c first to compute max_n. So the code structure would be:

Read a, b, c.

max_product = a * b * c

Compute div_count for 1..max_product.

But in the problem statement, a, b, c can be as small as 1. So if a=1, b=1, c=1, the product is 1. So the sieve code must handle that.

Now, the code steps:

Read a, b, c.

Compute max_product = a*b*c.

Initialize div_count array.

Then, for each d in 1 to max_product:

   for multiple in d, 2d, ... up to max_product:

       div_count[multiple] += 1.

This is O(max_product log max_product) time, which for max_product=1e6 is manageable.

Once div_count is precomputed, then proceed to compute the sum.

Now, which approach is better for the sum: triple loops or the alternative approach?

In Python, the triple nested loops may be too slow for 1e6 iterations. Let's see:

In Python, a loop like:

sum_ = 0
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            sum_ += div_count[i*j*k]

But for a=100, b=100, c=100, this is 1e6 iterations. Each iteration involves multiplying three numbers (i, j, k) to get i*j*k, then accessing the div_count array, then adding to sum. But in Python, each loop iteration has some overhead.

An alternative is to precompute all possible i*j*k in a list, then sum the div_count for each element, but that would require generating a list of 1e6 elements, which is possible but may not save time.

Alternatively, use itertools.product to generate the triplets, but again, not sure.

But perhaps the alternative approach with the freq_ij is better. Let's see:

Compute freq_ij as a dictionary where keys are the products i*j and values are the counts. Then, for each x in freq_ij, loop through k from 1 to c, compute x*k, and add freq_ij[x] * div_count[x*k] to the sum.

This reduces the code from three loops to two loops (a and b) plus a loop over x and k. The total number of operations is a*b + (number of x) * c. For a=100, b=100, c=100, this is 1e4 + (number of x)*1e2. If the number of x is 5e3, then total is 1e4 +5e5 =5.1e5 operations, which is half of the original 1e6.

But in Python, dictionaries are slower than list lookups, but the key is the product x. So perhaps the code is:

from collections import defaultdict

freq_ij = defaultdict(int)
for i in range(1, a+1):
    for j in range(1, b+1):
        product_ij = i * j
        freq_ij[product_ij] += 1

sum_ = 0
for x in freq_ij:
    count = freq_ij[x]
    for k in range(1, c+1):
        product = x * k
        sum_ += count * div_count[product]

sum_ %= MOD

But this code has two loops: one for i and j (1e4 steps) and another for x and k (1e6 steps). So the same as the triple loop approach in terms of steps, but perhaps faster because the inner loop is written in Python's for loops, which may be more efficient than triple loops.

But in Python, nested loops are inherently slow. So perhaps the triple loop is manageable. Let's see:

Another approach: use a generator expression and sum all at once.

sum_ = sum(div_count[i*j*k] for i in range(1, a+1) for j in range(1, b+1) for k in range(1, c+1)) % MOD

But this is a one-liner, but still involves 1e6 iterations. In Python, generator expressions are fast, but for 1e6 elements, it's manageable. Let's test with a=100, b=100, c=100. But the time is the main concern.

In the problem statement, the time limit is 2 seconds. So the code must run in under 2 seconds. Let's consider that in Python, each loop iteration is roughly 0.1 microseconds (but this is a rough estimate). For 1e6 iterations, that's 0.1 seconds. So the code would be acceptable. But the sieve part for 1e6 elements may take some time.

But let's see:

The sieve for 1e6 elements:

for d in 1 to 1e6:

   for multiple in range(d, 1e6+1, d):

       div_count[multiple] +=1

Each iteration for d=1: 1e6 steps.

d=2: 5e5 steps.

d=3: ~3.3e5 steps.

...

The sum of all steps is O(1e6 log 1e6), which is around 1.4e7 operations. In Python, each operation is a list increment, which is O(1). So 1e7 operations in Python would take maybe a second. So the sieve would take around 1 second. Then, the triple loops would take another 0.1-0.5 seconds. So the total time is under 2 seconds.

But when a=100, b=100, c=100, the max product is 1e6, so sieve is for 1e6 elements. So sieve is O(1e6 log 1e6) steps.

But how to optimize the sieve?

Wait, in the sieve, for each d, we increment all multiples of d. But in Python, loops for ranges are optimized. So the code:

for d in range(1, max_product + 1):
    for multiple in range(d, max_product +1, d):
        div_count[multiple] +=1

This is written in a way that the inner loop is handled by the range function, which is implemented in C. So this part might be relatively fast.

So the sieve code could be efficient enough.

So the overall code structure would be:

Read a, b, c.

Compute max_product = a*b*c.

If max_product is 0, then all are 0, but since a, b, c are at least 1, max_product is at least 1.

Compute div_count for 1..max_product.

Compute the sum of div_count[i*j*k] for all triplets.

Mod the sum by 1073741824.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    a, b, c = map(int, input_stream.readline().rstrip("\n").split())

    max_product = a * b * c
    MOD = 1073741824

    # Precompute divisor counts
    div_count = [0] * (max_product + 1)
    for d in range(1, max_product + 1):
        for multiple in range(d, max_product + 1, d):
            div_count[multiple] += 1

    sum_ = 0
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                sum_ += div_count[i * j * k]

    print(sum_ % MOD, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 6 7
""",
            "output": \
"""\
1520
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

Sample Input 2:

5 6 7

Output 1520. So code should handle that.

But in Python, the triple loops for a=100, b=100, c=100 would be 1e6 iterations. Each iteration involves i, j, k and the product. How much time would this take?

In Python, each loop iteration is slow. For example, 1e6 loop iterations can take about 0.1 seconds if it's a simple loop. But with three nested loops and arithmetic operations, it's possible that it takes longer. For instance, the inner loop in Python is slow. So 1e6 iterations might take 0.5-1 second. Combined with the sieve taking about 1 second, the total time would be under 2 seconds.

But what if a=100, b=100, c=100? The sieve would process up to 1e6, which is 1e6 steps for the outer loop, each with multiple inner steps.

Wait, the sieve code for d in 1 to 1e6:

for d in 1 to 1e6:

   for multiple in range(d, 1e6+1, d):

       div_count[multiple] +=1

The total number of operations is the sum for each d of (1e6 // d). For d=1, 1e6 operations. For d=2, 5e5 operations. And so on. The sum is approximately 1e6 * ln(1e6) + O(1e6). The natural log of 1e6 is about 14. So sum is about 1e6 * 14 = 1.4e7 operations. In Python, each operation is a list index and an increment. That's about 1.4e7 operations. How long would that take? Let's see, in Python, a for loop can process about 1e6 operations per second. So 1.4e7 operations would take about 14 seconds. Oh no, that's way too slow. So this approach would not work for a=100, b=100, c=100, as the sieve would take 14 seconds.

Wait, that's a problem. Because 1e6 is 1,000,000. So for d=1, the inner loop runs 1e6 times. For d=2, 5e5 times. For d=3, 333,333 times. And so on.

In Python, this is going to be way too slow. So the sieve approach is not feasible for 1e6 in Python.

So this is a problem. So we need to find a better way to compute d(i*j*k).

Alternative approach: compute the number of divisors of i*j*k on the fly, using the prime factors.

The number of divisors of a number is the product of (e_i +1) for each prime's exponent e_i in the prime factorization of the number.

So if we can compute the prime factors of i*j*k and their exponents, we can compute d(i*j*k) efficiently.

But how to compute the prime factors of i*j*k quickly.

But for i, j, k each up to 100, their product's prime factors can be found by combining the prime factors of i, j, and k.

So the idea is:

For each triplet (i,j,k), compute the exponents of primes in i*j*k by adding the exponents from i, j, and k. Then compute the product of (e_p +1) for all primes p.

But how to precompute the prime factors of numbers up to 100?

We can precompute for each number from 1 to 100, its prime factors. Then, for each triplet, combine the factors of i, j, and k, sum their exponents, and compute the product of (e +1).

This approach could be much faster, as it avoids the sieve for large n.

So the steps:

1. Precompute the prime factorization for all numbers from 1 to 100. For example, 6 factors into 2^1 * 3^1.

2. For each triplet (i,j,k), compute the combined prime factors by adding the exponents from i, j, and k. For example, i=2 (2^1), j=3 (3^1), k=4 (2^2), then the combined factors are 2^(1+0+2) * 3^(0+1+0) * ... etc.

3. Compute the product of (e_p +1) for all primes p present in the combined factors. This gives d(i*j*k).

4. Sum all these values modulo 2^30.

This approach's time complexity depends on the number of triplets (1e6) and the time to combine the prime factors for each triplet.

But how efficient is this?

For numbers up to 100, the primes are up to 97. So the list of primes up to 100 is [2,3,5,7,11,...,97]. There are 25 primes less than 100.

For each number up to 100, its prime factors can be represented as a dictionary or a list of (prime, exponent) pairs. For example, 6 would have {2:1, 3:1}.

So precompute a list for each number from 1 to 100, storing their prime factors.

Then, for each triplet (i,j,k), we can:

- Initialize a dictionary to track exponents.

- For each of i, j, k, iterate through their prime factors and add the exponents to the dictionary.

- Then, compute the product of (exponent +1) for all primes in the dictionary.

But in Python, dictionaries are somewhat slow. So perhaps, for each number, precompute a list of primes and exponents, and then for each triplet, merge the three lists into a single exponents dict.

But even this, for 1e6 triplets, each requiring merging three lists of primes (each up to say 3 primes per number) into a dict, then computing the product of (e+1), could be manageable.

Let's think. For each triplet:

- For i, j, k, look up their factors (precomputed).

- For each of their factors, add to a dictionary of exponents.

- Then, compute the product of (e+1).

But merging three factors for each triplet could be time-consuming. For example, for each triplet, the total number of primes considered is up to the sum of primes in i, j, and k. Since each number up to 100 can have at most log2(100) = 6 factors (like 64=2^6), but in reality, numbers like 60=2^2*3*5 have three primes. So each number has factors with a small number of primes.

So for each triplet, merging three numbers' factors may involve up to, say, 3*3=9 primes per number (but likely much less). So per triplet, we'd process maybe 10 primes, which is manageable.

So steps:

1. Precompute for each number x in 1..100, its prime factors as a dictionary (prime: exponent).

For example, factors[6] = {2:1, 3:1}.

2. For each triplet (i,j,k), combine the factors of i, j, k into a single dictionary, summing exponents.

3. The product of (e+1) for all primes in the combined dictionary is d(i*j*k).

4. Sum all these products.

This approach avoids precomputing the sieve for large numbers. It uses the fact that each triplet's product is up to 1e6, but instead of precomputing their divisor counts, we compute them on the fly using the factors.

So the question is: which approach is faster in Python?

The sieve approach is O(1e6 log 1e6) steps (which is too slow for Python), whereas the factorization approach is O(1e6 * 10) steps (processing 10 primes per triplet), which is 1e7 steps. But each step involves hash lookups and arithmetic.

But let's proceed to implement the factorization approach.

Implementing the factorization approach:

First, precompute factors for each number up to 100.

How to factorize a number? We can precompute primes up to 100, then for each number, divide by the primes and compute exponents.

Primes up to 100: [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97].

We can generate this list.

Then, for each x from 1 to 100:

   factors[x] = {}

   for p in primes:

       if p*p > x:

           break

       if x % p ==0:

           count =0

           while x % p ==0:

               count +=1

               x = x // p

           factors[x][p] = count

   if x >1:

       factors[x][p] =1  # Wait, no. If x is reduced to a prime larger than sqrt(original x), then add that.

Wait, perhaps a better way to factorize x:

Initialize x_copy = x.

Initialize a dictionary.

For each p in primes list (sorted):

   if p*p >x_copy:

       break

   if x_copy % p ==0:

       count =0

       while x_copy % p ==0:

           count +=1

           x_copy = x_copy //p

       factors[x][p] = count

if x_copy >1:

   factors[x][x_copy] =1

But this code would need to be written correctly.

But for numbers up to 100, this can be done quickly.

Alternatively, using trial division for each x from 1 to 100.

But this is manageable.

So code for precomputing factors:

primes_up_to_100 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

# Precompute factors for each number from 1 to 100
factors = [{} for _ in range(101)]  # factors[x] is a dict of primes to exponents

for x in range(1, 101):
    num = x
    for p in primes_up_to_100:
        if p*p > num:
            break
        if num % p == 0:
            cnt = 0
            while num % p == 0:
                cnt +=1
                num = num //p
            factors[x][p] = cnt
    if num >1:
        factors[x][num] = 1

But wait, for x=1, num will be 1 after loop, so factors[1] is empty. Which is correct.

So this code generates for each x from 1 to 100, a dictionary of primes and exponents.

Once factors are precomputed, for each triplet (i,j,k), we can merge their factors.

For example, for i=2, j=3, k=4:

i's factors: {2:1}

j's factors: {3:1}

k's factors: {2:2}

Merged factors: {2:1+0+2=3, 3:0+1+0=1}

The product of (3+1)*(1+1) =4*2=8. Which is d(2*3*4=24) = divisors are 1,2,3,4,6,8,12,24 → 8 divisors. Correct.

So the code would be:

sum_ =0
for i in 1..a:
    for j in 1..b:
        for k in 1..c:
            exponents = {}
            # Combine factors of i, j, k
            for d in [i, j, k]:
                for p, cnt in factors[d].items():
                    exponents[p] = exponents.get(p, 0) + cnt
            # Compute the product of (e +1)
            res = 1
            for e in exponents.values():
                res *= (e +1)
            sum_ += res
sum_ %= MOD

This code for each triplet combines the factors of i, j, k and computes the product of exponents+1.

But this approach involves three nested loops (1e6 iterations), and for each iteration, looping through the factors of i, j, k. The factors for each number are small (like 2-3 primes per number). So per triplet, we'd have to process 3 * average number of primes per number.

For example, each number has on average 2 primes. So per triplet, 3 * 2 =6 primes. So for 1e6 triplets, 6e6 operations, which is manageable.

But in Python, creating a new dictionary for each triplet and merging the factors could be slow. So perhaps using a defaultdict or other optimized data structure can help.

Alternative approach: use a list to collect all primes from i, j, k, then count their exponents. But that would require merging three lists of primes.

For example, for each triplet, collect all primes from i, j, k, then count their exponents.

But how to do this efficiently.

Another idea: for each of i, j, k, their factors are stored as dictionaries. For the triplet, iterate through the factors of i, then j, then k, and add their exponents to a single dictionary. Then compute the product.

In Python, dictionaries have items() which can be iterated. For example:

exponents = {}
for p, cnt in factors[i].items():
    exponents[p] = exponents.get(p, 0) + cnt
for p, cnt in factors[j].items():
    exponents[p] = exponents.get(p, 0) + cnt
for p, cnt in factors[k].items():
    exponents[p] = exponents.get(p, 0) + cnt

But this code loops through each of the three factors, and accumulates the counts.

But in Python, function calls and loops are relatively slow. For 1e6 triplets, each with three loops over factors, this could be expensive.

Another optimization: precompute for each number x a list of (prime, exponent) pairs. Then, for each triplet, iterate through the three lists and add the exponents.

For example, factors[i] is a list like [(p1, e1), (p2, e2), ...].

Then, for a triplet:

exponents = defaultdict(int)
for x in [i, j, k]:
    for p, e in factors[x]:
        exponents[p] += e
res = 1
for e in exponents.values():
    res *= (e +1)

But using defaultdict might be faster than using get and set.

So changing the factors to be stored as lists of tuples for each number.

So precompute factors as a list of lists:

factors = [[] for _ in range(101)]

Then, for x in 1..100:

   factors[x] is a list of (prime, exponent) tuples.

This way, during the triplet processing, for each x in [i,j,k], we can loop through factors[x] and add to a defaultdict.

So code:

from collections import defaultdict

sum_ =0
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            exponents = defaultdict(int)
            for x in [i,j,k]:
                for p, e in factors[x]:
                    exponents[p] += e
            res = 1
            for e in exponents.values():
                res *= (e +1)
            sum_ += res

sum_ %= MOD

This could be faster than using dictionaries for factors, as list iteration is faster.

So the key steps are:

- Precompute factors as lists of tuples for each number.

- For each triplet, loop through the factors of i, j, k and accumulate exponents in a defaultdict.

- Compute the product of (e+1).

Now, the factors for each number can be precomputed as lists of tuples. For example, for x=6, factors[6] would be [(2,1), (3,1)].

So the code for precomputing factors would be:

primes_up_to_100 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

factors = [[] for _ in range(101)]  # factors[x] is a list of (p, e) tuples.

for x in range(1, 101):
    num = x
    temp_factors = []
    for p in primes_up_to_100:
        if p*p > num:
            break
        if num % p ==0:
            cnt =0
            while num % p ==0:
                cnt +=1
                num = num //p
            temp_factors.append( (p, cnt) )
    if num >1:
        temp_factors.append( (num, 1) )
    factors[x] = temp_factors

So this code correctly generates the list of prime factors for each x.

Now, the triplet processing code:

sum_ = 0
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            exp = defaultdict(int)
            for x in [i, j, k]:
                for (p, e) in factors[x]:
                    exp[p] += e
            res = 1
            for e in exp.values():
                res *= (e +1)
            sum_ += res

sum_ %= 1073741824

This code uses defaultdict to accumulate exponents for each prime.

But in Python, defaultdict has some overhead. So perhaps using a regular dictionary and checking for keys would be faster. But I'm not sure. Alternatively, for each prime in the factors, increment the count in a dict.

But this code may be fast enough for the constraints.

Let's estimate the time:

For each triplet, the innermost code:

Loop over i, j, k.

For each, loop over factors[i], factors[j], factors[k].

Each factors list has, on average, 2-3 primes.

So for each triplet, 3 * 3 =9 primes.

For each of these primes, look up in the defaultdict and add the exponent.

Then, compute the product of (e+1) for all primes.

Assuming that each triplet's processing takes about 100 operations, for 1e6 triplets, that's 1e8 operations. Which in Python may take around 10 seconds. Which is way over the time limit.

But this approach is not feasible either.

So what's the alternative?

Alternative approach: precompute all possible products of i, j, k, and compute their divisor counts using precomputed exponents.

Wait, but how?

Another idea: note that the order of multiplication doesn't affect the number of divisors. So, the exponents in the prime factors are additive, regardless of the order of multiplication.

But the problem is that for each triplet (i,j,k), the product's prime factors are the sum of the exponents from i, j, and k.

So, perhaps we can precompute for each number x from 1 to 100, its prime exponents, and for each triplet, sum the exponents of i, j, and k, then compute the product of (e_p +1).

But to compute this efficiently, we can precompute for each x from 1 to 100, a list of primes and their exponents. Then, for a triplet (i,j,k), the exponents are the sum of the exponents of i, j, and k for each prime.

The question is how to compute this sum efficiently.

Another optimization: since the primes up to 100 are fixed, we can represent the exponents for a number as a dictionary where the keys are the primes up to 100, and the values are the exponents. This way, for each number, we have a fixed number of primes (25) and can store the exponents in a list or array.

For example, create a list of primes in order. For each number x, create an array where each entry is the exponent of the corresponding prime in x's factorization. Then, for a triplet (i,j,k), sum their exponent arrays element-wise, and compute the product of (e+1) for all non-zero exponents.

This could be more efficient, as the primes are fixed and we can use pre-allocated arrays.

Let's try this approach.

List of primes up to 100: let's order them, say, in increasing order. The list is:

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

There are 25 primes.

For each number x from 1 to 100, create an array of exponents for each prime in this list. For example, x=6 will have exponents [1,1,0,0,...0].

Then, for a triplet (i,j,k), the exponents are the sum of the exponents of i, j, and k for each prime. Then, for each prime in the list, if the sum is zero, we ignore it; otherwise, multiply (sum +1) into the result.

So precompute for each x from 1 to 100, an array of exponents, indexed by the primes list.

Then, for a triplet, compute the sum of exponents for each prime, then compute the product of (sum + 1) for primes where sum >0.

This way, each triplet's processing is a loop over 25 primes, adding their exponents and computing the product. But even if many exponents are zero, we still have to loop through all 25 primes.

But for 1e6 triplets, 25 operations per triplet is 25e6 operations, which is manageable.

But how to implement this.

Steps:

1. Precompute for each x from 1 to 100, an array (size 25) where each element is the exponent of the corresponding prime in x's factorization.

For example, x=2:

exponents[0] =1 (since primes[0] is 2)

others are zero.

x=6: exponents[0]=1 (2), exponents[1]=1 (3), others 0.

x=100: exponents[0]=2, exponents[2]=2 (5^2).

2. For each triplet (i,j,k):

   sum_exponents = [0] * 25

   sum_exponents = exponents[i][p] + exponents[j][p] + exponents[k][p] for each p in 0..24

   res = 1

   for p in 0..24:

       e = sum_exponents[p]

       if e >0:

           res *= (e +1)

   sum_ += res

So the code would look like:

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

exponents_dict = [[0]*len(primes) for _ in range(101)]  # exponents_dict[x][p_idx] is the exponent of primes[p_idx] in x's factorization.

for x in range(1, 101):
    num = x
    for p_idx, p in enumerate(primes):
        if num ==1:
            break
        cnt =0
        while num % p ==0:
            cnt +=1
            num = num //p
        exponents_dict[x][p_idx] = cnt

Now, for x=1, all exponents are zero.

For example, x=6:

primes are [2,3,5,7,...]. exponents_dict[6][0] =1, exponents_dict[6][1]=1, others 0.

Once this is precomputed, then for each triplet (i,j,k), we can sum the exponents for each prime:

sum_exponents = [exponents_dict[i][p_idx] + exponents_dict[j][p_idx] + exponents_dict[k][p_idx] for p_idx in range(len(primes))]

Then compute the product of (e + 1) for all e in sum_exponents where e >0.

But how to do this efficiently.

But even if e is zero, adding 1 and multiplying would multiply by 1, which has no effect. So we can compute the product as the product of (sum_exponents[p_idx] +1) for all p_idx in 0..24.

Because if sum_exponents[p_idx] is zero, then (0+1) is 1, which doesn't change the product.

So the code can be:

res = 1

for p_idx in range(len(primes)):
    res *= (sum_exponents[p_idx] + 1)

sum_ += res

This is a critical insight! Because even if a prime doesn't divide the product, adding 1 and multiplying by 1 has no effect. So we can ignore checking for e >0 and just multiply all (e +1).

This way, for each triplet, we loop through all 25 primes and multiply (e+1) for each. For primes not in the product's factors, e is 0, so (0+1) is 1, and multiplying by 1 doesn't change the product.

This reduces the code to:

sum_ =0
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            res = 1
            for p_idx in range(25):
                e = exponents_dict[i][p_idx] + exponents_dict[j][p_idx] + exponents_dict[k][p_idx]
                res *= (e +1)
            sum_ += res

sum_ %= MOD

This approach avoids using dictionaries and uses fixed-size arrays. This should be much faster in Python because list indexing is fast, and loops over fixed-size ranges are manageable.

So the steps are:

1. Precompute exponents_dict for each x from 1 to 100, using a list of 25 elements (exponents for each prime up to 100).

2. For each triplet, sum the exponents for each of the 25 primes, then compute the product of (e+1) for all primes, and add to the sum.

This approach requires for each triplet:

- 25 additions (summing exponents)

- 25 multiplications (product of (e+1))

But 25 operations per triplet, multiplied by 1e6 triplets, gives 25e6 operations. In Python, this should be manageable.

But even 25e6 operations in Python would take some time. For example, in Python, a loop with 25e6 iterations (each being a few operations) would take around a second or two. So this approach is feasible.

Let's test this code with the sample input.

Sample Input 1:

2 2 2

For triplet (1,1,1):

exponents_dict[1][p_idx] is 0 for all p_idx.

So for each p_idx, e=0+0+0=0. res = product of 1s → 1.

Which matches d(1)=1.

For triplet (1,1,2):

exponents_dict[2][0] =1 (prime 2).

sum exponents for 2: 0+0+1=1. So (1+1) =2. Other primes are 0. So res=2.

Which matches d(2)=2.

And so on.

So the code works.

Sample Input 2:

5 6 7

Output is 1520. Which the code should handle.

So this approach is correct.

Now, the code in Python:

Read a, b, c.

Precompute exponents_dict.

Then, iterate through all triplets, summing the product of (e+1) for all 25 primes.

This code should be fast enough.

So the final code:

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
MOD = 1073741824

# Precompute exponents for each number up to 100
exponents_dict = [[0]*len(primes) for _ in range(101)]  # 0..100

for x in range(1, 101):
    num = x
    for p_idx, p in enumerate(primes):
        if num == 0:
            break
        cnt = 0
        while num % p == 0:
            cnt += 1
            num = num // p
        exponents_dict[x][p_idx] = cnt

a, b, c = map(int, input().split())

total = 0
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            product = 1
            for p_idx in range(len(primes)):
                e = exponents_dict[i][p_idx] + exponents_dict[j][p_idx] + exponents_dict[k][p_idx]
                product *= (e + 1)
            total += product

print(total % MOD)

But wait, in Python, even this code may be slow for a=100, b=100, c=100. Because the nested loops are in Python, which is slow.

For example, the triple loops are 1e6 iterations. Each iteration has a loop over 25 primes. So 1e6 *25 = 25e6 operations. In Python, each loop iteration is slow. For example, if each of the 25 iterations takes 0.1 microseconds, the total time is 25e6 * 0.1e-6 = 2.5 seconds. Which is within the 2-second time limit.

But in reality, Python's loop overhead is higher. For example, each for p_idx in range(25) loop may take more time.

So how to optimize this code?

One possible optimization is to precompute the exponents for i, j, and k, and then compute the sum of exponents for each prime in a more vectorized way. But this is difficult in Python.

Another idea is to precompute for each possible i and j, their combined exponents, and then for each k, compute the triplet sum.

But this would require storing the combined exponents of i and j, which is a list of 25 elements for each pair (i,j). For a=100 and b=100, this is 1e4 pairs, each requiring 25 integers. This is 25e4 integers, which is manageable.

Then, for each pair (i,j), their combined exponents are stored, and for each k, the triplet exponents are the combined exponents of (i,j) plus exponents of k. Then compute the product of (e+1) for each prime.

This approach would reduce the number of loops from 1e6 to 1e4 (i,j pairs) plus 1e4 *1e2 (k for each pair) = 1e6 operations. But each step is still O(25) operations.

So code steps:

Compute for each (i,j) the sum of exponents.

pre_ij = a list where pre_ij[i][j] is the sum of exponents of i and j.

But in Python, this would require a nested loop for i and j.

But for each (i,j), sum the exponents:

for i in 1..a:

    for j in 1..b:

        combined = [exponents_dict[i][p] + exponents_dict[j][p] for p in range(25)]

        store combined.

Then, for each (i,j), when k is processed, the triplet exponents are combined plus exponents_dict[k][p].

This way, for each (i,j), we loop through k=1..c, and for each k, the exponents are pre_ij[i][j] + exponents_dict[k][p].

But storing pre_ij as a list of lists for each i and j.

But for a=100 and b=100, this requires 1e4 entries, each of 25 integers. That's 25e4 integers, which is manageable.

So code:

pre_ij = []
for i in range(1, a+1):
    for j in range(1, b+1):
        combined = [exponents_dict[i][p] + exponents_dict[j][p] for p in range(25)]
        pre_ij.append(combined)

Then, for each combined in pre_ij, and for k in 1..c:

    exponents = [combined[p] + exponents_dict[k][p] for p in range(25)]

    product = 1

    for p in range(25):

        product *= (exponents[p] + 1)

    total += product

This way, the code is:

pre_ij = []
for i in range(1, a+1):
    for j in range(1, b+1):
        combined = [exponents_dict[i][p] + exponents_dict[j][p] for p in range(25)]
        pre_ij.append(combined)

total =0
for combined in pre_ij:
    for k in range(1, c+1):
        product =1
        for p in range(25):
            e = combined[p] + exponents_dict[k][p]
            product *= (e +1)
        total += product

print(total % MOD)

But this code changes the loop structure to two nested loops (i,j) and (k), but the total number of operations is the same: 1e4 (i,j) * 1e2 (k) = 1e6 iterations, each with 25 operations. But in Python, it's possible that this code is faster, as the loops over i and j are merged into a single loop for pre_ij, and the inner loop over k is separated.

But the code may not be faster, as it's the same number of operations.

Another optimization is to precompute the exponents for k and store them, but this also doesn't save time.

An alternative approach is to use NumPy arrays to vectorize the operations, but given that the code must be in pure Python and use only standard libraries, this is not possible.

Another idea is to precompute for each k its exponents and compute the sum in a way that minimizes loops.

But perhaps the fastest way in Python is to use the triple loop with the exponents stored in lists and minimize the operations inside the loops.

Alternatively, precompute all possible exponents for i, j, and k and then combine them.

But I'm not sure.

But considering the code with the exponents stored in lists and loops over 25 primes for each triplet, this seems to be the best approach.

Thus, the final code is as follows:

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
MOD = 1073741824

exponents = [[0] * len(primes) for _ in range(101)]

for x in range(1, 101):
    num = x
    for idx, p in enumerate(primes):
        if num == 0:
            break
        cnt = 0
        while num % p == 0:
            cnt += 1
            num = num // p
        exponents[x][idx] = cnt

a, b, c = map(int, input().split())

total = 0

for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            res = 1
            for p in range(len(primes)):
                e = exponents[i][p] + exponents[j][p] + exponents[k][p]
                res *= (e + 1)
            total += res

print(total % MOD)

This code should handle the problem efficiently within the time constraints.
</think>

```python
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
MOD = 1073741824

# Precompute exponents for each number up to 100
exponents = [[0] * len(primes) for _ in range(101)]

for x in range(1, 101):
    num = x
    for idx, p in enumerate(primes):
        if num == 0:
            break
        cnt = 0
        while num % p == 0:
            cnt += 1
            num = num // p
        exponents[x][idx] = cnt

a, b, c = map(int, input().split())

total = 0

for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            res = 1
            for p in range(len(primes)):
                e = exponents[i][p] + exponents[j][p] + exponents[k][p]
                res *= (e + 1)
            total += res

print(total % MOD)
```
