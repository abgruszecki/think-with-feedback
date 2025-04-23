<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

So, the problem is about connecting splitters to create exactly n pipes with flowing water. Initially, there's one pipe. Then each splitter can be attached to a pipe that's already flowing. Each splitter has a certain number of outputs. Vova has splitters from 2 up to k outputs. So, each time you attach a splitter, you replace one existing pipe with x new ones. But the key is that each splitter can be used at most once. Wait, the problem says he has one splitter of each kind. So, he can use each splitter (with 2, 3, ..., k outputs) exactly once. So, for example, the 2-output splitter can be used once, the 3-output once, etc.

The goal is to find the minimum number of splitters needed to reach exactly n pipes, or return -1 if impossible.

Hmm. Let's think of how splitters contribute. Let's model the process.

Initially, there's 1 pipe. Each time we add a splitter, say of type x (so x outputs), we take one existing pipe and replace it with x pipes. So, each splitter increases the total count by (x-1). Because replacing 1 with x adds (x-1).

But the problem is that each splitter can be used at most once, and the splitters available are 2, 3, ..., k. So, each of those can be used 0 or 1 times.

So the total number of pipes after using some splitters is 1 + sum (s_i - 1) for each splitter s_i used. Because each splitter adds (s_i - 1) to the total. Wait, because replacing 1 with x gives an increase of x-1. So the total after m splitters is 1 + sum (s_i - 1) for each of the m splitters used. And each s_i is between 2 and k, inclusive? Wait, no. The splitters available are 2,3,...,k. So each s_i is in 2 to k, and each can be used once.

So the problem reduces to selecting a subset of the splitters (each can be used 0 or 1 times), such that 1 + sum (s_i - 1) = n. And we need to find the minimal number of splitters used. But wait, the splitters used must be distinct types. Because each can be used once.

Wait, the problem says "Vova has one splitter of each kind: with 2, 3, 4, ..., k outputs." So he can use each splitter once. So the splitters available are 2,3,...,k. Each can be used 0 or 1 times.

So, the sum (s_i - 1) for the selected splitters must equal (n-1). Because 1 + sum (s_i-1) = n.

So, the problem becomes: find a subset of the numbers 2-1=1, 3-1=2, 4-1=3, ..., k-1, such that their sum is exactly (n-1). And we need the minimal number of elements in such a subset. If no such subset exists, return -1.

Wait, because each splitter contributes (s_i -1) to the sum. For example, using a splitter with 2 outputs adds 1 to the sum. A splitter with 3 outputs adds 2, etc.

So the problem reduces to finding the minimal number of distinct terms from the sequence 1,2,3,..., (k-1) (since each splitter s_i is 2,3,...,k, so s_i -1 is 1 to k-1) such that their sum is exactly (n-1). Because 1 + sum(s_i-1) = n implies sum(s_i-1) = n-1.

But the splitters must be distinct. So each term in the sum must be a distinct integer from 1 to (k-1). And we need the minimal number of terms to sum to (n-1).

So the problem is equivalent to finding the minimal m such that the sum of m distinct integers from the set {1,2,...,k-1} is equal to (n-1). If no such m exists, output -1.

Now, the problem is transformed into a mathematical one: given a target sum S = n-1, and a set of numbers {1, 2, ..., K}, where K = k-1, find the minimal number of distinct terms to sum up to S. If K >=1, then the maximum possible sum with m terms is the sum of the m largest distinct numbers in the set. The minimal possible sum is the sum of the first m numbers (1+2+...+m).

So for the problem to have a solution, S must be between sum(1..m) and sum(K - m +1 ... K) for some m.

We need to find the minimal m where S is achievable as a sum of m distinct numbers from 1 to K.

But how do we compute this efficiently?

First, the minimal number of splitters m is the minimal m such that:

sum of the first m numbers (1+2+...+m) <= S <= sum of the m largest numbers in 1..K.

The sum of the first m numbers is m*(m+1)/2. The sum of the m largest numbers in 1..K is sum from (K - m +1) to K. Which is m*(2K - m +1)/2.

So for a given m, if S is between these two values, then there exists a way to choose m distinct numbers whose sum is S. Therefore, for such m, it's possible.

