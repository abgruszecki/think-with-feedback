<think>
Okay, let's try to solve this problem. So, the problem is about counting the number of configurations of magic gems that result in exactly N units of space. Each magic gem can be either kept as is (taking 1 unit) or split into M normal gems (taking M units). The order matters here because different indices being split count as different configurations. Hmm.

Let me think. So, for each configuration, let's say there are k magic gems that are split. Then, the total space contributed by split gems is k*M. The remaining (unused) magic gems contribute (total_magic - k)*1. Wait, wait. Wait, no. Wait, the problem says that Reziba chooses a set of magic gems and splits some of them. So each magic gem in the set can be either split or not. Wait, the problem statement says: the set includes magic gems, some of which are split. So the total space is the sum for each gem in the set: if split, it contributes M units, else contributes 1 unit.

Wait, no. Wait, the configuration is a set of magic gems. Each gem in this set is either split or not. So for each gem in the set, if split, it's M units. Otherwise, 1. So the total space is the sum over all selected gems: for each, add M if split, 1 otherwise.

So the problem reduces to finding the number of subsets of magic gems (since each gem is either included or not) where the sum of each gem's contribution (either 1 or M) equals exactly N. But wait, no. Wait, the problem allows choosing a set of magic gems, which could be any number. Then, for each gem in that set, you can choose to split it or not. So the total is sum (for each gem in the set) (M if split, 1 otherwise). And that sum must equal N.

But how can we model this? Let's see. Let's denote that for each possible split scenario, the sum is N. But how to count all possible such scenarios.

Alternatively, think of it as choosing a certain number of split gems and a certain number of non-split gems. Let's say that there are x split gems and y non-split gems. Then the total space is x*M + y*1 = N. Also, since each split gem and non-split gem are part of the set, the total number of gems in the set is x + y. But each split gem is part of the set, and each non-split gem is part of the set. So the total contribution is x*M + (y) *1 = N. But since y can be anything, but the sum must equal N.

Wait, but the problem states that Reziba chooses a set of magic gems, then splits some of them. So the set of magic gems selected must be such that when some are split (x of them), and the rest (y) are not split, then x*M + y = N. And x and y are non-negative integers such that x + y is the number of gems selected.

But the number of ways to choose the set and the split gems would be the sum over all possible x and y where x*M + y = N, and the number of ways to select x split and y non-split gems. Wait, but the problem allows any number of gems selected, as long as their split and non-split count sums to N.

Wait, but how can that be? Let's take x split gems and y non-split. Then, x*M + y = N. But also, the number of gems selected is x + y. However, since each split gem contributes M units, and each non-split contributes 1. So, the sum x*M + y must equal N.

But for a given x and y that satisfy x*M + y = N, how do we count the number of configurations?

Wait, the configurations are sequences where the indices of the split and non-split gems matter. So, for example, if there are x split gems and y non-split gems, then the total number of configurations is C(x + y, x) multiplied by 2^(x + y choose which ones are split?), wait no. Wait, no. Wait, the set of gems selected must consist of x split gems and y non-split gems. So the total number of gems selected is x + y, and among them, x are split. So the number of ways to choose which x are split is C(x + y, x). However, the gems can be selected in any order, but the problem says that the indices of the gems split matter. Wait, the problem says two configurations are different if the indices of the split gems differ.

Wait, the problem says: "Two configurations are considered different if the number of magic gems Reziba takes to form them differs, or the indices of gems Reziba has to split differ." So, for example, if you select two split gems and one non-split, that's a configuration. But if in another configuration, you select the same three gems but split different ones, that's a different configuration. So the order of selection doesn't matter as long as the same set of split and non-split gems are chosen. Wait, no. Wait, the indices matter. So the problem is considering that each magic gem is unique. So even if two different gems are selected as split in different configurations, those count as different.

So, the approach is to model this as follows: for each possible x (number of split gems) and y (number of non-split gems) such that x*M + y = N, the number of configurations is the product of (number of ways to choose x + y distinct magic gems) multiplied by (number of ways to choose which x of them are split). However, the problem states that the gems are selected, and the split ones are chosen among them. Wait, but the problem says that Reziba chooses a set of magic gems and splits some of them. So the set can be any subset (size k) of magic gems. Then, for each subset of size k, the number of ways is the sum over all possible x (number of split in the subset) such that x*M + (k - x) = N. For each such x, the count is C(k, x) multiplied by 1 (for choosing that subset and split x of them). But since the problem allows any number of subsets (any k), we need to sum over all possible k, and for each possible x in that k, such that x*M + (k - x) = N. Because in this model, y = (k - x), so substituting into x*M + y = N gives x*M + (k - x) = N → x(M - 1) + k = N → k = N - x(M - 1). But k must be at least x (since x is the number of split in the subset), but x can't be negative. Wait, perhaps we can model this as follows.

Let me reorganize the equation. Let's denote that for a split count x, the required total size of the subset (k) is k = N - x*(M-1). Because:

x*M + (k - x)*1 = N → x*M + k - x = N → x(M-1) + k = N → k = N - x(M-1).

