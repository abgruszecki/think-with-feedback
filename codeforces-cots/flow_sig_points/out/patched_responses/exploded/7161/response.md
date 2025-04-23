<think>
Okay, let's try to understand this problem. So the problem is about finding the number of ways to cut prefixes and suffixes from each of the m permutations such that the remaining subarrays are the same across all permutations and are non-empty. The answer is the number of such possible common subarrays.

Hmm. So, the main idea is to find all possible sequences that can be formed by trimming some prefix and suffix from each permutation, and these sequences must be identical in all m permutations. Then, count how many distinct such sequences there are.

The key here is to find all possible subarrays that are common to all m permutations when trimmed appropriately. Each such subarray is a contiguous sequence in each permutation, possibly after removing some elements from the front and/or back.

Let me think about how to approach this. Since m can be up to 10 and n up to 1e5, we need an efficient way that's O(nm) time, maybe. Because anything more than that could be too slow.

Let's think about the structure of the permutations. For each permutation, the possible subarrays that can be formed by trimming are all the possible intervals. But checking all possible intervals across all permutations is not feasible. So we need a smarter approach.

Wait, but the common subarray across all permutations must exist as a contiguous block in each permutation. So, the problem reduces to finding all sequences S such that S appears as a contiguous subarray in every permutation. Then, the count of all such S (without considering their position in each permutation, but the actual elements) is the answer.

Wait, no. Because the same sequence S can appear in different positions in different permutations, but as long as each permutation can have some trimming to leave S as their subarray, then S is a valid candidate. So the problem is to find all possible sequences S that exist in each permutation as a contiguous subarray (possibly in different positions) and count how many such S there are.

But how do we find all such S efficiently?

Alternatively, for each permutation, the possible subarrays are all possible intervals. But the intersection of all these sets (for all permutations) is the answer. But the number of possible subarrays is O(n^2) for each permutation, which is way too big for n=1e5.

So we need a different approach. Let's think about the positions of elements in each permutation.

Wait, perhaps the common subarray across all permutations must be a sequence where the order of elements is the same in all permutations. But that's not necessarily the case. For example, in the first example, the permutations are [1,2,3] and [2,3,1]. The possible common subarrays are [1], [2], [3], and [2,3]. The first permutation has [2,3] as a subarray, but the second permutation's subarray is [2,3], which is the same. So the order matters. So the subarray must be exactly the same sequence in all permutations.

So, the key is to find all possible contiguous sequences that appear in all permutations. But how?

An alternative approach is to model the problem as finding the intersection of all possible subarrays from each permutation. Since the permutations can vary, this seems challenging.

Wait, perhaps the approach is to find for each possible candidate sequence S, whether it exists as a contiguous subarray in all m permutations. But how to do this efficiently?

But given that m is up to 10, perhaps we can process each permutation's possible candidate sequences and find their intersection.

But even that seems impossible for large n. So we need a smarter way.

Another idea: the common subarrays must have their elements in the same order as in some permutation. Since each permutation is a permutation, the order in which elements appear in a subarray of a permutation is unique. So, for a subarray to be common to all permutations, the same sequence must appear as a contiguous subarray in every permutation. So, for example, if the sequence [2,3] exists in all permutations as a contiguous block, then it's a valid candidate.

So the problem reduces to finding all sequences S that are contiguous in every permutation. The number of such S is the answer.

But how to find all such S efficiently?

Hmm. Let's think about the first permutation. For each possible subarray S in the first permutation, check if S exists as a contiguous subarray in all other permutations. Then sum the count of such S.

But even that is O(n^2 * m) which is not feasible for n=1e5.

We need a way to compute this more efficiently.

Alternative approach: For each permutation, represent the positions of each element. For example, in permutation p, the position of element x is pos_p[x]. Then, a subarray in permutation 1 from index a to b is a sequence of elements. For this to be a contiguous subarray in permutation 2, the elements must form a consecutive block in permutation 2's position array.

Wait, perhaps not. Because the order in permutation 2's subarray must be the same. So, the elements in the subarray must appear in the same order as in permutation 1's subarray.

So, for a sequence [s_1, s_2, ..., s_k] to be a contiguous subarray in permutation p, the positions of s_1, s_2, ..., s_k must be consecutive and in the same order.

Wait, for example, permutation p is [2,3,1]. Then the subarray [3,1] is positions 1 and 2. The sequence is 3 followed by 1. So in another permutation, say [1,2,3], does this sequence exist as a contiguous subarray? No. But in the first example, the subarray [2,3] in the first permutation is present as the first two elements of the second permutation (since the second permutation is [2,3,1]). So in the second permutation, the positions of 2 and 3 are consecutive and in order.

So, the idea is: for the sequence S to be present as a contiguous subarray in permutation p, the positions of the elements of S in permutation p must form a consecutive range, and their order must match S's order.

Wait, but the order is determined by the permutation. So the elements of S must appear in exactly the same order in permutation p's subarray.

Therefore, for S to be a common subarray across all permutations, the elements of S must form a contiguous block in each permutation's position array, in the same order as S.

So, how to find such S?

An alternative approach is to find all possible sequences S that are common across all permutations. Let's first consider the first permutation and generate all possible S that could be candidates, then check if they are present in all other permutations.

