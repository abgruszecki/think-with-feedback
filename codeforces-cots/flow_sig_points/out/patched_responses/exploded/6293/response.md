<think>
Okay, let's see. The problem is to determine whether we can split the array into two non-empty consecutive parts with equal sums by moving exactly one element. Hmm. So, the idea is that after moving one element, there exists a split where the sum of the prefix equals the sum of the suffix.

First, I need to find out under what conditions this is possible. Let's think about the original array's total sum. Let's denote the total sum as S. If S is even, then it's possible to split without moving any elements only if there's a point where the cumulative sum is S/2. But since the problem requires moving exactly one element, even if S is even, we still have to check the possibility after moving.

Wait, but when we move an element, the total sum remains the same. So, after moving, the total sum is still S. To split the array into two parts with equal sums, S must be even. Because each part would have sum S/2. So the first thing to check is if the total sum is even. Wait, no. Wait, because moving an element doesn't change the total sum, right? Because we are just moving it, not adding or removing. So the sum S remains the same. So for the split to have equal sums, S must be even. So if S is odd, the answer is definitely NO. Because even after moving, the sum is still odd, so it's impossible to split into two equal parts. That's an important check. So first, check if the total sum is even. If not, output NO immediately.

So the first step: compute the total sum. If it's odd, return NO.

If it's even, then we need to check if there's a way to move one element so that the array can be split into two parts with sum S/2 each.

But how to model moving one element? Let's think. Moving an element can be thought of as removing it from the array and inserting it somewhere else. So, after moving, the array's elements are the same, just reordered. But the split has to be consecutive. So the split is based on the position after moving.

Wait, but when moving, the element is inserted into a new position. So for example, if the original array is [a, b, c], moving b to the end gives [a, c, b]. Then, the possible splits are after first element (a vs c + b), after second (a + c vs b), etc. So in this case, the sum of the split is determined by the new array.

So the problem reduces to: can we find an element to remove (and reinsert somewhere else) such that in the new array, there exists a split into two parts (prefix and suffix) with sum S/2 each.

Alternatively, perhaps there's a way to model this. Let's think of the original array. If there's a way to remove one element and insert it such that in the modified array, the sum of some prefix equals S/2.

Wait, but moving an element is equivalent to modifying the array by taking one element from position i and placing it in position j. So the modified array will have that element in a new position, but the rest in the same order except for the shift caused by the move.

But considering all possible moves is computationally expensive, especially for large n. So we need a smarter approach.

Let me think differently. Let's say that the total sum S must be even. So the target for each part is T = S/2.

Now, in the original array, perhaps there's a split where the sum is T, but since the problem requires moving exactly one element, that's not allowed. So we need to see if moving one element can create such a split.

But how?

Another approach: Let's consider that moving one element is equivalent to changing the sum of the left and right parts. For instance, if we move an element from the left part to the right part, or vice versa.

Alternatively, perhaps the movement can adjust the cumulative sums in such a way that after moving, the sum of a prefix becomes T.

Let me think of the original array's prefix sums. Let's compute the prefix sums array. For each possible split point k (after the k-th element), the sum is prefix[k], and the sum of the suffix is S - prefix[k]. We need to find a k where prefix[k] = T.

But in the original array, if there's such a k, then the answer is YES even without moving, but according to the problem statement, the split must be done after moving exactly one element. Wait, no. Wait, the problem says that Vasya will move some element before dividing. So the original array may already have a split, but since he must move an element (even if it's not needed), the answer would be NO in that case. Oh right! Because the problem requires that after moving one element, then the split is possible. So even if the original array can be split into two parts, if moving an element is required, then the answer is NO. So in other words, the original array can't already have a valid split. So the solution must involve moving exactly one element, even if it's not necessary. So the problem is to check whether after moving exactly one element, such a split exists.

So the steps are:

1. Check if total sum S is even. If not, output NO.
2. Otherwise, T = S/2.
3. Now, check whether there exists an element a_i such that when we remove a_i from the array, and insert it somewhere else, the new array has a split point k where the sum of the first k elements is T.

But how to model this?

Alternatively, perhaps the movement can allow us to adjust the sum of the prefix. Let's think: when moving an element from position i to position j (i != j), how does this affect the prefix sums?

