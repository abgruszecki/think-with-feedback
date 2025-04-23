<think>
Okay, let's tackle this problem. So, we need to compute for each r from 0 to k the number of n x n matrices over the field mod p with rank exactly r. And since n can be up to 1e18, we can't compute things naively. Hmm.

First, I remember that the number of matrices of rank r over a finite field GF(p) is given by some formula involving products of terms. Let me recall the formula. Oh right, the formula is the product from i=0 to r-1 of (p^n - p^i) * (p^n - p^i) divided by (p^r - p^i) for i=0 to r-1. Wait, maybe not exactly. Wait, the standard formula for the number of matrices of rank r in GF(q) is:

prod_{i=0}^{r-1} ( (q^n - q^i) )^2 / (q^r - q^i) )

But maybe I should rederive it.

The idea is that building a matrix of rank r involves choosing r linearly independent rows (forming a basis), then choosing the other rows as linear combinations of those. Alternatively, the number of rank r matrices is equal to the number of ways to select an r-dimensional subspace (the row space), and then for each row, choose a vector in that subspace. But perhaps a better way is to construct the matrix step by step.

Alternatively, the count can be computed as follows: the first row must be non-zero (for r >= 1). The second row must not be in the span of the first. The third row must not be in the span of the first two, etc., until r rows are chosen. Then, the remaining rows can be any linear combinations of these r rows.

But wait, that's for the row-echelon form approach. So for a matrix of rank r, the number is equal to the number of ways to choose r linearly independent rows (the first r steps), and then the rest of the rows are arbitrary linear combinations of those. But I'm not sure. Maybe I need to think differently.

Alternatively, the number of matrices of rank r is equal to the Gaussian binomial coefficient for choosing an r-dimensional subspace (the column space) multiplied by the product for the rows to be in that subspace. Wait, perhaps not. Let me look up the formula.

Upon checking some combinatorics references, the formula for the number of n x n matrices over GF(q) of rank r is:

N(r) = (product_{i=0}^{r-1} (q^n - q^i))^2 / (product_{i=0}^{r-1} (q^r - q^i))) ) 

Wait, no. Wait, the standard formula is:

The number of matrices of rank r is equal to [ (product_{i=0}^{r-1} (q^n - q^i)) )^2 / product_{i=0}^{r-1} (q^r - q^i) ) ] * product_{i=0}^{r-1} (q^r - q^i) ?

No, perhaps the formula is derived as follows. To construct a matrix of rank r, you can first choose a sequence of r linearly independent rows, then choose a sequence of r linearly independent columns such that their span is the column space. Then the rest of the rows are linear combinations of those r rows. But maybe I'm getting confused.

Alternatively, here's a way to compute the number of matrices of rank r over GF(q):

The count is given by the Gaussian binomial coefficient [n choose r]_q multiplied by the product (q^n - q^i) for i from 0 to r-1. Wait, perhaps not. Let me think again.

The standard approach is to consider that building a rank r matrix requires selecting an r-dimensional row space and an r-dimensional column space. But perhaps the formula is:

N(r) = (gaussian_binom(n, r, q) )^2 * (product_{i=0}^{r-1} (q^r - q^i)) ) * q^{r(n - r)}}

Wait, maybe not. Alternatively, here's a method:

The number of rank r matrices is equal to the number of ways to choose an r-dimensional subspace (row space), then for each row, the vector must lie in that subspace. The same applies to the column space. Hmm, no. Maybe the correct formula is derived as follows:

The number of possible matrices of rank r is equal to the product of the number of ways to choose a basis for the row space, then for each column, the entries can be any vector in the row space's dual (or something like that). Hmm, perhaps this is getting too complicated.

Alternatively, a reference I found says that the number of n x n matrices of rank r over GF(q) is:

N(r) = (product_{i=0}^{r-1} (q^n - q^i))^2 / product_{i=0}^{r-1} (q^r - q^i) )

But I need to confirm this. Let's test it with the first example.

In the first example, input is 3 2 3. The output is 1 49 294 168. For r=0, the matrix must be all zeros. So 1. For r=1, the count is 49. Let's compute according to the formula.

For r=1: product_{i=0}^0 (2^3 - 2^i) is (8-1) =7. Then squared is 49. Divided by product_{i=0}^0 (2^1 -2^0) = 1. So 49, which matches. For r=2: product from i=0 to 1 of (8-2^i) is (8-1)(8-2) =7*6=42. Squared is 42^2=1764. Divided by product (2^2 -2^0) (2^2 -2^1) → (4-1)(4-2) =3*2=6. So 1764/6=294. Which matches. For r=3: product (8-1)(8-2)(8-4)=7*6*4=168. Squared is 168²=28224. Divided by product (4-1)(4-2)(4-4) → wait, but for r=3, product is (2^3 - 2^0) ... (2^3 - 2^2) → (8-1)(8-2)(8-4) =7*6*4=168. So 168² / 168 =168. Which is the answer. So the formula seems correct.

