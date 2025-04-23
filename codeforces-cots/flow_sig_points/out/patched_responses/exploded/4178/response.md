<think>
Okay, let's tackle this problem. Hmm. The task is to find k integers such that the sum of 2^each equals n. And we need the largest number in the sequence to be as small as possible. Then, among those sequences with the minimal maximum, we need the lex largest one. Oh right, lex order means that when comparing two sequences, the first differing element should be as large as possible. So, for example, [3,3,2,1,0] is lex larger than [3,3,2,0,1] because at the fourth position, 1 is larger than 0.

First, let's think about how to approach the problem. The key constraints are n up to 1e18 and k up to 1e5. So the solution needs to be efficient, O(k) time probably.

The problem requires two main steps: checking if it's possible to form such a sequence, and then constructing the lex largest sequence with the minimal possible maximum.

Let me start by considering the binary representation of n. Because each term in the sum is 2^a_i, the sum is essentially the sum of these exponents. But the exponents can be positive, zero, or even negative. However, negative exponents complicate things because they add fractions. For example, 2^-1 is 0.5, so adding two of them gives 1. Which is how the third sample works: two -1's sum to 1.

So the first challenge is to model the sum correctly. Let's think: n can be written as the sum of k terms of the form 2^a_i. We need to find such a_i's that the maximum a_i is minimized, and the lex largest possible.

Wait, but how do we handle negative exponents? Because if we have a lot of small exponents (like -1), their sum can contribute to the total. But for the minimal maximum, perhaps the optimal approach is to use the largest possible exponents first, then break down larger exponents into smaller ones where needed.

Wait, the maximum a_i in the sequence is y. So the minimal possible y is the smallest possible maximum such that the sum of 2^a_i (k terms) equals n.

Let's think of the problem in terms of the binary representation. For example, if all terms were non-negative, then the sum would be the sum of k powers of two. But when exponents can be negative, it's possible to split higher exponents into lower ones.

Wait, perhaps the initial approach is to find the minimal possible y, then construct the sequence with that y, ensuring that the lex order is maximized.

So, how to find the minimal possible y?

Let's think of the problem as starting from the highest possible bits. Let's first represent n in binary. Then, for each exponent a_i, 2^a_i contributes to the sum.

But how to split into exactly k terms. Let's think of the process of breaking down exponents. For example, each time you split a term 2^a into two terms of 2^(a-1). This increases the count of terms by 1. So, if you have a total of m terms, you can split them into m + (split_count) terms.

But to reach exactly k terms, perhaps we need to find a way to split the initial binary representation into k terms, possibly splitting larger exponents into smaller ones, and possibly adding negative exponents.

Alternatively, perhaps the minimal possible maximum exponent y is determined by the highest exponent in the binary representation of n plus some splits. Hmm. Let's think about this.

Suppose the binary representation of n has the highest bit at position h. Then, if we can split some of the higher bits into lower bits to get exactly k terms. Wait, but splitting a higher bit into lower bits increases the count of terms. For example, 2^h becomes 2^(h-1) * 2. So splitting once gives 2 terms. So splitting a 2^h term into s terms of 2^(h-s) would require s splits. Not sure.

Alternatively, the minimal possible maximum y is such that the sum of 2^y terms multiplied by their count plus lower terms equals n, but this might not directly apply when exponents are negative.

Wait, perhaps we need to model this as a problem where we can split exponents into multiple terms, but each split reduces the exponent by 1 and doubles the count. For example, 2^a can be split into two 2^(a-1) terms. So splitting once increases the count by 1.

So the initial number of terms is the number of set bits in the binary representation of n when all exponents are non-negative. Then, each split increases the count by 1. So the minimal possible maximum exponent is the highest exponent in the binary representation, and each split allows us to increase the count.

But how to determine if it's possible to split into exactly k terms, given that the initial count is the number of set bits, and each split increases the count by 1.

Wait, let's denote the initial count of set bits as m. Then, each split increases m by 1. So to reach k, we need m + s = k, where s is the number of splits. But s must be non-negative. So if k < m, it's impossible. Wait, but no. Because if you split a higher bit into lower bits, but you can split multiple times. For example, splitting one term multiple times. Like, splitting a 2^h term once gives two 2^(h-1) terms. Splitting one of those again gives three terms (two 2^(h-2)), etc. Each split increases the count by 1.

So the maximum possible number of splits is unbounded. Wait, but if you split a term into s splits, how does that affect the count?

Each split increases the count by 1. So, if the initial count is m, and each split adds 1, then the minimal possible maximum exponent is the highest exponent in the binary representation. So the minimal maximum y is at least the highest exponent of n's binary. However, when you split higher exponents into lower ones, the maximum exponent may decrease. Wait, no. Because if you split a 2^h into two 2^(h-1), the maximum exponent becomes h-1, which is lower than h.

Wait, this is a key insight. So splitting higher exponents can reduce the maximum exponent. So perhaps the minimal possible maximum y is determined by how much we can split the higher exponents into lower ones, thereby reducing the maximum exponent and increasing the count of terms.

So the problem now is to find the minimal possible y such that the sum can be represented with k terms, each of which is ≤ y, and the sum of their 2^exponents equals n.

