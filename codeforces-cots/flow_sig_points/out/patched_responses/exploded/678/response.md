<think>
Okay, let's tackle this problem. So the task is to compute the sum p, which is the total number of sheets of paper used over n years. Each year starts with a days, then a+1, up to a+n-1 days. For each of these years, we need to find the maximum square divisor of the number of days in that year. Then, for each year, the number of sheets is the number of days divided by the square divisor. Because the maximum square divisor is the largest square that divides the year's days, the number of months (and thus sheets) is days / s, where s is the square.

So the problem reduces to, for each number x in the range [a, a+n-1], find the largest square that divides x. Then sum x divided by that square for all x in this range.

The challenge is to compute this efficiently for large values of a and n (up to 1e7 each, with a +n-1 up to 1e7). Let's think about the constraints. The maximum possible x is 1e7, and n can be up to 1e7. So a naive approach of checking each x individually and factorizing them would be too slow. For example, if we factor each x and compute the largest square divisor, that's O(n * sqrt(x)), which would be way too slow for n=1e7.

We need a more efficient way. Let's think about precomputing for all x up to 1e7 the largest square divisor. Then, for each x in the range, we can look up the precomputed value and compute x divided by that square.

So the key is to precompute, for each x up to 1e7, the maximum square that divides x. Once we have that, the sum can be computed in O(n) time.

The question is: how to compute the maximum square divisor for all x efficiently.

The maximum square divisor of x is the product of the even exponents of the prime factors. For example, if x = 2^3 *3^5 *5^0, then the square divisor is 2^2 *3^4 = (2*3^2)^2. The remaining exponents (2^1 *3^1) would be part of x divided by the square. So the square is the product of primes to the highest even exponents possible.

Alternatively, the maximum square divisor is the product of primes in the prime factorization of x with even exponents. So, for each x, the largest square divisor s is such that s divides x, and s is a square, and s is as large as possible. Then x/s is square-free (since after dividing by s, all exponents are even, but s takes the maximum possible even exponents).

Wait, no. Wait, the largest square divisor is the product of primes with exponents divided by 2, multiplied by 2. Wait, perhaps the standard way is to compute the square part. Let's think of x = m^2 * k, where k is square-free. Then the largest square divisor is m^2, and x / m^2 is k, which is square-free. So for x, the largest square divisor is x divided by the square-free part of x.

So the problem is equivalent to finding for each x, the square-free part (k) and then the number of sheets is k, because x / m^2 = k. Wait no: x = m² * k, where k is square-free. Then the number of sheets is x / (m²) = k. Wait, that's not right. Because x/s is the number of sheets, where s is the largest square divisor. So if x = s * (x/s), and s is the largest square possible. But x/s must be square-free. Because if x/s had a square factor, then s could be multiplied by that square and get a larger square divisor, which would contradict s being the maximum.

So, the number of sheets per year is x divided by the largest square divisor of x. Which is equal to the square-free part of x. Because x can be written as (m²) * k, where k is square-free. Then s = m², and x/s =k. So the number of sheets is k. So for each x, the answer is the square-free part of x.

So the problem reduces to, for each x in [a, a+n-1], compute the square-free part of x, then sum all those k's.

Now, the problem becomes: compute the sum of the square-free parts of all numbers in a given interval. So the key is to compute the square-free part for each x efficiently.

How to compute the square-free part of a number? The square-free part is the product of primes that appear an odd number of times in the prime factorization of x. For example, if x= 2^3 *3^4 *5^1, then the square-free part is 2^1 *5^1 = 10.

So the square-free part is x divided by the largest square divisor.

So how do we compute this for all x up to 1e7 efficiently?

The standard approach is to precompute for each number its smallest prime factor (SPF), then use that to factorize each number. But factorizing each number up to 1e7 and computing the square-free part could be manageable if optimized properly. However, with n up to 1e7, and each x up to 1e7, we need a solution that is O(1e7) time.

Alternative approach: precompute for each x up to 1e7 its square-free part.

The square-free part can be computed using inclusion-exclusion of square factors. For example, for each x, any square divisor is a multiple of squares of primes. So the square-free part is x divided by all squares of primes that divide x. Wait, but that's not correct. For example, x=72=2^3*3^2. The square-free part is 2, because 72 = (2*3)^2 * 2. So the square-free part is 2. So the square-free part is the product of primes that have an odd exponent in the prime factorization.

So the approach is to, for each x, track the exponents of its prime factors modulo 2. For primes with even exponents, they are excluded from the square-free part. For primes with odd exponents, they are included once.

So the square-free part can be computed by multiplying the primes that have an odd exponent in x's factorization.

So the idea is to precompute the square-free part for each x. How?

An efficient way is to use a sieve-like approach. We can initialize an array square_free where square_free[x] is the product of primes with odd exponents in x's factorization.

We can compute this using the sieve of Eratosthenes. For each prime p, we iterate through all multiples of p, and for each multiple x, we divide x by p as many times as possible, and check if the exponent is odd. If so, multiply square_free[x] by p. Wait, perhaps this is manageable.

Let me think: start with square_free[x] = 1 for all x. Then for each prime p, we process all multiples of p. For each multiple x, we count the exponent of p in x. If the exponent is odd, multiply square_free[x] by p, else multiply by 1 (do nothing).

But how to efficiently compute, for each x, the product of primes p where the exponent of p in x's factorization is odd.

Alternatively, we can use a sieve approach where for each prime p, we flip the square_free[x] by multiplying by p for each x divisible by p an odd number of times.