Our approach is to find the smallest m where m*(m+1)/2 <= S <= m*(2K - m +1)/2. But since K can be up to 1e9, and S up to 1e18, we need an efficient way.

So steps:

1. Check if S < 0: then impossible. Since n >=1, S = n-1 >=0. So only possible when S >=0.

Wait n can be 1, then S=0, and the answer is 0 splitters. Because 1 pipe is already present.

Wait the initial condition is that Vova starts with one pipe. So if n=1, he needs zero splitters. So first, check if n ==1: then if S is 0, return 0.

So for the general case:

If n ==1: answer is 0.

Else, S = n-1. We need to find m such that sum of m terms (distinct from 1 to K) equals S.

But how to find the minimal m.

Let's proceed.

We can model the problem as follows. For each possible m, check if it's possible to form S with m distinct terms from 1..K.

The minimal m is the smallest possible such that this is possible.

So, for each m from 0 up to K:

We need to check two things:

a) The minimal sum for m terms is sum(1..m) = m(m+1)/2. If S < this sum, then even the smallest possible sum with m terms is larger than S. So m is too big.

b) The maximal sum for m terms is sum(K - m +1 ... K) = m*(2K - m +1)/2. If S > this sum, then even the largest possible sum with m terms is smaller than S. So m is too small.

So the valid m's are those where sum_min <= S <= sum_max.

We need to find the smallest m where sum_min <= S <= sum_max.

If such m exists, then the answer is m. Else, it's impossible.

So, the algorithm would be:

Compute S = n-1.

If S < 0: return 0 (if n=1, but n can be 1, then S is 0, so the answer is 0).

Else:

For the minimal m, start from m=0 and check upwards. Wait, but how to compute this efficiently?

Wait, m can't be larger than K, because you can't have more distinct terms than there are elements in the set {1,2,...,K}.

So the possible m ranges from 0 to min(K, ...). But K can be up to 1e9, so iterating from 0 upwards is impossible.

So we need a way to compute the minimal m using mathematical expressions.

Alternatively, we can binary search m.

Wait, the minimal m is the smallest m where sum_min <= S and sum_max >= S.

Wait, but for m to be possible, S must be between sum_min(m) and sum_max(m). So the minimal m is the smallest m where sum_min(m) <= S and sum_max(m) >= S.

But how do we find that?

Alternatively, for a given m, we can compute sum_min and sum_max. Then check if S is in [sum_min, sum_max].

If yes, then m is a possible candidate. The minimal such m is the answer.

We need to find the smallest m for which this holds.

But how to find this m efficiently.

Let me think.

Let's consider that sum_min(m) = m(m+1)/2.

sum_max(m) = m*(2K - m +1)/2.

We need to find the smallest m such that sum_min(m) <= S <= sum_max(m).

So for m to be possible, two conditions must hold:

sum_min(m) <= S <= sum_max(m)

We need to find the minimal m where this is true.

If there exists such an m, then the answer is m. Else, it's impossible.

But how to compute this efficiently.

We can model this as a search problem for m.

The minimal possible m is 0 (if S=0, which is when n=1).

The maximal possible m is K, since you can't have more than K terms.

So, the possible m ranges from 0 to K.

But K can be up to 1e9, so linear search is impossible. So binary search on m.

Wait, but binary search may not directly apply because the condition isn't monotonic. Wait, perhaps for m increasing, the sum_max(m) may first increase and then decrease. Let's see.

sum_max(m) = m*(2K -m +1)/2. For m from 0 to K.

This is a quadratic function of m. Let's see:

At m=0, sum_max is 0.

At m=1: sum_max = (2K -1 +1)/2 *1 = (2K)/2= K.

At m=2: (2K -2 +1)*2 /2 = (2K-1)*2/2 = 2K-1.

Wait, but this depends on K. For example, if K is 5, then for m=5, sum_max is 5*(10 -5 +1)/2 =5*6/2=15.

Wait, sum_max(m) for m in 1..K is:

m*(2K -m +1)/2 = (m*(2K -m +1))/2.

Which is a quadratic in m: -m² + (2K+1)m /2.