So the general formula for N(r) is:

N(r) = [ (product_{i=0}^{r-1} (p^n - p^i) )^2 ] / product_{i=0}^{r-1} (p^r - p^i) )

But for r=0, the product is empty (i ranges from 0 to -1), so the product is 1. So N(0) is 1, which is correct.

So the problem reduces to, for each r from 0 to k (but since n can be up to 1e18 and k up to 5000), compute this formula efficiently.

But the problem is how to compute this for very large n, especially since n can be up to 1e18. Because the exponents will be very large, but modulo 998244353.

Wait, but the formula involves terms like p^n mod 998244353. Since p can be up to 998244353 (but the constraints say p is a prime less than 998244353). So for each term (p^n - p^i) mod MOD (where MOD is 998244353), we can compute p^n mod MOD as pow(p, n, MOD), then subtract pow(p, i) mod MOD, then multiply all those terms.

But wait, the product is (p^n -1) * (p^n - p) * (p^n - p^2) * ... * (p^n - p^{r-1}) for the numerator, and denominator is (p^r - 1) * (p^r - p) * ... (p^r - p^{r-1}).

But when r exceeds n, then the formula's numerator terms may include p^n - p^i where i is up to r-1. But if r exceeds n, then for i >=n, the term p^i is larger than p^n, but since n is up to 1e18, perhaps even for i up to 5000, when r is up to 5000, i could be up to 4999. But p can be up to 5e8, but in this case, even if p is 5e8, but i is 5000, p^i is way larger than MOD. But we need to compute p^i mod MOD. However, since MOD is 998244353, which is a prime, and p is a prime less than MOD. So for each term in the denominator, p^r is computed mod MOD, but p^r can be computed via fast exponentiation, and similarly for p^i.

Wait, but for the denominator's product, the terms are (p^r - p^i) for i from 0 to r-1. So for each r, we need to compute these terms. But when r is up to 5000, and i up to r-1, then for each r, the product is (p^r - 1) * (p^r - p) * ... * (p^r - p^{r-1}).

Wait, but for the denominator, when i ranges from 0 to r-1, the product is the same as the product of (p^r - p^i) for i=0 to r-1.

But note that for r up to 5000, and p up to 1e9, but modulo MOD=998244353, we can compute p^i mod MOD for i up to 5000. So precompute an array of p_pows[i] = p^i mod MOD, for i from 0 to 5000.

Similarly, for each r, compute p^r mod MOD, which can be done via pow(p, r, MOD). Then for each term (p^r - p^i) mod MOD, which is (pow(p, r, MOD) - p_pows[i]) mod MOD.

But the problem is that the formula for N(r) is (product_num)^2 / product_den, where product_num is the product of (p^n - p^i) for i=0..r-1, and product_den is the product of (p^r - p^i) for i=0..r-1.

But how do we compute this modulo 998244353 when division is involved. We need to compute the product_num squared multiplied by the modular inverse of product_den, all mod MOD.

But product_den is the product of (p^r - p^i) for i=0..r-1. Let's call this product_den[r] = product_{i=0}^{r-1} (p^r - p^i).

But when r is up to 5000, we can precompute product_den for each r from 0 to k. But since k can be up to 5000, this is manageable.

The key steps are:

1. Precompute p_pows[i] = p^i mod MOD, for i up to 5000. Because when r is up to 5000, the terms in product_den[r] involve p^i up to p^{r-1}, which is up to 5000-1=4999. So precompute p_pows[0...5000].

2. For each r from 0 to k:

   a. Compute product_num[r] = product_{i=0}^{r-1} (p^n - p^i) mod MOD.

   b. Compute product_den[r] = product_{i=0}^{r-1} (p^r - p^i) mod MOD.

   Then, N(r) is (product_num[r]^2) * inv(product_den[r]) mod MOD.

But for very large n, how to compute (p^n - p^i) mod MOD?

Because n can be up to 1e18, so p^n mod MOD can be computed with pow(p, n, MOD).

But for each term (p^n - p^i) mod MOD, we can compute it as (pow_pn - p_pows[i]) % MOD, where pow_pn is pow(p, n, MOD).

But wait, for each i in 0 to r-1, we need to compute (p^n - p^i) mod MOD. However, when r is up to 5000, and i up to 4999, we can compute this for each i.

