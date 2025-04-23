<think>
Okay, let's try to understand this problem. So, we need to compute for each p (from 0 to n), the number of subsequences of the given array such that the density of the subsequence is exactly p. Then, output all these s_p values modulo 998244353.

First, what's the density of an array? The density is the maximum p such that every possible c-array of length p is a subarray (subsequence, actually, since the indices are increasing) of the given array. Wait, no, the problem says that any c-array with p elements must be a subsequence of the array. So the density is the largest p where the array contains all possible combinations of p elements, each between 1 and c.

Wait, no. Let me re-read the definition. The density is the maximal p such that any c-array that contains p numbers is a subarray (subsequence) of the array. So, for example, if the density is p, then every possible sequence of p elements (each from 1 to c) must appear as a subsequence in the array. Otherwise, if there's even one p-length sequence that doesn't appear, then the density is less than p.

So the density of the array is the maximum p where the array is a supersequence for all possible p-length c-arrays.

Hmm. So, for a given subsequence of the original array, we need to determine its density p, and count all such subsequences for each possible p.

The problem requires us to compute, for each p from 0 to n, the number of subsequences (of any length) of the original array that have exactly density p.

Now, the challenge is to model this efficiently for n up to 3000, and c up to 3000. Since n and c are both up to 3e3, any O(n^2 c^2) algorithm might be manageable, but we have to be careful.

Let's think about the approach. For a subsequence to have density p, two conditions must hold:

1. The subsequence contains all possible p-length c-arrays as subsequences.
2. It does not contain all possible (p+1)-length c-arrays as subsequences.

