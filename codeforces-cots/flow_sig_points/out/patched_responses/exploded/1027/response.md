<think>
Okay, I need to solve this problem where given a binary string x, I have to compute the complexity of the dance pairs. The complexity is the number of inversions in the pairs (a, b) where a is from MDC and b is NFC's member, and each a is paired with b = a XOR x. 

First, let me understand what the problem is asking. The complexity counts the number of pairs (a, c) where a < c but their corresponding b's are in reverse order. So for each a and c where a < c, if (a XOR x) > (c XOR x), then this contributes to the complexity. So the problem reduces to counting the number of such pairs (a, c).

But how do I compute this efficiently, especially for n up to 100, which means the maximum a and c can be up to 2^100. That's way too big to handle with a brute force O(N^2) approach. So I need a smarter way.

Hmm. Let's think about the XOR operation. Let's denote x as a binary number of length n. Wait, the input is a binary string of length n. So x can be converted to an integer. But n can be up to 100, so x can be up to 2^100 - 1. But handling that as a number in Python is possible since it can handle big integers.

So the main idea is: For each pair a < c, check if a XOR x > c XOR x. The total number of such pairs is the answer.

But how can we compute this efficiently?

Let me think about the XOR properties. Let me denote x as a fixed value. Then, for each a and c, the condition is (a ^ x) > (c ^ x). Let's rearrange this condition. Since a < c, but (a^ x) > (c ^x). So the inversion is based on the XOR with x.

Wait, XOR with x is a bijection. So the pairs (a, a^x) are all unique. So the problem is equivalent to counting the number of inversions in the sequence of a^x values as a ranges from 0 to 2^n - 1, ordered by a. Wait, but a is from 0 to 2^n -1. Because the binary string's length is n, but the MDC has 2n members? Wait, wait. Wait, the problem statement says that the binary number x has length n, and both MDC and NFC have 2n members. Wait, that doesn't add up. Wait, the first paragraph says:

Each member of MDC is assigned a unique id i from 0 to 2n-1. Wait, but if x is a binary number of length n, then 2n-1 would be when n is the number of bits. Wait, perhaps there's a mistake here in the problem statement. Wait, looking back:

The input is a binary number x of length n. Then, each member i of MDC (which ranges from 0 to 2^n -1) dances with member i XOR x of NFC, which would have to be a member of NFC. So the members of NFC must also be numbered from 0 to 2^n -1. But the problem statement says MDC and NFC each have 2n members. Wait, this seems conflicting. Wait, perhaps there's a mistake in the problem statement translation. Let me re-read:

Wait, the problem says:

Each member of MDC is assigned a unique id i from 0 to 2n - 1. The same holds for each member of NFC. Wait, but if the input x has length n, then 2n -1 is a number with n bits. Wait, perhaps there's a confusion here. Because 2n-1 is different from 2^n -1.

Wait, this is a critical point. For example, the first example input is 11, which is n=2 bits. So the MDC has 2n=4 members (0,1,2,3), and the same for NFC. So x is 11 in binary, which is 3. So each MDC member i (0-3) is paired with i^3. Let's see:

i=0 → 0^3=3 → pair (0,3)

i=1 → 1^3=2 → (1,2)

i=2 → 2^3=1 → (2,1)

i=3 → 3^3=0 → (3,0)

The complexity is the number of pairs (a,c) where a < c and b > d (where b is a's pair, d is c's pair). Let's list all possible pairs:

For a=0, c can be 1,2,3.

Check their pairs:

a=0's pair is 3. c=1's pair is 2 → 3>2 → count +=1.

c=2's pair is 1 → 3>1 → count +=1.

c=3's pair is 0 →3>0 → count +=1. So total 3.

a=1, c=2 → 2's pair is 1. 2>1 → no. a=1 < c=2, but 2's pair (1) is less than a's pair (2). So 2 >1 is false. So 2 is not less than 1. Wait, wait. The pair for a=1 is (1,2) → b=2. The pair for c=2 is (2,1) → d=1. So a=1 < c=2. Check if 2 >1 → yes. So yes, this contributes. Wait, so for a=1 and c=2, since a <c but b=2 >d=1 → this is a valid pair.

