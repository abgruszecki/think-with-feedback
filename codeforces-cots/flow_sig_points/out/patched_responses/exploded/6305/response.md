<think>
Okay, let's see. I need to solve this problem where I have to count the number of answer suits such that after shifting them clockwise by one, the new score is strictly larger than the original. The constraints are pretty big, n up to 2e5, so any O(n) solution is manageable, but O(n^2) is definitely out. Let's think through the problem.

First, let's understand what's being asked. Each answer suit a_1, a_2, ..., a_n is a possible sequence of answers. The mistake shifts this sequence so that a_i becomes the answer to question i mod n +1. So the shifted sequence is a' where a'_i = a_{i-1} for i>1, and a'_1 = a_n.

The original score is the sum over all i of (a_i == h_i). The shifted score is the sum over i of (a_{i-1} (mod n) == h_i). So the condition is that the shifted score is strictly larger than the original.

We need to count all possible a sequences where this condition holds, modulo 998244353.

Hmm. Let's model this. For each a sequence, compute the original score S and shifted score S'. The count is the number of a's where S' > S.

Let me think about the variables. For each position i, in the original sequence, a_i must match h_i. But in the shifted sequence, a_{i-1} (with i-1 taken mod n) must match h_i. So for each i, the shifted a' for position i is a_{i-1}, which needs to match h_i.

So for each i, the original a_i's contribution is 1 if a_i == h_i. The shifted a' contributes 1 for position i if a_{i-1} == h_i (with i-1 mod n, so for i=1, it's a_n).

So the total S is sum_{i=1 to n} (a_i == h_i), and S' is sum_{i=1 to n} (a_{i-1} == h_i) where a_0 is a_n.

So S' - S is the difference between the sum over i of (a_{i-1} == h_i) - (a_i == h_i). We need S' - S > 0.

Let's compute this difference. For each i, the term is (a_{i-1} == h_i) - (a_i == h_i). The sum of all these terms must be positive.

Let's group the terms. For each i, the term is (a_{i-1} == h_i) minus (a_i == h_i). Summing this for all i from 1 to n. Let's see:

Sum over i=1 to n [(a_{i-1} == h_i) - (a_i == h_i)] = Sum [a_{i-1} == h_i] - Sum [a_i == h_i} ].

But the second sum is Sum [a_i == h_i} ] which is S. The first sum is S' (since S' is the sum of a_{i-1} == h_i for each i). So the difference is S' - S, which is the same as the sum of the terms (a_{i-1} == h_i - a_i == h_i). So the condition is that the sum of these terms is positive.

Wait, that's circular. Because S' is the shifted sum, which is sum of a_{i-1} == h_i. So the difference S' - S is exactly the sum of the terms for each i of (a_{i-1} == h_i) - (a_i == h_i). So the condition is that this sum is >0.

But perhaps we can model each variable's contribution. Let's think for each position i, the term is (a_{i-1} == h_i) - (a_i == h_i). So the sum is the sum over all i of these terms. Let's rearrange the sum:

Each a_j appears in exactly two terms: once as a_i-1 for some i, and once as a_i for some other i. Let's see:

For a particular j, consider when i = j+1. Then a_j is a_{i-1} in the term for i=j+1. And when i = j, a_j is a_i in the term for i=j.

So the total contribution for a_j is:

(a_j == h_{j+1}) (from i=j+1) minus (a_j == h_j) (from i=j).

But when j is the last element (j = n), then i=j+1 is i = n+1 mod n = 1. So for j=n, the term is (a_n == h_1) minus (a_n == h_n).

So each a_j contributes (a_j == h_{j+1}) - (a_j == h_j) to the sum. Because for each j, when you look at all the terms in the sum, a_j is part of the term for i=j+1 (as a_{i-1} = a_j) and part of the term for i=j (as a_i = a_j). So each a_j's contribution is (h_{j+1} is the h_i for i=j+1, which is when a_j is a_{i-1}).

So the total sum is sum_{j=1 to n} [ (a_j == h_{j+1}) - (a_j == h_j) ].

Wait, that's a key insight. Because the sum over i=1 to n of [(a_{i-1} == h_i) - (a_i == h_i)] can be rewritten as sum_{j=1 to n} [ (a_j == h_{j+1}) - (a_j == h_j) ] where j is from 1 to n, and h_{j+1} is h_1 when j=n. So the sum is the sum over all j of (a_j matches h_{j+1}) minus (a_j matches h_j).

So the total sum S' - S is sum_j [ (a_j == h_{j+1}) - (a_j == h_j) ].

We need this sum to be >0.

Let me rephrase this: for each j, when a_j is chosen, it contributes (h_{j+1} == a_j) - (h_j == a_j) to the total difference. So the total sum of these per-j terms must be positive.

