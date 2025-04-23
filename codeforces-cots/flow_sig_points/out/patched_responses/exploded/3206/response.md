<think>
Okay, let's try to solve this problem. So, the problem is about arranging numbers in a matrix to maximize its 'beauty' according to a specific recursive algorithm. Hmm. Let me read the problem statement again to make sure I understand it correctly.

The matrix is 2n x 2n in size, and we have exactly 4n numbers. Wait, wait, no, wait. Wait, the first line of input is 4n, but then the next line has 4n integers. Wait, no. Wait, the first line is an integer 4n, which means that the matrix size is 2n × 2n. Because 2n × 2n = 4n² cells. But the input gives 4n numbers. Wait, that can't be right. Wait, maybe there's a mistake here. Wait, the problem says that you have a 2n × 2n matrix and 4n integers. Wait, that's impossible. Because a 2n × 2n matrix has (2n)^2 cells. So if 4n is the number of integers, then (2n)^2 must equal 4n. But solving (2n)^2 =4n gives 4n² =4n → n² =n → n=0 or n=1. But that's only possible for n=1. So that's a contradiction. So there must be a mistake in the problem statement. Wait, perhaps the problem statement actually has a typo. Let me check the problem statement again.

Wait, the problem says: "He's got a square 2n × 2n-sized matrix and 4n integers. You need to arrange all these numbers in the matrix (put each number in a single individual cell)..." Oh right! So 4n is the number of integers. So 2n × 2n is equal to 4n, meaning that (2n)^2 =4n → 4n² =4n → n² =n → n(n-1)=0 → n=0 or 1. But the sample input has 4n=4, which is n=1. Then 2n=2, matrix is 2x2 (4 elements) and input has 4 elements. So that makes sense. Wait, but what about other values? For example, if n=2, 2n=4, so matrix is 4x4 (16 elements), but 4n=8. That's impossible. So this seems like a contradiction. Wait, no. Wait, maybe there's a mistake here. Oh wait, perhaps the problem statement is incorrect, and the number of integers is (2n)^2. Because otherwise, the problem makes no sense. So perhaps the first line of input is actually (2n)^2, which would make sense. For example, in the second sample input, 4n=4 implies n=1, matrix size 2x2. But the input has 4 numbers, which is (2n)^2=4. So that works. Wait, but according to the problem statement, the first line is 4n, but for n=1, that's 4, and the next line has 4 numbers. So in that case, the matrix is 2x2, which matches. But if the first line is 4n, then for n=2, the first line is 8, and the matrix would be 4x4 (16 elements). But 8 elements can't fill 16 cells. So there's a contradiction here. Therefore, the problem statement must have a mistake. Oh, wait. Wait, the problem says that the first line is 4n. Then 4n must be equal to the number of elements in the matrix, which is (2n)^2. So 4n = (2n)^2 → 4n =4n² → n² =n → n=0 or 1. So this is only possible when n is 0 or 1. But the sample input 2 has 4n=4 (so n=1) and 4 numbers. Which fits into a 2x2 matrix. But the sample input 2 is "4" numbers, which is 4n=4 → n=1. But when n=1, the matrix is 2x2, which holds 4 elements. So that works. But what about other values? For example, if 4n is 16, then n=4. Then the matrix is 8x8 (64 elements) but we have 16 numbers. Which is impossible. So this suggests that the problem statement is incorrect, and the first line of input is (2n)^2, not 4n. But that's not possible because the problem's examples and explanation would fit. Alternatively, perhaps the problem statement is correct, and we have a mistake here. Wait, perhaps the problem statement is correct, but the input 4n is (2n)^2. Because the first sample input has 1, which is 4n=1 → n=0.25. Which is not possible. Wait, that can't be. The first sample input is 1, so 4n=1 → n=0.25, but the matrix size is 0.5 × 0.5? Which makes no sense.

Wait, the first sample input is:

1

13

So the first line is 1, which is 4n. So n is 0.25. Which is impossible. But according to the problem statement, in the first case, n=0. So that the matrix is 0x0. But the problem says that when n=0, the beauty is the maximum element. So maybe the first line is 4n, but the matrix is 2n × 2n, which is 4n ×4n? No, that's not matching the samples.

Wait, this is getting confusing. Let's re-examine the problem statement.

The problem says:

The first line contains integer 4n (1 ≤ 4n ≤ 2·1e6). The next line has 4n integers. The matrix is 2n × 2n. So the number of elements in the matrix is (2n)^2. But 4n is the number of integers given. So (2n)^2 =4n → 4n²=4n → n² =n → n=0 or n=1. So the only possible values of 4n are 0 and 4. But that's impossible because the problem allows 1 ≤4n ≤ 2e6. So this is a contradiction. Therefore, the problem statement must have a mistake, but how?