So this contributes.

Then a=1 and c=3: pair for c=3 is 0. 2>0 → yes. So count +=1.

a=2 and c=3: pair for a=2 is 1, c=3's pair is 0 → 1>0 → yes. So count +=1.

So total pairs:

a=0: 3.

a=1: 2 (c=2 and c=3).

a=2:1 (c=3).

a=3: none.

Total is 3+2+1=6 → which matches the first example's output of 6.

So the example makes sense. Now, how to compute this for larger n up to 100, where 2^100 is way too big to process each pair.

We need an O(n) or O(n^2) approach.

The key is to model the inversion count based on the binary representation of x and the bits of the numbers a and c. Let's think in terms of the binary digits.

The problem is to count the number of pairs (a, c) where a < c and (a ^ x) > (c ^ x). Let's denote x as a binary number of length n. Since a and c are in [0, 2^n -1], as the MDC has 2n members? Wait, no. Wait, the MDC's members are 0 to 2n -1. But if the input x is of length n, then 2n-1 is a number with log2(2n) bits, but that may not align. Wait, the problem statement says the input x has length n, but the MDC has 2n members. Wait, this is conflicting. Wait, the problem statement says:

In the input, the first line contains a binary number x of length n, (1 ≤ n ≤100). Then, member i of MDC (0 ≤ i ≤2n-1) is paired with i XOR x. Wait, but 2n-1 may not be a power of two. For example, if n is 3, then 2n is 6, so members are 0-5. But XOR with x (which is 3 bits) would be 0-7. But NFC's members are 0-5 as well, since they have 2n members. Wait, this can't be. Because if x is a 3-bit number, then i can be up to 5 (binary 101). When you XOR with x (say 111), the result could be up to 5 XOR 7 = 2 (101 ^ 111 = 010, which is 2). Wait, but 5 XOR7 is 2, which is within 0-5? Wait, 5 is 101, 7 is 111. 101 XOR 111 is 010 (2). So for the MDC members, i ranges up to 5, which is 2*3-1=5. And the NFC members are 0-5. So the result i^x must be between 0 and 5. Wait, but when you compute i^x for i in 0-5 and x being a 3-bit number, you can get numbers up to 7. For example, if x is 7 (111), then i=5 (101) → 5^7= 2 (010). But if x is 7 (111), then i=3 is 011. 011 XOR 111 is 100 (4). Which is within 0-5. Wait, 4 is less than 5. So perhaps in this case, the x is given as a binary string of length n, but the actual value of x is considered as a number, and the NFC has 2n members. Wait, but 2n may not be a power of two. For example, if n=3, then 2n is 6, which is not a power of two. So the XOR could produce numbers up to 7, which is larger than 5. So this would imply that the pairing is invalid. So perhaps there's a misunderstanding here.

Wait, perhaps the problem statement has a mistake in the MDC and NFC members' count. Because if the input x is a binary number of length n, then the maximum value of x is 2^n -1. Then, when you compute i^x, for i in 0 to 2n-1, the result can be up to (2n-1) ^ (2^n -1). For example, when n=3, 2n=6, 2n-1=5 (101). x can be up to 7 (111). So 5 XOR 7 is 2 (binary 010). Which is 2, which is within 0-5. So perhaps all the results of i^x for i in 0..2n-1 will be in 0..2n-1? That's not necessarily the case. Wait, no. For example, if n=2 (input x has 2 bits), then 2n=4, and i ranges from 0 to 3. x can be 11 (3). Then, i=3 → 3^3=0, which is okay. i=2 (10) XOR 11 (3) is 01 (1). Also okay. But for n=1, x is 1. Then MDC has 2 members: 0 and 1. i XOR x would be 1 and 0, which are within the range 0-1. So perhaps in general, for MDC members i from 0 to 2n-1, and x is a binary number of length n, then i^x is also in 0 to 2n-1. Is that possible? Let's see.

