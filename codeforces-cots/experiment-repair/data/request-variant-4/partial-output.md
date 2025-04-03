<think>
Okay, let's tackle this problem. Hmm, the problem statement is a bit complex. Let's parse it carefully.

So, we have n pictures. Each has a weight w_i. When Nauuo visits the website, one picture is displayed with probability proportional to its weight. Then, after each visit, if she likes the picture (a_i is 1), we add 1 to its weight; else subtract 1. We need to compute the expected weights after m visits. Then output each as a modulo inverse under 998244353.

Constraints: n can be up to 2e5, m up to 3000. Oh right, the m is manageable with O(m^2) per test case? Because 3e3 squared is 9e6, which is acceptable.

Wait, but with n up to 2e5, we can't process each element for each step in O(n) time. That would be 2e5 * 3e3 = 6e8 operations, which might be too slow. So we need a way to model the expected values without per-element O(1) operations each step.

Hmm, let's think about the process. For each visit, the probability of selecting each picture depends on their current weights. But the process is dynamic; each step affects the next probabilities.

But since m is up to 3000, perhaps we can model the expected values using some dynamic programming approach that tracks certain parameters, and updates them efficiently each step.

Let me think about the variables involved. Let's denote the expected value of the weight of picture i after k steps as E_i(k). We need to compute E_i(m) for all i.

But how do the steps affect these expectations? Each step, a picture is selected based on the current weights (which are random variables themselves). Then, the selected picture's weight is adjusted by +1 or -1 based on a_i.

Wait, but the problem requires that after each visit, the weight is updated. So each step's selection is dependent on the current state, which includes all previous modifications.

This seems tricky because each step's selection probability depends on the current sum of weights, which is changing over time. However, since m is up to 3000, perhaps we can model the expectations in a way that accumulates the necessary terms without tracking all possible states.

Another idea: the expected change for each picture can be modeled using linearity of expectation and dynamic programming. Let's see.

Let's denote S(k) as the sum of all weights at step k. Then, the probability of selecting picture j at step k is E(w_j(k)) / E(S(k)), where E(S(k)) is the sum of all E_i(k). Wait, but this is only valid if the events are independent, which they might not be. However, perhaps due to linearity of expectation, we can model the expectations correctly.

Wait, the expectation of the weight after each step is influenced by whether the picture was selected in that step. Let's model this step by step.

At each step k (from 0 to m-1), the current expected weights are E_i(k). Then, during step k+1:

- We select a picture j with probability proportional to E(w_j(k)) / sum_E(k), where sum_E(k) is the sum of all E_i(k). But wait, actually, the selection probability is based on the actual current weights, which are variables. However, when taking expectations, perhaps the expected value of the selection is the expectation of the probability. Hmm, this might be a point where linearity of expectation is applied.

Alternatively, perhaps during each step, the expected change to each picture's weight can be calculated by considering the probability that it was selected, multiplied by the change (either +1 or -1 based on a_i).

Wait, no. Because when a picture is selected, it's modified (either +1 or -1). So for each step, the weight of the selected picture changes by 1 (if a_j is 1, add 1, else subtract 1). The other pictures' weights remain the same.

Therefore, the expected value of E_i(k+1) is equal to E_i(k) plus the probability that picture i was selected in step k+1 multiplied by (a_i * 1 + (1 - a_i)*(-1)), i.e., a_i*2 -1. Because if a_i is 1, then when selected, we add 1, so delta is +1. If a_i is 0, subtract 1, delta is -1. So delta is (2a_i -1) when selected.

But wait, the selection happens based on the current weights at step k. So the probability that j is selected at step k+1 is E(w_j(k)) / sum_E(k), assuming that sum_E(k) is the sum of all E_i(k) at step k. Because in expectation, the sum of the weights is sum_E(k), and the selection probability for j is proportional to its expected weight.

But is this correct? Because the actual selection probability depends on the actual weights, which are random variables. But the expectation of the selection probability is the expectation of (w_j / sum_w), where sum_w is the sum of all weights. However, this is not the same as E(w_j)/E(sum_w) unless the variables are independent or something. But maybe in this problem, given the way the steps proceed, the expected value can be approximated by this approach. Or perhaps this is a valid approach due to linearity.

This seems like a possible approach. Let's try to model it.

Let me define for each step, the variables E_i(k) as the expected weight of picture i after k steps. Then, the sum_S(k) = sum(E_i(k)).

At each step, when we process the (k+1)th visit:

For each picture i, the probability that it was selected in this step is E_i(k) / sum_S(k). Then, after selection, its weight is updated by (2a_i -1). So the expected change to E_i(k+1) is:

E_i(k+1) = E_i(k) + (probability that i is selected) * (2a_i -1) + sum_{j≠i} (probability that j is selected) * 0.