If p is 0, that means the subsequence is empty (since the empty array's density is 0). Wait, but according to the problem statement, the density is the maximal non-negative integer p such that any c-array of p numbers is a subsequence. The empty array has density 0, but if the subsequence is non-empty, but can't have any p >=1, then its density is 0. Wait, no. Let me think again. For example, if the subsequence is [1], then for p=1, we have to check if all possible 1-length c-arrays are present. Since c=1 here, the 1-length array is [1], which is present. So the density would be 1. But if the array is [1] and c=2, then the possible 1-length arrays are [1], [2]. Since [2] isn't present, the density is 0. So for a subsequence to have density p, it must contain all possible p-length sequences, but not p+1-length ones.

So the first step is to model the density of a subsequence. How can we compute the density of a given subsequence efficiently?

Alternatively, perhaps we can model the density in terms of the structure of the subsequence. Let's think: the density p is the maximum p such that the subsequence is a universal supersequence for all p-length sequences. So, how do we check that a given array S has density p?

This seems similar to the problem of determining the universality of a string for certain lengths. For example, in the first sample, since all elements are 1, any p-length sequence can only be 1s. So the density is the length of the subsequence. For example, the sample input 1's output shows that s_p is the binomial coefficient C(4, p), which makes sense because each subsequence of length k has density k. Because any p-length sequence (for p <=k) must be all 1s, and the subsequence's length is k, so the maximum p is k.

In the second example, the array is [1,2,3]. The only subsequence that has density 3 is the entire array. Because any 3-length sequence (for c=3) would need to have all possible permutations. Wait, but the problem requires that the array contains all possible c-arrays of length p as subsequences. For example, for p=3, the possible sequences are all 3-length sequences where each element is 1, 2, or 3. But the array [1,2,3] can't have all possible sequences. For example, [1,1,1] isn't a subsequence. So why is the output 0 for p=3?

Wait, the second example's output is 6 1 0 0. So for p=0, the count is 6. Wait, but the empty subsequence is counted as p=0, but according to the problem statement, the sequences are for k>=1. Wait no, the problem says: "for all 0 ≤ p ≤ n find the number of sequences of indices ... for all 1 ≤ k ≤n, such that..." Wait, no, the problem says: for all 0 ≤ p ≤n, s_p is the number of sequences of indices (for all k from 1 to n) such that the density is p. Wait, but the empty sequence is not considered here. Because k starts from 1. Wait, but the output includes s_0. So how is s_0 calculated?

Ah, perhaps the problem statement is a bit unclear. Let's read the problem statement again:

"For all 0 ≤ p ≤ n find the number of sequences of indices ... for all 1 ≤ k ≤ n ... such that density ... is equal to p."

Wait, no. The problem says, the sequences of indices are for all 1 ≤ k ≤ n. So the empty subsequence (k=0) is not considered. But in the first sample input, the output is 0 4 6 4 1. For p=4, the count is 1. That's the entire array (k=4). So the empty subsequence is not counted. So s_0 counts all subsequences (non-empty) with density 0. Wait, but the empty subsequence has density 0. But according to the problem statement, the output includes s_0, which counts all sequences of indices (for k ≥1) with density 0. Wait, that can't be. So the problem's output includes s_0, which is the number of non-empty subsequences (since k is from 1 to n) whose density is 0. But the empty subsequence is not considered here. So the problem requires us to count all non-empty subsequences (all possible k from 1 to n) for each possible p.

Wait, the problem statement says:

"the number of sequences of indices 1 ≤ i_1 < ... < i_k ≤ n for all 1 ≤k ≤n, such that ...".

So for each k from 1 to n, we consider all possible subsequences of length k. Then, for each such subsequence, we calculate its density p, and add 1 to s_p. So the output s_p is the total number of non-empty subsequences (since k starts at 1) that have density exactly p.

So in the first example, the output is 0 4 6 4 1.

Looking at the first sample input:

The array is 4 elements of 1, c=1. Any subsequence of length k has density k, because all elements are 1. So for k=1, there are 4 subsequences, each with density 1. For k=2, each has density 2. So for p=1, the count is 4; p=2 is 6, etc. But wait, in the output, s_0 is 0, which implies there are no non-empty subsequences with density 0. Which makes sense, because any non-empty subsequence here is made of 1s. For c=1, the possible sequences of p=1 must contain all 1s, but since c=1, the only possible 1-length sequence is [1], which all subsequences of length ≥1 contain. So each such subsequence of length k has density k, which for k up to 4. So the maximum p possible is 4 (when the entire array is taken). So the s_p values are the number of subsequences of length p. So s_1 is C(4,1) =4, s_2 C(4,2)=6, etc. s_0 is 0 because no non-empty subsequence has density 0.

In the second sample input, the array is [1,2,3], c=3. The output is 6 1 0 0. So s_0 is 6 (the number of non-empty subsequences with density 0). The only subsequence with density 1 is the entire array (k=3). Wait, no. The problem's output shows s_1 is 1. Let me think. For the array [1,2,3], any subsequence of length less than 3 would not include all three elements. For example, if the subsequence is [1,2], then for p=2, the density would be 0 because there's no way to have the sequence [3,3] as a subsequence, which is required for p=2. So any subsequence that is not the full array would have density 0, except maybe when it's the full array. Wait, but the full array has density 3? No, because the problem requires that all possible 3-length c-arrays are present as subsequences, which is impossible. For example, the 3-length sequence [1,1,1] is not a subsequence of [1,2,3]. Therefore, the entire array's density is 0. Wait, but the sample output says s_0 is 6 (the number of non-empty subsequences of length 1 and 2), and s_1 is 1. So the entire array (length 3) has density 1?

Hmm, perhaps my understanding is incorrect. Let's re-examine the second example.

Sample input 2:

3 3

1 2 3

Sample output: 6 1 0 0.

So the output is s_0=6, s_1=1, s_2=0, s_3=0.

So there are 6 non-empty subsequences (of length 1 or 2) with density 0, and 1 subsequence (the entire array) with density 1, and none for higher p.

So the entire array's density is 1. How?

The density is the maximum p such that all p-length c-arrays are present as subsequences. For p=1, the possible 1-length arrays are [1], [2], [3], which are all present. So the density is at least 1. For p=2, we need to check all possible 2-length sequences (each element in 1-3). For example, [1,1] is not present as a subsequence of the array. So the density cannot be 2. Hence, the maximum p is 1. So the entire array has density 1, which contributes to s_1. The other 6 subsequences (all of length 1 or 2) have density 0.

So, for the entire array, the density is 1. Because for p=1, all possible 1-length sequences are present, but for p=2, not all.

So the problem is to compute for each possible subsequence (non-empty) its density, and accumulate the counts.

Now, the challenge is to compute this for all possible subsequences, which is O(2^n) in the worst case, which is impossible for n=3000. So we need a dynamic programming approach or some combinatorial model that allows us to compute the counts efficiently.

So the key is to model the problem in terms of the structure of the array that determines the density p. For a given subsequence, the maximum p is determined by the minimal p where there exists a (p+1)-length sequence that is not present.

Hmm. So, perhaps the density is the minimal p such that the subsequence contains all possible p-length sequences but not all (p+1)-length ones. Wait, no. The density is the maximum p where all p-length sequences are present. So p is the largest such number.

So, to compute the density of a subsequence S, we need to find the maximum p where all possible sequences of length p (with elements from 1 to c) are present in S as a subsequence.

But how do we model this? For each possible p, we need to check if all possible c^p sequences are present as subsequences. But that's computationally impossible for even small p and c.

But given that c can be up to 3000, and p up to 3000, this is impossible. So there's a smarter way to model this.

Alternative approach: Let's think about the structure of the array that allows maximum p.

The maximum p is the maximum integer such that the array S is a supersequence for all possible c^p sequences. How can we model this?

This problem is similar to the problem of determining the minimal length of a supersequence that contains all possible sequences of a certain length. For example, the de Bruijn sequence for certain parameters.

But in our case, the given array's subsequences can have varying p, and we need to compute for each possible subsequence S what p is.

Alternatively, perhaps there's a way to model the density based on certain properties of the array S. For example, for the array S to have density p, it must contain all possible p-length sequences. So, for each possible p, we need to determine whether S contains all possible p-length sequences. But checking this for all possible p for each possible S is impossible.

So, the key is to find a way to model the density p of a given S efficiently.

Let me think differently. For a subsequence S of the original array, the density p is the maximum number such that all possible p-length sequences over 1..c are present as subsequences of S.

The problem seems similar to the concept of a universal set for certain string lengths. For example, a string is called a universal if it contains all possible sequences of a certain length as a substring. But here, the sequences can be non-consecutive (subsequence) and the array can be considered as a string where each element is a character from the alphabet {1..c}.

For a sequence to have density p, it must be universal for p-length sequences, but not for (p+1)-length ones.

So, the question is: How can we model the maximum p for a given subsequence S?

This seems challenging. Let's think about the necessary conditions for S to have a density of p.

For p=0: This means that S is empty. But according to the problem statement, S must be non-empty. Wait, no, because the problem counts non-empty subsequences. So p=0 for S means that S does not contain all possible 1-length sequences. For example, if S is [1,1] and c=2, then S's density is 0 because the 1-length sequence [2] is not present.

So, for S to have density p:

- For each possible sequence of length p (all elements in 1..c), S must contain it as a subsequence.
- There exists at least one sequence of length p+1 that is not present in S.

So, the problem is to compute for all possible non-empty S (subsequences of the original array), their maximum p, and count how many S's have that p.

But with n up to 3000, this is impossible to compute naively. So we need a DP approach that can model the necessary conditions.

Let me think about the problem from another angle. For a subsequence S to have density p, all possible p-length sequences must be present. How can this be modeled?

Perhaps we can model the problem by tracking, for each possible p, the earliest positions where each possible p-length sequence can be formed. But even that seems challenging for p up to 3000.

Alternatively, perhaps the maximum p for a given subsequence S is the minimum number of times each element from 1..c appears in S. For example, in the first sample where all elements are 1 and c=1, the number of 1's in S is k. Then, the maximum p is k. Because any sequence of k 1's is present. But if c=1 and the subsequence has length k, then p must be k. Because all possible sequences (which are just 1's) of length k are present. So for each element in the subsequence, if it's 1, then the density is the length of the subsequence.

This suggests that in the case where all elements are the same and c=1, the density is equal to the length of the subsequence. Which matches the first sample.

But in the second sample, the entire array has 1,2,3, each once. The maximum p is 1, because all 1-length sequences are present, but not all 2-length. So the number of times each element appears is 1. The minimal number of occurrences of any element is 1, but the maximum p is 1. So in that case, p is the minimal number of occurrences of each element. Hmm, that's interesting. Let's see:

If in S, each of the c elements appears at least m times, then can we have p >= m? For example, suppose S contains m copies of each element. Then, any sequence of length m can be formed by choosing one element from each of the m positions where that element appears. For example, if S has m copies of each of the c elements, then any sequence of length m can be formed by selecting the first occurrence of the desired element for each position.

So, in this case, the maximum p would be m. Because for any m-length sequence, you can pick the first occurrence of each element in the sequence. So if each element occurs at least m times, then the density is at least m.

But the maximum p could be higher. Wait, no. Because if each element occurs exactly m times, then for p=m+1, you need to have a sequence of m+1 elements. For example, if you have m+1 of the same element, but each element occurs only m times, then the sequence [x, x, ..., x] (m+1 times) is not present. So the maximum p is m.

So, this suggests that the maximum p is the minimal number of occurrences of each element in the subsequence S. So, for S to have p as its density, the minimal number of occurrences of any element in S must be exactly p, and there exists at least one element that occurs exactly p times. Because if all elements have >= p occurrences, but there's at least one element with exactly p, then the maximum p would be p. Wait, no. Let's think again.

Suppose the minimal count is m. Then, each element occurs at least m times. Then, any sequence of m elements can be formed by selecting one element from each of the m occurrences. So the density is at least m. But what about sequences longer than m? For example, if we have m+1 elements. So the maximum p is m.

So, in this model, the maximum p is the minimal number of times any element occurs in S.

Is this correct?

Let's test this with the second sample:

The entire array has each element once. So the minimal count is 1. So the maximum p is 1. Which matches the sample.

Another example: S has elements [1,2,1,2,1], c=2. The counts are 3 for 1, 2 for 2. Minimal count is 2. So p=2. So any 2-length sequence can be formed. For example, [1,1], [1,2], [2,1], [2,2]. Let's see:

For [1,1], the subsequence can be the first and third elements.

For [2,2], the subsequence can be the second and fourth elements.

Yes, so the minimal count is 2, and the maximum p is 2. But what about p=3? For that, the minimal count would need to be 3. So if S has elements 1,1,1,2,2,2, then the minimal count is 3, and p=3.

So, according to this model, the maximum p is equal to the minimal count of the elements in S.

But wait, what if the elements are arranged in a way that even if each element occurs m times, there exists a sequence of length m that is not present?

For example, S = [1,2,1,2], c=2. Each element occurs 2 times. Then, the minimal count is 2. So according to the model, p=2. Let's see if all 2-length sequences are present.

Possible sequences: [1,1], [1,2], [2,1], [2,2].

Yes:

- [1,1] can be formed by the first and third elements.
- [1,2] by first and second.
- [2,1] by second and third.
- [2,2] by second and fourth.

So p=2 is correct.

Another example: S = [1,2,3,1,2,3], c=3. Each element occurs 2 times. So minimal count is 2. So p=2. All 2-length sequences must be present. But for the sequence [1,3], is it present? Yes: elements 1 (first) and 3 (third). So all sequences are present. So p=2. Now, what about p=3. For example, [1,1,1] requires 3 1's. But S has only 2. So no. Hence, the maximum p is 2.

So this model seems to hold.

But what if S has elements [1,2,3,4], each occurring once. c=4. Minimal count is 1. So p=1. So all 1-length sequences are present. But what about 2-length sequences? For example, [1,1] is not present. So the maximum p is indeed 1.

Thus, the model that the maximum p is the minimal number of occurrences of any element in the subsequence S seems to hold.

So, the problem reduces to:

For each possible non-empty subsequence S of the original array, compute the minimal number of occurrences of any element in S, and then that is the p for which we increment s_p. Then, after processing all subsequences, output s_0 to s_n modulo 998244353.

But wait, is this always the case? Let's think of a scenario where the minimal count is m, but there exists a sequence of length m that is not present.

For example, suppose S has elements [1, 2, 1, 2], but the elements are arranged as 1, 2, 1, 2. The minimal count is 2. So p=2, and all 2-length sequences must be present. But in this case, they are. So the model holds.

Another example: S is [1, 2, 2, 2]. c=2. The minimal count of 1 is 1 (element 1 occurs once, element 2 occurs 3 times). So p=1. But for p=1, all 1-length sequences are present. So yes.

But what if S is [1, 2, 3, 1, 2, 3], and c=3. Each element occurs 2 times. So the minimal count is 2, so p=2. All 2-length sequences are present. For example, [1,1] can be formed by the first and fourth elements. [1,2] by first and second. etc. So yes.

So, the model holds.

Therefore, the problem reduces to counting the number of non-empty subsequences where the minimal number of occurrences of any element in the subsequence is exactly p. But wait, the model says that the maximum p is the minimal count of any element. So for a subsequence S, its density p is equal to the minimal number of occurrences of any element in S.

But wait, in the case where some elements are missing in S, then the minimal count would be zero, but since S is non-empty, that's impossible. So, for S to be a non-empty subsequence, all elements present in S have count >=1. But if some elements from 1..c are not present in S, then the minimal count is zero (for those elements not present). But since S is non-empty, but some elements are not present, then the minimal count is zero. However, in this case, the maximum p is zero. Because for p=1, the array must contain all 1-length sequences (all elements from 1..c). If S is missing some elements, then p is zero.

So, this suggests that the model is slightly more complex. The maximum p is the minimum between the minimal count of elements present in S and the number of elements present in S.

Wait, let me re-examine. For example, if S has elements [1,1,1], and c=2. Then the elements present are only 1. So for p=1, all 1-length sequences (1 and 2) must be present in S. But since 2 is not present, the density is zero. So in this case, the minimal count of elements present is 3 (count of 1 is 3), but because the other element is missing, the density is zero.

So the model must account for both the minimal count of elements present and whether all elements are present.

Ah, right. So the model should be adjusted as follows:

The density p of S is the minimum between:

- the minimal number of occurrences of each element present in S.

- the number of elements present in S.

Wait, no. Wait, in order for all p-length sequences to be present in S, S must contain all possible elements. For example, if c=3 and S contains only elements 1 and 2, then any sequence containing 3 is not present, so the density is zero. Therefore, for the density to be at least p=1, S must contain all elements from 1..c. Otherwise, the density is zero.

So, the model must first check whether S contains all c elements. If not, the density is zero. Otherwise, the density is the minimal number of occurrences of any of the c elements in S.

So, the density p is equal to the minimal number of occurrences of any element in S, provided that all c elements are present in S. Otherwise, p is zero.

So the model is:

If S contains all c elements, then p = min_{1 ≤ x ≤ c} (count_x in S).

Otherwise, p = 0.

So, for example:

- S is [1], c=1: contains all elements. count is 1. So p=1.

- S is [1,1], c=1: p=2.

- S is [1,2], c=2: contains all elements. min count is 1. So p=1.

- S is [1,2,3], c=3: min count is 1. p=1.

- S is [1,2,3,1,2,3], c=3: min count is 2. p=2.

So, this model seems to fit the samples.

In the first sample, c=1 and all elements are 1. So all non-empty subsequences contain all 1 elements. So min count is the length of the subsequence. Hence, p equals the length.

In the second sample, the only subsequence that contains all 3 elements is the full array. The min count is 1, so p=1. All other subsequences (of length 1 or 2) miss at least one element, hence p=0. So s_1 is 1, s_0 is 7-1=6 (since there are 7 non-empty subsequences in total for n=3: 3 choose 1 (3) + 3 choose 2 (3) + 1 (3 choose 3) = 7. So 7-1=6 for s_0, which matches the sample output.

The third sample:

Input is 5 2

1 2 1 2 1

Output is 10 17 4 0 0 0.

Let's see. The total number of non-empty subsequences is 2^5 -1 =31. The output is s_0=10, s_1=17, s_2=4.

So, s_0 + s_1 + s_2 = 10+17+4=31.

Now, according to the model, a subsequence contributes to s_p if either:

- It contains all 2 elements (1 and 2) → p is the minimum of the counts of 1 and 2 in the subsequence.

- Or, it does not contain all elements → p=0.

So, for s_0, it's the number of subsequences that miss at least one element. For s_1, it's the number of subsequences that contain both elements, and the min count is 1. For s_2, min count is 2.

Let's compute s_2: subsequences that contain both elements, with counts of 1 and 2 both >=2, and the minimal count is 2. So, the counts of 1 must be at least 2, and counts of 2 must be at least 2, and the minimal is 2.

But in the original array, there are 3 1's and 2 2's. So for a subsequence to have counts of 1 >=2 and 2 >=2, the subsequence must take at least 2 of each. But since the array has only 2 2's, the counts of 2 can be exactly 2. Then, the count of 1 must be >=2. So the minimal is 2. So how many such subsequences are there?

To choose 2 2's and at least 2 1's. The 2's are in positions 2 and 4. The 1's are in positions 1,3,5. So, the subsequence must include both 2's, and at least two 1's. So the 1's can be any subset of size >=2 from the three positions. So the number of such subsets is (2^3 - 1 -3) = 4 (since 3C0=1, 3C1=3 → subtract those from 8). So 4. Hence s_2 is 4.

Which matches the sample. So the model works.

Now, the problem is to compute for each possible p, the number of non-empty subsequences S where:

1. S contains all c elements, and the minimal count of any element in S is exactly p. → contributes to s_p.

OR

2. S does not contain all c elements. → contributes to s_0.

So the steps to solve the problem are:

For all non-empty subsequences S:

- If S does not contain all c elements → add 1 to s_0.

- Else:

   Let m be the minimal count of any element in S → add 1 to s_m.

Thus, the problem reduces to:

Compute two parts:

A. The number of non-empty subsequences that contain all c elements. For these, compute the minimal count m and count them per m.

B. The number of non-empty subsequences that do not contain all c elements. All these contribute to s_0.

Then, the answer is:

s_p = (B) if p=0 else (number of subsequences in part A with m = p).

So, our first task is to compute B, which is the total number of non-empty subsequences that are missing at least one element. But since the elements are up to 3000, inclusion-exclusion may not be feasible. So, perhaps we can compute B as (total non-empty subsequences) - (number of subsequences that include all c elements).

Total non-empty subsequences is 2^n -1.

The number of subsequences that include all c elements is the number of non-empty subsets that contain all c elements. Let's call this A_total. So B = (2^n -1) - A_total.

But how do we compute A_total?

But for the problem, we need not compute B directly. Instead, we can first compute A_total and its breakdown into s_p for p>=1, and then compute s_0 as (2^n-1) - sum_{p>=1} s_p.

So the crux of the problem is to compute the part A: the number of non-empty subsequences that include all c elements, and for each such subsequence, compute the minimal count of any element. Then, sum over all such subsequences grouped by their minimal count.

Now, how to compute this for part A.

The key is to model this with dynamic programming. Let's think about the elements in the array. Each element is a member of {1..c}.

We need to process each element in the array, and track for each possible count of each element, the minimal count among all elements.

But with c up to 3000, this seems challenging.

Alternative approach: Since all elements in the array are between 1 and c, and the problem is to consider subsequences that include all c elements, perhaps we can model the problem for each element's count.

Let me think of it as follows: For a subsequence to include all c elements, each element must appear at least once. Let's say that for each element x, the subsequence includes k_x occurrences of x. The minimal of k_x's is the p for this subsequence.

We need to count all possible combinations of k_x >=1 for each x, and compute the sum over all such combinations where the minimal k_x is p.

But how do we model this for the given array?

The array has multiple instances of each element. For example, for element x, the array may have m_x occurrences. So, for a subsequence to select t_x instances of x (t_x >=1), the number of ways is the product over x of C(m_x, t_x) for each x.

But the minimal t_x across all x is p. So, the problem is to compute for each p >=1, the sum over all possible combinations where each t_x >=1, and the minimal t_x is exactly p.

But this seems challenging, especially given that c can be up to 3000.

But perhaps we can model this with inclusion-exclusion. For each p, the number of combinations where each t_x >= p, and at least one t_x is exactly p, and all others are >=p.

Alternatively, the number of ways where all t_x >= p, minus the number of ways where all t_x >= p+1.

But wait, if the minimal t_x is exactly p, then all t_x >= p, and at least one t_x is p. So, the count for p is equal to the number of ways where all t_x >= p, multiplied by the inclusion-exclusion term for at least one being exactly p.

But maybe the inclusion-exclusion approach is not tractable for large c.

Alternative approach: For each element x, let's compute the number of ways to choose at least 1 occurrence of x, and for each possible count of x.

Then, for all elements, the minimal count across x is p. So for each p, we can compute the product of (sum_{t_x >=1} ways(x, t_x) for t_x >= p) minus the product of (sum_{t_x >=1} ways(x, t_x) for t_x >= p+1).

Wait, perhaps not. Let's think:

The number of ways where all elements x have at least p occurrences, and at least one element has exactly p occurrences. This can be calculated as:

total_p = (product_{x} (sum_{t >= p} ways(x, t))) - (product_{x} (sum_{t >= p+1} ways(x, t))))

But this is for the minimal count being exactly p.

Because the first term is the number of ways where all elements have at least p occurrences. The second term is the number of ways where all elements have at least p+1 occurrences. The difference between them is the number of ways where all elements have at least p occurrences, but not all have at least p+1. So this is exactly the number of subsequences where the minimal count is exactly p.

Thus, for part A, the number of subsequences with minimal count p is equal to:

(total_p) = product_{x} (S_x(p)) - product_{x} (S_x(p+1)), 

where S_x(p) is the number of ways to choose at least one occurrence of x, and exactly t_x >= p.

Wait, no. Because the product_{x} S_x(p) is the number of ways to choose for each x a t_x >=p (but in our problem, each t_x must be >=1, which is already handled by S_x(p) as p >=1). So, for example, if p=1, then S_x(1) is the number of ways to choose at least 1 occurrence of x (since t_x >=1). So product_{x} S_x(1) is the number of ways to choose at least one occurrence of each x. Then, product_{x} S_x(2) is the number of ways to choose at least two occurrences of each x. The difference between these two products is the number of subsequences where all x have at least 1 occurrence and the minimal count is exactly 1.

Similarly, for p=2, product_{x} S_x(2) - product_{x} S_x(3) is the number of subsequences where all x have at least 2 occurrences and the minimal count is exactly 2.

Thus, the count for each p is equal to the product for all x of S_x(p) minus the product for all x of S_x(p+1).

Therefore, the approach is:

For each p from 1 to max_p possible:

sum_p = (product_{x=1 to c} S_x(p)) - product_{x=1 to c} S_x(p+1).

Then, sum_p is the number of subsequences in part A where the minimal count is exactly p.

But how to compute S_x(p), which is the number of ways to choose at least p occurrences of x from its available occurrences.

But each x has m_x occurrences in the original array. For x to be present in the subsequence, we need to choose at least one occurrence. But in the product, for S_x(p), when p is 1, S_x(1) is 2^{m_x} -1 (number of non-empty subsets of x's occurrences). However, for S_x(p), where p >=1, it's the number of subsets of x's occurrences that have size >= p.

Wait, no. S_x(p) is the number of subsets of x's occurrences that have size >= p. Because in the product for sum_p, we are considering that each x has at least p occurrences. So, for each x, the number of ways to choose t_x >= p is S_x(p) = sum_{k=p}^{m_x} C(m_x, k).

But wait, the product for sum_p would require that each x has at least p occurrences, and the minimal count is exactly p. So, S_x(p) must be the number of subsets for x where the count is >= p.

So, for each x, the possible number of ways to choose t_x >= p is sum_{k=p}^{m_x} C(m_x, k).

But for x to have at least p occurrences, but possibly more.

Thus, the formula sum_p = product_{x} (sum_{k>=p} C(m_x, k)) ) - product_{x} (sum_{k >=p+1} C(m_x, k)) )

This gives the number of subsequences where all x have at least p occurrences, and at least one x has exactly p occurrences.

Thus, the problem is now to compute for each x, the prefix sums from p to m_x for C(m_x, k), for all p from 1 to m_x.

But since n can be up to 3000, and c up to 3000, this approach could be feasible if we can precompute the sum for each x and p.

So the steps are:

1. Precompute for each element x, the counts m_x (number of occurrences in the original array).

2. For each x, compute for all p >=1 the sum of combinations C(m_x, k) where k >=p. We can precompute these values using prefix sums for each x.

3. For each p >=1, compute the product of (sum_{k >=p} C(m_x, k)) for all x. Then, subtract the product of (sum_{k >=p+1} C(m_x, k)) for all x. The result is the number of subsequences where the minimal count is exactly p.

4. The sum over all p >=1 of these values is the total number of subsequences in part A (those that include all c elements). Then, the s_0 is (2^n -1) - sum_p (sum_p).

Thus, the crux is to compute the products for each p and then compute the differences.

Now, the challenge is to compute these sums efficiently.

First, we need to compute for each x, m_x is the number of occurrences of x in the original array. Then, for each x, precompute the sum of combinations for k >= p. For example, sum_p[x] is the sum of C(m_x, p) + C(m_x, p+1) + ... + C(m_x, m_x).

These can be precomputed for each x and for all possible p using dynamic programming. For each x, we can compute the suffix sums of the combination counts.

But for m_x up to 3000, and c up to 3000, precomputing for each x and p up to 3000 is feasible.

Once these suffix sums are precomputed, for each p, we can compute the product of sum_p[x] for all x. Then, the product for sum_{p+1} and subtract.

But how to compute the product for each p efficiently?

Let's note that the product over all x of sum_p[x] is needed for all possible p. So, for p from 1 to max_p, where max_p is the minimal m_x among all x (since if any x has m_x < p, sum_p[x] is zero, so the product becomes zero).

So, the maximal p we need to consider is the minimal m_x across all x. Because if there's any x with m_x < p, sum_p[x] is zero, and thus the product is zero. So for p > min(m_x), sum_p will be zero.

Thus, the possible p values are from 1 to min(m_x).

But if any x has m_x =0 (which can't happen here, since all x in the original array are between 1 and c. Wait, the problem states that the array is a c-array, so all elements are between 1 and c. So for all x in 1..c, m_x is at least zero. But if a x has m_x=0, then there's no way to include x in the subsequence, so part A is empty. But the problem statement's input guarantees that the array is a c-array, so all elements are between 1 and c. But some elements in 1..c may not appear in the array. For example, if c=3 and the array is [1,1,1], then m_2 and m_3 are zero. So, in this case, part A is zero, because no subsequence can include all elements (since 2 and 3 are not present in the array). So the sum for all p is zero.

But according to the model, part A is the number of subsequences that include all c elements. So, if any element x has m_x =0 in the array, then part A is zero, since there's no way to select at least one occurrence of x. So, in such cases, all s_p for p >=1 are zero, and s_0 is 2^n -1.

Thus, the algorithm must first check whether all c elements are present in the array. If not, then part A is zero, and all s_p for p >=1 are zero, and s_0 is 2^n-1.

Otherwise, proceed with the steps.

So, the first step is:

Check if any of the elements 1..c are not present in the array. If yes → part A is zero. So s_0 is 2^n-1, and all other s_p are zero.

But the problem's input array is a c-array, but not necessarily containing all elements. So, for example, if the array doesn't have all elements from 1..c, then part A is zero.

Thus, the first step is to check if the array contains all c elements. If not, then all non-empty subsequences are part B, so s_0 = 2^n -1, and other s_p =0.

But if the array contains all c elements, then proceed.

Now, for the case where all c elements are present (each m_x >=1).

We proceed to compute for each x, the suffix sums of combinations.

For each x in 1..c:

Compute for all p >=1, the sum s_p[x] = sum_{k=p}^{m_x} C(m_x, k).

We can compute this using dynamic programming for each x:

For example, for x with m_x occurrences:

s_p[x] for p from 1 to m_x can be computed as s_{p+1}[x] + C(m_x, p).

So, starting from p = m_x, s_p[x] = C(m_x, p) when p = m_x. Then, for p = m_x-1, s_p[x] = C(m_x, p) + s_{p+1}[x].

This way, we can precompute all s_p[x] in O(m_x) time per x.

Once we have all s_p[x] for all x and p, the next step is to compute for each possible p (from 1 up to min(m_x)), the product of s_p[x] across all x.

But with c up to 3e3 and p up to 3e3, this could be O(c * p_max), which is manageable.

But how to compute the product for each p efficiently?

The product for p is product_{x} s_p[x]. For each p, we can loop through all x and multiply their s_p[x].

But for p up to 3e3 and c up to 3e3, this is O(3e3 * 3e3) = 9e6 operations, which is acceptable.

Once we have the product for p and p+1, we compute the difference, which is the count for p.

But wait, in this model, the count for p is the product of s_p[x] minus the product of s_{p+1}[x}.

But we need to compute this for all p >=1.

However, when p exceeds the minimal m_x, the product of s_p[x] will be zero (since at least one x has m_x < p). So, for p > minimal m_x, the product is zero.

So the steps are:

1. Compute for all x, m_x.

2. Check if any m_x ==0. If yes, part A is zero. So s_0 = 2^n -1, and others are zero.

3. Else, compute for each x and p, s_p[x] = sum_{k=p}^{m_x} C(m_x, k).

4. Compute the minimal m_x (call it min_m). For p up to min_m, compute the product for p and p+1.

5. For each p from 1 to min_m:

   a. Compute product_p = product of s_p[x] for all x.

   b. Compute product_p1 = product of s_{p+1}[x] for all x.

   c. sum_p = (product_p - product_p1) mod MOD.

   d. Add sum_p to s_p.

6. The remaining steps:

   a. s_0 = (2^n -1 - sum_{p >=1} sum_p) mod MOD.

   b. For p from min_m+1 to n, s_p =0.

Now, the problem is to compute combinations C(m_x, k) for all x and k up to m_x.

But since m_x can be up to 3e3 (since n is up to 3e3), and c up to 3e3, precomputing a combination table up to 3e3 is feasible.

So, precompute a combination table C(n, k) for n up to 3e3 and k up to n.

But in Python, this can be done using dynamic programming or using a precomputed table with factorials and modular inverses.

But the problem requires that all computations are done modulo 998244353.

Thus, the steps are:

- Precompute factorials and inverse factorials modulo 998244353 up to 3e3.

- Compute C(n, k) as fact[n] * inv_fact[k] * inv_fact[n-k] mod MOD, for n >=k.

But since m_x can be up to 3e3, and for each x, s_p[x] requires summing C(m_x, k) for k >=p up to m_x.

Thus, the precomputation of combination numbers can be done for each x and k up to m_x.

But for each x, we can compute the suffix sums of combinations as follows:

Compute for x, m_x, the array comb_x where comb_x[k] = C(m_x, k) for 0 <=k <=m_x.

Then, for p from m_x down to 0:

s_p[x] = comb_x[p] + s_p+1[x]

Thus, for each x, we can compute the suffix sums in O(m_x) time.

So, in code:

For each x in 1..c:

   m = m_x

   compute comb = [0]*(m+1)

   for k in 0..m:

       comb[k] = C(m, k)

   compute s_p[x] for p from 0 to m:

       s_p[x] = sum_{k=p}^m comb[k]

   This can be done with a reverse loop:

       suffix = 0

       for p in range(m, -1, -1):

           suffix += comb[p]

           s_p[x][p] = suffix

But since for the problem, we need sum from k=p to m_x of comb[k], this can be computed.

Once we have the s_p[x] for all x, then for each p, we compute the product of s_p[x] for all x, and the product for p+1.

But to compute the product for all x, we can loop through each x and multiply the current product.

But for each p, the product is the product of s_p[x] for all x. However, if any s_p[x] is zero, then the product is zero.

But for x with m_x >= p, s_p[x] is non-zero (assuming x is present in the array).

But in the case where x's m_x >= p, s_p[x] is sum_{k=p}^{m_x} C(m_x, k). But if x is part of the array, and the array contains all c elements, then m_x >=1. So for p=1, s_p[x] is sum_{k=1}^m_x C(m_x, k) = 2^m_x -1.

But when p exceeds m_x, s_p[x] is zero.

So, for p <= min_m, where min_m is the minimal m_x, then for all x, m_x >= p, so s_p[x] is non-zero.

Thus, for p up to min_m, all x have s_p[x] >=1.

So, the code steps:

Compute all s_p[x] for x in 1..c, p up to m_x.

Compute min_m = min(m_x for x in 1..c)

For p from 1 to min_m:

   product_p = 1

   for x in 1..c:

       if p > m_x:

           product_p = 0

           break

       product_p = product_p * s_p[x] % MOD

   product_p1 = 1

   for x in 1..c:

       if p+1 > m_x:

           product_p1 = 0

           break

       product_p1 = product_p1 * s_{p+1}[x] % MOD

   sum_p = (product_p - product_p1) % MOD

   s[p] += sum_p

But this would be O(c) per p. For p up to 3e3, and c up to 3e3, this is O(3e3 * 3e3) = 9e6 operations.

This should be manageable.

But to optimize, precompute for each x the s_p[x] for all p up to m_x, and then for each p, loop through all x and multiply.

But for each x, m_x can be up to 3e3, so for each p up to 3e3, we can precompute s_p[x].

Thus, the code outline is:

Read n, c.

Read the array a.

Compute m_x for each x in 1..c.

Check if any x has m_x =0. If yes:

   total = pow(2, n, MOD) -1

   s = [0]*(n+1)

   s[0] = total

   print s[0], s[1], ..., s[n]

Else:

   Precompute combination numbers C(m_x, k) for all x and k.

   For each x:

       compute m = m_x

       compute comb = [C(m, k) for k in 0..m]

       compute s_p[x] for p from 0 to m:

           s_p[x][p] = sum_{k=p}^m comb[k]

   Compute min_m = min(m_x)

   precompute for each p from 1 to min_m:

       product_p = 1

       for x in 1..c:

           if p > m_x of x:

               product_p =0

               break

           product_p = product_p * s_p[x][p] % MOD

       product_p1 = 1

       for x in 1..c:

           if p+1 > m_x:

               product_p1 =0

               break

           product_p1 = product_p1 * s_p[x][p+1] % MOD

       sum_p = (product_p - product_p1) % MOD

       add sum_p to s[p]

   Compute total_A = sum(s[1..min_m])

   s_0 = (pow(2, n, MOD) -1 - total_A) % MOD

   create output array with s_0 followed by s[1], s[2], ..., s[n], filling 0 for p > min_m.

Now, the main steps are:

- Precompute the combination numbers for each x's count.

- Precompute the suffix sums for each x.

- Compute the products for each p and p+1.

Now, the key challenge is to precompute the combinations efficiently.

But in Python, for small m_x (up to 3e3), we can compute combinations using dynamic programming.

Alternatively, precompute factorials and inverse factorials up to 3e3, and compute C(n, k) as fact[n] * inv_fact[k] * inv_fact[n-k] mod MOD.

This is feasible.

So, let's code this.

First, precompute factorials and inverse factorials up to 3e3.

MOD = 998244353

max_n = 3000

fact = [1]*(max_n+1)

for i in range(1, max_n+1):

    fact[i] = fact[i-1] * i % MOD

inv_fact = [1]*(max_n+1)

inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)

for i in range(max_n-1, -1, -1):

    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def comb(n, k):

    if k <0 or k >n:

        return 0

    return fact[n] * inv_fact[k] % MOD * inv_fact[n -k] % MOD

But for each x with m_x occurrences, compute for all k from 0 to m_x.

Then, compute the suffix sums.

Thus, for each x, the steps are:

m = m_x

s_p_for_x = [0]*(m+2)  # up to m+1 to handle p+1

suffix = 0

for p in range(m, -1, -1):

    suffix += comb(m, p)

    suffix %= MOD

    s_p_for_x[p] = suffix

But for p >=1, since the problem requires p >=1, but for x with m_x >=1, the suffix for p=1 is sum_{k=1}^m_x C(m_x, k) = 2^m_x -1.

So, for each x, we can precompute the suffix sums.

Once this is done, for each p from 1 to min_m, compute the product of s_p[x][p] for all x, and the product of s_p[x][p+1] for all x.

If any x has m_x < p, then s_p[x][p] is zero, so the product is zero. But since min_m is the minimal m_x, for p <= min_m, all x have m_x >= p, so s_p[x][p] is non-zero.

Wait, no. For example, if min_m is 2 (the minimal m_x is 2), then for p=2, all x have m_x >=2. But for p=3, which is larger than min_m, there's x with m_x=2, so the product for p=3 is zero.

But in the code, after checking that all x have m_x >=1 (part A is possible), and min_m is the minimal m_x, then for p from 1 to min_m:

   product_p is product of s_p[x][p] for all x.

   since x's m_x >= min_m >= p, so s_p[x][p] is sum_{k=p}^m_x C(m_x, k) >= C(m_x, p) >= C(p, p) =1.

   So product_p is the product of these values.

For p+1, if p+1 exceeds some x's m_x, then product_p1 is zero. But when p ranges from 1 to min_m, then p+1 can exceed min_m only when p=min_m, since p can be up to min_m. For p=min_m, p+1 would be min_m+1, which exceeds x's m_x with m_x=min_m. Thus, product_p1 is zero. So sum_p for p=min_m is product_p -0 = product_p.

Thus, for each p, sum_p is computed as the difference.

Thus, this approach is correct.

Now, let's code this.

So, putting it all together:

Read n and c.

Read the array a.

Compute m_x for each x from 1 to c. If any x has m_x ==0, then part A is zero. So output is s_0 = (2^n -1) mod MOD, and others zero.

Otherwise:

Compute min_m = min(m_x)

Precompute for each x in 1..c:

   m = m_x

   compute s_p[x] for p from 0 to m.

   This can be done by precomputing the suffix sums.

Once all s_p[x] are computed.

For each p from 1 to min_m:

   product_p = 1

   for x in 1..c:

       product_p = product_p * s_p[x][p] % MOD

   product_p1 = 1

   for x in 1..c:

       if (p+1) > m_x[x]:

           product_p1 = 0

           break

       product_p1 = product_p1 * s_p[x][p+1] % MOD

   sum_p = (product_p - product_p1) % MOD

   s[p] += sum_p

Compute total = sum(s[1..min_m])

s_0 = (pow(2, n, MOD) -1 - total) % MOD

Finally, output s_0, s_1, ..., s_n. For p > min_m, s_p is zero.

Thus, the code will look like this.

But to handle the elements, we need to count m_x for each x in 1..c.

Now, let's test this with the sample inputs.

Sample input 1:

4 1

1 1 1 1

m_x for 1 is 4. All other x's (if any) have m_x=0, but c=1.

Wait, c=1. So all elements are 1. So m_x[1] =4. All x in 1..1 have m_x=4. So no x has m_x=0. So proceed.

min_m =4.

For p from 1 to 4.

For p=1:

product_p = product of s_p[x][1} for x=1.

s_p[x=1][1} is sum_{k=1}^4 C(4, k) = 15.

product_p =15.

product_p1 = product of s_p[x][2} for x=1.

s_p[x=1][2} is sum_{k=2}^4 C(4,k) = 11.

product_p1 =11.

sum_p =15 -11=4. But this is for p=1.

Wait, but according to the first sample, the sum_p for p=1 should be C(4,1) =4, for p=2 C(4,2)=6, etc. But according to this model, the sum_p for p=1 is 15-11=4. Which is correct. For p=1, the number of subsequences is 4. Similarly, for p=2:

product_p is product of s_p[x][2} for x=1. sum_{k=2}^4 C(4,k) =11.

product_p1 = sum_{k=3}^4 C(4,k) = 5.

sum_p=11-5=6.

For p=3:

product_p=5, product_p1=1 (sum_{k=4}^4 C(4,4)=1).

sum_p=5-1=4.

For p=4:

product_p=1 (sum_{k=4}^4 C(4,4)=1), product_p1=0.

sum_p=1-0=1.

Thus, sum_p for p=1 to4 are 4,6,4,1. Which matches the first sample's s_1=4, s_2=6, s_3=4, s_4=1.

s_0 is (2^4-1 - (4+6+4+1)) = (15-15)=0. Which matches the sample.

Thus, this code should work.

Another sample input 3:

5 2

1 2 1 2 1

m_x for 1 is 3, for 2 is 2. min_m is 2.

For p=1:

product_p is s_p[1][1} * s_p[2][1}.

s_p[1][1} is sum_{k=1}^3 C(3,k) =7.

s_p[2][1} is sum_{k=1}^2 C(2,k) =3.

product_p =7*3=21.

product_p1 is sum_{k=2}^3 C(3,k) * sum_{k=2}^2 C(2,k) → (3+1) * 1 →4 *1=4.

sum_p=21-4=17.

For p=2:

product_p is sum_{k=2}^3 C(3, k) * sum_{k=2}^2 C(2,k) → (3+1) *1=4.

product_p1 is sum_{k=3}^3 C(3, k) * sum_{k=3}^2 C(2,k) →1 *0=0.

sum_p=4-0=4.

Thus, sum_p for p=1 is17, p=2 is4. Total is 21. s_0= (31-21)=10. Which matches the sample.

Thus, the code should work.

Now, the code:

We need to:

- Read the array and count m_x for each x.

- Check if any x in 1..c has m_x=0.

- If not, proceed.

- Precompute s_p[x] for each x.

- Compute the products for each p.

Now, code:

MOD = 998244353

n, c = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

m_x = defaultdict(int)
for num in a:
    m_x[num] +=1

# Check if all elements 1..c are present
missing = False
for x in range(1, c+1):
    if m_x.get(x, 0) ==0:
        missing = True
        break

if missing:
    total = (pow(2, n, MOD) -1) % MOD
    output = [0]*(n+1)
    output[0] = total
    print(' '.join(map(str, output)))
else:
    # Precompute factorial and inverse factorial up to max(m_x)
    max_m = max(m_x.values())
    max_fact = max_m

    fact = [1]*(max_fact+1)
    for i in range(1, max_fact+1):
        fact[i] = fact[i-1] * i % MOD

    inv_fact = [1]*(max_fact+1)
    inv_fact[max_fact] = pow(fact[max_fact], MOD-2, MOD)
    for i in range(max_fact-1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

    def comb(n, k):
        if k <0 or k >n:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n -k] % MOD

    # Precompute s_p[x] for each x
    s_p = dict()  # x: list of s_p[x] from 0 to m_x[x]

    for x in range(1, c+1):
        m = m_x[x]
        s_p[x] = [0]*(m+2)  # 0..m+1
        suffix =0
        for p in range(m, -1, -1):
            suffix += comb(m, p)
            suffix %= MOD
            s_p[x][p] = suffix

    min_m = min(m_x.values())

    s = [0]*(n+2)  # up to n+1

    for p in range(1, min_m +1):
        product_p =1
        for x in range(1, c+1):
            product_p = product_p * s_p[x][p] % MOD

        # compute product_p1 for p+1
        product_p1 =1
        for x in range(1, c+1):
            if (p+1) > m_x[x]:
                product_p1 =0
                break
            product_p1 = product_p1 * s_p[x][p+1] % MOD

        sum_p = (product_p - product_p1) % MOD
        if sum_p <0:
            sum_p += MOD
        s[p] = sum_p

    total_A =0
    for p in range(1, min_m +1):
        total_A = (total_A + s[p]) % MOD

    s0 = (pow(2, n, MOD) -1 - total_A) % MOD
    if s0 <0:
        s0 += MOD

    output = [0]*(n+1)
    output[0] = s0
    for p in range(1, min_m +1):
        output[p] = s[p]
    for p in range(min_m +1, n+1):
        output[p] =0

    print(' '.join(map(str, output)))

This code should handle all cases correctly.

Let's test for the second sample:

Input: 3 3

1 2 3

m_x for 1, 2,3 are 1,1,1. min_m=1.

For p=1:

product_p = (sum_{k=1}^1 C(1,1))^3 = (1)^3 =1.

product_p1 = sum_{k=2}^1 C(1, k) for all x →0. So product_p1=0.

sum_p=1-0=1.

So s[1] =1.

s0= (2^3-1 -1) =7-1=6.

Which matches the sample.

Thus, the code should work.
</think>

```python
MOD = 998244353

n, c = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

m_x = defaultdict(int)
for num in a:
    m_x[num] += 1

missing = False
for x in range(1, c + 1):
    if m_x.get(x, 0) == 0:
        missing = True
        break

if missing:
    total = (pow(2, n, MOD) - 1) % MOD
    output = [0] * (n + 1)
    output[0] = total
    print(' '.join(map(str, output)))
else:
    max_m = max(m_x.values())
    max_fact = max_m

    fact = [1] * (max_fact + 1)
    for i in range(1, max_fact + 1):
        fact[i] = fact[i-1] * i % MOD

    inv_fact = [1] * (max_fact + 1)
    inv_fact[max_fact] = pow(fact[max_fact], MOD-2, MOD)
    for i in range(max_fact -1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

    s_p = {}
    for x in range(1, c + 1):
        m = m_x[x]
        s_p[x] = [0] * (m + 2)
        suffix = 0
        for p in range(m, -1, -1):
            suffix = (suffix + comb(m, p)) % MOD
            s_p[x][p] = suffix

    min_m = min(m_x.values())

    s = [0] * (n + 2)
    for p in range(1, min_m + 1):
        product_p = 1
        for x in range(1, c + 1):
            product_p = product_p * s_p[x][p] % MOD

        product_p1 = 1
        for x in range(1, c + 1):
            if (p + 1) > m_x[x]:
                product_p1 = 0
                break
            product_p1 = product_p1 * s_p[x][p + 1] % MOD

        sum_p = (product_p - product_p1) % MOD
        if sum_p < 0:
            sum_p += MOD
        s[p] = sum_p

    total_A = 0
    for p in range(1, min_m + 1):
        total_A = (total_A + s[p]) % MOD

    s0 = (pow(2, n, MOD) - 1 - total_A) % MOD
    if s0 < 0:
        s0 += MOD

    output = [0] * (n + 1)
    output[0] = s0
    for p in range(1, min_m + 1):
        output[p] = s[p]
    print(' '.join(map(str, output)))
```