But again, generating all possible S in the first permutation is O(n^2), which is impossible for n=1e5.

So, this approach won't work. Need a smarter idea.

Another thought: the maximum possible length of S is n. But for S to be present in all permutations, the order of elements in S must be the same in all permutations. But since each permutation is a permutation of the same elements, the only way a sequence S can be a contiguous block in all permutations is if S is a single element, or if S's elements form a contiguous block in the positions of all permutations.

Wait, no. Because in different permutations, the elements can be arranged in any order. So the sequence [2,3] exists in the first example in both permutations. How? Because in the first permutation, it's the first two elements, in the second permutation, it's the first two elements. So their positions are consecutive in each permutation, and in the same order.

But how can we model this?

Hmm. Let's think of the positions in each permutation. For each element x, we have in permutation j, the position is pos_j[x]. For a sequence S = [x1, x2, ..., xk], to be a contiguous subarray in permutation j, the positions of x1 in permutation j must be pos_j[x1], and x2's position is pos_j[x1]+1, and so on, up to xk's position being pos_j[x1] + k-1.

So for permutation j, the positions of the elements of S must form a consecutive increasing sequence with step 1, and their order must be exactly x1, x2, ..., xk.

Thus, for S to be a contiguous subarray in all permutations, for every permutation j, the positions of S's elements must form a consecutive sequence in j, starting at some start position s_j and ending at s_j + k-1, and the elements in this range must be exactly x1, x2, ..., xk in order.

So, the problem reduces to finding all possible sequences S that satisfy this condition for all permutations.

Now, the question is: how can we find all such S efficiently?

Let's consider the first permutation. For each possible starting index i and ending index j (i <= j), we can get the sequence S = permutation1[i..j]. Then, we need to check if this sequence appears as a contiguous subarray in all other permutations. But again, for n=1e5, this is O(n^2) which is impossible.

Alternative idea: The only possible sequences S that can be common to all permutations are those where, for each permutation j, the elements of S form a consecutive interval in permutation j's positions. So, for S to be a valid sequence, for each permutation j, the elements of S must appear in consecutive positions in permutation j, in the same order as S.

So, for example, if S is [x, y, z], then in permutation j, the positions of x, y, z must be consecutive and in the order x, y, z.

So, for S to be a valid sequence, all permutations must have their positions for the elements of S arranged in the same order, and consecutively.

Hmm. Let's model this for all permutations. Let's first pick a candidate sequence S. Then, for each permutation j, we need to check if the elements of S are in consecutive positions in permutation j, and in the correct order.

But how do we find all such S?

Alternative approach: For the first permutation, generate all possible candidate sequences S, and then for each S, check if it is present as a contiguous subarray in all other permutations.

But again, this is O(n^2) for the first permutation.

So, this approach is not feasible. Need another way.

Alternative idea inspired by the problem's constraints. Since m is up to 10, perhaps for each possible sequence S that is present in all permutations, we can find some way to model their positions.

Another approach: For each permutation, build a position map (pos_j[x] is the index of x in permutation j). Then, for any two elements x and y, in permutation j, if x comes immediately before y in some S, then in permutation j, pos_j[x] must be pos_j[y] - 1. But this must be true across all permutations.

Wait, but S is a sequence of elements. For S to appear as a contiguous subarray in all permutations, the elements in S must form a consecutive chain in all permutations, and the order of elements in S must be the same as their order in the first permutation.

Wait, perhaps this is a key insight. Let's think about the first permutation. For S to be a contiguous subarray in all permutations, the order of elements in S must be the same as in the first permutation, and in each permutation j, the elements of S must form a consecutive block in permutation j, in the same order as S.

But the order of elements in S in each permutation must be the same as in the first permutation's S. Because the sequence S must be the same in all permutations.

So, S is a sequence of elements in the order of the first permutation's subarray. Then, in permutation j, the elements must appear in that same order, consecutively.