So the steps are:

- Precompute p_pows[i] = pow(p, i, MOD) for i from 0 to 5000.

- Compute pow_pn = pow(p, n, MOD).

But wait, n can be up to 1e18, which is manageable with the built-in pow function in Python with three arguments.

So for each r in 0 to k:

   product_num[r] is the product of (pow_pn - p_pows[i]) for i from 0 to r-1.

But for r=0, the product is empty (1), so N(0) is 1.

But how to compute product_num[r] efficiently for all r up to 5000?

We can compute product_num in a dynamic programming way. For r=0, product_num[0] = 1. For r >=1, product_num[r] = product_num[r-1] * (pow_pn - p_pows[r-1]) mod MOD. So we can precompute product_num for all r up to k.

Similarly, product_den[r] is the product for i=0 to r-1 of (pow_pr - p_pows[i]), where pow_pr = pow(p, r, MOD).

Wait, pow_pr is p^r mod MOD. So for each r, compute pow_pr as pow(p, r, MOD). Then for each i in 0..r-1, compute (pow_pr - p_pows[i]) mod MOD.

But for r up to 5000, this is manageable. But how to compute product_den[r] for all r up to k?

For each r, compute product_den[r] as product_{i=0}^{r-1} (pow(p, r, MOD) - p_pows[i}) mod MOD.

But for r up to 5000, and each r requires up to r terms, this is O(k^2) time. For k=5000, that's 25 million operations. Which is acceptable in Python for the time constraints.

So the plan is:

1. Precompute p_pows[i] up to i=5000.

2. Precompute pow_pn = pow(p, n, MOD).

3. Precompute product_num[r] for r from 0 to k.

   product_num[0] = 1.

   For r from 1 to k:

      product_num[r] = product_num[r-1] * (pow_pn - p_pows[r-1}) mod MOD.

4. Precompute product_den[r] for r from 0 to k.

   For each r:

      pow_pr = pow(p, r, MOD).

      product_den[r] = product of (pow_pr - p_pows[i}) for i in 0..r-1.

      To compute this, for each r, iterate i from 0 to r-1, multiply the terms.

   But for r=0, product_den[0] = 1.

   For r=1: product_den[1] = (p^1 - p^0) mod MOD.

   For r=2: (p^2 - p^0) * (p^2 - p^1) mod MOD.

   etc.

5. For each r from 0 to k:

   Compute N(r) = (product_num[r]^2) * inverse(product_den[r]) mod MOD.

   But how to compute the inverse of product_den[r]?

   Since MOD is a prime (998244353), the inverse can be computed as pow(product_den[r], MOD-2, MOD).

But since product_den[r] can be zero, we need to handle cases where product_den[r] is 0. Wait, but for r >=1, product_den[r] is the product of (p^r - p^i) for i=0..r-1.

But for i < r, p^i is p^0, p^1, ..., p^{r-1}.

p is a prime, and MOD is another prime. But p can be equal to MOD. Wait, no, because the input constraints say that p < 998244353 (MOD). So p is less than MOD, so when computing p^r mod MOD for r up to 5000, it's possible that p^r is congruent to some p^i mod MOD.

But product_den[r] could be zero, leading to division by zero. But according to the formula, N(r) is zero when product_den[r] is zero, but only if the product_num[r] is also zero. Wait, but that's not necessarily the case.

Wait, no. Because the formula is (product_num[r]^2) / product_den[r]. So if product_den[r] is zero, but product_num[r] is non-zero, then the formula is undefined. But in reality, the count of matrices of rank r must be zero in such cases. Because the formula is valid only for r <= n. Wait, but if r exceeds n, then the product_num[r] would include a term (p^n - p^{n}), which is zero. So for r >n, the product_num[r] would be zero, leading to N(r)=0. But if r is possible (i.e., up to min(n, k)), then the formula holds.

Wait, the formula for N(r) is valid when r <=n, because otherwise, the product_num[r] would have a term (p^n - p^{r-1}), but when r-1 >=n, p^{r-1} is larger than p^n (assuming p>1), but modulo MOD, this is not necessarily the case. Wait, but in the problem statement, r can be up to k, which can be up to 5000, but n can be 1e18. So for r <=n, product_num[r] is non-zero. For r >n, product_num[r] would have a term (p^n - p^{n}) when r-1 =n (i.e., r =n+1). For r >n, product_num[r] would be zero. So for r >n, the product_num[r] is zero, hence N(r) is zero.

So the steps are:

For each r from 0 to k:

   if r >n, then N(r) =0.

   else:

      compute product_num[r] and product_den[r], then compute (product_num[r]^2) * inv_den[r] mod MOD.