So the problem reduces to counting the number of sequences a_1, ..., a_n where the sum over j of (a_j == h_{j+1}) - (a_j == h_j) is positive.

Each a_j can be from 1 to k. So the choices are independent except for their contributions to the sum.

But the sum is additive over the j's. So perhaps each a_j contributes a certain value, and we need the sum of all those values to be positive.

Let me model the possible contribution for each a_j. For each j, the possible choices of a_j can contribute:

If a_j is equal to h_{j+1}, then (1) if a_j is not equal to h_j, this contributes +1 (since 1-0=1). If a_j is equal to h_j as well (h_j == h_{j+1}), then (1-1)=0.

If a_j is not equal to h_{j+1}, but is equal to h_j, then (0-1) = -1.

If a_j is equal to neither, then 0.

So for each j, the possible contributions are:

- If a_j is h_{j+1} and not h_j: +1
- If a_j is h_j and not h_{j+1}: -1
- If a_j is both h_j and h_{j+1}: 0
- Else: 0.

So for each j, the possible contribution from a_j is determined by which of these cases a_j falls into.

So the problem is to select a_j for each j such that the sum of their individual contributions is positive.

Now, the key is to model the possibilities for each j and compute the total number of combinations where the sum of contributions is positive.

But with n up to 2e5, we need a way to model this efficiently.

Let me think of this as a dynamic programming problem. For each position j, track the possible sum so far and the number of ways to reach that sum. But since n is up to 2e5 and the possible sum can be up to n (since each j can contribute at most +1), this approach is impossible because the sum can range from -n to +n, leading to O(n^2) time, which is not feasible.

So we need a smarter approach. Let's consider the possible contributions per j and see if there's a way to model the problem combinatorially.

Let me consider that each j can contribute -1, 0, or +1, depending on a_j's choice.

But perhaps the sum of contributions must be at least +1. So the problem is equivalent to finding the number of sequences where the sum of the per-j contributions is >=1.

But how?

Alternatively, for each j, we can precompute the possible options for a_j and their contribution. Then, the problem is to compute the product of generating functions for each j's possible contributions, and sum the coefficients of the terms where the exponent is positive.

But multiplying polynomials for 2e5 terms is again impossible with standard FFT methods, given time constraints.

So we need a mathematical insight here. Let's see:

The sum of contributions across all j must be positive. Let's consider that each j has a certain set of possible contributions (say, c_j can be -1, 0, or +1, depending on the choices), and we need the sum of all c_j to be >0.

But since each j's contribution is determined by a_j's choice, which can have multiple possibilities, we can model this as a product over the options for each j, where each option adds a certain value to the total sum.

But again, with n up to 2e5, we need to find a way to compute this efficiently.

Let's think about the possible variables. For each j, let's compute the number of choices that lead to a contribution of +1, 0, or -1.

Let me denote for each j:

- x_j: number of a_j choices that give contribution +1.
- y_j: number of a_j choices that give contribution 0.
- z_j: number of a_j choices that give contribution -1.

Then, the total number of valid sequences is the sum over all possible combinations of contributions (c_1, c_2, ..., c_n), where sum c_j > 0, of the product of x_j if c_j=+1, y_j if c_j=0, and z_j if c_j=-1.

But calculating this sum directly is infeasible for large n. So we need a way to model this product and compute the required sum efficiently.

Hmm. Let's consider the generating function for each j. For each j, the generating function is:

f_j(t) = x_j * t^1 + y_j * t^0 + z_j * t^{-1}

Then, the total generating function is the product of f_j(t) for all j. The coefficient of t^s in this product gives the number of sequences where the sum of contributions is s. So the answer is the sum of coefficients of t^s for all s >0.

But again, multiplying all these polynomials is impossible for large n. So we need to find another way to compute this sum.

Wait, but maybe there's a clever mathematical way to compute this sum. Let's think: the sum we need is the sum over all possible sequences of choices, where the sum of their contributions is positive. Let's denote this sum as A.

Then, A is equal to the product of all (x_j + y_j + z_j) [the total possible choices] minus the sum over sequences where sum c_j <=0.

But even that might not help directly. Let's think of the problem in terms of the probabilities. But perhaps the contributions for each j are independent, so the generating function is the product of individual generating functions. However, even with that, the problem is how to compute the sum of the coefficients for exponents >0.

Alternatively, perhaps there's a way to model the expected value or use some inclusion-exclusion principle.

Alternatively, maybe there's a way to model the problem by considering the multiplicative contributions of each j when the sum is positive. But I'm not seeing it.

Wait, perhaps the problem can be transformed into the following: each j contributes a certain delta (either -1, 0, or +1). The total sum is the sum of deltas. We need to count the number of ways where this sum is positive.

But each delta is determined by the choice of a_j, which has x_j options for delta=+1, y_j for 0, z_j for -1.

So for each j, the possible deltas are:

If a_j is equal to h_{j+1} but not h_j: delta +1. The number of such a_j is 1 if h_{j+1} != h_j. Otherwise, if h_{j+1} == h_j, then a_j can't be equal to both, so x_j is zero. Wait, let's think again.

For a given j:

h_{j+1} is h[j % n + 1], right? Because for j = n, j mod n is 0, so j mod n +1 is 1, so h_1.

So for each j, we have h_j and h_{j+1}.

Case 1: h_j == h_{j+1}.

In this case, a_j can be:

- equal to h_j (and h_{j+1}): then the contribution is (1 - 1) = 0.

- not equal to h_j: contribution is 0 - 0 = 0.

So all choices for a_j in this case contribute 0. So the delta is 0.

Wait, no. Wait, if h_j == h_{j+1}, then:

For a_j, when a_j is equal to h_j (and h_{j+1} since they're equal), the contribution is (1 -1) =0.

If a_j is not equal to h_j, then (0 -0) =0. Because since h_{j+1} is equal to h_j, a_j is not equal to either. So in this case, for j where h_j == h_{j+1}, all possible a_j choices contribute 0.

So in this case, x_j is 0, y_j is k (since all choices contribute 0), z_j is 0.

Case 2: h_j != h_{j+1}.

In this case:

a_j can be equal to h_{j+1} but not h_j: contributes +1.

a_j can be equal to h_j but not h_{j+1}: contributes -1.

a_j can be equal to neither: contributes 0.

So the number of choices for each delta:

x_j = 1 (if a_j is exactly h_{j+1} but not h_j). But wait, h_j and h_{j+1} are different here. So a_j can be h_{j+1}, which is different from h_j.

So x_j is 1 (since a_j can be h_{j+1}, which gives +1).

z_j is 1 (a_j is h_j, which gives -1).

y_j is k-2 (the remaining options, which are neither h_j nor h_{j+1}).

So for j where h_j != h_{j+1}, x_j=1, z_j=1, y_j=k-2.

But if k=1, then this case is impossible because h_j and h_{j+1} would have to be equal. So we can safely assume that when h_j != h_{j+1}, k is at least 2.

Wait, but in the problem statement, k can be 1. Let's think: if k=1, then h_i must all be 1. So for all j, h_j and h_{j+1} are equal, so all j's are in case 1. So all choices for a_j are 1, which contribute 0. So the sum is 0. So there are no sequences where the sum is positive. So the answer is zero. So we can handle that as a special case if needed.

But back to the general case.

So, for each j, the possible delta is:

If h_j == h_{j+1}, delta is 0 for all choices. So the number of options is k, and for the generating function, this term is k * t^0.

If h_j != h_{j+1}, then the generating function is (1 * t^1) + ( (k-2) * t^0 ) + (1 * t^{-1} ) ).

So the generating function for such j is (t + (k-2) + t^{-1}).

So the problem becomes: multiply all the individual generating functions (for each j, either k * t^0, or t + (k-2) + t^{-1} ), then find the sum of coefficients for exponents >0.

So the key is to compute the product of these generating functions and sum the coefficients where the exponent is positive.

But how can we compute this efficiently?

Let me think. Let's denote the number of j's where h_j != h_{j+1} as m. For these m j's, each contributes a factor of (t + (k-2) + 1/t). For the other (n - m) j's, they contribute a factor of k. So the total generating function is (t + (k-2) + 1/t)^m multiplied by k^{n - m}.

So the problem reduces to computing the sum over s >0 of the coefficient of t^s in (t + (k-2) + 1/t)^m, multiplied by k^{n - m}.

But then, how to compute this sum?

Let me denote the polynomial as P(t) = (t + (k-2) + 1/t)^m. We need to compute the sum of coefficients of t^s for s >0.

But note that the exponents in P(t) can range from -m to +m, since each term in the expansion can contribute either +1, 0, or -1. So for each of the m factors, when multiplied, the exponents add up.

The sum over s>0 is the sum of coefficients of t^s for s =1, 2, ..., m.

But how can we compute this sum?

Let me consider that P(t) is equal to ( (t^2 + (k-2) t + 1 ) / t )^m. So P(t) = (t^2 + (k-2) t + 1)^m / t^m.

Thus, P(t) = (t^2 + (k-2) t +1 )^m / t^m.

So the generating function is (t^2 + (k-2) t +1 )^m multiplied by t^{-m}.

But expanding (t^2 + (k-2) t +1 )^m gives a polynomial of degree 2m. Then, multiplying by t^{-m} shifts the exponents down by m. So the exponents in P(t) range from -m to m.

But how can we find the sum of coefficients for exponents >0 in P(t)?

Alternatively, note that the sum of all coefficients in P(t) is (1 + (k-2) +1 )^m = k^m. Because substituting t=1 gives (1 + (k-2) +1 )^m = k^m.