But since for each j, the selection of j affects j's weight, and other pictures are not affected. Wait, no: if j is selected, then j's weight changes. So for each j, when j is selected, j's weight increases by (2a_j -1). So for all i, E_i(k+1) is equal to E_i(k) + (probability that j=i was selected) * (2a_i -1). Because when j is selected, only j's weight changes.

So for each step, the expected value for i is:

E_i(k+1) = E_i(k) + (E_i(k) / sum_S(k)) * (2a_i -1) * 1. Because in expectation, the contribution to E_i(k+1) is the probability that i is selected multiplied by the delta (2a_i -1).

Wait, but if i is selected, then its weight increases by (2a_i -1). So the delta is exactly (2a_i -1) if selected, 0 otherwise. So the expectation of the delta is (prob of being selected) * (2a_i -1). Therefore, yes, E_i(k+1) = E_i(k) + (prob of being selected) * (2a_i -1).

But the prob of being selected at step k+1 is E_i(k) / sum_S(k), because sum_S(k) is the sum of all E_i(k) (since each E_i(k) is the expected weight of i after k steps). So the sum of the weights' expected values is sum_S(k) = sum(E_i(k)).

Therefore, the recurrence is:

E_i(k+1) = E_i(k) + (E_i(k) / sum_S(k)) * (2a_i - 1) * 1.

Wait, but this seems like a linear recurrence. But sum_S(k) is also changing each step. Because sum_S(k+1) = sum_S(k) + sum over j of (prob j is selected) * (2a_j - 1).

But (2a_j -1) is 1 if a_j is 1, -1 otherwise. So sum_S(k+1) = sum_S(k) + sum_j ( (E_j(k)/sum_S(k)) * (2a_j -1) )

Hmm, that's interesting. Let's compute sum_S(k):

sum_S(k+1) = sum_i [ E_i(k+1) ]

= sum_i [ E_i(k) + (E_i(k)/sum_S(k)) * (2a_i -1) ) ]

= sum_E(k) + sum_i [ (E_i(k) * (2a_i -1)) / sum_S(k) ) ]

= sum_S(k) + (sum_i [ E_i(k)*(2a_i -1) ]) / sum_S(k)

But sum_i [ E_i(k)*(2a_i -1) ] is sum over all i of (2a_i -1)*E_i(k). Let's call this term T(k). Then sum_S(k+1) = sum_S(k) + T(k)/sum_S(k).

So sum_S(k+1) can be tracked as sum_S(k) + T(k)/sum_S(k).

But T(k) = sum_i (2a_i -1)*E_i(k) = sum_i [ (if a_i is 1, then 1, else -1) * E_i(k) ]

Which can also be written as sum_i ( a_i * 2 -1 ) * E_i(k) = sum_i ( (2a_i -1) ) * E_i(k).

So, during each step, we can compute T(k) as this sum.

So, the problem reduces to tracking E_i(k) for each i and sum_S(k) for each step.

But with n up to 2e5 and m up to 3e3, we need a way to compute this efficiently.

But considering that for each step, to compute E_i(k+1) for all i, we need to compute for each i the term (E_i(k) / sum_S(k)) * (2a_i -1), which can be done as a multiplicative factor per i.

But sum_S(k) is the same for all i in a particular step. So, for each step, we can precompute 1/sum_S(k), then multiply each E_i(k) by (1 + (2a_i -1)/sum_S(k)).

Wait, because E_i(k+1) = E_i(k) * (1 + (2a_i -1)/sum_S(k)) ). Because:

E_i(k+1) = E_i(k) + E_i(k) * (2a_i -1) / sum_S(k) )

= E_i(k) * (1 + (2a_i -1)/sum_S(k) )

Yes. So this is a multiplicative update for each i based on a_i.

This is a crucial insight. Because each E_i(k) is multiplied by a factor that depends on a_i and the current sum_S(k).

So, for each step, the update for E_i(k) can be expressed as:

E_i(k+1) = E_i(k) * (1 + (2a_i -1) / sum_S(k) )

Similarly, sum_S(k+1) = sum_S(k) + T(k)/sum_S(k), where T(k) = sum( (2a_i -1) * E_i(k) )

But T(k) can be rewritten as sum( (2a_i -1) * E_i(k) ) = sum( (2a_i -1) * E_i(k) ), which is the same as sum( (2a_i) * E_i(k) ) - sum( E_i(k) )

But sum( E_i(k) ) is sum_S(k). So T(k) = 2 * sum( a_i * E_i(k) ) - sum_S(k)

But sum( a_i * E_i(k) ) is the sum of E_i(k) for all i where a_i is 1. Let's call this sum_L(k). So sum_L(k) = sum( a_i * E_i(k) )

Then T(k) = 2 sum_L(k) - sum_S(k)