Wait, but how?

Alternatively, perhaps the process of splitting can be used to determine the minimal y. Let's consider the following approach:

1. Start by representing n as the sum of set bits in binary. For example, if n is 23 (10111), the initial terms are 16 (4), 4 (2), 2 (1), 1 (0). So m=4 terms, exponents 4, 2, 1, 0. Max exponent is 4. But we need 5 terms. So we need to split once. The minimal maximum would then be 3. Because splitting 16 (2^4) into two 8's (2^3) gives a total of 5 terms. The exponents would be 3,3,2,1,0. Max exponent is 3. Which is the sample 1.

So, the approach is to split the highest possible exponents to create more terms, which allows the maximum exponent to decrease.

So the steps could be:

- Find the minimal possible y such that the sum of 2^a_i (k terms, each a_i ≤ y) equals n.

But how?

Alternatively, let's model the problem as follows. The sum of k terms, each ≤ y, such that each term is 2^a_i, and the sum is n. We need to find the minimal y possible.

Once y is determined, we need to arrange the terms in lex order, which requires the largest possible sequence in lex order (so the earliest elements as large as possible).

So, first, the problem is to find the minimal possible y.

To find y, perhaps binary search can be used. Let's think:

We can perform a binary search on possible y values. For a given y, can we create k terms of 2^a_i (a_i ≤ y) that sum to n?

If we can find the minimal y where this is possible, then proceed.

But how to check for a given y, is it possible?

Wait, but the sum of k terms of 2^a_i where each a_i is ≤ y. So the minimal sum is k * 2^(-infty), but that's not helpful. Wait, but if all a_i are as small as possible (like very negative), the sum can be very small. So the idea is that for a given y, the sum must be n. But how to model this?

Alternatively, let's consider that each term is at most 2^y. So the sum of the terms is sum_{i=1 to k} 2^{a_i} = n. Each 2^a_i ≤ 2^y. So the sum is at least k * 2^{-infty} (but that's zero) and at most k*2^y.

But n must be in this range. But how to model this.

Alternatively, think of the problem as trying to split the sum n into k parts, each part is a power of two, and each is ≤ 2^y. So, the sum of these parts is n.

But how?

Alternatively, for a given y, the maximum per term is 2^y. So, the minimal sum when all terms are as small as possible (like 2^-infinite) is not bounded. So perhaps the binary search approach is not feasible.

Alternatively, perhaps the minimal possible y is determined by the following steps:

The maximum possible exponent in the initial binary representation is h. Then, each split of a term with exponent e into two terms of exponent e-1 increases the count by 1. But each split can only be done on terms of exponent higher than the current minimal y.

Wait, perhaps the process is to start with the initial binary representation (count m = number of set bits). Then, to reach k terms, we can split some terms. Each split of a term into two terms of lower exponent increases the count by 1.

But each split can be done on any term with exponent higher than some y. So, if we need to reach k terms, the number of splits needed is s = k - m. If s is negative, impossible. So first, if m > k: impossible. Because you can't decrease the number of terms. Because each split increases the count.

Wait, no. Wait, initial count is m. Each split increases the count by 1. So after s splits, the total count is m + s. So to reach k, we need m + s = k → s = k - m. So if k < m, then s is negative → impossible. So that's a case where the answer is "No". For example, in sample 3, n=1 (binary 1, m=1), k=2. So m=1, k=2 → possible. But sample 2 is n=13 (binary 1101, m=3), k=2. So m=3 >k=2 → impossible. So sample 2's output is "No".

So first check: if k < m → impossible.

But wait, maybe there's a way to split higher exponents and then combine. Hmm, no. Because each split increases the count. So, initial m is the minimal possible count. So if k < m, it's impossible.

So first condition: if k < m → output No.

Otherwise, we can proceed.

Now, the problem reduces to splitting (k - m) times, which each split increases the count by 1. But each split must be done on a term with exponent higher than some y, leading to the minimal possible maximum.

The goal is to split in a way that the maximum exponent is minimized.

So, for example, in sample 1: n=23 (binary 10111 → 16+4+2+1 → exponents 4,2,1,0 → m=4). k=5. So we need 1 split. The best way is to split the largest exponent (4) into two 3s. So now the exponents are 3,3,2,1,0 → max is 3.

Another example: if we need more splits, perhaps splitting the same term multiple times.

So, the strategy is to split the largest possible exponents first, to reduce the maximum exponent as early as possible.

So the approach is:

1. Find the initial count m (number of set bits). If k < m → output No.

2. Else, compute the required splits s = k - m.

3. Now, perform s splits by splitting the largest exponents possible. Each split takes a term of exponent e, splits it into two terms of e-1. This increases the count by 1.

But how to model this? We need to track the exponents and split them in a way that after all splits, the maximum exponent is as small as possible.

The key is to split the largest exponents first. Because splitting a larger exponent reduces the maximum exponent.

So, for example, if we have exponents [4, 2, 1, 0], and need to split once: split 4 into two 3s. Now max is 3.