But perhaps a better approach is to factor each x into primes and track the exponents mod 2.

But for x up to 1e7, factorization per x is O(number of primes up to sqrt(x)), which might be manageable if optimized.

Alternatively, here's a method inspired by the sieve of Eratosthenes:

We can compute for each x the square-free part as follows. Initialize the square_free array as 1. Then, for each prime p (using sieve), iterate over multiples of p, and for each x divisible by p, divide x by p as many times as possible. For each x, the exponent of p in x is the count of how many times p divides x. Then, if the exponent is odd, multiply the square_free[x] by p.

But how to do this efficiently.

Another approach: for each x from 1 to max_x (1e7), we can compute its square-free part by multiplying p for each prime p dividing x an odd number of times.

To compute this, we can for each x, maintain a list of primes that divide x, and track the exponents modulo 2.

But with x up to 1e7, and primes up to 1e7, this requires a sieve-based approach.

Alternatively, here's a way:

We can use a sieve to process each prime p and for each multiple of p^2, divide it by p^2. Then, the remaining part is square-free.

Wait, perhaps this is a better approach. Let me think.

The square-free part can be obtained by dividing x by the largest square divisor. Another way to compute it is to factor x into primes, and for each prime p, if it appears with exponent e, then include p in the square-free part if e is odd.

But how to compute this for all x efficiently.

Another idea: for each x, the square-free part is x divided by the product of all primes squared that divide x. Wait, no. For example, x=72=2^3 *3^2. The square-free part is 2. If we divide x by 2^2 (since 3^2 is even), but 72/(2^2 *3^2) = 72/(4*9) = 2. So square-free part is 2.

So the square-free part is x divided by the product of all primes squared in their factorization. Wait, but exponents may be higher than 2. For example, if a prime p has exponent 5, then p^4 is part of the square divisor, and the remaining p^1 is in the square-free part.

So the square divisor is the product of p^(2k) where 2k is the largest even exponent ≤ the exponent of p in x's factorization. So for x's factorization as product p^e, the square divisor is product p^(e - (e mod 2)). The square-free part is product p^(e mod 2).

Thus, the square-free part is the product of primes p where the exponent is odd in x's factorization.

So, to compute the square-free part, we can factor x into primes, and for each prime, check if its exponent is odd. If so, multiply into the square-free part.

But factorizing each x up to 1e7 is O(1e7 * average number of primes per x), which for 1e7 might be feasible if optimized. But for 1e7 numbers, even O(1e7) is manageable as it's linear.

But factorization per number can be done via trial division, but that's going to be slow for 1e7 numbers.

Alternatively, we can precompute for each x its square-free part using a sieve-based approach.

Here's a possible method:

Initialize square_free array to 1 for all x ≥ 1.

For each prime p up to sqrt(1e7), we process all multiples of p. For each x divisible by p, we can keep track of how many times p divides x. For each x, we can count the exponent of p in x's factorization. If the exponent is odd, we multiply square_free[x] by p. If even, we don't.

But this approach would require for each x, and for each prime p dividing x, to determine the exponent of p in x. This seems tricky with sieve.

Alternatively, here's an efficient way inspired by the sieve of Eratosthenes:

Initialize square_free as 1 for all x.

Then, for each prime p (found via sieve), for all multiples x of p, do the following:

For each x in p, 2p, 3p, ... up to max_x:

- Divide x by p as many times as possible. Let count be the number of times p divides x. So, count is the exponent of p in x's factorization.

- If count is odd, multiply square_free[x] by p. If even, multiply by 1 (do nothing).

But how to do this efficiently for all x and p.

Wait, but even this approach would require for each x to process all primes p dividing x. For x up to 1e7, and primes up to 1e7, this could be O(1e7 log log 1e7), which is manageable.

Wait, but how to handle this. Let's think:

We can precompute the smallest prime factor (SPF) for each x. Then, for each x, we can factor it into primes by dividing by SPF[x], and so on.

Once we have the SPF array, for each x, we can factorize it into primes and their exponents. Then, for each prime in the factorization, if the exponent is odd, multiply into square_free[x].

But this requires factorizing each x, which for x up to 1e7 could take O(1e7 * average number of primes per x). Since the average number of primes per x is logarithmic, this is O(1e7 * log 1e7), which is about 1e7 * 16 ≈ 1.6e8 operations. That's manageable.

So the steps are:

1. Precompute the smallest prime factor (SPF) for each x up to 1e7.

2. For each x from 1 to max_x (1e7), compute its square-free part:

   a. Factorize x into primes using SPF.

   b. For each prime p in the factorization, compute the exponent e. If e is odd, multiply p into the square-free part.

   c. So square_free[x] is the product of all primes p where e is odd in x's factorization.

3. Then, for the input a and n, sum the square_free[x] for x in a to a +n -1.

So the key is to precompute the square_free array efficiently.

Now, the problem is how to factorize x efficiently using the SPF array.

Let's outline the steps in code:

First, compute the SPF array.

max_x = 1e7.

spf = array of size max_x+1.

Initialize spf[i] = 0.

Then, for i from 2 to max_x:

   if spf[i] is 0, then it's a prime. Set spf[i] = i.

   then, for all multiples j of i starting from i*i up to max_x, if spf[j] is 0, set spf[j] = i.

Wait, no. The standard sieve for SPF is:

Initialize spf as array where spf[i] is the smallest prime factor of i.

Initialize spf[i] = 0 for all i.