Wait, n is the length of x. So x is a binary number of n bits. So x can be up to 2^n -1. The MDC's i ranges from 0 to 2n-1. But 2n-1 can be up to 2*100-1=199, which is less than 2^8-1. So x can be up to 2^100-1, which is way larger than 2n-1 when n is 100. So XORing i with x could result in a number larger than 2n-1, which would imply that the NFC member IDs are outside the allowed range. But according to the problem statement, the NFC has 2n members, so their IDs are 0 to 2n-1. So this suggests that the problem statement is incorrect. However, the sample inputs and outputs must be consistent. Let's look at the first sample input.

Sample Input 1:
11 → which is binary for 3. n is 2. So MDC members are 0 to 3 (since 2n=4 → 0-3). The x is 3 (binary 11). For each i in 0-3, the NFC member is i^3. For example:

i=0 → 0^3=3 → which is in 0-3. So valid.

i=1 → 1^3=2 → valid.

i=2 → 2^3=1 → valid.

i=3 →3^3=0 → valid.

So all are valid. But why? Because 3 is 2^2-1, and 2n=4. So 2n is 4, which is 2^2. So for this case, x is 2^2-1. So i ranges up to 3. XOR with x (3) would give values up to 3. So perhaps in the problem statement, the actual MDC and NFC members are 0 to 2^m -1, where m is the length of the binary x. But the problem statement says that the MDC has 2n members. So this is conflicting. Wait, perhaps the problem statement has a typo. Let me recheck the problem statement.

The problem statement says:

We know that member i from MDC dances with member i XOR x from NFC. So the NFC member's ID is i XOR x. But according to the problem statement, NFC's members have IDs from 0 to 2n-1. So when we compute i XOR x, it must be in that range for all i in 0 to 2n-1. But this is only possible if x is such that i XOR x is within 0 to 2n-1 for all i. Which would only be possible if x is 0, but that's not the case. So perhaps the problem statement has a mistake here, and the actual MDC and NFC members are 0 to 2^n -1. Because when x is a binary number of length n, then 2^n is the maximum possible for x. Then, for i in 0 to 2^n -1, i XOR x is also in 0 to 2^n -1. So that makes sense. But the problem statement says that MDC and NFC have 2n members, but that's not possible for n up to 100. Because 2n would be 200, but 2^100 is way larger. So this suggests that the problem statement has a mistake, and the correct number of members is 2^n for each club.

But given the sample input, the first sample has input 11 (n=2), which is 3. So the MDC has 2n=4 members (0-3), and NFC has 4 members. Then, i XOR x (3) for i in 0-3 gives 3,2,1,0, which are all in 0-3. So in that case, the code works. So perhaps the problem statement's MDC and NFC have 2^m members, where m is the length of x. But the problem statement says 2n, where n is the length of x. So this is confusing. However, given that the sample input works, perhaps the correct approach is that the number of members is 2^n, where n is the length of x. So the MDC and NFC each have 2^n members, with IDs from 0 to 2^n -1. The problem statement's description of 2n members is incorrect. Because, for the first sample input, n is 2, so 2n is 4, which is 2^2. So in that case, it's correct. But for a binary string of length n=3, 2n is 6, but 2^3 is 8. So there's a discrepancy here. But given the sample inputs, perhaps the actual MDC and NFC have 2^n members each. So the problem statement's mention of 2n is a mistake, and it's supposed to be 2^n. Because otherwise, the problem is not feasible.

So I think that's the case. Therefore, the problem is to consider that the MDC and NFC each have 2^n members, and their IDs are from 0 to 2^n-1. The input x is a binary string of length n, and thus x can be up to 2^n-1. Then, for each i in 0..2^n-1, the pair is (i, i^x), which is valid because i^x is in 0..2^n-1. So this makes sense.

Therefore, the actual problem is to compute the number of inversion pairs in the sequence b_i = i XOR x, where i ranges from 0 to 2^n-1. So the complexity is the inversion count of the array [0^x, 1^x, ..., (2^n-1)^x].

