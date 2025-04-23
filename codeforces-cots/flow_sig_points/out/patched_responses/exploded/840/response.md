<think>
Okay, let's see. The problem is about calculating the expected weight of each picture after m visits. Each visit, a picture is chosen with probability proportional to its weight. Then, if Nauuo likes the picture, its weight increases by 1, otherwise decreases by 1. We need to compute the expected value modulo 998244353.

Hmm, the constraints here are n and m up to 50. So even though the numbers are small, maybe a dynamic programming approach is feasible. Let's think about how the process works.

Each step, the choice of which picture to pick depends on the current weights. Then, the chosen picture's weight changes. So the state after each step depends on the current weights. But tracking all possible weights for each picture is impossible if m is 50 and each weight can vary by up to 50 steps (since each step changes by +1 or -1, but initial weights are up to 50, so after 50 steps, a picture could have weight as high as 50+50=100 or as low as 1-50, but since initial weight is at least 1, but subtracting could go negative, but maybe we can model it as possible negative values? Wait, but the problem says that the weight is non-negative. Wait, the problem statement says that the i-th picture has a non-negative weight. So during the process, the weights can't become negative. But how? Because, when a picture is not liked, subtracting 1 could take it to negative. But the problem states that when she does not like the picture, subtract 1. So what if the weight becomes zero and then subtract again? Does the problem allow that? The problem says that the initial weights are positive, but during the process, they can be adjusted. The problem's note in the first example shows that a picture's weight can be 2, then after subtraction becomes 1. So maybe during the process, the weights can be zero or even negative. But in the probability calculation, sum of all weights must be positive. Because if sum is zero, then division by zero. So how does the problem handle that? The problem statement says that the initial sum is the sum of w_i, which are all positive. So after m steps, the sum might change. But during the process, each step, when a picture is chosen, it's possible that after the update, the sum could be zero. But the problem statement says that there's at least one picture that Nauuo likes. So, for example, if all liked pictures' weights reach zero, but their sum is zero. Wait, but if a liked picture's weight is zero, then adding 1 would increase it. But if the sum of weights is zero, then when a picture is chosen, it's possible that the sum is zero, leading to division by zero. But the problem's constraints state that it's guaranteed that there's at least one liked picture, but perhaps during the process, sum can't become zero? Because even if a liked picture's weight is zero, when it's chosen (but sum is zero?), but that's impossible. Wait, this seems like a possible edge case. However, the problem's note in the second example has a single picture, which is liked. So each time, the weight increases by 1. So sum is 1, then 2, etc. So sum is always positive. So maybe the process ensures that the sum is always positive. Let me think: the initial sum is S = sum(w_i) >= 1 (since each w_i is at least 1). Each step, when a picture is chosen, if it's liked, add 1. So sum increases by 1. If not liked, subtract 1, so sum decreases by 1. But since sum starts at S >= 1, and each step, the sum could decrease by 1 (if the chosen picture is not liked). However, after m steps, the sum can't be zero? For example, if m is greater than S-1, then maybe sum can become zero. But in that case, the process would have a division by zero. So perhaps the problem guarantees that this scenario does not occur. But how? Because the problem statement does not mention that. So this suggests that we need to model the process even when the sum becomes zero, but according to the problem's setup, the sum can't be zero because there is at least one liked picture and their weights are being increased. Wait, no. Suppose there is a liked picture and a not liked one. Suppose the liked one's weight is 1, the not liked is 1. Then sum is 2. Then, the not liked is chosen, subtract 1. Sum becomes 1. Now, if the not liked is chosen again (but its weight is now 0, so subtract 1 would make it -1. But then sum is 0. Then next step, sum is zero. But the problem states that the probabilities are computed as weight_i / sum. So sum can't be zero. So how does the problem handle this?

Hmm, maybe the process ensures that the sum remains positive. But how? Because when a picture is not liked, subtracting 1 may lead to a situation where the sum is zero. But the problem's input requires that there's at least one liked picture, but the sum can still be zero. For example: suppose there's one liked picture with initial weight 1, and m is 2. The first step, the liked picture is chosen (prob 1/1), so weight becomes 2. Sum is 2. Then, in the next step, sum is 2. So sum is always positive. But if in some steps, the sum could be zero? Like, if a not liked picture is chosen and sum decreases by 1. Wait, but if sum was 1 (from previous step), and the not liked picture is chosen (sum becomes 0). Then, the next step's selection is impossible. So perhaps the problem's constraints implicitly ensure that sum remains positive. But how can we model that?

Alternatively, maybe during the process, when a picture is not liked, subtracting 1 may lead to its weight becoming negative, but the sum of all weights is still positive. For example, suppose two pictures: one liked with weight 3, one not liked with weight 2. Sum is 5. The not liked is chosen. Its weight becomes 1. Sum is 4. Then, not chosen again, becomes 0. Sum is 3. Then, chosen again, becomes -1. Sum is 2. So sum is still positive. So even if individual weights are negative, the sum is positive. So the process can proceed.

So for the problem's purposes, even if some weights are negative, the sum remains positive. So the selection probabilities are computed as weight_i / sum, which could be a negative probability? That's impossible. Wait, no, because the sum must be positive, and each weight_i can be negative, but sum is positive. So the probabilities are computed as (w_i)/sum. But some probabilities could be negative, which is impossible. Therefore, this scenario can't happen. Therefore, the problem must ensure that all weights are non-negative during the process. Wait, the problem statement says that the initial weights are non-negative. So during the process, when a picture is not liked, subtracting 1 could make its weight negative. Which would cause the sum to be sum of (some non-negative weights plus possible negative ones). But the sum might still be positive. For example, if one picture is liked (weight 2), another not liked (weight 1). Sum is 3. If the not liked is chosen, weight becomes 0. Sum is 2. Next step, if not liked is chosen again (weight 0), subtract 1, becomes -1. Sum is 1. So sum is positive, but the not liked's weight is -1. So the next time, the probability of choosing the not liked is (-1)/1, which is negative. Which is invalid. Therefore, the process as described is impossible, but the problem must have some constraints to prevent this.

This suggests that during the process, the weight of a not liked picture can't be decremented below zero. But the problem statement does not mention this. Therefore, perhaps the problem allows weights to become negative. But in that case, the probability could be negative, which is impossible. Therefore, the problem's setup must have some invariant that ensures that all weights are non-negative and sum is positive. But how?

Alternatively, maybe the problem allows the weight of a not liked picture to be subtracted even if it's zero, leading to negative weights, but the sum remains positive. But the probability calculation would have negative values for some w_i, which is impossible. Therefore, the problem's process must not generate negative weights, but the problem's statement does not specify any constraints to prevent this. Therefore, this is a possible ambiguity in the problem description. But the examples given in the problem notes include cases where a not liked picture's weight is subtracted. For example, the first sample input:

In the first example, the first picture is not liked. After the first visit, if the first picture is chosen (prob 2/3), its weight is 2-1=1, which is okay. The sum is 1+1=2, which is positive. Then, the second picture's weight is 1+1=2. So in this case, the process works.

But how to handle cases where a not liked picture's weight is subtracted to zero or below?

This is a problem. However, the problem statement doesn't mention anything about this. So perhaps the correct approach is to model the process as described, even if some weights go negative, and just compute the expected values, but in such a scenario, the probabilities would be invalid, leading to impossible situations. But the problem's examples do not have such cases, and the constraints are small. So perhaps the test cases are designed such that this scenario does not happen, so we can proceed under the assumption that during the process, all weights are non-negative. Alternatively, perhaps the problem allows weights to be negative but the sum is always positive, and the probabilities are computed as (w_i)/sum even if w_i is negative. But that would result in invalid probabilities (summing to 1, but some probabilities are negative). So this can't be. Therefore, perhaps the problem implicitly ensures that all weights are non-negative during the process.

Wait, but the problem's description says that the initial weights are positive. So after m steps, how can we ensure that all weights are non-negative? For liked pictures, their weight is increased each time they are chosen. So their weight can't decrease. For not liked pictures, each time they are chosen, their weight decreases by 1. So if a not liked picture is chosen enough times, its weight could become zero or even negative. For example, if a not liked picture's initial weight is 1, and it's chosen once, its weight becomes 0. If chosen again, it becomes -1.

This leads to a problem. However, perhaps the problem's constraints (like the initial weight and m being up to 50) allow such possibilities, and the code must handle them, even if the probabilities are computed as if they can be negative. But in that case, the sum is still positive because the sum starts as sum(w_i) >= 1 (since initial w_i are at least 1), and for each step, when a picture is chosen, if it's a liked one, sum increases by 1. If it's not liked, sum decreases by 1. So sum can be as low as (sum_initial - m). So if sum_initial >= m+1, then sum after m steps is >= 1, but if sum_initial < m+1, then sum could be zero or negative. Which would be impossible.

But the initial sum can be up to 50 * 50 = 2500 (since n is up to 50, each w_i up to 50). So for m=50, sum_initial can be 50, and m=50 steps, sum after all steps can be 50-50=0, leading to division by zero.

But the problem's input may not have such cases, but according to the problem statement, the code must handle all possible inputs as per the constraints.

This is a contradiction. So perhaps the problem ensures that the sum remains positive. But how? Because the problem's sample inputs include the first example where sum starts as 3, and after one step, sum is 2 or 3 (if the second picture is chosen, sum increases by 1 to 4). Wait, no. Let's recheck the first example.

First example input: n=2, m=1. a is [0,1]. w is [2,1]. So initial sum is 3. In the first visit, the first picture is chosen with probability 2/3. After subtracting 1, its weight becomes 1. Sum is 1+1=2. Or the second picture is chosen (probability 1/3), its weight becomes 2. Sum is 2+2=4. So sum after the step is 2 or 4. So sum is still positive.

But if in a step, the sum decreases by 1 each time, and m exceeds the initial sum, then sum can become zero. For example, initial sum is 1, m=2. Then, sum after two steps (if both steps are subtracting 1) would be 1-2 = -1, but sum can't be negative. So in this case, how is the process handled?

This suggests that there's an error in the problem statement, but perhaps the actual problem's test cases are designed such that during the process, the sum remains positive. Therefore, the code must proceed under the assumption that all steps are valid, and the sum remains positive.

So given that, how can we model the expected weights after m steps?

The key is to model the state transitions. The state is determined by the current weights of all pictures. However, even for n=50 and m=50, the possible states would be huge. For example, each picture's weight can change by up to m steps (each step +/- 1), but with m=50, each weight could vary up to 50 steps. So for each picture, the possible weight is up to initial +50 (if it's liked) or initial -50 (if not). But initial weights are up to 50, so the maximum possible weight after m steps is 100, and minimum could be 1-50= -49. So for each picture, possible weight values range from -49 to 100, which is 150 possible values. For n=50, the total number of possible states is 150^50, which is astronomically large. Therefore, a dynamic programming approach that tracks all possible states is impossible.