So, the problem is to find all possible sequences S (from the first permutation's possible subarrays) such that in every other permutation j, the elements of S form a consecutive block in permutation j, and the order matches S's order (i.e., the first permutation's order of S).

So, how can we model this?

Let me think: For the first permutation, any possible contiguous subarray S is a candidate. For each such S, we need to check that in every other permutation j, the elements of S appear consecutively in the same order as in S.

But how to check this efficiently for all S?

Another idea: For each permutation j, create a 'position' array where pos_j[x] is the index of x in permutation j.

Now, for a sequence S = [a_1, a_2, ..., a_k], in permutation j, the positions must be pos_j[a_1], pos_j[a_2], ..., pos_j[a_k], and these must form consecutive integers in order (i.e., pos_j[a_1] = p, pos_j[a_2] = p+1, ..., pos_j[a_k] = p +k-1 for some p).

This implies that for all i from 1 to k-1, pos_j[a_{i+1}] must be pos_j[a_i] +1.

Additionally, for permutation j, the elements in the positions pos_j[a_1] ... pos_j[a_k] must exactly be the elements a_1, a_2, ..., a_k in order.

So, for a given S, for each permutation j, the following must hold:

pos_j[a_1] = pos_j[a_2] -1 = pos_j[a_3] -2 = ... = pos_j[a_k] - (k-1).

But how to find all such S across all permutations.

Hmm. Let's think in terms of the first permutation. For each possible S in the first permutation, check for all other permutations j whether the elements of S are consecutive in j, and in the same order.

But again, this is O(n^2 * m) which is not feasible.

Alternative approach: Let's find all possible possible sequences S that are such that for all permutations j, the elements of S form a consecutive run in j's permutation, and the order is the same as in the first permutation.

But how?

Let's model the problem as follows. For the sequence S to be a contiguous subarray in all permutations, the following must hold:

For any two consecutive elements x and y in S, in permutation j, the position of y must be exactly one more than the position of x. So, for all j, pos_j[y] = pos_j[x] +1.

If this holds for all consecutive pairs in S and all permutations j, then S is a valid candidate.

So, for each possible pair x and y in the first permutation, if in all other permutations j, the position of y is exactly one more than the position of x, then x and y can be consecutive in S. Then, the maximum possible S is the longest possible sequence where each consecutive pair in S satisfies this condition.

But how to model this.

Wait, but S is a contiguous subarray in the first permutation. So, for each possible contiguous subarray in the first permutation, we can check if all consecutive pairs in S satisfy this condition across all permutations.

But again, this is O(n^2 * m), which is not feasible.

Alternative idea: For each element x, precompute for each permutation j, the next element in the first permutation. For example, if in the first permutation, after x comes y, then in permutation j, the position of y must be pos_j[x]+1.

If this is true for all j, then x can be followed by y in S.

So, for S to be a possible sequence, every consecutive pair in S (as per the first permutation) must satisfy that in all other permutations j, the next element's position is exactly the current element's position plus 1.

This allows S to be a chain of elements where each step is valid across all permutations.

So, the problem reduces to finding all intervals in the first permutation where each consecutive pair in the interval has this property.

So, the approach would be:

1. For each permutation j (including the first), create a position array pos_j, where pos_j[x] is the index of x in permutation j.

2. For each consecutive pair (x, y) in the first permutation, check if for all j >= 2, pos_j[y] == pos_j[x] + 1.

3. If this is true, then x and y can be consecutive in some S.

4. The problem now reduces to finding all intervals in the first permutation where all consecutive pairs in the interval have this property.

Then, each such interval is a possible S, and the answer is the number of such intervals.

So, the steps are:

- For each consecutive pair in the first permutation, determine if they are consecutive in all other permutations.

- Then, find all possible intervals in the first permutation where each consecutive pair in the interval is valid (i.e., they are consecutive in all other permutations).

- The count of such intervals is the answer.

This approach is O(n*m) time, which is feasible because n is up to 1e5 and m up to 10, giving 1e6 operations.

Once we have the valid consecutive pairs, the problem becomes finding the number of intervals in the first permutation where all consecutive pairs in the interval are valid. This is equivalent to finding the number of intervals in a binary array where each position is 1 if the pair is valid, 0 otherwise. The intervals are those where all elements in the interval are 1.

Wait, but in the first permutation, the consecutive pairs are from (1,2), (2,3), ..., (n-1, n). For each i from 1 to n-1, we check if in all other permutations, the next element in the first permutation is indeed next in their permutation. Then, the valid intervals are those where all consecutive pairs in the interval are valid.

So, for example, if in the first permutation, the pairs (a1, a2), (a2, a3) are valid, then the interval [a1, a2, a3] is valid.

The number of such intervals is the sum over the lengths of consecutive runs of valid pairs. For example, a run of k consecutive valid pairs contributes k*(k+1)/2 intervals (since each run of k+1 elements forms k+1 intervals of length 1, k intervals of length 2, etc.).

Wait, no. Let's see. For example, if there are k consecutive valid pairs, this corresponds to a sequence of elements in the first permutation of length k+1. The number of intervals (contiguous subarrays) in this run is (k+1)*k/2.

Wait, but how? Let's say we have a sequence of elements where all consecutive pairs are valid. For example, elements 1, 2, 3, 4. The valid pairs are (1,2), (2,3), (3,4). Then, the possible intervals are all possible intervals of length 1, 2, 3, 4. The count is 4 (length 1) +3 (length 2) +2 (length3) +1 (length4) = 10. Which is (4*5)/2 = 10. So, yes, for a run of k valid pairs (k+1 elements), the number of intervals is (k+1)*(k+2)/2? Wait no, for k=3 pairs (4 elements), sum from 1 to 4 is 10. (4*5)/2=10. So for a run of k valid pairs (k+1 elements), the sum is (k+1)*(k+2)/2. Wait, no: 1+2+...+m = m(m+1)/2. So for m elements, it's m(m+1)/2. But here, the run is of k+1 elements. So the sum is (k+1)*(k+2)/2. But wait, 4 elements give 4*5/2=10. Which matches.

So, the idea is to split the array into runs of consecutive valid pairs. Each run of length L (number of valid pairs) corresponds to a segment of L+1 elements. For each such run, the number of intervals is (L+1)*(L+2)/2. Then, the total is the sum of these over all runs.

But wait, no. Because each run is a maximal sequence of consecutive valid pairs. So, for example, if there are three consecutive valid pairs, this forms a run of length 3 (since there are 3 pairs) and 4 elements. The number of possible intervals here is 4*5/2=10. But if the run is split into smaller segments, like if there's a break in the valid pairs, the sum would be for each individual run.

So, the approach is:

- Precompute for each consecutive pair in the first permutation whether it is valid (i.e., in all other permutations, the next element's position is current +1).

- Then, split the first permutation into runs where consecutive pairs are valid. For each such run of length L (number of valid pairs), the number of intervals is (L+1) * (L+2) // 2 / 2? Wait, no. Wait, for L consecutive valid pairs, the elements are L+1 in number. So the number of possible intervals in this block is (L+1)*(L+2)/2? Wait no. Wait, the number of possible intervals in a sequence of m elements is m*(m+1)/2. Because for each possible starting index i and ending index j >=i, the number is sum_{k=1 to m} (m -k +1) ) = m*(m+1)/2.

So for a run of L+1 elements, the number is (L+1)*(L+2)/2. So for each run of L valid pairs (L is the number of pairs, which is (number of elements) - 1), the number of intervals is (L+1)*(L+2)/2.

Wait, but let's take L as the number of valid pairs. So for example, if there are 3 valid pairs, then there are 4 elements. So the intervals are 4*5/2 =10. So yes, (L+1)*(L+2)/2.

But wait, no. Because 3 pairs correspond to 4 elements, which gives 4*5/2=10 intervals. But (3+1)*(3+2)/2 =4*5/2=10. Yes. So the formula holds.

So, the plan is:

1. For the first permutation, process each consecutive pair (a_i, a_{i+1}) for i from 0 to n-2 (assuming 0-based index).

2. For each such pair, check if in all other permutations j, the position of a_{i+1} in j's permutation is pos_j[a_i] +1.

3. Mark each pair as valid or invalid.

4. Then, split the array of consecutive pairs into runs of consecutive valid pairs. For each run of length L (number of pairs), the number of intervals contributed is (L+1)*(L+2)/2.

5. Sum all such contributions to get the total answer.

Wait, but what about single-element intervals? Because even a single element is allowed. For example, if all pairs are invalid, then each single element is a valid interval. So in that case, the answer would be n.

But according to the problem statement, the remaining part must be non-empty. So any interval of length >=1 is allowed, as long as all consecutive pairs in it are valid (but for a single element, there are no pairs, so it's automatically valid).

Wait, wait. The problem requires that after trimming, the remaining subarray is the same across all permutations. So each such subarray can be of any length >=1, but the way to form it is by trimming each permutation's prefix and suffix to leave exactly the subarray S.

So for a single-element S, for each permutation, S must exist as a contiguous subarray (i.e., the element must be present, which it is). So every single element is a valid candidate. But according to our approach, how would this be handled?

Because for a single element S, there are no consecutive pairs, so it's considered a run of zero valid pairs. Then, the number of intervals contributed is (0 +1) * (0 + 2)/2 = 1 * 2 /2 =1. So each single-element interval is accounted for.

Wait, no. Because in the approach above, the runs are sequences of valid pairs. So a single element (no pairs) would be a run of length 0 (if the previous pair is invalid). So each single element is part of a run of length 0.

Wait, perhaps not. Let's model this.

Suppose the array of valid pairs is a binary array of length n-1, where each entry is 1 if the pair is valid, 0 otherwise. Then, the runs of 1's in this array determine the possible intervals. But for single elements (with no adjacent pairs valid), they are considered as runs of 0's.

So, the approach of splitting into runs of 1's and then calculating the intervals within those runs would miss the single elements that are not part of any run. Therefore, the approach must account for all possible intervals, including single elements.

Wait, no. Because for each single element, since there are no pairs, the entire array of pairs is considered as a run of zero valid pairs. So, for the run of zero, the contribution is (0+1)*(0+2)/2 =1*2/2=1. So each single element would contribute one interval.

But how? Let's think of the example where all pairs are invalid. Then, the runs are all sequences of zeros. For example, if n=3, the pairs are (a0,a1) invalid, (a1,a2) invalid. Then, the array is [0, 0]. The runs of 0's are two separate runs? Or the entire array is a run of 0's? No. The runs are sequences of consecutive 0's. So, in this case, the array [0, 0] is a single run of 0's. But according to the code that processes runs, this run would have length 2 (number of pairs). Then, the contribution would be (2+1)*(2+2)/2 =3*4/2=6. But wait, in this case, all pairs are invalid. So the valid intervals are the three single elements (each is a valid interval). But according to the formula, it would return 6, which is incorrect.

So this suggests that the approach is not correct. So what's wrong here?

Ah! Oh right, because the runs of 1's (valid pairs) contribute the intervals where all pairs in the run are valid. But the single elements (with no pairs) would be considered as individual intervals. So the previous approach would not count them. So the initial approach is wrong.

Wait, no. Because the formula is designed for runs of consecutive valid pairs. So, in the case where there are no valid pairs, the code would not count any intervals. But according to the problem statement, single elements are valid.

So the problem with the initial approach is that it counts only intervals that are part of runs of valid pairs, but single elements (even when no pairs are valid) are also valid.

Therefore, the correct approach must account for all possible intervals, including single elements, even if they are not part of any valid run.

Wait, but according to our earlier model, a single element is a valid interval. Because it can be formed by trimming to just that element. Since all permutations contain that element as a contiguous subarray (they are permutations, so every element is present, so any single element is trivially a contiguous subarray in each permutation).

Wait, that's right! So any single element is automatically a valid candidate. Because each permutation contains that element as a contiguous subarray (since it's part of the permutation). So the problem statement's answer includes all possible single elements (n possible), plus all possible longer sequences that are contiguous in all permutations.

But according to the initial approach, these single elements would not be counted. So that approach is wrong.

So, what's the mistake here?

Ah! Because the initial approach considers that for a sequence S of length 1, there are no consecutive pairs. So, the code would not check any pairs for validity. But according to the problem statement, any single element is a valid S.

But how to model this in the code.

The answer is that the initial approach must account for all single elements, plus any longer sequences where all consecutive pairs are valid.

So, the total answer is the sum of all the valid intervals in the runs (as computed before) plus the number of single elements. But no, because the valid intervals in the runs already include the single elements. For example, a run of k valid pairs (k+1 elements) contributes (k+1)*(k+2)/2 intervals, which includes all possible subintervals, including the single elements.

Wait, yes. For a run of k valid pairs (k+1 elements), the number of intervals is (k+1)(k+2)/2. For example, if k=0 (a single element), then (0+1)(0+2)/2 =1*2/2=1, which is correct (only the single element). If k=1 (two elements with a valid pair), then the number is 2*3/2=3, which includes the two single elements and the pair. So the formula correctly accounts for all possible intervals in the runs, including the single elements.

But in the case where all pairs are invalid, the runs are sequences of 0's, and the code would not count any intervals from those runs. But according to the problem statement, all single elements are valid. So the code would miss those.

So the initial approach is incorrect. So what's wrong here?

Ah, because the runs of 0's (invalid pairs) are not considered. So the code must account for single elements in any case. So, the correct approach is to sum:

sum over all runs of valid pairs of (L+1)*(L+2)/2) + sum over all elements that are not part of any valid run (i.e., single elements that are not part of any run with valid pairs).

Wait, no. Because even if an element is part of a run of valid pairs, it's counted in the run's contribution. But for elements not part of any run (i.e., between two invalid pairs), they are single elements and need to be counted.

Wait, this is getting complicated. Let's think of the binary array of valid pairs. For example:

If the array is [0,0,0], then for each element in the first permutation, there are no valid pairs. So each element is a valid interval. So the answer would be 3.

But according to the initial approach (summing runs of valid pairs), since there are no 1's in the array, the sum is zero. Then adding the single elements.

So, the correct approach is to:

1. Find all intervals where all consecutive pairs are valid (summing the runs as before).

2. Plus, count the number of elements that are not part of any such intervals. Wait, no. Because every element is part of some interval of length 1. So perhaps the initial approach is wrong, and the correct answer is the sum of all runs' contributions plus the sum of all elements not covered by any runs.

But that's not possible. Because even if an element is not part of any run of valid pairs, it's still a single-element interval and must be counted.

So, perhaps the initial approach is missing the fact that single elements are always valid. So the answer is the sum from the runs plus the number of single elements. Wait, no. Because the runs already include the single elements.

Wait, the problem is that in the case of a run of invalid pairs, the elements are not part of any valid run. So each element can be considered as a valid interval of length 1. So the answer should be the sum from runs of valid pairs plus the number of elements that are not part of any valid run.

But how to compute that.

Alternatively, every element is allowed as a valid interval of length 1. Because in any permutation, any single element is a contiguous subarray. So the answer is n plus the sum of (L+1)(L+2)/2 - (L+1) for each run of L valid pairs. Because the runs contribute (L+1)(L+2)/2 intervals, which includes all lengths from 1 to L+1. But the single elements are already counted in the runs, so adding n would be double-counting.

Wait, perhaps the initial approach is incorrect. Because for any single element, it's allowed as a valid interval. So the answer is the number of valid intervals (including single elements) plus the number of elements that are not part of any valid interval. No, that's not right.

Wait, perhaps the correct approach is to realize that all possible intervals in the first permutation where all consecutive pairs are valid are valid candidates. But also, all single elements are valid candidates.

But no, because the problem requires that the sequence S is a contiguous subarray in all permutations. So for a single element, this is automatically true. So every single element is a valid candidate. So the answer should include n (the number of single elements) plus the number of longer sequences that are contiguous in all permutations.

But according to the initial approach, the sum from runs is already including all possible intervals (including single elements) where all consecutive pairs are valid. But in the case where a single element has no valid pairs (neither before nor after it), then it is counted in the runs as a single run of zero pairs (but according to the formula, this contributes 1 interval). But for the code, the runs are only sequences of 1's (valid pairs). So how can this be handled?

Alternatively, perhaps the code should process the binary array of valid pairs and split it into runs of 1's and 0's. Then, for each run of 1's, compute the number of intervals as (L+1)*(L+2)/2. Additionally, for runs of 0's, each element in the run contributes 1 (the single-element interval).

But how to model this.

Wait, the binary array is a list of 0's and 1's. Each 1 represents a valid pair, and a 0 represents an invalid pair.

The runs of 1's correspond to consecutive valid pairs. For each such run of length L (number of 1's), there are L+1 elements, and the number of intervals in that run is (L+1)*(L+2)/2. This includes all possible intervals in that run.

The runs of 0's correspond to consecutive invalid pairs. For each such run of length K (number of 0's), the elements are K+1. For each element in this run, it can be a single-element interval. So the contribution is K+1.

