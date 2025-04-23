<think>
Okay, let's try to understand this problem. So, we need to count the number of blocks of each possible length from 1 to n in all the numbers from 0 to 10^n - 1, padded with leading zeros to make them exactly n digits. Then output each count modulo 998244353.

Hmm. Let's think about what a block is. A block is a consecutive segment of the same digit that can't be extended left or right. So for example, in 00027734000, the first three 0s form a block of length 3. Then 2 is a single, then 77 is a block of length 2, etc. Each position in the number can be part of a block of some length. But how do we count all these blocks across all possible n-digit numbers?

The key is to find, for each i from 1 to n, the total number of blocks of length exactly i in all the numbers.

Let's break this down. For each position in the n-digit number, maybe we can find out how many times a block of length exactly i starts at that position. Then sum over all positions and all digits.

Wait, but blocks can be of varying lengths, and their positions might overlap. So for example, a block of length 3 includes three positions. But we need to count each occurrence of a block exactly once for its length.

Alternatively, perhaps for each possible position in the number, determine how many blocks of length exactly i start there and are not part of a longer block. Wait, no. Because a block of length exactly i is a maximal sequence of the same digit. So, for a position j in the digit string, if the digit at j is the same as j-1 and j+1, then it's part of a longer block. But the block length is determined by how far it extends.

Hmm. Let's model this differently. For a block of length exactly i, it must consist of exactly i consecutive same digits, and the digits before and after (if they exist) must be different. Except for the edges of the number.

For example, a block of length i starting at position k (0-based) must satisfy:

- The next i-1 digits (positions k to k+i-1) are the same as the digit at k.
- The digit before position k (if k > 0) is different from the digit at k.
- The digit after position k+i-1 (if k+i-1 < n-1) is different from the digit at k.

Wait, no. Because the block can be at the start or end. So for example, if the entire number is the same digit, then it's a single block of length n. But if there's a part where digits change, then the blocks are determined by transitions.

Alternatively, the number can be split into blocks where each block is a sequence of the same digit, and consecutive blocks have different digits. So, for each number, the total number of blocks is the number of transitions between different digits plus one (since each transition starts a new block). But that's about the number of blocks, not their lengths. But here, we need to count for each possible length i, how many blocks of exactly that length exist across all numbers.

So the approach for solving this is to calculate for each possible i, the total number of blocks of length exactly i across all numbers.

Let's think for a specific i. How can we compute the number of blocks of length exactly i in all numbers?

Each such block can be in any position of the n digits. Let's model this as follows: For a block of length exactly i, it must be a sequence of i identical digits, such that either:

- The block is at the beginning of the number, and the digit after the block (if exists) is different.
OR
- The block is at the end of the number, and the digit before the block (if exists) is different.
OR
- The block is in the middle, and the digits before and after are different from the block's digit.

Additionally, the block can't be part of a longer sequence. So for example, a block of length i must have exactly i same digits, and not be part of a longer run.

So, for a block of length exactly i, it must be preceded by a different digit (if possible) and followed by a different digit (if possible).

So, for a block of length exactly i, the possible positions in the number are positions from 0 to (n - i). Wait, no. Because the block is exactly i digits long. So for a block starting at position s and ending at position s + i -1, that's i digits. So the possible start positions s can be from 0 to n - i.

Wait, the block of length i starts at s and occupies s, s+1, ..., s+i-1. So the maximum possible s is n - i.

Yes.

So, for each possible i, we can calculate the number of blocks of length exactly i as follows:

For each possible start position s (0 <= s <= n - i), count how many numbers have a block of exactly i digits starting at s. Then sum over all s and all possible digits (digits 0-9 for the block, but possibly with some constraints for leading zeros? Wait, but the problem says that numbers are written with leading zeros. So all numbers are considered as n-digit strings, possibly starting with zeros. So 000 is allowed as a valid 3-digit number. So leading zeros are allowed.

So, for each possible s (start position of the block) and digit d, the number of numbers where positions s to s+i-1 are d, and:

- If s > 0, the digit at s-1 is not d.
- If s + i < n, the digit at s+i is not d.

And the rest of the digits (positions not in s-1 to s+i) can be anything, except for the constraints that they don't create a longer block.

Wait, no. Because the rest of the digits are not part of the block. So the rest of the digits can be anything except that the block's adjacent digits (if they exist) are different. The rest of the digits can have their own blocks, but we are only counting the current block here.

Wait, the problem is to count all blocks of length exactly i in all numbers. So each occurrence of a block in any number contributes to the count. So even if a number has multiple blocks of length i, each of them is counted.

So, for a specific i, the total number of blocks of length i is the sum over all possible positions (start positions s) where a block of length i starts at s, and for each such s, the number of numbers that have a block of exactly i digits starting at s.

So the plan is: For each i, compute for each possible start position s (from 0 to n-i), the number of numbers where s is the start of a block of exactly i digits. Then sum all these over s.

So how do we compute for a given i and s, the number of such numbers?

Let's break it down. For a block of length exactly i starting at s, the digits s to s+i-1 are all d (some digit from 0-9), and:

- If s > 0, the digit at s-1 is not d.
- If s+i < n, the digit at s+i is not d.

The other digits (positions not in s-1, s, ..., s+i) can be any digits, but they can form their own blocks. However, for our current block (starting at s) to be exactly i in length, the adjacent digits must differ from d.

So, the steps for a given i and s:

1. Choose d: 10 possibilities (digits 0-9). However, if the block is starting at position 0 and s=0, then for example, if the entire number is all d, then the block is of length n, but if i is less than n, then the block of i is part of a longer block. So no, but in our case, we're ensuring that the block is exactly i, so the adjacent digits (if they exist) must be different.

So for each s and i:

The count for that s and i is:

number of d in 0-9 (10 choices) multiplied by:

the number of ways to set the adjacent digits (s-1 and s+i) to not be d, multiplied by the number of possibilities for the rest of the digits (those not in s-1, s, ..., s+i).

But what about the rest of the digits (positions not in s-1, s, s+1, ..., s+i)? They can be anything except for the constraints that they don't form a longer block. Wait, no. Because those digits are part of other blocks. But the problem is to count all blocks across all numbers. So each occurrence of a block in any position is counted. So when we are considering a particular block starting at s, we need to make sure that in that particular number, the block of i digits starting at s is a valid block (i.e., the adjacent digits are different). The rest of the digits in the number can be anything. So the rest of the digits (positions not adjacent to this block) can be any digits, as long as the adjacent conditions are satisfied.

So, for example, the digits before s-1 (if any) can be anything, as long as they don't affect the block starting at s. Similarly, the digits after s+i can be anything, but the digit at s+i must be different from d (if it exists).

So, for a given s and i:

The digits in positions s to s+i-1 are all d (10 choices).

If s > 0, then the digit at s-1 must be not d.

If s + i < n, then the digit at s + i must be not d.

The other digits (positions not in s-1, s, s+i) can be any digit, except that they don't affect the current block. So for example, the digits before s-1 can be anything, as long as the digit at s-1 is not d. The digits after s+i can be anything, as long as the digit at s+i is not d. The digits in the positions s to s+i-1 are fixed as d.

Wait, but the digits outside of the current block and its adjacent positions (s-1 and s+i) can be anything. So for example, the digits at positions 0 to s-2 can be anything, as long as they don't affect the current block. But since the current block starts at s, the digit at s-1 (if it exists) must not be d. The digits before s-1 can be anything. Similarly, the digits after s+i can be anything, but the digit at s+i (if exists) must not be d.

So, for the digits not adjacent to the block (positions < s-1 or positions > s+i), they can be any digit. But for the adjacent positions (s-1 and s+i), they must be different from d.

So, putting it all together:

For a given i and s:

The count is 10 (choices for d) multiplied by:

left = if s > 0: 9 (since the digit at s-1 can't be d. 9 choices)
       else: 1 (since there's no digit before s-1; but s=0 implies s>0 is false, so left is 1?)

Similarly, right = if s + i < n: 9 (digit at s+i can't be d)
                else: 1 (no digit after)

Then, the other positions (those not in s-1, s, ..., s+i) can be any digits. So for those positions:

The positions before s-1 (if any) can be any digits. The positions after s+i (if any) can be any digits. So the total possibilities for these positions are 10^(number of such positions).

So the number of possibilities is:

10 (d) * left * right * 10^(other positions).

Now, what is the number of other positions?

The total number of positions in the number is n.

The positions involved in the current block and adjacent checks are:

- s-1 (if s >0)
- s to s+i-1 (i positions)
- s+i (if s+i < n)

The other positions are all positions except these.

So the number of other positions is:

total_other = n - [ (s >0 ? 1 : 0) + i + (s+i < n ? 1 : 0) ]

So, for example:

If s=0 and i=2 in a n=5-digit number, then s-1 is invalid. s to s+1 is 0 and 1. s+i=2. If s+i < n (2 <5 yes), then we have s+i=2. So the adjacent positions are 0 (s-1 invalid) and 2. So the other positions are 3,4, and 5-1=4? Wait, n=5 digits are positions 0,1,2,3,4.

s=0, i=2. The block is positions 0 and 1. s+i=2. So positions 0,1 are the block. s+i=2. So if s+i <n (2 <5 yes), then the digit at position 2 must be not d. So the adjacent positions are 2. So the other positions are positions 3,4, and any positions before s-1 (which is none). So the other positions are 3,4. So 2 positions. So 10^2 possibilities.

So the formula for other positions:

other_positions = n - ( (s>0 ? 1 : 0) + i + (s+i <n ? 1 : 0) )

So total_other = n - ( (s>0) + i + (s+i <n) )

So the number of possibilities is:

count = 10 * left * right * (10 ** total_other)

But since n can be up to 2e5 and s can be up to n-i, which can be up to 2e5, we need a way to compute this efficiently for all possible s and i.

But even O(n^2) approaches would be too slow. So we need a way to compute this in O(n) time.

So the challenge is to find, for each i from 1 to n, the sum over all possible s (0 <= s <= n - i) of 10 * left(s, i) * right(s, i) * 10^(other_positions(s, i)).

But let's see if we can find a pattern here.

Let's reorganize the formula.

For a given i, and s:

left(s, i) is:

if s > 0: 9 (since s-1 exists and must not be d)
else: 1 (no s-1)

right(s, i) is:

if s + i < n: 9 (digit at s+i must not be d)
else: 1 (no s+i)

The other_positions is (n - ( (s>0) + i + (s + i <n) )) 

But (s>0) is 1 if s>0 else 0. Similarly for (s+i <n).

So other_positions = n - (a + i + b), where a and b are 0 or 1.

But a and b depend on s and i.

Let me see. Let's express other_positions as:

other_positions = (n - i) - ( (s>0) + (s+i <n) )

Because (a + i + b) = i + a + b. So n - (i + a + b) = (n -i) - (a + b).

So other_positions = (n -i) - (a + b) 

Where a is 1 if s>0, else 0.

b is 1 if s+i <n, else 0.

So the term 10^other_positions can be written as 10^{ (n -i) - (a + b) } = 10^{n -i} / 10^{a + b} }

So the count for s and i is:

10 * left * right * 10^{ (n -i) - (a + b) } 

But left is 9 if s>0 (a=1), else 1 (a=0). Similarly, right is 9 if b=1 (s+i <n), else 1.

So left = 9^a, because when a is 1 (s>0), left is 9, else 1.

Similarly, right = 9^b.

So the count becomes:

10 * 9^a * 9^b * 10^{ (n -i) - (a + b) } 

Which is equal to:

10 * 9^{a + b} * 10^{n -i -a -b} }

Which simplifies to:

10 * (9/10)^{a + b} * 10^{n -i} }

Hmm, that's interesting. Let's see:

Because 9^{a + b} * 10^{n-i -a -b} = 10^{n-i} * (9/10)^(a + b).

So the count is 10 * 10^{n-i} * (9/10)^(a + b) = 10^{n - i + 1} * (9/10)^(a + b).

But a and b are each 0 or 1. So a + b can be 0, 1, or 2.

But how to compute this for each s and i?

Alternatively, perhaps we can split into cases based on the positions of s.

For each i, the possible s can be in various positions where the start of the block is in the middle, start, end, or isolated.

Alternatively, for each i, the sum over s can be broken into three cases:

1. s is 0: then a=0 (since s>0 is false), and b=1 if s +i <n (i.e., i <n), else 0.

Wait, for s=0, s+i <n is equivalent to i <n. But when s=0, s+i =i. So if i <n, then s+i <n is true (since 0 <=s <=n-i implies that i <=n -s, but s is 0 here, so i <=n). So when s=0, i can be from 1 to n (since s can be 0 as long as i <=n). For s=0 and i =n, then s+i =n, which is not <n. So in that case, b=0.

So for s=0, the possible values of a and b are:

a=0, and b=1 if i <n, else 0.

Similarly, s =n -i (so the block ends at position n-1). For this s, s+i = (n -i) +i =n, which is >=n, so b=0.

So for each i, s can be 0, in the middle, or n-i.

But perhaps it's easier to consider all possible s in the range 0 <=s <=n-i.

But the problem is that for each s, the variables a and b (which are 0 or 1) depend on s and i.

But perhaps there's a way to group the terms based on the values of a and b.

For example, for a given i, how many s have a=0 and b=0? That's when s=0 and s+i >=n (i.e., s=0 and i >=n. But since s=0, i can be up to n. So when i =n, s=0, s+i =n, which is not <n. So for i =n, s=0 is the only possible s (since n-i=0, so s can only be 0). And a=0, b=0. So for i =n, the count is 10 * 1 *1 *10^{n -i} =10 * 1*1 *10^{0} =10. Which matches the first sample input (n=1, output 10).

So for the general case, perhaps we can split the sum into terms where a and b are 0, 1, or 2.

But how?

Let me think for a given i.

The possible combinations of a and b:

a can be 0 or 1 (since s can be 0 or not).

b can be 0 or 1 (since s+i can be <n or not).

So for a given i, the sum over s can be divided into four cases:

1. a=0, b=0: s=0 and s+i >=n. So i >=n. But when i >=n, the only possible s is 0 (since n-i <=0), but in this case, s+i =i >=n. So for i =n, s=0, a=0, b=0.

But i ranges from 1 to n. So when i =n, s=0, and s+i =n >=n. So this is the only case where a=0 and b=0.

2. a=0, b=1: s=0 and s+i <n. So i <n. For these cases, s=0 and i <n. So in this case, s+i =i <n. So s=0 is allowed only when i <=n-1. For example, if n=5, i=3, then s=0 is allowed (0 <=0 <=5-3=2). So s=0, a=0, b=1 (since 0+3=3 <5).

3. a=1, b=0: s>0 and s+i >=n. So s>0 and s +i >=n. But s <=n-i. So s can be from max(1, n-i) to n-i. But s <=n-i. So s+i <=n-i +i =n. So s+i >=n implies s+i =n. So s =n -i. But since s>0, this implies n-i >0. So i <n. For example, if i=3 and n=5, then s can be 2 (n-i=2). Then s+i=5, which is equal to n. So b=0.

4. a=1, b=1: s>0 and s+i <n. So in this case, s can vary from 1 to n-i-1 (since s +i <n implies s <n -i). So for example, if i=3 and n=5, s can be 0 (case 2) or 1 (n-i-1 =5-3-1=1). So s=1. Then s+i=4 <5. So a=1, b=1.

So for each i, the sum over s can be broken into these four cases. But some of these cases may not be possible for certain i values.

Let's handle each case:

Case 1: a=0, b=0. Only possible when i =n. So s=0. Then the count is 10 * 1 *1 *10^{n-i} =10*1*1*10^0=10. So for i=n, the sum is 10.

Case 2: a=0, b=1. This is possible only when i <n and s=0. So s=0 is allowed (since 0 <=0 <=n-i-0, which is 0 <=0 <=n-i). So the count for this s is 10 *1 *9 *10^{n-i - (0+1)} } = 10*9 *10^{n-i-1} = 9 * 10^{n-i} }

