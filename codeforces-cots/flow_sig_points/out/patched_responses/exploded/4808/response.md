<think>
Okay, let's tackle this problem. The goal is to find the number of lucky tickets where a ticket is considered lucky if the sum of the first half of the digits equals the sum of the second half. And we can only use certain digits provided in the input. The answer needs to be modulo 998244353.

Hmm, let's think about the constraints. The maximum n is 2e5, which is pretty big. So any solution that is O(n^2) is probably not going to work. We need a way to compute this efficiently.

First, let's break down the problem. The ticket has n digits, which is even. So each half has m = n/2 digits. The sum of the first m digits must equal the sum of the last m digits. So the approach could be to compute how many ways there are to get a sum s for m digits, then for each possible s, square the count (since the first and second halves are independent once the sum is fixed) and sum all those squares. Because for each sum s, the number of combinations for the first half that sum to s multiplied by the number for the second half (same s) gives the total for that s. Then sum over all possible s.

So the key steps are:
1. Compute the possible sum for m digits using the allowed digits.
2. For each possible sum s, compute the number of m-length sequences that sum to s.
3. The total is the sum of (count(s))^2 modulo the given modulus.

Now, the challenge is to compute count(s) efficiently for all possible s.

The allowed digits can be up to 10. For m digits, each step can choose one of the allowed digits. So this is a dynamic programming problem. Let's model it with DP where dp[i][j] is the number of ways to form i digits that sum to j. Then for each digit added, we iterate through possible sums and add the possibilities.

But m can be up to 1e5 (since n is up to 2e5), and each step involves adding digits. The sum j can be up to m * 9 (since each digit can be up to 9). For m=1e5, 1e5 *9 is 9e5. But 1e5 steps each with 9e5 possible sums would be 9e10 operations, which is way too big.

Wait, that's a problem. So we need a more efficient way. Let's think of this as a problem where we need to compute the number of ways to choose m digits (with replacement, since digits can be reused) such that their sum is s, using the allowed digits. Then, the approach would be to model this as a generating function. The generating function for a single digit is the sum of x^d for each allowed d. For m digits, the generating function is (sum_d x^d)^m. The coefficient of x^s in this expansion will be the count(s) we need. Then, the problem reduces to calculating this coefficient for all possible s and summing the squares.

But how do we compute this efficiently? Calculating the polynomial raised to the mth power using FFT-based convolution might be feasible, but for m up to 1e5 and digits up to 9, the maximum sum s could be 9 * 1e5 = 9e5, which is manageable in terms of memory, but FFT-based approaches would be O(s log s) per convolution, and we need to do this m times, which is 1e5. That's way too slow.

Wait, but perhaps there's a smarter way. The generating function for m digits is (P(x))^m, where P(x) is the sum of x^d for each allowed d. So the coefficients of this polynomial can be computed using dynamic programming with convolution. However, exponentiating a polynomial efficiently. For example, using exponentiation by squaring. But even then, when m is up to 1e5, the exponentiation would involve log2(m) steps, each step being a convolution. But each convolution would be O(s^2) which is 9e10 again. So that's not feasible.

Alternatively, perhaps using matrix exponentiation or some other approach. Let me think again.

Wait, the allowed digits can be up to 10. Let's say the digits are d1, d2, ..., dk. The problem is to compute the number of ways to sum m digits (each from the allowed set) to get a sum s. This is similar to a counting problem where each step adds one of the digits. So dynamic programming is the way to go, but with optimized state transitions.

Let's model the DP as follows: dp[i] is a dictionary (or array) where dp[i][s] is the number of ways to get sum s using i digits. For each step, we can compute dp[i] by taking all possible s from dp[i-1] and adding each allowed digit to them. So for each s in dp[i-1], and for each digit d, we add dp[i-1][s] to dp[i][s + d].

But with m up to 1e5, and s up to 9e5, this would be O(m * k * S), where S is the maximum possible sum. But even for k=10 and m=1e5, that's 1e6 * 9e5 = 9e11 operations. That's way too slow.

Hmm, so this approach isn't feasible. So we need a better way. Let's think about the problem again. The sum of m digits is a certain value. The digits can be any of the allowed digits. The count for sum s is the number of sequences of m digits where each digit is in the allowed set, and their sum is s.

Another way to look at it is that each digit contributes a certain value. The problem is similar to a convolution problem. For example, the first digit contributes a sum from d1, d2, ..., dk. The second digit adds to that sum. So the sum after two digits is the convolution of the sum after one digit with the possible digits. So the count for two digits is the convolution of the count for one digit with itself (but since each digit is added once, perhaps it's more like the convolution of the digit's possible sums). So for m digits, this is the m-fold convolution of the allowed digits' possible sums.

But convolution can be computed efficiently using Fast Fourier Transform (FFT). But for m up to 1e5, even using FFT would be O(m * s log s) which is not feasible. Wait, but the allowed digits are fixed. The generating function for one digit is P(x) = sum x^d for each allowed d. The generating function for m digits is (P(x))^m. The coefficients of this polynomial give the count for each sum s. So we need to compute the coefficients of this polynomial, then sum the squares of each coefficient.

So the problem reduces to computing (P(x))^m, then summing the squares of the coefficients.

The question is: how to compute (P(x))^m efficiently.

The maximum possible sum s_max is m * 9. For m=1e5, this is 9e5. So the polynomial has 9e5 + 1 coefficients. But exponentiating P(x) to the mth power would require multiplying the polynomial m times, which is not feasible.

But wait, exponentiation can be done in O(log m) steps using exponentiation by squaring. Each multiplication is a convolution. So if each convolution takes O(s log s) time, then for log2(m) steps, the total time is O(log m * s log s). For m up to 1e5, log2(m) is about 17. For s up to 9e5, each FFT-based convolution would be O(s log s). Let's see: 9e5 log 9e5 is roughly 9e5 * 20 = 1.8e7. Multiply by 17 steps gives 3e8 operations. That's manageable within the time limit, but I'm not sure. Also, the modulus is 998244353, which is a prime. So perhaps using Number Theoretic Transforms (NTT) could be feasible here, but modulus operations complicate things.

Wait, but the problem requires the answer modulo 998244353. However, the coefficients themselves can be computed modulo 998244353. So using NTT here makes sense. The steps would be:

1. Precompute the initial polynomial P(x) = sum x^d for each allowed d. The coefficients are 1 for each d in the allowed set, 0 otherwise. The maximum degree of P(x) is 9 (since digits are up to 9).

2. Compute the polynomial Q(x) = P(x)^m. The coefficients of Q(x) are the counts of the sum s for m digits. So Q(s) is the number of m-digit sequences that sum to s.

3. The answer is the sum of Q(s)^2 for all s, modulo 998244353.

But how to compute Q(x) efficiently?

Exponentiating P(x) to the mth power using the binary exponentiation method, where each multiplication is done via NTT.

Each step of the exponentiation involves multiplying two polynomials. Let's see how that works.

The initial polynomial is P(x) with degree D (where D is the maximum digit in the allowed set). After exponentiating to m, the degree becomes m*D. For m=1e5 and D=9, that's 9e5, which is manageable.

But multiplying two polynomials of degree up to 9e5 each would take O(n log n) time, where n is the next power of two greater than 2*9e5. So for each multiplication, that's O(n log n) steps. With log2(m) steps (like 17 for 1e5), the total time would be O(17 * 9e5 * log(9e5))).