The sum of coefficients for s>0 is equal to (sum of all coefficients) - (coefficient of s=0) - (sum of coefficients s<0).

But since the polynomial is symmetric in some way? Wait, let's see.

Wait, P(t) = (t + (k-2) + 1/t)^m. Let's see if the polynomial is symmetric. For example, consider replacing t with 1/t. Then:

P(1/t) = (1/t + (k-2) + t )^m = P(t). So P(1/t) = P(t). This implies that the coefficients of t^s and t^{-s} are equal. So the polynomial is symmetric around the exponent 0.

So the coefficient of t^s is equal to the coefficient of t^{-s}.

So the sum of coefficients for s>0 is equal to the sum of coefficients for s<0.

Thus, the sum of coefficients for s>0 plus the sum for s<0 plus the coefficient of s=0 is equal to k^m.

But since sum s>0 = sum s<0, then 2*sum s>0 + coeff(s=0) = k^m.

Thus, sum s>0 = (k^m - coeff(s=0)) ) / 2.

But we need the sum of coefficients s>0. So if we can compute the coefficient of s=0, then the answer is (k^m - coeff_0) ) / 2.

But wait, the sum of coefficients s>0 is (k^m - coeff_0) ) // 2. Because sum s>0 + sum s<0 = 2 * sum s>0 = (k^m - coeff_0).

So sum s>0 = (k^m - coeff_0) ) / 2.

Thus, the total answer is:

(total) = k^{n - m} * ( (k^m - coeff_0) / 2 )

So now, the problem reduces to computing coeff_0, which is the coefficient of t^0 in (t + (k-2) + 1/t)^m.

So the crux is to compute coeff_0, which is the central term in the expansion of (t + (k-2) + 1/t)^m.

How can we compute coeff_0 efficiently for m up to 2e5?

Let me think. Expanding (t + c + 1/t)^m, where c = k-2. The coefficient of t^0 is the number of ways to choose, for each of the m terms, either t (which contributes +1), c (0), or 1/t (-1), such that the sum of exponents is 0.

So each selection of exponents from the m terms must sum to zero.

This is equivalent to the number of balanced sequences of +1, 0, -1 steps over m steps that sum to zero.

Alternatively, each term contributes a delta of +1, 0, or -1. The sum of all deltas must be zero.

So the problem is to compute the number of ways to select m terms (each with three options) such that the sum of their deltas is zero.

This is equivalent to the number of sequences where the number of +1s equals the number of -1s, and the rest are 0s.

Let's formalize this. Let a be the number of +1s, b be the number of -1s, and c be the number of 0s. Then, a - b = 0 (sum to zero), and a + b + c = m. So a = b, and c = m - 2a.

So the possible a ranges from 0 to floor(m/2).

For each a in 0 to floor(m/2), the number of such sequences is:

C(m, a) * C(m -a, a) * (1)^a * (1)^a * ( (k-2) )^{m - 2a} }

Because:

- Choose a positions out of m for the +1s: C(m, a).

- Then choose a positions out of the remaining (m - a) for the -1s: C(m -a, a).

- The remaining (m - 2a) positions are 0s, each contributing (k-2) options.

Each +1 contributes a factor of 1 (the coefficient in the generating function for the term t, which is 1), and similarly for -1 (the 1/t term contributes 1). The 0s contribute (k-2).

So the total coeff_0 is sum_{a=0 to floor(m/2)} [ C(m,a) * C(m -a, a) * (k-2)^{m - 2a} } ]

So this sum is coeff_0. But computing this for m up to 2e5 is challenging. How can we compute this efficiently?

The key is to find a way to compute this sum modulo 998244353 quickly.

Let's denote S = sum_{a=0}^t [ C(m, a) * C(m -a, a) * (k-2)^{m-2a} }, where t = floor(m/2).

We need to compute this sum for m up to 2e5. How?

Let me consider that for each a, the term is:

term(a) = [ m! / (a! (a!) (m-2a)! )) ] * (k-2)^{m-2a} }

But this seems like a combinatorial coefficient. Alternatively, the term can be rewritten as:

C(m, a) * C(m -a, a) = m! / (a! (m -a -a)! a! )) ) = m! / ( a! a! (m-2a)! ) )

So it's the multinomial coefficient for choosing a items of one type, a items of another type, and the rest (m-2a) of a third type.

But perhaps there's a generating function approach here.

Alternatively, note that this sum S is the coefficient of x^m in the generating function ( (x + x^{-1} + (k-2)) )^m, but I'm not sure.

Alternatively, perhaps there's a recurrence formula for S.

But I'm not seeing it immediately. Let's think of possible dynamic programming approaches.

Let's consider building the sum S for each m up to some value. But since in our problem, m can be up to 2e5, we need an O(m) approach.