So we need a smarter approach. Let's think about the linearity of expectation. The expected value of each weight can be computed as the initial weight plus the expected number of times it was increased minus the expected number of times it was decreased. But wait, the process is that each time a picture is chosen, if it's liked, it's increased by 1. Otherwise, decreased by 1. So for each picture, the expected change after m steps is (number of times it was chosen and liked) * 1 plus (number of times chosen and not liked) * (-1). But for a liked picture, whenever it's chosen, it's increased. For a not liked picture, whenever it's chosen, it's decreased.

Wait, the like status is fixed. For each picture i, a_i is 0 or 1. So when a picture is chosen, if a_i is 1, then its weight increases by 1. If a_i is 0, its weight decreases by 1.

So the expected change for picture i is E[number of times chosen and a_i is 1] * 1 + E[number of times chosen and a_i is 0] * (-1). But since a_i is fixed, this can be rewritten as (if a_i is 1) E[number of times chosen] * 1, else E[number of times chosen] * (-1). Therefore, the expected value of the weight after m steps is:

E[w_i] = initial_w_i + (if a_i is 1: E[c_i] * 1) else E[c_i] * (-1)

where c_i is the number of times picture i was chosen during the m steps.

Therefore, the problem reduces to computing, for each i, the expected number of times it was chosen (E[c_i]), then apply the formula above.