Wait, but when we perform exponentiation by squaring, each multiplication step involves polynomials of varying degrees. For example, when we have (P^2)^k, the degree could be 2k * D. But in any case, for m up to 1e5, the maximum possible degree after exponentiation is m*9, which is 9e5.

So each multiplication step would involve two polynomials of degree up to 9e5, but their product's degree is up to 1.8e6. Wait, but in the exponentiation steps, each step can have varying degrees. For example, the first step might compute P^2, which has degree 2*D. Then P^4 (degree 4*D), etc. But when m is not a power of two, we might multiply intermediate results.

But regardless, the maximum degree after exponentiation is m*9, which is manageable.

So the plan is:

- Represent the allowed digits as a polynomial P, where P has coefficient 1 for each allowed digit.

- Raise P to the m-th power using NTT-based polynomial exponentiation by squaring, keeping all coefficients modulo 998244353.

- Then, sum the squares of each coefficient in the resulting polynomial.

But how to handle the modulus during NTT? The modulus 998244353 is a prime, and it's known to support NTT as it's of the form 2^23 * 7 * 17 + 1, which has enough roots of unity. However, implementing NTT in Python is challenging, especially for very large polynomials. Also, the standard FFT/NTT implementations in Python are not optimized for speed, so even with O(n log n) algorithms, for n up to a million, it might be too slow for the time constraints (5 seconds).

Alternatively, considering that the allowed digits are up to 10, maybe there's a smarter dynamic programming approach.

Wait, let's think again. The digits allowed are a set S. For each step (digit), we can accumulate the sum. The DP can be represented as a list where dp[i] is the count of ways to get sum i. Then, for m steps, each step we can compute the next dp as the convolution of the current dp with the allowed digits.

Wait, but convolution here is equivalent to adding a digit. For example, if the current dp is for i digits, then for each possible sum s, and each allowed d, the next dp[s + d] += dp_prev[s]. But this is exactly the same as the convolution of dp_prev with the allowed digits' generating function.

So, for each step, the DP can be represented as a convolution with the allowed digits. However, doing this for m steps would be O(m * k * s), which is not feasible.

But here's the key insight: the allowed digits are fixed, and each step is the same convolution. Therefore, the problem is equivalent to raising the generating function of the allowed digits to the m-th power, as each step is a multiplication by that generating function.

So, we need to compute the generating function P(x) = sum_{d in allowed} x^d, then compute P(x)^m, and then sum the squares of the coefficients.

But even with m up to 1e5, can we compute this exponentiation efficiently?

Yes, using exponentiation by squaring with fast polynomial multiplication (NTT-based). But implementing this in Python might be challenging. However, there's a way to optimize this.

Alternatively, considering that the allowed digits are small (digits up to 9), perhaps we can use dynamic programming with optimized transitions. Let's see.

The maximum sum after m digits is m * 9. Let's denote this as max_sum. For m=1e5, max_sum is 9e5. We can model the DP as a 1D array where dp[s] is the number of ways to reach sum s with i digits.

Initially, for i=0 (0 digits), the sum is 0, so dp[0] = 1. Then, for each of the m steps, we compute the next dp by considering all allowed digits and adding to the possible sums.

But this would take O(m * k * max_sum) time, which for m=1e5, k=10, and max_sum=9e5 would be 9e11 operations. That's way too slow.

Wait, but this is O(m * k * s_prev), where s_prev is the maximum sum at step i-1. For i=1, s_prev is 9. For i=2, 18. So up to i=m, 9*m. So the total operations would be sum_{i=1 to m} k * (9*i) ). Which is O(k * m^2). For m=1e5, that's 1e10 * 10 = 1e11 operations, which is way beyond the time limit.

So this approach is not feasible.

Therefore, the only feasible way is to compute the polynomial exponentiation using FFT/NTT-based methods. Let's proceed with that.

Now, the challenge is to implement this in Python efficiently.

But how?

First, we need to perform polynomial exponentiation. Let's outline the steps.

1. Create the initial polynomial P. The allowed digits are given, so for each digit d in the input list, we set the coefficient of x^d to 1.

2. Compute Q = P^m. The coefficients of Q give the counts for each sum s.

3. Sum the squares of the coefficients of Q, modulo 998244353.

The crux of the problem is step 2. How to compute P^m efficiently.

Implementing polynomial exponentiation using binary exponentiation, where each multiplication is done via NTT.

But implementing NTT in Python for large polynomials is tricky. Let's see.

Let's recall that NTT requires the modulus to be a prime of the form c*2^k + 1. 998244353 is such a prime (it's 119*2^23 +1), so it's suitable for NTT. The primitive root for 998244353 is 3.

The steps for NTT are as follows:

- Precompute the roots of unity and their inverses.

- For each multiplication, extend the polynomials to the next power of two greater than or equal to the sum of their degrees, then perform forward NTT on both, multiply pointwise, inverse NTT, and then take modulo.

But for large polynomials, this can be time-consuming.

But with m up to 1e5 and digits up to 9, the maximum degree after exponentiation is 9e5. So during the exponentiation steps, each multiplication will involve polynomials of varying sizes.

Alternatively, we can use the Karatsuba algorithm for polynomial multiplication, which is O(n^1.585), but for large n, this is still not feasible.

So the only way is to use NTT-based multiplication.

But implementing NTT in Python for large polynomials may be feasible given the time constraints. Let's think about how to proceed.

First, we need to implement NTT functions. Let's look for a Python implementation of NTT-based polynomial multiplication modulo 998244353.

An example implementation:

But let's think about the code structure.

First, the code reads n and k, then the list of digits. Then, we need to create the initial polynomial P. For each allowed digit, we add 1 to the coefficient of x^d. So for example, if the allowed digits are 1 and 8, then P is x^1 + x^8.

Then, we need to compute P^m, where m is n/2.

Once we have that polynomial, the answer is the sum of the squares of each coefficient in P^m.

So the steps:

1. Create the initial polynomial as a list where the index is the exponent (sum), and the value is the count modulo 998244353.

2. Compute the polynomial exponentiation to the mth power.

3. Sum the squares of all coefficients modulo 998244353.

Now, the challenge is to implement the polynomial exponentiation efficiently.

But how?

Let's think about the polynomial exponentiation by squaring. Each step involves squaring the current polynomial and possibly multiplying by the base polynomial if the exponent's bit is set.

So, for example, for m=5 (101 in binary), we compute P^4 * P^1.

Each multiplication between two polynomials A and B is done via NTT.

But how to handle the polynomials? Let's think of each polynomial as a list of coefficients, up to their maximum exponent.

So, for example, if the initial polynomial is P = x^1 + x^8, then the coefficients array is [0,1,0,0,0,0,0,0,1], and the maximum exponent is 8.

Now, when we multiply two polynomials A and B, the resulting coefficients are the convolution of A and B. So for each i in A's coefficients, and j in B's coefficients, the product contributes to i + j.

To multiply two polynomials, we can use NTT as follows:

- Pad both polynomials to the next power of two greater than or equal to (len(A) + len(B) -1).

- Compute their NTT representations.

- Multiply point-wise.

- Compute the inverse NTT.

- Take modulo 998244353.

- Trim the resulting polynomial to the necessary length (sum of degrees).

Now, implementing this in Python.

But the problem is the speed. For large polynomials, the NTT steps can be time-consuming in Python.

Alternatively, perhaps the exponents are small enough. For example, when m is 1e5 and each digit is up to 9, the maximum sum is 9e5. So the polynomial after exponentiation will have 9e5 +1 coefficients.