The maximum of this quadratic is at m = (2K+1)/2, which is when m is around K. So sum_max increases up to m=K, then decreases. Wait, but m can't be larger than K because you can't take more than K distinct numbers. So for m up to K, sum_max increases as m increases up to a certain point, then decreases.

But perhaps for m up to K, sum_max(m) is increasing until m is (2K+1)/2, but since m can't exceed K, this may not be the case. Wait, for m=K, sum_max(m) is K*(2K - K +1)/2 = K*(K+1)/2, which is the sum of 1+2+...+K. Wait, no. Wait, sum_max(m) for m=K is the sum of the K largest numbers in 1..K, which is 1+2+...+K. Which is K(K+1)/2. But that's the same as sum_min(K). Wait, no. sum_min(m) is 1+2+...+m. sum_max(m) is sum of the m largest numbers in 1..K, which for m=K is sum of 1..K. So sum_max(m) when m=K is same as sum_min(K). So sum_max(m) for m=K is sum_min(m). So this suggests that when m=K, sum_max(m) is sum_min(K) = K(K+1)/2. So if S is exactly sum_min(m), then m is possible.

So, back to the problem.

For each possible m, if sum_min(m) <= S <= sum_max(m), then it's possible to select m splitters.

But how to find the minimal m.

Hmm. Let's consider possible m. For each m, check if sum_min(m) <= S <= sum_max(m). If yes, then possible.

We need to find the minimal m for which this is true.

But how?

The sum_min(m) increases with m, as m increases.

sum_max(m) is a quadratic function. But for m up to K, sum_max(m) increases up to m= (2K+1)/2, but since m can't exceed K, sum_max(m) will increase up to m=K if K is less than the vertex.

Wait, perhaps for K >=1, sum_max(m) increases up to m=K. Let's see:

Take K=5. Then sum_max(m) for m from 0 to 5:

m=0: 0

m=1: 5*(2*5 -1 +1)/2 *1? Wait, no. Wait, sum_max(m) is the sum of the m largest numbers in 1..K. For K=5, the largest m numbers are 5,4,3,2,1.

So sum_max(1) is 5. sum_max(2) is 5+4=9. sum_max(3) is 5+4+3=12. sum_max(4) is 5+4+3+2=14. sum_max(5) is 15.

So sum_max(m) increases as m increases from 1 to 5.

So for K=5, sum_max(m) increases with m up to m=5.

Hmm. So for any K, sum_max(m) is the sum of the m largest elements, which are K, K-1, ..., K -m +1. So sum_max(m) is sum_{i=0 to m-1} (K - i) = m*K - sum_{i=0 to m-1} i = m*K - m(m-1)/2.

Which is m*(2K -m +1)/2.

So, for m up to K, sum_max(m) increases as m increases.

Because for each m, adding another element (the next largest) will add K - m to the sum. For example, m increases by 1, sum_max increases by K - m.

But K is fixed. For example, K=5:

sum_max(1) =5.

sum_max(2) =5+4=9 (increase by4).

sum_max(3)=5+4+3=12 (increase by3).

sum_max(4)=5+4+3+2=14 (increase by2).

sum_max(5)=5+4+3+2+1=15 (increase by1).

So sum_max(m) is increasing as m increases.

So for m from 0 to K, sum_max(m) increases.

But sum_min(m) = m(m+1)/2, which is also increasing as m increases.

So sum_min(m) and sum_max(m) are both increasing functions of m.

So for S given, we need to find the minimal m where sum_min(m) <= S and sum_max(m) >= S.

Since sum_min and sum_max are increasing, the possible m's form a range. The minimal m is the smallest m where sum_min(m) <= S and sum_max(m) >= S.

But how to find this m efficiently.

Let me think about possible m.

We can binary search m.

But what's the lower and upper bounds?

The minimal possible m is 0 (if S=0). The maximum possible m is min(K, m_max), where m_max is such that sum_min(m_max) <= S. But since sum_min increases, m_max is the maximum m where sum_min(m) <= S.

But maybe for some m, sum_min(m) <= S but sum_max(m) < S. So such m is invalid.

But the approach is to find the minimal m where sum_min(m) <= S and sum_max(m) >= S.

We can precompute the possible m's.

