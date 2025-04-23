<think>
Okay, let's see. The problem is about finding the maximum satisfaction Kefa can get by choosing m dishes out of n, without repeating any. And there are these k rules that give extra satisfaction if a dish x is immediately followed by y. The challenge is to model this optimally considering the constraints.

Hmm. So the constraints are n up to 18, m up to 18. Wait, when m is up to 18 and n is 18, that's manageable with dynamic programming (DP) that tracks the state of selected dishes and the last dish chosen. Because for each state, you need to track the last dish to account for the rules. 

The DP approach here would be a state represented by a bitmask (to track which dishes have been selected) and the last dish. Since n is 18, the bitmask can be 18 bits, which is 2^18 = 262,144 possible masks. And for each mask, we track the last dish (up to 18 possibilities). So the total number of states is 18 * 2^18. Let's compute that: 18 * 262,144 = 4,718,592. That's manageable, even for Python, considering each state transitions to possible next dishes.

Each state transition would involve adding a new dish that's not already in the mask. For each possible next dish, we calculate the new satisfaction by adding the dish's a_i plus any rules that apply if the previous dish was x and the next is y. 

So the steps would be:

1. Preprocess the rules into a dictionary where for a pair (x, y), we can quickly look up the value c. So we can have a 2D array, say, adj[x][y] = c. This way, when transitioning from a state with last dish x to adding y, we can add adj[x][y] if it exists.

2. Initialize the DP table. The initial state is when no dishes are selected (mask 0), but that's a bit tricky. Wait, no. Wait, for each possible starting dish (when mask has only one bit set), the DP value is a_i of that dish. Then, for each step, we build up the mask by adding dishes one by one, tracking the last dish.

Wait, the mask will represent the set of dishes selected so far. For a mask with exactly one dish, the last dish is that one, and the satisfaction is a_i of that dish.

For each state (mask, last), the DP value is the maximum satisfaction achievable by selecting those dishes in mask and ending with 'last'. 

So the transitions would be:

For each state (mask, last), and for each possible next dish 'next' not in mask, compute the new mask (mask | (1 << (next-1))), and the new satisfaction would be dp[mask][last] + a[next] + (the rule value if last is connected to next). 

The maximum of all these possibilities is stored in the new state.

We need to track for masks of size 1, 2, ..., m. So once we've built up the DP for all masks of size m, we take the maximum among all those states.

Yes, that makes sense. 

Now, considering the time constraints. Let's see. For each state, how many transitions do we have? For a mask with t dishes selected, there are (n - t) possible next dishes. So for each state (mask, last), we iterate over all possible next dishes not in the mask. The total number of transitions would be sum over all masks (number of possible next dishes) multiplied by the number of possible last dishes per mask.

But even with 4.7 million states, each with up to 18 transitions (since after each step, the number of possible next dishes decreases), the total operations would be roughly 18 * 4.7e6 = ~85 million. That's acceptable for Python, especially with optimized code using bitmask operations and precomputed adjacency matrices.

The key is to precompute the adjacency rules, so that for any transition from last to next, we can quickly get the added c value.

So the plan is:

- Read n, m, k.

- Read a list, which is 1-based? Or 0-based? The dishes are numbered from 1 to n in the input.

Probably, we can index them 0-based in the code for easier handling.

Wait, no. Let's see. The input for the rules uses xi and yi as 1-based. So perhaps in the code, it's easier to keep them as 1-based. So when building the adjacency matrix, we can have a 2D array (n+1) x (n+1), where adj[x][y] = c. So for x in 1..n and y in 1..n.

Then, when transitioning from last dish x (1-based) to next dish y (1-based), we check adj[x][y] and add c if present.

So, the steps:

Initialize a DP table, which can be a dictionary or a 2D array. But since n is 18, and masks are 18 bits, perhaps using a list of dictionaries or a 2D array where dp[mask][x] is the maximum satisfaction for that mask and last dish x.

But in Python, using a dictionary for each mask might be slow. So perhaps use a list of lists. For each mask, a list of size (n+1) (since dishes are 1-based to n) where each element represents the maximum satisfaction when the last dish is x. However, masks can be represented as integers, and for each mask, we need to track the last dish. 