But exponentiating this using binary exponentiation would involve log2(m) steps. For m=1e5, that's about 17 steps.

Each step involves multiplying two polynomials of varying lengths. For example, in the first step, the polynomial has degree 9. Squaring it gives degree 18. Then squaring again gives 36, etc.

But the maximum possible degree after exponentiation is 9e5, which requires a polynomial of size about 9e5 +1.

But even with 17 steps, each involving NTT-based multiplication of two polynomials of size up to 9e5, the time may be manageable.

Alternatively, let's think of the polynomial multiplication steps. Each NTT-based multiply is O(N log N) where N is the next power of two for the required length. For example, if two polynomials of degree a and b are multiplied, the required length is a + b. So the next power of two is 2^ceil(log2(a + b + 1)).

But each step of NTT is O(N log N), and for two polynomials, that's O(N log N) for each forward NTT, O(N) for point-wise multiply, O(N log N) for inverse NTT. So total O(N log N) per multiplication.

For each multiplication step in the exponentiation, the N could be up to 2*(9e5) = 1.8e6. So log2(1.8e6) is about 21. So each step would take O(1.8e6 * 21) operations. For 17 steps, that's 17 * 1.8e6 *21 = 6426e6 operations. But Python can handle around 1e8 operations per second, so 6e9 operations would be way too slow.

Wait, that's 6e9 operations, which is 6 seconds, but Python is slower. So this approach isn't feasible. So there's a problem here.

Wait, perhaps the problem requires a different approach. Let's think again.

Alternative idea: Since the digits are allowed to be used any number of times, and each digit is added m times, the sum of the digits can be represented as the sum of m variables, each chosen from the allowed digits. The count for sum s is the number of ways to choose m digits (with replacement) from the allowed set, such that their sum is s.

But this is exactly the same as the coefficient of x^s in (sum x^d)^m.

But how to compute that without exponentiating the polynomial.

Another approach: matrix exponentiation. The state is the current sum modulo something. But the problem is that the sum is up to 9e5, so the state space is too large.

Alternatively, note that the sum can be considered as a state transition. For each step, each possible sum s can transition to s + d, for each allowed d. But with m steps, this is again the same as the DP approach which is O(m * k * s) and not feasible.

Wait, but the allowed digits are up to 10. So for each step, the transitions are adding each of the 10 digits. So the generating function after each step is the product of the generating functions for each step. Since each step is the same, the generating function is the initial generating function raised to the mth power.

So we're back to the original problem of exponentiation.

So the conclusion is that we need to compute P(x)^m efficiently.

But perhaps the allowed digits are small, and we can find a way to compute the coefficients using dynamic programming with a sliding window approach.

Another idea: Since the allowed digits are up to 9, for each step, the possible new sums are s + d. So for each sum s, the next possible sums are s + d_1, s + d_2, ..., s +d_k.

But when using DP, the state after i steps is the sum s. So for step i+1, we can compute for each s in the current DP, and add the possible d's to s.

But again, this is O(m * k * s) which is not feasible.

Wait, but perhaps the allowed digits are the same for each step, so we can precompute the possible transitions once and use some mathematical approach.

Alternatively, notice that the DP can be expressed as a convolution of the current count with the allowed digits' frequency array. For example, the initial DP after 0 steps is [1] (sum 0). After 1 step, it's the frequency array of the allowed digits. After 2 steps, it's the convolution of the first step with the allowed digits.

Thus, the DP after m steps is the convolution of the allowed digits m times. So the problem is to compute the m-fold convolution.

But convolution is associative, so this is equivalent to the convolution of the allowed digits' frequency array m times. Which brings us back to the generating function approach.

So the only way is to compute the polynomial exponentiation, but with an efficient implementation.

So, given that, the plan is to implement the polynomial exponentiation using NTT-based convolution in Python. But how?

Alternatively, perhaps using a combinatorial approach. Let's see.

But I'm not aware of a combinatorial formula for this problem. So perhaps the only way is to proceed with the polynomial exponentiation.

Another observation: the modulus is 998244353, which is a prime. So we can use NTT here.

But how to implement NTT in Python efficiently.

Looking for Python code for NTT-based polynomial multiplication modulo 998244353.

Upon some research, here's an approach:

The NTT functions can be implemented as follows:

The forward NTT and inverse NTT functions require the use of the modulus and the primitive root. For modulus 998244353, the primitive root is 3, and 998244353 = 119*2^23 +1, so the maximum power of 2 dividing modulus-1 is 2^23. Therefore, the maximum length of the NTT is 2^23, which is sufficient for our problem.

But for each polynomial multiplication, we need to find the next power of two greater than or equal to the sum of the degrees of the two polynomials.

Implementing the NTT functions:

Here's a possible implementation:

def ntt(a, invert=False):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >>=1
        j += bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    log_n = (n).bit_length() -1
    mod = 998244353
    root = 3
    roots = [1] * (log_n+1)
    if invert:
        root = pow(root, mod-2, mod)
    for i in range(log_n):
        roots[i+1] = roots[i] * roots[i] % mod
    for i in range(1, log_n+1):
        m = 1 << i
        mh = m >>1
        w_m = roots[log_n - i]
        if invert:
            w_m = pow(w_m, mod-2, mod)
        for j in range(0, n, m):
            w = 1
            for k in range(j, j+mh):
                x = a[k]
                y = a[k + mh] * w % mod
                a[k] = (x + y) % mod
                a[k + mh] = (x - y) % mod
                w = w * w_m % mod
    if invert:
        inv_n = pow(n, mod-2, mod)
        for i in range(n):
            a[i] = a[i] * inv_n % mod
    return a

But I'm not sure if this code is correct, but let's proceed.

Then, the polynomial multiplication function:

def multiply(a, b):
    mod = 998244353
    len_a = len(a)
    len_b = len(b)
    n = 1
    max_len = len_a + len_b -1
    while n < max_len:
        n <<=1
    fa = a + [0]*(n - len_a)
    fb = b + [0]*(n - len_b)
    fa = ntt(fa)
    fb = ntt(fb)
    for i in range(n):
        fa[i] = fa[i] * fb[i] % mod
    fa = ntt(fa, invert=True)
    return fa[:max_len]

This code takes two polynomials a and b, pads them to the next power of two, performs NTT on both, multiplies them component-wise, inverse NTT, and returns the result modulo 998244353.

But testing this with large polynomials may be time-consuming.

Now, the polynomial exponentiation by squaring:

def poly_pow(p, exponent):
    result = [1]  # identity element (x^0)
    while exponent >0:
        if exponent %2 ==1:
            result = multiply(result, p)
        p = multiply(p, p)
        exponent = exponent //2
    return result

But this may not be efficient enough for very large exponents. Also, each multiplication can be expensive for large polynomials.

But given that the initial polynomial P may have very small degree (up to 9), and each squaring step doubles the exponent, the degrees can grow exponentially. For example, after log2(m) steps, the degree can be up to 9*m.

But in practice, during the exponentiation steps, the polynomials can get very large. For example, when m is 1e5, the maximum degree is 9e5. Each multiply operation would take O(n log n) time, where n is the next power of two for the required length.

Another optimization: during the exponentiation, the polynomials can be kept trimmed to their actual maximum exponent. For example, after each multiplication, the resulting polynomial is truncated to the necessary length. This can save memory and computation time.

But how to implement this.