Alternatively, we can iterate m from 1 upwards until sum_min(m) exceeds S, but for K up to 1e9, this is not feasible.

Alternative approach: find all possible m where sum_min(m) <= S and sum_max(m) >= S. The minimal such m is the answer.

Let me consider the conditions:

sum_min(m) <= S <= sum_max(m)

sum_min(m) = m(m+1)/2 <= S

sum_max(m) = m*(2K -m +1)/2 >= S

We can rewrite these two inequalities to find possible m.

The first inequality: m(m+1)/2 <= S → m² + m -2S <=0. The roots are m = [-1 ± sqrt(1+8S)]/2. The positive root is (sqrt(8S+1)-1)/2. So m must be <= this value.

The second inequality: m*(2K - m +1)/2 >= S → m*(2K -m +1) >= 2S → -m² + (2K+1)m - 2S >=0 → m² - (2K+1)m + 2S <=0. The roots are [(2K+1) ± sqrt( (2K+1)^2 - 8S ) ] /2.

The inequality holds when m is between the two roots. So m must be >= the lower root and <= the upper root.

So combining both inequalities, m must be in the range where it's less than (sqrt(8S+1)-1)/2 (from first inequality) and between the two roots of the second inequality's quadratic.

But this seems complicated.

Alternatively, for a given m, sum_min(m) and sum_max(m) can be computed quickly. So perhaps we can binary search m.

But how?

We can binary search m in the range [0, K], and check for each m if sum_min(m) <= S and sum_max(m) >= S. But since sum_min and sum_max are both increasing, the minimal m can be found by finding the smallest m where sum_min(m) <= S and sum_max(m) >= S.

But how?

Alternatively, the minimal possible m is the minimal m where sum_min(m) <= S and sum_max(m) >= S.

We can compute the minimal m as follows:

Find the minimal m where sum_min(m) <= S and sum_max(m) >= S.

But how?

We can find the minimal m such that sum_min(m) <= S and sum_max(m) >= S.

Let's first find the minimal possible m where sum_min(m) <= S. The maximum possible m where sum_min(m) <= S is m_max = floor( (sqrt(8*S +1) -1)/2 )

Then, for each m from 1 up to m_max, check if sum_max(m) >= S.

The minimal m that satisfies sum_max(m) >= S is the answer.

Wait, but sum_max(m) is increasing. So as m increases, sum_max(m) increases. So once m is such that sum_max(m) >= S, then all higher m's will also have sum_max(m) >= S (since sum_max is increasing). So for the minimal m, we can find the minimal m where sum_max(m) >= S, and sum_min(m) <= S.

But since sum_max increases with m, the minimal m for which sum_max(m) >= S is the smallest m where sum_max(m) >= S. However, this m may not satisfy sum_min(m) <= S. So, perhaps the correct approach is:

Find the minimal m such that sum_max(m) >= S and sum_min(m) <= S.

But how?

Because sum_max is increasing, for m >= some value, sum_max(m) will be >= S. The minimal such m is m_low.

But sum_min(m) is also increasing. So sum_min(m_low) may be greater than S, which is not allowed.

So, the valid m must satisfy sum_min(m) <= S and sum_max(m) >= S.

We can model this as follows: the minimal m is the maximum between the minimal m where sum_max(m) >= S and the minimal m where sum_min(m) <= S.

Wait, no. Because sum_min and sum_max are both increasing.

We need to find the smallest m where sum_max(m) >= S and sum_min(m) <= S.

Because sum_max increases, the minimal m where sum_max(m) >= S is m_low. But sum_min(m_low) could be larger than S. So in that case, it's invalid.

So perhaps, for m to be valid, m must be in the range [a, b], where a is the minimal m where sum_max(m) >= S, and b is the maximal m where sum_min(m) <= S.

But since sum_max is increasing and sum_min is also increasing, the intersection of these two ranges would be m_low to m_max. If m_low <= m_max, then there exists a solution. The minimal m in this range is m_low, but sum_min(m_low) could be <= S.

Wait, but sum_max(m) >= S and sum_min(m) <= S. So for m to be valid, both conditions must hold.

But how to find such m.

Alternative approach:

We can compute for each m, sum_min(m) and sum_max(m) are both increasing.