If we need to split again (s=2), split one of the 3s into two 2s. Now the exponents are [3,2,2,2,1,0]. Max is 3 again. Wait, no. Wait, splitting a 3 into two 2s would give two 2s, so after splitting once, the max is 3 (if another split is done on a 3). So perhaps, after splitting a 4 into two 3s, then splitting a 3 into two 2s, the max would be 3 again (since another 3 is present). So the max decreases only when all higher exponents are split.

Hmm, this suggests that splitting higher exponents first is the way to minimize the maximum.

So, the approach is to maintain a priority queue (max-heap) of the exponents. For each split, we take the largest exponent, split it into two (e-1) terms, and add them back into the heap. We do this s times. Then, the maximum exponent in the heap is the minimal possible.

Wait, but this would require s steps, each taking O(log m) time. But when s can be up to 1e5 (since k can be up to 1e5 and m up to 60 for n=1e18), this is feasible.

But how to model this?

Alternatively, since we need to split s times, and each split reduces the exponent of one term by 1 and increases the count by 1, the minimal maximum after all splits is the initial maximum exponent minus the number of splits we can apply to that exponent.

Wait, perhaps not. For example, if the initial max exponent is h. Each split of a term with exponent h gives two terms of h-1, which contribute to the count. If we split h as much as possible, then the maximum exponent is h - t, where t is the number of splits applied to h.

But other terms may have exponents higher than h-t. So maybe not.

Alternatively, let's model the exponents as a frequency map, counting how many times each exponent occurs. Then, for splitting, the highest exponent is processed first. Each split of a term in exponent e requires that the count of e is reduced by 1, and the count of e-1 is increased by 2. Each split uses one split (s decreases by 1). We need to do this s times.

The maximum exponent after all splits is the largest exponent in the frequency map.

So, the steps are:

1. Compute the binary representation of n. For each exponent e where 2^e is part of the sum (i.e., the set bits), note their counts. Initially, each exponent has count 1.

2. If the initial count m = sum of counts exceeds k → no.

3. Else, compute s = k - m.

4. For each split, select the largest possible exponent e in the current frequency map. Split one occurrence of e into two of e-1. This reduces the count of e by 1, increases count of e-1 by 2, and increases the total count by 1. s decreases by 1. Repeat until s=0.

5. After all splits, the frequency map will have exponents, and the largest exponent is the minimal possible maximum y.

Once we have this frequency map, we need to arrange the exponents in lex order. Lex order requires that the sequence is as lex largest as possible. Which means that in the sequence, the elements are non-increasing, but in the earliest positions, the largest possible exponents are placed.

Wait, no. Lex order for a sequence is determined by the first position where it differs. So the lex largest sequence is the one that has the largest possible first element, then the largest possible second element given the first, etc.

So for example, [3,3,2,1,0] is lex larger than [3,2,3,1,0], because the second element is 3 vs 2.

So to get the lex largest sequence, we need to collect the exponents in non-increasing order. So after generating all the exponents, sort them in non-increasing order.

But wait, after splitting, how are the exponents ordered? For example, after splitting the largest exponents, the exponents in the frequency map are in a way that the largest is as small as possible. Then, the sorted list of exponents (non-increasing) would give the lex largest sequence.

So, once all splits are done, the exponents are collected, sorted in non-increasing order, which would give the lex largest sequence.

So, the steps to solve the problem are:

1. Check if m (initial count of set bits) > k → output No.

2. Else, compute s = k - m.

3. Split s times, each time splitting the largest exponent in the current counts.

4. Once all splits are done, collect all exponents, sort them in non-increasing order.