So the problem reduces to counting the number of inversions in the permutation induced by XOR x. Now, inversion count in a permutation can be computed efficiently with a Fenwick Tree in O(n log n) time where n is the size of the array. But here, the size is 2^100, which is way too big. So we need a mathematical approach to compute this inversion count based on the binary representation of x.

So the key insight is to model the inversion count as a function of the bits of x. Let's think about how XOR affects the order.

Let's consider two numbers a and b, a < b. We want to count when (a^x) > (b^x).

Let's represent a and b in binary, and compare a^x and b^x.

Since XOR flips the bits where x has a 1. So, for each bit position where x has a 1, a and b's bits are flipped in that position when calculating a^x and b^x.

So, the comparison between a^x and b^x depends on the leftmost bit where a and b differ. Let's find the position where a and b differ the first time (from MSB to LSB). Suppose that position is k. Then, in the original a and b, the bit at position k in a is 0 and in b is 1 (since a < b). So, when XOR with x, the bits at position k for a^x and b^x are (a_k ^ x_k) and (b_k ^x_k) = (1 ^ x_k). So:

If x_k is 0: then a's bit becomes 0, b's becomes 1. So (a^x) has 0, (b^x) has 1 → a^x < b^x. So this pair does not contribute to the inversion count.

If x_k is 1: then a's bit becomes 1, b's becomes 0. So (a^x) > (b^x). So this pair contributes to the inversion count.

So, the pair (a < b) will be inverted (counted) in the inversion count if and only if the first differing bit in a and b is set to 1 in x.

Therefore, the total inversion count is equal to the number of pairs (a, b) where a < b and the first differing bit in a and b is a position where x has a 1.

So how can we compute this?

The inversion count can be calculated by considering each bit position. Let's process each bit from the highest (most significant) to the lowest.

For each bit position i (starting from the MSB), if the x has a 1 in this position, then any pair of numbers (a, b) where a < b and their first differing bit is position i will contribute to the inversion count.

The number of such pairs can be computed as follows:

For bit i, if x has a 1, then:

The number of pairs where the first differing bit is i is equal to the number of pairs (a, b) where a and b have the same bits above i, a has 0 in bit i, b has 1 in bit i, and the bits below i can be arbitrary (as long as a < b). However, since the first differing bit is i, the bits above i must be the same. So for each group of numbers where the bits above i are fixed (prefix), and in the i-th bit a has 0 and b has 1, then the number of pairs is (number of 0s in the i-th bit of the group) multiplied by (number of 1s in the i-th bit of the group), multiplied by 2^{number of bits below i} * (2^{number of bits below i} - 1)/2. Wait, maybe not. Let's think differently.

Wait, when the first differing bit is i, then the bits above i are the same. In the i-th bit, a has 0 and b has 1. The bits below i can be anything, but since a < b, after the i-th bit, the bits of a can be anything and the bits of b can be anything. Wait, no. Because the first differing bit is i, so the bits below i can be anything, but a is allowed to have any combination as long as a < b.

But since the first differing bit is i, the bits below i can be anything as long as a has 0 in i and b has 1 in i. Then, for the bits below i, there are 2^{i} possibilities for a and 2^i possibilities for b. For each such a and b, a has 0 in i, b has 1 in i. So the total number of possible pairs for a fixed prefix (bits above i) is (count_0) * (count_1) * (2^{2i} - 2^{i})/2. Wait, perhaps not. Let's re-examine.

Alternatively, for each group of numbers that share the same prefix up to the i-th bit (exclusive), the numbers in the group have the same bits higher than i. For each such group, consider the numbers where the i-th bit is 0 and 1. Let the count of 0s be A and 1s be B. Then, the number of pairs (a, b) where a is in the 0 group and b is in the 1 group is A * B. Each such pair (a, b) contributes to the inversion count if the first differing bit between a and b is i. But since the higher bits are the same, the first differing bit is indeed i. So for these pairs, the first differing bit is i, and if x has 1 in i, then they contribute.

