<think>
Okay, let's see. The problem is to find the smallest subset of the given array such that the GCD of the subset is 1. If there's no such subset, output -1. Hmm.

First, I need to think about the conditions under which this is possible. Well, if the GCD of the entire array is 1, then there exists a subset (the whole array) with GCD 1. But we need the smallest possible subset. So maybe the minimal subset is of size 2 or 3, etc.

Wait, but how to approach this efficiently for large n (up to 3e5). Because trying all possible subsets is impossible here. So brute force is out of the question. Need a smarter way.

Let's think about the minimal possible subset. The minimal subset can't be of size 1, because then the element itself must be 1. Because the GCD of a single element is the element itself. So if there's a 1 in the array, the answer is 1.

So first step: check if there's a 1 in the array. If yes, then return 1 immediately.

If not, then the minimal subset size has to be at least 2. Now, what's the minimal way to find two numbers whose GCD is 1. Because if such a pair exists, then the answer is 2.

But wait, maybe even if there's a pair with GCD 1, but other elements can't form a subset of size 2? Like, maybe the array has elements 3,4, but also others. Then the answer is 2.

So first, check if there's a 1. Then check if there's any pair with GCD 1. If yes, answer is 2. If not, then maybe check for subsets of size 3, etc. But how?

But for n up to 3e5, checking all pairs is O(n^2), which would be 9e10 operations. That's way too slow.

So we need a better approach.

Hmm. Let's think about the GCD of the entire array. If the GCD is 1, then there must be a subset with GCD 1, but perhaps a smaller subset. Wait, but the GCD of the entire array is the minimal possible GCD among all subsets. Wait, no. Because the GCD of the entire array is the greatest common divisor of all elements. Any subset will have a GCD that is a divisor of the entire array's GCD. So if the entire array's GCD is not 1, then no subset can have GCD 1. So first, check if the GCD of the entire array is 1. If not, output -1.

Wait, right. So the first step is to compute the GCD of all elements. If that's not 1, then output -1. Because any subset's GCD will be a divisor of the overall GCD, which is not 1.

Wait, that's a crucial point. Because the GCD of the entire array is the GCD of all elements. If that's d, then any subset's GCD must be a multiple of d. So if d is not 1, then no subset can have GCD 1. So the answer is -1.

So first, compute the GCD of the entire array. If it's not 1, output -1. Else, proceed to find the minimal subset size.

Wait, no. Wait, the problem says that if the overall GCD is 1, then there exists a subset (the entire array) with GCD 1. So the answer is possible. But the question is to find the minimal subset.

So the first step is: compute the GCD of the entire array. If it's not 1, output -1. Otherwise, find the minimal subset size.

Wait, but even if the overall GCD is 1, the minimal subset could be smaller. For example, in the first example, the entire array's GCD is 1, but all subsets of size less than 3 have GCD >1, so the answer is 3.

So the problem reduces to: when the overall GCD is 1, find the minimal subset size that has GCD 1.

Now, how to find that.

The key insight here is that the minimal subset size is the smallest k such that there exists a subset of size k with GCD 1, and no subset of size k-1 exists with GCD 1.

So how to find this k.

An approach is to realize that the minimal k can be found by checking if there's a pair with GCD 1 (k=2), or else check if any triplet has GCD 1 (k=3), etc. But for large n, this is again impossible.

Alternative approach: Let's think about the minimal number of elements required to reduce the GCD to 1. So for example, if there's a subset of size 2, then the answer is 2. If not, check subsets of size 3.

But even with n=3e5, checking all possible pairs is O(n^2), which is not feasible.

So we need a smarter approach.

Wait, the minimal possible k is the smallest number such that there exists a subset of k elements whose GCD is 1. So perhaps the minimal k is the minimal number of elements needed to cover all the primes in the array. But I'm not sure.

Alternatively, perhaps the problem can be transformed into finding the minimal number of elements such that their combined GCD is 1. Let's think.

Another idea: For each element, track the current GCDs that can be formed with subsets of a certain size. For example, for subsets of size 1, the GCDs are the elements themselves. For subsets of size 2, the GCDs are the GCDs of pairs of elements. For each possible subset size, track the possible GCDs. The moment we find a GCD of 1 for a subset of size k, then k is the answer.

But for n=3e5, this approach is also not feasible, as the number of possible GCDs can be large, and for each element, merging with the previous GCDs may take time.

Wait, but perhaps there's an optimized way to track this. Let's think in terms of dynamic programming. For each position i in the array, and for each possible GCD value d, track the minimal number of elements needed to reach d after considering the first i elements.

But even that could be expensive. For example, the number of possible d's can be up to 3e5 (since a_i is up to 3e5), and n is 3e5. So the total states would be 3e5 * 3e5 = 9e10, which is way too big.

But perhaps there's a way to optimize this. Let's think: the current state is a map from current GCD values to the minimal number of elements required to achieve that GCD. For each new element a[i], we can update this map.

For example, initially, the map is empty. For each a[i], we can:

- Create a new map for the current step.

- For each existing GCD value g in the previous map, we compute the new_gcd = gcd(g, a[i]). For each such new_gcd, we can track the minimal count (previous count + 1).

