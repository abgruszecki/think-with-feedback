<think>
Okay, let's try to solve this problem. So, the problem is about calculating the probability that after n swaps (where each swap is the middle cup swapping with either the left or right cup with equal probability), the key ends up in the middle cup. And n is the product of all elements in the array given. Then, we need to output this probability as a reduced fraction mod 1e9+7.

First, let's understand the process. The key starts in the middle. Each turn, Barney swaps the middle cup with one of the other two, each choice with 50% chance. After n swaps, we need to find the probability that the key is back in the middle.

Hmm. Let's model the possible states. The key is under a cup. But since the cups are arranged in a line, the possible positions are left, middle, right. Wait, but the key starts in the middle. Wait, no: the key is under a cup, and when swaps happen, the key moves with the cup. Wait, no: the problem statement says that the key always remains in the cup it was at the start. Wait, wait, wait. Oh, wait, no. Let me re-read that part.

Ah, the problem says: "the key always remains in the cup it was at the start". Oh right! So the key is under the cup, and when the middle cup is swapped with another, the key moves to the new position. Because the cup moves. Wait, no. Let's think: initially, the key is under the middle cup. Then, each swap is between the middle cup and one of the others. So, for example, if in the first swap, the middle swaps with the left, then the middle cup is now the one that was left. So the key is now under the left cup. Wait, but the key was under the middle cup. So after swapping, the key moves with the cup. So the position of the key depends on which swaps happened.