But sum_S(k) = sum_L(k) + sum( (1 - a_i) * E_i(k) ), since for a_i=0, (1 - a_i) is 1, and for a_i=1, it's 0.

Alternatively, sum_S(k) = sum_L(k) + sum_U(k), where sum_U(k) is the sum of E_i(k) for a_i=0.

So T(k) = 2 sum_L(k) - (sum_L(k) + sum_U(k)) ) = sum_L(k) - sum_U(k)

Which is the same as sum( (a_i * 1) * E_i(k) ) - sum( (1 - a_i) * E_i(k) ) = sum( [a_i - (1 - a_i)] * E_i(k) ) = sum( (2a_i -1)*E_i(k) ), which matches the original definition.

But perhaps tracking sum_L(k) and sum_U(k) could be useful. Because sum_L(k) is sum of E_i(k) for a_i=1, and sum_U(k) is sum for a_i=0.

But how?

Let's see: during each step, when we compute the new E_i(k+1), for each i, it's E_i(k) multiplied by (1 + (2a_i -1)/sum_S(k) )

So for a_i=1, the factor is 1 + (1)/sum_S(k) = 1 + 1/S.

For a_i=0, the factor is 1 - 1/S.

So, for each step, the sum_L(k+1) is sum over a_i=1 of (E_i(k) * (1 + 1/S) ), which is (sum_L(k)) * (1 + 1/S )

Similarly, sum_U(k+1) is sum over a_i=0 of (E_i(k) * (1 - 1/S) ), which is (sum_U(k)) * (1 - 1/S )

So sum_L(k+1) = sum_L(k) * (1 + 1/S )

sum_U(k+1) = sum_U(k) * (1 - 1/S )

Where S is sum_S(k) = sum_L(k) + sum_U(k )

This is a crucial observation. Because sum_L and sum_U can be tracked separately, and their updates are multiplicative factors based on the current sum_S.

So, if we track sum_L and sum_U for each step, and for each step, compute the new sum_L and sum_U based on the current S, then we can compute all the required values without tracking each individual E_i(k).

Because the E_i(k) for a_i=1 are all multiplied by (1 + 1/S) each step, and those for a_i=0 are multiplied by (1 - 1/S). So the sum_L and sum_U can be tracked as products of these factors over time.

Wait, this is possible because for all a_i=1, their E_i(k) are multiplied by the same factor each step, and similarly for a_i=0. So the sum of their E_i(k) can be tracked as sum_L and sum_U, which each have their own multiplicative factors.

If this is true, then the problem can be solved by tracking sum_L and sum_U for each step, and for each i, compute the product of their respective factors over all steps. Then, the final E_i(m) is the initial w_i multiplied by the product of factors for their a_i.

This would reduce the problem's time complexity to O(m), regardless of n, which is feasible for m up to 3e3.

Let me check this logic again.

At step k, for a_i=1:

E_i(k) = w_i * product_{t=0 to k-1} (1 + 1/S(t) )

Similarly, for a_i=0:

E_i(k) = w_i * product_{t=0 to k-1} (1 - 1/S(t) )

Because each step, the factor for a_i=1 is (1 + 1/S(t)), and for a_i=0 it's (1 - 1/S(t)).

So sum_L(k) = sum (w_i for a_i=1) * product_{t=0 to k-1} (1 + 1/S(t) )

sum_U(k) = sum (w_i for a_i=0) * product_{t=0 to k-1} (1 - 1/S(t) )

sum_S(k) = sum_L(k) + sum_U(k)

So, the idea is to precompute for all steps t, the factors (1 + 1/S(t)) and (1 - 1/S(t)), then compute the product for each a_i type (0 or 1), multiply by the initial sum of their weights, and then compute sum_L and sum_U step by step.

But how do we compute S(t) for each step?

S(t) is sum_L(t) + sum_U(t), which depends on the product of factors up to t-1.

So, the steps are:

Initialize sum_L_0 = sum of w_i where a_i=1.

sum_U_0 = sum of w_i where a_i=0.

S_0 = sum_L_0 + sum_U_0.

For each step from 0 to m-1:

Compute factor_L = (1 + 1/S(t))

factor_U = (1 - 1/S(t))

sum_L_{t+1} = sum_L_t * factor_L

sum_U_{t+1} = sum_U_t * factor_U

S_{t+1} = sum_L_{t+1} + sum_U_{t+1}

So, after m steps, sum_L_m is sum_L_0 multiplied by the product of (1 + 1/S(t)) for each t in 0..m-1.

Similarly for sum_U_m.

Then, for each picture i:

if a_i is 1:

E_i(m) = w_i * product_{t=0 to m-1} (1 + 1/S(t) )

if a_i is 0:

E_i(m) = w_i * product_{t=0 to m-1} (1 - 1/S(t) )

So, all pictures with a_i=1 have their expected values as their initial weight multiplied by the same product (product_L), and similarly for a_i=0 (product_U).