Alternatively, perhaps we can model the problem as follows: for each possible element a_i, we can check if moving it allows the sum of some prefix (after moving) to be T.

But how?

Let's consider moving a_i from position i to position j. Let's suppose j is in the left part (prefix) or right part (suffix). So, the effect on the sum would vary.

Alternatively, perhaps the idea is to find that after moving a_i, in the new array, there exists a split where the sum is T. So, for each element a_i, we can check if removing it and considering possible positions where inserting it would create a split point.

But trying all possible a_i and possible positions is O(n^2), which is not feasible for n=1e5.

Therefore, we need a smarter approach.

Let's think: when you move an element, the sum of the array remains the same (T*2). So the split must have exactly T in each part.

The idea is that after moving an element, the cumulative sum at some point k must be T. Let's see.

Suppose that in the original array, the prefix sum array is prefix. We can compute this array once.

Now, for each possible element a_i, when we remove it from the array, the prefix sums change. But inserting it elsewhere may allow the sum to reach T.

Wait, but inserting it back into the array would create a new array of size n (since we're just moving the element). So, after moving a_i, the array has the same elements, just reordered.

Hmm. So perhaps, for each possible a_i, we can check if there exists a position to insert it such that in the new array, some prefix sum is T.

But how?

Alternatively, maybe the movement can adjust the sum in a way that after moving a_i, the sum of the left or right part can be adjusted by the difference of a_i's position.

Let me try to model this. Let's suppose we take an element a_i and move it from its original position to some other position. How does this affect the prefix sums?

Let's imagine the original array is A, and after moving a_i to position j (j can be before or after its original position i), the new array is A'. Let's consider the prefix sum in A' at position k.

But calculating all possible possibilities for each a_i is expensive.

Alternatively, perhaps for each a_i, there's a way to check if moving it can help reach a certain sum.

Another idea: Let's think of the original array's prefix sums. Let's compute all possible possible splits in the original array. For each split point k (from 1 to n-1), the sum is prefix[k]. If we can find a way to adjust this sum by moving an element such that it becomes T.

Suppose that in the original array, the sum at split k is S_prev. If we move an element from the left part to the right part, then the sum of the left part (after split k) would decrease by a_i, and the right part would increase by a_i. Wait, perhaps not. Let me think again.

Wait, when you split the array into left and right parts, moving an element from left to right would subtract it from the left and add it to the right. Similarly for moving from right to left.

So, for example, suppose in the original array, the sum of the left part (prefix) is S_left. When we move an element a_i from the left part to the right part, the new S_left becomes S_left - a_i. Then, the sum of the right part (original S_right) becomes S_right + a_i. But in this case, after moving, the split is still at the same position k. But maybe the split point changes.

But this is getting complicated.

Alternatively, let's consider that for the split to be possible after moving an element a_i, there exists a split point k such that in the modified array, the sum of the first k elements is T.

So, for each possible a_i, we can model how moving it affects the possible sum of some prefix.

Let me try to model this.

Suppose we have the original prefix sums. For each element a_i, which is at position i in the array (assuming 0-based or 1-based? Let's say 1-based for the original array).

When we remove a_i from the array, the array becomes n-1 elements. But then inserting a_i into some position j (could be any position, including the same as i). The new array is of length n again.

But how to model the prefix sums after insertion?

Alternatively, perhaps the movement can be considered as removing a_i, then the sum of the array is S - a_i. Then, inserting it back in some position. But the sum remains S.

Wait, but inserting it back into the array doesn't change the sum. So after moving, the sum is still S. So the split must sum to T = S/2.

So the problem is equivalent to: can we move one element such that there exists a split point k (1<=k<=n-1) where the sum of the first k elements in the new array is T.

But how to model this efficiently?

Alternative approach: Let's imagine that moving a_i to some position j in the array. For each possible a_i, perhaps we can find whether there's a j such that inserting a_i at j creates a split where the sum is T.

But trying all possible j for each a_i is O(n^2), which is too slow.

Hmm. So we need a way to find, for each a_i, whether moving it to a certain position allows a split sum to reach T.

Another idea: Let's consider that after moving a_i, the sum of the first k elements in the new array is T.

Let's think of the original array as a sequence of elements. When we remove a_i, the array becomes A without a_i. Then inserting a_i into position j (could be anywhere) gives a new array. For this new array, the prefix sum at position k is the sum of the first k elements.

So, for example, if we insert a_i at position j, then:

- The new array is [a_1, a_2, ..., a_{j-1}, a_i, a_j, a_{j+1}, ..., a_{i-1}, a_{i+1}, ..., a_n}]. But this depends on the original positions.

Alternatively, perhaps it's easier to model the effect of moving a_i. For instance, moving a_i from its original position to position j. The effect on the prefix sums depends on the original positions and the new position.

But this seems complicated.

Alternative approach: Let's compute for each possible a_i, the sum that could lead to T when a_i is moved.

For example, suppose we have a_i. If we move a_i from the left part of a split to the right part, then the sum of the left part would decrease by a_i, and the sum of the right part would increase by a_i. Similarly, moving from the right to the left would have the opposite effect.

But perhaps the split point can be adjusted. For example, suppose in the original array, a split at k has sum S_prev. If we move an element from the left to the right, then the sum of the left part (split at k) becomes S_prev - a_i. If this equals T, then moving a_i to the right part would give a valid split. But the problem is that after moving, the split is in the modified array, not the original.

Alternatively, perhaps for each a_i, we can check if there's a split point k in the original array such that:

If a_i was moved from the left part (i <=k) to the right part (j >k), then the new sum of the first k elements would be (original sum up to k) - a_i. We want this to be T.

So T = original_prefix[k] - a_i. So original_prefix[k] - a_i = T => original_prefix[k] = T + a_i.

Alternatively, if a_i is in the right part (i >k) and moved to the left part (j <=k), then the sum of the first k elements would be original_prefix[k] + a_i. We want this to be T. So original_prefix[k] + a_i = T.

So these are two possibilities for each a_i.

So for each a_i, we can check:

Case 1: a_i is in the left part (original position i <=k), then the split sum after moving to right would be original_prefix[k] - a_i. We need this to be T.

So original_prefix[k] = T + a_i.

We can look for any k >=i such that original_prefix[k] equals T +a_i. Because when we move a_i from the left to the right part (split at k), the sum would decrease by a_i, so T is achieved.

Case 2: a_i is in the right part (original position i >k), then moving it to the left part (split at k) would add a_i to the left sum. So original_prefix[k] +a_i = T.

So we need to find a k where original_prefix[k] = T -a_i.

So for each a_i, in the original array, check if there's a k such that either:

a) original_prefix[k] = T +a_i, and a_i was originally at position i <=k. Then, moving a_i to the right part (split k) would give sum T.

