<think>
Okay, let's try to tackle this problem. Hmm, the problem statement says that we need to count the number of distinct ways to arrange the events over n days, following the pattern white, black, white stripes. Each stripe must have at least one day. Also, each day has events of the same type, and the order of events on a day matters. Oh right, even events of the same type are distinct, so permutations matter.

First, let's break down the problem into parts. We need to model the days as three stripes: white, black, white. Each stripe has at least one day. So the total days are split into three parts: w1, b_days, w2, where w1 >=1, b_days >=1, w2 >=1, and sum is n. So the sum of w1 + b_days + w2 = n.

So first, we need to find all possible ways to split the days into these three parts. For each split, we calculate the number of ways to assign events and arrange them.

But wait, the events have specific counts. The white stripes use good events (w total), and the black stripe uses not-so-good events (b total). However, each day in a white stripe must have at least one event. Similarly for the black stripe days.

Wait, but each day must have at least one event, right? Because the problem states that each day has at least one event. So each day in any stripe has at least one event. So for the white stripes, the sum of events across all days in the first white stripe and the second white stripe must equal w. Similarly, the sum of events in the black stripe days equals b.

But how are the events distributed across the days in each stripe? For example, the first white stripe has w1 days. Each day must have at least one event. So the total events in the first white stripe is some number, say x, and the second white stripe has (w - x) events. But each day in the first and second white stripes must have at least one event.

Wait, no. Wait, the events in white stripes are the good events (w in total). So all the days in the first and second white stripes are days with good events. Each day in these stripes must have at least one good event. Similarly, the days in the black stripe are days with not-so-good events, each with at least one such event.

So the problem is to split the days into three parts (w1, b_days, w2), with each part >=1. Then, distribute the good events (w) into the w1 + w2 days (each of which must have at least one event), and the bad events (b) into the b_days (each with at least one event). Also, the order of events on each day matters. For example, on a day with two good events, the order between them matters, so that's a permutation.

So the steps are:

1. Enumerate all possible splits of the days into w1, b_days, w2, where w1 + b_days + w2 = n, and each is >=1.

For each such split:

2. Calculate the number of ways to distribute the w good events into (w1 + w2) days, each day getting at least one event.

3. Similarly, calculate the number of ways to distribute the b bad events into b_days, each day >=1.

4. Multiply these two numbers, and multiply by the permutation of events (since each day's events can be ordered in any way).

Wait, but how does the permutation come into play? For example, if a day has k events of a type, the number of possible orderings is k! because all are distinct. For example, for good events, each arrangement of events in a day contributes a multiplicative factor of the factorial of the number of events on that day.

Wait, but the problem statement says that events are distinct. So for each day, the events are arranged in a particular order. So for example, if a day in the white stripe has 2 good events, say 1 and 2, then the possible orders are 1 followed by 2 or 2 followed by 1. So each day's events contribute a factorial term based on the number of events on that day.

So the total number of ways for the good events would be the product of:

- the number of ways to split the w events into (w1 + w2) days (each day >=1) multiplied by the product of the factorials of the counts in each day (since each count's events can be permuted).

Similarly for the bad events.

Wait, but distributing the events into days with orderings is similar to the concept of arranging the events into sequences. For example, for the good events: the total number of arrangements is equal to the multinomial coefficient multiplied by the product of the factorials of each group. Wait, maybe another way: Let's say we have to split a sequence of w elements into (w1 + w2) non-empty ordered lists (each list corresponds to a day's events). The number of ways to do this is equal to:

(w! ) * S, where S is the number of ways to split the elements into (w1 + w2) ordered groups, each non-empty, and then multiply by 1 for each group (since the order of the group is the permutation). Wait, no. Wait, if you split the elements into groups, then the order of the groups is fixed (since the days are ordered). But each group's order is a permutation of its elements. So the total number is equal to:

sum_{k_1 + ... + k_{m} = w} (product_{i=1 to m} k_i! ) ), where m is the number of days for good events (w1 + w2). But how to compute this sum?