Wait, but for mask in binary, each bit represents whether the dish is selected. So for a mask, the number of set bits is the number of dishes selected so far. So for each step, we can iterate through all possible masks with t bits set, and process them.

But how to manage the DP storage. For each mask, we can store a dictionary where keys are the last dish (from 1 to n) and the value is the maximum satisfaction for that state. Alternatively, for each mask, an array of size n+1 (indexes 0..n) where each entry is the maximum satisfaction for that last dish.

But considering that n is up to 18, each mask can have a list of 18 elements (since dishes are numbered 1..n). So for mask in 0 to 2^18-1, and for each x in 1..n, check if x is in the mask (bit is set). If the mask is 0, then no dishes are selected. But that's only the initial state. Wait, no. Because the mask represents the set of dishes selected. So for mask with exactly one bit set, we have one dish selected. 

So the initial states are all masks with exactly one bit set. For each such mask, the last dish is the one that's set, and the satisfaction is a_i of that dish. Then, for each mask with t dishes, we process transitions to masks with t+1 dishes.

So the DP can be initialized as follows:

For all x in 0..n-1 (if 0-based), but perhaps better to use 1-based:

For each dish x (1-based), create a mask with only x set. The DP[mask][x] = a[x-1] (since a is 0-based in the input). 

Wait, input for a is given as a list of n numbers. The first line after n, m, k is n space-separated numbers a1 ... an. So a is 0-based in the list, but x and y in the rules are 1-based. So in code:

a = list of a1, a2,... an. So a[0] is the a1 of the problem? Wait, no. Wait, the problem's second line is "n space-separated numbers ai (0 ≤ ai ≤ 1e9) — the satisfaction he gets from the i-th dish." So the first element is a_1, which corresponds to dish 1. So dish x in 1-based.

So in code, the array a is 0-based, but the first element is for dish 1, which is a bit confusing. Wait, no. Let's recheck:

No, wait. For example, in the first sample input:

2 2 1

1 1

The dishes are 1 and 2. Their a values are 1 and 1. The rule is 2 followed by 1 gives +1. So the maximum is 1 (dish 2) + 1 (dish 1) + 1 (rule) = 3. So the a list in code would be [1, 1], but dish 1 is index 0, and dish 2 is index 1. So when dish x is 2, the a[x-1] would be a[1], which is correct.

So for each x in 1..n, a[x-1] is the satisfaction.

So in code, the a list is 0-based, but the rules are 1-based for x and y. So for x in the rules, we have to check.

So, the adjacency matrix can be a 2D array where adj[x][y] = c for x and y from 1 to n.

So the plan is:

- Read n, m, k.

- Read a list of n numbers.

- Read k rules, and build adj[x][y] = c. Since each (x, y) is unique, we can just store them in a dictionary or a 2D array.

- Initialize DP. For each possible mask with exactly one dish (so each x from 1 to n), the mask is 1 << (x-1), and the DP value is a[x-1].

- Then, for masks with size from 2 to m:

   For each mask in the DP with size s (s < m), iterate through all possible last dishes (y) in that mask. Then, for each possible next dish (z) not in the mask, compute new_mask = mask | (1 << (z-1)). Then, the new DP value for new_mask and last dish z is the current DP[mask][y] + a[z-1] + adj[y][z] (if the rule exists). We take the maximum over all possible transitions.

- After processing all masks up to size m, collect all DP values for masks with exactly m dishes and take the maximum among all their possible last dishes.

So the key is to manage the DP efficiently. Let's think about how to represent the DP. Since in Python, a dictionary of dictionaries might be too slow for 4.7 million states. So perhaps using a list of arrays where for each mask, we have an array of size n+1 (indexes 0 to n), but in practice, for each mask, only the dishes present in the mask can have a value. But even that, with 2^18 masks and 18 entries each, it's manageable.

Wait, but for each mask, the possible last dishes are those in the mask. So for a mask, the number of possible last dishes is the number of set bits in the mask. So for each mask, we can track a list of possible last dishes, and their maximum values.