But wait, the other_positions is (n-i) - (a + b) = (n-i) - (0+1) =n-i-1. So 10^{n-i-1} multiplied by 10*9 (from left and right). So 10 *9 *10^{n-i-1} =9*10^{n-i}.

So for this case, the contribution to the sum is 9*10^{n-i} (only once, when s=0 and i <n).

Case 3: a=1, b=0. This occurs when s= n-i and s>0. So s =n-i must be >0, which implies that n-i >0 → i <n. For example, i=3 and n=5. Then s=2. So s>0. So the contribution here is 10 *9 *1 *10^{ (n-i) - (1 +0) } = 10*9*1 *10^{n-i-1} =9*10^{n-i} 

Wait, let's compute:

a=1 → left is 9, and b=0 → right is 1. So left*right=9*1=9.

other_positions is (n-i) - (1 +0) =n-i-1.

So 10 *9 *1 *10^{n-i-1} =9 * 10 * 10^{n-i-1} =9*10^{n-i}.

So for this case, the contribution is 9*10^{n-i} (only once, when s= n-i and i <n).

Case4: a=1, b=1. This occurs when s>0 and s +i <n. So s can range from 1 to (n-i-1). The number of s in this case is (n-i-1) -0 +1 -1 =n-i-1. Wait, s can be from 1 to (n-i-1), inclusive. The number of such s is (n-i-1) -1 +1 =n-i-1. For example, if n-i-1 =5, s ranges from 1 to5: 5 values.