Alternatively, this is the same as the number of ordered set partitions of the w events into m non-empty subsets, multiplied by the product of the factorials of the subset sizes. Wait, but that's exactly the same as the product of the factorials of the subset sizes multiplied by the multinomial coefficient. Wait, perhaps not. Let's think.

Suppose we have w distinct elements, and we want to partition them into m ordered non-empty lists. Each list's elements are ordered (i.e., the order within the list matters), and the order of the lists matters (since they correspond to days in sequence).

Alternatively, the total number of ways is equal to the sum over all possible splits (k_1, k_2, ..., k_m) where each k_i >=1 and sum k_i = w, of (w! / (k_1! k_2! ... k_m! )) * (k_1! * k_2! ... k_m! )) ). Because the multinomial coefficient (w choose k1, k2, ..., km) gives the number of ways to split the elements into groups of sizes k1, ..., km. Then, for each group, there are k_i! ways to arrange the elements. So the product is (w! / (k1! ... km! )) ) * (k1! ... km! ) = w! So the sum over all possible splits is w! * S, where S is the number of ways to split w elements into m non-empty ordered groups, which is equal to the Stirling numbers of the second kind multiplied by m! ?

Wait, no. The Stirling numbers count the number of ways to partition into non-empty subsets, but when the order of the groups doesn't matter. Here, since the days are ordered, the order of the groups matters. So the number of ways to split into m non-empty ordered groups is equal to the number of ordered partitions, which is equal to S(w, m) * m! where S is the Stirling number of the second kind. But in our case, each group's order matters (the order of elements in the group). So for each split into groups of sizes k_1,...,k_m, the total is (w! / (k1! ... km! )) * product(k_i! ) ) = w! So the sum over all possible splits (k_1 + ... +k_m = w, each k_i >=1) is w! multiplied by the number of compositions of w into m parts. Wait, the number of compositions (ordered) is C(w-1, m-1). So the total would be w! * C(w-1, m-1).

Wait, yes! Because for ordered groups, each group must have at least one element, the number of splits is the same as the number of compositions of w into m parts. The number of compositions is C(w-1, m-1). And for each such composition, the number of ways to arrange the elements is (w! / product(k_i! )) ) * product(k_i! ) ) = w! So for each split (k_1, ..., k_m), the total is w! So overall, the total number of ways is (number of compositions) * w! → which is C(w-1, m-1) * w!.

Wait, that seems right. Because the steps are:

1. Choose how to split the w elements into m ordered groups (each with at least 1 element) → C(w-1, m-1) ways.

2. For each group, the elements can be arranged in any order → for group i, which has k_i elements, there are k_i! possibilities.

But the problem is that the elements are distinct, and the order in which they are assigned to the groups matters. Wait, perhaps the correct approach is to think of the problem as:

We need to arrange the w elements into m sequences (days), each sequence being non-empty. The order of the days matters (since they are part of the overall day sequence), and the order within each day's events matters.

So for example, the first day's events can be any permutation of a subset of the events, as long as all m days are covered.

So the total number of such arrangements is equal to m! * S(w, m) * product over each group's permutations? Wait, perhaps not. Let me think differently.

Another approach: The problem is similar to distributing the w events into the m days (each day must have at least one), and the order of events within each day matters. The order of the days is fixed (since the days are in a sequence). So for each day, the events are ordered. So the total number is the product of the permutations for each day, multiplied by the number of ways to split the events into ordered days.

Alternatively, the total number is the same as the number of ordered lists of ordered non-empty sequences that partition the events.

This is equivalent to permuting the events and inserting m-1 separators between them. But since each day must have at least one event, the number of separators is m-1, and the events are ordered. So this is similar to the stars and bars problem but with permutations.

Wait, yes! For example, think of arranging all w events in a sequence. Then, inserting m-1 dividers into the w-1 gaps between events. Each divider splits the sequence into m parts. Each part is the events for a day. Then, the order within each day's events is the order in the original permutation. So the number of ways is (w-1 choose m-1) ) multiplied by w! (the number of permutations of the events). Because for each permutation, inserting m-1 dividers into the w-1 gaps gives the splits. So the total is (w-1 choose m-1) * w! ?