For i from 2 to max_x:

   if spf[i] is 0, then it's a prime. So set spf[i] = i.

   then, for j from i*i to max_x, step i:

       if spf[j] is 0, set spf[j] = i.

Wait, but that leaves some numbers (like multiples of primes larger than their square roots) with spf[j] not set. Hmm, perhaps a better approach is needed.

Alternative approach for SPF sieve:

Initialize spf as array of size max_x +1.

spf[1] = 1.

for i from 2 to max_x:

   if spf[i] is 0:

       spf[i] = i

       for j in range(i*i, max_x+1, i):

           if spf[j] is 0:

               spf[j] = i

   else:

       pass

Wait, no. That's not correct. Because for composite numbers, their spf is already set by their smallest prime factor.

Wait, perhaps the correct sieve for SPF is:

Initialize spf as array of size max_x+1.

for i from 2 to max_x:

    if spf[i] is 0:

        spf[i] = i

        for j in range(i*i, max_x+1, i):

            if spf[j] is 0:

                spf[j] = i

    else:

        # already has a smallest prime factor

        pass

But this leaves some composite numbers j that are multiples of primes larger than their current spf. For example, suppose j is 6. Its spf is 2. So when i=3, j=6 is already processed, spf[6] is 2. So when i=3, j=6 is not processed. So the code correctly sets spf[j] to the smallest prime factor.

So this approach correctly sets spf[j] to the smallest prime factor.

Once we have the SPF array, we can factorize any x by dividing by its SPF until x becomes 1.

So for each x, we can compute its square-free part as follows:

def compute_square_free(x, spf):

    res = 1

    while x != 1:

        p = spf[x]

        cnt = 0

        while x % p == 0:

            x = x // p

            cnt +=1

        if cnt %2 ==1:

            res *= p

    return res

So for x, this function factors x using the SPF array, tracks the exponents, and multiplies primes with odd exponents.

But for x up to 1e7, this would take O(number of primes in x's factorization) per x. Which for all x up to 1e7 is O(1e7 * average number of primes per x's factorization). The average is around log log x, which is acceptable.

So the plan is:

1. Precompute the SPF array for all x up to 1e7.

2. Precompute square_free[x] for each x in 1..1e7.

3. For the input a and n, compute the sum of square_free[x] for x from a to a+n-1.

Now, considering the constraints, the SPF sieve for x up to 1e7 is manageable.

But let's think about the time and memory.

The SPF array for 1e7 is manageable. Each entry is an integer (4 bytes), so 1e7 entries take about 40MB, which is under the memory constraints (256MB).

Then, the square_free array for 1e7 entries is also manageable, as each is an integer (probably 4 bytes). So 40MB again.

The sieve for SPF is O(n log log n), which for 1e7 is acceptable. The factorization for each x is O(number of primes in its factorization), which is O(1e7 * 10) (assuming each number has up to 10 primes on average), which is 1e8 operations, which is manageable within 4 seconds.

But wait, the maximum test case is when a=1 and n=1e7, so the code has to process 1e7 numbers, each requiring factorization. Let's see.

In Python, 1e8 operations may take about 10 seconds, but perhaps we can optimize.

Alternatively, we can precompute the square_free array during sieve processing.

