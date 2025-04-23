<think>
Okay, let's see. So the problem is to split the array of books into exactly k contiguous groups, each with at least one book, and maximize the bitwise AND of the sum of each group. Hmm, right.

The constraints are n up to 50 and k up to 50. Wait, but even with n=50 and k=50, that's just each shelf having one book. But the sums can be up to 50 * (2^50), which is a very big number, like 50 bits plus some. So we need to handle big integers here, but Python handles that fine.

The key is to find the maximum possible bitwise AND. Bitwise AND is maximized when as many high bits are set as possible. So the approach here is similar to finding the maximum XOR subset or something, where you check bits from high to low.

So maybe a bitmask approach. For each bit from the highest possible down to 0, check if it's possible to set that bit in the AND result, given that the higher bits are already set.

For example, let's start with the highest possible bit. Let's say we want to check if the result can have the 60th bit set. How do we check that?

We need to split the books into k shelves, such that each shelf's sum has all the bits that we have in our current mask (built from higher bits) plus this current bit. Then, the AND of all those sums would include this bit.

Wait, but how do we model this? It's a dynamic programming problem, perhaps.

Let me think. The bitwise AND is maximized when each bit is set if possible. So we can greedily try to set each bit from the highest down. For each bit position, we check if it's possible to split the array into k shelves such that all shelf sums have that bit set (along with any higher bits we've already determined). If yes, then we keep that bit in our result and proceed to lower bits.

This is a common approach in bitmask maximization problems. So the plan is:

1. Initialize the result as 0.
2. For each bit from the highest possible (like 60, since 2^50 is about 1e15, so 50 bits, but each sum could be up to sum of 50 numbers each 2^50, which is 50*2^50, so log2(50) is about 6, so 56 bits total) down to 0:
   a. Tentatively set this bit in the result (i.e., check if setting this bit along with the previously set bits is possible).
   b. Check if there's a way to split the array into k shelves such that each shelf's sum has all the bits set in the tentative result.
   c. If possible, keep this bit in the result; else, leave it unset.
3. Return the accumulated result.

The critical part is step 2b: how to check if such a split exists given a mask.

So for each candidate mask (built by including higher bits and the current candidate bit), we need to verify if there's a way to split the array into exactly k parts, each with sum & mask == mask. Because the AND of all the sums must have all bits set in the mask, each sum must have those bits set. Wait no: the AND of the sums will have a bit set only if all sums have that bit set. So if the mask is the bits we are trying to set in the final result, each sum must have all those bits set.

So for a given mask, we need to check if we can split the array into k contiguous segments where each segment's sum when ANDed with the mask equals the mask. Because that means that each sum has all the bits in the mask set. So the mask must be a subset of the bits of each sum.

So how to check this efficiently?

We can model this with dynamic programming. Let dp[i][j] be True if the first i books can be split into j shelves, each of which has a sum that includes the current mask bits.

The transitions would be: for each possible j (number of shelves), and for each possible split point. So for each i, j, check if there's a previous split point l (less than i) such that the sum from l+1 to i is a valid sum (sum & mask == mask) and the previous j-1 shelves can be formed up to l.

The base case is dp[0][0] = True (0 books, 0 shelves).

But for each mask, this could be O(n^2 k) time. But since n is up to 50 and k up to 50, the total per mask is 50 * 50 * 50 = 125,000 operations. Considering that the number of bits is up to 60, the total operations would be 60 * 125,000 = 7.5 million, which is manageable.

So the steps are:

1. Compute the prefix sums of the array to quickly calculate the sum of any interval.
2. For each bit from highest to lowest:
   a. Set the candidate mask as the current result OR (1 << bit).
   b. Check if it's possible to split the array into k shelves with each sum having all bits in the candidate mask set.
   c. If possible, update the result to the candidate mask.
3. Return the final result.

Now, how to compute the prefix sums. Let's precompute prefix where prefix[0] = 0, prefix[1] = a[0], prefix[2] = a[0] + a[1], etc. So the sum from l to r (0-based) is prefix[r] - prefix[l].

So for the DP:

mask is the current candidate mask. For each possible j (number of shelves), and for each possible i (number of books processed), we need to check if there's a way to split the first i books into j shelves, each with sum & mask == mask.

So, for dp[i][j], we check for all l < i whether dp[l][j-1] is True and sum from l to i (i.e., prefix[i] - prefix[l]) & mask == mask.

If yes, then dp[i][j] is True.

The base case is dp[0][0] = True.

The answer for a given mask is whether dp[n][k] is True.

So, the code outline is:

result = 0

