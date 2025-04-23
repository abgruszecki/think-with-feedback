<think>
Okay, let's tackle this problem. So the problem is about finding the maximum subarray sum in a big array formed by concatenating some small arrays based on a given sequence of indexes. The challenge is to handle very large input sizes efficiently without constructing the big array directly.

First, let's understand the problem. The big array is built by taking the sequence of small arrays as per the indexes provided. For example, if the indexes are [2,3,1,3], then we take the 2nd small array, then the 3rd, then the 1st, then the 3rd again, and concatenate them all. Then, we need to find the maximum sum of any consecutive elements in this big array.

The constraints are tight. The number of small arrays is up to 50, and the number of indexes (m) can be up to 250,000. Each small array can be up to 5000 elements. So if we naively concatenate all the small arrays as per the indexes, the big array's size could be 250,000 * 5000 = 1.25e9 elements, which is way too big to handle in memory. So we need a smarter approach.

The standard maximum subarray problem is solved using Kadane's algorithm, which runs in O(n) time and O(1) space. But here, we can't process the entire array directly because it's too large. Therefore, we need a way to model the concatenated array's properties without explicitly building it.

So the key idea is to precompute some information for each small array that allows us to compute the maximum subarray when they are concatenated multiple times.

Let's think about what happens when we have a sequence of small arrays. For example, if the sequence is A followed by B, the maximum subarray could be entirely in A, entirely in B, or span across A and B. To compute the maximum, we need to track:

1. The maximum prefix sum of the combined array (the maximum sum starting from the first element and extending to some point).
2. The maximum suffix sum of the combined array (the maximum sum ending at the last element and starting from some point).
3. The total sum of all elements in the combined array.
4. The maximum subarray sum within the combined array.

These four values can be computed for a sequence of small arrays by combining the precomputed information of individual arrays. For each small array, we can precompute these four values. Then, when combining two sequences (like A and B), we can compute the new four values based on the existing ones.

So, the plan is:

1. Preprocess each small array to compute its max_prefix, max_suffix, total_sum, and max_subarray (the standard Kadane's maximum for the array alone).
2. Then, as we process the sequence of indexes in the big array, we need to maintain the combined information (current max_prefix, max_suffix, total_sum, max_subarray) by merging with the next small array's precomputed data.
3. The maximum subarray sum at each step is the maximum of:
   a. The previous max_subarray
   b. The next array's max_subarray
   c. The previous suffix + the next prefix (if combining across the two)
4. Additionally, we need to track the new prefix (max between previous prefix and previous total + next prefix) and new suffix (max between next suffix and next total + previous suffix). The total sum is previous total + next total.
5. The overall maximum is the maximum of all these possibilities as we process each element in the sequence.

Wait, but how do we handle multiple occurrences of the same small array in the sequence? For example, if the sequence is [A, A], then combining the first A with the second A. But since each small array can be up to 5000 elements, processing each occurrence individually (like m times) could be manageable if m is 250,000 and each step is O(1). So the overall time would be O(m), which is acceptable.

So, the algorithm steps:

1. Preprocess each small array (1 to n) to compute:
   - max_prefix: maximum sum starting from the first element.
   - max_suffix: maximum sum ending at the last element.
   - total: sum of all elements.
   - best: the maximum subarray sum within the array.

2. Initialize a structure (like current) that holds the current combined max_prefix, max_suffix, total_sum, best. Initially, this structure is empty.

3. For each index in the big array's sequence:
   a. Get the precomputed data (prefix, suffix, total, best) for the current small array (index i).
   b. Combine this data with the current structure to compute the new combined data.
   c. Update the current structure to be the new combined data.
   d. Update the global maximum with the current best.

But how do we combine two structures (current and next array)?

Let's denote the current structure as left and the next array's structure as right.

The combined structure would be:

- combined_prefix = max(left.prefix, left.total + right.prefix)
   Because the maximum prefix could be either the prefix of the left part (if it's larger than adding the entire left and the prefix of the right), or the sum of the entire left plus the prefix of the right.

- combined_suffix = max(right.suffix, right.total + left.suffix)
   Similarly, the suffix is the max of the right's suffix or the right's total plus the left's suffix.

- combined_total = left.total + right.total

- combined_best = max(left.best, right.best, left.suffix + right.prefix)
   The best is the maximum of the individual bests or the sum of the left's suffix and right's prefix (the case where the maximum spans across the two).

So for each step, when we process a new small array, we need to combine the current accumulated structure with the new array's structure to form a new structure. The initial structure is empty, but when we add the first array, the combined structure is just the structure of that array.

Wait, but the initial structure can't be empty. The first array's structure is just its own data. Then, each subsequent array is merged with the current structure.

So, for example:

current starts as the data for the first array.

Then, for the second array:

new_prefix = max(current.prefix, current.total + second.prefix)
new_suffix = max(second.suffix, second.total + current.suffix)
new_total = current.total + second.total
new_best = max(current.best, second.best, current.suffix + second.prefix)

These four values become the new current structure.

Then, for the third array, we repeat the same process, combining the current structure with the third array's data.

This approach allows us to process each index in O(1) time, leading to O(m) time complexity, which is acceptable for m up to 250,000.

So the key is precomputing for each small array the four values (prefix, suffix, total, best), and then combining them in the order of the given indexes.

Now, let's think about how to precompute these four values for a single small array.

For a single array:

- The total is the sum of all elements.

- The max_prefix can be computed by keeping a running sum and tracking the maximum sum. For example, start with sum=0, for each element from left to right, add to sum, keep track of the maximum sum encountered.

- Similarly, the max_suffix can be computed by iterating from right to left, summing elements and tracking the maximum sum.

- The best is the maximum subarray sum, which can be found using Kadane's algorithm.

But wait, for the max_prefix and max_suffix, we need to have the maximum sum starting at the first element and going up to some point (prefix) and ending at the last element (suffix).

For example, in the array [3, 3], the prefix sum starts as 3 (sum of first element), then 3+3=6. So max_prefix is 6.

For the suffix sum, it's the same as the prefix here, since the array is all positive. So suffix is 6.

The best is 6.

Another example: [1, 6, -2]. The total is 5. The prefix sum is 1, 7 (1+6), 5 (1+6-2). So max_prefix is 7. The suffix is (-2) → 4 (6-2) → 5 (1+6-2). So max_suffix is 5. The best is 1+6=7.

So the code for preprocessing each small array would be:

For each small array:

Compute total: sum of all elements.

Compute prefix:

current_sum = 0

max_p = -infinity

for num in array:

    current_sum += num

    max_p = max(max_p, current_sum)

max_prefix = max_p

Similarly for suffix:

current_sum = 0

max_s = -infinity

for num in reversed(array):

    current_sum += num

    max_s = max(max_s, current_sum)

max_suffix = max_s

The best is computed via Kadane's algorithm.

So for Kadane's algorithm:

current_max = 0

max_sub = -infinity

for num in array:

    current_max = max(num, current_max + num)

    max_sub = max(max_sub, current_max)

So the best is max_sub.

Once we have these four values for each small array, the combination process can be done as described.

Now, the initial current structure is empty. But when processing the first small array in the sequence, the current becomes the data of that array.

Then, for each subsequent array in the sequence, we combine the current structure with the next array's data.

So, the steps:

Initialize current as None.

For each index in the big array sequence:

    get the small array's data (precomputed: prefix, suffix, total, best)

    if current is None:

        current = (prefix, suffix, total, best)

    else:

        new_prefix = max(current[0], current[2] + prefix)

        new_suffix = max(suffix, current[1] + total)

        new_total = current[2] + total

        new_best = max(current[3], best, current[1] + prefix)

        # Wait, wait, wait. Wait, the new_best is the maximum of:

        # - the best of the current (left part's best)

        # - the best of the next array (right part's best)

        # - the left's suffix + right's prefix (the overlapping part)

        # So new_best = max(left.best, right.best, left.suffix + right.prefix)

        # Then, the new_best is compared with the previous current.best and others.

        # But the overall new_best is the max of all possibilities.

        # Wait, the current.best is the best of the left part, and the new array's best is the right part. But when combining, the best could be any of these, or the combination of suffix and prefix.

        # So yes, new_best is the max of current.best, new array's best, and current.suffix + new array's prefix.

        # So the code for new_best is as above.

        # Then, the combined best is the maximum of the left's best, right's best, and left.suffix + right.prefix.

        # But also, the new combined structure's best is the maximum of all possible combinations, which includes the previous new_best, but also any other possibilities that might arise from combining the entire structures.

        # Wait, maybe I need to think again. When combining two structures, the combined best can be the maximum of:

        # left.best,

        # right.best,

        # left.suffix + right.prefix,

        # or any other possibilities from the combination's internal best.

        # But when combining left and right into a new structure, the new best is the maximum of these three possibilities.

        # Because the left's best is the maximum subarray that is entirely within the left, the right's best is entirely within the right, and the left's suffix plus right's prefix is the maximum that spans across.

        # Therefore, the new best is the maximum of left.best, right.best, left.suffix + right.prefix.

        # So, the combined best is the maximum between these three.

        # Then, when we compute the new_best, which is part of the new structure's best, we have to take the maximum of these three.

        # But also, the new structure's best must account for all possible subarrays in the combined array, which could be in the left part, the right part, or crossing both.

        # So, the combination logic for the best is correct.

        # So the code for new_best is as follows:

        combined_best = max(current[3], best, current[1] + prefix)

        # Wait, but the new combined structure's best is the maximum of:

        # the left's best (current[3]),

        # the right's best (best),

        # the left's suffix + right's prefix,

        # and also any other possibilities that might have been introduced by the combination's own prefix, suffix, etc.

        # No, because when combining the two parts, the new structure's best is the maximum between the individual bests and the cross sum. The structure's best is supposed to track the maximum subarray sum within the combined array. So, the maximum can be in the left part (current.best), in the right part (right.best), or spanning across the two (left's suffix + right's prefix). So combining the bests as max(left.best, right.best, left.suffix + right.prefix) is correct.

        # So the new_best is computed as the maximum of those three values.

        # Then, the current structure's best is updated to this new_best.

        # So the code for combining left and right:

        new_prefix = max(current[0], current[2] + prefix)

        new_suffix = max(suffix, current[1] + total)

        new_total = current[2] + total

        new_best = max(current[3], best, current[1] + prefix)

        # Then, the current structure is updated to (new_prefix, new_suffix, new_total, new_best).

        # Wait, but the new_best may not capture all possibilities. For example, the combined array's best could be a subarray that starts in the left part and extends into the right part but not necessarily the left's suffix plus the right's prefix. Hmm, but I think that the way we are combining the structures allows for this.

        # Let's see. The left structure's best is the maximum subarray sum in the left part. The right structure's best is the maximum in the right. The cross sum (left suffix + right prefix) is the maximum subarray that starts in the left and ends in the right. So the combined best is the maximum of these three possibilities. That covers all possible subarrays in the combined array: either entirely in left, entirely in right, or spanning both. So yes, this approach works.

        So the code for combining is correct.

        So, current becomes (new_prefix, new_suffix, new_total, new_best)

    Then, after each step, the global maximum is the maximum between the current best and the previous maximum.

Wait, no. The current structure's best is the maximum possible subarray in the combined array up to that step. So after each step, the global maximum should track the maximum between all the current.best values encountered so far.

Wait, no. Because the current.best for the combined array is the maximum possible subarray in that entire array. So as we process each index in the sequence, the current.best is the maximum subarray for the concatenation up to that index. So the global maximum is the maximum of all current.best values as we process each step.

But in the first example, after processing the first array (index 2), the current.best is the best of array 2, which is 6 (3+3). Then processing index 3 (array 3: [-5,1]). Combining array 2 and array 3.

The combined best would be max(6 (array2's best), array3's best (1), array2's suffix (6) + array3's prefix (-5+1= -4? Wait, the array3's prefix is the maximum sum starting from the first element. Array3 is [-5,1]. The prefix sum starts at -5, then -5+1=-4. So the max_prefix is -4? Wait, no. Let's recalculate.

For array3: elements are -5 and 1.

The sum for prefix is:

current_sum starts at 0.

First element: -5. current_sum += -5 → -5. max_p is -5.

Second element: 1. current_sum += 1 → -4. max_p is max(-5, -4) → -4. So the max_prefix is -4.

Similarly, the suffix sum: starts from right (1). current_sum is 1. Then add -5? No, wait, when reversed, the array is [1, -5]. So first element is 1, add to current_sum (1), then next element -5: current_sum becomes 1 + (-5) = -4. The max suffix is 1 (since max between 1 and -4 is 1). So the max_suffix is 1.

The total sum is -5 +1 = -4.

The best for array3: Kadane's algorithm. Let's see:

current_max = max(-5, -5) → -5. max_sub is -5.

Then next element 1: current_max = max(1, -5 +1= -4) → 1. max_sub is 1. So best is 1.

So when combining array2 (which has suffix 6) and array3 (prefix -4), the cross sum is 6 + (-4) = 2. The new_best is max(6, 1, 6 + (-4)) → max(6,1,2) →6. So the combined best is 6.

Then the current best remains 6. Then processing the next index (1) and so on. But in the example, the final maximum is 9. So the process must accumulate a better best as we go.

Hmm. So perhaps the way the combination works is correct, but we need to track the maximum possible as we process each element in the sequence.

So in code, the steps would be:

Read all the small arrays and precompute their four values.

Read the sequence of m indexes (each 1-based).

For each index in the sequence:

   get the precomputed data for that small array.

   combine it with the current structure (if any).

   update the current structure.

   update the global maximum (current_best).

The global maximum is the answer.

So the code structure is as follows:

Read n and m.

Then read n small arrays.

For each small array, compute prefix, suffix, total, best.

Then read the m indexes (but note that indexes are 1-based).

Then process each index in order, maintaining the current structure (prefix, suffix, total, best), and track the maximum best encountered.

Now, considering that m can be up to 250,000, and each step is O(1), this is manageable.

Now, let's code this.

But first, handle the small arrays.

For each small array:

Compute prefix: iterate left to right, sum elements, track max sum.

Compute suffix: iterate right to left, sum elements, track max sum.

Compute total: sum of elements.

Compute best using Kadane's algorithm.

Once these are precomputed, process the sequence.

Initialize current as None.

max_sum = -infinity

for each index in the sequence:

    idx = index -1 (since they are 1-based)

    curr_array = precomputed_data[idx]

    if current is None:

        current = (curr_array['prefix'], curr_array['suffix'], curr_array['total'], curr_array['best'])

        max_sum = max(max_sum, current[3])

    else:

        # Combine current with curr_array

        left_prefix, left_suffix, left_total, left_best = current

        right_prefix = curr_array['prefix']

        right_suffix = curr_array['suffix']

        right_total = curr_array['total']

        right_best = curr_array['best']

        new_prefix = max(left_prefix, left_total + right_prefix)

        new_suffix = max(right_suffix, left_suffix + right_total)

        new_total = left_total + right_total

        new_best = max(left_best, right_best, left_suffix + right_prefix)

        current = (new_prefix, new_suffix, new_total, new_best)

        max_sum = max(max_sum, new_best)

After processing all indexes, output max_sum.

Wait, but in the first example:

The indexes are 2,3,1,3.

Let's process step by step.

First index is 2 (array 2: [3,3]).

precomputed data for array2:

prefix: 6 (3+3)

suffix:6

total:6

best:6.

current is now (6,6,6,6). max_sum is 6.

Next index is 3 (array3: [-5,1]).

precomputed data:

prefix: -4 (sum is -5 +1= -4), which is the maximum of [-5, -4].

suffix: 1 (summing from right, 1 and then 1-5=-4. Max is 1).

total: -4.

best:1 (Kadane's gives 1 as maximum).

Combining current (6,6,6,6) with array3's data (-4,1,-4,1):

new_prefix = max(6, 6 + (-4)=2) →6.

new_suffix = max(1, 6 + (-4)=2) →2.

new_total =6 + (-4)=2.

new_best = max(6,1,6 + (-4) )= max(6,1,2) →6.

current is now (6,2,2,6). max_sum remains 6.

Next index is 1 (array1: [1,6,-2]).

array1's precomputed data:

sum elements:1+6-2=5.

prefix:1, 7 (1+6), 5 (1+6-2). Max is 7.

suffix: sum from right: -2 →5 (6-2) →5 (1+6-2). So max is 5.

best:7 (from 1+6).

Combining current (6,2,2,6) with array1's data (7,5,5,7):

new_prefix = max(6, 2 +7=9) →9.

new_suffix = max(5, 2 +5=7) →7.

new_total =2+5=7.

new_best = max(6,7, 2+7=9) →9.

current becomes (9,7,7,9). max_sum is now 9.

Next index is 3 (array3 again).

array3's data is same as before.

Combine current (9,7,7,9) with array3's data (-4,1,-4,1):

new_prefix = max(9, 7 + (-4) =3) →9.

new_suffix = max(1,7 + (-4) +1? Wait, wait.

Wait, right_suffix is 1, right_total is -4.

new_suffix = max(right_suffix, left_suffix + right_total) → max(1, 7 + (-4)) → max(1,3) →3.

new_total =7 + (-4) =3.

new_best = max(9,1,7 + (-4)) →9.

current becomes (9,3,3,9). max_sum remains 9.

So the final max is 9, which matches the example.

This approach works.

Another example in the input:

Input:

6 1

4 0 8 -3 -10

8 3 -2 -5 10 8 -9 -5 -4

1 0

1 -3

3 -8 5 6

2 9 6

1

The sequence is [1]. So the big array is the first small array. Let's see:

First small array is index 1 (since the input's indexes are 1-based). Wait, the indexes in the big array are given as the last line. In this case, the last line is 1. So the big array is the first small array.

What's the first small array?

The first small array's data is:

elements:0,8,-3,-10.

Compute prefix:

sums:

0 →0.

0+8=8 →max is 8.

8-3=5 →8 remains.

5-10=-5 →8.

max_prefix is 8.

suffix: start from the end:

-10 →-10.

-10-3 =-13 →-10 is max.

-13 +8= -5 →-5 is max.

-5 +0 =-5 →-5 is max.

Wait, the array is 0,8,-3,-10. Reversed array is -10, -3,8,0.

summing from right:

current_sum =0.

add -10 →-10. max_s is -10.

add -3 →-13. max_s remains -10.

add 8 →-5. max_s is -5.

add 0 →-5. max_s is -5.

So the max_suffix is -5.

Wait, maybe I'm miscalculating. Let's recompute.

Wait, for the array [0,8,-3,-10], the suffix is the maximum sum ending at the last element. So to compute the suffix sum:

Start from the end and sum towards the left.

The elements are [0,8,-3,-10].

The suffix can be:

-10 → sum is -10.

-3 + (-10) = -13 → sum is -13. So the maximum is -10.

Then 8 + (-3) + (-10) = -5 → sum is -5. So the maximum here is -5.

Then 0 +8 + (-3) + (-10) =-5 → sum is -5.

So the max_suffix is -5.

But wait, when computing the suffix sum, perhaps I should iterate from right to left, and for each position, calculate the sum from that position to the end, and track the maximum.

Alternatively, the correct way to compute the max_suffix is:

current_sum =0

max_s = -infinity

for num in reversed(array):

    current_sum += num

    if current_sum > max_s:

        max_s = current_sum

So for [0,8,-3,-10]:

reversed is [-10, -3, 8, 0]

current_sum starts at 0.

Add -10: current_sum is -10. max_s is -10.

Add -3: current_sum is -13. max_s remains -10.

Add 8: current_sum is -5. max_s is -5.

Add 0: current_sum is -5. max_s remains -5.

So max_suffix is -5.

The total sum is 0+8-3-10 = -5.

The best (Kadane's):

current_max starts at 0.

for 0:

current_max = max(0, 0) →0. max_sub is 0.

for 8:

current_max = max(8, 0+8=8) →8. max_sub is 8.

for -3:

current_max = max(-3, 8-3=5) →5. max_sub is 8.

for -10:

current_max = max(-10,5-10=-5) →-5. max_sub remains 8.

So the best is 8.

So the precomputed data for the first array is:

prefix=8, suffix=-5, total=-5, best=8.

So when the big array is just the first array, the max is 8, which matches the example's output.

So the code works.

So the code steps are correct.

Now, implementing this in Python.

But in Python, for handling large inputs, reading the input efficiently is crucial.

The problem states that m can be up to 250,000, and each small array can be up to 5000 elements. So for reading the input, we need to read the data efficiently.

But in Python, the standard input can be read using input().split(), but for very large inputs, this can be slow. However, in the problem statement, the input is given with m up to 250,000, which is manageable.

But for the small arrays, each can have up to 5000 elements, and there are up to 50 of them. So the total number of elements across all small arrays is up to 50*5000=250,000 elements, which is manageable.

So the plan is:

Read n and m.

Then read n lines. For each line, split into l integers. The first integer is l, followed by l integers.

For each small array, compute the four values (prefix, suffix, total, best).

Then read the m indexes (the last line), which is a list of m integers (1-based).

Process these indexes in order, maintaining the current structure (prefix, suffix, total, best), and track the maximum sum.

Now, implementing this.

Potential edge cases to consider:

- All elements are negative. Then the answer is the maximum element.

But according to the problem statement, you must select at least one element, so the code must handle that.

But in the preprocessing step, Kadane's algorithm will correctly find the maximum single element if all are negative.

Another edge case: the big array is formed by multiple copies of a small array that has a negative total sum but a positive prefix and suffix. For example, a small array with elements [5, -10, 5]. Its total is 0. Its prefix is 5 (max after first element), 5-10=-5, then 0. So max prefix is 5. Suffix is 5 (last element), then 5-10+5=0. Max suffix is5. Best is 5 (either first element or last element). Now, if you concatenate two copies, the big array is [5,-10,5,5,-10,5]. The best could be 5+5=10, which would be the sum of the last 5 of the first array and the first 5 of the second. So the code would combine the two arrays, their cross sum is 5 (suffix of first array) +5 (prefix of second) →10. So the code would find that.

So the code handles that.

Now, code implementation.

Implementing the code steps:

Read n and m.

precompute for each small array:

def compute_array(arr):

    # compute prefix

    current_sum = 0

    max_prefix = -float('inf')

    for num in arr:

        current_sum += num

        if current_sum > max_prefix:

            max_prefix = current_sum

    # compute suffix

    current_sum =0

    max_suffix = -float('inf')

    for num in reversed(arr):

        current_sum += num

        if current_sum > max_suffix:

            max_suffix = current_sum

    # total

    total = sum(arr)

    # best (kadane's)

    current_max = 0

    max_sub = -float('inf')

    for num in arr:

        current_max = max(num, current_max + num)

        if current_max > max_sub:

            max_sub = current_max

    return (max_prefix, max_suffix, total, max_sub)

But wait, for empty arrays? But according to the constraints, each small array has l >=1.

So this is okay.

Once these are computed, process the indexes.

Then read the list of m indexes (1-based), so for each index in the list, subtract 1 to get 0-based.

Now, process the indexes:

current = None

max_sum = -float('inf')

for idx in indexes:

    small = precomputed[idx]

    if current is None:

        current = small

        current_best = small[3]

    else:

        # combine current and small

        left_p, left_s, left_t, left_b = current

        right_p, right_s, right_t, right_b = small

        new_p = max(left_p, left_t + right_p)

        new_s = max(right_s, left_s + right_t)

        new_t = left_t + right_t

        new_b = max(left_b, right_b, left_s + right_p)

        current = (new_p, new_s, new_t, new_b)

        current_best = new_b

    if current[3] > max_sum:

        max_sum = current[3]

print(max_sum)

Wait, but in the code, after combining, the current's best is new_b, and we compare it to the max_sum. So after each step, whether it's the first or not, we update the max_sum.

Yes.

But what if the current's best is not the new_b? For example, if combining two arrays results in a new_b that is less than the previous max_sum. Then the max_sum remains the previous value. But since each step adds a new array, and the new_b is the best of the current combined array, the max_sum must be the maximum of all new_b's encountered.

Yes.

So the code is correct.

Now, handling the input.

In Python, for reading large inputs, using sys.stdin.readline is more efficient. So we can read the input as follows.

But in the problem statement, the input can be read via input().

But for the last line (the m indexes), when m is 250,000, using input().split() may be slow. So in Python, it's better to read from sys.stdin.

But for code submission, the code must read from standard input. So the code can be written as:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().split())

    arrays = []

    for _ in range(n):

        parts = list(map(int, input_stream.readline().split()))

        l = parts[0]

        arr = parts[1:]

        arrays.append(arr)

    indexes = list(map(int, input_stream.readline().split()))

    precomputed = []

    for arr in arrays:

        # compute prefix

        current_sum = 0

        max_prefix = -float('inf')

        for num in arr:

            current_sum += num

            max_prefix = max(max_prefix, current_sum)

        # compute suffix

        current_sum =0

        max_suffix = -float('inf')

        for num in reversed(arr):

            current_sum += num

            max_suffix = max(max_suffix, current_sum)

        # compute total

        total = sum(arr)

        # compute best using kadane's algorithm

        current_max = 0

        max_sub = -float('inf')

        for num in arr:

            current_max = max(num, current_max + num)

            max_sub = max(max_sub, current_max)

        precomputed.append( (max_prefix, max_suffix, total, max_sub) )

    current = None

    max_sum = -float('inf')

    for i in indexes:

        idx = i-1  # convert to 0-based

        small = precomputed[idx]

        if current is None:

            current = small

        else:

            left_p, left_s, left_t, left_b = current

            right_p, right_s, right_t, right_b = small

            new_p = max(left_p, left_t + right_p)

            new_s = max(right_s, left_s + right_t)

            new_t = left_t + right_t

            new_b = max(left_b, right_b, left_s + right_p)

            current = (new_p, new_s, new_t, new_b)

        if current[3] > max_sum:

            max_sum = current[3]

    print(max_sum, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 1
4 0 8 -3 -10
8 3 -2 -5 10 8 -9 -5 -4
1 0
1 -3
3 -8 5 6
2 9 6
1
""",
            "output": \
"""\
8
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

Another test case where the best is achieved by a cross between two copies of the same array.

Example:

A small array is [5,-10,5]. Precomputed:

prefix:5 (sum 5), then 5-10=-5, then 0. Max prefix is5.

suffix:5 (last element), then -10+5=-5, then 5-10+5=0. Max suffix is5.

total:0.

best:5 (first element or last element).

If we concatenate two copies of this array.

The combined array is [5,-10,5,5,-10,5].

The best subarray is 5 +5=10 (the last element of the first array and the first element of the second).

The code should compute this.

Processing the indexes [1,1].

First index: small array data is (5,5,0,5). max_sum is5.

Second index: combine (5,5,0,5) with (5,5,0,5):

new_p = max(5, 0 +5=5 →5.

new_s= max(5,5 +0=5 →5.

new_t=0+0=0.

new_b= max(5,5,5+5=10 →10.

current becomes (5,5,0,10). max_sum is10.

So the code outputs 10, which is correct.

Thus, the code works.
</think>

```python
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    arrays = []
    for _ in range(n):
        parts = list(map(int, sys.stdin.readline().split()))
        arr = parts[1:]
        arrays.append(arr)
    
    precomputed = []
    for arr in arrays:
        max_prefix = -float('inf')
        current_sum = 0
        for num in arr:
            current_sum += num
            max_prefix = max(max_prefix, current_sum)
        
        max_suffix = -float('inf')
        current_sum = 0
        for num in reversed(arr):
            current_sum += num
            max_suffix = max(max_suffix, current_sum)
        
        total = sum(arr)
        max_sub = -float('inf')
        current_max = 0
        for num in arr:
            current_max = max(num, current_max + num)
            max_sub = max(max_sub, current_max)
        
        precomputed.append((max_prefix, max_suffix, total, max_sub))
    
    indexes = list(map(int, sys.stdin.readline().split()))
    current = None
    max_sum = -float('inf')
    
    for idx in indexes:
        small = precomputed[idx-1]
        if current is None:
            current = small
        else:
            lp, ls, lt, lb = current
            rp, rs, rt, rb = small
            new_p = max(lp, lt + rp)
            new_s = max(rs, ls + rt)
            new_t = lt + rt
            new_b = max(lb, rb, ls + rp)
            current = (new_p, new_s, new_t, new_b)
        
        if current[3] > max_sum:
            max_sum = current[3]
    
    print(max_sum)

if __name__ == "__main__":
    main()
```