But how to structure this in code. Maybe using a dictionary where the key is the mask, and the value is another dictionary (last_dish: value). But with mask being up to 2^18, even with that, the masks can be stored as integers. But in Python, dictionaries have some overhead. So perhaps using a list of dictionaries, where the index is the mask. But 2^18 is 262,144, which is manageable. Wait, but 2^18 is 262,144 masks. So a list of size 2^18, where each element is a dictionary (key: last dish, value: satisfaction). But for each mask, the dictionary entries are only for the dishes present in the mask. 

Alternatively, for each mask, we can have a list of size n, where each entry is -infinity or the maximum satisfaction for that last dish. But since for a mask, the possible last dishes are those present in the mask, the list would have entries only for those positions. But for code efficiency, perhaps pre-initialize for each mask an array of size (n+1) where each entry is the maximum value for that last dish. But since n is 18, the array is 18 elements per mask. So for 2^18 masks, 18 elements each: 4.7 million entries total. Which is manageable as a list of lists.

But in Python, even 4.7 million entries might be a bit heavy for memory. Let's see: each entry is a number, which could be a 64-bit integer. 4.7 million entries would take about 38 MB (since each 64-bit integer is 8 bytes). That's manageable within the memory constraints.

So perhaps we can represent the DP as a list of dictionaries, where each mask's dictionary holds the maximum satisfaction for each possible last dish. But given that n is up to 18, even using a list of lists where each list is of length n+1 (for 0 to n) is possible. Wait, but the dishes are 1-based. So for each mask, the DP for last dish 0 would be unused. So perhaps the DP is a list where each element is an array of size (n+1), but only indices 1..n are used.

Alternatively, for each mask, store a dictionary with keys as the possible last dishes (which are in the mask) and values as the maximum satisfaction. This would be more memory-efficient since for a mask with t dishes, the dictionary has t entries. But for the worst case (mask with all 18 dishes), it's 18 entries. So total entries would be up to 18 * 2^18 = 4.7 million, each stored as a key-value pair. In Python, each dictionary entry is some overhead, but perhaps manageable.

But in practice, for speed, using a list of lists might be better. Let's say we pre-initialize a 2D array where for each mask, and each dish x, we track the maximum satisfaction. The initial state for masks with one dish x is a[x-1]. For other masks, the values are set to -infinity initially, and then updated as needed.

So the steps in code:

Initialize a DP array where dp is a list of size 2^18, each element is a list of size (n+1) (since dishes are 1-based). For each mask, dp[mask][x] is the maximum satisfaction when the mask is 'mask' and the last dish is x.

Initialize all dp[mask][x] to -infinity.

Then, for each dish x (1-based), set dp[1 << (x-1)][x] = a[x-1].

Then, for all masks in order of increasing number of bits (from 1 to m-1), iterate through all possible x (last dishes) in the mask. For each x, if dp[mask][x] is not -infinity, then for each possible next dish y not in the mask:

new_mask = mask | (1 << (y-1))

new_value = dp[mask][x] + a[y-1]

if there's a rule from x to y, add adj[x][y] to new_value.

Then, if this new_value is larger than the current dp[new_mask][y], update dp[new_mask][y] to new_value.

After processing all possible transitions, the answer is the maximum value among all masks with exactly m bits set, and all possible x in those masks.

So the code steps:

Read n, m, k.

Read a as list of integers (0-based in the list, but 1-based in the problem).

Read k rules and build the adjacency matrix. adj is a 2D array of size (n+1) x (n+1), initialized to 0, then for each rule, adj[x][y] += c.

Wait, no. Because each rule is unique (xi, yi), so for each (x, y), there's exactly one rule. So adj[x][y] can be directly set to c. So:

adj = [[0]*(n+1) for _ in range(n+1)]

for each rule:

    x, y, c = map(int, input().split())

    adj[x][y] = c  # since the rules are unique, no duplicates.

Then, precompute all possible masks and transitions.

Now, the DP:

Initialize max_bits = m.

We can precompute all masks in order of the number of bits set, so that we process masks with 1 bit, then 2 bits, up to m bits. This is more efficient because each transition from a mask with s bits to s+1 bits.