Wait, that makes sense. Because the permutation defines the order of events. Then, inserting m-1 dividers in the w-1 possible gaps gives the ways to split into m non-empty parts. So the total is (w-1 choose m-1) * w! for the good events. Similarly for the bad events.

But wait, the number of ways to split a permutation into m non-empty parts is (w-1 choose m-1). So for each permutation of the events, there are (w-1 choose m-1) ways to split it into m days. But each split corresponds to a different arrangement. So the total is (number of permutations) × (number of splits per permutation) → w! × (w-1 choose m-1). So the formula is correct.

So, for the good events, when split into m = w1 + w2 days (the sum of days in both white stripes), the total number of ways is C(w-1, m-1) * w! ?

Wait, but wait: for example, if m is 2, then C(w-1, 1) is w-1. Then multiplied by w! gives (w-1) * w! = w! * (w-1). But that's not correct. Wait, maybe I made a mistake here.

Wait, let's take a simple example. Suppose w=2 and m=2. Then the number of ways to split into 2 days is:

Each day must have 1 event. So the permutations of the 2 events. But splitting into two days, each with one event. The order of the days is fixed (since the days are part of the white stripes). So the number of arrangements is 2! × 1 (since there's only one way to split two elements into two days with one each). So 2! × 1 = 2. Which matches the formula C(1,1) * 2! → 1 × 2 = 2. Correct.

Another example: w=3, m=2. Then, the formula is C(3-1, 2-1) * 3! = C(2,1) * 6 = 2 *6=12. Let's see: for m=2 days, each with at least one event.

Possible splits are (1,2) and (2,1). For each permutation of the three events, split into the first day with the first k elements and the next day with the rest. So for each permutation, there are two possible splits. So total is 3! × 2 = 12. Which matches the formula. So the formula is correct.

So yes, the formula for the number of ways to arrange the events of a type (say, white) into m days (each with >=1 event) is (w-1 choose m-1) * w!.

Similarly for the bad events: (b-1 choose b_days-1) * b!.

But wait, in the problem statement, the black stripe's days are exactly b_days (each with at least one bad event). So for the bad events, the formula is (b-1 choose b_days-1) * b!.

So for each split into (w1, b_days, w2), the total ways would be:

number_of_splits = the number of ways to choose the split (w1, b_days, w2) where each >=1 and sum to n.

But how do we compute the number of possible splits (w1, b_days, w2) for a given n?

The splits are determined by w1, b_days, w2 >=1, and their sum is n.

So the number of such splits is equal to the number of integer solutions to w1 + b_days + w2 = n, where each variable is >=1. This is equivalent to (n-1 choose 2). Wait, because substituting variables to x = w1-1, y = b_days-1, z = w2-1, then x + y + z = n-3, and x,y,z >=0. The number of non-negative solutions is C(n-3 + 3-1, 3-1) = C(n-1, 2). So for each possible split, there are C(n-1, 2) possibilities? No, wait. Wait, the substitution gives x + y + z = n-3. The number of solutions is (n-3 +3-1) choose (3-1) )= (n-1 choose 2). So yes. So for each split (w1, b_days, w2), the number of possible combinations is (n-1 choose 2). But wait, no. Because each split is a tuple (w1, b_days, w2). The number of such tuples is the same as the number of compositions of n into three parts each >=1. Which is (n-1 choose 2). So for each split, we need to iterate over all possible (w1, b_days, w2) tuples where sum is n and each >=1.

Wait, but the problem is that for each split, the numbers w1 and w2 are part of the same white stripes. So, the first white stripe has w1 days, the black has b_days, the second white has w2 days. So for each possible split, the order matters between the first and second white stripes, but in this case, since the days are fixed (the first white stripe is before the black), the split is determined by the three parts.

So for each possible split (w1, b_days, w2), we need to compute the product of the ways for white events and black events.

So the overall plan is:

For each possible split (w1, b_days, w2) where sum is n and each >=1:

- Compute m_white = w1 + w2 (total white days)

- Compute m_black = b_days

