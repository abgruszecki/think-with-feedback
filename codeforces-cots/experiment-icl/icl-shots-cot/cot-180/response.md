<think>
Okay, I need to solve this programming problem. Let's read the problem statement carefully.

The problem is: Given an array of integers, perform two operations. First, rearrange the elements in any order. Then, choose a contiguous segment and flip the signs of all elements in that segment (or choose to do nothing). The goal is to maximize the sum of the array after these operations.

Hmm. Let's break down what steps we can take here.

First, since the first operation allows rearrangement, we can arrange the elements in any order. The second operation is flipping a contiguous segment. But after rearrangement, the order matters for the flipping step. Wait, but the flipping is after rearrangement. So the optimal approach would probably involve rearranging the array in a way that allows the flip of a contiguous segment to give the maximum possible sum.

So the key here is to find the best way to arrange the elements and then choose the best possible contiguous segment to flip. But how?

Let's think about what the flipping does. Flipping a segment [l..r] would invert the signs of all elements in that segment. So the sum after flipping is the original sum minus twice the sum of that segment (since flipping each element's sign is like adding -2*element to the sum). So to maximize the sum after flipping, we need to find a contiguous segment whose sum is as negative as possible. Because subtracting twice a negative number (which makes it positive) adds to the sum.

Wait, right. Let's see:

Original sum after rearrangement is S. If we flip a segment with sum K, the new sum becomes S - 2*K. Because each element in the segment is multiplied by -1, so the sum changes by (-K) - K = -2K.

Wait, no. Wait, original sum is S. When we flip the segment, the sum of that segment becomes -K. The total sum is S - K (original sum) + (-K) (sum after flip). So total sum is S - 2*K.

Wait, yes. So flipping the segment subtracts 2*K from the original sum. So to maximize the sum after flipping, we need to subtract the smallest possible value. Because if K is negative, subtracting 2*K (which is adding a positive value) increases the total sum.

So the optimal flipping step is to choose the contiguous segment whose sum is the smallest (most negative possible), because subtracting 2*K (which is adding a positive value when K is negative) gives a larger sum. However, if all possible segments have a non-negative sum, then flipping any of them would decrease the sum, so we should choose not to flip anything.

So the strategy for the flipping part is: find the contiguous segment (after rearrangement) with the minimum sum. Then, the maximum possible sum after flipping is S - 2*min_subarray_sum, where S is the sum after rearrangement.

But how does the rearrangement affect this? Because the rearrangement can arrange elements in any order. So the question becomes: how to arrange the elements such that the minimal possible contiguous subarray sum is as small as possible (so that when we flip it, we add as much as possible to the total sum).

Wait, but the rearrangement is done first, and then the flipping. So the rearrangement's goal is to allow us to have a contiguous segment (after rearrangement) with a sum that is as negative as possible, so that flipping it (thus adding -2*K, where K is negative) gives the maximum possible gain.

So the problem reduces to: arrange the elements in an order such that the minimal possible contiguous subarray sum is as small as possible, and then compute the maximum possible sum S - 2*K, where S is the sum of all elements (after rearrangement) and K is the minimal contiguous subarray sum in the rearranged array.

Wait, but S is the sum of all elements. Rearrangement doesn't change the sum of the array. Because rearrangement is just reordering. So the sum S is fixed as the sum of all elements, regardless of how we arrange them. Wait, that's a key point. Wait, the first operation is rearrangement. So the sum after rearrangement is the same as the original sum. Because you're just reordering elements. So S remains the same. Then, flipping a segment will change the sum by -2*K, where K is the sum of the segment in the rearranged array. So the total sum after operations is S + (-2*K), where K is the sum of the flipped segment (before flipping).

Therefore, the problem can be restated as: Rearrange the array in any order, then choose a contiguous segment (possibly empty) to flip. The maximum sum is S (original sum) minus twice the sum of the chosen segment. We need to choose the arrangement and segment such that this is maximized.

But since the arrangement can be any permutation of the elements, how can we arrange them to minimize the minimal possible contiguous subarray sum (to maximize the gain when we flip it)?

Wait, but the sum S is fixed. The sum of the array after rearrangement is the same as the original. So the problem is now: arrange the elements in any order, then find the minimal contiguous subarray sum in that arrangement, then the maximum possible sum is S - 2*K, where K is that minimal sum. So to maximize this sum, we need to minimize K as much as possible.

So the problem becomes: arrange the elements in such a way that there exists a contiguous subarray with sum K as small as possible (as negative as possible), so that when we subtract 2*K (which is adding a large positive value), the sum becomes as large as possible.

So the key is to find the arrangement of elements where the minimal contiguous subarray sum is as small as possible. Then, the maximum sum is S + 2*(-K) (since K is negative, this adds a positive value). So the problem reduces to finding the minimal possible K (sum of a contiguous subarray) over all possible arrangements of the elements.

But how can we find the minimal possible K given that we can arrange the elements in any order?

Wait, this is the crux of the problem. We need to arrange the elements such that there's a contiguous subarray with the smallest possible sum. Then, flipping that subarray will give the maximum possible sum.

But how to find such an arrangement?

Let's think about this. The minimal possible K (sum of a contiguous subarray) in any arrangement of the elements. How can we minimize K?

The minimal K would be the sum of the most negative possible combination of consecutive elements. So, perhaps arranging the array in such a way that all the negative numbers are grouped together, so that their sum is as negative as possible, and then flipping that segment would turn them positive and add their absolute value twice.

But how to arrange the elements to maximize the sum of a contiguous segment in the negative direction.

Alternatively, perhaps the minimal K can be the sum of all negative elements in the array. But that's only possible if they can be arranged in a contiguous block.

Wait, for example: suppose we have elements like [3, -2, -3]. If arranged as [3, -2, -3], the sum of the entire array is -2. The minimal contiguous subarray sum is -5 (the sum of -2 and -3). So flipping that gives 3 + 2 +3 =8.

But if the array were arranged as [-2, -3, 3], the minimal contiguous sum is -5 (the first two elements). So flipping that gives the same result.

