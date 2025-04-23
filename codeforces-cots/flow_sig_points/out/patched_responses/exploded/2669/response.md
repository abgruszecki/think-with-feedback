<think>
Okay, let's try to figure out this problem. So, the task is to find the smallest n such that n! divided by the product of a_i! is a positive integer. That means that the prime factors in n! must cover all the prime factors in the product of a_i!s. Right. So we need to compute the exponents of each prime in the product of a_i!s and then find the minimal n where for every prime, the exponent in n! is at least that value.

First, let's think about how to compute the exponents of primes in the product of a_i!s. For each prime p, the total exponent in q (which is product a_i!) is the sum of exponents of p in each a_i!.

Then, for each prime p, the exponent in n! must be >= the total exponent in q. So we need to find the minimal n such that for all primes p, the sum of exponents in each a_i! for p is <= the exponent of p in n!.

The challenge is to compute this efficiently given that the a_i can be up to 1e7 and there can be up to 1e6 of them.

So the steps are:

1. Compute the required exponents for each prime p in q. This is done by summing, for each a_i, the exponents of p in a_i! (which is floor(a_i/p) + floor(a_i/p^2) + ... until p^k > a_i).

But how do we compute this for all primes up to the maximum a_i efficiently?

Wait, the maximum a_i is 1e7. So primes up to 1e7 are possible. But iterating over each a_i and for each prime p up to a_i, compute exponents is going to be O(k * max_a_i / log max_a_i), which might be too slow if k is 1e6 and max_a is 1e7. That would be around 1e6 * 1e7 / log(1e7) ≈ 1e13 operations, which is way too much.

So we need a smarter approach.

Alternative approach: For each a_i, factorize a_i! into primes and accumulate the counts. But again, factorizing each a_i! directly is not feasible.

Wait, but the exponents of primes in a_i! can be calculated for each prime p as sum_{k=1}^∞ floor(a_i / p^k). So, for all primes p, the exponents contributed by a_i! is the sum of a_i divided by p, p squared, etc., until p^k > a_i.

So, for all a_i's, we need to compute for each prime p, the sum of floor(a_i / p) + floor(a_i / p^2) + ... and add all these sums across all a_i's.

The problem is to compute this total for each prime p, then find the minimal n such that for each p, the sum in n! is >= the total.

Now, the question is how to compute the sum of exponents for each prime p efficiently.

Let's think: For each a_i, the sum floor(a_i/p) + floor(a_i/p²) + ... is the exponent of p in a_i!. So the total exponents for p is the sum over all a_i of this sum.

But instead of processing each a_i and each prime p, which is O(k * average number of primes per a_i), which is too slow, perhaps we can precompute for each prime p, the sum over a_i of the exponents contributed by each a_i to p.

How can we compute that efficiently?

Let's think for a prime p. The exponent in q (product a_i!) is sum_{i=1 to k} (sum_{m=1 to ∞} floor(a_i / p^m)).

So for each prime p, we need to compute the total sum of floor(a_i / p) + floor(a_i / p²) + ... across all a_i.

So, perhaps for each prime p up to the maximum a_i, we can compute this sum.

But how to find all primes up to 1e7? Sieve of Eratosthenes would take O(n) time, which is manageable. But generating primes up to 1e7 is possible. For 1e7, sieve would take about O(1e7) time, which is acceptable in Python if optimized.

Once we have all primes, for each prime p, we compute the total exponent required for p.

Once we have all primes and their required exponents, then we can find the minimal n such that for each p, the sum in n! is >= the required exponent.

So the steps are:

1. Find all primes up to the maximum a_i.

2. For each prime p, compute the total required exponent (sum over all a_i of sum_{m=1} floor(a_i / p^m)).

3. Then, for each prime p, compute the minimal n_p such that the sum_{m=1} floor(n_p / p^m) >= required exponent. Then, the answer is the maximum of all such n_p.

So the minimal n is the maximum n_p across all primes p.

So how do we compute step 2 efficiently?

For each prime p, the total exponent required is sum_{a in a_list} (sum_{m=1} floor(a / p^m)).

This can be rewritten as sum_{m=1} sum_{a in a_list} floor(a / p^m).

But the sum over a in a_list of floor(a/p^m) is the same as the count of how many a's are >= p^m, multiplied by 1, plus how many are >= 2*p^m multiplied by 1, etc. Wait, not sure.

Alternatively, for a given p and m, each a_i contributes floor(a_i/p^m) to the total. So for all a_i, sum over a_i of floor(a_i/p^m) can be computed as follows: for each a_i, add floor(a_i/p^m), and sum all these.

But if the a_i's are up to 1e7 and m can be up to log_p(max_a), for each prime p, this could be expensive.

Wait, but the number of primes up to 1e7 is about 664,579. For each prime p, and for each m where p^m <= max_a, we need to compute the sum of floor(a_i / p^m) across all a_i. So for each p and each m, this is O(1) if we can count how many a_i are >= x for various x.

Wait, if we can precompute a frequency array for the a_i's, then for any x, the number of a_i >= x is the sum of frequencies from x to max_a. Then, the sum of floor(a_i / x) for all a_i is equal to sum_{q >= 1} count of a_i >= q*x.

Wait, because for each a_i, floor(a_i/x) is the number of multiples of x that are <= a_i. So, the sum over all a_i of floor(a_i/x) is equal to the sum_{q=1 to max_q} (number of a_i >= q*x).

So for a given x, sum_{a} floor(a/x) is sum_{q=1}^∞ cnt[q*x], where cnt is the count of a_i >= q*x.

But how to compute this efficiently?

If we have a frequency array freq, where freq[v] is the number of a_i equal to v. Then, a prefix sum from max_a down to 1 would give us the count of a_i >= v for each v.

So, first, we can create a frequency array for all a_i's. Let's say max_a is the maximum a_i. We create a list cnt_ge where cnt_ge[v] is the number of a_i >= v. Then, for any x, sum_{a} floor(a/x) = sum_{q=1}^floor(max_a/x) cnt_ge[q*x].

So, precomputing cnt_ge allows us to compute sum_{a} floor(a/x) efficiently.

