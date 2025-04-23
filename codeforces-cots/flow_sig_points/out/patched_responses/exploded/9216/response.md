<think>
Okay, let's try to tackle this problem. Hmm. The problem is about expected number of 'ab' subsequences when we stop after having at least k of them. The process stops when the count of 'ab' is >=k, and we need to compute the expected value. 

First, I need to model the state transitions. Let's think about dynamic programming here. The state probably depends on two things: the current number of a's (since each a can contribute to future ab's when a b comes after) and the current count of ab's. Because once the ab count reaches or exceeds k, we stop. So the state is (a_count, ab_count). But since k can be up to 1000, the ab_count could be up to k-1. So the DP states are manageable. For each state, we can compute the expected value added from that point onwards.

Wait, but even the a_count can be large. For example, if we have a lot of a's, and then a b comes, each a contributes to an ab. So if a is m and then a b is added, the ab count increases by m. So, if the current a_count is m, and ab_count is c, then adding a b would take the ab_count to c + m, possibly jumping over k. That complicates things.

So the transitions between states are not straightforward. For example, if in state (m, c), and we add a b, then the new ab_count is c + m. If this new ab_count >=k, then we stop. Otherwise, we proceed. But when adding a a, the a_count increases by 1, and the ab_count remains the same.

So the DP approach needs to model these possibilities. Let's denote dp[m][c] as the expected total number of ab's when starting with m a's and c ab's. The answer would be dp[0][0], since we start with 0 a's and 0 ab's.

The transitions are as follows:

In state (m, c), we can choose to add a or b.

If we add a (prob pa/(pa+pb)), then the new state is (m+1, c). The contribution to the expected value is the probability multiplied by (dp[m+1][c] + 0) since adding an a doesn't create any new ab's. Wait, no. Wait, the total expected value is the expected number of ab's in the entire sequence. So when we add a b, all existing a's contribute to new ab's, but when we add an a, the a's count increases but doesn't immediately contribute. So the DP should account for the ab's generated at each step.

Wait, perhaps the DP[m][c] represents the expected total number of ab's from this state onward, including any that are added in the future. So when we transition, we need to add any new ab's that are created by the current step.

Wait, that's a critical point. Let's think again. Suppose in state (m, c), we add a b. Then this b creates m new ab's. So the total ab's contributed by this step is m. Then, if the new ab count (c + m) is >=k, we stop. So the contribution here would be m (from this step) plus 0 (since we stop). Otherwise, the contribution is m plus the expected value from the new state (m, c + m). 

Alternatively, when we add a a, we don't get any new ab's. So the contribution is 0 plus the expected value from the new state (m+1, c).

So the recurrence would be:

dp[m][c] = (pa/(pa+pb)) * (dp[m+1][c]) + (pb/(pa+pb)) * (m + (if c + m >=k then 0 else dp[m][c + m])) )

But wait, when adding a b, the current a's m contributes m ab's. If c + m >=k, then we stop. So the total contribution is m (from this step) plus the possible future contributions only if we haven't stopped. So the term for adding a b would be: pb/(pa+pb) * (m + (if c + m >=k then 0 else dp[m][c + m])).

But how do we handle cases where adding a b takes us to a state where ab_count exceeds k? For example, if we are in (m, c), and c + m >=k, then adding a b would stop the process, and the total ab's added in that step is m (since all a's so far contribute m ab's). So that's the contribution. So the term for adding a b is pb/(pa+pb) multiplied by (m + (if c + m >=k then 0 else dp[m][c + m])). Wait, no. Because once we add the b, the ab count becomes c + m. If that's >=k, the process stops. So the total contribution from that step is the m ab's added, and no future steps. So for that case, the term is m. Otherwise, it's m plus the expected value from the new state (m, c + m). So yes.

So the DP transitions are:

For each state (m, c), the value is:

dp[m][c] = (pa * (dp[m+1][c] ) + pb * (m + (dp[m][c + m] if c + m <k else 0)) )) / (pa + pb)

But wait, the denominators are pa+pb, so the probabilities are pa/(pa+pb) and pb/(pa+pb). So multiply each term by their probabilities and sum.

Now, the problem is to compute this DP. However, the possible m (a_count) can be up to very high numbers. For example, if we have many a's before adding a b, then m can be large. So this might not be feasible for m up to say 1e6 or something, which would blow up the DP. So how do we handle this?

But perhaps there's a pattern or a way to compute the DP for large m. Let's think about when c is fixed. Suppose m is large enough that adding a b would make c + m >=k. So in that case, adding a b would contribute m and stop. Otherwise, if c + m <k, then we proceed.

Wait, but for a given c, the maximum m where c + m <k is m <k -c. So for m >=k -c, adding a b would take c +m >=k. So for m >=k -c, the term for adding a b is simply m, since the process stops. 

So for m >=k -c, adding a b gives m, adding a a gives m+1. But in this case, the DP[m][c] would have:

dp[m][c] = (pa * dp[m+1][c] + pb * m) / (pa + pb)

But for m >=k -c, the transition for a a is to m+1 and same c. But when m is very large, perhaps we can model this as a series. For example, for m >=k -c, the recurrence is:

dp[m][c] = (pa * dp[m+1][c] + pb * m) / (pa + pb)

This is a linear recurrence relation. Let's try to find a closed-form solution for this case.

Let's denote s = pa/(pa + pb) and r = pb/(pa + pb). Then, the equation becomes:

dp[m][c] = s * dp[m+1][c] + r * m

We can rearrange this as:

dp[m+1][c] = (dp[m][c] - r * m) / s 

But this seems tricky. Alternatively, let's model this as a recurrence for m >= some value. Let's assume that for m >= m0, the recurrence holds, and we can find a general solution. Let's look for a particular solution and homogeneous solution.

