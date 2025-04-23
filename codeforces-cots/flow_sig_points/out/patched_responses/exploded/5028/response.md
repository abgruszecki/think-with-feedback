<think>
Okay, I need to solve this problem where the King wants to determine the expected number of coin tosses required to select a knight with equal probability 1/n. The coin is fair, and the strategy must be optimal to minimize the expected tosses. Let's think through this step by step.

First, let's understand what's required. The problem is about finding the minimal expected number of coin flips needed to generate a uniform distribution over n options. Each flip gives a bit (0 or 1), and the King needs to decide a strategy that uses these bits in a way that each knight has exactly 1/n probability, and the expected number of flips is minimized.

Let's start with some examples. For n=2, the solution is 1/1. That's straightforward because one flip (heads or tails) gives two possibilities, each with probability 1/2. So expected flips is 1.

For n=3, the output is 8/3. Hmm, how does that work? Let's think. To represent 3 possibilities, you need at least log2(3) ≈ 1.58496 bits. So each trial would require flipping the coin multiple times until you can split the possibilities. Maybe using a decision tree approach where each path in the tree corresponds to a possible outcome. But since 3 is not a power of two, the process might involve some rejection of certain outcomes.

For example, one approach could be to flip the coin twice. The possible outcomes are 00, 01, 10, 11 (each with probability 1/4). If we assign three of these to the three knights and the fourth as a "reject" and try again. The probability of success each trial is 3/4, and each trial uses 2 flips. The expected number of flips would be 2 * (1/(3/4)) ) = 8/3, which matches the example. So that's how it's done here.

For n=4, the answer is 2/1. Since 4 is a power of two, two flips give exactly four possibilities. So each trial is two flips, no rejections. So expected value is 2.

So the general approach is to model this as a process where each step involves flipping some number of bits, and then based on those bits, either assign a knight or restart the process. The key is to find the minimal expected value.

The problem reduces to finding the minimal expected number of coin flips required to generate a uniform distribution over n outcomes using a fair coin. The expected value can be computed recursively.

Let's model this with dynamic programming. For a given n, E(n) is the minimal expected number of flips needed. Then, for each possible k (number of bits to generate in a trial), we can see how many outcomes can be grouped into n, and compute the expected value based on the probability of needing to restart.

Wait, perhaps another approach is better. Let's think of the process as a series of trials. Each trial consists of flipping t coins, which gives 2^t possible outcomes. We need to partition these outcomes into m groups where m is the maximum number such that m ≤ 2^t and m is a multiple of n. Wait, maybe not. Let me think again.