So here's the plan:

1. Read all a_i's, compute the frequency array. Then compute cnt_ge[v] for all v from 1 to max_a. cnt_ge[v] = sum_{i >= v} freq[i]. This can be done by initializing an array of size max_a + 1, then iterating from max_a down to 1, accumulating the sum.

For example, cnt_ge[v] = cnt_ge[v+1] + freq[v]. But wait, wait. Let's think. For each v, cnt_ge[v] is the number of a_i >= v. So:

cnt_ge[v] = cnt_ge[v+1] + freq[v] ?

No, that's not right. Wait, if v is 5, then a_i >=5 includes a_i=5, 6, 7, etc. So for v=5, cnt_ge[5] = freq[5] + cnt_ge[6]. So yes, starting from the max_a down, we can compute cnt_ge as cnt_ge[v] = cnt_ge[v+1] + freq[v], with cnt_ge[max_a + 1] = 0.

Once we have cnt_ge, then for any x, the sum of floor(a_i/x) over all a_i is the sum of cnt_ge[x], cnt_ge[2x], cnt_ge[3x], etc., until kx exceeds max_a.

So for each prime p, and for each m (p^m), the sum of floor(a_i/(p^m)) across all a_i is sum_{q=1 to ...} cnt_ge[q * (p^m)].

But how do we compute this sum efficiently for each (p^m)?

Let's break it down:

For a given x = p^m, sum_{a} floor(a/x) = sum_{q=1}^∞ cnt_ge[q*x]. So the sum is for q=1 to q_max where q*x <= max_a.

So for x = p^m, q_max = floor(max_a / x). For each q from 1 to q_max, add cnt_ge[q*x].

So for each x, we can compute this sum by iterating q from 1 to q_max and summing cnt_ge[q*x].

But for large x, like x = 1e7, q_max is 1, so it's just cnt_ge[1e7] if x=1e7. But for x=1, q_max could be 1e7, which would require 1e7 iterations, which is not feasible.

Wait, but x is p^m. For primes p, and m starts from 1. For each prime p, m increases until p^m exceeds max_a.

For example, for p=2 and max_a=1e7, m can go up to 23 (since 2^23 is ~8e6, but 2^24 is 16e6 which is over 1e7). So for each p, the maximum m is log_p (max_a), which is small.

But the problem is, for each p and m, x = p^m. So for x being p, p^2, p^3, etc. For each x, the sum is sum_{q=1} cnt_ge[q*x]. But for x=p, and when m=1, then x=p. So for each prime p, in the first step (m=1), x=p. Then the sum is sum_{q=1} cnt_ge[q*p].

But if p is 2 and max_a is 1e7, then q can be up to 5e6 (since 2*5e6 = 1e7). So for p=2, m=1, x=2, we need to iterate q from 1 to 5e6, adding cnt_ge[2q] each time. That's 5e6 operations for this p and m. But if there are 1e6 primes, this is impossible.

