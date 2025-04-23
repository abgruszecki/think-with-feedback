<think>
Okay, let's see. The problem is about finding all possible total costs the thief can have when taking exactly k products, with possible multiple items from the same kind. The input is the number of kinds n and k, then the list of a_i. We need to output all possible sums in sorted order.

Hmm. So the thief can take any combination of k items, each from any of the n types. The sum is the total. We need to compute all possible sums and output them sorted.

The first thing that comes to mind is dynamic programming. Because for each step, we can choose an item and accumulate the sum. But with k up to 1000 and each a_i up to 1000, the sum could be up to 1000*1000=1e6. So the DP state could be something like possible sums after taking m items. For each possible number of items m (from 0 to k), we track the possible sums. Then, for each step, when adding an item, we take the existing sums and add a_i to them, but considering how many items are taken.

Wait, but the order doesn't matter here. The sum is just the sum of k a_i's. So the problem reduces to finding all possible sums that can be formed by selecting k numbers (possibly with repetition) from the a_i array. The key is that each selection counts towards the total k.

So, how do we model this? Let's think about the possible sums for exactly m items. We can start with m=0, sum=0. Then, for each step from m=1 to m=k, we build the possible sums by adding each a_i to the sums from m-1.

Wait, but each step m can have a set of possible sums. For example, m=1 is the sum of one a_i. m=2 is the sum of two a_i's (could be same or different). So this seems like a BFS approach, where each level is m, and the nodes are possible sums, and edges are adding an a_i. But with m up to 1000, and possible sums up to 1e6, this could get expensive.

But perhaps we can use dynamic programming with a set for each m. Let's model it as a 2D array where dp[m] is the set of possible sums for exactly m items. Then for each m from 1 to k, we can compute dp[m] by adding each a_i to each sum in dp[m-1], then taking the union. However, for n and k up to 1000, this approach would have a time complexity of O(k * S * n), where S is the number of sums in each step. But S could be up to 1e6 for each m, which for k=1e3 would be 1e9 operations. That's way too slow.

Wait, that's a problem. So this approach might not be feasible for the constraints given. Let's think about alternative approaches.

Alternative approach: the problem is similar to the integer composition problem. Since the thief can take any number of items from each kind, but the total must be exactly k. So the sum is sum (x_i * a_i) where sum x_i = k, and x_i >=0.

So we need to find all possible combinations of x_i such that sum x_i =k, and compute the sum a_i *x_i for each such combination.

But enumerating all possible combinations is not feasible, since even with n=1000 and k=1000, the possibilities are way too big.

So we need a smarter way. Let's think of the minimal sum and maximal sum. The minimal sum would be when all k items are the smallest a_i. The maximal sum is when all are the largest a_i. So the sum can vary between k*min_a and k*max_a. But between those, there might be many possibilities. But how do we find all the possible sums?

Wait, but perhaps the possible sums form a contiguous range? No, that's not the case. For example, in the first sample input:

3 2

1 2 3. The possible sums are 1+1=2, 1+2=3, 1+3=4, 2+2=4, 2+3=5, 3+3=6. So the sums are 2,3,4,5,6. But 2 comes from two 1s, 3 is 1 and 2, etc. So the possible sums are 2,3,4,5,6. So there's a gap between 2 and 3, but not between others. Wait, but the output is 2 3 4 5 6. So in that case, the sums are contiguous. But maybe not always. Wait the second example: all 1s. So sum is 5. So that's a single value. Third example: output has various sums but they are not all consecutive. For instance, 9, then 11 (so a gap of 2), etc. So the sums are not necessarily contiguous.

Therefore, we need a way to track all possible sums efficiently.

Let me think again about the DP approach. Let's model dp[m] as a set of possible sums with exactly m items. Then, for each m from 1 to k, we can compute dp[m] by adding each a_i to all elements of dp[m-1].

But for k=1000 and each a_i up to 1000, the maximum possible sum is 1000*1000=1e6. So for each m, the size of dp[m] could be up to 1e6. But for 1000 steps, this is 1e9 operations, which is way too slow.

But wait, the problem's constraints are n and k up to 1000. So the DP approach's time complexity would be O(k * n * S), where S is the average size of the sets. For example, in the worst case, S is 1e6, but 1e3 * 1e3 * 1e6 = 1e12 operations. That's way beyond acceptable for Python, which can handle about 1e8 operations per second (but even that is a rough estimate). So this approach is not feasible.

We need a smarter way. Let's think about the problem differently. Since all x_i are non-negative integers summing to k, perhaps there's a mathematical way to model the possible sums.