So the total answer is the sum over all runs of 1's (each contributing (L+1)(L+2)/2) plus the sum over all runs of 0's (each contributing K+1).

But wait, why? Because in a run of 0's, all pairs are invalid. So any interval longer than 1 would have at least one invalid pair. Thus, the only valid intervals are the single elements. So for a run of K+1 elements (K 0's), the number of valid intervals is K+1.

So the correct approach is:

- Split the binary array (of valid pairs) into runs of 1's and 0's.

- For each run of 1's of length L (number of 1's), add (L+1)*(L+2)/2 to the answer.

- For each run of 0's of length K (number of 0's), add K+1 to the answer.

So this way, all single elements are accounted for, whether they are part of a run of 1's or 0's.

But let's test this against the examples.

First example:

Input:
3 2
1 2 3
2 3 1

First permutation is [1,2,3]. Check consecutive pairs (1,2) and (2,3).

For pair (1,2):

Check in permutation 2: pos_2[1] is 2 (0-based?), since permutation 2 is [2,3,1]. So pos_2[1] is 2. pos_2[2] is 0. So 0+1 is 1, which is not equal to pos_2[1] (2). So the pair (1,2) is invalid.

For pair (2,3):

In permutation 2, pos_2[2] is 0, pos_2[3] is 1. So 0+1 =1 == pos_2[3], so valid.