- The number of ways for white events is C(w-1, m_white-1) * w! if m_white <= w. Otherwise, zero (since you can't split w events into m_white days, each with at least one event).

Similarly for the black events: the number of ways is C(b-1, m_black-1) * b! if m_black <= b. Otherwise, zero.

Then multiply these two numbers for this split. Sum over all possible splits.

But wait, since m_white can be up to (n-2) days (since the split must have at least one day in each of the three parts, so w1 can be up to n-2 (if b_days=1, w2=1), but sum w1 + w2 = (n - b_days) >= 2. So m_white can be from 2 (if both w1 and w2 are 1) up to n-2 (if the black days are 1, and one of the white parts is 1 and the other is n-2-1 + 1? Not sure. Anyway, for each split, we need to check whether m_white <= w and m_black <= b.

But how to handle cases where m_white > w or m_black > b? Those splits would contribute zero to the total sum.

So the approach is:

For each possible split (w1, b_days, w2):

   if m_white = w1 + w2 > w → contribution is zero.

   if m_black = b_days > b → contribution is zero.

   else:

      ways_white = C(w-1, m_white-1) * factorial(w)

      ways_black = C(b-1, m_black-1) * factorial(b)

      total_contribution = ways_white * ways_black

Sum all such contributions.

So the problem reduces to:

- Precompute combinations C(a, k) modulo 1e9+9, for a up to (max possible value), which is (w-1 choose m_white-1) where m_white can be up to n (since w can be up to 4000). Similarly for b.

So for precomputing combinations, we need to compute up to (4000-1 choose ...), but for a up to 4000-1 (since m_white can be up to n, which is up to 4000). Wait, but the maximum possible m_white is (n-2) +1? Because the split must have w1 >=1, w2 >=1, so m_white = w1 +w2 >=2. But w could be up to 4000, so m_white could be up to 4000 (but n is up to 4000, so m_white can't be more than 4000). So for combinations C(w-1, m_white-1), we need to compute combinations where the upper term is up to 4000-1 = 3999, and the lower term is up to (m_white-1) which can be up to (4000-1) (if m_white is 4000). So combinations up to 3999 choose 3999, which is 1. So the maximum required is 4000 terms.

Similarly for C(b-1, m_black-1), m_black is up to n-2 (since w1 and w2 are each at least 1, so b_days can be up to n-2). But since b can be up to 4000, the same logic applies.

Therefore, precomputing combinatorial numbers is manageable.

So the steps are:

1. Precompute factorials up to max(w, b) modulo 1e9+9.

2. Precompute inverse factorials to compute combinations.

3. Precompute combination tables for C(a, k) mod MOD.

Alternatively, compute combinations on the fly using factorial[a] * inv_fact[k] * inv_fact[a -k] mod MOD.

Yes, that's possible.

So first, precompute factorial up to say 4000+4000 (since the maximum possible a in C(a, k) is 4000-1, but 4000 is manageable).

But let's see: for C(w-1, m_white-1), the maximum possible w is 4000, so the a is 3999, and k can be up to 3999.

Similarly for C(b-1, ...), a can be up to 4000-1 = 3999.

So precomputing factorial up to 3999 is sufficient. Wait, no. Because the combination formula is C(n, k) = factorial[n] / (factorial[k] * factorial[n-k] ), so if n is 3999, then factorial[3999] is required.

So precompute factorial up to 4000, and inverse factorial up to 4000.

So steps:

- Precompute fact array up to 8000 (maybe 4000 is enough, but to be safe, perhaps up to 8000). Wait, no. For example, when w is 4000, m_white can be up to 4000 (if possible), so a = 4000-1=3999, and k can be up to 3999. So fact needs to cover up to 3999.

So the plan is:

- Compute fact up to 1e5 (but for the problem constraints, up to 8000 is enough, but it's easier to code up to 1e4 or whatever).

But for Python, precomputing up to 4000+4000 is trivial in terms of time and memory.

So the steps for code:

1. Read n, w, b.

2. Precompute fact and inv_fact up to (max(w, b) + 4000) to handle all possible a and k. Wait, but in this case, for C(w-1, m_white-1), the maximum a is w-1, which can be up to 3999 (when w is 4000). Similarly for b.

Thus, precompute fact up to 4000-1 (3999) for w=4000. Wait, but fact needs to be up to 4000-1 + something. No, the maximum a in C(a, k) is max(w-1, b-1). So precompute fact and inv_fact up to 4000-1 = 3999.

So code:

MOD = 1e9+9

Compute fact = [1]*(max_n), where max_n is 4000+1 (so up to 4000).

But wait, when w is 4000, a is 3999, so fact needs to be computed up to 3999. So precompute fact up to 4000-1=3999.

But in code, for n up to 4000, and w up to 4000:

max_fact = max(w-1, b-1, n) → perhaps 4000-1 = 3999.

So, precompute fact and inv_fact up to 1e5, but for the problem constraints, 1e4 would suffice. But to be safe, let's precompute up to, say, 8000.

But perhaps precompute up to 10^5 to avoid any issues. But for n up to 4000, the code is manageable.

Now, in Python, precomputing factorial up to 8000 is trivial.

Once fact and inv_fact are precomputed, the combination function is:

def comb(a, k):
    if a <0 or k <0 or a <k:
        return 0
    return fact[a] * inv_fact[k] % MOD * inv_fact[a -k] % MOD

So for each split (w1, b_days, w2):

m_white = w1 + w2

m_black = b_days

Check:

if m_white > w: skip (since can't split w events into m_white days each with >=1)

if m_black > b: skip (same reason)

else:

ways_white = comb(w-1, m_white-1) * fact[w] % MOD

ways_black = comb(b-1, m_black-1) * fact[b] % MOD

contribution = (ways_white * ways_black) % MOD

sum all contributions.

Now, the question is how to iterate over all possible splits (w1, b_days, w2) where w1 >=1, b_days >=1, w2 >=1, and sum to n.

The sum is w1 + b_days + w2 = n. Each variable >=1.

We can loop through possible values of b_days from 1 to n-2 (since w1 and w2 must each be at least 1, so their sum is at least 2. So b_days can be from 1 to n-2).

For each b_days in [1, n-2], the remaining days are rem = n - b_days = w1 + w2. rem must be >=2 (since w1 and w2 are >=1 each). For each rem, the possible (w1, w2) pairs are (1, rem-1), (2, rem-2), ..., (rem-1, 1). For each such pair, the number of splits is 1 (since for fixed b_days, each (w1, w2) pair is unique).

Wait, no. For a fixed b_days, the possible w1 and w2 can be any pair that sums to rem = n - b_days, and each >=1. So the number of such pairs is (rem-1). For example, if rem=2: (1,1). rem=3: (1,2), (2,1) → 2 pairs.

So for each b_days in [1, n-2], the number of possible (w1, w2) pairs is (n - b_days -1). Because rem = n - b_days, and the number of ways to split rem into w1 +w2 where each >=1 is (rem-1 choose 1) = rem-1.

Thus, for each b_days, the contribution to the total is (rem-1) multiplied by the ways_white and ways_black for the current m_white = rem and m_black = b_days.

Wait, because for each possible b_days, the m_white is rem = w1 +w2 = n - b_days. And for each possible (w1, w2) pair (rem-1 possibilities), the m_white is fixed as rem. So the product of ways_white and ways_black is the same for all (w1, w2) pairs with the same rem and b_days.

So for a given b_days and rem = n - b_days, the number of (w1, w2) pairs is (rem-1). So for each such b_days and rem, the contribution to the sum is (rem-1) * (ways_white * ways_black), where ways_white and ways_black are computed for m_white=rem, m_black=b_days.

Thus, the code can be optimized to loop over b_days from 1 to n-2, compute rem = n - b_days. Then, compute the product of (rem-1) * (ways_white * ways_black) for that b_days and rem. Then sum all these.

This is a crucial optimization. Because instead of looping through all possible splits (w1, b_days, w2), which could be O(n^2) time (for n up to 4000), this approach reduces the loops to O(n) time, which is manageable.

So the steps are:

Initialize the answer as 0.

Loop b_days from 1 to (n-2):

   rem = n - b_days → rem >=2 (since n >=3, and b_days <=n-2 → rem = n - b_days >= 2).

   m_white = rem → must be >=2.

   m_black = b_days → must be >=1.

   check:

      if m_white > w: continue (since not possible to split w into m_white days each with >=1)

      if m_black > b: continue (same)

      else:

         compute ways_white = comb(w-1, m_white -1) * fact[w]

         compute ways_black = comb(b-1, m_black -1) * fact[b]

         contribution = (rem-1) * ways_white * ways_black

         add contribution to the answer.

So this approach reduces the loop from O(n^2) to O(n), which is acceptable for n=4000.

Now, let's test with the examples.

First example:

Input: 3 2 1 → output 2.

Possible splits:

b_days can be 1 (since n-2 = 1). So b_days=1.

rem=3-1=2 → m_white=2.

Check:

m_white=2 <= w=2 → yes.

m_black=1 <=b=1 → yes.

ways_white = comb(2-1, 2-1) * fact[2] → comb(1,1) =1 → 1 * 2! =2.

ways_black= comb(1-1, 1-1) * fact[1] → comb(0,0) =1 → 1 *1=1.

contribution is (2-1) * 2 *1 =1 *2 =2. So total sum is 2 → correct.

Second example:

Input 4 2 2 → output 4.

Possible splits:

n=4. So b_days can be 1, 2.

Loop for b_days=1:

rem=4-1=3 → m_white=3. But w=2 → m_white=3>2 → skip.

So contribution is zero.

Loop for b_days=2:

rem=4-2=2 → m_white=2 <=2. m_black=2 <=2.

ways_white: comb(2-1, 2-1) * 2! → 1 *2=2.

ways_black: comb(2-1,2-1) *2! →1*2=2.

contribution: (2-1)*2*2=1*4=4.

So total sum is 4 → correct.

Third example:

Input 3 2 2 → output 4.

Possible splits:

n=3. b_days can be 1 (since 3-2=1).

b_days=1 → rem=3-1=2. m_white=2 <=w=2. m_black=1 <=b=2.

ways_white: comb(1,1) *2! →1*2=2.

ways_black: comb(1, 0) → wait, comb(b-1, m_black-1) → b=2, m_black=1. So comb(2-1, 1-1) → comb(1,0)=1. Then multiplied by fact[2] → 2. So ways_black=1*2=2.

contribution: (2-1)*2*2=1*4=4 → correct.

So this approach works.

Now, code steps:

Implement the precomputation of fact and inv_fact up to (max possible a) which is max(w-1, b-1, n).

But since w can be up to 4000, and b up to 4000, then max a is 3999. So precompute fact up to 3999.

But in code, for the precomputation:

Compute fact[0 ... 4000], inv_fact[0 ...4000].

But in Python, how to compute modular inverses?

We can precompute fact and inv_fact arrays as follows:

MOD = 10**9 +9

max_fact = max(w-1, b-1, n) → but since w can be up to 4000, max_fact could be 4000-1=3999.

So:

Compute fact up to 4000-1=3999.

But let's compute up to 4000*2 to be safe, but for code, perhaps precompute up to 8000.

But code can be written as:

MOD = 10**9 +9

n, w, b = map(int, input().split())

max_needed = max(w-1, b-1)

max_fact = max(max_needed, n)

fact = [1]*(max_fact +1)
for i in range(1, max_fact +1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1]*(max_fact +1)
inv_fact[max_fact] = pow(fact[max_fact], MOD-2, MOD)
for i in range(max_fact-1, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def comb(a, k):
    if a <0 or k <0 or a <k:
        return 0
    return fact[a] * inv_fact[k] % MOD * inv_fact[a -k] % MOD

ans =0

for b_days in range(1, n-1+1): # from 1 to n-2, since w1 and w2 must be >=1, so rem = n -b_days >=2. So b_days <=n-2.

    if b_days > n-2:
        continue
    rem = n - b_days
    m_white = rem
    m_black = b_days

    if m_white > w or m_black >b:
        continue

    c_white = comb(w-1, m_white -1)
    c_black = comb(b-1, m_black -1)

    ways_white = c_white * fact[w] % MOD
    ways_black = c_black * fact[b] % MOD

    contribution = (rem-1) * ways_white % MOD
    contribution = contribution * ways_black % MOD

    ans = (ans + contribution) % MOD

print(ans % MOD)

Wait, in the loop for b_days in range(1, n-1 +1):

Wait, the maximum possible b_days is n-2. Because rem =n -b_days >=2 → b_days <=n-2. So the loop should run from 1 to n-2.

In code, the loop can be written as:

for b_days in range(1, n-1):

But wait, in Python, range is exclusive. So for n-2, the code should be range(1, n-1+1)? No. Because in Python, range(1, n-1) would be up to n-2-1. So to loop from 1 to n-2 inclusive, we need to write range(1, n-1+1)? Wait, no.

Wait, range in Python is [start, end), so to get all values from 1 to n-2 inclusive, the code is range(1, n-1) (since n-1 is the end, not included). For example, when n is 3, n-2 is 1. So range(1, 3-1) → range(1,2) → [1].

So yes. So the code should loop for b_days in range(1, n-1):

Because n-1 is the end, not inclusive, so for example, n=3: loop from 1 to 2 (but 2 is not included). So for n=3, the loop is 1.

So in code:

for b_days in range(1, n-1):

But wait, let's test for n=4:

n-1=3. So loop is 1,2. Which is correct (b_days can be 1 and 2).

Yes.

So this code should work.

Testing the first example:

n=3, w=2, b=1.

Loop runs for b_days in 1.

rem=3-1=2. m_white=2 <=2. m_black=1 <=1.

c_white = comb(1, 1) =1. ways_white=1*2=2.

c_black= comb(0,0)=1. ways_black=1*1=1.

contribution= (2-1)*2*1= 1*2*1=2. ans=2.

Output is 2.

Another example:

n=4, w=2, b=2.

Loop runs for b_days=1, 2, but since n-1=3, the loop is up to 2 (range(1,3)).

For b_days=1:

rem=4-1=3. m_white=3 >2 → skip.

For b_days=2:

rem=4-2=2. m_white=2 <=2. m_black=2 <=2.

c_white= comb(1,1)=1 → 1 *2=2.

c_black= comb(1,1)=1 →1 *2=2.

contribution= (2-1) *2 *2=1*4=4. So ans=4.

Correct.

Third example: n=3, w=2, b=2.

Loop runs for b_days=1.

rem=2. m_white=2 <=2. m_black=1 <=2.

c_white= comb(1,1) *2! →1 *2=2.

c_black= comb(1,0) →1 →1*2=2.

contribution: 1 *2*2=4.

So ans=4.

Thus, the code works.

Now, check the precomputation of fact and inv_fact.

For example, in the case where w=2, fact[w] is 2! =2.

comb(w-1, m_white-1) where m_white=2 → comb(1,1)=1.

Thus, code is correct.

So this should be the correct solution.
</think>

```python
MOD = 10**9 + 9

n, w, b = map(int, input().split())

max_needed = max(w - 1, b - 1)
max_fact = max(max_needed, n)

# Precompute factorial and inverse factorial
fact = [1] * (max_fact + 1)
for i in range(1, max_fact + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (max_fact + 1)
inv_fact[max_fact] = pow(fact[max_fact], MOD - 2, MOD)
for i in range(max_fact - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def comb(a, k):
    if a < 0 or k < 0 or a < k:
        return 0
    return fact[a] * inv_fact[k] % MOD * inv_fact[a - k] % MOD

ans = 0

# Iterate over possible black days (b_days)
for b_days in range(1, n - 1):
    rem = n - b_days
    m_white = rem
    m_black = b_days
    
    if m_white > w or m_black > b:
        continue
    
    c_white = comb(w - 1, m_white - 1)
    c_black = comb(b - 1, m_black - 1)
    
    ways_white = c_white * fact[w] % MOD
    ways_black = c_black * fact[b] % MOD
    
    contribution = (rem - 1) * ways_white % MOD
    contribution = contribution * ways_black % MOD
    ans = (ans + contribution) % MOD

print(ans % MOD)
```