Alternatively, the problem can be transformed into a knapsack problem where the number of items is exactly k, and each item can be chosen as part of the sum.

Wait, the standard knapsack problem is about maximizing value with capacity constraints, but here it's about finding all possible sums for exactly k items. So this is the "unbounded knapsack" problem with the twist that exactly k items must be taken.

So, the key is to model it as an exact version of the knapsack problem. So the DP approach would track, for each possible number of items m, the possible sums. So, the DP state is a 2D array, where dp[m][s] is True if sum s can be achieved with exactly m items.

But again, the problem is the size. For m up to 1e3 and s up to 1e6, the storage would be 1e9, which is impossible.

Wait, but perhaps we can use bitsets to represent the possible sums for each m. For example, for each m, we can have a bitmask where the ith bit represents whether sum i is possible. Then, for each m, the bitmask is the OR of (bitmask of m-1 shifted by a_i bits) for all a_i.

But in Python, handling large bitmasks can be done with integers. For example, each possible sum is a bit in an integer. For m=0, the bit is set at 0. For each a in a_i, we can compute the next step's bitmask by shifting the current bitmask by a bits. Wait, no. Because for m=1, the sum can be any a_i. So for m=1, the bitmask is the OR of (1 << a_i) for all a_i. For m=2, each sum is a sum of two a_i's. So for each a_i, take the m=1 bitmask, shift left by a_i, and OR all those together. But this approach would generate all possible sums for m=2.

But how do we handle the different combinations? Let's see.

Wait, for each step m, the possible sums are the sum of m a_i's. To compute this, the DP can be represented as a list of bitsets, where for each m, the bitset represents the possible sums. For m=0, sum is 0. For m=1, sum is each a_i. For m>1, the sum is the sum of m a_i's. So the transition is: for each m, the sum s can be achieved if there exists a_i such that s - a_i is in the set for m-1.

So, the DP transition for m is:

dp[m] = dp[m] | (dp[m-1] << a_i) for each a_i.

But in terms of bitsets, this would be:

bitset[m] = bitset[m-1] shifted left by a_i, OR'ed for all a_i.

Yes. So for each m, the bitset is the union of (bitset[m-1] << a_i) for all a_i.

But shifting left by a_i would add a_i to each possible sum in the previous step. So, for each a_i, we take the previous bitset (sums for m-1) and add a_i to each of those sums. The OR of all these gives the possible sums for m.

This approach would work. And using bitsets (or in Python, integers) allows us to represent the sums efficiently.

The maximum sum possible is k * max_a. For k=1e3 and a_i=1e3, the maximum sum is 1e6. So each bitset needs to be of size up to 1e6+1. But in Python, integers can handle arbitrary bits. However, for 1e6 bits, each bitset would be manageable as a Python integer, as long as the operations are efficient.

So the algorithm steps are:

1. Initialize a list of bitsets for each m. Since we only need the current and previous steps, perhaps we can optimize space by using two variables: prev and curr.

For m from 1 to k:

   curr = 0

   for each a_i in a:

       shifted = prev << a_i

       curr |= shifted

   prev = curr

But wait, no. Because for each a_i, adding it to the previous sums (m-1) gives the possible sums for m. So for example, prev is the bitset for m-1. Then, for each a_i, shifted is prev shifted left by a_i, which adds a_i to all possible sums. Then, the OR of all these shifted bitsets gives the possible sums for m.

But in Python, shifting left by a_i is the same as multiplying by 2^a_i, but that's not correct. Because the bits represent sums. For example, if a sum is s, adding a_i gives s + a_i, which would be the same as shifting the bit s by a_i positions. Wait, no. Wait, the bit for sum s is at position s. Shifting left by a_i would move that bit to s + a_i. So yes, shifting left by a_i is equivalent to adding a_i to each possible sum in the previous step.

Therefore, the algorithm is:

prev = 1 << 0 (sum 0 for m=0)

for m in 1 to k:

    curr = 0

    for a in a_list:

        curr |= prev << a

    prev = curr

At the end, the bits set in prev (for m=k) are the possible sums.

Wait, but this approach would allow adding multiple a's. However, this would compute the sum as the sum of m a's, where each a can be any of the a_i. So, for m=2, it's the sum of two a's, which can be the same or different. But in this approach, for each step m, each a_i is added once. Wait, no: for example, in the first step (m=1), prev is 1 << 0. Then, for each a_i, the shifted prev is 1 << (0 + a_i) = 1 << a_i. Then, ORing all these gives the bitset for m=1, which is each a_i as a sum.

For m=2, the process is similar: for each a_i, we take the sums from m=1 (each sum s), add a_i to get s + a_i, which is the sum of two items (the first from any of the a_i, the second is this a_i). So this correctly captures all possible pairs.