for bit in reversed(range(0, max_bit + 1)):
    candidate = result | (1 << bit)
    # check if possible to split with this candidate mask
    possible = False
    # compute prefix sums
    # run the DP
    dp = a 2D array of size (n+1) x (k+1), initialized to False
    dp[0][0] = True
    for i in 1 to n:
        for j in 1 to k:
            for l in 0 to i-1:
                if dp[l][j-1] is True:
                    current_sum = prefix[i] - prefix[l]
                    if (current_sum & candidate) == candidate:
                        dp[i][j] = True
                        break
    if dp[n][k] is True:
        result = candidate

So this is the approach. Now, considering the constraints.

But n is up to 50, k up to 50. For each mask, the DP loops through i from 1 to n (50), j from 1 to k (50), and for each (i,j), loops l from 0 to i-1 (up to 50). So per mask, 50 * 50 * 50 = 125,000 operations. For 60 bits, total is 7.5 million, which should be acceptable for Python.

But in Python, nested loops can be slow. So we need to optimize this.

Wait, but 7.5 million operations is manageable. Let's see: each loop iteration is a few operations. For Python, 1e6 operations take about 0.1s, so 7.5e6 would be about 0.75s. Since the time limit is 1s per test case, this should be okay.

But how to optimize the DP.

Alternative approach: for each j, precompute possible positions for j shelves, and for each i, track if it's possible.

But perhaps we can precompute the prefix sums once.

Wait, the prefix sum array can be precomputed once. Then for each mask, we check the sum between l and i.

So code steps:

Read n, k.

Read the array a.

Compute prefix sum: prefix[0] = 0, prefix[1] = a[0], prefix[2] = a[0]+a[1], etc.

Initialize result to 0.

For bit in reversed(range(60)):  # since 2^50 is 1e15, and sum of 50 books could be up to 50*2^50, which is 5e16, which is 56 bits.

    candidate = result | (1 << bit)

    # Now check if possible to split into k shelves, each sum & candidate == candidate.

    # Initialize DP. We can represent dp as a list of lists, or use a 2D array.

    dp = [ [False]*(k+1) for _ in range(n+1) ]
    dp[0][0] = True

    for i in range(1, n+1):
        for j in range(1, k+1):
            # Check all possible l < i where j-1 shelves can be made up to l, and sum from l to i is valid.
            # To find l from 0 to i-1.
            # If any such l exists, then dp[i][j] = True
            for l in range(0, i):
                if dp[l][j-1]:
                    s = prefix[i] - prefix[l]
                    if (s & candidate) == candidate:
                        dp[i][j] = True
                        break  # no need to check other l once found
            # Alternative approach: for j-1, precompute all possible l where dp[l][j-1] is True, then check if any of the sums from l+1 to i are valid.

    if dp[n][k]:
        result = candidate

Finally, output result.

But for Python, even with n=50 and k=50, this could be a bit slow. Let's think about optimizations.

The key is that for each i, j, the loop over l can be optimized. For example, precompute for each j-1 the list of possible l's. Then, for each i, j, iterate through those l's and check if the sum between l and i meets the candidate mask.

But how to do that.

Another optimization is that, for each j, we can keep a list of positions l where dp[l][j-1] is True. Then, for j-th shelf, for each i, check if any l in that list (l < i) has the sum from l to i meeting the mask.

But in code, perhaps for each j, we can track the possible l's for j-1, and for each i, iterate through those l's.

Alternatively, for each j, we can precompute the possible l's for j-1 and store them in a list. Then, for each i, j, we can loop through those l's (which are less than i) and check the sum.

But in Python, the inner loop may be the slow part. Let's think of ways to optimize.

Alternative idea: precompute all possible possible splits for each j.

Another way is to note that for each i, j, we can check for l in the possible positions where dp[l][j-1] is True, and sum between l and i meets the mask.

But how to efficiently check if any l in the possible positions for j-1 has a sum from l to i that is compatible with the mask.

Another approach: for each j, keep a list of possible l's for j-1. For each i, compute the sum from l to i (for each l in the list) and check if it matches the mask.

But how?

Wait, the sum is prefix[i] - prefix[l]. So for each i, and for each l in the list for j-1, check if (sum) & candidate == candidate.

So for a given j, j ranges from 1 to k.

So for each i in 1..n, j in 1..k:

We can precompute for j-1 all possible l's (where dp[l][j-1] is True). Then, for each of those l's, compute the sum from l to i, and check if the sum meets the mask.

If any l in that list satisfies the condition, then dp[i][j] is True.

So for each j, we can track a list of l's that are possible for j-1.

In code, for each j, during the iteration, we can have a list of possible l's for j-1. Then, for each i, we loop through those l's and check the sum.

This can reduce the number of l's we check. For example, if for j-1, there are few l's, then the inner loop is faster.

So here's the optimized approach:

For each candidate mask:

- Initialize a list of lists: prev_j. For each j, prev_j[j] is a list of l's where dp[l][j] is True.

But maybe for each j, track the possible l's for j-1.

Wait, let's think for the DP step.

Initially, dp[0][0] is True.

For j=1 to k:

   For each i from 1 to n:

       For each l in prev_j[j-1], where l < i:

           if (sum(l, i) & mask) == mask, then mark dp[i][j] as True.

So, in code:

prev = [ [ ] for _ in range(k+1) ]

prev[0].append(0)  # since dp[0][0] is True.

for j in 1 to k:

   current = [ ]  # list of i's where dp[i][j] is True.

   for i in 1 to n:

       for l in prev[j-1]:

           if l < i and (sum from l to i) & mask == mask:

               current.append(i)

               break  # since once found, no need to check other l's.

   prev[j] = current

At the end, check if n is in prev[k].

This approach would use the previous j-1's possible l's and check for each i. But how to manage this.

This could be more efficient because for each j and i, we only loop through the l's in prev[j-1], which may be a smaller list than 0 to i-1.

For example, if j is 1, then j-1 is 0. prev[j-1] is [0]. For each i, check sum from 0 to i (i.e., prefix[i] - prefix[0] = sum of first i books) and see if it's compatible with the mask. So for j=1, the current list would be all i where sum of first i books meets the mask.

Similarly for higher j.

This way, for each j, the inner loop is over the list of l's from prev[j-1], which could be much smaller than i.

So the code can be modified as follows:

for mask in ...:

   possible = False

   # Use a list of lists to track possible positions for each j.

   prev = [[] for _ in range(k+1)]

   prev[0] = [0]  # j=0 has position 0.

   for j in range(1, k+1):

       current_j = []

       for i in range(1, n+1):

           # Check if any l in prev[j-1] is less than i, and sum from l to i is compatible.

           for l in prev[j-1]:

               if l < i:

                   s = prefix[i] - prefix[l]

                   if (s & mask) == mask:

                       current_j.append(i)

                       break  # once found, no need to check other l's.

       prev[j] = current_j

   # Check if there's an entry in prev[k] that equals n.

   if n in prev[k]:

       possible = True

So in this approach, for each j, prev[j] is the list of i's where the first i books can be split into j shelves, each sum compatible with the mask.

But even here, for each j and i, we loop through all l's in prev[j-1], which could be O(n) in the worst case. So for j=50, i=50, and l's being 50 elements, it's again 50*50*50 per mask. But maybe in practice, it's faster because some of the l's are not in the list.

But this may not save time, but perhaps can be optimized further.

Alternatively, for each j and i, check all possible l's from prev[j-1], but in order, and break as soon as a valid l is found.

In Python, list comprehensions and early breaks can help.

Alternatively, precompute for each j-1 the possible l's, and for each i, check the sum from l to i for those l's.

But regardless, the time complexity per mask is O(k * n * m), where m is the average number of l's per j-1. But in the worst case, m can be O(n), leading to O(k n^2) per mask.

Hmm. Well, given the constraints, even with n=50 and k=50, 60 masks, it's 60 * 50 * 50 * 50 = 7.5e5 * 50? Wait, no. Wait, 50*50*50 is 125,000 per mask, multiplied by 60 is 7.5 million. Which is acceptable.

So perhaps the initial DP approach is manageable.

Now, let's look at the sample input.

Sample 1:

10 4

9 14 28 1 7 13 15 29 2 31

The output is 24, which is binary 11000 (24). So the AND of the four shelf sums must have bits 4 and 3 (8 + 16 = 24).

So during the mask building, the algorithm would check higher bits first.

Another thing to note is that the mask must be a subset of the AND of all shelf sums. So the candidate mask is built by OR-ing bits from high to low, and for each candidate, the algorithm checks if it's possible.

So code-wise, in Python, the code can be written as follows.

But first, compute the prefix sum. Then, for each bit from 59 down to 0, check if adding that bit to the current mask allows a valid split.

Now, the code:

Read n and k.

Read the list of a's.

Compute prefix sum.

Initialize result to 0.

For bit in reversed(range(60)):

    candidate = result | (1 << bit)

    # Check if split possible with this candidate.

    # DP table: dp[i][j] is True if first i books split into j shelves.

    # But since for each j, we only need j-1's data, we can optimize space.

    # However, for clarity, let's use a 2D array.

    dp = [ [False]*(k+1) for _ in range(n+1) ]

    dp[0][0] = True

    for i in range(1, n+1):

        for j in range(1, k+1):

            # For each possible l < i where j-1 shelves are made up to l.

            # So for l in 0..i-1:

            # If dp[l][j-1] is True, and sum from l to i is compatible.

            # To optimize, check all l where dp[l][j-1] is True.

            found = False

            for l in range(0, i):

                if dp[l][j-1]:

                    s = prefix[i] - prefix[l]

                    if (s & candidate) == candidate:

                        dp[i][j] = True

                        found = True

                        break  # no need to check other l's

            if found:

                continue

    if dp[n][k]:

        result = candidate