or

b) original_prefix[k] = T -a_i, and a_i was originally at position i >k. Then, moving a_i to the left part (split k) would give sum T.

If either of these is possible for any a_i, then the answer is YES.

So the steps would be:

Compute the total sum S. If S is odd, return NO.

Compute T = S/2.

Compute the prefix sum array.

For each element a_i in the array:

   Check if there exists a split k (1 <=k <=n-1) such that:

   case 1: a_i is in the left part (i <=k) and prefix[k] == T +a_i.

   OR

   case 2: a_i is in the right part (i >k) and prefix[k] == T -a_i.

If any a_i satisfies either case, then return YES.

If none do, return NO.

This approach would be O(n), since for each a_i, we can check the presence of T +a_i and T -a_i in the prefix sum array, considering the position i.

But how to efficiently check these conditions?

For case 1:

We need to find a k >=i where prefix[k] = T +a_i.

But the split k must be at least i, and <=n-1.

So for a_i at position i, we can look for any k in [i, n-1] where prefix[k] is T +a_i.

But how to check this quickly? We can precompute a hash set or a dictionary that maps the prefix sums to their indices, but since prefix sums can be up to 1e14 (since ai is up to 1e9 and n is 1e5), but using a hash set is feasible.

Wait, but we need to check if T +a_i exists in the prefix array at a position >=i. So perhaps for each a_i, we can compute T_plus = T +a_i, and see if T_plus exists in the prefix array, and the earliest index where it occurs is >=i, and the latest index is <=n-1.