Alternatively, the arrangement could be such that the minimal contiguous subarray is the sum of all the negative elements. Wait, but perhaps if there's a way to group all the negative elements into a contiguous block, then flipping that would give the maximum possible gain.

Wait, but what if the array has both positive and negative elements. For example, in the fourth test case, the array is [-99]. So arranging it as [-99], then flipping the entire array gives 99.

So perhaps the optimal arrangement is to arrange the elements such that all the negative elements are in a contiguous block. Then, flipping that block would turn all negatives into positives. But wait, the sum of the block would be the sum of all negatives. So flipping that block would add 2*abs(sum_of_negatives).

But in some cases, there might be a way to arrange the elements such that a particular contiguous subarray (not all the negatives) gives a more negative sum than the sum of all negatives. For example, if some positives are between negatives, perhaps their sum would be lower than the sum of all negatives.

Wait, let's see. Suppose the array is [3, -5, 2, -4]. The sum of all negatives is -9. But if arranged as [3, 2, -5, -4], then the sum of the entire array is (3+2-5-4) = -4. The minimal subarray is the last two elements, sum -9. Flipping that gives sum 3+2+5+4=14. Alternatively, if arranged as [-5, 3, 2, -4], the minimal sum is -5 (first element) or maybe 3+2+(-4) =1. Hmm, no. So in that case, grouping all negatives into a single block gives the minimal sum.

But perhaps in some cases, combining certain positive and negative elements can give a more negative sum. For example, if we have elements like [1, -3, -2, 4]. The sum of the negatives is -5. But if arranged as [4, 1, -3, -2], then the sum of the last two elements is -5. Alternatively, if arranged as [-3, 1, -2, 4], then the subarray [1, -2] sums to -1, which is better than -5. Wait, but that's not better. So perhaps grouping all the negatives together is better.

Wait, perhaps the minimal contiguous sum can be the sum of a subset of elements, not necessarily all the negatives. But in that case, how can we arrange them to get such a sum?

Alternatively, maybe the best possible K is the sum of the most negative possible subset of the elements, regardless of their arrangement. But since arrangement allows any permutation, perhaps the minimal possible K is the minimal possible sum of any subset of the array elements. Wait, no. Because the subset must be contiguous. So even if some elements can sum to a very negative value, but they are not contiguous, then arranging them in a way that allows them to be contiguous would allow that sum.

So perhaps the problem reduces to: find the minimal possible sum of any subset of elements (of the array) when arranged in some order such that those elements are contiguous. Then, the maximum sum is S + 2*abs(K), where K is that minimal sum.

But how to compute this?

Let me think. The minimal possible sum of a contiguous subarray in any arrangement is the minimal possible sum of any subset of the array's elements (since we can arrange them to be contiguous in the array). But wait, no. Because the arrangement can be any permutation. So for any subset of elements, we can arrange them in the array such that those elements form a contiguous subarray. For example, if I select a subset S of elements, then in the arrangement, we can place all elements of S together in a contiguous block, and the rest in any order. So the sum of S would be the sum of that contiguous block. Thus, the minimal possible K is the minimal sum of any subset of the elements (since any subset can be arranged to be contiguous). But wait, the subset has to be contiguous, but in the arrangement, yes. So the problem reduces to finding the minimal possible sum of any non-empty subset of the elements, and that's the K we can flip. But why non-empty? Because the flipping can be at most one segment, but not flipping is allowed. So the best K is the minimal between the minimal subset sum and zero. Because if all subset sums are positive, then flipping nothing gives K=0 (since subtracting 0 is better than subtracting a positive K). Wait, but K is the sum of the segment we flip. So if K is positive, then subtracting 2*K would make the sum S - 2*K. But S is fixed. So in that case, the best option is not to flip anything (since flipping would reduce the sum). So the optimal K is the minimal between the minimal possible subset sum (could be negative) and zero (if we choose not to flip). So the maximum sum after flipping is S - 2*min(0, minimal_subarray_sum). Because if the minimal subset sum is negative, then flipping that subset gives a gain. Otherwise, do nothing.

So the problem becomes: find the minimal possible sum of any subset of the array's elements (the minimal sum of a contiguous subarray in some arrangement), and then the maximum sum is S - 2*min(0, that minimal sum).

But how do we compute that minimal subset sum? Because the arrangement allows any permutation, the minimal subset sum is the minimal sum that can be formed by any subset of the elements. Because in the arrangement, those elements can be grouped into a contiguous block.

Wait, that's a crucial insight. Since the arrangement is arbitrary, the minimal sum of a contiguous subarray is the minimal possible sum of any subset of elements (could be any combination of elements, as long as they can be arranged to form a contiguous block). But in reality, any subset can be arranged to form a contiguous block, regardless of the order. So the problem reduces to selecting a subset of elements (non-empty) such that their sum is as small as possible. Then, arrange them in the array as a contiguous block, flip that block, and the sum becomes S + 2*abs(sum_of_subset).

Wait, but flipping the subset would add 2*abs(sum_of_subset) if sum_of_subset is negative.

But the minimal sum of a subset could be the sum of all negative elements. But perhaps there's a combination of elements (some positive and some negative) that sum to a lower value. For example, if you have elements like 5, -10, 3. Then the sum of all negatives is -10. But the subset {5, -10} sums to -5, which is worse. But the subset {-10} is better. So in this case, the minimal sum is -10.

Another example: elements like -2, -3, 4. The minimal subset sum is -5 (sum of -2 and -3). So flipping that subset would add 10 to the total sum.

So the problem is to find the subset of elements (non-empty) that has the minimal sum. Then, the maximum sum is S - 2*min(0, sum_of_subset).