So, for each s in 1 to m-1:

   for all masks with s bits set:

       for each x in 1..n where (mask & (1 << (x-1))) != 0 and dp[mask][x] != -infinity:

           for each y in 1..n where (mask & (1 << (y-1))) == 0:

               new_mask = mask | (1 << (y-1))

               new_val = dp[mask][x] + a[y-1] + adj[x][y]

               if new_val > dp[new_mask][y]:

                   dp[new_mask][y] = new_val

But this approach may be time-consuming because for each x in the mask, we have to iterate all possible y not in the mask. However, since the code is in Python, and considering that n is 18, for each x in the mask (up to 18), and for each possible y not in the mask (up to 18 - s), but s can be up to m-1 (up to 17). So for s=1, each mask has 1 x, and 17 possible y. So for each mask of s=1, 1*17 transitions. For s=17, each mask has 17 x, and 1 possible y, so 17*1 transitions. So overall, the number of transitions is manageable.

But in Python, for loops can be slow. So how can we optimize this?

Alternative approach: Precompute for all possible masks with s bits, iterate through each x in the mask, and for each y not in the mask.

But how to efficiently iterate over all y not in the mask?

In Python, for a given mask, the y's not in the mask can be found by (all possible y's where (mask & (1 << (y-1))) == 0). So for y in 1..n, if (mask & (1 << (y-1))) is 0.

So in code, for a given mask and x:

for y in range(1, n+1):

    if not (mask & (1 << (y-1))):

        ... process y.

But checking this for all y in 1..n each time may be time-consuming. But n is 18, so for each transition, it's 18 checks.

Alternatively, precompute for each mask the list of possible y's not in the mask. But for each mask, this list can be generated on the fly.

In Python, bitmask operations are fast, so checking if (mask & (1 << (y-1))) is zero for each y is manageable.

Now, the code:

We'll need to create a DP array. Since Python's default list creation for 2^18 elements is possible, but 2^18 is 262,144. For each of these, an array of n+1 elements (n=18, so 19 elements per mask) would be 262,144 * 19 = ~5 million elements. Each element can be initialized to -infinity.

In Python, using a list of lists:

max_mask = 1 << n

dp = [ [-inf]*(n+1) for _ in range(max_mask) ]

Then, for each x in 1..n:

mask = 1 << (x-1)

dp[mask][x] = a[x-1]

Then, for each mask in all possible masks with s bits, for s from 1 to m-1:

But how to iterate through masks in order of increasing number of bits. One way is to precompute for each s, the list of masks with s bits. But for n=18, this can be done with combinations. However, generating all combinations for each s might be time-consuming. Alternatively, iterate through all masks, check the number of bits, and process them in order.

But that's O(2^18) masks each time. Which is 262k per s. For m up to 18, s from 1 to 17: total 17*262k = 4.4 million. Which is manageable.

So in code:

from itertools import combinations

But perhaps a better way is to iterate all masks, and for each mask, count the number of set bits, and process them in order.

So:

for s in range(1, m):

    for mask in all_masks_with_s_bits:

        for x in 1..n:

            if mask has x set and dp[mask][x] != -infinity:

                for y in 1..n:

                    if y not in mask:

                        new_mask = mask | (1 << (y-1))

                        new_val = dp[mask][x] + a[y-1] + adj[x][y]

                        if new_val > dp[new_mask][y]:

                            dp[new_mask][y] = new_val

But how to get all masks with s bits? It's possible to generate them using combinations. For example, for s bits, generate all possible combinations of s dishes, then create the mask by ORing their bits. For n=18, generating combinations of s elements would take O(18 choose s) time. For s=9, 18 choose 9 is 48,620. For s=17, 18 choose 17 is 18. So this is manageable.

So for each s from 1 to m-1:

   generate all combinations of s elements from 1..n (but note that the dishes are 1-based here), and for each combination, create the mask by ORing 1<<(x-1) for each x in the combination.

   for each such mask:

       for x in the combination (since x is part of the mask):

           if dp[mask][x] is not -infinity:

               for y not in the combination:

                   compute new_mask, new_val, and update dp[new_mask][y] if better.

This approach could be more efficient as it directly generates masks with exactly s bits and loops through all x in the combination.