So the binary array is [0, 1].

Runs of 1's: a single run of length 1 (the second pair is valid).

So contribution from 1's: (1+1)*(1+2)/2 =2*3/2=3.

Runs of 0's: first run is of length 1 (the first pair is invalid). So contribution is 1+1=2 (since K=1, K+1=2).

But wait, the binary array is [0,1]. So the runs are:

Run 0: starts at 0, length 1.

Run 1: starts at 1, length 1.

So sum from 1's run: (1+1)*(1+2)/2 =3.

Sum from 0's run: 1+1=2 (since K=1, K+1=2).

Total is 3+2=5. But the correct answer for the first example is 4. So this suggests a problem.

Wait, but the first example's answer is 4. According to this approach, the sum would be 3+2=5, which is incorrect. So where is the mistake?

Ah, because the binary array for the first example is [0,1]. The runs are:

- run of 0's of length 1 (K=1): contributes 2 (K+1 =2).

- run of 1's of length 1: contributes 3.

Total 5. But the correct answer is 4. So this approach is wrong.

But why?

Let's look at the first example's permutations. The correct answer includes [1], [2], [3], [2,3]. So four options.

According to the approach:

The runs of 0's contribute 2 (the first two elements [1,2], which are in a run of 0's. Wait, the binary array is [0,1]. The first run is a 0 (pair (1,2) invalid), which has K=1 (number of 0's), so the run contributes K+1=2 (elements 1 and 2). Then the run of 1's (pair (2,3) valid) contributes (1+1)*(1+2)/2=3 (intervals [2], [3], [2,3]). The sum is 2+3=5. But according to the problem statement, the correct answer is 4.

So this approach is overcounting. The problem is that the run of 0's includes elements 1 and 2. But each of these can be a single-element interval (which is allowed). But when K=1 (run of 0's of length 1), K+1=2 (elements 1 and 2). But in reality, these elements are part of a run where the pair between them is invalid. So each of them is a valid single-element interval. So the contribution from this run should be 2 (elements 1 and 2). The run of 1's contributes 3 intervals (2,3, [2,3]). So total 2+3=5, but the correct answer is 4. What's wrong here?

