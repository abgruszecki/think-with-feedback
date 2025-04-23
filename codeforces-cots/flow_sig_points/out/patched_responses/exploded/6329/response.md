<think>
Okay, let's try to figure out this problem. So, George has to remove n - k cards by selecting contiguous segments each time, removing the minimum in that segment, and adding the segment's length to the total. The goal is to maximize the sum. And after all removals, the remaining cards must be exactly the sequence b given.

Hmm. The key here is to model which cards are removed and in what order so that the remaining sequence matches b, and the sum is maximized.

First, I need to understand how the process works. Each removal step affects the remaining cards. Since we have to end up with exactly the b sequence, the order in which we remove the other cards must preserve the order of the elements in b.

Wait, the problem states that after all removals, the remaining cards must be exactly the sequence b. So the order of the remaining cards is fixed as per b. That suggests that the elements in b must be a subsequence of the original array p. But how does that help here?

But the actual process of removing cards might affect which elements are left. For example, when you remove a card, all the remaining cards shift to fill the gap. So the elements in b must appear in the same order as they do in p, but not necessarily contiguous. Because each removal can take a contiguous segment, but when you remove an element from the middle, the left and right parts become connected. So the sequence of remaining elements must be a subsequence of p, in order. Since the problem says that it's possible to get the given b sequence, we don't have to check that. Our job is to compute the maximum possible sum of w's (segment lengths) in the removal steps.

So how do we model the process of removing elements not in b, and compute the maximum possible sum?

Let me think about the example given. For instance, in the first sample:

Original p is [2,1,3]. The target b is [1,3]. So George needs to remove the 2. How? The first step must be removing the 2. But the initial array is [2,1,3]. To remove the 2, which is the first element. But how? The segment chosen must include the 2. Wait, but the first step requires selecting a contiguous segment. The only possible way to remove the 2 is to choose a segment that includes it. Let's see. The first step is to remove one element (since n -k is 1 here). Wait, n is 3, k is 2. So one removal.

Wait, the first example's output is 1. So when removing the 2, the segment chosen must be of length 1. Because the sum is 1. So George can't choose a longer segment. Wait, but why can't he choose a longer segment? Because the segment must be contiguous. So in the first step, the available segments are all possible contiguous subarrays. For example, he can choose the entire array (length 3). Then the minimum in the array is 1 (the second element). Removing that would give him 3 sausages, but then the remaining elements would be 2 and 3. But the target is 1 and 3. So that's not possible. So in that case, the correct approach is to remove the 2 by selecting a segment of length 1 (the first element) and removing it, which gives 1 sausage and leaves 1 and 3. Hence the answer 1.

So the problem is to find the order of removing elements such that the target sequence is achieved, and the sum of the segment lengths is maximized.

The key is to model the necessary constraints on which elements can be removed in each step, and choose the segments in such a way that the sum is maximized.

So how do the elements in the original array relate to the target array? The target array must be a subsequence of the original array. Because, during each removal, the elements not in the target must be removed. The order of the elements in b must be the same as their order in p.

But given that the problem states that the target is achievable, we can ignore checking this.

Now, the problem reduces to selecting the order in which the non-b elements are removed, and the segments chosen for each removal, such that the sum of the segment lengths is maximized.

Each time we remove a non-b element, we must select a segment that includes it, but the segment can also include other elements (which may be either in b or already scheduled to be removed). However, once an element is removed, the remaining elements are contiguous again.

But how to model this in a way that allows efficient computation?

An important observation here is that the optimal strategy is to maximize the sum of the segment lengths chosen for each removal. Since each step contributes w to the sum, where w is the length of the segment chosen for that step, we need to maximize each w as much as possible.

But the order in which elements are removed affects the possible w's. For example, removing elements in a certain order might allow longer segments in later steps.

Alternatively, perhaps the optimal strategy is to remove elements in a way that allows each step to take the largest possible w. But how?

Another approach is to model the problem as selecting all the elements to be removed, and for each such element, determine the maximum possible w (segment length) possible when it is removed. Because once an element is removed, the elements around it are merged, which affects the possible segments for other elements.

But this seems complicated. So perhaps there's a way to model this by considering the positions of the elements in the original array and the target array.

Let me think of the target array as a subsequence of the original array. For example, in the first sample, the elements 1 and 3 are in positions 2 and 3. The element to be removed is 2, which is at position 1. When it's removed, the array becomes [1,3], which is the target.

In the second sample, the target is the even elements. So in the original array, the elements to remove are the odd ones. For each of these, when removed, the segment chosen must include them. For example, when removing 1 (the first element), the segment can be the entire array (length 10), but the minimum in that segment is 1. So removing it gives 10 sausages. Then the next elements to remove are 3, 5, 7, 9. Each time, the segment can be as large as possible. But how?

Wait, in the second example, the output is 30. Let's see: n is 10, k is 5. So 5 elements are removed. The sum is 30, so each step contributes 6. How? 5 steps with 6 each sum to 30. So perhaps for each removal, the segment length is 6. But how?

Hmm, perhaps in that example, when the elements to be removed are 1,3,5,7,9. Each time, when you remove one of them, the segment chosen is the current contiguous block that includes that element and some adjacent elements. For instance, removing 1 first: the segment could be [1,2,3,4,5,6,7,8,9,10], which is length 10. The minimum is 1, so removing it gives 10. Then the array becomes [2,3,4,5,6,7,8,9,10]. Next, remove 3. The segment could be the entire array (length 9), but the minimum is 2. So that's not possible. Wait, but 3 is the element to remove. So the segment must include 3, and the minimum in the segment must be 3, so that when you remove it, the sum increases by the segment length. But wait, the segment chosen must have a minimum equal to the element being removed. So, perhaps the elements to be removed are local minima in their respective segments when they are removed.

So the key is that each element to be removed must be the minimum of the segment chosen in that step. Therefore, the order in which elements are removed must be such that when an element x is removed, there exists a contiguous segment in the current array that includes x, and x is the minimum of that segment.

But how to model this for optimal sum?

An alternative approach is to realize that the elements that are to be removed must form a certain structure. Let's consider the elements of the original array that are not in the target array. Let's call these elements S. For each element x in S, we need to find the earliest possible step to remove it, but in such a way that when it is removed, the segment chosen includes x and has x as the minimum. The sum is the sum of the segment lengths for each x in S.

Wait, but the order of removal affects the possible segment lengths. For example, if you remove elements from the left first, the segments for the right elements may be longer.

But perhaps each x in S can be processed in a way that the maximum possible segment length for x is determined by the positions of the elements that are kept (elements in the target array) around x.

Let's consider the positions of the elements in the target array. For example, in the original array, the target elements form a subsequence. So between two consecutive target elements, there may be some elements that need to be removed.

For instance, between the i-th and (i+1)-th target elements in the original array, there are some elements. These must be removed. For each such element x in that range, the maximum possible segment length when x is removed is determined by the left and right boundaries of the region where x is the minimum.

Alternatively, for each x in S (elements to remove), the maximum possible w (segment length) when x is removed is equal to the number of elements in the interval [L, R], where L is the nearest element to the left of x in the target array (or the start of the array if there's no such element), and R is the nearest element to the right of x in the target array (or the end of the array if there's no such element). Because once these elements are fixed, the maximum segment that can include x and have x as the minimum is [L+1 ... R-1]. But how?

Wait, perhaps the elements in S that lie between two consecutive elements in B (the target array) can be processed in a way that allows their removal in any order, but each contributes a segment length equal to the size of their "block". Wait, perhaps the elements that are between two elements in B form a block, and when you remove them, the maximum possible segment length for each is the size of the block. Because once the elements in the block are removed, their removal can be done in an order that allows each to be the minimum in the entire block. For example, if the block is [3,2,5], then you can remove 2 first (as the minimum of the entire block, giving segment length 3), then 3 (as part of a segment of length 1?), but that's not possible. Wait, perhaps not.

Alternatively, maybe each element in S can be associated with a certain interval determined by the elements in B. For example, consider the original array divided into regions separated by the elements of B. Each such region consists of elements between two consecutive elements of B (or before the first B element, or after the last B element). These regions must be processed in a way that all elements in the region are removed. For each such region, the sum of the maximum possible w's for each element in the region can be computed.

But how to model this?

Let's take the second sample:

Original array: [1,2,3,4,5,6,7,8,9,10]

Target array: [2,4,6,8,10]. So the elements to remove are 1,3,5,7,9.

Between 2 and 4 in the original array, there is 3. So the region between 2 and 4 is just [3]. Similarly, between 4 and 6 is [5], etc. Each of these regions has a single element to remove. When removing 3, the segment can be [2,3,4], which is of length 3. But 3 is the minimum in this segment, so removing it gives a w of 3. Similarly for 5: the segment could be [4,5,6], length 3, etc. Each such element in these regions contributes 3 to the sum. There are 5 elements (1,3,5,7,9). Wait, but 1 is before the first element of B (2). So for 1, the region is from the start to 2. So the possible segment when removing 1 is [1,2], but the minimum is 1. So the segment length is 2, which gives 2. But in the sample, the output is 30. Let's see: 5 elements, sum 30. 30/5=6. So each step contributes 6. Hmm, perhaps my previous reasoning is incorrect.