Similarly, for case 2: T_minus = T -a_i. Check if T_minus exists in the prefix array, and the index where it occurs is <i (since i>k, so k can be from 1 to i-1, but split k can't be 0 because the split parts need to be non-empty).

So the plan is:

1. Compute S. If S is odd, return NO.

2. Compute T = S/2.

3. Compute the prefix array. Also, build a dictionary that maps each prefix sum to a list of indices where it occurs. The indices are 0-based or 1-based? Let's be precise here. Let's assume the array is 0-based for the code.

Wait, let's think again. Let's say the array is 1-based in the problem statement. But in code, it's easier to handle 0-based.

Let's see. For example, in the first sample input:

3 elements: 1,3,2.

Original prefix sums (0-based):

prefix[0] =1

prefix[1] =4

prefix[2] =6.

S=6, which is even. T=3.

For each a_i:

Take i=0 (a_i=1):

case1: T + a_i =3+1=4. Check if any k >=0 (i=0) in prefix array has value 4. Yes, prefix[1] is 4. So k=1. Then, split at k=1 in the modified array. The original split would be after k=1 elements. But after moving a_i (1) from position 0 (which is <=k) to the right part, the sum becomes 4-1=3, which is T. So this split would work. So the answer is YES.

So for this case, the code would find that a_i=1 (i=0) satisfies case1, since T+a_i=4 is present in prefix at position 1, which is >=i=0. Hence, the answer is YES.

So the approach works for the first example.

Now, in code:

We need to precompute a dictionary where for each sum in the prefix array, we have the list of indices where it occurs.

But for each a_i, in case1, we need to check if T +a_i exists in the prefix sum array, and that there's an index k >=i (since the element was originally in the left part) such that k is a split point (k is <=n-2? Wait, the split can be after k elements, leading to a prefix of k elements and a suffix of (n -k) elements. So in the modified array, the split points are from 1 to n-1 elements (since after moving, the array has n elements). So the split k can be 1, 2, ..., n-1 elements. Wait, original split in the original array is after k elements (0-based?), but after moving, the array is modified.

Hmm. Wait, in the code, when building the prefix array, for the original array, the split points are after 0-based index k, leading to k+1 elements in the prefix and (n - (k+1)) in the suffix. But when moving elements, the split points are based on the new array's indices.

But perhaps the approach is to check for all possible split points in the original array, but considering whether moving a_i can allow the sum at k in the modified array to be T.

But I think the earlier approach of checking for each a_i whether T +a_i exists in the prefix sum (case1) and T -a_i exists in the prefix sum (case2) is manageable.

So in code:

- Compute prefix array as the cumulative sum.

- Create a dictionary (like a defaultdict(list)) that maps each sum to a list of indices (0-based) where it occurs in the prefix array.

- For each a_i in the original array:

   Check case1: target = T + a_i

   Check if target is in the prefix sum.

   For each index k in the list of indices for target:

      if k >=i and k < n-1 (since split k is after k+1 elements in the original array? Wait, no. Split k in the original array is after index k (0-based), which gives a prefix of k+1 elements. For example, if the array is [a0, a1, a2], split after index 0 gives prefix [a0], suffix [a1, a2]. Split after index 1 gives prefix [a0, a1], etc. So the split points are 0-based indices from 0 to n-2.

   So in the code, the split k can be 0 to n-2 (since after k+1 elements, and the suffix must be non-empty). So for case1, the k must be in [i, n-2], because the element a_i is originally at position i (0-based). So moving it to the right part (split at k in original array) implies that in the original array, the split k is >=i.

Wait, but when you move a_i from the left part (i <=k) to the right part, the split after k in the original array (but after moving, the array is modified, so the split is in the new array). Hmm, perhaps the model is not directly applicable.

Alternatively, perhaps the approach is that in the original array, when a_i is in the left part (split k), moving it to the right part would reduce the sum of the left part by a_i, leading to T. So the original sum at k must be T +a_i.

But how does moving affect the split in the new array? Because after moving a_i, the split is in the new array's elements.

But maybe the model is correct. For example, in the original array, if the sum up to k is T +a_i, and a_i is in the left part (i <=k), then moving a_i to the right part would make the sum up to k (in the new array) equal to (T +a_i) -a_i = T, which is the desired value. So in this case, the split after k elements in the new array (after moving) would have sum T.

But how does moving a_i from the left to the right part affect the sum up to k?

In the original array, the sum up to k is prefix[k] = T +a_i. After moving a_i to the right part (somewhere after k), the sum up to k in the new array is prefix[k] -a_i (since a_i was removed from the left part and added to the right). So the sum becomes T, which is correct.

So the split after k elements in the new array would work.

Similarly, for case2: if the sum up to k in the original array is T -a_i, and a_i is in the right part (i >k), moving a_i to the left part (split after k) would add a_i to the sum, making it T.

So in the new array, the sum up to k would be (T -a_i) +a_i = T.

Thus, the split would work.

So the approach is correct.

Therefore, the code can proceed as follows:

For each a_i in the array (0-based index i):

   case1: compute target = T + a_i. Check if target exists in the prefix array, and there exists a k in the list of indices for target such that k >=i and k <=n-2 (since split after k elements in the new array must leave at least one element in the suffix). Wait, the split after k elements in the new array (of length n) must have 1 <=k <=n-1 elements in the prefix and the rest in the suffix. But in the original array, the split after k elements (0-based) is prefix[k], which is sum of elements 0 to k. So in the new array, the split is after k elements. Wait, maybe I'm getting confused here.

Wait, when moving a_i from position i to position j in the array, the new array is:

Original array: a0, a1, ..., ai-1, ai, ai+1, ..., aj-1, aj, ... an-1.

After moving ai to position j (if j >i):

The new array is a0, a1, ..., ai-1, ai+1, ..., aj-1, ai, aj, ..., an-1.

The split after k elements in this new array would sum the first k elements. So in the original approach, case1 is when the split is after k elements in the new array. But according to the model, this split's sum is T.

But according to the model, the sum after moving a_i from the left part (i <=k) to the right part (j >k) will make the new sum up to k equal to original_prefix[k] -a_i. So the split after k elements in the new array will have sum T.

But in this scenario, the k in the original array is the same as in the new array? Not exactly. Because after moving a_i, the indices of elements after i+1 are shifted. But according to the model, the split in the new array is after k elements, which is the same as the original array's k. So perhaps the model works regardless of the actual positions.

But how? For example, if a_i is in the left part (original array's split k), moving it to the right part (after the split) would reduce the sum of the first k elements by a_i. So in the new array, the sum up to k is T, which is correct.

Thus, the model is valid.

So in code, for case1, we need to check if there's a k in the prefix array (original) where the sum is T +a_i, and the index k is >=i (so a_i was in the left part) and k <=n-2 (since the split after k elements in the new array leaves n -k elements in the suffix, which must be >=1. So n -k >=1 => k <=n-1-1 => k <=n-2).

Wait, n-2 because the new array's split after k elements (0-based) requires that k+1 <=n-1. Because the suffix must have at least 1 element. So for example, if the new array has n elements, the split can be at k=0 (prefix has 1 element), up to k =n-2 (prefix has n-1 elements, suffix has 1). So split index in the new array is from 0 to n-2 (0-based), which is n-1 possible splits.

Thus, in case1, the k in the original array's prefix sum must be <=n-2, which is the maximum split index in the new array.

So for case1, for a_i, check if there exists a k in the prefix sum where:

prefix[k] == T +a_i,

k >=i,

k <=n-2.

Similarly, for case2: target = T -a_i.

Check if there exists a k in the prefix sum where:

prefix[k] == T -a_i,

k <i (since a_i is in the right part of split k in original array),

k <=n-2 (since split after k elements in new array must have suffix >=1).

Thus, the code can be structured as:

Compute the prefix array.

Build a map from sum to list of indices (k) where the sum occurs.

For each a_i in the array (0-based index i):

   check case1:

      target1 = T + a_i

      if target1 is in the sum map:

          for each k in sum_map[target1]:

              if k >=i and k <=n-2:

                  return YES

   check case2:

      target2 = T - a_i

      if target2 is in the sum map:

          for each k in sum_map[target2]:

              if k <i and k <=n-2:

                  return YES

But iterating through all k in sum_map for each a_i can be time-consuming. For example, if a particular sum occurs many times.

So to optimize, for each sum in the sum_map, we can store the list of indices sorted. Then, for a given a_i and target, we can perform a binary search to check if there's a valid k in the sorted list.

For example, for case1:

sum_map[target1] is a sorted list of indices. We need to find if there's any index in that list >=i and <=n-2.

Similarly for case2.

So steps:

1. Precompute the prefix array.

2. Create a defaultdict(list) called sum_indices, where each key is a sum, and the value is a sorted list of indices where this sum occurs.

3. For each a_i in the array (i from 0 to n-1):

   compute target1 = T + a_i

   if target1 in sum_indices:

       list_k = sum_indices[target1]

       using binary search, find if there's any element in list_k >=i and <=n-2.

   if yes, return YES.

   else, compute target2 = T -a_i

   if target2 in sum_indices:

       list_k = sum_indices[target2]

       using binary search, find if there's any element in list_k <i and <=n-2.

   if yes, return YES.

If after checking all a_i, none satisfy, return NO.

This approach would be O(n) for computing prefix sums, and O(n log n) for each a_i's binary search. But since n is 1e5, O(n log n) is acceptable.

But wait, for each a_i, we do two binary searches. So total time is O(n) (for prefix sums) + O(n log n) (for binary searches). For n=1e5, this is acceptable.

So the code can proceed as follows.

Now, let's code this.

First, handle edge cases. For n=1, since moving the element can't split the array into two non-empty parts (after moving, the array is still of length 1). So the answer is NO. So in code, if n ==1, output NO.

But the problem says the array is divided into two non-empty consecutive parts. So n must be at least 2. Wait, the input constraints say n can be 1. Wait, the problem statement says n is the size of the array, and Vasya wants to divide it into two non-empty consecutive parts. But if n is 1, this is impossible. So when n=1, the answer is automatically NO.

So in code:

if n <2, then output NO.

But according to the problem's constraints, n is given as 1 ≤ n ≤ 1e5.

So handle n=1: after moving, the array is still size 1, can't split into two parts. So output is NO.

So code steps:

Read n.

Read the array.

if n ==1: print NO.

Else:

compute S = sum(array)

if S is odd: print NO.

else:

   T = S//2

   compute prefix array.

   build sum_indices as a dictionary of lists, sorted.

   for each a_i in array:

      i is the current index (0-based)

      check case1:

         target1 = T +a_i

         if target1 in sum_indices:

             list_k = sum_indices[target1]

             using bisect_left, find the first index in list_k >=i.

             then, check if that element is <=n-2.

             if yes, return YES.

      check case2:

         target2 = T -a_i

         if target2 in sum_indices:

             list_k = sum_indices[target2]

             using bisect_right, find the insertion point of i, then check elements before that.

             for elements in list_k, check if any <=n-2 and <i.

             if yes, return YES.

   after all elements, return NO.

Now, for the binary search part.

For case1: we need to find any k in list_k where k >=i and <=n-2.

Since list_k is sorted, we can find the first index where k >=i. Then, check if that k is <=n-2.

If such a k exists, then yes.

For example, list_k is [3,4,5], i=3, n-2=5: 3 >=3 and <=5: yes.

So using bisect_left to find the first element >=i. The elements after that are all >=i. Then, check if the first such element is <=n-2.

Wait, but the list may have elements >=i but all larger than n-2. So we need to find if there exists any element in list_k that is >=i and <=n-2.

So the code for case1:

left = bisect.bisect_left(list_k, i)

for elements from left to end:

   if any element <=n-2, then yes.

But since list_k is sorted, after left, all elements are >=i.

So the first element in the list >=i is list_k[left], if left < len(list_k). Then, check if list_k[left] <=n-2.

If list_k[left] <=n-2, then yes. Else, if there's a larger element, it's also larger than n-2.

Wait no. For example, list_k could have elements [i, i+1, ... n-2, n-1, ...], but since split points can't be beyond n-2 (as split after k elements must leave suffix non-empty, which requires k <=n-2), so in this case, if list_k[left] <=n-2, then yes. Otherwise, no.

So for case1, if there exists an element in list_k >=i and <=n-2, then return yes.

So after finding the left insertion point, check if any element in list_k[left:] is <=n-2. But since list_k is sorted, if the first element (list_k[left]) is <=n-2, then there is such an element. Wait no. For example, list_k could be [5,6,7], i=5, n-2=4. Then, left is 0. list_k[left] is 5, which is >4. So no.

So in code, after finding left, we can check if the left index is within the list and list_k[left] <=n-2.

But if list_k is [5,6,7], and i=5, n-2=4, then the check would be list_k[left] (5) <=4? No. So no.

Thus, in code:

for case1:

if target1 exists in sum_indices:

   list_k = sum_indices[target1]

   left = bisect.bisect_left(list_k, i)

   if left < len(list_k) and list_k[left] <=n-2:

       return YES

Similarly for case2:

We need to find a k in list_k where k <i and <=n-2.

So list_k is sorted. So the elements in list_k are <=k's. So the maximum possible k is min(i-1, n-2). So we can find the rightmost k that is <= min(i-1, n-2).

Wait, the elements in list_k must be <i and <=n-2.

But n-2 could be >=i-1. For example, if i is 3, n is 5 (n-2=3), then min(i-1, n-2) is 2. But if i is 3 and n-2 is 3, then the element k must be <3 and <=3. So any k in list_k that is <=3 and <3.

So for case2:

We need to find any element in list_k that is <= (n-2) and <i.

Thus, the upper bound for k is min(n-2, i-1).

So list_k can have elements up to min(n-2, i-1).

But since list_k is sorted, we can find the largest element in list_k <= min(n-2, i-1).

Thus, for case2:

max_val = min(n-2, i-1)

if max_val <0: continue (since split can't be negative)

using bisect_right on list_k for max_val.

if there is any element <=max_val.

So code for case2:

if target2 exists in sum_indices:

   list_k = sum_indices[target2]

   max_val = min(n-2, i-1)

   if max_val <0:

       continue

   # find the largest element in list_k <= max_val

   pos = bisect.bisect_right(list_k, max_val) -1

   if pos >=0 and list_k[pos] <=max_val:

       return YES

Thus, for case2, we check if there's any element in list_k that is <= max_val (which is min(n-2, i-1)), which ensures that k <i and <=n-2.

But how to implement this.

In Python, the bisect module has bisect_left and bisect_right.

For case2, the steps are:

max_val = min(n-2, i-1)

if max_val <0: skip (since split can't be negative).

Else, find the rightmost element in list_k that is <=max_val.

bisect_right returns the insertion point for max_val in list_k.

So the index is bisect_right(list_k, max_val) -1.

If that index is >=0 and list_k[index] <=max_val, then yes.

For example:

list_k = [0, 1, 3], max_val=2.

bisect_right(list_k, 2) returns 2 (since inserting 2 after index 2 in the list [0,1,3] would be at position 2). So index is 2-1=1. list_k[1] is 1 <=2. So yes.

Another example: list_k = [4,5,6], max_val=3. Then bisect_right returns 0, index -1: invalid.

Thus, in code:

if target2 in sum_indices:

   list_k = sum_indices[target2]

   max_val = min(n-2, i-1)

   if max_val <0:

       continue

   pos = bisect.bisect_right(list_k, max_val) -1

   if pos >=0 and list_k[pos] <= max_val:

       return YES

This would work.

Now, code.

But wait, for case2, the split can be any k in list_k where k <=n-2 and k <i.

But the max_val is the minimum of n-2 and i-1. So if i is 0, then i-1 is -1, which makes max_val -1, but then we skip.

So code:

Now, let's code this.

Implementing with the bisect module.

But for each a_i, in case1 and case2, we perform the checks.

So:

import bisect

n = int(input())

if n <2:

    print("NO")

    exit()

a = list(map(int, input().split()))

total = sum(a)

if total %2 !=0:

    print("NO")

    exit()

T = total //2

prefix = []

current =0

sum_indices = dict()

for i in range(n):

    current += a[i]

    prefix.append(current)

    if current not in sum_indices:

        sum_indices[current] = []

    sum_indices[current].append(i)

for key in sum_indices:

    sum_indices[key].sort()

for i in range(n):

    ai = a[i]

    target1 = T + ai

    if target1 in sum_indices:

        list_k = sum_indices[target1]

        left = bisect.bisect_left(list_k, i)

        if left < len(list_k) and list_k[left] <= n-2:

            print("YES")

            exit()

    target2 = T - ai

    if target2 in sum_indices:

        list_k = sum_indices[target2]

        max_val = min(n-2, i-1)

        if max_val <0:

            continue

        pos = bisect.bisect_right(list_k, max_val) -1

        if pos >=0 and list_k[pos] <= max_val:

            print("YES")

            exit()

print("NO")

But wait, in the code, the sum_indices is built as follows:

for i in 0..n-1:

   add to prefix sum and add to sum_indices the current sum, with index i.

But the split in the original array after k elements (0-based) is allowed up to n-2. Because the original array is of size n. So, the split after k elements (0-based) must be <=n-2 (since the suffix must have at least one element). For example, split after index n-2 (0-based) gives prefix of n-1 elements, suffix of 1.

But in the code, when building the prefix sums, the sum_indices includes all indices from 0 to n-1. But when checking case1, we have to ensure that k <=n-2.

Thus, the code correctly checks if list_k[left] <=n-2.

But in the code, for case1, the list_k contains indices where the sum is target1, which could be up to n-1 (the entire array sum). But we need to ensure that k is <=n-2.

Thus, the code's check is correct.

Testing the first sample input:

Sample1:

3

1 3 2

sum is 6, T=3.

prefix sums are 1,4,6.

sum_indices:

1: [0]

4: [1]

6: [2]

For a_i=1 (i=0):

case1: target1 =3+1=4. sum_indices[4] is [1]. list_k = [1].

left = bisect_left([1], 0) → 0. check if 1 <=n-2=3-2=1. 1 <=1 → yes. So return YES.

Thus, code outputs YES.

Sample2:

5

1 2 3 4 5 → sum is 15, which is odd. So output is NO.

Sample3:

5

2 2 3 4 5 → sum is 16. T=8.

prefix sums: 2,4,7,11,16.

sum_indices:

2: [0]

4: [1]

7: [2]

11: [3]

16: [4]

For each a_i:

Take a_i=4 (index 3).

case1: T +4=12. sum_indices doesn't have 12.

case2: T-4=4. sum_indices[4] is [1]. check if any k in [1] <3 and <=3 (since n-2=5-2=3). k=1 is <=3 and <3 → yes. So code returns YES.

Thus, sample3 outputs YES.

So the code works.

Now, considering the data structures and efficiency.

Building the prefix sum and sum_indices is O(n), and for each a_i, the binary search operations are O(log n). Since there are O(n) elements, the total time is O(n log n), which is acceptable for n=1e5.

Memory usage is O(n) for the sum_indices.

Thus, this is the optimal approach.
</think>

```python
import bisect

n = int(input())
if n < 2:
    print("NO")
    exit()
a = list(map(int, input().split()))
total = sum(a)
if total % 2 != 0:
    print("NO")
    exit()
T = total // 2

prefix = []
current = 0
sum_indices = {}
for i in range(n):
    current += a[i]
    prefix.append(current)
    if current not in sum_indices:
        sum_indices[current] = []
    sum_indices[current].append(i)

for key in sum_indices:
    sum_indices[key].sort()

for i in range(n):
    ai = a[i]
    # Case 1: a_i is in the left part (k >= i)
    target1 = T + ai
    if target1 in sum_indices:
        list_k = sum_indices[target1]
        left = bisect.bisect_left(list_k, i)
        if left < len(list_k) and list_k[left] <= n - 2:
            print("YES")
            exit()
    # Case 2: a_i is in the right part (k < i)
    target2 = T - ai
    if target2 in sum_indices:
        list_k = sum_indices[target2]
        max_val = min(n - 2, i - 1)
        if max_val < 0:
            continue
        pos = bisect.bisect_right(list_k, max_val) - 1
        if pos >= 0 and list_k[pos] <= max_val:
            print("YES")
            exit()

print("NO")
```