So this approach would be O(total number of primes * average number of q's per p and m), which could be way too slow.

Therefore, we need a better way to compute the sum of floor(a_i / x) over all a_i.

Alternative approach: Precompute a frequency array, then for each x, the sum is sum_{v >= x} (floor(v/x) * freq[v]). But how?

Alternatively, the sum of floor(v/x) for all v in a_i is equal to sum_{v in a_i} floor(v/x).

But how can we compute this for all a_i and x efficiently?

But x can be up to 1e7, and for each x (like for all primes p and their exponents), so this is not feasible.

Wait, but the primes are up to max_a, and their exponents. So the x's are p^m where p is a prime and m >=1, p^m <= max_a.

The number of such x's is O(max_a log max_a) which is not manageable for 1e7.

Wait, perhaps the maximum number of x's is manageable. For example, primes up to 1e7, each with exponents up to log2(1e7) (~23). So for 6e5 primes, each with 23 exponents, that's 1.38e7 x's. For each x, we need to compute the sum of floor(v/x) for all a_i. If for each x, this can be computed in O(1) time using some precomputed structure, then this would be feasible.

So the key is to find a way to compute for any x, the sum of floor(v/x) over all a_i, quickly.

Hmm. Let's think of the sum as sum_{q=1}^max_q (number of a_i >= q*x) * 1. Because for each q, the count of a_i >= q*x gives the number of a_i that contribute at least q to the sum. But floor(v/x) for a v >= q*x but < (q+1)*x is q. So for each q, the total contribution to the sum is the number of a_i >= q*x.

So sum_{v} floor(v/x) = sum_{q=1}^{max_q} (count of a_i >= q*x).

Which is exactly the same as the sum of cnt_ge[q*x] for q starting from 1 until q*x > max_a.

So, if we have the cnt_ge array precomputed, then for any x, this sum can be computed by iterating q from 1 to q_max, where q_max is floor(max_a /x).

But as discussed earlier, for x=1, this would take up to 1e7 iterations, which is O(1e7) per x, which is way too slow.

So we need a smarter way to compute this sum.

Wait, but for x=1, the sum is the sum of cnt_ge[1], cnt_ge[2], cnt_ge[3], ..., cnt_ge[max_a]. Which is the same as the sum of (cnt_ge[v] for v >=1). But cnt_ge[v] is the number of a_i >=v. So the sum for x=1 is the sum_{v=1}^max_a cnt_ge[v]. But this is equivalent to the sum of all a_i, because each a_i contributes to cnt_ge[1], cnt_ge[2], ..., cnt_ge[a_i]. So the sum is sum_{a_i} a_i.

Wait, that's a crucial insight. Because sum_{v=1}^max_a cnt_ge[v] = sum_{a in a_list} a. Because for each a, the sum of cnt_ge[v] for v from 1 to a is a. So sum_{v=1}^max_a cnt_ge[v] is the sum of a_i's.

So, for x=1, the sum is sum_{a_i} a_i. Similarly, for x=2, the sum is sum_{q=1} cnt_ge[2q] = sum_{v even} cnt_ge[v]. But how to compute that efficiently?

Alternative idea: Precompute for each x, the sum of cnt_ge[x], cnt_ge[2x], cnt_ge[3x], ... until x*q > max_a.

But precomputing this for all possible x is impossible, as x can be up to 1e7.

So, perhaps the problem is manageable only if the primes are processed in a way that allows us to compute their required exponents efficiently.

Let's think again. For each prime p, the exponents required are sum_{m=1}^∞ (sum_{q=1}^∞ cnt_ge[p^m * q}).

Wait, but the exponents required for p is the sum over all m (sum_{q=1} cnt_ge[p^m * q}).

Alternatively, exponents_required(p) = sum_{m=1}^∞ sum_{q=1}^∞ cnt_ge[p^m * q} ?

No, wait. For each a_i, the exponent of p in a_i! is the sum_{m=1}^∞ floor(a_i / p^m). So the total exponents required for p is the sum over all a_i of this sum. Which can be rewritten as sum_{m=1}^∞ sum_{a_i} floor(a_i / p^m).

Each of these terms sum_{a_i} floor(a_i / p^m) can be computed as sum_{q=1}^floor(max_a / p^m) cnt_ge[p^m * q}.

So, for a given prime p, the exponents_required(p) is the sum over m (sum_{q} cnt_ge[p^m * q}).

But how to compute this efficiently.

Let's consider that for each prime p, we can compute exponents_required(p) as:

sum_{m=1}^\infty (sum_{q=1}^\infty cnt_ge[p^m * q} )

Which can be rewritten as sum_{k=1}^\infty cnt_ge[k} * (number of times p^m divides k, for all m >=1).

Wait, because each k can be written as k = p^m * q, where m >=1 and q is a positive integer. For each k, the number of (m, q) pairs that satisfy this is equal to the number of exponents m where p^m divides k. But since m is at least 1, this is the number of times p divides k (the exponent of p in the prime factorization of k) divided by 1. Because each m can be from 1 up to the exponent of p in k.

For example, if k is p^e, then the number of (m, q) pairs is e, since m can be 1, 2, ..., e, and q is p^{e-m}.

Wait, perhaps not. Let's see: For k = p^e * t where t is not divisible by p.

Then, k can be expressed as p^m * q, where m ranges from 1 to e, and q = p^{e - m} * t. For each such m, q is an integer not divisible by p. So the number of (m, q) pairs is e.

So, for each k, the number of times it is counted in exponents_required(p) is equal to the exponent of p in k.

Therefore, exponents_required(p) is equal to the sum over all k of cnt_ge[k] * (exponent of p in k).

But that's a key insight! Because then, for each prime p, exponents_required(p) is the sum over all multiples of p in the cnt_ge array, multiplied by their exponents.

But wait, no. Wait, exponents_required(p) is the sum over all k of cnt_ge[k] multiplied by the number of times p^m divides k for m >=1. Which is exactly the sum over all k of cnt_ge[k] multiplied by the exponent of p in k.

So for each prime p, exponents_required(p) = sum_{k=1 to max_a} cnt_ge[k] * (exponent of p in k).

But how can we compute this sum efficiently?

The problem is that for each prime p, we need to compute the sum of cnt_ge[k] multiplied by the exponent of p in k, for all k from 1 to max_a.

But this seems like a challenging task, given that the max_a can be up to 1e7 and there are up to 1e6 primes.

But let's think again. For each prime p, the exponent in k is the number of times p divides k. So, for each k, this is the sum of exponents of p in k's prime factors.

So, exponents_required(p) is sum_{k=1 to max_a} cnt_ge[k] * e_p(k), where e_p(k) is the exponent of p in k.

Hmm, but how to compute this sum efficiently.

Alternative approach: For each prime p, iterate through all multiples of p and accumulate the exponents.

For example, for p=2, all multiples of 2 contribute e_p(k) * cnt_ge[k]. So for each multiple k of p (i.e., 2,4,6,8...), we compute how many times p divides k and multiply by cnt_ge[k], then sum all these.

The key is that for each multiple of p, we can compute e_p(k) as the number of times p divides k.

But how to compute this for all primes p efficiently.

Wait, here's an idea:

For each prime p, we can generate all multiples of p and compute e_p(k) for each multiple k. Then sum cnt_ge[k] * e_p(k) over all k.

But for p up to 1e7, this would take O(max_a/p) operations for each p. Summing over all primes p, the total operations would be O(max_a * log log max_a), which is manageable.

Because the sum of 1/p for primes p <= N is approximately log log N, which for N=1e7 is about 3. So for max_a=1e7, the total operations would be O(1e7 * 3) = 3e7, which is acceptable in Python.

So here's the plan:

1. Precompute cnt_ge array.

2. For each prime p (from sieve), compute exponents_required(p) as follows:

   a. Initialize sum_p = 0.

   b. Iterate over all multiples of p, i.e., k = p, 2p, 3p, ..., up to max_a.

   c. For each k, compute e_p(k) (number of times p divides k).

   d. sum_p += cnt_ge[k] * e_p(k).

   e. After processing all multiples, sum_p is the exponents_required(p).

Once we have exponents_required for each p, then we need to find the minimal n such that for all p, the exponent of p in n! is >= sum_p.

Now, how to compute e_p(k) for each k?

For a multiple k = m * p, the exponent e_p(k) is the exponent of p in m*p. Which is e_p(m) + 1. So, for example:

k = p*1 → e_p(k) = 1.

k = p*2 → if 2 is divisible by p (only if p=2), then e_p(k) = 1 + e_p(2) (which is 1 if p=2, so e_p(k) = 2). Otherwise, e_p(k) is 1.

But how to compute e_p(k) efficiently for all multiples of p.

Wait, perhaps for each multiple k = p * m, e_p(k) = e_p(m) + 1. So we can compute e_p(k) recursively.

But that might be time-consuming. Alternatively, for each k divisible by p, e_p(k) is the maximum exponent e such that p^e divides k. So for each k, when we generate it as a multiple of p, we can compute e_p(k) by dividing by p until it's no longer divisible.

But for k up to 1e7, this is feasible.

Alternatively, for a given p, when generating multiples of p, for each multiple k = p * m, the exponent e_p(k) is 1 + e_p(m). But this requires memoization or a way to track e_p(m).

But maybe for each k, we can precompute the exponents for all primes. However, that would be too memory-intensive for 1e7.

Alternative idea: For each multiple k of p, e_p(k) can be computed by continuously dividing by p and counting the number of divisions. For example:

def count_p(k, p):
    cnt =0
    while k % p ==0:
        cnt +=1
        k =k//p
    return cnt

But for each multiple k of p, this function will return at least 1. So for k = p * m, the count_p(k,p) is at least 1.

But how efficient is this?

For example, for p=2, the multiples are 2,4,6,8, etc. For 2, count_p(2,2) is 1. For 4, it's 2. For 6, it's 1. For 8, it's 3, etc. But for each k, this is O(log_p k) time. So for all multiples of p up to max_a, this would take O((max_a/p) * log_p max_a) time. For p=2 and max_a=1e7, it's (5e6) * 23 (since 2^23 is about 8e6) → 1e8 operations. Which is way too much for Python.

So this approach is not feasible.

Alternative approach: For each multiple of p, we can compute e_p(k) on the fly.

For example, for p=3, the multiples are 3,6,9,12, etc.

For each multiple k = m * p, e_p(k) is e_p(m) + 1.

But if we process the multiples in order, m starts from 1 and increases. However, m can be divisible by p multiple times.

Wait, but if we process the multiples in order of increasing k, then when we reach k = p^e, we can compute e_p(k) as e.

But this seems tricky.

Alternative idea: For each prime p, generate all multiples of p, then for each such multiple k, compute e_p(k) as follows:

Initialize e = 1.

While k/p is divisible by p, increment e and divide k by p.

Wait, but this is the same as count_p(k, p) function. So for each k, we have to compute how many times p divides it.

But for large p, this could be manageable. For example, when p is large (say, 1e6), the multiples are few (e.g., 1e6, 2e6, etc.), and each of these multiples will have e_p(k) =1 unless k is a multiple of p^2, which is possible only if the multiple is p^2, 2p^2, etc.

But how to compute this efficiently.

Alternatively, for each multiple k of p, we can compute e_p(k) as the maximum e such that p^e divides k. So, e_p(k) = the exponent of p in k's prime factors.

But to compute this, for each k, we can compute it on the fly.

But this will take O( (max_a /p) * log_p (max_a/p) ) per prime p. The total for all primes would be O( sum_p (max_a/p) * log_p (max_a) ) ), which might be manageable for Python.