But wait, what about choosing the same a_i multiple times? For example, two a_1's. Let's say a_1 is 1. For m=2, the sum would be 2. How is this captured?

In m=1, the sum is 1. Then, in m=2, when adding a_1 (1) again, the sum becomes 2. So yes, this is included. So this approach correctly captures all possible sums of m a_i's, allowing repetitions.

So this approach seems correct.

But wait, how does this work when the same a_i is added multiple times? Let's see. For example, in the first step (m=1), the sum is each a_i. For m=2, for each a_i in the list, we add that a_i to all possible sums from m-1 (which is m=1). So for each a_j in a_list, the sum s_j + a_i is added. But since a_i can be any of the a's (including a_j), this allows the same a to be added multiple times.

Yes. So this approach correctly models the selection of any combination of k a_i's, possibly repeated.

But in the problem statement, the thief can take several products of the same kind, which is allowed. So the approach is correct.

So the key is to model this with a bitset approach, using bitwise operations to track possible sums efficiently.

Now, the question is, how to implement this in Python efficiently.

Let's think about the steps:

- Read n, k.

- Read the a list. But since there are duplicates in a, but the same a_i can be added multiple times, but in the bitset approach, adding the same a_i multiple times doesn't change the result. So perhaps we can first deduplicate the a list. Because adding a_i once is sufficient. For example, if the a list has duplicates, like [1, 1, 2], then for m=2, adding 1 again (from the first 1) and then another 1 (from the second 1) would generate the same shifts. So, deduplicating a can save some computation time.

Wait, but in the problem statement, the a_i are the costs of each kind. So each kind's cost is given, but the thief can take any of the kinds. So if two kinds have the same a_i, taking either gives the same contribution. But for the sum, it's the same as taking two of the same kind. So for example, if a list has two 1's, then for m=2, the sum can be 1+1 (taking two from the same kind), or 1+1 (taking one from each of the two 1's). But in the bitset approach, when we process each a_i (including duplicates), this would create the same shifts as processing the unique a_i's. So processing duplicates in a_i is redundant. Therefore, deduplicating the a list would speed up the code.

So, first, we can convert the a list to a set, then back to a list. That way, duplicates are removed.

So, in code:

a = list(map(int, input().split()))
a = list(set(a))

This step reduces the number of elements in a, which can be up to 1000. For example, if all a_i are the same, after deduplication, a has one element. So this step can save a lot of computation time.

Then, for each m from 1 to k:

    For each a_i in the deduplicated a list:

        curr |= prev << a_i

But shifting left by a_i can be a large shift. For example, if a_i is 1000 and k is 1000, then the sum can be up to 1e6, so the bitset for each step can be up to 1e6 bits. But in Python, integers can handle arbitrary bits, so even 1e6 bits is manageable.

But how efficient is this? Because for each a_i, the shift operation is O(1) in Python (as integers are handled as arbitrary precision). So for each m step, for each a_i in the unique list, we do a shift and OR.

But the number of a_i's after deduplication can be up to 1000 (if all are unique). So for m=1e3, and a_i=1e3, the total operations are 1e3 * 1e3 = 1e6 operations. Which is manageable in Python.

So the code steps are:

n, k = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a))  # Remove duplicates.

prev = 1  # represents sum 0 with 0 items.

for _ in range(k):
    curr = 0
    for num in a:
        curr |= prev << num
    prev = curr

Then, after k steps, prev will have bits set for all possible sums. Then, we need to collect all the set bits in prev and output them in sorted order.

Wait, but wait. The initial prev is 1 (bit 0 set, representing sum 0 with 0 items). Then, for each of the k steps, we build the sums for 1, 2, ..., k items.

But in the code above, the loop runs k times. For each iteration, m increases by 1. So after k iterations, prev represents the sums for exactly k items.

Yes. Because:

After first iteration (m=1), curr is the OR of 1 << a_i for each a_i. So sum 0 (from m=0) shifted by a_i gives a_i. So prev is the sum for m=1.

Yes. So the code is correct.

Once we have prev, which is a bitmask where the bits set correspond to the possible sums, we need to extract all the bits that are set and print them in order.

So, extract the bits by iterating through all possible positions and checking if the bit is set. Then sort them and output.

But in Python, how to find the set bits?

We can iterate through all possible bits. The maximum possible sum is k * max_a. So first, find the maximum a in the list, compute k * max_a. Then iterate from 0 to max_sum and check if the bit is set.

