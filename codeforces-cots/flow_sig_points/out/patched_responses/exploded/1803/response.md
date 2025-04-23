<think>
Okay, I need to solve this problem. Let me read the problem statement carefully.

So, the problem is about permutations of wise men and generating binary strings based on whether consecutive men in the permutation know each other. For each possible binary string of length n-1, we have to find how many permutations produce that string.

Hmm. The input gives the adjacency matrix of the wise men. Each permutation of the n men gives a binary string s of length n-1, where each s_i is 1 if the i-th and (i+1)-th in the permutation know each other. For all possible s (which are 2^(n-1) possibilities), output the count of permutations that result in each s.

Constraints are n up to 14. Oh, that's a bit tricky. Because 14! is a huge number, so brute-forcing all permutations is impossible. For n=14, even 14! is about 87 billion, which is way too big.

So, the approach has to be dynamic programming with bitmasking or some kind of state compression. Let's think.

Each permutation can be built step by step, adding elements one by one. But how to track the necessary information for the binary string s.

Wait, the binary string s depends on the consecutive pairs in the permutation. So, for a permutation p1, p2, ..., pn, s is s_1 to s_{n-1}, where s_i is 1 if p_i and p_{i+1} are connected.

So, to model this, when building a permutation incrementally, we need to track the last element added and the current state of the binary string's bits. But the problem is that the binary string's bits depend on the entire sequence of consecutive pairs in the permutation. For example, the first bit is the first two elements, the next bit is the second and third, etc. So, the entire path of the permutation's order determines the binary string.

But the binary string is of length n-1. For each permutation, all the bits are determined. However, for a dynamic programming approach, we need to track the necessary information that allows us to compute the binary string as we build the permutation.

Wait, the key observation here is that the binary string s is determined by the consecutive pairs in the permutation. So, when building a permutation step by step (e.g., adding elements one by one), the binary string s is built step by step as each new element is added. For example, when adding the third element to a permutation of two elements, the second bit of s is determined by the adjacency between the second and third elements.

Therefore, the state in the DP must include the current position (i.e., the length of the permutation built so far), the last element in the permutation (since the next element's adjacency with this last element will determine the next bit in the binary string), and the bits of the s string that have been determined so far.

But wait, the bits of s are built in order. For example, the first bit (s_1) is determined by the first two elements, the second bit (s_2) by the second and third, etc. So, when building a permutation of length k (k elements), the first k-1 bits are determined. So, for a permutation of length k, the state needs to track the current bits up to position k-1.

But for n=14, the binary string can have up to 13 bits. So, tracking the entire binary string as part of the state is feasible, since 2^13 is 8192 possible binary strings. But for each permutation step, we have to track the current state of the binary string, the last element in the permutation, and which elements have already been used.

Wait, but the DP state would be:

dp[mask][last][s] = number of permutations where:

- mask is a bitmask representing the set of used elements (since n is up to 14, mask can be 14 bits, which is manageable as 2^14=16384)

- last is the last element in the current permutation (0-based, perhaps, from 0 to n-1)

- s is the binary string (up to 13 bits, so 2^13=8192 possible values)

The total number of states would be 16384 (mask) * 14 (last) * 8192 (s) = 16384 *14 * 8192. Let's compute that:

16384 * 14 = 229376, multiplied by 8192 gives 229376 * 8192 = 1,880,840,192. That's about 1.8 billion states. Which is way too big for Python, even with optimizations. So, this approach is not feasible.

Alternative idea: Since the binary string is built step by step as the permutation is constructed, each step adds a new bit. So, when adding a new element to the permutation, the new bit is determined by the adjacency between the last element and the new element.

Wait, for example, when building a permutation of k elements, the first k-1 bits are already set. Adding the (k+1)-th element adds the k-th bit. Because the bits are in order: the first bit is between positions 1 and 2, the second between 2 and 3, etc. So, when building a permutation step by step, each time we add a new element, the new bit is determined by the previous last element and the new one.

So, the DP state could be:

mask: the set of used elements (n bits)

last: the last element in the permutation (n possibilities)

bits: the bits of the binary string that have been generated so far. Since each step adds a new bit when the permutation grows in length, the number of bits in the state is equal to the length of the permutation minus one.

Wait, for example:

- mask has k elements (k bits set). Then, the permutation has k elements. The number of bits in the binary string so far is (k-1). Because each step of adding an element contributes one bit (except the first element, which contributes nothing).

So, when mask has only one element (k=1), the binary string has zero bits. When mask has two elements, the binary string has one bit. When mask has three elements, two bits, etc. So, the binary string's current length is (number of elements in mask) - 1.

Therefore, the DP state can be represented as:

mask (n bits), last (n possibilities), s (current binary string bits, which has (number of elements in mask - 1) bits).

But wait, the binary string s for the permutation is determined by the sequence of consecutive elements. So, when the permutation is of length k, the binary string s has (k-1) bits. So, the s in the DP state for a permutation of length k is a (k-1)-bit string. But the problem requires that for each possible (n-1)-bit string, we count the permutations. So, the DP must track the entire s up to (k-1) bits as the permutation is built.

But for n=14, the s can be up to 13 bits. However, when the permutation is not complete (mask is not full), the s is shorter than 13 bits. For example, when mask has 5 elements, s is 4 bits. So, the state must track the entire s bits generated so far.

But the problem is that the s can have varying lengths. So, the DP state for mask with k elements will have s of length k-1. However, for the final answer, we need the s of length n-1. So, the DP must track the entire s up to the current permutation's length.

But how can this be done efficiently?

Alternative approach: The DP state is mask, last, and the entire s that has been generated so far. The s is a bitmask of length up to 13. But when mask has k elements, the s is (k-1) bits. So, for each state, the number of bits in s is determined by the mask. For example, mask with 3 elements (binary 111) would have s with 2 bits.

Wait, but how do we handle the varying bits? Because for a mask of size k, s is a (k-1)-bit number. But when adding a new element, the new s is formed by appending a new bit (the adjacency between the last element and the new element).

So, perhaps the DP can be built incrementally. For each mask, and last element, and current s (of length k-1 where k is the population count of mask), when adding a new element, we compute the new bit (adjacency between last and new), append it to s, and transition to the new state with mask | (1<<new), new as last, and new s.

This seems plausible. The problem is that for n=14, the number of possible s values can be up to 2^13=8192. The mask can be 2^14=16384, and last can be 14 possibilities. So, the state is mask (16384) × last (14) × s (up to 8192 for full mask). But for intermediate masks (like when mask has 7 elements, s is 6 bits, so 2^6=64 possibilities), the s part is smaller.

But even so, the total number of states could be manageable. Let's calculate for each mask size:

For each possible mask with k bits set:

- The number of possible s is 2^(k-1).

- The number of masks with k bits set is C(n, k).

For each such mask, last can be any of the k elements, and s can be 2^(k-1) possibilities.

So, for each k (from 1 to n), the total number of states for that k is C(n, k) × k × 2^{k-1}.

Summing this over k=1 to n:

Total states = sum_{k=1 to 14} [C(14, k) * k * 2^{k-1} } ]

