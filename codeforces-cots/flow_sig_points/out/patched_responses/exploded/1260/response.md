<think>
Okay, let's try to figure out this problem. So, the problem is about finding the number of pairs (l, r) such that the subarray from a_l to a_r is "good". A good sequence is one where, after possibly swapping any bits in any of the numbers (any number of times), the XOR of all elements in the subarray is zero.

Hmm, wait. Swapping bits in a number's binary representation. That means that for each number in the sequence, we can rearrange its bits in any order. So the actual value of the number can be any permutation of its bits. But how does that affect the XOR?

Wait, when you can rearrange the bits, the number can have any number of 1's and 0's, but the count of 1 bits is fixed. For example, 6 is 110 in binary, which has two 1's. So after any swap, it can become 3 (11), 5 (101), 6 (110), etc., but it will always have exactly two 1's. So the key here is that for each number, the only thing that matters is the number of 1 bits in its binary representation. Because when you can permute the bits, any permutation will result in a number with the same count of 1 bits, but in different positions. So for a number a_i, the count of set bits (let's call it c_i) is fixed. But when we compute the XOR, the order of the bits matters. Wait, how does the permutation of bits affect the XOR sum?

Wait, the XOR is computed bitwise. For each bit position, the XOR will be 1 if there's an odd number of 1's in that position across all elements. So, if we can permute the bits of each number, then for each bit position in the XOR result, we can arrange the 1's from each number to different positions. But how?

Wait, here's the crux: when you can rearrange the bits for each number, you can distribute the set bits of each number across any bit positions. So the problem reduces to being able to assign the set bits of each number to any positions such that, when all are XORed, the total is zero.

So the question is: what is the condition on the counts c_i (number of set bits in each a_i) such that there exists an assignment of the bits to positions such that the XOR of all elements is zero.

Let me think. For each bit position in the XOR result, the total number of 1's in that position across all elements (after permutation) must be even. Because XOR of a bit is 1 if the count is odd. So the entire XOR is zero only if, for all bit positions, the count of 1's is even.

But since each number's set bits can be arranged into any positions, the problem becomes whether the sum of all c_i (the total number of 1's across all elements in the subarray) is even. Wait, no. Because each number's set bits can be placed in any positions. So the total sum is the sum of all c_i. But each set bit can be placed in any position, but to have the XOR be zero, all bit positions must have an even number of 1's. So the sum of all 1's in all positions must be even? Wait, no. Because each 1 in a position contributes to that position's count. So the sum of all 1's is the sum over all positions of the number of 1's in that position. But if each position has an even count, then the total sum must be even (since even numbers sum to even). However, if the total sum is even, it's possible that each position's count is even, but not necessarily. For example, sum could be 4, which can be split into two positions each with 2 (even), or one position with 4 (even). So the condition that the total sum of all 1's (sum of c_i) is even is necessary. But is it sufficient?

Wait, no. Because even if the total sum is even, it might not be possible to split it into bits positions with even counts. For example, sum is 2. Then you can have two 1's in the same position (count 2, even) and the rest zero. That would work. So sum even is sufficient.

Wait, maybe the key insight is that the sum of all c_i must be even. Because if the sum is even, then you can arrange all the bits such that all positions have even counts. How?

Because you can pair the 1's. For example, each number's set bits can be arranged in pairs. For example, if the total number of 1's is even, you can arrange all of them into pairs in the same bit positions. Then each bit position has even counts, leading to XOR zero.

But how exactly? Let's think: for each number, when you can arrange the bits any way you like, you can choose which positions the 1's go to. So the problem reduces to: can we assign each 1 from each c_i to a bit position such that each position has an even count of 1's.