But for p=2, max_a=1e7, this would be (1e7 /2) * log2(1e7) ≈ 5e6 * 23 ≈ 1e8 operations, which is way too slow.

This is a problem. So this approach is not feasible.

So we need a better way to compute exponents_required(p) for all primes p.

Alternative idea: Precompute for each number up to max_a, its prime factors and exponents. Then for each prime p, exponents_required(p) is the sum of cnt_ge[k] * e_p(k) for all k.

But precomputing the exponents for all primes in each number up to 1e7 would require O(1e7 * log 1e7) memory, which is not feasible. Because for each number, storing the exponents for all primes is impossible.

Alternative idea: For each prime p, we can iterate through its multiples and count the exponents in a way that accumulates the sum without recomputing e_p(k) each time.

Wait, for example, for p=2:

All multiples of 2 contribute their exponents of 2. So the sum is:

sum_{k=2,4,6,8,...} cnt_ge[k] * e_p(k)

But each multiple can be written as 2^e * m, where m is odd. So e_p(k) is e.

But how to compute e_p(k) for all multiples of p.

Alternative approach: For each prime p, iterate through all exponents e starting from 1, and for each e, add cnt_ge[p^e] to the sum. Then for e=2, add cnt_ge[p^2] * 1 (since p^2 is divisible by p^2, and for each multiple of p^2, but wait, no. Wait, this approach might not work.

Wait, perhaps for each prime p, exponents_required(p) is the sum over e=1 to max_e of floor(sum_{a_i} (number of times p^e divides a_i! )).

Wait, no. That's the same as the original definition. So back to square one.

Alternative Idea: The sum of exponents_required(p) can be rewritten as:

sum_{a in a_list} sum_{m=1}^{∞} floor(a / p^m)

But for a given a and p, sum_{m} floor(a/p^m) is equal to the exponent of p in a!.

Which is known to be (a - sum of digits of a in base p) / (p-1). Wait, not sure. Wait, that formula applies to the sum of digits in base p for a.

Alternatively, the exponent of p in a! is given by Legendre's formula: sum_{m=1}^∞ floor(a / p^m).

But how can we compute this sum for all primes p and all a in a_list efficiently.

But the problem is that for each a in a_list, and each prime p <= a, we need to compute the sum of floor(a/p^m) for m=1 to infinity. Then sum these across all a in a_list.

But the number of a's is up to 1e6, and for each a, the number of primes up to a is O(a / log a), which for a=1e7 is about 6e5. So for 1e6 a's, this would be 1e6 * 6e5 = 6e11 operations, which is impossible.

So this approach is not feasible.

So back to the previous problem: how to compute exponents_required(p) for each prime p.

Alternative Idea: Let's think of exponents_required(p) as sum_{m=1}^\infty s_m, where s_m is the sum over all a_i of floor(a_i / p^m).

Then, for each prime p, compute s_1, s_2, ... until p^m > max_a.

But how to compute s_m efficiently.

But s_m is sum_{a_i} floor(a_i / p^m) = sum_{q=1}^{floor(max_a / p^m)} cnt_ge[q * p^m}.

So, for each m, we compute s_m and add to exponents_required(p).

Now, the question is, for a given p, how many m's are there where p^m <= max_a.

For example, for p=2 and max_a=1e7, m can be up to 23 (since 2^23 is 8,388,608 which is less than 1e7, and 2^24 is 16,777,216 which is larger).

So for each p, m ranges from 1 to log_p (max_a). Which is manageable.

But for each m, we need to compute s_m as sum_{q=1}^{q_max} cnt_ge[q*p^m}.

The problem is that for p^m being small, q_max can be very large. For example, if p=2 and m=1, q_max is 5e6 (since 2*5e6=1e7). So summing from q=1 to 5e6 for each such p and m is O(5e6) operations. For p=2, this would take 5e6 operations for m=1, then 2.5e6 for m=2, etc. The total for p=2 would be about 1e7 operations, which is manageable for a single prime, but if there are 6e5 primes, this is not feasible.

Thus, the key is to find a way to compute s_m for all m and p efficiently.

But how?

Alternative Idea: Precompute for all possible exponents m and primes p, but that's not feasible.

Alternative Idea: For each prime p, compute s_m for m=1, 2, ... until p^m > max_a. For each m, compute s_m as sum_{q=1 to q_max} cnt_ge[q * p^m}.

But the problem is that for p=2, m=1, the sum is over q=1 to 5e6. For each q, check if q * p^m is <= max_a. But even then, this is O(5e6) per m and p.

So, this approach is O(total number of primes * sum over m of (max_a / p^m)), which is O(max_a * sum_p (1/(p-1)) ), which for max_a=1e7 and sum_p (1/p) is about log log 1e7 ≈ 3. So O(3e7), which is manageable in Python.

Wait, sum_p (sum_{m=1}^infty (max_a / p^m)) ) = max_a sum_p (1/p (1/(1 - 1/p))) ) = max_a sum_p (1/(p-1)).