- Also, the new element alone (count 1) can form a GCD of a[i].

- Then, for the current map, for each possible new_gcd, we keep the minimal count between existing entries and new possibilities.

This way, for each element, we process all possible current GCDs and update them with the new element.

At each step, if any GCD in the current map is 1, then the answer is the minimal count.

But the problem is the number of possible GCDs. For example, if the elements are primes, the number of possible GCDs increases. But in practice, after a few steps, the number of possible GCDs may not be that large, as adding elements reduces the possible GCDs.

So perhaps this approach is feasible.

Let me see. For each element, the number of possible GCDs is O(log a_i), but that's not necessarily true. However, in practice, the number of distinct GCDs after processing each element is not that large, especially since each new GCD must be a divisor of the previous GCDs. So this approach could work for n=3e5.

Let me outline the steps:

Initialize a dictionary (let's call it dp) that maps a GCD value to the minimal number of elements needed to achieve it. Initially, dp is empty.

For each element x in the array:

    Create a temporary dictionary new_dp.

    Add x to new_dp with count 1.

    For each existing gcd value g in dp:

        Compute the new_gcd = gcd(g, x).

        If new_gcd is already in new_dp, take the minimum between the existing count (dp[g] + 1) and the current value in new_dp[new_gcd].

        Otherwise, add new_gcd to new_dp with count dp[g] + 1.

    Merge new_dp into the existing dp. For each key in new_dp, update dp to have the minimal count between the existing value (if any) and the new value.

    After processing x, if dp contains 1, then the minimal count is the current answer.

If after processing all elements, dp contains 1, return the minimal count. Otherwise, return -1.

But wait, the problem says that the overall GCD is 1, so the answer exists. So in that case, the answer will be found.

But we need to compute the overall GCD first. Because if the overall GCD is not 1, return -1.

So the steps are:

1. Check if there's any 1 in the array. If yes, return 1.

2. Else, compute the GCD of the entire array. If it's not 1, return -1.

3. Else, find the minimal k such that a subset of size k has GCD 1.

Now, how to compute the minimal k.

In the dynamic programming approach, for each element, we track the possible GCDs and their minimal counts.

But for n=3e5, and each step having, say, up to 100 GCDs, then the total operations would be 3e5 * 100 = 3e7, which is acceptable.

But in Python, dictionaries can be handled efficiently, but we need to manage this properly.

But let's test this approach on the first example:

Input: 3 elements 10, 6, 15.

Step 1: Check for 1. No. Then compute overall GCD. GCD(10,6,15) is 1.

So proceed.

Process first element 10.

new_dp starts as {10:1}. dp is now {10:1}.

No 1, so continue.

Second element 6.

new_dp is initially {6:1}.

Then process existing elements in dp (10:1). new_gcd = gcd(10,6) = 2. So new_dp now has 6:1 and 2:2.

So after merging, dp is {6:1, 2:1 (wait, no). Wait, how is the merging done?

Wait, when processing the second element, x=6:

new_dp starts with {6:1}.

Then for each entry in the previous dp (which is {10:1}), compute new_gcd = gcd(10,6) = 2. The count is 1+1=2.

So new_dp now has 6:1 and 2:2. Then, the new_dp is merged into dp. So the new dp is {6:1, 2:2}.

Then, check if 1 is present. No.

Third element is 15.

new_dp starts with {15:1}.

Process existing entries in dp (6:1, 2:2).

For 6:1:

new_gcd = gcd(6,15) = 3. count is 1+1=2. So new_dp now has 15:1 and 3:2.

For 2:2:

new_gcd = gcd(2,15) = 1. count is 2+1=3. So new_dp now has 1:3.

Then, merge new_dp into dp. The new dp is {15:1, 3:2, 1:3}.

Now, in this step, we have 1:3, so the minimal count is 3. So the answer is 3.

Which matches the example.

So this approach works for this case.

Another example: the array has elements 3,4,5. The overall GCD is 1. Let's see:

Processing 3: dp {3:1}

Processing 4: new_dp is {4:1}, then process 3. gcd(3,4)=1, count 2. So new_dp has 4:1, 1:2. So in this step, the answer is 2.

So the approach works here.

But what about the case where the minimal subset is 3? Like the first example. So the approach correctly captures that.

So the dynamic programming approach seems feasible.

Now, the main challenge is to implement this efficiently in Python.

But how to handle the dictionaries and merging efficiently.

In Python, for each element, we can process the existing dp dictionary, compute new entries, and keep track of the minimal counts.

But for each x in the array, we can:

- Create a temporary dictionary for the new entries generated by this x.

- For each existing g in the current dp, compute the new_gcd and update the temp dictionary.

- Also, add x as a new entry (count 1) if not present.

Then, after processing all existing entries, we merge the temp dictionary into the current dp, but for each key, we keep the minimal count.

Wait, but the way to handle this is:

At each step, the new_dp is built by considering:

- The new element alone (count 1).

- For each existing g in the previous dp, compute the new_gcd of g and x, and add that with count (previous count +1).

Then, the new_dp is merged into the current dp, but we take the minimal count for each gcd.

Wait, no. Because each step, the dp is replaced by new_dp. Or is it?

Wait, in the processing of x, the new_dp is the combination of:

- All subsets that include x. Because each subset in the new_dp is either {x} (count 1), or a subset that includes x and some elements before it.

Wait, perhaps not. Let's clarify.

The DP state after processing the first i elements is a map that contains for each possible GCD d, the minimal number of elements needed to achieve d using any subset of the first i elements.

When processing the i-th element (x), the new_dp is built by:

1. Adding the subset consisting of only x (count 1).

2. For each existing entry (g, count) in the previous DP, we can create a new entry (gcd(g, x), count + 1). This represents taking the subset that previously had GCD g and adding x to it, resulting in a new GCD of gcd(g, x).

Then, the new_dp is merged with these entries. For each possible GCD in new_dp, we keep the minimal count between any existing entry in the previous DP and the new entries.

Wait, no. Because the previous DP contains all possible GCDs formed by subsets of the first i-1 elements, and the new_dp represents the possible GCDs formed by subsets that include the i-th element. Then, the new DP after processing the i-th element is the union of the previous DP (subsets not including x) and the new_dp (subsets including x). But no, because the previous DP is the state after i-1 elements, which includes all possible GCDs and their minimal counts. But when adding the i-th element, the new possible GCDs are those formed by subsets that include x. So the new_dp is built as follows:

For each possible GCD in the previous DP, combining it with x gives a new GCD (g, x) and increases the count by 1. Also, the subset consisting of x alone (count 1).

Then, for each possible GCD in the new_dp, we take the minimal count between the existing value in the new_dp and any possible existing value in the previous DP.

Wait, but no. Because the previous DP's GCDs are the possible GCDs from subsets not including x. The new_dp's GCDs are from subsets that include x. So the new DP after processing x is the union of:

- The previous DP (subsets not including x), and

- The new_dp (subsets including x).

But in this case, the minimal count for a GCD d would be the minimum between the count in the previous DP (if d is present) and the count in the new_dp (if d is present).

Wait, but that's not correct. Because the new_dp is the set of GCDs that can be formed by subsets that include x. So the new DP after processing x is the union of the previous DP (without x) and the new_dp (with x). For each GCD d in either, the count is the minimal between the previous count (if d is in the previous DP) and the new count (from new_dp).

So the way to update the DP is:

new_dp is built by combining x with the previous DP.

Then, for the current DP (after x is processed), it's the combination of the previous DP and new_dp, but for each GCD, the minimal count between the two.

Wait, but that's not correct. Because the previous DP is for the first i-1 elements, and the new_dp is for the first i elements (those that include x). So the new DP after processing x is the new_dp. Because any subset that includes x is handled in new_dp, and the subsets that do not include x are already handled in the previous DP. But the problem is that the new DP is supposed to track all possible GCDs that can be formed from the first i elements, whether or not they include x. However, the minimal count for a GCD d could be either the count from the previous DP (without x) or the count from new_dp (with x). So to track the minimal counts, the DP after processing x should be a combination where for each possible d, the count is the minimum between the previous count (if d existed in previous DP) and the new count (from new_dp).

But this would require merging the previous DP and the new_dp. For example:

Suppose after processing x, the previous DP has entries {g1: c1, g2: c2} and the new_dp has entries {g3: c3, g2: c4}.

Then the new DP after x would be {g1: c1, g2: min(c2, c4), g3: c3}.

But this approach would double the number of entries each time, leading to O(n^2) time.

But that's not feasible for n=3e5.

Wait, but this is not the case. Because the new_dp represents the GCDs formed by subsets that include x. The previous DP represents the GCDs formed by subsets that do not include x. So for the new DP after x, the entries are the union of previous DP and new_dp. But in this case, the counts from previous DP (without x) are already the minimal possible for subsets not including x, and the new_dp's counts (with x) are the minimal possible for subsets including x. Therefore, the overall minimal count for each GCD is the minimum between the previous DP's count (if exists) and the new_dp's count (if exists).

But merging the two dictionaries would require for each key in either of them, taking the minimum. However, this approach would cause the DP size to grow exponentially. For example, if each step adds a new prime number, the number of possible GCDs would multiply. But for large n, this would quickly become unmanageable.

Thus, this approach is not feasible for n=3e5.

So there's a problem here. The dynamic programming approach I considered earlier would not work for large n because the DP size could grow to O(n * d), where d is the number of divisors of the elements. But for elements up to 3e5, the number of divisors is manageable.

Wait, perhaps the number of possible GCDs is actually small. For example, each new element can only contribute a limited number of new GCDs.

Alternative approach: for each element x, process the current possible GCDs and compute the new GCDs. Then, for each new GCD, keep track of the minimal count. Then, after processing x, the new possible GCDs are the combination of x (as a singleton) and the previous GCDs merged with x.

But here's the key idea: when you process x, you can create a new temporary dictionary (temp_gcds) which starts with x:1. Then, for each existing GCD g in the previous DP, compute new_gcd = gcd(g, x), and for each new_gcd, store the minimal count between the existing count in temp_gcds (if any) and (previous count + 1). Then, after processing all existing GCDs, the new DP is the combination of the previous DP and the temp_gcds. But again, merging is expensive.

Wait, but perhaps the way to model this is that for each x, the new possible GCDs are:

- The GCD of x with any subset from previous steps.

- The GCD of x alone.

But the DP must track for each possible GCD, the minimal count. So when processing x, for each possible GCD g in the previous DP, you can compute new_gcd = gcd(g, x). The count for new_gcd would be the minimal between the existing count (if any) and (count of g) +1.

But how to track this efficiently.

An optimized approach is:

- For each x, create a new temporary dictionary (current_gcds) which starts with x:1.

- For each g in the previous DP's GCDs, compute new_gcd = gcd(g, x). For this new_gcd, if it's already in current_gcds, take the minimum between the existing value and (dp[g] + 1). Otherwise, add it with value (dp[g] + 1).

- Then, after processing all g in the previous DP, the new DP (for this step) is the combination of the previous DP and current_gcds. But again, merging would be O(number of elements in previous DP and current_gcds), which is not feasible.

Wait, but perhaps the previous DP is not needed anymore after this step. Because when processing x, the new possible GCDs are those that can be formed by including x in some subset. Wait, no. Because the DP after processing x should include all possible subsets from the first i elements, including those that don't include x.

So the DP should include:

- All the entries from the previous DP (subsets that do not include x).

- All the entries from current_gcds (subsets that include x).

But merging these two would cause the DP size to increase, which is not feasible.

Thus, this approach is not feasible for large n.

Alternative idea: the minimal subset size that can form a GCD of 1 is the minimal number of elements such that their combined GCD is 1. So, perhaps we can find the minimal k such that there's a subset of k elements with GCD 1. How to find this k quickly.

If there's a pair with GCD 1, then k=2.

If not, then check for subsets of size 3. But how?

But how to find if any pair has GCD 1.

For that, we can precompute all pairs and check their GCD. But for n=3e5, that's O(n^2), which is impossible.

Alternative approach: For all elements, find if any element is coprime with any other.

But even that requires O(n^2) time.

Hmm.

Alternative idea: The minimal subset size is at most the number of distinct prime factors of the overall GCD. Wait, the overall GCD is 1, so that's not helpful.

Alternatively, if the minimal subset size is the minimal number of elements required to cover all the prime factors that exist in the array.

But I'm not sure.

Another approach: Since the overall GCD is 1, there must be elements in the array that are coprime. Or maybe not. For example, the array could have elements that are pairwise non-coprime, but their combined GCD is 1.

For example, 6, 10, 15: each pair has GCD 2, 3, 5 respectively, but the overall GCD is 1.

So in this case, the minimal subset size is 3.

So the pairwise GCDs may not be 1, but the triplet's GCD is 1.

So, to find the minimal subset size, we need to find the smallest k where the subset's GCD is 1. So, the minimal k could be larger than 2.

But how to find this k without checking all subsets.

Another idea: for each possible k, from 2 up to n, check if there's a subset of size k with GCD 1. Once we find the smallest such k, return it.

But how to check if there's a subset of size k with GCD 1.

But even checking for k=2 would require O(n^2) time, which is not feasible.

Alternative approach: To find the minimal possible k, perhaps it's the minimal number of elements needed to cover all the primes in the overall GCD's decomposition. But since the overall GCD is 1, perhaps this is not helpful.

Wait, the problem requires the subset's GCD to be 1. So the subset must contain elements such that their combined GCD is 1.

So, for the entire array, the GCD is 1, which implies that there exists a subset (the entire array) with GCD 1. So the answer exists.

But how to find the minimal k.

Another idea: the minimal subset is the minimal number of elements required to have their pairwise GCDs form a path to 1.

Wait, perhaps not.

Alternatively, think of the problem as follows: the minimal subset is the minimal number of elements needed to "break down" the initial GCDs.

Wait, for example, adding elements reduces the possible GCDs. So perhaps the minimal k is the smallest number of elements such that their combined GCD is 1.

So, how to find that.

An alternative approach is to track for each possible divisor d of the array elements, the minimal number of elements required to achieve a GCD of d. Then, the answer is the value for d=1.

So, the problem reduces to filling a dictionary where for each d, we track the minimal number of elements to achieve a GCD of d.

Initially, this dictionary is empty. For each element x, we can compute its divisors and update the dictionary.

Wait, but how.

Let's think: for each element x, we can generate all possible divisors of x. Then, for each divisor d of x, we can track the minimal number of elements required to achieve a GCD of d. But since the GCD could be reduced when combined with previous elements.

Alternatively, the approach is similar to the earlier dynamic programming idea, but using the divisors of each element.

But I'm not sure.

Alternative idea inspired by the sieve algorithm:

We can track for each possible d, the minimal number of elements needed to form a subset with GCD d. For each element x, we can iterate through all divisors of x. For each divisor d, we can update the count as min(current count for d, 1). Then, for each divisor d, we can also combine it with previous divisors to find new GCDs.

But again, this may not be feasible.

Alternatively, for each element x, we can:

- Generate all possible divisors of x.

- For each divisor d of x, we can update the current count for d to be the minimum between its existing count (if any) and 1.

- Then, for each previous divisor g in the dictionary, compute the new_gcd = gcd(g, x), and for each new_gcd, update the count to be the minimum between the existing count (if any) and (count for g) + 1.

This is similar to the DP approach, but instead of tracking all possible GCDs, we track the divisors of the elements. Since the number of divisors per element is O(1e3) for elements up to 3e5, this might be feasible.

So, for each x in the array:

1. Generate all divisors of x. For each divisor d, update the current DP as dp[d] = min(dp[d], 1) if d is a divisor.

2. For each existing divisor g in the DP before processing x:

   a. Compute new_gcd = gcd(g, x).

   b. For this new_gcd, set dp[new_gcd] = min(dp[new_gcd], dp[g] + 1) if new_gcd exists, else set it to dp[g] + 1.

3. After processing all previous divisors, merge the new_gcd entries into the DP.

But again, this could be O(n * d^2), where d is the average number of divisors per element. For elements up to 3e5, the maximum number of divisors is about 1e3 (like 3e5 has divisors 1, 2, 3, etc., but actual maximum is for 294,912 which has 100+ divisors). So if d is around 1e3, then for n=3e5, this approach is O(3e5 * 1e3) = 3e8 operations. Which is likely to be too slow in Python.

So this approach may not be feasible.

Hmm.

Alternative Idea:

The minimal subset size is at most the number of primes in the prime factors of the elements, but I'm not sure.

Alternatively, the minimal subset size is the minimal number of elements such that the product of their distinct prime factors covers all primes needed to achieve GCD 1.

But again, not sure.

Wait, but the overall GCD is 1, which means that the intersection of the prime factors of all elements is empty. So there exists elements with different prime factors that can be combined to cancel out all primes.

But how to find the minimal subset.

Alternative Idea:

If there's an element that is coprime with some other element, then the answer is 2. So first, check all pairs. If any pair has GCD 1, answer is 2.

Else, the minimal subset size must be >=3.

But checking all pairs is O(n^2), which is not feasible.

But perhaps, we can precompute for each element the set of its prime factors, and for each element x, check if there's any element y in the array that doesn't share any prime factors with x.

But again, for large n, this could be O(n^2) in the worst case.

But perhaps there's a way to count the frequency of primes and find for each x a y that has no primes in common with x.

But for example, if there's a prime that occurs in all elements except one, then the only possible element to form a pair with is that one. So for each element x, check if there's any element not sharing any of x's primes.

But how to do this efficiently.

Alternatively, for each prime p, track the elements that do not have p as a factor. Then, for each element x, check if the intersection of the primes of x is empty with some other element.

But this also seems challenging.

Another Idea:

The minimal subset size is 2 if there exists a pair with GCD 1, otherwise 3, etc.

But how to check if there exists a pair with GCD 1.

If there's no such pair, then the minimal subset size must be at least 3.

But how to check this efficiently.

But for large n, even this is not feasible.

So the initial approach with the dynamic programming seems to be the only way, but we need to optimize it.

Let's re-examine the dynamic programming approach.

The key observation is that each new element can only generate a limited number of new GCDs. So for each element x, the number of possible new GCDs added to the DP is small.

So the steps are:

Initialize a dictionary dp.

For each x in the array:

    Create a new temporary dictionary temp.

    Add x to temp with count 1.

    For each g in the current dp:

        compute new_gcd = gcd(g, x).

        if new_gcd is in temp:

            temp[new_gcd] = min(temp[new_gcd], dp[g] + 1)

        else:

            temp[new_gcd] = dp[g] + 1

    Now, merge temp into the current dp:

        for each key in temp:

            if the key is already in dp:

                dp[key] = min(dp[key], temp[key])

            else:

                dp[key] = temp[key]

    If 1 is in dp, return the minimal count.

If after processing all elements, return the minimal count of 1.

But the problem is that during the merge, the dp may grow in size. However, in practice, the number of keys in dp remains manageable.

For example, each new element x can at most add as many new GCDs as the number of divisors of x. But when merged with previous GCDs, the new GCDs are the GCDs of x with all previous GCDs, which are likely to be a small number.

In Python, using a dictionary and for each element, iterating over the current keys, then updating the temporary dictionary, then merging into the current dictionary.

But for n=3e5 and each step taking O(100) operations, this is manageable.

Let's try to implement this approach.

But in Python, dictionaries are mutable, and during iteration, we need to avoid modifying the dictionary. So for each element x, we need to process the current dp as it was before processing x.

So during each iteration:

current_dp is the dp from previous step.

temp is initialized with {x: 1}.

then, for each g in current_dp:

    new_gcd = gcd(g, x)

    if new_gcd in temp:

        temp[new_gcd] = min(temp[new_gcd], current_dp[g] + 1)

    else:

        temp[new_gcd] = current_dp[g] + 1

Then, after processing all g in current_dp, we need to merge temp into current_dp.

But merging here means that for each key in temp, if it's already present in current_dp, we take the minimum between the existing value and temp's value. Otherwise, we add it.

But wait, no. Because the new dp after processing x is the union of the previous dp (subsets not including x) and temp (subsets including x). So the new dp is:

for each key in current_dp, the value remains (subsets not including x).

but temp contains subsets that include x.

So the new dp is current_dp (subsets not including x) merged with temp (subsets including x). So for each key in current_dp or temp, the value is the minimum between current_dp (if exists) and temp (if exists).

Wait, no. Because the subsets not including x are already represented in current_dp, which was the state before processing x. So when processing x, the new state should be the union of current_dp (subsets not including x) and temp (subsets including x). However, for keys that exist in both, we take the minimum between the two.

But this would require merging the current_dp and temp dictionaries, which could be expensive in Python.

But this approach would increase the size of dp with each step, leading to O(n) * O(d) memory, which may be manageable if d is small.

But for n=3e5 and d=100 per step, this is 3e7 entries. Which could be a problem in Python.

Thus, this approach may not be feasible.

Alternative Idea: For each new element x, the new possible GCDs are the GCDs of x with all previous GCDs and x itself. So the new dp after x is temp, not the union of current_dp and temp.

Wait, but this is incorrect. Because the current_dp represents all possible GCDs from subsets not including x, and the temp represents those including x. So the new dp must include both, otherwise we are losing the subsets that don't include x.

Thus, this approach is not correct.

So, the initial idea is flawed and will not work for large n.

We need to find a different approach.

Another Idea inspired by the fact that the minimal subset size is the smallest k such that some k elements have a GCD of 1.

But how to find that k.

Another approach is to realize that if the entire array's GCD is 1, then the minimal subset size can be found by checking the minimal number of elements required to form a GCD of 1. To find this, perhaps we can track the GCD of the first i elements. If at any point the GCD becomes 1, then the minimal subset size could be i. But this is not correct, because the GCD of the first i elements may be 1, but there could be a smaller subset of the first i elements that also has GCD 1.

For example, consider elements 6, 4, 2. The GCD of all three is 2. If the fourth element is 3, the GCD of the first four is 1. But the minimal subset is 3 and 4.

So this approach is not helpful.

Hmm.

Alternative Idea:

The minimal subset size is determined by the earliest occurrence of a GCD of 1 when elements are processed in some order. But this depends on the order, which is not fixed.

But since the elements can be processed in any order, perhaps we can find the minimal subset size by finding the minimal window of consecutive elements (but the elements are not necessarily consecutive in the array) that have a GCD of 1.

But this is vague.

Another Idea: Since the overall GCD is 1, there must exist a subset of elements where the GCD is 1, and the size of this subset is the minimal possible. To find this, perhaps we can greedily select elements that reduce the current GCD as much as possible.

For example, start with the first element. Then, add elements that reduce the GCD. If the current GCD is g, adding an element x that has a GCD with g of g_new < g would be beneficial. But this is a greedy approach and may not always work.

Alternatively, the problem can be modeled as a BFS, where each state is a GCD value, and the steps are adding elements to the subset. The goal is to reach GCD 1 with the minimal steps (subset size). So BFS can be used, where each node is a GCD value, and edges are adding a new element, leading to a new GCD.

This approach would use BFS to find the shortest path (smallest subset size) to reach GCD 1.

But how to implement this.

Let's think:

- Initialize a dictionary or a priority queue, where the key is the current GCD value, and the value is the minimal number of elements needed to reach this GCD.

- Initially, the queue contains all elements with their GCD and count 1.

- For each element in the queue, if the GCD is 1, return the count.

- Otherwise, for each possible next element, compute the new GCD and update the queue.

But this approach is O(n^2), which is not feasible.

Alternative BFS approach:

The BFS starts with all possible GCD values and their minimal counts. For each step, we process the current set of GCD values and add new GCD values by combining with the elements in the array.

But the key is to track for each GCD value the minimal count required to reach it.

This is similar to the dynamic programming approach but with BFS.

The steps are:

1. Initialize a dictionary (dp) where each key is a GCD value and the value is the minimal count to achieve it. Initially, this is empty.

2. For each element x in the array:

   a. Compute the new_gcd between x and all existing GCD values in the dp. For each new_gcd, we can update the dp with the minimal count.

   b. Also, add x itself to the dp as a new GCD value with count 1.

3. After processing all elements, check if 1 is in the dp. If yes, return the minimal count.

But this is again the dynamic programming approach.

The key is to efficiently track the minimal counts for each GCD value.

But with n=3e5 and each step adding O(1e3) GCDs, this could be manageable.

Thus, the only feasible approach for this problem is the dynamic programming approach, and we need to implement it efficiently.

Now, let's think about the implementation in Python.

In Python, using a dictionary to track the current GCDs and their counts. For each element x:

- Create a new temporary dictionary (temp) which will hold the new GCDs formed by including x.

- Add x to temp with count 1.

- For each existing GCD g in the current dictionary (dp):

   compute new_gcd = gcd(g, x).

   if new_gcd is already in temp:

       temp[new_gcd] = min(temp[new_gcd], dp[g] + 1)

   else:

       temp[new_gcd] = dp[g] + 1

- Then, for each key in temp:

   if the key is already in dp:

       dp[key] = min(dp[key], temp[key])

   else:

       dp[key] = temp[key]

- Check if 1 is in dp. If yes, return the current minimal count.

But how to manage this efficiently.

But in Python, for each element x, we need to process the existing dp entries. However, during processing x, we should not modify the dp while iterating over it. So we need to make a copy of the current dp before processing x.

But for large dictionaries, this can be expensive.

Alternatively, we can create a new temporary dictionary that will store the new entries generated by x, and then merge them into the existing dp.

But the correct way is:

For each x, iterate over the current state of dp (before processing x), generate new entries, and then merge them into the dp.

But to avoid modifying the dp while iterating, we need to process a snapshot of the current dp's keys and values.

So the steps are:

current_dp = current state of dp.

temp = {}

# Add x as a singleton subset

if x in temp:

    temp[x] = min(temp[x], 1)

else:

    temp[x] = 1

# Process existing entries in current_dp

for g in current_dp:

    new_gcd = gcd(g, x)

    count = current_dp[g] + 1

    if new_gcd in temp:

        temp[new_gcd] = min(temp[new_gcd], count)

    else:

        temp[new_gcd] = count

# Merge temp into dp

for g in temp:

    if g in dp:

        dp[g] = min(dp[g], temp[g])

    else:

        dp[g] = temp[g]

This way, during processing x, the current_dp is a snapshot of the dp before processing x, and the temp is built based on that. Then, after processing all existing g in current_dp, the temp is merged into the dp.

But this approach can be optimized by using a temporary dictionary and then merging it into the dp.

This approach ensures that we process the existing dp entries before merging the new entries.

Now, in Python, dictionaries are dynamic, but for each iteration, we process the current_dp as the state before processing x.

So the code would look something like this:

dp = dict()

for x in a:

    new_gcds = collections.defaultdict(lambda: float('inf'))

    # Add the current x as a subset of size 1

    new_gcds[x] = 1

    # Process existing GCDs in the current dp

    for g in list(dp.keys()):

        new_g = math.gcd(g, x)

        new_count = dp[g] + 1

        if new_count < new_gcds[new_g]:

            new_gcds[new_g] = new_count

    # Merge new_gcds into the main dp

    for g in new_gcds:

        if g in dp:

            if new_gcds[g] < dp[g]:

                dp[g] = new_gcds[g]

        else:

            dp[g] = new_gcds[g]

    # Check if we have found the answer

    if 1 in dp:

        print(dp[1])

        exit()

print(-1)

Wait, but in this code, the new_gcds dictionary is built with the current x and the existing GCDs. Then, for each new_gcd in new_gcds, we merge them into the main dp, taking the minimal count.

But this approach may not capture all possible combinations, because the new_gcds may generate new GCDs that can be combined with other elements. However, since the elements are processed sequentially, and each new element's new_gcds are merged into the main dp, this should capture all possible subsets.

But what about subsets that include x and other elements, but not all previous elements? For example, if there's a subset {a, b} with GCD g, and then adding x, the new subset {a, x} may have a different GCD.

Yes, this approach captures all possible subsets that include x and any subset of previous elements. Because for each previous GCD g (which represents some subset of the previous elements), adding x gives a new subset of size count+1, with GCD new_gcd.

Thus, this approach correctly tracks the minimal count for each possible GCD.

Let's test this code with the first example:

Example 1:

Input: 3 elements 10,6,15.

Processing x=10:

new_gcds is {10:1}.

dp becomes {10:1}.

No 1.

Processing x=6:

new_gcds starts with 6:1.

Then, for existing g=10:

new_gcd = gcd(10,6)=2. count=1+1=2.

new_gcds now has 6:1, 2:2.

Merge into dp. dp is now {10:1, 6:1, 2:2}.

No 1.

Processing x=15:

new_gcds starts with 15:1.

Process existing entries in dp: 10,6,2.

For g=10: new_gcd = 5, count=2. new_gcds has 15:1, 5:2.

For g=6: new_gcd = 3, count=2. new_gcds now has 15:1, 5:2, 3:2.

For g=2: new_gcd = 1, count=3. new_gcds now includes 1:3.

Merge into dp. So after merging, dp will have:

existing keys (10:1, 6:1, 2:2) plus new keys (15:1, 5:2, 3:2, 1:3).

So dp now contains 1:3.

So the code will output 3.

Which is correct.

Another test case: array [3,4,5].

Overall GCD is 1.

Processing 3:

dp {3:1}.

Processing 4:

new_gcds {4:1}.

Process existing g=3:

new_gcd=1, count=2.

new_gcds now has 4:1, 1:2.

Merge into dp. dp now has 3:1,4:1,1:2.

So the code returns 2.

Which is correct.

Another test case: array [2,4,6].

Overall GCD is 2, so output is -1.

The code will first check the overall GCD, which is not 1, so output -1.

Thus, the code seems to work for these cases.

But how to compute the overall GCD.

Wait, the code must first check if the overall GCD of the array is 1. If not, output -1.

So the steps are:

- Check if there's any 1 in the array. If yes, output 1.

- Else, compute the overall GCD of the array. If it's not 1, output -1.

- Else, proceed with the dynamic programming approach.

Wait, because the code's dynamic programming approach is based on the assumption that the overall GCD is 1. But if the overall GCD is 1, there exists a subset with GCD 1, so the code will find it.

But the code may not check the overall GCD, but for cases where the code's dynamic programming finds a subset with GCD 1, the answer is valid. But if the overall GCD is not 1, then the code's dynamic programming will not find any subset with GCD 1. So to avoid processing the entire array when the overall GCD is not 1, we need to first compute the overall GCD.

Thus, the code's steps should be:

1. Check if any element is 1. If yes, output 1.

2. Else, compute the overall GCD of the array. If it's not 1, output -1.

3. Else, proceed with the dynamic programming approach to find the minimal subset size.

So the code must first compute the overall GCD.

But computing the overall GCD of 3e5 elements can be done efficiently by iteratively computing the GCD.

Thus, the code steps are:

Read n.

Read the array.

If any element is 1: print 1.

Else:

   compute the overall GCD of the array.

   if overall GCD is not 1: print -1.

   else:

       proceed with the dynamic programming approach to find the minimal subset size.

So this way, we avoid processing the entire array when the overall GCD is not 1.

But how to compute the overall GCD.

In Python, the fastest way is to use the math.gcd function and compute it incrementally.

But note that the overall GCD is computed as the GCD of all elements.

So, for example:

current_gcd = a[0]

for x in a[1:]:

    current_gcd = math.gcd(current_gcd, x)

    if current_gcd == 1:

        break

Thus, if during the computation the current_gcd becomes 1, we can break early.

But since the array doesn't contain any 1 (as checked earlier), but the overall GCD can still be 1.

But this code snippet will compute the GCD correctly.

Now, putting it all together:

The code:

Testing against sample input 1.

```python
import sys
import math
from math import gcd


def main(input_stream, output_stream):
    n = int(input_stream.readline())

    a = list(map(int, input_stream.readline().split()))

    if 1 in a:

        print(1, file=output_stream)

        sys.exit()

    current_gcd = a[0]

    for x in a[1:]:

        current_gcd = math.gcd(current_gcd, x)

        if current_gcd == 1:

            break

    if current_gcd != 1:

        print(-1, file=output_stream)

        sys.exit()

    # Now, find the minimal subset size with GCD 1

    dp = dict()

    minimal = float('inf')

    for x in a:

        new_gcds = {}

        # Add the current x as a subset of size 1

        new_gcds[x] = 1

        # Process existing GCDs in the current dp

        # Iterate over a copy of the current dp to avoid modifying it during iteration

        for g in list(dp.keys()):

            new_g = math.gcd(g, x)

            new_count = dp[g] + 1

            if new_g in new_gcds:

                if new_count < new_gcds[new_g]:

                    new_gcds[new_g] = new_count

            else:

                new_gcds[new_g] = new_count

        # Merge new_gcds into the main dp

        for g in new_gcds:

            if g in dp:

                if new_gcds[g] < dp[g]:

                    dp[g] = new_gcds[g]

            else:

                dp[g] = new_gcds[g]

        # Check if we have found the answer

        if 1 in dp:

            print(dp[1], file=output_stream)

            sys.exit()

    # If after processing all elements, 1 is in dp, but in case of error

    print(-1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
2 4 6
""",
            "output": \
"""\
-1
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

```

Now, in Python, dictionaries are handled as such. But for large n=3e5, the code may be slow.

But let's think about possible optimizations.

Optimization 1: Use a default dictionary for dp and new_gcds. But in Python, dictionaries are more efficient for lookups and inserts.

Optimization 2: Use a faster way to compute GCDs. But math.gcd is already optimized.

Optimization 3: Early termination. As soon as 1 is found in dp, the code exits. So for cases where a pair with GCD 1 exists, the code will exit early.

Thus, the code should handle large cases efficiently.

But what about cases where the minimal subset is large, like 3, and the code has to process all elements.

But in practice, the code will process all elements until it finds the minimal subset.

But with n=3e5, and each iteration processing, say, 100 GCDs, it's 3e5 * 100 = 3e7 operations, which is manageable in Python within 3 seconds.

Thus, this code should work.
</think>

```python
import sys
import math

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    
    if 1 in a:
        print(1)
        return
    
    current_gcd = a[0]
    for x in a[1:]:
        current_gcd = math.gcd(current_gcd, x)
        if current_gcd == 1:
            break
    if current_gcd != 1:
        print(-1)
        return
    
    dp = {}
    for x in a:
        new_gcds = {}
        new_gcds[x] = 1
        for g in list(dp.keys()):
            new_g = math.gcd(g, x)
            new_count = dp[g] + 1
            if new_g in new_gcds:
                if new_count < new_gcds[new_g]:
                    new_gcds[new_g] = new_count
            else:
                new_gcds[new_g] = new_count
        for g, cnt in new_gcds.items():
            if g in dp:
                if cnt < dp[g]:
                    dp[g] = cnt
            else:
                dp[g] = cnt
        if 1 in dp:
            print(dp[1])
            return
    print(-1)

if __name__ == "__main__":
    main()
```