So, the solution is:

1. Compute sum_L and sum_U initially.

2. For each of the m steps, compute factor_L and factor_U for the current step, update sum_L and sum_U, and track S(t) for each step.

3. For each step, track the product_L and product_U. Wait no. Because for each step, the factors are applied to the sum_L and sum_U. So for the initial sum_L_0, after m steps, sum_L_m is sum_L_0 * product_L, where product_L is the product of (1 + 1/S(t)) for t from 0 to m-1.

Similarly for sum_U_m = sum_U_0 * product_U.

So, during each step, we can track the product_L and product_U. Then, for each i:

if a_i is 1: the expected value is w_i * product_L.

if a_i is 0: w_i * product_U.

But how do we compute product_L and product_U?

Wait, product_L is the product of (1 + 1/S(t)) for each step t in 0 to m-1.

But S(t) is sum_L(t) + sum_U(t), which depends on the previous steps.

So during the simulation of each step, we can track S(t) and compute the products.

So, the steps would be:

Initialize sum_L = sum of w_i where a_i=1.

sum_U = sum of w_i where a_i=0.

product_L = 1 (for zero steps), product_U = 1.

But wait, for each step from 0 to m-1:

At step t, S = sum_L + sum_U.

Compute factor_L = (1 + 1/S )

factor_U = (1 - 1/S )

Then, for the next step:

sum_L *= factor_L

sum_U *= factor_U

Also, track product_L and product_U as the product of factors up to each step. For example, after m steps, product_L is the product of all (1 + 1/S(t)) for t=0 to m-1.

Wait, but sum_L after m steps is sum_L_0 multiplied by product_L. So product_L is the product of (1 + 1/S(t)) for each step t=0 to m-1.

So, during each step, we can compute the current factor_L and factor_U, multiply them into the product_L and product_U variables, and then update sum_L and sum_U.

Wait, no. Because sum_L and sum_U are updated each step by multiplying by their respective factors. So product_L is the product of all factors for a_i=1 steps.

So, here's the plan:

Initialize sum_L0 = sum of w_i where a_i=1.

sum_U0 = sum of w_i where a_i=0.

product_L starts at 1 (for zero steps), but after m steps, it's the product of all (1 + 1/S(t)) for t in 0..m-1.

product_U is similarly the product of (1 - 1/S(t)).

So, for each step t in 0 to m-1:

Compute S = sum_L + sum_U.

Compute inv_S = 1 / S mod MOD (since all divisions are modulo 998244353).

Then, factor_L = (1 + inv_S) mod MOD.

factor_U = (1 - inv_S) mod MOD.

Multiply product_L by factor_L mod MOD.

Multiply product_U by factor_U mod MOD.

Then, update sum_L = sum_L * factor_L mod MOD.

sum_U = sum_U * factor_U mod MOD.

Wait, but no. Because sum_L and sum_U are being updated each step. So after each step, sum_L is sum_L_prev * factor_L, and sum_U is sum_U_prev * factor_U. So the product_L and product_U variables are not needed, because sum_L and sum_U already incorporate all the factors up to the current step.

Wait, but how do we compute the product_L and product_U for each individual element? Because for each picture i with a_i=1, the expected value after m steps is w_i multiplied by the product of (1 + 1/S(t)) for each step t. Similarly for a_i=0.

But sum_L after m steps is sum_L_initial * product_L. Because sum_L starts as sum_L_initial, and each step multiplies by factor_L. So product_L is the product of all (1 + 1/S(t)) factors for each step. So, for all a_i=1, their expected value is w_i * product_L. Similarly for a_i=0, product_U.

Yes! So the key insight is that the multiplicative factors for each a_i group are the same across all steps. So for all a_i=1 pictures, their expected value is their initial weight multiplied by product_L. For a_i=0, multiplied by product_U.

So during the m steps, we can compute product_L and product_U as the product of (1 + 1/S(t)) and (1 - 1/S(t)) for each step t. Then, for each i, multiply their initial weight by product_L or product_U based on a_i.

So the steps for the solution are:

1. Precompute sum_L_initial (sum of a_i=1's w_i) and sum_U_initial (sum of a_i=0's w_i).

2. For each step in 0 to m-1:

   a. Compute S = sum_L + sum_U.

   b. Compute inv_S = 1 / S mod MOD.

   c. Compute factor_L = 1 + inv_S mod MOD.

   d. Compute factor_U = 1 - inv_S mod MOD.

   e. Multiply product_L by factor_L mod MOD.

   f. Multiply product_U by factor_U mod MOD.

   g. Update sum_L = sum_L * factor_L mod MOD.

   h. Update sum_U = sum_U * factor_U mod MOD.

3. For each i:

   if a_i is 1: output (w_i * product_L) mod MOD.

   else: output (w_i * product_U) mod MOD.