But in the code above, after k steps, the sum is exactly k items, so the possible sum is the sum of k a_i's, which can be as high as k*max_a (1e6). So we can compute the max_sum as k * max_a. Then, for s in range(0, max_sum + 1), check if (prev >> s) & 1 is 1. Collect all such s, sort them, and print.

But wait, after deduplication, the a list can be empty? No, because n is at least 1. But when you do set(a), even if all a_i are the same, the list will have one element.

So code steps to collect the result:

result = []
max_sum = k * max(a)
s = 0
while s <= max_sum:
    if (prev >> s) & 1:
        result.append(s)
        s += 1
    else:
        s += 1

Wait, but this is not efficient. Alternatively, we can iterate from 0 to max_sum and check each bit. But for max_sum up to 1e6, this would take 1e6 iterations. Which is manageable.

Alternatively, in Python, we can find the bits set in the integer using a loop. For example:

sums = []
s = 0
current = prev
while current:
    lsb = current & -current  # get the least significant bit set
    pos = (lsb).bit_length() - 1
    sums.append(pos)
    current ^= lsb

But this approach would collect the bits in reverse order (since we start from the least significant bit). Wait, no. The lsb is the least significant bit. For example, if the sum is 2, the bit is set at position 2. But lsb is 2^2, so (lsb).bit_length() - 1 is 2. So for the sample input, after k=2, the prev would be 0b111110 (binary for 2,3,4,5,6). The bits set at positions 2,3,4,5,6. So the loop would collect these positions and then sort them.

Wait, but the code above would collect the positions in increasing order. Because each time we take the least significant bit. For example, if the bits are 2,3,4,5,6, then the first lsb is 2 (bit 2), then after XOR, the next lsb is 3, etc. So the list would be [2,3,4,5,6], which is correct and already in sorted order. So no need to sort again.

Wait, no. Because in binary, the bits are stored as 0b100 (2) is lower than 0b1000 (3). So when you take the least significant bit each time, the positions are in order from smallest to largest. For example:

prev = 0b1111100 (binary for 2,3,4,5,6). The binary is 0b100 (2), then 0b1000 (3), etc. But when you compute current & -current, the least significant bit is the rightmost set bit. So for 0b1111100 (binary for 2,3,4,5,6), the lsb is 0b100 (position 2). Then, after XOR, the next lsb is 0b1000 (position 3). So the loop would collect 2,3,4,5,6 in order. So the sums list is already sorted. So no need to sort again.

Thus, this approach is more efficient than iterating through all possible positions.

So in code:

sums = []
current = prev
while current:
    lsb = current & -current
    pos = (lsb).bit_length() - 1
    sums.append(pos)
    current ^= lsb

Then, the sums list is already sorted in ascending order.

But wait, let's test with a sample:

Sample 1:

After processing, prev has bits set at 2,3,4,5,6. The binary is 0b111110. Let's see:

current = 0b111110 (62 in decimal)

lsb = 62 & -62 → 2. Because 62 in binary is 111110, and -62 is ... (two's complement). 62 & -62 is 2 (binary 10). Then pos is (2). Then current becomes 62 - 2 = 60 → 111100.

Next iteration:

lsb is 4 (100), pos is 2 → wait, no. Wait, 60 is 111100. 60 & -60 → 000100 (binary 4). (lsb.bit_length() -1 is 2 for 4? Wait, 4 in binary is 100, which has a bit_length of 3. 3-1=2. So pos is 2. But that's 4. So no, this approach is incorrect.

Wait, no. The bit_length of 4 is 3, so 3-1=2. But 4 is 2^2. So the position is 2. So 4 is 2^2. So the code is correct. Wait, wait, the code's pos is (lsb).bit_length() -1. For example, lsb is 4 (100), which is 2^2. So bit_length is 3 (since 100 is 3 digits), so 3-1=2. So pos is 2. But that's the exponent, not the value. Oh wait, no. The position is the exponent. So for 4, the position is 2. So the code is correct.

But the sum is 4, not 2. Wait, no. The lsb represents the sum. For example, if the sum is 4, then the bit is set at position 4, which is 2^4. Wait, no. Wait, the sum s is stored as the bit at position s. So for sum 4, the bit is 1 << 4. So the code's lsb is 1 << s, and pos is s.

Wait, let's think again. The sum s is represented by the bit at position s. So if s is 2, the bit is 1 << 2 = 4. So (lsb).bit_length() -1 for 4 is 2, which is correct. So the code is correct.

In the sample 1, the code would collect the sums 2,3,4,5,6 in order. So the output is correct.

Another example: in the third sample input:

3 3

3 5 11

The possible sums are 9, 11, 13, 15, 17, 19, 21, 25, 27, 33. Let's see. The code would collect these in order. So the code is correct.

So the code to collect the sums is as follows:

sums = []
current = prev
while current:
    lsb = current & -current
    pos = (lsb).bit_length() -1
    sums.append(pos)
    current ^= lsb

Then, print the sums separated by spaces.

Putting it all together, the code would be:

n, k = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a))  # Remove duplicates