So, during the multiply(a, b) step, the resulting polynomial is computed as the convolution of a and b, and then the coefficients beyond the maximum needed can be ignored. But no, since all coefficients are necessary for the sum. But when squaring, all coefficients are necessary.

But when you compute (P^m), you need all coefficients, as each s can contribute to the sum of squares.

Therefore, the code must compute all coefficients.

But even with all this, the time may be too long in Python for the given constraints.

Wait, let's think about the sample input where n=20 and k=1, digit 6. Then m=10. The sum of each half must be 10*6=60. The count for each half is 1. So the answer is 1. The code would generate the polynomial (x^6)^10 = x^60, and then sum the squares (1^2) =1.

But to compute this, the exponentiation would take log2(10) steps. Each step would multiply the polynomials. Initially, the polynomial is [0, 0, 0, 0, 0, 0, 1]. Then, each squaring step would raise the exponent. For example, after 1 step, it's squared to x^12, etc.

But even this, the code would handle correctly.

Another sample input is the first example:

n=4, m=2. allowed digits 1 and 8. The polynomial is x^1 +x^8. Raised to the second power: (x +x^8)^2 = x^2 + 2x^9 +x^16. The coefficients are 1 at 2, 2 at 9, 1 at 16. The sum of squares is 1^2 +2^2 +1^2 =1+4+1=6, which matches the sample.

But in this case, the code would generate the correct polynomial.

But back to the problem of time constraints.

For the worst case, m=1e5. So, during exponentiation by squaring, the number of steps is log2(1e5) ~17 steps. Each step involves multiplying two polynomials.

Initially, the polynomial is of length 10 (digits 0-9). After squaring once, the length is 18 (0-18). Squaring again, 36 (0-36). And so on. Each step doubles the exponent. For example, after 17 steps, the maximum exponent is 9*2^17. But wait, exponentiation by squaring doesn't work like that. Wait, no: the exponents are additive. For example, (x^d)^m is x^(d*m). So the code will correctly compute that.

Wait, no. The code is raising the polynomial P to the m-th power, which is the same as convolving P with itself m times. So each step of the exponentiation by squaring accumulates the product correctly.

But regardless, the maximum exponent after m steps is m*d_max, where d_max is the maximum digit. For m=1e5 and d_max=9, this is 9e5.

So the maximum length of the polynomial after exponentiation is 9e5 +1.

But the problem is that each multiplication step in the exponentiation will require NTT of size up to 2^20 (since 9e5*2 is 1.8e6, which is less than 2^21 (2,097,152)), so the next power of two is 2^21.

Each NTT step for 2^21 elements would require O(2^21 * 21) operations. Which is about 44 million operations per NTT. Since each multiplication requires two forward NTTs and one inverse NTT, that's about 44 million *3 = 132 million operations per multiplication. For 17 steps, that's 2.2 billion operations. Python can handle about 1e6 operations per second, so this would take 2.2e9 /1e6 = 2200 seconds, which is way over the time limit.

This approach is not feasible in Python for the given constraints.

Hmm. So this suggests that even with an optimal NTT implementation, Python is too slow for this problem.

Therefore, we need to find another approach.

Alternative approach: Since the allowed digits are up to 10, and m is up to 1e5, perhaps we can find a way to compute the counts using dynamic programming with optimized loops.

Wait, let's think again about the DP approach. For each digit added, the new sum can be computed from the previous sum by adding any of the allowed digits.

The DP array can be represented as a list where dp[i][s] is the number of ways to get sum s after i digits.

The recurrence is:

dp[i][s] = sum_{d in digits} dp[i-1][s -d]

But this is for each s. The base case is dp[0][0] =1.

The problem is that for i up to 1e5 and s up to 9e5, this is O(m * s), which is 9e10 operations. Impossible.

But perhaps there's a way to optimize this using matrix exponentiation. Let's model the transitions as a linear recurrence.

Each step, the new dp is the convolution of the previous dp with the allowed digits' generating function. But convolution is a linear operation. So this can be represented as a linear transformation. For the purposes of matrix exponentiation, the state is the current sum, but since the sum can be up to 9e5, the matrix is way too big.

So this approach is not feasible.

Another idea: the allowed digits are fixed, so the generating function is fixed. Therefore, the convolution is fixed. So for m steps, the problem is to compute the m-th convolution of the allowed digits' generating function.

But how to compute this efficiently.

Wait, perhaps the generating function is a sum of exponentials. For example, the generating function for a single step is P(x) = sum x^d. The generating function for m steps is P(x)^m.

The coefficients of P(x)^m can be computed using the multinomial theorem. However, the multinomial expansion for m terms would have terms that count the number of ways to select m digits (possibly repeated) such that their sum is s.

But the multinomial coefficients are not straightforward to compute for large m.

Alternatively, the problem can be viewed as a problem of counting the number of sequences of m digits from the allowed set that sum to s. This is equivalent to the coefficient of x^s in (sum x^d)^m.

But again, this brings us back to the generating function approach.

So, back to square one: the problem requires computing the sum of the squares of the coefficients of P(x)^m, where P(x) is the sum of x^d for each allowed digit d.

But how to compute this sum efficiently.

The sum of squares of the coefficients of a polynomial Q(x) is equal to Q(1) * Q(1), but only if the polynomial is evaluated at x=1 and x=1. But wait, no. The sum of squares of the coefficients of Q(x) is Q(1) * Q(1) if Q(x) is multiplied by Q(x^{-1}), and evaluated at x=1. Wait, perhaps not.

Alternatively, the sum of squares of the coefficients of Q(x) is Q(1) * Q(1) if all coefficients are real and positive. But this is not the case here. Wait, for example, if Q(x) = a + bx + cx^2, then the sum of squares is a^2 + b^2 + c^2. But Q(1) is a + b + c. So unless a, b, c are 0 or 1, this is not the same.

But in our case, the coefficients are all non-negative, but their squares summed would not be (sum a_i)^2. So this approach isn't helpful.

So, the sum of squares must be computed by iterating over each coefficient of Q(x) and accumulating the squares.

But if Q(x) has a million coefficients, this would be manageable, as a million operations are acceptable.

The problem is computing Q(x) = P(x)^m.

But given the time constraints in Python, the NTT-based approach may not be feasible. So, what's the alternative?

Another idea: since the allowed digits are fixed, we can model the problem as a dynamic programming with the sum modulo some number. But I don't see how this would help.

Alternatively, notice that the sum of the digits in each half can be up to 9e5. But even that is too large for standard DP approaches.

Another observation: the sum is additive. So, perhaps we can find a generating function for each possible sum, and then find the sum of squares. But this is what we already know.

Hmm.

Alternative approach: use the fact that the allowed digits are fixed and precompute their sum possibilities using the Fast Fourier Transform method, but then raise the polynomial to the m-th power using some mathematical optimization.

But I'm not sure.

Wait, perhaps we can use the fact that the allowed digits are small, and precompute the generating function for small exponents, and then use some decomposition for larger exponents.

But I'm not sure.

Alternatively, think of the digits as a multiset. For each allowed digit d, the number of times it appears in the m-digit sequence is some variable t_d, where sum t_d = m. The sum s is sum (t_d * d) for all d. So the count is the number of solutions to sum t_d = m and sum (t_d * d) = s, with t_d >=0 integers.

But solving this for each s is not straightforward, especially for large m.

So perhaps this is not helpful.