So the key is to compute E[c_i] for each i. Once we have that, the expected weight is:

expected_weight_i = w_i_initial + (a_i * E[c_i] - (1 - a_i) * E[c_i])

Which simplifies to:

if a_i is 1: expected_weight_i = w_i_initial + E[c_i]
else: expected_weight_i = w_i_initial - E[c_i]

So now, the problem is to compute E[c_i] for each i.

But how to compute E[c_i]? Each choice in each step depends on the current weights, which are changing over time. So the choice probabilities are not independent between steps. This makes it a dependent process, and the expectation is not straightforward.

However, given the small constraints (m up to 50), perhaps we can model this with dynamic programming where the state captures the current sum and the current weight of each picture, but even that seems impossible for n=50. Wait, but for each step, the probability of choosing each picture depends on their current weights, which are influenced by previous steps.

An alternative approach is to model the expected values of the weights and the sum. Let's consider that at each step, the probability of choosing picture i is equal to its current weight divided by the current sum. However, since the sum changes with each step, this is non-trivial.

Another observation is that the process is linear. For example, the expected values of the weights can be modeled using linearity, perhaps leading to a system of equations that can be solved step by step.

Let me think: for each step, let's denote the expected value of the weight of each picture after k steps as E_k[i], and the expected sum S_k = sum(E_k[i] for all i). Then, during step k+1, the probability that picture j is chosen is E_k[j] / S_k. Then, when j is chosen, its weight increases by a_j (if a_j is 1, +1, else -1). So the expected change for each picture i in step k+1 is:

For picture i, the expected change is:

delta_i = (prob_j=i) * (a_i ? +1 : -1 )

Wait, no. If picture j is chosen, then only j's weight changes. So for the (k+1)th step, the expected change in picture i's weight is:

sum over all j (prob_j) * (if j == i then (a_j ? +1 : -1) else 0 )

So delta_i = prob_j=i * (a_i ? +1 : -1 )

Therefore, the expected weight after step k+1 is:

E_{k+1}[i] = E_k[i] + delta_i.

But E_k[i] is the expected weight before step k+1. The sum S_k is the sum of E_k[i], and the probability of choosing j in step k+1 is E_k[j]/S_k.

Therefore, the recurrence is:

E_{k+1}[i] = E_k[i] + (E_k[i] / S_k) * (a_i ? 1 : -1 )

But wait, no. Because the probability that j is chosen is E_k[j]/S_k, and when j is chosen, j's weight is changed. So for each j, the contribution to E_{k+1}[i] is:

If j != i: the change to i's weight is zero. So for j == i: the change is (a_i ? +1 : -1), multiplied by the probability that j is chosen.

Thus, E_{k+1}[i] = E_k[i] + (prob_i) * (a_i ? 1 : -1 )

Where prob_i is E_k[i]/S_k.

But S_k is the sum of all E_k[i], since the expected sum is the sum of expected weights. So S_k = sum_{i=1 to n} E_k[i].

Therefore, this gives us a way to model the expected weights step by step. We can compute the expected weights after each of the m steps using this recurrence.

So for each step from 0 to m-1:

Compute S = sum(E_current[i] for all i)

For each i:

E_new[i] = E_current[i] + (E_current[i] / S) * (a_i ? 1 : -1 )

But since we are dealing with probabilities and expectations, this recurrence should hold.

Yes, this seems correct. Because the expected value is linear, and even though the actual process is stochastic, the expected value can be modeled using this recurrence.

So this reduces the problem to maintaining the expected weights after each step, and after m steps, output the expected weight for each picture.

Now, the key is to compute these steps efficiently. For each step, we can compute the sum S, then for each picture, compute the delta based on E_current[i] / S multiplied by (a_i ? 1 : -1), and add that to E_current[i].

But how to handle the divisions modulo 998244353? Because all operations must be done modulo 998244353, and divisions must be handled using modular inverses.

So for each step, we need to compute S as the sum of E_current[i], modulo 998244353. Then, compute 1/S mod 998244353 (the modular inverse). Then, for each picture i, compute (E_current[i] * inv_S) mod 998244353, multiply by (1 if a_i else -1), add to E_current[i], mod 998244353.

Wait, but since the steps are multiplicative, and each step's S is the sum of E_current[i], which can be zero? Well, according to the problem's constraints, the sum S must be positive. Because the initial sum is sum(w_i) which is at least 1 (since all w_i are at least 1). Then, each step, when the sum is S, the next sum depends on which picture is chosen. For example, if a picture with a_i=1 is chosen, then the sum increases by 1. If a_i=0, it decreases by 1. But when modeling expected sum, the expected sum after each step is sum(E_new[i]) = sum(E_current[i] + delta_i) = sum(E_current[i]) + sum(delta_i).

Let's compute sum(delta_i) for each step:

sum(delta_i) = sum( (E_current[i]/S) * (a_i ? 1 : -1) )

= (sum (E_current[i] * (a_i ? 1 : -1 )) ) / S

But since S is the sum of E_current[i], we can compute this:

sum (E_current[i] * (a_i ? 1 : -1 )) = sum( a_i E_current[i] - (1 - a_i) E_current[i] )

= sum( (2 a_i - 1) E_current[i] )

But since a_i is 0 or 1, this is sum ( (if a_i is 1: E_current[i] else -E_current[i] ) )

So the sum of delta_i is (sum (a_i E_current[i] - (1 - a_i) E_current[i] )) / S 

= (sum ( (2a_i -1) E_current[i] )) / S 

But S is the sum of E_current[i].

So the sum of delta_i is [sum ( (2a_i -1) E_current[i] ) ] / S 

Which is equal to [sum ( (a_i * 2 -1 ) E_current[i] ) ] / S 

But sum ( (a_i * 2 -1) E_current[i] ) is sum ( (a_i E_current[i] * 2 - E_current[i] ) )

Which is 2 sum (a_i E_current[i] ) - sum E_current[i] 

But sum E_current[i] is S. So this is equal to 2 sum_a - S, where sum_a is sum (a_i E_current[i] )

So sum(delta_i) = (2 sum_a - S ) / S 

So the expected sum after the step is S + (2 sum_a - S ) / S 

= (S * S + 2 sum_a - S ) / S 

= (S (S -1) + 2 sum_a ) / S 

Hmm, but this is the expected sum after the step. However, in our recurrence, the sum after each step is the sum of E_new[i], which is sum (E_current[i] + delta_i) = S + sum(delta_i).

But according to the recurrence, sum(delta_i) is (sum (delta_i )) which is (2 sum_a - S ) / S 

So sum(delta_i) = (2 sum_a - S ) / S 

Therefore, the new sum is S + (2 sum_a - S ) / S 

= (S^2 + 2 sum_a - S ) / S 

= S + (2 sum_a - S ) / S 

But sum_a is sum (a_i E_current[i] )

But a_i is 0 or 1, so sum_a is the sum of the expected weights of the liked pictures.

So this shows that the sum can be updated based on sum_a and S.