Wait, but sum_L and sum_U are being updated each step. So during each step, S(t) is sum_L + sum_U, which is sum_L_prev * factor_L_prev + sum_U_prev * factor_U_prev.

But why does sum_L and sum_U need to be tracked? Because the product_L and product_U variables are the product of factors for each step. So during each step, the product_L and product_U variables are built by multiplying the factors for that step, regardless of the sum_L and sum_U. So sum_L and sum_U are needed to compute S(t) for each step's factors, but the product_L and product_U variables are separate.

Wait, no. Because the factors depend on S(t), which is sum_L + sum_U at step t. But in the code, during each step, we first compute S as sum_L + sum_U, then compute the factors (1 ± inv_S), multiply product_L and product_U by these factors, then update sum_L and sum_U by multiplying their current values by the factors.

Wait, but in the code:

Initially, sum_L is sum_L_initial, sum_U is sum_U_initial.

product_L starts as 1.

product_U starts as 1.

Then, for each step:

current S is sum_L + sum_U.

compute inv_S = 1 / S mod MOD.

factor_L is 1 + inv_S.

factor_U is 1 - inv_S.

product_L = product_L * factor_L mod MOD.

product_U = product_U * factor_U mod MOD.

sum_L = sum_L * factor_L mod MOD.

sum_U = sum_U * factor_U mod MOD.

But after this, for the next step, the sum_L and sum_U have been updated. So the next S is sum_L + sum_U again.

Yes. So product_L and product_U are the product of factors from all steps, and sum_L and sum_U are updated each step to track the current sum.

But the product_L and product_U variables are what we need to compute the expected values for each picture.

So this approach will have O(m) time for the steps, and O(n) time for processing the initial and final steps. Since m is up to 3e3, and n up to 2e5, this is acceptable.

So the plan is:

- Precompute sum_L_initial and sum_U_initial.

- For m steps, compute S, inv_S, factors, and update product_L, product_U, sum_L, sum_U.

- For each picture, multiply their initial w_i by product_L or product_U based on a_i, modulo 998244353.

But how to compute inv_S? Since MOD is a prime (998244353), we can compute the modular inverse of S using pow(S, MOD-2, MOD).

But S can be zero? No, because the problem statement says that the initial sum of weights is at least 1 (since there is at least one a_i=1, and their weights are positive). Also, during steps, sum_L and sum_U are multiplied by factors that could lead to sum_S decreasing. Wait, but in the problem statement, there's a constraint that the sum of initial weights is at most 998244352 - m. Also, the process modifies weights by adding or subtracting 1 per step. So during the m steps, the sum can decrease, but the problem statement ensures that the initial sum is such that after all m steps, the sum remains non-negative. Wait, but how?

The problem statement says that the sum of initial weights is <= 998244352 - m. So after m steps, the sum can increase by up to m (if all steps add 1), but 998244352 - m + m = 998244352, which is allowed. But during steps, the sum could decrease. However, in the problem statement's input constraints, it's guaranteed that the initial sum is such that after m steps, all weights remain non-negative. Because the problem says "It is guaranteed that the sum of all the initial weights does not exceed 998244352 -m."

But when a_i=0 and the picture is selected, its weight decreases by 1. So during the steps, a picture's weight can become zero or even negative. But the problem says that the initial weight is at least 1. But during steps, a weight can go negative. However, the problem's note says that in the first example, after a step, the weight can be 1 (for a_i=0, subtract 1 from 2 to get 1). But wait, the initial w_i is 2, and after a step, it becomes 1. Then, for subsequent steps, it can become 0, then -1, etc. But how does that affect the probabilities? Because the weight is supposed to be non-negative. But the problem statement allows the weight to become negative. Hmm, but the problem says that the expected value may be negative, but we have to output it modulo 998244353.

But in our approach, we are tracking expected values, which could be negative. However, the modulo operation takes care of that.

But in the problem's sample input 1, after one visit, the first picture's weight is 1 (if selected) or 2 (if not). The expected value is (2/3)*1 + (1/3)*2 = 4/3. So the expected value is correct regardless of the actual possible weights.

So our approach correctly models the expected value even if individual weights go negative. Because expectation is linear, and the process is modeled in terms of expected values, not actual possible outcomes.

So back to the code.

The code will need to:

1. Read n and m.

2. Read a array (0s and 1s).

3. Read w array (positive integers).

4. Compute sum_L_initial = sum of w_i where a_i is 1.

   sum_U_initial = sum of w_i where a_i is 0.

5. Initialize product_L = 1, product_U = 1.

   sum_L = sum_L_initial mod MOD.

   sum_U = sum_U_initial mod MOD.