But in addition, for the lower bits (bits below i), the a and b can have any values, but since a < b in the original numbers (as a is in the 0 group and b is in the 1 group, and the first differing bit is i), the lower bits don't affect the order. So the number of pairs for this group and bit is A * B * (2^{i}) * (2^{i} - 1)/2. Wait, no. Wait, each a in the 0 group can be paired with each b in the 1 group. But since a is in the 0 group and b is in the 1 group, a < b. So each pair (a, b) where a is in the 0 group and b is in the 1 group will be counted. However, the numbers in the group have bits above i fixed, and the i-th bit is 0 for a and 1 for b. The lower bits (i-1 downto 0) can be anything. So the total number of pairs (a, b) in this group is (A * B), where A is the number of elements in the 0 subgroup (i-th bit 0), B is the number in 1 subgroup. Each pair (a, b) in these subgroups will have a < b, because their higher bits are same, and a's i-th bit is 0, while b's is 1. So regardless of the lower bits, a is less than b. So each such pair contributes if x's i-th bit is 1.

Therefore, for each bit i where x's i-th bit is 1, the number of pairs (a, b) where a < b and the first differing bit is i is equal to the number of pairs (a, b) where a is in a 0 subgroup and b is in the 1 subgroup, for the same prefix. The total number is sum over all possible groups (prefixes) of (count_0_in_group * count_1_in_group).

Wait, but for each bit i, the number of groups (prefixes) is 2^{n - i - 1}, since the higher bits (above i) can be any combination. For example, for i=2 in a 3-bit number, the higher bits are bits 3 and up (but n is 3, so the bits are 2,1,0). Wait, perhaps I'm getting the indices wrong. Let's think of the bits as numbered from MSB (highest) to LSB (lowest), with the MSB being position n-1 (assuming x is a binary number of length n). For example, if x is 11 (n=2), then the bits are in positions 1 and 0 (with 1 being the MSB).

So for a given bit position i (from 0 to n-1, where 0 is the LSB), the higher bits (positions n-1 down to i+1) can be any combination. For each combination of higher bits, the bits at position i are 0 for a and 1 for b. The lower bits (positions i-1 downto 0) can be anything. But in this case, the count_0_in_group is the number of elements in the group where the i-th bit is 0. For a group (a fixed prefix of higher bits), the i-th bit is 0 for the subgroup A and 1 for subgroup B. The count_0_in_group is 2^i (since for the lower i bits, any combination is allowed). Similarly, count_1_in_group is 2^i. Wait, no. Wait, the higher bits are fixed (the prefix), the i-th bit is 0 for A and 1 for B. The lower bits (i-1 downto 0) can be anything, so each subgroup (A and B) has 2^i elements. So for each group (prefix), the number of pairs is (2^i) * (2^i) = 2^{2i} pairs. However, since a < b, all pairs (a in A, b in B) contribute. The number of such pairs is (2^i) * (2^i) = 2^{2i} for each group. Then, the number of groups is the number of possible prefixes, which is 2^{n- (i+1)} }, because the higher bits (above i) can vary. Wait, the higher bits are the bits from i+1 to n-1. So for a bit i, the higher bits are positions i+1, ..., n-1. The number of possible combinations for these bits is 2^{(n-1) - (i+1) +1} } = 2^{n-1 - i} }.

Wait, for example, if n=3 and i=1 (the middle bit), then higher bits are positions 2 (MSB is position 2). The higher bits are position 2. So there are 2^1 possible combinations. For each combination of higher bits, the group is defined by that combination, and the i-th bit is 0 for A and 1 for B.

So for each bit i, the number of groups (prefixes) is 2^{ (n-1) - i } }, because the higher bits (i+1 ... n-1) can take any value. Each group contributes (2^i) * (2^i) pairs. So the total for bit i is 2^{ (n-1 - i) } * 2^{i} * 2^{i} } = 2^{n-1 -i} * 2^{2i} } = 2^{n-1 -i + 2i} } = 2^{n-1 + i} }.

But this is only if the i-th bit in x is 1. So the total inversion count is the sum over all bits i where x's i-th bit is 1 of (2^{n-1 + i} } ) ?

Wait, let's test this with the first sample input.