But regardless, the recurrence for the expected sum is S_{k+1} = S_k + (2 sum_a - S_k ) / S_k 

But how to compute this? Because in each step, S_k is known (the sum of E_current[i] ), sum_a is the sum of E_current[i] for liked pictures.

But for each step, the sum after the step can be computed as S_{k+1} = S_k + (2 sum_a - S_k ) / S_k 

But since S_k is sum of E_current[i], which is known.

So the recurrence allows us to compute the sum at each step, but we need to compute it via the individual E_current[i] terms.

But given that the recurrence for E_{k+1}[i] can be computed for each i, perhaps we can proceed step by step, for each of the m steps, updating each E_current[i] as per the recurrence.

So the steps are:

Initialize E_current[i] = w_i for all i.

For each step in 1..m:

   Compute S = sum(E_current[i]) mod MOD

   Compute inv_S = modular inverse of S mod MOD

   Compute sum_a = sum(E_current[i] for i where a_i is 1) mod MOD

   For each i:

      prob_i = E_current[i] * inv_S % MOD

      delta = prob_i * (1 if a_i else -1)

      E_current[i] = (E_current[i] + delta) % MOD

But since we are working modulo MOD (998244353), all additions and multiplications must be done modulo MOD.

But wait, in modular arithmetic, subtraction can be handled by adding MOD and then taking mod. So for a_i=0, delta is -prob_i, which is equivalent to (MOD - prob_i) mod MOD.

Yes.

This approach is feasible for n=50 and m=50. Each step involves O(n) operations, and there are m steps. So for n=50 and m=50, that's 50*50=2500 operations. Which is acceptable.

So the plan is:

1. Precompute the modular inverses as needed. Since each step involves dividing by S, which is sum(E_current[i]), which changes each step, we need to compute the modular inverse of S for each step.

2. For each step, compute S, then compute inv_S = pow(S, MOD-2, MOD). Then, compute for each i, the delta as (E_current[i] * inv_S % MOD) * (1 or -1) based on a_i. Then, update E_current[i].

But wait, what if S is zero? Since the problem says that there is at least one picture that Nauuo likes, the initial sum is at least 1. But in the steps, the sum may become zero. For example, if during a step, S is 1 and a not liked picture is chosen (so sum decreases by 1 to 0). But according to our recurrence, S_{k+1} would be S_k + (2 sum_a - S_k)/S_k. If S_k is 1, sum_a is sum of liked pictures' expected weights. If all liked pictures' expected weights sum to 0, then sum_a is 0. Then (2*0 -1)/1 = -1. So S_{k+1} = 1 + (-1) = 0. But then inv_S would be undefined. So this suggests that in such cases, the sum can become zero, leading to division by zero in the modular inverse.

But according to the problem's constraints, this is impossible. Because there is at least one liked picture. So in the initial step, sum_a is at least 1 (since sum of initial w_i of liked pictures is at least 1). So during each step, the expected sum_a (sum of liked pictures' expected weights) is maintained.

But even if sum_a is positive, the sum S could become zero. For example, if sum_a is 1, and S is 2. Then, 2 sum_a - S is 2*1 - 2 = 0. So S_{k+1} = S_k + 0 / S_k → 2. So sum remains 2.

But I'm not sure. Let's think of an example where sum becomes zero.

Suppose n=1, m=1. a_i is 0. But the problem states that there is at least one liked picture. So this scenario is impossible. So the code can assume that there is at least one liked picture.

Thus, the sum S starts at sum(w_i) >= 1, and in each step, sum can increase or decrease based on the sum_a.

But with the recurrence, sum_a is the sum of the expected values of the liked pictures. So even if the actual process could have sum zero, the expected sum may not be zero. So perhaps the recurrence always gives S_k >=1.

Let's see:

In the first step, S_0 is sum(w_i) >=1.