But generating all combinations for each s is O(18 choose s), which for s up to 17 is manageable.

So in code:

for s in range(1, m):

    # Generate all masks with s bits set

    for dish_indices in combinations(range(1, n+1), s):

        mask = 0

        for x in dish_indices:

            mask |= 1 << (x-1)

        # For each x in dish_indices (possible last dishes)

        for x in dish_indices:

            current_val = dp[mask][x]

            if current_val == -inf:

                continue

            # For each possible y not in dish_indices:

            for y in range(1, n+1):

                if y not in dish_indices:

                    new_mask = mask | (1 << (y-1))

                    added = adj[x][y]

                    new_val = current_val + a[y-1] + added

                    if new_val > dp[new_mask][y]:

                        dp[new_mask][y] = new_val

But wait, in the code above, checking if y is not in dish_indices can be done via (mask & (1 << (y-1))) == 0. Because dish_indices is the list of dishes in the mask, so the mask is built from those. So in code, for a given y, if (mask & (1 << (y-1))) == 0, then y is not in the mask.

So the code can be optimized to:

for s in range(1, m):

    for mask in all_masks_with_s_bits:

        for x in 1..n where (mask has x set):

            if dp[mask][x] is not -infinity:

                for y in 1..n:

                    if (mask & (1 << (y-1))) == 0:

                        new_mask = mask | (1 << (y-1))

                        new_val = dp[mask][x] + a[y-1] + adj[x][y]

                        if new_val > dp[new_mask][y]:

                            dp[new_mask][y] = new_val

But generating all masks with s bits is expensive. So using combinations might be better.

Alternatively, use the built-in function to iterate through all masks with s bits set.

But for Python, using itertools.combinations is manageable.

But wait, when we generate combinations of s dishes, each combination is a tuple of s elements. For each combination, the mask is the OR of 1 << (x-1) for x in the combination. Then, for each x in the combination, check if that x is the last dish. However, in the DP, the mask's possible last dishes are all dishes in the mask. So for each combination, the mask has exactly s bits set, and for each x in the combination, we check if the current value is valid (not -infinity).

But when you generate combinations, the same mask can be generated multiple times if the order is different, but since combinations are sorted, each combination is unique and the mask is unique. For example, combinations (1,2) and (2,1) are not generated by itertools.combinations; itertools returns them in sorted order. So for each combination, the mask is unique.

Wait, itertools.combinations returns elements in sorted order, so each combination is a unique tuple of elements in increasing order. So for a mask with bits 1 and 2 set, the combination will be (1, 2), which generates mask 0b11. So for each mask with s bits, combinations will generate exactly one combination. So the code above would process each mask exactly once.

But in code, when s=2, and the combination is (1,2), the code will process x as 1 and 2. But in the DP, the last dish could be either 1 or 2. So the code will process both possibilities.

This approach seems correct.

But what about the order of processing masks? For example, when s=2, the code processes all masks with two bits. Then, for each x in those masks (possible last dishes), transitions to masks with s+1 bits.

This approach is correct.

But generating the combinations for each s may be time-consuming for s up to 17, but given that n is 18, and s is up to m-1 (m up to 18), this is manageable.

Alternatively, for each mask in all possible masks, check how many bits are set and process them in order. Let's think.

We can loop through all masks from 1 to (1<<n) -1. For each mask, count the number of set bits. If the count is s, and we are processing masks for s bits in order, then process them when s is in 1 to m-1.

But how to process them in order of increasing s. For example, first process all masks with 1 bit, then 2 bits, etc.

In code:

for mask in range(1, 1 << n):

    s = bin(mask).count('1')

    if s >= m:

        continue

    for x in 1..n:

        if (mask & (1 << (x-1))) == 0:

            continue

        if dp[mask][x] == -inf:

            continue

        for y in 1..n:

            if (mask & (1 << (y-1))) == 0:

                new_mask = mask | (1 << (y-1))

                new_val = dp[mask][x] + a[y-1] + adj[x][y]

                if new_val > dp[new_mask][y]:

                    dp[new_mask][y] = new_val