Ah! Because the pair (1,2) is invalid. So the elements 1 and 2 cannot form a pair. But the run of 0's includes the elements 1 and 2. So the code counts them as two single-element intervals. Then, in the run of 1's (pair 2-3), the intervals are 2, 3, and 2-3. So total 2+3=5. But according to the problem statement, the answer is 4. What's the discrepancy?

Wait, the correct answer for the first example is 4. The valid intervals are [1], [2], [3], [2,3]. So according to the code's approach, it would count [1] (from the 0's run), [2] (from the 0's run?), [3] (from the 1's run), [2], [3], and [2,3]. So why does the code's approach give 5?

Because the code's approach for the 0's run (pair (1,2) invalid) gives K+1=2, which is the elements 1 and 2. But according to the problem statement, 1 is a valid interval, 2 is a valid interval, but 3 is also a valid interval. So the code's approach counts 2 (from 0's run) +3 (from 1's run) =5. But according to the problem statement, there are 4 valid intervals. So why?

Because in the first permutation, the elements are [1,2,3]. The intervals are:

- [1] (valid).

- [2] (valid).

- [3] (valid).

- [2,3] (valid).

Total 4.

But according to the code's approach, the 0's run contributes 2 elements (1 and 2), and the 1's run contributes 3 elements (2,3, and [2,3]). But the element 2 is counted in both runs. For example, the run of 0's contributes 1 and 2 as single elements, but the run of 1's includes 2 as part of the pair (2,3) valid. So in the code's approach, the element 2 is counted in both the 0's run and the 1's run. This leads to an overcount.

Ah, this is the mistake. The code's approach is counting overlapping intervals. So when the runs are split, elements can be counted multiple times.

For example, the element 2 is part of both the 0's run and the 1's run. But in reality, the element 2 is a single-element interval, which is counted once. But the code's approach would count it once as part of the 0's run and once as part of the 1's run. So the code is double-counting.

So the initial approach is incorrect.

So how to correctly model this.

The problem arises because the code's approach splits the array into runs of 0's and 1's, but elements at the boundary of a run of 0's and 1's are counted in both runs.

For example, the first example's runs are:

- 0's run: elements 1 and 2 (since the first pair is invalid).

- 1's run: elements 2 and 3 (since the second pair is valid).

So the element 2 is part of both runs. The code's approach counts element 2 once in the 0's run (as a single-element interval) and once in the 1's run (as part of the single-element intervals and the pair). So in total, element 2 is counted twice. But according to the problem, each element can be a valid single-element interval once.

So the approach is incorrect because it allows overlapping intervals.

Thus, the correct way to model this is to split the array of pairs into runs of consecutive 1's and 0's, and ensure that each element is only counted once.

But how?

Alternative approach: For each element, the maximum possible run it can be part of as a single element is 1. But how to split the elements into non-overlapping runs.

Wait, perhaps the correct way is to model the runs of 0's and 1's, and for the runs of 0's, each element is a single-element interval, and for the runs of 1's, the intervals are computed as before.

But the runs are in the pairs. So the runs of 0's (invalid pairs) are sequences of consecutive 0's. Each 0 in the pair array corresponds to two elements (i and i+1) that are not a valid consecutive pair.

So for example, a run of K 0's in the pair array corresponds to K+1 elements. Each of these elements is part of a run of 0's, but the elements may overlap with other runs.

But this is not possible, since the runs are consecutive in the pair array.

So, a run of K 0's in the pair array corresponds to K+1 elements, which is a sequence of elements where all K pairs between consecutive elements are invalid. So each element in this sequence is a single-element interval.

But the code's approach would count all K+1 elements as part of the run of 0's, contributing K+1 to the answer.

But when the runs of 0's are followed by runs of 1's, the elements at the boundary are only part of the 0's run. For example, in the first example's pair array [0,1], the first run of 0's is one element (pair 0) corresponds to elements 1 and 2. The next run is one 1 (pair 1) corresponds to elements 2 and 3. So elements 2 is part of both runs. But according to the code's approach, the run of 0's contributes 2 (elements 1 and 2), and the run of 1's contributes 3 (elements 2, 3, and [2,3]). So element 2 is counted in both.

But according to the problem statement, the single-element intervals are allowed, but they should be counted once.

So this approach leads to double-counting.

Thus, the code's approach is incorrect.

Alternative idea: The correct way to count the valid intervals is:

- All single elements are valid. So there are n valid intervals.

- Additionally, all longer intervals (>=2 elements) where all consecutive pairs are valid.

So, the answer is n + sum over all possible intervals of length >=2 where all consecutive pairs are valid.

But how to compute the sum over all possible intervals of length >=2.

But the initial approach's sum for runs of 1's gives the number of intervals of any length (including single elements). So perhaps the correct approach is to compute the sum from runs of 1's (which counts all intervals in those runs), subtract the number of single elements in those runs (since they are already counted in the n), then add n.

But this seems complicated.

Alternatively, the initial approach is incorrect because it counts single elements in both runs of 0's and 1's. So to correctly compute the answer:

- The number of valid intervals is the sum of:

   a) n (all single elements).

   b) the number of intervals of length >=2 in the runs of valid pairs.