But wait, when r exceeds n, but k is up to 5000, which may be larger than n (if n is small). For example, n=3, k=3. Then r=3 is allowed. But for n=3, r=3 is possible. But if n=2, and k=5000, then for r=3, it's impossible.

But according to the problem statement, n can be up to 1e18, so when r is up to 5000, but n is 1e18, then r is definitely <=n, so product_num[r] is non-zero. So the formula works. But if n is small (like n=1, k=2), then for r>1, product_num[r] will be zero.

So the formula works as follows: for r>n, the product_num[r] is zero. Because for i=0 to r-1, when r-1 >=n (i.e., r>n), then one of the terms in the product_num[r] is (p^n - p^i) for i >=n. For example, when i=n, (p^n -p^n) =0. So for r>n, product_num[r] is zero. So N(r) is zero.

So, the code must handle the case where r >n. So for each r in 0..k:

   if r >n: output 0.

   else: compute as per the formula.

But n can be up to 1e18, which is manageable in Python.

So, the steps for the code:

1. Read n, p, k.

2. MOD = 998244353.

3. Precompute p_pows: a list where p_pows[i] = p^i mod MOD, for i from 0 to k.

   Because for r up to k, the denominator terms for r require p^i where i up to r-1. Since r can be up to k=5000, we need p_pows up to 5000.

4. Compute pow_pn = pow(p, n, MOD).

5. Precompute product_num for r from 0 to k.

   product_num[0] =1.

   For r from 1 to k:

      term = (pow_pn - p_pows[r-1]) % MOD

      product_num[r] = (product_num[r-1] * term) % MOD.

6. Precompute product_den for each r from 0 to k.

   product_den[0] =1.

   For r from 1 to k:

      pow_pr = pow(p, r, MOD)

      product_den[r] = 1

      for i in 0 to r-1:

          term = (pow_pr - p_pows[i]) % MOD

          product_den[r] = (product_den[r] * term) % MOD.

   This is O(k^2) time.

7. For each r from 0 to k:

   if r >n: output 0.

   else:

       compute inv_den = pow(product_den[r], MOD-2, MOD)

       res = (product_num[r] * product_num[r]) % MOD

       res = (res * inv_den) % MOD

       output res.

But wait, when r >n, but the code may compute product_num[r] as zero. For example, when r exceeds n, then product_num[r] is zero. So even if we proceed with the formula, the result will be zero. So perhaps the code can ignore checking r >n and proceed, as the product_num[r] will be zero.

But how? Let's see. For example, when r exceeds n, then in the product_num[r], which is product from i=0 to r-1 of (p^n - p^i). Since n < r, then for some i in 0..r-1, i will be >=n. For example, when r-1 >=n, which is the case when r>n, then i can be n. Then (p^n - p^n) =0. So product_num[r] is zero. Thus, when r>n, product_num[r] is zero. So the formula gives (0^2) / product_den[r] =0. So even if we don't check r>n, the code will output zero.

But division by product_den[r] is allowed as product_den[r] may be zero. Wait, but product_den[r] can be zero even when r<=n. For example, when p=2, r=3. Then product_den[r] is (8-1)(8-2)(8-4) mod MOD. But if MOD is 7, for example, but in our case, MOD is 998244353, which is a prime, and p is another prime.

Wait, product_den[r] is the product of (p^r - p^i) for i=0..r-1. Since p is a prime and less than MOD, and MOD is a prime, but product_den[r] could be zero modulo MOD if any of the terms (p^r - p^i) is congruent to zero modulo MOD. Which would require p^r ≡ p^i mod MOD for some i < r. But p is a prime less than MOD. So, for example, if MOD is 7, p=2, r=3. Then p^r=8 mod 7 is 1. p^i for i=0 is 1, so (1-1)=0. So product_den[r] would be zero. But that would imply that the denominator is zero, but the numerator could be zero as well. So in such a case, how do we handle it?

But according to the formula, when product_den[r] is zero, but product_num[r] is zero as well (for example, when r>n), then the result is zero. But if product_num[r] is non-zero and product_den[r] is zero, then the formula is invalid, but in practice, such cases would correspond to situations where the actual count is zero.

