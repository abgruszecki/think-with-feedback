<think>
Okay, I need to solve this problem where I have to determine if an array can be sorted by swapping at most one pair of elements. Let's think about how to approach this.

First, the problem states that the array was originally sorted in non-decreasing order but might have had two elements swapped. So the goal is to check if the current array can be made sorted by swapping exactly two elements (or zero if it's already sorted).

Let me consider the steps. The straightforward approach would be to compare the current array with the sorted version and see how many positions differ. If there are exactly two differing positions, then swapping those two elements should make the array sorted. Also, if the array is already sorted (zero differences), then the answer is yes.

Wait, but what if there are more than two differing positions? Then it's impossible to fix with a single swap, so the answer is no.

So the plan is:
1. Compare the given array with its sorted version.
2. Collect all the indices where the elements differ.
3. If there are 0 differences, return YES.
4. If there are exactly two differences, check if swapping the elements at those two positions in the original array would make it sorted.
5. Otherwise, return NO.

But wait, maybe even when there are two differences, swapping those elements in the original array might not result in a sorted array. For example, imagine the original array is [3, 2, 1]. The sorted array is [1,2,3]. The differing positions are 0 and 2. Swapping those elements gives [1,2,3], which is correct. But what if the original array was [1,5,3,4,2,6]. The sorted array is [1,2,3,4,5,6]. The differing positions would be 1 and 4. Swapping 5 and 2 gives [1,2,3,4,5,6], which is correct. So in that case, yes.

But wait another example: suppose the original array is [2,1,3,4]. The sorted array is [1,2,3,4]. The differing positions are 0 and 1. Swapping them gives the correct array. So yes.

So the approach is correct for the two differences case. But how to verify that swapping those two elements would indeed result in the sorted array?

Alternatively, perhaps after swapping those two elements in the original array, the array becomes equal to the sorted array. So to check, we can take the original array, swap the two elements, and see if it's now sorted. But that could take O(n) time each time.

But since n can be up to 1e5, we need an efficient approach.

Wait, but in the case where the number of differing positions is exactly two, the sorted array would have those two elements in the swapped positions. So if we swap those two in the original array, the array should match the sorted array exactly.

Wait, maybe not. Let's think. Suppose the original array is a, and the sorted array is sorted_a. The differing positions are i and j. So in the original array, a[i] = sorted_a[j], and a[j] = sorted_a[i]. So swapping i and j in the original array would make a[i] = sorted_a[i], and a[j] = sorted_a[j], thus matching the sorted array.

Is that always the case? Let's see. Suppose the original array is [3,2,1]. The sorted array is [1,2,3]. The differing positions are 0 and 2. Swapping them in original gives [1,2,3], which is correct. Another example: [1,5,3,4,2,6]. Sorted is [1,2,3,4,5,6]. Differing positions 1 and 4. Swapping 5 and 2 gives the correct array.

So yes, if there are exactly two positions where the elements differ from the sorted array, then swapping those two elements in the original array would result in the correct array. Therefore, in that case, the answer is yes.

So the steps are:

- Compute the sorted array.
- Find all the indices where the original array and the sorted array differ.
- If the count is 0: yes.
- If the count is 2: yes.
- Else: no.

Wait, but what if the array is already sorted except for exactly two positions, but swapping those two positions doesn't fix the array? For example, consider [1, 3, 2, 4]. The sorted array is [1,2,3,4]. The differing positions are 1 and 2. Swapping them gives [1,2,3,4], which is correct. So that's okay.

Another example: [5,4,3,2,1]. The sorted array is [1,2,3,4,5]. The differing indices would be all 5 positions. So count is 5, which is more than 2. So answer is no.

Wait, but the sample input 2 is [3,2,1]. The sorted array is [1,2,3]. The differing positions are 0 and 2. So count is 2, hence yes. Which matches the sample.

So this approach seems correct.

So the algorithm is:

1. Create a sorted version of the array.
2. Compare the original and sorted arrays, collecting the indices where they differ.
3. If the number of differing indices is 0: output yes.
4. If the number is 2: check if swapping those two elements in the original array makes it sorted. Or, perhaps, just check if the original array's elements at those positions match the sorted array's elements in reverse.
   Wait, because in the sorted array, the elements at i and j are a_sorted[i] and a_sorted[j]. In the original array, the elements are a_sorted[j] and a_sorted[i]. So swapping those two would make them correct.

But to confirm that, perhaps the number of differing positions is 2, then the answer is yes. Because swapping those two would fix the array.

Wait, but perhaps the original array's elements are such that even if we swap two positions with differing elements, the array isn't sorted. For example, maybe there are other elements that are out of order. But according to the problem statement, the array could have been sorted except for exactly one swap. So the array can be made sorted by a single swap. So how can the array differ in two positions but swapping those two doesn't make it sorted?

Hmm. Let me think. Suppose the array is [1, 4, 3, 2, 5]. The sorted array is [1,2,3,4,5]. The differing indices are 1 and 3. Swapping the elements at these indices in the original array (4 and 2) gives [1,2,3,4,5], which is correct. So that's okay.

Another example: [2,1,3,5,4]. Sorted array is [1,2,3,4,5]. The differing indices are 0,1,3,4. So count is 4, so answer is no.

But if the count is 2, then the swap would work.

So the approach is to check the count. But wait, maybe the array is such that after swapping two elements, the rest are in order. For example, what if the original array is [3,2,1,4]. The sorted array is [1,2,3,4]. The differing indices are 0 and 2. Swapping them gives [1,2,3,4], which is sorted. So that's okay.

Wait, but what if the array is [1,3,2,4,6,5]. The sorted array is [1,2,3,4,5,6]. The differing indices are 1 and 2, 4 and 5. So four differences. So answer is no.

So the approach of checking the number of differing indices works.

Therefore, the algorithm is:

1. Compare the original array with the sorted array and collect all the differing indices.
2. If there are 0 differences: yes.
3. If there are exactly two differences: yes.
4. Else: no.

Wait, but in the second sample input:

Input is 3 elements: 3,2,1. The sorted array is 1,2,3. The differing indices are 0 and 2. So count is 2. So answer is yes.

Sample three input is 4 elements: 4,3,2,1. The sorted array is 1,2,3,4. So all four indices differ. So count is 4, answer is no. Which matches the sample.

So the approach seems correct.

But wait, let's think of a case where the array can be fixed by swapping two elements but the count of differing indices is more than two. For example:

Original array: [1, 5, 3, 4, 2]. Sorted array: [1,2,3,4,5]. The differing indices are 1,2,4. So count is 3. So according to our approach, the answer is no. But if we swap 5 and 2, the array becomes [1,2,3,4,5], which is sorted. So the answer should be yes, but according to the approach, we would output no. Which is a problem.

Wait, this is a critical case. Let's see:

Original array: [1,5,3,4,2]. Sorted array is [1,2,3,4,5]. The differing positions are:

Indices 1 (5 vs 2), 2 (3 vs 3? No, 3 is correct. Wait, original array is 5, 3,4,2. Wait no:

Original array is [1,5,3,4,2].

Original index 0: 1. Sorted index 0:1. Same.

Index 1:5 vs sorted's 2. Different.

Index 2:3 vs 3. Same.

Index3:4 vs4. Same.

Index4:2 vs5. Different.

So the differing indices are 1 and 4. So count is 2. Then the approach would say yes.

Wait, but in this example, swapping indices 1 and 4 gives [1,2,3,4,5], which is correct.

So the count is 2, so the answer is yes. So why did I think the count is 3?

Ah, because I made a mistake in analyzing the example. Let me recheck.

Original array: [1,5,3,4,2].

Sorted array is [1,2,3,4,5].

Comparing element by element:

Indices 0: 1 ==1 → same.

Index1:5 vs 2 → different.

Index2:3 vs3 → same.

Index3:4 vs4 → same.

Index4:2 vs5 → different.

So the differing indices are 1 and 4. Count is 2. So according to the approach, answer is yes. Which is correct.

So this example works.

Another example where swapping two elements not adjacent in the sorted array.

Another test case: [1, 3, 2, 4]. The sorted array is [1,2,3,4]. The differing indices are 1 and 2. Swapping them gives correct array. So count is 2 → yes.

So the approach works.

So the algorithm is correct.

So the steps are:

- Generate the sorted array.
- Compare each element with the original array.
- Collect the indices where they differ.
- If the count is 0 or 2, return yes, else no.

So the code can be written as follows.

Now, considering the constraints:

n can be up to 1e5. Sorting the array is O(n log n), which is acceptable. Then comparing the arrays is O(n), which is okay.

In Python, for n=1e5, this should be manageable.

Now, implement this.

So code steps:

Read n.

Read array as a list.

Create a sorted version of the array.

Compare the two, collect the indices where they differ.

If len(diffs) is 0 or 2: output YES else NO.

Wait, but what if the array is already sorted (len(diffs) ==0), then output yes. Correct.

If len(diffs) is 2: check if swapping the two elements would make the array sorted. But according to the earlier analysis, that's automatically the case. So we can proceed.

Wait, but wait. Let's think of a case where the array is almost sorted, but swapping two elements that are in the same position as the sorted array's elements would not fix it. Wait, but how?

For example, original array is [2,1]. Sorted is [1,2]. diffs are 0 and 1. Swapping them gives the sorted array. So yes.

Another example: [1,3,2,4]. The sorted array is [1,2,3,4]. diffs at 1 and 2. Swapping gives [1,2,3,4]. So correct.

But suppose a scenario where the original array has two elements swapped, but those elements are the same. For example, [1,2,3,2]. The sorted array is [1,2,2,3]. The original array's elements are [1,2,3,2], sorted is [1,2,2,3]. The differing indices are 2 and 3. Swapping elements 3 and 2 would result in [1,2,2,3], which is correct. So even if elements are equal, the code would return yes.

But what if the array is [2, 1, 2]. Sorted array is [1,2,2]. The original array is [2,1,2]. The diffs are at index 0 and 1. Swapping gives [1,2,2], which is correct. So code returns yes.

Another case: [3, 2, 1, 4]. Sorted array is [1,2,3,4]. Diffs are 0 and 2. Swapping them gives [1,2,3,4]. Correct.

So the code would work.

Therefore, the code can proceed as follows.

Now, the code in Python:

Read n.

a = list of integers.

sorted_a = sorted(a).

diffs = list of indices where a[i] != sorted_a[i]

If len(diffs) ==0 → YES.

elif len(diffs) ==2 → check if a[diffs[0]] == sorted_a[diffs[1]] and a[diffs[1]] == sorted_a[diffs[0]].

If so, then YES. Else, NO.

Wait, but earlier analysis said that if the number of diffs is exactly two, then the answer is yes. But perhaps in some cases, even with two diffs, swapping those two elements in the original array would not result in a sorted array.

Wait, for example:

Original array: [1, 5, 3, 4, 2, 6]. The sorted array is [1,2,3,4,5,6]. The diffs are at indices 1 and 4. Swapping 5 and 2 gives the correct array.

But what if the original array is [1, 5, 4, 3, 2, 6]. Sorted array is [1,2,3,4,5,6]. The diffs are at indices 1, 2, 3, 4. So four diffs → answer is no. So code works.

Another example: suppose original array is [2, 1, 3, 4]. Sorted is [1,2,3,4]. Diffs are 0 and 1. Swapping gives correct array → yes.

What if the original array is [3, 2, 1, 4, 5]. Sorted is [1,2,3,4,5]. Diffs are 0,1,2. So len(diffs) is 3 → answer is no.

So the code works.

But what about the following scenario: the array can be sorted with a single swap, but the number of differing positions is more than two. For example:

Original array: [1, 7, 3, 4, 5, 6, 2, 8]. Sorted is [1,2,3,4,5,6,7,8]. The diffs are at index 1 (7 vs2) and index6 (2 vs7). So two differing positions. Swapping 1 and 6 gives the correct array → yes. So code works.

Another example where the number of diffs is two but swapping doesn't work. Is that possible?

Wait, let's imagine:

Original array: [3, 2, 1, 4]. Sorted is [1,2,3,4]. Diffs are at 0 and 2. Swapping 3 and 1 gives [1,2,3,4], which is correct. So code says yes.

But what if the original array is [3, 2, 1, 4, 5, 6, 7]. Sorted is [1,2,3,4,5,6,7]. Diffs are 0 and 2. Swapping 3 and 1 gives correct array → yes.

So what's a case where the code would incorrectly return yes?

Wait, suppose the array is [1, 3, 2, 4]. Sorted array is [1,2,3,4]. Diffs are 1 and 2. Swapping them gives [1,2,3,4] → correct. So code returns yes.

But what if the array is [1, 4, 3, 2, 5]. Sorted array is [1,2,3,4,5]. Diffs are 1 and 3. Swapping 4 and 2 gives [1,2,3,4,5], correct. So code returns yes.

So I can't think of a case where the code would fail. So the code is correct.

Therefore, the code should be:

Read n, read the array, compute sorted array, compute diffs. If the number of diffs is 0 → yes. If it's 2, check if swapping those two elements in the original array makes it equal to the sorted array. If yes, output yes. Else no. Otherwise, output no.

Wait, but why do we need to check swapping those two elements? Because in some cases, even with two diffs, swapping them might not result in the correct array.

Wait, no. Because the sorted array is the correct one. So the original array's elements at the two diffs must be swapped to match the sorted array. So the check is to see if a[i] == sorted_a[j] and a[j] == sorted_a[i].

If that's the case, then swapping i and j in the original array will make it sorted. So the code must verify this.

Ah, right. Because in some cases, even if there are two diffs, the elements might not be swapped.

For example, imagine the original array is [1, 2, 4, 3, 5]. The sorted array is [1,2,3,4,5]. The differing indices are 2 and 3. In the original array, a[2] is 4, a[3] is 3. In the sorted array, a[2] is 3 and a[3] is4. So swapping those two positions in the original array gives [1,2,3,4,5], which is correct. So the code would return yes.

But what if the elements at those two positions are not each other's counterparts in the sorted array?

For example, original array is [1, 3, 2, 4]. Sorted array is [1,2,3,4]. The differing indices are 1 and 2. a[1] is3, a[2] is2. In the sorted array, a[1] is2, a[2] is3. So swapping them in original gives 2 and3, which matches. So code returns yes.

But suppose:

Original array is [1, 5, 3, 4]. Sorted array is [1,3,4,5]. The differing indices are 1 and 3. Original a[1] is5, a[3] is4. Sorted a[1] is3, a[3] is5. So swapping 5 and4 would give 4 and5 in the original array. The new array would be [1,4,3,5]. Sorted array is [1,3,4,5]. So this new array is not sorted. So the code would incorrectly return yes, but the actual answer is no.

Wait, but how can this happen? Let's see:

In this example, the original array is [1,5,3,4]. The sorted array is [1,3,4,5]. The differing indices are 1 (5 vs3), 2 (3 vs4), and 3 (4 vs5). So the count is three. So the code would output no. So this example is invalid.

Wait, no. Let's compute the sorted array of [1,5,3,4] → sorted is [1,3,4,5]. Comparing each element:

index 0: 1 → same.

index1:5 vs3 → different.

index2:3 vs4 → different.

index3:4 vs5 → different.

So three differing indices. So code returns no.

But let's create an example where there are exactly two differing indices but swapping them doesn't fix the array.

Example:

Original array: [1, 3, 2, 4]. Sorted array is [1,2,3,4]. Diffs are at indices 1 and2. Swapping gives correct array.

Another example: [2,1,3]. Sorted is [1,2,3]. Diffs are 0 and1. Swapping gives correct.

But what if:

Original array: [1, 4, 3, 2]. Sorted array is [1,2,3,4]. Diffs are 1 and3. Original a[1] is4, a[3] is2. Swapping them gives [1,2,3,4], which is correct.

So code returns yes.

But suppose:

Original array: [1, 2, 4, 3, 5, 6]. Sorted array is [1,2,3,4,5,6]. Diffs are at 2 and3. Swapping them gives [1,2,3,4,5,6] → correct.

Another example where there are two diffs but the elements are not each other's counterparts.

Wait, can that happen?

Suppose original array is [1, 5, 3, 4, 2]. Sorted array is [1,2,3,4,5]. Diffs are at indices 1 and4. Original a[1]=5, a[4]=2. In sorted array, a[1]=2, a[4]=5. So swapping indices 1 and4 in original array gives [1,2,3,4,5], which is correct.

So the code will return yes.

Another example: original array is [1, 5, 4, 3, 2, 6]. Sorted array is [1,2,3,4,5,6]. Diffs are indices 1,2,3,4. Count is 4 → code returns no.

So the code works.

But let's think of a case where the number of differing positions is two, but the elements are not swapped. For example:

Original array: [1, 3, 2, 4, 5]. Sorted array is [1,2,3,4,5]. Diffs are indices 1 and2. Original a[1] is3, a[2] is2. In the sorted array, a[1] is2 and a[2] is3. So swapping them gives correct array. So code returns yes.

So the code needs to check whether the elements in the two differing positions in the original array are the same as the elements in the sorted array but swapped. Because in cases where the two differing positions in the original array do not have elements that are each other's counterparts in the sorted array, swapping them would not result in a sorted array.

Wait, but how could the number of differing positions be two, but the elements at those positions in the original array are not the ones in the sorted array's positions?

For example:

Original array: [1, 5, 3, 4, 2, 6]. Sorted array is [1,2,3,4,5,6]. Diffs are indices 1 and4. Original a[1] is5, a[4] is2. In sorted array, a[1] is2 and a[4] is5. So swapping them in original array gives 2 and5, which matches sorted array.

But what if the original array is [1, 5, 3, 4, 7, 6]. Sorted array is [1,3,4,5,6,7]. Diffs are indices 1,4,5. So count is 3 → code returns no.

Hmm, I can't find a case where the number of differing positions is two, but swapping those two elements would not fix the array.

But perhaps this is possible. For example:

Original array: [3, 2, 1, 4, 5]. Sorted array: [1,2,3,4,5]. Diffs are indices 0 and2. Original a[0] =3, a[2] =1. Sorted a[0]=1, a[2]=3. So swapping indices 0 and2 gives [1,2,3,4,5], which is correct. So code returns yes.

Another example:

Original array: [2, 1, 4, 3]. Sorted array is [1,2,3,4]. Diffs are indices 0,1,2,3. So count is4 → code returns no.

But suppose the original array is [4, 2, 3, 1]. Sorted array is [1,2,3,4]. Diffs are indices 0,1,2,3. So code returns no.

Another scenario: What if there are two differing positions, but the elements are not swapped. For example:

Original array is [1, 3, 2, 4, 5]. Sorted array is [1,2,3,4,5]. Diffs are 1 and 2. Swapping gives correct array.

But what if the original array is [1, 3, 4, 2, 5]. Sorted array is [1,2,3,4,5]. Diffs are 1,2,3. Count is3 → code returns no.

So the code seems correct.

But wait, here's a possible problem. Suppose the array is [1, 2, 2, 3]. The sorted array is [1,2,2,3]. So no diffs → code returns yes.

But what if the array is [1, 3, 2, 2]. The sorted array is [1,2,2,3]. Diffs are indices 1 and3. Original a[1] is3, a[3] is2. Swapping them gives [1,2,2,3], which is sorted. So code returns yes.

But if the array is [1, 3, 3, 2]. Sorted array is [1,2,3,3]. Diffs are indices 1 and3. Original a[1] is3, a[3] is2. Swapping gives [1,2,3,3], which is sorted. So code returns yes.

Another example: array is [2, 1, 1, 1]. Sorted array is [1,1,1,2]. Diffs are 0 and3. Swapping gives [1,1,1,2]. So yes.

So all cases seem to work.

But wait, what if the array is [1, 4, 3, 2]. Sorted array is [1,2,3,4]. Diffs are indices 1 and3. Original a[1]=4, a[3]=2. Swapping gives [1,2,3,4], which is correct. So code returns yes.

Therefore, the code is correct.

But why is the code checking the two differing elements in the original array? Because if the count is two, but swapping those two elements in the original array doesn't make it sorted, then the answer is no.

But according to the problem statement, the array can be sorted by swapping exactly two elements. So in such a case, the code would return yes if the count is two, but that's incorrect.

Wait, but how can the count be two but swapping doesn't work?

Let me think of a scenario.

Example:

Original array: [1, 2, 4, 3, 5]. Sorted array is [1,2,3,4,5]. Diffs are indices 2 and3. Swapping them gives [1,2,3,4,5]. So code returns yes.

But what if the original array is [1, 5, 3, 4, 2]. Sorted array is [1,2,3,4,5]. Diffs are indices 1 and4. Swapping gives [1,2,3,4,5]. So code returns yes.

Another example:

Original array: [1, 3, 2, 5, 4]. Sorted array is [1,2,3,4,5]. Diffs are indices 1,2,3,4. Count is4 → code returns no.

But if you swap 3 and4 in the original array (indices3 and4), you get [1,3,2,4,5]. Which is not sorted. So code returns no.

But according to the problem statement, can the array be sorted by swapping any two elements? For example, if you swap indices 1 and2 (3 and2) in the original array, you get [1,2,3,5,4]. Which is not sorted. So code would not return yes.

But in this case, the array cannot be sorted by a single swap.

So the code correctly returns no.

Thus, the code's approach is correct.

So in code:

Compute the sorted array.

Compute the list of indices where a[i] != sorted_a[i].

If len(diffs) is 0 → YES.

Elif len(diffs) ==2:

   check if a[diffs[0]] == sorted_a[diffs[1]] and a[diffs[1]] == sorted_a[diffs[0]]. If yes → YES, else NO.

Else → NO.

Wait, this is important. Because there could be two differing indices but the elements in those positions in the original array are not the same as the elements in the sorted array's positions. For example:

Original array: [1, 2, 4, 3, 5]. Sorted array is [1,2,3,4,5]. Diffs are 2 and3. Original a[2]=4, a[3]=3. In sorted array, a[2]=3, a[3]=4. So swapping 2 and3 in original array gives correct array.

But what if:

Original array is [1, 2, 5, 4, 3]. Sorted array is [1,2,3,4,5]. Diffs are 2,3,4. Count is3 → code returns no.

Another example: [1, 3, 2, 5, 4]. Sorted is [1,2,3,4,5]. Diffs are indices1,2,3,4. Count is4 → code returns no.

But what if the original array is [1, 5, 3, 4, 2]. Diffs are indices1 and4. Swapping them gives correct.

But what if the original array is [1, 3, 2, 5, 4]. Sorted array is [1,2,3,4,5]. Diffs are 1,2,3,4 → count is4. So code returns no.

But what if the original array is [1, 4, 3, 2, 5]. Sorted array is [1,2,3,4,5]. Diffs are indices1 and3. Original a[1] is4, a[3] is2. sorted a[1] is2, a[3] is4. So swapping gives [1,2,3,4,5]. So code returns yes.

Thus, in code, when the count is two, we need to check that the two elements in the original array are exactly the two elements needed. Because even if the count is two, swapping those two elements might not result in a sorted array.

Wait, but in the case where the count is two, how could the elements not match? Let's think of a case.

For example, suppose original array is [1, 3, 2, 4]. Sorted array is [1,2,3,4]. Diffs are indices1 and2. original a[1]=3, a[2]=2. sorted a[1]=2, a[2]=3. Swapping gives [1,2,3,4], which is correct. So code returns yes.

Another example: original array [1, 2, 4, 3]. Diffs are 2 and3. Swapping gives correct.

But what if:

Original array is [1, 2, 5, 4, 3]. Sorted array is [1,2,3,4,5]. Diffs are indices2,3,4. So count is3 → code returns no.

But another example:

Original array is [1, 5, 3, 2, 4]. Sorted array is [1,2,3,4,5]. Diffs are indices1 and3. original a[1]=5, a[3]=2. sorted a[1]=2, a[3]=4. So swapping gives [1,2,3,5,4]. The new array would be [1,2,3,5,4]. The sorted array is [1,2,3,4,5]. So the new array is not sorted. So code would have two diffs, but swapping them doesn't fix the array. So code would output yes, but the actual answer is no.

Wait, but according to the code's logic, when the count is two, it checks whether a[diffs[0]] == sorted_a[diffs[1]] and a[diffs[1]] == sorted_a[diffs[0]]. If that's the case, then swapping would make the array sorted. Otherwise, no.

So in the example above, after swapping, the array would be [1,2,3,5,4]. The sorted array is [1,2,3,4,5]. The new array would have differing indices at 3 and4. So the count is two again. So the code would not output yes.

So, the code's check is necessary.

So the code should not just check if the count is two, but also whether the elements in the original array at those two positions are swapped in the sorted array.

So the code's logic is:

if the number of differing positions is two, then check if the original array's elements at those positions are exactly the elements in the sorted array's positions but swapped. If yes, then output yes. Else, no.

So this is an essential part of the code.

In the example I mentioned:

Original array: [1,5,3,2,4]. Sorted array is [1,2,3,4,5]. The differing positions are 1 (5 vs2) and3 (2 vs4).

So in the original array, a[1] =5, a[3] =2. In the sorted array, a[1] =2, a[3] =4.

So the check is:

a[1] == sorted_a[3] →5 ==4 → no.

a[3] == sorted_a[1] →2 ==2 → yes.

So overall, no. So the code would return no.

So the code is correct in this case.

Thus, the code must check that both elements match the swapped positions in the sorted array.

Therefore, the code's steps are:

- Compute the sorted array.

- Collect the indices where the original and sorted arrays differ.

- If len(diffs) is 0 → yes.

- If len(diffs) is 2 → check if the elements in the original array at those two positions are equal to the sorted array's elements at the swapped positions.

- Else → no.

So now, the code in Python:

Read n.

a = list(map(int, input().split())).

sorted_a = sorted(a).

diffs = [i for i in range(n) if a[i] != sorted_a[i]]

if len(diffs) ==0:

    print("YES")

elif len(diffs) ==2:

    i, j = diffs

    if a[i] == sorted_a[j] and a[j] == sorted_a[i]:

        print("YES")

    else:

        print("NO")

else:

    print("NO")

That should handle all cases.

Testing against sample inputs 1, 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    sorted_a = sorted(a)
    diffs = [i for i in range(n) if a[i] != sorted_a[i]]
    if len(diffs) == 0:
        print("YES", file=output_stream)
    elif len(diffs) == 2:
        i, j = diffs
        if a[i] == sorted_a[j] and a[j] == sorted_a[i]:
            print("YES", file=output_stream)
        else:
            print("NO", file=output_stream)
    else:
        print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
3 2 1
""",
            "output": \
"""\
YES
""",
        }, 
        {
            "input": \
"""\
4
4 3 2 1
""",
            "output": \
"""\
NO
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

Sample3:

Input 4 4 3 2 1. Sorted is [1,2,3,4]. diffs are 0,1,2,3 → code returns no.

Another test case where there are two diffs but swapping doesn't work:

Original array [1,5,3,2,4]. sorted array is [1,2,3,4,5]. diffs are 1 and3. a[1]=5, sorted_a[3]=4. a[3]=2, sorted_a[1]=2. So a[i] (5) != sorted_a[j] (4), so code returns no.

Thus, the code correctly handles this case.

So the code is correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a)
diffs = [i for i in range(n) if a[i] != sorted_a[i]]
if len(diffs) == 0:
    print("YES")
elif len(diffs) == 2:
    i, j = diffs
    if a[i] == sorted_a[j] and a[j] == sorted_a[i]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
```