So, for m to be valid, sum_min(m) <= S <= sum_max(m).

So the minimal valid m is the smallest m where sum_max(m) >= S and sum_min(m) <= S.

But how?

We can find the smallest m where sum_max(m) >= S. Let's call this m_low.

Then check if sum_min(m_low) <= S. If yes, then m_low is the answer.

If not, then there is no solution.

But why?

Because sum_max(m) is increasing. So for m >= m_low, sum_max(m) >= S.

But sum_min(m) is also increasing. So for the m_low, sum_min(m_low) may be larger than S.

In that case, even though sum_max is >= S, sum_min is larger than S, so no possible subset with m_low terms.

But then, perhaps even for m_low, sum_min(m_low) <= S.

But how?

Let me see.

sum_min(m) = m(m+1)/2.

sum_max(m) = m(2K -m +1)/2.

For example, if S is between sum_min(m) and sum_max(m) for some m, then m is valid.

But how to find the minimal m where this is possible.

Alternative idea: For a given m, the minimal sum is sum_min(m) and the maximal sum is sum_max(m). So if sum_min(m) > S, then even the minimal sum is larger than S, so this m is too big. If sum_max(m) < S, then even the maximal sum is too small, so this m is too small.

So the possible m must be such that sum_min(m) <= S and sum_max(m) >= S.

We need to find the minimal such m.

We can model this as a search problem. We can iterate m from 1 to m_max (which is the maximum m where sum_min(m) <= S), and for each, check if sum_max(m) >= S. The first m in this range where sum_max(m) >= S is the answer.

But how to compute this efficiently.

For example, since sum_max(m) is increasing, once we find the minimal m where sum_max(m) >= S and sum_min(m) <= S, that's the answer.

But how to find this m quickly.

Let me think of binary search.

We can binary search m in [1, m_max], where m_max is the largest m such that sum_min(m) <= S.

In each step, compute mid and check if sum_max(mid) >= S. If yes, then the answer could be mid or a smaller m. Else, need to look higher.

Wait, but sum_max is increasing, so once sum_max(m) >= S, any higher m will also have sum_max(m) >= S. So the minimal m in [1, m_max] where sum_max(m) >= S is the answer.

But only if sum_min(m) <= S.

But m_max is the largest m where sum_min(m) <= S. So for any m in [1, m_max], sum_min(m) <= S.

So if sum_max(m_max) >= S, then the minimal m is the smallest m where sum_max(m) >= S.

Because sum_max is increasing, the minimal m where sum_max(m) >= S is the first m in the range [1, m_max] where this is true.

But how to compute this.

So, binary search m between 1 and m_max, and find the minimal m where sum_max(m) >= S.

Because sum_max is increasing, the binary search can find the leftmost m where sum_max(m) >= S.

So steps:

1. Compute S = n-1.

2. If S ==0, then answer is 0 (if n=1).

3. Else:

   a. Check if K (k-1) is 0. If K is 0, then possible only if S=0. But since S >=1 here (n>1), then impossible. Return -1.

   b. Compute m_max = floor( (sqrt(8*S +1) -1)/2 ). This is the maximum m where sum_min(m) <= S.

   c. Compute the minimal m in [1, m_max] where sum_max(m) >= S.

   d. If such an m exists (i.e., sum_max(m_max) >= S), then the answer is m.

   e. Else, return -1.

But wait, sum_max(m_max) is the maximum possible sum for m_max terms. So if even that is less than S, then no possible m can satisfy.

So the algorithm is:

Compute S = n-1.

If S ==0: return 0.

Else:

If K ==0: return -1 (but K is k-1, which for k>=2 is at least 1. So K can't be 0).

Compute m_max = (sqrt(8*S +1) -1) // 2.

If m_max > K: then set m_max = K (since we can't use more than K terms).

Now, check if sum_max(m_max) >= S. If not, then even the maximum possible sum (using m_max terms) is less than S, so return -1.

Else, find the minimal m in [1, m_max] where sum_max(m) >= S.

This minimal m is the answer.

But how to compute this minimal m.

Because sum_max is increasing, we can binary search for the minimal m where sum_max(m) >= S.

Wait, sum_max(m) is sum of the m largest numbers in 1..K. So it's sum_max(m) = m*(2K -m +1)/2.

We can compute sum_max(m) for a given m.

So binary search between low=1 and high=m_max.

But let's see:

The minimal m where sum_max(m) >= S.

For example, for K=3 (k=4?), S=5.

sum_max(1) =3. sum_max(2)=3+2=5. So m=2.

But sum_max(2) is 5 >=5, so m=2 is the minimal.

So binary search would find 2.

So in code, this would work.

So, steps:

Check if S=0: answer 0.

Else:

Compute m_max = (sqrt(8S+1) -1) //2.

But m_max can be up to 1e9.

Then, compute the sum_max(m_max) = m_max*(2*K -m_max +1)/2.

If sum_max(m_max) < S: then impossible.

Else:

We need to find the minimal m where sum_max(m) >= S, with m <= m_max.

We can binary search this m.

The binary search will find the leftmost m where sum_max(m) >= S.

But sum_max is increasing, so the leftmost m is the minimal m that satisfies sum_max(m) >= S.

Once found, return that m.

Wait, but sum_max(m) is increasing, so the binary search can proceed as follows:

Initialize low=1, high = m_max.

result = -1.

While low <= high:

   mid = (low + high) //2

   current_sum = sum_max(mid)

   if current_sum >= S:

      result = mid

      high = mid -1

   else:

      low = mid +1

So after the loop, if result is found, return it. Else, return -1.

But since sum_max(m_max) >= S, the result must be found.

So, in code:

So putting it all together.

Now, let's test some examples.

Example 1:

Input:

4 3 → n=4, k=3 → K =3-1=2.

S =4-1=3.

Compute m_max:

sqrt(8*3 +1) = sqrt(25) =5 → (5-1)/2=2. So m_max=2.

sum_max(2) = 2*(2*2 -2 +1)/2 → 2*(3)/2=3. Which is equal to S=3. So yes.

Then binary search between 1 and 2.

Check mid=1: sum_max(1) =2 → 2 <3 → no. So low=2.

Check mid=2: sum_max(2)=3 >=3. So result=2. Answer is 2. Which matches the sample.

Another example:

Input 5 5 → n=5, k=5. K=4.

S=5-1=4.

m_max= (sqrt(8*4+1)-1)/2 → sqrt(33)=5.744 → (5.744-1)/2=2.372 → m_max=2.

sum_max(2) =2*(2*4 -2 +1)/2 → 2*(8-2+1)/2 → 2*7/2=7 >=4. So possible.

Binary search between 1 and 2.

Check mid=1: sum_max(1) is 4. So 4 >=4 → result=1. Then high=0. Loop ends. So answer is 1. Which matches the sample.

Third example:

Input 8 4 → K=3.

S=8-1=7.

m_max: sqrt(8*7 +1) = sqrt(57)=7.54 → (7.54-1)/2=3.27 → m_max=3.

sum_max(3) =3*(2*3 -3 +1)/2 → 3*(4)/2=6 <7. So sum_max(m_max)=6 <7. So no solution. Answer is -1. Which matches the sample.

Another test case: n=1, any k: returns 0.

Another case: n=2, k=2. S=1. K=1.

m_max= (sqrt(8*1+1)-1)/2 → (3-1)/2=1.

sum_max(1) =1*(2*1 -1 +1)/2=1*2/2=1 >=1. So answer is 1.

But sum_min(1) =1*2/2=1, which is <=1. So correct.

So, the code needs to handle these cases.

Now, the code steps:

Read n and k.

Compute S = n-1.

If S ==0: return 0.

Else:

K =k-1.

If K <1: then no splitters available. So if S>0, impossible.

But k is at least 2, so K is at least 1.

Compute m_max = floor( (sqrt(8*S +1) -1)/2 )

But since m_max can't exceed K, set m_max = min(m_max, K).

Compute sum_max(m_max). If sum_max(m_max) < S → return -1.

Else:

Binary search for the minimal m in [1, m_max] where sum_max(m) >= S.

Return that m.

But how to compute sum_max(m) quickly.

sum_max(m) = m*(2*K -m +1) // 2.

So code for sum_max:

def sum_max(m, K):

    return m * (2*K - m +1) // 2

Now, code:

Handle very large numbers. Since n can be up to 1e18, and k up to 1e9, K can be up to 1e9.

But all calculations are manageable.

Now, code:

Read n and k.

n, k = map(int, input().split())

if n ==1:

    print(0)

    exit()

S = n-1

K =k-1

# Compute m_max

m_max = int( ( ( (8*S +1)**0.5 -1 ) ) // 2 )

if m_max > K:

    m_max = K

# compute sum_max(m_max)

current_sum_max = m_max * (2*K - m_max +1) // 2

if current_sum_max < S:

    print(-1)

else:

    # binary search between 1 and m_max

    low =1

    high = m_max

    ans = -1

    while low <= high:

        mid = (low + high) //2

        s_max = mid*(2*K -mid +1) //2

        if s_max >= S:

            ans = mid

            high = mid -1

        else:

            low = mid +1

    print(ans if ans !=-1 else -1)

Wait, but sum_max(m_max) >=S, so the binary search must find ans.

But need to make sure.

So the code should work.

Test case where K is 3 (k=4), S=3.

m_max is 2. sum_max(2) is 2*(6-2+1)/2 = 2*5/2=5 >=3. So binary search.

low=1, high=2.

mid=1: sum_max(1) =3 → 3>=3. ans=1. high=0.

Loop ends. answer is 1.

But sum_min(1) is 1. So S=3 >=1. So yes. But sum_max(1) is3. So 3 >=3. So m=1 is possible. But wait, sum_max(1) is 3, which is exactly S. So the answer is 1.

But according to the first sample, the answer was 2. Wait, no. Wait the first sample's input was:

4 3 → n=4, k=3. So K=k-1=2.

S=3.

Then m_max is (sqrt(25) -1)/2=2.

sum_max(m_max=2) =2*(2*2 -2 +1)/2=2*(3)/2=3 ==3. So sum_max(2) is 3.

So binary search between 1 and 2.

Mid=1: sum_max(1) =2 → 2 <3. So no. low=2.

mid=2: sum_max(2)=3 >=3. ans=2. high=1. loop ends. So answer is 2. Which is correct.

So code works.

Another example: when K=4, S=4.

m_max = (sqrt(33)-1)/2= (5.744-1)/2= 2.372 → m_max=2.

sum_max(2) is 2*(8 -2 +1)/2=2*7/2=7 >=4.

binary search:

low=1, high=2.

mid=1: sum_max(1) =4 →4 >=4. ans=1. high=0. return 1.

sum_min(1)=1 <=4. So valid. Answer is1. Which is correct.

Thus, the code works.

So, in code:

The code should handle all the cases correctly.

So the code is:

Read n and k.

If n ==1: print 0.

Else:

Compute S =n-1.

Compute K =k-1.

Compute m_max as (sqrt(8*S +1) -1) //2, then clamp to K.

If sum_max(m_max) <S: print -1.

Else binary search for the minimal m in 1..m_max where sum_max(m) >=S.

Print m.

Now, code.

But in Python, for very large numbers, the square root might be imprecise. So perhaps, we can compute m_max via binary search.

Alternatively, use integer square root.

But in Python, for S up to 1e18, 8*S+1 is up to 8e18+1. The square root is about 2.8e9. So for m_max up to 2.8e9, which is manageable.

But in Python, the calculation of (8*S +1)**0.5 can have floating point precision issues.

For example, for S=1e18, 8*S+1 is 8e18+1. The square root is 894427190.999... So using integer conversion may lead to off-by-one errors.

So a better way to compute m_max is to perform binary search for the largest m where sum_min(m) <=S.

sum_min(m) = m(m+1)/2 <=S.

We can binary search m in 0 to 2e9 (since S is up to 1e18, m_max is up to around 4.4e9 for S=1e18). Wait, sum_min(m) = m(m+1)/2 <=S → m^2 ≈ 2S → m ~ sqrt(2S) → which is up to 1e9 for S=1e18 (since sqrt(1e18)=1e9).

So binary search for m_max as the largest m where m(m+1)/2 <= S.

This would be more accurate.

So the code can be adjusted.

So:

Compute m_max via binary search.

low =0, high = 2e18 (some large number).

find the largest m where m(m+1)/2 <= S.

Similarly.

So code steps for m_max:

low =0

high = int( (2*S)**0.5 ) +2  # initial high value.

m_max =0

while low <= high:

    mid = (low + high) //2

    sum_min = mid*(mid+1)//2

    if sum_min <=S:

        m_max =mid

        low=mid +1

    else:

        high=mid-1

Then, clamp m_max to K.

This is more accurate.

But since S can be up to 1e18, the binary search for m_max would take about 60 steps, which is manageable.

So the code can be adjusted accordingly.

This is safer to avoid floating point inaccuracies.

So let's rewrite the code:

Read n and k.

if n ==1:

    print(0)

    exit()

S =n-1

K =k-1

if K ==0:

    # then no splitters available. So S must be 0, which is not possible here.

    print(-1)

    exit()

# compute m_max as the maximum m where m*(m+1)/2 <=S.

low =0

high = 2*10**18  # arbitrary large number.

m_max =0

while low <=high:

    mid = (low + high) //2

    s_min = mid*(mid+1)//2

    if s_min <= S:

        m_max =mid

        low=mid +1

    else:

        high=mid-1

# clamp to K.

if m_max > K:

    m_max = K

# compute sum_max for m_max.

sum_max_mmax = m_max*(2*K - m_max +1) //2

if sum_max_mmax < S:

    print(-1)

else:

    # binary search for minimal m where sum_max(m) >= S.

    low =1

    high =m_max

    ans =-1

    while low <=high:

        mid = (low + high) //2

        s_max = mid*(2*K - mid +1) //2

        if s_max >=S:

            ans=mid

            high=mid -1

        else:

            low =mid+1

    print(ans)

Yes, this code should work.

Testing the first sample:

Sample 1:

n=4, k=3.

S=3, K=2.

Compute m_max.

sum_min(m) = m(m+1)/2 <=3.

Possible m:

m=2: 2*3/2=3 <=3 → yes.

m=3: 3*4/2=6>3. So m_max=2.

Clamp to K=2.

sum_max(m_max)=2*(4-2 +1)/2 → 2*3=6/2=3 >=3. So proceed.

Binary search between 1-2.

mid=1: s_max= 1*(4-1 +1)/2= (4*1)/2=2 <3 → no. low=2.

mid=2: s_max=3 >=3 → ans=2. Return 2.

Sample 2:

n=5, k=5 → K=4.

S=4.

Compute m_max.

sum_min(m) =m(m+1)/2 <=4.

Possible m=2: 3 → sum=3. m=3: 6>4. So m_max=2.

sum_max(2) =2*(8-2+1)/2=2*7/2=7 >=4.

Binary search between 1-2.

mid=1: s_max=4 >=4 → ans=1. high=0.

Return 1.

Sample3:

n=8, k=4 → K=3.

S=7.

Compute m_max: find m where sum_min(m) <=7.

m=3: 3*4/2=6 <=7.

m=4:4*5/2=10>7. So m_max=3.

Clamp to K=3.

sum_max(3) =3*(6 -3 +1)/2=3*4/2=6 <7. So return -1.

Thus, code works.

So, this code should handle all cases accurately, even for very large values.
</think>

```python
n, k = map(int, input().split())

if n == 1:
    print(0)
    exit()

S = n - 1
K = k - 1

# Find m_max using binary search
low, high = 0, 2 * 10**18
m_max = 0
while low <= high:
    mid = (low + high) // 2
    sum_min = mid * (mid + 1) // 2
    if sum_min <= S:
        m_max = mid
        low = mid + 1
    else:
        high = mid - 1

# Clamp m_max to K
if m_max > K:
    m_max = K

# Check if sum_max(m_max) >= S
sum_max_mmax = m_max * (2 * K - m_max + 1) // 2
if sum_max_mmax < S:
    print(-1)
else:
    # Binary search for minimal m where sum_max(m) >= S
    low, high, ans = 1, m_max, -1
    while low <= high:
        mid = (low + high) // 2
        current_sum = mid * (2 * K - mid + 1) // 2
        if current_sum >= S:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)
```