So, the sum of a) is n.

The sum of b) is for each run of L valid pairs (length L+1 elements), the number of intervals of length >=2. Which is (L+1)*(L+2)/2 - (L+1) = (L+1)*L/2.

For example, for a run of L=1 (two elements), the intervals of length >=2 is 1 (the pair). So (2*3/2) - 2 =3-2=1.

So for the first example, the run of 1 valid pair contributes 1 to part b. The sum a is 3, sum b is 1, total 4, which matches the correct answer.

Yes! So the correct approach is:

answer = n + sum over all runs of valid pairs of (L * (L+1) ) // 2.

Because for each run of L valid pairs (which corresponds to L+1 elements), the number of intervals of length >=2 is the total intervals ( (L+1)(L+2)/2 ) minus the number of single elements (L+1 ), which equals ( (L+1)(L+2)/2 ) - (L+1) ) = (L+1)( (L+2)/2 -1 ) = (L+1)( L / 2 ) = L(L+1)/2.

So, the formula for part b is sum over all runs of L valid pairs: L*(L+1)/2.

The part a is n.

So the correct answer is n + sum of L*(L+1)/2 for each run of L valid pairs.

Testing this on the first example:

Part a: 3.

The run of valid pairs is L=1 (the second pair is valid).

Contribution to part b: 1*(1+1)/2=1.

Total 3 +1=4, which is correct.

Another example: when all pairs are invalid. Then, part a is n, part b is 0. So answer is n.

Another test case: the third example in the problem.

Input:

2 2

1 2

2 1

Output: 2.

For this case, the first permutation is [1,2]. Check the pair (1,2).