But this approach requires iterating through all masks, which is 2^18 = 262k masks. For each mask, checking the number of bits is O(1) in Python (using bin(mask).count('1')), but bin is a string conversion which is O(n) time. Wait, for 18 bits, it's acceptable.

But in the worst case, for each mask, we check s and proceed. If s is not in the range [1, m-1], we skip. So for m=18, all masks with s up to 17 are processed. The number of masks processed would be sum_{s=1}^{17} C(18, s) = 2^18 -1 - C(18, 18) = 262143 -1 = 262142. So similar to the previous approach.

But in code, this approach may be faster because it avoids generating combinations and uses bitmask operations, which are fast in Python. So perhaps this approach is better.

So the code can be:

Initialize dp as before.

For each mask from 0 to (1 << n) -1:

    s = bin(mask).count('1')

    if s == 1:

        x = the dish in the mask (since s is 1)

        dp[mask][x] = a[x-1]

    elif s >= 1 and s < m:

        # process transitions

        for x in 1..n:

            if (mask & (1 << (x-1))) == 0:

                continue

            current_val = dp[mask][x]

            if current_val == -inf:

                continue

            for y in 1..n:

                if (mask & (1 << (y-1))) != 0:

                    continue

                new_mask = mask | (1 << (y-1))

                added = adj[x][y]

                new_val = current_val + a[y-1] + added

                if new_val > dp[new_mask][y]:

                    dp[new_mask][y] = new_val

But this approach is more straightforward. But how to iterate through x in the mask. For each mask, for x in 1..n, check if x is present. So for each mask, for x in 1..n:

if mask has x set, then proceed.

But for mask with s bits, this is O(n) per mask. For n=18 and 262k masks, this is 4.7 million checks, which is manageable.

So perhaps this is the way to go.

So in code, the main loop is:

for mask in range(1, 1 << n):

    s = bin(mask).count('1')

    if s > m:

        continue

    if s == 0:

        continue

    for x in range(1, n+1):

        if not (mask & (1 << (x-1))):

            continue

        current_val = dp[mask][x]

        if current_val == -inf:

            continue

        # iterate over all possible y not in mask

        for y in range(1, n+1):

            if mask & (1 << (y-1)):

                continue

            new_mask = mask | (1 << (y-1))

            added = adj[x][y]

            new_val = current_val + a[y-1] + added

            if new_val > dp[new_mask][y]:

                dp[new_mask][y] = new_val

But this code is O( (1<<n) * n * n ), which for n=18 is 262,144 * 18 * 18 = 84,934,656 operations, which is manageable in Python.

But wait, for s >= m, we don't process them. Because when s is the number of bits in mask, and we are processing transitions from s to s+1. So when s >= m, we can skip.

But in the code, we have 'if s > m: continue'. Wait, because s can be up to m-1. For example, when s is m-1, processing transitions to s+1 = m. But since m is up to 18, and the maximum s processed is m-1.

So the code should process all masks with s from 1 to m-1. So the condition 'if s > m' is not correct. It should be 'if s >= m'? Because when s is m, then transitions would be to m+1, which is beyond m. So for the code, masks with s >= m can be skipped.

Wait, but the code processes transitions from a mask with s bits to s+1 bits. For example, when s is m-1, transitions to s+1 = m. So masks with s bits from 1 to m-1 need to be processed.

So the condition should be 'if s >= m: continue', to skip masks with s >= m.

So in code:

if s >= m:

    continue

So masks with s >= m are skipped.

Thus, the code will process all masks with s from 1 to m-1. For each such mask, for each x in the mask, and for each y not in the mask, transitions to new_mask with s+1 bits.

But the code for initializing the DP for masks with s=1 is covered by this loop. Because when s=1, mask is a single bit. So the code will process the mask, x is the single dish in the mask, and transitions to s=2.

Thus, the code is correct.

Now, the answer is the maximum value in all masks with exactly m bits, and for each x in those masks, dp[mask][x].

So after processing all transitions, collect all masks with exactly m bits set, and for each, collect the maximum dp[mask][x] for x in the mask.

In code:

max_result = 0