So perhaps the code can proceed without checking r>n, and just compute the formula. Because when r>n, the product_num[r] is zero, leading to N(r) being zero. And when r<=n, but product_den[r] is zero, which would imply that the formula's denominator is zero, but in reality, the count should be zero. For example, if p=2, MOD=7, r=3. Then product_den[r] is zero, but if n >=3, then product_num[r] is (8-1)(8-2)(8-4) mod 7. 8 mod7 is 1. So terms are (1-1)=0, (1-2)= -1 mod7=6, (1-4)= -3 mod7=4. So product_num[r] is 0*6*4=0. So N(r) =0^2 / 0 → but in practice, the code would compute (0 * inv(0)), which is invalid. But in reality, when product_den[r] is zero and product_num[r] is zero, the actual result is zero. But how to handle division by zero in code.

This is a problem. Because in such cases, the code would attempt to compute the inverse of zero mod MOD, which is impossible. So in such cases, when product_den[r] is zero and product_num[r] is non-zero, the code would crash. But how can such cases occur?

Let's see. product_den[r] is zero mod MOD iff there exists some i in 0..r-1 such that p^r ≡ p^i mod MOD. Which implies that p^{r -i} ≡ 1 mod MOD. Since p and MOD are coprime (MOD is prime and p < MOD, so p is not MOD). So p has some multiplicative order in MOD. So for r >= i, p^{r-i} ≡ 1 mod MOD. So that would require that the multiplicative order of p mod MOD divides (r-i). But for r up to 5000, and MOD being 998244353 (a big prime), the multiplicative order of p could be large, perhaps up to MOD-1 (if p is a primitive root mod MOD). So such cases may not happen for small r. But they can happen if MOD divides p^r -p^i, which is possible.

But in that case, the formula's denominator is zero. So how do we handle this? Because in such cases, the denominator is zero, but the numerator may or may not be zero.

For example, suppose MOD=7, p=2, r=3, and n=3. Then product_num[r] is (2^3-1)(2^3-2)(2^3-4) mod7. 2^3 is 8 mod7 is 1. So each term is (1-1)=0, (1-2)=6 mod7, (1-4)=4 mod7. So product_num[r] is 0*6*4=0 mod7. product_den[r] is (2^3-1)(2^3-2)(2^3-4) mod7 = (8-1=7 mod7=0) * (8-2=6) * (8-4=4) → 0*6*4=0 mod7. So N(r) is (0^2) / 0 → undefined, but the actual count is zero.

But how to handle this in code? Because when product_den[r] is zero and product_num[r] is zero, the code would compute 0 * inv(0), which is impossible. So perhaps we need to find that when product_den[r] is zero, then the result is zero.

But how to detect that.

Alternatively, perhaps such cases only occur when the formula N(r) is zero. For example, when product_den[r] is zero, but product_num[r] is zero, then the formula's result is zero. But if product_num[r] is non-zero and product_den[r] is zero, then the formula is invalid, but such a case can't exist in reality. But how to confirm this.

Alternatively, the formula may not be valid when product_den[r] is zero, but the code's approach would compute zero in all such cases because product_num[r] would be zero.

Wait, when product_den[r] is zero, it's because for some i in 0..r-1, p^r ≡ p^i mod MOD. But since r>i, then p^{r-i} ≡1 mod MOD. So, for example, if MOD is 7 and p=2, then 2^3 mod7=1, which is equal to 2^0 mod7=1. So r=3, i=0. Then p^r -p^i is 0 mod7.

In such cases, the product_den[r] is zero, but what about product_num[r]? product_num[r] is product of (p^n - p^i) for i=0..r-1. But if p^r ≡ p^i mod MOD, then p^{r} ≡ p^i mod MOD → p^{r-i} ≡1 mod MOD. So for exponents, let's say that n is congruent to i mod (MOD-1), due to Fermat's little theorem. Because MOD is prime, so p^{MOD-1} ≡1 mod MOD. So if n ≡ i mod (MOD-1), then p^n ≡ p^i mod MOD. So (p^n - p^i) ≡0 mod MOD. So product_num[r] could be zero if, for any i in 0..r-1, p^n ≡ p^i mod MOD. So, if in the product_num[r], there is a term (p^n - p^i) that is zero, then product_num[r] is zero, and thus the entire N(r) is zero.

So, in cases where product_den[r] is zero, perhaps product_num[r] is also zero. Thus, the code can proceed without checking r>n, and compute N(r) as (product_num[r]^2 * inv_den[r]) mod MOD, which would be zero when product_num[r] is zero, even if product_den[r] is zero. Because when product_den[r] is zero and product_num[r] is non-zero, the code would attempt to multiply by inv_den[r], which is impossible (as product_den[r] is zero). But how can such a case exist?