Wait, perhaps the problem can be modeled by tracking the position of the key. Let's see. The key starts in the middle. Each swap is between the current middle and either left or right. After each swap, the new middle is the swapped cup. So, the key's position can be either in the middle (if it wasn't moved) or in the swapped position.

Wait, let's model each step:

Suppose the current arrangement is cups arranged as [A, B, C], with B being the middle. The key is under B. Then, during a swap, B is swapped with A (left) or C (right). Let's say we swap B with A. Then the new arrangement is [B, A, C]. The key is now under A, which is the new middle cup. Wait, no. Because the swap is between the current middle and the left or right. So after swapping, the middle becomes the other cup. For example, swapping middle (B) with left (A) results in the new arrangement being [B, A, C], and the new middle is A. But the key is under B (the original middle) which is now the left cup. So the key's position is now left. Then, in the next step, the middle is A, so swapping could be with B (left) or C (right).

Hmm. So the key's position can be in one of three positions: left, middle, right. But since the middle changes each time, maybe it's better to model the state as the position of the key relative to the current middle. Or perhaps model the transitions between states.

Alternatively, perhaps we can model the possible states as the key being in the middle (M), left (L), or right (R). Wait, but after each swap, the positions of the cups change, so the L and R positions may change. Hmm. Maybe it's better to model the state as the position of the key relative to the current arrangement of the cups.

Alternatively, perhaps the key's position can be tracked in terms of the current state. Let's think of the possible positions. Let's denote the states as:

- S: the key is in the middle (current middle cup)
- L: the key is in the left cup (which is not the middle)
- R: the key is in the right cup (which is not the middle)

Wait, but when a swap happens, the middle changes. So after a swap, for example, if we swap the middle (current S) with the left cup, the new middle is the left cup. So the key is now in the left cup (which was the previous middle), but the new arrangement's left is the previous middle's left. Wait, perhaps this is getting complicated. Maybe we can model the state transitions.

Let me think of the possible states. The key can be in the middle (state M), left (state L), or right (state R). At each step, depending on the current state, what happens when a swap is done.

Wait, the swap is between the current middle and either the left or right cup, each with 50% probability.

So, for example, if the current state is M (key is in the middle), then:

- If we swap with left: the middle becomes the left cup, so the key is now in the left cup (since it was in the middle). So the new state is L.

- If we swap with right: the key moves to the right, new state R.

So from M, after any swap, the state transitions to L or R with 50% each.

If the current state is L (key is in the left cup, which is not the current middle):

- The middle is now the other cup (the one that was swapped in previous steps). So when we swap the middle (which is not the key's cup) with left or right:

Wait, let's think. Suppose the key is in the left cup (state L). The current middle is a different cup. So when a swap occurs between the current middle and left or right:

Wait, when the current state is L, the key is in the left cup (which is not the current middle). So the current arrangement is:

Left (has key), Middle (some other cup), Right (another cup). Then, during the swap step, the middle cup (which is not the key) is swapped with either the left or right cup.

So for example, if we swap the middle with left (current left cup has the key):

After the swap, the middle becomes the left cup (the previous left becomes middle). But the key is in the left cup (the original left cup) which is now the middle. So the new state is M.

Alternatively, if we swap the middle with right (the right cup is not the key), the key remains in the left cup (since the swap is between the middle and right, which doesn't involve the key's cup). So the state remains L.

Wait, no. Let's re-express this:

Current state is L. The key is in the left cup (so the left cup is not the current middle). The current middle is in the middle position. So when the swap occurs:

If the middle is swapped with the left (which is the key's cup), then the key moves to the middle. So the new state is M.

If the middle is swapped with the right (not the key's cup), then the key remains in the left cup, but now the middle has been swapped with the right. The left cup (with key) is still in the left position. So the state remains L.

Wait, no. Let's model this step by step.

Current state is L: key is in the left cup. The current arrangement is [K, M, R]. The middle is M. So when we swap the middle (M) with left (K):

The new arrangement becomes [M, K, R]. The middle is now K. The key was in the left cup (which is now M), but wait, no. The key is in the cup that was the left cup. Wait, the key is in the cup that was initially the left. But after swapping M (middle) with left (K), the left becomes M, and the middle becomes K. So the key is now in the middle cup (K). So the state becomes M.

Alternatively, if the swap is with right (R): the middle (M) swaps with right (R). The new arrangement is [K, R, M]. The middle is R. The key is still in the left cup (K), which is still the left position. So the state remains L.

So for state L, the transitions are:

With 50% probability, swap with left (current left is the key's cup) → new state is M.

With 50% probability, swap with right → new state remains L.

Similarly for state R. If the key is in the right cup (state R), then:

Swap with left: the middle swaps with left (non-key cup), so the key remains in the right → state R.

Swap with right (key's cup): the middle swaps with right, so the key moves to the middle → state M.

So transitions:

State R:

50% chance to swap with left → state remains R.

50% chance to swap with right → state becomes M.

So putting this all together, the state transitions are as follows:

Current state | Swap choice | Next state
M | left → L
M | right → R
L | left → M
L | right → L
R | left → R
R | right → M

So for each state, the transitions can be modeled. Now, the problem is to compute after n swaps, the probability that the state is M.

We can model this as a Markov chain. Let's represent the probability of being in each state after each step. Let's denote:

At step t, the probabilities are:

P_M(t) = probability of being in state M.

P_L(t) = probability of being in state L.

P_R(t) = probability of being in state R.

We need to find P_M(n) after n steps.

We can model this with dynamic programming. However, since n can be as large as the product of elements up to 1e18 each, and the array can have up to 1e5 elements, we need a way to compute this efficiently.

Let's find a recurrence relation.

Looking at the transitions:

- When in state M:

After a swap, the next state is either L or R with 50% each.

So:

P_L(t+1) += 0.5 * P_M(t)

P_R(t+1) += 0.5 * P_M(t)

P_M(t+1) is 0 from M's transition.

- When in state L:

After a swap, if we swap left (50% chance), next state is M. If swap right (50% chance), next state is L.

So:

P_M(t+1) += 0.5 * P_L(t)

P_L(t+1) += 0.5 * P_L(t)

- When in state R:

After a swap, if swap left (50% chance), next state is R. If swap right (50% chance), next state is M.

So:

P_M(t+1) += 0.5 * P_R(t)

P_R(t+1) += 0.5 * P_R(t)

But since the initial state is M (since the key starts in the middle), at t=0, P_M(0) = 1, P_L(0) = 0, P_R(0) = 0.

Now, since the transitions are linear, perhaps we can model this as a matrix exponentiation problem. However, since n can be very large (product of up to 1e5 elements, each up to 1e18), we need to compute the transitions after n steps efficiently.

Alternatively, perhaps we can find a recurrence formula for P_M(t).

Let's see. Let's look for a pattern.

Let's compute the first few steps.

t=0: P_M=1, P_L=0, P_R=0.

t=1: After 1 swap.

From M, transitions to L and R each 0.5. So P_M(1) = 0, P_L=0.5, P_R=0.5.

t=2: 

From L: 0.5 chance to go to M, 0.5 to stay in L.

From R: 0.5 chance to go to M, 0.5 to stay in R.

So:

P_M(2) = 0.5 * P_L(1) + 0.5 * P_R(1) = 0.5*(0.5) + 0.5*(0.5) = 0.5.

P_L(2) = 0.5 * P_L(1) + 0.5 * P_R(1) * 0 (since transitions from R don't contribute to L)

Wait, no. Let's recalculate:

Wait, for t=2:

Each state's contributions:

From L (P_L(1) =0.5):

- 0.5 * 0.5 (swap left: contribute to M).

- 0.5 *0.5 (swap right: contribute to L).

From R (P_R(1) =0.5):

- 0.5 *0.5 (swap left: contribute to R).

- 0.5 *0.5 (swap right: contribute to M).

So:

P_M(2) = (0.5 * 0.5) [from L's left swap] + (0.5 *0.5) [from R's right swap] = 0.25 +0.25=0.5.

P_L(2) comes from L's swap right (0.5 *0.5) plus R's swap left (0.5 *0.5) (but R's swap left leaves it in R, so no contribution to L. Wait, no.

Wait, for state R, when a swap is left (i.e., the middle swaps with left), which in the state R scenario, the key is in R. So the swap is between the middle and the left cup (which is not the key's cup). So the swap would result in the middle becoming the left cup, but the key remains in R (which is now the right cup). So in the state R, swapping with left (middle and left) → next state is R. So for state R, when a swap is left (50% chance), the next state is R. When a swap is right (50% chance), next state is M.

Wait, perhaps I'm getting confused again. Let's re-examine the transitions.

For state L:

swap left (middle and left) → next state is M.

swap right (middle and right) → next state is L.

For state R:

swap left (middle and left) → next state is R.

swap right (middle and right) → next state is M.

So when in state R, swapping with left (middle and left) doesn't affect the key's position (since the key is in R), so the state remains R.

Similarly, when in state R and swap right, the key moves to the middle.

So, for t=2:

From L (0.5):

after swap left: 0.5 chance → M (0.5 *0.5 = 0.25).

after swap right: 0.5 chance → L (0.5 *0.5=0.25).

So contributes to M 0.25, L 0.25.

From R (0.5):

after swap left: 0.5 chance → R (0.5 *0.5 =0.25 → contributes to R).

after swap right: 0.5 chance → M (0.5 *0.5=0.25 → contributes to M).

So for M: 0.25 (from L) +0.25 (from R) = 0.5.

For L: 0.25 (from L's swap right) → total 0.25.

For R: 0.25 (from R's swap left) → total 0.25.

So P_M(2)=0.5, P_L(2)=0.25, P_R(2)=0.25.

t=3:

For each state:

M (0.5) → after swap, transitions to L and R each 0.5 *0.5=0.25 each.

L (0.25) → 0.5 chance to M (0.25 *0.5=0.125), 0.5 to L (0.125).

R (0.25) → 0.5 chance to M (0.125), 0.5 to R (0.125).

So:

P_M(3) = 0.125 (from L) +0.125 (from R) = 0.25.

P_L(3) comes from:

0.5 (from M's left swap: 0.5*0.5=0.25) → contributes 0.25 to L.

Plus the L's remaining (0.125) → from L's swap right.

So total L: 0.25 +0.125=0.375?

Wait, perhaps I need to model this step by step.

Wait, t=3:

Current probabilities are:

M: 0.5, L: 0.25, R:0.25.

Then, each state contributes to the next step.

For M (0.5):

each swap (left or right) leads to L or R.

So:

from M, 0.5 *0.5 → 0.25 added to L.

0.5 *0.5 →0.25 added to R.

For L (0.25):

0.5 chance to swap to M → 0.125 added to M.

0.5 chance to stay L →0.125 added to L.

For R (0.25):

0.5 chance to swap to M →0.125 added to M.

0.5 chance to stay R →0.125 added to R.

So total for t=3:

M: 0.125 +0.125 =0.25.

L: 0.25 (from M's left swap) +0.125 (from L's swap right) = 0.375.

R: 0.25 (from M's right swap) +0.125 (from R's swap left) → 0.375.

So P_M(3)=0.25.

Hmm. So the pattern seems to be that after even steps, P_M is 0.5, 0.5, etc. But wait, t=1: 0, t=2:0.5, t=3:0.25, t=4: ?

Let's compute t=4.

t=3: P_M=0.25, P_L=0.375, P_R=0.375.

For t=4:

From M (0.25):

each swap leads to L or R. So 0.25 *0.5 added to L and R each → 0.125 each.

From L (0.375):

0.5 chance to M (0.375 *0.5=0.1875) and 0.5 to L (0.1875).

From R (0.375):

0.5 chance to M (0.1875) and 0.5 to R (0.1875).

So M's contribution: 0.1875 (from L) +0.1875 (from R) =0.375.

L's contribution: 0.125 (from M's left swap) + 0.1875 (from L's swap right) + 0.1875 (from R's swap left? Wait, no. R's swap left is for R's transition. Wait, R's swap left (middle and left) → R remains R. So R's contribution to L comes only from when R transitions to M? Or no. Wait, no. Let me re-express the transitions.

Wait, for each state in the current step:

L contributes to M and L.

R contributes to M and R.

So for R, the contribution to R comes from R's swap left (0.5 chance).

So for t=4:

From L (0.375):

0.5 → M (0.1875)

0.5 → L (0.1875)

From R (0.375):

0.5 → M (0.1875)

0.5 → R (0.1875)

So M's total: 0.1875 +0.1875=0.375.

L's total: 0.1875 (from L's swap right) + 0.125 (from M's left swap) = 0.3125.

Wait, no. Because when M is swapped left, it contributes to L. So in the current step, M is 0.25. When swapped, for each swap from M (0.25):

- 50% to left (adding to L) → 0.25 *0.5=0.125 to L.

- 50% to right (adding to R) → 0.125 to R.

So for L's total:

0.125 (from M's left swap) + 0.1875 (from L's swap right) + 0.1875 (from R's swap left? No, R's swap left leaves them in R. So R's transitions contribute to R and M. So R's swap left contributes 0.1875 to R. So L's contributions are from M's left swap and L's swap right.

Wait, perhaps I'm getting confused again. Let's model it properly.

For t=4:

We have:

Previous state:

M=0.25, L=0.375, R=0.375.

Each step, for each state, compute their contribution to the next states.

From M (0.25):

- 50% to L → 0.25 *0.5 = 0.125 added to L.

- 50% to R →0.25 *0.5=0.125 added to R.

From L (0.375):

- 50% to M →0.375*0.5=0.1875 added to M.

- 50% to L →0.375*0.5=0.1875 added to L.

From R (0.375):

- 50% to M →0.375*0.5=0.1875 added to M.

- 50% to R →0.375*0.5=0.1875 added to R.

So summing up:

M_new = 0.1875 (from L) +0.1875 (from R) = 0.375.

L_new = 0.125 (from M's left) + 0.1875 (from L's swap right) = 0.3125.

R_new = 0.125 (from M's right) +0.1875 (from R's swap left) = 0.3125.

So P_M(4) = 0.375.

Hmm. So the pattern is that P_M alternates between certain values. Let's see:

n | P_M(n)
0 | 1
1 | 0
2 | 0.5
3 | 0.25
4 | 0.375
5 | 0.375 (?)

Wait, let me compute t=5.

t=4: P_M=0.375, P_L=0.3125, P_R=0.3125.

For t=5:

From M (0.375):

each swap to L or R: 0.375 *0.5 each →0.1875 added to L and R.

From L (0.3125):

0.5 to M (0.15625), 0.5 to L (0.15625).

From R (0.3125):

0.5 to M (0.15625), 0.5 to R (0.15625).

So M_new = 0.15625 (from L) + 0.15625 (from R) = 0.3125.

So P_M(5) = 0.3125.

Hmm. So the values are oscillating. But perhaps there's a pattern here.

Looking at even and odd steps:

For even n:

n=0 →1, n=2 →0.5, n=4 →0.375, n=6 →0.3125?

Wait, maybe not. Let's compute t=5 and t=6.

t=5: P_M=0.3125.

t=6:

From M (0.3125):

swap to L and R: 0.3125 *0.5 each →0.15625 each.

From L (0.3125 → 0.3125 is the previous L and R?)

Wait, perhaps I'm making a mistake here. Let me re-express the state transitions using a mathematical approach.

Let me model P_M(n) as a function. Let's see if we can find a recurrence for P_M(n).

Looking at the transitions:

At step n+1:

P_M(n+1) = 0.5 * P_L(n) + 0.5 * P_R(n).

Because from state L, 50% chance to transition to M, and same from R.

But since P_L(n) + P_R(n) = 1 - P_M(n), we can substitute:

P_M(n+1) = 0.5 * (P_L(n) + P_R(n)) ) = 0.5*(1 - P_M(n)).

So the recurrence is:

P_M(n+1) = 0.5*(1 - P_M(n)).

This is a key insight! Because if we can model this recurrence, then we can find a closed-form formula for P_M(n).

Yes! Because the next P_M is 0.5*(1 - previous P_M). So this recurrence can be solved.

So the recurrence is:

PM(n+1) = (1 - PM(n)) * 0.5

With PM(0) = 1.

So let's solve this recurrence relation.

We can write this as:

PM(n) = (1 - PM(n-1)) / 2.

Let's compute the first few terms:

PM(0) = 1.

PM(1) = (1 -1)/2 = 0.

PM(2) = (1-0)/2 = 0.5.

PM(3) = (1 -0.5)/2 = 0.25.

PM(4) = (1 -0.25)/2 = 0.375.

PM(5) = (1 -0.375)/2 = 0.3125.

Which matches the earlier calculations. So this recurrence is correct.

So the problem reduces to computing PM(n) where n is the product of the array elements. Then, we need to represent this as a fraction in reduced form modulo 1e9+7.

Now, the key is to find a closed-form formula for PM(n).

Let's try to find a pattern.

Let's compute PM(n) for small n:

n | PM(n)
0 | 1 = 1/1
1 | 0 =0/1
2 | 1/2
3 | 1/4
4 |3/8
5 |5/16
6 | 11/32
7 | 21/64
Hmm, wait. Let me compute:

n=4: (1-0.25)/2 = 0.75/2=0.375 →3/8.

n=5: (1-3/8)/2 →5/8 *0.5=5/16.

n=6: (1-5/16)/2 →11/32.

n=7: (1-11/32)/2 →21/64.

Hmm. The numerators are following a pattern. Let's see:

n=0: 1 →1/1.

n=1: 0 →0/1.

n=2:1/2.

n=3:1/4.

n=4:3/8.

n=5:5/16.

n=6:11/32.

n=7:21/64.

Looking at the numerators: 0, 1, 0, 1, 3, 5, 11, 21...?

Wait, perhaps the numerator and denominator can be expressed in terms of a recurrence.

Alternatively, perhaps the general formula can be found.

The recurrence is PM(n) = (1 - PM(n-1))/2.

We can solve this recurrence using standard techniques for linear recurrences.

The recurrence can be rewritten as:

PM(n) + (1/2) PM(n-1) = 1/2.

This is a linear nonhomogeneous recurrence relation.

The homogeneous solution is found by solving PM(n) + (1/2) PM(n-1) =0. The characteristic equation is r + 1/2 =0 → r= -1/2.

The particular solution can be found by assuming a constant solution. Let's say PM(n) = C.

Substituting into the recurrence:

C = (1 - C)/2 → 2C =1 -C →3C=1 →C=1/3.

So the general solution is PM(n) = A (-1/2)^n + 1/3.

We can determine A using the initial condition PM(0) =1.

At n=0: 1 = A (-1/2)^0 +1/3 →1 = A*1 +1/3 → A=2/3.

So the closed-form formula is:

PM(n) = (2/3) * (-1/2)^n + 1/3.

So for any n, this is the probability.

Let's test this formula for n=2:

(2/3) * ( (-1/2)^2 ) +1/3 = (2/3)(1/4) +1/3 → (2/12)+(4/12) =6/12=0.5 → correct.

n=3: (2/3)(-1/8) +1/3 → (-2/24) +8/24=6/24=0.25 → correct.

Yes, this formula works.

So PM(n) = [ 2 * (-1/2)^n +1 ] / 3.

Which can be written as PM(n) = (1 + (-1/2)^n * 2 ) /3.

Now, since we need to compute this for n being the product of the array elements, which can be very large (up to 1e5 elements, each up to 1e18, leading to n up to (1e18)^1e5 which is way beyond any exponentiation steps directly), we need to compute (-1/2)^n modulo MOD, but in fractions.

Wait, but since we have to compute this as a fraction, we need to represent PM(n) as a numerator and denominator.

So PM(n) = [1 + 2 * (-1/2)^n ] /3.

Let's compute this as a fraction. Let's denote (-1/2)^n as (-1)^n / 2^n.

So:

PM(n) = [1 + 2*(-1)^n / 2^n ] /3.

Combine the terms:

PM(n) = [2^n + 2*(-1)^n ] / (3 * 2^n).

So numerator = 2^n + 2*(-1)^n.

Denominator =3 * 2^n.

So the fraction is (2^n + 2*(-1)^n) / (3 * 2^n).

We can factor 2 from the numerator:

= 2 ( 2^{n-1} + (-1)^n ) / (3*2^n )

Wait, perhaps not necessary. Let's leave it as is.

So the numerator is 2^n + 2*(-1)^n.

Denominator is 3*2^n.

We need to simplify this fraction to its lowest terms.

Let's compute the GCD of numerator and denominator.

Let's denote numerator N = 2^n + 2*(-1)^n.

Denominator D = 3 * 2^n.

So GCD(N, D) is GCD(2^n + 2*(-1)^n, 3*2^n).

But 2^n and 3 are coprime (since 2 and 3 are primes), and 2^n and 2*(-1)^n share a factor of 2. Let's see:

Case when n is even:

Let n be even. Then (-1)^n =1.

So N= 2^n + 2*1=2(2^{n-1} +1).

D=3*2^n.

So GCD(N, D) = GCD(2(2^{n-1}+1), 3*2^n) = 2*GCD(2^{n-1}+1, 3*2^{n-1}).

But 2^{n-1} and 3 are coprimes, so GCD(2^{n-1}+1, 3*2^{n-1}).

We can compute GCD(2^{n-1}+1, 3) and GCD(2^{n-1}+1, 2^{n-1}).

GCD(2^{n-1}+1, 2^{n-1}) is GCD(1, 2^{n-1}) =1.

GCD(2^{n-1}+1,3):

If n-1 is even: 2^{n-1} mod 3 is (2^2)^k mod3=1^k mod3=1. So 2^{n-1} +1 mod3= 1+1=2 → GCD is 1.

If n-1 is odd: 2 mod3=2, 2^1 mod3=2, 2^3 mod3=2, etc. So 2^{n-1} mod3=2. So 2+1=3 → mod3 0. So GCD is 3.

So GCD(2^{n-1}+1,3) is 3 if n-1 is odd (i.e., n is even and n-1 is odd → n even and n is even → n is even and n is even. Wait, n is even. So n-1 is odd. So 2^{n-1} mod3=2 mod3=2. 2+1=3 mod3=0. So GCD is 3.

So for even n:

If n is even and n-1 is odd, which is always true for even n.

So GCD is 3 in this case.

But then:

So overall GCD is 2 * 3 =6.

Wait, but in the even case, N=2*(2^{n-1}+1).

D=3*2^n.

So the GCD would be 2*3=6, but only if 3 divides (2^{n-1} +1).

Which happens when n is even. Because 2^{n-1} is congruent to 2 mod3 when n-1 is odd (since 2^1=2 mod3, 2^3=8 mod3=2, etc. So for even n (n-1 is odd), 2^{n-1} mod3=2 → 2+1=3 mod3=0. So 3 divides (2^{n-1}+1).

So in even n case, the GCD(N, D) is 6. So the fraction can be simplified by dividing numerator and denominator by 6.

Wait, but let's test with n=2:

n=2 even.

N=2^2 +2*(1) =4+2=6.

D=3*4=12.

GCD(6,12)=6.

6/6=1, 12/6=2. So simplified fraction is 1/2 → which matches the example.

Another example: n=4 (even):

N=2^4+2*(1) =16+2=18.

D=3*16=48.

GCD(18,48)=6. 18/6=3,48/6=8 → 3/8 → matches earlier calculation.

So for even n:

simplify numerator and denominator by 6. So the fraction becomes ( (2^{n} + 2 ) /6 ) / ( (3*2^{n}) /6 ) → ( (2^{n-1} +1) ) / ( 2^{n-1} *3 / 3 ) → not sure. Wait, perhaps (6) is the GCD.

In even n case:

Numerator is 2(2^{n-1} +1), denominator is 3*2^n = 3*2*2^{n-1} = 6*2^{n-1}.

So GCD is 6 if (2^{n-1}+1) is divisible by 3.

Which is true for even n.

So for even n, N/D = (2^{n} +2)/ (3*2^n) → (2*(2^{n-1} +1)) / (3*2^n) → (2^{n-1} +1)/ (3*2^{n-1}).

So for even n, the simplified fraction is (2^{n-1} +1) / (3 * 2^{n-1}).

But 2^{n-1} and 3 are coprimes, since 2 and 3 are primes, and 3 doesn't divide 2^{n-1}.

So for even n, the simplified fraction has numerator 2^{n-1} +1 and denominator 3*2^{n-1}, which is already in reduced form.

Wait, let's see for n=2:

Numerator: 2^{1} +1 =3. Denominator 3*2^1=6. 3/6=1/2 → reduced.

But the GCD of 3 and 6 is 3, so 3/6 simplifies to 1/2 by dividing numerator and denominator by 3. But according to our previous analysis, the GCD was 6. So perhaps I made a mistake.

Wait, n=2 is even. N=6, D=12. GCD(6,12)=6. So 6/12=1/2 after dividing by 6. So the simplified fraction is 1/2.

But according to the formula for even n, (2^{n-1}+1)/(3*2^{n-1}) → (3)/(3*2) =1/2.

Which is correct.

So perhaps the GCD is 6 for even n. So when n is even, the simplified fraction is (N/6)/(D/6) = (6/6)/(12/6) =1/2.

So for even n:

simplified fraction is (2^{n} +2) / (3*2^{n}) → divided by 6 → ( (2^{n}+2)/6 ) / ( (3*2^{n})/6 ) → ( (2^{n-1} +1 ) ) / ( (3*2^{n-1}) ) → and since 2^{n-1} and 3 are coprime, this fraction is reduced.

So for even n, the reduced fraction is (2^{n-1} +1)/(3*2^{n-1}).

For odd n:

N=2^n +2*(-1)^n =2^n -2 (since n is odd, (-1)^n =-1).

Denominator D=3*2^n.

So N=2^n -2 = 2*(2^{n-1} -1).

D=3*2^n.

So GCD(N, D) = GCD(2*(2^{n-1}-1), 3*2^n).

Factors of 2: GCD is 2* GCD( (2^{n-1} -1 ), 3*2^{n-1} )

Now, 2^{n-1} -1 and 2^{n-1} are coprimes (since consecutive numbers). So GCD(2^{n-1}-1, 3*2^{n-1}) is GCD(2^{n-1}-1,3).

Because 2^{n-1} -1 and 2^{n-1} are coprimes, their GCD is 1. So the GCD becomes GCD(2^{n-1}-1,3).

Let's compute this.

2 mod3=2.

2^1 mod3=2 → 2-1=1 mod3 → GCD(1,3)=1.

2^2 mod3=1 →1-1=0 → GCD(0,3)=3.

2^3 mod3=2 →2-1=1 → GCD 1.

So for n-1 even (n is odd and n-1 is even → n is odd and n-1 is even? Wait, n is odd → n-1 is even.

So n-1 is even. So 2^{n-1} mod3 is (2^2)^k mod3=1^k mod3=1. So 2^{n-1}-1 mod3=0.

Thus, GCD(2^{n-1} -1,3)=3.

So GCD(N, D) =2 * 3=6.

So for odd n, N/D= (2^n-2)/(3*2^n) = [2(2^{n-1}-1)]/[3*2^n] = (2^{n-1}-1)/(3*2^{n-1}).

But (2^{n-1}-1) and 3*2^{n-1} have GCD of 3?

Wait, for example, n=3 (odd):

N=8-2=6. D=3*8=24. GCD(6,24)=6. So 6/24=1/4. Which is correct.

So simplified fraction for odd n is (2^{n-1} -1)/(3 * 2^{n-1}).

But 2^{n-1} and 3 are coprimes (since 2 and 3 are primes), and (2^{n-1} -1) can be divisible by 3. For example, when n-1 is even (since 2^{2k} mod3=1 →1-1=0 mod3).

So for odd n, the fraction can be simplified by dividing numerator and denominator by 3.

Wait, n=3:

(2^2-1)/(3*2^2) = (4-1)/12=3/12=1/4 → which is correct. GCD of 3 and 12 is 3.

So after dividing by 3, numerator becomes 1, denominator 4. Which is reduced.

So in the odd case, the simplified fraction is ( (2^{n-1} -1)/3 ) / 2^{n-1} → but since 2^{n-1} and (2^{n-1} -1)/3 are coprimes.

Wait, in the case of n=3: (4-1)/3 =1. So 1/4.

Yes.

Thus, the reduced fraction is:

For even n: (2^{n-1} +1) / (3 * 2^{n-1} )

For odd n: (2^{n-1} -1 ) / (3 * 2^{n-1} )

But how do we express this in terms of the original formula?

Alternatively, we can compute the numerator and denominator as follows:

We have:

For even n:

Numerator: 2^{n} + 2

Denominator: 3*2^{n}

For odd n:

Numerator: 2^{n} - 2

Denominator: 3*2^{n}

But after simplification by dividing numerator and denominator by 2, we get:

For even n:

(2^{n-1} +1) / (3*2^{n-1})

For odd n:

(2^{n-1} -1) / (3*2^{n-1})

In both cases, the numerator and denominator may have a GCD of 1 or 3.

Wait, for even n:

If (2^{n-1} +1) is divisible by 3, then GCD is 3, else 1.

But we saw that for even n, 2^{n-1} mod3 is 2, since n-1 is odd (even n →n-1 is odd). 2^{n-1} mod3=2. So 2+1=3 → divisible by3.

So for even n:

Numerator term (2^{n-1} +1) is divisible by 3. So:

(2^{n-1}+1) / (3*2^{n-1}) = [ (2^{n-1}+1)/3 ] / 2^{n-1}.

And since (2^{n-1}+1)/3 and 2^{n-1} are coprimes (since 2^{n-1} is even and (2^{n-1}+1) is odd, and 2^{n-1} is a power of 2).

So the simplified fraction for even n is ( (2^{n-1}+1)/3 ) / 2^{n-1}.

Similarly, for odd n:

(2^{n-1} -1) /3 divided by 2^{n-1}.

But regardless, the final reduced fraction is (a)/(b), where a and b are as computed.

But how do we compute this for very large exponents?

The problem states that n is the product of the array elements. The array can be up to 1e5 elements, each up to 1e18. So n can be up to (1e18)^1e5, which is way too big to compute directly.

But since we need to compute the numerator and denominator modulo 1e9+7, and also compute their reduced form, perhaps we can find a way to compute exponents modulo MOD-1, considering Fermat's little theorem.

But wait, the MOD is 1e9+7, which is a prime. So for modular inverse, we can use Fermat's little theorem.

But the problem is that exponents are huge. So we need to compute 2^{n} mod something.

Wait, but in the numerator and denominator for the even and odd cases, the exponents are n-1. So for the final simplified fraction:

For even n:

PM(n) = [ (2^{n} +2) /6 ] / [ (3*2^{n}) /6 ] = (2^{n} +2)/(3*2^{n}).

But after simplification, for even n, it's (2^{n-1} +1) / (3*2^{n-1}).

But for even n, n is even → n mod2=0.

Similarly for odd n, n mod2=1.

So, to compute the final fraction, we can first determine whether n is even or odd.

But since n is the product of the array elements, which may include even and/or odd numbers. So n is even if at least one element is even. Otherwise, it's odd.

So the first step is to compute whether n is even or odd. That's easy: check if any element in the array is even. If even one element is even, then the product is even. Otherwise (all elements are odd and k>=1), product is odd.

So this will determine whether the exponent n is even or odd.

Once we know the parity of n, we can compute the numerator and denominator accordingly.

But how to compute the exponents for the numerator and denominator modulo MOD.

Let's split into cases:

Case 1: n is even.

PM(n) = (2^{n} + 2) / (3*2^{n}) → after simplification, but for the reduced fraction, we need to compute (2^{n} + 2) and (3*2^{n}), then divide by their GCD.

But for large n, we can't compute 2^n directly. But since MOD is 1e9+7 (prime), we can compute exponents modulo MOD-1 for exponents in denominators (using Fermat's theorem), but I'm not sure.

Alternatively, we can represent the numerator and denominator modulo MOD, then compute the reduced fraction.

Wait, but the problem requires that we output the fraction as p/q, where p and q are coprimes, and then output p mod MOD and q mod MOD.

So the approach is:

1. Compute the numerator and denominator as per the formula.

2. Simplify them by dividing by their GCD.

3. Take the results modulo MOD.

So the problem is to compute the numerator and denominator for PM(n), simplify them by their GCD, then output the results modulo MOD.

But the exponents are huge.

So the key steps are:

- Compute the parity of n (even or odd).

- Compute 2^{n} mod MOD.

But n is the product of the array elements. How to compute 2^{n} mod MOD?

Since MOD is a prime (1e9+7), and 2 is coprime to MOD, we can use Fermat's little theorem. Since 2^(MOD-1) ≡ 1 mod MOD.

So 2^{n} mod MOD = 2^{n mod (MOD-1)} mod MOD, provided that MOD is prime and 2 is not a multiple of MOD.

Yes, since MOD=1e9+7 is prime, and 2 < MOD.

So to compute 2^a mod MOD, where a is a very large exponent (product of array elements), we can compute a mod (MOD-1), then compute pow(2, a_mod, MOD).

But the array elements can be up to 1e18 each, and up to 1e5 elements. So the product is n = product of a_i. To compute n mod (MOD-1), but since the product can be very large, we need to compute the product modulo (MOD-1), but each a_i can be up to 1e18, which makes this tricky.

But (a * b) mod m = ((a mod m) * (b mod m)) mod m.

So to compute the product of the array elements mod (MOD-1), we can process each element a_i, compute a_i mod (MOD-1), multiply them modulo (MOD-1), and that's the exponent mod (MOD-1).

But wait, the product of the array elements is n. So n mod (MOD-1) can be computed by multiplying each a_i mod (MOD-1), then taking the product modulo (MOD-1).

But since MOD-1 is 1e9+6, which is a large number, and each a_i can be up to 1e18, we can compute each a_i mod (MOD-1), then multiply all those mod (MOD-1) to get the product modulo (MOD-1).

Yes. So for example, for each a_i, compute a_i mod (MOD-1), then multiply all such terms modulo (MOD-1) to get the exponent mod (MOD-1).

Similarly, since we need to compute 2^{n} mod MOD, we can compute exponent mod (MOD-1) because of Fermat's theorem.

So, steps to compute 2^{n} mod MOD:

Compute exponent = product of array elements mod (MOD-1).

Then, 2^exponent mod MOD.

Similarly for exponents in the numerator and denominator.

Now, let's compute the required terms for each case.

Case 1: n is even.

PM(n) = (2^n + 2) / (3 * 2^n)

So numerator is 2^n +2.

Denominator is 3*2^n.

But we need to compute this fraction in reduced form.

The GCD of (2^n +2, 3*2^n) is GCD(2^n +2, 3*2^n) = GCD(2^n +2, 3*2^n).

But 2^n and 3 are coprime. So GCD(2^n +2, 3*2^n) = GCD(2^n+2,3) * GCD(2^n+2, 2^n).

GCD(2^n+2, 2^n) = GCD(2, 2^n) = 2.

So overall GCD is 2 * GCD( (2^{n} +2)/2, 3).

Since n is even, 2^n is even, so (2^n +2) is even, so (2^n +2)/2 = 2^{n-1} +1.

Then, GCD(2^{n-1} +1,3).

As earlier, when n is even, n-1 is odd. 2^{n-1} mod3=2.

So 2^{n-1}+1 mod3= 2+1=0. So GCD is 3.

So overall GCD is 2 *3=6.

So the reduced fraction is:

(2^n +2)/6 divided by (3*2^n)/6 → ( (2^{n} +2)/6 ) / ( (3*2^{n})/6 ) → numerator (2^{n} +2)/6, denominator (3*2^{n})/6.

But (2^{n} +2)/6 = (2^{n-1} +1)/3.

Denominator (3*2^{n})/6 = (2^{n} )/2 =2^{n-1}.

So reduced fraction is ( (2^{n-1} +1)/3 ) / 2^{n-1}.

So numerator_part = (2^{n-1} +1) /3.

Denominator_part = 2^{n-1}.

But since 2^{n-1} mod3 is 2 when n-1 is odd (since n is even), so 2^{n-1} +1 is divisible by 3.

So numerator_part is an integer.

So for even n, the reduced fraction is (numerator_part) / denominator_part.

But to compute this modulo MOD, we can compute numerator_part mod MOD and denominator_part mod MOD.

But how?

We can compute:

numerator_part = (pow(2, n-1, 3*MOD) +1) //3.

Wait, but since 3 divides (2^{n-1} +1), then (2^{n-1} +1) mod 3*MOD is congruent to 0 mod3. So we can compute (2^{n-1} +1) mod (3*MOD), then divide by 3.

But since MOD is a prime, 3 and MOD are coprimes (since MOD is 1e9+7, which is not divisible by 3). So 3 has a modular inverse modulo MOD.

Alternatively, compute 2^{n-1} mod (3*MOD), add 1, then divide by 3, then take modulo MOD.

But this may not be straightforward.

Alternatively, compute (pow(2, n-1, MOD) +1) * inv3 mod MOD, where inv3 is the inverse of 3 mod MOD.

Because:

(2^{n-1} +1) /3 mod MOD = [ (2^{n-1} mod MOD +1) ] * inv3 mod MOD.

This works only if 3 divides (2^{n-1} +1) mod MOD. But this may not be the case, but in reality, since we have even n, 3 divides (2^{n-1} +1) exactly, so when mod MOD is applied, adding 1 and multiplying by inv3 will give the correct result.

But perhaps I'm overcomplicating.

Let me think:

For even n, the numerator is (2^{n-1} +1)/3.

Denominator is 2^{n-1}.

So, in terms of mod MOD:

numerator_part mod MOD is [ (pow(2, n-1, MOD) +1) * inv3 ] mod MOD.

Denominator_part mod MOD is pow(2, n-1, MOD).

But inv3 is the inverse of 3 modulo MOD. Since MOD is 1e9+7 which is a prime, inv3 is pow(3, MOD-2, MOD).

Yes.

So for even n:

p = (pow(2, n-1, MOD) +1) * inv3 % MOD.

q = pow(2, n-1, MOD).

For odd n:

PM(n) = (2^n - 2) / (3 * 2^n )

Similarly, the GCD of numerator and denominator is 6.

So simplified fraction is (2^{n-1} -1)/3 / 2^{n-1}.

Again, compute:

pow(2, n-1, MOD) -1 divided by 3 → (pow(2, n-1, MOD) -1) * inv3 mod MOD.

Denominator is pow(2, n-1, MOD).

So for odd n:

p = (pow(2, n-1, MOD) -1) * inv3 % MOD.

q = pow(2, n-1, MOD).

Thus, the algorithm can be structured as follows:

1. Compute whether n is even or odd.

   - If any element in the array is even → n is even.

   - Else (all elements are odd and k>=1) → product is odd → n is odd.

2. Compute exponent_mod = product of array elements mod (MOD-1), since we need to compute 2^(exponent) mod MOD.

   But for exponents in even and odd cases:

   For even case:

   n is even.

   So, to compute pow(2, n-1, MOD):

   Since n is even, n = product of array elements → n-1 = product -1.

   So exponent is (product -1) mod (MOD-1).

   But (product -1) mod (MOD-1) can be computed as (product mod (MOD-1) -1) mod (MOD-1).

   Similarly, for odd case:

   n is odd.

   So n-1 is even.

   But the same approach applies.

   So steps:

   a. Compute product_mod_phi = product of (a_i mod (MOD-1)) for all i, mod (MOD-1).

   phi is MOD-1 since MOD is prime.

   So product_mod_phi = (product of all (a_i % (MOD-1))) % (MOD-1).

   Then, exponent_mod = product_mod_phi.

   So:

   For even case:

   exponent_for_2_power = (exponent_mod - 1) % (MOD-1).

   Because n-1 = product -1 → mod (MOD-1) is (product_mod_phi -1) mod (MOD-1).

   So pow(2, n-1, MOD) = pow(2, exponent_for_2_power, MOD).

   For odd case:

   n is odd → exponent_mod is product_mod_phi (since n is product mod (MOD-1)).

   So n-1 = product -1 → mod (MOD-1) is (exponent_mod -1) mod (MOD-1).

   So same as even case.

Wait, no. For even and odd cases, the exponent n-1 is calculated as (product -1), regardless of parity.

Wait, no. For even n:

n is even → product is even → n = product → n-1 is product -1.

For odd n:

n is odd → product is odd → n = product → n-1 is even.

So in all cases, exponent for 2^{n-1} is (product -1) mod (MOD-1).

So regardless of parity, the exponent is (product -1) mod (MOD-1).

Wait, no. The exponents in the even and odd cases are n-1, where n is the product of array elements. So regardless of whether n is even or odd, we need to compute 2^{n-1} mod MOD.

So to compute 2^{n-1} mod MOD, we can compute exponent as (n-1) mod (MOD-1), then compute pow(2, exponent, MOD).

But n can be computed as the product of the array elements. So:

We need to compute (product -1) mod (MOD-1), which is (product mod (MOD-1) - 1) mod (MOD-1).

So steps:

Compute product_mod_phi: product of all a_i mod (MOD-1), mod (MOD-1).

Then, exponent_for_2 = (product_mod_phi -1) % (MOD-1).

Then, pow_2 = pow(2, exponent_for_2, MOD).

Thus, pow_2 is 2^{n-1} mod MOD.

Once we have pow_2, compute p and q based on even/odd.

For even n:

p = (pow_2 +1) * inv3 % MOD.

q = pow_2.

For odd n:

p = (pow_2 -1) * inv3 % MOD.

q = pow_2.

But need to handle negative values. For example, in the odd case, if pow_2 is 0 (mod MOD), then (0 -1) is -1 mod MOD = MOD-1. Then multiply by inv3.

So yes.

Thus, the algorithm is:

1. Determine whether n is even or odd.

   - Even if any a_i is even.

   - Else, odd.

2. Compute product_mod_phi = product of (a_i % phi) mod phi, where phi = MOD-1=1e9+6.

   Because we need to compute n mod phi for 2^{n} mod MOD.

   But wait, no. For 2^{n-1} mod MOD, we need to compute (n-1) mod phi.

   So compute product_mod_phi = product of a_i mod phi, then exponent_for_2 = (product_mod_phi -1) mod phi.

3. Compute pow_2 = pow(2, exponent_for_2, MOD).

4. Compute inv3 = pow(3, MOD-2, MOD).

5. Depending on even or odd:

   a. If even:

      p = (pow_2 +1) * inv3 % MOD.

      q = pow_2 % MOD.

   b. If odd:

      p = (pow_2 -1) * inv3 % MOD.

      q = pow_2 % MOD.

6. Output p / q as a fraction with x = p mod MOD, y = q mod MOD.

But wait, in the even case, the numerator is (pow_2 +1) //3, but this is only valid if (pow_2 +1) is divisible by 3. Which may not be the case when working modulo MOD. However, in reality, since 3 divides (2^{n-1} +1) when n is even (as discussed earlier), then (pow_2 +1) is congruent to 0 mod3. So when working mod MOD, (pow_2 +1) is congruent to 0 mod3, so multiplying by inv3 will give the correct result.

But since we are working modulo MOD, which is not a multiple of 3, we can safely multiply by inv3.

Yes.

Now, the code steps:

Implement the steps above.

Now, the code must:

- Read k and the array a.

- Compute even = any element in a is even.

- Compute product_mod_phi: multiply all a_i mod phi, mod phi.

   Here, phi is MOD-1 = 1e9+6.

   For each a_i in a:

   mod_phi = a_i % phi.

   product_mod_phi = (product_mod_phi * mod_phi) % phi.

   Initially, product_mod_phi starts at 1.

- Compute exponent_for_2 = (product_mod_phi -1) % phi.

   But need to handle product_mod_phi = 0. If product_mod_phi is 0, then (0 -1) mod phi is phi-1.

- Compute pow_2 = pow(2, exponent_for_2, MOD).

- Compute inv3 = pow(3, MOD-2, MOD).

- Compute p and q based on even/odd.

But wait, in code:

MOD = 1e9 +7

phi = MOD-1 =1e9+6

For even case:

p = (pow_2 + 1) * inv3 % MOD

q = pow_2 % MOD

For odd case:

p = (pow_2 -1) * inv3 % MOD

q = pow_2 % MOD

But when pow_2 is 0 (like when n=1), in the even case it's impossible. For example, n=1 is odd, so it's handled in the odd case.

Testing the first example:

Input: 1 2 → product is 2 (even).

exponent_for_2 = (2-1) mod 1e9+6 =1.

pow_2 = 2^1 mod MOD=2.

even case:

p=(2+1)*inv3 mod MOD →3*333333336 mod MOD →1.

q=2.

So output is 1/2 → correct.

Second example:

Input:3 1 1 1 → product 1 (odd).

even = false.

exponent_for_2 = (1-1) mod phi →0.

pow_2=2^0=1.

p=(1-1) * inv3 →0*inv3=0.

q=1.

So output 0/1 → correct.

Another test case:

n=3 (odd).

product is 3 → odd.

exponent_for_2 = (3-1) mod phi →2.

pow_2=2^2=4.

p=(4-1)*inv3 →3*333333336 mod MOD= 100000001 mod MOD → 1.

q=4 mod MOD.

But wait, the correct PM(3) is 0.25 → 1/4.

Which matches.

So yes.

So the code should handle all cases correctly.

Now, code steps:

- Read k.

- Read the array a.

- Check if any element is even (even = any(a_i %2 ==0 for a_i in a)).

- Compute product_mod_phi.

- Compute exponent_for_2 = (product_mod_phi -1) % phi.

- Compute pow_2 = pow(2, exponent_for_2, MOD).

- Compute inv3 = pow(3, MOD-2, MOD).

- Compute p and q based on even.

Now, code implementation:

But for large k (up to 1e5 elements), and a_i up to 1e18, we need to compute the product mod phi efficiently.

But multiplying 1e5 elements modulo 1e9+6 (phi) is manageable.

But we need to handle each a_i mod phi, then multiply into product_mod_phi.

But since a_i can be up to 1e18, a_i mod phi can be computed as a_i % phi.

So code:

phi = 10**9 +6

product_mod_phi = 1

for num in a:

    product_mod_phi = (product_mod_phi * (num % phi)) % phi

exponent_for_2 = (product_mod_phi -1) % phi

pow_2 = pow(2, exponent_for_2, MOD)

Then, even = any(num %2 ==0 for num in a)

Compute p and q.

But for the 'any even' check, we can loop through the array and check.

But for large arrays (1e5 elements), this is O(k), which is acceptable.

So, the code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    k = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    MOD = 10**9 +7

    phi = MOD -1

    even = False

    for num in a:

        if num %2 ==0:

            even = True

    product_mod_phi = 1

    for num in a:

        product_mod_phi = (product_mod_phi * (num % phi)) % phi

    exponent_for_2 = (product_mod_phi -1) % phi

    pow_2 = pow(2, exponent_for_2, MOD)

    inv3 = pow(3, MOD-2, MOD)

    if even:

        p = (pow_2 +1) * inv3 % MOD

        q = pow_2 % MOD

    else:

        p = (pow_2 -1) * inv3 % MOD

        q = pow_2 % MOD

    print(f"{p}/{q}", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
1 1 1
""",
            "output": \
"""\
0/1
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

Second example:

3

1 1 1.

even is False.

product_mod_phi: 1*1*1 mod phi=1.

exponent_for_2: 1-1=0 mod phi=0.

pow_2=1.

p=(1-1)*inv3 →0.

q=1.

Third example: n=2.

product is 2 → even.

exponent_for_2: 2-1=1.

pow_2=2.

p=(2+1)*inv3 →3*inv3=1.

q=2 →1/2.

Which is correct.

Another example: n=3 (odd).

product is 3 → odd.

product_mod_phi =3 mod phi=3.

exponent_for_2 =3-1=2.

pow_2=4.

p=(4-1)*inv3 →3*inv3=1.

q=4 →1/4.

Which is correct.

Another example: n=4 (even).

product is4 → even.

product_mod_phi=4 mod phi=4.

exponent_for_2=4-1=3.

pow_2=8.

p=(8+1)*inv3=9*333333336 mod MOD →9 * 333,333,336 = 3,000,000,024 → mod 1e9+7 →3,000,000,024 - 3*1e9+7 →3e9+21 →3e9+21 mod 1e9+7 is 3e9+21 -3*(1e9+7) →3e9+21 -3e9-21=0 →0? No, wait.

Wait, 3e9+21 divided by 1e9+7:

3*(1e9+7) =3e9 +21 →3e9+21.

So 3e9+21 =3*(1e9+7) → mod is 0.

So (9 * inv3) mod MOD is 3 mod MOD.

Wait, 9*inv3 mod MOD is (9 * 333333336) mod MOD.

But 9 * 333333336 = 3,000,000,024.

3e9+24 mod 1e9+7:

1e9+7 is 1,000,000,007.

3e9+24 =3*1,000,000,000 +24 → 3,000,000,024.

3,000,000,024 divided by 1e9+7 →3,000,000,024 = 2*(1e9+7) + (999,999,990).

Wait, perhaps better to compute 3e9+24 mod 1e9+7.

1e9+7 is 1000000007.

3*1e9 is 3,000,000,000.

3e9+24 =3,000,000,024.

3e9+024 / 1e9+7 = 2 * (1e9+7) = 2,000,000,014.

3e9+24 -2e9+14 =1e9+10.

1e9+10 mod 1e9+7 is 3.

So 9 * inv3 mod MOD is 3.

So p=3 mod MOD.

q=8 mod MOD.

So 3/8 → which is 0.375 → correct.

So the code works.

Thus, the final code is as written.
</think>

```python
k = int(input())
a = list(map(int, input().split()))

MOD = 10**9 + 7
phi = MOD - 1

even = any(num % 2 == 0 for num in a)

product_mod_phi = 1
for num in a:
    product_mod_phi = (product_mod_phi * (num % phi)) % phi

exponent_for_2 = (product_mod_phi - 1) % phi
pow_2 = pow(2, exponent_for_2, MOD)
inv3 = pow(3, MOD - 2, MOD)

if even:
    p = (pow_2 + 1) * inv3 % MOD
else:
    p = (pow_2 - 1) * inv3 % MOD
q = pow_2 % MOD

print(f"{p}/{q}")
```