Wait, perhaps the problem's actual input is (2n)^2. Let's see. For example, in the first sample, the input is 1, which is (2n)^2=1 → 2n=1 → n=0.5. But that's not possible. Alternatively, perhaps the matrix is of size 2n ×2n, and the input has (2n)^2 integers. Then the first line is (2n)^2. So the first sample input is 1, which would be 1 number. The matrix is 1x1 (n=0.5?), but according to the problem statement's first step, if n=0, which would be a 1x1 matrix (since 2^0=1). Then the beauty is the maximum. So perhaps the problem statement's first line is (2n)^2, and in the first sample, 2n is 1, so n=0.5. But that's not possible. Wait, this is getting too confusing.

Alternatively, perhaps the problem statement's first line is 4n, but the matrix is 2n ×2n. For example, when 4n=4, then 2n=2, matrix is 2x2. The input has 4 numbers, which fit. So 4n must be equal to (2n)^2. Therefore, 4n = (2n)^2 → 4n=4n² → n² -n=0 → n(n-1)=0 → n=0 or 1. So the problem is only valid for n=0 or 1, but the problem's input allows 4n up to 2e6. That can't be. So this suggests that there's a mistake in the problem statement. But given that the sample inputs work for n=0 and 1, perhaps the actual problem is that the matrix is of size 2^k ×2^k, and each split into four 2^(k-1) ×2^(k-1) matrices. So the problem's approach is that each split reduces the matrix size by half each time. So the problem is that the matrix must be of size 2^k ×2^k, and the number of elements is (2^k)^2. So for example, when k=1, the matrix is 2x2, which has 4 elements. So the input line 4n would be 4 elements, which is 2^k where k=1. So 4n = (2^k)^2 → 4n =4 → n=1. But this only works for n=1. So this can't be. Therefore, perhaps the problem statement's 4n is actually (2n)^2. So the first line of input is (2n)^2, and the matrix is 2n ×2n. Then the sample input 4 is (2n)^2=4 → 2n=2 → n=1. So the input has 4 numbers, which makes sense. Then the second sample's input is 4, which is (2n)^2=4 → n=1. Then the matrix is 2x2 and the input has 4 numbers, which matches. So perhaps the problem statement's first line is (2n)^2. So the user input is (2n)^2, and the next line has (2n)^2 numbers. So the first line is the number of elements. Then the problem's first line is 1 for the first sample, which is (2n)^2=1 → 2n=1 → n=0.5. But that's not possible. But in the first sample, the matrix is 1x1 (since 2n × 2n when n=0.5 is 1x1). But according to the problem's note, when n=0, the beauty is m. But the first sample's output is 13, which is the only number. So perhaps the problem's actual input is (2n)^2, which is the size of the matrix. But the problem statement says that the first line is 4n, which is conflicting. So perhaps the problem statement's first line is actually (2n)^2, but the problem description is incorrect. Otherwise, the problem's input is impossible. But given that the examples work, perhaps the first line is (2n)^2. Let's proceed with that assumption. Otherwise, there's no way to reconcile the input with the matrix size.

Assuming that the first line is the number of elements, which is (2n)^2. Then, the problem's beauty is computed as follows: split the matrix into four submatrices of size 2^{n-1} × 2^{n-1} each time. So for example, a 2x2 matrix (n=1) is split into four 1x1 submatrices. Then, the beauty is the sum of the maximum of the current matrix plus the sum of the beauties of the four submatrices. But since each submatrix is 1x1, their beauties are their own maximum (since when n=0, beauty is m). So for the 2x2 matrix, the beauty is the maximum of the entire matrix (which is the maximum of all four elements) plus the maximum of each of the four submatrices (each of which is a single element). So the total beauty would be the sum of the four elements plus the maximum element. But wait, no. Because the algorithm is:

1. Find the maximum element m.
2. If n=0, beauty is m.
3. Else, split into 4 submatrices of size 2n-1 ×2n-1, and sum m plus the beauty of each submatrix.

Wait, but 2n-1 when n is current level. For example, when the matrix is 2x2, n=1. So each submatrix is 2*1 -1 =1, but wait, 2n-1 is 1 when n=1. So the submatrices are 1x1. So their beauty is their own maximum.

Wait, but perhaps the way the problem is structured is that the recursion is based on the level. For a matrix of size 2^k ×2^k, the beauty is the sum of the maximum in the current matrix plus the sum of the beauties of the four submatrices of size 2^{k-1} ×2^{k-1}. So the process continues until k=0 (size 1x1). So the total beauty is the sum of all the maximums at each level.