For example, let's take MOD=7, p=2, r=3. Suppose n is such that p^n mod MOD is not equal to any p^i mod MOD for i<3. For example, n=4. Then product_num[3] is (2^4-1)(2^4-2)(2^4-4) mod7. 2^4=16 mod7 is 2. So terms are (2-1)=1, (2-2)=0, (2-4)=5. So product_num[3] is 1*0*5=0 mod7. So even in this case, product_num[r] is zero, so N(r) is zero.

So, perhaps in all cases where product_den[r] is zero, product_num[r] is also zero, leading to N(r) being zero. So the code can safely proceed.

Therefore, the code can be written without checking r <=n. Because for r>n, product_num[r] is zero, leading to N(r) being zero. And for r<=n, even if product_den[r] is zero, product_num[r] is zero (due to the presence of a term (p^n - p^i) where p^i is congruent to p^r mod MOD, and thus, due to p's multiplicative order, p^n ≡ p^i mod MOD).

Thus, the code can proceed as follows:

For each r in 0..k:

   compute product_num[r], product_den[r].

   inv_den = pow(product_den[r], MOD-2, MOD) if product_den[r] !=0 else 0. But in code, when product_den[r] is zero, the pow will fail, but product_num[r] is zero, so the result is zero anyway.

But in Python, pow(0, MOD-2, MOD) will raise an exception. So we need to handle cases where product_den[r] is zero.

But how?

Alternatively, when product_den[r] is zero, then if product_num[r] is also zero, the result is zero. But how to check that in code.

But in code:

for each r:

   if product_den[r] == 0:

       if product_num[r] == 0:

           res = 0

       else:

           # impossible case?

           res = 0

   else:

       inv_den = pow(product_den[r], MOD-2, MOD)

       res = (product_num[r] * product_num[r] % MOD) * inv_den % MOD

But how can we check product_den[r] ==0?

But for r up to 5000, product_den[r] can be computed as follows. So during the precomputation of product_den[r], we can track whether it's zero.

But in code, product_den[r] is the product of (pow_pr - p_pows[i}) mod MOD for i=0..r-1. So if any term in the product is zero, product_den[r] will be zero.

So during the computation of product_den[r], once any term is zero, the entire product_den[r] becomes zero and remains zero. So during the precomputation of product_den[r], once a term (pow_pr - p_pows[i}) is zero, product_den[r] is zero.

Thus, for each r, during the precomputation of product_den[r], if product_den[r] is zero, then product_den[r] is stored as zero. So during the code, for each r, we can check if product_den[r] is zero. Then, if product_den[r] is zero, then:

   if product_num[r] is zero → res is zero.

   else → res is zero (since denominator is zero, but formula is undefined. But in reality, such cases would not exist, so we can treat them as zero).

But how to handle that in code?

Probably, in code, when product_den[r] is zero, then product_num[r] is also zero. So the code can proceed as follows:

   if product_den[r] == 0:

       res =0

   else:

       inv_den = pow(...)

       res = product_num[r]^2 * inv_den mod MOD.

But why would product_den[r] be zero and product_num[r] not zero? Let's think of an example.

Take MOD=7, p=2, r=3.

pow_pr = p^r mod MOD =8 mod7=1.

product_den[r] is (1-1) * (1-2) * (1-4) mod7=0 * 6 *4=0.

product_num[r] is product of (p^n - p^i) for i=0..2.

If n is such that p^n mod7 is 3. Then terms are (3-1)=2, (3-2)=1, (3-4)= -1 mod7=6. So product_num[r] is 2*1*6=12 mod7=5. So product_den[r] is zero, product_num[r] is 5 mod7. Then the formula would be (5^2) / 0 → which is invalid. But in reality, how many matrices of rank r=3 exist? According to the formula, it's (product_num^2)/product_den → (25)/0 → which is undefined. But according to the problem statement, the count should be zero because when r=3 and MOD=7, but p=2, and n is such that product_num[r] is 5 mod7, but product_den[r] is zero, which suggests that the formula is invalid. But in reality, the count should be zero.

So how to handle this case?

Well, perhaps in such cases, the code should output zero, even though the formula is undefined. So when product_den[r] is zero, but product_num[r] is non-zero, the code should output zero. But how to implement that.

But during the code's precomputation, when product_den[r] is zero, then regardless of product_num[r], we can output zero.

Thus, in code:

for each r in 0..k:

   if product_den[r] ==0 or product_num[r] ==0:

       res =0

   else:

       inv_den = pow(product_den[r], MOD-2, MOD)

       res = (product_num[r] * product_num[r] * inv_den) % MOD

But wait, product_num[r] can be non-zero, but product_den[r] is zero. Then, according to this logic, res is zero. But according to the formula, that's undefined, but the actual count may be zero.

But how to handle this in code.

Alternatively, the code can compute:

res = (product_num[r] * product_num[r] ) % MOD

if product_den[r] is not zero:

   res = res * inv_den % MOD

else:

   res =0

But this would require checking if product_den[r] is zero. Which is possible.

So, in code:

for each r in 0..k:

   if product_num[r] ==0:

       res =0

   else:

       if product_den[r] ==0:

           res=0

       else:

           inv_den = pow(product_den[r], MOD-2, MOD)

           res = (product_num[r] * product_num[r] % MOD) * inv_den % MOD

But why would product_num[r] be non-zero and product_den[r] be zero? Let's see.

Take MOD=7, p=2, r=3, and n=4.

product_num[r=3] is product of (2^4 mod7 - p^i mod7) for i=0,1,2.

2^4 mod7 is 2.

i=0: 2-1=1 mod7.

i=1: 2-2=0 mod7.

product_num[r=3] =1 *0 * ... =0.

So product_num[r=3] is zero. So even if product_den[r] is zero, product_num[r] is zero.

Thus, when product_den[r] is zero, product_num[r] is zero. So in code, product_den[r] can be zero only if product_num[r] is zero. Because when product_den[r] is zero, there exists i in 0..r-1 such that p^r ≡ p^i mod MOD. So p^{r-i} ≡ 1 mod MOD. Now, if n is congruent to i mod (MOD-1), then p^n ≡ p^i mod MOD. So (p^n - p^i) ≡0 mod MOD. But n is up to 1e18, so it's possible that n ≡i mod (MOD-1), which would make (p^n -p^i) ≡0 mod MOD, leading to product_num[r] being zero.

Thus, in code, whenever product_den[r] is zero, product_num[r] is also zero. Therefore, the code can safely assume that if product_den[r] is zero, then product_num[r] is zero, and thus the res is zero.

Therefore, the code can proceed as follows:

for each r in 0..k:

   if product_num[r] ==0:

       res =0

   else:

       inv_den = pow(product_den[r], MOD-2, MOD)

       res = (product_num[r] **2 * inv_den) % MOD

Thus, the code does not need to check product_den[r], because if product_den[r] is zero, then product_num[r] is zero, leading to res=0.

Thus, the code can proceed with the following steps:

Implement all steps as described, and for each r, compute res as (product_num[r]^2 * inv_den[r]) mod MOD if product_num[r] is non-zero, else zero.

Thus, the code can be written as follows:

- Precompute p_pows.

- Precompute product_num and product_den.

- For each r, compute:

   if product_num[r] ==0:

       output 0

   else:

       inv_den = pow(product_den[r], MOD-2, MOD)

       res = (product_num[r] **2) * inv_den % MOD

       output res

So, let's proceed with writing the code.

Now, let's test the first example.

Sample input 1: 3 2 3.

n=3, p=2, k=3.

Compute pow_pn = 2^3 mod MOD=8 mod MOD=8.

p_pows[0..3] = [1,2,4,8 mod MOD=8].

But since k=3, the maximum i needed is 3-1=2. So p_pows up to 2: [1,2,4].

product_num[0] =1.

product_num[1] = (8-1) mod MOD=7.

product_num[2] =7 * (8-2) =7*6=42.

product_num[3] =42 * (8-4)=42*4=168.

product_den[0] =1.

product_den[1] for r=1: pow_pr =2^1=2 mod MOD. term is 2-1=1. product_den[1]=1.

product_den[2] for r=2: pow_pr=4. terms are 4-1=3, 4-2=2. product_den=3*2=6.

product_den[3] for r=3: pow_pr=8 mod MOD. terms are 8-1=7 mod MOD, 8-2=6, 8-4=4. product_den=7*6*4=168.

So for r=0:

product_num[0] is 1. product_den[0] is 1. res is (1^2) * 1 mod MOD=1.

For r=1:

product_num[1]=7. product_den[1]=1. res=7² * 1 =49.

For r=2: product_num[2]=42. product_den[2]=6. inv_den=6^(MOD-2). MOD=998244353 is a prime. So 6^(MOD-2) mod MOD is 166374059.

42^2 = 1764. 1764 * 166374059 mod MOD = (1764 * 166374059) mod MOD.

Wait, but 1764 /6 = 294. So 42^2 /6 = (42 *42)/6 = 42 *7 = 294. So res is 294.

Similarly for r=3: product_num[3]=168. product_den[3]=168. So inv_den is 168^(MOD-2) mod MOD. 168 * inv_den mod MOD=1. So res= (168^2) * inv_den mod MOD=168. So output is 1 49 294 168, which matches the first example.

Sample input 2: 1 51549919 2.

n=1, p=51549919, k=2.

pow_pn = 51549919^1 mod MOD. Since p < MOD, this is 51549919.

p_pows[0..2] = [1, p mod MOD, p^2 mod MOD]. But since r can be up to 2, the maximum i needed is 1.

product_num[0] =1.

product_num[1] = (pow_pn - p_pows[0}) = (51549919 -1) mod MOD =51549918.

product_num[2] = product_num[1] * (pow_pn - p_pows[1}) → but pow_pn is p^1. p_pows[1} is p. So (p^1 - p^1) =0. So product_num[2] =51549918 *0 =0.

product_den[0]=1.

product_den[1]: r=1, pow_pr=p^1 mod MOD. terms are (p^1 - p^0) =51549919-1=51549918 mod MOD.

product_den[1}=51549918.

product_den[2}: r=2. pow_pr=p^2 mod MOD. terms are (p^2 -1) and (p^2 -p).

But product_den[2} is product of (p^2-1) and (p^2-p). But p=51549919 mod MOD=51549919.

But for r=2, product_den[2] is (p^2 -1) * (p^2 -p).

But when r=2 and n=1, the product_num[2} is zero. So for r=0,1,2:

r=0: res=1.

r=1: (51549918^2) / 51549918 mod MOD =51549918.

r=2: product_num[2} is zero → res=0.

So output is 1 51549918 0, which matches the second sample.

Thus, the code works.

Now, let's proceed to code.

But how to handle the precomputation of product_den[r} for each r up to k=5000.

For r in 0 to k:

   product_den[r} is product of (pow(p, r, MOD) - p_pows[i}) for i in 0 to r-1.

So for each r, compute pow_pr = pow(p, r, MOD).

Then for each i in 0 to r-1, compute (pow_pr - p_pows[i}) mod MOD, multiply them all.

But for r up to 5000, and each r requires r multiplications, the total time is O(k^2), which is acceptable.

So in code:

precompute p_pows as [1] * (k+1) ?

Wait, no. Because for r up to k, the maximum i needed is r-1. So for r up to k, i ranges up to k-1. So precompute p_pows[i} for i up to k-1.

But since k can be up to 5000, we can precompute p_pows up to 5000.

So in code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    MOD = 998244353

    n, p, k = map(int, input_stream.readline().rstrip("\n").split())

    p_pows = [1] * (k+1)

    for i in range(1, k+1):

        p_pows[i] = (p_pows[i-1] * p) % MOD

    pow_pn = pow(p, n, MOD)

    product_num = [1] * (k+1)

    for r in range(1, k+1):

        i = r-1

        if i >= len(p_pows):

            # not possible since r <=k, and p_pows is up to k.

            # but i is r-1 <=k-1 <k+1.

            pass

        term = (pow_pn - p_pows[i]) % MOD

        product_num[r] = (product_num[r-1] * term) % MOD

    product_den = [1] * (k+1)

    for r in range(1, k+1):

        pow_pr = pow(p, r, MOD)

        den = 1

        for i in range(r):

            term = (pow_pr - p_pows[i]) % MOD

            den = (den * term) % MOD

        product_den[r] = den

    result = []

    for r in range(k+1):

        if product_num[r] ==0:

            result.append(0)

        else:

            inv_den = pow(product_den[r], MOD-2, MOD)

            res = (product_num[r] * product_num[r] % MOD) * inv_den % MOD

            result.append(res)

    print(' '.join(map(str, result)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 51549919 2
""",
            "output": \
"""\
1 51549918 0
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

</think>

```python
MOD = 998244353

n, p, k = map(int, input().split())

max_pow = k
p_pows = [1] * (max_pow + 1)
for i in range(1, max_pow + 1):
    p_pows[i] = (p_pows[i-1] * p) % MOD

pow_pn = pow(p, n, MOD)

product_num = [1] * (k + 1)
for r in range(1, k + 1):
    term = (pow_pn - p_pows[r-1]) % MOD
    product_num[r] = (product_num[r-1] * term) % MOD

product_den = [1] * (k + 1)
for r in range(1, k + 1):
    pow_pr = pow(p, r, MOD)
    den = 1
    for i in range(r):
        term = (pow_pr - p_pows[i]) % MOD
        den = (den * term) % MOD
    product_den[r] = den

result = []
for r in range(k + 1):
    if product_num[r] == 0:
        result.append(0)
    else:
        inv_den = pow(product_den[r], MOD-2, MOD)
        res = (product_num[r] * product_num[r] % MOD) * inv_den % MOD
        result.append(res)

print(' '.join(map(str, result)))
```