6. For each of the m steps:

   a. Compute S = (sum_L + sum_U) % MOD.

   b. Compute inv_S = pow(S, MOD-2, MOD).

   c. Compute factor_L = (1 + inv_S) % MOD.

   d. Compute factor_U = (1 - inv_S) % MOD.

   e. product_L = (product_L * factor_L) % MOD.

   f. product_U = (product_U * factor_U) % MOD.

   g. sum_L = (sum_L * factor_L) % MOD.

   h. sum_U = (sum_U * factor_U) % MOD.

7. For each i in 0..n-1:

   if a[i] == 1:

      res = (w[i] * product_L) % MOD.

   else:

      res = (w[i] * product_U) % MOD.

   print(res)

But wait, why do we update sum_L and sum_U in each step? Because sum_L and sum_U are needed for the next step's S computation.

Yes. Because each step's S(t) is the sum of sum_L and sum_U after the previous step's updates.

But in code, sum_L and sum_U are updated after the product_L and product_U are multiplied. Wait, no. Let's see the order in code:

For each step:

Compute S as sum_L + sum_U.

Compute factors.

Update product_L and product_U by multiplying factors.

Then, update sum_L and sum_U by multiplying factors.

So the next step's S is sum_L * factor_L + sum_U * factor_U.

Which is sum_L_new + sum_U_new.

Which is correct, as sum_L and sum_U are updated.

Yes.

So this approach works.

Now, let's test this approach against the sample input.

Sample 1:

Input:

2 1

0 1

2 1

sum_L_initial = 1 (a_2 is 1, w_2=1).

sum_U_initial = 2 (a_1 is 0, w_1=2).

Step 0:

S = 2 + 1 = 3.

inv_S = 1/3 mod 998244353 = 332748118 (since 3 * 332748118 mod MOD is 1).

factor_L = 1 + 332748118 = 332748119 mod MOD.

factor_U = 1 - 332748118 = -332748117 mod MOD = 665496235 (since MOD is 998244353, adding MOD to make it positive).

product_L becomes 332748119.

product_U becomes 665496235.

sum_L becomes 1 * 332748119 mod MOD = 332748119.

sum_U becomes 2 * 665496235 mod MOD = 1330992470 mod 998244353. Let's compute 1330992470 - 1*998244353 = 332748117. So sum_U is 332748117.

But after this step, sum_L + sum_U is 332748119 + 332748117 = 665496236. But for this step, it's the first and only step.

Now, for each picture:

Picture 1: a_i=0, so product_U is 665496235. w_i is 2. So 2 * 665496235 mod MOD = 1330992470 mod MOD = 1330992470 - 1*998244353 = 332748117. But the sample output is 332748119.

Wait, this suggests that something is wrong.

Wait, the sample output for the first test case is 332748119 for both pictures. Let's see.

Wait, in the first sample, after 1 step:

For the first picture (a_i=0), product_U is (1 - 1/S(0)) where S(0) is 3. So 1 - 1/3 = 2/3. So product_U is 2/3. So 2 * 2/3 =4/3 mod MOD is 4/3 which is 4 * inv(3) mod MOD. inv(3) is 332748118. 4 * 332748118 mod MOD is (4 * 332748118) mod MOD. Let's compute 332748118 *4 = 1330992472. 1330992472 mod 998244353: 1330992472 - 1*998244353 = 332748119. So that's correct.

For the second picture (a_i=1), product_L is (1 + 1/3) =4/3. 1 *4/3 =4/3 mod MOD is same as above.

But according to the code:

product_L after step 0 is 332748119, which is (1 + 1/3) mod MOD. Because 1/3 mod MOD is 332748118. 1+332748118=332748119.

product_U after step 0 is 665496235, which is (1 - 1/3) mod MOD. 1-332748118 = -332748117 mod MOD. Adding MOD: 998244353 - 332748117 = 665496236. Wait, but 332748118 is 1/3 mod MOD. So 1 - 332748118 is (1 - 1/3) mod MOD. Which is 2/3 mod MOD. 2/3 mod MOD is (2 * inv(3)) mod MOD = 2 * 332748118 mod MOD = 665496236 mod MOD.

But in code, factor_U is (1 - inv_S) mod MOD. For inv_S = 332748118, 1 - 332748118 = -332748117. mod MOD is 998244353 - 332748117 = 665496236.

But in the code's step:

product_U is initially 1. Then multiplied by 665496236. So product_U becomes 665496236.

But in the first sample, the expected value for a_i=0 is 2 * (2/3) =4/3. But according to code, product_U is 665496236, which is 2/3 mod MOD. So 2 * 665496236 mod MOD is (2 * 665496236) mod MOD. Let's compute that: 2 * 665496236 = 1330992472. mod 998244353: 1330992472 - 1*998244353 = 332748119. Which matches the sample output.

So the code is correct.

Another sample: sample 2.

Input:

1 2

1

1