Alternatively, perhaps this sum can be expressed using the generating function (1 + x + x^{-1})^m, but I'm not sure.

Alternatively, notice that the sum S is the same as the sum over a of [ C(m, 2a) * C(2a, a) ) * (k-2)^{m-2a} } ] divided by something. Wait, perhaps not.

Wait, the term C(m, a) * C(m -a, a) can be rewritten as C(m, 2a) * C(2a, a). Because:

C(m, a) * C(m -a, a) = [ m!/(a! (m-a)! ) ] * [ (m -a)! )/(a! (m-2a)! ) ) ] = m! / (a! a! (m-2a)! )) 

Similarly, C(m, 2a) * C(2a, a) = [ m!/( (2a)! (m-2a)! )) ] * [ (2a)!/( a! a! )) ] = m!/( a! a! (m-2a)! )

So yes, the two expressions are equal. So term(a) = C(m, 2a) * C(2a, a) * (k-2)^{m-2a}.

So S is sum_{a=0}^t [ C(m, 2a) * C(2a, a) * (k-2)^{m-2a} } ]

This might help in finding a generating function or a recurrence.

Let me think of generating functions. Let's consider generating a term for each a: C(m, 2a) * C(2a, a) * x^{2a} * y^{m-2a} }, then set x =1 and y= (k-2).

But I'm not sure. Alternatively, perhaps the sum can be expressed as the coefficient of x^m in some generating function.

Alternatively, note that C(2a, a) is the central binomial coefficient, which is the number of ways to have a steps +1 and a steps -1. So for each a, the term involves choosing 2a positions (out of m) and then arranging a +1 and a -1 steps among them. The remaining (m-2a) steps are 0 steps, contributing (k-2) each.

But perhaps this is leading us into a combinatorial model where the sum S can be viewed as the number of ways to arrange m steps where each step is either a pair of +1 and -1 (a times) and (m-2a) 0 steps. But I'm not sure if this helps.

Alternatively, perhaps we can model the sum S using a generating function approach. Let's consider the generating function for S as follows:

For each step (each of the m factors), the contribution is (x + (k-2) + x^{-1} ), since each step can contribute +1 (x^1), 0 (x^0 multiplied by (k-2)), or -1 (x^{-1}).

Then, the generating function is (x + (k-2) + x^{-1})^m. The coefficient of x^0 in this expansion is exactly S.

So S is the coefficient of x^0 in (x + (k-2) + x^{-1})^m.

But how to compute this?

Hmm. Expanding (x + c + x^{-1})^m, where c = (k-2), and we need the coefficient of x^0.

Let me make a substitution y = x + x^{-1} + c. Then, the coefficient of x^0 in y^m is the sum S.

But how to compute this coefficient? Let's think of generating functions.

Alternatively, note that x + x^{-1} is 2 * cos(theta) if x = e^{i theta}. But this might be useful in a generating function approach using roots of unity. However, given that k can be up to 1e9, and m up to 2e5, perhaps this isn't feasible.

Alternatively, think of generating functions and recurrence relations. Let's denote f(m) as the coefficient of x^0 in (x + c + x^{-1})^m. Then, we can find a recurrence relation for f(m).

But how?

Let's think recursively. The coefficient of x^0 in (x + c + x^{-1})^m can be computed as follows:

(x + c + x^{-1})^m = (x + c + x^{-1}) * (x + c + x^{-1})^{m-1}

The coefficient of x^0 in this product is the sum over all possible exponents that multiply to give x^0.

So, when expanding (x + c + x^{-1}) * (x + c + x^{-1})^{m-1}, the coefficient of x^0 comes from:

- x (from the first term) multiplied by the coefficient of x^{-1} in (x + c + x^{-1})^{m-1}.
- c (from the first term) multiplied by the coefficient of x^0 in (x + c + x^{-1})^{m-1}.
- x^{-1} (from the first term) multiplied by the coefficient of x^1 in (x + c + x^{-1})^{m-1}.

But the coefficient of x^{-1} in (x + ... )^{m-1} is the same as the coefficient of x^1 in (x + ... )^{m-1} (due to symmetry, since substituting x → x^{-1} leaves the generating function the same). Let's denote f(m) as the coefficient of x^0 in (x + c + x^{-1})^m, and g(m) as the coefficient of x^1. Then, from the above, we have:

f(m) = c * f(m-1) + 2 * g(m-1)

But to find g(m), we need another recurrence.

Similarly, the coefficient of x^1 in (x + c + x^{-1})^m can be derived by expanding:

(x + c + x^{-1}) * (x + c + x^{-1})^{m-1}

The coefficient of x^1 is:

x * coefficient of x^0 in (m-1) term 

plus c * coefficient of x^1 in (m-1) term 

plus x^{-1} * coefficient of x^2 in (m-1) term.

