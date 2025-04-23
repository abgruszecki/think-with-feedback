<think>
Okay, let's see. The problem is to count the number of distinct sequences of positive integers where the gcd of all elements is exactly x and their sum is y. And we have to do this modulo 1e9+7. Hmm.

First, I need to understand the conditions. Let's think about the constraints. For the gcd to be x, all elements must be multiples of x. Because the gcd is the greatest common divisor, so if any element isn't a multiple of x, then the gcd can't be x. But even if all are multiples, the overall gcd could be a higher multiple. Wait, no. Wait, if all elements are multiples of x, then their gcd is at least x. But we need the gcd to be exactly x. So that means the gcd of all elements divided by x must be 1. Because if each a_i is x*b_i, then the gcd(a1,a2,...) is x * gcd(b1,b2,...). So for the original problem's gcd to be x, the gcd of the b_i's must be 1. And the sum of the a_i's is y, which translates to sum(x*b_i) = y → x * sum(b_i) = y. So y must be divisible by x, otherwise there are no possible sequences. That's the first thing to check.

So the first step is to check if y mod x is not zero. If not, output 0. Otherwise, let's let s = y/x. Then the problem reduces to finding the number of sequences of positive integers b1, b2, ..., bn (where n can be any positive integer) such that the sum of the b_i's is s, and the gcd of all the b_i's is 1. Then multiply each of those sequences by x to get the a_i's, and that's why the sum becomes y. So the problem is equivalent to counting the sequences for sum s and gcd 1, and then the answer is that count.

Now, the problem becomes: find the number of sequences (any length) of positive integers summing to s, with gcd 1. How to compute that?

Hmm. Let's think about inclusion-exclusion here. The total number of sequences that sum to s with all elements being positive integers is equal to 2^(s-1) choose (s-1). Wait, no. Wait, the number of sequences (ordered) of positive integers summing to s is equal to the number of compositions of s, which is 2^(s-1). Because each composition corresponds to placing a '+' between the s-1 possible gaps between 1s. For example, s=3 can be split as 1+1+1, 2+1, 1+2, 3. That's 4=2^2. So yes, the total is 2^{s-1}.

But we need the sequences where the gcd is exactly 1. So we can use inclusion-exclusion. Let's think of the Möbius function. Because the number of sequences where all elements are multiples of d is equal to the number of compositions of s/d into positive integers. But only if d divides s. Otherwise, zero.

Wait, but we need the sequences where the gcd of the elements is exactly 1. So we can subtract all sequences that have a gcd that's a multiple of some prime, etc. The standard approach here is to use Möbius inversion. Let me recall that the number of sequences with gcd exactly 1 is equal to the sum over d|s of μ(d) * C(s/d), where C(k) is the number of compositions of k where all elements are positive integers and their gcd is a multiple of d. Wait, maybe not. Let's think again.

Alternatively, for each d dividing s, the number of sequences with sum s and all elements divisible by d is equal to the number of compositions of s/d, since each element can be written as d*b_i, and the sum of d*b_i is s → sum b_i = s/d. The number of compositions of s/d into positive integers is 2^{(s/d) - 1} (if s/d >=1, else zero). So for each d, let f(d) be the number of sequences where all elements are divisible by d. Then f(d) is 2^{(s/d -1)} if d divides s and s/d >=1. Otherwise, zero.

But we want the number of sequences where the gcd is exactly 1. So that's equivalent to f(1) (sequences where all are divisible by 1) minus the sequences that have a gcd greater than 1. So using Möbius inversion, the number we want is sum_{d | s} μ(d) * f(d), where f(d) here is the number of sequences where all elements are divisible by d. Wait, but f(d) counts sequences where all elements are divisible by d, but their gcd could be a multiple of d. So to get the sequences where the gcd is exactly d, we can use Möbius function. The formula would be:

The number of sequences with gcd exactly 1 is equal to the sum over all d where d divides s, of μ(d) multiplied by the number of sequences where all elements are divisible by d (and their sum is s, so sum is s/d when divided by d). Because when all elements are divisible by d, the gcd must be a multiple of d. So summing μ(d) * f(d) over all d that divide s gives the inclusion-exclusion result.

So the formula is:

ans = sum_{d | s} μ(d) * 2^{(s/d -1) -1} + ...? Wait, no. Let's think again.

Wait, f(d) is the number of sequences where all elements are divisible by d, which is equivalent to the number of compositions of s/d into positive integers. Because each element is d*b_i, sum b_i = s/d. The number of compositions is 2^{(s/d -1)} if s/d >=1, else zero. So f(d) = 2^{ (s/d -1) } if d divides s and s/d >=1.

But for the Möbius inversion, the number of sequences with gcd exactly 1 is the sum_{d | s} μ(d) * f(1), where d is 1's divisors. Wait, maybe not. Let's clarify.

The Möbius inversion formula for multiplicative functions. Let me think of the standard approach. Let F(k) be the number of sequences where the gcd is a multiple of k. Then F(k) is equal to the sum_{d divisible by k} G(d), where G(d) is the number of sequences with gcd exactly d. So by Möbius inversion, G(k) = sum_{d divisible by k} μ(d/k) * F(d). So for our case, when k=1, G(1) = sum_{d divisible by 1} μ(d/1) * F(d) = sum_{d} μ(d) * F(d).

But F(d) is the number of sequences where the gcd is a multiple of d. But F(d) is equal to the number of sequences where all elements are divisible by d. Because if all elements are divisible by d, then their gcd is at least d, so the gcd is a multiple of d. Conversely, if the gcd is a multiple of d, then all elements are divisible by d. So F(d) is the same as the number of sequences where all elements are divisible by d. Which is 2^{(s/d -1)} if d divides s and s/d >=1. Otherwise zero.

So G(1) is the sum over all d dividing s of μ(d) * F(d), where F(d) is 2^{ (s/d -1) } if d divides s, else 0.

So the answer is sum_{d | s} μ(d) * 2^{ (s/d -1) }, but only if s/d >=1. Which requires that d <= s. But since d divides s, s/d is an integer. So if d divides s and s/d >=1, then s/d is a positive integer, so d is a divisor of s.