5. Check if the sum of 2^e for each e in the list equals n. If not, output No. (But according to the problem statement, it's guaranteed that if the answer exists, the sum is correct.)

Wait, but how to ensure that after splitting, the sum remains correct?

Because each split of 2^e into two 2^(e-1) terms maintains the sum. For example, 2^e = 2 * 2^{e-1} → splitting once, sum remains same.

Thus, the process of splitting s times maintains the sum equal to n. So, if the initial sum is n and m <=k, then after s splits, the sum remains n.

So the check for sum is not needed. Thus, the problem reduces to:

- Check if possible (k >= m and after s splits, the sum can be split into k terms).

But during the splitting steps, if the s splits can't be done (but according to the problem statement, the answer exists?), perhaps for cases where exponents are allowed to be negative.

Wait, but when can splitting not be possible? For example, if after splitting all possible exponents down to some lower bound (like negative), but in that case, you can split any exponent as much as needed. Because exponents can be negative.

So as long as s >=0, and k >= m, then it's possible. But is that always true?

Sample 3: n=1 (binary 1, m=1), k=2. So s=1. Split once:

Split 0 (2^0 =1) into two 2^-1 terms (each 0.5). So the sum is 1. So possible.

Another example: n=3 (binary 11, m=2), k=3. So s=1. Split one of the 1's (exponent 1) into two 0's. Now exponents are [0,0,1]. Wait, no. Wait, initial exponents are 1 and 0. m=2. So splitting the 1 into two 0's. The new exponents are two 0's and one 0. So sum is 0.5*2 + 0.5*2 + 1? Wait, no. Wait, 2^1 is 2. Splitting into two 2^0 terms (each 1). So the sum is 1 + 1 + 0 → sum is 2. But original n is 3. So this is wrong.

Wait, this suggests a problem. Wait, splitting a term of 2^e into two terms of 2^(e-1). So the sum remains the same. For example, 2^e = 2 * 2^(e-1) → sum remains same.

So when splitting, the sum is maintained. So the initial sum is correct. So after splitting s times, the sum remains correct.

So for the example n=3, m=2, k=3. Then s=1. So split one of the 1 exponents into two 0's. Then exponents are 0,0,0 (original exponents were 1 and 0, splitting 1 into two 0's gives two 0's and one 0). Sum is 0.5 + 0.5 + 0.5 = 1.5. Which is not 3. So what's wrong here?

Ah, wait, perhaps I have a misunderstanding of how exponents work when split. Let's re-express this. The original term is 2^e. Splitting it into two terms of e-1: 2^{e-1} + 2^{e-1} = 2 * 2^{e-1} = 2^e. So sum is maintained.

So in the case of n=3, which is 2^1 + 2^0. Sum is 2+1=3. Then, split the 2^1 term into two 2^0 terms. Now the terms are 2^0, 2^0, 2^0. Sum is 1+1+1 = 3. So correct.

But in the previous calculation, I was considering exponents as 1 and 0. After splitting 1 into two 0's: the exponents become 0,0,0. So 3 terms. Sum is 1+1+1=3. Correct.

So the splitting process works.

So, the process is correct as long as s is non-negative and k >=m.

So, the initial check is: if k < m → output No.

Else, s = k -m. We need to split s times.

So, the steps are:

- Compute the binary representation of n. For each set bit, record the exponent. Let m be the count of set bits.

- If k < m → output No.

- Else, s =k -m.

- Split s times: each split takes the largest exponent present and splits it into two of (exponent-1).

- Collect all the exponents into a list.

- Sort the list in non-increasing order to get the lex largest sequence.

Now, how to model this efficiently.

But n can be up to 1e18, which is 60 bits. So m can be up to 60. Then, s can be up to 1e5 -60 ~ 1e5. So, for s steps, we need an efficient way to track the largest exponents and split them.

Using a priority queue (max-heap) is feasible. But for s up to 1e5, each step is O(log m), but m can be up to 60 + s, which for 1e5 steps would be up to 1e5, leading to O(1e5 * log 1e5) time. Which is acceptable for Python.

But implementing a max-heap in Python can be done using the heapq module, but with negative numbers.

So, the steps in code:

1. Read n and k.

2. Check if n is zero. But according to constraints, n >=1. So no need.

3. Compute the binary representation of n. For each set bit, collect the exponents. For example, for n=23 (binary 10111), exponents are 4,2,1,0.

4. m = len(exponents). If k < m → output No.

5. Else, s =k -m.

6. Create a max-heap (using negative values) of the exponents. Or, perhaps, since the initial exponents are up to 60, we can use a frequency map that tracks the count of each exponent.

Wait, but using a frequency map and tracking the current maximum exponent would be more efficient. Because each split on the current maximum exponent would reduce it by 1, but other exponents may be higher.

Alternatively, since we need to split the largest exponent each time, perhaps the frequency map can track for each exponent e, how many terms are there. Then, for each split step:

- Find the current maximum exponent e.

- If there are terms at e:

   - Decrement the count of e by 1.

   - Increment the count of e-1 by 2.

   - s decreases by 1.

But how to track the current maximum exponent e efficiently?

We can track the current maximum exponent in a variable. Then, after each split, if the count of e becomes zero, the new maximum may be e-1 or some other exponent that was present before.

Wait, but other exponents could be higher than e-1. For example, if after splitting e, there are other exponents at e-1, but there's also an exponent at e-2. So the new maximum may not be e-1.

Wait, no. If the current maximum was e, then after splitting e into e-1, the next maximum is either e-1 (if there are other exponents at e-1) or the next highest exponent present.

But this approach might be time-consuming if after each split, we have to search for the new maximum.

Alternatively, using a max-heap. The heap can store all exponents, and each time we split an exponent e, we add two e-1 exponents. But the heap will have duplicates. So, for example, if there are multiple e's, splitting one e would replace one e with two (e-1)s. So the heap needs to track all the individual exponents.

But this could be very memory-intensive if s is large (like 1e5). For example, each split adds two elements. So for s=1e5, the heap could have up to 1e5 elements.

But in reality, when we split an exponent e into two e-1, we can manage this more efficiently by tracking the counts for each exponent.

So, using a frequency map (dictionary) where key is the exponent, value is the count. Then, the maximum exponent is tracked.

So, for example:

Initially, for exponents [4,2,1,0], the frequency map is {4:1, 2:1, 1:1, 0:1}.

The current maximum is 4.

Split 4 into two 3's. Now, frequency map becomes {3:2, 2:1, 1:1, 0:1}, and current maximum is 3.

But after that, if we need to split again, the maximum is 3, split one of them into two 2's. Now frequency map is {3:1, 2:3, 1:1, 0:1}. Current maximum is 3 again (since there's still a 3). Splitting that 3 into two 2's: frequency map {2:5, 1:1, 0:1}, current maximum is 2.