So for each x, possible if k is non-negative and x >=0, and k >= x (since the subset size is x + (k - x) = k, but x can't be larger than k). Wait, no. Because k is the subset size, and x is the number of split gems in the subset, which must be ≤ k. So x ≤ k.

But k is equal to N -x*(M-1). So substituting, x ≤ N -x*(M-1) → x +x(M-1) ≤ N → x*M ≤ N → x ≤ N/M. So x can be from 0 up to floor(N/(M)).

Wait, but N can be up to 1e18, so we need a way to compute this efficiently.

So for each x in possible values, compute k = N -x*(M-1). If k is non-negative and x <= k (since x is the number of split gems, which can't exceed the subset size), then the number of configurations for this x is C(k, x), since in a subset of k gems, we choose x to split.

But how do we sum this over all possible x?

So the total answer is sum_{x=0 to max_x} [ C(k, x) ] where k = N - x*(M-1), and k >= x, and k >=0.

But how do we compute this sum efficiently, given that N is up to 1e18?

We need to find all x where k is a non-negative integer and k >= x. Let's see:

Conditions for x:

1. k = N -x*(M-1) >=0 → x*(M-1) ≤ N → x ≤ N/(M-1). Since M >=2, M-1 >=1. So x_max for this condition is floor(N/(M-1)).

But also, since k >=x → N -x*(M-1) >=x → N >= x*(M-1 +1) → N >=x*M → x <= floor(N/M).

So the valid x's are those x that satisfy x <= min( floor(N/(M-1)), floor(N/M) )).

Wait, let me recheck:

From k >=x → x <= k → x <= (N - x*(M-1)) → x +x(M-1) <= N → x*M <= N → x <= N/M.

So x must be <= N/M. Since M is at least 2, this gives x_max as floor(N/M).

But also, k must be >=0. So x*(M-1) <= N → x <= N/(M-1). Since M >=2, M-1 is >=1, so N/(M-1) could be larger than N/M. For example, M=2: M-1=1 → N/(M-1) = N. So x can be up to N, but the second condition (x <= N/M) would restrict x to up to floor(N/2) for M=2.

So the upper bound for x is the minimum of floor(N/(M-1)) and floor(N/M). But wait, N/(M-1) could be larger than N/M. For example, M=3: M-1=2. N/(M-1) = N/2, N/M= N/3. So for M >=2, M-1 >=1, but N/(M-1) is larger than N/M only when M-1 < M → which is always true. Wait, M-1 is always less than M. So N/(M-1) is larger than N/M. So the upper bound for x is min( floor(N/(M-1)), floor(N/M) ) → but floor(N/M) is smaller. Wait, no:

Wait, N/(M-1) is larger than N/M since M-1 < M. So for example, M=2: M-1=1 → N/1 = N, M=2 → N/2. So N/(M-1) is N, and N/M is N/2. So the upper bound x must be <= N/M (floor), but N/M is smaller than N/(M-1). So the upper bound is x_max = floor(N/M).

But wait, in this case, x_max is the maximum x such that x <= floor(N/M), and x*(M-1) <=N → which is already satisfied since x <= N/M → x*(M-1) <= N/M * (M-1). For example, M=2: x*(M-1) =x*1. Since x <= N/2, x*1 <= N/2 < N → but if N is even, x_max = N/2. So x*(M-1) = N/2*1 = N/2 <= N. So yes.

So the valid x must satisfy x >=0, x <= floor(N/M), and N - x*(M-1) >=0. Wait, but since x <= N/M, then x*(M-1) <= (N/M)*(M-1) = N*(M-1)/M. Since M>=2, (M-1)/M <1. So x*(M-1) < N → N -x*(M-1) >0 → k = N -x*(M-1) >=0. So if x <= floor(N/M), then k = N -x*(M-1) is positive. So the only conditions are x >=0 and x <= floor(N/M). Because for x in this range, k is non-negative and >=x.

Wait, let's see:

k = N -x(M-1).

But x <= N/M → x*M <=N → x*M -x <= N -x → x(M-1) <= N -x → x(M-1) +x <=N → x*M <=N → which is true. But how does that relate to k >=x?

k = N -x(M-1) → k = N -x(M-1).

We need k >=x → N -x(M-1) >=x → N >=x(M) → x <= N/M → which is our x condition. So yes, if x is <= N/M, then k >=x.

So the valid x's are integers x >=0, x <= floor(N/M). So the sum is over x from 0 to x_max = floor(N/M), where for each x, we compute the combination C(k, x), where k = N -x*(M-1).

But wait, how does k relate to x? For each x, k is N - x*(M-1), which is >=x because x <= N/M.

So for each x in 0 <=x <= x_max, the number of configurations is C(k, x), where k = N -x*(M-1).

So the answer is sum_{x=0}^{x_max} C(k, x).

But the problem now is that for N up to 1e18, x_max could be up to 1e18 / 2, which is 5e17. So iterating from x=0 to x_max is impossible. Therefore, there must be a mathematical pattern or formula that allows us to compute this sum efficiently.

Hmm. Let's think about the sum S = sum_{x=0}^t C(n - x*(M-1), x) where t = floor(N/M). Wait, no. Wait, for each x, k = N -x*(M-1), which is n (the original problem's N) minus x*(M-1). So the sum is sum_{x=0}^t C(k, x) where k = N -x*(M-1) and t = floor(N/M).

But how can this sum be computed efficiently?

Wait, perhaps there's a way to model this as a recurrence relation, and then compute it using matrix exponentiation or some other method.

Alternatively, perhaps the sum can be expressed as a Fibonacci-like sequence. Let me see for small examples.

Take the first example input: N=4, M=2.

Then x_max is floor(4/2) =2. So x can be 0,1,2.

For x=0: k=4 -0*(1) =4. C(4,0)=1.

x=1: k=4 -1*1=3. C(3,1)=3.

x=2: k=4-2*1=2. C(2,2)=1.

Sum is 1+3+1=5 → which matches the first sample.

In the second sample, N=3, M=2 → x_max=1 (floor(3/2)=1).

x=0: k=3 → C(3,0)=1.

x=1: k=3-1=2 → C(2,1)=2.

Sum 1+2=3 → matches the sample.

So the sum works here.

But how to compute this for large N and M up to 100.

Hmm. Let's consider the general sum S = sum_{x=0}^t C(k_x, x), where k_x = N -x*(M-1), t = floor(N/M).

We need to find a way to compute S efficiently.

Let me think about possible recurrence relations.

Suppose we model S(N) as the sum up to x_max for N. Let's see what S(N) would look like.

For example, when M=2:

k_x = N -x*(2-1) = N -x.

So, the sum is sum_{x=0}^t C(N -x, x), where t = floor(N/2). 

Wait, for M=2, the problem reduces to summing C(N-x, x) for x from 0 to N//2. This is known to be the (N+1)th Fibonacci number. Wait, for example, for N=4: sum is C(4,0) + C(3,1) + C(2,2) =1+3+1=5 → which is Fib(5) (if Fib(0)=0, Fib(1)=1, Fib(2)=1, Fib(3)=2, Fib(4)=3, Fib(5)=5). So 5 is Fib(5).

For N=3: sum is C(3,0)+C(2,1)=1+2=3 → which is Fib(4)=3.

For N=2: x can be 0 and 1. C(2,0) + C(1,1) =1+1=2 → Fib(3)=2.

So for M=2, the sum is Fib(N+1). So the answer is the (N+1)th Fibonacci number modulo 1e9+7.

That's an interesting pattern. So when M=2, the sum is the (N+1)th Fibonacci number. So for M=2, the solution can be computed with a Fibonacci recurrence, and matrix exponentiation can be used to compute it in O(log N) time.

But what about other values of M?

For example, let's take M=3. Then k_x = N -x*2, and x can be up to floor(N/3).

So the sum is sum_{x=0}^t C(N-2x, x).

Is there a pattern here that can be modeled with a linear recurrence relation?

Let's see for some small values.

Take N=4, M=3. x can be 0,1 (since 4/3=1.333 → floor is 1).

x=0: C(4,0)=1.

x=1: C(4-2*1,1) = C(2,1)=2.

Sum 1+2=3.

What's the pattern here? Let's see for M=3.

For N=1: x can be 0. C(1,0)=1 → sum 1.

N=2: x can be 0 (since 2/3=0). So sum C(2,0)=1.

N=3: x_max=1. x=0: C(3,0)=1. x=1: C(3-2*1,1)=C(1,1)=1. Sum 2.

N=4: sum 3 as above.

N=5: x_max=1 (5/3=1.666). x=0: C(5,0)=1. x=1: C(5-2*1,1)=C(3,1)=3. Sum 4.

N=6: x_max=2. x=0: C(6,0)=1. x=1: C(4,1)=4. x=2: C(2,2)=1. Sum 1+4+1=6.

Hmm. Let's see if these numbers fit a recurrence. Let's list the sums S(N) for M=3:

N | S(N)
0 | C(0,0)=1 (but N starts from 1)
1 | 1
2 | 1
3 | 2
4 | 3
5 | 4
6 | 6
Wait, perhaps S(N) for M=3 follows a recurrence like S(N) = S(N-1) + S(N-3).

Let's check:

For N=3: S(3) = 2. S(2) =1, S(0) (assuming 1) → 1+1=2. Yes.

N=4: 3. S(3) + S(1) → 2 +1=3. Yes.

N=5: 4. S(4)+S(2) →3 +1=4. Yes.

N=6:6. S(5)+S(3)=4 +2=6. Yes.

So it seems that for M=3, the sum S(N) follows S(N) = S(N-1) + S(N-3).

Similarly, perhaps for general M, the sum S(N) follows a linear recurrence where each term is the sum of previous terms based on the step (M-1).

So for M=2, the recurrence is S(N) = S(N-1) + S(N-2) → Fibonacci.

For M=3, it's S(N) = S(N-1) + S(N-3).

For M=4, perhaps S(N) = S(N-1) + S(N-4) ?

Wait, let's test for M=4.

Take N=4, M=4. x can be up to 1 (4/4=1).

x=0: C(4,0)=1. x=1: C(4-3*1,1)=C(1,1)=1. Sum 2.

If the recurrence is S(N) = S(N-1) + S(N-4), then for N=4:

S(4) = S(3) + S(0). Suppose S(0) is 1. What is S(3) for M=4? For N=3, M=4: x can be 0. So sum is 1. So 1+1=2. Which matches. So yes.

Another example: N=5, M=4. x_max is 1 (5//4=1).

x=0: C(5,0)=1. x=1: C(5-3*1,1) = C(2,1)=2. Sum 3.

According to the recurrence: S(5) = S(4) + S(1). S(4) is 2 (from earlier), S(1) is 1. Sum 3. Correct.

So yes, for M=4, the recurrence S(N) = S(N-1) + S(N-M) where M is 4. So S(N) = S(N-1) + S(N-4).

So the general pattern is that for each M, the sum S(N) follows the recurrence S(N) = S(N-1) + S(N-M), with base cases determined by the possible values.

Thus, the problem reduces to computing the (N+1)th term in a linear recurrence relation of order M, where the recurrence is S(n) = S(n-1) + S(n-M).

Wait, but why N+1? Let's see for M=2.

For M=2, the sum for N=4 is 5, which is the 5th Fibonacci number. And indeed, the recurrence S(n) = S(n-1) + S(n-2) with S(0)=1, S(1)=1, S(2)=2, etc. So for N=4, S(4) is 5, which is Fib(5).

So for general M, the sum S(N) is the (N+1)th term in the sequence defined by the recurrence S(n) = S(n-1) + S(n-M) for n >= M, and S(0) = 1, S(1) = 1, ..., S(M-1) = 1 + ... ?

Wait, let's think about the base cases. For M=3, the recurrence is S(n) = S(n-1) + S(n-3) for n >=3. What are the base cases?

For M=3:

S(0) =1 (x=0: C(0,0)=1? But when N=0, but the problem states N>=1. But perhaps for the recurrence, S(0) =1, S(1)=1, S(2)=1, and S(3) = S(2) + S(0) → 1 +1=2. Which aligns with the previous example.

So the base cases for M is that for n <0, S(n)=0, and for n >=0 and n <M, S(n) =1.

Wait, no. For example, when M=3, S(0)=1, S(1)=1, S(2)=1. Then S(3) = S(2) + S(0) =1 +1=2. S(4)= S(3)+S(1)=2+1=3. S(5)= S(4) + S(2)=3+1=4. S(6)= S(5)+S(3)=4+2=6. Which matches the earlier example.

So the base case is S(0) =1, and for 0 <n <M, S(n)=1.

Wait, but how about for M=2. For S(0)=1, S(1)=1. Then S(2) = S(1) + S(0) =2. Which is correct (for N=1, sum is 1. For N=2, sum is 1 +1=2).

So the base cases are:

S(0) =1.

For 1<=n <M: S(n) =1 + S(n-1) ?

Wait, for M=3, S(0) =1. S(1) =1 (sum for N=1: x can be 0 → C(1,0) =1). Then S(1) =1. S(2) =1 (sum is C(2,0) =1). Then for n >=M, S(n) = S(n-1) + S(n-M).

But how about for M=4? Let's see:

S(0)=1.

S(1)=1 (sum for N=1: x=0 →1).

S(2)=1 (x=0 →1).

S(3)=1 (x=0 →1).

Then S(4)= S(3) + S(0) →1+1=2. Which matches earlier example.

So the base cases are S(n) =1 for n <M.

But how do we get there?

Wait, for M=3, S(0)=1, S(1)=1, S(2)=1. Then for n >=3, S(n) = S(n-1) + S(n-3).

So the general recurrence is:

For all n >=0:

S(n) = 1 if n < M.

Wait, no. Wait, for n <0, S(n) is 0. For 0 <=n <M: S(n) =1. For n >=M: S(n) = S(n-1) + S(n-M).

But why? Let's see for M=2:

For n=0: S(0) =1.

n=1: S(1) =1.

n >=2: S(n) = S(n-1) + S(n-2).

Which is the Fibonacci sequence, starting with S(0)=1, S(1)=1. So S(2)=1+1=2, which is correct (sum for N=2 is C(2,0) + C(0, 2) → but wait, x can be up to floor(2/2)=1. x=0: C(2,0)=1. x=1: C(2-1*1,1)=C(1,1)=1. Sum 2 → S(2)=2. Which is S(2) = S(1)+S(0) =1+1=2. So correct.

So the recurrence is:

S(n) = 1 for 0<=n < M.

For n >=M, S(n) = S(n-1) + S(n-M).

So the answer to our problem is S(N), where S is defined by this recurrence.

But for M up to 100 and N up to 1e18, how can we compute this efficiently?

The answer is to use matrix exponentiation. Since the recurrence is linear and has a fixed order (M), we can model it as a matrix and compute the nth term in O(M^3 log n) time.

The key steps are:

1. Determine the recurrence relation and the initial terms.

2. Build the transformation matrix for the recurrence.

3. Compute the nth term using matrix exponentiation.

So let's model this.

The recurrence is:

S(n) = S(n-1) + S(n-M), for n >= M.

The initial terms are S(0) =1, S(1)=1, S(2)=1, ..., S(M-1)=1.

For example, for M=3, the initial terms are [1, 1, 1], and for n >=3, S(n) = S(n-1) + S(n-3).

So the state vector for the matrix exponentiation would be the previous M terms. For example, to compute S(n), we need the previous M terms. So the state is [S(n), S(n-1), S(n-2), ..., S(n-M+1)].

The transformation matrix would be an MxM matrix that, when multiplied by the state vector, shifts the state and computes the next term.

For M=3, the state vector is [S(n), S(n-1), S(n-2)]. The next term S(n+1) is S(n) + S(n-2) (since M=3, so S(n+1) = S(n) + S(n+1 -3) = S(n) + S(n-2)).

So the transformation matrix for M=3 would be:

[1 0 1]   * [S(n), S(n-1), S(n-2)]^T = [S(n+1), S(n), S(n-1)]^T.

But let's see:

The new state after one step (from n to n+1) is [S(n+1), S(n), S(n-1)].

S(n+1) = S(n) + S(n-2).

So the first row of the matrix is [1, 0, 1], which when multiplied by [S(n), S(n-1), S(n-2)] gives 1*S(n) + 0*S(n-1) + 1*S(n-2) = S(n) + S(n-2) = S(n+1).

The second row is [1, 0, 0], which picks S(n) as the second element.

The third row is [0,1,0], which picks S(n-1) as the third element.

Wait, perhaps not. Let's model the state as [S(n), S(n-1), S(n-2)] for M=3.

To get the next state [S(n+1), S(n), S(n-1)], we need:

S(n+1) = S(n) + S(n-2).

So the first row of the transformation matrix is [1, 0, 1].

The second row is [1, 0, 0], since the new second element is S(n).

The third row is [0, 1, 0], since the new third element is S(n-1).

So the matrix for M=3 is:

1 0 1

1 0 0

0 1 0

In general, for M:

The transformation matrix T is an MxM matrix where:

- The first row has 1 in the first column and 1 in the M-th column (since S(n+1) = S(n) + S(n+1 - M) = S(n) + S(n+1 -M) → since n+1 -M is the term M steps back. Wait, for general M, S(n) = S(n-1) + S(n-M).

So S(n+1) = S(n) + S(n+1 -M).

But when building the matrix, the state vector contains the previous M terms. Let's say the state vector is [a_0, a_1, ..., a_{M-1}] = [S(n), S(n-1), ..., S(n - M +1)].

To compute S(n+1), we need a_0 (S(n)) + a_{M-1} (S(n - M +1)), but wait, S(n+1 - M) is S(n+1 -M) = S( (n+1) - M ). If the current state is for n, then the previous M terms are S(n), S(n-1), ..., S(n - M+1). So S(n-M +1) is S(n - (M-1)).

But S(n+1) = S(n) + S(n+1 -M) → which is S(n) + S(n+1 -M) = S(n) + S( (n+1) - M ) = S(n) + S( (n-M) +1 ) → but that term is part of the state vector only if (n-M)+1 >= n-M+1 - (M-1) → perhaps not. Hmm.

Wait, when the state is [S(n), S(n-1), ..., S(n-M+1)], then S(n-M) is not part of the state. So how can we compute S(n+1) = S(n) + S(n+1-M), which is S(n) + S(n+1-M), but when n+1-M is less than or equal to n-M+1 (since n+1-M <=n-M+1 is equivalent to 1 <=0, which is not possible). So n+1-M is less than n-M+1 → which is outside the current state.

So perhaps my initial approach is incorrect.

Alternatively, perhaps the state vector should contain the last M elements needed to compute the next term.

Wait, the recurrence is S(n) = S(n-1) + S(n-M).

So, to compute S(n), you need S(n-1) and S(n-M). But S(n-M) is not part of the previous M terms (assuming the state is the last M terms). For example, if M=3 and the state is [S(n-1), S(n-2), S(n-3)], then S(n) = S(n-1) + S(n-3), which is part of the state. So yes, in that case, the state holds the necessary terms.

Wait, let me re-express the recurrence.

The recurrence is:

For n >= M:

S(n) = S(n-1) + S(n-M).

So for example, with M=3:

n=3: S(3)=S(2) + S(0).

n=4: S(4)=S(3) + S(1).

n=5: S(5)=S(4) + S(2).

n=6: S(6)=S(5) + S(3).

So, each step requires S(n-1) and S(n-M). To compute S(n), you need to have the previous term (S(n-1)) and the term M steps back (S(n-M)).

So, the state vector must include all terms from S(n-1) down to S(n-M), so that when you compute the next term, the term S(n-M) is available.

But the state vector for the matrix exponentiation would need to include the last M terms. For example, for M=3, the state vector is [S(n-1), S(n-2), S(n-3)].

Wait, no. Let's think differently.

If the recurrence is S(n) = S(n-1) + S(n-M), then to compute the next term, we need the previous term and the term M steps before that.

But how to model this in a state vector. For example, if M=3, then each new term depends on S(n-1) and S(n-3). So the state must keep track of S(n-1), S(n-2), S(n-3) to allow the next term to compute S(n) = S(n-1) + S(n-3).

So the state vector is of size M. For M=3, the state vector would be [S(n-1), S(n-2), S(n-3)]. Then, the next state would be [S(n), S(n-1), S(n-2)].

To compute S(n), we use the first element (S(n-1)) and the third element (S(n-3)).

So the transformation matrix would need to take the state vector [a, b, c] (representing S(n-1)=a, S(n-2)=b, S(n-3)=c) and compute the new state [S(n) =a + c, a, b].

So the first row of the matrix would be [1, 0, 1] (because a + 0*b +1*c = a + c = S(n)). The second row would be [1, 0, 0] (to pick a as the second element). The third row would be [0, 1, 0] (to pick b as the third element).

So the transformation matrix for M=3 is:

[1 0 1]

[1 0 0]

[0 1 0]

Similarly, for general M, the transformation matrix would have a 1 in the first column of the first row, and a 1 in the M-th column of the first row. The other rows shift the elements down.

So the matrix for general M is:

Row 0: [1, 0, 0, ..., 0, 1] (1 in the first and M-th column)

Rows 1 to M-1: each row i has a 1 in column i-1. For example, row 1 has a 1 in column 0, others 0; row 2 has 1 in column 1, etc.

So the matrix is:

[1 0 ... 0 1]

[1 0 ... 0 0]

[0 1 ... 0 0]

...

[0 0 ... 1 0]

So this matrix, when multiplied by the state vector, gives the next state.

The initial state vector for the matrix exponentiation depends on the base cases. For example, for M=3, the initial terms are S(0)=1, S(1)=1, S(2)=1. So the state vector for n=2 (the maximum initial state) is [S(2), S(1), S(0)] = [1, 1, 1]. Then, to compute S(3), we apply the matrix once.

So the matrix exponentiation approach involves building this transformation matrix and then raising it to the (n - M +1)th power, then multiplying by the initial state vector.

But for the problem, the initial terms are S(0) =1, S(1) =1, ..., S(M-1)=1. So for n < M, S(n) =1.

So to compute S(N), which is our answer, we can proceed as follows:

- If N < M, the answer is 1.

- Otherwise, we need to compute S(N) using the recurrence.

The matrix exponentiation approach would allow us to compute S(N) efficiently.

The steps to implement this are:

1. For N < M: return 1.

2. Else, compute the required exponent (number of steps) as K = N - (M-1).

Wait, since the initial state is for S(M-1), S(M-2), ..., S(0), and to compute S(M), we need one step. For example, for M=3, initial state is [S(2), S(1), S(0)] = [1, 1, 1]. After one matrix multiplication (step), we get the state for S(3) =1+1=2. Then, for each step, the exponent increases by one.

The number of steps needed to reach S(N) is (N - (M-1)).

So, the exponentiation is done on the transformation matrix raised to the power of (N - M +1).

Then, multiply the initial state vector by this matrix, and the first element of the resulting vector is S(N).

So, the code steps are:

- Precompute the initial state vector. For M, the initial state is [S(M-1), S(M-2), ..., S(0)].

Since S(k) =1 for 0 <=k <M, the initial state vector is [1, 1, ..., 1] of length M.

- Build the transformation matrix T as described.

- Compute T raised to the power (N - M + 1).

- Multiply the initial state vector by this matrix to get the new state vector.

- The first element of the resulting vector is S(N).

But wait, matrix exponentiation works with matrix multiplication. The initial state is a vector of length M. How to represent this as a matrix multiplication?

Ah, in matrix exponentiation for linear recurrences, the state is represented as a vector, and the transformation matrix is designed such that each multiplication advances the state by one step.

So the code would model this correctly.

Now, implementing matrix multiplication and exponentiation in Python is feasible, but for M up to 100, and exponents up to 1e18, this needs to be efficient. However, since each matrix multiplication is O(M^3) and the exponent is log2(1e18) ≈ 60 steps, the total time is O(M^3 * log N), which is acceptable for M up to 100.

So the plan is:

- If N < M, output 1.

- Else:

   a. Create the transformation matrix T.

   b. Compute T^k where k = N - M +1.

   c. Multiply the initial state vector by T^k to get the new state.

   d. The first element of the resulting vector is S(N).

   e. Output that modulo 1e9+7.

But how to represent the matrix and perform the multiplication.

Let's proceed to code.

First, we need to handle very large exponents (up to 1e18 - M +1). So the matrix exponentiation must be done via binary exponentiation (exponentiation by squaring).

The code will have functions to multiply two matrices and to raise a matrix to a power.

Additionally, the initial vector is [1, 1, ..., 1], and the transformation matrix T is built as described.

Now, for the matrix multiplication function:

Each matrix is M x M. So for matrices A and B, the product C is such that C[i][j] = sum_{k=0 to M-1} A[i][k] * B[k][j] modulo MOD.

The vector multiplication is a vector multiplied by a matrix. The initial state vector is a row vector. So when we multiply the vector by the matrix, each new element is the dot product of the vector and the corresponding column of the matrix.

Alternatively, the state vector is a column vector, and the transformation matrix is multiplied on the left. The code can handle this either way, but for code simplicity, perhaps model the vector as a list of length M, and the matrix as M lists each of length M.

But in any case, the code must correctly perform the multiplication.

Alternatively, since the initial state is a vector [S(M-1), S(M-2), ..., S(0)], and after applying the matrix once, it becomes [S(M), S(M-1), S(M-2), ..., S(1)].

So, for the code:

def multiply(a, b):

   result = [[0]*len(b[0]) for _ in range(len(a))]

   for i in range(len(a)):

       for k in range(len(b)):

           if a[i][k] ==0:

               continue

           for j in range(len(b[0])):

               result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % MOD

   return result

def matrix_pow(mat, power):

   result = [[0]*len(mat) for _ in range(len(mat))]

   for i in range(len(mat)):

       result[i][i] =1

   while power >0:

       if power %2 ==1:

           result = multiply(result, mat)

       mat = multiply(mat, mat)

       power //=2

   return result

But this is O(M^3) for each multiply, which is acceptable for M=100 and log2(1e18) steps. For 100x100 matrices, each multiply is 1e6 operations, and log2(1e18) is around 60, so 60*1e6*2 (since squaring and multiplying) → about 1e8 operations, which is manageable in Python for 3 seconds.

But perhaps we can optimize the code by using a more efficient way of multiplying matrices, possibly with tuples or other structures. But for the given constraints, it's manageable.

Once the matrix is raised to the required power, we multiply the initial state vector by the matrix. The initial state vector is a row vector [1,1,...,1] of length M.

Wait, but when we multiply the vector by the matrix, it's a row vector multiplied by the matrix. So the code for the vector-matrix multiplication would be:

def vector_mult(vec, mat):

   new_vec = [0]*len(vec)

   for i in range(len(vec)):

       for j in range(len(mat)):

           new_vec[i] = (new_vec[i] + vec[j] * mat[j][i]) % MOD

   return new_vec

Wait, no. Let's see. If the vector is a row vector, then to multiply by the matrix (which is MxM), the result is a row vector where each element is the sum of vec[k] * mat[k][i] for each i.

Alternatively, the matrix is stored such that mat[i][j] represents the coefficient for transitioning from j to i. Then, the multiplication would be:

new_vec[i] = sum over j (vec[j] * mat[j][i]).

So for code, given a row vector vec and matrix mat, the multiplication is:

new_vec = [0] * M

for i in range(M):

   for j in range(M):

       new_vec[i] = (new_vec[i] + vec[j] * mat[j][i]) % MOD

So the code would look like that.

Alternatively, perhaps the matrix is stored as a list of rows, each row is a list of columns. Then, the matrix multiplication code would need to handle this.

But perhaps it's easier to represent the matrix as a list of rows, where each row is a list of columns. Then, the vector is a list of length M, and the multiplication is:

vec = [sum( (vec[j] * mat[j][i]) for j in range(M) ) % MOD for i in range(M) ]

Wait, no. That would be for each element in the new vector, it's the sum over j of vec[j] * mat[j][i], for each i. Which is correct for a row vector multiplied by the matrix.

So the code for multiplying a row vector by the matrix is:

new_vec = [0] * M

for i in range(M):

   for j in range(M):

       new_vec[i] = (new_vec[i] + vec[j] * mat[j][i]) % MOD

But in the case of matrix exponentiation, when the matrix is raised to the power k, and the initial vector is multiplied by the matrix^k, this gives the new vector after k steps.

So, in code:

if N >= M:

    k = N - (M-1)  # because the initial state is for M-1, and each step increases the state by 1.

    # build the transformation matrix

    mat = [[0]*M for _ in range(M)]

    for i in range(M):

        if i ==0:

            mat[i][0] =1

            mat[i][M-1] =1

        else:

            mat[i][i-1] =1

    # compute mat^k

    mat_pow = matrix_pow(mat, k)

    # initial vector is [1,1,...,1]

    initial = [1]*M

    # multiply initial by mat_pow

    result = [0]*M

    for i in range(M):

        for j in range(M):

            result[i] = (result[i] + initial[j] * mat_pow[j][i]) % MOD

    # the first element of the resulting vector is S(M-1 + k) = S(N)

    print(result[0] % MOD)

else:

    print(1 % MOD)

Wait, the initial vector is [S(M-1), S(M-2), ..., S(0)], which is [1,1,...,1], since all S(k) for k < M are 1.

After multiplying by mat^k, the resulting vector is [S(M-1 +k), S(M-2 +k), ..., S(k)].

But k is N - (M-1), so M-1 +k = N.

So the first element of the resulting vector is S(N).

Yes.

So the code would work.

Now, let's test this code with the sample inputs.

Sample Input 1:

4 2 → M=2.

Since N >=M (4 >=2), k =4-1=3.

The initial vector is [1,1] (since M=2, the initial state is [S(1), S(0)]).

The transformation matrix for M=2 is:

row 0: [1, 1]

row 1: [1, 0]

So matrix_pow is mat^3.

Let's compute mat^3.

mat^1 is:

1 1

1 0

mat^2 = mat * mat:

(1*1 + 1*1) (1*1 + 1*0) → (2, 1)

(1*1 + 0*1) (1*1 +0*0) → (1,1)

So mat^2:

2 1

1 1

mat^3 = mat^2 * mat:

row 0: 2*1 +1*1 =3; 2*1 +1*0=2.

row 1: 1*1 +1*1=2; 1*1 +1*0=1.

mat^3:

3 2

2 1

Multiplying the initial vector [1,1] by mat^3:

For each element in the resulting vector:

result[0] =1*3 +1*2=5 → mod 1e9+7 is5.

result[1] =1*2 +1*1=3.

So the resulting vector is [5,3]. The first element is 5, which matches the first sample.

Sample Input 2: 3 2 → M=2, N=3.

k=3-1=2.

mat^2 is:

2 1

1 1.

Initial vector [1,1].

Multiply by mat^2:

result[0] =1*2 +1*1=3.

result[1] =1*1 +1*1=2.

So the first element is3 → matches the second sample.

So the code works for these cases.

Now, the code must be written in Python, handling large exponents with matrix exponentiation.

But in Python, for large M=100, the code may be slow. However, given the time constraints (3 seconds) and M=100, 100^3 is 1e6 per multiply, and log2(1e18) is 60 steps, so total operations are 60*1e6 * 2 = 1.2e8 operations. Which is manageable.

But in Python, even 1e8 operations might take time, but perhaps the code can be optimized by representing the matrix as a list of lists of integers and using for loops.

Another optimization is to precompute the initial matrix and then raise it to the required power using exponentiation by squaring.

Now, the code:

Implement the matrix exponentiation and multiply functions.

But in Python, nested list comprehensions can be slow. So, perhaps using tuples and more efficient loops.

But for the given problem, the code should work.

So, the code outline is:

MOD = 10**9 +7

Read N and M.

if N < M:

    print(1%MOD)

else:

    # build the transformation matrix.

    def multiply(a, b):

        res = [[0]*M for _ in range(M)]

        for i in range(M):

            for k in range(M):

                if a[i][k] ==0:

                    continue

                for j in range(M):

                    res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD

        return res

    def matrix_power(mat, power):

        result = [[0]*M for _ in range(M)]

        for i in range(M):

            result[i][i] =1

        while power >0:

            if power %2 ==1:

                result = multiply(result, mat)

            mat = multiply(mat, mat)

            power = power //2

        return result

    # build the matrix.

    mat = [[0]*M for _ in range(M)]

    for i in range(M):

        if i ==0:

            mat[i][0] =1

            mat[i][M-1] +=1

        else:

            mat[i][i-1] =1

    k = N - (M-1)

    mat_pow = matrix_power(mat, k)

    initial = [1]*M

    # multiply initial by mat_pow.

    res_vec = [0]*M

    for j in range(M):

        for i in range(M):

            res_vec[i] = (res_vec[i] + initial[j] * mat_pow[j][i]) % MOD

    print(res_vec[0] % MOD)

But in Python, loops for M=100 would be 100^3 for multiply, which is 1e6 operations per multiply. For log2(1e18) steps, which is about 60, the total multiply operations are 60*2 = 120, so total operations are 120e6 → 120 million, which might be tight for Python in 3 seconds.

But perhaps with some optimizations, such as using pre-allocated lists and avoiding creating new lists in multiply.

Alternative approach: precompute the transformation matrix and use bit manipulation for exponentiation.

Alternatively, perhaps use a different matrix multiplication approach, such as using numpy for faster matrix operations, but the problem states that the code must read from stdin and write to stdout, and not use any additional libraries.

So, it's better to proceed with the pure Python code, but optimize the multiply function.

Here's an optimized version of the multiply function:

def multiply(a, b):

    res = [[0]*M for _ in range(M)]

    for i in range(M):

        ai = a[i]

        resi = res[i]

        for k in range(M):

            aik = ai[k]

            if aik ==0:

                continue

            bk = b[k]

            for j in range(M):

                resi[j] = (resi[j] + aik * bk[j]) % MOD

    return res

This way, we avoid some lookups by storing a[i] in ai and res[i] in resi. Also, the inner loop uses bk = b[k], which is a row of b.

Another optimization is to represent the matrix as a list of tuples of tuples, but perhaps this doesn't help much.

Alternatively, perhaps precompute the transpose of the second matrix to improve cache locality, but this might complicate the code.

But for the purposes of this problem, the code should work within the time constraints.

Testing for M=100 and N=1e18:

The code would compute the matrix exponent for N-M+1 = 1e18 -99 steps, which is about 1e18, which takes log2(1e18) ≈60 steps. Each step involves two matrix multiplies (squaring), and the initial multiply steps. For M=100, each multiply is 1e6 operations, so 60 * 1e6 * 2 = 120e6 operations. Python can handle this in under 3 seconds, but it's tight.

But perhaps the code can be further optimized.

Alternative approach: note that the matrix is sparse. For the transformation matrix:

- The first row has 1 in positions 0 and M-1.

- The other rows have 1 only in position i-1.

So, the multiply function can be optimized to handle these sparsity.

For example, when multiplying two matrices a and b:

For the first row of the result, it's a[0][0] * b[0][j] + a[0][M-1] * b[M-1][j].

For other rows, it's a[i][i-1] * b[i-1][j].

But perhaps this is a stretch, but it's worth considering.

Let's see:

The transformation matrix T has the following structure:

Row 0: T[0][0] =1, T[0][M-1] =1, others 0.

Row i (i>0): T[i][i-1] =1, others 0.

When multiplying two such matrices A and B, the resulting matrix C will have:

C[0][j] = A[0][0] * B[0][j] + A[0][M-1] * B[M-1][j]

For i>0, C[i][j] = A[i][i-1] * B[i-1][j]

But since A is a transformation matrix, each row i>0 of A has a 1 at A[i][i-1], and zeros elsewhere.

So, for example, when multiplying A and B:

C[0][j] = A[0][0] * B[0][j] + A[0][M-1] * B[M-1][j]

For i>0:

C[i][j] = B[i-1][j]

Because A[i][k] is 1 only when k=i-1, so C[i][j] = A[i][i-1] * B[i-1][j] = 1*B[i-1][j].

But since B is also a transformation matrix, B's rows for i>0 are zeros except for B[i][i-1] =1.

Wait, no. After multiple multiplications, the matrices may not retain the same structure. But for the case of exponentiating T, perhaps the structure can be maintained.

Wait, the transformation matrix T is:

Row 0: [1, 0, ..., 0, 1]

Row i (i>0): [0,...,1,0,...], where the 1 is at position i-1.

So, when we multiply two such matrices, let's see:

Let A = T^a and B = T^b. What is C = A * B?

For row 0 of C:

C[0][j] = A[0][0] * B[0][j] + A[0][1]*B[1][j] + ... + A[0][M-1]*B[M-1][j]

But since A is a transformation matrix, A[0][0] and A[0][M-1] are 1. The other elements of A[0] are 0.

So C[0][j] = B[0][j] + B[M-1][j].

For rows i>0:

C[i][j] = B[i-1][j]

This is because the only non-zero element in row i of A is at A[i][i-1] =1.

So, when multiplying two transformation matrices, the result is another transformation matrix with:

Row 0 is sum of row 0 and row M-1 of B.

Rows i>0 are row i-1 of B.

This is a key insight that can be used to optimize the multiplication.

Thus, the matrix multiplication can be optimized to take O(M) time instead of O(M^3) time.

This reduces the complexity from O(M^3) to O(M) per multiplication.

For M=100, this would make each multiplication O(100) operations instead of 1e6.

So the code can be optimized as follows.

When multiplying two transformation matrices A and B, the resulting matrix C is computed as:

For row 0:

C[0][j] = (B[0][j] + B[M-1][j]) % MOD

For rows i>0:

C[i][j] = B[i-1][j]

But since B is a transformation matrix, for i>0, B[i-1][j] is 1 only if j = (i-1)-1 = i-2. Wait, no. The structure of B depends on how many times it's been exponentiated.

Wait, the matrix exponentiation approach may not maintain the structure of the transformation matrix, except when the initial matrix is T and we are exponentiating it. Let's think recursively.

When raising T to the power k, the resulting matrix T^k is such that:

- For row 0, it's the sum of rows 0 and M-1 of T^{k-1}.

- For row i>0, it's row i-1 of T^{k-1}.

This suggests that the transformation matrices can be represented as a list of rows, where each row is represented in a compressed form.

But how to compute T^k in O(k*M) time.

Alternatively, for each exponentiation step, the matrix can be represented in terms of its rows, and each multiplication step can be done in O(M) time.

But this requires a different way of representing the matrix.

Let's model the matrix during exponentiation as follows:

The matrix T^k can be represented by its rows. Each row is a list of M elements.

But due to the structure, when exponentiating T, the matrices have a certain structure that allows us to compute their product quickly.

But this requires deeper analysis.

Alternatively, when raising T to the power of k, the resulting matrix can be described in terms of Fibonacci-like numbers.

But I'm not sure. Let's try to find a pattern.

For M=3:

T = [
[1,0,1],
[1,0,0],
[0,1,0]
]

T^2 = T*T:

Row 0: T[0][0]*T[0][0] + T[0][2]*T[2][0] → 1*1 + 1*0 =1? Wait, no. Wait, matrix multiplication is more complex.

Alternatively, perhaps the approach to represent the matrix in a compressed way and multiply them in O(M) time is possible.

For example, the transformation matrices have the following structure:

- Row 0: sum of two rows of the previous matrix.

- Rows 1 to M-1: shifted down by one from the previous matrix.

So, when multiplying two transformation matrices, the resulting matrix can be computed in O(M) time.

This would allow the multiply function to run in O(M) time, which for M=100 is manageable.

Thus, the code can be optimized by representing the matrices as a list of rows, and multiplying them in O(M) time using the structural properties.

The key steps for multiplying two transformation matrices A and B:

- The resulting matrix C's row 0 is the sum of B's row 0 and B's row M-1.

- For rows i>0, C's row i is B's row i-1.

Thus, the multiplication can be done as follows:

def multiply(a, b):

    # a and b are transformation matrices.

    # compute the product c = a * b.

    c = [[0]*M for _ in range(M)]

    # row 0 of c is sum of row 0 of b and row M-1 of b.

    for j in range(M):

        c[0][j] = (b[0][j] + b[M-1][j]) % MOD

    # rows 1 to M-1 of c are rows 0 to M-2 of b.

    for i in range(1, M):

        for j in range(M):

            c[i][j] = b[i-1][j]

    return c

But wait, this is only valid if a is the identity matrix? No. But when a and b are transformation matrices, perhaps this is how the multiplication works.

Let's test this for M=2.

T = [[1,1], [1,0]]

T^2 = T*T:

Original multiplication:

Row 0: 1*1 +1*1=2; 1*1 +1*0=1 → row 0 [2,1]

Row 1:1*1 +0*1=1; 1*1 +0*0=1 → row 1 [1,1]

But according to the optimized multiply function:

sum row 0 and row 1 of b (which is T):

sum [1,1] + [1,0] → [2,1].

For row 0 of c: [2,1].

Rows 1 of c is row 0 of b → [1,1].

But the actual result of T*T is [[2,1], [1,1]], which matches.

Yes. So the optimized multiply function works for M=2.

Another test: M=3.

Let's compute T*T.

Original T:

Row 0: [1,0,1]

Row 1: [1,0,0]

Row 2: [0,1,0]

Multiply T by T:

Row 0 of result is row0 of T multiplied by T.

row0 of T is [1,0,1], multiply by T:

sum (1*1 +0*1 +1*0) →1?

Wait, perhaps it's better to compute T*T using the optimized multiply function.

According to the function:

c's row 0 is sum of T's row0 and T's row2.

T's row0 is [1,0,1], T's row2 is [0,1,0]. sum: [1+0, 0+1, 1+0] = [1,1,1].

Rows 1 and 2 of c are T's rows 0 and 1.

So c is:

row0: [1,1,1]

row1: [1,0,1]

row2: [1,0,0]

But the actual T*T matrix would be:

For row0:

T[0][0]*T[0][0] + T[0][1]*T[1][0] + T[0][2]*T[2][0] = 1*1 + 0*1 +1*0 =1.

T[0][0]*T[0][1] + T[0][1]*T[1][1] + T[0][2]*T[2][1] =1*0 +0*0 +1*1=1.

T[0][0]*T[0][2] + T[0][1]*T[1][2] + T[0][2]*T[2][2] =1*1 +0*0 +1*0=1.

So row0 is [1,1,1].

Row1 of T*T is row0 of T multiplied by T's rows:

T[1][0]*T[0][0] + T[1][1]*T[1][0] + T[1][2]*T[2][0] =1*1 +0*1 +0*0=1.

Similarly, the entire row1 is [1,0,1].

Row2 is T[2][0]*T[0][0] + ... which is 0*1 +1*1 +0*0 =1, then other elements.

Wait, perhaps the actual multiplication would give:

Row1 of T*T is the row0 of T multiplied by T matrix.

No, row1 of T is [1,0,0]. So when multiplying T by T, the row1 of the result is [1,0,0] multiplied by T.

Which is 1* row0 of T + 0* row1 of T + 0 * row2 of T → row0 of T → [1,0,1].

So the result of T*T is:

row0: [1,1,1]

row1: [1,0,1]

row2: [1,0,0]

Which matches the optimized multiply function.

So the optimized multiply function works correctly.

This implies that the multiplication can be done in O(M) time, which is a huge optimization.

Thus, the code can be optimized by using this multiply function, reducing the time complexity from O(M^3) to O(M) per multiplication.

The exponentiation by squaring would then take O(M * log K) time, which is manageable for M=100 and K=1e18.

Thus, the code can be rewritten with this optimized multiply function.

The code steps are:

Read N and M.

If N < M: print 1.

Else:

    Compute k = N - (M-1).

    Initialize the transformation matrix T.

    Compute T^k using exponentiation by squaring, using the optimized multiply function.

    The initial vector is [1]*M.

    Multiply this vector by T^k to get the result.

    The first element of the resulting vector is the answer.

The optimized multiply function is:

def multiply(a, b):

    # a and b are transformation matrices.

    # compute c = a * b.

    c = [[0]*M for _ in range(M)]

    # row 0 is sum of row 0 and row M-1 of b.

    for j in range(M):

        c[0][j] = (b[0][j] + b[M-1][j]) % MOD

    # rows 1 to M-1 are rows 0 to M-2 of b.

    for i in range(1, M):

        for j in range(M):

            c[i][j] = b[i-1][j]

    return c

The matrix exponentiation function:

def matrix_power(mat, power):

    # Initialize result as identity matrix.

    result = [[0]*M for _ in range(M)]

    for i in range(M):

        result[i][i] =1

    while power >0:

        if power %2 ==1:

            result = multiply(result, mat)

        mat = multiply(mat, mat)

        power //=2

    return result

But wait, the identity matrix for this structure isn't the usual identity matrix. The identity matrix for matrix multiplication would have:

row 0: [1, 0, ..., 0, 1]?

No. Wait, the identity matrix I should satisfy I * T = T.

But according to the multiply function, when a is the identity matrix, multiplying it with T should give T.

But according to the multiply function, the identity matrix should have row 0 as sum of row0 and row M-1 of T, which is T's row0 + T's row M-1.

But this is not the case.

Wait, the identity matrix for this optimized multiply function would be such that, when multiplied by any matrix B, the result is B.

But according to the multiply function, when a is the identity matrix:

row0 of result is sum of row0 of B and row M-1 of B.

Rows 1-M-1 of result are rows 0-M-2 of B.

So to get B as the result, the identity matrix must be such that:

sum of row0 of B and row M-1 of B must equal row0 of B.

And rows 1-M-1 of B must be rows 0-M-2 of B.

This is only possible if row M-1 of B is zero, and rows 0-M-2 of B are shifted down.

But this is not possible for arbitrary B. Thus, the initial assumption that the identity matrix is the standard identity matrix is incorrect. This implies that the current approach for matrix exponentiation is incorrect.

This is a problem. The matrix exponentiation approach requires that the identity matrix is the multiplicative identity.

But the multiply function is specific to the transformation matrices. However, the initial matrix T is not the same as the standard matrix. Thus, the matrix exponentiation approach may not work as expected.

Alternatively, perhaps the initial matrix exponentiation is not using the correct identity matrix.

This suggests that the optimized multiply function is only valid when multiplying two transformation matrices, but not when multiplying by the identity matrix.

Thus, the previous approach may not work.

This indicates that the optimized multiply function is not compatible with the standard matrix exponentiation approach, and the initial approach must be revised.

This is a major issue. To resolve this, perhaps the identity matrix for the optimized multiply function is different.

For the standard identity matrix I, I * T = T. But according to the optimized multiply function:

For the identity matrix I, multiplying by T would result in:

row0 of I*T is sum of T's row0 and T's row M-1.

Rows 1-M-1 of I*T are T's rows 0-M-2.

But T's row0 is [1,0,..,1], and row M-1 is [0,...,1,0].

So the sum would be [1,0,...,1] + [0,...,1,0] → [1,0,...,1+0, ...], but depends on M.

But the identity matrix should leave T unchanged. This is not the case.

Thus, the optimized multiply function is not compatible with the standard matrix exponentiation approach. Therefore, the previous approach of using the optimized multiply function is incorrect.

This is a critical error in the previous reasoning. Thus, the matrix exponentiation must use the original multiply function, which handles all elements of the matrix, even if it's slower.

This means that the code cannot be optimized using the previous approach, and must use the original O(M^3) multiply function.

But with M=100 and log2(1e18) steps, this may be too slow in Python.

Alternative idea: note that the initial state vector is [1,1,...,1], and the transformation matrix is T. The resulting vector after k steps is T^k multiplied by the initial vector.

But since the initial vector is [1,1,...,1], perhaps there's a way to compute the result without explicitly multiplying the matrices.

But I'm not sure.

Alternatively, note that the sequence S(n) is a linear recurrence with characteristic equation x^M - x^{M-1} - 1 =0.

But solving this for large M is not feasible.

Alternatively, use the matrix exponentiation approach with the original multiply function.

Thus, the code must proceed as follows, even if it's slow for M=100.

But for the given problem statement, the code must be correct.

Thus, the final code is as follows:

Read N and M.

If N < M: print(1).

Else:

Compute the transformation matrix T.

Compute T^(N-M+1).

Multiply the initial vector [1,1,...,1] by T^(N-M+1).

The first element of the resulting vector is the answer.

So, the code:

MOD = 10**9 +7

N, M = map(int, input().split())

if N < M:

    print(1 % MOD)

else:

    def multiply(a, b):

        res = [[0] * M for _ in range(M)]

        for i in range(M):

            for k in range(M):

                if a[i][k]:

                    for j in range(M):

                        res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD

        return res

    def matrix_pow(mat, power):

        result = [[0]*M for _ in range(M)]

        # Identity matrix

        for i in range(M):

            result[i][i] =1

        while power >0:

            if power %2 ==1:

                result = multiply(result, mat)

            mat = multiply(mat, mat)

            power //=2

        return result

    # Build the transformation matrix.

    mat = [[0]*M for _ in range(M)]

    for i in range(M):

        if i ==0:

            mat[i][0] =1

            mat[i][M-1] +=1

        else:

            mat[i][i-1] =1

    k = N - (M-1)

    mat_pow = matrix_pow(mat, k)

    # Initial vector is [1, 1, ..., 1]

    # Multiply the initial vector by mat_pow.

    # The initial vector is [S(M-1), S(M-2), ..., S(0)] = [1,1,...,1]

    # The result is [S(M-1 +k), S(M-2 +k), ..., S(k)] = [S(N), S(N-1), ..., S(N-M+1)]

    res = [0] * M

    for i in range(M):

        for j in range(M):

            res[i] = (res[i] + mat_pow[j][i]) % MOD

    print(res[0] % MOD)

But wait, the initial vector is [1, 1, ..., 1], which when multiplied by mat_pow gives:

result[i] = sum_{j} initial[j] * mat_pow[j][i]

But since initial[j] is 1 for all j, this is sum_{j} mat_pow[j][i].

So the code can compute the resulting vector as the sum of each column of the matrix_pow.

Thus, the code computes the sum of each column and takes the first element.

This is what the code does.

Testing this code for the samples:

Sample Input 1:

4 2.

M=2, N=4.

k=4-1=3.

mat_pow is T^3.

The matrix T is:

[1,1]

[1,0]

T^3 is:

[3, 2]

[2, 1]

Sum of columns:

For column 0: 3+2=5 → res[0] =5.

For column 1:2+1=3 → res[1]=3.

So the code outputs res[0] =5.

Sample Input 2:

3 2.

k=3-1=2.

mat_pow is T^2.

T^2 is:

[2,1]

[1,1]

Sum of columns:

2+1=3 → res[0] =3.

So the code outputs 3.

Thus, the code works.

So, despite the O(M^3) multiply function, the code should pass all test cases within the time constraints for M up to 100 and N up to 1e18.

The final code is as follows.
</think>

```python
MOD = 10**9 + 7

N, M = map(int, input().split())

if N < M:
    print(1 % MOD)
else:
    # Matrix multiplication function
    def multiply(a, b):
        res = [[0] * M for _ in range(M)]
        for i in range(M):
            for k in range(M):
                if a[i][k]:
                    for j in range(M):
                        res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % MOD
        return res

    # Matrix exponentiation
    def matrix_pow(mat, power):
        result = [[0] * M for _ in range(M)]
        # Identity matrix
        for i in range(M):
            result[i][i] = 1
        while power > 0:
            if power % 2 == 1:
                result = multiply(result, mat)
            mat = multiply(mat, mat)
            power //= 2
        return result

    # Build transformation matrix
    mat = [[0] * M for _ in range(M)]
    for i in range(M):
        if i == 0:
            mat[i][0] = 1
            mat[i][M-1] += 1
        else:
            mat[i][i-1] = 1

    k = N - (M - 1)
    mat_pow = matrix_pow(mat, k)

    # Compute the result vector by summing columns of mat_pow
    res = [0] * M
    for j in range(M):
        for i in range(M):
            res[i] = (res[i] + mat_pow[j][i]) % MOD

    print(res[0] % MOD)
```