Wait in the second sample, the output is 30. Let's calculate:

n=10, k=5. So n -k =5 steps. The sum is 30, so each step adds 6. So how is that possible?

Ah! Wait, perhaps when removing 1, the segment can be [1,2,3,4,5,6], with length 6. The minimum is 1. So when you remove 1, the sum increases by 6. Then, the array becomes [2,3,4,5,6,7,8,9,10]. Now, the next element to remove is 3. The segment could be [2,3,4,5,6], length 5. The minimum here is 2, which is part of B, so can't be removed. So that's not allowed. Wait, but we need to remove 3. So the segment chosen must include 3 and have 3 as the minimum. So the segment could be [3,4,5,6], length 4. The minimum is 3. So adding 4. But that would sum 6+4+ ... ?

Hmm, but the sample's output is 30. So maybe each of the 5 steps contributes 6. How?

Wait, perhaps the initial segment is the entire array (length 10) for removing 1. Then, after that, the array is [2,3,4,5,6,7,8,9,10]. Then, the next step is to remove 3, but the segment must be as large as possible. The segment could be [3,4,5,6,7,8,9,10], which has length 8. The minimum here is 3, so removing it gives 8. Then, for 5, the segment could be [5,6,7,8,9,10], length 6. Sum so far 10 + 8 +6 ... but 10+8=18, then +6=24, then 7 is next, etc. Hmm, but this doesn't sum to 30.

Alternatively, maybe the order of removal allows each step to take a segment that includes the entire current array. For example:

First, remove 1 from the entire array (length 10, sum +=10).

Now, array is [2,3,4,5,6,7,8,9,10]. Then, the next element to remove is 3. The entire array is length 9. The minimum here is 2 (part of B), so can't. So we need to choose a segment where 3 is the minimum. For example, the segment [3,4,5,6,7,8,9,10] (length 8). The minimum is 3, so sum +=8. Now array is [2,4,5,6,7,8,9,10].

Next, remove 5. The segment from 4 to 6 (4,5,6) is length 3. Sum +=3. Or maybe a larger segment. The segment [4,5,6,7,8,9,10] (length 7), but the minimum is 4 (part of B). So that's not allowed. So the segment must be [5,6,7,8,9,10], which has minimum 5. So sum +=6. Then array becomes [2,4,6,7,8,9,10].

Then, remove 7. The segment could be [7,8,9,10], sum +=4. Then remove 9 from [9,10], sum +=2. Total sum is 10+8+6+4+2=30. Oh, right! So that's the 30 sum. So each step's segment length is 10, 8, 6, 4, 2: which sum to 30.

But how to model this process? The key here is that each element to be removed is the minimum in its entire remaining segment, allowing the maximum possible segment length each time.

But how can we compute this for the general case?

The elements to be removed must be processed in the order of decreasing value. Because, if you remove larger elements first, then smaller elements can take larger segments.

Wait, for example, in the second sample, the elements to remove are 1,3,5,7,9. These are all odd. But in the order of 9,7,5,3,1. For each:

- Remove 9 first: the segment would be [9,10], sum +=2. Then 7 is in a longer segment, etc. But that's not optimal.

But in the optimal order, you process the elements in the order of increasing values, so that smaller elements are removed first, allowing larger elements to be removed in larger segments. Wait, in the second sample, 1 is the smallest, then 3, etc. So removing them in that order allows each to take the largest possible segment.

So perhaps the optimal strategy is to process the elements to be removed in the order of increasing values. Because when you remove a smaller element first, the remaining elements (larger than it) can be removed in longer segments.

Yes. Because a smaller element can be the minimum of a larger segment. So if you remove the smallest elements first, their segments can be as large as possible, and larger elements can be removed later, possibly in larger segments where they are the minimum.

So the key insight is: process the elements to be removed in increasing order of their values. For each such element, the maximum possible segment length is determined by the current positions of the elements in the target array, which form boundaries that the segment cannot cross.

So how to model this?

We can model each element to be removed as part of a certain interval determined by the elements in the target array. For each such element x in S (elements to be removed), the interval in which x resides is between two elements in B (the target array). For example, in the original array, the elements in B are ordered. So for each x in S, we can find the left and right neighbors in B that are immediately before and after x in the original array. Then, the maximum possible segment for x is the entire interval between these two neighbors (including x). However, once other elements in the interval are removed, the available segment may shrink.

But if we process x in increasing order, then when x is the smallest in its interval, the entire interval is available. Once x is removed, the remaining elements in the interval are larger than x, so their segments can be determined.

Wait, perhaps the maximum possible segment length for each x in S is the length of the interval in the original array where x is the minimal element. And the sum of these interval lengths for all x in S is the answer.

But how to compute that.

Let me think. For each element x in S, the maximum possible w (segment length) when it is removed is the number of elements in the interval between the left and right elements in B that x is between. For example, in the second sample:

For x=1, the left neighbor is None (start of the array), right neighbor is 2. So the interval is from the start to 2 (elements 1 and 2). But when x is 1, which is in this interval, the maximum possible segment is from start to 2, but when x is the minimum in that segment, the entire segment can be chosen, which has length 2. However, in the sample, when x=1 is removed, the segment chosen was length 10, which is the entire array. So my previous reasoning is wrong.

Wait, that's confusing. So perhaps the segment can include elements from other intervals. Because when x is the minimum in a larger segment, that's allowed.

So the maximum possible w for x is determined by how far left and right we can extend from x's position in the original array, such that all elements in that extended segment are >= x. Because x must be the minimum in the segment. So the segment can include elements from the left and right intervals (if they are >= x). So the left boundary is the first element to the left of x which is in B and has a value < x. Similarly, the right boundary is the first element to the right of x which is in B and has a value < x. Because if there's an element in B that is less than x, then x can't be the minimum in a segment that includes that element.

Wait, but elements in B are fixed and cannot be removed. So when x is to be removed, the segment chosen must not include any elements in B that are smaller than x. Otherwise, x would not be the minimum in that segment.

Ah! So for x to be the minimum in the segment chosen during its removal, the segment must not contain any element in B that is smaller than x. Because elements in B are not removed and thus are part of the array at that time.

So the segment for x must be between the left and right elements in B that are the first to the left and right of x and have a value less than x. Because including any such element would make x not the minimum.

So the maximum possible segment length for x is the number of elements between the left boundary (L) and right boundary (R), exclusive. L is the last element in B to the left of x that is less than x. R is the first element in B to the right of x that is less than x. Then, the segment is the range (L_pos+1, R_pos-1), and its length is R_pos - L_pos -1.

If there is no such L, then L is the start of the array. If there is no R, then R is the end of the array.

Wait, let's think. For example, in the second sample:

For x=1 (element in S), the left boundary is non-existent (no elements in B to the left of x). The right boundary is 2 (since 2 is the first element in B to the right of x, and 2>1. Wait, but wait. Wait, B is [2,4,6,8,10]. So for x=1, the first element in B to the right is 2. Since 2 is greater than x (1), then the right boundary is the first element in B to the right of x that is less than x. But there are no such elements. Because all elements in B to the right of x are greater than x. So the right boundary is undefined. So the segment for x=1 can be from the start of the array (since no left boundary) to the end of the array (since no right boundary). Because in this case, the entire array is the segment. The minimum is 1, which is x. So removing x=1 gives a segment of length 10. But why in the second sample, the answer is 30, which suggests that each removal contributes 6, but according to this model, x=1 contributes 10.

Hmm, this suggests that my model is incorrect.

Wait, perhaps the maximum possible segment length for x is determined by the left and right elements in B that are the first to the left and right of x in the original array. But regardless of their values. Because the elements in B are not removed, so the segment must be a contiguous part of the current array. However, during the removal process, when elements are removed, the remaining elements are contiguous. So the segment for x can't cross any elements in B that are to be kept. Because those elements are in B and thus are kept. So the segment must be between two consecutive elements in B.

Wait, perhaps the elements in B form a skeleton that divides the original array into regions. Each region is between two consecutive elements in B (or before the first or after the last). The elements in S (to be removed) within each region can be removed in such a way that their segments are within that region. Because once you process a region, the elements outside are part of B and can't be included in the segment.

Wait, for example, in the second sample, the regions are:

- before 2: contains 1.

- between 2 and 4: contains 3.

- between 4 and 6: contains 5.

- between 6 and 8: contains7.

- between 8 and 10: contains9.

So each region has one element to remove. For the first region (before 2), the segment can be the entire region (length 1) when removing 1. But the sample shows that removing 1 in a segment of length 10. That contradicts this model.

So perhaps this model is incorrect. So what's the correct way to model this?

Another approach: the elements in B form a subsequence of the original array. So, during the removal process, the elements of B are preserved in their order. Therefore, the regions between consecutive B elements are those areas where all elements in between must be removed. But the order in which they are removed can vary, and the segments can cross into other regions as long as the B elements are not part of the segment.

Wait, but the B elements are part of the array until the end. So when choosing a segment to remove x, which is between B elements a and b, the segment can include a and/or b only if a and b are not part of the segment. Because, for x to be the minimum in the segment, a and b must be greater than x. Otherwise, the minimum would be a or b, which are in B and cannot be removed.

Ah, right! Because the segment chosen must have x as its minimum. So during the removal of x, any elements in B that are in the segment must be greater than x. Otherwise, x wouldn't be the minimum.

Therefore, for x, the segment must be contained between the left and right B elements that are greater than x, and are the first ones to the left and right of x in B.

For example, in the second sample, x=1. The B elements are 2,4,6,8,10. The first B element to the right of x is 2. Since 2>1, the left boundary is start of array (since there's no B element to the left of x). The right boundary is the position of 2. So the segment can be from the start of the array up to (but not including) 2. So the segment length is 1 (only x itself). But that's not what happened in the sample. So why?

Wait, no. The segment for x=1 can be the entire array. Because in the entire array, the minimum is x=1. So why is that possible? Because all B elements (2,4,6,8,10) are greater than x=1. So including them in the segment is allowed. Because x is the minimum.

Ah! So the segment can include B elements as long as they are all >= x. Because x is the minimum. So for x=1, all B elements are greater than 1, so the entire array is a valid segment. The minimum is 1, so removing it gives a segment length of 10.

So the maximum possible segment for x=1 is 10.

So the model is: for each x in S, the segment can span from the leftmost possible position to the rightmost possible position, where all elements in B within that segment are >= x. Then, the length of this segment is the maximum possible w for x.

But how to compute this?

The steps:

1. Find all elements in B and their positions.

2. For each x in S:

   a. Find the leftmost B element that is less than x. Let's call it L. If none exists, L is the start of the array.

   b. Find the rightmost B element that is less than x. If none exists, R is the end of the array.

   c. The segment for x is from (L_pos + 1) to (R_pos - 1). Wait, no. Wait, we need to include all positions from the first position after L to the last position before R. Because L is the first B element to the left of x that is less than x. Similarly, R is the first B element to the right of x that is less than x.

   Or perhaps L is the last B element to the left of x with value < x. Similarly, R is the first B element to the right of x with value < x.

   Then, the segment for x is between L and R. Because including any B elements with value < x would make x not the minimum.

   So the left boundary is the maximum position of B elements to the left of x that are less than x. The right boundary is the minimum position of B elements to the right of x that are less than x.

   If there are no B elements to the left less than x, then the left boundary is the start of the array (position 0). Similarly for the right.

   Then, the segment for x starts at left_boundary_pos + 1 (if there's a left boundary) or 0 (if no left boundary), and ends at right_boundary_pos - 1 (if there's a right boundary) or n-1 (if no right boundary).

   The length of the segment is (end - start + 1).

But how to find these L and R efficiently?

We can pre-process the B elements and for each B element, store their positions in the original array.

Then, for each x in S, we can:

- Find the positions in B where the elements are before x's position.

- Among those, find the largest element that is less than x. Let's call this L_val. The position of L_val in the original array is L_pos.

- If there is no such L_val, then the left boundary is the start.

- Similarly, find the positions in B where the elements are after x's position.

- Among those, find the smallest element that is less than x. Let's call this R_val. The position of R_val is R_pos.

- If there is no such R_val, then the right boundary is the end.

Then, the segment for x is from L_pos + 1 to R_pos - 1.

The length of this segment is (R_pos - L_pos - 1 + 1) = R_pos - L_pos - 1 + 1 = R_pos - L_pos.

Wait, no. The number of elements from a to b (inclusive) is b - a + 1.

So if the segment starts at start = L_pos +1 and ends at end = R_pos -1, then the length is end - start +1 = (R_pos-1) - (L_pos +1) +1 = R_pos - L_pos -1.

So the length is R_pos - L_pos -1.

But wait, in the second sample for x=1:

B elements are [2,4,6,8,10]. Their positions in the original array are 1,3,5,7,9.

x=1 is at position 0. Looking for B elements less than x to the left: none. To the right: all B elements are greater than x. So left boundary is start (position 0's left is none, so L_pos is -1?), and right boundary is none, so R_pos is 10 (n=10, original array is 0-based up to 9). So the segment is from L_pos +1 = 0 to R_pos -1 =9. So length is 9-0 +1 =10. Which matches the sample.

So the formula is correct.

Another example: x=3 in the second sample. x=3 is at position 2. The B elements to the left are 2 (at position 1), which is less than 3. So L_val is 2, L_pos=1. The B elements to the right are 4,6,8,10. The first of them less than 3 is none. So R_val is none, R_pos is 10 (the end of the array, which is position 9 +1). So segment is from 1+1=2 to 10-1=9. Length is 9-2+1=8. Which matches the sample's second step.

So the algorithm is:

For each x in S (elements to be removed), compute the left and right boundaries as described. The maximum possible w for x is the length of the segment between these boundaries. Summing these lengths for all x in S gives the answer.

But wait, how to find L and R efficiently?

The key steps:

1. Preprocess the elements of B to know their positions in p. For example, create a list of B elements with their indices in p.

2. For each x in S (elements not in B), find:

   a. The largest element in B that is less than x and appears before x in p.

   b. The smallest element in B that is less than x and appears after x in p.

If such elements exist, then L_val is the largest B element before x that is less than x. R_val is the smallest B element after x that is less than x. Their positions in p are L_pos and R_pos.

If no such L_val exists, then L_pos is -1. If no R_val exists, then R_pos is n.

The segment for x is from L_pos+1 to R_pos-1.

The length is (R_pos -1) - (L_pos +1) +1 = R_pos - L_pos -1.

So the problem reduces to, for each x in S, compute this length and sum them all.

Now, how to efficiently compute L_val and R_val for all x in S.

First, let's note that B is a subsequence of p, but in the same order. So the B elements are in the order they appear in p.

So, for each x in S, which is not in B, we can find the positions in B where x would fit.

But since B is a list of elements in p in order, we can preprocess for each element in B, their indices in p.

Then, for each x in S, we need to find:

- The last element in B that is less than x and appears before x's position in p.

- The first element in B that is less than x and appears after x's position in p.

This can be done using binary search.

For example:

Let B be sorted by their positions in p. For each x in S, with position pos_x in p:

We can split B into elements before pos_x and elements after pos_x.

For elements before pos_x, we want the largest element in B less than x.

For elements after pos_x, we want the smallest element in B less than x.

Wait, no. For elements after pos_x, we want the first element (in terms of position) in B that is less than x and is to the right of pos_x. But since the elements are ordered in B as per their positions in p, the elements after pos_x in B have positions greater than pos_x.

Wait, the list B is in the order of their positions in p. So, for example, if B has elements [p3, p5, p7], then the positions are 3,5,7 in p.

So, the list B is sorted in increasing order of their positions in p.

Thus, for a given x in S, with position pos_x, the elements in B that are before pos_x are those elements in B with position < pos_x. Similarly for after.

So for each x in S:

1. Find all elements in B with position < pos_x. Among these, find the maximum element (in value) that is less than x. This is L_val.

   If none exists, L_val is undefined.

2. Find all elements in B with position > pos_x. Among these, find the minimum element (in value) that is less than x. This is R_val.

   If none exists, R_val is undefined.

Wait, no. Wait, the elements in B after pos_x have positions > pos_x. But their values may be in any order. Wait, B is a subsequence of p, but the values in B can be anything. So to find the first element in B after pos_x that is less than x, perhaps we can look for the elements in B after pos_x and find the smallest one in value that is less than x. But how?

Alternatively, for elements in B after pos_x, we need the first one (earlier in position) that is less than x. Because in the original array, these elements are after pos_x. The first such element in the B list (since B is ordered by position) is the earliest one after pos_x.

Wait, but if B is ordered by position, then for elements after pos_x, their positions are increasing. So the elements in B after pos_x are ordered from left to right.

So, for x in S, to find the first B element after pos_x that is less than x, we can iterate through B elements in order (from left to right) starting from the first element in B with position > pos_x. Among these, find the first element (earliest in position) that is less than x. Once found, that's R_val.

But this approach would be O(k) per x in S, which is O(n^2) if k is large. Which is not acceptable for n up to 1e6.

Thus, we need a way to find these elements efficiently.

Alternative approach: precompute for each B element the next and previous elements in B that are less than certain values.

But this might be tricky.

Another idea: for each x in S, the elements in B can be divided into those before and after pos_x. For the elements before pos_x, we can find the maximum element less than x. For the elements after pos_x, we can find the minimum element less than x.

Wait, no. Because for the elements after pos_x, we need the first (in terms of position) element that is less than x. Because that would determine the R_pos.

Alternatively, for the elements after pos_x, the first element (earliest in position) that is less than x would be the R_val, and R_pos is its position.

But how to find that efficiently.

This seems like a problem that can be solved with binary search.

Let me reorganize:

Let's process B in order of their positions. For each x in S, we can find the B elements before and after x's position.

For elements before x's position (pos_x):

We need the largest B element (in value) that is less than x.

But wait, no. We need the largest B element (in value) less than x and with position < pos_x. But perhaps that's not the case.

Wait, the problem is to find the maximum B element in the set {b in B | pos(b) < pos_x and b < x}.

Because the left boundary is the last (in terms of position) B element that is less than x and comes before x. Wait, no. Wait, the left boundary is the largest B element (in value) less than x, but perhaps that's not correct.

No. The left boundary is the first B element to the left of x (in position) that is less than x. Wait, no. Let's see.

The left boundary is the largest (in position) B element that is less than x and is to the left of x. So among all B elements with position < pos_x and value < x, we need the one with the maximum position. Because that's the closest B element to x's left that is less than x.

Similarly, the right boundary is the smallest (in position) B element that is less than x and is to the right of x.

Because the left boundary is the last B element to the left of x that is less than x, and the right boundary is the first B element to the right of x that is less than x.

So for x in S:

Left boundary:

We need the largest position in B where B's element is less than x and has position < pos_x.

Right boundary:

We need the smallest position in B where B's element is less than x and has position > pos_x.

So the approach is:

For each x in S:

- Find in B the elements that are before pos_x (i.e., their positions in p are less than pos_x) and have value < x. Among them, the one with the largest position (closest to pos_x).

- Find in B the elements that are after pos_x (position > pos_x) and have value < x. Among them, the one with the smallest position (closest to pos_x).

These two elements are the left and right boundaries.

If no such elements exist, then the left boundary is considered to be at position -1 (start of array), and the right boundary is at position n (end of array).

The segment for x is then from left_pos + 1 to right_pos -1.

The length is right_pos - left_pos -1.

How to compute this efficiently.

The key is to pre-process B's positions and values, and for each x in S, find the left and right boundaries.

So let's pre-process B as a list of tuples (value, position), sorted by position.

Then, for each x in S, with pos_x = p.index(x) (assuming p is a list where each element is unique), we can:

For left boundary:

- Use binary search to find the largest element in B with position < pos_x and value < x.

For right boundary:

- Use binary search to find the smallest element in B with position > pos_x and value < x.

But how to perform this efficiently.

But B is sorted by position. So for left boundary:

We can first find all elements in B with position < pos_x. This can be done using binary search to find the largest index in B where position < pos_x.

Within these elements (B_left), we need to find the maximum element (value) that is less than x. But no, wait: we need the maximum position in B_left where value < x. Because the left boundary is the closest to pos_x (highest possible position) among B elements with value < x and position < pos_x.

So for B_left (all elements in B with position < pos_x), we need to find the maximum possible position (i.e., the last element in B_left) that has value < x.

Wait, no. Because the elements in B_left are sorted by position (since B is sorted by position), the last element in B_left is the one with the largest position. So among B_left, we can iterate from the end backwards and find the first element with value < x.

But this would take O(k) time in the worst case, which is not feasible for large k.

Alternative approach: for each element in B, we can pre-process for each position, the maximum value up to that position. But I'm not sure.

Alternatively, for B_left (sorted by position), we can have a binary search for the rightmost element with value < x.

But B_left is a list of elements sorted by position, but their values can be arbitrary. So binary search isn't possible on value.

Hmm, this seems tricky.

Another idea: since B is sorted by position, but their values are arbitrary, for the left boundary, we can split B into elements before pos_x. For these elements, we need the one with the highest position (closest to pos_x) that has value < x.

But since B is sorted by position, the elements before pos_x form a prefix of B. So we can find the largest index j where B[j].position < pos_x. Then, in the subarray B[0..j], we need to find the largest index i where B[i].value < x. The element at i will have the largest possible position (since B is sorted by position, and i is the largest possible in the prefix where B[i].value < x).

But how to find this i efficiently.

This can be done using a binary search on the prefix B[0..j], but looking for the maximum i where B[i].value < x.

But since the values are not sorted, this is not possible. So perhaps we need to build a structure that allows us to query for the maximum i in a prefix where B[i].value < x.

But how?

Alternatively, we can precompute for each position in B, the maximum and minimum values up to that point. But I'm not sure.

Alternatively, we can process the elements in B and build a segment tree or a binary indexed tree (Fenwick tree) that allows us to query, within a range of B elements, the maximum i where B[i].value < x.

But building such a structure for 1e6 elements is possible, but may be time-consuming.

Alternatively, for each x in S, after finding j (the largest index in B where B[j].position < pos_x), we can perform a linear scan backwards from j to 0 in B to find the first element with value < x. But this would take O(k) time in the worst case, which is not feasible for large k.

This seems like a dead end.

Wait, but the problem constraints are up to n=1e6. So any O(n) or O(n log n) solution would be acceptable.

Let's think differently. Since B is a subsequence of p, and the elements in B are in order of their positions in p, perhaps we can pre-process for each element in B, the maximum elements to the left and right.

Alternatively, for each element in B, we can maintain a list of all elements in B that are to the left and have certain properties.

But I'm not seeing it.

Alternative approach inspired by the sample solution:

We can precompute for each x in S, the left and right boundaries as follows:

For the left boundary:

- Iterate through B in order of increasing positions (since they are already ordered this way).

- For each element in B, we can keep track of the elements in B that are less than x. For x in S, we can find the last element in B that is before x's position and is less than x.

But again, this seems like it's O(k) per x.

Alternative idea inspired by the problem's sample where processing elements in increasing order gives the optimal sum:

If we process the elements in S in increasing order, then for each x, the left and right boundaries are determined by the elements in B. Because the elements in B are fixed.

But how to compute the left and right boundaries for each x in S.

Perhaps the key is to precompute for each x in S:

- left boundary: the maximum B element's position among B elements before x's position and with value < x.

- right boundary: the minimum B element's position among B elements after x's position and with value < x.

But again, the challenge is to compute these efficiently.

An alternative approach is to note that the left and right boundaries are the same regardless of the order in which x is removed. So for each x in S, the maximum possible w is fixed and can be computed once, and the sum is the sum of these w's.

This suggests that the order in which the elements are removed does not affect the sum. Which seems counterintuitive, but perhaps is correct.

Wait, but in the second sample, the sum is 30, which is the sum of 10 + 8 +6 +4 +2 = 30. But according to the model where each x's w is (R_pos - L_pos -1), for x=1, R_pos is the position after x (which is n=10). So R_pos is 10, L_pos is -1. So the length is 10 - (-1) -1 = 10. For x=3, L_val is 2 (position 1), R_val is none (so R_pos=10). So length is 10-1-1=8. For x=5, L_val=4 (position3), R_val is none (R_pos=10). So length is 10-3-1=6. For x=7: L_val=6 (position5), R_pos=10. Length 10-5-1=4. For x=9: L_val=8 (position7), R_pos=10. Length 10-7-1=2. Sum is 10+8+6+4+2=30. Which matches.

So the sum is indeed the sum of (R_pos - L_pos -1) for each x in S. And this sum is fixed regardless of the order in which the elements are removed. Therefore, the maximum possible sum is simply the sum of these values for all x in S.

This is a crucial insight. The order of removal does not affect the sum. Each element x in S can be removed in a segment of length (R_pos - L_pos -1), and the sum is the sum of these lengths.

Therefore, the problem reduces to computing for each x in S, the values of L_pos and R_pos as described, then summing (R_pos - L_pos -1) for all x in S.

This makes the problem solvable in O(n log k) time, which is acceptable for n up to 1e6.

Now, the challenge is to compute L_pos and R_pos for each x in S efficiently.

To compute L_pos and R_pos:

We can pre-process B as a list of tuples (value, position), sorted by position.

For each x in S:

1. Find all elements in B with position < pos_x (B_left). Among these, find the one with the largest position where value < x. L_pos is that element's position. If none exists, L_pos is -1.

2. Find all elements in B with position > pos_x (B_right). Among these, find the one with the smallest position where value < x. R_pos is that element's position. If none exists, R_pos is n.

Once L_pos and R_pos are found, the contribution is (R_pos - L_pos - 1).

So, how to find L_pos and R_pos efficiently.

Step 1: Finding L_pos.

We can use binary search to find the largest index j in B where B[j].position < pos_x. This gives B_left = B[0..j].

In B_left, we need to find the largest element (by position) with value < x. Since B_left is sorted by position, we can iterate through B_left in reverse order (from j to 0) and find the first element with value < x. But for large j, this would be O(k) time, which is not acceptable.

Alternative approach: for each B element, precompute a structure that allows us to query, for a given prefix B[0..j], the maximum position where value < x.

This can be done using a binary indexed tree or a segment tree.

But for each x in S, we need to process B_left, which is the elements in B up to j (where B[j].position < pos_x), and then find the maximum position in B_left where value < x.

But building a segment tree for B elements where each node stores the values and positions, and allows for range queries for maximum position with value < x.

But this seems complex.

Alternative idea: for each element in B, during a single pass, we can keep track of the maximum positions where the value is less than x.

But this also seems unclear.

Another approach is to note that for B elements sorted by position, we can build a binary search tree augmented with information that allows for efficient maximum queries.

Alternatively, since B is sorted by position, which is the same as their order in the array, we can precompute for each index i in B, the maximum position in B[0..i] where value < x. But x varies for each query.

Alternatively, for each x in S, after finding j (the largest index in B where position < pos_x), we can use a binary search on B[0..j] to find the rightmost element with value < x.

But since the values in B are not sorted, binary search is not possible.

So this seems impossible.

Alternative approach inspired by the sample:

For each x in S, the left boundary is the last element in B (sorted by position) before x's position with value < x.

To find this, we can:

- Find the elements in B with position < pos_x. This can be done with a binary search for the largest index j where B[j].position < pos_x.

- Among B[0..j], we need the largest i where B[i].value < x.

To find this i, we can scan B[j], B[j-1], ..., B[0] until we find an element with value < x. But this is O(k) in the worst case.

But for large k (up to 1e6), this would be O(nk) time, which is 1e12 operations. Not acceptable.

Hmm. This is a problem. So we need a way to find, for a given x and j, the largest i in [0..j] where B[i].value < x, in O(1) or O(log k) time.

This requires a data structure.

The problem is similar to range maximum query with a condition on the value.

We can pre-process for each position j in B, a data structure that allows us to query the maximum i ≤ j where B[i].value < x.

But this is possible using a segment tree where each node stores the values in a certain range and allows binary search for the largest i with value < x.

But building such a segment tree would be O(k) space and O(k log k) time.

For each query, we can perform a binary search over the segment tree for the range [0..j], and find the rightmost element with value < x. This would take O(log k) time per query.

This seems feasible.

Similarly for the right boundary.

So the plan is:

Preprocess B into a segment tree that allows queries for the maximum i in a range [0..j] where B[i].value < x.

Another segment tree for the right boundary queries, which would find the minimum i in a range [j..k-1] where B[i].value < x.

But how to build these segment trees.

Alternatively, for the left boundary:

- Preprocess a segment tree where each node stores the list of values in its range, sorted.

Then, for a query [0..j], we can traverse the segment tree nodes that cover [0..j], and for each node, perform a binary search to find the largest element in the sorted list that is less than x. Keep track of the maximum index found.

This approach has O(k) preprocessing and O(log k * log m) per query, where m is the size of the largest node.

But for k up to 1e6, this could be manageable.

But in Python, implementing such a segment tree for 1e6 elements may be challenging due to time constraints.

Alternative idea: since B is sorted by position, perhaps we can precompute for each element in B, the maximum element less than x in the prefix up to that element.

But this also seems unclear.

Alternatively, for each x in S, after finding j (the largest index in B with position < pos_x), we can perform a binary search on the values of B[0..j] to find the largest value less than x. But this is only possible if the values are sorted.

But B is not sorted by value. So this isn't possible.

Hmm. This is a real problem. How can we efficiently find, in a list of numbers, the rightmost index where the value is less than x?

This is a classic problem that can be solved with a binary search if the list is sorted. But since B is not sorted by value, we can't do that.

Thus, unless we can pre-process B in a way that allows these queries efficiently, this approach won't work.

Alternative approach:

We can pre-process for each element in B, a list of the elements sorted by position. Then, for each x in S:

- Find j using binary search (since B is sorted by position), which gives the largest B element before x's position.

- Then, for the left boundary, we need to find the largest element in B[0..j] with value < x. This is equivalent to finding the maximum value in B[0..j] that is less than x. No, wait, it's the maximum position (since we want the closest to x's position), but the element's value must be less than x.

Wait, but the elements in B[0..j] are sorted by position, but their values are arbitrary. So the maximum position is B[j].position, but we need to check if B[j].value < x. If yes, then L_pos is B[j].position. If not, we have to look for the next one.

But this approach would require checking each element from j down to 0 until we find one with value < x, which is O(k) in the worst case.

This is not feasible for large k.

Thus, another approach is needed.

Wait, perhaps we can precompute for each element in B, the previous element in B that is less than it. But this is not directly helpful.

Alternatively, let's consider that the B elements are processed in order, and for each element in B, we maintain a data structure that allows us to query for the maximum position where the value is less than x.

But this is unclear.

Another idea: since the elements in B are processed in order of their positions, and for each x in S, the left boundary is the last B element before x with value < x, perhaps we can precompute for each position in p, the last B element before it with value less than x.

But x varies for each S element.

This seems challenging.

Alternative Idea Inspired by the Sample:

The maximum possible w for each x in S is determined by the left and right boundaries of B elements that are less than x. To compute these boundaries, we can use the following steps:

- For the left boundary, find the last B element (in terms of position) before x's position that has a value less than x. The position of this element is L_pos.

- For the right boundary, find the first B element (in terms of position) after x's position that has a value less than x. The position of this element is R_pos.

If such elements exist, the segment for x is between L_pos and R_pos, and the length is R_pos - L_pos - 1.

If no left boundary exists, L_pos is -1. If no right boundary exists, R_pos is n.

So the problem reduces to finding these two elements for each x in S.

The key is to find these two elements efficiently.

Let me think about how to find the left boundary.

We can pre-process B into a list sorted by position. For each x in S, with position pos_x, the left boundary is the largest position among B elements with position < pos_x and value < x.

To find this efficiently:

1. Use binary search to find the largest j where B[j].position < pos_x. This gives the rightmost B element before x's position.

2. Among B[0..j], find the largest i where B[i].value < x. The position of B[i] is the left boundary.

Similarly for the right boundary:

1. Use binary search to find the smallest j where B[j].position > pos_x. This gives the leftmost B element after x's position.

2. Among B[j..k-1], find the smallest i where B[i].value < x. The position of B[i] is the right boundary.

The problem is step 2 in both cases.

For step 2 in the left boundary:

We can model the elements B[0..j] as a list and find the rightmost element with value < x. This can be done with a binary search if the values are sorted, but they aren't.

Alternative approach using a binary indexed tree (Fenwick tree):

We can build a Fenwick tree that stores the maximum position for each value. But since the values can be up to 1e6, this is not feasible.

Alternative approach using a segment tree:

We can build a segment tree where each node represents a range of B elements and stores the maximum position in that range where the value is less than x.

But since x varies, this approach is not directly applicable.

Another Idea:

For each x in S, after finding j (the largest index in B where B[j].position < pos_x), we can iterate through the B elements from j down to 0 and check if their value is less than x. The first such element encountered is the left boundary.

This is O(k) in the worst case, but perhaps in practice, for most cases, this would be O(1) per query. But for worst-case scenarios, this would be O(nk), which is not acceptable.

So this approach won't work for the given constraints.

Thus, I'm stuck. Perhaps there's a smarter way to model this problem.

Let's think differently. Since the answer is the sum of (R_pos - L_pos -1) for each x in S, and the order of removal doesn't matter, we can compute this sum efficiently if we can find for each x in S the L_pos and R_pos.

But how?

Another Idea: For the left and right boundaries, perhaps we can use the fact that B is a subsequence of p and that the elements in B are in order. For example, the left boundary for x can be the last element in B that appears before x in p and is less than x. Similarly, the right boundary is the first element in B that appears after x in p and is less than x.

So for each x in S, we can:

- Iterate through B and find the last element in B that is before x in p and has a value < x. This can be done by iterating B in order and tracking the last valid element.

But this would require O(k) per x, which is not feasible.

Alternative Idea Inspired by the Monotonic Stack:

The left boundary for x can be found using a monotonic stack. For example, if we process B elements in order and maintain a stack that keeps track of elements in decreasing order. For each element in B, we can pop elements from the stack until we find an element less than x. The top of the stack is then the left boundary. However, this is for a fixed x, which is not the case here.

Alternatively, for each B element, precompute the previous element in B that is less than it. This can be done using a monotonic stack in O(k) time.

But how does this help for x in S?

Hmm. For example, if x is in S and appears between B[i] and B[i+1], then the left boundary for x would be the maximum between B[i] and any previous elements in B that are less than x. Not sure.

Another Idea: Since the left and right boundaries are based on B elements, perhaps we can pre-process for each possible value x, the relevant boundaries. But x can be up to 1e6, and this would require O(n) space, which is manageable.

But how to pre-process.

For example:

- Preprocess for each position in p, the last B element before it that is less than the value at that position.

- Preprocess for each position in p, the first B element after it that is less than the value at that position.

This way, for any x in S (which is a value in p), we can find the last B element before x's position in p with value < x, and the first B element after x's position in p with value < x.

This can be done using a monotonic stack approach.

Let's think:

We can process the B elements in order of their positions. For each B element, we can keep track of the elements in B that are less than the current element.

But I'm not sure.

Alternatively, process the entire array p and for each element, track the previous B element that is less than it and the next B element that is less than it.

This can be done in O(n) time using a monotonic stack.

Here's how:

For each element in p, to find the previous B element that is less than it:

Initialize a stack that keeps track of B elements in order of their positions. We process each element in p in order. For each element, if it is in B, we update the stack. For non-B elements, we don't update the stack but can query the stack to find the last B element less than it.

But this approach may not work because the B elements are not necessarily contiguous in p.

Alternative Idea: For each element x in p (whether in B or not), we can precompute:

- left_b: the last element in B that is before x's position in p and has value < x.

- right_b: the first element in B that is after x's position in p and has value < x.

Once these are precomputed, for each x in S, the L_pos and R_pos can be retrieved in O(1) time.

The challenge is to compute left_b and right_b for all x in p efficiently.

This can be done using a monotonic stack approach, similar to the problem of finding the nearest smaller element on the left and right.

Let's process all elements in p, and for each element x, track the nearest B element to the left that is smaller than x.

Similarly, track the nearest B element to the right that is smaller than x.

But how to handle the fact that B elements are a subset of p.

Let's proceed step by step.

Preprocessing left_b:

Initialize a stack that keeps track of B elements encountered so far, sorted in a way that allows us to find the last one less than current x.

For each element in p in order:

- If the element is in B:

   - While the stack is not empty and the top element >= current element's value:

       - Pop from the stack.

   - The previous B elements in the stack are those with value < current element's value.

   - Push current element's value and position to the stack.

- For any element (whether in B or not):

   - The left_b for this element is the last element in the stack with value < current element's value. This can be found by binary searching the stack.

But this approach requires the stack to maintain elements in a sorted order. However, the stack is maintained in a way that elements are in increasing order. This is similar to the standard approach for the nearest smaller element problem.

Let me clarify:

For the left_b:

We process p from left to right.

We maintain a stack of B elements, which are kept in increasing order of their values. For each element in p (whether in B or not), we can binary search the stack to find the largest value less than current element's value. The corresponding position is left_b.

If the element is in B, we then update the stack by popping all elements >= current value and pushing the current element.

This way, the stack remains in increasing order.

Similarly for the right_b:

Process p from right to left.

Maintain a stack of B elements in increasing order of their values. For each element in p, find the first B element to the right with value less than current element's value.

This way, for each x in p, we can compute left_b and right_b in O(1) or O(log k) time per element.

Once left_b and right_b are precomputed for all elements in p, then for each x in S, we can:

- L_pos is left_b[x].position if left_b[x] exists, else -1.

- R_pos is right_b[x].position if right_b[x] exists, else n.

Then, the contribution to the sum is (R_pos - L_pos - 1).

This approach is O(n log k) time for preprocessing, and O(1) per query for the x in S.

This seems feasible.

So the steps are:

1. Read n, k, p, and b.

2. Create a set of B elements for O(1) lookups.

3. Preprocess for each element in p, the left_b and right_b.

   a. For left_b:

      i. Initialize a stack that keeps track of B elements in increasing order of value.

      ii. For each element in p from left to right:

          - If the element is in B:

              - Pop elements from the stack while the top element's value >= current value.

              - The left_b for this element is the top of the stack (if any).

              - Push current element's value and position into the stack.

          - Else:

              - Binary search the stack to find the largest value < current element's value.

              - left_b for this element is the corresponding element in the stack.

   However, this may not work for non-B elements, as the stack may contain B elements encountered so far.

   So for each element in p (whether in B or not), the left_b is the last B element to the left (in p) that has a value < current element's value.

So the stack approach for left_b:

Process each element in p from left to right.

When an element is processed:

- If it is in B:

   - While the stack is not empty and the top element's value >= current value, pop.

   - left_b for this element is the top element of the stack (if any).

   - Push current element onto the stack.

- If it is not in B:

   - Binary search the stack to find the largest element with value < current element's value. This element is the left_b.

   - If no such element exists, left_b is None.

But how to binary search the stack.

The stack is maintained in increasing order of values. Because whenever a new B element is added, all elements >= current value are popped. So the stack is in strictly increasing order.

Therefore, for a given current element x (not in B), we can binary search the stack to find the largest element with value < x. Since the stack is sorted, this can be done in O(log k) time.

Similarly for right_b.

Thus, the preprocessing steps are:

For left_b:

- Initialize stack as empty.

- For each element in p in order from left to right:

   val = p[i]

   if val is in B:

      while stack and stack[-1].value >= val:

          stack.pop()

      if stack:

          left_b[i] = stack[-1]

      else:

          left_b[i] = None

      stack.append( (val, i) )

   else:

      # binary search the stack for the largest value < val

      low = 0

      high = len(stack) - 1

      res = -1

      while low <= high:

          mid = (low + high) // 2

          if stack[mid].value < val:

              res = mid

              low = mid + 1

          else:

              high = mid -1

      if res != -1:

          left_b[i] = stack[res]

      else:

          left_b[i] = None

For right_b:

- Initialize stack as empty.

- For each element in p in reverse order (from right to left):

   val = p[i]

   if val is in B:

      while stack and stack[-1].value >= val:

          stack.pop()

      if stack:

          right_b[i] = stack[-1]

      else:

          right_b[i] = None

      stack.append( (val, i) )

   else:

      # binary search the stack for the smallest value < val

      low = 0

      high = len(stack) - 1

      res = -1

      while low <= high:

          mid = (low + high) // 2

          if stack[mid].value < val:

              res = mid

              high = mid - 1

          else:

              low = mid + 1

      if res != -1:

          right_b[i] = stack[res]

      else:

          right_b[i] = None

Once left_b and right_b are precomputed for all elements in p, the sum can be computed as follows:

For each x in S (elements in p not in B):

   i = position of x in p.

   L = left_b[i]

   R = right_b[i]

   L_pos = L.position if L else -1

   R_pos = R.position if R else n

   contribution = R_pos - L_pos - 1

   total += contribution

So this approach would have a time complexity of O(n log k) for preprocessing, and O(n) for summing.

Given that n is up to 1e6, and each binary search is O(log k), this should be feasible.

Now, implementing this in Python.

But how to implement this efficiently.

First, read the input:

Read n and k.

Read p as a list.

Read b as a list.

Create a set of b elements for O(1) lookups.

Then, create a list to map each element in p to its index (since p contains distinct elements).

pos_in_p = {val: idx for idx, val in enumerate(p)}

Then, create a set B_set = set(b).

Now, for each element in p, we can check if it is in B_set.

Then, precompute left_b and right_b for each element in p.

Implementing the left_b processing:

left_b is a list of tuples (value, position) or None.

But for the purpose of this problem, we only need the position of the left and right boundaries.

So for each element i in p:

left_b[i] = position of last B element to the left with value < p[i], or -1 if none.

Similarly, right_b[i] = position of first B element to the right with value < p[i], or n if none.

But to implement this, we need to process the stack as described.

Let's proceed step by step.

Implement left_b:

stack = []

left_b = [-1] * n

for i in range(n):

    val = p[i]

    if val in B_set:

        # update stack

        while stack and stack[-1][0] >= val:

            stack.pop()

        if stack:

            left_b[i] = stack[-1][1]

        else:

            left_b[i] = -1

        stack.append( (val, i) )

    else:

        # binary search the stack

        low = 0

        high = len(stack) - 1

        res = -1

        while low <= high:

            mid = (low + high) // 2

            if stack[mid][0] < val:

                res = mid

                low = mid + 1

            else:

                high = mid -1

        if res != -1:

            left_b[i] = stack[res][1]

        else:

            left_b[i] = -1

Similarly for right_b:

stack = []

right_b = [n] * n

for i in range(n-1, -1, -1):

    val = p[i]

    if val in B_set:

        # update stack

        while stack and stack[-1][0] >= val:

            stack.pop()

        if stack:

            right_b[i] = stack[-1][1]

        else:

            right_b[i] = n

        stack.append( (val, i) )

    else:

        # binary search the stack

        low = 0

        high = len(stack) - 1

        res = -1

        while low <= high:

            mid = (low + high) // 2

            if stack[mid][0] < val:

                res = mid

                high = mid - 1

            else:

                low = mid + 1

        if res != -1:

            right_b[i] = stack[res][1]

        else:

            right_b[i] = n

But wait, for the right_b processing, we are looking for the first B element to the right that is less than val. So the stack should be maintained in a way that allows binary search for the smallest element < val.

But the stack in right_b processing is maintained in increasing order when processed from right to left. Let me think:

When processing from right to left, for B elements:

- The stack is maintained in increasing order of values. Because each time a B element is processed, elements in the stack with value >= current val are popped. Thus, the stack is in increasing order.

So for a non-B element val, we need to find the first element in the stack (from left to right, which represents elements to the right of i in p) that is less than val. Since the stack is in increasing order, the first such element is the leftmost element in the stack < val. Hence, during binary search, we find the leftmost element < val, and that gives the earliest position (in terms of B elements to the right) that is less than val.

Wait, no. Because when processing from right to left, the stack contains B elements encountered so far (which are to the right of the current position). For example, when processing i in reverse order, the stack contains B elements to the right of i. The stack is maintained in increasing order of values. So for a non-B element at position i, we need to find the smallest element in the stack (earliest in the stack, which is the first element encountered in reverse order) with value < val. This will give the earliest B element to the right with value < val, which corresponds to the first B element after i in p with value < val.

Wait, but the stack is in increasing order. So the first element in the stack with value < val would be the leftmost one. So binary search would find the leftmost element < val. For example, stack is [2,3,5], val=4. The elements less than 4 are 2 and 3. The leftmost is 2. But when processing from the right, the stack is built in increasing order. So the leftmost element in the stack is the smallest value. So in this case, the first element less than val would be 2.

But in terms of position in p, which is to the right of i, the smallest value may not be the earliest in position.

Wait, no. Because the stack is built by processing elements from right to left. So the first element added to the stack is the rightmost B element, then moving left. The stack is maintained in increasing order. So the elements in the stack are B elements to the right of i, and their values are in increasing order.

For example, if B elements to the right of i are [5,3,2], then the stack after processing them would be [2,3,5] (but processed in reverse order, the stack would be built by adding 5, then 3 (popping 5), then 2 (popping 3), so the stack would be [2,3,5]? Or perhaps the processing is different.

No, when processing elements from right to left:

For each element in p in reverse order:

If it is a B element:

   while stack is not empty and stack[-1].val >= current val:

       pop

   then append current val.

So the stack is maintained in increasing order.

So for B elements processed in reverse order, the stack is increasing.

Thus, when processing a non-B element at position i, to find the first B element to the right (in p) that is less than current val, the correct approach is to find the leftmost element in the stack that is less than val. Because the stack is in increasing order, the leftmost element < val is the smallest possible value, which corresponds to the first B element encountered to the right (in p) that is less than val.

But I'm not sure. For example, if the stack contains B elements [2,3,5], and val is 4, then the elements less than 4 are 2,3. The leftmost is 2. But the position of 2 in p is to the right of i. So perhaps this corresponds to the first B element to the right that is less than val.

Yes. Because the stack is built from right to left, so elements are added in the order of decreasing position. But the stack is maintained in increasing order of values. So the leftmost element in the stack with value < val is the smallest such value, but since the stack is built from right to left, this element may have a position that is further to the right than other elements with larger values.

For example, consider B elements in p at positions 5, 4, 3, with values 3, 2, 5. When processed in reverse order (i=5, then i=4, then i=3):

- At i=5, val=3. Stack is empty. Append. Stack becomes [(3,5)].

- At i=4, val=2. Pop 3 (3 >=2). Stack is empty. Append (2,4). Stack is [(2,4)].

- At i=3, val=5. Stack has 2 <5. Append. Stack is [(2,4), (5,3)].

Now, stack is in increasing order of values.

For a non-B element at i=2, val=4. Binary search the stack to find the leftmost element <4. The elements are 2 and 5. 2<4, 5>4. So the leftmost element is 2. So the right_b for i=2 is 4 (position of 2 in B element).

But in the p array, the B elements are at positions 3,4,5. The first B element to the right of i=2 is at position3 (val 5), then 4 (val2), then5 (val3). The first B element to the right of i=2 with value <4 is at position4 (val2). So the right_b is position4.

So the binary search correctly finds the leftmost element in the stack (which is the smallest value), which is 2, corresponding to position4.

Thus, the approach works.

Therefore, the code for right_b is correct.

Once left_b and right_b are computed, the total sum is the sum of (right_b[i] - left_b[i] -1) for each element i in p that is not in B.

Now, implementing this in Python.

But for large n=1e6, we need to manage the binary searches efficiently.

But in Python, using lists and binary search with the bisect module can be efficient enough.

Wait, but the stack is a list of tuples (val, pos). The binary search needs to compare based on the val.

But for the left_b processing, when a non-B element is encountered, the stack contains B elements sorted in increasing order of val.

So during the binary search, the mid element's val is compared to the current val.

Thus, the code for left_b and right_b processing should be as described.

But how to handle the binary search in Python.

Implementing the left_b processing:

For non-B elements, when processing from left to right:

stack is a list of tuples (val, pos), sorted in increasing order.

We need to find the largest val in the stack less than current val.

This can be done using bisect.bisect_left.

For example:

import bisect

# stack_vals is a list of tuples (val, pos), sorted by val.

# We can create a separate list of vals for binary search.

# But for efficiency, since the stack is maintained in increasing order, the val list is sorted.

vals = [x[0] for x in stack]

idx = bisect.bisect_left(vals, val) - 1

if idx >=0:

    left_b[i] = stack[idx][1]

else:

    left_b[i] = -1

This would be more efficient than manually implementing the binary search.

But in the code above, when a non-B element is encountered, the stack contains the B elements encountered so far, sorted in increasing order.

So for each non-B element:

vals = [x[0] for x in stack]

using bisect to find the rightmost val < current val.

But bisect.bisect_left returns the first index where val can be inserted to keep the list sorted.

So if we have vals = [a_0, a_1, ..., a_m], sorted in increasing order.

We want to find the largest index j where a_j < val.

bisect.bisect_left(vals, val) gives the insertion point.

If the insertion point is 0, then all elements are >= val, so no such j exists.

Else, the insertion point is j+1, so the largest j is insertion_point -1.

Thus, for the left_b processing:

if the element is not in B:

vals = [x[0] for x in stack]

insertion_point = bisect.bisect_left(vals, val)

if insertion_point ==0:

    left_b[i] = -1

else:

    left_b[i] = stack[insertion_point-1][1]

Similarly for right_b processing:

vals = [x[0] for x in stack]

insertion_point = bisect.bisect_left(vals, val)

if insertion_point ==0:

    no elements < val

else:

    j = insertion_point -1

But wait, for right_b, the stack is sorted in increasing order. We need to find the first element in the stack (smallest index) where val < current val. Because the stack is sorted in increasing order, the first such element is the leftmost one. For example, if stack is [2,3,5], current val is 4. The elements less than 4 are 2,3. The first (smallest) is 2, but we need the first element in the stack that is less than val. So the right_b[i] is the first element in the stack that is < val. But how to find that.

Wait, in the right_b processing, the stack is sorted in increasing order. So the elements are [a_0, a_1, ..., a_m], where a_0 < a_1 < ... < a_m.

We want to find the smallest a_j < val. Which is the first a_j < val. So the first occurrence of a_j < val is a_0, if a_0 < val. Otherwise, there is no such element.

Wait, no. For example, stack is [2,3,5], val is 4. All elements <4 are 2 and 3. The first element is 2. So the right_b[i] would be the position of 2.

But in terms of the original p array, the 2 is the leftmost element in the stack (which is processed from right to left, so 2 is the earliest element in the stack, which is the furthest to the right in p).

Thus, to find the first element in the stack (smallest index) where val < current val, we can use bisect_left to find the insertion point and then check if the insertion point is 0. If not, the first element < val is a_0.

Wait, no. For example, stack [2,3,5], val=4. a_0=2 <4, a_1=3<4, a_2=5>4. So all elements before insertion point (2) are less than 4. The first element is 2.

So for the right_b processing, the first element < val is a_0.

But how to find this.

Thus, the right_b for a non-B element is the first element in the stack (smallest index) with val < current val. Since the stack is sorted in increasing order, the first such element is the first element < val. So the first element in the stack that is < val is a_0 if a_0 < val, else none.

So for right_b:

vals = [x[0] for x in stack]

insertion_point = bisect.bisect_left(vals, val)

if insertion_point ==0:

    # all elements are >= val

    right_b[i] = n

else:

    # there are elements < val. The first is a_0.

    # no, wait. The first element < val is a_0, but only if a_0 < val.

    # wait, the insertion_point is the first index where vals[j] >= val.

    # So elements before insertion_point are < val.

    # So the first element < val is at index 0.

    # So in this case, the first element < val is at insertion_point-1.

    # For example, vals = [2,3,5], val=4. insertion_point is 2. elements before 2 are [2,3]. So insertion_point-1 is 1. So stack[1][0] =3 <4. So the first element < val is 2 (index 0).

    # So this approach is incorrect.

Thus, the previous approach for right_b is incorrect. Hence, the binary search code I had earlier (for right_b) is correct.

In the right_b processing, for non-B elements:

We need to find the first element in the stack (smallest index) where val < current val. Since the stack is sorted in increasing order, the first element < current val is the leftmost element in the stack where val < current val.

Thus, the correct approach is to binary search for the leftmost element < current val.

Which can be done with a modified binary search.

For example:

low = 0

high = len(stack)-1

res = -1

while low <= high:

    mid = (low + high) //2

    if stack[mid][0] < current_val:

        res = mid

        high = mid -1

    else:

        low = mid +1

if res !=-1:

    right_b[i] = stack[res][1]

else:

    right_b[i] = n

This way, res is the smallest index where stack[mid][0] < current_val.

Thus, the code for right_b processing is correct.

So in Python, for large n=1e6, the code needs to handle this efficiently.

But implementing this in Python with loops may be too slow. Let's try to optimize.

But perhaps the code can be optimized using the bisect module.

For right_b:

vals = [x[0] for x in stack]

# find the first element < val.

insertion_point = bisect.bisect_left(vals, val)

if insertion_point ==0:

    # no elements < val

    right_b[i] = n

else:

    # all elements before insertion_point are < val.

    # the first such element is at index 0.

    # but wait, no. For example, vals = [2,3,5], val=4. insertion_point is 2. elements before are 0,1. So the first element < val is 0.

    # So the first element is 0.

    # So the first element < val is the smallest index where val < current_val.

    # So in this case, the first element is at insertion_point - (insertion_point -1) ? No.

    # This approach is incorrect. So the manual binary search is needed.

Thus, the manual binary search is needed.

But for n=1e6, and each binary search O(log k), this is manageable.

In Python, loops are relatively slow for large n, but for 1e6 elements, and each binary search taking 20 steps (log2(1e6) is 20), this is 2e7 steps, which is acceptable.

Thus, the code can proceed as follows.

But first, we need to read the elements of B and create a set.

Then, process p to compute left_b and right_b.

Finally, for each element in p not in B, compute the contribution.

Now, let's put this all together.

The code:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())

    p = list(map(int, input_stream.readline().rstrip("\n").split()))

    b = list(map(int, input_stream.readline().rstrip("\n").split()))

    B_set = set(b)

    pos_in_p = {val: idx for idx, val in enumerate(p)}

    left_b = [-1] * n

    stack = []

    for i in range(n):

        val = p[i]

        if val in B_set:

            # Update stack

            while stack and stack[-1][0] >= val:

                stack.pop()

            if stack:

                left_b[i] = stack[-1][1]

            else:

                left_b[i] = -1

            stack.append( (val, i) )

        else:

            # Binary search for the largest value < val in the stack

            low = 0

            high = len(stack) - 1

            res = -1

            while low <= high:

                mid = (low + high) // 2

                if stack[mid][0] < val:

                    res = mid

                    low = mid + 1

                else:

                    high = mid - 1

            if res != -1:

                left_b[i] = stack[res][1]

            else:

                left_b[i] = -1

    right_b = [n] * n

    stack = []

    for i in range(n-1, -1, -1):

        val = p[i]

        if val in B_set:

            # Update stack

            while stack and stack[-1][0] >= val:

                stack.pop()

            if stack:

                right_b[i] = stack[-1][1]

            else:

                right_b[i] = n

            stack.append( (val, i) )

        else:

            # Binary search for the first element < val in the stack

            low = 0

            high = len(stack) - 1

            res = -1

            while low <= high:

                mid = (low + high) // 2

                if stack[mid][0] < val:

                    res = mid

                    high = mid - 1

                else:

                    low = mid + 1

            if res != -1:

                right_b[i] = stack[res][1]

            else:

                right_b[i] = n

    total = 0

    for i in range(n):

        if p[i] not in B_set:

            L = left_b[i]

            R = right_b[i]

            contribution = R - L - 1

            total += contribution

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10 5
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10
""",
            "output": \
"""\
30
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

n=10, k=5.

p = [1,2,3,4,5,6,7,8,9,10]

b = [2,4,6,8,10]

B_set = {2,4,6,8,10}

Processing left_b:

For i=0 (1), not in B. Stack is empty. left_b[0] =-1.

i=1 (2) is in B. Stack is empty. left_b[1]=-1. Push (2,1).

i=2 (3), not in B.

Binary search stack for val=3.

Stack is [ (2,1) ].

mid=0: 2 <3. res=0. low=1.

Exit loop. res=0. left_b[2]=1.

i=3 (4) in B. Stack has (2,1). 2<4. left_b[3]=1. Push (4,3).

i=4 (5) not in B. stack is [2,4]. binary search for 5.

stack vals are 2,4. Both <5. res=1. left_b[4]=3.

i=5 (6) in B. stack has 2,4. 4<6. left_b[5]=3. Push (6,5).

i=6 (7) not in B. stack is [2,4,6]. binary search for7.

All elements <7. res=2. left_b[6]=5.

i=7 (8) in B. stack has 2,4,6. 6<8. left_b[7]=5. Push (8,7).

i=8 (9) not in B. stack is [2,4,6,8]. binary search for9.

All elements <9. res=3. left_b[8]=7.

i=9 (10) in B. stack has 2,4,6,8. 8<10. left_b[9]=7. Push (10,9).

Processing right_b:

Processing from right to left.

i=9 (10) in B. Stack is empty. Push (10,9). right_b[9]=10.

i=8 (9) not in B. stack is [10]. binary search for9.

stack[0][0]=10>9. res=-1. right_b[8]=10.

i=7 (8) in B. stack is [10]. 10>=8. pop. stack empty. Push (8,7). right_b[7]=10.

i=6 (7) not in B. stack is [8,10]. binary search for7.

stack[0][0]=8>7. res=-1. right_b[6]=10.

i=5 (6) in B. stack is [8,10]. 8>=6. pop. 10>=6. pop. stack empty. Push (6,5). right_b[5]=10.

i=4 (5) not in B. stack is [6,8,10]. binary search for5.

stack[0][0]=6>5. res=-1. right_b[4]=10.

i=3 (4) in B. stack is [6,8,10]. 6>=4. pop. 8>=4. pop. 10>=4. pop. stack empty. Push (4,3). right_b[3]=10.

i=2 (3) not in B. stack is [4,6,8,10]. binary search for3.

stack[0][0]=4>3. res=-1. right_b[2]=10.

i=1 (2) in B. stack is [4,6,8,10]. 4>=2. pop. 6>=2. pop. 8>=2. pop. 10>=2. pop. stack empty. Push (2,1). right_b[1]=10.

i=0 (1) not in B. stack is [2,4,6,8,10]. binary search for1.

stack[0][0]=2>1. res=-1. right_b[0]=10.

Now, for elements not in B:

i=0: contribution=10 - (-1) -1=10.

i=2: L=1, R=10. contribution=10-1-1=8.

i=4: L=3, R=10. 10-3-1=6.

i=6: L=5, R=10. 10-5-1=4.

i=8: L=7, R=10. 10-7-1=2.

Sum:10+8+6+4+2=30. Correct.

Thus, the code works.

Now, handling large inputs.

The code reads n and k, then p and b.

It creates a set B_set for O(1) lookups.

Then, processes left_b and right_b.

Finally, sums the contributions.

The code should be efficient enough for n=1e6.

In Python, using list comprehensions and loops with binary search should work within the time constraints.

Potential optimizations:

- Precompute the B elements' positions in p. Since B is a subsequence of p, but the order is not necessarily sorted.

- However, the current approach processes each element in p once.

The code should work correctly.
</think>

```python
import bisect

n, k = map(int, input().split())
p = list(map(int, input().split()))
b = list(map(int, input().split()))

B_set = set(b)
left_b = [-1] * n
stack = []

# Compute left boundaries
for i in range(n):
    val = p[i]
    if val in B_set:
        while stack and stack[-1][0] >= val:
            stack.pop()
        if stack:
            left_b[i] = stack[-1][1]
        else:
            left_b[i] = -1
        stack.append((val, i))
    else:
        low, high, res = 0, len(stack) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if stack[mid][0] < val:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        left_b[i] = stack[res][1] if res != -1 else -1

right_b = [n] * n
stack = []

# Compute right boundaries
for i in range(n-1, -1, -1):
    val = p[i]
    if val in B_set:
        while stack and stack[-1][0] >= val:
            stack.pop()
        if stack:
            right_b[i] = stack[-1][1]
        else:
            right_b[i] = n
        stack.append((val, i))
    else:
        low, high, res = 0, len(stack) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if stack[mid][0] < val:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        right_b[i] = stack[res][1] if res != -1 else n

total = 0
for i in range(n):
    if p[i] not in B_set:
        total += (right_b[i] - left_b[i] - 1)

print(total)
```