In permutation 2, pos_2[1] is 1, pos_2[2] is 0. So pos_2[2] is 0, which is not pos_2[1]+1. So the pair is invalid.

So, the valid pairs array is [0]. So part a is 2. There are no valid runs of pairs (L=0). So part b is 0. Total answer is 2, which matches the sample.

Another example: the second sample input, but let's not compute it here.

So the correct approach is:

- Compute the valid pairs array for the first permutation.

- Split into runs of 1's (valid pairs) and compute for each run the L (number of valid pairs in the run), and accumulate sum += L*(L+1)/2.

- The answer is n + sum.

So now, the steps are:

1. For the first permutation, compute the valid pairs (for each consecutive pair, check if in all other permutations, the next element is pos_j[x]+1).

2. Split the valid pairs array into runs of consecutive 1's.

3. For each run of length L, add L*(L+1)/2 to the sum.

4. The answer is n + sum.

This should give the correct count.

Now, the code:

First, read n and m.

Read m permutations. Then, for each permutation j, create a pos_j dictionary that maps elements to their indices.

For the first permutation, process each consecutive pair (a[i], a[i+1]) for i in 0 to n-2.

For each such pair, check for all j from 1 to m-1 if pos_j[a[i+1]] == pos_j[a[i]] +1.

If this is true for all j, then the pair is valid (mark as 1), else 0.

Once we have the valid_pairs array (list of 0's and 1's), split it into runs of 1's.

For each run, compute L (the length of the run, which is the number of consecutive 1's).

Sum += L*(L+1) // 2.

The answer is n + sum.

Yes, this should work.

Now, let's code this.

Read the input.

Read n and m.

Read m permutations. Each permutation is a list of integers.

Then, for each permutation j, create a dictionary pos[j] where pos[j][x] = index of x in permutation j.

Then, for the first permutation, process each consecutive pair.

valid_pairs = list()

for i in range(n-1):

    x = first_perm[i]

    y = first_perm[i+1]

    valid = True

    for j in range(1, m):

        if pos[j].get(y, -1) != pos[j].get(x, -2) +1:

            valid = False

            break

    if valid:

        valid_pairs.append(1)

    else:

        valid_pairs.append(0)

Then, split valid_pairs into runs of 1's.

current_run_length = 0

sum_runs =0

for bit in valid_pairs:

    if bit ==1:

        current_run_length +=1

    else:

        if current_run_length >0:

            sum_runs += current_run_length * (current_run_length +1) //2

            current_run_length =0

# after loop, check if there's a run left

if current_run_length >0:

    sum_runs += current_run_length * (current_run_length +1) //2

answer = n + sum_runs

print(answer)

Yes.

Let's test this against the first example:

Sample input:

3 2

1 2 3

2 3 1

valid_pairs for first permutation:

Pair 1-2: check in permutation 2 (indexes 0-based):

pos_j[1] in permutation 2 is 2.

pos_j[2] is 0. 0 +1 is 1 != 2. So pair is invalid. valid_pairs[0] =0.

Pair 2-3: pos_j[2] is 0, pos_j[3] is 1. 0+1=1 ==1. So valid_pairs[1] =1.

valid_pairs is [0, 1].

sum_runs is processed:

The first element is 0: current_run_length remains 0.

Second element is 1: current_run_length becomes 1. Loop ends, and after processing, current_run_length is 1.

sum_runs += 1*2//2=1.

answer =3 +1=4. Correct.

Another test case:

Input:

2 2

1 2

2 1

valid_pairs for first permutation:

Pair 1-2: in permutation 2, pos_j[1] is 1, pos_j[2] is 0. 0+1=1 !=1. So valid_pairs is [0].

sum_runs is 0.

answer =2 +0=2.

Correct.

Another test case where all pairs are valid. For example:

n=3, m=1. Then, since m=1, all pairs are valid.

valid_pairs is [1,1].

sum_runs is (2 *3)//2=3.

answer is3 +3=6.

Which would be all possible intervals: 3 single elements, 2 pairs, 1 triplet. Total 6, which is correct.

Thus, this approach should work.
</think>

```python
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    perms = []
    for _ in range(m):
        perm = list(map(int, sys.stdin.readline().split()))
        perms.append(perm)
    
    # Precompute positions for each permutation
    pos = [dict() for _ in range(m)]
    for j in range(m):
        for idx, x in enumerate(perms[j]):
            pos[j][x] = idx
    
    if m == 1:
        # All possible single elements and their intervals
        print(n * (n + 1) // 2)
        return
    
    first_perm = perms[0]
    valid_pairs = []
    
    for i in range(n - 1):
        x = first_perm[i]
        y = first_perm[i + 1]
        valid = True
        for j in range(1, m):
            px = pos[j].get(x, -1)
            py = pos[j].get(y, -1)
            if py != px + 1:
                valid = False
                break
        valid_pairs.append(1 if valid else 0)
    
    sum_runs = 0
    current_run = 0
    for bit in valid_pairs:
        if bit:
            current_run += 1
        else:
            if current_run > 0:
                sum_runs += current_run * (current_run + 1) // 2
                current_run = 0
    if current_run > 0:
        sum_runs += current_run * (current_run + 1) // 2
    
    answer = n + sum_runs
    print(answer)

if __name__ == "__main__":
    main()
```