Let's compute this sum.

For example:

For k=1: C(14,1)*1 *2^0 =14 *1*1=14.

For k=2: C(14,2)*2 *2^1= 91 *2 *2= 364.

k=3: C(14,3)*3 *4= 364 *3 *4= 4368.

k=4: C(14,4)*4 *8= 1001 *4 *8= 32032.

k=5: 2002 *5 *16= 2002 *80 = 160,160.

k=6: 3003 *6 *32= 3003 *192= 576,576.

k=7: 3432 *7 *64= 3432*448= 1,537, 536.

k=8: 3003*8*128= 3003 *1024= 3,075,072.

k=9: 2002*9*256= 2002*2304= 4,615, 648? Let me compute 2002*2304: 2000*2304=4,608,000; 2*2304=4608 → total 4,612,608.

k=10: 1001*10*512= 1001*5120= 5,125,120.

k=11: 364 *11*1024= 364*11264= 4, 097, 216?

Wait 364 * 11264: 364 * 10,000 = 3,640,000; 364 * 1,264 = 364*(1200+64) = 364*1200=436,800 + 364*64=23,296 → total 3,640,000 + 436,800 +23,296 = 4,100,096.

k=12: 91*12*2048= 91*24,576= 2,236, 416? Let's compute 91 *24,576: 90*24,576 = 2,211,840; 1*24,576=24,576 → total 2,236,416.

k=13: 14*13*4096= 14*53,248= 745,472.

k=14: 1 *14 *8192= 114,688.

Now, summing all these up. Let's see:

k=1:14 → total 14.

k=2:364 → 378.

k=3:4368 → 4746.

k=4:32,032 → 36,778.

k=5:160,160 → 196,938.

k=6:576,576 → 773,514.

k=7:1,537,536 → 2,311,050.

k=8:3,075,072 → 5,386,122.

k=9:4,612,608 → 9,998,730.

k=10:5,125,120 → 15,123,850.

k=11:4,100,096 → 19,223,946.

k=12:2,236,416 → 21,460,362.

k=13:745,472 → 22,205,834.

k=14:114,688 → 22,320,522.

So the total number of states is about 22 million. That's manageable in Python, but we have to use efficient data structures and optimize the code.

The plan is to use dynamic programming where for each state (mask, last, s), we track the number of permutations that reach that state. Then, when the mask is full (all n bits set), the s is of length n-1, and we can accumulate the count for that s.

So the steps are:

1. Precompute the adjacency matrix from the input.

2. Initialize the DP: for each single element (mask with one bit set, last is that element, s is empty). For mask with one element (k=1), the s is 0 bits, so we represent it as 0 (but since the length is 0, perhaps the value is not used; but in the code, when adding a new element, the s is built by appending bits).

Wait, for mask with one element, the permutation is just that element, so no bits are set. So the initial state is mask=1<<i, last=i, s=0 (but s here is 0 bits, so the value is 0 but the length is 0).

But in the DP, when we process mask of size 1 (k=1), and when adding a new element, the mask becomes size 2. Then, the s for the new state is the adjacency between the previous last (i) and the new element (j). So, the s for the new state is a 1-bit value (0 or 1). Then, the DP transitions for mask= (1<<i | 1<<j), last=j, s = (adj[i][j]).