But due to symmetry, the coefficient of x^{k} is equal to the coefficient of x^{-k}. So coefficient of x^2 in (m-1) term is equal to coefficient of x^{-2} in (m-1) term. But we are interested in x^1 in the product, so the third term contributes x^{-1} multiplied by coefficient of x^2 in (m-1) term, which is the same as coefficient of x^{-2} in (m-1) term. But I'm not sure how to model this.

Alternatively, perhaps we can model this with dynamic programming, keeping track of f(m) and g(m), where g(m) is the coefficient of x^1 in (x + c + x^{-1})^m.

Let's see:

For m=0: (x + c + x^{-1})^0 is 1. So f(0) = 1 (x^0 term is 1), g(0) =0.

For m=1: (x +c +x^{-1}) → the x^0 term is c → f(1) = c. The x^1 term is 1 → g(1) =1.

For m=2: (x +c +x^{-1})^2 → the x^0 term comes from x * x^{-1}, x^{-1} * x, and c^2. So 2*1 + c^2 → f(2)= 2 + c^2. The x^1 term comes from x*c, c*x, x^{-1}*x^2 (but x^2 is not present). Wait, this approach might get complicated.

Alternatively, let's think for m=1: coefficient of x^1 is 1.

For m=2: (x +c +x^{-1})^2 = x^2 + 2c x + (2 + c^2) + 2c x^{-1} + x^{-2}. So coefficient of x^1 is 2c, and coefficient of x^0 is 2 + c^2. So f(2) = 2 + c^2, g(2) = 2c.

For m=3: multiply (x +c +x^{-1}) by (x^2 + 2c x + (2 + c^2) + 2c x^{-1} + x^{-2}).

The x^0 term comes from:

x * x^{-1} (coefficient 2c) → 2c * 1 = 2c.

c * coefficient of x^0 in the previous term (2 + c^2) → c*(2 + c^2).

x^{-1} * coefficient of x^1 (2c) → 2c * 1 → 2c.

So total f(3) = 2c + c*(2 + c^2) + 2c = 4c + 2c + c^3 → 6c + c^3.

Similarly, coefficient of x^1 in m=3:

x * coefficient of x^0 (2 + c^2) → 1*(2 + c^2).

c * coefficient of x^1 (2c) → c*2c = 2c².

x^{-1} * coefficient of x^2 (1) → 1*1 =1.

So total g(3) = (2 + c²) + 2c² +1 = 3 + 3c².

Hmm. This seems to get complicated. But perhaps there's a recurrence relation between f(m) and f(m-1), f(m-2), etc.

Looking for a pattern, let's compute f(m) for small m:

m=0: f(0)=1.

m=1: f(1)=c.

m=2: f(2) = c^2 + 2.

m=3: c^3 + 6c.

m=4: c^4 + 12c² + 6.

Hmm, these look like the coefficients are related to the central terms of the expansion of (x + c + 1/x)^m.

But how to find a recurrence?

Let's see:

For m=0 → 1.

m=1 → c.

m=2 → 2 + c².

m=3 → c³ + 6c.

m=4 → 6 + 12c² + c^4.

m=5 → 20c + 30c^3 + c^5.

This seems similar to the sequence for the central terms of the trinomial coefficients, multiplied by some factors.

Alternatively, perhaps there's a generating function formula. For example, the generating function for f(m) would be the sum_{m=0}^\infty f(m) t^m = ?

But I'm not sure.

Another approach is to use generating functions and the fact that (x + c + 1/x) can be written as (x + 1/x) + c. Let's let d = x + 1/x. Then, (d + c)^m. Then, the generating function is (d + c)^m. We need the coefficient of x^0 in this expansion.

But d = x + 1/x, so (d + c)^m = sum_{k=0}^m C(m, k) d^k c^{m-k}.

The coefficient of x^0 in d^k is the number of ways to have x^{a} * x^{-b} where a + b = k and a - b =0 → a = b = k/2. So k must be even, and the coefficient is C(k, k/2) if k is even. Otherwise, it's zero.

So the coefficient of x^0 in (d + c)^m is sum_{k even} C(m, k) * C(k, k/2) * c^{m -k}.

Which is exactly the sum S that we are trying to compute.

So this doesn't help directly, but confirms that the sum is as we have.

So, the problem is to compute this sum S = sum_{a=0}^{floor(m/2)} C(m, 2a) * C(2a, a) * c^{m-2a} }, where c =k-2.

Now, for m up to 2e5, how can we compute this sum efficiently?

The answer is to precompute the factorials and inverse factorials modulo 998244353, and then compute each term of the sum and accumulate them.

But even that could be O(m) per test case, which is acceptable for m up to 2e5.

But let's see:

Each term in the sum is:

term(a) = C(m, 2a) * C(2a, a) * c^{m-2a}

But C(m, 2a) can be rewritten as m!/( (2a)! (m-2a)! )