Wait, here's an alternative approach for precomputing square_free. For each prime p, iterate through multiples of p and toggle the presence of p in the square_free product. For example, for each x divisible by p, we can track the exponent of p in x's factorization mod 2. If the exponent is odd, multiply p into square_free[x]. If even, divide by p (but since we can't track that, perhaps we need to think differently).

Alternatively, for each prime p, iterate over x in multiples of p. For each x, we can divide x by p as many times as possible, and if the exponent is odd, multiply p into the square_free. But how to track the exponents.

Alternatively, here's a sieve-based approach inspired by the inclusion-exclusion principle:

Initialize square_free as 1 for all x.

For each prime p:

   for x in multiples of p:

       current exponent of p in x's factorization is e.

       if e is odd after considering p, then multiply square_free[x] by p.

But how to track e. Because during sieve processing, for each x, when we process p, perhaps we can track how many times p divides x.

But this approach would need to process each prime p and for each multiple x of p, check how many times p divides x. But in practice, this would be O(p log p) per prime p, which might not be efficient for large primes.

Alternatively, for each x, when we process it in the sieve, we can track the square-free part as we find each prime factor. For example, during sieve processing, whenever a prime p is found as a factor of x, we can track the exponent mod 2 and update square_free[x] accordingly.

But I'm not sure how to integrate this into the sieve.

So perhaps the best approach is to precompute the SPF array first, then for each x from 2 to max_x, compute its square_free value by factorizing using SPF, as outlined earlier.

But in Python, factorizing 1e7 numbers using SPF may be too slow.

Wait, in Python, loops are slower than in C++ or other compiled languages. So for 1e7 numbers, each taking an average of say 5 steps in the factorization loop, that's 5e7 operations, which could take a while. Let's think: each loop iteration is checking the SPF, etc. For example, for x=2^e, the loop would take O(1) steps (since all factors are 2). For numbers with multiple primes, more steps.

But how much time would this take in Python? For example, a for loop in Python can handle about 1e6 iterations per second. So 1e7 iterations would take 10 seconds, which is over the time limit.

So this approach might be too slow for Python. Therefore, we need a more efficient way to compute the square-free part for all x in the range [1, 1e7].

Alternative idea: Precompute for each x the square-free part by using the sieve to track the presence of square factors.

Another approach: the square-free part is the product of the distinct primes in x's factorization. Wait, no. For example, x=72=2^3*3^2. The square-free part is 2. But the distinct primes are 2 and 3. So this approach is not correct.

So back to the original idea. How else can we compute the square-free part?

Another approach is to note that the square-free part can be computed as x divided by the largest square divisor. So for each x, we can compute the largest square divisor by finding all squares that divide x and selecting the maximum.

But finding the largest square divisor of x is equivalent to x divided by the square-free part.

Alternatively, the largest square divisor of x is x / square_free_part(x).

So the problem is to compute square_free_part(x) for each x.

An alternative way to compute square_free_part(x) is to iterate through all primes up to sqrt(x) and divide x by p^2 whenever possible, but this again might be slow.

Alternatively, for each x, if it's square-free, then its square-free part is x. Otherwise, divide out square factors.

Wait, but how to check for square factors.

But this approach would require for each x to check for squares that divide it, which is not efficient for large x.

Alternative idea inspired by Möbius function:

The square-free part is the product of primes dividing x an odd number of times. The Möbius function is zero if x has a squared prime factor; else, it's (-1)^k where k is the number of distinct prime factors. So the square-free part is the product of primes dividing x, but only those that have odd exponents.

Hmm.

Another approach: precompute for each x the square-free part by iterating through all primes up to x and handling their exponents.

But again, this isn't efficient.

Alternatively, here's a sieve-based approach for square-free numbers:

We can compute square_free_part[x] by initializing it to 1. Then, for each prime p, we iterate through all multiples of p and multiply square_free_part[x] by p. Then, for multiples of p², we divide square_free_part[x] by p² (but since this is multiplicative, perhaps there's a way to track it).

Wait, perhaps for each prime p, we can iterate through multiples of p and track how many times p divides each x. Then, for each x, if the count is odd, multiply by p.

But this seems similar to the earlier approach.

Alternatively, here's a different idea: For each x, the square-free part is the product of primes p where p divides x but p² does not divide x. But no, that's not correct. For example, x=18=2*3². The square-free part is 2. Here, 3² divides x, so we don't include 3. But 2 is included. But in this case, the square-free part is 2.

So the square-free part is the product of primes p that divide x, but the exponent of p in x is odd. So, even if p² divides x, but the exponent is 3, then p is included.

So the key is the exponent modulo 2.

Another approach inspired by the sieve of Eratosthenes:

Initialize square_free[x] = 1.

For each prime p:

   for x in multiples of p:

       current_count = 0

       temp = x

       while temp % p == 0:

           current_count +=1

           temp = temp // p

       if current_count %2 ==1:

           square_free[x] *= p

But this would require for each prime p, for each multiple x of p, to factor x's exponent of p. Which is O(p log x) for each prime p. For primes up to 1e7, this is not feasible.

So back to the original idea: precompute the SPF array, then for each x, compute the square-free part by factorizing x into primes and exponents, and multiply the primes with odd exponents.

In Python, even with 1e7 numbers, this could be manageable if the code is optimized. Let's think about possible optimizations.

First, the SPF sieve in Python can be implemented as follows:

max_x = 1e7.

But wait, the input says that a + n-1 can be up to 1e7. So the maximum x we need to process is up to 1e7. So we need to compute square_free[x] for x up to 1e7.

So the steps are:

1. Read a and n, compute the upper limit as upper = a +n -1.

2. Compute the maximum x needed as max_x = upper.

3. Precompute SPF for all x up to max_x.

4. Precompute square_free for all x up to max_x.

5. Sum square_free[x] for x from a to upper.

So the code can precompute up to max_x, which can be up to 1e7.

But implementing this in Python with speed is challenging.

Let's think about how to implement this efficiently.

First, the SPF sieve:

In Python, for sieve implementations, using lists and for loops can be slow. So perhaps using a sieve for SPF for 1e7 is possible.

Sample code for SPF sieve in Python:

def compute_spf(max_x):
    spf = list(range(max_x+1))  # Initialize to index
    for i in range(2, int(max_x**0.5) +1):
        if spf[i] == i:  # i is prime
            for j in range(i*i, max_x+1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

Wait, this code initializes spf as [0,1,2,3,...,max_x]. Then, for each i from 2 to sqrt(max_x), if i is prime (spf[i] ==i), then for multiples j of i starting from i*i, if spf[j] is still j (not yet marked), set spf[j] to i.

This correctly marks the smallest prime factor for each composite j. For primes, spf[j] remains j.

Once the spf array is computed, factorization of x can be done by repeatedly dividing by spf[x].

So for each x in 2 to max_x:

factors = []
while x != 1:
    p = spf[x]
    factors.append(p)
    x = x // p

But in this case, we need to track exponents, not just factors.

So for square_free, for each x, we need to track for each prime p in factors, whether the exponent is odd.

So the code for square_free is:

square_free = [1] * (max_x +1)

for x in range(2, max_x+1):
    current = x
    sf = 1
    while current != 1:
        p = spf[current]
        cnt =0
        while current % p ==0:
            current = current // p
            cnt +=1
        if cnt %2 ==1:
            sf *= p
    square_free[x] = sf

But in Python, looping from 2 to 1e7 and for each x, factorizing it, could be very slow.

For example, for 1e7 x's, each requiring on average say 3 divisions (since numbers get smaller when divided by their SPF), this is 3e7 operations. But Python is slow, so this might take a long time.

So for example, 1e7 iterations in Python can take about 1 second per million iterations, leading to 10 seconds for 1e7, which is over the time limit.

So we need to find a way to optimize this.

Alternative approach: Precompute the square_free array using a sieve-like method.

Here's an alternative idea inspired by the sieve:

For each prime p, for all multiples x of p, we can track the number of times p divides x. If the exponent is odd, multiply square_free[x] by p.

But how to do this efficiently.

We can precompute for each prime p, then for each x in multiples of p, determine the exponent of p in x's factorization.

But how to track this.

Another approach: For each prime p, iterate through all multiples of p, and for each x, divide x by p as many times as possible, and count the exponent. If the exponent is odd, multiply the square_free[x] by p.

But for x=1e7, the number of primes is up to 1e7. So this would be O(1e7 log 1e7) operations, which is not manageable.

So perhaps this is not feasible.

Alternative idea: note that the square-free part can be computed incrementally. For example, when x is a prime p, its square-free part is p. For x = k*p, where p is a prime not dividing k, the square-free part of x is square_free[k] * p. If p divides k, then the square-free part of x is square_free[k/p] * p^0 (if even exponent) or something else.

This seems difficult.

Alternative approach using multiplicative functions:

The square-free part is a multiplicative function. That is, if x and y are coprime, then square_free(x*y) = square_free(x) * square_free(y).

So we can compute the square_free array using this property.

We can initialize square_free as 1 for all x. Then, for each prime p, we process all multiples of p and update square_free.

For example:

for each prime p:

   for x in p, 2p, 3p, ... up to max_x:

       if x is divisible by p:

           if x/p is divisible by p:

               square_free[x] = square_free[x/p^2]

           else:

               square_free[x] = square_free[x/p] * p

But this is not correct. For example, take x = p^3. Then x/p = p^2. square_free[x/p] is square_free[p^2] = 1 (since p^2's exponents are even). Then square_free[x] = 1 * p, which is correct since p^3's exponent is 3 (odd).

But this requires checking if x is divisible by p^2. Alternatively, for x = p^k * m, where m is not divisible by p, then square_free[x] = square_free[m] * p^(k mod 2).

But how to compute this incrementally.

Another way: For each x, when we process its smallest prime factor p, and factor x into p and x/p. Then, if x/p has p as a factor, then the exponent of p in x is exponent in x/p plus 1. So:

square_free[x] = square_free[x/p] * p if exponent of p in x is odd.

But again, this requires tracking exponents.

Alternatively, we can compute square_free[x] by multiplying p for each p in the prime factors of x with odd exponents.

But this brings us back to the original approach of factorizing x.

So perhaps the only way is to proceed with the original approach, and try to optimize it as much as possible in Python.

Let's proceed with the code:

Implement the sieve for SPF, then for each x from 2 to max_x, compute the square_free[x] by factorizing using the SPF array.

But in Python, loops are slow, so we need to optimize the factorizations.

Alternative idea: precompute the square_free array in a way that uses the SPF array and memoizes the exponents.

Alternatively, note that when we factor x using the SPF array, we can track the primes and their exponents. For example:

def compute_square_free(x, spf):

    res = 1

    while x != 1:

        p = spf[x]

        count = 0

        while x % p == 0:

            x = x // p

            count +=1

        if count %2 ==1:

            res *= p

    return res

So for each x, this code loops until x is 1, gets the smallest prime factor, divides x by p until it can't, counts the exponent, and multiplies p into res if the exponent is odd.

But for x up to 1e7, this function would be called 1e7 times, which is computationally expensive in Python.

Alternative idea: precompute the square_free array during the sieve processing.

For example, during the sieve process, whenever we find a prime p, we can update all multiples of p by checking their exponents.

But I'm not sure how to implement this.

Alternatively, precompute the square_free array using a list and modifying it in place.

But it's not clear.

Another approach is to realize that for x, square_free[x] can be computed as square_free[x // p] * p if the exponent of p in x is odd, or square_free[x // p^2] if the exponent is even.

But this requires knowing how many times p divides x.

Alternatively, we can use dynamic programming:

For x in increasing order:

   if x is 1: square_free[x] =1.

   else:

       p = spf[x]

       divide x by p to get count.

       if count is even:

           square_free[x] = square_free[x // (p^count)]

       else:

           square_free[x] = square_free[x // (p^count)] * p

But how to compute this.

Alternatively, here's a way:

For each x from 2 to max_x:

   p = spf[x]

   if x % p ==0:

       remainder = x // p

       if remainder % p ==0:

           # x is divisible by p^2.

           # So square_free[x] is square_free[ x // (p*p) ] * (p if (exponent count is odd) else 1)

           # But how to track exponents.

           # We can compute the exponent of p in x.

           # Alternatively, since spf[x] is p, and remainder is x/p, if remainder's spf is also p, then x is divisible by p^2.

           # So x = p^k * m, where m is coprime with p.

           # The exponent of p in x is k.

           # So, if k is even:

               # square_free[x] = square_free[m]

           # else:

               # square_free[x] = square_free[m] * p

           # But how to compute m and k.

           # To find m and k:

           m = x

           k =0

           while m % p ==0:

               m = m // p

               k +=1

           if k %2 ==0:

               square_free[x] = square_free[m]

           else:

               square_free[x] = square_free[m] * p

       else:

           # x is divisible by p once.

           square_free[x] = square_free[remainder] * p

   else:

       # x is prime.

       square_free[x] = x

But this approach requires for each x to compute m and k, which again is O(k) steps. For x up to 1e7, this could be manageable.

But in Python, even this might be too slow.

Alternatively, we can compute this in a dynamic programming way, using the SPF array.

Here's how:

We can compute square_free[x] based on square_free[x/p], multiplied by p if the exponent of p in x is odd.

But how to track the exponents.

Alternatively, when x is divided by its smallest prime factor p, the exponent of p in x can be found by dividing x by p until it's no longer divisible by p. The count is the number of divisions.

Then, if the count is odd, square_free[x] = square_free[x // p^count] * p.

Else, square_free[x] = square_free[x // p^count].

But again, this requires factorizing each x.

But perhaps this is the way to proceed.

But in Python, even with this approach, the time may be too slow.

So perhaps the only way is to proceed and implement this as efficiently as possible.

So let's proceed to code.

First, read a and n.

Compute upper = a +n-1.

max_x = upper.

Compute spf for 2 to max_x.

Compute square_free array.

Sum square_free[x] for x in a to upper.

Now, let's implement this in Python.

But in Python, loops are slow. So, to compute the SPF array efficiently, use a sieve as follows:

def compute_spf(max_x):
    spf = list(range(max_x +1))  # Initialize to index
    for i in range(2, int(max_x**0.5) +1):
        if spf[i] == i:  # i is a prime
            for j in range(i*i, max_x+1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

Then, compute square_free.

But even this sieve may take a few seconds for max_x=1e7.

Then, for square_free:

square_free = [1]*(max_x+1)

for x in range(2, max_x+1):
    current = x
    res =1
    while current !=1:
        p = spf[current]
        cnt =0
        while current % p ==0:
            current = current //p
            cnt +=1
        if cnt %2 ==1:
            res *=p
    square_free[x] = res

This code is O(1e7 * average number of factors per x), which in the worst case is O(1e7 * log x).

But in Python, this may take a lot of time.

Alternative idea: use a helper function to compute square_free and memoize as we go.

But not sure.

Another optimization is to precompute the exponents in a list and reuse them.

But perhaps not.

Another idea is to note that when x is a prime, its square-free part is x.

So for x where spf[x] ==x (i.e., primes), square_free[x] =x.

So we can precompute square_free[x] =x for primes, then for composites, compute based on their factors.

But the code would still need to factorize the composites.

Alternatively, precompute square_free for all x during the sieve.

But this requires a clever sieve approach.

Alternatively, for each x, the square_free[x] can be computed as square_free[x/p] * p if the exponent of p in x is odd, or square_free[x/p] if even.

But how to track exponents.

Alternatively, here's a way:

For each x from 2 to max_x:

   p = spf[x]

   if x == p:

       # x is prime, so exponent is 1.

       square_free[x] = p

   else:

       # x is composite.

       # Let's find how many times p divides x.

       cnt =0

       temp = x

       while temp % p ==0:

           temp = temp // p

           cnt +=1

       if cnt %2 ==1:

           square_free[x] = square_free[temp] * p

       else:

           square_free[x] = square_free[temp]

This approach uses the SPF array to factor x into p and temp (x/p^cnt).

If cnt is odd, then multiply square_free[temp] by p.

This is because temp is x divided by p^cnt. So, in the square-free part, p's exponent is cnt mod 2. So if cnt is odd, p is included once.

This recursive approach can be implemented iteratively.

But for x=1e7, this would require for each x to compute temp and cnt.

But how to compute cnt and temp efficiently.

The code would be:

square_free = [0]*(max_x +1)

square_free[1] =1

for x in range(2, max_x+1):

    if square_free[x] !=0:

        continue

    p = spf[x]

    if x ==p:

        # x is prime.

        square_free[x] =p

    else:

        # compute cnt of p in x.

        temp =x

        cnt =0

        while temp %p ==0:

            temp = temp //p

            cnt +=1

        if cnt %2 ==1:

            square_free[x] = square_free[temp] *p

        else:

            square_free[x] = square_free[temp]

But this code isn't correct because for composite x, when we compute temp and cnt, the temp may have other factors, and square_free[temp] may not have been computed yet.

For example, x=4, spf[x]=2.

temp=4 /2^2=1.

cnt=2, even.

square_free[4] = square_free[1] =1.

Which is correct.

But for x=6:

spf[x]=2.

temp=6 divided by 2^1 (since 6/2=3, which is not divisible by 2). cnt=1, which is odd.

square_free[6] = square_free[3] *2.

But square_free[3] hasn't been computed yet.

So the code will fail.

So this approach won't work, as we need to compute x in order such that temp is processed before x.

But x can be up to 1e7, and processing in order from 2 to max_x may not ensure that temp is processed before x.

Thus, this approach isn't feasible.

So the only way is to precompute square_free for all x by factorizing each x using the SPF array.

But in Python, this is going to be too slow for max_x=1e7.

Alternative idea: Precompute square_free using numpy arrays for faster access. But this may not be feasible.

Another idea: note that square_free[x] can be computed as the product of the primes in the prime factorization of x with odd exponents. So, for x, if we can find all primes that divide x with an odd exponent, multiply them.

But again, factorizing x is needed.

Alternative approach for the problem:

The sum we need is the sum of the square-free parts of all numbers from a to a+n-1.

But the square-free part is multiplicative. So, the sum can be computed using inclusion-exclusion over square factors.

But I'm not sure.

Alternative idea: precompute the Möbius function, and use it to compute the square-free part.

But the Möbius function is zero if x has a square factor. Otherwise, it's (-1)^k where k is the number of distinct prime factors. But how does this relate to the square-free part.

Alternatively, the square-free part of x is the product of the primes dividing x. So, it's the radical of x divided by the radical of x's square-free part. Not sure.

Alternatively, the square-free part is equal to the radical of x divided by the square factors. But not sure.

Perhaps this is a dead end.

So, given the time constraints, perhaps the best way is to proceed with the original approach, and try to optimize the code as much as possible.

Now, let's test the code on the sample inputs.

Sample Input 1:

25 3

Sample Output: 30

The years are 25,26,27.

25's square-free part is 25 (since 25=5^2, but square-free part is 5^(2 mod 2) → 5^0 →1. Wait wait, no. Wait 25's square-free part is 1? Because 25's largest square divisor is 25, so 25 divided by 25 is 1. So the number of sheets is 1. But according to the sample explanation, 25 has 1 month of 25 days. So the sheets are 25 / 25 =1. So square_free_part(25) is 1.

But according to the code:

When x=25, factorized as 5^2. So exponents are even. So square_free_part is 1.

So the code would compute 25's square-free part as 1.

Similarly:

x=26: 2*13 → exponents are 1 for each, so square_free_part is 2*13=26. So sheets are 26/1=26.

x=27: 3^3 → exponent is 3. So square-free part is 3. So sheets are 27/9=3.

Sum is 1 +26 +3=30. Which matches the sample.

So the code should be correct.

But let's see the code.

The code would compute for x=25:

factors are 5,5 → exponents 2. So square_free is 1.

x=26: factors 2,13 → exponents 1 each → product 2*13=26.

x=27: factors 3^3 → exponent 3 mod 2 is 1 → square_free 3.

Sum is 1+26+3=30.

Sample Input 2:

50 5 → sum 125.

The years are 50,51,52,53,54.

50: 50=2*5^2. Square-free part is 2*1 =2. Sheets is 50/25=2.

Wait, but according to the sample's note, the sum is 125. Let's see:

Sample Input 2:

The output is 125. According to the sample explanation, the sum is 125.

Let's compute each year:

Year 50: square-free part is 2 (since 50=2 * 5² → square-free part is 2). So sheets is 50/25 = 2 → square_free_part is 2.

Year 51: 3*17 → square-free part 3*17=51 → sheets 51.

Year 52: 4*13 → square-free part is 13 → sheets 52/4=13.

Year 53: prime → square-free part is 53 → sheets 53.

Year 54: 54=2*3^3 → square-free part is 2*3=6 → sheets 54/(9) =6.

Sum: 2 +51 +13 +53 +6 = 125. Which matches the sample.

So the code is correct.

So the code is correct. Now, the challenge is to implement it efficiently in Python.

But in Python, the factorizing loop for 1e7 numbers may be too slow.

Possible optimizations:

1. Precompute the SPF array and compute square_free in a vectorized way.

But vectorization in Python is difficult.

Alternative idea: use a C-like approach with a precomputed list and a loop.

But in Python, loops are slow.

Alternative approach: use the math library's functions for factorization.

But not sure.

Another optimization: process the x's in a way that uses the smallest prime factor and cache the square_free.

But I think the code as outlined is the best possible, and the only way to proceed.

Another optimization: precompute the square_free array using a sieve-like approach, but I'm not sure.

But given the time constraints, perhaps the code will pass if the sieve and square_free array are computed efficiently.

Now, let's write the code.

The code will read a and n, compute upper =a +n-1. Then compute SPF up to upper. Then compute square_free for all x up to upper, then sum from a to upper.

In Python:

But for max_x up to 1e7, the lists may take a lot of memory, but 1e7 integers are manageable.

But in Python, lists are zero-based, so for max_x=1e7, we need a list of size 1e7+1.

Sample code:

def main():
    import sys
    a, n = map(int, sys.stdin.readline().split())
    upper = a +n -1
    max_x = upper

    # Compute SPF
    spf = list(range(max_x +1))
    for i in range(2, int(max_x**0.5)+1):
        if spf[i] ==i:  # i is prime
            for j in range(i*i, max_x+1, i):
                if spf[j] ==j:
                    spf[j] =i

    # Compute square_free
    square_free = [1]*(max_x+1)
    for x in range(2, max_x+1):
        current = x
        res =1
        while current !=1:
            p = spf[current]
            cnt=0
            while current %p ==0:
                current = current //p
                cnt +=1
            if cnt %2 ==1:
                res *=p
        square_free[x] = res

    # Sum from a to upper
    total =0
    for x in range(a, upper+1):
        total += square_free[x]

    print(total)

if __name__ == "__main__":
    main()

But this code may not be efficient enough for large inputs.

Testing this code with the sample inputs:

First sample input:

25 3 → output 30.

Second sample:

50 5 → output 125.

Now, what about the time?

For max_x=1e7, the SPF sieve would take O(n log log n) time. The square_free loop is O(n * average number of primes per x), which is O(1e7 * 3) → 3e7 steps.

In Python, this would take perhaps 10 seconds, which is over the 2-second time limit.

So this code will probably get a time limit exceeded error for large inputs.

Thus, we need a better approach.

Alternative idea: precompute square_free using a sieve that tracks the count of each prime.

Another approach inspired by the sieve:

For each x, the square-free part is the product of primes dividing x an odd number of times. So, for each prime p, every time it appears in the factorization of x, we can toggle the presence of p in square_free[x].

This is similar to the sieve of Eratosthenes, but we need to track the parity of the exponent.

But how?

Here's an approach:

Initialize square_free as 1 for all x.

For each prime p:

   for x in multiples of p:

       current_x = x

       count =0

       while current_x % p ==0:

           current_x = current_x // p

           count +=1

       if count %2 ==1:

           square_free[x] *=p

           square_free[x] //= p if previously multiplied.

But this is not efficient.

Alternative idea: For each x, the square-free part is the product of primes p for which the exponent in x is odd. So, for each x, the square-free part can be computed as the product of primes in the prime factorization of x, where each prime is included once if the exponent is odd, and not included if even.

So, the square-free part is the product of distinct primes in the prime factorization of x with odd exponents.

Thus, the square-free part can be computed as the product of the distinct primes in x's factorization, each multiplied once for every occurrence of odd exponents.

But again, this requires factorization.

Thus, the code may not be feasible in Python for large max_x.

Alternative approach: precompute the square-free part for all x using a sieve approach, where for each prime p, we iterate through multiples of p and multiply p to the square_free[x] for each x divisible by p an odd number of times.

But how to track the exponents.

An alternative approach is to realize that the square-free part can be computed by dividing x by the largest square divisor. To compute the largest square divisor, we can for each x, compute the product of primes to the highest even exponent.

But again, this brings us back to the original problem.

So, perhaps the only way to proceed is to optimize the code as much as possible in Python.

Possible optimizations:

1. Precompute the SPF array using a faster sieve method.

In Python, the current sieve for SPF is O(n log log n), but the inner loop is implemented in Python, which is slow.

Alternative idea: precompute the SPF array using a faster method, such as a bitwise sieve or using numpy. But this may not be feasible.

Another optimization: compute the square_free array in a way that avoids redundant operations.

For example, once x is processed, we can cache the square_free[x] value.

But in the current code, each x is processed once.

Another optimization is to replace the inner loops with more efficient code.

For example, in the square_free loop:

for x in range(2, max_x+1):

    current = x

    res =1

    while current !=1:

        p = spf[current]

        cnt =0

        while current % p ==0:

            current = current //p

            cnt +=1

        if cnt %2 ==1:

            res *=p

    square_free[x] = res

This can be optimized by precomputing the primes and their exponents for each x.

But how.

Alternatively, note that once we have the spf, we can factor x as follows:

def factor(x):

    factors = []

    while x !=1:

        p = spf[x]

        factors.append(p)

        x = x //p

    return factors

Then, group the factors into primes and their counts.

Then, for each prime in the factors, if count is odd, multiply.

But this is the same as the current code.

Another optimization: precompute the exponents during the SPF sieve.

But I'm not sure.

Alternatively, use a memoization approach for factorization.

But this won't help for x up to 1e7.

So, perhaps the code is as efficient as possible.

But in Python, this will be too slow for large inputs.

Alternative idea: use precomputed sieve of square-free parts.

But how.

Another approach: realize that the square-free part of x is the same as x divided by the largest square divisor.

The largest square divisor is the product of all primes^ even exponents in x's factorization.

So, the largest square divisor is the product of primes^ (exponent //2 *2).

Thus, the square-free part is x divided by this product.

So, to compute the square-free part, we can compute x divided by the largest square divisor.

The largest square divisor can be computed as the product of primes^ (exponent //2 *2).

But again, this requires factorization.

Thus, no gain.

Another idea: precompute all squares up to sqrt(1e7) and check for divisibility. But this is O(1e7) per x, which is not feasible.

Thus, the code is correct but may not be efficient enough for Python.

Possible last-resort optimization: precompute the square_free array using a sieve-based approach.

Here's an alternative approach:

Initialize square_free as 1 for all x.

For each prime p:

   for x in p, 2p, 3p, ... up to max_x:

       current = x

       exponent =0

       while current % p ==0:

           current = current //p

           exponent +=1

       if exponent %2 ==1:

           square_free[x] *= p

       else:

           square_free[x] *=1

But this requires for each prime p, iterating through all multiples of p and counting exponents. This is O(n log n) time, which is not feasible for n=1e7.

Thus, this approach is not feasible.

So, the code as written is the only way, but it may not pass the time constraints in Python.

Thus, perhaps the problem is intended to be solved with a sieve-based approach for square-free part computation.

Another idea: the square-free part of x is equal to the product of all primes dividing x.

Wait, no. For example, x=4, primes dividing x is 2. square-free part is 1.

No.

But the product of the distinct primes is the radical of x. But radical is different from square-free part.

Thus, no.

Thus, the code as written is correct but may be too slow in Python.

But given the problem statement, the correct code is as written, and the user is to provide it.

But given that, the code may not pass in Python for large inputs due to time constraints. However, according to the problem statement, the code should be in Python and optimized for speed and memory.

Perhaps there's a mathematical way to compute the sum of square-free parts for a range.

But I'm not aware of any such formula.

Thus, the code is as written.
</think>

```python
import sys

def main():
    a, n = map(int, sys.stdin.readline().split())
    upper = a + n - 1
    max_x = upper

    # Compute smallest prime factors (SPF)
    spf = list(range(max_x + 1))
    for i in range(2, int(max_x**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, max_x + 1, i):
                if spf[j] == j:
                    spf[j] = i

    # Precompute square-free parts
    square_free = [1] * (max_x + 1)
    for x in range(2, max_x + 1):
        current = x
        res = 1
        while current != 1:
            p = spf[current]
            cnt = 0
            while current % p == 0:
                current //= p
                cnt += 1
            if cnt % 2 == 1:
                res *= p
        square_free[x] = res

    # Calculate the total sum
    total = 0
    for x in range(a, upper + 1):
        total += square_free[x]

    print(total)

if __name__ == "__main__":
    main()
```