So the key insight here is that, in order to maximize the beauty, we need to select certain elements to be the maximums at each level of the recursion, and sum all those maximums.

Let me think about this. For a matrix of size 2n x 2n (but perhaps n here is different from the problem's n). Let's think recursively. The beauty is the maximum of the current matrix, plus the sum of the beauties of the four submatrices. Each of those submatrices is split again, and so on, until the base case.

So the beauty is equal to the sum of all the maximums at each level of the recursion. Each split contributes the maximum of the current matrix, and each of the four splits contributes their own maximums. So the total beauty is the sum of the maximums of each matrix in each split.

But how many times do we have to select a maximum at each level? Let's think about the number of matrices at each level. For a matrix of size 2^k ×2^k:

- At the top level (level 0), we have 1 matrix. Its maximum contributes once.
- At level 1, the matrix is split into 4 matrices of size 2^{k-1} ×2^{k-1}. Each of these contributes their maximum once.
- At level 2, each of the 4 matrices is split into 4 more, leading to 4^2 matrices. Each contributes their maximum.
- This continues until level k, where each matrix is 1x1. Each contributes their maximum (the single element).

So the total number of maximums we need to sum is 4^0 (1) + 4^1 (4) + 4^2 (16) + ... +4^{k-1} (if k levels). Wait, no. Let's think for a matrix of size 2^k ×2^k. The number of splits is k levels. For example:

- k=0: 1x1 matrix. Sum is 1 element (level 0).
- k=1: 2x2 matrix. Sum is 1 (top level) +4 (submatrices) =5 elements. Which matches the second sample's output of 14=4+1+2+3+4. Wait, in the sample input, the numbers are 1,2,3,4. The maximum of the top level is 4. The four submatrices (each 1x1) contribute 1,2,3,4. Sum is 4 + (1+2+3+4) =4+10=14. Which is correct.

So the sum is the sum of all maximums at each level. The number of maximums at each level is 4^m, where m is the level. For example, for k=2 (matrix 4x4):

- level 0: 1 matrix → 1 maximum.
- level 1: 4 matrices →4 maximums.
- level 2: 16 matrices →16 maximums.
Total sum: 1 +4 +16=21 maximums. Wait, but for a 4x4 matrix, the split would be into four 2x2 matrices. Each of those would split into four 1x1 matrices. So the levels are:

- level 0: 4x4 →1 maximum.

- level 1: split into 4 2x2 matrices →4 maximums.

- level 2: each 2x2 split into 4 1x1 →16 maximums (but each 1x1's maximum is their own element).

So the total sum is 1 (level 0) +4 (level1) +16 (level2) =21.

But how many elements are there in total? 4x4=16 elements. So how can we sum 21 elements? That's impossible. So this suggests that there's a mistake in the way the levels are considered.

Wait, perhaps the levels are different. Let's think again for the 2x2 matrix (k=1):

- level 0: 1 matrix, sum 4 (max of the entire matrix).

- level 1: 4 matrices (each 1x1), sum 1+2+3+4=10.

Total sum 4+10=14.

But the total elements are 4. So how can there be 5 maximums (1+4) when there are 4 elements? Because the same elements are being considered at multiple levels. For example, in the 2x2 matrix, the elements are arranged such that the top-level maximum is 4, and each of the submatrices (the elements themselves) contributes their own value. So in this case, each element is counted once (in the submatrix's level). The top-level maximum is 4, which is one element, then the four submatrices' maximums are 1,2,3,4. So the sum is 4 (top) +1+2+3+4 (sub) =14. But the sum of all elements is 10, plus the top maximum 4 gives 14. Wait, that's not possible. Wait, the sum of the four elements in the sample is 1+2+3+4=10. Then the total beauty is 4 (top max) + sum of the four submatrix maxima (1+2+3+4) =14. Which is 10 plus 4. So the total sum is the top maximum plus the sum of all elements. Wait, but the sum of the submatrix maxima is the sum of all elements, since each submatrix is a single element. So in this case, the beauty is the top maximum plus the sum of all elements. But how?

Ah, wait, perhaps the total sum is the sum of the maximums at each level of the recursion. So for the 2x2 matrix:

- The top level maximum is 4. Then, each of the four submatrices (each 1x1) contributes their own maximum (1, 2,3,4). So the sum is 4 +1+2+3+4=14.

Which is the maximum plus the sum of all elements. But the sum of all elements is 10, but 4+10=14. So how is this possible? Because the top maximum is included once, and the elements are included once. So in this case, the sum is the sum of all elements plus the maximum. But that's not always the case. For example, if the matrix was 1x1 (n=0), the sum is just the maximum, which is the element itself. For a 4x4 matrix (n=2), the sum would be the maximum of the entire matrix plus the sum of the maxima of each of the four 2x2 submatrices, and each of those submatrices would contribute their maximum plus the sum of their four 1x1 elements. So for a 4x4 matrix, the total sum is the global maximum (for the 4x4) plus the sum of the four maxima of each 2x2 submatrix plus the sum of all 16 elements.

Wait, no. Let's think again. For the 4x4 matrix:

- The top level maximum is added once.

Then, each of the four 2x2 submatrices adds their own maximum (four maxima).

Then, each of those four 2x2 submatrices is split into four 1x1 matrices, so each 2x2 submatrix contributes four maxima (the elements). So for each 2x2 submatrix, their sum is their maximum plus the sum of their four elements. So the total sum is:

global_max + (sum of four submatrix maxima) + (sum of all 16 elements).

Wait, no. Because each 2x2 submatrix's beauty is its maximum plus the sum of the four elements (since each is a 1x1 matrix). So for the four 2x2 submatrices, their beauty is (max of 2x2) + sum of their four elements. Then, the total sum is:

global_max (4x4) + sum of (max of each 2x2 submatrix + sum of their elements).

Which is equal to global_max + sum of the four 2x2 submatrix maxima + sum of all 16 elements.

But then the total sum is (global_max + sum of 4 maxima) + sum of all elements. Which would be sum of all elements plus the sum of maxima at each level.

But how many levels are there? For a 2n x 2n matrix (assuming that n is such that the matrix is 2^k x 2^k, perhaps). For example, when k=2 (4x4), there are three levels:

Level 0: 4x4 matrix. Max added once.

Level 1: 4 matrices of 2x2. Each adds their max. Total 4.

Level 2: 16 matrices of 1x1. Each adds their max (the element itself). So sum is 16 elements.

Total sum: 1 (level 0) +4 (level1) +16 (level2) =21. But the sum of elements is 16, and the sum of the maxima (level0 and level1) is 1+4=5, so the total would be 5 +16=21.

Which suggests that the total sum is equal to the sum of all elements plus the sum of the maxima at each level except the last one. Because the last level (1x1 matrices) contribute their elements as their maxima.

So for a matrix of size 2^k x2^k:

sum of all elements (each contributes once, as the maximum of their 1x1 submatrix) plus the sum of maxima at each higher level.

So the problem reduces to selecting, for each level from 0 to k-1, the maximum elements at that level, and then summing all those maxima along with the sum of all elements.

Wait, this seems to be the key insight. Because the beauty is the sum of all maximums chosen at each split. The maximum of the entire matrix is added once. Then, each split into four submatrices adds their maxima. Then each of those is split again, adding their maxima, and so on until the 1x1 matrices. However, the 1x1 matrices contribute their element (the maximum) as part of their beauty.

But in the sample input 2, the sum is the maximum of the top matrix (4) plus the sum of the four elements (1+2+3+4=10) which equals 14. Which is 4 (top max) + 10 (sum of elements). So this suggests that the sum of all elements is the sum of the maxima at the last level (the 1x1 matrices), and the other levels contribute their own maxima.

So the total beauty is equal to the sum of all the elements (each contributes once as their own maximum in the 1x1 matrix) plus the sum of the maxima from each level except the last level.

Wait, for the 2x2 matrix (k=1), the levels are:

Level 0: top matrix (2x2), max added once.

Level 1: four 1x1 matrices, each contributes their element. Sum of these is 10.

So the total beauty is level0 max (4) + sum of level1 elements (10) =14.

Which is 4 + 10 =14.

For a 4x4 matrix (k=2), the levels are:

Level0: max of 4x4 matrix (added once).

Level1: four 2x2 matrices, each's max is added once (sum of four maxima).

Level2: sixteen 1x1 matrices, sum of their elements (sum of all 16).

Total beauty is level0 + level1 + level2.

So the beauty is sum of all elements (level2) plus the sum of level0 and level1 maxima.

So the problem becomes: arrange the elements in the matrix such that the sum of the maxima at each level (from 0 to k-1, where the matrix is 2^k x2^k) plus the sum of all elements is maximized.

But how do we choose the maxima at each level to maximize this sum?

The key observation here is that at each level, certain elements are candidates to be selected as the maximum for their submatrix. The higher the level, the larger the submatrix. So for the top level (level0), the entire matrix's maximum is selected, which is the largest element. Then, for each of the four submatrices (level1), the maximum in each is selected (but not overlapping with the level0 maximum). Then for level2, each of those submatrices is split into four, and their maxima are selected (again, not overlapping with any higher level maxima), and so on.

Wait, but the elements are arranged in the matrix. So each element can be part of multiple submatrices at different levels. For example, an element in a 4x4 matrix is part of the entire matrix (level0), part of a 2x2 submatrix (level1), part of a 1x1 submatrix (level2). But once it's selected as the maximum at a higher level, it cannot be selected again at lower levels. Because the maximum of a higher level's submatrix is part of the sum, but lower levels (smaller submatrices) would not include that element again.

Wait, no. Because the maxima are selected at each level. For example, the level0 maximum is the global maximum. Then, for each of the four submatrices at level1 (the four quadrants), their maxima are chosen (but these could be the same as the level0 maximum if it's in that quadrant). But wait, no. Because after selecting the level0 maximum (the largest element), the four submatrices at level1 would each have their own maxima, which could be different elements. But the same element can't be selected again in a lower level, because once it's part of a higher level's maximum, it's part of the sum for that level, but lower levels (smaller submatrices) can still include it again.

But this approach would require that each element can contribute to multiple levels. For example, the largest element (selected as level0's maximum) would be part of one of the level1 submatrices, which could select it again as their maximum. Then, in their submatrix's split into level2, it's again part of a 1x1 matrix. So the same element would be added once for level0, once for level1, and once for level2, plus its own value in the sum of elements. But that's impossible, since the element can only be used once. So this suggests that each element can be counted in exactly one of the levels.

Wait, but how does the algorithm work? The algorithm is recursive. For a matrix, the beauty is the sum of the current maximum plus the sum of the beauties of the four submatrices. So once the current maximum is chosen, it's included once. The submatrices are formed by splitting the current matrix into four parts. So the current maximum is part of one of the four submatrices. Then, in that submatrix's beauty calculation, its maximum is chosen again. So the same element can be included multiple times. But this would result in a higher sum. For example, if the largest element is in a 2x2 matrix, the sum would be that element (level0) plus that element again (as part of one of the level1 submatrices) plus that element again (as part of a level2 submatrix) plus its own value in the sum. So the sum would be 4+4+4+4=16 for that element. But this is possible only if the same element is part of multiple submatrices in different levels.

But that's impossible because each element is part of exactly one submatrix at each level. For example, in a 2x2 matrix, the element chosen as the maximum for the entire matrix is part of one of the four 1x1 submatrices, so it's added once as the level0 maximum, and once as its own 1x1 submatrix. So the total contribution is 4+4=8, but according to the sample input, the sum is 14. So the sample input's sum is 4 (level0 maximum) plus 1+2+3+4 (level1 maximums) = 14. But according to this, the maximum of level0 is 4, which is part of one of the level1 submatrices. So in that submatrix, the maximum is 4 again, which would contribute to the level1 sum. So the sum would be 4 (level0) +4 (level1) + 1+2+3+4 (level2) =4+4+10=18. But the sample output is 14, which contradicts this.

This suggests that the way the algorithm works is that once a maximum is chosen at a higher level, it is not considered in the lower levels. So the submatrices are processed after removing the elements chosen at higher levels.

But that's not possible, because the problem says to arrange all numbers in the matrix. So all elements must be placed in the matrix, and each element is used exactly once.

So the confusion arises because the same element can be part of multiple levels' maxima, leading to it being counted multiple times. However, in the sample input, the sum is 14. Which is 4 (level0) + 1+2+3+4 (level1, which are the four elements). But in this case, the level0 maximum is 4, which is part of one of the level1 submatrices. So why does the level1 submatrix's maximum also include 4?

Because in the problem's algorithm, the beauty of the submatrix is computed recursively. So the maximum of the current submatrix is taken from all elements in it, regardless of previous steps. So the same element can be chosen as the maximum of multiple levels.

But this would mean that the sum can be maximized by choosing the largest element at every possible level. Which is possible only if the largest element is in the smallest possible submatrix (so it's selected at all higher levels). For example, in a 4x4 matrix, the largest element is in a 2x2 submatrix, which is part of the entire matrix. So the largest element would be selected as the maximum of the entire matrix (level0), then as the maximum of its 2x2 submatrix (level1), then as the maximum of its 1x1 submatrix (level2). So it would contribute three times to the sum, plus its own value in the sum of elements, leading to a total contribution of 3*element + element =4*element. But that's only possible if the largest element is placed in such a way that it is part of every split's submatrix.

But this seems impossible, except for the top-level maximum. Because when the matrix is split into four submatrices, the top-level maximum is in one of them, and that's the only submatrix that can have that element. So in that submatrix's split into four parts, the element is in one of the four. So each level contributes one occurrence of the maximum. So the maximum element is counted once for each level it is the maximum of a submatrix.

So for a matrix of size 2^k x2^k, the maximum element can contribute k+1 times (once for each level from 0 to k). But how?

Let's take an example. Suppose the matrix is 4x4 (k=2). The largest element is placed in the top-left quadrant (submatrix A). So:

- Level0: maximum is this element (counted once).

- Level1: submatrix A's maximum is this element (counted again).

- Level2: the 1x1 submatrix in submatrix A's top-left quadrant has this element (counted again).

So this element contributes 3 times (levels 0,1,2) plus once as part of the sum of elements (level2). So total of 4 times.

But the sum of elements includes every element once. So the element is counted once as part of the sum of elements (level2), plus once for each level where it's a maximum.

So the problem's total beauty is sum_{all elements} element + sum_{all maxima in levels 0 to k-1} maxima.

Because the sum of elements is the sum of all the maxima in level k (since each element is a 1x1 matrix's maximum). The levels 0 to k-1 contribute their maxima.

Therefore, the total beauty is sum of all elements plus the sum of maxima from levels 0 to k-1.

Thus, the problem reduces to selecting the maxima at each level (from 0 to k-1) such that the sum of those maxima is maximized, and then adding that sum to the sum of all elements.

But how to select these maxima?

The key is to choose the largest possible elements for the higher levels. Because each element can be used as a maximum in one level. For example, the largest element is used as the maximum in level0. The next four largest elements are used as the maxima in level1. Then the next 16 elements are used as maxima in level2. And so on.

But wait, each level has 4^m maxima, where m is the level number. For example, level0 has 1, level1 has 4, level2 has 16, etc. So the number of elements required for the maxima is 1 +4 +16 + ... +4^{k-1} = (4^k -1)/3.

So for example:

- k=0: (4^0 -1)/3 =0. But that's level0, which requires 1 element. So perhaps the formula is (4^{k} -1)/3.

Wait, for k=1 (matrix 2x2):

Levels 0 and 1-1=0. So levels 0: sum is 1. So (4^1 -1)/3 = (4-1)/3=1. Which matches.

For k=2 (matrix4x4):

sum from level0 to level1: 1+4=5. (4^2-1)/3= (16-1)/3=5. Correct.

Yes, so the number of maxima needed from levels 0 to k-1 is (4^k -1)/3.

But the total number of elements in the matrix is 4^k. So the sum of maxima needed is (4^k-1)/3 elements, and the sum of elements is 4^k elements. So when we add them, we get (4^k-1)/3 +4^k = (4^k-1 +3*4^k)/3 = (4*4^k -1)/3 = (4^{k+1} -1)/3 - something. But this is just the total sum of the elements plus the maxima.

But how to maximize the sum of the maxima from levels 0 to k-1.

The approach is to select the largest (4^k-1)/3 elements and sum them, then add the sum of all elements.

Wait, but the sum of all elements plus the sum of the maxima from levels 0 to k-1 is equal to the sum of all elements plus the sum of those maxima. But since the sum of all elements includes all elements, including those used as maxima in levels 0 to k-1. So the total sum is sum(elements) + sum(maxima) = sum(elements) + sum of the (4^k-1)/3 largest elements.

Wait, no. Because sum(elements) includes all elements, including those used as maxima. So adding sum(maxima) would count those elements twice. But according to the problem's algorithm, the sum of the maxima is part of the beauty, and the sum of the elements is part of the beauty (each element contributes once as a 1x1 matrix's maximum). So the total beauty is sum(maxima at all levels 0 to k-1) + sum(elements).

But the sum of elements is the sum of maxima at level k (since each element is a 1x1 matrix's maximum). So the total beauty is the sum of maxima from level0 to levelk. Because levelk is the 1x1 matrices.

But level0 to levelk-1 have their maxima (summing to (4^k-1)/3), and levelk's maxima sum to 4^k (the sum of all elements).

So the total beauty is (sum of (4^k-1)/3 elements) + sum of all elements.

Wait, no. Because the sum of level0 to levelk-1 maxima is sum of (4^0 +4^1 + ... +4^{k-1}) = (4^k-1)/3 elements, and the sum of levelk (all elements) is 4^k elements. So the total beauty is sum of (4^k-1)/3 elements (the maxima) plus sum of all elements.

Which is sum of elements plus sum of maxima.

But sum of elements includes the maxima. So the total is sum(elements) + sum(maxima). So the maxima are added twice. But according to the problem's sample input 2:

sum(elements) is 1+2+3+4=10.

sum(maxima) is 4 (level0) +1+2+3+4 (level1) =14. But according to the sample, the output is 14. So according to this formula, sum(elements) + sum(maxima) would be 10+14=24, which is not the case. So this suggests that the formula is incorrect.

So there's a misunderstanding here. Let me re-examine the problem's algorithm.

The beauty is computed as follows:

At each step, the beauty is the maximum of the current matrix plus the sum of the beauties of the four submatrices.

For example, for a 2x2 matrix:

beauty = max(matrix) + sum(beauty(submatrix) for each of the four submatrices).

Each submatrix is 1x1, so their beauty is their element.

Thus, the beauty is max + a1 +a2 +a3 +a4.

But the sum of elements is a1+a2+a3+a4. So the total beauty is sum(elements) + max. Which is the case in the sample input.

So for the 2x2 matrix, the sum of maxima from levels 0 and 1 is 4 (level0) +4+1+2+3 (level1's submatrix maxima? No. Wait, each submatrix's maximum is the element itself, so level1's sum is 1+2+3+4. So the total beauty is 4 (level0) +1+2+3+4 (level1's sum of maxima) =4+10=14. Which is the sum of the level0 maximum and the sum of the four level1 maxima.

But the sum of the elements is 10, and the sum of the maxima from level0 and level1 is 4+10=14. So the total beauty is sum of the maxima from level0 to level k-1 (k=1, so k-1=0: level0) plus sum of the elements (level1's sum). Wait, no.

Wait, in this case, for k=1, the levels are 0 and 1. But the algorithm for k=1 (2x2 matrix) has:

beauty = m (level0) + sum of four submatrices' beauties (level1).

Each submatrix's beauty is their maximum (since they are 1x1). So level0's maximum is added once, level1's four maxima are added once each. So the total beauty is 1 (level0) +4 (level1) maxima, sum of five elements. Which is 4+1+2+3+4=14.

But the sum of elements is 1+2+3+4=10. So the sum of the maxima from level0 and level1 is 4+1+2+3+4=14. Which is the same as sum of elements (10) plus level0's maximum (4). Which is 14.

So for k=1, the total beauty is sum(elements) + level0's maximum.

But according to the formula, the number of maxima from level0 to k-1 (k-1=0) is 1. So sum of the largest 1 elements (4) plus sum of elements (10) =14. Which matches.

For a 4x4 matrix (k=2), the number of maxima needed from levels0 to k-1 (levels0 and 1) is 1+4=5. So the sum of the top 5 elements plus sum of all elements.

For example, if the elements are sorted in descending order, and we take the top 5 elements, sum them and add to the sum of all elements.

Yes! Because the total beauty is sum of the elements (each counted once as their own 1x1 matrix's maximum) plus the sum of the maxima from levels0 to k-1 (which is the sum of the top (4^k -1)/3 elements).

So the solution is to sort all elements in descending order. Then take the first (4^k -1)/3 elements and sum them. Then add the sum of all elements to get the total beauty.

Because (4^k -1)/3 is the number of maxima needed for levels0 to k-1. Since the higher levels contribute more maxima (level0:1, level1:4, etc.), the largest elements should be chosen for these positions.

Thus, the steps to solve the problem are:

1. Compute k from the input size. The input has m=4n elements. Wait, no. Wait, the input's first line is 4n. Which, according to the samples, seems to be equal to (2n)^2. For example, the first sample has 4n=1 → n=0.25, but matrix size is 1x1 (2n=0.5x0.5? No. This is impossible. So the original problem statement must have a mistake. But given that the samples work if we assume that the input size is (2n)^2, which equals 4n. Then 4n must be a perfect square. For example, 4n = s², where s is the matrix size. So matrix size is s x s =2n ×2n. So s=2n. So 4n= s² → s= sqrt(4n) → 2n= sqrt(4n) → 4n²=4n → n=1. Which only works for n=1 and s=2. So this suggests that the problem statement has a mistake. 

But the original problem statement says that the matrix is 2n ×2n, and the input has 4n elements. Which is only possible for 2n ×2n =4n → n=1. So this is a contradiction. Therefore, perhaps the problem statement's input is (2n)^2, and the matrix size is 2n ×2n. So for example, the first line of input is (2n)^2. So the first sample input has 1 element (1=1^2 → n=0.5?), but according to the problem statement, when n=0, the beauty is the maximum. But this is only possible if the matrix is 1x1 (n=0 → 2^0=1). So perhaps the first line is the number of elements (2n)^2, and the matrix is 2n ×2n. Then, for example, the first sample's input is 1 (elements), which is a 1x1 matrix. The beauty is 13. Which matches.

The second sample's input is 4 elements (matrix 2x2, n=1). So the first line is 4 (number of elements), which is (2n)^2 →2n=2 →n=1.

So the problem's first line is (2n)^2, the matrix is 2n ×2n. So the first line is the number of elements (m), which must be a perfect square. Then, m= (2n)^2, and the input has m elements.

So to find k, where m= (2^k)^2 → m=4^k. So k is log2(s), where s is the matrix size. For example, m=4: 4=4^1 →k=1. m=16 →k=2.

So the number of levels is k. The sum of maxima from levels0 to k-1 is the sum of the top (4^k -1)/3 elements.

The sum of all elements is the sum of all m elements.

So the total beauty is sum of all elements plus sum of the top (4^k -1)/3 elements.

Wait, but in the first sample, m=1 →k=0. The sum of maxima from levels0 to k-1 = sum from 0 to -1, which is zero. So the beauty is sum of elements (13) + 0 =13. Which matches.

In the second sample, m=4 →k=1. (4^1-1)/3 = (4-1)/3=1. So sum of the top 1 elements is4. Sum of elements is 10. So total 14. Which matches.

Another example: m=16 (4x4 matrix, k=2). (4^2-1)/3=5. So sum of top 5 elements plus sum of all 16 elements.

So the algorithm is:

Sort all elements in non-increasing order.

Compute the number of maxima needed, which is (4^k -1)/3, where k is log2(s), and s is the matrix size (s= sqrt(m)).

Sum the first (4^k-1)/3 elements and add to the sum of all elements.

Thus, the steps are:

1. Read m elements.

2. Compute k, where m=4^k. Because m is (2n)^2, which is (2^k)^2=4^k. So m must be a power of4. For example, m=1 (4^0), m=4 (4^1), m=16 (4^2), etc.

3. Compute the number of maxima needed as (m-1)/3. Since 4^k -1 is m-1, and divided by 3.

4. Sort the elements in descending order.

5. Sum the first (m-1)/3 elements.

6. Sum all elements.

7. The total beauty is the sum from step5 plus the sum from step6.

Thus, the code would be:

Read m from input.

Read list of elements.

sum_all = sum(elements)

elements_sorted = sorted(elements, reverse=True)

k = log(m, 4)

required = (m-1) //3

sum_maxima = sum(elements_sorted[:required])

result = sum_all + sum_maxima

print(result)

But wait, for m=4, required is (4-1)/3=1. So sum_maxima is first element (4). sum_all is 10. Total 14. Which is correct.

For m=1, required=0. sum_maxima is 0. sum_all=13. Total 13. Correct.

For m=16, required=(16-1)/3=5. So sum first 5 elements.

So the code is correct.

So the problem reduces to summing all elements, plus the sum of the largest (m-1)/3 elements, where m is the number of elements, which must be a power of 4.

But the problem's input states that the first line is 4n. But according to this solution, the first line is m, which is (2n)^2. So there is a mistake in the problem statement. However, given the sample inputs, the first line of the input is m, the number of elements. So the first sample's first line is 1 (number of elements), the second sample's first line is4.

Thus, the correct code is to read the first line as m, then read m elements, then proceed as described.

So the code is straightforward.

But now, how to compute m. For example, in the first sample input, the first line is 1, which is the number of elements. So the code reads m, then reads m elements. Then compute required = (m-1)//3.

Then sum all elements plus sum of the first required elements.

Thus, the code is as follows:

Read m from input.

Read list of elements.

sum_all = sum(elements)

elements_sorted = sorted(elements, reverse=True)

required = (m-1) //3

sum_maxima = sum(elements_sorted[:required])

result = sum_all + sum_maxima

print(result)

Testing this code with the sample inputs.

Sample 1:

Input:

1

13

m=1.

required =0.

sum_all=13.

sum_maxima=0.

result=13+0=13. Correct.

Sample2:

Input:

4

1 2 3 4

m=4.

required= (4-1)/3=1.

sum_all=10.

sum_maxima=4.

result=10+4=14. Correct.

Another test case: m=16.

required= (16-1)/3=5.

elements sorted are [a1 >=a2 >= ... >=a16].

sum_maxima = sum(a1+a2+a3+a4+a5).

sum_all is sum of all 16.

So the code would give sum_all + sum of the top5.

Which aligns with the theory.

Thus, the code is correct.

Therefore, the solution is to sort the elements, sum all elements, and sum the top (m-1)//3 elements, then add them.
</think>

```python
def main():
    import sys
    input = sys.stdin.read().split()
    m = int(input[0])
    a = list(map(int, input[1:m+1]))
    sum_all = sum(a)
    a_sorted = sorted(a, reverse=True)
    required = (m - 1) // 3
    sum_max = sum(a_sorted[:required])
    print(sum_all + sum_max)

if __name__ == "__main__":
    main()
```