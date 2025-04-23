<think>
Okay, let's try to figure out how to solve this problem. The task is to compute the function f(x, y) as defined. Let's understand the function first.

The function f(a, b) is recursive. For the base case, when b is 0, it's 0. Otherwise, it's 1 plus f(a, b - gcd(a, b)). So each step, we subtract the gcd of a and current b from b, and increment the count by 1. We need to find how many steps it takes to reduce b to 0.

But for large values of x and y (up to 1e12), a straightforward recursive or iterative approach that computes each step one by one would be way too slow. So we need a smarter way to calculate the steps in bulk when possible.

Let's think about how the process works. Suppose we have a current value of b. The gcd(a, b) is g. Then, subtracting g from b gives the new b. But maybe there's a way to compute how many times we can subtract multiples of g before the gcd changes.

Wait, but the problem is that the gcd(a, b) could change each step. For example, if a is 3 and b is 5. Let's walk through the example:

First step: gcd(3,5) is 1. Subtract 1 → b becomes 4. Count is 1.
Second step: gcd(3,4) is 1. Subtract 1 → b becomes 3. Count is 2.
Third step: gcd(3,3) is 3. Subtract 3 → b becomes 0. Count is 3. So total steps 3, which matches the example.

Another example: x=6, y=3. gcd(6,3) is 3. Subtract 3 → 0. So one step. Correct.

So the key is to find how the gcd changes as we reduce b. Let's think about when the gcd(a, b) changes. Suppose current gcd is g. Then, when we subtract g from b, the new b is (b - g). Then, the new gcd(a, b') where b' is b - g. But since a was a multiple of g (since g is the gcd), and b was a multiple of g, then b' is also a multiple of g. So the new gcd(a, b') must be the gcd(g, b')/g ? Wait, maybe not. Wait, let's see:

If a = g * a', and b = g * b', then gcd(a, b) is g * gcd(a', b'). Then when we subtract g, the new b is g*(b' - 1). Then the new a and new b are still multiples of g, so the gcd would be g * gcd(a', b' - 1). So the gcd can decrease, but remains a multiple of the original g.

Wait, but maybe in each step, the gcd can stay the same or decrease, but not increase. So the process can be broken down into phases where during each phase, the gcd remains a certain value. Then, for each phase, we can compute how many steps are needed until the gcd changes.

So the approach is to find all the possible g values (gcds) that occur during the process and compute the steps in bulk for each phase where the current g remains the same.

Let's formalize this.

Let’s denote that in a certain phase, the current gcd is g. Then, during this phase, each step reduces b by g. But wait, no. Because after subtracting the current g (which is the gcd(a, current b)), the next step's gcd may change.

Wait, but during the phase where the gcd is g, the steps would involve subtracting g each time, but only until the next time the gcd(a, new_b) changes.

Wait, no. Let's take the first example again. The initial gcd is 1. Then subtracting 1 each step. But in that case, after each subtraction, the new b is (5-1=4, then 4-1=3, then 3-3=0). Wait, but when b becomes 3, the gcd(3,3) is 3, which changes. So in the first phase, the steps where the gcd is 1 are two steps (from 5 to 4, then to 3), but in the third step, the gcd jumps to 3.

So how can we model this? For each possible g (the current gcd), we need to compute how many steps can be taken where the gcd remains g. Then, the next phase will have a new gcd.

So the algorithm would be:

Initialize res = 0, current_b = y.

While current_b > 0:

    Compute g = gcd(x, current_b)
    subtract g from current_b, add 1 to res. But this is the naive approach. Instead, find how many steps can be taken in this phase where the next steps would subtract g each time until the gcd changes.

Wait, but how can we find the number of steps in this phase?

Let me think. Suppose current_b is B. The current gcd is g = gcd(x, B). Then, after subtracting g once, the new B is B - g. Now, the new gcd is g_new = gcd(x, B - g). Let's see:

x = a * g, since g divides x (as it's the gcd of x and B). B was a multiple of g (since g is gcd of x and B). So B = b * g. Then, B - g = (b-1)*g. So x = a * g, B - g = (b-1)*g. So the gcd of a*g and (b-1)*g is g * gcd(a, b-1). So the new gcd is g * gcd(a, b-1). So the new gcd could be the same as g (if a and b-1 are coprime), or a smaller multiple.

Wait, but in this case, the next step's gcd is either the same as g (if the new gcd is g) or lower. So when would the steps continue to subtract g?

In other words, during the current phase, we can take k steps where in each step, the current_b is reduced by g, and the gcd remains g. Once the new_b is such that the gcd(x, new_b) is not g, then the phase ends.

But how can we compute k, the number of steps in this phase?

Alternatively, we can model the problem as follows: when the current_b is B, and the current gcd is g. We want to find the maximum number of steps s such that when we subtract s*g from B, the new_b is B' = B - s*g, and in all steps from B down to B' (excluding B'), the gcd was g. Then, the new gcd when B becomes B' is different from g.

So how to find s?

Let’s see. Let's write x = g * x', and B = g * B'. Then, B' = B/g, x' = x/g. Since g is the gcd(x, B), x' and B' must be coprime (since we divided by their gcd). Now, when we subtract s steps of g, B becomes B - s*g = g*(B' - s). So the new B is g*(B' - s). The new gcd is g * gcd(x', B' - s).

So the new gcd is g * d, where d = gcd(x', B' - s). For the next step to have the same g, we need d = 1. But during the steps, the s is such that each subtraction of g would lead to a new B, and the new gcd for that new B would be g * d_i. However, for all steps in the current phase, the d_i must be 1. But perhaps after s steps, when B reaches B' - s, d becomes different than 1.

But how to find the maximum s such that for all t in 0 < t <= s, B' - t is coprime with x'?

Wait, perhaps not exactly. Because in each step, after subtracting t*g, the new B is B - t*g = g*(B' - t), and the new gcd is g * gcd(x', B' - t). So for the phase to continue, we need that the gcd(x', B' - t) must be 1. Because then the next step's gcd would be g * 1 = g, so the phase continues. Wait, but no. Because in the next step, the current_b is B - t*g, and the new gcd is g * gcd(x', B' - t). So if that is equal to g, then the phase continues. Otherwise, the gcd becomes smaller than g, so the phase ends.

So the phase ends when the new gcd is less than g. So the maximum s we can take is such that when we subtract s steps of g, the new B is B - s*g, and the new gcd (after s steps) is less than g.

But how to find s?

Alternatively, the phase ends when the new_b (after subtracting s steps) is such that the gcd(x, new_b) < g. Let's think:

The new_b is B - s*g. So, new_b = g*(B' - s). So the gcd(x, new_b) = g * gcd(x', B' - s).

We want the first s where this gcd is less than g, which happens when gcd(x', B' - s) < 1? No, that's not possible. Wait, the gcd is at least 1. Wait, perhaps the new gcd is g * d, where d is the gcd(x', B' - s). So if d is less than 1, that's impossible. So the only way for the new gcd to be less than g is if d < 1, which is impossible. Wait, that can't be right.

Wait, perhaps I made a mistake here.

Original x and current_b are such that x = g * x', current_b = g * b', where gcd(x', b') = 1. Because the gcd(x, current_b) is g.

Now, after subtracting s steps of g, the new_b is g*(b' - s). So the new gcd is g * d, where d = gcd(x', b' - s). So for d to be greater than 1, x' and (b' - s) must share a common divisor d > 1.

So the phase ends when (b' - s) is not coprime with x'. So, the maximum s such that (b' - s) is coprime with x' is the first s where (b' - s) shares a common divisor with x'.

Wait, no. Because s is the number of steps. Wait, maybe the way to model this is: we want to find the largest possible s such that for all steps from 0 to s-1, the (b' - t) is coprime with x', and then when t = s, (b' - s) is not coprime with x'. But that's not necessarily the case. It could be that after s steps, the new_b is such that the next step's gcd is less than g.

Alternatively, the current phase can take s steps where each step subtracts g. The phase stops when the new_b (after s steps) has a gcd with x that is less than g. So the maximum s is the maximum number of steps where, after subtracting s*g, the new_b's gcd with x is less than g. But how?

Wait, perhaps the phase can be extended as long as (x, new_b) has gcd g. So the steps in this phase are all the steps where the gcd remains g. Then, when the new_b is such that the gcd becomes less than g, we stop the phase.

So the problem is: find the maximum s where for all t in 0 <= t < s, the gcd(x, B - t*g) is g, and the next step (after s steps) would have a gcd less than g.

But this seems complicated. How to compute s?

Alternatively, since after each step, the new_b is B - t*g (for t steps), and we need to find the first t where the gcd(x, B - t*g) is less than g.

Wait, but the first occurrence where this happens will be when (B - t*g) is such that the gcd(x, B - t*g) is a divisor of g, but not equal to g. So, the first t where x and (B - t*g) have a gcd less than g.

But x is fixed. Let's think about x and B - t*g. Since B is a multiple of g (B = g*b'), and x is a multiple of g (x = g*x'), then B - t*g = g*(b' - t). So the gcd(x, B - t*g) = g * gcd(x', b' - t).

So, the gcd will be equal to g if and only if gcd(x', b' - t) is 1. So for each step in the phase, as long as (b' - t) and x' are coprime, the phase continues. Once (b' - t) and x' share a common divisor greater than 1, the gcd of x and B-t*g will be g * d, where d is that common divisor, which is greater than 1. So that's when the phase ends.

So, the phase ends when (b' - s) and x' have a gcd greater than 1. So the maximum number of steps s that can be taken in this phase is the maximum s where (b' - s) is the first value in the sequence b', b'-1, b'-2, ... such that gcd(x', (b' - s)) > 1. Then, the number of steps in this phase is s steps.

Wait, no. Because in each step, the current_b decreases by g. So the steps in the phase are s steps where in each step, the current_b is B, B-g, B-2g, ..., B-(s-1)g, and after s steps, current_b is B - s*g, which is when the gcd changes.

But how to compute s? Let's think:

We need to find the maximum s such that (b' - s) has a gcd greater than 1 with x'. But since x' and b' are coprime (because the initial gcd was g, which is the product of the original x and B's gcd), when we subtract steps, we need to find the first s where (b' - s) shares a common divisor with x'.

Alternatively, the maximum s is the minimal d such that (b' - d) shares a common divisor with x', and then s is (current_b' - (d)) steps. Wait, perhaps not.

Wait, let me rephrase: In the current phase, the initial B is g*b'. x' is x/g. We are looking for the maximum s such that (b' - s) is coprime with x' for all 0 <= s < s_max, but (b' - s_max) is not coprime with x'.

So s_max is the largest value where (b' - s_max) is the first (from the current B') to reach a point where the gcd is no longer 1. So s_max is (b' - k), where k is the largest number <= b' such that gcd(k, x') > 1.

Wait, maybe not. Let's think again. Suppose x' is some number. Then, when we subtract s steps of 1 from b' (since each step subtracts 1 in the x' terms), we need to find the first s where (b' - s) shares a common divisor with x'. The maximum s we can take is (b' - (k)), where k is the smallest number less than or equal to b' such that k and x' are not coprime. Then, the s_max is (b' - k) steps. Because subtracting s steps would take us to k = b' - s, and we need to find the largest s such that k is the first number where gcd(k, x') > 1.

Alternatively, the maximum number of steps s that can be taken in this phase is (b' - k) where k is the smallest number ≤ b' where gcd(k, x') > 1. Then, s = b' - k.

Wait, for example, let's say x' is 3, and b' is 5. Then, x' is 3, b' is 5. We subtract steps until (5 - s) shares a divisor with 3. The possible k values are 3, 6 is not possible. So the first k is 3. So s_max is 5 - 3 = 2 steps. Then, after 2 steps, current_b is 5-2=3, which shares a divisor 3 with x' (3). So the next phase's gcd is g * 3, which is 3*1*3=3*3=9? Wait, no. Original g was 1 (since in the example x=3, y=5. x is 3, which is x' = 3, and initial g is 1. So in this phase, x' is 3, and b' is 5. Then, s_max is 2 steps. After that, the new b' is 5-2=3. The new gcd is 3* gcd(3,3) =3*3=9. Wait, but original x is 3, and the new_b is 3. The gcd(3,3) is 3. So yes. So in this case, after 2 steps, the phase ends, and the next phase's gcd is 3.

So the maximum steps s in this phase is 2. Then, the next phase's current_b is 3, and the gcd is 3.

So in that case, the steps are s=2, then we add 2 steps to the result, then proceed to the next phase.

So the problem reduces to, for each phase, compute s_max as (b' - k), where k is the maximum possible value ≤ b' such that k is the first number in the sequence (starting from b' and decreasing by 1 each step) that shares a common divisor with x'.

But how to compute k efficiently?

Alternatively, k is the largest number less than or equal to b' such that gcd(k, x') > 1. So the maximum s is (b' - k), but we need to find the minimal possible k (i.e., the smallest possible k) to maximize s.

Wait, no. If k is the largest possible, then s would be as small as possible. Wait, no. Because s is the number of steps. For example, if k is the smallest possible (like 0), then s is b' -0 = b' steps. But that's not possible. Because in that case, all steps would be subtracted until k=0, but during that process, some steps might have k where gcd(x',k) is greater than 1.

Wait, perhaps this approach isn't correct. Let's think differently.

The steps in the current phase can be taken until the next step would result in a new_b where the gcd is not g. So, we need to find the smallest s where (b' - s) has a common divisor with x' greater than 1. Then, the maximum steps we can take in this phase is (s-1) steps. Because once we take (s) steps, the new_b would have a gcd less than g, but up to (s-1) steps, the gcd is still g.

Alternatively, the maximum s is (s') where s' is the smallest s where (b' - s) shares a divisor with x' >1, and then the steps we can take is (s') steps. Wait, no. Let's see:

For example, x'=3, b'=5. The possible s values are 0,1,2,3,4,5. We need to find the first s where (5 - s) shares a divisor with 3. Let's see:

s=0: 5 -0=5 → gcd(3,5)=1. No.
s=1: 4 → gcd(3,4)=1. No.
s=2:3 → gcd(3,3)=3. Yes. So the first s where it happens is s=2. So the maximum steps in this phase is 2 steps (from 5 to 3). So after 2 steps, the new_b is 3, which has a gcd of 3*3=9 (if original g was 1). So the next phase's gcd is 3*3=9. But original x is 3, so in the next phase, x is 3, new_b is 3. gcd(3,3) is 3, so subtract 3 steps. Then current_b becomes 0.

So in this example, the first phase allows 2 steps, then the next phase allows 1 step (3 →0). So total steps 3.

So the problem is to find the minimal s where (b' - s) has a gcd with x' > 1, then the number of steps in this phase is s steps (because subtracting s steps would take us to (b' -s) which is the first value that has a common divisor with x').

Wait, but in that case, for the example x'=3, b'=5: the minimal s is 2 (since s=2 is the first s where (5-2) =3 has gcd 3 with x'=3. So the steps in the phase would be s=2 steps. Then the new_b is 3, which has a gcd of 3*3=9. But the next step would subtract 9 from 3, which is not possible. Wait, no. Wait, the current_b is 3 (after subtracting 2 steps of 1). Then the next step's gcd is gcd(3,3) =3. So subtract 3 → 0. So that's one step. So the total steps are 2+1=3.

So the way to model this is: each phase, subtract s steps where s is the minimal s such that (b' - s) has a common divisor with x' >1. Then, the number of steps in the phase is s steps. Then, the new_b is (b' - s) * g. Then, compute the next phase's g as g_new = g * d, where d is the gcd(x', (b' - s)).

But how to compute s efficiently?

So the problem is to find the minimal s ≥1 such that (b' - s) shares a divisor with x' greater than 1. Then, the maximum steps in this phase is s steps. Because in the current phase, each step subtracts g, and after s steps, the new_b is (b' - s)*g, which has a gcd with x of g*d, where d is the gcd(x', (b' -s)). So the next phase's gcd is g*d.

But if there's no such s (i.e., all (b' -s) for s from 1 to b' are coprime with x'), then the phase can take all possible steps (b' steps), which would reduce the current_b to 0, and the process ends.

So how to compute the minimal s?

The minimal s is the minimal s where (b' -s) has a common divisor with x' greater than 1. So (b' -s) must be divisible by at least one prime factor of x'.

So to compute s, we can find the largest prime factor of x' that divides any of the numbers (b' - s) for s from 1 to b'. Then, the minimal s would be the minimal such s where (b' -s) is divisible by any prime factor of x'.

Wait, but how?

Alternatively, for each prime factor p of x', compute the maximum k where p divides (b' - s), which implies s ≡ (b' mod p). So s can be (b' mod p) or (b' mod p) - p (if that's possible). Wait, no. Because (b' - s) mod p =0 → s ≡ b' mod p.

So for each prime factor p of x', the possible s where (b' -s) is divisible by p is s ≡ b' mod p. The minimal s (≥0) is s = (b' mod p). For example, if p=3 and b'=5, then 5 mod 3 is 2. So s=2. Then (5-2)=3, which is divisible by 3. So for p=3, the s is 2.

So the minimal s across all prime factors of x' would be the minimal of (b' mod p) for each prime p of x', and then take the minimal s. But wait, no. Because for each prime p, the minimal s is (b' mod p). If that is 0, then s=0 is possible. But s must be ≥1 (since we subtract s steps). Wait, no. Because in the phase, each step is subtracting s steps. So s can be 0 steps if there's no such s, but in that case, the phase would take 0 steps and proceed to the next phase. But that can't happen. So perhaps for each prime p in x's factors, the possible s is (b' mod p), but if that's 0, then (b' mod p) is 0, so s=0 would mean (b' -0) is divisible by p. But in that case, the current_b is already at a point where the next step's gcd would be p. So in that case, s=0 steps can be taken, which implies that the phase is zero steps. That's not possible.

Wait, perhaps I'm getting this wrong. Let's think again. For each prime p that divides x', we can find the minimal s such that (b' -s) is divisible by p. That s is equal to (b' mod p). If (b' mod p) is zero, then s=0. But since in the phase, we can take steps s where s is the minimal such that (b' -s) is divisible by p, then if (b' mod p) is zero, then s=0. But that would imply that the current b' is already divisible by p. But since x' and b' were coprime (from the initial phase's setup), this can't happen. Because x' and b' are coprime. So any prime factor of x' cannot divide b'. So (b' mod p) is not zero. So s can be (b' mod p), which is in the range [1, p-1].

So for each prime p in the prime factors of x', the minimal s for which (b' -s) is divisible by p is (b' mod p). Then, among all these possible s values, the minimal s is the minimal (b' mod p) across all primes p dividing x'.

So for example, if x' is 6 (primes 2 and 3), and b' is 5:

For p=2: 5 mod 2 is 1. So s=1. (5-1=4, divisible by 2).

For p=3:5 mod 3 is 2. So s=2. (5-2=3, divisible by 3).

So the minimal s is 1. So the phase would take 1 steps, then the new_b is (5-1) =4. The next phase's gcd would be g * 2 (since x'=6, new_b'=4, which is 4/2=2, and gcd(6,2)=2 → d=2. So new gcd is g*2. But what is the original g here? Let's say original g was 1.

So in this case, the phase would take 1 step, adding 1 to the result. Then the new_b is 4, and the new gcd is 2. Then, the next phase would process this.

But wait, the steps are subtracted from the current_b. So after s steps of g, the new_b is (b' -s) *g. So in this case, original g is 1. So after 1 step, new_b is (5-1)*1=4. Then, the new phase's gcd is gcd(x, 4) = gcd(6,4) = 2. So the next phase's g is 2. Then, we proceed.

So the steps in the first phase are 1 step. Then, the next phase will have g=2, and current_b=4.

So in the next phase, x=6, current_b=4. So x/g=3, current_b/g=2. So x'=3, b'=2. So x' and b' are coprime (since 3 and 2 are coprimes). So we need to find the minimal s where (2-s) is divisible by any prime factor of x'=3. The primes are 3. For p=3, 2 mod 3 is 2. So s=2. But 2-s=0. 0 is divisible by 3. So s=2. But the current_b is 2. Subtracting 2 steps of g=2 would take current_b to 2-2*2= -2, which is impossible. So perhaps in this case, the minimal s is 2 steps, but that's more than the current_b allows. So in this case, since (2-s) must be >=0, s can't be larger than 2. So s=2 would take current_b to 0. Then, the new gcd is gcd(6, 0) which is 6. But according to the function's definition, when b is 0, we return 0. So in this case, after the phase, the new_b is 0. So this phase's steps would be 2 steps. So the total steps are 1 (first phase) + 2 (second phase) = 3 steps. Wait, but what is the actual process here?

Original x is 6, initial y=4.

Step 1: gcd(6,4) is 2. Subtract 2 → current_b becomes 2. Res +=1.

Step 2: gcd(6,2) is 2. Subtract 2 → current_b becomes 0. Res +=1. Total steps 2. So the answer is 2. But according to the model, the phases would be:

First phase: x' =6/2=3, b'=4/2=2. Then, we need to find the minimal s where (2-s) is divisible by primes of x' (3). For p=3: 2 mod 3 is 2. s=2. But 2-s=0. So s=2 steps. So in this phase, we subtract 2 steps of 2, each step reduces current_b by 2. So after two steps, current_b is 0. So res +=2. So the total steps would be 2. Which matches the example.

Hmm. So the model works.

So, to compute the minimal s in each phase, we need to:

1. For each prime factor p of x', compute s_p = b' mod p. If s_p is 0, then s_p is 0 (but this can't happen as x' and b' are coprimes, so p doesn't divide b').

2. The minimal s is the minimal s_p among all primes p of x'.

3. If x' is 1 (i.e., x has no prime factors), then the gcd remains g for all steps. So the phase can take all steps (b' steps), as x' is 1. So since gcd(1, anything) is 1. So in this case, s = b' steps.

So the algorithm would be:

Loop until current_b is 0:

   compute g = gcd(x, current_b)

   compute x' = x / g

   compute b' = current_b / g

   if x' == 1:

       res += b'

       break

   else:

       find all the prime factors of x'

       for each prime p in factors of x':

           s_p = b' mod p

       s_min = min(s_p for all p)

       if s_min == 0:

           s_min = 0

       else:

           s_min = the minimum of all s_p

       if all s_p are >= b' (i.e., no primes in x' divide any (b' - s)) for s up to b'):

           then s = b' (take all steps)

       else:

           s = s_min

       res += s

       current_b = current_b - s * g

But wait, in the case where x' is 1, the phase can take b' steps. So that's handled.

But how to compute the prime factors of x' quickly?

But x can be up to 1e12, and x' can be up to 1e12 / 1 = 1e12. So factoring x' could be time-consuming if done naively. So we need an efficient way to factor numbers up to 1e12.

But for numbers up to 1e12, trial division could work if optimized. For example, trial division up to sqrt(n) can handle numbers up to 1e12, since sqrt(1e12) is 1e6. So trial division up to 1e6 is manageable.

Alternatively, we can use Pollard's Rho algorithm for faster factorization.

But for code submission, especially in Python, trial division up to 1e6 may be acceptable for numbers up to 1e12, especially since the number of test cases is small (per test case).

So, the steps are:

For each phase:

1. Compute g = gcd(x, current_b)

2. Compute x' = x // g, current_b' = current_b // g

3. If x' is 1:

   add current_b' to the result and break.

4. Else:

   find all the prime factors of x' (unique primes, since factors can be repeated, but we need unique ones)

   for each prime p in the factors:

       compute s_p = current_b' mod p

   find the minimum s_p among these. Let's call it s_min.

   but wait, if s_min is 0, but x' and current_b' are coprimes (from step 3, since x' and current_b' are coprimes?), which can't be possible. Because current_b' is current_b // g, and x' is x // g. So x and current_b have gcd g. So x' and current_b' are coprimes.

So if x' and current_b' are coprimes, then current_b' mod p can't be 0, since p is a prime factor of x', which is coprime with current_b'.

Therefore, for each p, s_p is in the range [1, p-1].

Then, s_min is the minimal such s_p.

But how to handle the case where there are no primes (x' is 1)? Which is handled in step 3.

So the minimal s is s_min. Then, the steps in this phase is s_min.

But wait, let's think: after s_min steps, current_b' becomes current_b' - s_min. So (current_b' - s_min) must be divisible by p, which is a prime factor of x'. So the new_b' is (current_b' - s_min) = k*p.

But then, the new x' and new_b' (current_b' - s_min) would have gcd p (since p divides x' and current_b' - s_min). So the next phase's g would be g * p.

So after s_min steps, the new current_b is (current_b' - s_min) * g.

But then, in the next phase, the new g is gcd(x, new_current_b) = gcd(g x', (current_b' - s_min) g) = g * gcd(x', current_b' - s_min) = g * p (since p divides both x' and current_b' - s_min).

So the next phase's steps would process this new g.

So the code outline is:

def compute_f(x, y):

    res = 0

    current_b = y

    while current_b > 0:

        g = gcd(x, current_b)

        if g == 0:

            break  # shouldn't happen

        x_prime = x // g

        b_prime = current_b // g

        if x_prime == 1:

            res += b_prime

            break

        # find all prime factors of x_prime

        primes = get_unique_prime_factors(x_prime)

        if not primes:  # x_prime is 1, but that's handled above

            res += b_prime

            break

        # compute s_min = min (b_prime mod p for p in primes)

        s_min = min(b_prime % p for p in primes)

        # but wait, if any (b_prime % p) is zero, but that's impossible since x' and b' are coprimes

        # compute the minimal s_p

        s = s_min

        if s == 0:

            # impossible, since primes are factors of x', and x' and b' are coprimes

            # so this can't happen

            pass

        # compute how many steps to take: s steps

        res += s

        current_b = current_b - s * g

    return res

But wait, in the case where x' is 6 (primes 2 and 3), and b' is 5:

primes are 2 and 3.

b_prime mod 2 = 1 (5 mod 2 is 1)

b_prime mod 3 = 2 (5 mod 3 is 2)

s_min is 1. So steps is 1. Then current_b = 5* g (which is initial g) minus s * g. Wait, no. current_b was divided by g earlier. So current_b is (b_prime - s) * g.

Wait, current_b is initialized as current_b = y. Then, in each iteration:

current_b is divided by g to get b_prime. So current_b is g * b_prime.

So after s steps of subtracting g each step, the new current_b is (b_prime - s) * g. Because each step subtracts g, s times: current_b = current_b - s * g = g*b_prime - s*g = g*(b_prime -s).

So yes.

Thus, the code correctly subtracts s steps.

But how to compute the prime factors of x_prime?

We need a function to compute the unique prime factors of a number.

Implementing this in Python.

But for numbers up to 1e12, trial division is feasible.

So the function get_unique_prime_factors(n) would return the set of primes dividing n.

But for n up to 1e12, trial division up to sqrt(n) is acceptable.

So here's the code for that:

def get_unique_prime_factors(n):

    factors = set()

    i = 2

    while i * i <= n:

        if n % i == 0:

            factors.add(i)

            while n % i == 0:

                n = n // i

        i += 1

    if n > 1:

        factors.add(n)

    return factors

This code will return the unique prime factors of n.

Testing this:

For n=6, factors are 2 and 3.

For n=3, factors are {3}.

For n=12, factors are {2,3}.

Yes.

Now, putting this all together.

But there's a case where x_prime is 1. For example, x=2, y=3. Then, in the first iteration:

g = gcd(2,3)=1.

x_prime =2/1=2, but no, wait, x is 2, current_b is 3.

Wait, no: x is 2, current_b is 3. g = gcd(2,3)=1. So x_prime =2/1=2, b_prime =3/1=3.

x_prime is 2, which is not 1. So find primes of 2, which is {2}.

Compute s_p = 3 mod 2 → 1. So s_min=1.

Add 1 to res. current_b becomes 3 -1*1=2.

Next iteration: current_b is 2.

g = gcd(2,2)=2.

x_prime=2/2=1, b_prime=2/2=1.

x_prime is 1 → add 1 to res and break. Total res=2.

But according to the actual steps:

Step 1: gcd(2,3) is 1. Subtract 1 → 2. res=1.

Step 2: gcd(2,2) is 2. Subtract 2 → 0. res=2. Correct.

So the code works.

Another example: x=6, y=3.

First iteration: current_b=3. g = gcd(6,3)=3.

x_prime=6/3=2. b_prime=3/3=1.

primes of 2 → {2}.

s_p=1 mod 2 →1. s_min=1.

But current_b is 3. Then, subtract s * g → 1 *3=3. So current_b becomes 3-3=0. res +=1.

Loop ends. So the answer is 1. Correct.

Another example: x=3, y=5.

First iteration:

g=1. x_prime=3, b_prime=5.

primes of 3 → {3}.

s_p=5 mod3 →2. s_min=2.

res +=2 → current_b =5 - 2*1=3.

Next iteration: current_b=3.

g=3. x_prime=3/3=1. b_prime=3/3=1.

x_prime is 1 → res +=1. Total res=3. Correct.

Thus, the code works for the sample inputs.

Now, the code needs to handle large numbers. For example, x and y up to 1e12.

But the key is that the factorization step for x_prime can be done quickly. For example, if x is a prime number, then x_prime could be up to 1e12, but the trial division would check up to sqrt(x_prime), which is 1e6, which is manageable.

But what if x_prime is a large prime? Like 1e12. Then the trial division will check up to 1e6, but since 1e6^2 is 1e12, which is the maximum possible x_prime, it would take O(1e6) operations per factorization. But 1e6 iterations in Python are acceptable within the time limit (since each iteration is a simple mod operation and loop). But wait, in the worst case, when x is a product of two primes of around 1e6, this would take O(1e6) steps. However, the number of phases is logarithmic in y. For example, each phase reduces current_b by s steps, which could be up to O(b') steps. But in the worst case, each phase could reduce current_b by a small number of steps. But since y can be up to 1e12, the number of phases could be up to log(y) steps. For example, each phase reduces the current_b by a factor of at least 2. So for 1e12, log2(1e12) is about 40 steps. Each step requires factorization of x_prime, which in the worst case is O(1e6) steps. 40 * 1e6 = 4e7 operations. Which might be tight for Python's time limit of 1 second (as Python can handle around 1e8 operations per second, but 4e7 is 40 million, which is 0.4 seconds. So perhaps acceptable.

But there are possible optimizations. For example, memoizing the factors of x. But since x is fixed, perhaps precomputing its factors once. Wait, in the code, x is fixed, but x_prime can change in each phase. Because x_prime is x divided by the current g. So for example, if x is 6 and current_b is 5, then x_prime is 6/1 =6. Then, in the next phase, x is 6, current_b is 3. The gcd is 3, so x_prime is 6/3=2. So the x_prime changes in each phase. So it's not possible to precompute the factors of x once. So each phase may need to factor a different x_prime.

Thus, the factorization code needs to be as efficient as possible.

Another optimization: during the factorization of x_prime, after dividing out a prime, we can check if the remaining n is 1 and break early.

The current code does this. For example, if n is divided by 2, then 2 is added to factors. Then, while n is divisible by 2, it's divided by 2. Then, if n becomes 1, the loop breaks.

So that's efficient.

Thus, the code should work for the given constraints.

Now, writing the Python code.

But in Python, the gcd function can be obtained from math.gcd, but note that math.gcd returns the absolute value, but since x and current_b are positive, it's okay.

But also, note that in Python 3, math.gcd returns the correct gcd, but if current_b is zero, but in the loop, current_b is checked to be greater than zero. So that's handled.

So the code:

Implement the steps as described.

Read x and y, then compute f(x, y).

The code:

import math

def get_unique_prime_factors(n):

    factors = set()

    if n == 1:

        return factors

    i = 2

    while i * i <= n:

        if n % i == 0:

            factors.add(i)

            while n % i == 0:

                n = n // i

        i += 1

    if n > 1:

        factors.add(n)

    return factors

x, y = map(int, input().split())

res = 0

current_b = y

while current_b > 0:

    g = math.gcd(x, current_b)

    x_prime = x // g

    b_prime = current_b // g

    if x_prime == 1:

        res += b_prime

        break

    primes = get_unique_prime_factors(x_prime)

    s_min = min( (b_prime % p) for p in primes )

    res += s_min

    current_b = current_b - s_min * g

print(res)

Wait, but in the code, when x_prime is 1, we add b_prime to res and break. That's correct.

But let's test this code with the examples.

First example:

Input 3 5:

The code:

current_b =5.

g = gcd(3,5)=1.

x_prime=3/1=3.

b_prime=5/1=5.

primes of 3: {3}.

s_min =5%3=2.

res +=2. current_b=5 - 2*1=3.

Next iteration:

current_b=3.

g =3.

x_prime=3/3=1.

b_prime=3/3=1.

add 1 to res. res is 2+1=3. Break. Correct.

Second example:

Input 6 3.

current_b=3.

g =3.

x_prime=6//3=2.

b_prime=3//3=1.

x_prime !=1.

primes of 2: {2}.

s_min=1%2=1.

res +=1. current_b=3-1*3=0. Loop ends.

Total res=1. Correct.

Another test case: x=2, y=3.

current_b=3.

g=1.

x_prime=2.

primes {2}.

s_min=3%2=1.

res +=1. current_b=3-1*1=2.

Next iteration:

current_b=2.

g=2.

x_prime=2//2=1.

res +=2//2=1.

Total res=2.

Which is correct.

Another test case: x=6, y=4.

current_b=4.

g = gcd(6,4)=2.

x_prime=6//2=3.

b_prime=4//2=2.

primes {3}.

s_min=2%3=2.

res +=2. current_b=4 - 2*2=0. Loop ends. res=2.

Which is correct.

Another example: x=12, y=15.

First iteration:

current_b=15.

g=3.

x_prime=4.

primes are 2.

b_prime=5.

s_min=5%2=1.

res +=1. current_b=15 -1*3=12.

Next iteration:

current_b=12.

g=12.

x_prime=12/12=1.

res +=12/12=1. Total res=1+1=2.

But what's the actual steps:

Step1: gcd(12,15)=3. subtract 3 →12. res=1.

Step2: gcd(12,12)=12. subtract12 →0. res=2. Correct.

So code works.

Thus, the code should be correct.
</think>

```python
import math

def get_unique_prime_factors(n):
    factors = set()
    if n == 1:
        return factors
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            while n % i == 0:
                n = n // i
        i += 1
    if n > 1:
        factors.add(n)
    return factors

x, y = map(int, input().split())

res = 0
current_b = y

while current_b > 0:
    g = math.gcd(x, current_b)
    x_prime = x // g
    b_prime = current_b // g
    if x_prime == 1:
        res += b_prime
        break
    primes = get_unique_prime_factors(x_prime)
    s_min = min((b_prime % p for p in primes), default=0)
    res += s_min
    current_b -= s_min * g

print(res)
```