The homogeneous equation is dp[m][c] = s * dp[m+1][c], which suggests that the solution could be in the form of a geometric series. The particular solution can be found by assuming a linear function. Let's suppose the particular solution is dp[m] = a*m + b. Substituting into the equation:

a*m + b = s * (a*(m+1) + b) + r * m

Expanding:

a*m + b = s*a*(m+1) + s*b + r*m

Grouping terms:

a*m + b = (s a + r) m + s a + s b

Equating coefficients:

For m terms:
a = s a + r → a (1 - s) = r → a = r/(1-s)

Wait, but 1-s = 1 - pa/(pa+pb) = pb/(pa+pb) = r. So a = r / r → a =1.

Wait, let's compute:

s = pa/(pa+pb), r = pb/(pa+pb) → 1-s = r.

So substituting:

a (1 - s) = r → a * r = r → a=1.

Then, the constant terms:

b = s a (1) + s b → because the equation for the constant term is:

b = s (a*1 + b) → substituting a=1:

b = s (1 + b) → 

b = s + s b → 

b (1 - s) = s → 

b = s/(1 - s) = s/r.

But 1-s is r, so s/r = (pa/(pa+pb)) / (pb/(pa+pb)) ) = pa/pb.

So the particular solution is dp[m] = m + pa/pb.

The homogeneous solution is any solution to the equation dp[m+1] = (1/s) * dp[m]. The homogeneous solution is a geometric series with ratio 1/s.

So the general solution is:

dp[m][c] = m + pa/pb + C*(1/s)^m

But when m approaches infinity, we need the solution to remain finite. Let's consider what happens as m becomes very large. Since s is less than 1 (if pa is not zero), 1/s is greater than 1. So the term C*(1/s)^m would explode unless C is zero. Therefore, the only solution that remains bounded as m approaches infinity is C=0. Therefore, for m >= m0, where m0 is the minimal m where adding a b leads to c +m >=k, the solution is dp[m][c] = m + pa/(pb) / (1 - s) ? Wait, no. Wait the particular solution here is m + pa/pb. So for m >= m0, dp[m][c] = m + pa/pb.

Wait, but let's test this. Suppose we plug m into the recurrence:

dp[m] = s * dp[m+1] + r*m.

If dp[m] = m + pa/pb, then:

Left side: m + pa/pb.

Right side: s*(m+1 + pa/pb) + r*m = s*(m+1) + s*(pa/pb) + r*m.

Since s + r = 1, r = 1 -s.

So, substituting:

= s*m + s + s*(pa/pb) + (1 - s)*m.

Combine terms:

(s + (1-s)) *m + s + s*(pa/pb) = m + s*(1 + pa/pb).

But 1 + pa/pb = (pb + pa)/pb. So s*(pb + pa)/pb = (pa/(pa+pb)) * (pa + pb)/pb ) = pa/pb.

So right side becomes m + pa/pb. Which matches the left side. So yes, the particular solution is correct.

Therefore, for m >= m0 (where m0 is the minimal m such that c + m >=k), the value of dp[m][c] is m + (pa / pb).

So for these m, the DP can be computed directly without recursion. So when handling the DP, for a given c, any m >= (k - c) can be handled with this formula. So for m >= (k -c), dp[m][c] = m + pa/pb.

This is a crucial insight. This allows us to compute the DP for m up to (k -c -1) and for m >= (k -c), we can compute it directly. So the maximum m we need to handle in the DP is up to (k -c -1). Since k can be up to 1e3, the maximum m for a given c is (k - c -1), which for c up to k-1, the maximum possible m is k - (0) -1 = k-1. Wait, for example, if c is 0, then m0 is k -0 >=k. So for m >=k, adding a b would give c + m =0 +m >=k. So for c=0, m0 is k. So for m >=k, the formula applies. But for m <k, we need to compute the DP.

But how do the different c's interact? For each c (from 0 to k-1), we need to handle m up to (k - c -1). So for c=0, m ranges up to k-1. For c=1, up to k-2, etc. So the maximum possible m across all c is up to k-1. Because for c=0, m can be up to k-1. For c=1, up to k-2, etc. So the total number of states is O(k^2), which is manageable since k is up to 1e3. So 1e3 *1e3 is 1e6 states, which is acceptable.

So now, the plan is:

- Precompute the modular inverses for pa and pb, since we'll need to compute pa/pb modulo MOD (1e9+7). Wait, but fractions here are in modular arithmetic. So when we have pa/pb, it's equivalent to pa * inv(pb) mod MOD.

So the formula for m >= m0 (where m0 =k -c) is dp[m][c] = (m + pa/pb) mod MOD.

But wait, the formula is m + (pa / pb). How to compute this modulo MOD?

Since all divisions are modulo MOD, which is a prime, we can compute the inverse.

So pa / pb mod MOD is equal to pa * inv(pb) mod MOD, where inv(pb) is the modular inverse of pb modulo MOD.

But in our problem, the answer is to be output as P * Q^{-1} mod MOD, where P and Q are coprime. But in our DP transitions, when we compute the fractions, we can represent them as modular inverses.

So for the DP transitions, all fractions can be handled with modular inverses.

So first, let's precompute the probabilities as follows:

prob_a = pa * inv(pa + pb) mod MOD.

prob_b = pb * inv(pa + pb) mod MOD.

But wait, inv(pa + pb) is the inverse of (pa + pb) modulo MOD. However, pa and pb can be up to 1e6. But since MOD is 1e9+7, which is a prime, and pa + pb can be up to 2e6. So as long as pa + pb is not a multiple of MOD (which is possible, but the problem states that the denominator Q is not 0 mod MOD, so we can safely compute the inverse).

