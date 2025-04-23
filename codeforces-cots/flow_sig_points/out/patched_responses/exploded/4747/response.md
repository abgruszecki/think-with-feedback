<think>
Okay, let's tackle this problem. So the task is to determine if we can turn x into y by performing some number of allowed operations. The operations involve taking the binary representation of x, adding a 0 or 1 to the right, reversing it, and then converting back to decimal. Hmm.

First, let's understand the operation better. Let's take an example. Let's say x is 34. Its binary is 100010. If we add a 0, it becomes 1000100. Then reverse it, which gives 0010001. But leading zeros are removed, so that's 10001 which is 17. Alternatively, adding 1 gives 1000101, reverse to get 1010001 (binary for 81).

So the key steps here are: append a 0 or 1, reverse the bits (leading zeros are stripped after reversing), and that's the new x.

We need to see if starting from x, through any sequence of these operations, we can reach y.

The problem constraints are up to 1e18 for x and y, which is a big number. So any brute force approach that tries all possible paths is out of the question. We need a smarter approach.

Let's think about the possible transformations. Each step gives us two options: append 0 or 1, reverse, and then proceed. But since the numbers can be up to 1e18, the binary representations can be up to 60 bits. So even considering all possible binary strings of up to 60 bits is manageable, but maybe there's a way to model this more efficiently.

Wait, but maybe we can model this as a BFS problem. However, with numbers up to 1e18, the BFS queue could become too large. For example, each step could generate two new numbers, and if we have 60 steps, that's 2^60 possibilities. That's way too big. So BFS is not feasible here.

So we need a way to model this without exploring all possibilities. Let's think in reverse. Instead of trying to build up from x to y, maybe we can work backwards from y and see if we can reach x. Because working backwards might limit the possibilities. Let's see.

What's the reverse operation? Suppose we have a number z that was obtained by an operation from some previous number w. So to get z, w's binary was modified by appending 0 or 1, then reversed. So to reverse this process, given z, we can reverse its binary to get the original binary after appending a bit. Then, that binary must end with 0 or 1 (since the original step was adding a 0 or 1). So the reversed binary (before appending) would be the binary of w plus the appended bit. Wait, maybe not. Let me think.

Original step: w is converted to binary, let's say B. Then, append a bit (0 or 1) to get Bb (b is 0 or 1). Then reverse this new binary string, which gives (Bb)^R. Then leading zeros are stripped. Then convert to decimal to get z.

So the original binary of w is B. The operation appends a bit b, making B followed by b, then reverses that. So z's binary is the reverse of Bb, without leading zeros.

So working backwards: if z can be transformed into some previous step, then its binary must be a prefix of some reversed string that ends with a 0 or 1. Wait, maybe not. Let me think differently.

Suppose we have z, and want to find possible predecessors. The predecessors would be numbers that, when you perform an operation on them, result in z. So the binary of the predecessor (say, w) would be such that when you append a 0 or 1, reverse, and strip leading zeros, you get z's binary.

Alternatively, for the reverse process: z's binary, when reversed, ends with either 0 or 1. Then, the predecessor would be the number formed by the reversed binary of z with that last bit removed. But we also have to account for leading zeros when reversed.

Wait, perhaps the reverse operation is as follows: To find a possible predecessor of z, take the binary of z, reverse it. Then, the result must end with either 0 or 1 (since during the original operation, we appended a 0 or 1). Then, the predecessor's binary is the reversed binary of z without the last bit. However, there might be cases where after reversing, the binary starts with 1 (since leading zeros are stripped in the original operation). Hmm, this is getting a bit confusing.

Let's take an example. Let's say during the forward operation, the original binary is B. We append a 0 to get B0. Reverse it, which is 0B reversed. Wait, no. The appending is to the right. So B is a binary string (without leading zeros). Then appending a 0 gives B followed by 0, so the binary is B0. Reversing this gives 0 followed by B reversed. Then leading zeros are stripped. So for example, if B is 100010 (34), appending 0 gives 1000100. Reversed is 0010001. Leading zeros are stripped to 10001 (17). So the result is 17.