C(2a, a) is (2a)!/(a! a! )

So the product is m!/( (2a)! (m-2a)! ) * (2a! )/(a! a! ) ) = m!/( (a! a! (m-2a)! ) )

But this is the same as the original term(a).

But combining, term(a) is (m! )/( a! a! (m-2a)! ) * c^{m-2a}

So we can precompute factorials and inverse factorials modulo 998244353, then compute for each a, this term.

But m can be up to 2e5, and for each a from 0 to m//2, we need to compute term(a) and sum them up.

The total number of terms per test case is O(m/2), which for m up to 2e5 is acceptable.

So the plan is:

1. Precompute factorials and inverse factorials up to 2e5.

2. For each test case:

   a. Compute m (number of positions where h_j != h_{j+1}).

   b. Compute c = k-2.

   c. Compute the sum S = sum_{a=0 to floor(m/2)} [ (m! / (a! a! (m-2a)! )) * c^{m-2a} } mod 998244353.

   d. Compute the answer as (k^m - S) * inv(2) mod MOD * k^{n - m} mod MOD.

   e. Also, handle cases where k=1, since in that case, all h_j must be 1, leading to m=0, and then S=1, so the answer is (1^0 -1)/2 * 1^{n} → (1-1)/2 *1 =0.

But wait, let's handle k=1:

If k=1, then all h_i must be 1. So for each j, h_j and h_{j+1} are equal, so m=0. So S = sum_{a=0}^0 term(0) = term(0) = (0!/(0!0!0! )) * c^0 = 1 (since 0! is 1, and c^0=1). So S=1. Then the answer is (1^0 - 1)/2 * 1^{n} = (1-1)/2 *1 =0.

Which is correct, since all a sequences are 1's, and shifting them gives the same sequence. So S' =S, which is not larger.

So the code needs to handle the case where c =k-2 can be negative (when k=1, c= -1). But modulo is handled properly.

Now, the steps:

Compute factorial and inv_factorial up to 2e5.

For each test case:

- Compute m by checking how many positions j have h[j] != h[j+1], where j runs from 1 to n (with j+1 being 1 for j=n).

- Compute c = (k-2) mod MOD.

- If m ==0:

   then the sum S is 1 (term(0)).

   So answer is (pow(k, m, MOD) - S) // 2 * pow(k, n -m, MOD) mod MOD.

But when m=0, k^m is 1. So (1 -1)/2 * ... =0.

But for m=0 and any k, since all j's are in case 1 (h_j == h_{j+1}), all a_j contribute 0. So the sum S' - S is zero. So no sequences are counted. So the answer is zero, which matches.

So, for m=0, the answer is zero.

But in code, even when m=0, the calculation (k^m - S)/2 * ... gives (1-1)/2 * ... =0.

So code can proceed normally.

So the code steps:

Read n, k, h.

Compute m:

m = 0

for j in 0 to n-1:

   current_h = h[j]

   next_h = h[ (j+1) % n ]

   if current_h != next_h:

      m +=1

Compute c = (k-2) mod MOD.

Compute pow_c = [1] * (m+1) where pow_c[i] is c^i mod MOD.

Compute pow_c up to m.

Compute S = sum_{a=0 to m//2} [ (comb(m, 2a) * comb(2a, a) ) * pow(c, m -2a) } mod MOD.

But comb(m, 2a) * comb(2a, a) can be computed as (m! ) / (a! a! (m-2a)! )).

But to compute this modulo MOD, we can precompute factorial and inverse factorial.

So the term is:

term = (fact[m] * inv_fact[a] % MOD) * inv_fact[a] % MOD * inv_fact[m - 2*a] % MOD * pow_c[m - 2*a] % MOD.

Sum all such terms for a from 0 to floor(m/2).

Once S is computed, the answer is:

answer = (pow(k, m, MOD) - S) * inv_two % MOD * pow(k, n -m, MOD) % MOD.

But since division by 2 is equivalent to multiplying by the modular inverse of 2, which is 499122177 in MOD 998244353.

So inv_two = 499122177.

But wait, the formula is (k^m - S) / 2. So since we are in modulo arithmetic, we multiply by the inverse of 2.

So yes, the code will compute ( (pow(k, m, MOD) - S ) * inv_two ) % MOD, multiply by pow(k, n - m, MOD), and then mod MOD.

Now, the code steps are:

- Precompute fact and inv_fact up to 2e5.

But wait, the maximum possible m is up to n, which is 2e5. So we need to precompute fact and inv_fact up to 2e5.

But for each term, the denominator is a! * a! * (m-2a)!. So the maximum a can be up to m//2, which is up to 1e5. So the maximum a! needed is up to 1e5, and m-2a can be up to m (2e5). So the precomputed fact and inv_fact need to be up to 2e5.