Print(result)

Yes, this seems correct.

But in Python, creating a 2D array for each mask may be memory-consuming? But n is 50, k is 50, so each dp is (51 x 51) = 2601 booleans, which is negligible.

So the code is manageable.

Testing the sample input:

Sample 1:

prefix[0] = 0

prefix[1] =9

prefix[2] =23

prefix[3] =51

prefix[4] =52

prefix[5] =59

prefix[6] =72

prefix[7] =87

prefix[8] =116

prefix[9] =118

prefix[10] =149

Now, let's say during the mask check for 24 (binary 11000). The candidate mask would be 24. So each shelf's sum must have bits 4 and 3 set (16 + 8 = 24).

The split is 5 books, 2 books, 2 books, 1 book.

First sum is 9+14+28+1+7=59. 59 in binary is 111011. AND with 24 (11000) is 24. So yes.

Second sum is 13+15=28, which is 11100. AND with 24 is 24.

Third sum is 29+2=31. AND with 24 is 24.

Fourth sum is 31. AND with 24 is 24.

So the code would find a split and thus include the bitmask 24.

So the code should work.

Now, the code in Python:

But wait, in the code, for each i and j, we loop through l from 0 to i-1. This is O(n^2 k) per mask.

But given the constraints, it's acceptable.

Now, code:

Read n, k.

Read a as a list.

Compute prefix.

Initialize result to 0.

For bit in reversed(range(60)):

    candidate = result | (1 << bit)

    dp = [ [False]*(k+1) for _ in range(n+1) ]

    dp[0][0] = True

    for i in range(1, n+1):

        for j in range(1, k+1):

            for l in range(i):

                if dp[l][j-1]:

                    s = prefix[i] - prefix[l]

                    if (s & candidate) == candidate:

                        dp[i][j] = True

                        break

    if dp[n][k]:

        result = candidate

Print(result)

Yes.

But wait, in Python, the initial code for prefix sum is:

prefix = [0]*(n+1)

for i in range(1, n+1):

    prefix[i] = prefix[i-1] + a[i-1]

Yes.

Testing with sample input 1:

Sample 1's prefix after 10 books is 149.

But during the check for candidate mask 24, the code would compute the dp table.

At i=5 (prefix[5] is 59), j=1:

j=1, so j-1=0. l must be 0 (since dp[0][0] is True). Sum is 59-0=59. 59 & 24 is 24. So dp[5][1] is True.

But in the problem, the first shelf is 5 books, but the split requires 4 shelves. So the code needs to split into 4 shelves.

The DP must track for j=4 shelves. So for the final i=10, j=4.

But during the mask check for 24, the code would compute whether there's a split into 4 shelves, each sum & 24 ==24.

The code's DP would find this and thus set the candidate to 24.

So the code should work.

Another sample: second input.

7 3

3 14 15 92 65 35 89

The sum for the first shelf is 3+14+15+92 = 124. Sum is 124. 124 in binary is 1111100. The mask is 64 (1000000). 124 &64 is 64. The second shelf is 65, which &64 is 64. The third shelf is 35+89=124, &64 is 64. So the AND is 64.

The code would check for higher bits first. For example, when checking the 6th bit (64), the code would see that the split into 3 shelves is possible.

Thus, the code would include 64 in the result.

So the code should handle this.

Now, let's implement this in Python.

The code must read input from stdin, compute, and output.

So here's the code:

Read n and k.

Read the list of a's.

Compute prefix sum.

Initialize result to 0.

Loop over bits from 59 down to 0:

   candidate = result | (1 << bit)

   Initialize dp as 2D array of False.

   dp[0][0] = True.

   For each i in 1..n:

       for each j in 1..k:

           for l in 0..i-1:

               if dp[l][j-1] is True and (sum from l to i) & candidate == candidate:

                   dp[i][j] = True

                   break

   if dp[n][k] is True, set result = candidate.

Print result.

So the code is as follows.
</think>

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + a[i - 1]

result = 0

for bit in reversed(range(60)):
    candidate = result | (1 << bit)
    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for l in range(i):
                if dp[l][j - 1]:
                    s = prefix[i] - prefix[l]
                    if (s & candidate) == candidate:
                        dp[i][j] = True
                        break
    
    if dp[n][k]:
        result = candidate

print(result)
```