Sample Input 1: 11 → binary x is 11, n=2. So x's bits are 1 (bit 1) and 1 (bit 0). So for each bit i=0 and i=1, since x has 1 in both bits.

For i=1 (MSB), the contribution is 2^{2-1 +1} = 2^{2} =4.

For i=0, contribution is 2^{2-1 +0} = 2^1=2.

Summing 4+2=6, which matches the sample output. So this formula seems correct.

Sample Input 2: 01 → x is 01 (n=2). Bits are 0 (bit 1) and 1 (bit 0). So only i=0 contributes. The contribution is 2^{2-1+0} = 2^1=2. Which matches the sample output of 2.

Sample Input 3: 1 → x is 1 (n=1). So bit i=0. Contribution is 2^{1-1+0} = 1. Which matches the sample output of 1.

So the formula works. So the approach is to iterate over each bit position i (from 0 to n-1). For each bit i, if x's bit is 1, add 2^{ (n-1) + i } to the answer. Then take the sum modulo 1e9+7.

But wait, in the first sample, for i=1 (the MSB in n=2), the contribution is 2^{2-1 +1} = 2^2=4. For i=0, 2^{1+0}=2. Sum is 6. Which is correct.

So the formula is for each bit i where x's i-th bit is 1, add 2^{(n-1) +i} to the total.

But wait, how is that possible? Let me re-derive.

For a bit i, the number of pairs where the first differing bit is i and x has 1 in that bit is:

number of groups (prefixes) * (number of pairs per group).

Each group has 2^i numbers in the 0 subgroup and 2^i numbers in the 1 subgroup. So pairs per group is (2^i) * (2^i) = 2^{2i}.

Number of groups is 2^{ (n-1) - i }, because the higher bits (i+1 to n-1) are arbitrary. So each group is a combination of these higher bits.

Total pairs for bit i: 2^{ (n-1 -i) } * 2^{2i} } = 2^{ (n-1 -i) + 2i } = 2^{n-1 +i }.

Yes. So for each bit i where x's i-th bit is set, the contribution is 2^{n-1 +i}.

So the solution is:

1. Read the binary string x.

2. For each bit position i (from 0 to n-1, where i=0 is the LSB), check if x has a 1 in that position.

3. For each such i, compute 2^{(n-1 +i)} modulo 1e9+7.

4. Sum all these contributions and output the sum modulo 1e9+7.

Wait, but how do we determine the bit positions? Because the binary string may have leading zeros. For example, if x is given as '01', which is n=2. Then the bits are 0 (bit 1, MSB) and 1 (bit 0). So for x= '01', the bits are in positions 1 (MSB) and 0 (LSB). So the MSB is position n-1, and the LSB is 0.

Yes. So the binary string is of length n, and the bits are indexed from 0 (LSB) to n-1 (MSB). Or wait, the leftmost character of the string is the highest bit. For example, the string '11' is 1 (bit 1) and 1 (bit 0), assuming n=2. So the first character is the highest bit. So for the string, the leftmost character is the MSB (position n-1), and the rightmost is LSB (position 0).

So when parsing the binary string, for each character in the string, the first character is the (n-1)th bit, the second is (n-2), and so on. For example, '11' for n=2 is bits 1 and 0. So to check each bit, we need to process the string from left to right, each character corresponds to a bit from MSB (position n-1) downto LSB (position 0).

Wait, for the input '01', which is of length 2 (n=2), the bits are in positions 1 and 0. The string is '0' followed by '1', so bit 1 is 0, bit 0 is 1.

So for each character in the input string, the index in the string is i (0-based), which corresponds to the bit position (n-1 - i). For example, in the string of length 2, the first character (index 0) is bit 1, the second (index 1) is bit 0.

So to loop through the bits of x, we need to iterate over each character in the string, and for each position in the string, determine if the bit is set. For example, the string '01' has bits in positions 1 (0) and 0 (1). So for i in 0 to n-1, the bit position is (n-1 - i) when reading from left to right. Wait, no. For example, the string '01' for n=2: the first character is bit 1 (MSB), the second is bit 0 (LSB). So for the string index j (0-based), the bit position is (n-1 - j). So j=0 → position 1, j=1 → position 0.

