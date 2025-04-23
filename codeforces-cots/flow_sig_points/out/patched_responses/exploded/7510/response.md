<think>
Okay, let's see. We need to determine if one binary string can be transformed into another using those operations. Hmm. What's the operation exactly? Oh right, any two adjacent characters, replace them with x XOR y and x OR y (but the order isn't specified, because we can choose which one to replace with p and which with q). Wait, wait. Wait, the operation is: pick two adjacent characters, x and y. Then compute p = x XOR y, q = x OR y. Then replace one of them with p and the other with q. So the order here matters. For example, if the two are 1 and 1, then p is 0, q is 1. So replacing them as 0 and 1 would give 01, or as 1 and 0 would give 10. But the problem says that in one operation, you can do either. So for the example where a is 11, you can turn it into 01 or 10.

But how do these operations affect the overall properties of the string? Let's think about invariants. Maybe there's some property that remains the same no matter what operations you perform, and if a and b don't share that property, then it's impossible. Otherwise, maybe they can be transformed.

First, let's think about the sum of the bits. Because each operation takes two bits and replaces them with two other bits. Let's see what the sum of the two bits after the operation is. Let x and y be the original bits. Then p = x XOR y, q = x OR y. The sum of p and q is (x XOR y) + (x OR y). Let's compute this for all possible x and y.

Case 1: x=0, y=0. Then p=0, q=0. Sum is 0+0=0. Original sum was 0. So sum remains the same.

Case 2: x=0, y=1. p=1, q=1. Sum is 2. Original sum was 1. So sum increases by 1.

Case 3: x=1, y=0. Same as case 2. Sum increases by 1.

Case 4: x=1, y=1. p=0, q=1. Sum is 1. Original sum was 2. So sum decreases by 1.

Hmm, so the sum can increase, decrease, or stay the same. So the sum isn't an invariant. So that's probably not useful.

Wait, but maybe there's a different invariant. Let's think about the total number of 1's modulo something. Or perhaps the multiset of bits. Alternatively, maybe the parity of the sum of all bits is an invariant. Let's check.

Wait, let's see. Let's take two adjacent bits and replace them with p and q. The original sum of all bits is S. The new sum is S - x - y + p + q. Let's compute p + q for each possible x and y.

p = x^y, q = x | y.

x^y is (x + y) mod 2. x|y is 1 if at least one is 1. So:

For x=0, y=0: p=0, q=0. Sum p+q is 0.

Original x + y is 0. So the change is 0 - 0 = 0. So S remains same.

For x=0, y=1: p=1, q=1. Sum p+q is 2. Original x + y is 1. So change is +1. So S increases by 1.

For x=1, y=0: same as above. Sum p+q is 2, original is 1. Change +1.

For x=1, y=1: p=0, q=1. Sum p+q is 1. Original x + y is 2. So change is -1. So S decreases by 1.

So each operation can change the sum by -1, 0, or +1. So the sum can vary. So the sum itself isn't an invariant. So maybe the parity of the sum is also not an invariant. For example, if sum is even, after a change of +1, it becomes odd. So parity can change.

Hmm. So that's not helpful.

Another approach: what happens when you perform operations on the string. Let's see if there's a way to model the possible transformations. For example, maybe the order of operations can lead to certain configurations, but perhaps some properties of the string as a whole are preserved.

Alternatively, maybe we can model the problem as being able to permute the bits in any order, but with certain constraints. For example, maybe after some operations, the bits can be rearranged, but the total number of 1's must meet some condition.

Wait, but in the first example, a is "11" (sum 2) and b is "10" (sum 1). So sum can decrease. But the answer is YES. So sum can change. So sum isn't fixed.

What's the key here? Let's think differently. Let's see if there's a way to compute some invariant. For example, the multiset of bits, but perhaps in some way.

Wait, let's think about the total number of 1's. Let's see if there's any invariant related to that. Let's consider how the operation affects the total number of 1's.

Suppose we have two bits x and y. Their sum is x + y. After replacing them with p and q (x^y and x|y), the sum is (x^y) + (x|y). Let's compute this:

x^y is (x + y) mod 2, and x|y is (x + y) when x and y are 0 or 1. Wait, no. For x=1, y=1, x|y is 1. So x|y is 1 if at least one is 1.

So for x and y, their sum can be 0, 1, or 2. Let's compute p + q for each case.

Case 1: x + y = 0 (both 0): p=0, q=0. Sum 0. So sum remains 0.

Case 2: x + y = 1 (one is 0, the other 1): p=1, q=1. Sum 2. So sum increases by 1.

Case 3: x + y = 2 (both 1): p=0, q=1. Sum 1. So sum decreases by 1.

So each operation can change the total sum by +1, -1, or leave it the same. Therefore, the sum can vary. But perhaps the sum has some parity property.

Wait, but when you perform an operation, how does it affect the sum's parity?

Original sum is S. After operation, sum becomes S - (x+y) + (p+q). Let's compute (p+q) - (x+y):

Case 1: x=0, y=0: (0+0) - (0+0) = 0. So parity remains same.

Case 2: x=0, y=1: (1+1) - (0+1) = 2 -1 = 1. So parity changes.

Case 3: x=1, y=0: same as case 2. Parity changes.

Case 4: x=1, y=1: (0+1) - (2) = -1. So parity changes (since -1 is odd, so adding it to S changes parity).

So in cases 2, 3, 4, the operation changes the parity of the sum. But wait, in case 1, the parity remains the same. Wait, but in case 2 and 3, the sum increases by 1 (from 1 to 2: sum changes from odd to even). So for those cases, the parity flips. In case 4, sum changes from 2 (even) to 1 (odd). So parity flips.

So in all cases except case 1 (which leaves sum the same, so parity same), the parity flips. Wait, no. Let's see:

Original sum S is the sum of all bits. Let's say when we perform an operation, the sum changes by delta, which is (p+q) - (x+y). For parity, it's the delta mod 2 that matters.

So delta mod 2 in each case:

Case 1: delta is 0. So parity remains same.

Case 2 and 3: delta is 1 mod 2 (since delta is 1). So parity flips.

Case4: delta is -1 mod 2, which is 1. So parity flips.

So each operation either keeps the parity the same (if delta is even) or flips it (if delta is odd). Wait, but in case 1, delta is 0 mod 2, so parity remains. In other cases, delta is 1 mod 2, so parity flips.

So when you perform an operation, the parity of the total sum can either stay the same or flip, depending on which two bits you choose.

Hmm, this complicates things. Because the parity can change in some operations. So the sum's parity isn't fixed. So this doesn't give us an invariant.

Alternative approach: perhaps the multiset of bits can be manipulated in a way that the sum of the bits can be adjusted, but with certain constraints.

Wait, but the problem allows multiple operations. Let's think about the possible transformations. Let's consider the following: perhaps the order of operations can allow us to arrange the bits in any order, provided that the sum of the bits is possible.

Wait, for example, in the first sample input:

a is "11" (sum 2), b is "10" (sum 1). So sum decreases by 1. That's possible. But how?

But in another example, if a is "1" and b is "01", then the answer is NO. Because the original string has length 1, and the target has length 2. So the operation can't change the length. Wait, wait! Oh right, the operation replaces two adjacent characters with two new characters. So the length of the string remains the same. So the first thing to check is if the lengths of a and b are the same. If not, then it's impossible. Wait, no! Wait, the problem says "the strings can have different lengths". So wait, the operation is applied to the string a, which can have any length. But how can the length change? Let me re-read the problem.

Wait, the problem statement says: "In one operation the mayor may take any two adjacent characters of a string... Then he replaces one of the two taken characters by p and the other one by q." So each operation is performed on two adjacent characters, replacing each with a new value. So the length of the string remains the same. Therefore, if a and b have different lengths, the answer is automatically NO. But in the input examples, the second example has a of length 1 and b of length 2, so output is NO.

Wait, but the problem statement says: "the strings can have different lengths." So for example, if a is length 2, can it become length 3? No, because each operation leaves the length the same. So the lengths of a and b must be equal. Otherwise, it's impossible.

So the first check should be: if the lengths of a and b are different, output NO.

But wait, let's check the second example. Input is a = "1", b = "01". The output is NO. Because the lengths are different (1 vs 2). So that's correct.

So the first step in solving the problem is to check if the lengths of a and b are equal. If not, return NO.

So that's the first condition. If that's not met, output is NO.

So the first thing to do in the code is check len(a) == len(b). If not, output NO.

Now, assuming len(a) == len(b), what's next?

Then we need to check whether a can be transformed into b via any number of operations.

But how? Let's think about possible invariants.

Wait, when you perform the operation on two adjacent bits, you can generate two new bits. But perhaps there's a way to model the possible transformations. Let's think about the possible pairs (p, q) that can be formed from (x, y).

For example, for x and y:

Case 1: 00 → p=0, q=0. So the pair becomes 00. No change.

Case 2: 01 → p=1, q=1. So possible pairs are 11 (order depends on which is replaced first). Wait, but the operation allows replacing one with p and the other with q. So for x=0 and y=1, we can replace x with p (1) and y with q (1), making 11. Or replace x with q (1) and y with p (1), same result. So the pair becomes 11.

Case 3: 10 → same as case 2, resulting in 11.

Case 4: 11 → p=0, q=1. So possible pairs are 0 and 1 (order can be 01 or 10).

So for each possible pair of adjacent bits, the operation can change them into certain other pairs.

But how do these operations affect the entire string? It's unclear. Let's think of the problem in terms of the entire string's properties.

Wait, perhaps the key is to realize that the sum of all bits modulo 3 is an invariant. Wait, that's a random thought, but perhaps not. Let's see. For example, when the operation is performed, the sum can change by -1, 0, +1. So modulo 3, the sum can change by -1, 0, +1. But that doesn't seem to form an invariant. So perhaps not.

Alternatively, perhaps the multiset of bits can be transformed in certain ways. For example, if the sum is S, can we reach any sum S' such that S' ≡ S mod something? Or perhaps the sum can be adjusted as long as certain conditions are met.

Alternatively, maybe the key is that the number of 1's can be increased or decreased in certain ways. Let's consider that:

Suppose the sum of the bits in a is S_a, and in b is S_b.

We need to determine whether it's possible to reach S_b from S_a by a series of steps where each step can add or subtract 1, or leave it the same. But since each operation can change the sum by +1, -1, or 0 (but no, wait: the operation can change the sum by +1, -1, or 0). Wait, no. For example, the sum after the operation is S + delta, where delta is (p+q) - (x + y). As we saw earlier, delta can be 0, +1, or -1.

But wait, no: for x=0 and y=0, delta is 0. For x=0 and y=1, delta is 2 -1 = +1. For x=1 and y=1, delta is 1 - 2 = -1.

So the sum can be increased by 1, decreased by 1, or stay the same.

But how do these operations affect the possible sum transitions?

For example, if S_a is 2, can we reach S_b = 1? Yes, as in the first example. So that's possible.

If S_a is 1, can we reach S_b = 0? Let's see. For example, suppose a is "10". Let's say we perform the operation on the two bits (1 and 0). Then they become 1 and 1. So sum increases by 1 to 2. Then if we perform the operation again on those two 1's, sum decreases by 1 to 1. So maybe it's possible to go back and forth. Hmm.

But perhaps the sum is not the only consideration. Let's think about another example.

Example 3:

Input:
a = 000 (sum 0)
b = 101 (sum 2)

The output is NO.

So even though the sum can be increased (from 0 to 2 is possible via two operations that add +1 each), but in this case it's impossible. So there must be another condition.

So sum is not the only factor. There's something else that determines the possibility.

Hmm. Let's look for another invariant.

Another idea: the parity of the number of 1's in the entire string. Wait, but that's the same as the sum's parity, which we saw can change.

Alternatively, perhaps the maximum number of 1's that can be achieved. For example, perhaps once you reach a certain sum, you can't go beyond that. Or maybe the sum can be adjusted up or down as needed, but with certain constraints.

Alternatively, perhaps the key is that the sum of the bits can be adjusted, but the parity of the sum of the bits is preserved modulo something. Wait, perhaps when the sum is zero, it's impossible to reach any other sum. But the first case shows that sum 2 can be reduced to 1.

Another approach: think about the problem as a graph where each node is a possible string of length n. Edges are the possible operations. But for n up to 1e6, this is impossible to model directly.

But perhaps for the problem, there's a pattern that can be checked quickly. Let's think of some small cases.

Case 1: n = 1. Then the string is a single bit. There are no two adjacent characters, so no operations can be performed. So a must equal b. So if a is 1 and b is 1: YES. Else, NO.

Case 2: n = 2. Let's see possible transformations.

For example, starting with 11. As per the first example, after one operation, it can become 10 or 01. Then, applying another operation to the two adjacent bits (which are 1 and 0 in the case of 10), we can turn them into 1^0=1 and 1|0=1. So 11 again. Or perhaps other possibilities.

Wait, if the string is 10, the operation can be applied to the two bits (1 and 0). The p and q are 1 and 1, so the new string is 11. So the sum can go back up.

So for n=2, the sum can vary between 1 and 2, depending on the operations.

Hmm.

But how do these operations affect the bits? For example, if the sum is 1 (e.g., 10), you can perform an operation to make sum 2 (11). Then, you can perform an operation again to get sum 1 (01 or 10). So sum can toggle between 1 and 2.

So for a string of length 2, the sum can be any number between 0 and 2, but wait:

Wait, starting from 00 (sum 0), the operation leaves it as 00. So sum can't change. So for n=2, if the initial sum is 0, you can't change it. If the initial sum is 1, you can reach 2. If initial sum is 2, you can reach 1.

So in that case, the possible sum transitions for n=2:

- sum 0 → sum 0 (only possible if initial sum is 0)
- sum 1 → sum 2, then back to 1, etc.
- sum 2 → sum 1, then back to 2, etc.

So for n=2, the possible sum of the target depends on the initial sum.

But in the first example, the initial sum is 2, and target sum is 1. So possible.

But what about for a string of length 3?

Let's take a string of 000. Sum is 0. Since all pairs are 00, each operation leaves them as 00. So sum remains 0. So target must have sum 0.

But in example 3, a is 000 (sum 0), and b is 101 (sum 2). So output is NO. Which makes sense because the sum can't be increased from 0.

But wait, why? Because the initial sum is 0, and each operation can't increase it. Because in a string of 000, any two adjacent bits are 00. Performing the operation on them gives 00 again. So sum remains 0.

So for n ≥2, if the initial sum is 0, then the sum can never change. Because any two adjacent bits are 0, and applying the operation leaves them as 0 and 0. So sum remains 0.

So that's a key insight: if the initial sum is 0, then the sum cannot change. So the target's sum must also be 0. Otherwise, it's impossible.

Similarly, if the initial sum is 0 and the target sum is 0, but the target has different bits (like 000 → 000 is possible), but maybe even the bits can be rearranged. Wait, but in this case, all operations leave the bits as 0. So the string can't change. So for sum 0, the string must remain the same. Because any two adjacent bits are 00, which after operation remain 00. So the entire string is immutable if it's all 0s.

So for example, if a is 000 and b is 000, then YES. But if a is 000 and b is 0000, then NO (different lengths). Or if b is 001, then NO (sum is 1, which can't be achieved from sum 0).

So the key points so far:

1. If len(a) != len(b) → NO.

2. If the length is 1 → a must equal b.

3. For length ≥2:

   a. If the sum of a is 0 → the entire string must be all 0s. So b must also be all 0s. Otherwise, NO.

   b. Else, can we reach any sum that is possible via the operations, provided that sum is possible? But how?

Wait, but when the initial sum is not zero, what can happen? For example, for a string of 11 (sum 2), the sum can be reduced to 1. For a string of 10 (sum 1), sum can be increased to 2.

So when the initial sum is non-zero, perhaps the sum can be adjusted up or down, but perhaps there's a parity or other condition.

Wait, perhaps when the sum is non-zero, the target's sum must have the same parity as the initial sum, but this doesn't hold. For example, initial sum 2 (even) can be transformed into sum 1 (odd). So parity changes. So parity isn't a fixed invariant.

Hmm. So what else could be the invariant?

Another idea: the multiset of bits can be transformed into any permutation if the sum is non-zero. Wait, but that's not possible. For example, in the first example, 11 can become 10. But can it become 01? Yes, by applying the same operation on the two bits again.

Wait, but when you have 11, after one operation you can get 10 or 01. Then, if you have 10, applying the operation again gives 11. So you can toggle between them. So the order of the bits can be changed.

Wait, perhaps the bits can be reordered in any way as long as the sum is allowed.

So for example, if a is 10 (sum 1), and the target is 01 (sum 1), then it's possible. Because after one operation, 10 becomes 11. Then, another operation on the two 1's gives 01. So the order can be changed.

Alternatively, perhaps the bits can be permuted freely as long as the sum is non-zero and the length is ≥2.

But how? Let's see. For example, can we turn 10 into 01? Yes. So the order can be swapped. So perhaps any permutation is possible.

But how to permute the bits when there are more than two elements. For example, can we swap the first and third bits in a three-element string?

Hmm. Let's consider a three-element string, say 100. The sum is 1.

We can perform operations on the first two bits (1 and 0) → replace them with 1 and 1. Now the string is 110. Then, perform an operation on the second and third bits (1 and 0) → replace with 1 and 1. Now the string is 111. Sum is 3.

Then, perform an operation on the first two bits (1 and 1) → replace with 0 and 1. So string becomes 011. Then, perform an operation on the first and second bits (0 and 1) → 1 and 1. So string becomes 111 again. Hmm, this might not help.

Alternatively, maybe there's a way to permute the bits by shifting them through adjacent swaps. But how?

Alternatively, perhaps the order of the bits doesn't matter. As long as the sum is correct, and the sum is non-zero, and the length is ≥2, then any permutation is possible. So the multiset of bits can be arranged in any order, and thus the target must have the same multiset of bits (sum) and same length.

But this isn't the case. For example, the first example: a is 11 (sum 2), target is 10 (sum 1). The sum changes, but the answer is YES. So the sum can change. So that's not the case.

So the sum can change, as long as the operations allow.

Wait, but how can the sum change? For example, in the first example, the sum decreases by 1. So the sum can be adjusted by using the operations.

So perhaps the key is that as long as the sum of the initial and target is possible given the operations, and the sum of the initial is non-zero, then it's possible.

But how to model the possible sum transitions.

Alternatively, maybe when the sum of the initial is non-zero, then it's possible to reach any sum. But this isn't the case. For example, if the initial sum is 1 and the target sum is 3 for a string of length 3. Let's see:

If the initial string is 100, sum 1. Can we reach sum 3?

Yes. Apply operation on 1 and 0 → 11. String becomes 110. Sum is 2. Then apply operation on 1 and 0 → 11. Sum is 3. So yes.

So sum can increase.

But what if the initial sum is 1 and target sum is 0? Well, that's possible only if the initial sum can be reduced to 0. But how?

But for sum 1, can we reach sum 0? Let's see.

For a string of length 2. Initial sum 1: 10.

Applying the operation turns it into 11 (sum 2). Then applying the operation again on the two 1's gives sum 1. So sum can't get to zero. So for a string of length 2, initial sum 1 can't reach sum 0.

So that's a case where the sum cannot reach zero. So the sum cannot be zero if the initial sum is non-zero and the length is 2.

So how to model this?

Hmm. Maybe the sum can be any value as long as it is possible to reach via the allowed operations, but this depends on the length of the string.

Alternatively, perhaps the following conditions are necessary and sufficient:

1. len(a) == len(b).

2. If len(a) == 1 → a == b.

3. Else:

   a. If sum of a is zero → sum of b must be zero and all bits are zero.

   b. Else:

      i. sum of b must be at least 1.

      ii. sum of a and sum of b must have the same parity, or some other condition.

Wait, but in the first example, sum a is 2, sum b is 1. They have different parity. So that's a problem.

Hmm. So that can't be.

Another idea: when the sum is non-zero, the sum of the target can be any number, as long as it's possible to reach via the operations. But how?

Let me think: for a string of length n >= 2 and sum > 0:

- Each operation can either increase, decrease, or leave the sum the same.

But perhaps the sum can be adjusted to any possible value, provided that the sum of the target is at least 1 and (sum_a - sum_b) is even or odd. But I'm not sure.

Alternatively, when the sum of a is non-zero, the sum of b can be any number >=1. But that's not true. For example, in the case of n=2 and sum_a=1, sum_b can't be 0.

So what is the possible range for sum_b given sum_a and n?

Hmm. Let's think of sum_b as follows:

If sum_a is zero → sum_b must be zero.

Else:

sum_b must be >=1.

Additionally, for n=2 and sum_a=2 (all 1's), sum_b can be 1.

But for n=2 and sum_a=1, sum_b can be 1 or 2.

So sum_b can vary.

But what's the general rule?

Perhaps when the sum of a is non-zero, the sum of b can be any value between 1 and the maximum possible sum for that length. But that's not helpful.

Alternatively, perhaps the sum of b can be any value as long as sum_b >= 1. Because, with sum_a >= 1, you can increase or decrease the sum through operations.

But how?

Wait, for example, consider a string of length 3 with sum 1. Can you reach sum 3? Yes, as shown earlier. Can you reach sum 0? No, because sum 0 would require all bits to be zero. Which is impossible if sum_a was non-zero (since sum_a is 1, and sum 0 would require sum_a to be zero).

Wait, no. Because sum 0 would mean all bits are zero, and that requires sum_a to be zero. So for sum_b to be zero, sum_a must be zero.

So the key conditions are:

- If len(a) != len(b) → NO.

- If len is 1 → a must equal b.

- Else:

   - If sum_a == 0 → sum_b must be 0 and all bits in b must be zero.

   - Else:

      - sum_b must be at least 1.

      - And, the multiset of bits in a can be transformed into b through some operations.

But how to check the last condition?

Another observation: the operations allow us to generate new 1's. For example, if you have 0 and 1, you can turn them into two 1's. So the sum can increase.

But perhaps when the sum of a is non-zero, the multiset of bits in b can have any number of 1's as long as there is at least one.

But that's not correct. For example, in the third example:

a is 000 (sum 0), so b must be 000. But in the example, b is 101 (sum 2), which is not allowed, hence the answer is NO.

But in other cases, when sum_a is non-zero, perhaps the multiset of bits can be transformed into any other multiset of bits with sum >=1.

But how to verify this?

Wait, let's think about a string of length 3 with sum 2 and target sum 3. Is that possible?

Original sum is 2, target is 3. So we need to increase sum by 1. For example, take two 1's in the original string. Replacing them with 0 and 1. Sum becomes 2-2 + 1 = 1. Then take the remaining 1 and one of the 0's (if any). Wait, maybe this is getting complicated.

Alternatively, perhaps the key is that when sum_a is non-zero, then the answer is YES if and only if sum_b is also non-zero. Because you can manipulate the sum to reach any non-zero value.

But in the first example, sum_a is 2 (non-zero) and sum_b is 1 (non-zero). So allowed.

In the case of a being 10 (sum 1), and b being 01 (sum 1), which is allowed.

In the case of a being 10 (sum 1), and b being 00 (sum 0), which is not allowed. So sum_b must be non-zero.

But what about the sum being even or odd? For example, if sum_a is 2 (even), can sum_b be 1 (odd)? Yes. So the parity doesn't matter.

So the only conditions are:

- len(a) == len(b).

- If len is 1, then a == b.

- If len >= 2:

   - sum_a is zero → sum_b is zero, and all bits in b are zero.

   - sum_a is non-zero → sum_b must be non-zero, and all bits in b can be arranged via some operations.

But how do we check whether the multiset of bits in b can be arranged via the operations.

Wait, but the operations allow us to swap adjacent bits. For example, in the first example, 11 can be transformed into 10 or 01. So the order can be changed.

But can the order of the bits be rearranged arbitrarily? For example, can we turn 100 into 001 or 010, etc.?

If so, then the multiset of bits (count of 1's and 0's) would determine the answer. So as long as sum_b is non-zero, and the sum of a is non-zero, and the length is the same, then the answer is YES.

But that can't be true. For example, take a string of 111 (sum 3) and target string of 000 (sum 0). But sum is non-zero, so answer would be NO. But sum of target is zero, which is invalid. So that's covered by the condition.

Another example: a is 100 (sum 1), target is 011 (sum 2). So sum is non-zero, and target sum is also non-zero. According to this hypothesis, the answer would be YES. But can we actually reach that?

Let's see. a is 100.

First, perform operation on the first two bits (1 and 0) → 1 and 1. So string becomes 110. Sum is 2.

Then, perform operation on the second and third bits (1 and 0) → 1 and 1. So string is 111. Sum is 3.

Now, perform operation on the first two bits (1 and 1) → 0 and 1. So string is 011. Sum is 2. That's the target. So yes, it's possible.

So sum can increase and decrease. So as long as the sum of a is non-zero, and sum of b is non-zero, and the lengths are the same, then it's possible.

But wait, what about a = 11 (sum 2), b = 10 (sum 1). That's allowed. So the sum can decrease.

But another example: a is 11 (sum 2), b is 00 (sum 0). sum_b is zero, so answer is NO.

So the conditions are:

If len(a) != len(b) → NO.

Else if len(a) == 1 → a == b.

Else if sum(a) == 0:

   if sum(b) == 0 and all characters in b are 0 → YES.

Else → NO.

Else:

   if sum(b) != 0 → YES.

   else → NO.

So this would mean that for len(a) == len(b) >= 2, and sum(a) > 0, sum(b) > 0 → YES.

But what about cases where sum(a) is non-zero but sum(b) is non-zero, but the multiset can't be formed? Like a has even number of 1's and b has odd number. But the first example shows that it's possible. So sum parity doesn't matter.

So the code would be:

Check if len(a) == len(b). If not, output NO.

If len is 1, then a == b.

Else:

sum_a = number of '1's in a.

sum_b = number of '1's in b.

If sum_a == 0:

   if sum_b == 0 and b is all '0's → YES.

   else → NO.

Else:

   if sum_b == 0 → NO.

   else → YES.

Wait, but in this case, sum_b can be any non-zero value. For example, a sum_a=2, sum_b=1 → YES.

But according to this logic, any sum_b >=1 is allowed. So for example:

a is 11 (sum 2), b is 10 (sum 1) → sum_b is 1 ≥1 → YES.

Another example: a is 11, b is 00 → sum_b is 0 → NO.

But what about the third example in the problem:

a is 000 (sum 0), b is 101 (sum 2). So sum_a is 0, sum_b is 2. So len is same (3). So output is NO.

Which matches the sample.

Another example: a is 100, b is 011. sum_a is 1, sum_b is 2. So output is YES.

But according to the code logic, since sum_a is non-zero and sum_b is non-zero, output YES.

Which is correct.

But what about a case where sum_b is non-zero but it's impossible to reach? For example, a is 10 (sum 1), len 2. Can we reach a sum_b of 2?

Yes. Apply operation on 1 and 0 → 11. sum is 2.

So yes.

What about a sum_a of 1 and sum_b of 3 for len 3. For example, a is 100, sum 1. Target is 111, sum 3. Can we reach that?

Yes. Apply operations as follows: 100 → 110 (sum 2) → 111 (sum 3).

So yes.

So the code logic would work.

But wait, what about the case where a is 11 (sum 2), and b is 01 (sum 1). The code would output YES, which is correct.

So the code's approach is:

- Check lengths.

- If len is 1, compare the strings.

- Else, check sum_a. If it's zero, then b must be all zeros.

- Else, sum_b must be non-zero.

So, the code can be written as follows.

Now, to implement this.

But also, when sum_a is zero and len >=2, then b must have all zeros. Because the initial string is all zeros and any operation leaves it unchanged.

So in code:

Read a and b.

if len(a) != len(b):

    print("NO")

else:

    if len(a) == 1:

        if a == b:

            print("YES")

        else:

            print("NO")

    else:

        sum_a = a.count('1')

        sum_b = b.count('1')

        if sum_a == 0:

            if sum_b == 0 and b == '0' * len(b):

                print("YES")

            else:

                print("NO")

        else:

            if sum_b >= 1:

                print("YES")

            else:

                print("NO")

Wait, but sum_b >=1 is equivalent to sum_b !=0. Because sum_b can't be negative.

But what about when sum_a is non-zero and sum_b is non-zero, but the target is not possible for some other reason? For example, a is 11 (sum 2), len 2. Target is 00 (sum 0). Then output is NO. Which is correct.

Another example: a is 11 (sum 2), len 2. Target is 10 (sum 1). Output is YES.

But according to the code, sum_b is 1 >=1 → YES.

So the code works for this case.

Another example: a is 10 (sum 1), len 2. Target is 00 (sum 0) → NO.

But sum_b is 0 → code outputs NO.

So the code seems to handle all cases.

But what about the following case:

a is 10 (sum 1), len 2. Target is 11 (sum 2). Then code outputs YES.

Which is correct, as the operation can be applied to the two bits to turn into 11.

So the code seems to handle all the cases correctly.

So this is the solution.

Now, let's test it against the examples.

Example 1:

Input:

11

10

len is 2.

sum_a = 2. sum_b =1.

sum_a is non-zero, sum_b >=1 → YES.

Output: YES. Correct.

Example 2:

Input:

1

01

len is 1 vs 2 → NO. Output: NO. Correct.

Example 3:

Input:

000

101

len is 3. sum_a is 0. So check sum_b is 0 and all chars in b are 0. sum_b is 2 → NO. Output: NO. Correct.

Another example: a is 000, b is 000 → YES.

a is 000, b is 000 → sum_a is 0. sum_b is 0. So YES.

Another example: a is 00, b is 00 → YES.

a is 0, b is 0 → YES.

a is 0, b is 1 → len 1, output NO.

So the code should handle all these cases.

Thus, the code is correct.
</think>

```python
a = input().strip()
b = input().strip()

if len(a) != len(b):
    print("NO")
else:
    n = len(a)
    if n == 1:
        print("YES" if a == b else "NO")
    else:
        sum_a = a.count('1')
        sum_b = b.count('1')
        if sum_a == 0:
            if sum_b == 0 and b == '0' * n:
                print("YES")
            else:
                print("NO")
        else:
            print("YES" if sum_b != 0 else "NO")
```