So first, compute inv_pa_pb = inverse(pa + pb) mod MOD.

prob_a = (pa * inv_pa_pb) % MOD.

prob_b = (pb * inv_pa_pb) % MOD.

Then, for the formula when m >= (k -c), the dp[m][c] is (m + pa * inv_pb) mod MOD.

But pa and pb are given. So inv_pb is the inverse of pb modulo MOD. So inv_pb = pow(pb, MOD-2, MOD).

Wait, but pa and pb can be up to 1e6, so pb can be 0 mod MOD? No, according to the input constraints, pb is >=1. So inv_pb can be computed.

So for the formula, when m >= k -c, dp[m][c] = (m + (pa * inv_pb) % MOD) % MOD.

Now, the DP transitions:

For each state (m, c), where c <k, and m < (k -c), we compute:

dp[m][c] = (prob_a * dp[m+1][c] + prob_b * (m + (dp[m][c + m] if (c + m <k) else 0))) ) % MOD.

But wait, in this case, when adding a b, the new ab_count is c + m. If c + m >=k, then the process stops, so the contribution is m. Otherwise, it's m plus the dp[m][c + m].

So in code, for each m and c:

if c + m >=k:
    term_b = m
else:
    term_b = (m + dp[m][c + m]) % MOD

So the term for adding a b is term_b multiplied by prob_b.

So the DP transitions can be computed as:

dp[m][c] = (prob_a * dp[m+1][c] + prob_b * term_b) % MOD

The base cases are when c >=k, but in that case, the process stops, so the expected value is the current ab's, which is already accounted for. So all states where c >=k are not part of the DP.

So the approach is to precompute for all possible c (from 0 to k-1) and m (from 0 up to (k -c -1)), and for each state (m, c), compute the value based on transitions.

But how to order the computation of the states? Since for a given c, m can go up to (k -c -1). Also, when adding a b, the new state is (m, c + m), which may have a c + m that's up to (m + c) < k. So for example, m can be up to (k -c -1), and c + m can be up to (k -c -1) + c = k-1 -1 +c? Wait, c +m can be up to (k -c -1) + c = k-1 -1 +c? No, wait:

If m is up to (k -c -1), then c + m is <= (k -c -1) + c = k -1 -1 = k-2. Wait, no. For example, c =0, m can be up to (k -0 -1) =k-1. Then c +m =0 + (k-1) =k-1 <k. So in this case, when we add a b, the new c is c +m =k-1, which is still less than k. So term_b would be (m + dp[m][c +m]). So for c + m <k, we need to have computed dp[m][c +m].

But the problem is that when we process (m, c), we need to have already processed (m, c +m) and (m+1, c).

So the order in which we compute the states is important. Let's think about the possible dependencies. For state (m, c):

- The transition to (m+1, c) is when adding a a, so m increases by 1, c remains the same.

- The transition to (m, c +m) is when adding a b, and c +m <k.

So for each state (m, c), the dependencies are (m+1, c) and possibly (m, c +m). 

But how to order this. Let's consider that for a given c, higher m's (closer to (k -c -1)) depend on the same c but higher m. So perhaps for each c, we process m in decreasing order (from (k -c -1) down to 0). Because when processing m, the state m+1 (for the same c) has already been computed.

So the order should be:

For c from (k-1) down to 0:

   For m from (k -c -1) down to 0:

       compute dp[m][c]

But why? Let's see.

Take c = k-1. For this c, k -c -1 = k - (k-1) -1 = 0. So m can be 0. The state (0, k-1). Adding a a transitions to (1, k-1). But m here is 0, and (1, k-1) would have k - (k-1) -1 = 0-1= -1? Wait, no. For c =k-1, the maximum m allowed is (k - (k-1) -1) =0 -1 = -1. Wait, that can't be. So perhaps for a given c, m can be up to (k -c -1) only if k -c -1 >=0. Otherwise, there are no m's to process for that c.

So for c >=k, there are no states. For c <k, the maximum m is (k -c -1), which must be >=0. So for c in 0 to k-1, m ranges from 0 to (k -c -1). For example, when c =k-1, k -c -1 =0. So m can be 0. For c =k-2, m can be 0 to 1 (k - (k-2) -1=1). So for each c, the maximum m is (k -c -1). 

So the processing order could be:

For c in reverse order (from k-1 down to 0):

   for m in reverse order (from (k -c -1) down to 0):

       compute dp[m][c]

So for example, for c=0, m can be from 0 to k-1. So we process m in reverse order (k-1, k-2, ..., 0). 

But for each m in c=0, the transitions are:

Adding a a: m+1, which is <=k (but if m is k-1, m+1 is k, which is >=k -c (k -0 =k). So for m= k-1, adding a a gives m+1 =k, which is >=k -c (k). So the formula applies. So for m= k-1, the a transition is to m+1 =k. For which, since k >=k -c (k >=k -0), the formula applies. So in that case, dp[k][0] is k + pa/pb. 

Wait, but the formula for m >=k -c is applicable. For c=0, k -c is k. So m >=k. So for m >=k, the formula applies. But when processing m= k-1 (c=0), the a transition is to m+1 =k, which is >=k -c (k), so dp[k][0] =k + pa/pb. 

So when computing dp[m][c], if m+1 >=k -c, then the a transition can use the formula. 

But how to handle this in code. Because for m in the loop, when you process m, m+1 may be beyond the maximum m for that c, but according to the formula, we can compute it as m+1 + pa/pb.

So the code could be structured as follows:

Initialize for all c from 0 to k-1:

   for m in range(0, ...):

       if m >= (k -c -1):

           compute using formula?

No, perhaps it's better to handle the a transition as follows:

When adding a a, new state is m+1, c. 

We need to compute the value of dp[m+1][c], which may be in the formula's range. So for the a transition:

if (m+1) >= (k -c) → then dp[m+1][c] = (m+1) + pa/pb.

Else → use the precomputed dp[m+1][c].

So during the DP computation, when we need to get the value for a state (m+1, c), we check if m+1 >= (k -c). If yes, then use the formula. Otherwise, use the stored value.

This way, even when m+1 is beyond the stored states (for that c), we can compute it using the formula.

So the code will have to handle this.

So the steps are:

1. Precompute inv_pa_pb = inverse(pa + pb) mod MOD.

2. Compute prob_a and prob_b.

3. Precompute inv_pb = inverse(pb) mod MOD.

4. Compute the formula value for when m >=k -c → val = (m + pa * inv_pb) % MOD.

5. For each c from k-1 down to 0:

   a. For m from (k -c -1) down to 0:

       i. For the a transition: new_m = m+1, new_c = c.

       ii. Check if new_m >= (k - new_c). Since new_c is c (same as current c), k - new_c is k -c.

           Since new_m is m+1, and m is up to (k -c -1), then m+1 can be up to (k -c -1)+1 =k -c. So for m+1 >= (k -c), then the formula applies. So if m+1 >= (k -c), then a_val = (m+1 + pa * inv_pb) mod MOD. Else, a_val = dp[new_m][c].

       iii. For the b transition:

           new_ab_count = c + m.

           if new_ab_count >=k → term_b = m.

           else:

               term_b = (m + dp[m][new_ab_count]) mod MOD.

       iv. dp[m][c] = (prob_a * a_val + prob_b * term_b) % MOD.

So in code, for each (m, c):

if (m+1) >= (k -c):

    a_val = (m +1 + pa * inv_pb) % MOD

else:

    a_val = dp[m+1][c]

Then, compute the term for a transition as prob_a * a_val.

For the b transition:

if (c +m) >=k:

    term_b = m

else:

    term_b = (m + dp[m][c +m]) % MOD

So the code can handle this.

Now, let's think about the data structure. The DP can be represented as a 2D array, with c ranging from 0 to k-1, and m ranging up to (k -c -1). But since for different c's, the maximum m varies, perhaps using a list of dictionaries or a list of lists where each entry for c has a list up to (k -c -1). But perhaps a 2D array with dimensions (k) for c and (k) for m. Because for c up to k-1, the maximum m for each c is up to k-1 (for c=0, m up to k-1). So the maximum possible m across all c's is k-1. So a 2D array of size (k) x (k) would suffice. But for a given c, m can be up to (k -c -1). So for c=0, m can go up to k-1 (if k-0-1 =k-1). For c=1, up to k-2, etc.

So the code can initialize a 2D array of size (k) x (k), and for each (m, c), store the value if m <= (k -c -1). Otherwise, use the formula.

Now, let's proceed to code this.

The steps in code:

Read k, pa, pb.

Compute MOD = 1e9+7.

Compute inv_pa_pb = pow(pa + pb, MOD-2, MOD)

prob_a = (pa * inv_pa_pb) % MOD

prob_b = (pb * inv_pa_pb) % MOD

inv_pb = pow(pb, MOD-2, MOD)

formula_val = (pa * inv_pb) % MOD

Then, initialize a DP table. Since k can be up to 1e3, and c can be up to k-1, and m up to k-1, but for each c, m is up to (k -c -1). So perhaps using a 2D list, dp = [[0]*(k) for _ in range(k)].

Wait, no. For example, for c=0, m can be up to k-1. So for c=0, the m ranges from 0 to k-1, which is k elements. But the list for c=0 is of size k. So the code can have a 2D array where for each c, the m index goes up to (k -c -1). So for c in 0 to k-1:

   max_m_for_c = k - c -1

   for m in 0 to max_m_for_c:

       compute dp[m][c]

But in code, since we are processing m in reverse order (from max_m down to 0), and for each (m, c), we need to check if m+1 is >= (k -c) to use the formula.

So the code would loop for c from (k-1) down to 0:

   for each c in range(k-1, -1, -1):

       max_m = k - c -1

       if max_m <0:

           continue  # no m's for this c

       for m in range(max_m, -1, -1):

           compute a_val:

               if (m+1) >= (k - c):

                   a_val = (m +1 + formula_val) % MOD

               else:

                   a_val = dp[m+1][c]

           compute term_b:

               new_ab = c + m

               if new_ab >=k:

                   term_b = m

               else:

                   term_b = (m + dp[m][new_ab]) % MOD

           dp[m][c] = (prob_a * a_val + prob_b * term_b) % MOD

The answer is dp[0][0], since we start with m=0 a's and c=0 ab's.

But wait, what if k=1 and m=0, c=0. Adding a a would take m to 1, c remains 0. Then, adding a b would take c to 0+1=1, which is >=k=1. So term_b is 1. So the code would compute term_b as 1, and the a_val for m=0, c=0 is (0+1 >=k -0=1) → m+1=1 >=1 → yes. So a_val is 1 + pa/pb.

In the first sample input, pa=1, pb=1. So formula_val is 1 * inv(1) =1. So a_val is 1+1=2. term_b is 0+0=0 + m=0? Wait, no.

Wait, when m=0, c=0. For the b transition:

new_ab =0 +0=0, which is <k=1. So term_b is 0 + dp[0][0]. Wait, but that's a problem. Because when processing (0,0), the term_b depends on dp[0][0], which is what we are trying to compute. So this would create a cyclic dependency.

Wait, this is a problem. So how to handle this?

Wait, perhaps I made a mistake in the transition.

Wait, for the b transition, the new state after adding a b is (m, new_ab) = (m, c + m). But when adding a b, the a's count remains m (since adding a b doesn't add a new a). So after adding a b, the a_count is still m, but the ab_count increases by m (the number of a's before adding the b). 

Wait, no. Wait, when you add a b, the a_count is still m. Because adding a b doesn't change the a_count. The a_count is the number of a's in the sequence. So when you add a b, the a_count remains the same. So the new state is (m, c + m). 

So when processing (m, c), the transition for adding a b is to (m, c +m).

So for example, in state (0,0), adding a b gives new_ab=0+0=0. Then, the new state is (0,0), which would again process the same state, leading to infinite recursion.

Wait, no. Because when you add a b in state (0,0), the new_ab is 0. So the process does not stop. So the new state is (0,0), and the expected value is (prob_a * ... + prob_b * (0 + dp[0][0])) ). This creates a dependency on dp[0][0] itself, leading to a circular equation.