prev = 1  # represents sum 0 (for 0 items)
for _ in range(k):
    curr = 0
    for num in a:
        curr |= prev << num
    prev = curr

sums = []
current = prev
while current:
    lsb = current & -current
    pos = (lsb).bit_length() - 1
    sums.append(pos)
    current ^= lsb

print(' '.join(map(str, sums)))

Wait, but what if prev is zero? Like in the case where no possible sums exist (but according to the problem statement, the thief takes exactly k items. So if a is empty, but according to the constraints, n is at least 1, so a can't be empty. So prev will be non-zero.

But in code, if after k steps, prev is zero (but that's impossible because there are a_i's and the thief can take exactly k items).

So this code should work.

Testing the first sample:

Input:
3 2
1 2 3

After deduplication, a is [1,2,3].

prev starts as 1 (sum 0, 0 items).

First iteration (k=1):

curr = 0
for each a_i:
    shift prev (1) by a_i:
    for 1: 1 << 1 = 2 → binary 10.
    for 2: 1 << 2 =4 → 100.
    for 3: 1<<3=8 →1000.
    OR them: 10 | 100 | 1000 = 1110 (14 in decimal). So curr is 14 (sums 1,2,3).

prev becomes 14.

Second iteration (k=2):

curr = 0.

For each a_i (1,2,3):

prev is 14 (binary 1110). Shifting by 1:

1110 <<1 = 11100 (sums 2,3,4). OR into curr.

Shifting by 2: 1110 <<2 → 111000 (sums 3,4,5). OR into curr.

Shifting by 3: 1110 <<3 → 1110000 (sums 4,5,6). OR into curr.

So curr is 11100 | 111000 | 1110000 → 11100 (12) | 111000 (56) → 111100 (60) | 1110000 (112) → 1111100 (124). So binary 1111100 is 124. The bits set are positions 2,3,4,5,6. So sums are 2,3,4,5,6. Which matches the sample.

So code works.

The second sample:

5 5

1 1 1 1 1.

After deduplication, a is [1].

prev starts as 1.

After 5 iterations:

Each time, curr is prev <<1.

First iteration: 1 <<1 = 2 (sum 1).

Second iteration: 2 <<1 =4 (sum 2).

After 5 times: sum is 5, so the bit is 1 <<5 =32.

So sums is [5], which matches the sample.

Third sample:

3 3

3 5 11.

After deduplication, a is [3,5,11].

prev starts as 1.

Iteration 1 (m=1):

sums are 3,5,11.

prev is 1 <<3 | 1<<5 | 1<<11 → 8 +32 +2048 = 2088.

Iteration 2 (m=2):

for each a_i:

prev <<3: 2088 <<3 = 16704 (sums 6, 8, 14, 16, ...).

prev <<5: 2088 <<5 = 66816 (sums 8, 10, 16, ...).

prev <<11: 2088 <<11 = 2088*2048=4,280, 832.

But ORing these gives all possible sums of two a_i's.

After three iterations, the code would generate the possible sums for three a_i's. The code correctly generates the required output.

So this approach should work.

Now, considering the time and memory constraints. For Python, using integers to represent the bits is efficient. For example, even for 1e6 bits, the integer can be handled as a long integer. Shifting and OR operations are optimized in C for Python, so even large numbers are manageable.

Testing for k=1000 and a_i=1000 (maximum possible sum 1e6). Then, the code runs k=1000 loops, each loop processing up to 1e3 a_i's. For each a_i, the shift and OR operations take O(1) time in Python (as the integer operations are handled in C). So 1e3 * 1e3 = 1e6 operations, which is acceptable for Python within 5 seconds.

The space used is minimal, as only prev and curr are stored as integers.

Thus, this code should be efficient enough for the problem's constraints.
</think>

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a))  # Remove duplicates to optimize processing

prev = 1  # Initially represents sum 0 with 0 items (bit 0 set)

for _ in range(k):
    curr = 0
    for num in a:
        curr |= prev << num
    prev = curr

# Extract all possible sums from the bitmask
sums = []
current = prev
while current:
    lsb = current & -current
    pos = (lsb).bit_length() - 1
    sums.append(pos)
    current ^= lsb

print(' '.join(map(str, sums)))
```