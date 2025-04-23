<think>
Okay, let's tackle this problem. So, the problem is about Alice choosing a consecutive segment of cards and Bob removing one card from that segment to minimize the score. We need to find the maximum possible score after Bob's removal. Hmm.

Let me think. The key here is that Alice picks a segment [l, r], and then Bob removes the card j in that segment which causes the total sum of the remaining cards to be as small as possible. So for each possible segment, we have to consider the sum of the segment minus the maximum element (since Bob would remove the maximum element to minimize the sum, right?), but wait wait. Wait, no. Wait, the score is sum of the segment minus the card Bob removes. But Bob wants to minimize the score, so he will remove the card that has the maximum value in the segment. Because subtracting the maximum gives the smallest possible sum. So the score for a segment [l, r] is (sum of a_l to a_r) minus the maximum element in [l, r]. But wait, if the segment has length 1, then the score is 0. So in that case, sum minus the single element (since it's the only one) gives 0.

So the problem reduces to: find the maximum value of (sum of segment - maximum in segment) over all possible non-empty segments. And for segments of length 1, that sum is 0.

So our task is to compute, for all possible consecutive segments, the sum of the segment minus the maximum in the segment, then take the maximum of all those values. But how do we do that efficiently?

The constraints are up to n=1e5. So any O(n^2) approach is impossible. So we need an O(n) or O(n log n) solution.

So the question is, how to compute for all possible segments the (sum - max) and find the maximum of these, but efficiently.

Hmm. Let's think about how to model this. Let's consider for each possible segment [l, r], sum(l, r) - max(l, r). We need the maximum of this over all l <= r.

The challenge is that for each segment, we need the sum and the maximum. The sum can be computed quickly with a prefix sum array, but the maximum is tricky. For each segment, the maximum can be found using a sliding window or a segment tree, but even that would take O(n^2) time in the worst case, which is not feasible.

Wait, perhaps there's a smarter way. Let's think: the optimal segment must have certain properties. For example, maybe the maximum element is the smallest possible, so that when subtracted, the sum is as large as possible. Alternatively, perhaps the sum is as large as possible, and the maximum is as small as possible. But how to combine these two.

Alternatively, perhaps we can model this as sum of the segment minus the maximum element. So the problem is equivalent to finding a segment where (sum - max) is maximized.

So, for a given segment, the value is (sum) - (max). So how can we maximize this? For each possible segment, compute this value.

But how?

Hmm. Let's think of the maximum element in the segment. For each element a[i], consider it as the maximum in some segments. Then for those segments, the value would be sum of the segment minus a[i]. So for each a[i], we can find the best possible segment where a[i] is the maximum, and compute (sum - a[i]) for those segments. Then take the maximum over all a[i] and their best segments.

But how to do that?

Alternatively, perhaps we can split the problem into two parts: for each possible segment, sum and max. We need sum - max. So to maximize sum - max, we can consider that sum is (sum of elements) and max is subtracted. So higher sum is good, lower max is good. But we need to find a segment where sum is as high as possible and max is as low as possible, but these are conflicting goals.

Hmm. But perhaps the optimal solution is a segment that includes a lot of positive numbers but has a small maximum. Or maybe even a segment where the sum is high even after subtracting the max. For example, if a segment has sum 10 and the max is 5, then the value is 5. Another segment with sum 8 and max 3 gives 5 as well. So the same value.

But how to find this efficiently.

Another angle: the maximum of sum - max over all subarrays. Let's see for small examples.

Take the first example: 5, -2, 10, -1,4. The entire array sum is 5-2+10-1+4 = 16. Max is 10. So 16-10=6. Which is the answer.

In the second example: [5,2,5,3,-30,-30,6,9]. The best is [1,4], sum is 5+2+5+3=15. Max is 5. So 15-5=10.

So the approach here is to find a segment where sum is high and the max is as low as possible given that sum.

But how to compute this for all possible segments.

Alternative idea: For each possible subarray, the value is (sum - max). Let's think about how to compute this for all possible subarrays and find the maximum.

But again, how to compute this efficiently.

The sum can be computed with prefix sums. The max can be found using a segment tree for range maximum queries, but even then, for each possible segment, querying the max would take O(1) with O(n) preprocessing. But there are O(n^2) possible segments, which is not feasible.

So we need a way to process this without checking every possible segment.

Wait, but maybe the optimal solution is a segment where all elements except the maximum contribute to the sum. For example, the maximum is subtracted. So the best is a segment where the sum is as high as possible, but with the maximum being as small as possible given that sum.

Alternatively, perhaps for some subarrays, the maximum is the minimal possible for their sum. But not sure.

Another approach: For each possible subarray, the value is sum minus the maximum. Let's think of all possible subarrays and compute this value.

But to compute all of these, we need to find for each possible subarray its sum and its maximum. But doing this naively is O(n^2), which is impossible for n=1e5.

Hmm. So the problem is similar to finding for all subarrays the (sum - max), and finding the maximum of that. But how?

Wait, but perhaps the maximum (sum - max) can be achieved by a subarray where all elements except the maximum are positive. So that even after removing the max, the sum is high. Or maybe even when the max is positive, but other elements contribute enough.

Alternatively, maybe the best segments are those where the maximum is the smallest possible. So for example, a segment with all elements negative except one. Then the sum would be sum of the negatives plus the max, subtract the max gives sum of the negatives. But if all elements are negative, then sum of the segment minus the max (which is the largest negative, so least negative) would give a sum that's even more negative. So perhaps in such cases, the best is a segment of length 1, which gives 0.

So the key is to find segments where sum - max is as large as possible. How?

Alternative approach: for each element in the array, consider it as the maximum in a subarray, and find the maximum (sum - a[i]) for all subarrays where a[i] is the maximum. Then, take the maximum over all elements.

But how to find, for each a[i], the maximum sum of a subarray where a[i] is the maximum. Then subtract a[i] from that sum. Then compare all these.

But how to compute that.

This approach is similar to the problem of finding for each element the maximum sum of a subarray where the maximum is that element.

If we can find for each a[i], the maximum sum of a subarray where a[i] is the maximum, then for each i, the value is sum - a[i], and the maximum over all these would be the answer.

But how to compute that.

Hmm. Let's think. For each element a[i], the maximum sum of a subarray where a[i] is the maximum. So the subarray must include a[i], and all elements in the subarray are <= a[i]. And among all such subarrays where a[i] is the maximum, we need the one with the maximum sum.

Then for that sum, subtract a[i], which gives the value (sum - a[i]). We take the maximum of all such values across all i.

But how to find for each a[i], the maximum sum of a subarray where a[i] is the maximum.

This seems like a problem that can be approached using a monotonic stack to track the next greater elements, and find the ranges where a[i] is the maximum.

Wait, this is a standard problem in arrays. For each element, find the maximum subarray where it is the maximum. The approach involves using a monotonic stack to find for each element the left and right boundaries where it is the maximum. Then, within those boundaries, find the maximum subarray sum that includes a[i].

But how.

Alternatively, for each a[i], the left and right boundaries are the first elements to the left and right that are greater than a[i]. So the maximum subarray where a[i] is the maximum must lie between left+1 and right-1. Then, within that range, the maximum subarray sum that includes a[i] can be found by finding the maximum prefix sum from i to left, and the maximum suffix sum from i to right.

Wait, perhaps I'm recalling some techniques from the Largest Rectangle in Histogram problem, but here it's a bit different.

Alternatively, let's think of the problem where for each a[i], we need to find the range where a[i] is the maximum. The left boundary is the first element to the left that is greater than a[i], and the right boundary is the first element to the right that is greater than or equal to a[i], or something like that, depending on whether we allow duplicates.

Once we have that range, the maximum sum subarray that includes a[i] and has a[i] as the maximum would be the subarray within that range. Then, for that subarray, the sum is computed, and then we subtract a[i] to get the value for the problem.

But how to compute this.

Alternatively, for each a[i], the maximum possible sum of a subarray where a[i] is the maximum can be found by expanding to the left and right as much as possible, but only including elements <= a[i]. However, the sum could be improved by selecting a smaller interval that includes a[i], but with higher sum.

But how?

Alternatively, here's an approach inspired by the Kadane's algorithm. Let's think of for each element a[i], find the maximum sum subarray that includes a[i], and in which a[i] is the maximum element. Then, for each such subarray, compute sum - a[i], and take the maximum over all.

To compute this for all elements efficiently, perhaps we can use a monotonic stack approach to find the left and right boundaries for each element where it's the maximum, and then use some precomputed prefix sums to find the maximum sum within those boundaries.

So here's a possible plan:

1. Precompute for each a[i], the left and right boundaries where a[i] is the maximum. For example, left[i] is the index of the last element to the left of i that is greater than a[i], and right[i] is the index of the first element to the right of i that is greater or equal to a[i]. This way, the range (left[i]+1, right[i]-1) is the maximal range where a[i] is the maximum element.

2. For each a[i], the subarrays where a[i] is the maximum must lie within [L, R] where L is left[i]+1 and R is right[i]-1.

3. Now, within this range, the maximum subarray sum that includes a[i] can be computed by finding the maximum prefix sum to the left of i (within L to i) and the maximum suffix sum to the right of i (within i to R). The total sum would be (max_prefix) + (max_suffix) - a[i], because a[i] is included in both.

Wait, maybe not. Let me think. The maximum subarray sum that includes a[i] and is within [L, R] can be the sum from l to r where l is in [L, i], r is in [i, R], and the sum is maximized. To find this, perhaps we can split it into two parts: the maximum sum from L to i (inclusive) ending at i, and the maximum sum from i to R (inclusive) starting at i. Then the total sum is the sum of the left part and the right part minus a[i] (since a[i] is counted in both).

But how to compute these efficiently.

Alternatively, for each i, once we have the boundaries L and R, we can compute:

left_max = maximum sum of a subarray ending at i, within [L, i].

right_max = maximum sum of a subarray starting at i, within [i, R].

Then the maximum sum for a subarray that includes i and is within [L, R] is left_max + right_max - a[i].

Because the left_max is the maximum sum from L to i, and right_max is the maximum sum from i to R. Combining them gives the maximum sum for a subarray that starts anywhere in L..i and ends anywhere in i..R.

But since a[i] is counted twice in left_max and right_max, we subtract it once.

Then, the maximum sum for a subarray where a[i] is the maximum is (left_max + right_max - a[i]). Then subtract a[i] from that sum (since Bob removes a[i], which is the maximum) to get the value (left_max + right_max - a[i] - a[i]) = left_max + right_max - 2*a[i].

Wait no. Wait, the sum of the subarray is left_max + right_max - a[i], and then subtract a[i] (the maximum) gives (left_max + right_max - a[i]) - a[i] = left_max + right_max - 2*a[i].

But wait, no. The sum is left_max (sum from some l to i) plus right_max (sum from i+1 to r) plus a[i]. Wait, maybe not. Let me re-express this.

Wait, left_max is the maximum sum of a subarray ending at i. For example, from some l' to i, where l' >= L and <=i.

right_max is the maximum sum of a subarray starting at i. For example, from i to some r' <= R.

But when you combine these, you can't just add them because i is included in both. So the combined sum would be left_max (sum from l' to i) plus (sum from i+1 to r'), which is left_max + (right_max - a[i]). Because the right_max starts at i, but the sum from i to r' is a[i] + sum from i+1 to r'. So the right_max can be written as a[i] + sum(i+1 to r'). So when you combine left_max (sum from l' to i) and sum from i+1 to r', the total sum is left_max + sum(i+1 to r') = left_max + (right_max - a[i]).

Thus the total sum is left_max + (right_max - a[i]) = left_max + right_max - a[i]. Then subtract the maximum (a[i]) gives (left_max + right_max - a[i]) - a[i] = left_max + right_max - 2a[i].

So the value for this subarray is left_max + right_max - 2a[i].

But wait, this is for the subarray that combines the left part and the right part. But maybe the maximum sum for the entire range is either the left_max alone, or the right_max alone, or their combination. So we need to consider all possibilities.

Alternatively, for the range [L, R], the maximum subarray sum that includes a[i] and lies within [L, R] can be found by:

max_subarray_sum = max( left_max, right_max, left_max + right_max - a[i] )

But since a[i] is part of both left_max and right_max, adding them would count a[i] twice. So combining them would give a sum of left_max + right_max - a[i]. Which could be larger than either left_max or right_max alone.

So the maximum sum is the maximum of these three possibilities.

Then, the value (sum - a[i]) is (max_subarray_sum - a[i]). So for this case, the value would be (max_subarray_sum - a[i]).

Wait, no. Because the sum of the subarray is max_subarray_sum, and then Bob subtracts a[i], which is the maximum. So the value is sum - a[i], which is (max_subarray_sum - a[i]).

So the value for this subarray is (max_subarray_sum - a[i]).

So the maximum over all such possible subarrays (where a[i] is the maximum) would be (max_subarray_sum - a[i]).

Therefore, for each i, the maximum possible value contributed by subarrays where a[i] is the maximum is (max_subarray_sum - a[i]).

We need to compute this for all i and take the maximum.

So the steps would be:

1. Precompute for each i the left and right boundaries where a[i] is the maximum.

2. For each i, compute the left_max (max sum of a subarray ending at i, within [L, i]).

3. Compute the right_max (max sum of a subarray starting at i, within [i, R]).

4. The max_subarray_sum for i's range is the maximum of (left_max, right_max, left_max + right_max - a[i]).

5. Then, the value for i is (max_subarray_sum - a[i]).

6. Take the maximum of all these values, and also compare with 0 (for segments of length 1).

So the overall approach is O(n) time, assuming that we can compute the left and right boundaries, left_max and right_max efficiently.

Now, how to compute left and right boundaries.

For finding the left and right boundaries where a[i] is the maximum, we can use a monotonic stack approach. This is similar to the problem of finding the next greater element.

For example, for each i, left[i] is the index of the last element to the left of i that is greater than a[i]. The right[i] is the index of the first element to the right of i that is greater than or equal to a[i]. This ensures that the range [left[i]+1, right[i]-1] is the maximal range where a[i] is the maximum.

Wait, why greater than or equal to? Because if an element to the right is equal to a[i], then that element can't be part of a subarray where a[i] is the maximum (since it's equal and in the same subarray). So the right boundary is the first element >= a[i].

Wait, but in the case of duplicates. For example, if the array is [5,5], then the left boundary for the first 5 is -1, the right boundary for the first 5 is 1. So the range is [0, 0], meaning that the first 5 is the maximum in the subarray [0,0]. But the second 5 is part of a subarray [1,1], and also the entire array [0,1] where the maximum is 5. But in this case, the approach would treat each 5 as the maximum in their own ranges. But for the entire array, the maximum is 5, and which element is considered as the maximum? Both are, but how does the stack approach handle this.

Hmm. The way the boundaries are set determines which elements are considered as the maximum for each possible subarray. For example, using a stack approach where for each element, left[i] is the last element > a[i], and right[i] is the next element >= a[i], this ensures that the range [left[i]+1, right[i]-1] is the maximal range where a[i] is the maximum. Because any subarray that includes a[i] and is within this range will have a[i] as the maximum element (since elements to the left are <= a[i], elements to the right are < a[i]).

Wait, not exactly. For example, if right[i] is the first element >= a[i], then any subarray that includes i and extends to the right up to right[i]-1 will have all elements <= a[i]. But since right[i] is >= a[i], the subarray [left[i]+1, right[i]-1] may include elements equal to a[i]. But if the stack approach uses strict inequalities, then perhaps the right[i] is first element greater than a[i], which would allow elements equal to a[i] to be in the same range.

This part is a bit tricky. Let me recall the standard approach for finding the next greater element.

In the standard approach, for next greater element to the right (NGE), we process elements from right to left. For each element, we pop elements from the stack until we find an element that is greater than the current element. The top of the stack is the NGE index. Then push the current element to the stack.

So for left[i], we process the array from left to right. For each i, left[i] is the last element to the left that is greater than a[i]. For right[i], we process from right to left, and find the first element to the right that is greater than or equal to a[i]. Wait, but in this case, the boundaries may vary based on the comparison operators.

Wait, perhaps to find the left and right boundaries where a[i] is the maximum, the correct way is to use a monotonic stack to find the previous greater element and next greater or equal element. Or perhaps the other way around. Let's think.

Suppose we want to find for each i the maximal range where a[i] is the maximum. The left boundary is the last index where the element is greater than a[i], and the right boundary is the first index where the element is greater than a[i]. Then, the range (left[i]+1, right[i]-1) is the maximal range where a[i] is the maximum. Because any element in this range is <= a[i], except for the left and right boundaries. So in this case, for the array [5,5], for the first 5, left[i] is -1, right[i] is 1 (since the next element greater than 5 is not found, so right[i] is n, where n is 2). So the range is [0,1-1] = [0,0]. So for the first 5, the range is [0,0], meaning that the maximum is 5. For the second 5 (index 1), left[i] is 0 (since the element at 0 is 5, which is not greater than 5), and right[i] is 2. So the range is [1, 1]. So each 5 is considered as the maximum in their own single elements. However, the subarray [0,1] has maximum 5, but in our approach, neither of the 5's would be considered as the maximum in that subarray. So this suggests that the approach is not capturing all possible ranges.

Hmm. So perhaps the way to model the left and right boundaries is such that the range [L, R] for a[i] includes all subarrays where a[i] is the maximum. So for example, in the case of [5,5], the subarray [0,1] would have a maximum of 5, but according to the approach, neither 5 is considered as the maximum in that range. Which is a problem.

Wait, but in that case, when considering the first 5 (index 0), the right boundary is 2 (n=2, since there's no element after it that is greater than 5). So the range is [0,1], which is correct. So for index 0, left[i] is -1 (no elements to the left), right[i] is 2 (since no element to the right is greater than 5). So the range is [0, 1], which is the entire array. So for a[i] at index 0, the range is [0,1], and a[i] is the maximum in that range. Then, when processing that i, the left_max and right_max would consider the entire range [0,1], and the sum would be 5+5=10. Then subtract a[i] (5), the value is 5. Which is correct. But according to the problem statement, for a segment of length 2, the score is sum - max. So 5+5-5=5. Which is correct.

So perhaps the way to set the left and right boundaries is: left[i] is the last element > a[i], and right[i] is the first element >= a[i]. Or perhaps left is >= and right is >.

Wait, let me check.

In the standard approach for finding for each element the number of subarrays where it is the maximum, the left and right boundaries are determined as follows:

left[i] is the last index where a[j] >= a[i], and right[i] is the next index where a[j] > a[i]. Then, the number of subarrays where a[i] is the maximum is (i - left[i]) * (right[i] - i).

But this is for counting the number of subarrays. For our problem, perhaps we need to use a similar approach.

Alternatively, perhaps the correct way to set left and right boundaries is:

left[i] is the last index where a[j] > a[i], and right[i] is the first index where a[j] >= a[i]. Then, for any subarray that starts after left[i] and ends before right[i], a[i] is the maximum. Because in this case, any element in that subarray to the left of i is <= a[i], and elements to the right are < a[i]. So the maximum is a[i].

But for duplicate elements, this would split the ranges. For example, in the array [5,5], for the first 5 (index 0), the left[i] is -1 (no element to the left), and the right[i] is 1 (the next element >= 5 is at index 1). So the right[i] is 1. So the range is [0, 1-1] = [0,0]. Which is not correct. So in this case, the first 5 would be considered as the maximum in the subarray [0,0], but the second 5 would be considered as the maximum in the subarray [1,1]. But the entire array's maximum is 5, but no element is considered as the maximum in that range. So this approach would miss that case.

So this suggests that the way of setting left and right boundaries is not correct.

Hmm. This indicates that perhaps the way to set the left and right boundaries is such that left[i] is the last index where a[j] >= a[i], and right[i] is the first index where a[j] > a[i]. Then, the subarrays where a[i] is the maximum would be from left[i]+1 to right[i]-1.

In this case, for the array [5,5], for the first 5 (index 0), left[i] is -1 (since there are no elements before it with a[j] >=5), and right[i] is the first element after 0 where a[j] >5, which is none, so right[i] = n=2. So the range is [0+1, 2-1] = [1,1]. So the first 5 is considered the maximum in subarrays that start and end at 0. The second 5 (index 1) would have left[i] as 0 (since a[0] >=5), and right[i] is 2. So the range is [1,1], so the second 5 is considered the maximum in its own subarray. So the entire array [0,1] would not be considered as a subarray where either 5 is the maximum. But this is wrong, as the maximum is 5. So this approach would miss that.

So perhaps the correct way is to set left[i] as the last index where a[j] > a[i], and right[i] as the first index where a[j] >= a[i]. Then, the range is [left[i]+1, right[i]-1], which allows a[i] to be the maximum in subarrays within that range.

Wait, let's test this for the array [5,5]. For index 0, left[i] is -1 (no elements to the left >5). Right[i] is the first index >=0 where a[j] >=5. That's index 0 itself, but we look for elements after i. So for index 0, right[i] would be index 1 (since a[1] >=5). So the range is [0+1, 1-1] = [0,0]. For index 1, left[i] is 0 (since a[0] >5 is false? a[0] is 5, so 5 is not greater than 5. So left[i] would be the last index where a[j] >a[i]. a[i] is 5. So a[j] has to be greater than 5. There are none, so left[i]=-1. Then right[i] is the first index after 1 where a[j] >=5, which is 2 (n=2). So the range for index 1 is [0+1, 2-1] = [1,1]. So again, the entire array [0,1] is not covered. So this approach would not consider any of the elements as the maximum in that subarray.

This indicates that perhaps the stack approach for left and right boundaries is not capturing the necessary ranges for the problem. So how to handle duplicates?

Alternatively, perhaps the way to handle this is to adjust the comparison operators. For example, for the left boundary, use >=, and for the right boundary, use >. This way, the left[i] is the last index where a[j] >= a[i], and right[i] is the first index where a[j] > a[i]. Then, the range [left[i]+1, right[i]-1] includes all subarrays where a[i] is the maximum.

Wait, let's see. For example, for the array [5,5], for index 0: left[i] is -1 (no elements before). Right[i] is the first element after 0 where a[j] >5. Which is not found, so right[i] is n=2. So the range is [0+1, 2-1] = [0,1]. So for i=0, the range is [0,1], and a[i] is 5, which is the maximum in that range. So when processing i=0, the left_max and right_max would consider the entire range. So the sum would be 5+5=10. Subtract a[i] (5) gives 5. Which is correct. For i=1: left[i] is the last index where a[j] >=5. That's index 0. So left[i]=0. Right[i] is 2. So the range is [0+1=1, 2-1=1]. So for i=1, the range is [1,1]. So the sum is 5, subtract 5 gives 0. So the maximum of 5 and 0 would be 5, which is correct.

So in this case, the approach works. So perhaps the correct way is to find for each element the left and right boundaries as follows:

- left[i] is the last index where a[j] >= a[i], and right[i] is the first index where a[j] > a[i]. Then, the range is [left[i]+1, right[i]-1]. Within this range, a[i] is the maximum.

So in this case, for the array [5,5], the first 5 (index 0) has left[i] =-1, right[i] =2. So range [0,1], and a[i] is the maximum in any subarray within that range. For the second 5 (index 1), left[i] is 0, right[i] is 2. So range [1,1]. So when processing i=0, the subarrays that include i=0 and are within [0,1] are considered, and a[i] is the maximum. So the maximum sum for those subarrays would be 5+5=10. Subtracting 5 gives 5, which is correct.

So this approach seems to handle duplicates correctly.

So now, the plan is:

1. For each element a[i], compute left[i] as the last index to the left where a[j] >= a[i]. Compute right[i] as the first index to the right where a[j] > a[i].

2. For each i, the range is [left[i]+1, right[i]-1]. Within this range, a[i] is the maximum.

3. For each i, compute the maximum subarray sum that includes i and is within this range.

4. The value for i is (sum of that subarray) - a[i].

5. The maximum of all these values and 0 (for length 1 segments) is the answer.

Now, the challenge is to compute left and right arrays efficiently. This can be done using a monotonic stack.

For example, for left[i]:

Initialize an empty stack. Process the array from left to right. For each i:

- While the stack is not empty and a[stack[-1]] < a[i], pop from the stack.

- Now, if the stack is not empty, left[i] is stack[-1]. Else, left[i] = -1.

- Push i to the stack.

Wait, no. Because we need to find the last index j < i where a[j] >= a[i]. So when processing i, we need to pop all elements in the stack that are less than a[i], and the next element in the stack (if exists) is the last j with a[j] >= a[i]. Then left[i] is that j.

Wait, perhaps not. Let me think.

Stack-based approach for left[i] (previous greater or equal):

Initialize stack as empty. For each i in 0..n-1:

- While stack is not empty and a[stack[-1]] < a[i], pop from stack.

- If stack is empty, left[i] = -1. Else, left[i] = stack[-1].

- Push i to stack.

Wait, but this would capture the last element j < i where a[j] >= a[i], because any elements in the stack that are smaller than a[i] are popped. So the stack maintains elements in decreasing order. So for a[i], the elements remaining in the stack after popping are those >= a[i]. So the top of the stack is the last j where a[j] >= a[i]. So left[i] is that j.

Yes, this seems correct.

Similarly, for right[i], we need to find the first j >i where a[j] > a[i]. To compute this, we can process the array from right to left.

Initialize stack as empty. For each i from n-1 downto 0:

- While stack is not empty and a[stack[-1]] <= a[i], pop from stack.

- If stack is empty, right[i] = n. Else, right[i] = stack[-1].

- Push i to stack.

This way, for each i, right[i] is the first index j > i where a[j] > a[i].

Once left and right are computed, the next step is to compute left_max and right_max for each i.

left_max[i] is the maximum sum of a subarray ending at i, within the range [left[i]+1, i].

right_max[i] is the maximum sum of a subarray starting at i, within the range [i, right[i]-1].

These can be computed using Kadane's algorithm, but modified to work within the boundaries.

But how to do this efficiently.

Let's think of computing left_max:

For each i, we can compute the maximum sum ending at i, but only considering elements from left[i]+1 to i.

Similarly, for right_max[i], compute the maximum sum starting at i, considering elements from i to right[i]-1.

So for left_max:

We can precompute a prefix sum array. Then, for each i, the maximum sum ending at i is the maximum between a[i] and (max sum ending at i-1 in the allowed range) + a[i].

Wait, but the allowed range is left[i]+1 to i. So the start of the subarray can be any index >= left[i]+1 and <=i.

So the maximum sum ending at i is the maximum of (prefix_sum[i] - prefix_sum[k]) for k in [left[i], i-1], and also considering a[i] alone.

Alternatively, since prefix_sum[i] is sum of a[0..i], the sum from k+1 to i is prefix_sum[i] - prefix_sum[k].

So the maximum sum ending at i is prefix_sum[i] minus the minimum prefix_sum[k] in the range [left[i], i-1].

Because the minimum prefix_sum[k] would give the maximum difference.

So for each i, left_max[i] = prefix_sum[i] - min_prefix, where min_prefix is the minimum prefix_sum[k] for k in [left[i], i-1].

Similarly, for right_max[i], we need the maximum sum starting at i, which can be found using suffix sums.

Alternatively, for right_max[i], it's the maximum sum from i to r, where r is <= right[i]-1.

So for right_max[i], we can use a suffix sum array. suffix_sum[i] = a[i] + suffix_sum[i+1]. Or perhaps prefix sum again.

Wait, maybe we can use the prefix sum approach for left_max and right_max.

But let's see:

left_max[i] = maximum sum of a subarray ending at i, and starting at any position >= left[i]+1.

So the sum is sum a[k..i], where k >= left[i]+1.

To compute this, the prefix sum array can be used. The sum is prefix_sum[i+1] - prefix_sum[k], where k ranges from left[i]+1 to i.

So the maximum sum is prefix_sum[i+1] - min(prefix_sum[k] for k in [0..i] where k >= left[i]+1 and <=i).

But to compute this efficiently for each i, we need a way to find the minimum prefix_sum in the range [left[i]+1, i].

This can be done using a segment tree for range minimum queries, but building a segment tree would take O(n) time and each query O(logn) time. For n=1e5, this is acceptable.

Similarly for right_max[i], the maximum sum starting at i is the maximum sum of a subarray starting at i and ending at any r <= right[i]-1.

The sum is sum a[i..r] = prefix_sum[r+1] - prefix_sum[i].

To find the maximum of this for r in [i, right[i]-1], we need to find the maximum (prefix_sum[r+1] - prefix_sum[i]).

Which is equivalent to finding the maximum prefix_sum[r+1] in the range [i, right[i]-1], and subtracting prefix_sum[i].

So for right_max[i], we need the maximum prefix_sum[r+1] where r is in [i, right[i]-1]. Then right_max[i] = (max_prefix - prefix_sum[i]).

Thus, the approach is:

Compute prefix_sum array.

For each i:

left[i] = previous greater or equal index.

right[i] = next greater index.

Compute for left_max[i] the minimum prefix_sum in [left[i]+1, i-1], and then left_max[i] = prefix_sum[i] - min_val.

But wait, the subarray can start at any k >= left[i]+1 and end at i. So the sum is prefix_sum[i+1] - prefix_sum[k]. So the maximum sum is prefix_sum[i+1] - (min prefix_sum[k] for k in [left[i]+1, i]).

Wait, because prefix_sum[i+1] is sum from 0 to i. So subtracting prefix_sum[k] gives sum from k to i.

So for left_max[i], the maximum sum ending at i is the maximum over k <= i of (prefix_sum[i+1] - prefix_sum[k]), where k is >= left[i]+1 and <=i.

So the minimum prefix_sum[k] in [left[i]+1, i] gives the maximum difference.

So left_max[i] = prefix_sum[i+1] - min(prefix_sum[k] for k in [left[i]+1, i]).

Similarly, for right_max[i], the maximum sum starting at i is the maximum over r >=i of (prefix_sum[r+1] - prefix_sum[i]), where r <= right[i]-1.

This is equivalent to finding the maximum prefix_sum[r+1] in the range [i, right[i]-1], then subtracting prefix_sum[i].

So right_max[i] = max(prefix_sum[r+1] for r in [i, right[i]-1]) - prefix_sum[i].

Thus, to compute left_max and right_max for all i, we need to:

1. Build the prefix_sum array.

2. For each i, find the minimum prefix_sum in [left[i]+1, i], and compute left_max[i] = prefix_sum[i+1] - min_val.

3. For each i, find the maximum prefix_sum in [i+1, right[i]] (since r+1 is from i+1 to right[i], because r can be up to right[i]-1).

Then, right_max[i] = (max_val - prefix_sum[i]).

But how to compute these min and max ranges efficiently.

The straightforward approach is to use a segment tree for range minimum and range maximum queries. Preprocess the prefix_sum array into a segment tree. Then, for each i, query the min in [left[i]+1, i] and the max in [i, right[i]-1 + 1] (because r can be up to right[i]-1, so r+1 is up to right[i]).

But building a segment tree for 1e5 elements is manageable, and each query is O(logn), so for 1e5 elements, the total time would be O(n logn), which is acceptable.

Alternatively, use a sparse table for range min and max queries, which allows O(1) query after O(n logn) preprocessing.

Yes, a sparse table is a good choice here, as it allows O(1) queries for range min and max.

So the steps are:

1. Compute left and right arrays using the stack approach.

2. Compute prefix_sum array of size n+1, where prefix_sum[0] = 0, prefix_sum[k] = a[0] + ... + a[k-1].

3. Preprocess prefix_sum into a range min sparse table and a range max sparse table.

4. For each i:

   a. Compute the range for left_max[i]: from (left[i] +1) to i (inclusive), in the prefix_sum array. So the indices are [left[i]+1, i] in prefix_sum. The minimum in this range is min_val.

   b. left_max[i] = prefix_sum[i+1] - min_val.

   c. Compute the range for right_max[i]: from i+1 to right[i]. Because r can be up to right[i]-1, so r+1 is up to right[i]. The maximum in this range is max_val.

   d. right_max[i] = max_val - prefix_sum[i].

5. Then, compute the possible maximum subarray sum for i's range: the maximum of (left_max[i], right_max[i], left_max[i] + right_max[i] - a[i]).

6. The value for i is (sum - a[i]) where sum is this maximum subarray sum. So value = (max_subarray_sum) - a[i].

7. The answer is the maximum of all these values and 0.

Now, the code steps.

First, compute left and right arrays.

Then compute prefix_sum.

Then build sparse tables for range min and max.

Then process each i to get left_max and right_max.

Finally, compute the maximum value.

Let's test this approach on the first example.

Example 1:

n=5

a = [5, -2, 10, -1,4]

prefix_sum is [0,5,3,13,12,16]

Compute left and right for each i.

For i=0 (a[0] =5):

left[i] is -1 (no elements to the left).

right[i] is the first element to the right >5. Looking at a[1]=-2 (<=5), a[2]=10 (>5). So right[0] =2.

range is [0+1, 2-1] = [0,1].

left_max[0] = prefix_sum[0+1] - min(prefix_sum[0+1 ... 0] (since left[i]+1 is 0, i is 0). So the range is [0..0]. prefix_sum[0] is 0? Wait, the prefix_sum array is of size 6 for n=5. So prefix_sum[0] =0, prefix_sum[1] =5, prefix_sum[2]=3, etc.

Wait, the left_max[i] for i=0 is the sum of a subarray ending at i=0, starting at left[i]+1 = 0. So the subarray is [0..0], sum is 5. So left_max[0] =5.

But according to the code steps:

The range for left_max[i=0] is left[i]+1 =0 to i=0. So in the prefix_sum array, the indices are 0 to 0 (since prefix_sum[i+1] is prefix_sum[1] =5. So the sum is prefix_sum[i+1] - prefix_sum[k], where k ranges from 0 to 0. So min_val is prefix_sum[0] =0. So left_max[0] =5 -0 =5.

Yes.

The range for right_max[i=0] is from i+1=1 to right[i] =2. So in the prefix_sum array, indices 1 and 2 (since right[i] is 2, so r can be up to 1 (right[i]-1 =1). So r+1 can be up to 2. So the range is prefix_sum[1..2]. The maximum of prefix_sum[1] =5 and prefix_sum[2] =3 is 5. So right_max[0] =5 -5=0.

So the maximum subarray sum for i=0 is max(5,0,5+0-5=0) =5. The value is 5-5=0.

But this is for the subarray [0,0], which has sum 5. Bob removes it, so score 0.

But the actual optimal in example 1 is when Alice selects the entire array. Let's see what happens for i=2 (a[i]=10).

For i=2:

left[i] is the last index j <2 where a[j] >=10. a[0]=5 <10, a[1]=-2 <10. So left[i] =-1.

right[i] is the first index j>2 where a[j]>10. a[3] is -1, a[4] is4: none. So right[i]=5 (n=5). So the range is [0,4].

left_max[i=2] is prefix_sum[3] (sum 0..2, which is 5-2+10=13) minus the min prefix_sum in [0,2] (prefix_sum[0],1,2: 0,5,3). min is 0. So left_max =13-0=13.

right_max[i=2] is max of prefix_sum[3..5] (sum up to index 3 is 13-1=12, index4 is12+4=16). So prefix_sum[3] =13-1=12, prefix_sum[4] =12, prefix_sum[5] =16. So max is16. right_max[i=2] =16 -13 =3.

So the maximum subarray sum for i=2 is max(13,3,13+3-10=6). So 13. Value is 13-10=3. Which is not the maximum. So this is for the subarrays where 10 is the maximum. So in this case, the best is the entire subarray [0,4], sum is 5-2+10-1+4=16. Subtract 10 gives 6. Which is correct. But according to our calculation for i=2, the value is 3. So why the discrepancy?

Ah, because the approach is considering the subarrays where a[i] is the maximum. In the entire array [0,4], the maximum is 10. So i=2 is the maximum. So our code should compute for i=2 the maximum possible sum of a subarray where a[i] is the maximum, which is the entire array. But according to the left_max and right_max for i=2, the sum is 13 (sum from 0 to 2) plus 3 (sum from 2 to4) minus 10, giving 13+3-10=6. Wait, no. Let me re-calculate.

Wait, left_max[i=2] is 13 (sum of [0..2] is 13), right_max[i=2] is 3 (sum of [3..4] is 3). So the maximum subarray sum is the max of 13, 3, 13+3-10=6. So 13. Then the value is 13-10=3. But the actual sum of the entire array is 16, and subtracting 10 gives 6. So where is the error?

Ah, because the code computes left_max and right_max within the range where a[i] is the maximum. But in this case, the left_max[i=2] is the maximum sum ending at i=2 in the range [0,2], but the right_max[i=2] is the maximum sum starting at i=2 in the range [2,4]. But combining them would give the sum from 0 to 2 (13) plus the sum from 3 to4 (3) → 16. But the code's approach for combining left_max and right_max is left_max + right_max - a[i], which is 13 +3 -10 =6. Which is the sum of the entire array. So the maximum subarray sum is the maximum between 13,3,6 →13. So the code would select 13, and the value is 13-10=3. Which is incorrect.

But why?

Because the code is considering for each i the maximum sum of a subarray where a[i] is the maximum, but the way left_max and right_max are computed might not capture the maximum possible sum in the entire range.

Ah, here's the problem: the code for left_max and right_max considers the sum within the left and right ranges, but when combining them, it's possible that the sum of the entire range is higher than either left_max or right_max. However, the code's way of combining left_max and right_max is left_max + right_max - a[i], which is the sum of the left part plus the sum of the right part, but since a[i] is counted once in each, subtracting a[i] gives the sum of the combined subarray.

But in this example, the left_max is 13 (sum of [0..2]), the right_max is3 (sum of [3..4]). Their combination is 13+3-10=6, which is the sum of the entire array. But the code's approach chooses the maximum of 13,3,6, which is 13. So the code's calculation for i=2 would yield a value of 13-10=3. But the actual maximum possible value when a[i] is the maximum is 16-10=6. So the code is missing this case.

So what's wrong?

The code's approach to compute the maximum subarray sum for i=2's range [0,4] is missing the case where the entire range is considered. Because when combining left_max and right_max, the code computes left_max + right_max - a[i], which is the sum of the left part and right part minus a[i] (since a[i] is counted twice). But in this case, the left part is [0..2] sum 13, the right part is [3..4] sum 3. The combined sum is 13 +3 -10 =6, which is correct. However, the code's approach picks the maximum of 13,3,6 →13. So the code thinks the maximum sum for a subarray where a[i] is the maximum is 13. But the actual maximum sum is 16 (the entire array sum). So why is this discrepancy?

Because the code's left_max and right_max calculations are not capturing the entire range.

Ah! The left_max[i=2] is computed as the maximum sum of a subarray ending at i=2, within the range [0,2]. So the left part is [0..2], sum 13. But in the range [0,4], the entire array is allowed, so the sum from 0 to4 is 16. But according to the code's logic, the right_max for i=2 is the maximum sum starting at i=2 in the range [2,4]. The sum starting at 2 can be [2..4], which is 10-1+4=13. Which is sum 13. But according to the code's calculation, right_max[i=2] is3. How?

Let me re-calculate right_max for i=2.

For i=2:

right[i] is5. So the range for right_max[i=2] is from i=2 to right[i]-1=4. So r can be from 2 to4. So the sum starting at i=2 is sum from 2 to r.

The prefix_sum array is:

prefix_sum[0] =0

prefix_sum[1] =5

prefix_sum[2] =3

prefix_sum[3] =13

prefix_sum[4] =12

prefix_sum[5] =16

So the sum from 2 to r is prefix_sum[r+1] - prefix_sum[2].

r can be 2,3,4.

sum from 2 to2: a[2] =10 → prefix_sum[3] - prefix_sum[2] =13-3=10.

sum from 2 to3: 10 + (-1) =9 → prefix_sum[4]-prefix_sum[2] =12-3=9.

sum from 2 to4:9+4=13 → prefix_sum[5]-prefix_sum[2] =16-3=13.

The maximum of 10,9,13 is13. So right_max[i=2] is13.

But according to the code's calculation, right_max[i=2] is prefix_sum[r+1] in the range i+1=3 to right[i]=5 (since r+1 can be up to right[i]=5, which is prefix_sum[5]. So the range for the prefix_sum is from i+1=3 to right[i]=5. So the indices are 3,4,5. The maximum prefix_sum in these indices is prefix_sum[3]=13, prefix_sum[4]=12, prefix_sum[5]=16. Maximum is 16. So right_max[i=2] =16 - prefix_sum[2] (3) →16-3=13. Yes.

So right_max[i=2] is13.

So left_max[i=2] is13 (sum from 0 to2:13).

right_max[i=2] is13 (sum from 2 to4:13).

The maximum subarray sum is the maximum of 13 (left_max), 13 (right_max), and 13+13-10=16. So the maximum is16.

So the value is16-10=6. Which is correct.

Ah, so the code's approach would compute for i=2 the maximum sum as 16 (left_max + right_max - a[i] =13+13-10=16). Then the value is16-10=6, which is correct.

So why did the earlier calculation have an error?

Because I had incorrectly computed right_max[i=2] as3. But according to the code's approach, right_max[i=2] is13. So in that case, the code would correctly compute the maximum sum as 16, leading to the correct value of6.

So the code's approach works in this case.

So the problem must have been a miscalculation earlier.

Therefore, the code's approach is correct.

Now, let's proceed to code this.

The steps are:

Implement the stack-based approach for left and right.

Compute prefix_sum.

Build sparse tables for range min and max.

Compute left_max and right_max for each i.

Compute the maximum value.

Also, need to consider the case where the segment is of length 1 (value 0), which can be the maximum if all other possibilities are negative.

So the code outline is:

Read n and a.

Compute left and right arrays.

Compute prefix_sum.

Build sparse tables for range min and range max.

For each i:

   compute left_max[i] = prefix_sum[i+1] - range_min(left[i]+1, i).

   compute right_max[i] = range_max(i+1, right[i]) - prefix_sum[i].

   max_sub_sum = max(left_max[i], right_max[i], left_max[i] + right_max[i] - a[i])

   current_value = max_sub_sum - a[i]

   if current_value > max_value:

       max_value = current_value

After processing all i, the answer is max(max_value, 0).

Now, coding this in Python.

But implementing a sparse table for range min and max.

But for Python, the standard way to build a sparse table is as follows:

For each power of two, precompute the min/max for intervals of length 2^j.

The sparse table for range min:

log_table = [0]*(n+1)

for i in 2..n:

    log_table[i] = log_table[i//2] +1

Then, build a table st where st[j][i] is the min in the interval starting at i of length 2^j.

Similarly for max.

But for the prefix_sum array of size n+1, since the indexes are from 0 to n.

So the code steps for the sparse tables:

Build the log table.

Build the st_min and st_max tables.

For range queries:

def get_min(l, r):

   if l > r: return inf

   length = r - l +1

   k = log_table[length]

   return min(st_min[k][l], st_min[k][r - (1<<k) +1])

Similarly for get_max.

Now, let's code this.

But in Python, for n=1e5, building the sparse tables would take O(n log n) time and space, which is manageable.

But wait, the prefix_sum array is size n+1. So for the sparse tables, we have to build for n+1 elements.

But n is up to 1e5, so n+1 is 1e5+1. The log_table for 1e5+1 is manageable.

Now, code for left and right:

Compute left array:

left = [-1]*n

stack = []

for i in range(n):

    while stack and a[stack[-1]] < a[i]:

        stack.pop()

    if stack:

        left[i] = stack[-1]

    else:

        left[i] = -1

    stack.append(i)

Wait, no. Because for left[i], we need the last index where a[j] >= a[i]. Wait, according to our earlier approach, left[i] is the last index j <i where a[j] >= a[i]. So the condition for the stack is while stack is not empty and a[stack[-1]] < a[i], we pop. The remaining element is the last j where a[j] >= a[i].

Yes.

So the code for left is:

left = [-1]*n

stack = []

for i in range(n):

    while stack and a[stack[-1]] < a[i]:

        stack.pop()

    if stack:

        left[i] = stack[-1]

    else:

        left[i] = -1

    stack.append(i)

Similarly, right array:

right = [n]*n

stack = []

for i in range(n-1, -1, -1):

    while stack and a[stack[-1]] <= a[i]:

        stack.pop()

    if stack:

        right[i] = stack[-1]

    else:

        right[i] = n

    stack.append(i)

Yes. Because for right[i], we are looking for the first j >i where a[j] > a[i]. So the condition is while stack and a[stack[-1]] <= a[i], pop. The remaining element is the first j with a[j] > a[i].

So this code should correctly compute left and right arrays.

Now, the prefix_sum:

prefix_sum = [0]*(n+1)

for i in range(n):

    prefix_sum[i+1] = prefix_sum[i] + a[i]

Now, build the sparse tables for prefix_sum.

But how to build them for range min and range max.

Implementing the sparse tables:

max_log = 17  # since 2^17 is larger than 1e5+1

st_min = [[0]*(n+1) for _ in range(max_log)]

st_max = [[0]*(n+1) for _ in range(max_log)]

for i in range(n+1):

    st_min[0][i] = prefix_sum[i]

    st_max[0][i] = prefix_sum[i]

for j in range(1, max_log):

    for i in range(n+1 - (1 << j) +1):

        st_min[j][i] = min(st_min[j-1][i], st_min[j-1][i + (1 << (j-1))])

        st_max[j][i] = max(st_max[j-1][i], st_max[j-1][i + (1 << (j-1))])

log_table = [0]*(n+2)

for i in range(2, n+2):

    log_table[i] = log_table[i//2] +1

Then, for range min query:

def get_min(l, r):

    if l > r:

        return float('inf')

    length = r - l +1

    k = log_table[length]

    return min(st_min[k][l], st_min[k][r - (1 <<k) +1])

Similarly for get_max:

def get_max(l, r):

    if l > r:

        return -float('inf')

    length = r - l +1

    k = log_table[length]

    return max(st_max[k][l], st_max[k][r - (1 <<k) +1])

Now, for each i:

left_part = left[i] +1

right_part = i

min_val = get_min(left_part, right_part)

left_max_i = prefix_sum[i+1] - min_val

For right_max:

start = i+1

end = right[i]

max_val = get_max(start, end)

right_max_i = max_val - prefix_sum[i]

Then, the maximum subarray sum is max(left_max_i, right_max_i, left_max_i + right_max_i - a[i])

value = max_sub_sum - a[i]

Update the global maximum.

Finally, the answer is max(global_max, 0)

Now, let's test this code with the first example.

Example 1:

n=5

a = [5, -2, 10, -1,4]

prefix_sum = [0,5,3,13,12,16]

left array:

i=0: stack is empty. left[0]=-1. stack becomes [0]

i=1: a[1] =-2. stack has 0. a[0]=5 < -2? No. So pop. Stack empty. left[1]=-1. stack [1].

i=2: a[2]=10. stack has 1. a[1]=-2 <10 → pop. stack empty. left[2] =-1. stack [2].

i=3: a[3] =-1. stack has 2. a[2] =10 >=-1. So left[3] =2. stack becomes [2,3].

i=4: a[4]=4. stack has 3,2. a[3] =-1 <4 → pop. stack becomes [2]. a[2]=10 >=4. So left[4]=2. stack [2,4].

right array:

Processing from 4 down to 0.

i=4: stack is empty. right[4]=5 (n=5). stack [4]

i=3: a[3]=-1. stack has4. a[4]=4 >-1 → right[3] =4. stack [3,4]

i=2: a[2]=10. stack has3 (a= -1) and4 (4). a[3] =-1 <=10 → pop. a[4] =4 <=10 → pop. stack empty. right[2] =5. stack [2]

i=1: a[1]=-2. stack has2. a[2]=10 >-2 → right[1] =2. stack [1,2]

i=0: a[0]=5. stack has1 (a=-2) and 2 (a=10). a[1]=-2 <=5 → pop. a[2]=10 >5 → right[0] =2. stack [0,2]

So the right array is:

right = [2,2,5,4,5]

For i=2:

left[i]=-1, right[i]=5.

left_part =0, right_part=2.

get_min(0,2): prefix_sum[0],1,2 are 0,5,3. min is0.

left_max_i=13-0=13.

right_max_i: start=3, end=5.

prefix_sum[3]=12, prefix_sum[4]=12, prefix_sum[5]=16.

get_max(3,5) is16. right_max_i=16 -13 (prefix_sum[2]=3) →16-3=13.

max_sub_sum = max(13,13, 13+13-10 →16) →16. value=16-10=6.

Which is correct.

Now, let's code this.

The code in Python should look like this.

But for n up to 1e5, the code may take some time, but within the time limits.

Now, let's write the code.
</think>

```python
import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    if n == 0:
        print(0)
        return
    
    # Compute left and right boundaries
    left = [-1] * n
    stack = []
    for i in range(n):
        while stack and a[stack[-1]] < a[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
    
    right = [n] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)
    
    # Compute prefix sums
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + a[i]
    
    # Build sparse tables for range min and max
    max_log = 17
    log_table = [0] * (n + 2)
    for i in range(2, n + 2):
        log_table[i] = log_table[i // 2] + 1
    
    st_min = [[0] * (n + 1) for _ in range(max_log)]
    st_max = [[0] * (n + 1) for _ in range(max_log)]
    for i in range(n + 1):
        st_min[0][i] = prefix_sum[i]
        st_max[0][i] = prefix_sum[i]
    
    for j in range(1, max_log):
        for i in range(n + 1 - (1 << j) + 1):
            st_min[j][i] = min(st_min[j-1][i], st_min[j-1][i + (1 << (j-1))])
            st_max[j][i] = max(st_max[j-1][i], st_max[j-1][i + (1 << (j-1))])
    
    def get_min(l, r):
        if l > r:
            return float('inf')
        length = r - l + 1
        k = log_table[length]
        return min(st_min[k][l], st_min[k][r - (1 << k) + 1])
    
    def get_max(l, r):
        if l > r:
            return -float('inf')
        length = r - l + 1
        k = log_table[length]
        return max(st_max[k][l], st_max[k][r - (1 << k) + 1])
    
    max_value = -float('inf')
    for i in range(n):
        # Compute left_max[i]
        L = left[i] + 1
        R = i
        min_val = get_min(L, R)
        left_max = prefix_sum[i+1] - min_val
        
        # Compute right_max[i]
        start = i + 1
        end = right[i]
        max_val = get_max(start, end)
        right_max = max_val - prefix_sum[i]
        
        # Calculate possible max subarray sum
        combine = left_max + right_max - a[i]
        current_max = max(left_max, right_max, combine)
        current_value = current_max - a[i]
        
        if current_value > max_value:
            max_value = current_value
    
    print(max(max_value, 0))

if __name__ == "__main__":
    main()
```