sum_a_0 is sum(w_i for liked pictures) >=1 (since there's at least one liked picture).

So in step 0 (the first step), S_0 is >=1.

The new sum S_1 is S_0 + (2 sum_a_0 - S_0)/S_0.

= [ S_0^2 + 2 sum_a_0 - S_0 ] / S_0 

= [ S_0 (S_0 -1) + 2 sum_a_0 ] / S_0 

But sum_a_0 is >=1, and S_0 is sum of w_i >= sum_a_0 >=1.

So for example, if S_0 = sum_a_0 =1:

Then S_1 = (1*(0) + 2*1 ) /1 = 2.

If S_0 is 2, sum_a_0 is 1:

S_1 = (2*(1) + 2*1 ) /2 → (2 +2)/2=4/2=2.

Hmm, sum remains the same.

But if S_0 is 3, sum_a_0 is 1:

S_1 = (3*2 + 2*1 ) /3 → (6+2)/3=8/3=2.666...

But in modular arithmetic, this would be handled as fractions.

But the problem is that the recurrence could generate S steps where S_k is not an integer. But in the code, all variables are represented modulo 998244353 as integers. So for example, if S_k is 3 (mod MOD), then 8/3 mod MOD would be computed as 8 * inv(3) mod MOD.

But the code would compute S_k+1 correctly using the modular inverse.

Thus, in the code, for each step, compute S as the sum of E_current[i], then compute inv_S as pow(S, MOD-2, MOD). Then compute sum_a as the sum of E_current[i] where a_i is 1.

Then, for each i:

delta = (E_current[i] * inv_S % MOD) * (1 if a_i else -1) 

But in code, when a_i is 0, delta is subtracted. So in code, we can handle this as:

delta = (E_current[i] * inv_S) % MOD 

if a_i is 0:

   delta = (-delta) % MOD 

Then, E_current[i] = (E_current[i] + delta) % MOD 

So this approach should work.

Let's test this with the first sample input:

Sample 1:

n=2, m=1.

a = [0,1]

w = [2,1]

Initial E_current = [2,1]

Step 1:

S = 2 + 1 =3.

sum_a = 1 (since only the second picture is liked).

inv_S = 3^{-1} mod 998244353. Let's compute that. 3*332748118 = 998244354 ≡ 1 mod 998244353. So inv_S is 332748118.

For each picture:

Picture 0 (a_i=0):

prob = 2 * inv_S mod MOD = 2 * 332748118 mod MOD = 665496236 mod MOD. 

delta = -prob → MOD - 665496236 = 332748117.

E_new[0] = 2 + 332748117 mod MOD = (2 + 332748117) = 332748119 mod MOD.

Picture 1 (a_i=1):

prob = 1 * inv_S mod MOD = 332748118.

delta = + prob = 332748118.

E_new[1] = 1 + 332748118 = 332748119 mod MOD.

So after one step, the expected weights are both 332748119, which is 4/3 mod MOD. Which matches the sample output.

Yes. So the code would output these values.

Another sample: the second sample input:

Sample 2:

n=1, m=2, a=[1], w=[1].

Initial E_current = [1].

Step 1:

S=1. sum_a=1.

inv_S = 1^{-1} =1.

prob for the only picture is 1*1 =1.

delta = +1 (since a_i=1).

E_new =1 +1=2.

Step 2:

S=2. sum_a=2.

inv_S=499122177 (since 2 * 499122177 mod MOD = 998244354 mod MOD =1).

prob=2 * inv_S mod MOD = 2 * 499122177 mod MOD = 998244354 mod MOD →1.

delta =1. 

E_new =2 +1=3.

So after two steps, the expected weight is 3, which matches the sample.

Thus, the approach works for the samples.

So the code should follow this approach: iterate m times, each time compute the sum, inv_S, sum_a, and then compute each delta and update the expected values.

Now, in code:

We can represent E_current as a list of integers modulo 998244353.

Initialize E_current = list(w).

For each step in range(m):

   S = sum(E_current) % MOD

   inv_S = pow(S, MOD-2, MOD)

   sum_a = sum(E_current[i] for i in range(n) if a[i] ==1) % MOD

   temp = E_current.copy()

   for i in range(n):

      prob = (E_current[i] * inv_S) % MOD

      if a[i] ==1:

          delta = prob

      else:

          delta = (-prob) % MOD

      temp[i] = (E_current[i] + delta) % MOD

   E_current = temp

Wait, but this code is incorrect. Because during the step, the delta for each picture depends on the original E_current[i], not the updated ones. So the code must compute all the deltas based on the current state before any updates, then apply all deltas at once.

Yes. So during each step, all deltas are computed based on E_current (the state before the step), and then all E_current[i] are updated by adding delta[i]. So the code must compute all deltas first, then update each E_current[i].

Thus, in code:

for each step in m:

   compute S = sum(E_current) mod MOD

   inv_S = pow(S, MOD-2, MOD)

   compute delta for each i based on E_current[i], inv_S, and a[i]

   create new_E array where new_E[i] = (E_current[i] + delta[i]) mod MOD

   set E_current = new_E

Thus, in code:

for _ in range(m):

    S = sum(E_current) % MOD

    inv_S = pow(S, MOD-2, MOD)

    deltas = []

    for i in range(n):

        prob = E_current[i] * inv_S % MOD

        if a[i]:

            delta = prob

        else:

            delta = (-prob) % MOD

        deltas.append(delta)

    for i in range(n):

        E_current[i] = (E_current[i] + deltas[i]) % MOD

This way, all deltas are computed based on the original E_current, and then applied.

This is correct.

So the code can be written as:

Read n and m.

Read the a array.

Read the w array.

MOD = 998244353

E_current = list(w) mod MOD (though since w_i are given as integers, we can just take them modulo MOD).

for each step in m:

   compute S = sum(E_current) mod MOD.

   compute inv_S = pow(S, MOD-2, MOD)

   compute deltas for each i.

   update E_current.

Finally, output each E_current[i] mod MOD.

But since in each step the E_current is kept mod MOD, this should handle everything.

Testing this code against the samples:

Sample 1:

After processing one step, the E_current is [332748119, 332748119], which matches the sample.

Sample 2:

After two steps, E_current is [3], as expected.

Sample 3:

It's a larger example, but the code should compute it correctly.

Now, the code can be written as:

Read n, m.

a = list of integers (0 or 1).

w = list of initial weights.

MOD = 998244353

E_current = [x % MOD for x in w]

for _ in range(m):

    S = sum(E_current) % MOD

    inv_S = pow(S, MOD-2, MOD)

    deltas = []

    for i in range(n):

        prob = (E_current[i] * inv_S) % MOD

        if a[i]:

            delta = prob

        else:

            delta = (-prob) % MOD

        deltas.append(delta)

    for i in range(n):

        E_current[i] = (E_current[i] + deltas[i]) % MOD

print(' '.join(map(str, E_current)))

But wait, in the code, for each step, the sum is computed as sum(E_current). But in the steps, the sum may vary. For example, sum(E_current) after mod may not be the same as the actual sum. But since all operations are done modulo MOD, the code should correctly track the sum modulo MOD.

Yes. Because all additions and multiplications are done modulo MOD, the code correctly represents the expected values modulo MOD.

Therefore, this code should work correctly.
</think>

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
w = list(map(int, input().split()))
MOD = 998244353

e_current = [x % MOD for x in w]

for _ in range(m):
    s = sum(e_current) % MOD
    inv_s = pow(s, MOD - 2, MOD)
    deltas = []
    for i in range(n):
        prob = (e_current[i] * inv_s) % MOD
        if a[i]:
            delta = prob
        else:
            delta = (-prob) % MOD
        deltas.append(delta)
    for i in range(n):
        e_current[i] = (e_current[i] + deltas[i]) % MOD

print(' '.join(map(str, e_current)))
```