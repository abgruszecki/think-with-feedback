<think>
Okay, let's tackle this problem. Hmm. So the problem is to choose for each a_i a b_j such that when we compute all the a_i & b_j's, the OR of all those results is minimized. Oh right, the goal is the minimal possible OR of all c_i's.

First, I need to understand how the OR works here. The OR accumulates all the set bits. So once a bit is set in any c_i, it will be present in the final result. To minimize the OR, we want as few bits set as possible. So the best case is when all c_i's are zero, which would make the OR zero. But that's only possible if for every a_i, there's a b_j such that a_i & b_j is zero. Otherwise, we have to set some bits.

The approach here might be to check possible candidate answers and see if they can be achieved. Since the maximum possible bit is up to 2^9 (since a_i and b_j are up to 2^9-1), the maximum possible OR is up to 2^9-1 = 511. So the possible answers are between 0 and 511.

So the plan is to check each possible candidate OR value from 0 upwards. For each candidate 'mask', we check if it's possible to select b_j's for each a_i such that all the c_i's (a_i & b_j) OR together to the mask. The smallest such mask is the answer.

Wait, but how do we check if a given mask is possible? For each a_i, we need to find at least one b_j such that (a_i & b_j) | mask_candidate == mask_candidate. Because when you OR all c_i's, they can't set any bit that's not set in the mask. So each c_i must be a subset of the mask's bits. So for each a_i, there must exist some b_j where (a_i & b_j) is a subset of the mask. Then, when OR'ed together, their union is the mask (or possibly a subset, but since we're trying to find the minimal mask, we need the mask to be the union).

Wait, no. The mask is the candidate, but the actual OR could be a subset of it. Wait, no. Because the candidate is the OR of all c_i's. So if we pick a candidate mask, then the actual OR after choosing the c_i's must be exactly mask. But since we want the minimal possible OR, maybe we can check for each possible mask (starting from 0 upwards) whether there's a way to select the c_i's such that their OR is at most the mask. Wait, but how?

Alternatively, here's a better way: For a given mask, can we choose for each a_i a b_j such that the OR of all (a_i & b_j) is a subset of the mask, and the OR of all those is exactly the mask. Wait, maybe not. Maybe the candidate mask is the minimal possible. So when we check a mask, we need to see if for all a_i, there exists a b_j where (a_i & b_j) has bits that are a subset of the mask. Because then when OR'ed all together, the total OR would be the union of all their bits. So if the candidate mask is the minimal possible, then the OR would be exactly the union. So to find the minimal mask, we can check all possible masks in increasing order. For each mask, check if for every a_i there exists a b_j such that (a_i & b_j) & (~mask) is zero (i.e., all set bits in (a_i & b_j) are in the mask). Then, the OR of all such c_i's would be a subset of mask. However, the minimal mask would be the minimal such mask where this is possible, and also, the union of all c_i's is exactly the mask. Wait, but how do we ensure that the union is exactly the mask? Because maybe the actual OR is a subset of the mask, which is even smaller. So perhaps the approach is to check whether there exists a mask such that all a_i can have a c_i that is a subset of the mask, and the OR of all c_i's is the mask. But this seems complicated.

Alternatively, perhaps the correct approach is to iterate the possible masks in order from 0 to 511. For each mask, check if for every a_i, there exists a b_j such that (a_i & b_j) is a subset of the mask (i.e., (a_i & b_j) & ~mask) == 0. If this is true for all a_i, then we can choose those b_j's, and the OR of all c_i's will be the union of their bits, which could be up to mask. But the mask might be higher than necessary. Wait, but the OR of all c_i's could be less than the mask. However, since we are iterating from 0 upwards, the first mask where such a selection exists would be the minimal possible OR. Because even if the actual OR is lower than the mask, the mask is the upper bound, but since we check in order, the first valid mask would be the minimal possible.

Wait, no. Let's think. Suppose the actual OR is X, which is less than the mask. Then, when we check mask = X, the check would pass (since for each a_i, there's a b_j that allows c_i to be a subset of X, and the OR is X). So when we check masks in order, starting from 0, the first mask for which the check passes (i.e., all a_i can choose a b_j that their c_i is a subset of the mask) will be the minimal possible OR. Because if the actual OR is X, then mask X would pass, and if X is the minimal possible, then the first mask in the iteration that passes is X.