for mask in range(1, 1 << n):

    s = bin(mask).count('1')

    if s != m:

        continue

    current_max = max( [ dp[mask][x] for x in range(1, n+1) if (mask & (1 << (x-1))) ] )

    if current_max > max_result:

        max_result = current_max

print(max_result)

But to compute current_max, for each mask, we need to check all x in the mask and take the maximum.

But in code, since in Python, it's possible to loop through the x's in the mask.

But for each mask with m bits, looping through all x in 1..n and checking if x is in the mask can be done efficiently.

Alternatively, precompute the list of x's in the mask:

But for each mask, the x's are those where (mask & (1 << (x-1))) != 0.

So in code:

max_result = -inf

for mask in range(1, 1 << n):

    if bin(mask).count('1') != m:

        continue

    # Get all x in mask

    for x in range(1, n+1):

        if mask & (1 << (x-1)):

            if dp[mask][x] > max_result:

                max_result = dp[mask][x]

print(max_result)

But even this loop is O( (1<<n) * n ), which for n=18 and m=18, the masks with m bits are C(18, 18) = 1. So the loop is manageable.

But when m is 18, the code checks only mask (1<<18) -1, and for x in 1..18. So it's O(1) for that case.

Thus, the code should work.

Now, let's test this approach with the sample inputs.

Sample Input 1:

2 2 1

1 1

2 1 1

In this case, the adjacency matrix has adj[2][1] = 1.

The DP initialization for masks with 1 bit:

mask 0b10 (dish 2), dp[0b10][2] = 1.

mask 0b1 (dish 1), dp[0b1][1] = 1.

Then, processing masks with s=1:

For mask 0b10 (s=1), x=2:

for y=1 (not in mask):

new_mask is 0b11. new_val is 1 (current_val) + a[0] (dish 1) + adj[2][1] (1) → 1 + 1 +1 = 3.

So dp[0b11][1] = 3.

For mask 0b1 (x=1), for y=2:

new_val is 1 (a[0]) + a[1] (1) + adj[1][2] (0) → 1+1+0=2. So dp[0b11][2] = 2.

So the masks with s=2 (m=2) have:

mask 0b11, x can be 1 or 2. The maximum is 3.

Sample Output is 3. Correct.

Sample Input 2:

4 3 2

1 2 3 4

2 1 5

3 4 2

So the dishes are 1,2,3,4 with a = [1,2,3,4].

adj[2][1] =5, adj[3][4] =2.

We need to choose 3 dishes. The maximum is 4 + 2 +1 +5 = 12.

Wait, in the example, the best sequences are 4,2,1 or 2,1,4. Let's see:

For 4,2,1:

a[3] (4) + a[1] (2) + a[0] (1) → 4+2+1=7.

Plus the rule 2→1 (5). So total 7+5=12.

Similarly, 2→1→4:

a[1] (2) + a[0] (1) + a[3] (4) → 7.

Plus the rule 2→1 (5) → total 12.

So the maximum is 12.

Let's see how the DP handles this.

For masks of size 3:

The best mask is probably 2,1,4. The mask would be 1<<1 | 1<<0 | 1<<3 → 0b1001 (dish 1 is 0th bit? Wait, no. Wait, dishes are 1-based in the code. So dish 1 is represented by 1<<0, dish 2 by 1<<1, etc.

So mask for dishes 1,2,4 is 0b1011 (binary) which is 1 + 2 + 8 = 11. Or wait, the mask is dishes 2 (bit 1), 1 (bit 0), 4 (bit 3) → 0b1011 (binary 11). 

But for the transition, when the last dish is 2 (bit 1), then adding 1 (bit 0) would get the rule. Then adding 4 (bit 3) would not get any rule. 

But in the code, the transitions are built step by step.

This seems correct, but the code should find the maximum of 12.

Thus, the code should work.

Now, the code in Python:

Implementing the approach.

But note that in Python, integers can be as big as needed, so no overflow issues.

The code steps:

Read n, m, k.

Read a as list of integers.

Read k rules, and fill adj matrix.

Initialize the DP.

Then loop through all masks, process transitions.

Finally, collect the maximum for masks with m bits.

But in Python, using a list of lists for the DP.

But for n=18, 2^18 masks is 262,144. So the DP will be a list of 262,144 elements, each a list of n+1 elements (19 elements). Each initialized to -infinity.

But initializing this in Python can be done as:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    INF = float('-inf')

    n, m, k = map(int, input_stream.readline().split())

    a = list(map(int, input_stream.readline().split()))

    adj = [[0]*(n+1) for _ in range(n+1)]

    for _ in range(k):

        x, y, c = map(int, input_stream.readline().split())

        adj[x][y] = c

    max_mask = 1 << n

    dp = [ [INF]*(n+1) for _ in range(max_mask) ]

    # Initialize masks with one dish.

    for x in range(1, n+1):

        mask = 1 << (x-1)

        dp[mask][x] = a[x-1]

    # Process all masks in order.

    for mask in range(1, max_mask):

        s = bin(mask).count('1')

        if s >= m:

            continue

        for x in range(1, n+1):

            if not (mask & (1 << (x-1))):

                continue

            current_val = dp[mask][x]

            if current_val == INF:

                continue

            # Iterate all possible y not in mask.

            for y in range(1, n+1):

                if mask & (1 << (y-1)):

                    continue

                new_mask = mask | (1 << (y-1))

                new_val = current_val + a[y-1] + adj[x][y]

                if new_val > dp[new_mask][y]:

                    dp[new_mask][y] = new_val

    # Find the maximum value among masks with m dishes.

    max_result = INF

    for mask in range(max_mask):

        if bin(mask).count('1') != m:

            continue

        for x in range(1, n+1):

            if mask & (1 << (x-1)):

                if dp[mask][x] > max_result:

                    max_result = dp[mask][x]

    print(max_result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 3 2
1 2 3 4
2 1 5
3 4 2
""",
            "output": \
"""\
12
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

Sample 2:

The code should find the maximum of 12.

Thus, the code should handle both cases correctly.

Now, for memory optimization: The DP is a list of max_mask elements, each a list of n+1 integers. Each entry is a 64-bit integer. For Python, each integer is stored as an object, which may use more memory. However, given that 262k * 19 = ~5 million entries, and each entry is a float (in this case, since we use INF which is float), but for Python, even that should be manageable within 256MB. Because 5 million * 4 bytes (assuming 32-bit floats) is 20MB, but Python uses more, but likely still acceptable.

Alternatively, using integers instead of floats. Since the initial a[x-1] can be up to 1e9, and with up to 18 steps, each adding up to 1e9 + 1e9 (from rules), the total can be up to 3e10 * 18 = 5.4e11, which fits in Python's integer type.

But in the code, INF is set to float('-inf'). So the initial DP is filled with float('-inf'), but when the values are updated to integers (like 1, 3, etc.), but in Python, integers and floats can coexist. So the code should work.

Thus, the code should be correct and efficient.
</think>

```python
import sys

def main():
    INF = float('-inf')
    n, m, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    adj = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(k):
        x, y, c = map(int, sys.stdin.readline().split())
        adj[x][y] = c
    
    max_mask = 1 << n
    dp = [ [INF] * (n + 1) for _ in range(max_mask) ]
    
    for x in range(1, n + 1):
        mask = 1 << (x - 1)
        dp[mask][x] = a[x - 1]
    
    for mask in range(1, max_mask):
        s = bin(mask).count('1')
        if s >= m:
            continue
        for x in range(1, n + 1):
            if not (mask & (1 << (x - 1))):
                continue
            current_val = dp[mask][x]
            if current_val == INF:
                continue
            for y in range(1, n + 1):
                if mask & (1 << (y - 1)):
                    continue
                new_mask = mask | (1 << (y - 1))
                new_val = current_val + a[y - 1] + adj[x][y]
                if new_val > dp[new_mask][y]:
                    dp[new_mask][y] = new_val
    
    max_result = INF
    for mask in range(max_mask):
        if bin(mask).count('1') != m:
            continue
        for x in range(1, n + 1):
            if mask & (1 << (x - 1)) and dp[mask][x] > max_result:
                max_result = dp[mask][x]
    
    print(max_result)

if __name__ == "__main__":
    main()
```