But sum_p 1/(p-1) is not convergent. Wait, no. sum_p 1/p converges to about log log N. So sum_p 1/(p-1) is roughly sum_p 1/p + sum_p 1/(p(p-1)) ), which converges. But in practice, for primes up to 1e7, sum_p 1/(p-1) is manageable.

But in any case, the total operations would be O(max_a * log log max_a) which is about 1e7 * 3 → 3e7 operations. Which should be manageable.

So, here's the plan:

1. Read all a_i's, compute the frequency array.

2. Compute cnt_ge array.

3. Sieve of Eratosthenes to find all primes up to max_a.

4. For each prime p in the sieve:

   a. Initialize exponents_required_p = 0.

   b. For m from 1 to log_p (max_a):

      i. Compute x = p^m.

      ii. Compute q_max = floor(max_a / x).

      iii. If q_max == 0, break.

      iv. For q from 1 to q_max:

           exponents_required_p += cnt_ge[q * x]

      v. Add this to exponents_required_p.

   c. After processing all m, store exponents_required_p.

5. For each prime p, find the minimal n_p such that sum_{m=1}^\infty floor(n_p/p^m) >= exponents_required_p.

6. The answer is the maximum n_p over all primes p.

But step 4.b.iv is O(q_max) per p and m, which is acceptable for 3e7 operations.

But even this might be tight in Python for large primes.

Alternative Idea: Optimize the computation of s_m for each p and m.

For example, for x = p^m, q ranges from 1 to q_max = floor(max_a /x).

The sum s_m is sum_{q=1 to q_max} cnt_ge[q *x].

But cnt_ge is an array where cnt_ge[v] is the number of a_i >=v. So cnt_ge[q*x] is the number of a_i >= q*x.

But this is equivalent to the sum of freq[v] for v >= q*x.

So, the sum s_m is sum_{q=1}^q_max sum_{v >= q*x} freq[v}.

Which can be rewritten as sum_{v >= x} freq[v} * floor(v/x).

Because for each v >=x, floor(v/x) is the number of q's such that q*x <=v. For example, v=5, x=2 → q can be 1 and 2 → floor(5/2) = 2.

But this is the same as the original sum.

So s_m is sum_{v >=x} freq[v} * floor(v/x).

Which is the same as sum_{v in a_i} floor(v/x).

But how to compute this sum efficiently.

This brings us back to the original problem: compute sum_{v in a_i} floor(v/x) for x=p^m.

But this sum can be computed as sum_{q=1}^q_max cnt_ge[q*x}.

But how to compute this sum quickly.

An alternative approach is to realize that for a given x, the sum is the same as the sum of all multiples of x, but this is not helpful.

But if we precompute the cnt_ge array, and then for each x, compute the sum of cnt_ge[x], cnt_ge[2x], etc., up to floor(max_a/x), this is manageable.

But again, for x=1, this would require 1e7 iterations, which is not feasible.

So, here's the crux of the problem: For each prime p, and each m, we need to compute the sum of cnt_ge[p^m], cnt_ge[2*p^m], ..., cnt_ge[q_max*p^m}.

But how to compute this sum efficiently.

An alternative Idea: Precompute a prefix sum array for cnt_ge, but reversed. For example, a cumulative sum from max_a down to 1. But the sum from x to y can be computed as sum_ge[x] - sum_ge[y+1]. So, the sum of cnt_ge for all v >= x is sum_ge[x].

But how to compute the sum of cnt_ge for v that are multiples of x.

For example, x=2: multiples are 2,4,6, etc. The sum is cnt_ge[2] + cnt_ge[4] + ... + cnt_ge[2*q_max}.

But the problem is that these multiples are not contiguous in the cnt_ge array, so we can't directly compute their sum using a prefix sum.

But what if we can precompute for all possible x, the sum of cnt_ge[x], cnt_ge[2x], ... ?

This is similar to a sieve approach. For each x, iterate over multiples and accumulate the sum.

But for x up to 1e7, this would take O(1e7 log 1e7) time, which is not feasible.

But perhaps for x being p^m, where p is a prime, this is manageable.

But even then, for each prime p and each m, x is p^m. For example, for p=2, m=1, x=2; m=2, x=4; etc.

So, the total number of x's is O( sum_p log_p max_a ), which is about O( (max_a / log max_a) ) * log max_a) = O(max_a). So it's O(1e7) x's. For each x, summing over the multiples would take O(max_a/x) steps. The total steps would be O(max_a log max_a), which is about 3e8 for max_a=1e7. This is manageable in C++ but may be tight in Python.

But in Python, even 1e8 operations are going to be too slow. So this approach may not be feasible.

Thus, we need to find a way to compute s_m for each prime p and m in O(1) time, using precomputed data structures.