So the initial state for each i is mask=1<<i, last=i, s=0 (but since the s has 0 bits, perhaps the code can treat s as 0 (but in the transitions, when we append a bit, the s is shifted left and the new bit is added. For example, when the current s is of length l, appending a bit makes it length l+1. So for the initial state (s length 0), appending a bit makes the s length 1.

So, the initial DP is:

dp[mask][last][s] = 1 for mask=1<<i, last=i, s=0 (but s has 0 bits here). So, for each i, we have a starting state.

But in Python, representing the DP as a dictionary or a list of dictionaries may be possible. However, given the number of states (22 million), using lists and preallocating the possible states would be more efficient.

But given that Python's dictionaries are not as fast as arrays, perhaps using a 3-dimensional array where each dimension is mask, last, and s. But the mask can be up to 14 bits (16384 possibilities), last can be 14, and s up to 13 bits (8192). However, for each mask, the possible s is determined by the number of set bits in mask minus one. For example, mask with k bits set can have s up to 2^{k-1} possible values.

But storing a 3D array for all possible masks, last, and s is not feasible in memory. For example, 16384 masks ×14 last ×8192 s would be 16384×14×8192 = 1.8 billion entries, which is way too big.

Alternative approach: For each step (mask with k bits set), process the states for that mask, and represent the DP transitions using a dictionary or a list of current states. For each mask, we can process the possible (last, s) pairs and compute transitions to the next mask by adding an unused element.

So, the code can process the masks in order of increasing number of set bits. For each mask, and each possible (last, s) in the DP for that mask, and for each possible next element not in the mask, compute the new mask, new last (the next element), and new s (current s shifted left by 1, OR with the adjacency bit between last and next element).

This way, we can handle the transitions efficiently.

So, the steps would be:

- Precompute adjacency matrix as adj[i][j] = 1 if i and j know each other, else 0.

- For each mask in order of increasing population count (from 1 to n):

   - For each (last, s) in the current mask's DP entries:

      - For each possible next element j not in mask:

         - Compute the bit to append: adj[last][j]

         - new_mask = mask | (1<<j)

         - new_s = (s << 1) | adj[last][j]

         - Update the DP for new_mask, last=j, new_s by adding the current count.

This approach iterates through all possible transitions, and accumulates the counts.

The DP can be represented as a list of dictionaries, where for each mask, we have a dictionary that maps (last, s) to the count. But for efficiency, perhaps using a list of defaultdicts or some optimized structure.

But for Python, even with n=14, and 22 million total transitions, it's manageable if the code is optimized.

So, let's think about how to represent the DP.

Initially, for mask with 1 bit set (each individual element), the DP entries are (last=i, s=0). The count is 1 for each i.

Wait, but when mask is 1<<i, the s is 0 bits. So when we add a new element j, the s becomes 1 bit: adj[i][j].

So, for the first step (mask size 1), the s is 0 bits. When adding j, the new s is adj[i][j], which is 1 bit.

Then, for mask size 2, the s is 1 bit.

So, the code can process masks in order of their population count. For each mask, process all possible (last, s) pairs. For each, try adding each possible j not in mask, compute the new_s as (s << 1) | adj[last][j], but wait, no: when the current s has k-1 bits (mask has k bits), adding a new element increases the s to k bits. So, for example:

current s is a (k-1)-bit number. When adding a new element, the new s is (s << 1) | adj[last][j], which is a (k)-bit number.

But wait, for the mask with k bits, the s has (k-1) bits. So, when we add a new element, the s becomes (k) bits. So, for the transition, the new_s is (current s) << 1 | adj[last][j].

But for example, if current s is 0 (0 bits, when k=1), then adding j gives new_s = (0 << 1) | adj[i][j] → adj[i][j], which is 1 bit.

Yes. So this logic holds.

Thus, the code can be structured as:

Initialize a dictionary (or list) for each mask. For mask with 1 bit set, the entries are (last, 0) with count 1.

Then, iterate through all masks in order of increasing population count.

For each mask:

   For each (last, s) in the current mask's DP entries:

      For each j not in mask:

          bit = adj[last][j]

          new_mask = mask | (1<<j)

          new_s = (s << 1) | bit

          Increment the count for new_mask, last=j, new_s by the current count.

Once all masks are processed, the final answer is the counts for mask = (1<<n) -1 (all bits set), and all possible s of length n-1. Then, for each x in 0..2^{n-1}-1, output the count for s equal to x.

But how to handle the s in the output order? The problem states that the x-th position corresponds to the binary string s where s_i is floor(x / 2^{i-1}) mod 2. Wait, that's equivalent to the binary representation of x, but reversed.

Wait, let's see:

The problem statement says for x, the binary string s is such that s_i = floor(x / 2^{i-1}) mod 2 for 1 ≤ i ≤ n-1.

For example, x in binary is written as s_1 s_2 ... s_{n-1}, where s_1 is the least significant bit (since 2^0 is the divisor for i=1). So, the binary representation of x is s_1 s_2 ... s_{n-1} as bits from least to most significant. So, for x=3 (binary 11), the string s would be 11, but with s_1 = 1, s_2=1.

Wait, for x=3, which is 11 in binary, the string s would be 11 for n-1=2. But according to the problem's definition:

i ranges from 1 to n-1. For i=1, s_1 is (x / 2^0) mod 2 → x mod 2. For i=2, (x / 2^1) mod 2. So, s_1 is the least significant bit (LSB), s_2 the next, etc. So the binary string is s_1, s_2, ..., s_{n-1}, which is the reverse of the standard binary representation (where the LSB is the rightmost bit). For example, x=5 (binary 101) would correspond to s_1=1, s_2=0, s_3=1 (for n-1=3), which is the binary string 101 but written as s_1 to s_3 as 1, 0, 1. So the string is the bits of x in reverse order of their positions.

Wait, no. Let's take x=5 (binary 101) for n-1=3.

i=1: x/(2^0) mod 2 → 5 mod 2 =1 → s_1=1.

i=2: x/(2^1) mod 2 →5//2=2, 2 mod 2=0 → s_2=0.

i=3: x/(2^2) mod 2 →5//4=1 →1 mod2=1 → s_3=1.

So the string s is "1 0 1", which is 101. Which is the binary representation of x (5 is 101). Wait, but the binary representation of 5 is 101, which is the same as the string s. So for this example, the order is the same as the binary digits. But that's because when you take the bits in the order of s_1 to s_{n-1}, each bit is the i-th bit of x, where the bits are ordered from least significant to most significant. So the string s is the binary representation of x, written as s_1 (LSB) to s_{n-1} (MSB).

Wait, for x=5 (binary 101), which is 1*2^2 +0*2^1 +1*2^0=5. The bits are written as s_1=1 (LSB), s_2=0, s_3=1 (MSB). So the string s is "101", which is the same as the binary representation of x=5. So in this case, the string s is the binary digits of x in reverse order? No, because x=5 is 101, and s is 101. So it's the same order.

Wait, no. Wait, for example, x=6 (binary 110), which is 6= 1*2^2 +1*2^1 +0*2^0. The string s would be s_1=0, s_2=1, s_3=1. So the string s is "0 1 1", which is 011. But x=6 is 110. So the s is the reverse of the binary digits.

Ah, so the problem's definition of s is that the bits are ordered from least significant to most significant. So the binary string s is the bits of x in the order of the LSB first, MSB last. So for x=6 (binary 110, which is 6= 6= 1*4 + 1*2 + 0*1), the s string would be 0 (s_1) followed by 1 (s_2) followed by 1 (s_3). So the string is "011".

But x=6's binary is 110, which is MSB first. So the s string is the reverse of the binary digits.

Therefore, to map x to the corresponding s string, s is the reverse of the binary digits of x. Wait, no. Let's see: x=6 is 110 in binary (3 bits). So the bits are 1 (MSB, 2^2), 1 (2^1), 0 (2^0). For the s string, s_1 is x mod 2 →0, s_2 is (x//2) mod 2 → (3 mod2)=1, s_3 is (x//4) mod2 → (1 mod2)=1. So s is 0,1,1 → "011", which is the reverse of x's binary digits (110 → reversed is 011). So for x=6, s is "011".

Thus, the s string for x is the reverse of the binary digits of x. So, the output order is such that the x-th entry corresponds to the s string which is the reverse of the binary digits of x (with leading zeros to make it length n-1).

So, when generating the answer, the count for x is the number of permutations that generate the s string which is the reverse of the binary digits of x.

Wait, but the problem statement says that for x, the s string is constructed as s_i = floor(x / 2^{i-1}) mod 2. So for each i, s_i is the (i-1)th bit of x (since dividing by 2^{i-1} and mod 2 gives the (i-1)th bit, starting from 0).

For example, x=5 is 101 in binary. The bits are:

bit 0: 1 (2^0)

bit 1: 0 (2^1)

bit 2: 1 (2^2)

For i=1: 2^{i-1} = 2^0 → bit 0.

i=2: 2^1 → bit 1.

i=3: 2^2 → bit 2.

Thus, s_1 is bit 0, s_2 is bit 1, s_3 is bit 2. So the s string is s_1, s_2, s_3 → which is the bits of x in the order of bit 0, bit 1, bit 2. So the s string is the binary digits of x written in reverse order (since binary is written as bit 2, bit 1, bit 0 for x=5, which is 101).

Thus, to get the s string for x, we take the binary representation of x, pad it with leading zeros to make it n-1 bits, reverse the bits, and that's the s string.

Therefore, in the DP, when we have the full mask (all bits set), the s is a (n-1)-bit number. For each such s, we need to map it to x such that the bits of x are the reverse of s. Wait, no. Because the s stored in the DP is the concatenated bits from the permutation steps. For example, s in the DP for the full mask is the sequence of bits s_1, s_2, ..., s_{n-1}, where s_i is the adjacency between the i-th and (i+1)-th elements in the permutation. 

But according to the problem's output, the x-th entry corresponds to the s string where s_i = floor(x / 2^{i-1}) mod 2. So for x=0, all s_i are 0. For x=1, s_1=1, others 0. For x=2, s_2=1, others 0. Etc.

Therefore, the DP's s is the same as the x's binary representation, but with the bits ordered as s_1 (LSB of x), s_2 (next bit), etc.

For example, in the first sample input:

The output is 0 0 0 6.

The input is 3 wise men who all know each other. So any permutation will have s_1=1 and s_2=1. The s string is 11. The x corresponding to this is 3, because x=3 in binary is 11. According to the problem's s definition, s_1=3 mod 2=1, s_2= (3//2) mod 2=1. So the x is 3. The output's fourth entry (x+1=4) is 6. Which matches the sample.

So, the DP's final s for the full mask is the s string as per the problem's definition. Thus, for each x in 0..2^{n-1}-1, the count is the number of permutations that generate s as x's bits according to the problem's definition.

Therefore, once the DP is completed, for the full mask, the counts are stored in the DP entries (last can be anything, but mask is full), and the s is the x's binary bits as per the problem's definition. So, to collect the answer, we need to aggregate all the counts for each s in the full mask's DP entries.

Thus, after processing all masks, the full mask (all bits set) has all possible s values of length n-1. For each s in the full mask's DP entries, we sum all counts across all possible last elements.

So, the code will:

- For the full mask (mask = (1<<n) -1), collect all s and their counts. Then, for each x from 0 to 2^(n-1) -1, compute the corresponding s (the bits of x as per the problem's definition) and output the count for that s.

But how to compute s for a given x?

Wait, the x represents the s string according to the problem's definition. So, for each x, the s string is constructed as follows: for each position i (1-based), s_i is the (i-1)th bit of x (starting from LSB). So, the s string is the binary representation of x, but each bit is in the order of their positions in the binary digits of x. For example, x=5 (binary 101) would have s_1=1 (LSB), s_2=0, s_3=1 (MSB of x). So the s string is 1,0,1 → 101, which is x's binary digits in the same order.

Wait, this seems contradictory. Let's take x=5 (binary 101) and n-1=3. So, the s string has three bits.

s_1 = x mod 2 → 1.

s_2 = (x//2) mod 2 → (5//2)=2 mod 2 →0.

s_3 = (x//4) mod 2 →5//4=1 mod2 →1.

So s string is 1 0 1 → which is the same as x's binary digits. So for x=5, the s string is 101. So the x's binary representation is the same as the s string.

But in this case, the order of the bits is preserved. So, the x's binary representation (with leading zeros to make it n-1 bits) is the s string. So, for example, x=3 (binary 11) and n-1=3 would be 011, so s string is 011.

Wait, but n-1 is 3, so x can be up to 7 (111). So, for x=3, the binary is 11, which padded to 3 bits is 011. Then, s_1=3 mod2=1, s_2=3//2=1 mod2=1, s_3=3//4=0 mod2=0. So the s string is 110 → s_1=1, s_2=1, s_3=0. Wait, no. Wait, for x=3 and n-1=3:

i ranges from 1 to 3.

s_1 = 3 mod 2 → 1.

s_2 = (3//2) mod2 →1 mod2=1.

s_3 = (3//4) mod2 →0 mod2=0.

So s string is 1 1 0 → 110, which is the binary representation of 6 (110). But x is 3.

Ah, I see. So this is the crux. So, the s string for x is not the same as the binary digits of x. Instead, the s string is the binary digits of x, but interpreted in reverse. Because for x=3 (binary 11), the s string for n-1=3 is 110, which is 6. So the s string is the binary digits of x, left-padded with zeros to length (n-1), and then reversed.

Wait, but in this case, x=3 would have a binary of 11, padded to 3 bits as 011. The s string would be 110 (reverse of 011). So x=3's s string is 110, which is 6.

Thus, the s string for x is the reverse of the binary representation of x, padded to (n-1) bits.

Therefore, for each x, the corresponding s in the DP is the reverse of x's binary string (padded to (n-1) bits), converted to an integer.

So, to map x to the s value stored in the DP, we need to:

1. Convert x to a binary string of length (n-1), padding with leading zeros.

2. Reverse the binary string.

3. Convert this reversed string to an integer, which is the s value used in the DP.

For example, x=3 (binary 11, padded to 3 bits as 011 → reversed is 110 → which is 6. So s=6.

But wait, in the first sample input, the output is 0 0 0 6. Which corresponds to x=0 (000 → reversed 000 → s=0), x=1 (001 → reversed 100 → s=4), x=2 (010 → reversed 010 → s=2), x=3 (011 → reversed 110 → s=6). The sample output shows that the fourth number (x=3) is 6, which is the count for s=6.

In the first sample, all permutations produce the s string 11 (for n=3, the string has two bits), which is 3 in binary. Reversed, it's 11 (two bits) → 3. So in the DP, the s would be 3. But according to the sample, the output for x=3 (binary 11) is 6. Wait, this seems conflicting.

Wait, n=3, so n-1=2. So the s string for the permutation is two bits. For example, the permutation 1,2,3 (all connected) has s=11 (binary), which is 3. The corresponding x would be 3's binary, but reversed. So, for two bits, x=3 (binary 11) reversed is 11 → 3. So the s string is 3. But according to the sample, the output for x=3 is 6. Wait, but the sample output shows that for the first test case, the fourth number (x=3) is 6. Because x ranges from 0 to 3 (2^2-1=3), the output is four numbers. For x=3, s is 3. The sample's output shows that this is 6, which is the correct count. So the code's DP for s=3 would have a count of 6.

But according to our previous analysis, x=3 corresponds to s=3. So how does this fit?

Ah, because for n-1=2, the s stored in the DP is a 2-bit number. x=3 in binary is 11, which corresponds to s_1=3 mod2=1, s_2=3//2 mod2=1. So the s string is 11, which is 3. So in the DP's final entries, the count for s=3 is 6, which matches the sample. So in this case, the x's binary is the same as the s string. So no reversal is needed. But this contradicts the previous example where x=3 and n-1=3 required reversal.

Wait, perhaps I made a mistake in the previous analysis. Let me re-examine.

For x=3 (binary 11) when n-1=2, s has two bits. s_1 is x mod2=1, s_2 is (x//2) mod2=1. So the s string is 11, which is 3. So no reversal is needed. So for the first sample, the DP's s=3 has count 6.

But according to the sample, the fourth number (x=3) is 6, which matches. So the s for x is the same as the binary representation of x, but with each bit determined by the formula s_i = (x >> (i-1)) & 1. So for each x, the s string is the collection of bits (x's bits), where each bit is (x >> (i-1)) &1. For example, for x=3 (binary 11), and i=1,2 (n-1=2), the bits are 1, 1. So s is 11, which is 3. So in the DP, the s is 3, and the count is 6. So the x's s is directly the s stored in the DP. Therefore, no reversal is needed. So the previous analysis about reversal was incorrect.

So, the mapping between x and the s in the DP is straightforward: x is the integer representation of the s string, with s_1 as the least significant bit (bit 0 of x), s_2 as bit 1 of x, and so on. For example, s_1 is the 0th bit, s_2 is the 1st bit, etc.

Therefore, to get the count for x, we need to look up the DP's s value equal to x. Because the s in the DP is exactly the binary number formed by the bits s_1, s_2, ..., s_{n-1}, which corresponds to x.

Wait, but how? Let's see:

x is an integer. The s string for x is determined by the formula s_i = (x >> (i-1)) &1. So, the s string is a sequence of bits where the first bit is (x & 1), the second bit is (x >>1) &1, etc. So, the s string is the binary representation of x, written in the order of the bits from least significant to most significant. For example, x=5 (binary 101) would have s_1=1 (bit 0), s_2=0 (bit 1), s_3=1 (bit 2). So the s string is 101, which is 5 in decimal. Therefore, s in the DP is exactly x. So, for each x, the count is the number of permutations that generate s=x.

Therefore, the answer is simply for each x in 0 to 2^{n-1}-1, output the count of s=x in the DP for the full mask.

Thus, the code can, after processing all masks, collect the counts for the full mask's s values and output them in order of x from 0 to 2^{n-1}-1.

So, the code steps:

- Read n.

- Read the adjacency matrix. Since the matrix is symmetric (as per the problem statement), but each entry is the adjacency between i and j.

But in the input, the j-th character of the i-th line is '1' if i knows j. Since the relation is symmetric, but the input may have redundant information. However, the code can read each line, and for adj[i][j], set adj[i][j] = (input[i][j] == '1').

But since the problem states that the adjacency matrix is symmetric (if i knows j, j knows i), but the code can read it directly.

Once adj is read, the code proceeds with the DP.

The DP can be represented using a dictionary for each mask. For example, a list of dictionaries, where for each mask, we have a dictionary that maps (last, s) to the count.

But for efficiency, perhaps using a defaultdict for each mask. However, in Python, handling masks up to 16384, and for each mask, a dictionary of (last, s) → count, may be feasible.

Alternatively, for each mask, the code can keep a dictionary of (last, s) → count. But given that for each mask, the s's bit length is determined by the mask's population count minus one, perhaps we can process the masks in order of increasing population count.

The code outline:

Initialize the DP.

For each i in 0..n-1:

   mask = 1 << i

   dp[mask][(i, 0)] = 1

Then, for each mask in order of increasing population count:

   for each (last, s) in dp[mask].items():

       for j in 0..n-1:

           if not (mask & (1 << j)):

               bit = adj[last][j]

               new_mask = mask | (1 << j)

               new_s = (s << 1) | bit

               dp[new_mask][ (j, new_s) ] += dp[mask][ (last, s) ]

Once all masks are processed, the final answer is the counts for mask = (1 << n) -1. For this mask, collect all s values and their counts (summing over all possible last elements).

Finally, for each x in 0 to 2^{n-1} -1:

   output the count for x.

But in Python, how to manage the DP for each mask.

Implementing this requires a way to store for each mask, the current (last, s) pairs and their counts. For Python, using a list of defaultdict or a dictionary where the keys are masks and the values are other dictionaries may be feasible.

But for efficiency, using a list where each index is a mask, and each entry is a defaultdict that maps (last, s) tuples to counts.

But for n=14, mask can be up to 2^14=16384. So a list of size 16384, where each element is a defaultdict. But in Python, initializing this may take some time.

Alternative approach: Use a dictionary to track the current states. For each mask, we can process it once all masks with smaller population counts have been processed.

But how to process masks in order of increasing population count.

An efficient way is to precompute the order of masks by their population count. For example, create a list of masks sorted by the number of set bits. This can be done by generating all masks from 1 to (1<<n) -1, and sorting them based on the bit count.

Once the masks are sorted, the code can iterate through them in order.

So, in code:

n = int(input())

adj = []
for _ in range(n):
    s = input().strip()
    adj.append( [int(c) for c in s] )

from collections import defaultdict

max_mask = 1 << n

# Precompute the order of masks sorted by the number of bits.
masks = []
for mask in range(max_mask):
    if mask ==0:
        continue
    masks.append(mask)

masks.sort(key=lambda x: bin(x).count('1'))

# Initialize DP: a dictionary where for each mask, we have a defaultdict that maps (last, s) to count.
dp = [defaultdict(int) for _ in range(max_mask)]

for i in range(n):
    mask = 1 << i
    dp[mask][ (i, 0) ] = 1

for mask in masks:
    # Current mask's population count is k = bin(mask).bit_count()
    k = bin(mask).count('1')
    if k ==1:
        continue  # already initialized
    # Iterate over all (last, s) pairs in the current mask's DP
    current_dp = dp[mask]
    # Wait, no. The masks are processed in order of increasing population count. But the code above has already initialized the masks with population count 1. Then, when processing a mask, we have to consider transitions from masks with smaller population counts.
    # Wait, no. The current loop is for mask in masks (sorted by population count). So, masks are processed in order of increasing k. Thus, when processing mask, all transitions to mask would have come from masks with k-1 bits set. So, perhaps the code above is wrong. Because the code as written is processing each mask in order, and for each, processing their (last, s) pairs. But the transitions to new_mask would be adding to the new_mask's DP. So, for each mask in the sorted list (by k), we process all possible transitions from mask to new_mask. But the code as written for the DP would have the mask's DP entries already filled.

But the code as written above is incorrect. Because when you process mask, the transitions from mask are to new_mask. But new_mask is a mask with k+1 bits set, which would be processed later (since masks are sorted by increasing k).

Wait, the code is as follows:

- For each mask in the sorted list (order of increasing k):

   For each (last, s) in dp[mask]:

      For each j not in mask:

          new_mask = mask | (1<<j)

          new_s = (s << 1) | adj[last][j]

          dp[new_mask][ (j, new_s) ] += dp[mask][ (last, s) ]

So, for each mask (with k bits), we process all transitions to new_mask (k+1 bits), and accumulate counts in new_mask's DP entries.

This is correct. Because when processing mask with k bits, all masks with k+1 bits have not been processed yet (since masks are sorted in increasing k order). So, the transitions to new_mask (k+1 bits) are computed before new_mask is processed.

Yes, this is the correct approach. So, the code is correct.

Once all masks are processed, the final mask is (1<<n) -1. For this mask, collect all s values and their counts.

But in the DP for this mask, each entry is (last, s) → count. So, for each s, we need to sum all counts for all possible last.

So:

final_counts = defaultdict(int)
full_mask = (1<<n) -1
for (last, s), cnt in dp[full_mask].items():
    final_counts[s] += cnt

Then, the output is a list of 2^(n-1) entries, where each entry x is final_counts[x].

But the order is x from 0 to 2^(n-1) -1.

So, the output is:

print(' '.join( str(final_counts[x]) for x in range(2**(n-1)) ))

But in Python, for n=14, 2^13=8192 entries, which is manageable.

But let's test this approach with the first sample input:

Sample input 1:

3

011

101

110

adj matrix is:

row 0: 0 1 1

row 1: 1 0 1

row 2: 1 1 0

But since the problem states that the adjacency matrix is symmetric, and no man knows himself (diagonal is 0).

So for all i and j, adj[i][j] is 1 if i and j are different (since in sample 1, all know each other).

Thus, any permutation will have consecutive pairs that know each other. So for any permutation, the s string is 11 (bits 1 and 1), which is 3 (binary 11).

Thus, final_counts[3] = 6 (3! permutations). The output is 0 0 0 6, which corresponds to x=0,1,2,3. Only x=3 has count 6.

In the code, after processing all masks, the full_mask is 7 (111 in binary, which is 3 elements). For this mask, the s is 3 (binary 11). The code will collect all (last, 3) entries and sum them.

Each permutation contributes 3 as the s, so the final_counts[3] = 6.

Thus, the code should work.

Now, for the second sample input:

Sample input 2:

4

0101

1000

0001

1010

The adjacency matrix is:

row 0: 0 1 0 1

row 1: 1 0 0 0

row 2: 0 0 0 1

row 3: 1 0 1 0

But each row i is the list of known j's (columns).

But the adjacency is symmetric. For example, adj[0][1] is 1, so adj[1][0] is 1. But the input's second line is 1000, which for i=1, j=0 is 1. So adj[1][0] is 1.

But in the input, row 1 is '1000', so adj[1][j] for j=0 is 1, others are 0. So adj[1][0]=1, adj[1][1]=0, adj[1][2]=0, adj[1][3]=0.

Similarly for others.

The output is 2 2 6 2 2 6 2 2.

Which has 8 elements (2^3=8).

So the code should correctly compute the s counts.

Now, the main challenge is to implement the code efficiently in Python, given the 22 million possible states.

But with n=14, the code may take a long time, but the problem allows up to 2 seconds. For Python, this could be tight. So, we need to optimize the code as much as possible.

Possible optimizations:

1. Precompute the masks in order of increasing population count. This is already done.

2. Represent the DP as a list of defaultdicts, but using tuples (last, s) as keys. However, in Python, tuples are hashable and can be used as keys.

But for speed, perhaps using a list of dictionaries, where each dictionary uses (last << 20) | s as the key, but that may not help.

Alternatively, using a list of dictionaries where the keys are (last, s) tuples.

Another optimization is to process the transitions in a way that minimizes the number of operations. For example, precompute all possible j's not in mask for each mask.

But in Python, for each mask, checking each j in 0..n-1 to see if they are not in mask is O(n) per mask. For n=14, this is manageable.

Another optimization is to precompute the adjacency bits as a 2D array of integers.

But the code as written should be manageable.

Now, let's write the code.

The code will:

- Read n.

- Read n lines, each of length n. For each line, convert to a list of integers (0 or 1).

- Precompute the masks in order of increasing population count.

- Initialize the DP.

- Iterate through each mask in the order.

- For each (last, s) in the mask's DP, generate new transitions.

- Update the new_mask's DP entries.

- After processing all masks, collect the final counts for the full mask.

- Output the counts in order.

But in Python, using defaultdict for each mask's DP may be slow. Alternative, use a list of defaultdicts, and for each transition, increment the count.

But the code can proceed as follows:

But for the initial code, it would look like:

n = int(input())
adj = []
for _ in range(n):
    s = input().strip()
    adj.append([int(c) for c in s])

from collections import defaultdict

max_mask = 1 << n

# Precompute masks in order of increasing population count.
masks = []
for mask in range(max_mask):
    if mask == 0:
        continue
    masks.append(mask)

masks.sort(key=lambda x: bin(x).count('1'))

dp = [defaultdict(int) for _ in range(max_mask)]

for i in range(n):
    mask = 1 << i
    dp[mask][ (i, 0) ] = 1

for mask in masks:
    current_entries = list(dp[mask].items())
    for (last, s), cnt in current_entries:
        for j in range(n):
            if not (mask & (1 << j)):
                bit = adj[last][j]
                new_mask = mask | (1 << j)
                new_s = (s << 1) | bit
                dp[new_mask][ (j, new_s) ] += cnt

full_mask = (1 << n) - 1
result = [0] * (2 ** (n-1))
for (last, s), cnt in dp[full_mask].items():
    result[s] += cnt

print(' '.join(map(str, result)))

But this code may not handle the full_mask correctly. For example, the full_mask's s is a (n-1)-bit number. So for n=3, the s is 2 bits. For each x in 0..3, the code outputs result[x], which is the count of permutations that generated s=x.

This should work.

Testing the first sample:

After processing, the full_mask is 7 (binary 111). The DP for this mask will have (last, s) entries where s is 3 (binary 11). Each permutation contributes to s=3. So result[3] = 6. All other entries are 0. So the output is 0 0 0 6.

The code would generate this.

For the second sample, the code should compute the correct counts.

But for Python, the code may be too slow for n=14. Let's see.

For n=14, masks have 2^14=16384 possible values. The masks are processed in order of population count. For each mask, the number of (last, s) entries is C(n, k) * k * 2^{k-1} / (sum over k). But for k=7, this is 3432 *7 * 64= 1,537,536 entries. Processing each entry involves iterating over all possible j not in the mask (which for k=7 is 7 elements used, so 7 not in the mask, so 7 possible j's).

But for n=14, the total number of transitions is around 22 million. Python may handle this in 2 seconds if optimized, but may be tight.

Possible optimizations:

1. Use integers for last and s, and combine them into a single key. For example, for each (last, s), we can represent the key as last * (2^max_s_bits) + s. But for s up to 2^13=8192, and last up to 14, the key is 14 * 8192 + 8191 = 122, 8, 192 → 14*8192 is 114688, so the maximum key is 114688 + 8191= 122879. This is manageable as an integer.

But in Python, using a tuple (last, s) is efficient enough. Alternatively, using a single integer key may be faster.

Modify the code to represent the key as last * (1 << (n-1)) + s. But this would require knowing the maximum s possible, which is (1 << (n-1)) -1. So for each mask with k bits set, the s is (k-1) bits. So for the full mask, s is (n-1) bits. So for the key, during transitions, the s can be up to 2^13-1=8191 for n=14. So the key would be last * 8192 + s. For last up to 13 (0-based), this would be 13 * 8192 + 8191 = 13*8192 is 106496 + 8191 = 114687. So the key is an integer up to 114687.

So, in the code, change (last, s) to key = last * (1 << (n-1)) + s. Then, the DP can use integers as keys.

But for mask with k bits set, the s is (k-1) bits. So for k < n, the s is less than 1<< (k-1). But when storing the key as last * (1<< (n-1)) + s, the s may have leading zeros. But this is okay.

This optimization may reduce the time by using integer keys instead of tuples.

Modify the code:

Initialize the DP as a list of defaultdict(int), where the keys are integers representing last and s combined.

For example:

In the initial step:

mask = 1 << i

key = i * (1 << (n-1)) + 0

dp[mask][key] = 1

Then, during transitions:

for key, cnt in current_entries.items():

    last = key // (1 << (n-1))

    s = key % (1 << (n-1))

    for j in not in mask:

        new_last = j

        bit = adj[last][j]

        new_s = (s << 1) | bit

        new_key = new_last * (1 << (n-1)) + new_s

        dp[new_mask][new_key] += cnt

This way, the key is an integer, which may be faster to hash and process.

But this requires precomputing the maximum s shift, which is (n-1) bits.

So, in code:

max_shift = n-1

for i in range(n):

    mask = 1 << i

    key = i * (1 << max_shift) + 0

    dp[mask][key] = 1

Then, during processing:

for mask in masks:

    current_dp = dp[mask]

    for key, cnt in current_dp.items():

        last = key // (1 << max_shift)

        s = key % (1 << max_shift)

        for j in range(n):

            if not (mask & (1 << j)):

                bit = adj[last][j]

                new_mask = mask | (1 << j)

                new_s = (s << 1) | bit

                new_key = j * (1 << max_shift) + new_s

                dp[new_mask][new_key] += cnt

But in this approach, when s is shifted left by 1, the new_s could be up to (1 << (max_shift)) -1, which is 2^(n-1) -1. For example, for a mask with k=14 bits, the s is 13 bits, so new_s can be up to 8191 for n=14.

This approach may save time in handling the keys as integers instead of tuples.

Another optimization is to precompute the adjacency matrix as a list of lists of integers.

But in the code, adj is already a list of lists of integers.

Thus, the code can be modified to use integer keys for the DP entries.

Let's try this.

The modified code:

n = int(input())
adj = []
for _ in range(n):
    s = input().strip()
    adj.append( list(map(int, s)) )

from collections import defaultdict

max_mask = 1 << n
max_shift = n-1

# Precompute masks in order of increasing population count.
masks = []
for mask in range(1, max_mask):
    masks.append(mask)

masks.sort(key=lambda x: bin(x).count('1'))

dp = [defaultdict(int) for _ in range(max_mask)]

for i in range(n):
    mask = 1 << i
    key = i * (1 << max_shift)
    dp[mask][key] = 1

for mask in masks:
    current_dp = dp[mask]
    for key, cnt in list(current_dp.items()):
        last = key // (1 << max_shift)
        s = key % (1 << max_shift)
        for j in range(n):
            if not (mask & (1 << j)):
                bit = adj[last][j]
                new_mask = mask | (1 << j)
                new_s = (s << 1) | bit
                new_key = j * (1 << max_shift) + new_s
                dp[new_mask][new_key] += cnt

full_mask = (1 << n) - 1
result = [0] * (1 << (n-1))
for key, cnt in dp[full_mask].items():
    s = key % (1 << max_shift)
    result[s] += cnt

print(' '.join(map(str, result)))

This code uses integer keys, combining last and s. This may be faster in Python.

Another optimization: precompute the masks and their population count. But in the code, this is already done.

Another possible optimization is to use bitmask's population count as a variable to precompute and use in loops.

But the code is now structured.

In terms of memory, for n=14, each mask's DP can have up to C(14,7)*7*2^6 = 3432 *7*64= 1,537,536 entries. But using defaultdict(int) may be memory-intensive. Alternative, use a list of dictionaries, but in Python, dictionaries are efficient for sparse data.

But given the time constraints, this code should pass for n=14.

Testing this code with the sample inputs:

Sample input 1:

3

011

101

110

The code will generate the correct output.

Sample input 2:

4

0101

1000

0001

1010

The code should generate the sample output 2 2 6 2 2 6 2 2.

Thus, the code should work.
</think>

```python
n = int(input())
adj = []
for _ in range(n):
    s = input().strip()
    adj.append(list(map(int, s)))

from collections import defaultdict

max_mask = 1 << n
max_shift = n - 1

masks = []
for mask in range(1, max_mask):
    masks.append(mask)
masks.sort(key=lambda x: bin(x).count('1'))

dp = [defaultdict(int) for _ in range(max_mask)]

for i in range(n):
    mask = 1 << i
    key = i * (1 << max_shift)
    dp[mask][key] = 1

for mask in masks:
    current_dp = dp[mask]
    for key in list(current_dp.keys()):
        cnt = current_dp[key]
        last = key // (1 << max_shift)
        s = key % (1 << max_shift)
        for j in range(n):
            if not (mask & (1 << j)):
                bit = adj[last][j]
                new_mask = mask | (1 << j)
                new_s = (s << 1) | bit
                new_key = j * (1 << max_shift) + new_s
                dp[new_mask][new_key] += cnt

full_mask = (1 << n) - 1
result = [0] * (1 << (n - 1))
for key, cnt in dp[full_mask].items():
    s = key % (1 << max_shift)
    result[s] += cnt

print(' '.join(map(str, result)))
```