sum_L_initial =1, sum_U_initial=0.

m=2 steps.

Step 0:

S =1 +0 =1.

inv_S =1.

factor_L=1+1=2 mod MOD.

factor_U=1-1=0 mod MOD.

product_L becomes 2.

product_U becomes 0.

sum_L becomes 1*2=2 mod MOD.

sum_U becomes 0 *0=0.

sum_L is 2, sum_U is 0.

Step 1:

S =2 +0=2.

inv_S = pow(2, MOD-2, MOD) = 499122177.

factor_L = 1 + 499122177 = 499122178 mod MOD.

product_L becomes 2 * 499122178 mod MOD. Let's compute 499122178 *2 = 998244356 mod MOD is 998244356 - 998244353 =3. So product_L is 3.

product_U remains 0.

sum_L is 2 *499122178 mod MOD = 998244356 mod MOD =3.

sum_U is 0 *0 =0.

After 2 steps, the product_L is 3, product_U is 0.

The picture has a_i=1, so output 1 *3 =3 mod MOD. Which matches the sample.

So the code works.

So now, the code can be written as follows.

We need to read the input, sum the initial sum_L and sum_U. Then process m steps, each time updating product_L and product_U, sum_L and sum_U.

Then, for each i, multiply the initial w_i by product_L or product_U based on a_i.

But since sum_L and sum_U can be large, but we compute everything mod 998244353.

But note that during the steps, sum_L and sum_U can be 0. For example, in sample 2, sum_U_initial is 0. So during step 0, sum_U is multiplied by 0, so sum_U remains 0.

But when sum_L and sum_U are 0, their sum would be 0, which would make S=0, leading to division by zero. But according to the problem constraints, the initial sum is >=1, and during steps, the sum can't reach zero because:

Wait, the problem says that the initial sum of weights is such that after m steps, the sum doesn't exceed 998244352. But during steps, the sum can decrease. For example, if all steps are a_i=0, then sum_S would decrease by 1 each time. But the problem's input ensures that the initial sum is such that after m steps, the sum is still positive? Or does it not?

The problem says: "It is guaranteed that the sum of all the initial weights does not exceed 998244352 -m."

But during steps, each step can add or subtract 1 to the sum. The sum after m steps could be sum_initial + (number of steps where a picture is liked) - (number of steps where a picture is disliked).

But the problem's input constraint is that sum_initial + m <= 998244352.

But during steps, the sum can be sum_initial + (sum (delta for each step)). Each delta is either +1 or -1.

But the problem statement allows sum_initial to be up to 998244352 -m, meaning that even if all steps add 1 (sum_initial + m <= 998244352 -m + m = 998244352), which is allowed.

But during steps, sum_S can become zero. But according to the code, the sum_L and sum_U are computed modulo MOD. So sum_S can be zero modulo MOD, but in reality, the actual sum could be MOD *k. However, this would not be possible given the constraints. But the problem statement does not guarantee that sum_S is non-zero at each step. So what happens if sum_S is zero mod MOD during a step?

In such a case, inv_S would be zero's inverse, which is impossible. But according to the problem's input constraints, the initial sum is at least 1. But during steps, sum_S can reach zero modulo MOD.

But how to handle that? For example, if sum_S becomes MOD, then S mod MOD is 0, which would make inv_S undefined.

But according to the problem's input constraints, the sum of initial weights is at least 1 (since there's at least one picture with a_i=1 and initial weight >=1). However, during the steps, sum_S could be MOD, leading to S mod MOD being zero. This would cause a division by zero error in the code.

But how to handle this?

The problem statement's input constraints say: "the sum of all the initial weights does not exceed 998244352 -m".

But MOD is 998244353. So the initial sum plus m can be at most 998244352, so sum_initial + m <= 998244352. So during steps, the sum can increase by m, but sum_initial + m is 998244352. So sum_S can never reach 998244353, which is MOD. So sum_S during all steps is at most 998244352. Which is MOD-1. So modulo MOD, sum_S is sum_S's actual value. So inv_S is the modular inverse of sum_S mod MOD, which is valid since sum_S is >=1 and < MOD.

So during the code's steps, sum_S is always between 1 and MOD-1. Therefore, inv_S is always computable.

Thus, the code is safe.

Therefore, the code can proceed as outlined.

So now, the code:

Read n, m.

Read a list.

Read w list.

sum_L = sum(w[i] for i in range(n) if a[i] ==1) % MOD.

sum_U = sum(w[i] for i in range(n) if a[i] ==0) % MOD.

product_L =1

product_U =1

for each step in range(m):

    S = (sum_L + sum_U) % MOD

    inv_S = pow(S, MOD-2, MOD)

    factor_L = (1 + inv_S) % MOD

    factor_U = (1 - inv_S) % MOD

    product_L = (product_L * factor_L) % MOD

    product_U = (product_U * factor_U) % MOD

    sum_L = (sum_L * factor_L) % MOD

    sum_U = (sum_U * factor_U) % MOD