Each such s contributes:

10 *9 *9 *10^{ (n-i) -2} 

Because a=1 and b=1, so a +b=2. other_positions is (n-i) -2. So 10^{(n-i)-2}.

So the contribution per s is 10 * 9*9 *10^{n-i-2} = 81 *10^{n-i-1}.

So for each of the (n-i-1) s in this case, the contribution is 81*10^{n-i-1}.

So the total for case4 is (n-i-1) *81 *10^{n-i-1}.

Putting all cases together for a given i:

Total blocks of length i is:

case1 (if i ==n) → 10.

case2 (if i <n) → 9*10^{n-i}

case3 (if i <n) →9*10^{n-i}

case4 (if i <n) → (n-i-1)*81 *10^{n-i-1}

So for i <n:

sum = case2 + case3 + case4 

=9*10^{n-i} +9*10^{n-i} + (n-i-1)*81*10^{n-i-1} 

= 18*10^{n-i} + (n-i-1)*81 *10^{n-i-1}

= 10^{n-i-1} * (18*10 + (n-i-1)*81 )

= 10^{n-i-1} ( 180 + 81(n-i-1) )

Factor out 9:

= 9 *10^{n-i-1} (20 + 9(n -i -1) )

But maybe not necessary.

Alternatively:

Let's factor 10^{n-i-1}:

18*10^{n-i} = 18*10 *10^{n-i-1} =180*10^{n-i-1}

Similarly, (n-i-1)*81*10^{n-i-1} is the same as 81*(n-i-1) *10^{n-i-1}

So the sum is (180 +81*(n-i-1)) *10^{n-i-1}

Factor 9:

=9 * (20 +9*(n-i-1)) ) *10^{n-i-1}

Hmm, but perhaps we can find a pattern here.

Alternatively, for i <n:

sum = 18 *10^{n-i} + 81*(n-i-1)*10^{n-i-1}

= 10^{n-i-1} (18 *10 + 81 (n-i-1) )

=10^{n-i-1} ( 180 + 81 (n-i-1) )

= 10^{n-i-1} * 81 ( (180/81) + (n-i-1) )

But 180/81 = 20/9 ≈2.222... which is not helpful.

Alternatively, factor 9:

= 9 * 10^{n-i-1} ( 20 +9 (n-i-1) )

But perhaps this isn't helpful.

So, combining all terms:

For i <n, the total is:

sum = 2 *9 *10^{n-i} + (n-i-1) *9*9 *10^{n-i-1}

Which is 18*10^{n-i} + 81*(n-i-1)*10^{n-i-1}

= 10^{n-i-1} (18 *10 + 81 (n-i-1) )

= 10^{n-i-1} (180 +81(n-i-1) )

We can factor 9 from the terms inside:

180 = 9 *20, 81 =9*9.

So:

= 9*10^{n-i-1} (20 +9(n-i-1) )

Which is 9*10^{n-i-1} (9(n-i-1) +20 )

Hmm.

But perhaps we can compute this for each i as follows:

For each i from 1 to n-1:

sum = 9 * 10^{n-i-1} * ( 9*(n-i-1) + 20 )

And for i =n:

sum=10.

So, the formula for the count when 1 <=i <n is:

count = 9 * ( 9*(n-i-1) +20 ) * 10^{n-i-1} 