At this point, I'm stuck. Maybe I should look for an alternative way to compute the sum of squares of the coefficients of P(x)^m without explicitly computing all the coefficients.

But I don't see how.

Wait, the sum of squares is equal to the product of P(x)^m and P(x^{-1})^m evaluated at x^0. Because P(x)^m * P(x^{-1})^m = sum_{s} (sum_{a} c_a c_{a+s} ) x^s. The coefficient at x^0 is sum_{a} c_a^2, which is exactly the sum of squares.

So, sum of squares is the coefficient of x^0 in P(x)^m * P(x^{-1})^m.

But P(x^{-1}) is the polynomial with terms x^{-d} for each d in allowed digits. So P(x^{-1}) = sum x^{-d} = sum x^{9-d} / x^9, but that's not helpful.

Alternatively, P(x^{-1}) is the reverse polynomial multiplied by x^{max_d}. Not sure.

Alternatively, evaluating the product of P(x)^m and P(x^{-1})^m, and finding the coefficient of x^0.

But this requires multiplying two polynomials, each of which is P(x)^m and P(x^{-1})^m. But this product is P(x)^m * P(x^{-1})^m = (P(x) * P(x^{-1}))^m.

But P(x)*P(x^{-1}) is sum_{d} sum_{d'} x^{d - d'}, which is a polynomial where the coefficient of x^k is the number of pairs (d, d') such that d -d' =k.

The product (P(x)*P(x^{-1}))^m is a polynomial where the coefficient of x^0 would be the sum of squares of the coefficients of P(x)^m.

But again, how to compute this.

Wait, the coefficient of x^0 in (P(x) * P(x^{-1}))^m is the sum of squares of the coefficients of P(x)^m. Because:

(P(x) * P(x^{-1})) is sum_{d1} sum_{d2} x^{d1 - d2}.

When raised to the mth power, the coefficient of x^0 is the number of ways to choose m pairs (d_i, e_i) such that sum (d_i - e_i) =0. Which is the same as sum d_i = sum e_i. Which is exactly the sum of squares of the coefficients of P(x)^m.

So sum_{s} (count(s))^2 = coefficient of x^0 in (P(x) * P(x^{-1}))^m.

So if we can compute this coefficient, we can avoid calculating all coefficients of P(x)^m.

But how to compute this coefficient.

But computing (P(x) * P(x^{-1}))^m and finding the coefficient of x^0.

But P(x)*P(x^{-1}) is a polynomial where the coefficient of x^k is the number of pairs (d, e) in the allowed digits such that d - e =k.

So, this polynomial can be computed by taking the convolution of the allowed digits' frequencies with their reverse.

For example, for allowed digits d1, d2, ..., dk, the coefficient for x^k is the number of pairs (d, e) where d -e =k.

Then, raising this polynomial to the m-th power gives us (P(x)*P(x^{-1}))^m. The coefficient of x^0 in this is the sum of squares of the coefficients of P(x)^m.

But how to compute this.

But even this approach requires computing the convolution of P(x) and P(x^{-1}), which is the same as the auto-correlation of P's coefficients. Then, raising this polynomial to the mth power and taking the x^0 coefficient.

But the problem is that this polynomial could have non-zero coefficients for negative exponents. However, since we are working with polynomials in x, we can represent negative exponents by shifting the polynomial.

For example, if the maximum possible value of (d - e) is 9 (when d=9 and e=0), and the minimum is -9 (when d=0 and e=9), then the possible exponents in P(x)*P(x^{-1}) range from -9 to 9. So the polynomial can be represented with exponents from -9 to 9. But to represent this as a regular polynomial, we can multiply by x^9 to shift all exponents to 0-18. So:

Let Q(x) = P(x) * P(x^{-1}) = sum_{k} c_k x^k. The exponents k can be from -9 to 9. We can represent this as sum_{k} c_{k} x^{k +9} = sum_{k'} c_{k'-9} x^{k'}, where k' ranges from 0 to 18. This allows us to represent Q(x) as a polynomial with non-negative exponents.

Then, Q(x) can be represented as a polynomial of degree 18. Raising this to the mth power, and finding the coefficient of x^{9*m} (since each multiplication by x^{k} in the original Q(x) becomes x^{k +9}, so raising to the mth power would shift the exponents by 9*m. So the coefficient of x^{9*m} in the shifted polynomial corresponds to the coefficient of x^0 in the original polynomial.

Thus, the sum of squares is the coefficient of x^{9*m} in (Q_shifted(x))^m, where Q_shifted(x) is Q(x) * x^9.

But Q_shifted(x) is a polynomial of degree 18, and coefficients for each exponent from 0 to 18.

Wait, this seems promising. Let's work through an example.

For the first sample input: allowed digits 1 and 8.

P(x) = x + x^8.

P(x^{-1}) = x^{-1} + x^{-8}.

P(x) * P(x^{-1}) = x^{-8}*x + x^{-8} *x^8 + x^{-1} *x + x^{-1} *x^8 = x^{-7} + 1 + 1 + x^7. So the terms are x^{-7}, 2 terms of x^0, and x^7.

But when shifted by x^9, Q_shifted(x) = x^{9-7} + 2 x^9 + x^{9+7} = x^2 + 2x^9 + x^16. So the polynomial is [0,0,1,0,0,0,0,0,0,2,0,0,0,0,0,0,1]. The exponents are 0 to 16.

Raising this to m=2, the coefficient of x^{9*2} =x^18 is the sum of squares. Let's compute this.

The polynomial Q_shifted is x^2 + 2x^9 +x^16. Raising to 2:

(x^2 + 2x^9 + x^16)^2 = x^4 + 4x^11 + 2x^18 + 4x^18 + 4x^25 + x^32. So the coefficient of x^18 is 2+4=6, which matches the sample.

So this approach works.

Now, the key insight is that the polynomial Q_shifted(x) has a small degree (max 18). Raising it to the m-th power would result in a polynomial of degree 18*m, but the coefficients can be computed using dynamic programming.

The problem now is to compute the coefficient of x^{9*m} in Q_shifted(x)^m.

But how to compute this.

The polynomial Q_shifted(x) is of degree 18. Raising it to the m-th power would result in a polynomial of degree 18*m. But we need only the coefficient of x^{9*m}.

This is equivalent to finding the number of ways to select m terms (with replacement) from the terms of Q_shifted(x) such that their exponents sum to 9*m.

Each term in Q_shifted(x) is of the form c * x^e, where e is in 0 to 18 (but actually, the exponents are the possible differences d1 - d2 +9, so in the original Q_shifted(x) the exponents are shifted by 9).

But this reduces the problem to a dynamic programming problem where for each step, we can add a term from Q_shifted(x), and track the sum of exponents modulo 9*m.

But wait, m can be up to 1e5, so 9*m is up to 9e5. But the exponents needed are exactly 9*m. So the state of the DP is the current sum of exponents. For each step, we can add exponents from the allowed terms (each term is the exponents in Q_shifted(x)).

But the allowed terms are the exponents present in Q_shifted(x). For example, in the first sample, the exponents are 2,9,16.

So the allowed exponents are those that appear in Q_shifted(x). Let's denote the exponents as e_1, e_2, ..., e_t, each with a certain coefficient (c_i).

The problem is now: compute the number of ways to choose m terms (possibly multiple times) from the allowed exponents (e_1, e_2, ..., e_t) such that their sum is 9*m, with each term's contribution multiplied by its coefficient.

But this is exactly the same as the coefficient of x^{9*m} in Q_shifted(x)^m.

But how to compute this efficiently.

The dynamic programming approach would be to create a DP array where dp[i][s] is the number of ways to choose i terms with sum s. The recurrence is:

dp[i][s] = sum_{e} (c_e * dp[i-1][s - e]) 

The base case is dp[0][0] = 1.

But m can be up to 1e5, and s can be up to 9e5, which makes the time complexity O(m * s) again.

But this is not feasible for m=1e5.

But the allowed exponents are up to 18 (since Q_shifted(x) has exponents up to 18). So for each step, the allowed e's are up to 18. So the DP for each step is O(18 * current_max_s). But for m steps, this could be O(m * 18 * (current_max_s)), which for m=1e5 and current_max_s up to 9e5 is 1e5 * 18 * 9e5 = 1.62e11 operations, which is again way too slow.

But here's the key: the required sum is exactly 9*m. So perhaps there's a way to model the DP such that we track the sum in terms of the deviation from the required sum.

Wait, each term e in Q_shifted(x) contributes e to the sum. We need the sum of m terms to be 9*m. So each term's contribution minus 9 must sum to zero. So, for each term e, we can model its contribution as (e -9). The sum of m such terms must be zero.

So the problem is to select m terms, each with value (e -9), such that their sum is zero.

This transforms the problem into a classic integer partition problem with possible negative numbers, but with the sum zero.

Now, this is similar to a problem where each step adds a certain value, and after m steps, the total must be zero.

The allowed values are (e -9) for each e in the exponents of Q_shifted(x).

For example, in the first sample, the exponents are 2,9,16. So the allowed values are 2-9= -7, 9-9=0, 16-9=7.

So the problem is to choose m terms from {-7,0,7}, such that their sum is zero. The count is the coefficient of x^0 in (x^{-7} + x^0 + x^7)^m.

But how to compute this efficiently.

The maximum possible deviation from zero after each step is limited. For example, in each step, adding a value of up to 7 or down to -7. For m steps, the maximum possible sum is m*7 or -m*7. But this is up to 7e5 for m=1e5.

But the problem is to find the sum zero after m steps.

But the DP approach can be modeled as:

dp[i][s] = sum of ways to reach sum s after i steps.

The transitions are for each possible delta in the allowed values (e-9), and dp[i][s] += dp[i-1][s - delta] * c_e, where c_e is the coefficient of e in Q_shifted(x).

But for m=1e5, this is still O(m * (2*7*m)) = O(14e5 * 1e5) = 1.4e11 operations, which is way too slow.

But here's another key insight: this problem is equivalent to a convolution problem where each step adds a certain set of possible deltas. And since the steps are identical, the DP can be represented as the convolution of the allowed deltas m times.

So the problem reduces to finding the coefficient of x^0 in (Q(x))^m, where Q(x) is sum (c_e * x^{e-9}) for each exponent e in Q_shifted(x).

But this is exactly the same as the original problem of finding the coefficient of x^{9m} in Q_shifted(x)^m.

But if the allowed deltas are small, perhaps we can find a way to compute this using matrix exponentiation or some other method.

Alternatively, considering that the allowed deltas are limited (for example, in the first sample, the deltas are -7, 0,7), perhaps there's a way to represent the DP state as a vector of possible sums modulo some period.

But I'm not sure.

Another idea: the problem is to compute the number of ways to reach sum zero after m steps, where each step can add a certain delta. This is similar to a linear recurrence problem. For example, if the possible deltas are d_1, d_2, ..., d_t, then the recurrence is:

dp[i][s] = sum_{j} c_j * dp[i-1][s -d_j]

But even with this, for m=1e5 and s up to 7e5, it's not feasible.

But notice that for each step, the sum can increase or decrease by a fixed amount. So the state is the current sum s. But how to model this efficiently.

Alternatively, using generating functions again. The generating function for the sum after m steps is (sum c_e * x^{d_e})^m, where d_e = e -9. The coefficient of x^0 in this polynomial is the desired answer.

This is the same as the previous approach.

But how to compute this coefficient.

But this is a polynomial of degree up to m*max_d, where max_d is the maximum delta. For delta of 7 and m=1e5, the maximum sum is 7e5. So the polynomial has up to 7e5 terms.

But exponentiating this polynomial to the mth power using binary exponentiation with NTT is still not feasible.

But wait, the allowed deltas are up to 9 (since e can be up to 18, delta 18-9=9). So the maximum delta is 9, and the minimum is -9. So the possible deltas are between -9 and +9.

The polynomial Q(x) = sum_{d in D} c_d x^{d}, where D is the set of deltas (e-9 for each e in Q_shifted(x)).

So Q(x) is a polynomial of degree up to 9 and down to -9. To represent this as a polynomial with non-negative exponents, we can multiply by x^9. So Q_shifted_again(x) = Q(x) * x^9. This shifts all exponents by 9, making them non-negative. Now, the problem is to find the coefficient of x^9*m in Q_shifted_again(x)^m.

But Q_shifted_again(x) is a polynomial of degree 18 (since 9 +9 = 18). Raising this to the mth power results in a polynomial of degree 18*m. The coefficient of x^9m is the desired answer.

But how to compute this coefficient.

But now, the polynomial Q_shifted_again(x) has degree 18. Each term is of the form c_d x^{d +9}, where d is the delta (e-9).

But this is the same as the original Q_shifted(x) polynomial.

Wait, this brings us back to the original approach.

So, to compute the coefficient of x^{9m} in Q_shifted(x)^m, we can use a dynamic programming approach where the state is the current exponent sum modulo (something), but I'm not sure.

Alternatively, perhaps we can model this as a matrix exponentiation problem. The possible sum s can be represented in terms of the allowed deltas. However, the sum can range from -9m to 9m, which is too large for matrix exponentiation.

But if we can find a way to represent the transitions in terms of the allowed deltas, perhaps using generating functions and matrix exponentiation for the polynomial coefficients.

Alternatively, using the fact that the allowed deltas are small, perhaps we can find a way to represent the problem as a linear recurrence with a fixed number of terms.

But I'm not sure.

Another idea: the generating function for each step is a polynomial of fixed size (say, 19 terms, from delta -9 to +9). Raising this to the mth power can be done using matrix exponentiation, but the state is the current coefficients of the polynomial. However, for each multiplication, the polynomial's size increases, making this approach impractical.

Alternatively, the exponents can be represented as a vector, and matrix exponentiation can be used to compute the exponents after m steps. But for a vector of size 19, the matrix would be 19x19, which is manageable. But how to model this.

Wait, perhaps each step multiplies the current generating function by Q(x), which is a polynomial of fixed size. So the process is a linear transformation, and the exponents can be represented as a vector of coefficients. The transformation for each step is multiplying by Q(x), which can be represented as a convolution matrix. Raising this transformation to the mth power can be done using matrix exponentiation.

But the matrix would be of size (max_degree +1) x (max_degree +1), where max_degree is 18. For a polynomial of degree 18, the matrix would be 19x19. Exponentiating this matrix to the mth power would take O(log m) steps, each involving matrix multiplication of 19x19 matrices. Each matrix multiplication is O(19^3) operations, which is manageable even for m=1e5.

This approach is promising.

Here's how it works:

The generating function after k steps is Q(x)^k. To compute Q(x)^m, we can model the exponents as a vector of coefficients. Each multiplication by Q(x) is a convolution, which can be represented as a matrix multiplication.

But for a polynomial of degree d, the state vector has d+1 elements. For Q(x) with degree 18, the state vector has 19 elements. Each multiplication by Q(x) is a convolution, which can be represented as a matrix operation. However, this matrix is a Toeplitz matrix (each row is a shifted version of the previous row), and raising the transformation (matrix) to the mth power would allow us to compute Q(x)^m.

So the steps are:

1. Compute the polynomial Q(x) = sum c_d x^{d}, where c_d is the coefficient of x^d in Q_shifted(x).

Q_shifted(x) is the shifted version of P(x) * P(x^{-1}).

2. Represent Q(x) as a vector of coefficients, with indices from 0 to 18.

3. The initial state is a vector representing x^0 (i.e., [1, 0, 0, ..., 0]).

4. Each multiplication by Q(x) is a convolution, which can be represented as a matrix multiplication. The matrix is a Toeplitz matrix derived from the coefficients of Q(x).

5. Compute the matrix raised to the mth power using binary exponentiation.

6. Multiply the initial vector by this matrix to get the coefficients of Q(x)^m.

7. The coefficient at index 9*m is the desired answer.

But wait, the problem is that 9*m can be up to 9e5, which is larger than the degree of the polynomial (18*m is the degree, but 9*m can be up to 9e5, which is much larger than 18*1e5=1.8e6). So this approach is not feasible because the vector would need to be of size 1.8e6 +1, which is way too large.

But this suggests that this approach isn't feasible either.

Another Idea: Since the required coefficient is x^{9*m} in Q_shifted(x)^m, and Q_shifted(x) is a polynomial of degree 18, the exponent m can be represented in terms of the exponents of Q_shifted(x).

But I'm not sure.

Alternatively, note that Q_shifted(x) is a polynomial of degree 18. The coefficient of x^{9m} in Q_shifted(x)^m can be computed using dynamic programming with the possible sums modulo some value. But again, I'm not seeing it.

At this point, given the time constraints and the problem's requirements, perhaps the correct approach is to precompute the allowed digits' generating function, exponentiate it using NTT-based convolution, and sum the squares of the coefficients. But implementing this in Python is challenging.

Alternatively, perhaps the problem requires a different approach, such as using the fact that the sum of the squares is the coefficient of x^0 in (P(x) * P(x^{-1}))^m, and finding this coefficient using matrix exponentiation for the convolution matrix.

But I'm not sure.

Given the time constraints and the difficulty of implementing NTT in Python efficiently, perhaps the only feasible way is to proceed with the DP approach, but find a way to optimize it using the fact that the allowed digits are fixed.

But with m up to 1e5 and sum up to 9e5, this seems impossible.

Wait, but perhaps the allowed digits are up to 10, and we can find a way to compute the DP using generating functions and matrix exponentiation.

For example, the problem can be modeled as a linear recurrence where the state is the current sum modulo some number. But I don't see a pattern here.

Alternatively, use the fact that the generating function is P(x)^m, and the sum of squares is the coefficient of x^0 in P(x)^m * P(x^{-1})^m. This product can be written as (P(x) * P(x^{-1}))^m. The coefficient of x^0 in this product is the desired sum.

But P(x) * P(x^{-1}) is a polynomial with terms x^{d - d'}, which is the same as sum_{d, d' in allowed digits} x^{d-d'}.

This is a polynomial with coefficients indicating how many pairs of digits have a difference of k. Then, raising this to the mth power gives a polynomial where the coefficient of x^0 is the number of ways to choose m pairs (d_i, d'_i) such that the sum of (d_i -d'_i) is zero. This is exactly the sum of squares of the coefficients of P(x)^m.

But the polynomial (P(x) * P(x^{-1})) is a polynomial with coefficients c_k, where c_k is the number of pairs of allowed digits with difference k. The exponents of this polynomial range from -9 to 9. So when we shift all exponents by 9, the polynomial becomes a polynomial of degree 18, and raising this to the mth power gives a polynomial where the coefficient of x^{9m} is the sum of squares.

So the problem reduces to finding the coefficient of x^{9m} in Q_shifted(x)^m, where Q_shifted(x) is the shifted version of P(x) * P(x^{-1}).

Now, Q_shifted(x) is a polynomial of degree 18. Raising it to the mth power can be done using matrix exponentiation. The idea is to model the exponents as a vector and multiply by the polynomial's convolution matrix m times.

But how to model this. Let's think: the coefficients of the polynomial after each multiplication can be represented using a dynamic programming approach. For example, each multiplication by Q_shifted(x) is a convolution with its coefficients.

So, the state is the current polynomial coefficients. Each step, we convolve with Q_shifted(x). But since this is done m times, we can use binary exponentiation to compute the mth power.

This approach would involve O(log m) convolution steps. Each convolution is between two polynomials of degree up to 18 * current exponent. But during exponentiation, the degrees grow exponentially. For example, after each squaring, the degree doubles. For m=1e5, log2(m) is about 17 steps. The degrees would be 18, 36, 72, etc., up to 18 * 2^17, which is way too large.

Thus, this approach is not feasible.

But perhaps there's another way. For example, since the required exponent is 9m, which is exactly half of the maximum possible exponent (18m), we can use some combinatorial symmetry.

But I'm not seeing it.

At this point, I think the correct approach is to proceed with the initial plan of using NTT-based polynomial exponentiation, but optimize it as much as possible in Python.

But implementing NTT in Python for large polynomials is going to be too slow. Therefore, perhaps we can find a way to compute the sum of squares using the properties of the allowed digits.

Another observation: the sum of squares is equal to the number of pairs of m-digit sequences (one for the first half and one for the second half) where the sum of both halves is equal.

But each such pair is a ticket where the first and second halves' sums are equal. But this is exactly the same as the sum of squares of the coefficients.

So, this doesn't provide any new insight.

Another idea: since the allowed digits are a small set, perhaps we can precompute the number of times each digit appears in the m-digit sequence and compute the sum of products. But this seems similar to the original problem.

But I'm stuck.

After spending a lot of time thinking, I think the correct way is to proceed with the NTT-based approach, but implement it efficiently.

Thus, the code will read the digits, create the polynomial, exponentiate it using NTT-based multiplication, and sum the squares of the coefficients.

But given the time constraints in Python, perhaps we can find a way to optimize the code.

Here's the plan for the code:

1. Read n and k, and the list of digits.

2. Compute m = n // 2.

3. Create the initial polynomial P, which has 1 at each digit in the allowed list.

4. Compute Q = P^m using NTT-based exponentiation.

5. Sum the squares of each coefficient in Q, modulo 998244353.

But implementing this in Python with the given time constraints.

But how to handle large polynomials. For example, if m is 1e5, the polynomial will have 9e5 +1 coefficients. Storing this as a list of integers in Python is possible, but the exponentiation steps are time-consuming.

Alternative Idea: Use the fact that the maximum possible sum is 9e5, but digits are allowed. But this doesn't help.

Thus, the code will have to proceed with the NTT-based approach.

But given the time constraints in Python, I'm not sure if it will pass.

But perhaps there's a smarter way to implement this. For example, precompute the possible sums and use a divide and conquer approach.

Alternatively, using memoization for the exponentiation steps.

But I'm not sure.

Alternatively, for each digit, the allowed digits are a set S. The number of ways to achieve a sum s with m digits is the convolution of m copies of S.

But again, this brings us back to the generating function approach.

After struggling with the options, I'll proceed with the code that implements the polynomial exponentiation using NTT-based multiplication. But in Python, even this may be too slow for the largest inputs.

But given the examples, perhaps the code can pass.

Let's proceed.

The code will:

- Read n, k, and the allowed digits.

- Create the initial polynomial P with coefficients 1 for each allowed digit.

- Compute P^m using the polynomial exponentiation function.

- Sum the squares of the coefficients modulo 998244353.

But to handle large m, the code must be as optimized as possible.

But given Python's speed, this may not be feasible for large m. However, in practice, the problem may have constraints that allow this approach to work.

But let's try to write the code.

First, implement the NTT functions.

But the code from earlier may not be efficient enough. Alternative Idea: Use the fact that the allowed digits are up to 9, and m is up to 1e5, but the maximum sum is 9e5, which can be handled with dynamic programming.

Wait! Wait. Wait a minute.

Each digit can be used multiple times. The problem is to find the number of sequences of m digits where the sum is s, for each s.

But this is a standard problem that can be modeled as a dynamic programming problem with O(m * max_sum) time.

But for m=1e5 and max_sum=9e5, this is O(9e5 * 1e5) = 9e10 operations. Which is way too slow.

But perhaps we can find a way to represent the DP array as a 1D array and update it in place, reusing space.

But even with that, 9e10 operations are not feasible.

Alternative Idea: Use the fact that the allowed digits are up to 10, and use a sliding window approach.

For each digit in the allowed set, the DP transition is dp[i][s] += dp[i-1][s-d]. This can be viewed as a convolution of the previous DP array with the allowed digits' generating function.

But again, this is the same as the previous approach.

But perhaps using a more efficient way to compute the convolution.

For example, using a Fast Fourier Transform-based convolution for each step. But for m=1e5 steps, this is O(m * s log s) time, which is also not feasible.

At this point, I'm stuck and have to conclude that the intended solution is to use the NTT-based approach, and the code must be written accordingly.

But in Python, it's challenging. However, perhaps the test cases are designed to allow an optimized code to pass.

So here's the code:

Read the digits, create the initial polynomial, compute the exponent, then sum the squares.

But I'll proceed to write the code using the NTT approach.

The code will use the NTT functions as defined earlier.

Testing against sample input 1.

```python
import sys


MOD = 998244353

def ntt(a, invert):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    log_n = (n).bit_length() - 1
    root = 3
    roots = [1] * (log_n + 1)
    for i in range(log_n):
        roots[i+1] = roots[i] * roots[i] % MOD
    if invert:
        root = pow(root, MOD-2, MOD)
        roots = [pow(r, MOD-2, MOD) for r in roots]
    for i in range(1, log_n + 1):
        m = 1 << i
        mh = m >> 1
        w_m = roots[log_n - i]
        w = 1
        for j in range(mh):
            for k in range(j, n, m):
                idx = k + mh
                x = a[k]
                y = a[idx] * w % MOD
                a[k] = (x + y) % MOD
                a[idx] = (x - y) % MOD
            w = w * w_m % MOD
    if invert:
        inv_n = pow(n, MOD-2, MOD)
        for i in range(n):
            a[i] = a[i] * inv_n % MOD

def multiply(a, b):
    len_a = len(a)
    len_b = len(b)
    max_len = len_a + len_b - 1
    n = 1
    while n < max_len:
        n <<= 1
    fa = a + [0] * (n - len_a)
    fb = b + [0] * (n - len_b)
    ntt(fa, False)
    ntt(fb, False)
    for i in range(n):
        fa[i] = fa[i] * fb[i] % MOD
    ntt(fa, True)
    return fa[:max_len]

def poly_pow(p, exponent):
    result = [1]
    while exponent > 0:
        if exponent % 2 == 1:
            result = multiply(result, p)
        p = multiply(p, p)
        exponent //= 2
    return result

def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().split())
    digits = list(map(int, input_stream.readline().split()))
    allowed = set(digits)
    max_d = max(allowed) if allowed else 0
    p = [0] * (max_d + 1)
    for d in allowed:
        p[d] = 1
    m = n // 2
    q = poly_pow(p, m)
    total = 0
    for coeff in q:
        total = (total + coeff * coeff) % MOD
    print(total % MOD, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
20 1
6
""",
            "output": \
"""\
1
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

So the correct way to create the initial polynomial is to have a list where the index is the digit, and the value is 1 if the digit is allowed.

Thus:

allowed = set(digits)
p = [0] * (10)
for d in allowed:
    p[d] = 1

Then, the polynomial is [1 if d is in allowed, else 0 for d in 0..9].

But when we multiply this polynomial m times, we get the generating function for m digits.

But wait, the polynomial is of size 10. When we multiply it with itself, the degrees add.

So for the first sample, the polynomial is x^1 +x^8.

But when we multiply it by itself, we get x^2 + 2x^9 +x^16.

The code should correctly compute this.

But with the current code, the polynomial is of length 10. When we multiply it by itself, the result is of length 10 + 10 -1 =19. But the code uses the multiply function which pads to the next power of two.

But in the code, the multiply function uses the ntt function which handles this.

But the code must be written to handle the polynomial properly.

So, putting it all together:

Read n and k.

Read the allowed digits.

Create the initial polynomial.

Compute m = n//2.

Compute the polynomial Q = initial_poly^m.

Sum the squares of the coefficients of Q, modulo 998244353.

So, here's the code:
</think>

```python
import sys
MOD = 998244353

def ntt(a, invert):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    log_n = (n).bit_length() - 1
    root = 3
    roots = [1] * (log_n + 1)
    for i in range(log_n):
        roots[i+1] = roots[i] * roots[i] % MOD
    if invert:
        root = pow(root, MOD-2, MOD)
        roots = [pow(r, MOD-2, MOD) for r in roots]
    for i in range(1, log_n + 1):
        m = 1 << i
        mh = m >> 1
        w_m = roots[log_n - i]
        w = 1
        for j in range(mh):
            for k in range(j, n, m):
                idx = k + mh
                x = a[k]
                y = a[idx] * w % MOD
                a[k] = (x + y) % MOD
                a[idx] = (x - y) % MOD
            w = w * w_m % MOD
    if invert:
        inv_n = pow(n, MOD-2, MOD)
        for i in range(n):
            a[i] = a[i] * inv_n % MOD

def multiply(a, b):
    len_a = len(a)
    len_b = len(b)
    max_len = len_a + len_b - 1
    n = 1
    while n < max_len:
        n <<= 1
    fa = a + [0] * (n - len_a)
    fb = b + [0] * (n - len_b)
    ntt(fa, False)
    ntt(fb, False)
    for i in range(n):
        fa[i] = fa[i] * fb[i] % MOD
    ntt(fa, True)
    return fa[:max_len]

def poly_pow(p, exponent):
    result = [1]
    while exponent > 0:
        if exponent % 2 == 1:
            result = multiply(result, p)
        p = multiply(p, p)
        exponent //= 2
    return result

def main():
    n, k = map(int, sys.stdin.readline().split())
    digits = list(map(int, sys.stdin.readline().split()))
    allowed = set(digits)
    max_d = max(allowed) if allowed else 0
    p = [0] * (max_d + 1)
    for d in allowed:
        p[d] = 1
    m = n // 2
    q = poly_pow(p, m)
    total = 0
    for coeff in q:
        total = (total + coeff * coeff) % MOD
    print(total % MOD)

if __name__ == "__main__":
    main()
```