So the algorithm is:

- Iterate mask from 0 to 511 in increasing order.
- For each mask, check if for every a_i in a, there exists a b_j in b such that (a_i & b_j) & (~mask) == 0. (Which is equivalent to (a_i & b_j) | mask == mask, but perhaps easier to compute as (a_i & b_j) OR mask is mask, which is the same as (a_i & b_j) is a subset of mask.)
- The first mask for which this condition is true is the minimal possible OR. So we return that mask.

Yes, that makes sense. Because once the condition is true, it's possible to select for each a_i a b_j such that each c_i's bits are subset of the mask. Then the OR of all c_i's would be a subset of the mask. But we need the minimal possible such OR. However, since the mask is checked in order, the first such mask where the condition is true is the minimal possible OR. Because even if the actual OR is lower, the mask would be the minimal possible. Wait, perhaps the actual OR can be lower than the mask. But how?

Wait, suppose the mask is 5 (binary 101). For all a_i, there exists a b_j such that (a_i & b_j) is a subset of 5. But when we collect all those c_i's, their OR could be, say, 4 (binary 100). Then the actual OR is 4, which is lower than the mask. But in that case, when the algorithm checks mask=4, would the condition pass? Because if all c_i's can be subset of 4, then when mask=4 is checked, the condition would pass, and thus mask=4 would be a candidate. So the algorithm would return 4 as the answer, not 5.

So the original approach is correct only if the first mask where the condition is true is indeed the minimal possible OR. So the algorithm is correct.

So the steps are:

1. Precompute for all possible masks (from 0 to 511) in order.
2. For each mask, check for every a_i if there exists a b_j in b where (a_i & b_j) & (~mask) == 0. This ensures that the c_i's bits are a subset of the mask.
3. The first such mask (smallest) is the answer.

Because even though the mask could be larger than the actual OR, the actual OR would have a lower mask which would be checked first and thus returned.

For example, in the first sample input:

a = [2,6,4,0], b = [2,4]

Check mask=0: For each a_i, can we find a b_j where a_i & b_j is 0?

a1=2 (10): possible b_j's are 2 (10) → 2&2=2 (10), which is not 0. Or 4 (100) → 2&4=0. So yes. So a1 can choose 4 (b_j=4) → c_i=0.

a2=6 (110): possible b_j's. 6&2= 2 (10), which is 2. But 2 & ~mask (0) → 2 & ~0 is 2, but mask is 0. So 2&~0 = 2, which is not zero. So for mask 0, a2 can't find any b_j. So mask 0 is invalid.

Then check mask=1. Similarly, check for each a_i.

But the first valid mask in the sample is 2, which is the answer.

So the algorithm correctly finds that mask=2 is the minimal possible.

Another example is the second sample, where the answer is 0. So mask 0 is valid. Let's see why. For all a_i, there's a b_j such that a_i & b_j is 0. The a array includes 0. So for that a_i (0), any b_j will result in 0. For the other a_i's (like 1,9, etc.), check if there's a b_j in their list (1,1,4,5,1,4) such that a_i & b_j is 0.

Wait, for a_i=9 (1001), can there be a b_j that when ANDed gives 0? The b_j must have 0 in all bits where 9 has 1. So 9 is 1001 in binary. So any b_j that has 0 in the first and fourth bits (assuming 0 is the least significant bit). Let's see the b array: 1 is 0001, 4 is 0100, 5 is 0101. So for a_i=9 (1001), the bits 0 and 3 are set. So any b_j that has 0 in those bits. For example, 4 (0100) has 0 in bit 0. So 9 &4 is 0. So yes, there's a b_j (4) for a_i=9. So in the second sample, all a_i's can choose a b_j that gives 0, hence the OR is 0.

So the algorithm will check mask=0 first. For each a_i, check if there's a b_j such that (a_i & b_j) is a subset of 0 (i.e., zero). If yes, then mask 0 is valid, and is the answer.

So the approach works.

Now, the problem reduces to efficiently checking for each mask whether all a_i's can find a suitable b_j.

Now, the steps in code would be:

Loop over masks from 0 to 511 (inclusive). For each mask:

   For each a_i in a:

      Check if there exists a b_j in b where (a_i & b_j) & (~mask) == 0. This is equivalent to (a_i & b_j) | mask == mask. So (a_i & b_j) must be a subset of the mask.

      If any a_i has no such b_j, this mask is invalid, proceed to next mask.

   If all a_i's have at least one valid b_j, return this mask as the answer.

Now, the key is to precompute for each a_i the set of possible (a_i & b_j) for all b_j in b. Then, for each mask, check if for each a_i, any of its possible (a_i & b_j) is a subset of the mask.

But how to compute this efficiently.

First, for each a_i, precompute all possible (a_i & b_j) values. Then, for each mask, check if all a_i's have at least one value in their possible (a_i & b_j) set that is a subset of the mask.

But how to check if any of the possible c_i for a_i is a subset of the mask. For a given a_i and mask, iterate through all possible c_i in the precomputed set, and see if (c_i & (~mask)) == 0. Alternatively, for each a_i's possible c_i values, check if any of them is a subset of the mask.

So, precompute for each a_i a list of possible c_i options (a_i & b_j for all j), and then for each mask, check for each a_i whether any of their options is a subset of the mask.

But since n and m are up to 200, for each a_i, the number of possible options is up to 200, so for each mask, the check would be O(n * m), which for n=200 and m=200 is 40,000 operations per mask. And masks are 512 possibilities, so 512 * 40,000 = 20,480,000 operations. That's acceptable for Python in 1 second, as 2e7 operations are manageable.

Alternatively, precompute for each a_i a set of possible c_i's, and for each a_i, check if any c_i in the set is a subset of the mask.

Yes. So the steps in code would be:

1. Read n, m.

2. Read a array and b array.

3. Precompute for each a_i in a, the set of possible c_i's: {a_i & b_j for j in 0..m-1}

4. Sort all possible masks from 0 to 511 in increasing order.

5. For each mask in order:

   a. Check for each a_i's possible c_i's: does any of them have (c_i & ~mask) == 0?

   b. If all a_i's have at least one such c_i, then return this mask.

So in code, for each a_i, loop through their possible c_i's and see if any is subset of mask. If any a_i has none, then skip this mask.

Now, let's see the code.

First, read n and m, then the a and b arrays.

Then precompute for each a_i in a, the set of possible c_i's. For example:

pre = []
for ai in a:
    s = {ai & bj for bj in b}
    pre.append(s)

Then, for each mask in 0..511:

for mask in range(512):
    valid = True
    for s in pre:
        found = False
        for c in s:
            if (c & ~mask) == 0:
                found = True
                break
        if not found:
            valid = False
            break
    if valid:
        print(mask)
        exit()

So this is O(512 * n * k), where k is the average number of elements in each s (up to m, 200). So 512*200*200 = 20,480,000 operations. That's acceptable.

But can we optimize this?

For example, precompute for each a_i the possible c_i's, then for each mask and a_i, check if the intersection between the c_i's and the mask's subset is non-empty.

Alternatively, for each a_i, precompute a bitmask where for each possible c_i, we track which masks include it. But that might not help directly.

But the current approach is manageable.

Another optimization: for each a_i's possible c_i's, precompute a set, and for each mask, check if any c_i in the set is a subset of mask. Since the mask is being checked for all possible subsets, perhaps precompute for each a_i a bitmask where each bit represents whether a certain mask can be satisfied by that a_i. But that's O(n * 512) space, which is manageable (200 * 512 = 102400 bits, which is 12.8 KB). Then for each mask, check if all a_i's have a 1 in their bitmask for that mask.

But how to build that bitmask.

Alternatively, for each a_i, precompute all possible possible_masks that are supersets of any of its c_i's. Then for a given mask, if all a_i's have at least one c_i that is a subset of mask, then the mask is valid.

But this approach would precompute for each a_i a list of masks that can be covered by its c_i's. Then, when checking a mask, for each a_i, check if mask is in their list. But this seems like the same as the original approach.

Alternatively, for each a_i, precompute a set of all possible masks that can be achieved by any of its c_i's. Then, the valid masks are the intersection of all these sets. The minimal mask in this intersection is the answer.