So the code will precompute fact and inv_fact up to 2e5.

Let's proceed to code.

But what about when m is 0? Then, the sum S is 1 (only a=0 is considered). But in the code, when m is 0, the loop will run for a=0, but m-2a=0. So pow_c[0] is 1.

Thus, the code will handle it.

Now, let's test the first example:

Input:

3 3

1 3 1

h = [1,3,1]

Check for j from 0 to 2 (0-based):

j=0: h[0]=1, next h[1] =3 → not equal. m increases.

j=1: h[1]=3, next h[2]=1 → not equal. m increases.

j=2: h[2] =1, next h[0] =1 → equal. no increment.

So m=2.

c=3-2=1.

So S is sum for a=0 and a=1.

a=0:

term = (2! ) / (0! 0! 2! ) * 1^2 → (2/(1*1*2)) *1 → (2/2) *1 =1.

a=1:

(2! )/(1! 1! 0! ) * 1^0 → (2/(1*1*1)) *1 → 2*1=2.

So S=1+2=3.

pow(k, m) =3^2=9.

(9-3)/2 =3. multiply by 3^{3-2} =3^1=3 → 3*3=9 → which matches the example.

So code works.

Another example: input 3 3 1 3 1 → m=2.

Yes, the code gives the correct answer.

Another test case: when m=1. For example, n=1, k=3, h=[1]. Then, j=0: h[0] =1, next j+1 mod 1 is 0. So h[0] == h[0], so m=0. Then answer is 0.

So code handles this.

Another test case: when k=1. Then, all h must be 1. So m=0. Answer is 0.

So the code will handle all these cases.

Now, the code can be written as follows.

First, precompute factorials and inverse factorials up to 2e5.

Then, for each test case:

- Read n, k.

- Read h as a list.

- Compute m.

- Compute c = (k-2) mod MOD.

- Precompute pow_c up to m.

- Compute sum S.

- Compute answer.

But how to handle pow_c?

We can compute c^ (m - 2a) as pow(c, m-2a, MOD). But for m up to 2e5, and per a up to m//2, this is O(m) per test case. But exponentiating for each a may be slow. So precompute pow_c up to m steps, so that pow_c[d] is c^d mod MOD.

Yes. So precompute pow_c as follows:

pow_c = [1] * (m +1)

for i in 1 to m:

   pow_c[i] = pow_c[i-1] * c % MOD

Then, for a given a, m-2a can be up to m. But since m is up to 2e5, this is manageable.

Thus, the code can precompute pow_c up to m.

Now, let's code.

So the code steps:

Precompute fact and inv_fact up to 2e5.

Read n, k.

Read h as a list of integers.

Compute m.

If k ==1:

   if all h are 1:

       answer is 0.

   else:

       impossible (since h can't have other values, but according to input constraints, h_i <=k. So if k=1, h must be all 1. So m=0, answer 0.

But code can proceed as before.

Compute c = (k-2) % MOD.

Compute pow_c for exponents from 0 to m.

Compute S.

Compute the answer as ( (pow(k, m, MOD) - S) * inv_two % MOD ) * pow(k, n -m, MOD) % MOD.

Thus, the code is as follows.
</think>

```python
MOD = 998244353
MAX = 2 * 10**5 + 5

# Precompute factorial and inverse factorial modulo MOD
fact = [1] * MAX
for i in range(1, MAX):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * MAX
inv_fact[MAX-1] = pow(fact[MAX-1], MOD-2, MOD)
for i in range(MAX-2, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

inv_two = pow(2, MOD-2, MOD)

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr +=1
    k = int(input[ptr])
    ptr +=1
    h = list(map(int, input[ptr:ptr+n]))
    ptr +=n
    
    # Compute m
    m = 0
    for i in range(n):
        j = (i+1) % n
        if h[i] != h[j]:
            m +=1
    
    if m ==0:
        print(0)
        return
    
    c = (k -2) % MOD
    
    # Precompute pow_c up to m
    pow_c = [1]*(m+1)
    for i in range(1, m+1):
        pow_c[i] = pow_c[i-1] * c % MOD
    
    S =0
    max_a = m //2
    for a in range(0, max_a +1):
        rem = m - 2*a
        if rem <0:
            continue
        # Compute term = C(m, 2a) * C(2a, a) * c^rem
        # which is fact[m] / (a! a! rem! ) 
        term = fact[m]
        term = term * inv_fact[a] % MOD
        term = term * inv_fact[a] % MOD
        term = term * inv_fact[rem] % MOD
        term = term * pow_c[rem] % MOD
        S = (S + term) % MOD
    
    km = pow(k, m, MOD)
    numerator = (km - S) % MOD
    part = numerator * inv_two % MOD
    part = part * pow(k, n -m, MOD) % MOD
    print(part)
    
if __name__ == "__main__":
    main()
```