But 9*(n-i-1) +20 =9(n-i-1) +20 =9(n-i) -9 +20 =9(n-i) +11.

So:

count =9*(9(n-i) +11 -9 +20) → no, perhaps I made a mistake here.

Wait, 9*(n-i-1) is 9(n-i-1) =9n -9i -9.

Add 20 gives 9n -9i +11. Not sure.

Alternatively, perhaps the expression can be written as 9(n-i-1) +20 = 9(n-i) -9 +20 =9(n-i) +11.

Yes. So:

count =9*(9(n-i) +11) *10^{n-i-1} ?

Wait, no. 9*(n-i-1) +20 =9(n-i-1) +20 = 9(n-i) -9 +20 =9(n-i) +11.

So yes.

So:

count = 9*(9(n-i) +11) *10^{n-i-1} ?

Wait, no. Because the original formula is 9*(9(n-i-1)+20) * 10^{n-i-1} ?

Wait, let's re-calculate:

Original sum for i <n:

sum =9 *10^{n-i} +9*10^{n-i} + (n-i-1)*81*10^{n-i-1}

Which is 18*10^{n-i} + 81*(n-i-1)*10^{n-i-1}

Factor 9*10^{n-i-1}:

=9*10^{n-i-1} ( 2*10 +9*(n-i-1) )

=9*10^{n-i-1} ( 20 +9(n-i-1) )

Which is the same as 9*10^{n-i-1} (9(n-i-1) +20 )

So yes.

Now, for each i from 1 to n-1:

count[i] =9 * (9*(n-i-1) +20) *10^{n-i-1}

But wait, 20 is 2*10, but I'm not sure how helpful that is.

But regardless, the formula seems manageable.

So the problem reduces to, for each i in 1..n:

if i ==n:

   result is 10

else:

   result is 9 * (20 +9*(n-i-1)) * (10^(n-i-1)) )

mod 998244353.

So now, how do we compute this efficiently?

The challenge is to compute 10^k modulo 998244353 for k up to 2e5, and then for each i compute the term.

But first, precompute the powers of 10 modulo MOD, where MOD=998244353.

So precompute pow10 = [1]*(n+1)

pow10[0] =1

for k in 1 to n:

   pow10[k] = (pow10[k-1] *10) % MOD

But for n up to 2e5, this is O(n) time.

Then, for each i:

if i ==n:

   res =10

else:

   exponent = (n-i-1)

   term = (9 * (20 + 9*( (n-i-1) )) ) * pow10[exponent] 

   term = term % MOD

So wait, for example:

if n=2 and i=1:

exponent =2-1-1=0. pow10[0] is 1.

20 +9*(2-1-1) =20+0=20. 9*20=180. 180*1=180. Which matches the first output of 180.

For i=2 and n=2: the sum is 10, which matches the second output of 10.

Another example: n=3, i=1.

exponent=3-1-1=1. pow10[1]=10.

20+9*(3-1-1) =20 +9*1=29. 9*29=261. 261 *10=2610 mod MOD.

So for i=1, count is 2610.

Wait, but let's verify this.

For i=1 and n=3:

Each block of length 1 must be a single digit that is different from both its left and right neighbors. But since the block is exactly 1, the digit must be different from both left and right, if they exist.

But wait, for i=1, the block is length 1. So for each position s in 0..2 (since n=3, i=1, so s can be 0,1,2).

For each s:

The count is 10 * left * right * 10^{ other }

For s=0:

left (s>0) is false → left=1.

s+i =1 <3 → right=9.

other positions: 3 - (0+1+1) =3 -2=1.

So 10^1.

So term for s=0 is 10 *1*9 *10^1 =10 *9 *10 =900.

s=1:

left=9 (s>0).

s+i=2 <3 → right=9.

other positions: 3- (1+1+1) →3-3=0. 10^0=1.

term:10*9*9 *1= 810.

s=2:

left=9 (s>0).

s+i=3 >=3 → right=1.

other positions:3- (1+1+0) →1. 10^1=10.

term:10*9*1*10=900.

Summing all three:900 +810 +900= 2610 → which matches the formula's result of 2610.

So the formula works.

So the formula for i <n is correct.

So the plan is:

1. Precompute the powers of 10 modulo 998244353 up to n.