But the problem is that the valid masks for a_i are all masks that are supersets of any of their c_i's. So for each a_i, the set of valid masks is all masks that are >= (bitwise) any of the c_i's. Because if a mask includes all the bits of a c_i, then that c_i is a subset of the mask.

Wait, no. The mask can be any value. For a c_i, any mask that includes all the bits of c_i is a valid mask for that a_i. So for a_i, the set of valid masks is the union of all possible masks that are supersets of each c_i in a_i's possible c_i's.

For example, if a c_i is 2 (binary 10), then all masks that have the second bit set (or higher bits) will include this c_i. But the condition is that (c_i & ~mask) == 0. Which means that all bits set in c_i are also set in mask. So mask must be a superset of c_i. So for each c_i, the valid masks for a_i are all masks where mask | c_i == mask (i.e., mask includes c_i's bits).

So for each a_i, the valid masks are the union of all masks that are supersets of any of its c_i's. The overall valid masks are the intersection of all a_i's valid masks. The minimal mask in this intersection is the answer.

So how to precompute this.

But how can we compute for each a_i the set of masks that are supersets of any of their c_i's.

For example, for c_i = 2 (binary 10), the superset masks are all masks that have the second bit set, regardless of other bits. So for each a_i, the valid masks are all masks where any of their c_i's is a subset of the mask.

So the problem reduces to for each mask, check if it is a superset of at least one c_i for each a_i.

So for each a_i, the set of valid masks is the union of (all masks >= c_i) for each c_i in a_i's possible c_i's.

Then, the valid masks for the problem are the intersection of all a_i's valid masks. The minimal such mask is the answer.

But how to compute this efficiently.

Alternatively, for each a_i, precompute the set of possible c_i's, then for each possible mask in order from 0 to 511, check if the mask is a superset of at least one c_i for each a_i.

This is the same as the original approach.

So the code can proceed as before.

Now, let's test this approach with the sample inputs.

First sample input:

n=4, m=2.

a = [2,6,4,0]

b = [2,4]

precompute for each a_i:

a_0 (2) & b_j's:

2&2=2, 2&4=0. So possible c_i's are {0,2}

a_1 (6) & b_j's: 6&2=2, 6&4=4. So {2,4}

a_2 (4) & b_j's:4&2=0,4&4=4 → {0,4}

a_3 (0) & any b_j is 0. So {0}

Then, for mask=2 (binary 10):

Check each a_i's possible c_i's:

a_0: possible 0 and 2. 0 & ~2 is 0 (since mask is 2, ~mask is 11111101 in 8 bits). Wait, in binary, mask 2 is 10. So ~mask (assuming 9 bits) is 111111101. So 0 & ~mask is 0, which is allowed. 2 & ~mask is 2 & 11111101 = 0. So both 0 and 2 are subsets of mask 2. So a_0 is okay.

Wait, 0 is a subset of any mask. So for mask 2, the c_i can be 0 or 2.

So for a_0, any of those options works.

a_1's possible c_i's are 2 and 4. For mask 2:

4 in binary is 100. So 4 & ~mask (10) is 100 & 11111101 (assuming 9 bits) → 100. Which is 4, not zero. So 4 is not a subset of mask 2. So 2 is allowed. So in a_1's possible c_i's, 2 is allowed. So a_1 can choose c_i=2 (which is 2 & 2 from b_j=2).

a_2's possible c_i's are 0 and4. 0 is allowed. 4 is not. So a_2 can choose 0.

a_3's c_i's are 0, which is allowed.

Thus mask=2 is valid.

So the code will return 2.

Yes.

Another sample:

Second sample, answer is 0.

For each a_i:

a_7 is 0, so its c_i's are 0.

Other a_i's: For example, a_i=9 (1001). The possible c_i's are 9&b_j.

Looking at b array: 1,1,4,5,1,4.

So 9&1 is 1 (binary 0001), 9&4 is 0 (since 9 is 1001, 4 is 0100; AND is 0000). So for a_i=9, possible c_i's include 0, so mask 0 is valid.

Thus all a_i's can find a c_i which is 0, so mask 0 is valid.

Third sample's answer is 147. So the code would process all masks until 147, which is the first valid.

But the code will find the minimal mask, which is correct.

So the code is correct.

Now, to implement this in Python.

But wait, in Python, for checking (c & ~mask) ==0. Since in Python, integers can be larger, but since mask is up to 511 (9 bits), ~mask will be a negative number if we use bitwise operations. Wait, but how to handle this correctly.

Wait, in Python, the bitwise NOT operator (~) returns the two's complement of the number. For example, ~mask is equal to -mask -1. But when mask is up to 511 (binary 111111111), ~mask is -512 (since 511 is 0b111111111, ~511 is 0b...1111111111111111000000000000, which in two's complement is -512). So when we compute (c & ~mask), this is equivalent to (c & (all bits except mask bits set)), which is not the intended behavior.