So, the sum of all c_i (the total number of 1's in the subarray) must be even. Because if the sum is even, then you can arrange them into pairs. For example, if the sum is 4, you can assign two 1's to position 0 and two to position 1, etc. Each position has even counts. So XOR is zero.

But if the sum is odd, then it's impossible to split into even counts. So the necessary and sufficient condition is that the sum of c_i in the subarray is even.

Wait, that's a big leap. Let me confirm. So for a subarray to be good, the sum of the number of set bits in each element must be even. Because only then can we arrange the bits such that every bit position has an even number of 1's. So that's the key. So the problem reduces to finding the number of subarrays where the sum of c_i is even.

If that's the case, then the problem becomes similar to the standard problem of finding the number of subarrays with even sum. But here the sum is the sum of the counts of set bits in each element.

So the solution is to precompute for each element a_i, the count of set bits, c_i = bin(a_i).count('1'). Then, we need to find the number of subarrays [l, r] where the sum of c_l to c_r is even.

But how do we compute that efficiently? The standard approach for counting the number of subarrays with even sum is to use a prefix sum array and track the parity (even or odd) of the prefix sums. Let me think:

Let S[i] be the sum of the first i elements. Then, the sum from l+1 to r is S[r] - S[l]. We want this difference to be even, which means S[r] and S[l] must have the same parity. So for each r, the number of l's where S[r] and S[l] have the same parity (including l=0, which is the prefix sum of 0 elements) is the number of valid subarrays ending at r.

So, the total count is the sum over all r of the number of previous prefix sums (including the initial 0) that have the same parity as S[r].

Thus, the approach is to compute the prefix sum mod 2, and keep a count of how many times each parity (0 or 1) has been seen up to each point. Then, for each r, add the count of prefix sums with parity equal to current sum mod 2.

This is O(n) time and O(1) space, since we just need to track the counts of even and odd parity.

So the steps are:

1. For each a_i, compute c_i as the number of set bits in a_i.
2. Compute the prefix sum mod 2. Let's call this prefix_parity.
3. Keep track of the counts of even and odd parities as we go. For each current parity, add the count of previous occurrences of the same parity to the total.
4. Initialize the count with prefix_parity 0 (sum of zero elements is even).

But wait, in our case, the sum of the c_i's in the subarray [l+1, r] must be even. So the sum from l+1 to r is (prefix[r] - prefix[l]) mod 2 must be 0. So prefix[r] mod 2 == prefix[l] mod 2.

So, for each r, the number of l's (0 <= l <= r) where prefix[r] and prefix[l] have the same parity is the contribution to the total. So the total is the sum over all r of the number of times the current parity has been seen before, including the initial 0.

So the algorithm is:

Initialize a dictionary or a counter that starts with {0: 1} (the parity of the sum 0 is even, and we've seen it once).

Then, for each element in the prefix sum parity array (which is built incrementally), we:

- Check the current parity (current_sum_mod_2).
- Add the count of previous occurrences of this parity to the total.
- Increment the count for this parity.

So, for example, the initial count is {0:1}.

Then, as we process each c_i:

current_parity = (current_parity + c_i) % 2

Then, the number of valid subarrays ending at this position is the count of current_parity in the map. Then, increment the map for current_parity by 1.

So the code would look like:

count = 0
current_parity = 0
parity_counts = {0: 1}
for num in c:
    current_parity = (current_parity + num) % 2
    count += parity_counts.get(current_parity, 0)
    parity_counts[current_parity] = parity_counts.get(current_parity, 0) + 1

So this counts all the valid subarrays where the sum is even.

Thus, the problem reduces to calculating the number of subarrays with even sum of the set bits counts.

But wait, does this logic hold? Let's test with the examples.

First example input:

3
6 7 14

c_i for 6 is 2 (binary 110), 7 is 3 (111), 14 is 3 (1110).

c array is [2,3,3]. The sum of the entire array is 8 (even), so the entire array is a valid subarray. The sum of 3+3 is 6, even. So the pairs (2,3) and (1,3) are valid, which gives count 2. But according to the code, let's see:

Let's compute the parity as we go.

Initialize parity_counts {0:1}, current_parity 0.

First element is 2 (even). current_parity becomes 0. The current_parity is 0. The count += parity_counts[0] → 1. Now parity_counts[0] becomes 2.

Second element is 3 (odd). current_parity becomes (0 +3) %2 =1. The count += parity_counts[1] (which is 0). Then increment parity_counts[1] to 1.

Third element is 3 (odd). current_parity becomes (1+3)%2 → 0. So current_parity is 0. The count += parity_counts[0] which is 2. So total count is 1 (from first step) +0 (second) +2 (third) = 3. But the sample output is 2. Wait, this is a problem.

Wait, in the first example, the code as per this approach would compute 3, but the correct answer is 2. So something's wrong here.

Hmm, this suggests that our initial reasoning is incorrect. What's wrong here?

Wait the sample input:

The first example's c array is [2,3,3]. The possible subarrays:

[1,1]: sum 2 → even → valid.

But according to the note, in the first example, the valid pairs are (2,3) and (1,3). So why is (1,1) not considered valid?

Ah, because the problem requires that after permuting the bits of each number in the subarray, the XOR is zero. So in the first case, the subarray [1,1], sum is 2. So according to our previous reasoning, this is even, hence the subarray is valid. But according to the note in the example, this is not a valid pair. So there's a contradiction here.

Wait what's the correct answer for the first example? According to the sample input, the output is 2. But according to our approach, the code would compute 3. So our approach is wrong.

Hmm, this indicates that our initial conclusion that the sum of c_i must be even is incorrect. So our reasoning was wrong.

So what's wrong here?

Let me re-examine the problem. The actual condition is whether there exists a way to arrange the bits of each number in the subarray such that the XOR is zero. So the sum of the c_i's being even is necessary, but perhaps not sufficient.

Wait, perhaps the sum of the c_i's must be even, but also each individual number's c_i can be arranged such that the total sum per bit is even.

But how? Let me think of the first example's [1,1] case. The subarray is [6], which has c_i=2. So sum is 2, even. According to our reasoning, this should be valid. But according to the sample, it's not considered a valid pair.

Wait but according to the note in the first example, the valid pairs are (2,3) and (1,3). So the [1,1] subarray (the first element alone) is not considered valid. So why?

Because when we have a single element, the XOR is itself. We can rearrange the bits of 6 (binary 110) into any permutation of the bits, but the XOR (which is the element itself) must be zero. So the XOR after rearrangement must be zero. But the only way for a single element to have XOR zero is if the element is zero. But the element here is 6, which after permutation can be any number with two 1's. For example, 3 (binary 11), which XORed with itself would be 3 ^ 3 = 0. Wait, no. Wait, the subarray has length 1. So the XOR is the element itself. So even if we can arrange the bits, the element can be any permutation of its bits, but the XOR (which is the element) must be zero. So the only way for a subarray of length 1 to be valid is if the element can be rearranged into zero. But that's impossible unless the element is zero. Because any element with at least one 1 bit can't be rearranged to zero. Because the count of 1's is fixed.

Wait, wait. For a single element, the XOR of the subarray is the element itself (after any rearrangement). So for the XOR to be zero, the element must be zero. But in the first example, the first element is 6. Which has two 1's. So after rearrangement, it can be any number with two 1's, like 3, 5, 6, etc. None of these are zero. So the XOR can't be zero. Hence, the subarray [1,1] (single element) is not valid. But according to our previous reasoning, the sum of c_i is even (2), which would suggest that it is valid. So our initial approach is wrong.

So what's the mistake in the reasoning?

Ah! The mistake is that when the sum of c_i is even, it's possible to split the 1's into even counts per bit position, but this requires that each individual 1 can be assigned to any bit. But for a single element, the sum of c_i is even (say, 2), but the element can only contribute 1's to certain positions. For example, a single element with c_i=2 can assign two 1's to the same bit position (so XOR is zero in that position). But that would make the entire XOR equal to that bit position's value. So the XOR would be 2^k for that position, which is not zero. Wait, no. Because for a single element, the sum of the c_i is 2, so you can arrange the two 1's in the same position. Then, that bit position has two 1's (even count), so the XOR is 0. But the other positions are zero. So the total XOR is zero. Wait, that's possible.

Wait, wait. Let's think again. For a single element with c_i=2, can we arrange the bits such that the XOR (which is the element itself) is zero?

The XOR of a single element is the element itself. So even if the bits are arranged in the same position, the value is (1 << k) * 2, but that's not possible. Wait, for example, 6 (binary 110) can be rearranged as 3 (binary 11), which has value 3. The XOR is 3, which is non-zero. Alternatively, can we arrange the two 1's in different positions? Like, for example, 1 in the 0th position and 1 in the 1st position. Then the value is 3, XOR is 3. If we arrange both 1's in the same position, like the 1st position (binary 2^1 + 2^1 = 2^1 * 2 = 2^2?), wait no. Wait, each 1 in the same position would add up. But XOR is for each bit, the count mod 2. So arranging two 1's in the same position would result in 0 for that bit. So the XOR would be zero.

Wait, but how can you arrange two 1's in the same position? Because each bit can be assigned once per element. For example, the element is allowed to have two 1's in the same bit position. Is that possible?

Wait, the operation allows swapping any pair of bits. So for a number like 6 (110), after swapping, you can have 110 (same as before) which has two 1's in positions 1 and 2 (assuming 0-based). Or 101 (5), which has 1's in positions 0 and 2. But you can't have two 1's in the same position. Because the original number has exactly two bits set. So when you swap bits, you can arrange their positions, but each bit can only appear once in each position. So for example, you can't have two 1's in the same bit position. Because each number has exactly c_i bits set, and each bit in the number is either 0 or 1. So after any permutation of the bits, the number will have exactly c_i 1's, each in distinct positions.

Wait, no. Because when you swap bits, you're just changing the order of the bits. So for example, the number 6 (binary 110) is 3 bits long, but when you swap the first two bits, you get 011 (3). But you can't create a number with two 1's in the same position. Because each bit in the binary representation is a single digit. So the count of 1's is fixed, but each 1 must be in a distinct position.

Wait, that's a critical mistake in the initial reasoning. Oh my god! So the problem says you can swap any pair of bits in the binary representation. But the binary representation has a fixed number of bits. For example, the number 6 is 110. If you swap the first and second bits (from left, but perhaps leading zeros are allowed?), but in reality, numbers are represented with their binary digits, including leading zeros if necessary? Or are leading zeros considered as part of the binary representation?

Wait, the problem statement says, "swap any pair of bits in its binary representation". For example, they transformed 6 (binary 110) into 3 (binary 11) by swapping the third and second bits (assuming leading zeros are allowed). So the binary representation may have leading zeros. So any bit in the binary representation, including leading zeros, can be swapped. For example, 6 is ...000000110 (but the exact number of leading zeros isn't specified). So when swapping bits, you can have any number of leading zeros. So the actual binary representation is considered as an infinite sequence of bits, but in practice, only the positions where the original number has bits set (or leading zeros) can be swapped. Wait, no. The problem says you can swap any pair of bits. So the binary representation can be considered as an infinite sequence of bits, but for numbers with finite bits, the rest are zeros. So when you swap bits, you can swap any two positions, including leading zeros. For example, 6 is 110 in binary (assuming leading zeros can be considered), but when you swap the first bit (from the right) with the 100th bit (which is zero), the number becomes 2^99 + 2^1, which is a very large number. So the number of set bits (c_i) remains two, but the positions can be any.

Wait, but if we can swap any two bits, regardless of their positions, then the set bits can be placed in any positions. So for example, a number with c_i set bits can have those bits in any positions. So the 1's can be arranged in any positions, even non-overlapping ones, but each 1 is in a distinct position. So, the sum of the c_i's is the total number of 1's in all elements, and each 1 can be placed in any position (possibly overlapping with others).

But how does that affect the XOR sum?

The XOR is computed bitwise. So for each bit position, the XOR is 1 if the number of 1's in that position across all elements (after rearrangement) is odd. To have the total XOR be zero, all bit positions must have even counts.

So the problem reduces to: can we assign each of the c_1 + c_2 + ... + c_k (for the subarray) 1's to bit positions such that each position has an even number of 1's.

But since the sum of all 1's is even (since each position has even count, sum is even), then the sum must be even. So the sum being even is a necessary condition.

But is it sufficient?

Yes. Because if the sum is even, we can pair the 1's. Each pair can be assigned to the same bit position, leading to even counts. For example, if there are 4 1's in total, assign two pairs to the same position. Then that position has 2 (even) 1's. The rest are zero. So the XOR is zero.

Wait, but each pair must be from the same element? No. For example, two elements each contributing two 1's. Each can contribute their two 1's to the same bit position. So that position has 4 1's (even), others have zero. So XOR is zero.

So the sum of c_i must be even for the subarray to be good. That's the necessary and sufficient condition.

But in the first example, why is the subarray [1] (6) not considered valid?

Wait, according to this logic, it should be valid. Because the sum of c_i is 2 (even). So we can assign the two 1's to the same bit position. Then that position has two 1's (even), XOR is zero.

But according to the sample input, the first example's output is 2. The code according to the initial approach would compute:

The c array is [2,3,3]. Let's compute the prefix sum mod 2.

prefix[0] = 0 (sum of 0 elements).

prefix[1] = 2 mod 2 = 0.

prefix[2] = (2+3) mod 2 = 1.

prefix[3] = (2+3+3) mod 2 = 0.

Then, for each step:

After first element (i=1):

current_parity is 0. The count is parity_counts[0] (1) → total becomes 1. So this counts the subarray [1,1].

After second element (i=2):

current_parity is 1. parity_counts[1] is 0 → adds 0. Now, parity_counts[1] becomes 1.

After third element (i=3):

current_parity is 0. parity_counts[0] is now 2 (initial 0 and prefix 1). So adds 2 to total. Total becomes 1+0+2=3.

But sample output is 2. So why is there a discrepancy?

Because according to the problem statement, the subarray [1,1] (single element 6) is not valid. But according to our logic, it should be valid. What's the issue here?

Ah, here's the mistake. The initial approach assumes that any even sum implies the subarray is good. But in reality, there's a case when the subarray length is 1. For such cases, even though the sum is even, the subarray is only valid if the single element can be arranged such that the XOR (which is the element itself) is zero. Which is only possible if the element can be rearranged into zero. Which is impossible unless c_i is zero. Because to have the element be zero after rearrangement, the count of set bits (c_i) must be zero. So even if the sum is even, if the subarray length is 1, it's only valid if c_i is zero. So this case must be handled separately.

So the initial approach is missing this condition. Therefore, our previous reasoning is incorrect.

This explains why the first example's [1,1] is not valid. Because the sum is even (2), but the element can't be arranged to have a value of zero. Because c_i is 2, which can't be zero. So the sum being even is necessary but not sufficient in the case of subarrays of length 1.

So the problem is more complex than initially thought.

So the correct condition is:

For a subarray to be good:

If the length is 1:

   The sum of c_i (which is the single c_i) must be zero (i.e., the element is zero). But wait, the element can be rearranged into any permutation of its bits. So if c_i is zero, the element is zero. So the XOR is zero, valid.

If the length is more than 1:

   The sum of c_i must be even, and:

   Either the sum is even, and the length is more than 1.

Wait, but in the case of length 1, even if sum is even, it's only valid if the sum is zero (i.e., c_i is zero). Because the element's value after rearrangement can only be zero if there are no set bits.

So the correct approach is to compute all subarrays where:

- Either the subarray has length 1 and the c_i is zero.

OR

- The subarray has length >= 2 and the sum of c_i is even.

So the total count is:

number of subarrays with sum even and length >=2, plus the number of elements with c_i=0.

But how to compute this?

Let's think:

In the initial approach, the code counts all subarrays with even sum (including those of length 1). But we need to subtract those subarrays of length 1 with even sum (since they are only valid if their sum is zero).

So the total count would be:

total_even_subarrays = initial approach's answer.

subtract the number of elements where c_i is even (since these are counted in the initial approach but only valid if c_i is zero).

Then add the number of elements where c_i is zero (since those are valid).

So:

result = (initial total) - (number of even c_i) + (number of c_i equal to zero).

But how to compute this?

Alternatively:

The valid subarrays are:

- All subarrays of length >=2 with even sum.

- Plus, subarrays of length 1 where c_i is zero.

So:

We can compute the initial answer (counting all even sum subarrays, including length 1). Then subtract the count of elements with even c_i (since they were included in the initial answer but are only valid if c_i is zero). Then add the count of elements with c_i zero (since those are valid).

So:

result = (initial_total) - even_count + zero_count.

Where:

- initial_total is the result from the initial approach (counting all even sum subarrays, including length 1).

- even_count is the number of elements with even c_i (i.e., the number of length 1 subarrays that were incorrectly counted as valid if c_i is even but non-zero).

- zero_count is the number of elements with c_i zero (correctly valid length 1 subarrays).

But how?

Wait, the initial approach counts all subarrays with even sum. For length 1, those are exactly the elements with even c_i. But among these, only those with c_i zero are valid. So the number of valid length 1 subarrays is zero_count.

So the correct answer is:

(initial_total - (even_count - zero_count)) + zero_count.

Which simplifies to initial_total - even_count + 2 * zero_count.

Alternatively:

initial_total counts even_count (elements with even c_i) as valid. But of those, only zero_count are valid. So the number of invalid length 1 subarrays counted is (even_count - zero_count). So subtract that from initial_total, and add zero_count.

So the correct total is:

initial_total - (even_count - zero_count) + zero_count = initial_total - even_count + 2*zero_count.

Alternatively:

The correct count is (initial_total - even_count) + zero_count.

Because the initial approach includes even_count subarrays of length 1, of which only zero_count are valid. So the initial approach's total is:

(number of valid subarrays of length >=2) + even_count.

But the correct answer is (number of valid subarrays of length >=2) + zero_count.

So the difference is (even_count - zero_count). So subtract (even_count - zero_count) from initial_total.

So:

result = initial_total - even_count + zero_count.

Yes, because:

initial_total = valid_subarrays_ge2 + even_count.

But the correct result is valid_subarrays_ge2 + zero_count.

So subtracting (even_count - zero_count) from initial_total gives:

initial_total - even_count + zero_count = (valid_subarrays_ge2 + even_count) - even_count + zero_count = valid_subarrays_ge2 + zero_count.

Which is correct.

So the approach now is:

1. Compute the initial answer as before (count all even sum subarrays, including length 1).

2. Compute even_count as the number of elements with c_i even.

3. Compute zero_count as the number of elements with c_i zero.

4. The correct answer is initial_total - even_count + zero_count.

So this adjustment will handle the case where a length 1 subarray has even c_i but non-zero, which are invalid.

Let's test this with the first example.

First example's c array is [2,3,3].

even_count: 2 is even, 3 is odd, 3 is odd → even_count is 1.

zero_count: none of the elements are zero → zero_count is 0.

initial_total computed by the initial code is 3 (as before).

So the result is 3 - 1 + 0 = 2, which matches the sample output.

Another example: the second sample input:

4

1 2 1 16

The elements are 1 (binary 1 → c=1), 2 (10 → c=1), 1 (c=1), 16 (10000 → c=1).

So c array is [1,1,1,1].

Each c_i is 1 (odd). So even_count is zero. zero_count is zero.

The initial_total would be computed as follows:

prefix_parity starts at 0.

Process first element (1): parity becomes 1 → count += 0 (parity_counts has {0:1}, current is 1. So count remains 0. Then add 1 to parity_counts[1] → {0:1, 1:1}.

Second element (1): parity (1+1) mod 2 = 0. count += parity_counts[0] → 1. Total becomes 1. Then add to parity_counts[0] → 2.

Third element (1): parity (0+1) → 1. count += parity_counts[1] (1) → total 2. Then parity_counts[1] becomes 2.

Fourth element (1): parity (1+1) → 0. count += parity_counts[0] (2) → total 4. Then parity_counts[0] becomes 3.

So initial_total is 4.

even_count is zero (all c_i are 1, which is odd). zero_count is zero. So the result is 4 -0 +0 =4, which matches the sample output.

Another test case: suppose there's an element with c_i=0. For example, input is [0]. Then c_i is 0. even_count is 1 (0 is even), zero_count is 1. initial_total would be 1 (the count of even sum subarrays). So result is 1 -1 +1 =1.

Another example: element is 3 (c_i=2). Even_count is 1, zero_count is 0. initial_total would count it as 1. result is 1-1 +0 =0. Which is correct, because the element is 3 (c_i=2 even), but can't be rearranged to zero (since two set bits can be arranged as 3, which is 11, XOR of 3 is 3, not zero). So the subarray [1,1] is invalid.

But wait, according to the initial approach, sum is even (2). So the code counts it. But according to the adjusted approach, even_count is 1, zero_count 0. So the result is 1-1+0=0. Correct.

So this adjustment handles the cases where length 1 subarrays have even c_i but are not zero.

Thus, the correct approach is to compute the initial total using the prefix parity method, then subtract the number of elements with even c_i and add the number of elements with zero c_i.

So now, the steps to solve the problem:

1. For each a_i, compute c_i = bin(a_i).count('1').

2. Compute the initial_total using the prefix parity approach (counting all even sum subarrays, including length 1).

3. Compute even_count as the number of c_i that are even.

4. Compute zero_count as the number of c_i equal to zero.

5. The result is initial_total - even_count + zero_count.

Now, to implement this in Python.

But first, we need to compute c_i for each a_i. Given that a_i can be up to 1e18, but in Python, bin() is efficient.

Then, compute initial_total using the standard parity counting.

Now, code outline:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    c = [bin(x).count('1') for x in a]

    even_count = 0
    zero_count = 0
    for cnt in c:
        if cnt % 2 == 0:
            even_count +=1
        if cnt ==0:
            zero_count +=1

    current_parity = 0
    parity_counts = {0: 1}
    initial_total =0
    for num in c:
        current_parity = (current_parity + num) %2
        initial_total += parity_counts.get(current_parity,0)
        parity_counts[current_parity] = parity_counts.get(current_parity,0) +1

    result = initial_total - even_count + zero_count
    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
1 2 1 16
""",
            "output": \
"""\
4
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

4

1 2 1 16

c = [1,1,1,1]. even_count=0. zero_count=0.

initial_total:

current_parity=0, parity_counts {0:1}.

Processing 1: parity becomes 1. add 0. total 0. parity_counts[1] =1.

Processing 1: parity becomes 0. add parity_counts[0] (1). total=1. parity_counts[0] =2.

Processing 1: parity becomes 1. add parity_counts[1] (1). total=2. parity_counts[1]=2.

Processing 1: parity becomes 0. add parity_counts[0] (2). total=4. parity_counts[0]=3.

result=4-0+0=4. Correct.

Another test case: input [0], c=0.

even_count=1, zero_count=1.

initial_total: processing 0. current_parity 0. add parity_counts[0] (1). initial_total=1. parity_counts[0] becomes2.

result=1-1+1=1. Which is correct.

Another test case: input [3], c=2.

even_count=1, zero_count=0.

initial_total=1. result=1-1+0=0. Correct.

So the code works for these cases.

Thus, the correct approach is to use the prefix parity method and adjust for the length 1 subarrays that are invalid.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
c = [bin(x).count('1') for x in a]

even_count = 0
zero_count = 0
for cnt in c:
    if cnt % 2 == 0:
        even_count += 1
    if cnt == 0:
        zero_count += 1

current_parity = 0
parity_counts = {0: 1}
initial_total = 0
for num in c:
    current_parity = (current_parity + num) % 2
    initial_total += parity_counts.get(current_parity, 0)
    parity_counts[current_parity] = parity_counts.get(current_parity, 0) + 1

result = initial_total - even_count + zero_count
print(result)
```