So, the approach is to track the current maximum exponent. Each time, split one of the current maximum into two (current maximum -1). But if after splitting, the count of current maximum becomes zero, then the new maximum is current maximum -1, but only if there are existing exponents at current maximum -1. Otherwise, we have to find the next maximum.

Wait, no. For example, after splitting a 3 into two 2's, if there are other 3's left (like after the first split of 3, we have one 3 left), then the current maximum remains 3.

So, the current maximum can be tracked as a variable. Each time, when we split, if the count of the current maximum is reduced to zero, then we need to find the next maximum exponent present. Otherwise, the current maximum remains the same.

But how to find the next maximum exponent when the current maximum's count becomes zero?

This could be time-consuming if the frequency map is large. However, since exponents can be negative, but each split reduces the exponent by 1, and we can split any number of times, the current maximum can decrease over time.

But how to track this efficiently.

Alternative approach: keep track of the current maximum. Each time, split the current maximum until it's exhausted (count becomes zero), then the next maximum is current_max -1, and so on.

Wait, no. Because there may be other exponents in the frequency map that are higher than current_max -1.

Wait, no. Because the current maximum is the highest exponent present. So if after splitting, current_max's count becomes zero, then the new maximum is the next highest exponent present. For example, if the frequency map has {3:0, 2:5, ...}, then the current maximum is 2.

But how to track this.

An alternative is to keep a priority queue that contains all possible exponents (sorted in max order). But that's not feasible for large s.

Alternatively, since each split reduces the maximum exponent by 1 at most, we can track the current maximum and decrement it as needed.

So, the algorithm would be:

Initialize a frequency dictionary (freq) where keys are exponents and values are counts.

Initialize the current_max as the maximum exponent in the initial exponents.

s = k - m.

For each split in s splits:

   if freq[current_max] == 0:

       current_max -=1

   else:

       # split one exponent current_max into two (current_max-1)

       freq[current_max] -= 1

       if freq[current_max] == 0:

           del freq[current_max]

       # add two to current_max-1

       freq[current_max-1] = freq.get(current_max-1, 0) + 2

       s -=1

But wait, how do we handle the case when current_max is not present, but there are higher exponents? That's not possible because current_max is the maximum.

So the steps are:

current_max is initially the highest exponent.

for each of s splits:

   take one count from current_max.

   add two counts to current_max-1.

   if after this, freq[current_max] is zero, then current_max decreases by 1 until we find a current_max where freq[current_max] is non-zero.

But wait, after splitting current_max, the new current_max may be current_max-1 only if all higher exponents are zero.

For example, suppose current_max is 5. After splitting once, current_max becomes 4. But if there are other exponents in the frequency map with higher than 4 (like 5 still exists), then current_max remains 5.

Wait, no. Because the split is done on the current_max. So after splitting, the current_max's count is reduced by 1. So if after splitting, the current_max's count is now zero, then the next current_max is the next highest exponent in the frequency map.

But how to track that?

Perhaps the approach of keeping track of the current_max and then decrementing it until a non-zero frequency is found is not sufficient. For example:

Suppose the initial exponents are 5, 3, 2.

current_max is 5.

split 5 into two 4's. Now, current_max's count is zero. So current_max is decremented by 1 to 4.

split 4 into two 3's. current_max is 4, but after split, count of 4 becomes 1 (since we added two 4's and split once). Wait, no. Let's see:

Initial freq: {5:1, 3:1, 2:1}

split 5 into two 4's. freq becomes {4:2, 3:1, 2:1}. current_max is 4.

split 4 into two 3's. freq becomes {4:1, 3:3, 2:1}. current_max is still 4.

split 4 into two 3's again. freq becomes {3:5, 2:1}. current_max is now 3.

So in this case, after splitting 4's count becomes zero, we need to check if there's any exponent higher than 3. But since 3 is the next highest, current_max is updated to 3.

So the approach of decrementing current_max until a frequency is found is incorrect. Instead, after splitting, the current_max may remain the same if there are remaining exponents.

Wait, the current_max is the maximum exponent in the frequency map. So after splitting, the current_max's count is reduced by 1. If it's still positive, then the current_max remains. Otherwise, we need to find the new maximum exponent in the frequency map.

But how to track the new maximum exponent in the frequency map efficiently?

One way is to use a priority queue (max-heap) that contains all the exponents present in the frequency map. However, since we can have multiple entries of the same exponent, but the frequency map's count for that exponent is non-zero, we need to manage the heap entries.

But this can be tricky. For example, after splitting an exponent, the heap may have old entries.

Alternatively, since each split reduces the current_max's count by 1 and increases the count of current_max-1 by 2, we can track the current_max and then, when it's exhausted, the next current_max is current_max-1, but only if there are counts in that exponent. Otherwise, we need to find the next highest exponent.

Wait, but how?

Alternatively, we can note that after splitting current_max, the new exponents are current_max-1, and the current_max's count is reduced. So, the next split will either be on current_max (if there are remaining counts) or on current_max-1.

But in practice, after splitting the current_max once, if there are remaining counts in current_max, then the next split is again on current_max. Otherwise, current_max is decremented by 1.

But this approach may miss higher exponents. For example, suppose we have exponents 5 and 4.

current_max is 5. split once: 5's count becomes zero, so current_max is 4.