So, for each j in 0..n-1 (for the input string), the bit is in position (n-1 -j).

So to check if x's bit in position k is set, we need to look at the character at index (n-1 -k) in the string. For example, for position k=1 (MSB in n=2), the character is at index 0. For position k=0, character is at index 1.

So, for all k in 0..n-1, the corresponding string index is (n-1 -k). So to check if the k-th bit is set, we need to check if the character at index (n-1 -k) is '1'.

Therefore, the steps are:

For each k from 0 to n-1 (bit positions, LSB to MSB? Or MSB to LSB? Wait, no. Wait, in the problem statement, the x is given as a binary number. For example, '11' represents the binary number 11, which is 3. So the leftmost character is the MSB, and the rightmost is LSB. So the bit positions are from 0 (LSB) to n-1 (MSB). For example, '11' has bits set at position 1 (MSB) and 0 (LSB).

So when processing the input string x, which is of length n, the bits are numbered from 0 (LSB) to n-1 (MSB). But the string is written in the order from MSB to LSB. So the first character in the string is the MSB (bit position n-1), the next is bit n-2, and so on, until the last character (bit position 0).

So to get the value of x, the string is parsed as bits from left (MSB) to right (LSB). But when considering individual bits, the bit positions are 0 (LSB) to n-1 (MSB). For example, the string '10' (n=2) represents x= 1*2^1 + 0*2^0 = 2. So bit 1 (MSB) is 1, bit 0 (LSB) is 0.

So to check whether the k-th bit of x is set (for k from 0 to n-1), the position in the string is (n-1 -k). For example, for k=0 (LSB), the position in the string is n-1. For k=1 (if n>1), the position in the string is n-2.

So, for each k in 0..n-1:

bit_set = (x_str[n-1 -k] == '1')

If bit_set, then the contribution is 2^{ (n-1) +k }.

Sum all such contributions.

So the algorithm is:

sum =0

for k in 0 to n-1:

    if x has bit set at position k:

        sum += 2^ (n-1 +k )

sum mod 1e9+7.

So now, the code can be written as follows:

Read the binary string x_str.

n = len(x_str)

mod = 10**9 +7

res =0

for k in range(n):

    # check if the k-th bit is set.

    # the position in the string is (n-1 -k)

    pos = n-1 -k

    if x_str[pos] == '1':

        exponent = (n-1) +k

        res += pow(2, exponent, mod)

        res %= mod

print(res % mod)

Wait, but let's test this with the sample inputs.

Sample Input 1: '11' → n=2.

k ranges from 0 to 1.

k=0:

pos =2-1 -0=1. x_str[1] is '1'. So exponent= 2-1 +0=1. 2^1=2. So add 2.

k=1:

pos=2-1-1=0. x_str[0] is '1'. exponent=1+1=2. 2^2=4. Add 4+2=6. Correct.

Sample Input 2: '01' → n=2.

k=0: pos=2-1-0=1. x_str[1] is '1' → exponent 1+0=1. 2^1=2.

k=1: pos=2-1-1=0. x_str[0] is '0' → no contribution.

Sum is 2. Correct.

Sample Input 3: '1' → n=1.

k=0: pos=1-1 -0=0. x_str[0] is '1'. exponent=0 +0=0. 2^0=1. Correct.

Yes, this code seems to work.

So the code reads the binary string, iterates for each bit position k (0 to n-1), computes whether the k-th bit in x is set, and if so, adds 2^{n-1 +k} mod 1e9+7 to the result.

This code runs in O(n) time, which is acceptable for n up to 100. The exponents are up to 100-1 +100 = 199, so 2^199 is manageable with modular exponentiation.

Therefore, this is the optimal solution.
</think>

```python
x = input().strip()
n = len(x)
mod = 10**9 + 7
result = 0

for k in range(n):
    pos = n - 1 - k
    if x[pos] == '1':
        exponent = (n - 1) + k
        result = (result + pow(2, exponent, mod)) % mod

print(result)
```