2. For each i from 1 to n:

   if i ==n:

      result is 10 mod MOD.

   else:

      exponent =n-i-1

      term = (20 +9* (exponent)) ) *9 

      term = term * pow10[exponent]

      mod MOD.

So for example, when exponent is (n-i-1), which is the exponent in 10^{exponent}.

So the code steps are:

Read n.

Compute pow10 array up to n.

Then for each i in 1..n:

   if i ==n:

      ans[i] =10 % MOD

   else:

      exponent =n-i-1

      part1 =20 +9 * exponent

      total =9 * part1

      total = (total * pow10[exponent]) % MOD

      ans[i] =total

But in the code, we need to output the answers for i=1 to i=n in order.

But in the formula, for i=1, the exponent is n-1-1 =n-2. So pow10[n-2].

But when n=2, exponent for i=1 is 0. Which is correct.

But wait, for n=3 and i=1: exponent=3-1-1=1. Which is correct.

So the code would be:

MOD =998244353

n =int(input())

pow10 = [1]*(n+2)

for k in range(1, n+2):

   pow10[k] = (pow10[k-1]*10) % MOD

ans = []

for i in range(1, n+1):

   if i ==n:

      ans.append(10% MOD)

   else:

      exponent =n -i -1

      part1 =20 +9 * exponent

      total = (9 * part1) % MOD

      total = (total * pow10[exponent]) % MOD

      ans.append(total)

print(' '.join(map(str, ans)))

But wait, let's test this against the examples.

First example: n=1.

pow10 is [1, 10, ...]

For i=1:

since i==n, append 10 mod MOD. So output is 10.

Which matches.

Second example: n=2.

For i=1:

exponent =2-1-1=0.

part1 =20 +9*0=20.

total=9*20=180. multiply by 10^0=1 →180 mod MOD.

For i=2: append 10.

So output is 180 10.

Which matches.

Third example: n=3, i=1:

exponent=3-1-1=1.

pow10[1]=10.

part1=20 +9*1=29.

9*29=261. 261 *10=2610 mod MOD.

So the code for i=1 gives 2610.

Which aligns with our previous manual calculation.

So this code should work.

Now, let's check the edge case where i= n-1. For example, n=3, i=2.

exponent=3-2-1=0.

part1=20 +9*0=20.

total=9*20=180. multiply by 10^0 →180.

But what's the actual count for i=2 and n=3.

Each block of length 2.

For all possible s (0 and 1):

s=0: block is positions 0 and 1.

adjacent check: s=0, so left is 1 (no digit before). s+i=0+2=2 <3 → right must be different.

So left=1, right=9.

other positions: positions 2 (but s+i=2, so adjacent to the block. So other positions are positions not in s-1 (0-1= -1), s to s+i-1 (0,1), s+i (2). So other positions are 3 - (0 + 2 + 1) →3 -3=0. So 10^0=1.

So term for s=0:10 *1*9 *1 =90.

s=1: positions 1,2. left is digit 0 (s>0, so must be different from d. So left=9. right is s+i=3 >=3 → right=1. other positions: 3 - (1+2+0) →0. So 10*9*1 *1=90.

Total sum is 90+90=180. Which matches the code's output.

So the code works.

Another edge case: n=2, i=1.

Exponent =0. So 20 +0=20. 9*20=180. 10^0=1. So 180*1=180.

Yes.

So the code is correct.

Now, regarding the constraints. n can be up to 2e5. Precomputing pow10 up to 2e5 is O(n), which is acceptable. Then, for each i, we compute O(1) time. So overall O(n), which is acceptable for n=2e5.

Memory-wise, the pow10 array is O(n), which is acceptable for 2e5.

So this approach is optimal.
</think>

```python
MOD = 998244353
n = int(input())

if n == 0:
    print(0)
else:
    pow10 = [1] * (n + 1)
    for k in range(1, n + 1):
        pow10[k] = (pow10[k-1] * 10) % MOD
    
    result = []
    for i in range(1, n + 1):
        if i == n:
            res = 10 % MOD
        else:
            exponent = n - i - 1
            part = (20 + 9 * exponent) % MOD
            res = (9 * part) % MOD
            res = (res * pow10[exponent]) % MOD
        result.append(res)
    
    print(' '.join(map(str, result)))
```