split again: 4's count is split into two 3's. current_max is 3.

But suppose there's another exponent 6 in the frequency map. But this is impossible, since current_max is the maximum.

So the approach is correct.

But how to handle cases where other exponents are present?

Let me think of an example:

Initial exponents: 5, 4, 3.

current_max is 5. split once: 5's count becomes zero, so current_max is 4.

split again: 4's count is split into two 3's. current_max is 4-1=3 (if 4's count becomes zero). But wait, if the initial count for 4 is 1, after splitting, 4's count is 0. So current_max is now 3.

But in the frequency map, there is also a 3. So after splitting 4 into two 3's, the frequency map becomes 3:3. current_max is 3.

So yes.

So the approach works.

Thus, the steps are:

- Track the current_max as the current maximum exponent.

- For each split:

   - Decrease the count of current_max by 1.

   - If the count of current_max becomes zero, remove it from the frequency map.

   - Increase the count of (current_max-1) by 2.

   - If current_max's count is now zero, then current_max is updated to current_max-1. However, this may not be correct if there are other exponents with higher exponents.

Wait, no. Because current_max was the maximum exponent. So after splitting, the only possible higher exponents could be if there were other exponents with the same current_max. But after splitting, if current_max's count is zero, then the new current_max is the next highest exponent in the frequency map.

But how to find the next highest exponent?

This suggests that using a frequency map and a current_max variable is not sufficient, as after current_max's count is zero, there might be other exponents higher than current_max-1.

For example:

Initial exponents: 5, 5, 3.

current_max is 5.

split once: count of 5 is 2-1=1. So current_max is still 5.

split again: count of 5 is 1-1=0. So current_max is decremented by 1 to 4. But the frequency map now has 3:1. So the new current_max is 3. But according to the frequency map, the highest exponent is 3. So the code would have current_max as 4, but in reality, the highest exponent is 3.

This would be a mistake.

Ah, this is a problem. Because after splitting current_max (5) into two 4's, the frequency map for 5 becomes zero, so current_max is decremented to 4. But the frequency map has 4:2, so current_max should remain 4. Then, when splitting 4 into two 3's, current_max is 4 again.

So the code's approach would work in this case.

Wait, in the example:

Initial exponents: 5,5,3. current_max is 5.

split once: count of 5 is 2-1=1. current_max remains 5.

split again: count of 5 is 1-1=0. So current_max is decremented by 1 to 4. Now, the frequency map has 4:2 (from the two splits of 5) and 3:1.

current_max is 4. So next split is on 4.

split again: count of 4 is 2-1=1. add two 3's. So frequency map becomes 4:1, 3:3. current_max is 4.

split again: count of 4 is 1-1=0. So current_max is decremented to 3. Now, frequency map has 3:3.

So after splitting, the current_max is correctly found.

So the approach of decrementing current_max by 1 each time the count reaches zero seems to work.

But in reality, after current_max's count is zero, there may be other exponents in the frequency map that are higher than current_max-1. For example:

Initial exponents: 5, 4.

current_max is 5.

split once: 5's count is 0. current_max is decremented to 4. But the frequency map has 4:1 (original) plus two 4's from splitting 5. So 4's count becomes 3.

So current_max is 4. Correct.

Another example:

Initial exponents: 5, 6.

current_max is 6.

split once: 6's count becomes 0. current_max is decremented to 5. But frequency map has 5:1 and 5's count is 1 (from the split of 6 into two 5's). So current_max is 5.

Yes.

But what if after splitting, the current_max-1 is not the next highest exponent?

For example:

Initial exponents: 5, 3.

current_max is 5.

split once: 5's count becomes 0. current_max is decremented to 4. But frequency map has 4:2 (from split of 5) and 3:1. So current_max is 4.

Yes.

Another split: split 4 into two 3's. Now frequency map has 4:1, 3:3. current_max is 4.

split again: 4's count becomes 0. current_max is 3. frequency map has 3:3.

So this works.

So the approach of tracking current_max and decrementing it by 1 each time the count becomes zero works, even if there are other exponents in the frequency map. Because after splitting, the current_max is decremented until it finds the next exponent.

But how does this work if there's an exponent higher than current_max-1?

Wait, current_max is the maximum exponent in the frequency map. So if we split current_max into current_max-1, there can't be any exponents higher than current_max. So when current_max's count is zero, the next current_max must be current_max-1, or a lower exponent.

But there could be exponents in the frequency map with exponents higher than current_max-1. For example, current_max is 5, and the frequency map has 5:0, 4:2, 3:1. So current_max is now 4. But 4 is higher than 3.

Yes. So the approach of decrementing current_max by 1 each time the count becomes zero works because after splitting, the next highest exponent is current_max-1.

So the code can proceed as follows:

- Use a frequency map (dictionary) to track the counts of each exponent.

- current_max is initialized to the maximum exponent in the initial list.

- for s splits:

   while current_max is not present in the frequency map or its count is zero:

       current_max -=1

   if current_max is not present (like after all exponents are split down to negative infinity), but that can't happen since the sum is maintained.

   then, subtract one from the count of current_max. If count becomes zero, remove it from the frequency map.

   add two to current_max-1.

   s decreases by 1.

But the while loop to decrement current_max until we find an exponent with count>0.

Wait, for example, after splitting current_max, which was 5, into two 4's. current_max is now 5, but count is zero. So we decrement current_max to 4, check if count is present and >0. If yes, proceed. Otherwise, decrement again.

But how to implement this.

The code could be:

from collections import defaultdict

freq = defaultdict(int)

for e in exponents:

    freq[e] += 1

current_max = max(exponents) if exponents else 0

s = k - m

while s > 0:

    # Find the current_max with count >0

    while current_max not in freq or freq[current_max] == 0:

        current_max -= 1

    # Split current_max

    freq[current_max] -= 1

    if freq[current_max] == 0:

        del freq[current_max]

    freq[current_max - 1] += 2

    s -= 1

After all splits, collect all exponents into a list.

But how to collect all exponents from the frequency map. For example, for each exponent e, add e to the list count times.

Then, sort the list in non-increasing order to get the lex largest sequence.

For example, after splits, the frequency map might have 3:2, 2:1, 1:1, 0:1. So the exponents are [3,3,2,1,0], which sorted is [3,3,2,1,0].

Yes.

So the code steps are:

After the splitting:

result = []

for e in sorted(freq.keys(), reverse=True):

    result.extend([e] * freq[e])

Then, check if the length is exactly k. If yes, output.

But the code must handle exponents in the frequency map in sorted order.

But for the sample input 1:

After splitting once, freq is {3:2, 2:1, 1:1, 0:1}. So sorted in reverse order, the exponents are 3,3,2,1,0. Which matches the sample.

Now, for the third sample:

n=1, k=2.

Initial exponents: [0]. m=1.

s=1.

current_max is 0.

split once:

freq[0] becomes 0, then add two -1's.

current_max is decremented to -1.

So the exponents are -1, -1. So the sorted list is [-1, -1], which matches the sample.

Yes.

So this approach works.

Now, to code this in Python:

But first, how to compute the initial exponents.

n can be up to 1e18. So we need to find all the exponents where the binary representation of n has a 1.

So for each bit in n's binary representation, if it's set, add the exponent (bit position) to the exponents list.

But n can be up to 1e18, which is 60 bits. So for example, n=1 is 1 in binary, exponent 0.

So for example, n=23 is 10111 → exponents 4,2,1,0.

Wait, but for each bit, the exponent is the position, starting from 0 for the least significant bit.

Yes. So for each bit i (starting from 0), if the bit is set, then the exponent is i.

So code to generate exponents:

exponents = []

bit = 0

temp = n

while temp > 0:

    if temp & 1:

        exponents.append(bit)

    temp >>= 1

    bit += 1

But this gives the exponents in increasing order. Wait, no. For example, n=23 (binary 10111) has bits set at 0,1,2,4. So exponents list is [0,1,2,4]. But the initial max is 4.

But the code appends the bits in the order of the least significant bit first. So exponents list is [0,1,2,4], but after reversing, the order is [4,2,1,0]. No, no. Wait, the code appends the exponents in order of the bit positions, starting from 0 (LSB). So for 23 (binary 10111), the bits are set at positions 0,1,2,4. So exponents list is [0,1,2,4]. So the initial exponents are [0,1,2,4]. The max is 4.

But when creating the frequency map, the code uses these exponents. So in the frequency map, each exponent appears once. So initial freq is {0:1, 1:1, 2:1,4:1}.

But when processing the current_max, the initial current_max is 4.

Split s=1 times:

current_max is 4. split into two 3's.

freq[4] becomes 0, so delete. Add 3:2.

current_max is 3.

But now, after splitting once, the exponents are 3,3,2,1,0. Which is correct.

So the code for generating the initial exponents is correct.

Now, code steps:

Read n and k.

Compute exponents as the list of bit positions where the bit is set.

m = len(exponents)

if k < m:

    print("No")

    exit()

if k == m:

    exponents_sorted = sorted(exponents, reverse=True)

    print("Yes")

    print(' '.join(map(str, exponents_sorted)))

    exit()

else:

    s = k -m

    # proceed with splitting.

Implement the frequency map and current_max.

But for large exponents (up to 60), and s up to 1e5, this approach is feasible.

But for the frequency map, using a defaultdict(int) is okay.

Once the splitting is done, collect all the exponents and sort in reverse order.

But what if the frequency map has exponents that are not present in the initial list but added via splits?

Yes. For example, after splitting 4 into two 3's, the exponents 3 are added.

So the code will collect all exponents from the frequency map.

Then, once collected, sort in reverse order.

So the code:

from collections import defaultdict

n, k = map(int, input().split())

# Compute initial exponents.

exponents = []

temp = n

bit = 0

while temp > 0:

    if temp % 2 == 1:

        exponents.append(bit)

    temp = temp // 2

    bit +=1

m = len(exponents)

if k < m:

    print("No")

    exit()

if k == m:

    # output sorted in reverse order.

    exponents_sorted = sorted(exponents, reverse=True)

    print("Yes")

    print(' '.join(map(str, exponents_sorted)))

    exit()

# Else, proceed with splitting.

s = k -m

freq = defaultdict(int)

for e in exponents:

    freq[e] +=1

current_max = max(exponents) if exponents else 0

while s >0:

    # Find current_max with count >0.

    # Because initially current_max is valid, but after splits, it may not.

    while current_max not in freq or freq[current_max] ==0:

        current_max -=1

    # Split current_max.

    freq[current_max] -=1

    if freq[current_max] ==0:

        del freq[current_max]

    freq[current_max-1] +=2

    s -=1

# Now collect all exponents.

result = []

for e in sorted(freq.keys(), reverse=True):

    result.extend([e] * freq[e])

# Check if the length is k.

# Because of the splits, it should be.

print("Yes")

print(' '.join(map(str, result)))

But let's test this code against the samples.

Sample 1:

Input:

23 5

23 in binary is 10111 → exponents are 0,1,2,4 (wait, no. Wait, let's compute exponents.

Wait, temp starts as 23.

temp % 2 → 1 → exponents.append(0)

temp becomes 11.

temp %2 → 1 → exponents.append(1)

temp becomes 5.

temp%2 →1 → exponents.append(2)

temp becomes 2.

temp%2 →0 → no. temp becomes 1.

temp%2 →1 → exponents.append(3).

temp becomes 0. loop ends.

So exponents are [0,1,2,3]. Wait, no.

Wait, let's re-calculate for n=23.

n is 23. Let's compute:

bit 0: 23 %2=1 → exponents.append(0) → temp=11, bit 1.

bit 1: 11%2=1 → exponents.append(1) → temp=5, bit 2.

bit 2:5%2=1 → exponents.append(2) → temp=2, bit3.

bit3: 2%2=0 → temp=1, bit4.

bit4:1%2=1 → exponents.append(4) → temp=0, loop ends.

So exponents are [0,1,2,4].

So m=4. k=5. s=1.

current_max is 4.

split once:

freq[4] becomes 0. del. add 3:2.

current_max is 3.

collect exponents:

sorted(freq.keys(), reverse=True) →3,2,1,0.

freq[3] is 2, freq[2] is 1, freq[1] is 1, freq[0] is1.

so result is [3,3,2,1,0], which matches the sample.

Sample 3:

n=1, k=2.

exponents are [0]. m=1. s=1.

split once.

current_max is 0.

split into -1: 2.

current_max is now -1.

result is sorted in reverse order [-1, -1], which is correct.

Sample 2:

n=13 (binary 1101 → exponents 0,2,3). m=3. k=2 <3 → output No.

So code seems to work.

Now, test for n=3, k=3.

n=3 (11) → exponents 0,1. m=2. s=1.

split once.

current_max is 1.

split into two 0's. freq[0] becomes 3 (initial 0 and 2 from split).

result is [0,0,0], sum 1+1+1=3.

sorted in reverse → [0,0,0].

Yes.

Another test case: n=4 (100), exponents [2]. k=3.

s=2.

current_max is 2.

split once: 2 becomes 0, add two 1's. freq[1]=2.

current_max is 1.

split again: take 1, split into two 0's. freq[1]=1, add two 0's → freq[0] =3.

now, s=0.

result is [1,0,0,0] (after collecting exponents: sorted reverse →1,0,0,0 → but wait, the frequency map after splits:

split 2 → 1:2.

split 1 → 0:2+1 (initial 0 from split of 2? No.

Wait, initial exponents are [2], so freq starts as {2:1}.

split once: s=2-1=1.

current_max is 2.

split 2 into two 1's. freq[2] becomes 0, deleted. freq[1] becomes 2.

s becomes 1.

current_max is now 1.

split 1: split into two 0's. freq[1] is 2-1=1. add two 0's. freq[0] is 2.

s becomes 0.

so the frequency map is {1:1, 0:2}.

collect exponents: sorted reverse is 1,0,0.

but the total count is 1+2=3, which is correct. So the result is [1,0,0].

sum is 2^1 + 2^0 + 2^0 = 2+1+1=4.

Yes.

But the sorted list is [1,0,0], which is lex largest possible.

Yes.

So the code works.

Now, the code reads n and k, computes the exponents correctly, manages the frequency map and current_max correctly, and sorts the result in reverse order.

Thus, this code should handle all test cases correctly.
</think>

```python
from collections import defaultdict

n, k = map(int, input().split())

exponents = []
temp = n
bit = 0
while temp > 0:
    if temp % 2 == 1:
        exponents.append(bit)
    temp = temp // 2
    bit += 1

m = len(exponents)
if k < m:
    print("No")
else:
    if k == m:
        exponents_sorted = sorted(exponents, reverse=True)
        print("Yes")
        print(' '.join(map(str, exponents_sorted)))
    else:
        s = k - m
        freq = defaultdict(int)
        for e in exponents:
            freq[e] += 1
        current_max = max(exponents) if exponents else 0
        while s > 0:
            while current_max not in freq or freq[current_max] == 0:
                current_max -= 1
            freq[current_max] -= 1
            if freq[current_max] == 0:
                del freq[current_max]
            freq[current_max - 1] += 2
            s -= 1
        
        result = []
        for e in sorted(freq.keys(), reverse=True):
            result.extend([e] * freq[e])
        print("Yes")
        print(' '.join(map(str, result)))
```