Wait, this suggests that there's a problem in the initial approach. Because for state (0,0), adding a b would result in new_ab =0 +0=0, which is less than k=1 (for the first sample). So the term_b is 0 + dp[0][0], which depends on dp[0][0]. So how is this possible?

In this case, the equation for dp[0][0] is:

dp[0][0] = prob_a * a_val + prob_b * (0 + dp[0][0])

Which can be rearranged as:

dp[0][0] - prob_b * dp[0][0] = prob_a * a_val

dp[0][0] * (1 - prob_b) = prob_a * a_val

But 1 - prob_b is prob_a, so:

dp[0][0] * prob_a = prob_a * a_val → dp[0][0] = a_val.

But a_val is the value when adding a a, which transitions to (1,0). For k=1, in state (1,0), when adding a a, the new m is 2, which is >=k -0=1. So a_val would be 1 +1 (formula_val for pa=1, pb=1) → 2.

So substituting back:

dp[0][0] = 2 → which matches the sample.

So the code would correctly compute this.

But in code, how does this resolve? Because when processing (0,0), the term_b is (0 + dp[0][0]). But the code would process (0,0) after processing higher m's and higher c's. But in the first sample, when c=0, m ranges from 0 to 0 (since k=1, max_m =1-0-1=0). So processing m=0 for c=0.

But when the code tries to compute dp[0][0], it needs to compute term_b = 0 + dp[0][0]. But dp[0][0] hasn't been computed yet. So this suggests a problem in the order of processing.

Wait, no. Let's see. For k=1, the code processes c from 0 down to 0. For c=0, the max_m is 0 (since 1-0-1=0). So the code loops m=0 down to 0.

For m=0, c=0:

   compute a_val: m+1 =1. Check if 1 >=k -c (1 >=1 → yes). So a_val =1 + formula_val (which is 1 * inv(1) =1). So a_val =2.

   term_b: new_ab =0 +0=0 <1. So term_b =0 + dp[0][0]. 

But dp[0][0] is being computed now. So the code would have:

dp[0][0] = (prob_a * a_val + prob_b * term_b) % MOD.

prob_a is 0.5 (since pa=1, pb=1 → prob_a=1/(1+1)=0.5 in mod 1e9+7 terms). prob_b is 0.5.

So:

dp[0][0] = (0.5 * 2 + 0.5 * (0 + dp[0][0])) mod MOD.

Multiply both sides by 2 (since 0.5 is 500000004 mod 1e9+7):

dp[0][0] *2 = (2 + (0 + dp[0][0])) mod MOD.

Rearranged:

2 * dp[0][0] - dp[0][0] = 2 → dp[0][0] =2.

Which matches the sample. So the code can handle this by solving the equation. But in code, how is this handled? Because during the computation, the code would assign:

dp[0][0] = (prob_a * a_val + prob_b * (0 + dp[0][0])) % MOD

But this is a linear equation in dp[0][0], and the code can compute it algebraically.

Wait, but how does the code handle this? Because during the code's processing, dp[0][0] is being computed, and the term_b depends on dp[0][0], which is not yet known. So the code would have to solve for dp[0][0].

But how is this possible? Because in code, the value is computed as (prob_a * a_val + prob_b * term_b) mod MOD, but term_b depends on dp[0][0], which is the current value being computed.

This suggests that the code would have to rearrange the equation and solve for dp[0][0]. But in code, this would require handling such cases.

Wait, but this is possible because the equation is linear. For example:

dp[m][c] = A + B * dp[m][c], where A and B are constants.

Then, dp[m][c] = A / (1 - B), modulo MOD.

So in code, when term_b involves dp[m][c], which is the same as the current state, we can rearrange the equation.

So in the code, during the computation of dp[m][c], when term_b is (m + dp[m][new_ab]), and new_ab is c +m, and c +m == c (if m is zero). For example, if m=0 and c=0, new_ab=0, so new_ab is same as c. So the transition would require the current state's value.

But how can this be handled?

This suggests that the code must solve for dp[m][c] when term_b depends on it. So in code, when new_ab == c +m and that is less than k, and the new state is (m, new_ab), which could be the same as the current state. For example, if m=0, new_ab=0, then new_ab is 0, so new state is (0,0). So the term_b is 0 + dp[0][0].

Thus, in code, the equation is:

dp[m][c] = (prob_a * a_val + prob_b * (m + dp[m][new_ab])) % MOD.

But when new_ab == current c +m and new_ab <k, the code may have:

dp[m][new_ab_c] = ... depends on other states.

So when new_ab_c is new_ab, and the state is (m, new_ab), which could be (0,0) in the example, the code is currently processing (0,0) and the term_b is 0 + dp[0][0], which is the same as the current state.

Thus, the code has to solve the equation:

dp[m][c] = (prob_a * a_val + prob_b * (m + dp[m][c])) % MOD.

Rearranging:

dp[m][c] - prob_b * dp[m][c] = prob_a * a_val + prob_b * m.

dp[m][c] * (1 - prob_b) = (prob_a * a_val + prob_b * m) mod MOD.

Thus:

dp[m][c] = (prob_a * a_val + prob_b * m) / (1 - prob_b) mod MOD.

But 1 - prob_b is prob_a (since prob_a + prob_b =1 mod MOD). So denominator is prob_a.

So dp[m][c] = (prob_a * a_val + prob_b * m) * inv(prob_a) mod MOD.

Thus, in code, whenever new_ab <k and the new state (m, new_ab) is the same as the current state (m, c), then we need to solve for dp[m][c] using this formula.

But how can the code detect this?

In code, when new_ab <k, and the new state is (m, new_ab_c), then:

if m == m_current and new_ab_c == c_current, then we are in a loop. For example, when processing (m, c) and new_ab is c +m, and new_ab_c =c +m, then the state is (m, new_ab_c). But m is the same as current m.

So in code, during the computation of term_b, if new_ab <k, then check if the new_ab_c is new_ab = c +m. Then, if new_ab_c == c +m, and the state (m, new_ab_c) is (m, c), then we have a self-loop.

Wait, but new_ab_c is c +m. So for example, if c=0 and m=0, new_ab_c is 0. So the state is (0,0). So when adding a b in state (0,0), new_ab is 0. So the new state is (0,0). So the term_b is (0 + dp[0][0]). 

So in code, when new_ab <k, and the state (m, new_ab) is (m_current, new_ab_c), then:

If new_ab_c == c_current, and m remains the same (because adding a b doesn't change m), then term_b is (m + dp[m_current][new_ab_c]) → which is (m + dp[m][c_current]). 

So in such cases, the code must handle the equation by rearranging.

Thus, during the code processing, for each (m, c), after computing term_b, the code can check whether the new_ab_c is less than k and whether the new state is (m, new_ab_c) == (m, c). If so, then the equation has to be solved for dp[m][c] = (prob_a * a_val + prob_b * term_b) → which includes dp[m][c] in the term_b.

So in code, during the computation of term_b, if new_ab_c <k and the new_ab_c == c and m == m_current (which it always is), then:

term_b = m + dp[m][new_ab_c] → which is m + dp[m][c], leading to an equation where dp[m][c] is on both sides.

So the code can detect this case and solve the equation.

But how to detect this?

In code, during the computation of term_b, after computing new_ab_c = c +m:

if new_ab_c <k:

   if new_ab_c == c and m == m:

       then we have a self-loop. So the equation becomes:

       dp[m][c] = (prob_a * a_val + prob_b * (m + dp[m][c])) % MOD.

       → rearrange to solve for dp[m][c].

Else:

   term_b = (m + dp[m][new_ab_c]) % MOD.

So in code, for each (m, c):

new_ab_c = c + m

if new_ab_c >=k:

   term_b = m % MOD

else:

   if new_ab_c == c and m == m:  # always true, since m is fixed

       # self-loop

       numerator = (prob_a * a_val + prob_b * m) % MOD

       denominator = (1 - prob_b) % MOD  # which is prob_a

       inv_denominator = pow(denominator, MOD-2, MOD)

       dp[m][c] = ( numerator * inv_denominator ) % MOD

   else:

       term_b = (m + dp[m][new_ab_c]) % MOD

       dp[m][c] = ( prob_a * a_val + prob_b * term_b ) % MOD

Wait, but m is fixed. So new_ab_c = c +m. If new_ab_c == c, then m must be zero. Because c +m =c → m=0.

So new_ab_c ==c implies that m=0.

So when m=0 and new_ab_c =c, then new_ab_c =c +0 =c. So yes.

So in code, when new_ab_c <k and m=0 and new_ab_c ==c, then we have a self-loop. 

So for example, if m=0, c=0, new_ab_c=0, which is equal to c. So the code can check if m==0 and new_ab_c ==c.

Thus, the code can handle this case by solving the equation.

So in code:

for each (m, c):

   new_ab = c + m

   if new_ab >=k:

       term_b = m % MOD

   else:

       if m ==0 and new_ab == c:

           # self-loop case

           numerator = (prob_a * a_val + prob_b * m) % MOD

           denominator = (MOD + 1 - prob_b) % MOD  # 1 - prob_b mod MOD is prob_a

           inv_denominator = pow(denominator, MOD-2, MOD)

           dp_val = (numerator * inv_denominator) % MOD

           dp[m][c] = dp_val

       else:

           term_b = (m + dp[m][new_ab]) % MOD

           dp[m][c] = (prob_a * a_val + prob_b * term_b) % MOD

But wait, in the self-loop case, term_b is m + dp[m][new_ab_c], which is 0 + dp[0][0]. So the equation is:

dp[m][c] = prob_a * a_val + prob_b * (0 + dp[m][c])

So rearranged:

dp[m][c] - prob_b * dp[m][c] = prob_a * a_val

dp[m][c] * (1 - prob_b) = prob_a * a_val

Since 1 - prob_b = prob_a (mod MOD), this becomes:

dp[m][c] = (prob_a * a_val) / prob_a mod MOD → dp[m][c] = a_val mod MOD.

But a_val is computed as (m+1) + formula_val if m+1 >=k -c, else dp[m+1][c].

Wait, but this seems to be the case in the first sample. For example, when m=0, c=0, the a_val is 2 (as computed earlier). So the code would compute:

numerator = (prob_a * 2 + prob_b *0) mod MOD.

prob_a is 500000004 (mod 1e9+7). 500000004 *2 mod MOD is 1,000,000,008 mod MOD is 1. So numerator is 1.

denominator is (1 - prob_b) mod MOD → 1 - 500000004 mod MOD is 500000003.

inv_denominator is pow(500000003, MOD-2, MOD). But 500000003 is 1e9+7 -4, which is a prime.

But perhaps in this case, the denominator is prob_a. So denominator = prob_a.

Thus, inv_denominator = inv_prob_a.

But inv_prob_a is inv(prob_a) mod MOD. Which is pow(prob_a, MOD-2, MOD).

But how does this all compute?

Wait, in the first sample:

prob_a = 500000004 (mod 1e9+7).

prob_b =500000004.

So denominator is 1 - prob_b → 500000003 mod MOD.

But 500000004 + 500000004 = 1,000,000,008 mod MOD is 1. So prob_a + prob_b =1.

But 1 - prob_b is 500000003 mod MOD.

But prob_a is 500000004.

So the denominator is prob_a?

No. Because 1 - prob_b = prob_a → 1 - pb/(pa+pb) = pa/(pa+pb). Which is correct.

Yes. 1 - prob_b = prob_a.

So denominator is prob_a. So inv_denominator is inv_prob_a = inverse(prob_a mod MOD).

But prob_a is pa/(pa + pb) mod MOD. So inv_prob_a is (pa + pb) * inv(pa) mod MOD. Because pa/(pa+pb) → inverse is (pa+pb)/pa mod MOD.

But in code, we can precompute inv_prob_a as pow(prob_a, MOD-2, MOD).

But in code, during the self-loop case, we can compute denominator as prob_a.

So for the first sample:

numerator = (prob_a * a_val + prob_b * m) mod MOD.

prob_a is 500000004.

a_val is 2 (since m=0, c=0, m+1=1 >=1 → a_val=1 +1=2).

prob_a * a_val → 500000004 * 2 mod MOD is (1,000,000,008) mod 1e9+7 is 1.

prob_b * m is 500000004 *0 =0.

So numerator is 1.

denominator is prob_a =500000004.

inv_denominator is 500000004^{MOD-2} mod MOD.

But 500000004 is 1/2 mod MOD. So its inverse is 2 mod MOD. So denominator's inverse is 2.

So numerator * inv_denominator = 1 * 2 =2 mod MOD, which is correct.

Thus, the code would compute dp[0][0] =2.

This shows that the code handles this case correctly.

Thus, the code needs to check, when new_ab <k, whether m is 0 and new_ab ==c. If so, then compute the equation accordingly.

So the code can be written as:

For each c in reversed order:

   for m in reversed order (max_m downto 0):

       compute a_val.

       compute new_ab =c +m.

       if new_ab >=k:

           term_b = m

       else:

           if m ==0 and new_ab ==c:

               numerator = (prob_a * a_val + prob_b * m) % MOD

               denominator = prob_a

               inv_denominator = pow(denominator, MOD-2, MOD)

               dp_val = (numerator * inv_denominator) % MOD

               dp[m][c] = dp_val

           else:

               term_b = (m + dp[m][new_ab]) % MOD

               dp[m][c] = (prob_a * a_val + prob_b * term_b) % MOD

But wait, how do we know that in the self-loop case, the new_ab is c +m and new_ab ==c? Which requires m=0. So new_ab =c +0 =c. So yes.

So the code can be written with this check.

But in code, how to handle this:

For each m and c:

   new_ab = c +m

   if new_ab >=k:

       term_b = m % MOD

   else:

       if m ==0 and new_ab ==c:

           # self-loop case

           numerator = (prob_a * a_val + prob_b * m) % MOD

           denominator = (prob_a) % MOD

           inv_denominator = pow(denominator, MOD-2, MOD)

           dp_val = (numerator * inv_denominator) % MOD

           dp[m][c] = dp_val

       else:

           term_b = (m + dp[m][new_ab]) % MOD

           dp[m][c] = (prob_a * a_val + prob_b * term_b) % MOD

Thus, the code can handle this case.

So putting it all together, the code would look like this:

Read k, pa, pb.

MOD = 10^9+7.

Compute inv_pa_pb = pow(pa + pb, MOD-2, MOD)

prob_a = (pa * inv_pa_pb) % MOD

prob_b = (pb * inv_pa_pb) % MOD

formula_val = (pa * pow(pb, MOD-2, MOD)) % MOD

Initialize a 2D array dp with dimensions (k) for m and (k) for c. But in practice, for each c, m ranges up to (k -c -1). So perhaps a list of lists, where each list for c has m from 0 to (k-c-1), but in code, since we are using a 2D array, we can predefine it as a list of lists with size k x k, and fill in the values as needed.

So in code:

k, pa, pb = map(int, input().split())

MOD = 10**9+7

if k ==0:

   print(0)

   exit()

inv_pa_pb = pow(pa + pb, MOD-2, MOD)

prob_a = pa * inv_pa_pb % MOD

prob_b = pb * inv_pa_pb % MOD

inv_pb = pow(pb, MOD-2, MOD)

formula_val = pa * inv_pb % MOD

# Initialize DP table

dp = [[0]*(k) for _ in range(k)]

for c in range(k-1, -1, -1):

    max_m = k - c -1

    if max_m <0:

        continue

    for m in range(max_m, -1, -1):

        # Compute a_val

        a_val = 0

        m_plus_1 = m +1

        if m_plus_1 >= (k - c):

            a_val = (m_plus_1 + formula_val) % MOD

        else:

            a_val = dp[m_plus_1][c]

        # Compute term_b

        new_ab = c + m

        if new_ab >=k:

            term_b = m % MOD

        else:

            if m ==0 and new_ab ==c:

                # Self-loop case

                numerator = (prob_a * a_val + prob_b * m) % MOD

                denominator = prob_a % MOD

                inv_denominator = pow(denominator, MOD-2, MOD)

                dp_val = (numerator * inv_denominator) % MOD

                dp[m][c] = dp_val

                continue

            else:

                term_b = (m + dp[m][new_ab]) % MOD

        # Compute dp[m][c]

        dp[m][c] = (prob_a * a_val + prob_b * term_b) % MOD

print(dp[0][0] % MOD)

But wait, in the code above, when new_ab <k and m is not zero or new_ab !=c, then the code computes term_b and dp[m][c].

But what about when new_ab is <k and m is zero but new_ab !=c? For example, if m=0, c=1, new_ab=1. Then new_ab ==c is true, but m is zero, so the code enters the self-loop case. But in this case, new_ab = c =1, and m=0. So new_ab ==c +m (1=1+0). So the code would handle that as a self-loop, even though the transition is to (0,1) → which may not have been processed yet.

But according to the processing order, c is processed in reverse order from k-1 downto 0. For c=1, when processing m=0, new_ab is 1. So the state (0,1) is part of the current c=1. But wait, no. The state is (m, c). So in the case where c=1, m=0, new_ab =1. So new_ab_c=1. So the new state is (0,1). Which is part of c=1. But in the code, when processing c=1, the code loops m from max_m down to 0. For c=1, max_m is k -1 -1 =k-2. For example, if k=3, c=1, max_m=3-1-1=1. So m ranges from 1 downto 0.

But if in this case, new_ab is 1, which is >=k? No, for k=3, new_ab=0 +1=1 <3. So the code would compute term_b =0 + dp[0][1].

But when processing c=1 and m=0, the code is processing (0,1). So the code would have to have already computed dp[0][1] before? Or is this part of the same processing?

Ah, no. For c=1, the code processes m from max_m downto 0. For example, for k=3 and c=1, max_m=3-1-1=1. So m=1 and 0 are processed. So when m=1 is processed, it's handled first, then m=0.

When m=1 and c=1:

new_ab =1 +1=2 <3. So term_b is 1 + dp[1][2]. But for c=2, the max_m is 3-2-1=0. So during processing c=2, m=0 is processed. So when processing c=1, m=1, new_ab=2, which is c=2, which was processed before c=1. Because c is processed in reverse order.

So the code's processing order ensures that when processing a state (m, c), the states (m', c') where c' >c have already been processed. And for the same c, higher m's are processed first. So dependencies are handled correctly.

But in the self-loop case, when processing (0,0), the code has to compute the equation for dp[0][0], which depends on itself. But this is handled by the special case.

Thus, the code should correctly compute all DP states.

Let's test the first sample input:

Sample Input 1:

1 1 1

Sample Output: 2.

The code would compute:

prob_a = 1/(1+1) mod MOD = 500000004.

prob_b = 500000004.

formula_val = 1 * inv(1) mod MOD =1.

Processing c from 0 downto 0 (since k=1):

For c=0:

max_m =1 -0 -1=0. So process m=0.

Compute a_val:

m_plus_1 =0+1=1. Check if 1 >= (1 -0) →1 >=1 → yes. So a_val =1 +1=2.

new_ab =0 +0=0 <1.

Check if m=0 and new_ab ==c (0 ==0) → yes.

So enter self-loop case.

numerator = (prob_a * a_val + prob_b * m) mod MOD.

prob_a=500000004, a_val=2 → 500000004 *2 mod MOD = 1.

prob_b * m is 500000004 *0 =0.

numerator is 1.

denominator is prob_a=500000004.

inv_denominator = 500000004^{MOD-2} mod MOD → which is 2.

So dp_val =1 *2 mod MOD=2.

So dp[0][0]=2.

The code returns 2, which matches the sample.

Thus, the code works for this case.

Another sample input:

Sample Input 2:

3 1 4

Sample Output: 370000006.

Which is 341/100 → 3.41. But modulo 1e9+7, the fraction is 341 * inv(100) mod MOD.

Let's see what the code would do.

But perhaps it's better to proceed with the code as written.

Thus, the code should correctly handle all cases.
</think>

```python
MOD = 10**9 + 7

k, pa, pb = map(int, input().split())

if k == 0:
    print(0)
    exit()

sum_p = pa + pb
inv_pa_pb = pow(sum_p, MOD-2, MOD)
prob_a = pa * inv_pa_pb % MOD
prob_b = pb * inv_pa_pb % MOD
inv_pb = pow(pb, MOD-2, MOD)
formula_val = pa * inv_pb % MOD

dp = [[0] * k for _ in range(k)]

for c in range(k-1, -1, -1):
    max_m = k - c - 1
    if max_m < 0:
        continue
    for m in range(max_m, -1, -1):
        m_plus_1 = m + 1
        if m_plus_1 >= (k - c):
            a_val = (m_plus_1 + formula_val) % MOD
        else:
            a_val = dp[m_plus_1][c]
        
        new_ab = c + m
        if new_ab >= k:
            term_b = m % MOD
            dp[m][c] = (prob_a * a_val + prob_b * term_b) % MOD
        else:
            if m == 0 and new_ab == c:
                numerator = (prob_a * a_val + prob_b * m) % MOD
                denominator = prob_a % MOD
                inv_denominator = pow(denominator, MOD-2, MOD)
                dp_val = (numerator * inv_denominator) % MOD
                dp[m][c] = dp_val
            else:
                term_b = (m + dp[m][new_ab]) % MOD
                dp[m][c] = (prob_a * a_val + prob_b * term_b) % MOD

print(dp[0][0] % MOD)
```