Then, for each i in 0..n-1:

    if a[i] ==1:

        res = (w[i] * product_L) % MOD

    else:

        res = (w[i] * product_U) % MOD

    print(res)

But wait, in the code, sum_L and sum_U are updated after the product_L and product_U are updated. But the product_L and product_U are for the current step's factors. Let's see:

In each iteration, the steps are:

Compute S based on current sum_L and sum_U.

Compute factors.

Multiply product_L and product_U by factors.

Update sum_L and sum_U by multiplying by factors.

Yes. So the product_L and product_U accumulate the factors for each step.

So this is correct.

Testing this code against the samples.

Sample 3:

Input:

3 3

0 1 1

4 3 5

sum_L_initial =3+5=8.

sum_U_initial =4.

m=3 steps.

But the steps are a bit long to compute manually.

But the code should handle it.

So the code should output the correct results.

So the code seems correct.

Now, let's implement it in Python.

But note that for large n (2e5), we need to read the inputs efficiently.

In Python, we can read the inputs via input().split(), but need to process them as integers.

So, the code would be as follows:

MOD = 998244353

n, m = map(int, input().split())

a = list(map(int, input().split()))

w = list(map(int, input().split()))

sum_L = 0

sum_U = 0

for ai, wi in zip(a, w):

    if ai ==1:

        sum_L += wi

    else:

        sum_U += wi

sum_L %= MOD

sum_U %= MOD

product_L = 1

product_U = 1

for _ in range(m):

    S = (sum_L + sum_U) % MOD

    inv_S = pow(S, MOD-2, MOD)

    factor_L = (1 + inv_S) % MOD

    factor_U = (1 - inv_S) % MOD

    product_L = (product_L * factor_L) % MOD

    product_U = (product_U * factor_U) % MOD

    sum_L = (sum_L * factor_L) % MOD

    sum_U = (sum_U * factor_U) % MOD

res = []

for ai, wi in zip(a, w):

    if ai ==1:

        res.append( (wi * product_L) % MOD )

    else:

        res.append( (wi * product_U) % MOD )

print(' '.join(map(str, res)))

But wait, sum_L and sum_U are computed modulo MOD initially, then during steps, the factors are multiplied modulo MOD, and the sum_L and sum_U are kept modulo MOD.

But the product_L and product_U are also computed modulo MOD.

This should correctly compute the product for each step.

Let's test this code with an executable snippet.

```python
def test_program(input_stream, output_stream):
  MOD = 998244353

  n, m = map(int, input_stream.readline().split())
  a = list(map(int, input_stream.readline().split()))
  w = list(map(int, input_stream.readline().split()))

  sum_L = 0
  sum_U = 0
  for ai, wi in zip(a, w):
      if ai == 1:
          sum_L = (sum_L + wi) % MOD
      else:
          sum_U = (sum_U + wi) % MOD

  product_L = 1
  product_U = 1
  current_sum_L = sum_L
  current_sum_U = sum_U

  for _ in range(m):
      S = (current_sum_L + current_sum_U) % MOD
      inv_S = pow(S, MOD-2, MOD)
      factor_L = (1 + inv_S) % MOD
      factor_U = (1 - inv_S) % MOD

      product_L = (product_L * factor_L) % MOD
      product_U = (product_U * factor_U) % MOD

      current_sum_L = (current_sum_L * factor_L) % MOD
      current_sum_U = (current_sum_U * factor_U) % MOD

  result = []
  for ai, wi in zip(a, w):
      if ai == 1:
          res = (wi * product_L) % MOD
      else:
          res = (wi * product_U) % MOD
      result.append(res)

  print(' '.join(map(str, result)), file=output_stream)

import io

TEST_CASES = [{
    "input": """\
2 1
0 1
2 1\
""",
    "output": """\
332748119
332748119\
""",
}, {
    "input": """\
1 2
1
1\
""",
    "output": """\
3\
""",
}, {
    "input": """\
3 3
0 1 1
4 3 5\
""",
    "output": """\
160955686
185138929
974061117\
""",
}, ]

for i, test_case in enumerate(TEST_CASES):
    in_stream = io.StringIO(test_case["input"])
    expected_output = test_case["output"].rstrip()

    out_stream = io.StringIO()
    test_program(in_stream, out_stream)
    real_output = out_stream.getvalue().rstrip()

    assert real_output == expected_output, \
        f'Test case {i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}'

print('Tests passed 😎')
```

RUN_SNIPPET
```text
Traceback (most recent call last):
  File "<stdin>", line 109, in <module>
AssertionError: Test case 0 failed.
Expected: '332748119\n332748119'
Got: '332748119 332748119'
```