Alternatively, each trial uses some number of bits (like k bits) such that 2^k ≥ n. Then, we can assign each of the n possible outcomes to certain k-bit sequences. But if 2^k mod n is not zero, then the probability of each outcome is (2^k // n) / 2^k. Wait, no. For example, for n=3, 2^2=4. Assign each of 3 outcomes to one of the 4 possibilities, and leave one as a rejection. Then, the probability of success in a trial is 3/4, and the expected number of trials is 4/3. Each trial uses 2 flips. So the expected flips are 2 * 4/3 = 8/3, which matches the example.

So the general idea is to find the smallest k such that 2^k ≥ m, where m is the least multiple of n that is ≤ 2^k. Wait, perhaps not. Let me rephrase. For a given trial, we want to generate as many usable outcomes as possible. The process is to find a k where 2^k is divisible by m (but m is not necessarily equal to n). Wait, maybe for each possible k, we can generate 2^k possible outcomes. Then, we can group these outcomes into groups of size (2^k // n). Wait, perhaps not.

Alternatively, the process is as follows: find the smallest k such that 2^k is at least n. Then, split the 2^k outcomes into n groups, each of size s = 2^k // n. The remaining r = 2^k % n outcomes are rejected. The probability that a trial (k flips) is successful is (2^k - r)/2^k = (n * s)/2^k. So the expected number of trials is 2^k/(n*s). The expected number of flips is k * (expected number of trials). But wait, this might not hold because the trials can vary in k. Hmm, maybe not.

Alternatively, perhaps the optimal strategy is to use a binary decision tree where each node represents a possible flip, and the leaves correspond to the outcomes. Each leaf has probability 1/n. The expected number of flips is the average depth of the leaves. But building such a tree optimally might be tricky.

Another approach is to model this as entropy and expected value. But perhaps a better way is to model this using the concept of entropy and optimal encoding, but I'm not sure.

Alternatively, the problem can be modeled using the concept of the minimal expected number of bits needed to generate n equally probable outcomes. The minimal expected number is log2(n) (Shannon's source coding theorem). But since each flip gives a bit, the expected number of flips can't be lower than log2(n). However, log2(n) is not always an integer, so we have to account for that. For example, for n=3, log2(3) ≈1.585, which is less than 8/3 ≈ 2.666. So perhaps the optimal strategy is to use multiple trials, each time attempting to cover as much as possible.

Wait, but the example for n=3 gives an expected value of 8/3, which is higher than log2(3). That suggests that the initial approach with trials is the correct model.

So the correct approach is to find the optimal k for each step, but how?

An alternative approach is to model E(n) as the minimal expected number of flips required. We can write a recurrence relation for E(n).

Let me think. For E(n), the King can choose to flip t coins, which gives a binary string of length t. Then, based on this string, he can decide to assign an outcome (a knight) or restart. The strategy is to choose t and a way to split the 2^t possibilities into n groups, each with exactly (2^t - r)/n possibilities, where r is the remainder 2^t mod n.

Wait, perhaps. For example, when n is a power of 2, then t is log2(n) and r is 0. So all possibilities are used, no restarts. Hence E(n) = log2(n).

But when n is not a power of two, then for a certain t, 2^t can be split into n groups each of size s = 2^t // n, and r = 2^t mod n. The total successful outcomes per trial are n*s, so the number of possible successful outcomes is n*s, and the probability of a successful trial is (n*s)/2^t. Then, the expected number of trials is 1/p = 2^t/(n*s) = (n*s + r)/(n*s) = 1 + r/(n*s). Hmm, maybe not. Wait, 2^t = n*s + r. So the probability of success is (n*s)/(n*s + r) = (2^t - r)/(2^t) → s/(s + r/n). Not sure.

But the expected number of trials is 1/(probability of success) → 2^t/(n*s). Because each trial has probability (n*s)/2^t of success. Then the expected number of trials is 2^t/(n*s). Each trial takes t flips, so the expected total flips is t * 2^t/(n*s) + (1 - (n*s)/2^t) * (t + E(n)). Wait, this seems complicated.

Wait, the recurrence would be: Each time, the King uses t flips, which gives a result that either assigns a knight (success) or requires a restart (failure). The expected number of flips would then be:

E(n) = t * p_success + (1 - p_success) * (t + E(n)), where p_success is the probability of success in the current trial.

Wait, solving for E(n):

E(n) = t * p_success + (t + E(n)) * (1 - p_success)

Rearranging:

E(n) = t * p_success + (t + E(n))*(1 - p_success)

E(n) = t * p_success + t*(1 - p_success) + E(n)*(1 - p_success)

E(n) = t [p_success + 1 - p_success] + E(n)*(1 - p_success)

E(n) = t + E(n)*(1 - p_success)

Bringing terms together:

E(n) - E(n)*(1 - p_success) = t

E(n) * p_success = t

E(n) = t / p_success

So this shows that the expected value is t divided by the probability of success. Which makes sense, because each trial takes t flips, and the expected number of trials is 1/p_success. So the total flips are t * (1/p_success) = t/(p_success).

So for the example of n=3, the King can choose to use t=2 flips. Then 2^2=4, which gives 4 possible outcomes. He can assign 3 outcomes to the knights (each with probability 1/4), and one outcome as a failure. The probability of success is 3/4, so E(3) = 2/(3/4) = 8/3. Which matches the sample.

So the key is to choose t and s (the number of trials) such that 2^t >= s, and s is chosen to maximize the probability of success. Wait, no. The problem is to find the minimal E(n) by choosing t and s such that s is the number of successful outcomes possible in each trial, and s is a multiple of n. Wait, perhaps the optimal strategy is to use the minimal possible t such that 2^t >= n, but that's not the case. Let's see.

For example, n=5. Let's see:

t=3: 2^3=8. Then 8 mod 5 is 3. So the number of successful outcomes per trial is 5 * 1 (since 8//5=1). So s=1. The probability of success is 5/8. So E(5) would be 3/(5/8) = 24/5 = 4.8.

Alternatively, could we use a larger t? Let's see. For t=4: 2^4=16. 16 mod 5 is 1. 16//5=3. So each knight is assigned 3 outcomes, and there is 1 rejected. So s=3. The probability of success is (5*3)/16 = 15/16. Then E(5) would be 4/(15/16) = 4*16/15 = 64/15 ≈4.2667, which is better than 24/5=4.8. So using a larger t can give a better expected value.

So the optimal strategy may not be the minimal t. Therefore, the problem is to find, for each n, the best possible t that gives the minimal E(n) = t * (2^t) / (n * s), where s = 2^t // n.

Wait, because in the recurrence, E(n) is t / p_success, where p_success is (n * s) / 2^t. Because for each trial, the number of successful outcomes is n*s (each of the n knights is assigned s possible outcomes). So p_success = (n*s)/2^t. So E(n) = t * 2^t/(n*s).

So for each possible t, we can compute s = floor(2^t / n), then compute the value t * 2^t / (n*s). The minimal such value over all possible t is the answer.

Wait, but how do we know that this approach (using a single t) is the optimal? Because maybe combining multiple different t's can give a lower expected value. But according to the recurrence, the King can choose the best possible t for each step. Wait, but perhaps the optimal strategy is to always use the same t for each trial, which would lead to E(n) = t/(p_success) where p_success is (n*s)/2^t. But maybe there's a better strategy where the King uses varying t's based on previous outcomes.

But the problem states that the King follows the optimal strategy, which minimizes the expected number of tosses. So we need to find the strategy (possibly using varying numbers of flips in each trial) that gives the minimal expected value.

But modeling this seems complicated. However, according to some research, this problem is known as the problem of generating a uniform distribution over n elements using a fair coin, and the minimal expected number of coin flips is given by the sum over k of (k * (2^k mod n)) / (n * 2^k). Wait, that's a different approach.

Alternatively, according to the Knuth-Yao algorithm, the minimal expected number of flips is given by the sum of the binary digits of the expansion of 1/n. But I'm not sure. Alternatively, there's a formula involving the binary representation of n.

But perhaps the optimal approach is to model the expected value as the minimal over all possible t of (t * 2^t)/(n * s), where s = floor(2^t /n). But how to find this t?

Alternatively, the optimal expected number of coin flips can be found by considering all possible t's where 2^t >= n, and for each t, compute E(n) for that t, then take the minimum.

Wait, for example, n=5:

t=3: 8 possible outcomes. s=1 (since 8//5=1), E=3*8/(5*1) =24/5=4.8.

t=4: 16//5=3, s=3. E=4*16/(5*3) =64/15 ≈4.2667.

t=5: 32//5=6. 5*6=30. 32-30=2. So s=6. E=5*32/(5*6) =32/6=5.333..., which is worse than t=4.

t=6: 64//5=12. 12*5=60, 64-60=4. So s=12. E=6*64/(5*12) = (6*64)/(60) = 64/10=6.4. Worse.

So t=4 gives the minimal E for n=5.

So for each n, we need to find the t that gives the minimal value of (t * 2^t) / (n * s), where s = floor(2^t /n).

But how do we find this t efficiently for n up to 10000?

Let's think about how to compute this. For a given n, we need to compute for various t (starting from the minimal t where 2^t >=n) and find the t that gives the minimal value.

But since n is up to 10000, 2^t can get large. However, for each n, the t's to check can't be more than, say, 30 bits. Because 2^20 is about a million, which is larger than 10000. For n up to 1e4, t can't be larger than 20 or so. So for each n, we can iterate t from the minimal possible (ceil(log2(n))) up to, say, 40, compute the value (t * 2^t) / (n * s), where s=2^t //n, and take the minimum of these.

Wait, but how to find the best t?

Let's take the example of n=3.

t=2: 2^2=4. s=1. E=2*4/(3*1)=8/3 ≈2.666.

t=3: 8//3=2. s=2. E=3*8/(3*2)=4. So worse.

t=4:16//3=5. s=5. E=4*16/(3*5)=64/15≈4.266. Worse.

So the minimal is t=2.

Another example, n=5. The best is t=4.

So the minimal t is not necessarily the minimal possible (ceil(log2(n))). So for each n, we need to check all possible t up to a certain limit.

The problem then is to find, for each n, the minimal E(n) over all possible t where t >= ceil(log2(n)).

But how to compute this for each n up to 1e4 efficiently.

The code needs to:

1. For each n, compute the minimal E(n) over all possible t.

But how? Let's think:

For each possible t (starting from t_min = ceil(log2(n)) ), compute s = 2^t //n. Then compute the value (t * 2^t) / (n * s). We need to find the minimal such value over all t.

But for each t, this value can be calculated. The challenge is to find the t that gives the minimal value.

But for n up to 1e4 and t up to, say, 40 (since 2^40 is way larger than 1e4 * 1e4), this is manageable.

So the steps for code:

Given n, compute E(n) as follows:

- For each possible t starting from t_min = ceil(log2(n)) up to a certain maximum (like t_min + 20 or something):

   - Compute 2^t. But for t up to 40, 2^t is manageable even as a big integer.

   - s = 2^t // n

   - current_value = t * 2^t / (n * s)

   - track the minimum current_value over all t.

Once the minimal current_value is found, we need to represent this as a fraction a/b in reduced form.

Wait, but current_value is (t * 2^t) / (n * s), where s=2^t //n. Let's see:

s = floor(2^t /n). So 2^t = s *n + r, where r is between 0 and n-1.

But then current_value = t * 2^t / (n*s) = t*(s*n + r)/(n*s) = t*(1 + r/(n s)).

But that might not help much. However, to compute the fraction exactly, we can represent each term as numerator and denominator.

But for large t, 2^t can be very big, but since n is up to 1e4 and t up to 40, 2^t can be up to 1e12, which is manageable as Python integers.

So the code will need to compute for each t, the numerator and denominator of the current_value as a fraction, then find the minimal value among all t.

But comparing fractions can be done by cross-multiplying to avoid floating point inaccuracies.

But for the code, perhaps we can precompute for each t the value (t * 2^t) as numerator and denominator (n * s) and track the minimal fraction.

Wait, for a given t, the fraction is (t * 2^t) / (n * s), where s = (2^t) // n.

So for each t, compute numerator = t * (2 ** t), denominator = n * s.

We need to find the minimal fraction among all possible t's. Once the minimal is found, reduce the fraction and output as a/b.

So the code steps:

1. Read n.

2. If n ==1, output 0/1 (since you don't need any tosses). Wait, but according to the problem statement, n can be 1. What's the expected value when there's only one knight? The answer is 0, because you don't need any tosses. So the output is 0/1.

3. Else:

   a. Compute t_min = ceil(log2(n)).

   b. Iterate t from t_min to t_max (like t_min + 30 steps, or until we find that adding higher t's doesn't yield better fractions).

   c. For each t:

      i. Compute pow2_t = 2 ** t.

      ii. s = pow2_t // n.

      iii. If s ==0: skip (since 2^t <n, but t >= t_min implies 2^t >=n, so this can't happen).

      iv. numerator = t * pow2_t.

      v. denominator = n * s.

      vi. Compute the fraction numerator/denominator. Compare to the current minimum.

   d. Find the minimal fraction among all possible t's.

4. Reduce the minimal fraction to its simplest form (divide numerator and denominator by GCD).

5. Output as "a/b".

But how to choose t_max? For example, when n is 1e4, log2(n) is about 13.28, so t_min is 14. Then for t up to, say, 40, but how to find the t that gives the minimal value. Let's see for some n.

Take n=3:

t=2: 4, s=1. 2*4=8. denominator 3*1=3. 8/3 ≈2.666.

t=3: 8//3=2. numerator=3*8=24. denominator 3*2=6. 24/6=4. So larger.

So no need to check beyond t=2 here.

Another example: n=5.

t=3: 8//5=1. numerator=3*8=24. denominator 5*1=5. 24/5=4.8.

t=4:16//5=3. 4*16=64. denominator 5*3=15. 64/15≈4.266.

t=5:32//5=6. 5*32=160. denominator 5*6=30. 160/30=5.333. Worse.

t=6:64//5=12. 6*64=384. denominator 5*12=60. 384/60=6.4. Worse.

So t=4 is the best.

Another example: n=6.

t_min is 3 (since 2^3=8 >=6).

t=3:8//6=1. numerator 3*8=24. denominator 6*1=6. 24/6=4. So 4.

t=4:16//6=2. 4*16=64. denominator 6*2=12. 64/12=5.333. Worse.

t=5:32//6=5. 5*32=160. denominator 6*5=30. 160/30=5.333. Worse.

So the best is t=3, E=4.

Which makes sense. Because with t=3, 8 possibilities. 6 knights get 1 each, 2 rejected. Probability of success is 6/8=3/4. Expected trials is 8/(6*1)=8/6=4/3. Expected flips is 3 * 4/3=4.

So the code needs to iterate t from t_min up to some upper limit, compute the fraction for each t, and pick the minimal one.

But how to choose the upper limit for t. Because for some n, the minimal t could be larger than t_min. For example, let's take n=7.

t_min is 3 (2^3=8 >=7).

t=3: 8//7=1. numerator 3*8=24. denominator 7*1=7. 24/7 ≈3.428.

t=4:16//7=2. numerator 4*16=64. denominator 7*2=14. 64/14=32/7≈4.571. Worse.

t=5:32//7=4. 5*32=160. denominator 7*4=28. 160/28=40/7≈5.714. Worse.

So the best is t=3. So in this case, the minimal t is t_min.

Another example where higher t is better: n=5 (as discussed earlier).

So how to find up to which t we need to check?

An alternative approach is to iterate t until the current_value starts increasing again. Because for some n, after a certain t, the current_value increases, and higher t's would not yield better values.

But how to model this.

Alternatively, for each n, iterate t from t_min to t_min + 40. Because even if the minimal is found later, adding 40 steps would be manageable. 40 steps would take us to t_min + 40. For n up to 1e4, 2^40 is way larger than needed. But for code, even 40 steps is manageable.

So code steps:

For each t in the range t_min to t_min + 40:

   compute the current_value (t * 2^t) / (n * (2^t //n)).

Track the minimal current_value.

But 40 steps for each n up to 1e4 is acceptable.

So the code can proceed as follows.

Now, the code needs to handle n=1 as a special case, since 0 flips are needed.

For n >=2:

Compute t_min as the smallest integer such that 2^t_min >=n. Which can be computed as t_min = ceil(log2(n)).

In Python, since log2 is available in the math module. But for exact powers of 2, log2(n) will be integer, so ceil(log2(n)) is the same as log2(n). For example, n=4: log2(4)=2.0. So t_min=2.

Now, for each t in the range t_min to t_min + 100 (we can choose a large enough upper limit, like 100 steps):

   compute pow2_t = 1 << t.

   s = pow2_t // n.

   if s ==0: continue (but since t >= t_min, 2^t >=n, so s is at least 1).

   numerator = t * pow2_t.

   denominator = n * s.

   current fraction is numerator/denominator.

   compare this to the current minimum fraction, and keep track of the minimum.

Once all t's are considered, the minimal fraction is found.

Then, reduce this fraction by dividing numerator and denominator by their GCD.

Now, for example, when n=3, the minimal is t=2, numerator 8, denominator 3. GCD(8,3) is 1. So output 8/3.

For n=4, t=2: numerator 8, denominator 4*2=8. 8/8=1, which is 1/1. So output 1/1.

Wait wait. For n=4, t=2. 2^2=4. s=4//4=1. So denominator is 4*1=4. numerator=2*4=8. 8/4=2. So the fraction is 2/1. Which matches the sample. So why in the previous example, the code says denominator 8?

Wait, no. Let's recalculate:

For n=4 and t=2:

pow2_t =4.

s=4//4=1.

denominator =4 *1=4.

numerator=2*4=8.

So the fraction is 8/4=2/1. Which is correct.

So the code works.

Another example: n=5.

The code would compute for t=3,4,5, etc.

For t=4:

pow2_t=16.

s=16//5=3.

denominator=5*3=15.

numerator=4*16=64.

64/15 is 4.266..., which is the minimal.

So the code finds this.

Now, the code needs to generate all possible t's starting from t_min up to some t_max. The question is: what is the maximum t that could possibly be the minimal? For example, for n=5, t=4 is better than t=3.

But how to find the upper bound for t. Let's think of when adding more bits (increasing t) can lead to a better (smaller) E(n).

For each t, the value is (t * 2^t) / (n * s), where s = 2^t //n.

As t increases, 2^t increases exponentially, but s also increases. Let's see:

s = 2^t //n.

The ratio (2^t)/(s) can be written as (s *n + r)/s =n + r/s, where r is 2^t mod n.

So (t * 2^t) / (n *s) = t*(n + r/s)/n = t*(1 + r/(n s)).

As t increases, s increases exponentially (since 2^t is exponential), so r/s tends to zero. So the value approaches t*1. So the ratio approaches t. But since t increases, the value would eventually increase again. So there's a minimal point where the value is the smallest, after which increasing t would cause the value to first decrease and then increase.

But for example, when t increases by 1, 2^t doubles. So for s=2^t //n, if 2^t is a multiple of n, then s=2^t /n, and the next step s would be 2^(t+1)/n, which is 2*s. So for such t, the ratio (t+1)*2^(t+1)/(n * 2*s) = (t+1)*2/(n s) * (2^t) / (2^t) ... wait, perhaps not.

Alternatively, for a t where 2^t is a multiple of n, then s=2^t /n. Then the ratio is (t * 2^t) / (n * (2^t /n )) ) = t * 2^t * n / (n * 2^t ) ) = t. So E(n) is t. For example, when n is a power of two, like n=4, t=2. So E(n)=2. Which is correct.

But if n is not a power of two, and for some t, 2^t is a multiple of n, then E(n)=t, which is better than any other t's. Because for any higher t, the ratio would be t (since s=2^t /n, which is 2^{t-k} if n=2^k *m where m is odd, for example. Not sure. But if 2^t is a multiple of n, then E(n) is t, which is the minimal possible (since for any higher t, the value is t, which is larger than the current t). So the minimal possible E(n) for such n is the minimal t where 2^t is a multiple of n.

But for example, if n is 3, then there's no t where 2^t is a multiple of 3, since 2 and 3 are coprime. So the minimal E(n) must be found among the t's where 2^t is not a multiple of n.

But how can we check whether 2^t is a multiple of n for some t. For that, n must be a power of 2 multiplied by some other factors. For example, if n is even but not a power of two, then 2^t can be a multiple of n.

Wait, no. For example, n=6. 6 is 2 *3. 2^t must be a multiple of 6. But 2^t is 2^t, which is 2 multiplied t times. So 2^t is divisible by 6 only if t >=1 and 3 divides 2^t. But 2 and 3 are coprime. So 3 divides 2^t only if t=0, which is impossible. So 2^t is never divisible by 6. Hence, for n=6, there is no t where 2^t is a multiple of n. So the minimal E(n) is 4, as computed earlier.

Thus, for n where n is not a power of two and has odd prime factors, 2^t can't be a multiple of n. Hence, in such cases, the minimal E(n) is achieved at a certain t, which could be larger than t_min.

But how to find it. Since we can't iterate t up to infinity, we need a practical upper bound.

The code can iterate t from t_min to t_min + 40. The number 40 is arbitrary but chosen to cover cases where higher t's may lead to better ratios. Let's see for n=5.

t=4: value is 4*16/(5*3) =64/15 ≈4.266.

t=5:5*32/(5*6)=32/6≈5.333.

t=6:6*64/(5*12)=64/10=6.4.

So after t=4, the values start increasing, so after 4 steps, no better values. So in the code, checking up to t_min + 40 would be sufficient.

Thus, the code can proceed as follows:

For each t in the range t_min to t_min + 100 (a safe upper limit), compute the ratio, and keep track of the minimal.

Now, in code:

We need to compute t_min as the smallest integer where 2^t >=n. So t_min = ceil(log2(n)).

In Python, math.log2(n) returns the log base 2. So for example, log2(3) is ~1.58496. So ceil gives 2.

But to compute t_min correctly, we can use the formula:

t_min = n.bit_length()

Because for example, for n=3 (binary 11), bit_length is 2. For n=4 (100), bit_length is 3, but log2(4) is 2. So perhaps this approach is incorrect.

Wait, no. Let's see:

n=1 → binary 1 → bit_length is 1 → log2(1)=0. So ceil(log2(1))=0. But t_min should be 0, but according to the code, for n=1, we have to return 0/1.

But in the code, for n=1, the code handles it as a special case. For n >=2, we compute t_min as the smallest t where 2^t >=n.

But how to compute t_min.

Another way: t_min is the ceiling of log2(n). So for n not a power of two, t_min = floor(log2(n)) +1. For example, n=3: log2(3)=1.58..., floor is 1, +1=2.

For n=4 (exact power of two), log2(4)=2.0, so t_min=2.

In Python, we can compute t_min as:

t_min = (n-1).bit_length()

Because for example, n=3 (binary 11): (n-1) is 2 (binary 10), bit_length is 2. So t_min=2.

n=4: (4-1)=3 (binary 11), bit_length is 2. So t_min=2.

This works because (n-1).bit_length() gives the number of bits required to represent n-1 in binary, which is the same as the position of the highest set bit. For numbers that are powers of two, (n-1) is all ones in the lower bits. So for n=4, (n-1)=3 (binary 11), which has a bit_length of 2. So t_min=2.

So the code can compute t_min as (n-1).bit_length().

Now, the code steps:

Read n.

If n == 1:

   print("0/1")

Else:

   t_min = (n-1).bit_length()

   min_num = None

   min_den = None

   for t in range(t_min, t_min + 100):

       pow2_t = 1 << t  # equivalent to 2^t

       s = pow2_t // n

       if s ==0:

           continue  # but since t >= t_min, this won't happen

       numerator = t * pow2_t

       denominator = n * s

       # compare this fraction to the current minimum

       if min_num is None or numerator * min_den < min_num * denominator:

           min_num = numerator

           min_den = denominator

   # after checking all t's up to t_min+100, compute GCD and output

   gcd = math.gcd(min_num, min_den)

   a = min_num // gcd

   b = min_den // gcd

   print(f"{a}/{b}")

But wait, how do we know that iterating up to t_min + 100 is sufficient? For example, could there be a case where the minimal value is found at t_min + 50?

Well, given that 2^t grows exponentially, after a certain t, the value (t * 2^t)/(n * s) will start increasing. For example, let's take n=5. The minimal t is 4. For t=4, s=3 (16//5=3). For t=5, s=6 (32//5=6). The denominator for t=5 is 5*6=30. numerator is 5*32=160. So 160/30=5.333, which is worse than t=4's 64/15=4.266.

Similarly, for t=6, 64//5=12 → denominator 60. numerator=6*64=384 → 384/60=6.4.

So the value increases. So after the minimal t, the value starts to increase. So the code only needs to find the minimal t in the range t_min to some t_max where the value starts increasing again.

But how to find t_max. For the code, using t_min + 100 is safe, as even for large t's, the code would compute the values and the minimal would be found.

But in practice, for any n up to 1e4, the minimal t is within t_min + 20 steps. For example, for n=1e4, log2(1e4) is about 13.2877, so t_min is 14. Adding 100 steps would take us to t=114. But 2^114 is a very large number, but in Python, it's manageable as an integer.

But calculating 2^t for t=100 is possible, but for t=100, 2^t is a 30-digit number. However, for the code, even if we compute t=100, it's manageable.

Thus, the code can safely iterate t up to t_min + 100.

Now, let's test the code with the sample inputs.

Sample Input 2:

2

Sample Output: 1/1

For n=2, t_min is 1 (since (2-1).bit_length() is 1). So iterate t=1 to 1+100=101.

For t=1:

pow2_t=2.

s=2//2=1.

numerator=1*2=2.

denominator=2*1=2. 2/2=1. So the minimal is 1/1.

Other t's: for t=2, pow2_t=4. s=4//2=2. numerator=2*4=8. denominator=2*2=4. 8/4=2. Worse. So the code returns 1/1.

Sample Input 3:

3

Sample Output 8/3.

t_min is (3-1).bit_length()=2 (since 2 is 10 in binary, bit_length is 2).

t=2:

pow2=4. s=1. numerator=2*4=8. denominator=3*1=3. ratio 8/3 ≈2.666.

t=3:

pow2=8. s=2. numerator=3*8=24. denominator=3*2=6. 24/6=4. Worse.

Thus, minimal is 8/3.

Sample Input 4:

4.

t_min is (4-1).bit_length()=2 (3 is 11 in binary, bit_length is 2). So t starts at 2.

t=2: pow2=4. s=1. numerator=2*4=8. denominator=4*1=4. 8/4=2. So the output is 2/1.

Which matches the sample.

Thus, the code works for the samples.

Now, code needs to handle n=1 as a special case.

Thus, the code should read n, and if n is 1, output 0/1.

Else, proceed as above.

Now, let's code this in Python.

But we have to be careful with the loop. For each t in range(t_min, t_min + 100), which in Python is inclusive of t_min and up to t_min + 99. So 100 steps.

But perhaps in practice, we need to check even higher t's. But given the examples, this should suffice.

Thus, the code can be written as:

import math

n = int(input())
if n == 1:
    print("0/1")
else:
    t_min = (n-1).bit_length()
    min_num = None
    min_den = None
    for t in range(t_min, t_min + 100):
        pow2_t = 1 << t
        s = pow2_t // n
        if s == 0:
            continue  # impossible since t >= t_min
        numerator = t * pow2_t
        denominator = n * s
        if min_num is None:
            min_num = numerator
            min_den = denominator
        else:
            # Compare fractions numerator/denominator and min_num/min_den
            # a/b < c/d iff a*d < c*b
            if numerator * min_den < min_num * denominator:
                min_num = numerator
                min_den = denominator
    # Reduce the fraction
    g = math.gcd(min_num, min_den)
    a = min_num // g
    b = min_den // g
    print(f"{a}/{b}")

Testing this code with the sample inputs:

Sample 1:

Input 2:

n=2.

t_min = (2-1).bit_length() = 1.

Loop t from 1 to 100:

t=1: pow2=2. s=1. numerator=2. denominator=2. 2/2=1. So min_num=2, min_den=2.

t=2: pow2=4. s=2. numerator=2*4=8. denominator=2*2=4. 8/4=2. So 8/4 is 2, which is worse. So the minimal is 1/1.

After loop, reduce 2/2 → 1/1.

Sample 2: n=3.

t_min is 2.

t=2: 4//3=1. numerator=2*4=8. denominator=3*1=3. 8/3.

t=3:8//3=2. numerator 3*8=24. denominator 3*2=6. 24/6=4. Worse.

Thus, minimal is 8/3.

Sample 3: n=4. Output is 2/1.

Thus, the code works.

Another test case: n=5.

The code should find t=4 as the minimal.

In the loop, t ranges from 3 (t_min is (5-1).bit_length()=3, since 4 is 100 in binary, bit_length is 3) to 103.

t=3: 8//5=1. numerator=3*8=24. denominator=5*1=5. 24/5=4.8.

t=4:16//5=3. numerator=4*16=64. denominator=5*3=15. 64/15 ≈4.266.

t=5:32//5=6. numerator=5*32=160. denominator=5*6=30. 160/30=5.333.

Thus, the minimal is 64/15. Which reduces to 64/15 (GCD is 1). So output is 64/15.

Thus, the code is correct.

Thus, the code should work for all cases.
</think>

```python
import math

n = int(input())
if n == 1:
    print("0/1")
else:
    t_min = (n - 1).bit_length()
    min_num = None
    min_den = None
    for t in range(t_min, t_min + 100):
        pow2_t = 1 << t
        s = pow2_t // n
        if s == 0:
            continue
        numerator = t * pow2_t
        denominator = n * s
        if min_num is None:
            min_num, min_den = numerator, denominator
        else:
            if numerator * min_den < min_num * denominator:
                min_num, min_den = numerator, denominator
    g = math.gcd(min_num, min_den)
    a = min_num // g
    b = min_den // g
    print(f"{a}/{b}")
```