In the reverse direction, if we have z =17, binary is 10001. To find possible predecessors, we reverse this binary to get 10001 reversed, which is 10001 (since it's a palindrome). Then, since during the original step, a 0 or 1 was appended, the reversed binary (after stripping leading zeros) would have a 0 or 1 as the last bit. Wait, no. The original reversed binary (before stripping leading zeros) would have been the B followed by the appended bit, reversed. So during the reverse process, the reversed binary of z (before stripping leading zeros) would have been the B followed by the bit, reversed. So when we reverse the binary of z (after stripping leading zeros), we get Bb, where b is the appended bit (0 or 1). Then, the predecessor would be the number formed by B.

Wait, perhaps the reverse process is: For a given z, the possible predecessors are the numbers obtained by taking the binary of z, reversing it, then adding a 0 or 1 at the end (but wait, no, the reverse process would involve removing the last bit). Let me think again.

Original operation: to go from w to z, you append a bit (0 or 1) to the binary of w, reverse the result, strip leading zeros. So the binary of z is the reversed (binary of w + b), stripped of leading zeros.

So to reverse the process, given z, the possible predecessors (w's) are the numbers obtained by taking the binary of z, prepending zeros (if needed) to get the reversed (binary w + b), then removing the last bit (b), reversing again to get the binary of w. But this seems complicated.

Alternatively, the binary of z is the reversed (binary w + b), without leading zeros. So to reverse, the reversed binary of z must start with the reversed (binary w + b). Wait, not sure. Let me see.

Let me represent the binary of w as B. Then, appending b gives Bb. Reversing this gives (Bb)^R. Then stripping leading zeros gives the binary of z. So the binary of z is equal to (Bb)^R with leading zeros removed. So (Bb)^R must be the binary of z with possible leading zeros added. For example, if z's binary is 10001, then (Bb)^R could be 0010001, which would have leading zeros stripped to get 10001. So when reversing, the binary of z could have leading zeros when reversed. So when working backwards, the binary of z could be extended with leading zeros (since when reversed, the leading zeros become trailing zeros, which are part of the original Bb).

So for the reverse process, given z's binary (let's call it S), we can consider all possible strings that are S with leading zeros added, then reversed, and then split into B and a bit. So for example, S is '10001' (z=17). To find predecessors, we can take any string T that is S with leading zeros added (like '0010001'), reverse it to get T_rev = '1000100'. Then, this T_rev is the Bb (binary of w followed by b). So B is '100010' (since the last bit is 0), and b was 0. So the predecessor w would be the number represented by '100010' (34). Alternatively, if we add leading zeros to S, say, make T = '00010001', then reverse to get '10001000', which ends with 0. So B is '1000100' (68), but then appending 0 would result in 68's binary plus 0, reversed, which would be 1000100 -> append 0: 10001000, reverse: 00010001 (stripped to 10001, which is 17). So in this case, the predecessor would be 68. But this would be a possible path. But wait, the original operation allowed appending a 0 or 1. So when reversing, the last bit of T_rev must be either 0 or 1, and that's the b. So when we split T_rev into B and b, B is T_rev without the last bit, and the last bit is b (0 or 1).

So the reverse process for a given z is to generate all possible T_rev by adding leading zeros to S (binary of z) and reversing, then check if T_rev ends with 0 or 1. Then, the possible predecessors are T_rev without the last bit (converted to decimal), but also considering that T_rev must have no leading zeros (since when reversed, the original Bb had no leading zeros, because B is the binary of w which has no leading zeros, and adding a bit to the end). Wait, not sure. Let's think again.

The original Bb is the binary of w followed by a 0 or 1. So B is a binary string with no leading zeros (since w is a positive integer). Then Bb is also a binary string with no leading zeros, but when reversed, the first bit (of Bb reversed) is the last bit of Bb. Which could be 0 or 1. So when reversed, leading zeros would be stripped. So the binary of z is (Bb reversed) with leading zeros stripped. So the binary of z is the reverse of Bb, but without leading zeros. So when we reverse the binary of z (after adding leading zeros if needed), we get Bb with leading zeros (since the original reversed Bb could have leading zeros which were stripped). So to find all possible Bb possibilities, we need to consider all possible ways to add leading zeros to the binary of z, reverse it, and then split into B and b (where b is 0 or 1).

For example, in the case of z=17 (binary 10001), the possible T (binary with leading zeros added) could be:

10001 (no leading zeros added), reversed is 10001, which ends with 1. Then B is 1000, b is 1. So the predecessor is 1000 in binary (8), and when we append 1, reverse, etc. But let's check: 8's binary is 1000. Append 1 gives 10001. Reverse gives 10001 (same as original, so leading zeros stripped would be 10001, which is 17. So yes, 8 is a predecessor of 17 via appending 1. So when z=17, possible predecessors are 8 and 34. Wait, let's see. For T_rev being 100010 (from earlier example), that would require adding leading zeros to z's binary. Wait, how?

Let me take another example. For z=17 (binary 10001), adding a leading zero makes T = 010001. Reverse it to get 100010. Split into B (10001) and b (0). So B is 10001 (17 in decimal). So the predecessor would be 17. Then appending 0 to B (17) gives 100010, reversed is 010001 which becomes 10001 (17 again). So that's a loop. Hmm.

Alternatively, the original approach is to generate all possible predecessors for a given z by considering all possible leading zeros added to the binary of z, then reversing, then checking if the last bit is 0 or 1, then taking the rest as the binary of the predecessor.

But this seems computationally intensive. However, for numbers up to 1e18, the binary representations are up to 60 bits. So the possible ways to add leading zeros are up to 60 bits. For example, the binary of z is S. When reversed, the length of S is len(S). Adding leading zeros to S would create a longer binary, but when reversed, the leading zeros become trailing zeros, but the actual Bb would have those trailing zeros. But when we split into B and b, the trailing zeros could be part of B. Wait, perhaps not. For example, if S is '10001' (len 5), adding two leading zeros would make it '0010001' (len 7). Reverse gives '1000100'. So Bb is '1000100', which ends with 0. So B is '100010' (34), and the predecessor is 34. Which aligns with the original example where 34 appending 0 gives 1000100, reversed to 0010001 (stripped to 10001, which is 17). So the predecessor is 34.

So in reverse process, given z=17, possible predecessors are 34 (when T is '0010001') and 8 (when T is '10001' reversed gives 10001, split into 1000 and 1).

So each step in reverse can generate up to two possible predecessors. But how many leading zeros can we add? Because each added leading zero when reversed becomes a trailing zero in Bb, but B must be a valid binary (without leading zeros). So for example, when we add leading zeros to S and reverse, the B part (after removing the last bit) must not have leading zeros. So B can't start with 0. So when we reverse S (with added leading zeros) and split into B and b, B must start with 1.

Wait, because B is the binary of w, which is a positive integer. So B cannot have leading zeros. So when we split T_rev into B and b (the last bit), B must start with 1.

Therefore, when working backwards, for each possible T (binary of z with some leading zeros added), we reverse it to get T_rev. Then, the last bit of T_rev is b (0 or 1). The remaining part (without the last bit) is B. But B must be a valid binary (starts with 1). So if after removing the last bit, the remaining part starts with 0, then this T is invalid.

So for the reverse process, the steps are:

1. For the current number z, generate all possible T strings by adding any number of leading zeros to the binary of z. For example, if z's binary is '101', possible T's are '101', '0101', '00101', etc., up to a certain maximum length (like 60 bits plus some).

2. For each T, reverse it to get T_rev.

3. Split T_rev into two parts: the first part is B (all except the last bit), the last bit is b (0 or 1).

4. Check if B is non-empty and starts with '1'. If so, then convert B to decimal, and that's a possible predecessor w.

5. Also, check if the original T_rev (before splitting) ends with 0 or 1. Because during the forward process, the appended bit was 0 or 1. So in the reverse process, the last bit (b) can be 0 or 1.

But wait, in the reverse process, the b can be 0 or 1, but in the forward process, the appended bit was 0 or 1. So in the reverse process, when we split T_rev into B and b, the b must be either 0 or 1. Which it is, since T_rev is a binary string (with leading zeros) that ends with either 0 or 1. So for each T_rev, the last bit is either 0 or 1. So for each T, we can split T_rev into B and b. But B must start with 1. So the key is that B must start with 1.

So the reverse process for a given z is to generate all possible T's (binary of z with leading zeros added), reverse them, split into B and b, check if B starts with 1, and collect those B's as possible predecessors. Each such B is a possible predecessor.

Additionally, there's another possibility: when z is obtained by appending a bit and then reversing. But what about the case where the original Bb after reversing is exactly equal to the binary of z, i.e., no leading zeros were stripped. For example, if Bb reversed has no leading zeros, then that's the case handled by adding no leading zeros.

So the approach would be: for each possible number of leading zeros (0 up to some maximum) added to the binary of z, generate T, reverse it to get T_rev, split into B and b, check if B is a valid binary (starts with 1), and collect the predecessors.

But how many leading zeros can we add? Let's see. The maximum possible length of the binary of z is 60 bits. Adding leading zeros can make the binary up to 60 + k bits. But when reversed, the T_rev would have those leading zeros as trailing zeros, but when split into B and b, B can be up to len(T_rev) -1 bits. But B must be a valid binary (starts with 1), which requires that the first bit of B is 1. So the T_rev, after splitting, the B part (which is the first len(T_rev)-1 bits) must start with 1.

So for each possible T (binary of z with leading zeros added), reversed and split into B and b, we need to check if B starts with 1. So for example, T is '0010001' (binary of z=17 with two leading zeros). Reversed is '1000100'. Split into B=100010 (binary of 34) and b=0. So B starts with 1, so this is a valid predecessor.

Another example: T is '00010001'. Reversed is '10001000'. Split into B=1000100 (binary 68) and b=0. B starts with 1, so 68 is a predecessor.

But how many leading zeros can we add? Let's think. The maximum possible T_rev would be when we add leading zeros such that the T's length is up to 60 bits (since the maximum possible binary of y is 60 bits). Wait, but when working backwards, the predecessor's binary can be up to 60 bits as well. So adding leading zeros to T (binary of z) may allow us to generate longer B's. However, the maximum length of T_rev is 60 + k, where k is the number of leading zeros added. But if we add too many leading zeros, then T_rev would start with a lot of zeros, which when reversed, become trailing zeros. For example, adding a lot of leading zeros to T would make T_rev a longer string. However, when split into B and b, B must start with 1. So even if T_rev starts with zeros, when split into B (the first len(T_rev)-1 bits) and b, the B must start with 1.

But if T_rev starts with a 0, then the first bit of B (the first len(T_rev)-1 bits of T_rev) would start with 0. Which is invalid, so such cases are rejected.

Therefore, for each possible T (binary of z with leading zeros added), we can generate T_rev and check if the first bit of B (the first len(T_rev)-1 bits) is 1. If yes, then that B is a predecessor.

But how many leading zeros can we add? Let's consider that T_rev's length is len(T_rev) = len(T) = len(z_bin) + k (k is the number of leading zeros added). For example, if the binary of z is of length m, then adding k leading zeros makes T of length m + k. Reversed, T_rev is of length m +k. Split into B (m +k -1 bits) and b (1 bit). For B to start with 1, the first bit of B (the first bit of T_rev) must be 1. So the first bit of T_rev must be 1.

But T_rev is the reversed T, which is the binary of z with leading zeros added. So when T has leading zeros, the reversed T (T_rev) will end with those zeros. So for example, T is '0010001' (binary of z=17 with two leading zeros), reversed T_rev is '1000100'. The first bit of T_rev is 1, so the B part (the first 6 bits) is '100010', which starts with 1. So valid.

But if we add leading zeros such that T starts with '00010001', then T_rev is '10001000'. The first bit is 1, so B is '1000100' (binary of 68), which starts with 1. Valid.

But if we add leading zeros such that T starts with a lot of zeros, then T_rev ends with those zeros. So the first bit of T_rev is 1 (since the binary of z starts with 1, and adding leading zeros to T would not affect the leading 1 in the reversed T_rev). Wait, no. Wait, the binary of z is S, which starts with 1. Adding leading zeros to T (the binary of z with leading zeros added) would make T start with 0, but the reversed T_rev would start with the last bit of T. For example, if T is '00101', then T_rev is '10100'. The first bit is 1. So even if T starts with 0, the reversed T_rev starts with the last bit of T, which is the original binary of z's last bit. Wait, no. Let's see: z's binary is S. For example, S is '10001'. Adding leading zeros to T would make T '0010001'. Reversed is '1000100'. The first bit is 1.

So the reversed T_rev's first bit is the last bit of T, which is the last bit of S. Because T is S with leading zeros added. The reversed T_rev is the reverse of T, so the first bit of T_rev is the last bit of T. Since S is the binary of z, which is a positive integer, so S starts with 1 and ends with some bit (could be 0 or 1). So the reversed T_rev's first bit is the last bit of S.

But in the reverse process, when we split T_rev into B and b, B is the first len(T_rev)-1 bits. So B starts with the first bit of T_rev, which is the last bit of S. So for B to start with 1, the last bit of S must be 1. If the last bit of S is 0, then B would start with 0, which is invalid, so no predecessors can be found for such T's.

Wait, that's an important point. So the first bit of T_rev is the last bit of T. But T is S with leading zeros added. So the last bit of T is the last bit of S (since adding leading zeros doesn't change the end of the string). So the first bit of T_rev is the last bit of S. So for the first bit of B (which is the first bit of T_rev) to be 1, the last bit of S (the original z's binary) must be 1. Otherwise, all possible T_rev's first bits would be 0, making B invalid unless there's a scenario where the leading zeros added to T cause the reversed T_rev to have a leading 1. Wait, but no. Because adding leading zeros to T would make T start with 0, but the end of T is the same as the end of S. So the reversed T_rev starts with the end of T, which is the end of S. So if the original z's binary ends with 0, then all T_rev's first bit is 0, so B would start with 0, which is invalid. So in this case, there are no possible predecessors via this route. So if z's binary ends with 0, then in reverse process, the only possible predecessors would be those generated when the reversed T_rev's first bit is 1, which requires that the last bit of S (z's binary) is 1. So if z's binary ends with 0, then the only possible way to have a predecessor is if the last bit of S is 1, which it's not. Wait, this is getting complicated.

Let me rephrase. For B to start with 1, the first bit of T_rev must be 1. The first bit of T_rev is the last bit of T. T is the binary of z with leading zeros added, so the last bit of T is the last bit of z's binary. Therefore, the first bit of T_rev is the last bit of z's binary.

So, for the reverse process to generate any valid predecessors, the last bit of z's binary must be 1. Because otherwise, the first bit of T_rev is 0, so B starts with 0, which is invalid.

Wait, this is a critical observation. So if the binary of z ends with 0, then when you add leading zeros to form T, the last bit of T is still 0. So reversed T_rev starts with 0, so B (the first len(T_rev)-1 bits) starts with 0, which is invalid. So in this case, no predecessors can be found via this method. However, this is not the case. For example, let's take z=8 (binary 1000). The last bit is 0. So according to this reasoning, there are no predecessors. But according to the sample input 3, 2 cannot become 8, but what about other cases?

Wait, in the sample input 3, x=2 and y=8. The answer is NO. Let's see. 2 in binary is 10. The possible operations are append 0 (100 reversed is 001 → 1), append 1 (101 reversed is 101 → 5). So after one operation, 2 can become 1 or 5. Then from 1, append 0 → 10 reversed is 01 → 1, append 1 → 11 reversed is 11 → 3. From 5 (101), append 0 → 1010 → reversed is 0101 → 5, append 1 → 1011 reversed is 1101 → 13. So 8 is not reachable from 2.

But the reverse process would have z=8 (binary 1000). The last bit is 0, so all possible T's when reversed would start with 0, making B invalid. So no predecessors. So when z's binary ends with 0, the reverse process cannot find any predecessors.

But wait, what about the case where z was generated by appending 0, but the reversed binary after stripping leading zeros ends with 0. Hmm. For example, consider the original process where w=3 (binary 11). Append 0 to get 110. Reverse to get 011 → stripped to 11 (3). So z=3 here. So the binary of z is 11. Ends with 1. So in reverse process, predecessors are possible.

Another example: suppose z=17 (binary 10001) which ends with 1. Then predecessors can be found, as we saw.

But if z's binary ends with 0, then reverse process can't find any predecessors. So this implies that if z's binary ends with 0, then the only way to reach z is through appending 0 in the forward process, but then the reversed binary (after appending) would end with 0. But how?

Wait, no. Let me think. Suppose we have a case where the original appending was a 0, and the reversed binary (after appending) had leading zeros stripped. For example:

Original w is 34, binary 100010. Append 0 → 1000100. Reverse is 0010001 → stripped to 10001 (17). So z=17's binary ends with 1. So in the reverse process, we can find predecessors.

But if the appending was 0, and the reversed binary after stripping has last bit 0. How?

For example, suppose w=4 (binary 100). Append 0 → 1000. Reverse is 0001 → stripped to 1. So z=1. Binary of z is 1, ends with 1. So predecessors can be found.

Another example: w=5 (101). Append 0 → 1010. Reverse is 0101 → stripped to 101 → 5. So z=5 ends with 1. So in reverse process, we can find predecessors.

But wait, the case where z's binary ends with 0 would require that during the forward process, the reversed Bb (after appending) has a leading zero. For example:

Suppose w= 6 (binary 110). Append 0 → 1100 → reversed is 0011 → stripped to 11 (3). So z=3's binary is 11 (ends with 1).

Another example: w= 9 (1001). Append 0 → 10010 → reversed is 01001 → stripped to 1001 (9). So z=9's binary ends with 1. So in this case, appending 0 and reversing brings you back to 9.

So it's possible to have a cycle. But in any case, the reverse process only allows predecessors if the binary of z ends with 1.

So, the key insight is: when working backwards, z can only have predecessors if its binary ends with 1 or if it's possible to generate the current z via some other path.

Wait, but what if the binary of z ends with 0? Then according to our earlier reasoning, no predecessors can be found. So the only way to reach z is if z is the original x. So in this case, if x is equal to y (z=y), then it's possible. Otherwise, if y's binary ends with 0, and x != y, then it's impossible.

But wait, the original x can be equal to y, in which case the answer is YES. So when y is equal to x, regardless of binary, the answer is YES.

So in the reverse approach, the algorithm would proceed as follows:

- Start from y. If y is x, return YES.

- Otherwise, generate all possible predecessors of y by reversing the process. Then check if any of these predecessors is equal to x. If not, proceed to generate predecessors of these predecessors, and so on, until we either find x or exhaust all possibilities.

But since the numbers can be up to 1e18, and each step can generate multiple predecessors, the BFS could still be feasible if the number of possible predecessors per step is limited.

But how many predecessors can a number have? For example, for a number z with binary ending with 1, the number of predecessors depends on the possible ways to add leading zeros to z's binary and reverse.

But each possible T (binary of z with leading zeros) can generate a predecessor if after reversing and splitting, B starts with 1.

But adding leading zeros to the binary of z can create many possible T's, which when reversed and split, may generate different B's.

But how many leading zeros can we add? For example, if the binary of z is S of length m, adding up to 60 leading zeros would create T of length up to 60 + m. But since 60 is manageable, perhaps we can process all possible T's with leading zeros up to a certain length.

Alternatively, since the maximum possible length of a binary number is 60 bits (for 1e18), adding leading zeros would create T's of varying lengths, but when reversed, the T_rev's would have trailing zeros. However, the first bit of T_rev is the last bit of S (the original binary of z). So for T_rev's first bit to be 1 (so that B starts with 1), the last bit of S must be 1.

So, if the binary of z ends with 0, then no predecessors can be found. So for such a z, we can't have any predecessors, so if y is such a number and not equal to x, the answer is NO.

So the reverse process can only generate predecessors if the binary of z ends with 1.

So the steps for the reverse process are:

1. If y == x: return YES.

2. Otherwise, check if the binary of y ends with 1. If not, then return NO (unless x can be transformed into y in zero steps, which is already checked).

3. For each possible T (binary of y with leading zeros added), generate T_rev. Split into B and b. Check if B is non-empty and starts with 1. Then convert B to decimal and collect all possible predecessors.

4. For each collected predecessor, check if it's equal to x. If yes, return YES. Otherwise, add these predecessors to a queue and repeat the process.

But the problem is that even with this approach, there could be a lot of possibilities. So we need to find a way to efficiently generate all possible predecessors for a given z.

But how many possible predecessors can there be for a given z? Let's think. For example, the binary of z is S (ends with 1). Then, the possible predecessors are generated by adding leading zeros to S, reversing, splitting into B and b (b is 0 or 1? Wait, no. Because the original appending step added 0 or 1. So during reverse, the last bit of T_rev (which is the b) can be 0 or 1. But in this case, since T_rev is the reversed T, which is the binary of z with leading zeros added. So T_rev's last bit is the first bit of T. Since T is the binary of z with leading zeros added, the first bit of T is 0 (since leading zeros are added). So the last bit of T_rev is 0. So b is 0. Wait, that's a problem.

Wait, let's take an example. Suppose z's binary is S = '101' (ends with 1). We add leading zeros to create T = '00101'. Reversed T_rev is '10100'. So T_rev's last bit is 0. So when we split T_rev into B (1010) and b (0), then B is 1010 (binary 10). So the predecessor is 10. Then, when we append 0 to 10 (binary 1010), reverse to get 0101 (stripped to 101, which is 5). So this works.

But in this case, the b is 0, which is the last bit of T_rev (which is 0). So for all T's in the reverse process (binary of z with leading zeros added), T_rev's last bit is the first bit of T, which is 0 (since T has leading zeros added). So during the reverse process, all generated predecessors will have a b of 0. But wait, in the forward process, the appended bit can be 0 or 1. So during the reverse process, the possible predecessors must have a b (appended bit) of 0 or 1. But according to this example, the b is always 0. So there's a contradiction.

This suggests that the reverse process can't capture all possible predecessors. So there's a mistake in the reasoning.

Wait, let's go back. The original appending can be either 0 or 1. So during the forward process, for a given w, we can generate two possible z's: one by appending 0 and another by appending 1, then reversing and stripping leading zeros.

So in the reverse process, for a given z, there are two possible ways to get to it: either the last bit appended was 0 or 1. But how can we distinguish between them?

Ah! The mistake is in the earlier reasoning. The T_rev is the binary of w followed by the appended bit. So during the reverse process, the possible predecessors are not limited to appending 0. Because in the forward process, the appended bit could be 0 or 1. So in the reverse process, for a given z, there are two possible appended bits (0 and 1) that could have been used. Wait, but how does that affect the reverse process?

Wait, no. For the forward process, each step appends either 0 or 1 to the binary of w, then reverses it and strips leading zeros. So during the reverse process, to find the predecessors of z, we need to consider both possibilities: that the appended bit was 0 or 1.

But according to our earlier approach, the appended bit is determined by the last bit of T_rev. But when we add leading zeros to T (binary of z), T_rev can have various forms, and the last bit of T_rev is the first bit of T (which is 0 if we added leading zeros). So in the reverse process, the possible appended bits (0 or 1) are not directly considered. Instead, the appended bit is determined by the last bit of T_rev, which depends on the leading zeros added.

But this suggests that the reverse process may not capture all possible predecessors, but only those that were generated via appending 0. But wait, no. Because the appended bit in the forward process can be 0 or 1, and during the reverse process, we need to consider all possible T's (binary of z with leading zeros added) and generate all possible B's that could have been appended with either 0 or 1. So the reverse process must consider all possible ways to append 0 or 1 during the forward step.

But how to model that in reverse. Maybe the correct approach is to consider that during the forward step, appending 0 or 1 gives two possible Bb's. In reverse, we need to consider both possibilities.

Alternatively, perhaps the reverse process must generate two possibilities for each possible T: one where the appended bit was 0, and one where it was 1. But I'm not sure.

Alternatively, the appended bit in the forward process is the last bit of Bb. When reversed, that becomes the first bit of T_rev. So during the reverse process, the appended bit is the first bit of T_rev. But no, that's not correct. Let's think:

Forward process: B is binary of w. Append b (0 or 1) → Bb. Reverse → (Bb)^R. Strip leading zeros → z's binary.

Reverse process: z's binary is S. We prepend leading zeros to S to get T, reverse T to get (Bb)^R. Then Bb is (T_rev). So B is the first len(T_rev) -1 bits, and b is the last bit. So the appended bit in the forward step is b.

So during the reverse process, the appended bit is the last bit of T_rev. So when we generate possible predecessors, the appended bit can be 0 or 1, but it's determined by the T_rev's last bit. So during the reverse process, to find all possible predecessors, we must consider all possible T's (binary of z with leading zeros added), and for each T_rev, the appended bit is the last bit of T_rev. But during the forward process, the appended bit was either 0 or 1. So during the reverse process, the T_rev's last bit must be 0 or 1. But the T_rev is the reverse of T, which is the binary of z with leading zeros added. So the last bit of T_rev is the first bit of T, which is 0 if leading zeros were added. So the appended bit in the forward process is 0 for all predecessors generated this way. But that can't be right.

This suggests that there's a flaw in the reverse approach. Because the appended bit in the forward step can be 0 or 1, but in the reverse process, the appended bit is determined by the first bit of T (which is 0 if leading zeros are added). So the reverse approach only captures the cases where the appended bit was 0. But what about cases where the appended bit was 1?

Ah! This is a critical mistake. Because in the forward process, when we append a 1 and reverse, the resulting binary may have leading zeros stripped. So during the reverse process, when we add leading zeros to the binary of z, we are effectively considering all possible Bb that, when reversed and stripped of leading zeros, would result in z. So the appended bit can be 1, but during the reverse process, adding leading zeros to z's binary allows us to recover the Bb that was reversed and stripped.

But how?

Let's take an example. Suppose during the forward process, appending 1 to B (binary of w) gives B1. Reversed, this is 1B^R. Leading zeros may be present if B ends with zeros. For example, B is 1000 (w=8). Append 1 → 10001. Reverse → 10001 (same as original), which is 17. So the binary of z is 10001. During reverse process, z's binary is 10001. Adding leading zeros to T gives possible T's like '10001', '010001', '0010001', etc. Reversed T_rev is '10001', '100010', '1000100'. For each of these, split into B and b.

For T_rev '10001' (from T='10001'), split into B=1000 and b=1. So B is 8, and the appended bit was 1. So this is a valid predecessor.

For T_rev '100010' (from T='010001'), split into B=10001 (17) and b=0. So this would have been appending 0.

So during the reverse process, when we add leading zeros to T (binary of z), the appended bit (b) is the last bit of T_rev, which can be 0 or 1. But how?

Wait, T is the binary of z with leading zeros added. So T starts with 0's followed by the binary of z. Reversing T gives T_rev which ends with the leading zeros added. For example, T is '0010001' (binary of z=17 with two leading zeros). Reversed is '1000100'. The last bit is 0, so b is 0. B is '100010' (34). So the predecessor is 34, which was the case in the original example.

Another example: T is '10001' (no leading zeros added). Reversed is '10001'. Split into B=1000, b=1. So predecessor is 8, which was the case when appending 1 to B=8 (binary 1000 → 10001 → reversed 10001 → 17).

So during the reverse process, the appended bit (b) can be 0 or 1, depending on the T chosen. But how do we capture both possibilities?

Ah! Because during the reverse process, adding leading zeros to T allows us to generate various T_rev's, which may end with 0 or 1. For example, if the original appended bit was 1, then during the reverse process, the T that is the binary of z with no leading zeros added will generate a T_rev that ends with 1. But if the appended bit was 0, then we need to add leading zeros to T so that the T_rev ends with 0.

So during the reverse process, by adding leading zeros to T (binary of z), we can generate all possible T_rev's that could have been the Bb in the forward process. This includes cases where the appended bit was 0 or 1.

Thus, the reverse process naturally captures all possible appended bits (0 or 1) by varying the number of leading zeros added to T. For example, when we add no leading zeros, the appended bit is the last bit of T_rev, which is the last bit of z's binary. If that last bit is 1, then it corresponds to an appended bit of 1. Adding leading zeros allows us to generate T_rev's that end with 0, corresponding to appended bit 0.

So, the reverse process can capture all possible predecessors, regardless of whether the appended bit was 0 or 1, by considering all possible T's (binary of z with varying numbers of leading zeros added).

But how to generate all possible T's that could lead to valid B's (predecessors).

The algorithm for the reverse approach would be:

1. Start with y. If y == x, return YES.

2. If y's binary ends with 0, then it can't have any predecessors (except if y is x). So return NO.

3. Otherwise, generate all possible predecessors by adding leading zeros to y's binary, reversing, splitting into B and b, and collecting B's that are valid (start with 1).

4. For each predecessor, check if it's equal to x. If yes, return YES.

5. If not, add these predecessors to a queue and continue the BFS.

But the problem is that adding leading zeros to T can generate an infinite number of possibilities, but in practice, since B must be a positive integer, the length of B can't be longer than 60 bits. So for each possible T, the length of T_rev is len(T) = len(z_bin) + k, where k is the number of leading zeros added. When reversed, T_rev has length len(z_bin) +k. Splitting into B (len(z_bin) +k -1 bits) and b (1 bit). B must be a positive integer, so its binary must start with 1 and be at least 1. So the maximum possible len(B) is 60 bits. Therefore, the maximum possible len(T_rev) is 61 bits (since B is up to 60 bits, and b is 1 bit). So len(T_rev) = len(B) +1 <=61. So len(T) = len(T_rev) = len(B)+1 <=61. Since len(T) is len(z_bin) +k, and len(z_bin) can be up to 60 bits, k can be up to 61 - len(z_bin). For example, if z_bin is 5 bits, then k can be up to 56. But this is manageable.

So the approach is:

- For each possible number of leading zeros added to the binary of z (k from 0 to ... ), generate T.

- Reverse T to get T_rev.

- Split into B and b. Check if B is valid (starts with 1).

- If valid, convert B to a decimal number and add to the predecessors.

But how many leading zeros can be added? Since T_rev must have length len(z_bin) +k, and B is len(T_rev) -1 bits. B must be a positive integer, so len(B) can be up to 60 bits. So len(T_rev) can be up to 61 bits. Therefore, len(T) = len(z_bin) +k <=61. So k can be up to 61 - len(z_bin).

For example, if z_bin is 5 bits, k can be up to 56. So for each z, we need to generate all T's where the total length of T is up to 61 bits. This would involve adding leading zeros from 0 up to 61 - len(z_bin) times.

But this can be a lot, but manageable since 61 is a small number.

So the steps are:

- For the current number in the BFS (starting with y), generate all possible predecessors by:

   a. Generate the binary of the current number.

   b. Check if the binary ends with 0. If yes, no predecessors. Continue.

   c. Otherwise, generate all possible T's by adding leading zeros to the binary (up to 61 - len(binary) times).

   d. For each T, reverse it to get T_rev.

   e. Split T_rev into B_part (all but last bit) and b.

   f. Check if B_part starts with 1. If yes, convert B_part to decimal to get predecessor.

   g. Collect all unique predecessors.

- Check if any of the predecessors is x. If yes, return YES.

- Otherwise, add the predecessors to the BFS queue, and repeat.

But how to manage this in code, especially handling leading zeros?

Another thing to note is that adding leading zeros to the binary of z may create T's of varying lengths, but the reversed T_rev will have trailing zeros. For example, adding leading zeros to T increases the length, which when reversed, adds trailing zeros to T_rev. These trailing zeros correspond to the leading zeros added to T.

So for each possible T (binary of z with leading zeros added), the steps are:

- T is a binary string consisting of leading zeros followed by the binary of z.

- T_rev is the reverse of T.

- Split T_rev into B_part (all except last bit) and last bit (b).

- If B_part starts with '1', then convert B_part to decimal as a possible predecessor.

But since leading zeros in B_part are allowed only if they are part of the binary string (but the binary of B_part must start with 1). Wait, B_part is the binary of the predecessor w. So B_part must be a valid binary number, which means it cannot have leading zeros. So when we split T_rev into B_part and b, B_part must not have leading zeros.

Wait, no. B_part is the binary of w. So it must not have leading zeros. So when we split T_rev into B_part and b, B_part must be a binary string that starts with 1. So during the reverse process, for each T, after reversing to get T_rev, we check if the first part (B_part) starts with 1. If yes, then it's a valid predecessor.

So the code steps would be:

For a given current number (z):

1. If z == x: return YES.

2. Convert z to binary string S.

3. If the last character of S is '0': no predecessors, return False.

4. Else:

   a. Generate all possible T strings by adding leading zeros to S. The number of leading zeros can be from 0 up to (61 - len(S)).

   b. For each T in these possibilities:

      i. Reverse T to get T_rev.

      ii. Split T_rev into B_part (all characters except last) and last_bit.

      iii. Check if B_part starts with '1' and is not empty.

      iv. If so, convert B_part to decimal number (w).

      v. Add w to the predecessors set.

5. For each w in predecessors:

   a. If w has not been visited before, add to the queue.

So the code will perform a BFS, but with a visited set to avoid cycles.

But how to generate all possible T strings with leading zeros added, up to a certain length?

In code:

For example, S is the binary of z. The possible T's are all strings of the form '0'*k + S, where k is 0, 1, 2, ... up to max_k = 61 - len(S).

So len(T) = len(S) +k. But len(T) can't exceed 61 bits.

So for each k in 0 to (61 - len(S)), generate T as '0'*k + S.

But this could be a lot of T's. For example, if S is 1 bit (like binary '1'), then k can be up to 60, leading to 61 different T's. For each T, we reverse it, split, check, and possibly add to predecessors.

But 61 possibilities per step is manageable.

So the BFS approach would proceed as follows:

- Use a queue to process numbers in BFS order.

- Use a visited set to avoid reprocessing the same number.

- For each number dequeued:

   a. If it's x, return YES.

   b. Generate all possible predecessors.

   c. For each predecessor, if not in visited, add to queue and visited.

- If queue is empty, return NO.

But what about the maximum possible steps? Since each step appends a bit, the maximum possible steps is 60 (since numbers up to 1e18 have 60 bits). So the BFS depth is limited to 60 steps. And in each step, the number of possibilities is up to 60 * 2 (but in practice, much less). So the total number of nodes processed is manageable.

So this approach should be feasible.

Now, let's code this.

First, we need to convert numbers to binary, add leading zeros, reverse, split, check validity, etc.

Edge Cases:

- x == y: return YES.

- y's binary ends with 0 and x != y: return NO.

- y's binary ends with 1: generate predecessors and check.

Also, during BFS, we need to track visited numbers to avoid cycles. For example, if a number appears again in the BFS, we can skip it.

So the code outline is:

Read x and y.

If x == y: print YES.

Else:

   Check if y == 0: but since y >=1, no.

   Convert y to binary. If ends with 0: print NO.

   Else:

      BFS queue starts with y.

      visited = {y}

      while queue not empty:

         current = queue.pop()

         generate all possible predecessors of current.

         for each predecessor w:

             if w == x: return YES.

             if w not in visited and w <= 1e18 (since numbers can't exceed 1e18 in steps):

                 add to queue and visited.

      If loop ends, return NO.

Now, let's implement this.

But how to generate all possible predecessors for a given current number.

Implementing the steps:

For current z:

   bin_z = bin(z)[2:]

   if bin_z[-1] == '0': continue (no predecessors)

   else:

      len_z = len(bin_z)

      max_k = 61 - len_z

      for k in 0 to max_k:

          T = '0' *k + bin_z

          T_rev = T[::-1]

          if len(T_rev) <1: continue (unlikely)

          B_part = T_rev[:-1]

          if not B_part: continue (B_part is empty)

          if B_part[0] != '1': continue

          # convert B_part to decimal.

          w = int(B_part, 2)

          # add to predecessors.

So this code snippet would generate all possible predecessors for current z.

But how to handle the case where B_part is empty? For example, if T_rev is of length 1, then B_part is empty. Which is invalid.

Thus, the code skips such cases.

Now, let's test this with the sample input.

Sample Input 4:

34 69 → output YES.

Let's see.

x =34, y=69.

Check if 34 ==69: no.

Check y's binary: 69 is 1000101. Ends with 1.

Generate predecessors of 69.

For each possible k (0 to 61 - 7=54):

T is '0'*k + '1000101'.

For example, k=0: T is '1000101', reversed is '1010001'.

B_part is '101000', which is 40. So predecessor is 40.

k=1: T is '01000101', reversed is '10100010'. B_part is '1010001' (81). So predecessor is 81.

k=2: T is '001000101', reversed is '101000100'. B_part is '10100010' (162). So predecessor is 162.

But wait, the sample input says that 34 can become 69 via two steps: 34→81→69.

Let's see.

In the BFS:

Start with y=69. Check if 69 ==34: no.

Generate predecessors.

For k=0: T is '1000101' (69's binary). T_rev is '1010001'. B_part is '101000' (40). So 40 is a predecessor.

But does 40's binary end with 0: yes. So 40 can't have predecessors.

But how do we get to 81?

Ah, let's see. For k=1, T is '01000101', which reversed is '10100010'. B_part is '1010001' → 81.

So 81 is a predecessor of 69. So in the BFS, we add 81 to the queue.

Then, when processing 81:

Check if 81 is 34: no.

Generate predecessors of 81.

81's binary is 1010001, ends with 1.

Generate T for k=0: T=1010001 → reversed is 1000101. B_part is 100010 → 34. So predecessor is 34.

So when processing 81, 34 is found, return YES.

Thus, the code would find this path.

Thus, the BFS approach works.

Now, code implementation.

But there's a possible optimization: since numbers can be up to 1e18, but during the BFS, each step reduces the number of bits by at least 1 (when appending 0 or 1 and reversing), but I'm not sure. But in any case, the BFS is manageable.

Now, code:

Read x and y.

If x == y: print YES.

Else:

   Check if y's binary ends with 0: if so, NO.

   Else:

      Initialize queue with y.

      visited = {y}

      while queue not empty:

         current = queue.pop(0)

         generate predecessors:

         bin_current = bin(current)[2:]

         if bin_current[-1] != '1': continue.

         len_current = len(bin_current)

         max_k = 61 - len_current

         predecessors = set()

         for k in range(0, max_k +1):

             T = '0'*k + bin_current

             T_rev = T[::-1]

             if len(T_rev) < 1:

                 continue

             B_part = T_rev[:-1]

             if not B_part:

                 continue

             if B_part[0] != '1':

                 continue

             w = int(B_part, 2)

             if w > 1e18:

                 continue

             if w == x:

                 print("YES")

                 exit()

             if w not in visited and w <= 1e18:

                 predecessors.add(w)

         for w in predecessors:

             if w == x:

                 print("YES")

                 exit()

             if w not in visited:

                 visited.add(w)

                 queue.append(w)

      print("NO")

But in Python, the queue is implemented as a list. Using pop(0) is O(n), which can be slow for large queues. To optimize, use deque from collections.

Thus, the code should use deque and popleft().

Also, in the code, when generating predecessors, for each possible k, we generate T and check.

Now, let's code this.

The code would look like this:

Testing against sample input 4.

```python
import sys
from collections import deque


def main(input_stream, output_stream):
    x, y = map(int, input_stream.readline().split())

    if x == y:
        print("YES", file=output_stream)
        sys.exit()

    def has_ending_one(num):
        return bin(num)[-1] == '1'

    if not has_ending_one(y):
        print("NO", file=output_stream)
        sys.exit()

    visited = set()
    q = deque()
    q.append(y)
    visited.add(y)

    found = False

    while q:
        current = q.popleft()
        if current == x:
            print("YES", file=output_stream)
            found = True
            break
        bin_current = bin(current)[2:]
        if bin_current[-1] != '1':
            continue
        len_bin = len(bin_current)
        max_k = 61 - len_bin
        for k in range(max_k + 1):
            T = '0' * k + bin_current
            T_rev = T[::-1]
            if len(T_rev) < 1:
                continue
            B_part = T_rev[:-1]
            if not B_part:
                continue
            if B_part[0] != '1':
                continue
            w = int(B_part, 2)
            if w == x:
                print("YES", file=output_stream)
                found = True
                q.clear()
                break
            if w <= 10**18 and w not in visited:
                visited.add(w)
                q.append(w)
        if found:
            break

    if not found:
        print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
8935891487501725 71487131900013807
""",
            "output": \
"""\
YES
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

Another test case: input 3, where x=2 and y=8.

y=8's binary is 1000. Ends with 0. So the code returns NO.

Another test case: input 2, x=7, y=4.

y=4's binary is 100. Ends with 0. So code returns NO.

The code should handle all cases correctly.

So this should be the solution.
</think>

```python
import sys
from collections import deque

def main():
    x, y = map(int, sys.stdin.readline().split())

    if x == y:
        print("YES")
        return

    # Check if y's binary ends with 0
    if (y & 1) == 0:
        print("NO")
        return

    visited = set()
    q = deque()
    q.append(y)
    visited.add(y)

    found = False

    while q:
        current = q.popleft()
        # Generate all possible predecessors
        bin_current = bin(current)[2:]
        max_k = 61 - len(bin_current)
        for k in range(max_k + 1):
            T = '0' * k + bin_current
            T_rev = T[::-1]
            if len(T_rev) < 2:
                continue  # Need at least one bit for B_part and one for b
            B_part = T_rev[:-1]
            if not B_part or B_part[0] != '1':
                continue
            w = int(B_part, 2)
            if w == x:
                print("YES")
                return
            if w <= 10**18 and w not in visited:
                visited.add(w)
                q.append(w)

    print("NO")

if __name__ == "__main__":
    main()
```