Alternative Idea: Use a binary indexed tree or a segment tree to represent the cnt_ge array, allowing for fast summation of multiples of x.

But building such a structure for 1e7 elements is memory-intensive and time-consuming.

Alternative Idea: Note that the sum s_m is the sum of cnt_ge[x], cnt_ge[2x], ..., cnt_ge[ q_max x]. For each x, this sum is equal to sum_{k=1}^q_max cnt_ge[kx}.

But this sum can be computed as the sum of cnt_ge[v] for all v divisible by x.

So, for each x, the sum is the sum of cnt_ge[v] where v mod x == 0.

But how to compute this efficiently.

Another Idea: For each x, the sum can be computed as sum_{v= x, 2x, 3x, ...} cnt_ge[v}.

Which can be written as sum_{d=1}^\infty cnt_ge[d*x}.

So, the sum is sum_{d=1} cnt_ge[d*x}.

To compute this sum, we can note that d ranges up to floor(max_a /x).

But how to compute this sum quickly.

An alternative approach is to precompute a frequency array freq_ge, where freq_ge[v] = cnt_ge[v}, and then for each x, sum over all multiples of x in freq_ge.

But this is exactly the same problem as before.

So, perhaps the only feasible way is to precompute for each x (p^m) the sum of its multiples' cnt_ge values.

But given the time constraints in Python, this might not be possible.

So, what's the alternative?

Perhaps precompute the sum for each x once, but how.

Another Idea: Precompute for each x, the sum of cnt_ge[x] + cnt_ge[2x] + ... + cnt_ge[kx}, where kx is the largest multiple of x <= max_a.

But this is not feasible for all x up to 1e7.

But if we only need to compute this for x being p^m where p is a prime, and m >=1, then the number of x's is manageable.

But how.

Alternatively, for each prime p, and for each m, compute x = p^m, and then compute the sum.

But again, this could be manageable.

But for each x, how to compute the sum of multiples.

In Python, for x in p^m:

sum_q = 0

current = x

while current <= max_a:

    sum_q += cnt_ge[current]

    current += x

But for x=2 and max_a=1e7, this would take 5e6 iterations. Which is 5e6 operations for this x. But for x=4, it would take 2.5e6, and so on.

For each prime p, the total number of iterations for all m is (max_a/p) + (max_a/p²) + ... + (max_a/p^e) = max_a/(p-1). Which for p=2 is 1e7/1 = 1e7 iterations, which is way too slow.

Thus, this approach is not feasible.

So, I'm stuck. Let's think of another way.