So first, check if x divides y. If not, output 0. Otherwise, compute s = y/x. If s is 0 (but x and y are positive, so this can't happen), but x and y are positive, so s is at least 1. Then compute all divisors d of s, compute μ(d) for each, multiply by 2^{ (s/d -1) }, sum over all d dividing s, and that's the answer.

So the steps are:

1. Check if y is not divisible by x: output 0.

2. Else compute s = y / x.

3. Find all divisors of s.

4. For each divisor d of s, compute μ(d).

5. For each such d, compute term = μ(d) * 2^{(s/d -1)}. Sum all terms.

6. The sum is the answer, modulo 1e9+7.

So the main steps are:

- Factorize s into primes.

- Generate all divisors of s.

- Compute the Möbius function for each divisor.

- Compute 2^k mod MOD for exponents up to s/d. Since s can be up to 1e9 / 1 → 1e9. So s/d can be up to 1e9. So 2^(1e9) mod MOD can be computed using fast exponentiation. But for each d, 2^{ (s/d -1) }, which could be up to 2^1e9. So for each d, compute the exponent e = (s/d -1), then compute pow(2, e, MOD).

So the steps in code:

First, check if x > y or y %x !=0 → output 0.

Else s = y//x.

If s ==0 → output 0. But since x and y are positive, s is at least 1.

Then compute all prime factors of s. Then generate all divisors of s. Then for each divisor d, compute μ(d). Then sum μ(d) * 2^{ (s/d -1) }, mod MOD.

So how to factorize s?

s can be up to 1e9. Factorizing s is manageable with trial division. But for 1e9, trial division up to sqrt(s) is acceptable. Because sqrt(1e9) is 3e4, which is manageable.

Once factors are found, generate all divisors. For example, if s has prime factors p1^e1, p2^e2, etc., then the divisors are the products of p_i^a_i where 0 <= a_i <= e_i.

Then for each divisor d, compute the Möbius function. The Möbius function μ(n) is 0 if n has a squared prime factor. Otherwise, μ(n) is (-1)^k where k is the number of distinct prime factors.

So for each divisor d, check if any prime factor in its factorization has exponent >=2. If so, μ(d) is 0. Otherwise, count the number of primes in the factorization and set μ to (-1)^k.

So the steps for generating the divisors and their Möbius function:

Once we have the prime factors of s (with exponents), we can generate all divisors by taking each combination of exponents (0 to e_i) for each prime.

For example, if s factors into p^a * q^b, then the divisors are p^i q^j for 0<=i <=a, 0<=j <=b.

For each such divisor, during generation, we can track how many primes are in its factorization (with exponent exactly 1), and whether any prime has exponent >=2 (which would make μ=0).

So when generating the divisors, for each prime factor, when building the divisor, if the exponent selected is >=2, then the μ function for that divisor is 0. Otherwise, the number of primes with exponent 1 is the count, and μ is (-1)^count.

So for example, if the divisor is p^2, then μ is 0. If it's p^1 * q^1, then μ is 1. If it's p^1, then μ is -1.

So, during the divisor generation, for each divisor d, we can compute μ(d) as follows:

- Initialize μ as 1.

- For each prime in the factorization of d:

   - If the exponent of the prime in d is 1 → multiply μ by -1.

   - If the exponent is >=2 → μ becomes 0, break.

So during the generation, when building each divisor, we can track whether any prime in its factorization has exponent >=2. If so, μ is zero. Otherwise, μ is (-1) to the number of primes in the factorization.

So, putting this all together:

Let's code this.

First, factorize s into its prime factors.

Then generate all divisors of s.

For each divisor d, compute μ(d).

Compute sum over all d of μ(d) * pow(2, (s/d -1), MOD).

But s can be up to 1e9, so s/d can be as small as 1 (if d = s). So s/d ranges from 1 to s.

But pow(2, e) can be computed efficiently with pow(2, e, MOD).

But for e up to 1e9, the pow function in Python can handle this quickly with the built-in pow function (which uses exponentiation by squaring).

So the key steps are:

Factorize s. Generate all divisors. For each divisor, compute μ. Multiply by 2^{(s/d-1)}, sum all terms modulo MOD.

Now, how to factorize s.

Implement trial division up to sqrt(s). Check all primes up to sqrt(s). For each i starting from 2 up to sqrt(s), check if i divides s. For each i, while divisible, count the exponent. Add to the factors. Then, after processing all i up to sqrt(s), if the remaining s is >1, add it as a prime factor.

So code for factorization:

def factorize(s):

    factors = {}

    i = 2

    while i*i <= s:

        while s % i ==0:

            factors[i] = factors.get(i,0) +1

            s = s//i

        i +=1

    if s>1:

        factors[s] =1

    return factors

Wait, but for example, if s is 12, factors would be {2:2, 3:1}.

Then generate all divisors from the factors.

Generating all divisors can be done via recursive backtracking. For each prime in the factors, and exponents up to the exponent in the factors.

But for speed, perhaps using iterative approach. For example, start with [1], then for each prime p and its exponents, multiply existing divisors by p^k for k from 1 to exponent.

For example:

factors = {p1:e1, p2:e2, ...}

divisors = [1]

for p in factors:

    exponents = factors[p]

    temp = []

    for d in divisors:

        for k in 0 to exponents:

            temp.append( d * (p^k) )

    divisors = temp

But that's not exactly correct. Wait, perhaps for each prime, generate all possible exponents and multiply to existing divisors.

So for each prime p in factors:

   current list of divisors is multiplied by p^k for k from 0 to e (since exponents can be 0 to e). Wait, but exponents are the maximum allowed. So for example, if current divisors are [d1, d2], and p has exponent 2, then for each d in current list, multiply by p^0, p^1, p^2.

But in code, for each prime in factors:

   new_divisors = []

   for d in divisors:

       for k in 0 to e:

           new_divisors.append( d * p^k )

   divisors = new_divisors

But this approach would generate all possible combinations.

But this would be O(number of divisors) * sum (exponents +1) over primes. For s up to 1e9, the maximum number of divisors is 1008 (for s=735134400, which has 1344 divisors). But for s up to 1e9, the maximum number of divisors is 1008 (but more likely, for the given s, the number is manageable). So generating all divisors is feasible.

But for each divisor, we also need to compute μ(d) on the fly. So perhaps during the divisor generation, track the current μ value.

Alternatively, during the generation of each divisor, track the prime exponents and compute μ.

So here's a plan:

Initialize the list of divisors as [ (1, 1) ], where the tuple is (d, μ(d)).

Then, for each prime p with exponent e in factors:

   For each existing divisor (d_val, mu_val) in the list:

       For k in 0 to e:

           if k ==0:

               new_d = d_val * p^0 = d_val

               new_mu = mu_val (no change)

               but since p^0 is 1, the exponents for p in the new_d is 0 → no effect.

           else:

               new_d = d_val * p^k

               if k >=2:

                   new_mu = 0 (since p^2 divides d)

               else:

                   new_mu = mu_val * (-1)

           So, for k in 0 to e:

               new_d = d * p^k

               new_mu:

                   if k ==0:

                       same as before.

                   elif k ==1:

                       multiply mu by -1. (since adding a new prime factor)

                   else:

                       new_mu is 0.

So during the iteration over the primes, we can build the list of (d, μ) pairs.

This way, when generating each possible divisor, we track its μ value.

Wait, but how does this work?

Let's see. For example, suppose the factors are {2:2, 3:1}.

Initial list: [(1, 1)].

Process p=2, e=2:

   For each (d, mu) in list:

       k=0: new_d = 1*2^0=1, new_mu=1*1=1.

       k=1: new_d=1*2^1=2. new_mu=1 * (-1) = -1.

       k=2: new_d=1*2^2=4. new_mu=0 (since k >=2).

   So after processing p=2, the list is:

       (1,1), (2,-1), (4,0).

   Then, process p=3, e=1.

   For each element in the list:

       (1,1):

           k=0: (1,1).

           k=1: (3, -1).

       (2,-1):

           k=0: (2, -1).

           k=1: (2*3=6, -1 * -1 =1).

       (4,0):

           k=0: (4, 0).

           k=1: (4*3=12, 0 * anything is 0 (since even if k=1, the mu is 0 *-1=0? Wait, no. The existing mu is 0, so even when adding a new prime, since the existing mu is 0, the new mu is 0 *-1 = 0.

   So after processing p=3, the list is:

       (1,1), (3,-1), (2,-1), (6,1), (4,0), (12,0).

So the divisors are 1, 3, 2, 6,4,12.

Each with their μ values. For example, divisor 6 is 2*3, each exponent 1. So μ is 1. Divisor 4 has exponent 2 in 2, so μ is 0. Divisor 12 has 2^2*3 → mu is 0.

So this approach correctly tracks the μ values.

Thus, the way to generate the divisors and their μ values is to process each prime and generate new divisors by multiplying by the prime's exponents, and track the mu value.

So the code steps:

- Initialize a list of (d, mu) tuples, starting with (1,1).

- For each prime p in the factors:

   For exponents from 1 to the max exponent of p (e):

       For each existing (d, mu) in the list:

           multiply by p^k and update mu.

   Wait, but the code needs to generate all possible exponents for p. Let me think again.

Wait, for a prime p with exponent e in s, when generating divisors, for each existing divisor d (from the previous primes), we can multiply it by p^0, p^1, ..., p^e. So for each existing (d, mu), we generate e+1 new divisors.

But to track μ correctly:

For each new exponent k (from 0 to e):

   if k ==0: the new divisor is d * p^0 = d. The mu remains the same.

   else:

       if k ==1:

           the new divisor is d * p.

           if the current mu is 0, then new mu is 0.

           else, new mu is mu * (-1) (since adding a new prime factor with exponent 1).

       else: (k >=2)

           the new divisor is d * p^k. Then, since the exponent of p is >=2, the μ becomes 0.

So in code, during the processing of each prime p and exponent e:

   temp = []

   for (d, mu) in current list:

       for k in 0 to e:

           if k ==0:

               new_d = d * (p^0) = d.

               new_mu = mu

               add (new_d, new_mu) to temp.

           else:

               new_d = d * (p^k)

               if mu ==0:

                   new_mu = 0

               else:

                   if k >=2:

                       new_mu =0

                   else:

                       new_mu = mu * (-1)

               add (new_d, new_mu) to temp.

   Wait, but this would generate duplicate divisors. For example, when processing p=2 with exponent 2, and existing divisor is (2, -1). For k=0, the new_d is 2, mu -1. But when k=0, we're just adding the same divisor again. So this approach would create duplicates. So perhaps the code needs to avoid that by generating all possible exponents for the current prime and combining with existing divisors.

Alternatively, perhaps during the processing of each prime, we need to generate all possible exponents for that prime and multiply with existing divisors. So the code should generate all possible exponents for the current prime and multiply each existing divisor by p^k for k from 0 to e. But for each existing (d, mu), we generate new entries for each k, which may include the existing d (k=0). Wait, no. Because when processing a new prime, the existing divisors have not yet considered this prime, so for k=0, we can keep the existing d, and for k>0, multiply by p^k.

But the way to generate all divisors is to, for each prime, generate all possible exponents and combine them with existing divisors. So the code for generating divisors with μ would be:

current_divisors = [(1, 1)]

for (p, e) in factors.items():

    new_divisors = []

    for (d, mu) in current_divisors:

        for k in range(e + 1):

            if k == 0:

                new_d = d * (p**0)

                new_mu = mu

                new_divisors.append( (new_d, new_mu) )

            else:

                if mu == 0:

                    # any exponent here, the mu remains 0.

                    new_mu = 0

                else:

                    if k ==1:

                        new_mu = mu * (-1)

                    else:

                        # k >=2 → new_mu is 0.

                        new_mu = 0

                new_d = d * (p**k)

                new_divisors.append( (new_d, new_mu) )

    current_divisors = new_divisors

But wait, this approach will generate multiple entries for the same d. For example, when processing p=2, e=2:

current_divisors starts as [(1,1)].

Processing p=2, e=2:

for each (d=1, mu=1):

   k=0 → (1,1)

   k=1 → (2, -1)

   k=2 → (4, 0)

so new_divisors is [ (1,1), (2,-1), (4,0) ]

Then processing next prime, say p=3, e=1:

For each (d, mu) in new_divisors:

   for k in 0,1:

       if k=0:

           new_d remains same, mu same.

       else:

           if mu is not zero:

               if k=1: new_mu = mu * (-1)

           else: new_mu =0.

So for (1,1):

   k=0 → (1,1)

   k=1 → (3, -1)

for (2,-1):

   k=0 → (2,-1)

   k=1 → 2*3=6, mu= (-1)*-1=1.

for (4,0):

   k=0 → (4,0)

   k=1 → (12,0)

So new_divisors becomes [ (1,1), (3,-1), (2,-1), (6,1), (4,0), (12,0) ]

So each of these are unique divisors. So the code will generate all possible divisors, each once.

But this approach may generate duplicates when a prime is processed again. But since factors are processed in order, and each prime is processed once, the code will generate each divisor exactly once.

Thus, this approach is correct.

Once all primes are processed, current_divisors is the list of all divisors of s, each with their μ values.

Then, for each (d, mu) in current_divisors, we compute the term mu * 2^{(s/d -1)}, and sum all such terms.

But s is fixed (y/x). So for each divisor d, compute s/d, subtract 1, compute 2^ that exponent, multiply by mu, sum all.

But since s is divisible by x, and s = y/x. So when x divides y, s is integer. So for d to be a divisor of s, s/d is integer.

So in code:

sum_ans = 0

for (d, mu) in current_divisors:

    if mu ==0:

        continue  # term is zero, skip

    t = s // d  # since d divides s

    exponent = t -1

    if exponent <0:

        # but since d divides s, s/d is at least 1. So exponent is 0 when t=1.

        # s/d >=1 → exponent >=0

    term = mu * pow(2, exponent, MOD)

    sum_ans = (sum_ans + term) % MOD

sum_ans is the answer.

So putting this all together.

Now, let's test the sample input.

Sample 1:

Input 3 9 → x=3, y=9.

Check 9 mod 3 is 0 → s=3.

So s=3.

Factorize 3 → {3:1}.

Generate divisors:

current_divisors = [(1,1)]

processing p=3, e=1:

new_divisors is [ (1,1) (k=0), (3, -1) (k=1) ]

So divisors are 1 and 3.

For each:

d=1, mu=1:

t=3/1=3 → exponent 2. pow(2,2) is 4. term is 1*4=4.

d=3, mu=-1:

t=3/3=1 → exponent 0. pow(2,0)=1. term is (-1)*1 =-1.

Sum is 4-1=3 → which matches the sample output.

Sample 2:

x=5, y=8 → 8 mod5=3≠0 → output 0.

Another test case: x=1, y=3 → s=3. Same as sample 1, answer is 3.

Another case: x=1, y=2 → s=2. Factors are {2:1}. Divisors 1 and 2.

For d=1, mu=1: exponent 2-1=1 → 2^1=2. term 2.

d=2, mu=-1: exponent 1-1=0 → 1. term -1.

Sum 2-1=1. So answer is 1. What's the sequences? The sequences are [2], [1,1], but wait no. Wait, the sum is 2. So sequences of positive integers sum 2, with gcd 1.

Possible sequences: [1,1], [2]. The gcd of [1,1] is 1. The gcd of [2] is 2. So the answer is 1. Which matches the sum.

So the code works for this case.

Now, code steps:

Implement factorization.

But in Python, for factors up to sqrt(s), which for s up to 1e9 is manageable.

Then generate divisors and their μ values as described.

Then compute the sum.

Edge cases:

- s=1: divisors are 1. μ(1) is 1. exponent 0 → 1. So term is 1*1=1. So answer is 1. Which represents the sequence [1], but multiplied by x. So yes.

Another case: x=2, y=2. s=1. The answer is 1. The sequence is [2], which gcd is 2. So no. Wait, no. Wait x=2, y=2. y/x=1. So sum of the b_i's is 1. So the sequences of b_i's must sum to 1. The only possible sequence is [1]. The gcd is 1. So the answer is 1. Then, the a_i's are [2*1] → [2]. The gcd is 2, but the problem requires the gcd to be exactly x. So the code works here.

So the code works.

Now, code.

Now, let's code the steps.

First, read x and y. Check if y %x !=0 → print 0.

Else, compute s = y//x.

Factorize s.

Generate all divisors and their μ values.

Compute the sum.

Now, code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    MOD = 10**9 +7

    x, y = map(int, input_stream.readline().rstrip("\n").split())

    if y %x !=0:

        print(0, file=output_stream)

    else:

        s = y//x

        if s ==0:

            print(0, file=output_stream)

        else:

            # factorize s

            factors = {}

            temp = s

            i=2

            while i*i <= temp:

                if temp%i ==0:

                    cnt =0

                    while temp%i ==0:

                        cnt +=1

                        temp = temp//i

                    factors[i] = cnt

                i +=1

            if temp>1:

                factors[temp] =1

            # Generate divisors and their mu values

            divisors = [ (1, 1) ]

            for p, e in factors.items():

                new_divisors = []

                for (d, mu) in divisors:

                    for k in range(e +1):

                        if k ==0:

                            new_d = d * (p**k)

                            new_mu = mu

                            new_divisors.append( (new_d, new_mu) )

                        else:

                            if mu ==0:

                                current_mu =0

                            else:

                                if k >=2:

                                    current_mu =0

                                else:

                                    current_mu = mu * (-1)

                            new_d = d * (p**k)

                            new_divisors.append( (new_d, current_mu) )

                divisors = new_divisors

            # Compute the sum

            ans =0

            for (d, mu) in divisors:

                if mu ==0:

                    continue

                t = s //d

                exponent = t-1

                ans = (ans + mu * pow(2, exponent, MOD)) % MOD

            print( ans % MOD , file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 8
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

So code should work.

Another test case: s=4.

Factors are {2:2}

Processing p=2, e=2:

Initial divisors [(1,1)]

For each (d, mu) in divisors:

   k=0: (1,1)

   k=1: new_d=2, mu= -1.

   k=2: new_d=4, mu=0.

new_divisors = [ (1,1), (2,-1), (4,0) ]

Then for each:

d=1, mu=1 → t=4, exponent 3 → 8 → term 8.

d=2, mu=-1 → t=2, exponent 1 → 2 → term -2.

d=4, mu=0 → skipped.

sum is 8-2=6.

What's the actual count?

The sequences of positive integers summing to 4 with gcd 1.

Possible sequences:

[1,1,1,1] → gcd 1.

[1,1,2], permutations → gcd 1.

[1,3], permutations → gcd 1.

[2,2] → gcd 2 → not counted.

[4] → gcd4 → not counted.

So the valid sequences are:

All compositions of 4 except those where all elements are even.

The number of compositions of 4 is 2^3=8. Subtract the compositions where all elements are even (sum 4, each even → elements are 2's. So the sum is 4 → elements can be 2+2, 4, 2+1+1 (but wait, no. Wait, the sum is 4, but elements are even. So possible sequences are 2+2, 4, 2+1+1 is not allowed since 1 is odd. So the sequences are those where all elements are even. So sum must be 4, and each element is even → elements are 2 and 2, or 4.

The number of such sequences is the number of compositions of 4/2=2. So 2^1=2. So the answer should be 8 - 2*1 (using inclusion-exclusion). But according to the code's approach:

sum over d|4 of μ(d)*2^(4/d -1).

The divisors of 4 are 1,2,4.

μ(1)=1, μ(2)=-1, μ(4)=0.

So sum is 1*2^(4/1 -1) + (-1)*2^(4/2 -1) + 0 → 2^3=8 → 8 + (-1)*2^(1) =8-2=6. Which matches the code's calculation. So the code works.

Thus, the code should handle all cases.
</think>

```python
MOD = 10**9 + 7

x, y = map(int, input().split())

if y % x != 0:
    print(0)
else:
    s = y // x
    if s == 0:
        print(0)
    else:
        factors = {}
        temp = s
        i = 2
        while i * i <= temp:
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                factors[i] = cnt
            i += 1
        if temp > 1:
            factors[temp] = 1
        
        divisors = [(1, 1)]
        for p, e in factors.items():
            new_divisors = []
            for (d, mu) in divisors:
                for k in range(e + 1):
                    if k == 0:
                        new_d = d
                        new_mu = mu
                    else:
                        new_d = d * (p ** k)
                        if mu == 0:
                            new_mu = 0
                        else:
                            new_mu = -mu if k == 1 else 0
                    new_divisors.append((new_d, new_mu))
            divisors = new_divisors
        
        ans = 0
        for (d, mu) in divisors:
            if mu == 0:
                continue
            t = s // d
            exponent = t - 1
            ans = (ans + mu * pow(2, exponent, MOD)) % MOD
        
        print(ans % MOD)
```