Wait, but the sum_of_subset could be the sum of any subset of elements. Because in the arrangement, we can arrange those elements to be contiguous. So, regardless of their original positions, they can be arranged as a contiguous block, so their sum can be flipped. Therefore, the minimal sum that can be achieved by any subset (non-empty) is the minimal possible sum. Then, the maximum sum is S plus twice the absolute value of that minimal sum (if it's negative). Otherwise, if all subsets are positive, then flipping nothing gives S.

So the problem reduces to: find the minimal sum of any non-empty subset of the elements. Then, the maximum sum is S + max(0, -2*min_subset_sum).

Wait, no. Because the formula is S - 2*K, where K is the sum of the subset. If K is negative, then S - 2*K = S + 2*|K|. So the maximum between S and S - 2*K (if K is negative). So the overall maximum is the maximum of (S - 2*K, S). So we can choose to flip the subset if K is negative (so that the sum increases by 2*|K|), or not flip otherwise.

Therefore, the maximum possible sum is the maximum between S (if we don't flip anything) and (S - 2*K) where K is the minimal possible subset sum (could be negative). So the maximum sum is max(S, S - 2*K). Since S is fixed, this is equivalent to S - 2*min(K, 0). Because if K is negative, then S - 2*K is larger than S. If K is non-negative, then S is larger.

Thus, the problem is to compute the minimal sum of any non-empty subset of the elements. Let's call this K. Then, the answer is max(S, S - 2*K).

So how to compute K, the minimal possible subset sum of the elements (any subset, non-empty) ?

Wait, but the elements can be any subset. For example, in the first test case:

Elements are -2, 3, -3.

The possible non-empty subsets and their sums:

-2 → -2

3 →3

-3 →-3

-2+3 →1

-2-3 →-5

3-3 →0

All three: -2+3-3 =-2.

So the minimal subset sum is -5 (sum of -2 and -3). So the maximum sum is S (sum of all elements: -2+3-3 =-2) minus 2*(-5) → -2 +10=8. Which matches the example.

So the solution is to find the minimal possible subset sum among all non-empty subsets of the array. Then compute max(S, S - 2*K), where K is that minimal sum.

Wait, but how to compute the minimal subset sum?

Wait, the minimal subset sum can be any subset of elements. Not necessarily contiguous in the original array, but in the rearranged array, they can be contiguous. So the minimal sum is the minimal possible sum of any non-empty subset of the elements, regardless of their order. But since the elements can be arranged in any order, the minimal subset sum is the minimal possible sum of any non-empty subset of the elements.

Wait, but in the arrangement, the subset can be contiguous. So any subset of the elements can be arranged as a contiguous block. Therefore, the minimal possible K is the minimal sum of any non-empty subset of the elements.

So the problem reduces to:

For each test case:

1. Compute the sum S of all elements.

2. Find the minimal sum K of any non-empty subset of the elements.

3. The answer is max(S, S - 2*K).

So the key is to compute K, the minimal possible subset sum.

But wait, the minimal sum can be the sum of any subset of elements, not just a contiguous one in the original array. Because in the rearranged array, any subset can be contiguous.

So the minimal subset sum is the minimal sum of any non-empty subset of the array elements. So K is the minimal sum of any non-empty subset of the array elements.

Ah, that's a crucial insight. So the problem now is to compute for each test case the minimal sum of a non-empty subset of the array. Then, the answer is max(S, S-2*K).

So how to compute K?

The minimal subset sum can be found using a dynamic programming approach, similar to the subset sum problem. But since the elements can be positive or negative, it's a bit more involved.

Let's think. We can model this as follows: for each element, we can choose to include it in the subset or not. We need to track the possible sums and find the minimal one.

The standard approach for subset sum is to track possible sums. Since the elements can be up to 50 elements, each of absolute value up to 100, the total possible sum range is up to 50*100=5000 in magnitude. But since elements can be negative, the possible sums can be as low as -5000 and as high as 5000.

But since the problem constraints for n are small (n up to 50), but for t up to 1000, we need an efficient way to compute K for each test case.

Wait, for n=50, a DP approach would be feasible. Let's see.

We can model this with a DP array that tracks possible sums. For each element, we can add it to the existing subsets or not.

Let's see. The possible sums can range from -50*100 to 50*100, which is a range of 10000. So for each element, we can track all possible sums that can be formed by including or excluding the element.

But for n=50, and t=1000, this might be computationally feasible.

But how to implement this.

Alternatively, considering that we need the minimal sum, perhaps there's a way to track the possible minimal sums. Let's think.

Another approach is to realize that the minimal subset sum can be found by considering all possible subsets. However, this is O(2^n), which for n=50 is impossible. So we need a dynamic programming approach.

The idea is to track all possible sums that can be formed with subsets of the elements.

Initialize a set of possible sums. Start with 0 (sum of empty subset). Then, for each element, for each existing sum in the set, add the element to it and keep track of all possible sums. But since we are looking for the minimal sum, perhaps we can track all possible sums and find the minimal one.

But for n=50, and each element up to 100 in absolute value, the possible sums are up to 50*100=5000 in each direction. So the total possible sums are up to 10001 (from -5000 to 5000). But with 50 elements, the possible sums can be up to ±50*100= ±5000.

But with 50 elements, the number of possible sums could be up to (50 * 100)*2 +1 = 10,001. So for each element, the DP can track all possible sums that can be achieved.

So the steps for a test case:

- Read the array.

- Compute the sum S.

- Compute all possible subset sums (non-empty) and find the minimal sum K.

- The answer is max(S, S - 2*K).

So the key part is to compute K.

Now, let's think about how to compute K.

We can use a dynamic programming approach where we track possible sums. For each element, we can either include it in the subset or not.

But since the elements can be positive or negative, including an element can either decrease or increase the sum.

The approach can be:

Initialize a set of possible sums, initially containing 0 (empty subset). Then, for each element a in the array, we update the set by adding all possible sums that can be formed by including a (sum + a) and the existing sums (sum).

But since we are interested in non-empty subsets, after processing all elements, the minimal sum is the minimal in the set excluding 0.

But how to track this.

Alternatively, we can track all possible sums and keep the minimal one. But during processing, we can track all possible sums and their presence.

So here's a plan:

Initialize a boolean array (or a set) that tracks which sums are possible. Initially, sum 0 is possible (empty subset).

For each element a in the array:

- For each possible sum s that was achievable before adding this element, we can create a new sum s + a.

- Update the possible sums with these new values.

After processing all elements, the possible sums are all the subset sums of the array, including the empty subset. So we need to find the minimal sum among all subset sums except the empty subset (sum 0).

But wait, the empty subset is not allowed. So K is the minimal subset sum of any non-empty subset. So after processing all elements, the possible sums are all subset sums (including empty). We need to find the minimal sum in the set of sums, excluding 0. If all elements are non-negative, then the minimal sum is the smallest element, but if there are negative elements, it could be the sum of some combination.

So the algorithm for K:

Initialize a set (or a boolean array) of possible sums. Start with 0 (empty subset). For each element a in the array, generate new possible sums by adding a to existing sums. After processing all elements, collect all possible sums (excluding 0) and find the minimal one.

This can be implemented using a dynamic programming approach with a set.

But for efficiency, we can use a bitmask-like approach, tracking possible sums with a list or a boolean array.

Let's consider the possible sums. For each test case, the elements can be in the range [-100,100], and n up to 50. So the minimal possible sum is -50*100 = -5000, and the maximum is 5000.

So the possible sums range from -5000 to 5000. That's 10001 possible values.

We can represent this with a boolean array of size 10001, where each index represents a possible sum. Since the minimal possible sum is -5000, we can shift the index by 5000. So index 0 represents sum -5000, index 1 represents sum -4999, ..., index 10000 represents sum 5000.

So the steps are:

1. For each test case:

   a. Read the array.

   b. Compute S.

   c. Compute all possible subset sums.

   d. Find the minimal subset sum (non-empty), K.

   e. The answer is max(S, S - 2*K).

2. To compute K:

   a. Initialize a boolean array dp of size 10001, where dp[i] is True if the sum (i - 5000) is possible.

   b. Initialize dp[5000] = True (sum 0).

   c. For each a in the array:

      i. Create a new array next_dp, initially a copy of dp.

      ii. For each possible sum s (represented by index j in dp) where dp[j] is True:

          new_sum = (j - 5000) + a

          new_index = new_sum + 5000

          if new_index is between 0 and 10000, set next_dp[new_index] to True.

      iii. Update dp to be next_dp.

   d. After processing all elements, iterate through all possible sums (indices in dp) where the sum is not zero (i.e., j != 5000), and dp[j] is True. Find the minimal (j -5000).

   e. If no such sum (only sum 0 is possible), then K is 0. But wait, since all elements are zero, any subset sum is zero. So K is zero.

But how can that be? Because the array may consist of all zeros. Then the minimal subset sum is zero, so the answer is S (which is zero) - 2*0 = zero, which is correct.

So, for the array [0], the possible subset sums are 0 (non-empty). So K is zero, answer is max(0, 0-0) =0.

So the DP approach will correctly find K as the minimal subset sum.

Now, implementing this in Python.

But wait, how to handle the shifting. For each possible sum, we add 5000 to get the index. For example, sum -5000 is index 0, sum 0 is 5000, sum 5000 is 10000.

So the steps for the DP:

Initialize a list of 10001 elements, all False. Then set dp[5000] = True (sum 0).

For each a in the array:

   create a new list next_dp as a copy of the current dp.

   for each j in 0..10000 where dp[j] is True:

       current_sum = j -5000

       new_sum = current_sum + a

       new_j = new_sum +5000

       if 0 <= new_j <= 10000:

           next_dp[new_j] = True

   dp = next_dp

But this approach could be time-consuming for n=50 and t=1000, but given the constraints, perhaps it's manageable.

Wait, for each test case, the DP loop runs n times. For each element, we iterate over all 10001 possible sums. For each element, the time per test case is O(10001 * n). For n=50, that's 50*10001 = 500,050 operations per test case. And with t=1000, that's 500 million operations. Hmm, that's a lot. But wait, in Python, 500 million operations would be way too slow. So this approach might not be feasible for n=50 and t=1000.

Wait, but n is up to 50, and t is up to 1000. So 50*1000=50,000 test elements. But each test case has n up to 50, so the total number of elements across all test cases is up to 50 * 1000 = 50,000.

But each element in a test case requires O(10001) steps. So 50,000 * 10001 = 500,050,000 operations. That's half a billion operations. In Python, that might be tight but manageable, especially since each operation is simple (checking a boolean and updating another array).

Alternatively, perhaps we can optimize by tracking possible sums as a set. For each test case, we start with a set containing 0. Then, for each element, we add to the set all elements (s + a) where s is in the current set. Then, after processing all elements, the minimal sum is the minimal element in the set (excluding zero).

But for n=50, the size of the set could grow exponentially. For example, if all elements are distinct and not overlapping in their sum, the number of possible sums can be up to 2^50, which is impossible. But since the elements can be up to 100 in absolute value, and n=50, the possible sums are bounded between -5000 and 5000. So the maximum possible number of sums is 10001, so the set approach can be feasible. Because even if you process 50 elements, each element can add up to 10001 possible sums. So using a set for each test case would have O(50 * 10001) operations, which is acceptable.

So here's an alternative approach:

For each test case:

   Read array.

   Compute S.

   Initialize a set of possible sums, starting with 0.

   For each a in array:

       new_sums = set()

       for s in current_sums:

           new_sums.add(s + a)

       current_sums = current_sums.union(new_sums)

   Then, the possible subset sums are all elements in current_sums except 0 (since the empty subset is 0). Find the minimal sum in current_sums, excluding 0.

   If the minimal sum is <=0, then the answer is S - 2*K. Else, the answer is S.

But this approach uses sets to track possible sums, and for each element, it iterates through the current sums and adds new ones. However, since the possible sums are limited to [-5000, 5000], the size of the set is bounded by 10001 elements. So for each element, the loop over the set is O(10001) steps. For 50 elements, that's 50*10001 steps per test case.

This is the same as the DP approach, but in practice, using sets in Python might be slower than using a boolean array. So perhaps the boolean array approach is more efficient.

So, let's proceed with the boolean array approach.

Implementing this in Python:

We can precompute the offset (5000) and use a list of booleans to track possible sums.

So code steps:

Read t test cases.

For each test case:

   Read n.

   Read the list of a.

   Compute S = sum(a).

   Initialize dp as [False] * 10001. dp[5000] = True (sum 0 is possible).

   For each num in a:

       next_dp = dp.copy()

       for j in range(len(dp)):

           if dp[j]:

               current_sum = j -5000

               new_sum = current_sum + num

               new_j = new_sum +5000

               if 0 <= new_j < 10001:

                   next_dp[new_j] = True

       dp = next_dp

   # Now, find the minimal sum in dp (excluding 0)

   min_sum = float('inf')

   for j in range(len(dp)):

       if dp[j] and (j !=5000):

           current_sum = j -5000

           if current_sum < min_sum:

               min_sum = current_sum

   # If no non-zero sum (impossible, since n >=1)

   if min_sum == float('inf'):

       # This can only happen if all elements are zero. Then the minimal subset sum is zero.

       min_sum =0

   ans = max(S, S - 2*min_sum)

   print(ans)

Wait, but what if the array has all elements zero? Then, the possible subset sums are 0 (since any non-empty subset sum is zero). So K is zero. So the answer is max(S, S -2*0) → S. Which is correct.

But in the code above, when min_sum is float('inf'), which happens when there are no non-zero sums possible. That is, when all possible subset sums are zero (the array is all zeros). But for an array of all zeros, the minimal sum is zero. So the code correctly handles this by setting min_sum to zero.

But the code as written would set min_sum to zero only when all possible subset sums are zero. But in that case, the for loop would find that all j in dp are either 5000 (sum zero) or other values (but since all subsets are zero, dp[j] is True only when j is 5000). So the for loop would not find any j !=5000. Hence, min_sum remains infinity, and the code sets min_sum to zero.

But for example, the input case where the array is [0], then the possible subset sums are 0. So the code would set min_sum to zero. The answer is max(0, 0-0) =0. Correct.

So the code should handle this case correctly.

Now, test the sample inputs.

Sample Input 1:

3

-2 3 -3

Sum S is -2+3-3 = -2.

The possible subset sums are:

-2,3,-3, (-2+3)=1, (-2-3)=-5, (3-3)=0, (-2+3-3)= -2.

So the minimal sum is -5.

The answer is S - 2*(-5) → -2 +10=8. Which matches the sample.

Sample Input 2:

1

0

Sum is 0. The minimal subset sum is 0. Answer is max(0, 0-0) =0.

Sample Input 3:

2

0 1

Sum is 1. The possible subset sums are 0,1,0+1=1. So minimal sum is 0 (subset {0}).

So answer is max(1, 1-2*0) =1.

Sample Input 4:

1

-99

Sum is -99. Minimal subset sum is -99. Answer is -99 -2*(-99) =99.

Sample Input 5:

4

10 -2 -3 7

Sum is 10-2-3+7=12.

The minimal subset sum is the sum of -2 and -3: -5. So answer is 12 -2*(-5) =12+10=22.

Sample Input 6:

5

-1 -2 -3 -4 -5

Sum is -15. The minimal subset sum is sum of all elements: -15. Answer is -15 -2*(-15) =-15 +30=15.

Sample Input 7:

6

-41 22 -69 73 -15 -50

Sum is -41 +22 is -19, -19-69 is -88, +73 →-15, -15-15= -30, -30-50= -80.

The minimal subset sum. Let's see. The elements are negative and positive. What's the subset with the most negative sum?

For example, the subset {-41, -69, -15, -50} sum is -41-69-15-50 = -175. So the answer would be sum S is -80, then the answer is -80 -2*(-175) =-80 +350=270. Which matches the sample output.

Sample Input 8:

12

1 2 3 ...12 → sum is 78. All elements are positive. The minimal subset sum is 1. But since it's positive, flipping would not be done. So answer is 78.

So the code should handle all these cases correctly.

Now, code implementation.

But in Python, the for loop for each j in 0..10000 could be slow. So how can we optimize this?

Alternative approach: for each element, we can generate all possible new sums by adding the element to existing sums. But using a set for the possible sums.

But perhaps using a set-based approach with bitmasking. Let's see.

Another approach is to use a bitmask (a list of booleans) and for each element, we can generate new sums by adding the element to existing sums.

But in code, the way to do this is:

Initialize a list dp of 10001 elements, all False. Set dp[5000] = True.

Then for each num in the array:

   Create a new list next_dp, which is a copy of dp.

   For each j in 0..10000 where dp[j] is True:

       new_j = j + (num). But wait, j is the index, which represents sum s = j -5000.

       So adding num to s gives s + num = (j -5000) + num.

       The new index is (s + num) +5000 = j + num.

       So for example, j is 5000 (sum 0), adding a num of -5 would make new_j = 5000 + (-5) =4995, which represents sum -5.

       So new_j is j + num.

       So for each j where dp[j] is True, new_j can be j + num. If new_j is within 0 <= new_j <=10000, then next_dp[new_j] is True.

So, in code:

for each num in a:

    next_dp = [x for x in dp]  # copy

    for j in range(10001):

        if dp[j]:

            new_j = j + num

            if 0 <= new_j <= 10000:

                next_dp[new_j] = True

    dp = next_dp

Wait, but this is not correct. Because j represents sum s = j -5000. So when we add num to s, the new sum is s + num = (j -5000) + num. The new index is (s + num) +5000 = j -5000 + num +5000 = j + num. So yes, new_j is j + num.

Thus, the code can be written as:

for each num in the array:

    next_dp = dp.copy()

    for j in range(10001):

        if dp[j]:

            new_j = j + num

            if 0 <= new_j <= 10000:

                next_dp[new_j] = True

    dp = next_dp

So this way, we avoid converting j to sum and back. We can directly compute new_j as j + num.

But this is only correct if the sum is (j -5000). So adding num to the sum is equivalent to adding num to j (the index). Because (j -5000) + num = (j + num) -5000.

Yes. So this code is equivalent to the previous approach, but more efficient as it avoids recomputing the sum.

Thus, this code is correct.

So the code for the DP part is as follows:

Read the array.

Initialize dp = [False] * 10001.

dp[5000] = True.

For each num in a:

   next_dp = dp.copy()

   for j in range(10001):

       if dp[j]:

           new_j = j + num

           if 0 <= new_j <= 10000:

               next_dp[new_j] = True

   dp = next_dp

Then, find the minimal sum (j-5000) where j is in 0..10000, dp[j] is True, and j !=5000.

So the code:

min_sum = float('inf')

for j in range(10001):

    if dp[j] and j !=5000:

        s = j -5000

        if s < min_sum:

            min_sum = s

if min_sum == float('inf'):

    min_sum =0

ans = max(S, S - 2*min_sum)

print(ans)

This should work.

Testing the sample input 1:

Test case 1: array [-2, 3, -3]

Processing first element -2:

dp starts as all False except 5000 (sum 0).

next_dp is initially a copy. Then for j=5000 (sum 0), new_j =5000 + (-2) =4998. So next_dp[4998] becomes True.

dp becomes next_dp: 5000 and 4998 are True.

Next element 3:

for j in 0..10000:

if dp[j] is True (j=4998 and 5000).

For j=4998: new_j =4998+3=5001. So next_dp[5001] is True.

For j=5000: new_j =5000+3=5003. So next_dp[5003] is True.

But next_dp was a copy of dp (which has 4998 and 5000 as True). So after processing 3, the next_dp has 4998, 5000, 5001, 5003 as True.

Then, dp becomes this.

Third element is -3:

For each j in next_dp:

current j's are 4998, 5000, 5001, 5003.

For each j in dp:

j=4998: new_j=4998-3=4995 (sum 4995-5000= -5). So next_dp[4995] is True.

j=5000: new_j=5000-3=4997. So next_dp[4997] is True.

j=5001: new_j=5001-3=4998. Already True.

j=5003: new_j=5003-3=5000. Already True.

So after processing all three elements, the possible sums include 4995 (sum -5), 4997 (sum -3), 4998 (sum -2), 5000 (sum 0), 5001 (sum 1), 5003 (sum 3), etc.

So the minimal sum is -5. Which is correct. So ans is S -2*(-5) =-2 +10=8.

So the code works.

Now, code implementation.

So the complete code:

Read t.

for each t:

   read n.

   read list a.

   S = sum(a)

   dp = [False] * 10001

   dp[5000] = True  # sum zero

   for num in a:

       next_dp = dp.copy()

       for j in range(10001):

           if dp[j]:

               new_j = j + num

               if 0 <= new_j <= 10000:

                   next_dp[new_j] = True

       dp = next_dp

   min_sum = float('inf')

   for j in range(10001):

       if dp[j] and j !=5000:

           s = j -5000

           if s < min_sum:

               min_sum = s

   if min_sum == float('inf'):

       min_sum =0

   ans = max(S, S - 2 * min_sum)

   print(ans)

But wait, for the case where the array has all elements zero, then all subset sums are zero. So the code would set min_sum to zero. The answer would be max(0, 0-0) =0, which is correct.

Testing the second sample input:

Test case 2:

1

0

sum is 0.

Processing:

dp starts with 5000 True.

Processing num 0:

for j=5000: new_j =5000+0=5000. But next_dp is a copy of dp, so after processing, next_dp is the same as dp. So after processing, dp still has only 5000 as True.

So the loop for j in dp:

only j=5000. But j !=5000 is false. So min_sum remains infinity. So code sets min_sum to zero.

ans is max(0, 0-0)=0.

Correct.

Test case 3:

2

0 1

sum S=1.

Processing:

Initial dp[5000] = True.

Processing first element 0:

next_dp is copy of dp. Then for j=5000 (sum 0):

new_j=5000+0=5000 (sum 0). So next_dp remains with 5000 as True.

Processing second element 1:

next_dp is copy of current dp (only 5000 True).

for j=5000:

new_j=5000+1=5001 (sum 1). So next_dp[5001] is True.

So after processing, dp has 5000 and 5001 True.

Possible subset sums are 0, 0+1=1, 0+0=0 (but subset can't be empty. Wait, but the code allows all subset sums, including empty. So the code is considering all subsets, including empty. But when we calculate K, we exclude the empty subset sum (sum 0).

So in this test case, the possible subset sums are 0 (empty), 0 (subset with just the first zero), 1 (subset with the second element), 1 (subset with both 0 and 1), 0 (subset with both zeros and the 1? Wait, no. The array is [0,1]. The possible non-empty subsets are:

{0} →0, {1} →1, {0,1} →1.

So the minimal sum is 0. So ans is max(1, 1-0) =1.

Which matches the sample.

In code, after processing both elements, dp has True at 5000 (sum 0), 5001 (sum 1). So when checking, j=5000 is excluded. The other j is 5001 (sum 1). So the minimal sum is 0 (from j=5000?), no. Wait, no. Because the code excludes j=5000. So the possible sums are 1. Wait, but that's not correct.

Wait, the code in this case would have the possible subset sums as 0 (empty), 0 (subset {0}), 1 (subset {1}), and 1 (subset {0,1}).

Wait, but the code tracks all possible subset sums, including empty. So after processing the two elements, the subset sums are:

0 (empty), 0 (just the first element), 1 (just the second), 0+1=1 (subset {0,1}).

So the possible subset sums are 0 and 1. But non-empty subsets are 0 and 1. So the minimal sum is 0.

But in the code, after processing all elements:

dp is True for j=5000 (sum 0), j=5000 (from the first element?), j=5001 (sum 1) from the second element.

Wait, let's walk through the code step by step.

Initial dp: [False] *10001, dp[5000] = True.

First element is 0:

processing this element:

for j in 5000 (True):

new_j =5000 +0 =5000. So next_dp[5000] becomes True. But dp was already True. So next_dp remains same as dp.

After processing first element, dp is still True only at 5000.

Second element is 1:

for j in 5000:

new_j =5000+1=5001. So next_dp[5001] becomes True.

So after processing second element, dp is True at 5000 (sum 0) and 5001 (sum 1).

Now, when checking for j in 0..10000:

j=5000 → sum 0. But excluded because j !=5000 is false.

j=5001 → sum 1.

So the minimal sum is 1. But this is wrong. Because the subset {0} (the first element) has sum 0, which is allowed. So why isn't that sum tracked in the code?

Ah, here's a mistake in the code.

The code is processing the array elements, and for each element, it's adding the current element to all possible subset sums (including the empty subset).

Wait, but the code initializes the dp with sum 0 (empty subset). Then, for each element, it adds the element to the existing subset sums, including the empty subset.

So for the first element (0), the possible subset sums after processing are 0 (empty subset) and 0 +0=0 (subset {0}).

Wait, no. The code adds 0 to all existing subset sums, which includes 0. So new subset sums are 0 (empty) and 0+0=0 (subset {0}).

Wait, no. The way the code works is:

Initially, dp[5000] is True (sum 0, empty subset).

For the first element (0):

for each j where dp[j] is True (j=5000):

   new_j =5000 +0=5000.

so next_dp[5000] becomes True (already True).

So after processing the first element, the possible subset sums are still just sum 0 (empty subset), and sum 0 (subset with first element 0).

But how are these tracked? Because when we process the first element, the code adds 0 to existing sums. So existing sums are [0]. Adding 0 gives 0. So the possible sums are 0 (empty subset) and 0 (subset with first element). But since both are 0, the dp remains True at 5000.

So after processing the first element, the possible sums are 0 (empty subset) and 0 (subset {0}).

So for the second element (1):

for each j where dp[j] is True (5000):

   new_j =5000 +1=5001. So next_dp[5001] is True.

So the possible subset sums after processing both elements are:

- empty subset (0) → dp[5000] True.

- subset {0} → sum 0 → dp[5000] True.

- subset {1} → sum 1 → dp[5001] True.

- subset {0,1} → sum 1 → dp[5001] True.

So the non-empty subset sums are 0 and 1.

But in the code, after processing all elements, the code looks for j where dp[j] is True and j !=5000. So j=5001 (sum 1) is the only such j.

But the subset {0} has sum 0, which is j=5000, which is excluded. So the code's code is wrong in this case.

Ah, this is a problem. The code is excluding j=5000 (sum 0) even though some non-empty subsets sum to zero.

So the code's approach of excluding j=5000 (sum 0) is incorrect. Because the empty subset is sum 0, but non-empty subsets can also sum to zero.

For example, if the array is [0], the only non-empty subset sum is 0. But the code would exclude j=5000, leading to min_sum being set to 0 via the if min_sum == inf condition.

But in the case of the third test case, the subset {0} is a valid non-empty subset with sum 0. But the code is excluding j=5000, which is sum 0. So the code would not find that sum and would compute the minimal sum as 1, leading to the answer max(1, 1-2*1) = max(1, -1) →1, which is correct. But wait, the answer should be 1. But why is the subset {0} allowed in the third test case?

Wait, in the third test case, the array is [0,1]. The possible non-empty subsets are:

{0}: sum 0.

{1}: sum 1.

{0,1}: sum 1.

So the minimal subset sum is 0. So the answer is max(1, 1-2*0) =1.

But according to the code, after processing the elements, the possible non-empty subset sums are 0 and 1. But the code is excluding j=5000 (sum 0) even though it is a valid non-empty subset sum. So why?

Ah, the problem is that the code considers all subset sums, including the empty subset. But when we generate the possible sums, the empty subset is sum 0 (j=5000). Non-empty subsets that sum to 0 are also represented by j=5000. So the code excludes all sums that are zero, including those from non-empty subsets.

This is a bug.

So the code is incorrect. It excludes all subset sums of zero, but some of those are from non-empty subsets. So the code is missing those cases.

So how to fix this?

We need to track whether the subset sum is zero but comes from a non-empty subset.

This complicates the approach. Because the subset sum of zero can be from the empty subset (which is not allowed) or from a non-empty subset (like [0]).

Thus, the current approach cannot distinguish between these two cases.

Therefore, the code as written is incorrect for cases where there are non-empty subsets that sum to zero.

For example, the third test case:

The code finds that j=5000 is True (sum 0), but excludes it. But there is a non-empty subset (the subset {0}) that sums to zero. So the code's current approach is incorrect.

Thus, we need to find a way to track whether a sum can be achieved by a non-empty subset.

So the solution is to track two things: the possible sums that can be formed by non-empty subsets. Then, find the minimal sum among those.

But how to track this.

Alternative approach:

We can track two separate sets: one for the empty subset and another for non-empty subsets.

But perhaps a better way is to track the possible sums for non-empty subsets.

So the initial DP starts with empty subset sum (0), and then for each element, the new sums are formed by adding the element to all previous sums (including empty subset).

But we need to track only the sums from non-empty subsets.

Thus, the correct approach is to track the possible sums for non-empty subsets. So, the initial DP is empty. For each element, we add the element to all possible sums formed by previous non-empty subsets, and also the element itself (as a subset containing just the element).

But how to model this.

Alternative approach:

We can track a set of possible sums for non-empty subsets.

Initially, this set is empty.

For each element in the array:

   new_sums = {num} (the subset containing just this element).

   for s in current_set:

       new_sums.add(s + num)

   current_set = current_set.union(new_sums)

Thus, after processing all elements, current_set contains all possible sums of non-empty subsets.

This approach correctly tracks only non-empty subsets.

But this approach is feasible in Python using sets. Let's see.

For example, third test case:

array [0,1]

Processing first element 0:

current_set is empty. new_sums is {0}. current_set becomes {0}.

Processing second element 1:

new_sums is {1}.

Then, adding 0 +1=1. So new_sums becomes {1, 1} → {1}.

current_set is {0} union {1} → {0,1}.

Thus, the possible non-empty subset sums are 0,1. The minimal is 0. So the answer is max(1, 1-2*0) =1. Correct.

Thus, this approach correctly includes the subset {0} sum 0.

So the code should use this approach.

Thus, the code should track possible sums of non-empty subsets.

But how to implement this using a boolean array.

Let's think.

Initially, no sums are possible (since no non-empty subsets).

For each element in the array:

   temp = new possible sums generated by adding this element to existing sums.

   Also, include the element itself (as a subset consisting of only itself).

   So, for the first element, the sum is the element itself.

   For subsequent elements, the new sums are existing sums + element, and the element itself.

Thus, the correct way to model this is:

Initialize a set of possible non-empty subset sums. Start as empty.

For each element in the array:

   new_sums = set()

   new_sums.add(element)  # subset containing only this element.

   for s in current_sums:

       new_sums.add(s + element)

   current_sums = current_sums.union(new_sums)

Thus, after processing all elements, current_sums contains all possible non-empty subset sums.

This approach is correct.

But for n=50, and possible sums up to 5000 in absolute value, this approach can be implemented using a boolean array.

But the code needs to track the possible sums of non-empty subsets.

So the code would need to initialize a boolean array where dp[j] is True if there exists a non-empty subset that sums to (j -5000).

So the steps are:

Initialize dp as [False] * 10001.

For each element in the array:

   create a temporary array temp_dp to track new sums.

   temp_dp is initially all False.

   for each j in 0..10000:

       if dp[j] is True:

           new_j = j + element

           if 0 <= new_j <=10000:

               temp_dp[new_j] = True

   # add the element itself (as a subset of size 1)

   element_j = 5000 + element

   if 0 <= element_j <=10000:

       temp_dp[element_j] = True

   # merge temp_dp into dp:

   for j in 0..10000:

       if temp_dp[j] or dp[j]:

           dp[j] = True

Thus, this way, dp tracks all possible sums of non-empty subsets.

Let's see:

For the third test case:

Processing first element 0:

temp_dp is initialized to all False.

Add the element_j =5000+0=5000. So temp_dp[5000] =True.

merge into dp: dp becomes temp_dp → True at 5000.

Processing second element 1:

temp_dp is all False.

For j in dp where True (j=5000):

   new_j =5000+1=5001. So temp_dp[5001] =True.

Then, add element_j =5000+1=5001. So temp_dp[5001] is already True.

Merge into dp:

dp[j] becomes True for 5000 and 5001.

Thus, the possible sums are 0 and 1. The minimal is 0. So the answer is correct.

Thus, the code needs to be modified to track non-empty subset sums.

So the revised code is:

For each test case:

   Read n and the array.

   sum_S = sum(a)

   dp = [False] * 10001

   for num in a:

       temp_dp = [False] * 10001

       # Add subsets that include this num.

       # First, subsets formed by adding num to existing subsets.

       for j in range(10001):

           if dp[j]:

               new_j = j + num

               if 0 <= new_j <=10000:

                   temp_dp[new_j] = True

       # Add the subset consisting of only this num.

       element_j = 5000 + num

       if 0 <= element_j <=10000:

           temp_dp[element_j] = True

       # Merge temp_dp into dp.

       for j in range(10001):

           if temp_dp[j]:

               dp[j] = True

   if not any(dp):

       # array is empty? But n >=1.

       # But if all elements are such that their sum is out of range.

       # but according to the problem statement, n >=1.

       # So this case is impossible.

       # But for safety, set K=0.

       min_sum =0

   else:

       min_sum = min( (j-5000) for j in range(10001) if dp[j] )

   ans = max(sum_S, sum_S - 2*min_sum)

   print(ans)

This code correctly tracks non-empty subset sums.

So the code now correctly handles the third test case.

Let's re-examine test case 3:

After processing first element 0:

temp_dp is initialized, then element_j=5000. So temp_dp[5000] is True.

Merge into dp: dp[5000] is True.

Processing second element 1:

temp_dp is initialized.

For j in dp where True (5000):

   new_j =5000+1=5001. So temp_dp[5001] is True.

Add element_j=5000+1=5001 → temp_dp[5001] is True.

Merge into dp: dp[5000] and 5001 are True.

Thus, the possible sums are 0 and 1.

The minimal sum is 0.

So ans is max(1, 1-0) =1.

Correct.

Another example: test case 4 (array [-99]):

Processing the element -99:

temp_dp is initialized.

Add element_j=5000 + (-99) =4901 → sum 4901-5000= -99.

So temp_dp[4901] is True.

Merge into dp: dp[4901] is True.

Thus, the minimal sum is -99.

Ans is sum_S (which is -99) -2*(-99) →-99+198=99.

Correct.

Thus, the code is now correct.

But how to handle the case where the array has elements that sum to a value outside the possible range. For example, an array with elements summing to -6000, which is outside the range. But in the code, the element_j is clamped to the range 0..10000.

Wait, no. For example, if num is -6000, then element_j=5000 + (-6000) =-1000 → j= -1000, which is <0. So element_j is not added to temp_dp.

But according to the problem constraints, the array elements are between -100 and 100, and n is up to 50.

So the minimal possible sum for a subset is -50*100= -5000. Which is within the range. So no element_j will be out of range.

Thus, the code is safe.

Thus, the code should now handle all test cases correctly.
</think>

```python
def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        n = int(input[idx])
        idx +=1
        a = list(map(int, input[idx:idx+n]))
        idx +=n
        sum_S = sum(a)
        dp = [False]*10001
        for num in a:
            temp_dp = [False]*10001
            # Add subsets formed by adding num to existing subsets
            for j in range(10001):
                if dp[j]:
                    new_j = j + num
                    if 0 <= new_j <=10000:
                        temp_dp[new_j] = True
            # Add subset consisting of only this num
            element_j = 5000 + num
            if 0 <= element_j <=10000:
                temp_dp[element_j] = True
            # Merge temp_dp into dp
            for j in range(10001):
                if temp_dp[j]:
                    dp[j] = True
        # Find the minimal sum
        min_sum = 0
        found = False
        for j in range(10001):
            if dp[j]:
                current = j -5000
                if not found or current < min_sum:
                    min_sum = current
                    found = True
        ans = max(sum_S, sum_S - 2*min_sum)
        print(ans)

if __name__ == "__main__":
    main()
```