Alternative Idea: Precompute for each possible x (prime power) the sum of cnt_ge[x's multiples] using mathematical formula.

But how.

Wait, sum_{q=1}^∞ cnt_ge[x*q} is the same as sum_{v=x, 2x, ...} cnt_ge[v}.

But cnt_ge[v} is the number of a_i >=v.

So, sum_{v=x, 2x, ...} cnt_ge[v} = sum_{v=x, 2x, ...} sum_{a in a_i} (a >=v ? 1 : 0).

This can be rewritten as sum_{a in a_i} sum_{v=x, 2x, ...} (v <=a} 1.

For each a, the number of v's that are multiples of x and <=a is floor(a/x).

So, sum_{v=x, 2x, ...} cnt_ge[v} = sum_{a in a_i} floor(a/x).

But this is exactly what we need to compute s_m.

So, the sum for x=p^m is sum_{a in a_i} floor(a/x).

Which is the same as s_m.

So, the sum s_m is sum_{a in a_i} floor(a/x).

But this sum can be computed as follows:

For each a in a_i, floor(a/x) is simply a//x.

So, if we can compute the sum of a//x for all a in a_i, that gives us s_m.

But how to compute this sum for a given x.

But x is up to 1e7. For each x, the sum would be O(1) if we have a frequency array and precomputed sums for each x.

But how to compute the sum of floor(a/x) for all a in a_i.

Let's think of this sum as sum_{a} freq[a] * (a//x).

We can precompute a frequency array freq[a], and for each x, compute the sum of freq[a] * (a//x) for a from 1 to max_a.

But this would require O(max_a) operations per x, which is not feasible.

Alternative Idea: Precompute a prefix sum array for each a, but I'm not sure.

Alternatively, use the frequency array and precompute the sum of floor(a/x) for all possible x.

But this is not feasible for x up to 1e7.

Alternative Idea: For each x, the sum can be computed as sum_{k=0}^∞ (number of a_i >=k*x) * 1, which is what we discussed earlier. But how to compute this sum in O(1) time per x.

But this requires having a data structure that can quickly answer the count of a_i >= q*x for any q and x.

But given that x can be up to 1e7 and q can be up to 1e7/x, this is challenging.

But with the cnt_ge array, for any x, the sum is sum_{q=1}^q_max cnt_ge[q*x}.

So, the problem reduces to for a given x, compute the sum of cnt_ge at multiples of x.

But how to compute this sum efficiently.

Perhaps, for each x, the sum can be computed as:

sum_q cnt_ge[q*x} = sum_{m=x}^max_a cnt_ge[m} * (1 if m mod x == 0 else 0).

But this requires iterating over all multiples of x and summing cnt_ge[m}, which is O(max_a/x) per x.

Which brings us back to the same problem.

Thus, I think the only way is to proceed with this approach and optimize it as much as possible in Python.

Let's outline the steps again:

1. Read k and the list of a_i's.

2. Find the maximum a_i, max_a.

3. Create a frequency array freq of size max_a+1.

4. Populate freq with the count of each a_i.

5. Compute cnt_ge[v], the number of a_i >=v, for all v from 1 to max_a.

   This can be done by:

   cnt_ge = [0] * (max_a + 2)

   cnt_ge[max_a + 1] = 0

   for v in range(max_a, 0, -1):

       cnt_ge[v] = cnt_ge[v+1] + freq[v]

6. Generate all primes up to max_a using sieve of Eratosthenes.

7. For each prime p in the sieve:

   a. Compute the required exponent for p.

   b. This exponent is sum_{m=1}^∞ sum_{q=1}^∞ cnt_ge[p^m * q}.

   c. For each m, compute x = p^m.

   d. If x > max_a, break.

   e. Compute q_max = max_a // x.

   f. For q from 1 to q_max:

       add cnt_ge[x*q] to the required exponent.

8. For each prime p, compute the minimal n_p such that the exponent of p in n_p! is >= required exponent.

9. The answer is the maximum n_p across all primes.

Now, the question is how to optimize steps 7c to 7f in Python.

In Python, loops can be slow, but using list comprehensions and precomputed cnt_ge arrays can help.

But for x = p^m, which can be up to max_a, and q up to max_a/x, this can be a lot of iterations.

But let's think about how to optimize this.

For example, when x is large, q_max is small. So for primes p close to max_a, x=p is already large, and q_max is 1. So for each such p, the loop runs once.

But for small primes like 2, the loops run many times.

So, perhaps, for each prime p, we can generate all possible exponents m, compute x = p^m, and then compute the sum for that x by summing cnt_ge[x * q] for q from 1 to q_max.

But to speed this up, we can use the following:

Instead of iterating q from 1 to q_max and accumulating cnt_ge[x*q], we can precompute the sum for each x using a mathematical formula.

But I'm not sure.

Alternative Idea: Precompute the cnt_ge array, and for each x, use a slice of cnt_ge starting at x and stepping x. Then sum all elements in this slice.

In Python, this can be done as follows:

current = x

sum_s = 0

while current <= max_a:

    sum_s += cnt_ge[current]

    current += x

But this is the same as before and is O(q_max) time.

But in Python, for small q_max, this is manageable. For large q_max (like 5e6 for x=2), this will take time.

But perhaps using a precomputed list of cnt_ge and stepping through it with steps of x can be optimized using numpy.

But since the problem requires that the code reads from stdin and writes to stdout, and numpy is not allowed (or is it? The problem says to use Python 3, but doesn't mention numpy. So probably, the code must use pure Python.

Thus, for large x=2, this loop will take 5e6 iterations, which could be very slow in Python.

This suggests that this approach is not feasible for Python for large inputs.

Thus, we need a better way.

Let me think again about the problem.

We need to compute for each prime p, the sum over m of sum_{a in a_i} floor(a/p^m).

But this is the same as sum_{a in a_i} (sum_{m=1}^\infty floor(a/p^m)).

Which is the same as sum_{a in a_i} exponent of p in a!.

Which is the same as sum_{a in a_i} (sum_{k=1}^\infty floor(a/p^k)).

So, for each prime p, the required exponent is the sum of exponents of p in each a_i!.

But exponents of p in a_i! can be computed using Legendre's formula.

So, if we can compute for each a in a_i, the exponents of all primes p in a! and accumulate them, that would work.

But the problem is that a_i can be up to 1e7 and there can be 1e6 of them. So for each a_i, we would need to factorize a_i! into primes, which is not feasible.

But wait, the exponents for each prime p in a_i! can be computed as sum_{m=1}^\infty floor(a_i/p^m).

So, for each a_i, and each prime p <=a_i, compute this sum and accumulate it.

But for 1e6 a_i's, each requiring up to 1e7 primes (but actually up to their own a_i), this is impossible.

Alternative Idea: For each prime p, the sum of exponents over all a_i's is the sum over all a_i's of sum_{m=1}^\infty floor(a_i/p^m) = sum_{m=1}^\infty sum_{a_i} floor(a_i/p^m) = sum_{m=1}^\infty s_m, where s_m is sum_{a_i} floor(a_i/p^m).

So, the problem is to compute s_m for each p and m.

But s_m is sum_{a_i} floor(a_i/x), where x = p^m.

But sum_{a_i} floor(a_i/x) is sum_{q=1}^\infty cnt_ge[q*x}.

So, the key is to find a way to compute this sum quickly for all x = p^m.

But again, this seems like the same problem.

But perhaps, we can precompute a data structure that allows us to quickly compute the sum of cnt_ge at multiples of x for any x.

This is similar to a frequency table where for each x, the sum of multiples is known.

But how to do this.

Alternative Idea: Precompute for each x, the sum of cnt_ge[x] + cnt_ge[2x] + ... + cnt_ge[kx}, where kx <= max_a.

But with x up to 1e7, this is not feasible.

Thus, I'm stuck. Perhaps the only way is to proceed with the initial approach and hope that it passes in Python.

So, let's proceed to code this approach.

First, generate the primes up to max_a using sieve of Eratosthenes.

Then, precompute the cnt_ge array.

For each prime p, compute the required exponents by iterating over m from 1 upwards, compute x = p^m, and sum cnt_ge[x*q] for q from 1 to q_max.

But in Python, loops are slow, especially for large x.

But for the test case where the input is 2 a_i's of 1000, the maximum a is 1000.

In this case, for p=2, the required exponents are 1000//2 + 1000//4 + ... for each a_i, multiplied by 2. Then summed.

So, the code should compute this correctly.

But for large primes and large exponents, it's manageable.

So, let's proceed to code.

But first, sieve of Eratosthenes for max_a up to 1e7.

But generating sieve for 1e7 in Python can be memory-intensive. For example, a sieve of 1e7 elements is 1e7 bits, which is about 1.25MB. But in Python, using a list of booleans would require 1e7 bytes (about 10MB), which is manageable.

But for efficiency, perhaps use a sieve optimized for space.

But let's proceed.

So, the code steps are:

Read k and a list of a_i's.

Compute frequency array.

Compute cnt_ge.

Generate primes up to max_a using sieve.

For each prime p:

   compute the required exponents.

   by iterating m from 1 to infinity:

       x = p^m

       if x > max_a: break

       q_max = max_a // x

       sum_m = 0

       current = x

       while current <= max_a:

           sum_m += cnt_ge[current]

           current += x

       required_exponents += sum_m

Then, for each prime p, compute the minimal n_p such that the exponent of p in n_p! is >= required_exponents.

The minimal n_p is the smallest n such that sum_{m=1}^\infty floor(n/p^m) >= required_exponents.

To find this n_p, we can perform a binary search between low and high.

The minimal n_p is the smallest n where the sum of exponents of p in n! is >= required_exponents.

The sum for a given n can be computed as sum_{m=1}^\infty floor(n/p^m).

We can compute this sum for any n quickly.

So, for each prime p and required exponent, we can perform binary search to find the minimal n_p.

The initial binary search boundaries can be 0 and required_exponents * p.

Because for n = required_exponents * p, the sum is at least required_exponents.

But perhaps a better upper bound is possible.

But for the purposes of binary search, it's manageable.

Once all n_p are computed, the answer is the maximum of these n_p.

Now, let's code this.

But given the time constraints in Python, this code may not pass for large inputs.

But perhaps we can optimize some steps.

First, sieve of Eratosthenes for max_a.

But in Python, sieve for 1e7 is manageable.

Example sieve:

def sieve(n):

    is_prime = [True] * (n+1)

    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5)+1):

        if is_prime[i]:

            for j in range(i*i, n+1, i):

                is_prime[j] = False

    primes = [i for i, val in enumerate(is_prime) if val]

    return primes

But for n=1e7, this will take O(n log log n) time, which is acceptable.

Next, compute the frequency array and cnt_ge.

For example:

max_a = max(a_list)

freq = [0] * (max_a + 1)

for a in a_list:

    freq[a] += 1

cnt_ge = [0] * (max_a + 2)

cnt_ge[max_a + 1] = 0

for v in range(max_a, 0, -1):

    cnt_ge[v] = cnt_ge[v+1] + freq[v]

Then, for each prime p in primes:

required = 0

current_p = p

while True:

    x = current_p

    if x > max_a:

        break

    q_max = max_a // x

    # sum cnt_ge[x], cnt_ge[2x], ..., cnt_ge[q_max*x]

    sum_s = 0

    current = x

    while current <= max_a:

        sum_s += cnt_ge[current]

        current += x

    required += sum_s

    current_p *= p

Once required is computed, find the minimal n_p via binary search.

But the binary search for each prime may be time-consuming.

But given that the number of primes is up to 6e5, and each binary search has log2(required) steps, which is manageable.

But wait, the binary search for each p can be optimized.

The function f(n) = sum_{m=1}^\infty floor(n/p^m) is non-decreasing in n. So we can binary search for the minimal n where f(n) >= required.

The sum f(n) can be computed as:

sum = 0

current = p

while current <= n:

    sum += n // current

    current *= p

So for a given n and p, this sum is computed in log_p(n) steps.

Thus, for binary search, for each p, the minimal n_p is found by:

low = 0

high = required * p

while low < high:

    mid = (low + high) // 2

    s = sum_floor(mid, p)

    if s >= required:

        high = mid

    else:

        low = mid + 1

Thus, the code for sum_floor is straightforward.

Putting it all together.

But in Python, this code may be too slow for large inputs.

But given the problem constraints, this is the best possible approach.

Now, let's write the code.

But first, let's test the code with the examples.

Example 1:

Input:

2

1000 1000

The product of a_i!s is (1000!)^2.

So the required exponents for each prime p is 2 * exponent of p in 1000!.

We need to find the minimal n such that exponent of p in n! >= 2 * exponent of p in 1000!.

For p=2, exponent in 1000! is 1000//2 + 1000//4 + ... = 500 + 250 + 125 + 62 + 31 + 15 + 7 + 3 + 1 = 994.

So required exponents for p=2 is 2 * 994 = 1988.

The minimal n for p=2 is such that exponent of 2 in n! >= 1988.

The minimal such n is 2000, as 2000//2 + 2000//4 + ... = 1000 +500 +250+125+62+31+15+7+3+1 = 1993 >= 1988.

Thus, the output is 2000.

The code should compute this correctly.

Example 2:

Input:

1

2

q = 2! = 2. We need n! / 2 to be integer, which requires n! >=2. The minimal n is 2.

The code should output 2.

Now, let's code.

But considering Python's speed, for large inputs (k=1e6, a_i=1e7), this code may not pass, but I'm not sure.

But according to the problem statement, the code is expected to be optimized.

But in Python, the sieve for 1e7 will take time, but manageable.

The main problem is the loop for x = p^m and q.

But perhaps for small primes, this loop is too slow.

But given the time constraints of 5 seconds, it's possible that this code will pass.

So here's the Python code.
</think>

```python
import sys

def main():
    input = sys.stdin.read().split()
    k = int(input[0])
    a_list = list(map(int, input[1:k+1]))
    
    if not a_list:
        print(0)
        return
    
    max_a = max(a_list)
    
    # Frequency array
    freq = [0] * (max_a + 2)
    for a in a_list:
        freq[a] += 1
    
    # Compute cnt_ge: cnt_ge[v] = number of a >= v
    cnt_ge = [0] * (max_a + 2)
    cnt_ge[max_a + 1] = 0
    for v in range(max_a, 0, -1):
        cnt_ge[v] = cnt_ge[v + 1] + freq[v]
    
    # Sieve of Eratosthenes to get primes up to max_a
    sieve_max = max_a
    is_prime = [True] * (sieve_max + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(sieve_max**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, sieve_max + 1, i):
                is_prime[j] = False
    primes = [i for i, val in enumerate(is_prime) if val]
    
    max_n = 0
    for p in primes:
        required = 0
        current_p = p
        while True:
            x = current_p
            if x > max_a:
                break
            sum_s = 0
            current = x
            while current <= max_a:
                sum_s += cnt_ge[current]
                current += x
            required += sum_s
            next_p = current_p * p
            if next_p > sieve_max:
                break
            current_p = next_p
        
        # Binary search for minimal n_p
        low = 0
        high = required * p  # Upper bound can be optimized
        best = 0
        while low <= high:
            mid = (low + high) // 2
            total = 0
            divisor = p
            while divisor <= mid:
                total += mid // divisor
                divisor *= p
            if total >= required:
                best = mid
                high = mid - 1
            else:
                low = mid + 1
        if best > max_n:
            max_n = best
    print(max_n)

if __name__ == "__main__":
    main()
```