Wait, no. Wait, the problem is that in Python, integers are of arbitrary length. So, for mask=2 (binary 10), ~mask would be ...11111101. So when you do c & ~mask, where c is a 9-bit number, then the result would be c AND the bits that are not set in mask. But in Python, since integers can have leading 1's (for negative numbers), this might not be correct.

So to correctly compute (c & ~mask) == 0, but only considering the first 9 bits (since the c's can't have more than 9 bits), perhaps we need to mask off the higher bits. Wait, but how?

Alternatively, perhaps the correct way is to compute (c | mask) == mask, which is equivalent to (c is a subset of mask).

Because if c is a subset of mask, then all bits in c are set in mask, so ORing them with mask gives mask. So (c | mask) == mask.

Yes! That's a better way. Because (c | mask) == mask if and only if c is a subset of mask.

So instead of (c & ~mask) == 0, we can check (c | mask) == mask.

This avoids the problem with Python's bitwise not operator.

So in code, for each c in a_i's possible c_i's, check if (c | mask) == mask.

Yes. So this is a better way. Let's adjust the code accordingly.

So for each mask in 0..511:

for mask in range(512):
    valid = True
    for s in pre:
        found = any( (c | mask) == mask for c in s )
        if not found:
            valid = False
            break
    if valid:
        print(mask)
        exit()

This should handle all cases correctly, regardless of Python's handling of bitwise operations.

So now, the code is correct.

Now, let's code this.

The steps:

Read n and m.

Read a array.

Read b array.

Precompute for each a_i in a the set of (a_i & b_j for b_j in b), then store as a set.

Then iterate mask from 0 to 511, in order.

For each mask, check for each a_i's set of c_i's if any c_i in it satisfies (c_i | mask) == mask.

If all a_i's have at least one such c_i, output the mask and exit.

Otherwise, proceed.

Now, in Python, for each a_i, precompute the set of possible c_i's.

In code:

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pre = []
for ai in a:
    s = set()
    for bj in b:
        s.add(ai & bj)
    pre.append(s)

for mask in range(512):
    ok = True
    for s in pre:
        found = False
        for c in s:
            if (c | mask) == mask:
                found = True
                break
        if not found:
            ok = False
            break
    if ok:
        print(mask)
        exit()

Yes. This should handle all cases.

But wait, the precompute step can be optimized. For example, for each ai, we can create a set of possible c_i's, but in Python, the order of checking in the set is arbitrary. However, since the 'any' function in Python checks elements in arbitrary order (as sets are unordered), but as soon as one element is found, it returns True. So the code is correct.

Another optimization: precompute for each a_i the list of possible c_i's, but using a set removes duplicates. So for example, if multiple b_j's result in the same c_i, it's stored once. This reduces the number of checks per a_i.

Yes, which is better. Because if there are duplicate c_i's, it's redundant to check them all. So using a set is better.

Thus the code is correct.

Testing the first sample:

pre[0] for a=2 is {0,2}, for a=6 is {2,4}, etc. When mask=2 is checked, the code will find that:

For each a_i:

a_0: 0 | 2 is 2 → yes. 2 | 2 is 2 → yes. So any of them works. So found=True.

a_1: check 2 |2=2, which equals mask. So found=True.

a_2: 0 |2=2, yes. So found=True.

a_3: 0 |2=2, yes. So mask=2 is valid, and printed.

Thus correct.

The code should work.
</think>

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pre = []
for ai in a:
    possible = set()
    for bj in b:
        possible.add(ai & bj)
    pre.append(possible)

for mask in range(512):
    valid = True
    for s in pre:
        if not any((c | mask) == mask for c in s):
            valid = False
            break
    if valid:
        print(mask)
        exit()
```